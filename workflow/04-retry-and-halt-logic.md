# Retry & Halt Logic

No stage in this system retries indefinitely, and no stage fails
silently. This file is the single authoritative reference for both.

---

## 1. Retry Limits, By Stage

```
Market Research:              3 attempts
Concept Generation:           5 attempts
Concept IP Review:            3 attempts
Concept Revision:             3 attempts
Prompt Engineering:           3 attempts
Prompt IP Validation:         3 attempts
Final Artwork IP Review:      3 attempts
Design Review:                3 attempts
```

Every iterative state in the canonical workflow (see
`workflow/01-canonical-state-machine.md`) is covered by this table.
None are open-ended.

---

## 2. Failure Handling, By Category

| Failure | Trigger Example | Action |
|---|---|---|
| **Research Failure** | Insufficient market information | Request more information from the user |
| **Opportunity Failure** | No differentiation possible | Return to Market Research (if improvable) or halt (if not) |
| **IP Failure** | Trademark conflict at any gate | Block or redirect — scope depends on the gate, see `workflow/02-ip-gates.md` |
| **Concept Failure** | Concepts too generic | Generate new concepts |
| **Prompt Failure** | AI output unsuitable for SVG | Refine the prompt |
| **Review Failure** | Design Review repeatedly fails | Return to Prompt Engineering |

---

## 3. IP Gate Retry Behavior Specifically

IP gates (States 3, 8A, 10A, 11A) don't follow quite the same pattern
as other retries, because MODIFY and BLOCK mean different things:

**MODIFY** → returns to the specific upstream stage that needs
revision:
- Concept IP Review MODIFY → Concept Revision
- Prompt IP Validation MODIFY → Prompt Refinement
- Final Artwork IP Review MODIFY → regenerate from the same approved
  prompt (State 11)

**BLOCK** → does **not** retry automatically. A blocked IP direction
needs a strategic change, not another attempt at the same thing. It
produces an **IP Block Report** instead:

```
IP Block Report
- Reason
- Detected Risk
- Safer Alternatives
```

---

## 4. Opportunity Failure — The Judgment Call

State 6 (Opportunity Scoring) is the one place retry behavior requires
an actual judgment, not just a counter. When Opportunity Score comes
back low, ask:

> Can the opportunity be improved, or is the market direction
> fundamentally weak?

- **Improvable** (e.g. under-researched, needs a sharper angle) →
  return to Market Research, within its 3-attempt limit.
- **Fundamentally weak** (e.g. the niche itself has no viable angle
  regardless of research depth) → halt directly as
  `HALTED_OPPORTUNITY_FAILURE`, don't burn remaining research attempts
  on something that won't improve.

> **Saturation-Driven Low Score Rule (Cross-Wired Guidance):**
> When Opportunity Score comes back low (<5.5), explicitly inspect **Competition Difficulty**:
> - If **Competition Difficulty ≤ 2 (Extreme Saturation tier)**, the weak score is driven directly by market saturation.
> - **Action:** Do NOT output a generic, non-actionable `Opportunity Failure Report`. Instead, route directly to `playbooks/niche-saturation-reality-check.md` to provide the 3 actionable paths forward:
>   1. **`[a]` Proceed anyway:** Build hyper-differentiated concepts (pushing 3 of 4 originality layers).
>   2. **`[b]` Narrow the niche:** Pivot to a specific micro-niche / subculture layer and re-evaluate.
>   3. **`[c]` Explore a different direction:** Abandon the saturated keyword and explore an open niche.

In practice: if you've already used all 3 Market Research attempts and
the opportunity still scores low (and CD > 2), treat that as settled — don't keep
re-researching past the limit hoping for a different outcome. The
distinction above is for judgment *before* exhausting retries, not a
way to extend them.

**Output on halt (when CD > 2):**

```
Opportunity Failure Report
- Reason
- Failed Dimension(s)
- Score Breakdown
- Attempt History
- Alternative Opportunities
```

---

## 5. Terminal State

Every exhausted retry path — regardless of category — enters:

```
WORKFLOW_HALTED
```

This is not a silent stop. It always produces a structured report and
triggers escalation (§7 below).

---

## 6. Halt Categories

```
HALTED_RESEARCH_FAILURE
HALTED_OPPORTUNITY_FAILURE
HALTED_IP_FAILURE
HALTED_CONCEPT_FAILURE
HALTED_PROMPT_FAILURE
HALTED_REVIEW_FAILURE
```

Every failure in the §2 table above maps to exactly one of these
categories.

---

## 7. Human Escalation

After any `WORKFLOW_HALTED`, the system provides:

```
Failure Summary
Reason
Previous Attempts
Alternative Directions
Human Decision Required
```

**Default behavior: request a human decision.** The system does not
silently terminate, does not guess at a workaround, and does not
proceed on a lower-confidence path without saying so. If the user
wants a different default (e.g. auto-abandon and move to the next
archived concept without asking), that's a configuration choice to
make explicitly — it is not the default.

---

## 8. Human Review Checkpoints (Available, Not Just On Failure)

Independent of any halt, a human can step in at:

- Opportunity Approval (State 6)
- Concept Selection (State 9)
- Generated Artwork Review (State 11A / State 12)
- Final Product Decision (State 13)

These checkpoints exist whether or not anything has failed — Principle
5 (`SYSTEM_INSTRUCTIONS.md` §3) means the human is never locked out of
a decision just because the automated path is going fine.
