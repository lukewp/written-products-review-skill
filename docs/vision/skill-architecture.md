# Skill Architecture

Resolved design decisions for the written products review skill, informed by `writing-great-skills` principles, the `skill-creator` anatomy, and the `/grilling` + `/domain-modeling` interview patterns.

## Core principle

**Predictability**: the agent takes the same *process* every run — same gates, same completion criteria, same output formats — even though the content it produces varies by document. Every structural choice below serves this.

## Architecture: hybrid entry point + per-stage context files

```
written-products-review/
├── SKILL.md              # process skeleton, stage index, gate pattern (~200 lines)
├── references/
│   ├── audience.md        # P1: audience clarification questions + storage format
│   ├── first-read.md      # P2: first-read prompt + highlights output format
│   ├── 01-analysis.md     # Review 1: strategic insight checklist + completion criteria
│   ├── 02-organization.md # Review 2: structure checklist + 5-section template
│   ├── 03-line-edit.md    # Review 3: line-by-line rules + current/potential format
│   ├── 04-read-aloud.md   # Review 4: readability analysis + title check
│   ├── 05-sensitivity.md  # Review 5: sensitivity flags + classification check
│   ├── 06-fresh-eyes.md   # Review 6: sub-agent pattern + comparison protocol
│   ├── 07-packaging.md    # Review 7: format validation checklist
│   ├── 08-accessibility.md# Review 8: a11y audit checklist
│   ├── 09-presentation.md # Review 9: (conditional) slide-specific checks
│   └── 10-publishing.md   # Review 10: (conditional) SEO/LLM optimization
│   ├── DIA-style-quick-reference.md  # compact analytic writing rules (loaded in stage 3, DIA branch)
│   ├── DIA-style-manual.md           # full DIA style manual (grep-only, 9700 lines)
│   ├── ap-style-rules.md             # (to create) AP Style strict rules (loaded in stage 3, AP branch)
│   └── style-rules.md               # (to create) general rules from checklist sources (default branch)
└── scripts/                          # (future) deterministic tooling for format inspection
```

**Why hybrid, not monolithic:** a monolithic SKILL.md with all 12 stages inlined would exceed 500 lines (sprawl) and expose post-completion steps that cause premature completion. The hybrid splits by sequence: the agent sees only the current stage's prompt, loaded via context pointer when reached.

**Why not fully modular (separate skills per stage):** the stages share a single invocation surface ("/review") and a single state machine. Splitting into 12 separate skills would spend context load on 12 descriptions and require the user to remember which to invoke. One entry point, many reference files, zero extra context load.

## Gate pattern

Each stage is a **gate**. The agent cannot advance until:

1. The stage's **completion criteria** are met (checkable, exhaustive conditions).
2. The agent produces a **stage output** in a defined format.
3. The user confirms: proceed, resubmit, or skip (with warning).

The SKILL.md defines the gate protocol. Each stage reference file defines its specific completion criteria and output format.

### Completion criteria examples

- **P1 (Audience):** brief artifact complete — all 8 fields populated via sequential interview, user confirms the brief is accurate. Gate: brief confirmed.
- **Review 1 (Analysis):** every checklist item assessed with pass/fail + commentary. Gate: assessment complete, user confirms.
- **Review 3 (Line-edit):** every flagged issue presented as current/potential pair. Gate: all flags surfaced, user confirms.
- **Review 6 (Fresh eyes):** sub-agent summary produced and compared to P2 highlights. Gate: comparison presented, user confirms alignment.

## Leading words

These compact concepts anchor consistent agent behavior across stages:

- **gate** — each stage is a gate the document must pass. The word recruits the pretraining concept of quality gates, checkpoints, and go/no-go decisions.
- **current/potential** — the diff format for line-level edits (stage 3). Already established in the GPT prompt and real usage. Should be the standard format whenever the skill suggests specific rewrites.
- **fresh eyes** — the sanity-check pattern (stage 6). Anchors the sub-agent's role: it has never seen this document before and approaches it without the reviewing agent's accumulated context.
- **highlights** — the positive-first output from the initial read (P2). Returns in stage 6 when the fresh-eyes summary is compared to the original highlights.
- **brief** — the audience context artifact produced by P1. A structured document that accumulates during the interview and becomes the single source of truth all subsequent stages reference for "who is this for and why."

## Interview pattern (from `/grilling`)

The P1 audience stage and any other user-facing intake use an interview protocol adapted from the `/grilling` and `/domain-modeling` skills, not a form dump.

### Principles

1. **One question at a time.** Ask one, wait for the answer, then ask the next. "Asking multiple questions at once is bewildering." The answer to one question may sharpen or eliminate later ones.

