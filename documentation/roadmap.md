# Roadmap

The goal is continuous improvement while maintaining the core
philosophy — see `documentation/architecture-decisions.md` before
proposing changes to anything already decided there.

---

## Current State (v1.0)

Complete:

- Market intelligence framework
- Competition analysis
- Buyer psychology
- IP risk/originality framework (four-gate architecture)
- Three-level scoring architecture
- Creative strategy
- Prompt engineering
- SVG production guidance (guidance only — see ADR-6)
- Etsy SEO integration concept

---

## Near-Term (v1.1 Candidates)

**Expanded knowledge base** — more niche research examples, style
libraries, buyer psychology patterns, seasonal calendars. Low-risk
additive work; doesn't touch existing architecture.

**Better prompt systems** — prompt testing examples, failure
correction methods. ⚠️ **Not included:** model-specific prompt
optimization. This was already considered and explicitly rejected —
see `documentation/architecture-decisions.md` ADR-7. The prompt
architecture is deliberately model-independent; if you're proposing
per-tool templates, read ADR-7's reasoning first.

**More industry examples** — additional worked workflows for
weddings, professions, holidays, hobbies, family products, following
the pattern in `examples/worked-examples.md`.

---

## Longer-Term (v2.0 Possibilities)

**Analytics feedback loop** — sellers provide views, favorites, sales,
and conversion data so the system learns from real outcomes.
⚠️ **Scope note:** this requires marketplace publishing integration,
which is explicitly out of scope for the core system (see
`SYSTEM_INSTRUCTIONS.md` §4 and `integration/etsy-seo-handoff.md` §7).
Any analytics capability should be built as an optional adapter, not
merged into the core — don't reopen the publishing-scope question that
was already settled.

**Community knowledge system** — users contribute successful concepts,
failed experiments, and market insights back to a shared knowledge
base.

**Advanced automation** — potential integrations with keyword tools,
Etsy analytics, trend monitoring, competitor tracking. Note this list
does **not** include automated vectorization — see ADR-6 for why that
was deliberately descoped, and what would need to be true before
revisiting it.

---

## Long-Term Vision

To become an open-source intelligence framework that helps independent
creators compete with professional design teams by combining market
research, creative strategy, and AI-assisted production knowledge.

---

## Guiding Philosophy

AI should not replace creativity — it should amplify research ability,
strategic thinking, creative exploration, and production quality. The
best results come from Human Creativity + AI Intelligence + Market
Understanding + Professional Execution, together — not from
automating any one of them away.
