# Architecture Decisions

This file exists so that hard-won fixes don't get quietly reversed by
a future contributor who doesn't know why something is the way it is.
Each entry states the decision, why it was made, and what was tried
before landing on it. If you're about to change something described
here, read the reasoning first — there's a good chance the
alternative you're considering was already tried and rejected.

---

## ADR-1: IP is a gate, never a score

**Decision:** IP risk is evaluated exclusively through four gates
(Keyword, Concept, Prompt, Final Artwork — see
`workflow/02-ip-gates.md`). It is never one of the weighted or
averaged dimensions in Opportunity Score, Concept Score, or Quality
Score.

**Why:** Early drafts of this system scored IP as one input among
several (e.g. "IP Safety: 15%" folded into an overall opportunity
average). This meant a concept with real trademark exposure could
still clear a high bar if its other scores were strong enough — a
legal/policy concern getting outvoted by unrelated factors like visual
appeal. A permission-to-continue decision and a ranking decision are
different kinds of judgment; blending them lets one silently
compensate for the other.

**Also rejected:** treating IP as a single gate at the very start
only. This was abandoned because generated artwork can introduce risk
that wasn't present in the original keyword or prompt (see ADR-2).

---

## ADR-2: Four IP gates, not one

**Decision:** IP is checked at four separate points: Keyword (State 3),
Concept (State 8A), Prompt (State 10A), and Final Artwork (State 11A).

**Why:** Each stage can introduce risk the previous stage couldn't see.
A clean keyword can lead to a concept that references a trademark. A
clean concept can produce a prompt with copied phrasing. A clean prompt
can still cause an image model to hallucinate a recognizable
character — the model, not the system, introduces that risk, and
nothing upstream of image generation can catch it. The fourth gate
(Final Artwork Review) exists specifically because the first three all
evaluate *intent* (text), and none of them can see the actual pixels a
model produces.

**Also rejected:** a single comprehensive check after generation only.
Rejected because it wastes generation effort on directions that were
never going to be safe (better to catch a trademarked keyword before
spending a research pass on it).

---

## ADR-3: BLOCK scope narrows as the pipeline progresses

**Decision:** A BLOCK at the Keyword gate kills the entire opportunity
direction. A BLOCK at the Concept gate removes only that one concept.
A BLOCK at the Prompt or Final Artwork gate affects only that prompt
or artwork.

**Why:** The further into the pipeline something is, the more upstream
work has already been validated. Killing the whole direction over one
bad concept in an otherwise-fine niche would throw away validated
research for no reason.

---

## ADR-4: Three scoring levels, not one, and IP isn't in any of them

**Decision:** Opportunity Score (Level 1, State 6), Concept Score
(Level 2, State 9), and Quality Score (Level 3, State 12) each answer a
different question and use different dimensions. See
`workflow/03-scoring-architecture.md`.

**Why:** Early drafts had at least three different, mutually
incompatible dimension lists purporting to describe "concept
evaluation," plus a separate mismatch on "quality evaluation" criteria
across different sections of the same document. The three-level model
replaced all of them with one canonical list per level. Critically:
each level answers a genuinely different question (market viability vs.
creative selection vs. production readiness) — so dimensions
shouldn't be shared or duplicated across levels even where they sound
similar (e.g. "Buyer Appeal" at Level 1 is not the same measurement as
"Buyer Alignment" at Level 2).

**Lesson learned the hard way:** even after this was declared fixed,
a full document sweep later found the fix hadn't actually reached every
place it needed to — a stale dimension list persisted in one state
definition, and a differently-stale list persisted in a quality-review
section, for some time after the "fix" shipped. See ADR-8.

---

## ADR-5: Opportunity Score weighting was preserved, not flattened

**Decision:** When IP Safety was removed as a scored dimension (ADR-1),
the remaining six dimensions' weights were proportionally renormalized
to sum to 100%, preserving the original priority ordering (Demand,
Buyer Appeal, and Differentiation weighted highest; Competition
weighted lowest). See `workflow/03-scoring-architecture.md` §Level 1.

**Why:** An intermediate draft accidentally replaced the weighted
formula with a flat, equal-weighted average when IP was removed — a
silent methodology change with no stated rationale, discovered and
corrected afterward. The lesson: removing one input from a weighted
formula means renormalizing the remaining weights, not abandoning
weighting.

---

## ADR-6: Vectorization is explicitly out of scope

