# Playbook — Cutting Machine Complexity Thresholds

**Purpose:** turn the qualitative guidance in
`../prompts/svg-production-optimization.md` §3 and §5 ("premium does
not mean maximum detail," "avoid tiny isolated elements") into concrete,
checkable thresholds a prompt or generated concept can actually be
evaluated against.

**Where it's used:** during Prompt Engineering (State 10) when writing
SVG technical requirements, and during Design Review (State 12) when
evaluating SVG Suitability.

---

## Why concrete thresholds, not just "keep it simple"

"Avoid excessive detail" is true but not checkable — two people will
disagree on what counts as excessive. These thresholds give a specific
line to check a concept or generated image against.

---

## Cutting Machine Compatibility Checklist

Run through this list. Each **fail** should lower the SVG Suitability
component of Concept Score or Quality Score
(`../workflow/03-scoring-architecture.md`) rather than being treated as
a separate blocker — production difficulty is a scoring input, not a
gate.

### Minimum feature size
- **Pass:** the smallest individual detail in the design (a line, a
  gap between shapes, a small internal element) is proportionally no
  smaller than roughly 1/40th of the design's overall width.
- **Fail:** fine details that would require a blade or laser to
  resolve features smaller than that — these tend to tear, fuse, or
  disappear when actually cut.
- **Concrete example:** a design meant to be cut at 4 inches wide
  shouldn't rely on details finer than roughly 1/10 inch to read
  correctly.

### Isolated/floating elements
- **Pass:** every visual element connects to the main body of the
  design, or is large enough to survive as an independent cut piece
  (roughly larger than a fingernail at final intended size).
- **Fail:** small dots, thin isolated lines, or tiny separate shapes
  with no connection to anything else — these are the single most
  common cause of "why did my cut fall apart" complaints.

### Line weight consistency
- **Pass:** line thickness varies by no more than roughly 3x across
  the design (e.g. thinnest line isn't dramatically thinner than the
  thickest).
- **Fail:** a design that mixes bold thick outlines with hairline
  fine details in the same composition — the thin parts fail before
  the thick parts finish cutting cleanly.

### Internal detail density
- **Pass:** internal detail (texture, patterning, fine linework)
  occupies less than roughly half of the design's total visual area,
  with the rest being clean, connected shapes.
- **Fail:** a design where the majority of the visual interest comes
  from fine internal texture rather than the overall silhouette —
  this is the "beautiful as a picture, unusable as a cut file" failure
  mode described in `../prompts/svg-production-optimization.md` §2.

### Path/shape closure
- **Pass:** every shape reads as closed (a complete outline, no gaps).
- **Fail:** open or ambiguous outlines that require guessing where a
  shape's boundary actually is — this fails at the vectorization step
  (the user's own manual process, per
  `../prompts/svg-production-optimization.md` §6), not something this
  system fixes automatically.

---

## Complexity Level → Recommended Product Type

Use this to sanity-check a complexity recommendation against the
stated use case from Intake (`../workflow/00-intake-and-interview.md`
§3.7).

| Complexity Level | Cutting machine (Cricut/Silhouette) | Laser cutting | Print-only (no cutting) |
|---|---|---|---|
| Simple | ✅ Ideal | ✅ Ideal | ✅ Fine, but likely under-differentiated (see `niche-saturation-reality-check.md`) |
| Medium | ✅ Good, standard recommendation | ✅ Good | ✅ Good |
| Detailed | ⚠️ Check against the checklist above carefully | ✅ Generally fine — laser tolerances differ from blade cutting | ✅ No cutting constraints apply |
| Premium/collector | ⚠️ Often too fine for reliable cutting — flag to the user | ⚠️ Check checklist | ✅ No cutting constraints apply |

**If the use case is "printing only" (no cutting machine at all):**
skip this entire playbook — none of these thresholds apply. Confirm
the use case from Intake before applying cutting-machine constraints
to a print-only product.

---

## What to say when a concept fails this checklist

Don't just say "too complex." Name the specific failure and the
specific fix:

```
This concept as described would likely have production issues on a
cutting machine: [specific failing item, e.g. "the internal texture
detail on the fur takes up most of the visual area, which usually
tears when actually cut"].

Suggested fix: [specific change, e.g. "simplify to a flat silhouette
with 2-3 defining internal lines rather than full texture rendering"].

This doesn't affect the SVG Suitability score if the product is meant
for printing only rather than cutting — let me know if that's the
case.
```
