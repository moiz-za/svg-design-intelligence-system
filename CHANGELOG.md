# Changelog

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
