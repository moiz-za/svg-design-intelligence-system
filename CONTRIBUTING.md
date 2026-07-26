# Contributing

ESVG-DIS is meant to stay accessible, transparent, reusable, and
community-driven — see `documentation/usage-guide.md` §Open
Source Philosophy. Contributions are welcome.

---

## Before You Start

**If your change touches anything in `workflow/`** (the state machine,
IP gates, or scoring architecture), read
`documentation/architecture-decisions.md` first. Several things in
this system that look like they could be simplified or "fixed" were
already tried that way and reverted for a specific reason — the file
explains why. If you still think a change is right after reading it,
that's a legitimate reason to open a discussion, not a reason to skip
reading it.

**If your change adds a knowledge file, prompt template, or example**,
you're in lower-risk territory — these are additive and don't need to
touch existing architecture.

---

## What's Easy to Contribute

- **New style templates** (`prompts/style-templates/`) — following the
  existing template format.
- **New worked examples** (`examples/`) — following the format in
  `examples/worked-examples.md`. A full pipeline walkthrough with real
  (internally consistent) scores is more useful than a short sketch.
- **Expanded knowledge content** (`knowledge/`) — niche-specific
  patterns, additional buyer psychology examples, additional
  competition patterns. Keep new content consistent with the canonical
  models already established (five-dimension Concept Score,
  four-dimension Quality Score, six-dimension Opportunity Score) —
  don't introduce a new competing dimension list. See
  `documentation/glossary.md` if you're unsure what a term already
  means in this system.

---

## What Needs More Care

- **Changes to `workflow/02-ip-gates.md` or `workflow/03-scoring-architecture.md`**
  — these are the most cross-referenced files in the repo. A change
  here can silently break assumptions in every `knowledge/` file that
  references them.
- **Adding a new scored dimension anywhere** — check
  `documentation/architecture-decisions.md` ADR-1 and ADR-4 first. IP
  should never become a scored dimension again, and dimensions
  shouldn't be duplicated across scoring levels.
- **Adding a new AI tool to the reasoning/image-gen lists** in
  `SYSTEM_INSTRUCTIONS.md` §6 — make sure it goes in the correct
  category (see ADR-7) and that the tool split stays consistent
  everywhere it's referenced.

---

## Checklist Before Submitting

- [ ] Does this introduce a new scored dimension? If so, does it
      duplicate something already scored at another level?
- [ ] Does this touch IP handling anywhere? If so, does it keep IP as
      a gate, not a score?
- [ ] If this adds a cross-reference to another file, does that file
      actually say what you're citing it for?
- [ ] If this changes a worked example's numbers, do the numbers still
      add up under the stated formula?
- [ ] Have you run a search for the term/section you're changing
      across the *whole* repository, not just the file you're editing?
      (See `documentation/architecture-decisions.md` ADR-8 — a partial
      check that misses other live instances of the same issue is a
      known failure mode in this project's own history.)

---

## Reporting Issues

Open an issue describing: which file, what's inconsistent or wrong,
and — if you can — which other file it conflicts with. "This
contradicts X" is more actionable than "this seems off."
