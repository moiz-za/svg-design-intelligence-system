# Market Intelligence

Used in **State 2 — Market Research** of the canonical workflow. See
`workflow/01-canonical-state-machine.md` for where this fits.

> **Scope note:** this file covers keyword analysis, demand, trends,
> and market gaps — everything that belongs specifically to State 2.
> Buyer psychology is its own state and file
> (`knowledge/buyer-psychology.md`, State 4). Competition analysis is
> its own state and file (`knowledge/competition-intelligence.md`,
> State 5). Opportunity scoring happens after both of those, in State 6
> (`workflow/03-scoring-architecture.md`). Don't treat this file as
> covering all of market research end-to-end — it's one state among
> several.

---

## 1. Purpose

Before any creative work begins, understand:

- designs customers are likely to purchase
- niches with realistic commercial opportunity
- underserved market segments
- opportunities for differentiation

A successful Etsy SVG product requires: **Demand + Buyer Intent +
Competitive Opportunity + Creative Differentiation + Production
Feasibility.** This file covers the first and last of those five most
directly; the others are covered in the files noted above.

---

## 2. Philosophy

Most sellers start with "what design can I create?" Start instead with:

> What problem, identity, emotion, or desire causes someone to
> purchase this product?

Understand the market before suggesting creative directions.

---

## 3. State 2 Process

```
Check Research Log (state-templates/esvg-research/research-log.md)
↓ — if this niche was already researched, see §3.1 before continuing
Keyword Analysis
↓
Attempt Live Search (§3.2) — falls back to reasoning if unavailable
↓
Market Demand Assessment
↓
Trend Analysis
↓
Market Gap Identification
↓
→ hand off to State 3 (Keyword IP Screening)
```

### 3.1 Check the Research Log First

Before starting fresh research, check
`state-templates/esvg-research/research-log.md` for the same or a
closely related keyword. If a prior entry exists:

- Show the user the prior result (date, score, top concept selected)
  and ask whether they want fresh research (markets change, and a
  prior reasoning-only estimate may be worth redoing with live search)
  or to build on the prior pass.
- Regardless of which they choose, never re-suggest a concept listed
  in that niche's "IP-Blocked Concepts" column.
- If proceeding, append a new row to the log rather than overwriting
  the old one — a niche can legitimately be researched more than once
  over time.

If no prior entry exists, or this tool/session has no access to the
log (stateless free-tier use), proceed directly to Keyword Analysis.

### 3.2 Dual-Mode Research: Live Search vs. Reasoning Estimate

**This is the most important addition in this file.** Wherever this
framework calls for demand, trend, or gap analysis, attempt it in this
order:

**Live mode (preferred):** if a search/browsing tool is available,
search Etsy directly for the keyword and closely related terms. Read
actual current listings — what exists, how many, what themes repeat,
what's actually being sold right now. Ground demand and trend
assessments in what's really there, not in training-data assumptions
about what's probably popular.

**Reasoning mode (fallback):** if no search tool is available (e.g.
free ChatGPT without browsing enabled, or this document pasted into a
plain-text context with no tools), or live search returns nothing
useful for an obscure niche, fall back to reasoning-based analysis —
the same qualitative judgment this framework has always used.

**Always label which mode produced the output.** Every Market
Intelligence Report (§8) and every scoring example (§9) must carry a
`Data Source` tag:

```
Data Source: Live Etsy Search
```
or
```
Data Source: Reasoning-Based Estimate (live search unavailable —
treat demand/trend figures as directional, not verified)
```

Never present a reasoning-based estimate with the same apparent
confidence as a live-search-grounded one. This is the same honesty
principle already applied to IP risk assessments
(`workflow/02-ip-gates.md` §9) and commercial scores
(`knowledge/commercial-opportunity-scoring.md` §6) — a number without
a stated confidence level is misleading by omission.

---

## 4. Keyword Intelligence

Analyze the provided keyword from multiple angles.

**Search meaning** — what is the buyer actually searching for? Is the
keyword product-focused or inspiration-focused? Are they looking for a
finished product or a design file?

Example: "Dog SVG" could mean dog-lover merchandise, a pet memorial
product, a breed-specific design, a Cricut project, printable artwork,
or a gift product. Don't assume — the rest of research should narrow
this down.

