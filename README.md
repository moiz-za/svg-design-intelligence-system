# Etsy SVG Design Intelligence System (ESVG-DIS)

**An open-source AI skill for commercial SVG research, strategy, and
premium prompt engineering.**

ESVG-DIS turns any capable AI assistant (ChatGPT, Claude, Gemini, Grok,
or similar) into a commercial SVG design strategist for Etsy sellers —
before a single image gets generated.

---

## What This Is

Most sellers can generate an image. Few can reliably generate:

- a design customers actually want
- a design that's commercially differentiated
- a design that avoids IP risk
- a design suitable for SVG/vector conversion
- a design that can compete in a saturated marketplace

ESVG-DIS solves the strategy problem *before* production begins. It
does not replace your creative tools — it's the intelligence layer that
guides research, concept development, and prompt engineering, then
hands off to your existing image-generation and vectorization workflow.

**This is a skill, not an app.** It's a set of markdown files you load
into your own AI agent. No account, no API key, no installation beyond
copying files.

---

## What This Is Not

ESVG-DIS does **not**:

- generate final SVG files
- automatically trace raster images
- operate Illustrator or Inkscape for you
- upload products to Etsy
- guarantee sales
- replace professional legal review of trademark/copyright questions

Your existing tools stay in the loop for artwork generation,
vectorization, and publishing. ESVG-DIS handles the thinking that
happens before and around those steps.

---

## Who It's For

- **Etsy digital product sellers** — SVG, PNG, JPG, DXF, EPS, Cricut,
  Silhouette, printable artwork, digital bundles.
- **AI-assisted designers** using ChatGPT, Gemini, Claude, Grok,
  Midjourney, Flux, Ideogram, Leonardo, or similar tools.
- **New sellers** who need help finding profitable niches, reading
  competition, and avoiding common early mistakes.
- **Experienced sellers** who want faster research, more scalable
  ideation, and stronger originality/differentiation.

---

## Installation

1. Download or clone this repository.
2. Upload the files into your AI assistant of choice (project files,
   custom GPT knowledge, Claude Project files, or equivalent).
3. Paste the setup message below to activate it.
4. Start with your first product idea, keyword, or niche.

### Setup Message

```
You are now operating using the Etsy SVG Design Intelligence System
(ESVG-DIS). Read SYSTEM_INSTRUCTIONS.md first and follow it exactly.
Analyze before creating. Prioritize commercial value, originality, IP
safety, and SVG production suitability, in that order when they
conflict.
```

### Example

```
User: I want to create Christmas SVG designs.

Agent: I'll analyze market demand, buyer motivation, competition, and
IP risk for this niche before generating any concepts or prompts.
```

See `examples/christmas-svg-workflow.md` for a complete worked run
through every stage.

---

## How It Works

ESVG-DIS follows a fixed research-to-prompt pipeline: market research →
IP screening → buyer psychology → competition analysis → opportunity
scoring → creative strategy → concept generation → concept-level IP
review → concept evaluation → prompt engineering → prompt-level IP
validation → you generate artwork → final-artwork IP review → design
quality review → handoff to your Etsy SEO process.

IP risk is checked four separate times along this path, and is always
a pass/fail gate — never something that gets averaged away by a strong
score elsewhere. Full detail: `SYSTEM_INSTRUCTIONS.md` and
`workflow/02-ip-gates.md`.

---

## Repository Structure

```
README.md                    you are here
SYSTEM_INSTRUCTIONS.md       load this into your agent first
workflow/                    process logic — states, gates, scoring, retries
knowledge/                   subject-matter frameworks (market, buyer psych, IP, etc.)
prompts/                     prompt engineering + per-tool templates
integration/                 handoff to Etsy SEO/listing systems
examples/                    complete worked workflows
documentation/               glossary, architecture history, roadmap
```

---

## Philosophy

This project is meant to stay:

- **accessible** — no paid tools required to use the core system
- **transparent** — every scoring rule and gate is documented, not a
  black box
- **community-driven** — contributions, corrections, and new prompt
  templates are welcome

See `CONTRIBUTING.md` for how to propose changes, and
`documentation/architecture-decisions.md` for the reasoning behind the
current design — including the mistakes that got caught and fixed
along the way.

---

## License

Open source. See `LICENSE`.
