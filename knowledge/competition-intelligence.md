# Competition Intelligence

Used in **State 5 — Competition Analysis** of the canonical workflow,
after Buyer Psychology (State 4) and before Opportunity Scoring
(State 6). See `workflow/01-canonical-state-machine.md`.

---

## 1. Purpose

Analyze existing marketplace competition to find opportunities for
differentiated SVG products. The purpose is **not** to copy successful
designs — it's to understand why certain designs perform well, what
customers respond to, where competitors are weak, and how to build a
genuinely stronger alternative.

Competition research provides strategic insight. It is not a blueprint
for imitation.

---

## 2. Philosophy

The common mistake: "find a bestseller and make something similar."
This fills the marketplace with repeated concepts, identical
compositions, generic artwork, and declining differentiation for
everyone, including the copier.

The better sequence:

```
Observe Market Success
↓
Understand Customer Attraction
↓
Identify Missing Value
↓
Create New Interpretation
↓
Develop Original Design Direction
```

---

## 3. Five Research Questions

1. **What designs already exist?** Common themes, popular styles,
   repeated layouts, frequently used symbols.
2. **Why do customers purchase them?** Emotional appeal, identity
   connection, gifting potential, visual attractiveness.
3. **What makes them successful?** Strong thumbnail, clear message,
   niche targeting, recognizable style, customer relevance.
4. **Where are competitors weak?** Generic concepts, poor originality,
   outdated styles, weak storytelling, limited audience targeting.
5. **How can a new product be meaningfully different?** The answer
   becomes the creative opportunity.

---

## 4. Live Research (Preferred) with Reasoning Fallback

**This is the most important addition to this file.** Competition
analysis is only as good as the evidence behind it — don't rely on
training-data assumptions about what's "probably" saturated when real,
current data is available.

**Live mode (preferred):** if a search/browsing tool is available,
search Etsy directly for the keyword and its close variants. Read the
actual current top listings — not to copy them, but to extract real
patterns:

- What subject matter, styles, and compositions actually repeat across
  the current top results?
- Roughly how many listings compete for this term right now?
- What do current listing titles/descriptions emphasize?
- What do actual customer reviews (if visible) say is missing or
  disappointing?

This is the same live-evidence principle used in
`knowledge/market-intelligence.md` §3.2, applied here to visual/
thematic pattern extraction rather than keyword/demand data. Never
require copying anything found this way — analyze it, don't reproduce
it. See §9, Avoiding Competitive Copying.

### 4. Three-Tier Data Source Model: Live (Full) vs. Live (Partial) vs. Reasoning

Carry the exact same 3-tier Data Source model used in Market Intelligence through to the Competition Intelligence Report (§12) and scoring:

1. **Live Etsy Search (Full):** search tool returned rich, structured competitor listings and active sales signals.
2. **Live Etsy Search (Partial / Thin Data):** live search ran, but returned sparse or thin competitor results (common in obscure long-tail queries). Treat competition and saturation signals as directional/qualitative rather than fully verified proof.
3. **Reasoning-Based Estimate (Fallback):** no search tool available or live search failed. Fall back to qualitative reasoning using general knowledge.

Every Competition Intelligence Report (§12) must carry one of these tags:

```
Data Source: Live Etsy Search (Full)
```
or
```
Data Source: Live Etsy Search (Partial / Thin Data — treat signals as directional)
```
or
```
Data Source: Reasoning-Based Estimate (live search unavailable — directional estimate)
```

---

## 5. Competitor Analysis Dimensions

**Visual analysis** — subject matter, composition, style, complexity
(detail level, visual richness, uniqueness, production difficulty).

**Commercial analysis** — positioning (e.g. "Generic Dog SVG" vs.
"Golden Retriever Mom Emotional Gift SVG"), target buyer (who, why,
what emotion drives it), product opportunity (single design, bundle,
personalization).

**Customer feedback analysis** — reviews reveal real information.
Positive signals ("beautiful design," "exactly what I wanted") show
what to preserve. Negative signals (difficult to cut, poor quality,
missing formats, too generic) show exactly where the gap is. A cluster
of "too many similar designs" complaints is a direct signal to
prioritize originality.

---

## 6. Pattern Detection

**Overused pattern example** (camping niche): animal silhouette +
heart + name text → high saturation, low differentiation.

**Opportunity pattern example**: animal identity + storytelling element
+ unique symbolic composition + premium illustration style → higher
perceived value.

---

## 7. Gap Analysis

Example:

```
Market: Teacher SVG
Current Competition: basic teacher quotes, apple icons, classroom symbols
Weakness: most designs target "all teachers" generically
Opportunity: personality-based teacher identity collections
             (science teacher, literature teacher, art teacher,
             kindergarten teacher) with premium badge compositions
```

---

## 8. Differentiation Matrix

| Element | Typical Competitors | Opportunity |
|---|---|---|
| Concept | Generic | Unique storytelling |
| Style | Common | Premium visual language |
| Audience | Broad | Micro-niche targeting |
| Composition | Simple | Advanced composition |
| Emotion | Low | Strong identity connection |
| Production | Basic | SVG-aware design |

---

## 9. Avoiding Competitive Copying

**Do:** analyze patterns, understand demand, identify gaps, create new
concepts.

**Do not:** reproduce layouts, recreate artwork, copy phrases, imitate
unique styles, or modify existing designs slightly and call it new.

---

## 10. Competition Level (Qualitative)

```
Low:     Few sellers, clear opportunity
Medium:  Demand exists, differentiation required
High:    Many sellers, strong uniqueness required
Extreme: Dominated by a small number of major established sellers,
         leaving little room for a new independent listing to compete
```

**Converting to the Level 1 formula:** Opportunity Score
(`workflow/03-scoring-architecture.md`) needs a numeric **Competition
Difficulty** score, 1-10, where higher = *easier* (this is inverted —
see that file's note on why). Unified scale mapping across the system:
- **Low Competition (Easy Entry):** 8 – 10
- **Moderate Competition (Balanced):** 5 – 7
- **High Competition (Saturated):** 3 – 4
- **Extreme Saturation (Hard Entry):** 1 – 2 (triggers Saturation Reality Check per `playbooks/niche-saturation-reality-check.md`)

---

## 11. Competitive Opportunity Formula (State 5, informal read)

```
Market Demand
+ Customer Interest
+ Competitor Weakness
+ Originality Potential
− Saturation
= Opportunity Potential
```

This is a directional read during competition analysis, not the formal
Level 1 Opportunity Score (which uses different, weighted inputs — see
`workflow/03-scoring-architecture.md`). IP risk is not a term in this
formula either; it's evaluated separately by the Keyword IP Screening
gate — see `workflow/02-ip-gates.md`.

---

## 12. Output: Competition Intelligence Report

```
Competition Intelligence Report
1. Current Market Landscape
2. Common Design Patterns
3. Successful Elements
4. Overused Elements
5. Customer Expectations
6. Market Weaknesses
7. Differentiation Opportunities
8. Recommended Creative Direction
9. Data Source: [Live Etsy Search / Reasoning-Based Estimate]
```

---

## 13. Rules

- Study competitors strategically, not for imitation.
- Prefer live search over reasoning-only estimates; always label which
  one actually produced the analysis.
- Avoid derivative designs.
- Prioritize originality.
- Search for underserved audiences.
- Create improvements rather than duplicates.