2. **Facts are extracted, decisions are asked.** If the user has already provided context (uploaded document, project description, prior conversation), the skill extracts what it can and presents it for confirmation. Only gaps are put to the user as questions. "If a fact can be found by exploring, look it up rather than asking me. The decisions, though, are mine."

3. **The brief builds incrementally.** Each answer is recorded into the **brief** artifact immediately — not batched after all questions. The user sees it accumulating and can correct course mid-interview. By the end of P1, the brief is complete.

4. **Challenge fuzzy language.** When answers are vague or overloaded, push for precision. "You said 'the leadership team' — do you mean the client's executive committee, or your internal management?" This matters because every subsequent review stage evaluates the document against the audience the brief describes.

5. **Recommend, don't just ask.** For each question, the skill offers its recommended answer based on context it's already seen. The user confirms, edits, or overrides. This reduces cognitive load and speeds the interview.

### The brief artifact

The brief is a structured document produced during P1 that persists across the entire review session. It contains:

- **Reader**: who they are, their role, their span of action and influence
- **Decisions**: what decisions the reader is confronting
- **Mission**: their mission, objective, and approach
- **Questions asked**: specific questions the reader asked us to address
- **Topic**: what update or topic we're communicating
- **Priority**: why this work was prioritized above other work
- **Significance**: why the reader will find this work significant
- **Style standard**: which style ruleset governs this review (see Branching below)

Every stage reference file can assume the brief exists and point to it. The brief is also the input to the stage 6 fresh-eyes sub-agent (along with the current document).

## Branching: style standards

The review process is the same regardless of style standard — same 12 stages, same gates, same completion criteria. What changes is the ruleset loaded during stages 1–3. This is a classic branch per `writing-great-skills`: "inline what every branch needs, push behind a pointer what only some branches reach."

During P1, the brief collects a **style standard** field. Three values:

- **General** *(default)* — built-in rules from the checklist sources (Smart Brevity, Strunk & White, Tufte). 25-word sentence max. Loaded from `references/style-rules.md`.
- **DIA** — DIA/IC analytic production standards. 20-word sentence max, words of estimative probability, analytic phrase map, banned qualifier stacking, specific capitalization/abbreviation/number conventions. Loads `references/DIA-style-quick-reference.md` into context at stage 3; `references/DIA-style-manual.md` available for grep lookups. Also sharpens stages 1–2: analysis must use proper WEPs, judgments must follow the analytic phrase map.
- **AP Style** — strict Associated Press style adherence for journalism, PR, and public communications. Loads AP-specific rules (to be codified in `references/ap-style-rules.md`). Differences from general: no Oxford comma (unless the user overrides), specific title/number/date conventions, attribution standards.

The flag is set once during P1 and recorded in the brief. Stage reference files check it to decide which style materials to load. Users can also provide their own style guide as an overlay on any standard.

## Resolved design decisions

### 1. Skill architecture → Hybrid

One SKILL.md entry point (~200 lines) with context pointers to per-stage reference files in `references/`. Each stage file is loaded only when the agent reaches that stage. This prevents sprawl and premature completion.

### 2. Stage navigation → Sequential with skip

Stages proceed in order. The user can skip forward with a warning ("stage 3 builds on stage 2 findings — skip anyway?"). The gate pattern enforces this: each gate produces output that later stages may reference, so skipping is the user's informed choice.

### 3. State persistence → Structured state + conversation

Key metadata (audience context, current stage number, pass/fail history per stage, document version identifier) persists in a lightweight state structure. Full review commentary stays in conversation context. This allows resume if the conversation is interrupted.

### 4. Edit-resubmit loop → User-driven with suggested edits

At each stage, if the document fails checks, the skill presents specific findings (and current/potential pairs for stage 3). The user edits externally and resubmits. The skill re-runs the same stage on the resubmitted version. The skill does not auto-apply edits — the author retains control.

### 5. Fresh-eyes sub-agent → Sub-agent with isolated context

Stage 6 spawns a sub-agent that receives only: (a) audience metadata from P1, (b) the current document. It does NOT receive prior review history. Its job: summarize the document's key takeaways and flag errors. The reviewing agent then compares this summary to the original P2 highlights and asks the user if the fresh-eyes takeaways match their intent.

### 6. Style guide reference → Layered (built-in base + optional user overlay)

The skill ships with built-in style rules from three layers:

- `references/DIA-style-quick-reference.md` — compact rules for analytic writing: words of estimative probability, banned qualifier stacking, buried verbs, sentence structure (max 20 words, active voice, BLUF-first). Loaded into context during stage 3.
- `references/DIA-style-manual.md` — the full 9,700-line DIA Style Manual for Intelligence Production. Too large for context; grep-only for specific rule lookups (compounding, capitalization edge cases, abbreviation conventions).
- `references/style-rules.md` *(to be created)* — additional rules derived from the checklist's non-DIA sources (Smart Brevity, Strunk & White, AP Style, Tufte).

