#!/usr/bin/env python3
"""package-skill: keep Agent Skills portable and self-contained.

One script, vendored into every skill repo (canonical copy: lukewp/skills/tools/).
Standard library only, so it runs on macOS, Linux and CI without installs.

  python3 scripts/package-skill.py check   # validate, drift-check, path-lint (CI)
  python3 scripts/package-skill.py sync    # copy canonical files into skill folders
  python3 scripts/package-skill.py build   # check, then write dist/<name>.zip per skill

What it enforces
  1. Agent Skills spec frontmatter (agentskills.io/specification): name rules,
     name == directory, description 1-1024 chars, compatibility <= 500 chars,
     metadata is a string->string map, no unknown top-level fields.
  2. Self-containment: every file a skill mentions (references/, scripts/,
     assets/, agents/) exists inside the skill folder. Mentions of files that
     only exist at the repo root are errors, because only the skill folder is
     ever installed.
  3. Canonical copies: files listed in skill-sync.json are copied from their
     canonical location into the skill folder; `check` fails if a copy drifts.
  4. Portability warnings: harness-specific wording without a fallback.
  5. Packaging: dist/<name>.zip with <name>/ as the top level, the shape both
     claude.ai upload and the OpenAI Skills API expect.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path.cwd()
SKILLS_DIR = ROOT / "skills"
SYNC_FILE = ROOT / "skill-sync.json"
DIST = ROOT / "dist"

ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PATH_RE = re.compile(r"(?<![\w/.-])((?:references|scripts|assets|agents)/[\w./-]+\.\w+)")
BARE_RE = re.compile(r"`([\w-]+(?:\.[\w-]+)*\.(?:md|json|yaml|yml|txt|py|js|sh))`")
# Files a skill legitimately names that it creates at run time or that live in the
# user's workspace. Each repo can extend this in skill-sync.json "runtime_names".
RUNTIME_NAMES = {"SKILL.md"}
EXCLUDE = {".DS_Store"}
MAX_FILES = 500                 # OpenAI Skills API limit per version
MAX_ZIP_BYTES = 50 * 1024 ** 2  # OpenAI Skills API zip limit
PORTABILITY_HINTS = [
    (re.compile(r"\$\{CLAUDE_SKILL_DIR\}"), "uses ${CLAUDE_SKILL_DIR}; also give the path relative to SKILL.md"),
    (re.compile(r"\bAgent tool\b"), "names Claude's Agent tool; describe sub-agents generically with a no-sub-agent fallback"),
    (re.compile(r"\bTask tool\b"), "names a harness-specific tool; describe it generically"),
]

errors, warnings = [], []


def err(msg):
    if msg not in errors:
        errors.append(msg)


def warn(msg):
    if msg not in warnings:
        warnings.append(msg)


def parse_frontmatter(text, where):
    """Minimal YAML subset: top-level `key: value`, folded `>`/`|` blocks, and one nested map."""
    if not text.startswith("---\n"):
        err(f"{where}: SKILL.md must start with '---' frontmatter")
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        err(f"{where}: frontmatter not closed")
        return {}, text
    block, body = text[4:end], text[end + 4:]
    data, key, mode, buf = {}, None, None, []

    def flush():
        nonlocal key, mode, buf
        if key and mode in (">", "|"):
            data[key] = (" " if mode == ">" else "\n").join(s.strip() for s in buf).strip()
        key, mode, buf = None, None, []

    for raw in block.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indented = raw.startswith((" ", "\t"))
        if indented and mode in (">", "|"):
            buf.append(raw)
            continue
        if indented and mode == "map":
            k, _, v = raw.strip().partition(":")
            data[key][k.strip()] = v.strip().strip('"').strip("'")
            continue
        flush()
        k, sep, v = raw.partition(":")
        if not sep:
            err(f"{where}: unparseable frontmatter line: {raw!r}")
            continue
        k, v = k.strip(), v.strip()
        if v in (">", "|", ">-", "|-"):
            key, mode = k, v[0]
        elif v == "":
            key, mode = k, "map"
            data[k] = {}
        else:
            data[k] = v.strip('"').strip("'")
    flush()
    return data, body


def validate_skill(skill_dir):
    where = f"skills/{skill_dir.name}"
    md = skill_dir / "SKILL.md"
    text = md.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text, where)

    for k in fm:
        if k not in ALLOWED_FIELDS:
            err(f"{where}: frontmatter field '{k}' is not in the Agent Skills spec")
    name = fm.get("name", "")
    if not name:
        err(f"{where}: missing name")
    elif len(name) > 64 or not NAME_RE.match(name):
        err(f"{where}: name '{name}' must be 1-64 chars, lowercase a-z 0-9 and single hyphens")
    elif name != skill_dir.name:
        err(f"{where}: name '{name}' must match directory '{skill_dir.name}'")
    desc = fm.get("description", "")
    if not (1 <= len(desc) <= 1024):
        err(f"{where}: description must be 1-1024 chars (is {len(desc)})")
    if "compatibility" in fm and not (1 <= len(fm["compatibility"]) <= 500):
        err(f"{where}: compatibility must be 1-500 chars")
    if "metadata" in fm and not isinstance(fm["metadata"], dict):
        err(f"{where}: metadata must be a map of string to string")
    if text.count("\n") > 500:
        warn(f"{where}: SKILL.md is over 500 lines; move detail into references/")

    # Self-containment: every mentioned file must exist inside the skill folder.
    texts = [(md, body)] + [(p, p.read_text(encoding="utf-8", errors="ignore"))
                            for p in sorted(skill_dir.rglob("*.md")) if p != md]
    for path, content in texts:
        rel = path.relative_to(skill_dir)
        for m in PATH_RE.finditer(content):
            target = m.group(1).rstrip(".,;:)")
            if "<" in target or "*" in target:
                continue
            if not (skill_dir / target).exists():
                err(f"{where}/{rel}: mentions '{target}', which is not inside the skill folder")
        # Bare file names in backticks (`METHOD.md`) must also resolve inside the skill.
        present = {p.name for p in skill_dir.rglob("*") if p.is_file()}
        for m in BARE_RE.finditer(content):
            fname = m.group(1)
            if fname not in present and fname not in RUNTIME_NAMES:
                err(f"{where}/{rel}: mentions `{fname}`, which is not inside the skill folder")
        for pat, why in PORTABILITY_HINTS:
            if pat.search(content):
                warn(f"{where}/{rel}: {why}")
        if path == md:
            if "../" in content:
                err(f"{where}/SKILL.md: '../' reaches outside the skill folder")

    files = [p for p in skill_dir.rglob("*") if p.is_file() and p.name not in EXCLUDE]
    if len(files) > MAX_FILES:
        err(f"{where}: {len(files)} files exceeds the {MAX_FILES}-file limit")
    return name


def load_spec():
    return json.loads(SYNC_FILE.read_text(encoding="utf-8")) if SYNC_FILE.exists() else {}


def load_sync():
    return [(ROOT / s["from"], ROOT / s["to"]) for s in load_spec().get("copies", [])]


RUNTIME_NAMES.update(load_spec().get("runtime_names", []))


def check_sync():
    for src, dst in load_sync():
        if not src.exists():
            err(f"skill-sync.json: canonical file missing: {src.relative_to(ROOT)}")
        elif not dst.exists():
            err(f"skill-sync.json: copy missing: {dst.relative_to(ROOT)} (run: package-skill.py sync)")
        elif src.read_bytes() != dst.read_bytes():
            err(f"skill-sync.json: {dst.relative_to(ROOT)} has drifted from {src.relative_to(ROOT)} (run: package-skill.py sync)")


def do_sync():
    for src, dst in load_sync():
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
        print(f"synced {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


def skill_dirs():
    if not SKILLS_DIR.is_dir():
        err("no skills/ directory at the repo root")
        return []
    return sorted(p.parent for p in SKILLS_DIR.glob("*/SKILL.md"))


def check():
    names = [validate_skill(d) for d in skill_dirs()]
    check_sync()
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    if errors:
        print(f"package-skill: FAIL ({len(errors)} errors, {len(warnings)} warnings)")
        sys.exit(1)
    print(f"package-skill: OK ({len(names)} skill(s), {len(warnings)} warnings)")
    return names


def build():
    check()
    DIST.mkdir(exist_ok=True)
    for d in skill_dirs():
        out = DIST / f"{d.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(d.rglob("*")):
                if p.is_file() and p.name not in EXCLUDE:
                    z.write(p, Path(d.name) / p.relative_to(d))
        size = out.stat().st_size
        if size > MAX_ZIP_BYTES:
            print(f"error: {out.name} is {size} bytes, over the 50 MB limit")
            sys.exit(1)
        with zipfile.ZipFile(out) as z:
            top = {n.split("/")[0] for n in z.namelist()}
            if top != {d.name} or f"{d.name}/SKILL.md" not in z.namelist():
                print(f"error: {out.name} must contain only {d.name}/ at the top, with {d.name}/SKILL.md")
                sys.exit(1)
            print(f"built dist/{out.name}: {len(z.namelist())} files, {size} bytes")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    {"check": check, "sync": do_sync, "build": build}.get(cmd, lambda: sys.exit(f"unknown command: {cmd}"))()
