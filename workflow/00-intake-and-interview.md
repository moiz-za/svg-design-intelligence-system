# 00 — Intake & Interview (State 1: INTAKE)

This is the first state in the canonical workflow (see
`SYSTEM_INSTRUCTIONS.md` §5). Nothing else begins until this stage
produces a Creative Brief.

---

## 1. Why This Stage Exists

A keyword alone is not enough to start research. "Dog SVG" tells you
nothing about who's buying, why, or what they're buying it for. Before
any research, scoring, or concept work begins, the agent needs to
understand:

- who the buyer is
- why they would purchase
- what product category is targeted
- what design direction is appropriate

Do not skip straight to concept generation from a bare keyword.

---

## 2. Collection Philosophy

Collect information progressively, not all at once:

```
Initial User Request
↓
Required Information Check
↓
Missing Information Questions (only if needed)
↓
Research Context Established
↓
Analysis Begins (State 2: Market Research)
```

Don't overwhelm a new seller with every possible question. Match the
depth of the interview to the complexity of what they've already given
you.

---

## 3. Required Inputs

### 3.1 Primary Keyword / Product Idea
The starting point, not the final design — e.g. "Golden Retriever SVG,"
"Halloween Witch SVG," "Teacher Appreciation SVG." Treat the keyword as
something to evaluate for viability, not something to accept at face
value.

### 3.2 Target Marketplace
Default: **Etsy**. Other options if stated: Creative Market, Design
Bundles, So Fontsy, personal website, other digital marketplaces.
Marketplace affects customer expectations, competition, pricing, and
positioning.

### 3.3 Target Customer
Who the product is for — e.g. "women 25-45 who love dogs," "teachers
buying classroom products," "gift buyers." If the user doesn't know,
infer likely buyers through research rather than blocking on this
question.

### 3.4 Product Type
What's actually being made — single SVG, SVG bundle, PNG download,
Cricut design, laser-cutting file, t-shirt design, sticker design,
print-on-demand artwork. Different product types drive different
creative decisions downstream.

### 3.5 Design Style Preference (optional)
Vintage, minimalist, luxury, hand-drawn, retro, cartoon, engraving,
badge, boho, dark gothic, watercolor-inspired, etc. If not given,
recommend a style based on market analysis rather than asking.

### 3.6 Complexity Level
Simple, medium, detailed, or premium/collector style. Default
recommendation for Etsy SVG products is **medium to premium** — highly
generic simple icons face extreme competition. (Premium does not mean
maximum detail — see `knowledge/design-quality-review.md`.)

### 3.7 Intended Use Case
Cricut cutting, Silhouette cutting, t-shirt printing, mug printing,
sticker creation, home decor, digital download. This directly affects
prompt engineering later.

---

## 4. Optional Advanced Inputs

For experienced sellers who volunteer more context:

- **Competitor examples** (links, screenshots, existing listings) —
  used only for market understanding and differentiation analysis,
  **never for copying.**
- **Existing shop information** — niche, current audience, previous
  winners/failures, for consistency.
- **Brand direction** — e.g. "premium handmade feel," "funny designs,"
  "minimal aesthetic."
- **Seasonal intent** — Christmas, Halloween, Valentine's Day, Mother's
  Day, evergreen. Affects timing and competition.

---

## 5. Two Interview Modes

### Minimum Input Mode (beginners)
Required only: Keyword, Audience, Product. The agent fills the rest
through research.

```
User: Create a dog SVG

Agent: Before creating concepts, I'll analyze:
- dog niche demand
- popular buyer segments
- competition
- opportunities for differentiation

I need to determine the strongest direction first.
```

### Advanced Research Mode (experienced sellers)

```
Keyword: Golden Retriever SVG
Audience: Dog moms
Product: Cricut SVG Bundle
Market: USA Etsy
Goal: Premium emotional designs
Style: Vintage engraving
Competitor Examples: Provided
```

More upfront detail → deeper, faster downstream analysis. Don't force
a beginner into this mode, and don't withhold it from a seller who
volunteers it.

---

## 6. Input Validation Checklist

Before moving to State 2 (Market Research), confirm:

- **Commercial clarity** — does the keyword represent a purchasable
  product?
- **Audience clarity** — is there an identifiable buyer, stated or
  inferable?
- **Product clarity** — is the intended output format understood?
- **Preliminary risk awareness** — does the keyword show an *obvious*
  IP concern on its face (e.g. a named franchise, a trademarked
  character)?

> **Important:** the check above is a lightweight sanity check only —
> it is not the formal IP gate. The actual Keyword IP Screening gate is
> State 3, runs after Market Research, and is defined in
> `workflow/02-ip-gates.md`. Don't treat a clean pass here as IP
> clearance; it only means there's no glaring red flag blocking you
> from starting research at all.

If required information is missing, ask targeted questions — don't
guess silently on something the user could just tell you.

---

## 7. Expand Into a Creative Brief

Once inputs are gathered, expand them into an internal Creative Brief.
This is the artifact every later stage consumes — later stages should
not re-derive this from scratch.

**Example**

User input: `Camping SVG`

Expanded brief:

```
Market: Etsy Digital Downloads
Audience: Outdoor enthusiasts, campers, gift buyers
Purchase Motivation: Identity expression and hobby connection
Opportunity: Premium vintage outdoor badge designs
Production: Black and white vector-friendly artwork
Preliminary Risk Note: Avoid existing camping brands and logos
                        (formal screening happens at State 3)
```

---

## 8. Output of This Stage

```
ESVG-DIS Creative Brief

Contains:
- Product Intent
- Target Customer
- Market Context
- Buyer Motivation
- Production Requirements
- Research Direction
- Preliminary Risk Notes (not a substitute for the State 3 gate)
```

This brief is the foundation for every stage that follows. Proceed to
State 2 (Market Research) — see `knowledge/market-intelligence.md`.
