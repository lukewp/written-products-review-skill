# Review 7: Packaging

*Derived from the checklist's "Seventh Review: Packaging."*

Format-level checks on the delivered artifact. Where the document format allows inspection (docx, pdf, pptx), inspect it. Where you have only text, assess what you can and flag the rest as items the author must verify in the source file.

## Completion criteria — assess each

- [ ] **Web-safe fonts.** All fonts used are generally available (email/web-safe). A font the reader's device can't render breaks the layout.
- [ ] **Font consistency.** Header and body fonts, if different, are consistent and intentional throughout — not an accident of copy-paste.
- [ ] **Image resolution.** Included images are at a resolution appropriate for the layout — not pixelated, not bloating the file.
- [ ] **Links work.** Embedded links are clickable and verified (they resolve to what they claim).
- [ ] **Page numbers.** Page numbers exist.

## How to run it

For a text-only review, you cannot see fonts or rendered images — say so, and convert those items into a checklist the author runs against the source file. For an inspectable format, check directly (e.g., verify links resolve, confirm page numbers are present).

## Stage output — Packaging validation

```
## Review 7 — Packaging

- Web-safe fonts: [verified / author to confirm in source]
- Font consistency: […]
- Image resolution: […]
- Links verified: [list checked + result, or author to verify]
- Page numbers: [present / missing]

**To fix:** […]
**Author must verify in source file:** [items not inspectable from text]
```

## Completion gate

Passes when each item is assessed or explicitly handed to the author to verify in the source, fixes are listed, and the author confirms: proceed to Stage 8, or resubmit.
