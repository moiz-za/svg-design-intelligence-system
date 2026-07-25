# Changelog

## v1.1.0 — Skill Depth & Live Research

Built in direct response to a gap analysis against the companion
`etsy-seller-seo-system` repo — see
`documentation/architecture-decisions.md` for the reasoning behind
each addition below.

**Live research:**
- `knowledge/market-intelligence.md` and
  `knowledge/competition-intelligence.md` now instruct live Etsy
  search when available, with an explicit, labeled fallback to
  reasoning-based estimates when it isn't (no browsing tool, free-tier
  chat, or an obscure niche search returns nothing). Every research
  output now carries a `Data Source` tag so estimates are never
  presented with false confidence.

**Cross-session memory (deliberately lightweight):**
- New `state-templates/esvg-research/research-log.md` — a single-file
  research log, not a multi-file database (this system does research
  and concept development, not published-listing tracking, so it
  doesn't need SEO's heavier structure).
- New `skill/scripts/bootstrap.py` — idempotent state initializer for
  Claude Code/Cowork, tested end-to-end including idempotency.
- Free-tier equivalent: a Research Log Snapshot block printed at the
  end of a session for the user to paste back in next time — same
  protection, no infrastructure required.

**`skill/SKILL.md` — full rewrite:**
- From a 338-word pointer file to a ~1,800-word real execution engine:
  input auto-detection table, 17 numbered phases mapped to the
  canonical workflow, concrete output format templates, standalone
  capabilities (IP screening alone, concept comparison alone, resume
  from log), honest scope section, quick-reference numbers table.

**New `playbooks/` — concrete, checkable tactical rules** (the
knowledge files describe risk *categories* abstractly; these are the
actual lists/thresholds to check against):
- `trademark-and-ip-stoplist.md` — checkable franchise/brand/style-
  imitation word list plus scan algorithm, wired into all 3 text-based
  IP gates.
- `niche-saturation-reality-check.md` — precise 4-criteria trigger for
  when to honestly warn that a generic concept won't differentiate in
  an oversaturated niche, before spending effort on concept
  development.
- `cutting-machine-thresholds.md` — concrete, checkable production
  limits (minimum feature size, isolated elements, line weight,
  detail density) replacing vague "keep it simple" guidance.
- `honest-diagnosis-pointers.md` — a diagnostic table for repeated
  failures, naming the likely real cause (weak niche, generic
  strategy, wrong concept, or entirely out of this system's scope)
  instead of defaulting to "try again."

**Distribution:**
- New `esvg-dis.skill` — a packaged, downloadable zip of exactly what
  `SKILL.md` depends on (`workflow/`, `knowledge/`, `prompts/`,
  `integration/`, `playbooks/`, `state-templates/`, `skill/`).
  Verified to contain no build artifacts. Unzips directly into
  `~/.claude/skills/` — no git clone required.

**Fixed during this round:**
- All of `skill/SKILL.md`'s internal cross-references were missing
  their `../` prefix (the file lives one folder below repo root) —
  every link would have silently resolved to a nonexistent path. Fixed
  with a targeted find-replace and verified.
- A `__pycache__` artifact from testing `bootstrap.py` briefly leaked
  into the first packaging attempt — caught and excluded before
  shipping.

---

## v1.0.0 — Initial Release

**Core system:**
- Full canonical workflow: 13 states from Intake through SEO Handoff.
- Four-gate IP architecture (Keyword, Concept, Prompt, Final Artwork),
  with PASS/MODIFY/BLOCK decisions and per-gate scope rules.
- Three-level scoring architecture (Opportunity, Concept, Quality
  Score), with IP deliberately excluded from all three — IP is a gate,
  never a score.
- Retry limits and halt/escalation logic for every iterative stage.
- Eight knowledge frameworks: market intelligence, competition
  intelligence, buyer psychology, IP risk/originality, commercial
  opportunity scoring, creative strategy, concept development, design
  quality review.
- Prompt engineering framework, SVG production optimization guidance,
  six style-based prompt templates, and a prompt refinement guide.
- Etsy SEO system handoff integration.
- A full worked example (complete pipeline walkthrough with real
  scores) plus two shorter illustrative sketches.

**Access:**
- `skill/` — real Claude Skill package for Claude Code/Cowork (paid).
- `portable/` — single-file condensed version for any tool, free or
  paid tier.
- `INSTALL.md` — per-tool setup instructions, free and paid paths.

**Documentation:**
- Full glossary of every canonical term used across the system.
- Architecture decision record — the reasoning behind every corrected
  design decision, kept specifically so fixes don't get silently
  reversed.
- Roadmap with explicit cross-references to decisions already settled
  (so future proposals don't reopen closed questions without reading
  why they were closed).

**A note on how this system was built:** this repository was built
from a working specification that went through multiple rounds of
review before implementation. Several rounds of that review caught the
same class of bug recurring in different places — most notably, IP
risk being folded into a numeric score in several different sections
even after the rule "IP is gate-only" was established elsewhere in the
same document. The full history of what was caught and fixed is in
`documentation/architecture-decisions.md`, specifically ADR-8, which
is worth reading before assuming any part of this system is simpler
than it looks.

---

## Unreleased / Under Consideration

See `documentation/roadmap.md` for near-term and longer-term
possibilities, including explicit notes on what's already been
considered and rejected (model-specific prompt templates, automated
vectorization) so those questions aren't reopened without cause.
