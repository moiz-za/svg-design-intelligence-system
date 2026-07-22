# Concept Development

Used in **State 8 — Concept Generation** of the canonical workflow.
Concept Ranking (State 9) uses the scoring model in
`workflow/03-scoring-architecture.md` (Level 2) — summarized again
here with a worked example, but that file is authoritative if anything
conflicts.

---

## 1. Purpose

Convert creative strategy into unique, commercially viable design
concepts. The goal is not generating *many* ideas — it's generating
*better* ideas.

---

## 2. Philosophy

Most AI output fails because it generates obvious ideas, generic
symbols, predictable layouts. Build concepts from: Market Insight +
Buyer Psychology + Originality + Visual Storytelling = Premium Concept.

---

## 3. Process (State 8)

```
Creative Strategy
↓
Concept Exploration
↓
Concept Expansion
↓
Originality Review (informal, within this state)
↓
Production Review (informal, within this state)
↓
→ State 8A: Concept IP Review [GATE]
↓
→ State 9: Concept Ranking
```

The IP gate and formal ranking are separate canonical states, not the
last two steps of this process — see
`workflow/01-canonical-state-machine.md`.

---

## 4. What Each Concept Should Include

- **Core Idea** — what's the main visual story?
- **Symbol System** — what elements communicate meaning?
- **Composition** — how are elements arranged?
- **Buyer Connection** — why will someone care? (This is a descriptive
  question here, not the same thing as the Buyer Alignment *score* in
  Concept Ranking below — answering it well is what earns a high Buyer
  Alignment score.)
- **Differentiation** — why is it not another generic design?

---

## 5. Concept Expansion

A basic idea should be expanded through multiple layers before it's
ready to rank.

- Input: "Coffee SVG"
- Basic concept: "Coffee cup" — this is not enough on its own.
- Expanded concept: "Vintage coffee house emblem combining handcrafted
  coffee symbolism, morning ritual emotion, typography-inspired badge
  structure, and artisan cafe identity."

See `knowledge/ip-risk-and-originality.md` §4-5 for the transformation
method and layering framework this expansion should draw on.

---

## 6. Premium Concept Characteristics

A strong concept has:

- **Recognition** — the buyer understands the idea quickly.
- **Emotional Value** — the buyer feels connected.
- **Visual Memorability** — it stands out in search results.
- **Production Feasibility** — it can become a quality SVG.
- **Originality** — it doesn't resemble common marketplace designs.

---

## 7. Concept Ranking (State 9)

Evaluated using the canonical five-dimension Concept Score model:
Originality, Buyer Alignment, Emotional Strength, Visual Potential,
SVG Suitability. Full formula: `workflow/03-scoring-architecture.md`.

**Example:**

```
Concept A
Originality: 7 | Buyer Alignment: 8 | Emotional Strength: 7
Visual Potential: 8 | SVG Suitability: 9
Overall: 7.8

Concept B
Originality: 10 | Buyer Alignment: 9 | Emotional Strength: 9
Visual Potential: 9 | SVG Suitability: 8
Overall: 9.0
```

Concept B becomes the recommended direction.

Both concepts have already passed Concept IP Review (State 8A) before
reaching this comparison — IP is not one of the ranking dimensions
here, and shouldn't be reintroduced as one. See
`workflow/02-ip-gates.md` for why.

---

## 8. Output: Concept Portfolio

```
Concept Portfolio
For each concept:
- Concept Name
- Design Description
- Buyer Appeal
- Differentiation
- Visual Elements
- Risk Notes
- Production Notes
```

These are descriptive summary fields for presenting the portfolio to
the user — not a second scoring pass. The actual scores live in the
Concept Ranking step above.
