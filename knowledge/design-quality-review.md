# Design Quality Review

Used in **State 12 — Design Review** (Level 3 of 3), after the Final
Artwork IP Review gate (State 11A) and before SEO Handoff. See
`workflow/01-canonical-state-machine.md` and
`workflow/03-scoring-architecture.md`.

---

## 1. Purpose

A final evaluation before a seller invests time producing and
publishing a product. The purpose is to prevent weak designs from
entering production — this is the last checkpoint, not a formality.

---

## 2. Philosophy

The question is not "is this image beautiful?" It's "is this a
commercially valuable SVG product?" A striking image that can't be
cleanly vectorized, or that doesn't differentiate in a thumbnail grid,
fails this review regardless of how good it looks in isolation.

---

## 3. The Four Dimensions

```
1. Commercial Appeal
2. Visual Quality
3. SVG Suitability
4. Marketplace Differentiation
```

**Why only four, and why not Originality or IP:**

- **Originality** and **Buyer Alignment** are already scored at Concept
  Score (Level 2, State 9). Re-scoring them here would duplicate that
  evaluation instead of measuring what Level 3 actually exists to
  measure: production-readiness of the *finished artwork*.
- **IP** is not scored here either. The finished artwork passes through
  a dedicated Final Artwork IP Review gate (State 11A) before this
  review even begins — see `workflow/02-ip-gates.md`. That gate exists
  precisely because generated art can introduce IP risk that wasn't
  present in the approved prompt; Design Review assumes that's already
  been cleared.

### Commercial Appeal Review
- Would a buyer understand the product immediately?
- Does it target a clear audience?
- Does it create purchase motivation?

### Visual Quality Review
- Is composition balanced?
- Is the focal point clear?
- Does it look professional?

(Originality itself was already evaluated at Concept Score. This
checks whether the finished artwork executed that original concept
well *visually* — it's a different question from "is the idea
original," and doesn't re-score that.)

### SVG Review
- Can this reasonably become a clean vector?
- Are shapes clear?
- Are details manageable?

### Marketplace Review
- Does it stand out in thumbnails?
- Does it offer something different?
- Is positioning clear?

---

## 4. Final Design Score

```
Commercial Appeal: 9/10
Visual Quality: 8/10
SVG Suitability: 8/10
Marketplace Differentiation: 9/10
Overall: 8.5/10
```

IP is already confirmed safe at State 11A before this score is
calculated — it's not one of the four inputs above.

---

## 5. Output: Design Quality Report

```
Design Quality Report
1. Strengths
2. Weaknesses
3. Improvement Suggestions
4. Production Concerns
5. Final Recommendation
```

**On failure:** return to State 10 (Prompt Engineering), within the
retry limit defined in `workflow/04-retry-and-halt-logic.md`. This
usually means the prompt needs refinement, not that the concept itself
was wrong — the concept already passed Level 2 to get here.
