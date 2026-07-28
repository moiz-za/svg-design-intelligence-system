# Canonical State Machine

This is the single authoritative state-by-state definition of the
ESVG-DIS workflow. `SYSTEM_INSTRUCTIONS.md` §5 shows the flow at a
glance — this file is the detail behind each state.

For IP gate mechanics (States 3, 8A, 10A, 11A), full detail lives in
`workflow/02-ip-gates.md` — this file shows only where each gate sits
in sequence and what it hands off to next, so gate logic isn't
duplicated in two places. Same for scoring (States 6, 9): full detail
in `workflow/03-scoring-architecture.md`. Same for retries: full
detail in `workflow/04-retry-and-halt-logic.md`.

---

## Full Sequence

```
START
↓
1.  INTAKE
↓
2.  MARKET RESEARCH
↓
3.  KEYWORD IP SCREENING          [GATE]
↓
4.  BUYER PSYCHOLOGY ANALYSIS
↓
5.  COMPETITION ANALYSIS
↓
6.  OPPORTUNITY SCORING
↓
7.  CREATIVE STRATEGY
↓
8.  CONCEPT GENERATION
↓
8A. CONCEPT IP REVIEW             [GATE]
↓
9.  CONCEPT EVALUATION
↓
10. PROMPT ENGINEERING
↓
10A. PROMPT IP VALIDATION         [GATE]
↓
11. USER GENERATION PHASE
↓
11A. FINAL ARTWORK IP REVIEW      [GATE]
↓
12. DESIGN REVIEW
↓
13. SEO HANDOFF
↓
END
```

---

## STATE 0 — START

**Purpose:** Initialize the workflow.
**Input:** The user's initial request (e.g. "Create Halloween SVG
ideas").
**Output:** Move to Intake.

---

## STATE 1 — INTAKE

**Purpose:** Understand user requirements.
Full detail: `workflow/00-intake-and-interview.md`.

**Collects:** keyword/topic, target marketplace, product type, target
audience (if known), design goal, restrictions.

