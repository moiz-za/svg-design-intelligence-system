---
name: svg-design-intelligence-system
description: >
  Etsy SVG Design Intelligence System (ESVG-DIS). A market research,
  buyer psychology, IP risk screening, and prompt engineering skill for
  creating original, commercially viable SVG product concepts for
  Etsy. Use when the user wants to research an Etsy SVG product idea,
  evaluate a niche's commercial opportunity, develop original design
  concepts, screen for IP/trademark risk, or generate AI image
  prompts for SVG production.
---

# SVG Design Intelligence System — Skill Entry Point

## Installation

**This skill depends on the rest of the repository it ships with.**
Copy the **entire repository**, not just this folder, into your
Claude skills directory:

```bash
cp -r svg-design-intelligence-system ~/.claude/skills/svg-design-intelligence-system
```

Restart Claude Code or Cowork. The skill will be discovered via this
file (`skill/SKILL.md`), but it reads its actual operating logic from
the sibling folders one level up: `../SYSTEM_INSTRUCTIONS.md`,
`../workflow/`, `../knowledge/`, `../prompts/`, `../integration/`.

If you copy only this `skill/` folder without the rest of the
repository, the skill will load but won't be able to resolve any of
its own cross-references — it will not work correctly. This is a
known constraint of this repo's current structure (see
`../documentation/architecture-decisions.md` if curious why it's
structured this way rather than fully self-contained like some other
Claude skills).

---

## What This Skill Does

On activation, follow `../SYSTEM_INSTRUCTIONS.md` exactly. In summary:
research an Etsy SVG product idea through market intelligence, buyer
psychology, competition analysis, and commercial opportunity scoring;
screen for IP/trademark risk at four separate checkpoints; develop and
rank original creative concepts; engineer AI image-generation prompts;
and hand off a structured product-intelligence package once the user
has generated and approved final artwork.

This skill does **not** generate SVG files, trace images, or publish
listings — see `../SYSTEM_INSTRUCTIONS.md` §4 for the full scope
boundary.

---

## Activation

When this skill is loaded and the user describes a product idea,
keyword, or niche, begin at State 1 (Intake) —
`../workflow/00-intake-and-interview.md` — and proceed through the
canonical workflow in `../workflow/01-canonical-state-machine.md`.

Do not skip directly to concept generation or image prompts from a
bare keyword. Research and IP screening come first.
