# IP Gates — Canonical Reference

This is the single authoritative file for how ESVG-DIS handles
intellectual property risk. If anything elsewhere in this repository
describes IP evaluation differently, this file governs.

**The one rule that matters more than any other in this file:**

> **IP is only ever a gate. It never contributes to a score.**

IP risk decides *whether a direction is allowed to continue.* It never
gets averaged in with commercial appeal, visual quality, or any other
scored dimension. A concept with real IP risk cannot be waved through
because it scores well elsewhere. See
`workflow/03-scoring-architecture.md` for why gates and scores are
architecturally separated.

---

## 1. Philosophy

> Inspiration is allowed. Imitation is not.

The job is to tell the difference between **creative influence** and
**derivative copying.** A successful marketplace design is recognizable,
valuable, and independently created — not a redraw of something that
already exists.

---

## 2. The Five Risk Categories

Evaluate every keyword, concept, and prompt against these:

1. **Trademark risk** — brand names, team names, character names,
   company logos, official slogans. Ask: does this reference a known
   brand? Would a buyer associate it with a specific company?
2. **Copyright risk** — movie characters, cartoon characters, famous
   artwork, recognizable fictional designs, copied illustrations. Ask:
   is this based on specific existing artwork? Would removing small
   details still leave it identifiable?
3. **Style imitation risk** — never prompt "in the style of [living
   artist]." Use artistic characteristics, visual techniques, and
   historical references instead.
   - Avoid: `Create a design like Artist X`
   - Better: `Create a hand-engraved vintage illustration with detailed
     line work, traditional printmaking characteristics, and antique
     botanical composition.`
4. **Franchise association risk** — fictional universes, famous
   characters, branded events, recognizable mascots. Warn the user
   before concept development, not after.
5. **Marketplace similarity risk** — not a legal issue, a commercial
   one: a design can be fully original and still be commercially weak
   because it's indistinguishable from thousands of existing listings
   (e.g. generic pumpkin + generic text + common font). This risk feeds
   differentiation work, not the IP gates below — see
   `knowledge/ip-risk-and-originality.md` for the originality-engineering
   side of this.

---

## 3. The Four Gates

Four checkpoints exist across the workflow. Each uses the same decision
vocabulary: **PASS / MODIFY / BLOCK.**

| # | Gate | State | Scope of a BLOCK |
|---|------|-------|-------------------|
| 1 | Keyword IP Screening | State 3 | Entire opportunity/direction |
| 2 | Concept IP Review | State 8A | Single concept only |
| 3 | Prompt IP Validation | State 10A | Single prompt direction |
| 4 | Final Artwork IP Review | State 11A | Single generated artwork |

Notice the scope narrows as the workflow progresses — an early BLOCK
kills the whole direction because the *input itself* is unsafe; a late
BLOCK only discards the one artifact in question, because everything
upstream of it already passed review.

### Gate 1 — Keyword IP Screening (State 3)
Runs after Market Research, before Buyer Psychology. Catches unsafe
inputs at the source.

```
Input: "Disney Halloween SVG"

Risk Level: High
Reason: Contains protected brand reference.
Decision: BLOCK
Recommendation: Explore original Halloween themes without brand
                 association.
```

BLOCK here terminates the entire direction and suggests alternatives —
the opportunity itself is unsafe, not just one execution of it.

### Gate 2 — Concept IP Review (State 8A)
Runs after Concept Generation. The market opportunity already passed
Gate 1 — this checks whether a *specific concept* introduces risk the
keyword didn't have. Example: "teacher niche" passes Gate 1 fine, but
one specific concept uses a trademarked phrase.

BLOCK here removes only that concept; the workflow continues evaluating
the remaining concepts in the batch. It does not restart research.

### Gate 3 — Prompt Validation (State 10A)
Runs after Prompt Engineering, before the user generates any artwork.
Checks the actual prompt text for protected references, copied styles,
famous characters, or trademarked phrases that may have crept in during
prompt drafting even though the underlying concept was clean.

BLOCK here removes the unsafe prompt elements and returns to Prompt
Engineering — the concept itself doesn't need to be re-evaluated.

### Gate 4 — Final Artwork IP Review (State 11A)
Runs after the user generates artwork, before Design Review. This gate
exists because the first three gates all evaluate *intent* — the
keyword, the concept, the prompt text. None of them can see the actual
pixels an image-generation model produces. A clean prompt can still
generate an unsafe image (a hallucinated logo, a too-close resemblance
to a known character). This is the only gate that checks the finished
output itself.

- **PASS** → continue to Design Review.
- **MODIFY** → return to User Generation Phase; regenerate from the
  same already-approved prompt.
- **BLOCK** → return to Prompt Engineering; the prompt itself needs
  revision, since simply regenerating would likely repeat the same
  issue.

---

## 4. Decision Actions, Universally

| Decision | Meaning | Action |
|---|---|---|
| **PASS** | Original, generic, or independently created | Continue |
| **MODIFY** | Influenced by common themes, unclear similarity, possible confusion | Revise before proceeding |
| **BLOCK** | Direct trademark use, famous characters, copied franchise references, protected slogans | Stop the current direction (scope per gate, see table above); offer safer alternatives |

---

## 5. Retry Limits

Every gate's MODIFY path is retry-limited — none of them loop
indefinitely:

```
Concept IP Review:        3 attempts
Prompt IP Validation:     3 attempts
Final Artwork IP Review:  3 attempts
```

Exhausting retries at any gate produces a structured report and follows
the halt/escalation rules in `workflow/04-retry-and-halt-logic.md` —
it does not fail silently, and it does not proceed anyway.

---

## 6. IP Risk vs. IP Safety — Same Axis, Inverse Numbers

These two terms describe the same measurement from opposite directions.
Never treat them as two different checks.

```
IP Safety Score = 10 − IP Risk Score
```

Example: IP Risk 8/10 ⟺ IP Safety 2/10. Both numbers describe the same
underlying risk level.

---

## 7. IP Safety vs. Originality — Different Axes, Don't Confuse Them

**IP Safety/Risk** (this file) is a legal-exposure gate: trademark,
copyright, franchise association. **Originality** is a craft-quality
score measuring how differentiated and creatively distinct a concept
is — it's one of the five dimensions in Concept Score (see
`workflow/03-scoring-architecture.md` and
`knowledge/ip-risk-and-originality.md`). A concept can be perfectly
IP-safe and still score low on originality (e.g. a generic heart icon —
zero legal risk, zero differentiation). The two are evaluated
separately and should never be merged into one number.

---

## 8. Reporting Standard

Every IP assessment reports both values and the decision, not just a
pass/fail flag:

```
IP Assessment

Risk Level: Low
Risk Score: 2/10
Safety Score: 8/10
Decision: PASS
```

---

## 9. Disclaimer

ESVG-DIS provides analytical guidance, not legal advice. The user
remains responsible for final design review, trademark verification,
copyright compliance, and marketplace policy compliance. Never present
a PASS/MODIFY/BLOCK decision as a legal guarantee.
