## Project vision

The skill implements a multi-stage written products review process (12 stages total: 2 pre-review gates, 8 core reviews, 2 conditional stages). The interactive vision board at `docs/vision/skill-vision.html` is the canonical reference for stage definitions, gap analysis between the checklist v6 and the original GPT prompt, and open design decisions. Read it before making architectural choices.

Architecture decisions (resolved via `writing-great-skills` principles): `docs/vision/skill-architecture.md`. This is the canonical reference for structural choices — hybrid architecture, gate pattern, progressive disclosure, leading words, and failure mode defences.

Roadmap and acceptance criteria: `docs/roadmap.md`. Milestones are written test-first — read the acceptance criteria before starting work on one.

**The checklist is canonical.** `insights-report-checklist.md` at the repo root is the source of truth. Stage reference files under `skills/written-products-review/references/` are *derived* from it and cite the checklist section they came from. A rule changes in the checklist first. Editing a rule in a reference file without editing the checklist is a bug — see `docs/adr/0001-checklist-is-canonical.md`.

**The skill folder ships alone.** Only `skills/written-products-review/` is installed. Never make the skill depend on a file outside it. Canonical root files are copied in with `python3 scripts/package-skill.py sync`; run `check` before committing. See `docs/adr/0002-skill-folder-is-self-contained.md`.

## Agent skills

### Issue tracker

Issues are tracked in GitHub Issues on `lukewp/written-products-review-skill` via the `gh` CLI. External PRs are not a triage surface. See `docs/agents/issue-tracker.md`.

### Triage labels

Default label vocabulary (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout — one `CONTEXT.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.
