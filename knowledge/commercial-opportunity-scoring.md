# Commercial Opportunity Scoring

Used in **State 6 — Opportunity Scoring** (Level 1 of 3). The formula
and weights are canonical in `workflow/03-scoring-architecture.md` —
this file covers how to actually judge each dimension, with examples.
Don't recompute the formula differently here; if anything below seems
to conflict with that file, that file wins.

---

## 1. Purpose

Evaluate whether a design idea has realistic commercial potential
*before* investing time in creative production. This isn't about
guaranteeing sales — no system can do that — it's about making a
better decision by weighing multiple business factors together instead
of just one.

---

## 2. The Common Mistake

> "This keyword has many searches, so I should create it."

This ignores competition, buyer motivation, originality, IP risk, and
production feasibility. A single strong signal doesn't make an
opportunity — evaluate the complete picture: Demand + Buyer Motivation
+ Market Gap + Differentiation + Production Suitability, weighed
against Competition and Risk.

---

## 3. The Six Dimensions

IP is **not** one of these — it's a gate (State 3), not a score. See
`workflow/02-ip-gates.md`.

### Market Demand
Are customers actively interested? Factors: search interest,
marketplace presence, audience size, niche activity, purchasing
behavior.
- 1-3, Weak: limited audience, unclear buying intent, low activity.
- 4-6, Moderate: some interest, existing buyers, needs strong
  positioning.
- 7-10, Strong: active buyers, passionate audience, proven commercial
  interest.

### Buyer Appeal
Emotional connection and purchase motivation. Does this represent
identity? Solve a need? Is it giftable? Does it connect emotionally?
- "Generic Flower SVG" → 5/10.
- "Grandmother's Garden Memorial SVG" → 9/10. Same subject matter,
  completely different appeal once it's tied to a specific meaning.

### Competition Difficulty
High competition doesn't automatically mean a bad opportunity — it can
mean proven demand. Evaluate: number of competitors, quality of
existing products, seller dominance, uniqueness opportunities.
**Scored inversely: 10 = easy opportunity, 1 = extremely difficult
market.**
- **8 – 10 (Low Competition / Easy Entry):** Few competitors, weak designs.
- **5 – 7 (Moderate Competition):** Active market, room to differentiate.
- **3 – 4 (High Competition):** Heavy competition, dominant sellers.
- **1 – 2 (Extreme Saturation):** Overwhelmed market (triggers Saturation Reality Check).

Don't invert this twice when it flows into the formula — the
formula in `workflow/03-scoring-architecture.md` already expects the
inverted number.

### Differentiation Potential
How easily can this become unique? Factors: available creative angles,
underserved audiences, storytelling possibilities, visual innovation.
- "Funny Dog SVG" → Low.
- "Vintage Adventure Badge Collection for Specific Dog Breeds" → High.

### Trend Strength
- **Evergreen** — pets, family, hobbies, professions. Long-term
  opportunity.
- **Seasonal** — Christmas, Halloween, graduation. Time-dependent.
- **Temporary** — short-lived trends. Requires caution; don't build a
  whole strategy around something that may be gone in weeks.

### Production Suitability
Because the output feeds an SVG workflow: evaluate traceability,
silhouette clarity, layer separation, line quality, conversion
difficulty.
- High score: clear shapes, controlled detail, strong contrast,
  recognizable composition.
- Low score: realistic shading, excessive texture, photographic
  elements, complex gradients — these fight the vectorization process
  downstream (`workflow/01-canonical-state-machine.md`, State 11).

---

## 4. Classification

| Score | Label | Recommendation |
|---|---|---|
| 9.0-10 | Exceptional Opportunity | Proceed |
| 7.5-8.9 | Strong Opportunity | Proceed with refinement |
| 5.5-7.4 | Moderate Opportunity | Improve concept before production |
| Below 5.5 | Weak Opportunity | Explore alternatives (see `workflow/04-retry-and-halt-logic.md` §4 for the improvable-vs-fundamentally-weak judgment call) |

---

## 5. Comparing Multiple Concepts

Comparing concepts against each other happens **after** this stage, at
State 9 (Level 2 — Concept Score), using a different five-dimension
model — not these six. See `workflow/03-scoring-architecture.md` and
`knowledge/concept-development.md`. Don't reuse Opportunity Score
dimensions to rank concepts; they're evaluating different questions.

---

## 6. Human Decision Layer

Scores support decisions — they don't replace judgment. A user may
reasonably choose a lower-scoring concept because of personal
expertise, brand direction, audience knowledge, or creative preference.
Don't present the score as an override of the user's own judgment.

---

## 7. Output: Commercial Opportunity Report

```
Commercial Opportunity Report
1. Opportunity Summary
2. Market Demand
3. Buyer Appeal
4. Competition Analysis
5. Differentiation Potential
6. Production Suitability
7. Final Score
8. Recommendation
```

(IP status is reported separately via the Keyword IP Screening gate
output — not part of this score. See `workflow/02-ip-gates.md`.)

---

## 8. Rules

- Evaluate opportunities before creation.
- Never rely on one metric alone.
- Reward originality.
- Consider buyer psychology.
- Consider production reality.
- Communicate uncertainty rather than presenting scores as guarantees.
