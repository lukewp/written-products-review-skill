# Written Products Review

A deployable slash-skill that walks authors through a multi-stage editing and publishing process for written products — reports, briefs, memos, presentations. Based on the Insights Report Checklist (v6), which synthesizes principles from Smart Brevity, Strunk & White, Tufte, AP Style, and the Army War College Communicative Arts Directive.

## Where this came from

The checklist began in 2016 as a Word document its author used on his own writing. It became a Google Doc, then a standard: at the U.S. Department of State, staff who wanted a research product reviewed had to first write a brief answering the audience questions, then complete the entire checklist themselves. Only then would it go up for review — where it was run from the top a second time. The process was not popular. The products were exceptional.

A custom GPT followed in 2023. It worked, and it struggled: nothing held it to the process, and nothing measured whether it was any good.

This repo is the fourth iteration, and the first one that can be held to both.

## What it does

The skill runs a document through up to 12 review stages, each a quality gate the document must pass before advancing:

| Stage | Focus |
|-------|-------|
| P1 | Audience interview — build a **brief** describing the reader, their decisions, and why this work matters |
| P2 | First read — highlights only, no edits |
| 1 | Analysis and strategic insight — does it answer the questions asked? |
| 2 | Organization — executive summary, logical structure, assert-support-analyze flow |
| 3 | Line-by-line — style rules, sentence length, current/potential edit pairs |
| 4 | Read aloud — readability, awkward phrasing, title and filename check |
| 5 | Sensitivity — nothing scandalous, classification markings appropriate |
| 6 | Sanity check — fresh-eyes sub-agent summarizes the document cold |
| 7 | Packaging — fonts, image resolution, links, page numbers |
| 8 | Accessibility — alt text, header tags, table headers, chart descriptions |
| 9 | Presentation *(if applicable)* — font sizes, breathing space, PDF delivery |
| 10 | Publishing *(if applicable)* — SEO, LLM citation optimization |

At each gate, the author can revise and resubmit or skip forward.

## Status

**Pre-build.** Architecture is resolved and the audience stage (P1) is written. `SKILL.md` and the remaining eleven stage files do not exist yet. The skill is not yet installable.

See [`docs/roadmap.md`](docs/roadmap.md) for the milestones and what "done" means for each.

## Install

*Not yet — this section describes the target, not the present. Tracked as M6 in the roadmap.*

As a Claude Code plugin:

```
/plugin marketplace add lukewp/written-products-review-skill
/plugin install written-products-review@lukewp
```

Or copied into your project, so you can edit the checklist to fit your house style:

```
npx skills@latest add lukewp/written-products-review-skill
```

## Repo layout

```
insights-report-checklist.md   ← the checklist. Canonical. See ADR 0001.
AGENTS.md                      ← agent-facing project context
skills/
  written-products-review/
    SKILL.md                     process skeleton and gate protocol (not yet written)
    references/                  per-stage review criteria, derived from the checklist
      audience.md                  P1: audience interview protocol
      DIA-style-quick-reference.md compact analytic writing rules
      DIA-style-manual.md          full DIA style manual (grep-only, 9,700 lines)
docs/
  roadmap.md                   ← milestones and acceptance criteria
  adr/                           architectural decision records
  vision/
    skill-vision.html            interactive vision board (stages, gaps, decisions)
    skill-architecture.md        resolved architecture decisions
  agents/                        engineering skill config (issue tracker, triage, domain)
fixtures/                      ← the test corpus (not yet built — see M1)
```

## Architecture

Hybrid entry point: one `SKILL.md` (~200 lines) holds the process skeleton and gate protocol. Each stage loads its review criteria from a separate file in `references/`, so the agent only sees the current stage — preventing premature completion.

The checklist is the source of truth. Every stage reference file is *derived* from it and cites the section it came from; when a rule changes, it changes in the checklist first ([ADR 0001](docs/adr/0001-checklist-is-canonical.md)).

Full rationale in [`docs/vision/skill-architecture.md`](docs/vision/skill-architecture.md). Interactive vision board at [`docs/vision/skill-vision.html`](docs/vision/skill-vision.html).

## License and attribution

Two licenses, because this repo holds two different things.

| What | License |
|------|---------|
| The checklist, the stage criteria, the style guides, the docs — everything in `insights-report-checklist.md`, `skills/**/references/`, and `docs/` | [CC BY 4.0](LICENSE-CONTENT) |
| The skill scaffolding and any tooling — `SKILL.md`, `scripts/`, manifests | [MIT](LICENSE-CODE) |

Use it, fork it, adapt it to your firm's house style, use it on client work. The one thing asked in return is credit:

> Based on the Insights Report Checklist by Luke Peterson (2016–2026), https://github.com/lukewp/written-products-review-skill

Third-party material included in this repo is listed in [`NOTICE.md`](NOTICE.md).

## Source material

The checklist draws from: Allen, Schwartz & VandeHei (*Smart Brevity*); Cook (*Line by Line*); Fogarty (*Grammar Girl*); Orwell (*Politics and the English Language*); Provost (*100 Ways to Improve Your Writing*); Strunk & White (*Elements of Style*); Truss (*Eats, Shoots & Leaves*); Tufte (*Visual Display of Quantitative Information*); AP Stylebook (2024–2026); U.S. Army War College Communicative Arts Directive (2020).
