# Glossary

Every term below is used consistently across this repository. If a
definition here ever seems to conflict with how a term is used
elsewhere, this file is wrong and should be fixed to match the
workflow files — `workflow/` and `knowledge/` are the source of truth
for mechanics; this file just defines vocabulary.

---

### AI Chat Agent
A reasoning tool used for strategy, research, and analysis — ChatGPT,
Gemini, Claude, Grok, or any general-purpose AI assistant. Distinct
from an **Image Generation Model** (below). See `SYSTEM_INSTRUCTIONS.md`
§6.

### Buyer Persona
A structured profile of the target customer — identity, interest,
purchase motivation, emotional driver, preferred style, buying trigger.
Produced in State 4. See `knowledge/buyer-psychology.md` §3.

### Competition Difficulty
One of the six Opportunity Score dimensions. Scored **inversely**: 10 =
easy opportunity, 1 = extremely difficult market. Not to be confused
with a plain "competition level," which is qualitative (Low/Medium/
High/Extreme) — see `knowledge/competition-intelligence.md` §10 for
the conversion between the two.

### Concept
A specific creative direction — not just a subject, but a subject
combined with a theme, symbolic elements, composition, and
differentiation strategy. See `knowledge/concept-development.md`.

### Concept Portfolio
The full set of concepts generated at State 8, before ranking. Concepts
that fail Concept IP Review (State 8A) are removed from the portfolio;
the rest proceed to Concept Score.

### Concept Score
Level 2 of the scoring architecture. Answers "which creative direction
is strongest?" Five dimensions: Originality, Buyer Alignment,
Emotional Strength, Visual Potential, SVG Suitability. See
`workflow/03-scoring-architecture.md`.

### Creative Brief
The structured output of State 7 (Creative Strategy) — product
position, target buyer, emotional goal, design theme, visual language,
differentiation strategy, SVG production requirements. The direct
input to Concept Generation (State 8). See
`knowledge/creative-strategy.md` §3.

### Differentiation
The quality of being meaningfully distinct from existing marketplace
designs — not just visually different, but different in concept,
audience, style, or story. See `knowledge/creative-strategy.md` §6 and
`knowledge/ip-risk-and-originality.md`.

### Gate
A pass/fail checkpoint that determines *permission to continue*, as
opposed to a **Score** (below), which ranks options. IP is always
evaluated through a gate, never a score. Four gates exist in this
system — see `workflow/02-ip-gates.md`.

### Halt / WORKFLOW_HALTED
The terminal state entered when a stage exhausts its retry limit
without succeeding. Always produces a structured report and, by
default, requests a human decision — never a silent stop. See
`workflow/04-retry-and-halt-logic.md` §5-7.

### Image Generation Model
A tool that produces raster images from a prompt — ChatGPT Images,
Gemini Image Generation, Midjourney, Flux, Ideogram, Leonardo. Distinct
from an **AI Chat Agent** (above); only used at State 11.

### IP Risk
The probability of legal or marketplace conflict for a given keyword,
concept, prompt, or generated artwork. Higher = worse. See
`workflow/02-ip-gates.md` §6.

### IP Safety
The inverse of IP Risk: confidence that something is safe.
`IP Safety = 10 − IP Risk`. Higher = better. Never confuse this with
**Originality** (below) — they measure different things.

### Micro-Niche
A specific, smaller audience segment within a broad market — e.g.
"Golden Retriever Mom" rather than "Dog SVG." Usually less saturated
than the broad category it sits inside. See
`knowledge/buyer-psychology.md` §4.

### Opportunity Score
Level 1 of the scoring architecture. Answers "should we create
something in this market at all?" Six dimensions, weighted: Market
Demand, Buyer Appeal, Differentiation Potential (23.5% each),
Production Suitability, Trend Strength (11.8% each), Competition
Difficulty (5.9%). See `workflow/03-scoring-architecture.md`.

### Originality
A craft-quality dimension measuring uniqueness and differentiation —
part of Concept Score (Level 2). Distinct from IP Safety: a concept can
be perfectly IP-safe and still score low on originality. See
`knowledge/ip-risk-and-originality.md` §6.

### PASS / MODIFY / BLOCK
The universal decision vocabulary used at all four IP gates. PASS =
continue. MODIFY = revise before proceeding (retry-limited). BLOCK =
stop the current direction; scope of "current direction" varies by
gate — see `workflow/02-ip-gates.md` §3-4.

### Product Intelligence Package
The handoff artifact produced at State 13 — target audience, buyer
persona, positioning, emotional angle, design description, keyword
context, differentiation points. Passed to the Etsy SEO System. See
`integration/etsy-seo-handoff.md` §5.

### Quality Score
Level 3 of the scoring architecture. Answers "is this ready for
production?" Four dimensions: Commercial Appeal, Visual Quality, SVG
Suitability, Marketplace Differentiation. Does not include IP
(already gated at State 11A) or Originality/Buyer Alignment (already
scored at Concept Score) — see `workflow/03-scoring-architecture.md`.

### Score
A ranking mechanism used to compare options, as opposed to a **Gate**
(above), which determines permission to continue. IP is never scored —
only gated.

### State
One node in the canonical workflow (e.g. "State 6 — Opportunity
Scoring"). See `workflow/01-canonical-state-machine.md` for the
complete list.

### SVG Suitability
A recurring evaluation factor at multiple levels — how well a concept
or artwork will trace, vectorize, and hold up as a cutting-machine
file. Appears in both Concept Score (Level 2) and Quality Score
(Level 3), evaluating different things at each stage: at Level 2, the
concept's inherent suitability; at Level 3, whether the actual
generated artwork realized that suitability.
