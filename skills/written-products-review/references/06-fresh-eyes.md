# Review 6: Fresh Eyes (Sanity Check)

*Derived from the checklist's "Sixth Review: Sanity Check" — "have somebody who has not read this report yet do a basic scan for errors."*

The checklist calls for a person who has never seen the document. The skill's equivalent is a **fresh-eyes sub-agent**: a reviewer with no accumulated context, spun up specifically so its read is uncontaminated by everything the reviewing agent now knows.

This stage matters more than "scan for errors" suggests. It is the one point in the review where the document is judged by something that was **never told whom to like, what the author intended, or what the earlier stages found**. It is the structural check against the reviewer softening toward a document it has spent five stages getting to know.

## The sub-agent protocol

Spawn a sub-agent (Agent tool, `general-purpose`) that receives **only two things**:

1. The **audience facts from the brief** it needs to judge relevance — reader's role, span, and the decision they face. **Do not** pass the author's name, the client relationship, quality judgments, or any prior review history.
2. The **current document.**

Instruct it to return, cold:

- **Takeaways:** the document's key points, as *it* understands them — what would a reader do or believe after reading this?
- **Errors:** anything that looks wrong — factual slips, broken logic, typos, claims that don't follow.

It has never seen this document and has no stake in it. That is the entire value.

## Compare to the highlights

Take the sub-agent's **takeaways** and set them beside the **highlights** from P2 — what *you* flagged as the document's best, most important points on the first read.

- **Do they match?** If the cold reader's takeaways are the points the author meant to land, the document is communicating.
- **Do they diverge?** If the fresh reader walks away with different takeaways — or misses the big idea entirely — that is a finding: the document is not landing its intended message, however good the underlying analysis.

Present the comparison to the author and ask whether the fresh-eyes takeaways match their intent.

## Completion criteria

- [ ] Sub-agent spawned with **only** audience facts + document (no author identity, no relationship, no prior review history).
- [ ] Sub-agent returned cold takeaways and an error scan.
- [ ] Takeaways compared, point by point, to the P2 highlights.
- [ ] Divergences surfaced as findings; the author asked whether takeaways match intent.

## Stage output — Fresh-eyes comparison

```
## Review 6 — Fresh eyes

Fresh-eyes takeaways: […]
Fresh-eyes errors: […]

Comparison to P2 highlights:
- [highlight] ↔ [did the cold reader land it? matched / diverged / missed]

**Finding:** [where the intended message failed to land, if anywhere]
```

## Completion gate

Passes when the sub-agent ran blind, its takeaways are compared to the highlights, divergences are stated, and the author confirms the takeaways match their intent (or resubmits to fix what didn't land).
