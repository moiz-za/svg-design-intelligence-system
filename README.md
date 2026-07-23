# Etsy SVG Design Intelligence System (ESVG-DIS)

> An honest, research-first AI skill for creating original, commercially
> viable SVG product concepts for Etsy — before any image generation
> happens. Runs inside Claude, ChatGPT, Gemini, or Grok.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![Workflow States](https://img.shields.io/badge/workflow_states-13-blue.svg)](workflow/01-canonical-state-machine.md)
[![IP Gates](https://img.shields.io/badge/IP_gates-4-green.svg)](workflow/02-ip-gates.md)

---

## What This Is

Most AI-assisted design tools go straight from keyword to image. This
one doesn't. ESVG-DIS researches the market, screens for IP risk,
understands buyer psychology, evaluates commercial opportunity, and
develops genuinely differentiated concepts — all before a single
prompt gets sent to an image generator.

**This is a skill, not an app.** No account, no API key, no hosted
service. It's markdown files you load into an AI assistant you
already have.

---

## What It Actually Does

- ✅ Runs a full **market intelligence** pass — demand, buyer intent,
  trend classification, market gaps — before suggesting anything.
- ✅ Screens for **IP/trademark risk four separate times** (keyword,
  concept, prompt, and the finished artwork itself) — not once, and
  never as something a strong design score can override.
- ✅ Builds an actual **buyer persona and purchase motivation**
  analysis, not just a subject description.
- ✅ Scores **commercial opportunity** on six weighted dimensions
  before any creative work starts.
- ✅ Generates and ranks **30-50 concepts** on a five-dimension model,
  not just one idea.
- ✅ Produces **model-independent prompts** that work across ChatGPT
  Images, Gemini, Midjourney, Flux, Ideogram, and Leonardo.
- ✅ Gives explicit **SVG production guidance** — traceability,
  cutting-machine compatibility, complexity management.

## What It Explicitly Will NOT Do

- ❌ Won't generate the final SVG file, trace an image, or operate
  Illustrator/Inkscape for you.
- ❌ Won't upload anything to Etsy.
- ❌ Won't promise a sales outcome — commercial scoring is guidance,
  not a guarantee.
- ❌ Won't give legal advice — IP screening is analytical risk
  assessment, not a trademark clearance.
- ❌ Won't let a strong visual score excuse real IP risk. Every gate
  in this system can override every score.

---

## Quick Start

### Option A — Claude Code / Cowork (paid, recommended for regular use)

```bash
git clone https://github.com/moiz-za/svg-design-intelligence-system.git
cp -r svg-design-intelligence-system ~/.claude/skills/svg-design-intelligence-system
```

Restart Claude. Done — see `skill/SKILL.md` and `INSTALL.md` for
detail.

### Option B — Any tool, free or paid

1. Open `portable/ESVG-DIS-Instructions.md`.
2. Upload it as a file (or paste its contents) into a new chat with
   ChatGPT, Claude, Gemini, or Grok.
3. Paste the activation message at the end of that file.
4. Describe your product idea.

Full per-tool instructions: `INSTALL.md`.

---

## Using This for Free (No Paid Account Needed)

You don't need Claude Pro, ChatGPT Plus, or any subscription to use
the complete system. The `portable/` document contains the entire
workflow condensed into one file, designed specifically to work in a
plain, free-tier chat.

| Tool | Free tier works? | Notes |
|---|---|---|
| **Claude.ai (free)** | Yes | Upload or paste the portable doc in a regular chat. |
| **ChatGPT (free)** | Yes | Same pattern. |
| **Gemini (free)** | Yes | Same pattern. |
| **Grok (free)** | Yes | Same pattern. |

**What you keep on the free path:** the entire workflow — all four IP
gates, full scoring architecture, all prompt engineering guidance.

**What you lose on the free path:** cross-session memory (re-upload
the portable doc each new conversation) and the deeper per-topic
detail that lives in the full `knowledge/` files. See `INSTALL.md` for
the complete breakdown.

---

## How You Use It

**Researching a new product idea:**
> "I want to create Golden Retriever SVG designs for Etsy."

The system researches the market, screens the keyword for IP risk,
analyzes buyer psychology, evaluates the competition, and only then
scores the opportunity and starts developing concepts.

**Once you've picked a concept:**
The system engineers a complete generation prompt — subject, style,
composition, SVG requirements, negative prompt — ready to paste into
your image generator of choice.

See `examples/worked-examples.md` for a full pipeline walkthrough with
real scores at every stage.

---

## What's in the Box

```
svg-design-intelligence-system/
├── README.md                          you're here
├── SYSTEM_INSTRUCTIONS.md             entry point for the full multi-file version
├── INSTALL.md                         setup steps, free and paid
├── CHANGELOG.md                       version history
├── LICENSE                            MIT
├── CONTRIBUTING.md                    how to contribute
│
├── skill/
│   └── SKILL.md                       Claude Skill entry point
│
├── portable/
│   └── ESVG-DIS-Instructions.md       single-file condensed version, any tool
│
├── workflow/                          process logic: states, IP gates, scoring, retries
│   ├── 00-intake-and-interview.md
│   ├── 01-canonical-state-machine.md
│   ├── 02-ip-gates.md
│   ├── 03-scoring-architecture.md
│   └── 04-retry-and-halt-logic.md
│
├── knowledge/                         subject-matter frameworks
│   ├── market-intelligence.md
│   ├── competition-intelligence.md
│   ├── buyer-psychology.md
│   ├── ip-risk-and-originality.md
│   ├── commercial-opportunity-scoring.md
│   ├── creative-strategy.md
│   ├── concept-development.md
│   └── design-quality-review.md
│
├── prompts/                           prompt engineering + style templates
│   ├── prompt-engineering-framework.md
│   ├── svg-production-optimization.md
│   ├── prompt-refinement-guide.md
│   └── style-templates/
│       ├── universal.md
│       ├── vintage.md
│       ├── minimalist.md
│       ├── character.md
│       ├── typography.md
│       └── bundle-creation.md
│
├── integration/
│   └── etsy-seo-handoff.md            handoff to Etsy SEO/listing systems
│
├── examples/
│   └── worked-examples.md             complete pipeline walkthrough
│
└── documentation/
    ├── glossary.md
    ├── architecture-decisions.md      why things are built the way they are
    ├── installation-guide.md
    └── roadmap.md
```

---

## Who This Is For

- **Etsy digital product sellers** — SVG, PNG, DXF, EPS, Cricut,
  Silhouette, printable products.
- **AI-assisted designers** using any of the reasoning or image
  generation tools listed above.
- **New sellers** who need help finding a viable niche and avoiding
  common early mistakes (generic designs, IP risk, oversaturated
  markets).
- **Experienced sellers** who want faster, more structured research
  and stronger differentiation.

---

## What Makes It Different

| | Typical AI design prompting | This system |
|---|---|---|
| Starting point | Keyword to image | Keyword, research, strategy, concept, prompt |
| IP risk | Checked once, if at all | Checked 4 times, always as a hard gate, never averaged into a score |
| Concept generation | One idea | 30-50 concepts, ranked on 5 dimensions |
| Originality | Assumed | Actively engineered via a 4-layer differentiation model |
| Tool dependency | Often tool-specific prompts | Model-independent, same template across 6 image tools |
| Cost | Often requires a paid account | Full system works on free tiers |
| Scope honesty | Often implies it does everything | Explicit about what it won't do, no fake SVG automation |

---

## Realistic Expectations

This system makes research and creative strategy dramatically more
rigorous. It does not guarantee a design will sell, and it does not
replace your own judgment about your brand, your audience, or your
production capabilities. Scores throughout this system are decision
support, not verdicts — see `knowledge/commercial-opportunity-scoring.md`
§6.

---

## Companion Repository

Designed to work alongside
[`etsy-seller-seo-system`](https://github.com/moiz-za/etsy-seller-seo-system)
— that repo handles listing/SEO optimization once you have a finished
product. Neither depends on the other; use either independently or
together. See `integration/etsy-seo-handoff.md`.

---

## Contributing

See `CONTRIBUTING.md`. Before changing anything in `workflow/`, read
`documentation/architecture-decisions.md` — several design choices
that look simplifiable were already tried that way and reverted for a
specific, documented reason.

---

## License

MIT — see `LICENSE`. Not affiliated with Etsy.
