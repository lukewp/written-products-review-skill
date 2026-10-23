# ADR 0002 — The skill folder is self-contained

**Status:** Accepted (2026-10-23)

## Context

Users of the installed skill reported that Claude said it could not see the skill's materials. There were two causes.

1. **The canonical checklist lived outside the skill.** `SKILL.md` named `insights-report-checklist.md` "at the repository root" as the source of truth. Only `skills/written-products-review/` is ever installed, on any platform, so the checklist was never there.
2. **Plugin sync on claude.ai drops subfolders.** In an October 2026 session, all 23 skills installed through plugin sync, from several authors, arrived as `SKILL.md` alone. Anthropic's own skills, installed as zips, arrived complete. Claude's documentation says the whole folder should be copied, so this is a platform bug, but the skill has to survive it.

The skill is also wanted in ChatGPT and Codex, which read the same Agent Skills format.

## Decision

- ADR 0001 stands: the checklist at the repo root is canonical. `scripts/package-skill.py sync` copies it, and `NOTICE.md`, into `references/`. `check` fails on drift, on any file the skill names that is not inside its folder, and on frontmatter outside the Agent Skills spec. CI runs it, the official `skills-ref` validator, and a zip build on every push.
- `SKILL.md` gains a **Step 0** that checks its reference files are present and, if not, tells the user to reinstall from the zip instead of reviewing from memory.
- Fresh eyes is worded generically, with a same-context fallback for surfaces that have no sub-agents.
- The repo carries both `.claude-plugin/plugin.json` and a portable root `plugin.json`, plus `agents/openai.yaml` for ChatGPT.
- The recommended claude.ai install is the zip from `package-skill.py build`.

## Consequences

- Editing `skills/written-products-review/references/insights-report-checklist.md` directly is a bug. Edit the root checklist and run `sync`.
- `package-skill.py` is vendored from the maintainer's skills tooling; update it by copying the newer version in, not by editing it here.
