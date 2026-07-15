# Fixtures — the test corpus

This is the skill's test suite. Everything in `docs/roadmap.md` depends on it, and it comes before any review stage is built.

## Why this exists

The checklist's evidence base, until now, is that people at the Department of State hated using it and their products came out exceptional. That is true, and it is not a test. It cannot tell you whether checklist v7 is better than v6, and it cannot tell a stranger on GitHub whether this skill is worth installing.

The 2023 custom GPT was *fine*. It was fine because nothing measured it.

A fixture corpus makes a change to the checklist **checkable**: run the skill over the corpus, and see what it catches now that it didn't catch before. That is the difference between revising the checklist by evidence and revising it by taste.

## Layout

```
fixtures/
  <slug>/
    brief.md              the P1 audience context — who this was for, what they were deciding
    document.md           the report itself, as submitted for review
    expected-findings.md  what a competent reviewer MUST surface. The assertion.
    notes.md              (optional) provenance, what was sanitized, why this one is here
```

## What makes a good fixture

**Real, or realistic enough to fail the way real documents fail.** Sanitize client work — change names, numbers, and identifying detail — but do not smooth out the flaws. Invented bad writing fails in tidy, obvious ways. Real bad writing fails by burying the recommendation on page four, by answering a question nobody asked, by hedging a finding into uselessness. Those are the failures worth catching.

**A spread.** The corpus needs at least:

- **two deliberately flawed** documents, with different *kinds* of flaw — one that fails on analysis (Review 1: doesn't answer the question asked, unstated assumptions), one that fails on organization or line-level craft (Reviews 2–3).
- **at least one genuinely good** document. This is the false-positive control, and it is the one people forget. A reviewer that finds twelve problems in a strong report is not a strict reviewer, it is a broken one — and an author who gets flooded with false findings stops reading them.
- ideally one **near-miss**: broadly solid, with a single serious flaw. This is the hardest case and the most diagnostic.

## `expected-findings.md` — the assertion

This is the heart of it. Write it **before** the skill exists to surface anything, so the skill is graded against a human's judgment rather than the corpus being quietly bent to match whatever the skill happens to produce.

```markdown
# Expected findings — <slug>

## Must catch
Findings a competent reviewer cannot miss. If the skill misses one of these, it has failed.

- [ ] **Review 1 (Analysis):** The report never answers the reader's actual question — they
      asked whether to renew the contract; the report describes vendor performance and stops.
- [ ] **Review 3 (Line-by-line):** Executive summary is 340 words with no bolded takeaway.

## Should catch
Real findings, but a good reviewer might reasonably rank them lower.

- [ ] **Review 2 (Organization):** "Background" heading — the checklist calls for a headline
      that carries the finding.

## Must NOT flag
False-positive traps. Things that look like problems and are not.

- [ ] The 31-word sentence in §3 is a quotation from the client's own RFP. Quoting it
      verbatim is correct; "shorten it" would be wrong.
```

The **Must NOT flag** section matters as much as the others. It is the only thing that keeps the skill honest about precision, and it is the section that only someone with real reviewing experience can write.

## A warning about the corpus itself

`expected-findings.md` is a human writing down the right answer. It will be incomplete. The skill will eventually surface true findings that are not in it.

**Those are not false positives. They are bugs in the corpus.** When it happens, add the finding to the fixture — do not "fix" the skill for being right. Budget for updating the corpus roughly as often as the skill.

## Status

Empty. This is M1, and it is the long pole.
