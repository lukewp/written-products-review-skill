# ADR 0001 — The checklist is canonical

**Status:** Accepted (2026-07-14)

## Context

The rules exist twice. `insights-report-checklist.md` states them for humans; the skill's stage reference files state them again in a form an agent can execute. Two copies of one ruleset will drift.

This is not a hypothetical. `skill-architecture.md` lists **Duplication** in its failure-mode table and commits to defending against it, and the repo's entire purpose is to evolve the checklist across versions — v6 today, v7 after the build. A drifting second copy makes "what does the checklist say" unanswerable exactly when it matters most.

Three options were considered:

1. **Checklist canonical** — reference files derived from it.
2. **Skill canonical** — the reference files hold the real rules; the checklist is rendered out for human readers.
3. **Both, hand-maintained** — keep them in sync by hand.

## Decision

**The checklist is canonical.** `insights-report-checklist.md` is the source of truth. Every stage reference file is derived from it and cites the checklist section it came from. When a rule changes, it changes in the checklist first, and the reference file follows.

Option 3 is the failure mode we already named, so it was never really available.

Option 2 is defensible on engineering grounds — the executable form is the one that actually runs — but it inverts what this project is. The checklist is the artifact with a ten-year history, the citations, and the license. It is the IP. The skill is one way of executing it, and there will be others: a human reading it on paper, another vendor's agent, the next harness after this one. The thing that outlives the runtime should be the thing that holds the rules.

## Consequences

- Every reference file carries a provenance header naming its checklist section. A rule with no section is a rule that hasn't been agreed to yet.
- Editing a rule in a reference file without editing the checklist is a bug, not a shortcut.
- Drift becomes detectable, which means it can eventually be linted. Whether derivation is done by hand or by script is left open (see the roadmap's open questions) — the *direction* is what this ADR fixes, not the mechanism.
- The checklist must be able to express everything a stage needs. Where it can't, that is a gap in the checklist and a reason to revise it — which is the point of the repo.
- Cutting v7 means editing the checklist and re-deriving. The skill never becomes the place where new rules are born.
