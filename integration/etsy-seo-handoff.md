# Native Etsy SEO & Listing Engine

Used in **State 13 — SEO Handoff & Listing Creation**, the final state of the canonical workflow (`workflow/01-canonical-state-machine.md`).

This module embeds the complete 2026 Etsy SEO listing engine directly into ESVG-DIS (drawing from native frameworks in `integration/etsy-seo-engine/seo-guide.md`, `listing-guide.md`, and `policies.md`), ensuring every product engineered by ESVG-DIS is delivered as a 100% complete, fully optimized Etsy listing.

---

## 1. Native Listing Output Requirements

State 13 MUST generate a complete, production-ready Etsy listing package in a single response, enforcing strict 2026 Etsy SEO rules:

### 📌 A. Title Optimization Rules (`integration/etsy-seo-engine/seo-guide.md`)
- **Character Limit:** Maximum 140 characters.
- **Primary Keyword Front-Loading:** The primary high-intent search phrase MUST appear within the **first 40 characters** (critical for mobile search cards & Etsy algorithm indexing).
- **Formatting:** Front-loaded, high-converting long-tail phrases separated by clean pipes (`|`) or slashes (`/`).
- **No Keyword Stuffing:** Avoid repetitive word salads or unnatural phrasing.

### 🏷️ B. 13 Search Tags Rules (`integration/etsy-seo-engine/playbooks/`)
- **Exact Count:** Exactly 13 tags (never leave available tag slots empty).
- **Tag Character Limit:** Every single tag MUST be **≤ 20 characters**.
- **Zero Duplicates:** No repeated tags or redundant phrases across the 13 slots.
- **Tag Diversity:** Mix primary keywords, niche modifiers, craft machine terms (`cricut file`, `shirt svg`), and buyer/occasion terms.

### 💰 C. Pricing Engine (`integration/etsy-seo-engine/listing-guide.md`)
- **Single SVG Design:** $2.50 – $4.99 (based on visual complexity and buyer appeal).
- **SVG Bundle / Collection:** $5.99 – $12.99 (based on set size and market demand).

### 📋 D. Full Listing Description & Disclosure (`integration/etsy-seo-engine/policies.md`)
Every output must include a fully structured listing description containing:
1. **Hook & Value Proposition:** High-converting opening paragraph targeting the buyer persona.
2. **Included File Formats:** SVG, PNG (300 DPI high resolution, transparent background), EPS, DXF, PDF.
3. **Machine & Software Compatibility:** Cricut Design Space, Silhouette Studio (Designer Edition+), Brother ScanNCut, Laser Cutters, Sublimation Printers.
4. **Commercial & Personal License Terms:** Personal & Small Business commercial usage rights.
5. **Etsy 2026 AI Creation Disclosure Section:**
   - **Listing Dropdowns:** *"I did"* | *"Made to order"* | *"Finished product or digital file"*
   - **Factual Description Transparency Note:** *"Original vector illustration engineered with AI assistance and hand-curated vector cleanup per Etsy Creativity Standards."*

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
Native Etsy SEO Listing Engine (State 13)  ← Complete Title, 13 Tags, Pricing & Description
```
