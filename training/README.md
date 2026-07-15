# Training dropbox — private, never committed

Drop real documents here. **Nothing in this directory is ever committed** — `.gitignore` excludes `training/*`, and a pre-commit hook hard-blocks it even if something gets force-added. This README is the only file in here that git tracks.

## What this is for

This is the raw drop zone. Real insights reports, in whatever shape they actually exist. Messy is fine — messy is the point.

The corpus flows one way:

```
training/          →   (sanitize)   →   fixtures/
private, real                           public, safe to ship
never committed                          in the repo
```

Documents land here. What ends up in `fixtures/` is either a sanitized version or a synthetic stand-in that reproduces the same *failure*, paired with an `expected-findings.md` that carries your actual review judgment.

You can also just run the skill against `training/` directly and never promote anything. A private regression suite that nobody else can see is still a regression suite — and the aggregate scores from it ("catches 87% of must-catch findings across 12 documents") are publishable evidence that discloses nothing.

## Before you put anything in here

**Do not place classified or CUI material in this directory.** Not sanitized, not redacted, not "mostly cleaned." A gitignore is a convenience, not a control. This is a laptop in a git repo, and the wrong file here is a spill.

**Client-confidential work:** check what your engagement terms actually permit before the document leaves your own storage — including before you show it to an agent, which sends it to an API. When in doubt, sanitize first. It's cheap.

## Sanitization checklist

Run this before a document is shown to anyone or anything, and again before it's promoted to `fixtures/`:

- [ ] **Names** — client, people, internal staff, product names. Replace consistently (a find-replace that leaves one instance behind is the classic failure).
- [ ] **Numbers** — revenue, headcount, dates, contract values. Change the magnitudes, keep the *shape*: if the finding depends on a number being surprisingly small, it must stay surprisingly small.
- [ ] **Sector and geography** — if the client is identifiable from "the only lithium refiner in Nevada," change it.
- [ ] **Quotes and verbatims** — anything quoted from a client interview or internal doc is doubly sensitive and searchable.
- [ ] **Metadata** — author, company, and revision history live inside `.docx` and `.pdf` files. Converting to markdown drops them; check anything you didn't convert.
- [ ] **Filename** — the thing everyone forgets.
- [ ] **The flaws survive.** This is what makes the fixture worth anything. Sanitize the identity, not the writing. A buried recommendation must stay buried; a 340-word executive summary must stay 340 words.

## Suggested layout

Anything works — this is your scratch space. But if you want to run the skill against these directly:

```
training/
  <slug>/
    document.md            the report
    brief.md               (optional) who it was for, what they were deciding
    expected-findings.md   your review judgment — the part that actually matters
```

The `expected-findings.md` is the valuable artifact. The document is only the stimulus; your findings are the label. Write them **before** running the skill, or you will unconsciously grade the skill against itself.

See `fixtures/README.md` for the full format and `fixtures/TEMPLATE/` for the template.