Users can optionally provide their organization's style guide, which overlays the defaults.

### 7. Document format handling → Tiered

Text analysis for all stages. Optional format-level inspection (via docx/pdf/pptx skill integration) for Packaging (7), Accessibility (8), and Presentation (9) stages. The skill detects document type and activates format inspection if available.

## Failure mode defences

| Failure mode | Defence |
|---|---|
| Premature completion | Sharp completion criteria per stage + sequence splitting (future stages hidden) |
| Sprawl | Progressive disclosure: SKILL.md is process skeleton only; checklist details in reference files |
| Duplication | Audience questions defined once in `references/audience.md`; style rules once in `references/style-rules.md` |
| No-ops | No "be thorough" or "provide detailed feedback" — each stage specifies exact checklist items and output format |
| Negation | No "don't skip stages" — gate pattern positively requires output before advancing |
| Sediment | Each stage file is independently prunable; dead items don't accumulate in the main SKILL.md |

## Scoped future work

### Style rule override pattern

Style standards conflict with each other on specific rules. The most concrete example: the base checklist mandates the Oxford comma ("unless strenuously instructed by management not to do so"), while AP Style omits it by default. The DIA standard tightens sentence length from 25 to 20 words.

When built, the override system needs to handle:

- **Standard-level overrides**: AP flips the Oxford comma default; DIA tightens sentence length. These are known conflicts, documented per-standard in the reference files.
- **User-level overrides**: the user's custom style guide may override *any* rule in *any* standard. User overrides take highest precedence.
- **Conflict surfacing**: when a standard overrides a base rule, stage 3 should note the override explicitly ("AP Style: Oxford comma omitted per standard — your base checklist requires it. AP wins here unless you override.") so the user knows what's being applied.

Precedence ladder: user overlay > style standard > base checklist rules. Each reference file should document which base rules it overrides and why.

### Custom style guide: user documentation

Users need guidance on how to provide their own style guide as an overlay. To be documented (likely in the SKILL.md or a `references/custom-style-guide.md`):

- **Format**: a markdown file with rules structured as the skill expects — categorized by the stages they affect (analysis, organization, line-edit) so the skill knows when to load them.
- **Scope**: a custom guide can add rules (things the base doesn't check), tighten rules (stricter sentence length), relax rules (allow passive voice in certain contexts), or flip defaults (no Oxford comma).
- **How to provide it**: upload the file at the start of the review, or point to a path. The skill records it in the brief under "Style standard" as an overlay.
- **What the skill does with it**: loads it alongside the selected standard's reference file during stages 1–3. User rules that conflict with standard rules win.

### Companion skill: style guide generator (`/generate-style-guide`)

A separate skill — distinct invocation surface, distinct leading word ("generate" vs. "review") — that produces a custom style guide file consumable by the review skill.

**Inputs** (any combination):
- Sample artifacts: the user uploads 3–5 documents that represent their desired style. The skill analyzes patterns — sentence length distribution, voice preference, terminology choices, formatting conventions, punctuation habits.
- Grilling interview: the skill walks the user through style decisions one at a time (Oxford comma? sentence length cap? passive voice tolerance? abbreviation policy? number formatting?) using the `/grilling` pattern — one question, recommended answer, wait for confirmation.
- Existing style guide: the user provides a prose style guide (PDF, Word doc, web page). The skill extracts machine-actionable rules from it.

**Output**: a markdown file in the format the review skill expects, saved to the user's workspace. The user can then reference it as their custom overlay in future reviews.

**Architecture notes**:
- This is a model-invoked skill (needs its own description) because users may ask for it unprompted ("help me create a style guide").
- It produces a file that the review skill consumes — the two skills are coupled by file format, not by invocation.
- The grilling branch reuses the `/grilling` interview protocol. The sample-analysis branch is novel — it needs a pattern-extraction prompt that identifies stylistic choices from exemplar documents.
- Could also be used to *update* an existing custom style guide based on new samples or changed preferences.

## Open questions (not yet resolved)

- **Read-aloud (stage 4):** The checklist frames this as a human activity. The GPT prompt offers TTS. For the skill, we lean toward computational readability analysis (awkward phrasing detection, sentence rhythm analysis) plus a title/filename check — but this needs prototyping.
- **Cross-product references (stage 1):** "Does it refer to findings from other recent internally-written products?" requires corpus access. Likely out of scope for v1; flag as a human checkpoint.
- **Format inspection tooling (stages 7–9):** What specific scripts or tool integrations are needed? Depends on whether we ship with docx/pdf parsing or delegate to existing skills.
