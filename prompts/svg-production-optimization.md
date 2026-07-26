# SVG Production Optimization

Guidance for designing concepts and prompts that actually survive the
trip from AI-generated image to production-ready SVG. Referenced from
`prompts/prompt-engineering-framework.md` (State 10) and relevant again
at State 12 (Design Review) — see `knowledge/design-quality-review.md`.

---

## 1. Purpose

ESVG-DIS does not create final SVG files — see `SYSTEM_INSTRUCTIONS.md`
§4. But it must still guide users toward designs that can realistically
*become* quality vector products. Good guidance here is the difference
between a design that vectorizes cleanly and one that costs the seller
an hour of manual cleanup.

---

## 2. Why This Matters

AI image generation and SVG production are different disciplines. A
beautiful AI image can still fail as an SVG. Common failure points:
excessive detail, disconnected shapes, poor line structure, impossible
tracing, unclear layers.

```
Design Thinking + Vector Thinking = Better SVG Products
```

Neither alone is enough — a technically clean vector of a boring
concept isn't valuable, and a brilliant concept that can't vectorize
isn't usable.

---

## 3. SVG Design Requirements

**Shape clarity** — recognizable forms, clean boundaries, strong
visual hierarchy.

**Line quality** — prefer consistent strokes, smooth curves, controlled
thickness. Avoid broken lines, random marks, unstable edges.

**Contrast** — black artwork on white background is preferred; high
contrast improves tracing, cutting, and printing all at once.

**Detail management** — premium does not mean maximum detail. Balance
visual richness against production practicality. A design covered in
fine detail may look impressive as a raster image and become an
unusable tangle of paths once traced.

---

## 4. Traceability Requirements

A strong SVG concept allows: easy background removal, clean vector
conversion, separated elements, predictable paths. If a concept
requires guessing where one shape ends and another begins, it will
trace poorly regardless of how good the prompt was.

---

## 5. Cricut / Cutting Machine Considerations

Designs intended for cutting machines should avoid: extremely thin
lines, tiny isolated elements, excessive internal details, fragile
structures — these either fail to cut cleanly or produce pieces too
delicate to handle.

Recommend instead: stronger shapes, larger connected areas, practical
cutting paths.

---

## 6. Human Production Workflow

This is the workflow ESVG-DIS hands off to — the user owns every step
of it:

```
AI Generated Concept
↓
User Review
↓
Vector Conversion
↓
Manual Cleanup
↓
Layer Organization
↓
Export Formats
↓
Final Quality Check
```

---

## 7. Supported Output Formats

The final seller workflow may produce SVG, PNG, JPG, EPS, DXF, or PDF —
exact format depends on customer requirements. ESVG-DIS's job ends at
guiding toward a design that *can* become these formats cleanly, not
producing the files itself.

**Etsy Digital Delivery Policy Note:**
- Etsy instant download allows up to 5 digital files per listing, max 20MB per file.
- If producing multi-format bundles exceeding 20MB, deliver via a PDF download page containing secure cloud storage links (Google Drive / Dropbox).

---

## 8. Production Notes Output

Every final prompt package should include:

```
Production Notes:
Recommended complexity: [Level]
Tracing difficulty: [Low/Medium/High]
Suggested cleanup: [Instructions]
Recommended formats: [List]
```
