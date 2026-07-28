# Native Etsy SEO & Listing Engine

Used in **State 13 — SEO Handoff & Listing Engine**, the final state of the canonical workflow (`workflow/01-canonical-state-machine.md`).

This module embeds the complete 2026 Etsy SEO listing engine natively into ESVG-DIS (drawing from native frameworks in `integration/etsy-seo-engine/seo-guide.md`, `listing-guide.md`, and `policies.md`). Every product engineered by ESVG-DIS is delivered as a 100% complete, production-ready, fully optimized Etsy listing.

---

## 1. 2026 Etsy Search Engine Optimization Rules

### 📌 A. Title Optimization Rules (`integration/etsy-seo-engine/seo-guide.md`)
- **Maximum Length:** 140 characters.
- **Primary Keyword Front-Loading:** The primary high-intent search phrase MUST appear within the **first 40 characters** (critical for mobile truncated search cards & Etsy algorithm indexing).
- **Structure:** Natural, high-converting long-tail phrases separated by clean pipes (`|`) or slashes (`/`).
- **No Keyword Stuffing:** Avoid repetitive word salads or subjective buzzwords (*beautiful, amazing, perfect*).

### 🏷️ B. 13 Search Tags Rules (`integration/etsy-seo-engine/playbooks/`)
- **Exact Count:** Exactly 13 tags (never leave available tag slots empty).
- **Tag Character Limit:** Every single tag MUST be **≤ 20 characters** (including spaces). Tags >20 chars are silently rejected by Etsy's system.
- **Zero Duplicates:** No repeated tags or redundant phrases across the 13 slots.
- **Tag Indexing Spread:** Combine primary keywords, subculture/niche modifiers, craft machine terms (`cricut file`, `shirt svg`), and recipient/occasion terms.

### 🌐 C. The 5-Surface Indexing Spread Principle
A keyword is indexed most strongly by Etsy's algorithm when the same phrase cluster appears across **5 distinct surfaces**:
1. **Title:** First 40 characters (primary keyword present).
2. **Tags:** At least 3 of the 13 tags contain words from the primary cluster.
3. **Attributes:** At least 1 attribute value echoes a primary-cluster word (Style, Occasion, Recipient).
4. **Description Meta Zone:** First 160 characters include the primary keyword.
5. **Hero Image Alt Text:** Includes the primary keyword.

### 💰 D. Pricing Engine (`integration/etsy-seo-engine/listing-guide.md`)
- **Single SVG Design:** $2.50 – $4.99 (based on visual complexity and buyer appeal).
- **SVG Bundle / Collection:** $5.99 – $12.99 (based on set size and market demand).

---

## 2. Integrated Workflow

```
Market Research (State 2)
↓
IP Screening & Buyer Psychology (States 3-4)
↓
Opportunity Scoring & Saturation Check (States 6-7)
↓
Concept Development & Ranking (States 8-9)
↓
Prompt Engineering & Engine Tuning (State 10)
↓
Design Quality & Vector Review (States 11-12)
↓
Native Etsy SEO Listing Engine (State 13)  ← Complete Title, 13 Tags, Attributes, Description, & Alt Text
```

---

## 3. Mandatory Listing Output Template & Execution Protocol

When State 13 executes, the executing agent MUST NOT output a brief summary or generic text. The agent MUST populate and render the following **exact Markdown structure**:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NATIVE ETSY LISTING PACKAGE — STATE 13
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRIMARY KEYWORD: [Primary Keyword] · difficulty: [Low-Medium / Medium] · ~[N] search results

TITLE:
[Insert 140-character front-loaded title here]

📱 Mobile Preview Card (First 40 chars):
┌───────────────────────────────────────┐
│ [First 40 characters of title]...     │
└───────────────────────────────────────┘
Word count: [X] words (aim 6-12) ✅  ·  Char count: [X] / 140 ✅

TAGS (13/13):
1.  [Tag 1] ([X] chars ✅)
2.  [Tag 2] ([X] chars ✅)
3.  [Tag 3] ([X] chars ✅)
4.  [Tag 4] ([X] chars ✅)
5.  [Tag 5] ([X] chars ✅)
6.  [Tag 6] ([X] chars ✅)
7.  [Tag 7] ([X] chars ✅)
8.  [Tag 8] ([X] chars ✅)
9.  [Tag 9] ([X] chars ✅)
10. [Tag 10] ([X] chars ✅)
11. [Tag 11] ([X] chars ✅)
12. [Tag 12] ([X] chars ✅)
13. [Tag 13] ([X] chars ✅)
*(Verification Check: Exactly 13 tags, 0 duplicates, all ≤20 characters including spaces)*

ATTRIBUTES:
Style: [Value]    Occasion: [Value]    Recipient: [Value]    Category: Craft Supplies & Tools > Canvas & Surfaces > Stencils, Templates & Transfers > Cut Files

DESCRIPTION:
[Meta zone — first 160 chars: "..."] ✅

### 🌟 [Attention-Grabbing Product Hook Title]
[2-3 sentences targeting buyer persona, emotional trigger, and core craft use case]

### 📁 Included File Formats
- **1x SVG File:** Clean, layered vector paths optimized for Cricut & Silhouette cutting.
- **1x PNG File:** High-resolution 300 DPI transparent background (4000x4000px).
- **1x EPS File:** Professional vector graphics editing format.
- **1x DXF File:** Silhouette Studio Basic Edition format.
- **1x PDF File:** Vector print & preview format.

### ✂️ Machine & Software Compatibility
- Cricut Design Space
- Silhouette Studio (Designer & Basic Editions)
- Brother ScanNCut
- Laser Cutters (Glowforge, xTool, Omtech)
- Sublimation Printers & Heat Press software

### 📜 Usage Rights & Commercial License
- **Personal Use:** Unlimited personal crafting & gifts.
- **Commercial Use:** Small Business Commercial License included for up to 500 physical end-products (t-shirts, mugs, totes, decals).
- **Restrictions:** Reselling, sharing, or redistributing digital files in any format is strictly prohibited.

## 🛡️ Etsy 2026 AI Creation Disclosure & Settings
- **About this listing dropdowns:**
  - *Who made it?* **I did**
  - *What is it?* **A finished product or digital file**
  - *When was it made?* **Made to order / Recently made**
- **Factual Description Transparency Note:**
  *"Original vector illustration engineered with AI assistance and hand-curated vector path cleanup per Etsy 2026 Creativity Standards."*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HERO IMAGE ALT TEXT (Etsy + Pinterest):
[100-150 characters containing primary keyword for accessibility & search indexing]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PINTEREST MARKETING BLOCK:
PIN TITLE: [Pin title ≤100 chars]
BOARD NAME: [Board name 25-40 chars]
BOARD DESCRIPTION: [Board description 150-300 chars]
PIN DESCRIPTION: [Pin description 220-232 chars, no hashtags]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INDEXING SPREAD: Title ✅  ·  Tags (3+) ✅  ·  Attributes ✅  ·  Meta Zone ✅  ·  Alt Text ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BEFORE YOU PUBLISH CHECKLIST:
□ Title updated on Etsy (verify mobile preview card)
□ All 13 tags updated (verify all ≤20 chars)
□ Description updated (copy first 160 chars carefully into meta section)
□ Attributes updated (Style / Occasion / Recipient)
□ Hero image alt text updated (includes primary keyword)
□ Category set to Cut Files
□ Save ➔ preview ➔ confirm no tags got truncated
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
