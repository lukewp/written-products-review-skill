# Roadmap

Written test-first: each milestone states **how we'll know it's done** before it states what to build. A milestone is finished when its acceptance criteria pass, not when the work "feels" complete — the same discipline the checklist itself imposes on a document.

The ordering is deliberate. **The test corpus (M1) comes before any review stage is built.** The 2023 GPT struggled because nothing measured it, and the only evidence the checklist worked was that products at State came out good. That is a true story and it is not a test. Until a change to the checklist can be shown to catch something it previously missed, "v7 is better than v6" is a matter of taste.

---

## M0 — Foundation *(this commit)*

**Done when:** a stranger lands on the repo and can answer three questions without asking — what is this, what does it cost me to use it, and what state is it in. And every third-party document in the repo has a known, stated license.

- [x] README: provenance, stages, status, install target, license
- [x] Roadmap with acceptance criteria (this file)
- [x] CC BY 4.0 / MIT split, attribution string, `NOTICE.md`
- [x] Plugin layout (`.claude-plugin/`, `skills/written-products-review/`)
- [x] ADR 0001 — the checklist is canonical; reference files are derived
- [ ] **Verify the DIA Style Manual's license.** It is 370KB of someone else's document sitting in a repo we are licensing to the public. It is almost certainly a U.S. government work and therefore public domain — but confirm it rather than assume it, and record the finding in `NOTICE.md`. If it turns out not to be redistributable, it comes out and the quick-reference gets rewritten from first principles.

## M1 — The corpus *(the test suite)*

**Done when:** we can run the checklist against a document and get a score we didn't make up.

- [ ] `fixtures/` holds **at least five real insights reports**. Sanitized or synthetic if client work can't be published — but they must fail the way real documents fail, not the way invented examples fail.
- [ ] At least two are deliberately flawed, and at least one is genuinely good.
- [ ] Each fixture has an `expected-findings.md`: the findings a competent reviewer **must** surface, written by a human, before the skill exists to surface them. This is the assertion.
- [ ] A documented way to run a review over a fixture and diff actual findings against expected.

**Everything is red at this point.** No stage exists, so every fixture fails every assertion. That is the correct starting state and the reason this milestone comes first.

> Judgment call to make here: `expected-findings.md` is a human writing down the right answer. It will be incomplete, and the skill will eventually surface true findings that aren't in it. Those are not false positives — they are corpus bugs. Budget for updating the corpus as often as the skill.

## M2 — The spine

**Done when:** the skill runs on a fixture through P1 and P2 and **refuses to advance** without a confirmed brief and a highlights list. The gate holds even when the user pushes on it.

- [ ] `SKILL.md` — process skeleton, stage index, gate protocol
- [ ] P2 (`first-read.md`); P1 (`audience.md`) already written
- [ ] Session state: current stage, pass/fail history, document version

Test the gate adversarially. A gate that yields when the user says "just skip it and give me the edits" is not a gate, and that failure mode is what made the GPT merely fine.

## M3 — The core reviews

**Done when:** on the flawed fixtures, stages 1–3 surface **most of the expected findings** with few false positives on the clean one. Set the real numbers once M1 gives us a baseline — a target invented now would just be a number we made up.

- [ ] Stages 1–3: analysis, organization, line-by-line
- [ ] `style-rules.md` (General — the default), `ap-style-rules.md`
- [ ] Style-standard branching: General / DIA / AP, selected in P1
- [ ] The precedence ladder actually works: user overlay > style standard > base checklist. The known collision is the Oxford comma — the checklist mandates it, AP drops it. Stage 3 must say out loud which rule won and why.

This is the heart of the skill. If M3 doesn't beat a careful human read on the flawed fixtures, nothing downstream matters.

## M4 — The rest of the reviews

**Done when:** stages 4–8 run, and the two stages that needed prototyping have been prototyped rather than guessed at.

- [ ] **Prototype first — read-aloud (4).** The checklist frames this as a human activity; the GPT offered text-to-speech. We lean toward computational readability analysis plus the title/filename check, but this is a guess and it needs a throwaway prototype before it becomes a stage file.
- [ ] **Prototype first — fresh eyes (6).** The interesting question is whether a cold sub-agent's takeaways diverge from the author's intent in a way that is *useful*. If they never diverge, the stage is theater. Test it before building it.
- [ ] Stages 5, 7, 8: sensitivity, packaging, accessibility

## M5 — Conditional stages and format inspection

**Done when:** stages 9–10 run on a real `.pptx` and a real published page, not on a description of one.

- [ ] Stages 9 (presentation), 10 (publishing)
- [ ] Decide the format-inspection question the architecture doc left open: ship docx/pdf/pptx parsing, or delegate to existing skills

## M6 — Release

**Done when:** someone who has never met us installs it, runs it on their own report, and gets a review they'd have paid for.

- [ ] Plugin manifest verified — both install paths actually work from a clean machine
- [ ] **Sample style guides.** The DIA quick-reference is already one; ship two or three more (a consulting house style, a public-comms style) to demonstrate the overlay format and give the future generator skill a target output.
- [ ] **Cut checklist v7** — from what the build taught us, with the corpus as evidence for each change. This is the payoff: the first version of the checklist revised against something other than taste.
- [ ] `/generate-style-guide` companion skill — scoped in the architecture doc. Deliberately *after* release, not before.

---

## Open questions

Carried from [`skill-architecture.md`](vision/skill-architecture.md); each needs an answer before the milestone that depends on it.

| Question | Blocks |
|---|---|
| Read-aloud: TTS, or computational readability analysis? | M4 |
| Cross-product references (stage 1) requires corpus access. Out of scope for v1 and flagged as a human checkpoint? | M3 |
| Format inspection (stages 7–9): ship parsing, or delegate? | M5 |
| How are reference files *derived* from the checklist — by hand with a cited section header, or generated by a script that can detect drift? | M3 |
