---
name: svg-design-intelligence-system
description: >
  Etsy SVG Design Intelligence System (ESVG-DIS). Market research, IP
  risk screening, buyer psychology, commercial opportunity scoring,
  original concept development, and AI prompt engineering for Etsy SVG
  sellers. Triggers on "research an Etsy SVG niche", "find a profitable
  SVG idea", "check if [keyword] SVG is a good opportunity", "screen
  this idea for trademark risk", "give me SVG concepts for [niche]",
  "write me a prompt for [design idea]". Uses live Etsy search when
  available; falls back to reasoning with an explicit confidence label
  when it isn't. Maintains a single-file research log at
  ~/esvg-research/research-log.md for cross-session memory on
  Claude/Cowork.
---

# ESVG-DIS — SVG Design Intelligence System

**Schema version:** 1.2 (Featuring System Laws & Caveman Output Protocol)

---

## 📜 THE 5 IMMUTABLE SYSTEM LAWS

All phase executions MUST strictly enforce `../playbooks/system-laws.md`:

1. **Immutable Pipeline Integrity:** Process every state/phase sequentially without skipping.
2. **Zero-Hallucination Evidence Traceability:** Empirical data or explicit fallback tagging.
3. **Binary IP Supremacy:** IP gates (1-4) are hard binary pass/modify/block checks.
4. **Caveman Output Protocol:** Crisp, bullet-first, token-efficient outputs by default; full raw reports unlocked on demand (`"expand"`, `"full report"`).
5. **Native Listing Engine Mandate:** State 13 natively executes all 8 SEO listing phases.

---

## ⚡ HOW THE SKILL WORKS — Read first

One core action, run start-to-finish or resumed partway through,
depending on what the user gives you.

| Input the user provides | What happens |
|---|---|
| Bare keyword/niche ("Golden Retriever SVG") | **Full pipeline** from State 1 (Intake) |
| Keyword + explicit prior context ("I already know my audience is...") | Full pipeline, skip re-asking what's already given |
| Pasted Research Log snapshot from a prior session | **Resume** — check it against current request before re-researching |
| "Just check IP risk on [X]" | **Standalone IP screening** — State 3 gate only, see Capabilities |
| "Compare these concepts: A, B, C" | **Standalone Concept Evaluation** — State 9 scoring only |
| "Write me a prompt for [fully-specified concept]" | Confirm the concept has actually cleared IP screening first, see the note below, then go straight to Prompt Engineering (State 10) |
| Anything genuinely ambiguous | Ask ONE question before proceeding, per `../workflow/00-intake-and-interview.md` |

**Important, don't let "just give me a prompt" skip IP screening.**
If a user asks for a prompt on a concept that hasn't been screened, run
the Keyword IP Screening gate (State 3) on it first, briefly, before
writing the prompt. This takes one step and prevents building a whole
prompt around something that turns out to be blocked. See
`../workflow/02-ip-gates.md`.

---

## 📦 ON EVERY FULL-PIPELINE RUN — Execution sequence

### Phase 0 — Auto-bootstrap state (Cowork/Claude only, silent)

```bash
python3 ~/.claude/skills/svg-design-intelligence-system/scripts/bootstrap.py
```

Idempotent. Creates `~/esvg-research/research-log.md` from the bundled
template on first run; does nothing on subsequent runs. The user never
sees this. For non-Cowork tools (ChatGPT/Gemini/Grok/free Claude):
skip this, state lives in the conversation, or in a Research Log
Snapshot the user pastes at the start (see Output Format).

### Phase 1 — Load existing state (silent)

Read `~/esvg-research/research-log.md` if it exists. For non-Cowork
tools, use any pasted snapshot instead. See
`../state-templates/esvg-research/research-log.md` section "How This Gets
Used" for exactly what to check and when.

### Phase 2 — Intake (State 1)

Collect required inputs per `../workflow/00-intake-and-interview.md`:
keyword, marketplace (default Etsy), target customer, product type,
complexity, use case. Ask only for what's genuinely missing, don't
re-ask what the user already gave you or what the research log already
answers for this niche.

### Phase 3 — Market Research (State 2)

Per `../knowledge/market-intelligence.md`: keyword analysis, demand
assessment, trend classification, market gap identification.
**Attempt live Etsy search first; label output with the 3-tier Data Source model** (Full Live vs. Partial/Thin Live vs. Reasoning Fallback per section 3.2 of that file). Produce the Market Intelligence Report.

### Phase 4 — Keyword IP Screening (State 3) `[GATE 1 of 4]`

