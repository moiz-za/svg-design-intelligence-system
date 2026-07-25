# Playbook — Honest Diagnosis Pointers

**Purpose:** when something keeps failing, name the *actual* likely
cause instead of defaulting to "try again with a better prompt/design."
Not every problem this system encounters is a design problem — some
are market problems, some are expectation problems, and pretending
otherwise wastes the user's retries and money.

**Where this applies:** any repeated failure — Opportunity Score
staying low across re-research, Concept Score staying low across
regeneration, Design Review repeatedly failing, or a user reporting
that a finished, approved product still isn't selling.

---

## Diagnostic Table

| Symptom | Likely real cause | What NOT to do | What to actually say |
|---|---|---|---|
| Opportunity Score stays low even after re-researching (near/at the 3-attempt limit in `../workflow/04-retry-and-halt-logic.md`) | The niche itself may be fundamentally weak, not under-researched | Keep suggesting "try a different keyword phrasing" indefinitely | Apply the judgment call in `../workflow/04-retry-and-halt-logic.md` §4 directly — say plainly this may be a weak market, not a research gap |
| Concept Score stays low across multiple regenerations at State 8/9 | The Creative Strategy (State 7) itself may be generic, not the individual concepts | Keep generating more concepts from the same weak strategy | Go back one stage — the Creative Brief needs a sharper differentiation angle, not more volume of concepts from the same angle |
| Design Review keeps failing (State 12) after 2+ Prompt Engineering revisions | The underlying *concept* may not translate well to SVG, not the prompt wording | Keep tweaking prompt language indefinitely | Per `../prompts/prompt-refinement-guide.md` §"When to stop refining," suggest returning to Concept Ranking (State 9) for a different concept from the portfolio |
| User reports a finished, approved product "isn't selling" | This is now a listing/SEO/marketplace visibility problem, or a pricing problem, or simply insufficient time on the marketplace — not a design-system problem | Try to re-diagnose it as a design flaw and offer to regenerate | Say plainly: this is now outside ESVG-DIS's scope (see `../SYSTEM_INSTRUCTIONS.md` §4) and route to `../integration/etsy-seo-handoff.md` — the SEO/listing system, not this one, is built to diagnose sales performance |
| Niche saturation reality check (`niche-saturation-reality-check.md`) was shown and dismissed, and the resulting concepts still score low on Differentiation | The user chose to proceed despite the warning — that's a legitimate choice, but the outcome isn't a system failure | Act surprised or repeat the warning again | Acknowledge plainly: this is the differentiation cost that was flagged earlier; offer options [b] or [c] from that playbook again if they'd like to reconsider |
| IP gate keeps BLOCKing regenerated concepts for the same niche | The niche itself may sit close to protected territory (see Franchise Association Risk, `../knowledge/ip-risk-and-originality.md` §2) | Keep regenerating hoping one slips through | Say plainly this niche has a structural IP problem, not a one-off bad concept, and suggest a genuinely different angle |

---

## The general principle

Before recommending "try again," ask: **would trying the same action
again plausibly produce a different result, or is the actual bottleneck
one stage upstream (or entirely outside this system's scope)?**

If the bottleneck is upstream → say so, and go back to that stage
rather than iterating downstream indefinitely.

If the bottleneck is outside ESVG-DIS's scope entirely (listing
optimization, pricing, marketplace timing, seller reputation) → say so
plainly and route to the right resource, per
`../SYSTEM_INSTRUCTIONS.md` §4. Don't stretch this system's scope to
sound more helpful than it actually can be — see the Honest Scope
section in `../skill/SKILL.md`.

---

## Tone rules

- State the likely cause directly, don't hedge it into vagueness.
- Never blame the user's execution when the more likely cause is
  structural (a weak niche, a generic strategy, an out-of-scope
  problem).
- Always pair the diagnosis with a concrete next step, not just a
  named problem.