**Transition:**
- Sufficient information → `INTAKE COMPLETE` → **State 2**
- Missing information → `REQUEST CLARIFICATION` (ask, don't guess)

---

## STATE 2 — MARKET RESEARCH

**Purpose:** Understand market opportunity.
Full detail: `knowledge/market-intelligence.md`.

**Analyzes:** search demand, niche size, buyer interest, seasonal
relevance, marketplace patterns.

**Output:** Market Intelligence Report (demand level, audience size,
opportunity notes).

**Transition:** → **State 3**

---

## STATE 3 — KEYWORD IP SCREENING `[GATE 1 of 4]`

**Purpose:** Identify legal and marketplace risk before any creative
investment happens.
Full detail: `workflow/02-ip-gates.md`.

**Decision:** PASS / MODIFY / BLOCK.
**Scope of BLOCK:** entire opportunity/direction — the input itself is
unsafe, not just one execution of it.

**Transition:**
- PASS/MODIFY resolved → **State 4**
- BLOCK → terminate direction, offer alternatives (does not proceed)

---

## STATE 4 — BUYER PSYCHOLOGY ANALYSIS

**Purpose:** Understand why customers buy.
Full detail: `knowledge/buyer-psychology.md`.

**Analyzes:** buyer identity, emotional motivation, purchase scenario,
gifting potential.

**Output:** Buyer Persona Report.
**Transition:** → **State 5**

---

## STATE 5 — COMPETITION ANALYSIS

**Purpose:** Understand existing marketplace conditions.
Full detail: `knowledge/competition-intelligence.md`.

**Analyzes:** competitor saturation, common patterns, weaknesses,
differentiation opportunities.

**Output:** Competition Intelligence Report.
**Transition:** → **State 6**

---

## STATE 6 — OPPORTUNITY SCORING

**Purpose:** Decide whether the opportunity deserves creative
development.
Full detail: `workflow/03-scoring-architecture.md` (Level 1 —
Opportunity Score).

**Inputs:** market research, buyer psychology, competition analysis.
(Note: IP has already been gated at State 3 — it is not a scoring
input here. See `workflow/02-ip-gates.md` §7 for why IP and scoring
stay separate.)

**Decision:**
- **High score (≥ 7.5):** check Competition Difficulty. If CD ≤ 2 & generic concept → trigger Niche Saturation Reality Check (`playbooks/niche-saturation-reality-check.md`), then continue → **State 7**.
- **Moderate score (5.5 – 7.4):** improve concept angle / research → return to **State 2**.
- **Low score (< 5.5):** check Competition Difficulty. If CD ≤ 2 (Extreme Saturation), trigger 3-Path Niche Saturation Guidance (`playbooks/niche-saturation-reality-check.md` & `workflow/04-retry-and-halt-logic.md` §4) offering Proceed / Narrow / Redirect choices. If CD > 2 & non-improvable → `HALTED_OPPORTUNITY_FAILURE`.

---

## STATE 7 — CREATIVE STRATEGY

**Purpose:** Define the creative direction.
Full detail: `knowledge/creative-strategy.md`.

**Creates:** Creative Brief — product positioning, visual style,
emotional direction, differentiation strategy, SVG requirements.

**Transition:** → **State 8**

---

## STATE 8 — CONCEPT GENERATION

**Purpose:** Create multiple original design directions.
Full detail: `knowledge/concept-development.md`.

**Rules:** concepts must match buyer psychology, avoid IP risk (see
State 8A immediately after), provide differentiation, remain SVG
feasible.

**Output:** Concept Portfolio (multiple concepts).
**Transition:** → **State 8A**

---

## STATE 8A — CONCEPT IP REVIEW `[GATE 2 of 4]`

**Purpose:** Check whether any specific concept in the portfolio
introduces IP risk the keyword itself didn't have — the opportunity
already passed Gate 1, this checks each individual concept.
Full detail: `workflow/02-ip-gates.md`.

**Decision:** PASS / MODIFY / BLOCK, applied per concept.
**Scope of BLOCK:** single concept only. The concept is removed from
the portfolio; the workflow continues evaluating the remaining
concepts. Research and opportunity approval are not repeated.

**Transition:**
- Portfolio has at least one PASS/MODIFY-resolved concept → **State 9**
- Every concept BLOCKed → return to **State 8** (regenerate, within
  retry limits) or, if exhausted, halt (see
  `workflow/04-retry-and-halt-logic.md`)

---

## STATE 9 — CONCEPT EVALUATION

**Purpose:** Select the strongest concept from the surviving portfolio.
Full detail: `workflow/03-scoring-architecture.md` (Level 2 — Concept
Score).

**Evaluation factors:** Originality, Buyer Alignment, Emotional
Strength, Visual Potential, SVG Suitability. (IP is not one of these —
every concept reaching this state already passed State 8A.)

**Output:** Selected Concept Direction.

**Rejection handling:** rejected concepts are archived, not deleted —
future research may reveal a use for them later.

**Transition:** → **State 10**

---

## STATE 10 — PROMPT ENGINEERING

**Purpose:** Convert the selected concept into a high-performance, tool-tailored AI generation prompt package.
Full detail: `prompts/prompt-engineering-framework.md` and `prompts/engine-tuning-guide.md`.

**Prompt must include:** subject, concept, audience, style,
composition, SVG requirements, technical restrictions, negative prompt, and anti-shadow inline rules.

**Output:** Multi-Tool AI Generation Prompt Package (providing tailored prompt variants for Google Gemini/Imagen 3, Midjourney v6, ChatGPT/DALL-E 3, and Flux 1.1).
**Transition:** → **State 10A**

---

## STATE 10A — PROMPT IP VALIDATION `[GATE 3 of 4]`

**Purpose:** Check the actual prompt text for protected references,
copied styles, famous characters, or trademarked phrases that may have
crept in while drafting — even though the underlying concept already
passed State 8A.
Full detail: `workflow/02-ip-gates.md`.

**Decision:** PASS / MODIFY / BLOCK.
**Scope of BLOCK:** single prompt direction. The unsafe elements are
removed from the prompt; the concept itself does not need
re-evaluation.

**Transition:**
- PASS/MODIFY resolved → **State 11**
- BLOCK exhausted (retry limit reached) → escalate per
  `workflow/04-retry-and-halt-logic.md`

---

## STATE 11 — USER GENERATION PHASE

**Purpose:** Human-controlled artwork creation.

**Important rule:** ESVG-DIS does NOT create or approve final SVG
files. The user decides the image tool, vectorization method, cleanup
process, and final formats.

**Recommended user workflow:** generate image → review → vectorize →
clean → export files.

**Transition:** → **State 11A**

---

## STATE 11A — FINAL ARTWORK IP REVIEW `[GATE 4 of 4]`

**Purpose:** Evaluate the actual generated artwork for IP risk. The
first three gates all evaluate intent (keyword, concept, prompt text)
— none of them can see the actual pixels an image model produced. A
clean prompt can still generate an unsafe image. This is the only gate
that checks the finished output itself.
Full detail: `workflow/02-ip-gates.md`.

**Decision:** PASS / MODIFY / BLOCK.
**Scope of BLOCK:** single generated artwork.

**Transition:**
- PASS → **State 12**
- MODIFY → return to **State 11** (regenerate from the same approved
  prompt)
- BLOCK → return to **State 10** (the prompt itself needs revision —
  simply regenerating would likely repeat the same issue)

---

## STATE 12 — DESIGN REVIEW

**Purpose:** Evaluate the user's generated design direction.
Full detail: `knowledge/design-quality-review.md`;
`workflow/03-scoring-architecture.md` (Level 3 — Quality Score).

**Review areas:** Commercial Quality, Originality, SVG Suitability,
Marketplace Differentiation. (IP was already confirmed at State 11A —
it is not one of these four dimensions.)

**Transition:**
- Approved → **State 13**
- Needs improvement → return to **State 10** (within retry limits)

---

## STATE 13 — SEO HANDOFF

**Purpose:** Transfer product intelligence to Etsy listing
optimization.
Full detail: `integration/etsy-seo-handoff.md`.

**Output:** Product Intelligence File — buyer persona, product angle,
keywords, positioning, design description.

**Transition:** → **END**

---

## Failure Handling, By Category

| Failure | Example | Action |
|---|---|---|
| Research Failure | Insufficient market information | Request more information |
| IP Failure | Trademark conflict at any gate | Block or redirect (scope per gate — see `workflow/02-ip-gates.md`) |
| Opportunity Failure | No differentiation possible | Return to research, or halt if unimprovable |
| Concept Failure | Too generic | Generate new concepts |
| Prompt Failure | AI output unsuitable for SVG | Refine prompt |

Full retry limits and terminal halt behavior for every row above:
`workflow/04-retry-and-halt-logic.md`.

---

## Human Review Checkpoints

Human involvement is available at:

- Opportunity Approval (State 6)
- Concept Selection (State 9)
- Generated Artwork Review (State 11A / State 12)
- Final Product Decision (State 13)

---

## State History Logging

Every workflow run should maintain a record of: current state, previous
states, decisions made, rejected options (including archived concepts
from State 9), and final output. This is what makes a halted or
escalated workflow resumable rather than a dead end.