Per `../workflow/02-ip-gates.md`. Run the keyword against
`../playbooks/trademark-and-ip-stoplist.md` first — it's the concrete,
checkable version of the risk categories in that gate. **Mandatory Fallback:** Do not treat a stoplist miss as automatic PASS — evaluate general trademark/franchise knowledge for un-listed brands (e.g. Dungeons & Dragons, Warhammer, Pokémon). Decision: PASS / MODIFY / BLOCK.

- **BLOCK** -> stop here. Produce an IP Block Report (reason, detected
  risk, safer alternatives). Do not proceed to Phase 5. Do not
  auto-retry, this needs a new direction from the user.
- **PASS / MODIFY-resolved** -> continue.

### Phase 5 — Buyer Psychology Analysis (State 4)

Per `../knowledge/buyer-psychology.md`: analyze 6 purchase motivations (Identity, Gift, Hobby, Emotion, Aesthetic & Subculture, Problem Solving), buyer persona, micro-niche identification, identity layering.

### Phase 6 — Competition Analysis (State 5)

Per `../knowledge/competition-intelligence.md`. **Attempt live Etsy
search first; fall back to reasoning if unavailable, and label the
output accordingly** (section 4 of that file). Produce the Competition
Intelligence Report.

### Phase 7 — Opportunity Scoring (State 6)

Per `../workflow/03-scoring-architecture.md`, Level 1. Six weighted
dimensions, IP excluded (already gated in Phase 4).

- **Score >= 7.5** -> before proceeding, check
  `../playbooks/niche-saturation-reality-check.md` — if its four
  trigger criteria are all met, show that reality check before Phase 8
  rather than after.
- **Score 5.5-7.4** -> flag as moderate; ask the user whether to refine
  research or proceed anyway.
- **Score < 5.5** -> check **Competition Difficulty**:
  * **If CD ≤ 2 (Extreme Saturation):** Do NOT halt silently or output a generic failure report. Cross-wire directly to `../playbooks/niche-saturation-reality-check.md` and present the 3 actionable paths forward (`[a]` Proceed with heavy differentiation, `[b]` Narrow to a micro-niche, `[c]` Explore a different keyword) per `../workflow/04-retry-and-halt-logic.md` §4.
  * **If CD > 2:** Apply the judgment call in `../workflow/04-retry-and-halt-logic.md` §4: improvable -> return to Phase 3 (within 3 attempts); fundamentally weak -> halt as `HALTED_OPPORTUNITY_FAILURE`, produce the Opportunity Failure Report, and stop. Check `../playbooks/honest-diagnosis-pointers.md` if this is a repeated failure.

### Phase 8 — Creative Strategy (State 7)

Per `../knowledge/creative-strategy.md`. Produce the Creative Brief:
position, buyer, emotional goal, theme, visual language,
differentiation strategy, SVG requirements.

### Phase 9 — Concept Generation (State 8)

Per `../knowledge/concept-development.md`. Generate 30-50 concepts. **Proactive IP Rule:** Be proactively IP-aware at creation time (section 3.1) — avoid brand-associated signature combinations (e.g. cape+mask+chest emblem) during initial generation rather than relying solely on Gate 2 as a filter. **Check the Research Log's "IP-Blocked Concepts" column for this niche first, never regenerate something already blocked.**

### Phase 10 — Concept IP Review (State 8A) `[GATE 2 of 4]`

Per `../workflow/02-ip-gates.md`. Applied per concept. BLOCKed concepts
are removed from the portfolio (scope: single concept, not the whole
batch), log them to the Research Log's IP-Blocked column. Continue
with survivors.

### Phase 11 — Concept Evaluation (State 9)

Per `../workflow/03-scoring-architecture.md`, Level 2. Five-dimension
score, rank the surviving portfolio, present the top 2-3 to the user
for selection, don't auto-pick without user confirmation unless
explicitly asked to.

### Phase 12 — Prompt Engineering (State 10)

Per `../prompts/prompt-engineering-framework.md`, `../prompts/engine-tuning-guide.md`, and the relevant `../prompts/style-templates/` file. Check concept against `../playbooks/cutting-machine-thresholds.md` for Cricut limits (≥ 1/40th width, min 2-3pt line weight). Build the **Multi-Tool AI Prompt Package** providing engine-tuned variants for:
1. **Google Gemini / Imagen 3** (anti-shadow, zero paper texture inline directive)
2. **Midjourney v6** (`--no` parameter flags)
3. **ChatGPT / DALL-E 3** (anti-rewrite directive)
4. **Flux 1.1 / Flux Pro** (flat 2D stroke precision)

### Phase 13 — Prompt IP Validation (State 10A) `[GATE 3 of 4]`

Per `../workflow/02-ip-gates.md`. BLOCK removes unsafe prompt elements
only; concept doesn't need re-evaluation.

### Phase 14 — User Generation + Final Artwork IP Review (States 11, 11A) `[GATE 4 of 4]`

