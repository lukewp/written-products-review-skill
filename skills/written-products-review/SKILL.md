---
name: written-products-review
description: Review a written product — an insights report, brief, memo, or presentation — through a multi-stage quality-gate process before it goes to its reader. Use when the user wants a report/brief/memo/deck reviewed, edited, or checked before delivery; when they ask "review this product / is this ready to send / run the checklist on this"; or when they want a rigorous editorial pass on analytic or client-facing writing. Based on the Insights Report Checklist (v6) by Luke Peterson.
---

# Written Products Review

A written product passes through **up to twelve stages**, each a **gate**. The document cannot advance to the next gate until the current one's completion criteria are met, its stage output is produced, and the author confirms. The process is the same every run; only the content changes. That predictability is the point — the same gates, the same completion criteria, the same output formats, every document.

This file is the **process skeleton**. Each stage's detailed checklist, completion criteria, and output format live in a reference file loaded only when that stage is reached. Do not load a stage's reference file before you get there.

## Source of truth

Every stage is derived from `insights-report-checklist.md` (v6) at the repository root. The checklist is canonical; these reference files execute it. If a rule here conflicts with the checklist, the checklist wins.

## The gate protocol

Each stage is a gate. To pass a gate:

1. **Meet the completion criteria.** Each stage reference file lists exhaustive, checkable conditions. Every one must be assessed — not "looks good," but each item, explicitly.
2. **Produce the stage output** in the format the reference file defines.
3. **Get the author's decision:** *proceed* to the next gate, *resubmit* a revised document to re-run this gate, or *skip* forward with an explicit warning.

Never advance without all three. Never auto-apply edits — surface findings; the author revises and resubmits. The author retains control of the document at every gate.

**Skipping.** The author may skip a stage. Warn first, concretely: "Stage 3 builds on the organization findings from Stage 2 — skip anyway?" A skip is the author's informed choice; record it as skipped (not passed) in the state.

## The stages

| # | Stage | Reference file | Gate |
|---|-------|---------------|------|
| P1 | **Audience** | `references/audience.md` | The **brief** is complete and confirmed. |
| P2 | **First read** | `references/first-read.md` | **Highlights** produced — positives only, no edits. |
| 1 | **Analysis & strategic insight** | `references/01-analysis.md` | Every analysis item assessed. |
| 2 | **Organization** | `references/02-organization.md` | Structure assessed against the five-section contemplation. |
| 3 | **Line-by-line** | `references/03-line-edit.md` | Every flagged line presented as a **current/potential** pair. |
| 4 | **Read aloud** | `references/04-read-aloud.md` | Readability pass + title/filename check done. |
| 5 | **Sensitivity** | `references/05-sensitivity.md` | Every sensitivity flag surfaced. |
| 6 | **Fresh eyes** | `references/06-fresh-eyes.md` | Sub-agent summary compared to the P2 highlights. |
| 7 | **Packaging** | `references/07-packaging.md` | Format validation complete. |
| 8 | **Accessibility** | `references/08-accessibility.md` | Accessibility audit complete. |
| 9 | **Presentation** *(if a deck)* | `references/09-presentation.md` | Slide checks complete, or stage marked N/A. |
| 10 | **Publishing** *(if public)* | `references/10-publishing.md` | Publication checks complete, or stage marked N/A. |

Stages proceed **in order**. 9 and 10 are conditional: run 9 only for a presentation/deck, 10 only for a document being published publicly online. If a conditional stage does not apply, mark it N/A and proceed — do not skip silently.

## State

Maintain a lightweight state block across the session so the review can resume if interrupted:

```
## Review state
Document: [name/version identifier]
Style standard: [General / DIA / AP] [+ user overlay]
Current stage: [P1 / P2 / 1 … 10]
History: [P1 ✓ · P2 ✓ · 1 ✓ · 2 resubmitted×1 ✓ · 3 → current]
```

The **brief** (from P1) and the **highlights** (from P2) persist in full for the whole session — later stages reference them. Everything else in the state is metadata.

## Leading words

These compact terms anchor consistent behavior. Use them exactly.

- **gate** — each stage is a gate the document must pass. Quality checkpoint; go/no-go.
- **brief** — the audience artifact built in P1. The single source of truth for *who this is for and why*. Every later stage may assume it exists and reference it.
- **highlights** — the positive-first output of P2. What was great, flagged on the first read. Returns in Stage 6.
- **current/potential** — the diff format for line-level edits (Stage 3). Show the author the current text and a potential rewrite, side by side. This is the standard format whenever the skill proposes a specific rewrite anywhere.
- **fresh eyes** — the Stage 6 sub-agent that has never seen the document and receives no prior review history. Its job: summarize the document cold.

## Style branching

The review process is identical regardless of style standard; what changes is the ruleset loaded during **Stages 1–3**. The **brief** records one **style standard**, set in P1:

- **General** *(default)* — `references/style-rules.md`. Smart Brevity / Strunk & White rules; 25-word sentence max.
- **DIA** — loads `references/DIA-style-quick-reference.md` into context at Stage 3; `references/DIA-style-manual.md` is grep-only for specific rule lookups (do not read it in full). Also sharpens Stages 1–2: words of estimative probability, the analytic phrase map, 20-word sentence max.
- **AP** — `references/ap-style-rules.md`. Strict AP for journalism/PR/comms; no Oxford comma by default.

A user may provide their own style guide as an **overlay** on any standard. Precedence: **user overlay > style standard > base checklist rules.** When an overlay or standard overrides a base rule, say so at Stage 3 ("AP omits the Oxford comma; your base checklist requires it — AP wins here unless you override").

## Starting a review

1. Confirm you have the document (text, or a file to inspect).
2. Load `references/audience.md` and run **P1** to build the brief. If the user has already supplied rich audience context, extract it, present the brief, and confirm — don't re-interview.
3. Advance through the gates in order, loading one reference file at a time.

Begin at P1.
