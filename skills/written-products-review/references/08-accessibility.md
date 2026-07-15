# Review 8: Accessibility

*Derived from the checklist's "Eighth Review: Accessibility."*

A product that excludes readers who use assistive technology is a product that fails those readers entirely. These checks are mechanical and non-negotiable.

## Completion criteria — assess each

- [ ] **Alt text on images.** Every image has alt text describing it.
- [ ] **Real header tags.** Document section headers use a header tag (H1/H2/…), not merely a larger or bold font. A screen reader navigates by header tags; visually-large text it cannot see.
- [ ] **Table header tags.** Tables have a header tag on the header-row elements, so assistive tech announces column/row headers.
- [ ] **Chart accessibility.** Chart images are alt-tagged, **and** the title and description appear inline in the document text — not baked into the image where a screen reader can't reach them.

## How to run it

For an inspectable format, check the actual tags. For text-only, assess what's present in the markup and convert the rest into author-verification items. Where alt text is missing, it is not enough to say "add alt text" — where you can, draft the alt text as a **current/potential** suggestion the author can drop in.

## Stage output — Accessibility audit

```
## Review 8 — Accessibility

- Alt text on images: [n of m have it — which are missing]
  Suggested alt text: [image → draft alt text]
- Header tags (not just large font): [pass / fail — which headers are fake]
- Table header tags: [pass / fail]
- Chart title/description inline (not in image): [pass / fail]

**To fix:** […]
```

## Completion gate

Passes when each item is assessed, missing alt text is drafted where possible, fixes are listed, and the author confirms: proceed to Stage 9 (if a deck) or Stage 10 (if publishing) or finish, or resubmit.
