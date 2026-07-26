# Scoring Architecture

Three sequential scoring levels, each answering a different question.
IP risk is never one of the scored dimensions at any level — it is
handled exclusively by the gates in `workflow/02-ip-gates.md`. If a
concept reaches a scoring level, it has already passed every IP gate
that precedes it.

```
Level 1 — Opportunity Score   "Should we create something in this market?"
↓
Level 2 — Concept Score       "Which creative direction is strongest?"
↓
Level 3 — Quality Score       "Is this ready for production?"
```

---

## Level 1 — Opportunity Score (State 6)

**Question:** Should we create something in this market at all?

**Dimensions and weights** (original weighting preserved; IP Safety
removed and remaining weights proportionally renormalized — see
rationale below):

```
Market Demand              23.5%
Buyer Appeal               23.5%
Differentiation Potential  23.5%
Production Suitability     11.8%
Trend Strength             11.8%
Competition Difficulty      5.9%
```

**Formula:**

```
Opportunity Score = (
  (Market Demand × 23.5)
+ (Buyer Appeal × 23.5)
+ (Differentiation Potential × 23.5)
+ (Production Suitability × 11.8)
+ (Trend Strength × 11.8)
+ (Competition Difficulty × 5.9)   ← INVERTED: 10=easy market, 1=hard market
) ÷ 100
```

**Why these weights:** Demand, Buyer Appeal, and Differentiation carry
the most weight because they're the strongest indicators of commercial
opportunity. Production and Trend support the decision but influence it
less. Competition Difficulty carries the least weight — high
competition doesn't automatically eliminate an opportunity, it just
raises the bar for differentiation.

**Competition Difficulty** is scored on an **inverted scale**: a
*harder* market gets a *lower* number. Plug the inverted number
directly into the formula above — do not invert it again.
- 10 = virtually no competition, easy entry
- 5 = moderate competition, room to differentiate
- 1 = extremely saturated, dominant sellers, very hard to break in

Don't confuse this with "Competition Opportunity" — that name doesn't
exist; use "Competition Difficulty" everywhere.

**Output:** Proceed, or Reject Opportunity.

**On rejection:** if the opportunity can plausibly be improved, return
to State 2 (Market Research) within its retry limit. If it's
fundamentally weak (not just under-researched), halt as
`HALTED_OPPORTUNITY_FAILURE` — see
`workflow/04-retry-and-halt-logic.md`.

---

## Level 2 — Concept Score (State 9)

**Question:** Which creative direction is strongest?

**Dimensions** (five, unweighted average):

1. **Originality** — uniqueness, differentiation, distance from
   existing marketplace patterns.
2. **Buyer Alignment** — target audience connection, identity
   relevance, purchase motivation.
3. **Emotional Strength** — storytelling, emotional trigger,
   memorability.
4. **Visual Potential** — thumbnail impact, composition strength,
   design attractiveness.
5. **SVG Suitability** — traceability, vector conversion feasibility,
   production practicality.

**Formula:**

```
Concept Score = (Originality + Buyer Alignment + Emotional Strength
                 + Visual Potential + SVG Suitability) ÷ 5
```

**Output:** Selected Concept Direction. Rejected concepts are archived,
not deleted — they may be useful in future research.

> **Note on this model:** earlier drafts of this system had three
> different, incompatible versions of "concept evaluation criteria" in
> circulation. This five-dimension model is the one that superseded all
> of them. Don't reintroduce "Market Appeal," "Commercial Strength," or
> "Market Alignment" as separate criteria here — they're represented by
> Buyer Alignment and Visual Potential above.

---

## Level 3 — Quality Score (State 12)

**Question:** Is this final design direction ready for production?

**Dimensions** (four):

1. Commercial Appeal
2. Visual Quality
3. SVG Suitability
4. Marketplace Differentiation

IP Safety is deliberately **not** one of these. By the time Quality
Score is calculated, the artwork has already passed the Final Artwork
IP Review gate (State 11A). Including IP here again would recreate the
exact gate/score duplication this architecture exists to prevent —
see `workflow/02-ip-gates.md`.

**Output:** Approve, or Revise (return to State 10 — Prompt
Engineering, within retry limits).

---

## How the Levels Connect

```
Low Opportunity Score   → Stop (or halt, see above)
High Opportunity Score  → Generate Concepts

Low Concept Score       → Discard that concept
High Concept Score      → Create Prompt

Low Quality Score       → Improve Direction (back to Prompt Engineering)
```

Each level is a checkpoint, not a re-scoring of the level before it. A
concept doesn't carry its Opportunity Score forward into Concept
Score — different question, different dimensions, independent
evaluation.

---

## Conflict Resolution Rule

If scored dimensions disagree on the strongest option, resolve in this
priority order:

```
1. Production Feasibility
2. Buyer Appeal
3. Differentiation
4. Market Demand
```

**Why this order:** a high-demand idea that can't safely or practically
become a product isn't valuable, so feasibility wins ties.

**IP is never part of this list.** Anything reaching a comparison at
this stage has already passed every applicable IP gate (Keyword
Screening, Concept IP Review, Prompt Validation, Final Artwork
Review) — there's no remaining IP variable to arbitrate. This rule
only governs conflicts among the actual scored dimensions above.
