# Prompt Refinement Guide

Used when generated output doesn't meet quality expectations — at
State 11A (Final Artwork IP Review, if MODIFY) or State 12 (Design
Review, if returning to Prompt Engineering). See
`workflow/04-retry-and-halt-logic.md` for retry limits on these loops.

---

## Diagnose, Don't Just Regenerate

If AI output is weak, don't simply hit regenerate with the same
prompt and hope for a different result. Diagnose *why* it's weak, then
correct the specific cause.

---

## Common Problems and Corrections

**Problem: Too detailed**
```
Reduce micro-details.
Increase silhouette clarity.
Simplify internal shapes.
```

**Problem: Looks generic**
```
Increase storytelling.
Add unique symbolic elements.
Create stronger audience connection.
```
(Cross-reference: `knowledge/ip-risk-and-originality.md` §5, Four
Originality Layers — a "looks generic" result usually means only the
Concept Layer was addressed and the other three weren't.)

**Problem: Hard to trace**
```
Reduce overlapping elements.
Increase closed shapes.
Improve separation between objects.
```

---

## When to Stop Refining and Reconsider the Concept

If the same problem persists after 2-3 refinement attempts, the issue
may not be the prompt at all — it may be that the underlying concept
itself doesn't translate well to the SVG Suitability requirements. In
that case, don't keep refining the prompt indefinitely; consider
returning further upstream to Concept Ranking (State 9) and evaluating
whether a different concept from the portfolio would produce better
results. This is a judgment call, not an automatic rule — but burning
all remaining Design Review retry attempts on a concept that was
always going to be hard to vectorize wastes the retry budget defined
in `workflow/04-retry-and-halt-logic.md`.
