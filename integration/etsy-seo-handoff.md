# Native Etsy SEO & Listing Engine

Used in **State 13 — SEO Handoff & Listing Engine**, the final state of the canonical workflow (`workflow/01-canonical-state-machine.md`).

This module embeds the complete 2026 Etsy SEO listing engine natively into ESVG-DIS (drawing from native frameworks in `integration/etsy-seo-engine/seo-guide.md`, `listing-guide.md`, `policies.md`, and `playbooks/`). Every product engineered by ESVG-DIS is delivered as a 100% complete, production-ready, fully optimized Etsy listing.

---

## 1. The 8 Mandatory Execution Phases

When State 13 executes, the agent MUST run through all 8 execution phases sequentially:

### 📋 Phase 1: Policy & Algorithm Freshness Check
- Verify current Etsy seller policies (`integration/etsy-seo-engine/policies.md`).
- Ensure output complies with August 11, 2026 Etsy Creativity Standards (computerized tool usage disclosure rules).

### 🔍 Phase 2: Keyword Overlap & Cannibalization Prevention
- Read existing keywords from `~/esvg-research/research-log.md`.
- If candidate primary keyword overlaps with a previously created listing in the user's log, issue a **Keyword Overlap Warning** offering 3 pivot choices:
  - `[a]` Pivot to a sibling phrase from Phase 4 research
  - `[b]` Keep phrase anyway (Etsy de-duplication risk)
  - `[c]` Re-keyword previous listing

### 📌 Phase 3: Title Construction & Character Limit Validation
- **Length:** ≤ 140 characters (including spaces).
- **Word Count:** 6 to 12 words (aim under 15 words).
- **Primary Keyword Front-Loading:** Primary search phrase MUST appear within the **first 40 characters**.
- **No Comma-Chain Stuffing:** Natural phrasing separated by clean pipes (`|`) or slashes (`/`).
- **No Subjective Fillers:** Strip buzzwords (*beautiful, amazing, stunning, incredible, perfect*).

### 🏷️ Phase 4: 13 Tags Construction & Character Limit / Duplication Audit
- **Exact Count:** Exactly 13 tags (never leave tag slots blank).
- **Character Limit:** Every tag MUST be **≤ 20 characters** (including spaces). Tags >20 chars are silently rejected by Etsy.
- **Zero Phrase Duplicates:** No exact 2+ word phrase repeats across tags.
- **No Single Word Tags:** Use multi-word long-tail phrases (`softball mom svg`, not `svg`).
- **Verification Audit:** Output the exact character count per tag (`[Tag] ([X] chars ✅)`).

### 📂 Phase 5: Attributes & Category Mapping
- **Category:** `Craft Supplies & Tools > Canvas & Surfaces > Stencils, Templates & Transfers > Cut Files`
- **Attributes:** Style, Occasion, Recipient. At least 1 attribute value MUST echo a word from the primary keyword cluster.

### 📝 Phase 6: Full 8-Block Description & 160-Char Meta Zone
- **Meta Zone (First 160 chars):** Must contain the primary keyword and function as a complete product pitch.
- **Length:** 250 to 700 words.
- **No Generic Openers:** Prohibit "Thank you for visiting" or "This listing is for".
- **Structure:** Opening Hook → Value & Features → Included File Formats (SVG, PNG 300 DPI 4000x4000px, EPS, DXF, PDF) → Instant Delivery → Machine Compatibility (Cricut, Silhouette, Laser, Sublimation) → Usage License (Personal & Small Business Commercial up to 500 items) → Etsy 2026 AI Creation Disclosure → Closing.

### 🖼️ Phase 7: Hero Image Alt Text & Pinterest Marketing Block
- **Hero Alt Text:** 100–150 chars containing primary keyword.
- **Pinterest Block:** Pin title (≤100 chars), Board name (25–40 chars), Board description (150–300 chars), Pin description (220–232 chars, no hashtags).

### 💾 Phase 8: Log Maintenance & Database Sync
- Automatically append/update the listing entry in `~/esvg-research/research-log.md` with: Date, Keyword, Primary Keyword, Title, Tags, Price, Status, and Data Source tag.

---

## 2. The 5-Surface Indexing Spread Principle

A keyword is indexed most strongly by Etsy's algorithm when the same phrase cluster appears across **5 distinct surfaces**:
1. **Title:** First 40 characters (primary keyword present).
2. **Tags:** At least 3 of the 13 tags contain words from the primary cluster.
3. **Attributes:** At least 1 attribute value echoes a primary-cluster word (Style, Occasion, Recipient).
4. **Description Meta Zone:** First 160 characters include the primary keyword.
5. **Hero Image Alt Text:** Includes the primary keyword for accessibility & search indexing.

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
□ Log entry saved to ~/esvg-research/research-log.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
