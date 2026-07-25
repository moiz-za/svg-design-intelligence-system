# Installation & Usage Guide

For installation steps and per-tool setup (free and paid), see
`INSTALL.md` at the repository root — this file doesn't repeat those.
It covers two things neither `README.md` nor `INSTALL.md` does: the
practical seller-facing workflow (as distinct from the internal state
machine), and the open-source contribution philosophy.

---

## No Programming Experience Required

ESVG-DIS is an AI knowledge package — markdown files loaded into an AI
assistant's context. There's nothing to compile, run, or configure
beyond uploading the files and pasting the setup message from
`README.md`.

---

## The Practical Seller Workflow

This is deliberately a simpler view than the 13-state canonical
workflow (`workflow/01-canonical-state-machine.md`) — that file is
for understanding or extending the system's internals; this is what
it actually feels like to use as a seller:

```
Research
↓
Review Opportunity
↓
Select Concept
↓
Generate Artwork
↓
Create SVG Files
↓
Optimize Listing
↓
Publish
```

Everything through "Create SVG Files" is ESVG-DIS-assisted. "Optimize
Listing" and "Publish" happen in a separate SEO tool — see
`integration/etsy-seo-handoff.md`.

---

## Open Source Philosophy

This project is meant to stay:

- **Accessible** — no paid tools required to use the core system.
- **Transparent** — every scoring rule and gate is documented in
  `workflow/`, not a black box.
- **Reusable** — fork it, adapt it to a different marketplace, extend
  it to a different product category.
- **Community-driven** — contributions are welcome.

Users are encouraged to modify frameworks, improve prompts, add
examples, and contribute improvements back. See `CONTRIBUTING.md` for
how.

Before changing anything in `workflow/`, read
`documentation/architecture-decisions.md` first — several design
choices there look arbitrary until you see what was tried before them.