**Keyword intent classification:**

- **Commercial intent** — buyer likely wants to purchase. E.g. "Golden
  Retriever Mom SVG," "Teacher Shirt SVG," "Halloween Cricut Bundle."
- **Informational intent** — buyer is researching. E.g. "How to make
  SVG," "SVG tutorial."
- **Inspirational intent** — buyer is looking for ideas. E.g. "Cute
  dog designs," "Camping ideas."

Commercial-intent keywords receive higher opportunity scores.

---

## 5. Demand Analysis

**Buyer interest** — are people actively searching for this topic?
Does the niche have passionate buyers? Does the audience identify
strongly with the theme?

**Emotional connection** — higher purchase probability often exists
when products represent identity, hobbies, professions, family, pets,
beliefs, or communities.

- Weak: "Dog Image SVG"
- Stronger: "Golden Retriever Mom Pride Design" — connects to identity,
  not just subject matter.

**Purchase motivation** — identify the likely reason for purchase:

- Self-expression — "I want something representing me."
- Gift purchase — "I want something meaningful for someone."
- Project need — "I need a design for my craft project."
- Seasonal purchase — "I need this for an event or holiday."

---

## 6. Trend Analysis

Classify the opportunity as:

- **Evergreen** — consistent year-round demand (pets, professions,
  hobbies, family, motivational themes).
- **Seasonal** — high demand during specific periods (Halloween,
  Christmas, Valentine's Day, Graduation).
- **Short-term trend** — temporary popularity (viral memes, internet
  trends, temporary events).

**Trend evaluation rule:** don't blindly follow trends. Evaluate a
trend by Trend Popularity + Commercial Intent + Longevity + Design
Opportunity. A viral topic can still be a poor commercial direction if
it lacks longevity or a clear design angle — and separately, if it
carries IP risk, that gets caught at the Keyword IP Screening gate
(State 3), not folded into this evaluation. IP is never a scored term
in any formula in this system — see `workflow/02-ip-gates.md`.

---

## 7. Market Gap Identification

The most valuable output of this research: **Existing Demand + Customer
Need − Available Quality Solutions = Market Opportunity.**

Examples:
- Existing market: generic teacher SVGs → Gap: premium classroom
  identity badges designed for specific teaching personalities.
- Existing market: dog breed SVGs → Gap: emotional memorial designs
  combining breed identity with storytelling elements.

---

## 8. Output: Market Intelligence Report

```
Market Intelligence Report
1. Keyword Analysis
2. Buyer Intent
3. Demand Assessment
4. Trend Classification
5. Market Gaps
6. Recommended Direction
7. Preliminary Risk Notes (informational only — not the formal
   gate; see workflow/00-intake-and-interview.md §6)
8. Data Source: [Live Etsy Search / Reasoning-Based Estimate]
```

(Competition Level is added to this report after State 5 completes —
see `knowledge/competition-intelligence.md`.)

---

## 9. Preliminary Scoring Example

```
Demand: 8/10
Trend: 9/10
Differentiation Opportunity: 9/10
Data Source: Live Etsy Search
```

These are informal, directional numbers used during State 2 — not the
formal Level 1 Opportunity Score, which is calculated in State 6 after
Buyer Psychology and Competition are also known. See
`workflow/03-scoring-architecture.md` for that formula. IP risk is
never part of either figure — it's reported separately by the gate.

Scores are guidance, not guarantees.

---

## 10. Worked Example

**Input:** `Camping SVG`

**Output:**

> The camping SVG category has strong evergreen demand but high
> saturation. Most existing designs rely on basic outdoor icons.
> Opportunity exists in premium storytelling designs targeting
> experienced campers, outdoor families, and adventure gift buyers.
> Recommended direction: collectible vintage expedition-style designs
> with unique narratives rather than generic camping icons.

---

## 11. Rules

- Research before creating.
- Check the research log before starting from scratch on a niche.
- Prefer live search over reasoning-only estimates; always label which
  one actually produced the output.
- Identify buyers before designing (State 4 does this in depth).
- Search for opportunities before generating ideas.
- Never copy successful listings — study *why* they work, not *what*
  they look like.
- Prioritize differentiation over imitation.
