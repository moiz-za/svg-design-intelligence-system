# Research Log

**Last updated:** (auto-updated by the skill on Claude Code/Cowork; for
other tools, the user pastes this back in at the start of a session —
see `SKILL.md` §Session State)

This is the entire state model for ESVG-DIS. Deliberately one file, not
a database — this system does research and concept development, not
published-listing tracking, so it doesn't need SEO's heavier
multi-file structure (no listing IDs, no refresh schedules, no SQR
imports — none of that maps to anything ESVG-DIS actually does).

**Purpose:** prevent the same niche from being re-researched from
scratch, and the same concept from being re-suggested, across separate
sessions. Nothing more.

---

## Researched Niches

| Date | Keyword/Niche | Opportunity Score | Data Source | Top Concept(s) Selected | IP-Blocked Concepts (don't resuggest) |
|---|---|---|---|---|---|
| *YYYY-MM-DD* | *example: Golden Retriever SVG* | *8.0 — Strong* | *Live Etsy Search* | *Vintage heritage badge / adventure companion* | *(none)* |

*The example row above shows the format. Remove it once real research
exists. The skill appends a new row after every completed research
pass through State 6 (Opportunity Scoring) — see
`workflow/01-canonical-state-machine.md`.*

---

## How This Gets Used

**At State 2 (Market Research):** before starting fresh research, check
this log for the same or a closely related keyword. If found:
- Show the user the prior result (score, date, top concept) and ask
  whether they want fresh research (markets change) or to build on the
  prior pass.
- If proceeding with fresh research, still avoid re-suggesting the
  exact same concept already listed as "Top Concept(s) Selected" for
  that niche — differentiate from it, don't repeat it.

**At State 8 (Concept Generation):** never regenerate a concept that
appears in the "IP-Blocked Concepts" column for the niche in question.

**Data Source column:** always carry over from whichever research mode
actually ran (Live Etsy Search or Reasoning-Based Estimate) — see
`knowledge/market-intelligence.md` §Dual-Mode Research. A logged score
from a reasoning-only pass is weaker evidence than one from live
search; don't treat them as equally reliable when deciding whether to
re-research.

---

## Notes

- Dates are appended, not overwritten — a niche can appear more than
  once if it's been researched at different times (markets change).
- This file is intentionally small. If it starts accumulating dozens
  of niches and becomes hard to scan, that's a signal the user has
  outgrown the lightweight model — not a reason to add more structure
  automatically. Flag it to the user rather than silently expanding
  the schema.
