# Native Etsy SEO & Listing Engine

Used in **State 13 — SEO Handoff & Listing Engine**, the final state of the canonical workflow (`workflow/01-canonical-state-machine.md`).

This module embeds the complete 2026 Etsy SEO listing engine natively into ESVG-DIS (drawing from native frameworks in `integration/etsy-seo-engine/seo-guide.md`, `listing-guide.md`, `policies.md`, and `playbooks/`). Every product engineered by ESVG-DIS is delivered as a 100% complete, production-ready, fully optimized Etsy listing.

---

## 0. Gate 0 — AI & Image Compliance (mandatory)

Before Phase 1, run `integration/etsy-seo-engine/playbooks/ai-image-compliance.md` against the item, content type, and image plan. The result outranks SEO: a non-compliant listing can be removed however well it ranks.

| Result | Action |
|---|---|
| `⛔ BLOCKED` | Do **not** output the listing package. Explain the rule, cite the source, offer the compliant alternative. |
| `⚠️ ACTION REQUIRED` | Output the package, but prepend the missing item to the pre-publish checklist. |
| `✅ PASS` | Print the compliance block once (item origin, content type, image plan, disclosure, gate). |

Non-negotiable: digital downloads need a **real preview or excerpt of the actual files**; physical, customised, and pattern/recipe products need **at least one real unedited photo**; AI imagery can never be the only image of a finished result; bot-generated listings and AI-authored functional instructions are prohibited.

---

## 1. The 8 Mandatory Execution Phases

When State 13 executes, the agent MUST run through all 8 execution phases sequentially, strictly following `integration/etsy-seo-engine/listing-guide.md`:

### 📋 Phase 1: Policy & Algorithm Freshness Check & Automated Sync
- Verify current Etsy seller policies (`integration/etsy-seo-engine/policies.md`) against the **22 October 2026** baseline — Creativity Standards, Listing Image Requirements, and the AI-use announcement.
- Ensure output complies with the 22 October 2026 AI and listing-image rules and the August 11, 2026 computerized-tool originality rules.
- **Portable / Web Mode:** When web browsing is enabled, execute a live web search for `"Etsy seller policies 2026"` / `"Etsy listing image requirements"` / `"Etsy AI policy"` to verify active marketplace rules before generating the listing package. Apply any newly detected policy rules directly to the output.
- **Full System / CLI Mode:** Run `python3 scripts/sync_etsy_policy.py --from-seller` to pull policy and engine rulebooks one-way from the standalone Etsy Seller SEO System (`skill/references/`) into ESVG-DIS (`integration/etsy-seo-engine/`). Direction matters: the seller repo is the policy source of truth — never overwrite newer seller files with stale local copies.

### 🔍 Phase 2: Keyword Overlap & Cannibalization Prevention
- Read existing keywords from `~/esvg-research/research-log.md`.
- If candidate primary keyword overlaps with a previously created listing in the user's log, issue a **Keyword Overlap Warning** offering 3 pivot choices:
  - `[a]` Pivot to a sibling phrase from Phase 4 research
  - `[b]` Keep phrase anyway (Etsy de-duplication risk)
  - `[c]` Re-keyword previous listing

### 📌 Phase 3: Title Construction & Validation (`listing-guide.md` §1)
- **Mandatory Title Formula:** `[Primary Keyword] [Style/Theme Descriptor] | [Format or Use-Case]`
- **SVG Example:** `Funny Cat Mom SVG Bundle | Cricut Clipart PNG EPS`
- **Hard Limits & Prohibitions:**
  - **Word Count Limit:** MUST be **6 to 12 words**. ABSOLUTE MAXIMUM: **14 words**. Any title with 15 or more words is INVALID and MUST be rejected and rewritten immediately.
  - **Length Limit:** ≤ 140 characters (including spaces).
  - **Primary Keyword Front-Loading:** Primary search phrase MUST appear within the **first 40 characters** (critical for mobile display and search algorithm indexing).
  - **PROHIBITED SUBJECTIVE WORDS STOPLIST (ZERO ALLOWED):** Do NOT use filler adjectives or subjective fluff: `cute`, `adorable`, `beautiful`, `perfect`, `stunning`, `amazing`, `incredible`, `pretty`, `awesome`, `gorgeous`, `lovely`, `sweet`, `unique`, `best`, `top`, `wonderful`, `charming`.
  - **No Comma-Chain Stuffing:** Natural phrasing separated by clean pipes (`|`) or slashes (`/`).
  - **No Trademarks or Sales Words:** Zero brand names, celebrity names, or promotional words (*on sale, free, best seller*).