**Decision:** ESVG-DIS does not trace raster images, operate
Illustrator/Inkscape, or produce actual SVG files. State 11 (User
Generation Phase) and the handoff to manual vectorization are both
owned by the user. See `SYSTEM_INSTRUCTIONS.md` §4 and
`prompts/svg-production-optimization.md` §6.

**Why:** An earlier, much larger version of this project attempted to
be a full hosted platform including an automated vectorization
subsystem. That subsystem alone would have required a computer-vision
R&D effort comparable in scope to the rest of the system combined, an
undecided build-vs-integrate decision (write a tracer from scratch vs.
wrap paid tools like Illustrator/Vector Magic), and — critically — an
unverified assumption that automated tracing could even meet a
"manufacturing-ready" quality bar for illustration-heavy concepts. None
of that was resolved before the project was rescoped to what it is
now: a research-and-prompting skill, explicitly not a production
pipeline. If automated vectorization is ever revisited, it should be
tested against a real benchmark (a set of concepts run through a
candidate engine, checked against actual cutting-machine output)
before being adopted — not assumed to work.

---

## ADR-7: Reasoning agents and image generation models are different categories

**Decision:** ChatGPT, Gemini, Claude, and Grok are "AI Chat Agents" —
used for the research/strategy/prompting stages. ChatGPT Images, Gemini
Image Generation, Midjourney, Flux, Ideogram, and Leonardo are "Image
Generation Models" — used only at State 11. See
`SYSTEM_INSTRUCTIONS.md` §6 and `documentation/glossary.md`.

**Why:** An earlier draft listed tools inconsistently — the same model
name appearing in a "target users" list but not in the actual prompt
template section, with no stated reason for the discrepancy. The
underlying issue was conflating two different capabilities: writing
strategy/prompts vs. generating images. Once separated into two
categories, the inconsistency resolved itself and the two lists stopped
needing to match.

**Also rejected:** per-model prompt templates (e.g. a Midjourney-
specific template with tool-specific parameter syntax). Rejected
because the actual prompt architecture in this system
(`prompts/prompt-engineering-framework.md`) is explicitly
model-independent by design — the same template structure is meant to
work across all supported image tools. Building per-tool templates
would have meant inventing syntax that was never part of the reviewed
system.

---

## ADR-8: A correction pass and a full sweep are different claims

**Decision:** No specific rule here — this is a process note, kept
because it's the reason ADR-4's "lesson learned" happened at all.

**What happened:** A correction pass fixed every issue that had
already been explicitly raised in review. It was then described as
complete. A subsequent full sweep of the entire document — checking
every section, not just the ones already flagged — found five more
live instances of the same bug pattern (IP silently folded into a
score) and a three-way dimension-list mismatch that the "complete"
correction pass had missed entirely.

**Why this is recorded:** "we fixed the cases we found" and "we
checked every case" are different claims, and it's easy to
accidentally present the first as if it were the second. If you're
doing a correction pass on this system in the future, say explicitly
which one you did.

---

## ADR-10: Multi-Tool Prompt Engineering Extensions (Superseding ADR-7's per-tool rejection)

**Decision:** While prompt *concepts* and baseline prompt architectures remain strictly model-agnostic, State 10 (Prompt Engineering) and `prompts/engine-tuning-guide.md` explicitly output **Multi-Tool AI Generation Prompt Packages** providing tailored syntax variants for Google Gemini / Imagen 3, Midjourney v6, ChatGPT / DALL-E 3, and Flux 1.1.

**Why:** Empirical testing across real image generation engines revealed that strict single-template model independence failed in practice:
1. **Google Gemini / Imagen 3** frequently added unwanted paper textures, 3D embossing, and drop shadows unless given positive inline anti-shadow commands (`"Pure 2D flat black ink graphic vector on solid white #FFFFFF background. Zero shadows, zero paper texture..."`).
2. **ChatGPT / DALL-E 3** automatically rewrote prompts under the hood unless given an explicit anti-rewrite directive (`"DALL-E Instruction: Do not alter or embellish..."`).
3. **Midjourney v6** requires `--no` parameter flags and `--style raw` to suppress lighting and depth.

Rather than forcing sellers to manually hack prompts when an AI engine renders unwanted shadows or textures, State 10 generates optimized variants for all major engines while preserving the underlying single concept. This decision explicitly supersedes the "Also rejected: per-model prompt templates" clause in ADR-7.
