# Worked Examples

## Example 1: Golden Retriever SVG — Complete Pipeline Walkthrough

This example walks every state in the canonical workflow
(`workflow/01-canonical-state-machine.md`) with real scores computed
from the actual formulas in `workflow/03-scoring-architecture.md`, so
you can see how the numbers actually connect end to end.

---

### State 1 — Intake

```
Keyword: Golden Retriever SVG
Goal: Create premium Etsy SVG products
```

### State 2 — Market Research

Strong evergreen demand in the pet niche. Generic pet silhouettes are
highly saturated — most existing listings are simple breed outlines.
Opportunity exists in emotional pet identity rather than literal
depiction.

### State 3 — Keyword IP Screening `[GATE]`

"Golden Retriever" is a breed name, not a protected term.

```
Risk Level: Low
Risk Score: 1/10
Safety Score: 9/10
Decision: PASS
```

### State 4 — Buyer Psychology Analysis

```
Buyer: Dog owners who view pets as family members
Emotional Drivers: Love, pride, connection
Identity Connection: 9/10 | Emotional Strength: 8/10
Gift Potential: 7/10 | Audience Passion: 9/10
Purchase Motivation: 8/10 | Memorability: 8/10
```

### State 5 — Competition Analysis

Saturated with generic silhouettes (dog outline + heart + name text).
Gap: nobody is doing heritage/adventure-badge styling for specific
breeds — most competition is flat and decorative, not narrative.

```
Competition Level: High → Competition Difficulty: 4/10 (inverted scale)
```

### State 6 — Opportunity Scoring

```
Market Demand: 9         × 23.5 = 211.5
Buyer Appeal: 8           × 23.5 = 188.0
Differentiation Potential: 7 × 23.5 = 164.5
Production Suitability: 9 × 11.8 = 106.2
Trend Strength: 9         × 11.8 = 106.2
Competition Difficulty: 4 × 5.9  =  23.6
                                  --------
                          Sum =  800.0 ÷ 100 = 8.0
```

**Opportunity Score: 8.0 → Strong Opportunity → Proceed with
refinement** (see `workflow/03-scoring-architecture.md` §Classification).

### State 7 — Creative Strategy

```
Product Position: Premium vintage golden retriever heritage badge
Theme: Adventure companion
Style: Engraved outdoor emblem
Target Buyer: Dog owners seeking identity-based merchandise, not
              generic pet decor
```

### State 8 — Concept Generation

Two concepts from the portfolio, for comparison:

- **Concept A** — generic dog silhouette + heart + "Golden Retriever"
  text. Matches the saturated pattern identified in State 5.
- **Concept B** — vintage heritage badge: golden retriever rendered as
  an adventure-companion emblem, engraved outdoor styling, symbolic
  elements (compass, trail markings).

### State 8A — Concept IP Review `[GATE]`

Both concepts: no trademarked references, no copied compositions.

```
Decision (both): PASS
```

### State 9 — Concept Evaluation

```
Concept A: Originality 3, Buyer Alignment 5, Emotional Strength 4,
           Visual Potential 5, SVG Suitability 8 → 5.0

Concept B: Originality 9, Buyer Alignment 9, Emotional Strength 9,
           Visual Potential 8, SVG Suitability 9 → 8.8
```

**Concept B selected.** This is exactly the differentiation gap
identified back in State 5 — Concept A would have shipped straight
into the saturated pattern.

### State 10 — Prompt Engineering

```
DESIGN PROMPT:
Create a premium monochrome vintage golden retriever SVG emblem
representing loyalty, adventure, and companionship. Vintage engraving
style, collectible heritage badge composition, symbolic outdoor
elements (compass, trail markings), strong readable silhouette.

[Full technical requirements per prompts/style-templates/vintage.md]

NEGATIVE PROMPT:
[Per prompts/prompt-engineering-framework.md §8]
```

### State 10A — Prompt IP Validation `[GATE]`

No protected references in the prompt text.

```
Decision: PASS
```

### State 11 — User Generation Phase

User generates the artwork externally using the prompt above (see
`prompts/style-templates/vintage.md`), reviews the result, and
proceeds to vectorization.

### State 11A — Final Artwork IP Review `[GATE]`

Generated artwork checked against the same risk categories — no
unintended trademark or copyright issues introduced during generation.

```
Decision: PASS
```

### State 12 — Design Review

```
Commercial Appeal: 9/10
Visual Quality: 8/10
SVG Suitability: 9/10
Marketplace Differentiation: 8/10
Overall: 8.5/10 → Approved
```

### State 13 — SEO Handoff

```
Product Intelligence Package:
- Target Audience: Dog owners, 25-55, identity-driven pet merchandise buyers
- Buyer Persona: Golden retriever owner who sees their dog as family
- Product Positioning: Premium heritage/adventure badge, not generic pet decor
- Emotional Angle: Loyalty, adventure, companionship
- Design Description: Vintage engraved heritage badge emblem
- Keyword Context: Golden Retriever SVG, dog mom SVG, pet memorial adjacent
- Differentiation Points: Narrative/heritage styling vs. saturated
  silhouette+heart+text pattern
```

Handed off to the Etsy SEO System — see
`integration/etsy-seo-handoff.md`.

---

## Example 2: Halloween Witch SVG (Sketch)

```
Input: Halloween Witch SVG
Market: High seasonal demand, very competitive
Common competition: cartoon witches, simple pumpkins, generic text
Opportunity: Premium gothic storytelling

Creative Direction: Dark vintage witchcraft heritage emblem
Avoid: specific characters, franchise references, common Halloween icons
```

This keyword warrants extra attention at State 3 — witch/Halloween
imagery sits close to several franchise properties, so the Keyword IP
Screening gate should be applied carefully even though "Halloween
Witch" itself isn't a protected term. See
`knowledge/ip-risk-and-originality.md` §2 (Franchise Association Risk).

---

## Example 3: Teacher SVG (Sketch)

```
Existing market: thousands of generic teacher designs
Opportunity: move from occupation to personality
Examples: Science Teacher, Literature Teacher, Art Teacher,
          Kindergarten Teacher

Creative Direction: Premium identity badge collection for specific
                     teacher personalities
```

This is the same micro-niche pattern covered in
`knowledge/buyer-psychology.md` §4 — broad occupational keywords are
usually saturated; splitting into specific personas is a repeatable
differentiation move, not unique to this niche.
