# Written Products Review

A Claude Code skill that walks an author through a multi-stage editorial review of a written product — an insights report, brief, memo, or presentation — before it reaches its reader. It implements the **Insights Report Checklist**, a review process refined over nearly a decade of professional practice.

The skill runs a document through up to twelve **gates**. Each gate has explicit completion criteria and a defined output; the document cannot advance until the gate is met and the author confirms. The process is the same every run — same gates, same criteria, same formats — so the review is predictable regardless of what's being reviewed.

## Where this came from

The checklist began in 2016 as a Word document its author used on his own writing. It became a Google Doc, then a standard: at the U.S. Department of State, staff who wanted a research product reviewed had to first write a brief answering the audience questions, then complete the entire checklist themselves. Only then would it go up for review — where it was run from the top a second time. The process was not popular. The products were exceptional.

A custom GPT followed in 2023. It worked, and it struggled: nothing held it to the process. This repository is the next iteration, and the first one built as a proper skill — with the checklist as a canonical, versioned source and the review logic derived from it.

## What it does

| Stage | Focus |
|-------|-------|
| P1 | **Audience** — build a *brief*: who the reader is, the decision they face, why this matters |
| P2 | **First read** — a viewing pass; capture what's *great*, no edits |
| 1 | **Analysis & strategic insight** — does it answer the question and advise the decision? |
| 2 | **Organization** — executive summary first, logical structure, assert–support–analyze |
| 3 | **Line-by-line** — style rules, sentence length, *current/potential* edit pairs |
| 4 | **Read aloud** — readability, awkward phrasing, title and filename |
| 5 | **Sensitivity** — nothing scandalous or embarrassing; classification marking |
| 6 | **Fresh eyes** — a blind sub-agent reads the document cold; compare to P2's highlights |
| 7 | **Packaging** — fonts, image resolution, links, page numbers |
| 8 | **Accessibility** — alt text, header tags, table headers, chart descriptions |
| 9 | **Presentation** *(decks)* — font sizes, breathing space, PDF delivery |
| 10 | **Publishing** *(public docs)* — search and LLM-citation positioning |

At each gate the author revises and resubmits, or proceeds. The skill surfaces findings; it never silently rewrites the author's work.

### Style standards

Stages 1–3 load a style ruleset chosen in the brief: **General** (Smart Brevity / Strunk & White), **DIA** (IC analytic production standards — words of estimative probability, 20-word sentences), or **AP** (journalism/PR). Authors can layer their own style guide as an overlay; precedence is *user overlay > style standard > base checklist*.

## Install

**On claude.ai or the Claude desktop app, upload the zip.** Download `written-products-review.zip` from the latest [skill-check run's artifacts](https://github.com/lukewp/written-products-review-skill/actions/workflows/skill-check.yml) (or build it: `python3 scripts/package-skill.py build`), then go to Customize → Skills → upload. As of October 2026, skills installed through plugin sync on claude.ai arrive as `SKILL.md` alone, without their `references/` folder, and the skill cannot run its stages (ADR 0002). The skill's Step 0 detects this and says so.

**ChatGPT desktop, Codex, and the OpenAI API** read the same skill format. Copy `skills/written-products-review/` into `~/.codex/skills/`, install it as a plugin (the root `plugin.json` is in the portable format), or upload the zip to the OpenAI Skills API.

**As a Claude Code plugin.** Both lines are needed, in this order — the first registers the marketplace, the second installs from it:

```
/plugin marketplace add lukewp/written-products-review-skill
/plugin install written-products-review@lukewp
```

Restart Claude Code afterward; a running session won't pick up a newly installed plugin.

Or copied into a project, so you can adapt the checklist to your house style. This uses [`skills`](https://github.com/vercel-labs/skills), a third-party CLI from Vercel Labs:

```
npx skills@latest add lukewp/written-products-review-skill
```

Then invoke it by asking Claude to review a report, brief, memo, or deck — or run it explicitly on a document you want checked before it ships.

## Build

```
python3 scripts/package-skill.py sync    # after editing insights-report-checklist.md or NOTICE.md
python3 scripts/package-skill.py check   # what CI runs: frontmatter, self-containment, drift
python3 scripts/package-skill.py build   # writes dist/written-products-review.zip
```

The checklist stays canonical at the repo root (ADR 0001). `sync` copies it into the skill folder, because only the skill folder is ever installed. Never edit the copy.

## Status

**v6 implemented; validation in progress.** The skill is structurally complete — `SKILL.md` plus all twelve stage files — and derives from checklist v6. It is being validated against a corpus of real documents, and the checklist continues to evolve; a v7 is in progress.

## Repo layout

```
insights-report-checklist.md   ← the checklist (v6). Canonical. See ADR 0001.
skills/
  written-products-review/
    SKILL.md                     process skeleton, gate protocol, stage index
    references/                  per-stage criteria, each derived from the checklist
      audience.md                  P1 · first-read.md P2 · 01–10 the review gates
      style-rules.md · ap-style-rules.md      style rulesets (Stage 3)
      DIA-style-quick-reference.md · DIA-style-manual.md   DIA standard (Stage 3)
docs/
  roadmap.md                     milestones and acceptance criteria
  adr/                           architectural decision records
  checklist-history/             the lineage: v4, v5, v6 as they shipped
  vision/                        architecture rationale + interactive vision board
fixtures/                        scaffold for the test corpus
```

## Architecture

Hybrid entry point: one `SKILL.md` holds the process skeleton and gate protocol; each stage loads its criteria from a separate reference file only when reached, so the agent sees one stage at a time. This prevents sprawl and premature completion.

The checklist is the source of truth. Every stage file is *derived* from it and cites the section it came from; a rule changes in the checklist first ([ADR 0001](docs/adr/0001-checklist-is-canonical.md)). Full rationale in [`docs/vision/skill-architecture.md`](docs/vision/skill-architecture.md).

## License and attribution

Two licenses, because this repo holds two things.

| What | License |
|------|---------|
| The checklist, the review criteria, the style guides, the docs | [CC BY 4.0](LICENSE-CONTENT) |
| The skill scaffolding and any tooling | [MIT](LICENSE-CODE) |

Use it, fork it, adapt it to your firm's house style, use it on client work. The one thing asked in return is credit:

> Based on the Insights Report Checklist by Luke Peterson (2016–2026), https://github.com/lukewp/written-products-review-skill

Third-party material bundled here (the DIA Style Manual, public-domain and FOIA-released) is documented in [`NOTICE.md`](NOTICE.md).

## Source material

The checklist draws on: Allen, Schwartz & VandeHei (*Smart Brevity*); Cook (*Line by Line*); Fogarty (*Grammar Girl*); Orwell (*Politics and the English Language*); Provost (*100 Ways to Improve Your Writing*); Strunk & White (*Elements of Style*); Truss (*Eats, Shoots & Leaves*); Tufte (*Visual Display of Quantitative Information*); the AP Stylebook (2024–2026); and the U.S. Army War College Communicative Arts Directive (2020).