Hand off the prompt package for the user to run externally. When they
return with generated artwork (described or shown), run the Final
Artwork IP Review per `../workflow/02-ip-gates.md` before Phase 15.

### Phase 15 — Design Review (State 12)

Per `../knowledge/design-quality-review.md`, Level 3. Four dimensions —
for the SVG Suitability dimension specifically, check against
`../playbooks/cutting-machine-thresholds.md` if a cutting machine is
the use case. Approved -> Phase 16. Needs improvement -> return to
Phase 12, within retry limits. If this is a repeated failure, check
`../playbooks/honest-diagnosis-pointers.md` before recommending
another prompt revision.

### Phase 16 — SEO Handoff & Listing Engine (State 13)

Per `../integration/etsy-seo-handoff.md` and `../integration/etsy-seo-engine/`. Execute all **8 Mandatory Execution Phases**:

1. **Policy & Algorithm Freshness Check & Automated Sync:** Verify output against August 11, 2026 Etsy Creativity Standards. In Portable/Web Mode, run a live web search for `"Etsy seller policies 2026"` / `"Etsy creativity standards"` to verify active rules. In Full System/CLI Mode, run `python3 scripts/sync_etsy_policy.py` to auto-sync local policy rulebooks across repositories.
2. **Keyword Cannibalization Prevention:** Check candidate primary keyword against `~/esvg-research/research-log.md`; issue overlap warning if already used.
3. **Title Construction:** Formula: `[Primary Keyword] [Style/Theme Descriptor] | [Format or Use-Case]`. Max 140 characters. Primary focus keyword MUST be front-loaded in the **first 40 characters**. **Word Count Guardrail: MUST be 6–12 words (MAXIMUM 14 words).** Reject any title with 15+ words. **Prohibited Subjective Words Stoplist (ZERO ALLOWED):** `cute`, `adorable`, `beautiful`, `perfect`, `stunning`, `amazing`, `incredible`, `pretty`, `awesome`, `gorgeous`, `lovely`, `sweet`, `unique`, `best`, `top`, `wonderful`, `charming`.
4. **13 Search Tags:** Exactly 13 tags, every tag **≤ 20 characters** (including spaces), no exact 2+ word phrase shared across more than 2 tags, character count listed per tag (`[Tag] ([X] chars ✅)`).
5. **Attributes & Category Mapping:** Style, Occasion, Recipient mapped to Cut Files category (`Craft Supplies & Tools > Canvas & Surfaces > Stencils, Templates & Transfers > Cut Files`).
6. **5-Surface Indexing Spread Check:** Verify primary keyword touches Title (first 40 chars), Tags (3+ tags), Attributes, Description Meta Zone (first 160 chars), and Hero Alt Text.
7. **Full 8-Block Description:** Hook, File Formats (SVG, PNG 300 DPI, EPS, DXF, PDF), Cricut/Silhouette/Laser compatibility, License Terms (Personal & Small Business Commercial), and **Etsy 2026 AI Creation Disclosure settings** (*"I did"* / *"Made to order"*).
8. **Hero Alt Text & Pinterest Marketing Block:** 100-150 char alt text containing primary keyword, Pin title, Board name, Board description, Pin description (220-232 chars — write naturally first, then count characters and explicitly expand/trim to land within 220-232 chars before finalizing), and Pre-Publish Checklist.
9. **No Short Summaries:** Do NOT output a soft summary or generic text — output the full, ready-to-copy listing package.

### Phase 17 — Write state (Cowork/Claude only)

Append a row to `~/esvg-research/research-log.md`: date, keyword,
Opportunity Score, Data Source, top concept(s) selected, any
IP-blocked concepts. For non-Cowork tools: output the Research Log
Snapshot block instead (see Output Format).

---

## 🎨 OUTPUT FORMAT

### Research summary (after Phase 7)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OPPORTUNITY ANALYSIS — [keyword]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DATA SOURCE: [Live Etsy Search / Reasoning-Based Estimate]

Market Demand: [X]/10    Buyer Appeal: [X]/10
Differentiation: [X]/10   Production Suitability: [X]/10
Trend Strength: [X]/10    Competition Difficulty: [X]/10

OPPORTUNITY SCORE: [X.X]/10 — [Exceptional/Strong/Moderate/Weak]

IP SCREENING: [PASS/MODIFY/BLOCK] — [one-line reason]

RECOMMENDATION: [proceed / refine / explore alternative]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Concept portfolio (after Phase 11)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP CONCEPTS — [keyword]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. [Concept name] — Score: [X.X]/10
   [One-line description]
   Originality [X] · Buyer Alignment [X] · Emotional Strength [X]
   Visual Potential [X] · SVG Suitability [X]

