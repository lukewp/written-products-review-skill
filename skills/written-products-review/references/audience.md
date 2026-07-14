# P1: Audience interview

Build the **brief** — the audience context artifact that every subsequent review stage references. This is an interview, not a form.

## Before asking anything

Check what context already exists. The user may have:

- Uploaded a document (scan its intro, executive summary, and any metadata for clues about audience)
- Provided a project description or Epic description in the conversation
- Mentioned the reader, their role, or the purpose in passing

Extract every fact you can from available context. Present what you found: "Based on your document's introduction, it looks like the intended reader is [X] and the core question is [Y]. Does that sound right?"

Only ask the user about gaps — fields where you have nothing or are uncertain.

## The interview

Ask one question at a time. For each, offer your recommended answer if you have enough context to guess. Wait for the user's response before continuing.

Challenge vague answers. "Leadership" is not a reader — a specific person or role is. "They need to know about our findings" is not a decision — what will they *do differently* after reading this?

### Question sequence

1. **Reader.** Who is the intended reader? What is their role?
   - Push for specificity: name, title, or at minimum a concrete role ("the CTO" not "leadership").

2. **Decisions.** What decisions might they be confronting?
   - The answer shapes what the document must *recommend*, not just *report*. If the reader isn't facing a decision, the document is informational — that changes how reviews 1 and 2 evaluate it.

3. **Mission.** What is their mission, objective, and approach?
   - This is the reader's context, not the author's. What is the reader trying to accomplish in their role?

4. **Span.** What is their span of action and influence?
   - What can this reader actually *do* with the information? This bounds the scope of actionable recommendations.

5. **Questions asked.** What specific questions did they ask us to address?
   - If the reader asked specific questions, the document must answer them. Review 1 evaluates this directly. If none were asked, note that — it changes how "answers the questions asked" is interpreted.

6. **Topic.** What is an update or other topic you're familiar with and they need to know about?
   - This surfaces the author's intent: what they want to communicate beyond answering questions.

7. **Priority.** Why did we choose to prioritize this work above other work?
   - Establishes the stakes. If the answer is weak, the document may need a stronger "why this matters" framing.

8. **Significance.** Why will the reader find this work significant?
   - This is the reader's perspective, not the author's. What makes *them* care? The answer often differs from the author's reason for prioritizing.

9. **Style standard.** Is this document held to a specific style standard?
   - Offer three options: **General** (default — Smart Brevity / Strunk & White rules, 25-word sentence max), **DIA** (DIA/IC analytic production standards — WEPs, analytic phrase map, 20-word sentence max), or **AP Style** (strict AP adherence for journalism/PR/comms).
   - If the reader is in the intelligence community or the document is an analytic product, recommend DIA. If it's a press release, media advisory, or public-facing communications piece, recommend AP. Otherwise default to General.
   - The user can also provide their own style guide as an overlay on any standard.

## Building the brief

After each answer, update the brief immediately. The user should see it growing, not receive it as a surprise at the end.

Present the brief in this format after each update:

```
## Brief

**Reader:** [name/role, span of action]
**Decisions:** [what they're deciding]
**Mission:** [their objective and approach]
**Questions asked:** [specific questions, or "none specified"]
**Topic:** [what we're communicating]
**Priority:** [why this work was prioritized]
**Significance:** [why the reader will care]
**Style standard:** [General / DIA / AP Style] + [user overlay if provided]
```

Omit fields not yet answered. As each field fills in, the brief takes shape.

## Completion

The gate passes when:

1. All 8 brief fields are populated (Reader and Span merge into one field; Style standard has a value).
2. The user has confirmed the complete brief is accurate.
3. No fields contain vague language that would prevent a reviewer from evaluating the document against this audience.
4. Style standard is one of General, DIA, or AP Style (plus optional user overlay).

If the user wants to skip a field, record it as "not specified" — don't leave it blank. Downstream stages need to know the difference between "we don't know" and "we haven't asked yet."

## Shortcut: pre-filled brief

If the user provides a complete or near-complete audience context upfront (e.g., pasted from an Epic description), extract all fields, present the brief, and ask for confirmation. Skip the sequential interview — it would waste their time. Only fall back to one-at-a-time questioning for missing or ambiguous fields.
