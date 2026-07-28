# Playbook — Niche Saturation Reality Check

**Purpose:** when a user wants to enter a heavily saturated niche with
a generic concept, give an honest reality check about realistic
differentiation difficulty — before they invest in full concept
development and prompt engineering.

**Why this exists:** telling someone "great, let's build concepts" for
a generic idea in an extremely saturated niche is dishonest if the
concept has no real differentiation angle. Better to flag the
difficulty at Opportunity Scoring (State 6), before Creative Strategy
and Concept Generation spend effort on something unlikely to stand
out.

**Dual-Branch Triggering:** This playbook applies to **BOTH**:
1. **Strong Opportunity Scores (≥ 7.5) with Saturation Risk (CD ≤ 2):** Warns the seller before spending effort on generic concepts.
2. **Weak Opportunity Scores (< 5.5) Driven by Extreme Saturation (CD ≤ 2):** Replaces generic, unhelpful halt logic with actionable 3-path guidance (*Proceed / Narrow / Redirect*) per `../workflow/04-retry-and-halt-logic.md` §4.

**Where it triggers:** after Opportunity Scoring (State 6), when ALL four criteria below hit.

---

## When to trigger (precise criteria)

ALL four must be true. If any one is false, skip this check and
proceed normally.

**Criterion 1 — Competition Difficulty in Extreme Saturation tier (score ≤ 2):**
Competition Difficulty score ≤ 2/10 (per
`../workflow/03-scoring-architecture.md` — scores 1–2 represent Extreme Saturation, while scores 3–4 represent High Competition without triggering mandatory saturation halt).

**Criterion 2 — Generic concept OR trend-cliché modifier:**
The user's original input lacks a genuine differentiation angle because it meets either (a) or (b):
- **(a) Bare generic input (triggers):** "Dog SVG," "Coffee mug SVG," "Halloween stickers."
- **(b) Trend-cliché modifier (triggers):** The input contains a modifier (e.g. "Cottagecore," "Boho," "Groovy 70s," "Y2K"), BUT this modifier itself has become an oversaturated default formula:
  * *In Live Mode:* verified if live search shows 20+ top listings executing the exact same visual formula (e.g., "Cottagecore Frog & Mushroom").
  * *In Reasoning Mode:* evaluate whether the modifier is a recognized marketplace trend cliché where the default visual formula is known to be saturated across Etsy/Pinterest. Do not skip Criterion 2(b) in Reasoning Mode simply because live search was unavailable.
- **Not generic / genuine angle (skip this check):** "Golden Retriever memorial SVG for senior dog owners," "vintage botanical coffee house emblem," "goblincore apothecary label SVG bundle for potion bottles."

**Criterion 3 — Mature, homogeneous competition (if live search ran):**
If Phase 6 (Competition Analysis) ran in Live mode, this criterion
requires: the current top listings show highly repetitive
patterns/compositions (the same 2-3 visual formulas repeated across
most top results) and appear to be from established sellers (many
reviews/sales signals if visible). If Phase 6 ran in Reasoning mode
(no live search available), rely on general knowledge of the category
instead — don't skip this criterion just because live data wasn't
available.

**Criterion 4 — No differentiation strategy proposed yet:**
Creative Strategy (State 7) hasn't yet identified a genuine
differentiation angle (concept, audience, style, or story
differentiation per `../knowledge/creative-strategy.md` §6).

If all four hit → output the reality check block below, before
proceeding to Concept Generation (State 8).

---

## The reality check output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ NICHE SATURATION REALITY CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before building concepts, you should see what you're walking into.

YOUR NICHE: "[keyword]"
DATA SOURCE: [Live Etsy Search / Reasoning-Based Estimate]

COMPETITION SNAPSHOT:
- Competition Difficulty: [X]/10 (Extreme saturation)
- Dominant pattern(s) repeated across most existing listings:
  [pattern 1], [pattern 2], [pattern 3]
- [If live data] Top listings appear to be from established,
  long-running shops.

WHY A GENERIC VERSION OF THIS WON'T DIFFERENTIATE:
A design that repeats [dominant pattern] will look like the hundreds
of other listings already doing exactly that. Differentiation, not
just execution quality, is what's missing from the current input.

WHAT WOULD ACTUALLY WORK HERE:

[1] Sharper micro-niche targeting. "[keyword]" is broad; "[keyword] for
    [specific audience/occasion/identity]" is a different, less
    saturated market. See `../knowledge/buyer-psychology.md` §4,
    micro-niche identification.

[2] A genuinely different style or story angle, not just a variation
    on the dominant pattern — see the Four Originality Layers in
    `../knowledge/ip-risk-and-originality.md` §5. Stacking at least 3
    of the 4 layers (concept, symbolic, composition, detail) is usually
    what separates a real differentiator from a cosmetic tweak.

[3] A different product angle entirely within the same broad interest
    area — e.g. if generic pet SVGs are saturated, a specific
    breed/life-stage/occasion combination may not be.

WHAT WOULD YOU LIKE TO DO?

[a] Proceed anyway — build concepts for "[keyword]" as-is
[b] Narrow the niche — give me a more specific angle (audience,
    style, or story) and I'll re-run Competition Analysis on that
[c] Explore a different concept within the same interest area

Default if no reply: [a] proceed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## After the reality check

- **[a] Proceed anyway:** continue to Concept Generation (State 8)
  normally, but note in the Research Log
  (`../state-templates/esvg-research/research-log.md`) that this
  warning was issued for this niche — useful context if the user
  returns later.
- **[b] Narrow the niche:** ask for the refined angle, re-run
  Competition Analysis (Phase 6) on the narrower niche. If Competition
  Difficulty improves meaningfully, proceed. If still Extreme, loop
  back to [a] or [c].
- **[c] Explore a different concept:** return to Creative Strategy
  (State 7) within the same broad interest area, looking for an
  under-served angle rather than the originally generic one.

---

## Tone rules

- Honest, not discouraging — state the pattern, not a verdict on the
  user's judgment.
- Concrete: real patterns from real data when Live mode ran, not vague
  warnings.
- Always offer 3 paths, never just "this won't work."
- Default to proceeding — the user decides; this playbook informs, it
  doesn't block. (Contrast with the IP gates, which genuinely can
  block — saturation is a commercial judgment call, not a legal one.)

---

## What this playbook does NOT do

- Does not decide for the user — they can always proceed anyway.
- Does not apply when the input already has a clear differentiation
  angle (Criterion 2 fails → no warning, proceed normally).
- Does not promise that a narrower niche will succeed either — it
  only says the current generic version is unlikely to.
