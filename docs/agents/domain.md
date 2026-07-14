# Domain Docs — Consumer Rules

## Layout

**Single-context.** This repo has one bounded context.

- `CONTEXT.md` at the repo root — domain language, key concepts, ubiquitous language
- `docs/adr/` — architectural decision records (ADR format: `NNNN-title.md`)

## Consumer rules

1. **Read `CONTEXT.md` before making domain-level suggestions.** If a term is defined there, use it — don't invent synonyms.
2. **Read relevant ADRs before proposing architectural changes.** An ADR records a decision that was already made; don't re-litigate it unless the user asks to.
3. **When a new decision is made, write a new ADR.** Use the next available number. Follow the template in `docs/adr/0000-template.md` if it exists; otherwise use: Status, Context, Decision, Consequences.