2. [Concept name] — Score: [X.X]/10
   ...

Which would you like to develop into a prompt?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Prompt package (after Phase 12)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROMPT PACKAGE — [concept name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DESIGN PROMPT:
[full prompt text]

NEGATIVE PROMPT:
[full negative prompt]

SVG PRODUCTION NOTES:
Recommended complexity: [level]
Tracing difficulty: [Low/Medium/High]
Suggested cleanup: [notes]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Paste the design prompt into your image generation tool
□ Review the result against the negative prompt list
□ Come back with the result for Final Artwork IP Review
□ Vectorize and clean up per prompts/svg-production-optimization.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### For non-Cowork tools — Research Log Snapshot (end of session)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCH LOG SNAPSHOT — Save this. Paste at start of next session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Date | Keyword | Score | Data Source | Top Concept(s) | IP-Blocked |
|---|---|---|---|---|---|
| [date] | [keyword] | [X.X] | [Live/Reasoning] | [concept] | [none/list] |
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🛠 CAPABILITIES TRIGGERED BY USER INPUT

### Standalone IP screening ("is [X] SVG safe to make?")
Run Phase 4 (State 3, Keyword IP Screening) alone. Report PASS/MODIFY/
BLOCK with reasoning. Doesn't require the full pipeline.

### Standalone concept comparison ("which of these is stronger: A vs B")
Run Phase 11 (State 9, Concept Evaluation) alone on the user-provided
concepts. Note in the output that these weren't screened through
Concept IP Review (Phase 10) unless the user confirms they already
were.

### Resume from a Research Log entry
If the user pastes a prior snapshot or the log already has this
niche, follow `../state-templates/esvg-research/research-log.md` section
"How This Gets Used" before deciding whether to re-research or build
on the prior pass.

---

## 📚 REFERENCE FILES — Load as needed

### Workflow (process logic)
- `../workflow/01-canonical-state-machine.md` — full state definitions
- `../workflow/02-ip-gates.md` — all 4 gates, decision vocabulary, scope
- `../workflow/03-scoring-architecture.md` — all 3 scoring levels
- `../workflow/04-retry-and-halt-logic.md` — retry limits, halt behavior

### Knowledge (subject matter)
- `../knowledge/market-intelligence.md`, `competition-intelligence.md`,
  `buyer-psychology.md`, `ip-risk-and-originality.md`,
  `commercial-opportunity-scoring.md`, `creative-strategy.md`,
  `concept-development.md`, `design-quality-review.md`

### Prompts
- `../prompts/prompt-engineering-framework.md`,
  `svg-production-optimization.md`, `prompt-refinement-guide.md`
- `../prompts/style-templates/` — universal, vintage, minimalist,
  character, typography, bundle-creation

### Playbooks (concrete, checkable — not just descriptive frameworks)
- `../playbooks/trademark-and-ip-stoplist.md` — the actual checkable
  list behind the IP gates
- `../playbooks/niche-saturation-reality-check.md` — when to warn
  honestly about a generic concept in a saturated niche
- `../playbooks/cutting-machine-thresholds.md` — concrete production
  thresholds, not just "keep it simple"
- `../playbooks/honest-diagnosis-pointers.md` — what to say when
  something keeps failing, instead of defaulting to "try again"

### Examples
- `../examples/worked-examples.md` — complete pipeline walkthrough with
  real scores, plus two shorter illustrative sketches. Useful for
  calibrating expected output format and seeing real decisions in context.

---

## 🚫 HONEST SCOPE — What this skill will NOT do

- Will NOT generate the final SVG file, trace an image, or operate
  Illustrator/Inkscape.
- Will NOT upload anything to Etsy.
- Will NOT promise a sales outcome, scores are decision support, not
  guarantees.
- Will NOT give legal advice, IP screening is analytical risk
  assessment, not trademark clearance.
- Will NOT let a strong score override a real IP risk. Every gate can
  override every score, never the reverse.
- WHEN live search is unavailable -> says so directly, labels the
  output as a reasoning-based estimate, and proceeds anyway rather than
  refusing to help.

---

## 📋 QUICK-REFERENCE NUMBERS

| Field | Value |
|---|---|
| IP gates | 4 (Keyword, Concept, Prompt, Final Artwork) |
| Scoring levels | 3 (Opportunity, Concept, Quality) |
| Opportunity Score weights | Demand/Buyer Appeal/Differentiation 23.5% each, Production/Trend 11.8% each, Competition 5.9% |
| Concept Score dimensions | 5, unweighted average |
| Quality Score dimensions | 4, unweighted average |
| Concept Generation retry limit | 5 attempts |
| Market Research retry limit | 3 attempts |
| Most other retry limits | 3 attempts |
| Recommended concept batch size | 30-50 |