### 🏷️ Phase 4: 13 Tags Construction & Character Limit / Duplication Audit (`listing-guide.md` §2)
- **Exact Count:** Exactly 13 tags (never leave tag slots blank).
- **Character Limit:** Every tag MUST be **≤ 20 characters** (including spaces). Tags >20 chars are silently rejected by Etsy.
- **Phrase Overlap Limit:** No exact 2+ word phrase may repeat across more than 2 tags (maximum 2 tags may share a 2-word phrase cluster).
- **No Single Word Tags:** Use multi-word long-tail phrases (`softball mom svg`, not `svg`).
- **Verification Audit:** Output the exact character count per tag (`[Tag] ([X] chars ✅)`).

### 📂 Phase 5: Attributes & Category Mapping (`listing-guide.md` §3 & §5)
- **Category:** `Craft Supplies & Tools > Canvas & Surfaces > Stencils, Templates & Transfers > Cut Files`
- **Attributes:** Style, Occasion, Recipient. At least 1 attribute value MUST echo a word from the primary keyword cluster.

### 📝 Phase 6: Full 9-Block Description & 160-Char Meta Zone (`listing-guide.md` §4)
- **Meta Zone (First 160 chars):** Must contain the primary keyword and function as a complete product pitch.
- **Length:** 250 to 700 words.
- **No Emojis:** Zero emojis allowed in description text or section headers (prevents spam signals and ensures screen-reader accessibility).
- **No Generic Openers:** Prohibit "Thank you for visiting" or "This listing is for".
- **Structure:** Opening Hook → Value & Features → Included File Formats (SVG, PNG 300 DPI 4000x4000px, EPS, DXF, PDF) → Instant Delivery → Machine Compatibility (Cricut, Silhouette, Laser, Sublimation) → Usage License (Personal & Small Business Commercial up to 500 items) → AI & Image Disclosure → Closing.

### 🖼️ Phase 7: Hero Image Alt Text, Image Plan & Pinterest Marketing Block (`listing-guide.md` §6)
- **Hero Alt Text:** 100–150 chars containing primary keyword.
- **Image Plan:** Product-type compliant slot plan — slot 1 is the clearest true image of what the buyer receives; digital downloads include a real preview/excerpt of the actual files; physical/custom/pattern products lead with a real unedited photo.
- **Pinterest Block:** Pin title (≤100 chars), Board name (25–40 chars), Board description (150–300 chars), Pin description (220–232 chars, no hashtags — write naturally first, then count characters and explicitly expand/trim to land within 220–232 chars before finalizing).

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

When State 13 executes, the executing agent MUST NOT output a brief summary or generic text. The agent MUST populate and render the following **exact Markdown structure matching `listing-guide.md`**:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NATIVE ETSY LISTING PACKAGE — STATE 13
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRIMARY KEYWORD: [Primary Keyword] · difficulty: [Low-Medium / Medium] · ~[N] search results

TITLE:
[Title using formula: Primary Keyword + Style Descriptor | Format or Use-Case]

📱 Mobile Preview Card & Title Verification:
┌───────────────────────────────────────┐
│ [First 40 characters of title]...     │
└───────────────────────────────────────┘
First 40 chars: "[First 40 chars text...]" ✅
Word count: [X] words (MUST be 6–12 words, MAX 14) ✅
Char count: [X] / 140 ✅
Subjective words check: 0 subjective words used ✅

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
*(Verification Check: Exactly 13 tags, all ≤20 characters including spaces, no phrase shared across >2 tags)*

ATTRIBUTES:
Style: [Value]    Occasion: [Value]    Recipient: [Value]    Category: Craft Supplies & Tools > Canvas & Surfaces > Stencils, Templates & Transfers > Cut Files

