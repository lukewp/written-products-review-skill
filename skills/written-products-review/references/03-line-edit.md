# Review 3: Line-by-Line

*Derived from the checklist's "Third Review: Line-by-Line." This is where the **style standard** ruleset loads.*

## Load the style ruleset first

Read the brief's **style standard** and load the matching rules **now**:

- **General** → read `references/style-rules.md`.
- **DIA** → read `references/DIA-style-quick-reference.md` into context. For a specific rule dispute (compounding, capitalization edge cases, abbreviation conventions), grep `references/DIA-style-manual.md` — do **not** read it in full.
- **AP** → read `references/ap-style-rules.md`.

If the author supplied a style **overlay**, load it too. Precedence: **user overlay > style standard > base checklist.** When a standard or overlay overrides a base checklist rule, say so explicitly in your findings.

## The format: current/potential

Every line-level suggestion is a **current/potential** pair — never a vague instruction. Show the author exactly what they wrote and exactly what you propose:

```
Current:   "It is important to note that the results, which were significant, suggest a trend."
Potential: "The significant results suggest a trend."
```

The author decides whether to adopt each. Do not auto-apply.

## Completion criteria — assess each (base checklist rules)

- [ ] **Style-guide alignment.** Does the product align to the relevant style guide (the loaded ruleset)?
- [ ] **Sentence length.** All sentences within the standard's cap — **25 words** (General/AP) or **20 words** (DIA). Flag every sentence over the cap with a current/potential pair.
- [ ] **"That" and "which".** The report avoids "that" and "which" except where the sentence cannot be rewritten more succinctly without them.
- [ ] **Three words → one.** Authors eliminated three words where two or one work.
- [ ] **Extra syllables cut.** Prefer the shorter word where it carries the same meaning.
- [ ] **Selective bolding.** Authors selectively bolded key ideas (not everything — bolding everything bolds nothing).
- [ ] **White space.** White space is used to make key findings stand out.
- [ ] **Headline over "Executive Summary".** Did the authors consider a brief summary **headline** instead of the literal words "Executive Summary" as the header? If so, the first sentence should offer detail under the headline.
- [ ] **Emoji for emphasis.** If appropriate for the audience in the brief, emoji used for emphasis (e.g., in section headers). Audience-dependent — check the brief.
- [ ] **Oxford comma.** Authors use the Oxford comma — **unless** the standard overrides it (AP omits it by default) or management strenuously instructs otherwise. State which rule applied.

Apply any additional rules from the loaded ruleset and overlay.

## Stage output — Line edits

```
## Review 3 — Line-by-line

**Style standard applied:** [General / DIA / AP] [+ overlay]
**Overrides in effect:** [e.g., "AP: Oxford comma omitted — base checklist requires it; AP wins"]

Current/potential pairs:
1. Current:   "…"
   Potential: "…"   — [rule: sentence length / redundancy / …]
2. …

**Criteria assessment:** [each item PASS/FAIL/N/A + one line]
```

## Completion gate

Passes when the correct ruleset was loaded, every flagged issue is a current/potential pair, every base item is assessed, overrides are stated, and the author confirms: proceed to Stage 4, or resubmit.