DESCRIPTION:
[Meta zone — first 160 chars: "..."] ✅

### [Attention-Grabbing Product Hook Title]
[2-3 sentences targeting buyer persona, emotional trigger, and core craft use case]

### Included File Formats
- **1x SVG File:** Clean, layered vector paths optimized for Cricut & Silhouette cutting.
- **1x PNG File:** High-resolution 300 DPI transparent background (4000x4000px).
- **1x EPS File:** Professional vector graphics editing format.
- **1x DXF File:** Silhouette Studio Basic Edition format.
- **1x PDF File:** Vector print & preview format.

### Machine & Software Compatibility
- Cricut Design Space
- Silhouette Studio (Designer & Basic Editions)
- Brother ScanNCut
- Laser Cutters (Glowforge, xTool, Omtech)
- Sublimation Printers & Heat Press software

### Usage Rights & Commercial License
- **Personal Use:** Unlimited personal crafting & gifts.
- **Commercial Use:** Small Business Commercial License included for up to 500 physical end-products (t-shirts, mugs, totes, decals).
- **Restrictions:** Reselling, sharing, or redistributing digital files in any format is strictly prohibited.

## Etsy AI & Image Disclosure & Settings
- **About this listing dropdowns:**
  - *Who made it?* **I did**
  - *What is it?* **A finished product or digital file**
  - *When was it made?* **Made to order / Recently made**
- **Mandatory Description Disclosure (AI-generated artwork):**
  *"Created with AI assistance using my own prompts and refined by me."*
- **If listing images were AI-edited (recommended):**
  *"Some listing images were edited with AI tools for lighting and background; the item itself is shown accurately."*
- Never claim "no AI", "100% handmade", or "hand-drawn" if AI use is unconfirmed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMAGE PLAN (product-type compliant):
Slot 1: [Clearest true image of what the buyer receives — real file preview for digital downloads]
Slot 2: [Bundle grid / all designs or second real angle]
Slot 3: [Close-up of best design or detail]
Slot 4: [Lifestyle mockup — must match the delivered files exactly]
Slot 5: [What's included infographic]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI & IMAGE COMPLIANCE:
Item origin:     [human-made / seller-prompted AI / unknown — do not guess]
Content type:    [physical / digital design / functional instructions / prompt bundle]
Image plan:      [real file preview / unedited photo confirmed / licensed POD mockup / ACTION REQUIRED: <what's missing>]
Disclosure:      [required — added / required — MISSING / not stated — add only if AI was used]
Gate:            ✅ PASS  ·  ⚠️ ACTION REQUIRED  ·  ⛔ BLOCKED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HERO IMAGE ALT TEXT (Etsy + Pinterest):
[100-150 characters containing primary keyword for accessibility & search indexing]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PINTEREST MARKETING BLOCK:
PIN TITLE: [Pin title ≤100 chars]
BOARD NAME: [Board name 25-40 chars]
BOARD DESCRIPTION: [Board description 150-300 chars]
PIN DESCRIPTION: [Pin description 220-232 chars, no hashtags — count characters and explicitly expand/trim to land within 220-232 chars before finalizing]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INDEXING SPREAD: Title ✅  ·  Tags (3+) ✅  ·  Attributes ✅  ·  Meta Zone ✅  ·  Alt Text ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BEFORE YOU PUBLISH CHECKLIST:
□ Title updated on Etsy (verify mobile preview card)
□ All 13 tags updated (verify all ≤20 chars)
□ Description updated (copy first 160 chars carefully into meta section)
□ Attributes updated (Style / Occasion / Recipient)
□ AI disclosure line present (if AI generated the artwork)
□ Image plan uploaded (real file preview for digital; unedited real photo for physical)
□ No AI-only image of a finished result; no misleading edits
□ Listing reviewed and published by a human (no bulk/bot publishing)
□ Hero image alt text updated (includes primary keyword)
□ Category set to Cut Files
□ Save ➔ preview ➔ confirm no tags got truncated
□ Log entry saved to ~/esvg-research/research-log.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Engineered by Moiz Zoaib Ali | moiz.solutions | tools.moiz.solutions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
