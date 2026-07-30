# Etsy SVG Design Intelligence System (ESVG-DIS)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)](CHANGELOG.md)
[![GitHub Repo Stars](https://img.shields.io/github/stars/moiz-za/svg-design-intelligence-system?style=flat&label=stars)](https://github.com/moiz-za/svg-design-intelligence-system)
[![Last Commit](https://img.shields.io/github/last-commit/moiz-za/svg-design-intelligence-system)](https://github.com/moiz-za/svg-design-intelligence-system/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/moiz-za/svg-design-intelligence-system)](https://github.com/moiz-za/svg-design-intelligence-system)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Supported Tools](https://img.shields.io/badge/compatibility-Claude%20%7C%20ChatGPT%20%7C%20Gemini%20%7C%20Grok-orange.svg)](#free-tier-compatible)

> An honest, research-first AI skill for creating original, high-converting, and production-ready SVG product concepts for Etsy — before any image generation happens.

**Created & Maintained by:** [Moiz Zoaib Ali](https://moiz.solutions) ([@moiz-za](https://github.com/moiz-za)) · **Tools Portal:** [tools.moiz.solutions](https://tools.moiz.solutions) · **Contact:** [193383930+moiz-za@users.noreply.github.com](mailto:193383930+moiz-za@users.noreply.github.com)

---

## Table of Contents

- [What Is ESVG-DIS?](#what-is-esvg-dis)
- [Quick Demo](#quick-demo)
- [Key System Features](#key-system-features)
- [The Canonical 13-State Workflow](#the-canonical-13-state-workflow)
- [Why ESVG-DIS Beats Generic Prompting](#why-esvg-dis-beats-generic-prompting)
- [Quick Start & Installation](#quick-start--installation)
- [Repository Structure](#repository-structure)
- [Complete Self-Contained Etsy System](#complete-self-contained-etsy-system)
- [Community & Support](#community--support)
- [Author & Maintainer](#author--maintainer)
- [License & Disclaimer](#license--disclaimer)

---

## What Is ESVG-DIS?

Most AI tools for Etsy sellers jump straight from **keyword → image prompt**. This causes digital sellers to create generic artwork, untraceable vector shapes, or trademark-infringing designs that get shop accounts suspended.

**ESVG-DIS flips the script: Strategy & IP Verification First, Image Generation Last.**

It functions as an expert **commercial product strategist, IP risk reviewer, buyer psychologist, and vector production specialist** combined — providing the intelligence layer before you generate a single prompt.

> **This is a modular AI skill, not a paid SaaS app.** No subscription, no API keys, no hosted service. It consists of open-source knowledge frameworks and state engines you load into Claude, ChatGPT, Gemini, or Grok.

---

## Quick Demo

After loading the skill, describe a product idea and the system runs a full 13-state pipeline. Here's a condensed example of the output you get:

```
┌────────────────────────────────────────────────────────────┐
│ OPPORTUNITY SCORE: 8.2/10 │
├────────────────────────────────────────────────────────────┤
│ Demand: 8.5  ·  Buyer Intent: 8.0  ·  Competition Gap: 7.5 │
│ IP Gate 1: ✅ PASS (keyword cleared)                        │
│ Concept Score (top pick): 8.8/10 · Quality: 8.5/10          │
│                                                             │
│ Etsy Listing Title (≤140 chars):                            │
│ "Boho Mountain SVG · Wilderness Landscape | Digital Cut File"│
│ Tags: #mountain #boho #wilderness #svg #cutfile #cricut …   │
└────────────────────────────────────────────────────────────┘
```

Full concept matrices, raw research data, and prompt engineering rationale remain in session memory and are unlocked on demand (`"expand"`, `"full report"`).

---

## Key System Features

| Feature | Description |
| :--- | :--- |
| **Caveman Output Mode** | Default output style is crisp, high-density, bullet-first, and zero-fluff to minimize token consumption by up to 70%. Full raw reports remain preserved in state memory and rendered on demand (`"expand"`, `"full report"`). |
| **5 Immutable System Laws** | Non-bypassable directives enforcing zero state skips, zero hallucinations, binary IP supremacy, Caveman token efficiency, and 8-phase native Etsy SEO execution. |
| **4-Stage IP Risk Gates** | Hard legal checkpoints (Keyword, Concept, Prompt, Final Artwork). **IP is a binary gate (PASS/MODIFY/BLOCK)** — high commercial scores can *never* override legal risk. |
| **Dual-Mode Research & Policy Verification** | Uses live Etsy search & policy web verification when browsing is enabled; falls back to qualitative reasoning with an explicit `Data Source` tag on free/offline models. |
| **3-Level Scoring Architecture** | Evaluates **Opportunity Score** (State 6), **Concept Score** (State 9), and **Quality Score** (State 12) across weighted commercial dimensions. |
| **Cricut & Vector Ready** | Enforces vector production thresholds (min detail ≥ 1/40th width, no tiny floating shapes, closed outlines, controlled line weight). |
| **Buyer Psychology Layer** | Maps purchase motivations (Identity, Gift, Hobby, Emotion) and layers micro-niches to bypass oversaturated broad keywords. |
| **Multi-Tool Engine Prompts** | Engineered prompts optimized for **ChatGPT Images, Midjourney, Flux, Ideogram, Leonardo, and Gemini**. |
| **Native 8-Phase Etsy SEO Engine** | State 13 executes policy check, keyword overlap scan, 140-char title, 13 search tags ≤20 chars, 5-surface indexing, 8-block description with Etsy AI disclosure, alt text & Pinterest block, and research log sync. |
| **Automated Dual-Repo Policy Sync** | `scripts/sync_etsy_policy.py` auto-syncs policy and engine rulebooks bidirectionally with `etsy-seller-seo-system`. |
| **Strict Title & Tag Guardrails** | Enforces 6–12 word title limit (max 14), mandatory formula `[Primary Keyword] [Style Descriptor] \| [Format]`, prohibited subjective words stoplist. |
| **100% Free Tier Compatible** | Full single-file portable edition available for free ChatGPT, Claude, Gemini, and Grok users. |

---

## The Canonical 13-State Workflow

```
 1. INTAKE ──► 2. MARKET RESEARCH ──► 3. KEYWORD IP SCREENING [GATE 1]
                                           │ PASS
                                           ▼
 4. BUYER PSYCHOLOGY ──► 5. COMPETITION ANALYSIS ──► 6. OPPORTUNITY SCORING
                                                           │ Score ≥ 7.5
                                                           ▼
 7-9. CREATIVE CONCEPT DEV [GATE 2: CONCEPT IP] ──► 10. PROMPT ENGINEERING
                                                           │ [GATE 3: PROMPT IP]
                                                           ▼
 11-13. ARTWORK PRODUCTION [GATE 4: FINAL IP] ──► 12. QUALITY REVIEW
                                                   ──► 13. ETSY SEO HANDOFF
                                                        (title, tags, desc,
                                                         pricing, disclosure)
```

Each state checks the previous output before proceeding. Failed states trigger retry logic (with escalation after the 3rd attempt). IP is never negotiable — any gate can **BLOCK** the pipeline regardless of commercial score.

---

## Why ESVG-DIS Beats Generic Prompting

| Dimension | Typical AI Prompting | ESVG-DIS System |
| :--- | :--- | :--- |
| **Workflow Starting Point** | Keyword → Instant Image Generation | Research → IP Gate → Strategy → Concept → Prompt |
| **IP Protection** | Ignored or checked post-generation | **4 Mandatory Binary Gates** (never averaged into a score) |
| **Commercial Intent** | Optimizes for visual aesthetics only | Evaluates Demand, Buyer Persona, Giftability, & Saturation |
| **Concept Variety** | Single prompt generation | Generates **30–50 concepts** scored across 5 dimensions |
| **Vector Production** | Complex gradients & untraceable textures | Enforces closed paths, flat fills, & cutting machine thresholds |
| **Cost / Platform** | Often tied to specific paid SaaS tools | **100% Free Tier Compatible** (Claude, ChatGPT, Gemini, Grok) |

---

## Quick Start & Installation

### Option A — Claude Code / Cowork (Paid, Recommended)

1. Download `esvg-dis.skill` from the repository root.
2. Unzip into your skills folder:
   ```bash
   mkdir -p ~/.claude/skills/svg-design-intelligence-system
   unzip esvg-dis.skill -d ~/.claude/skills/svg-design-intelligence-system
   ```
3. Restart Claude Code/Cowork. The skill activates automatically when you ask about Etsy SVG product research.

### Option B — Any AI Model, Free or Paid (No Setup Needed)

Works on **ChatGPT (Free/Plus), Claude.ai (Free/Pro), Gemini (Free/Advanced), or Grok**:

1. Open [`portable/ESVG-DIS-Instructions.md`](portable/ESVG-DIS-Instructions.md).
2. Copy the entire file content (or upload it as a document in a new chat).
3. Paste the activation prompt found at the bottom of the file.
4. Describe your initial product keyword.

*(See [`INSTALL.md`](INSTALL.md) for detailed per-tool setup and troubleshooting.)*

---

## Repository Structure

```
svg-design-intelligence-system/
├── README.md               ← you are here
├── SYSTEM_INSTRUCTIONS.md   entry point for full multi-file version
├── INSTALL.md               setup instructions (free and paid)
├── CHANGELOG.md             version history
├── LICENSE                  MIT License
├── CONTRIBUTING.md          contribution guidelines
├── esvg-dis.skill           packaged Claude Skill distribution archive
│
├── skill/                   Claude Skill execution engine (17 phases)
│   ├── SKILL.md
│   └── scripts/
│       └── bootstrap.py     state initializer (~/esvg-research/)
│
├── portable/
│   └── ESVG-DIS-Instructions.md   single-file edition for free-tier users
│
├── workflow/                process logic, IP gates, & scoring
│   ├── 00-intake-and-interview.md
│   ├── 01-canonical-state-machine.md
│   ├── 02-ip-gates.md
│   ├── 03-scoring-architecture.md
│   └── 04-retry-and-halt-logic.md
│
├── knowledge/               subject-matter frameworks
│   ├── market-intelligence.md
│   ├── competition-intelligence.md
│   ├── buyer-psychology.md
│   ├── ip-risk-and-originality.md
│   ├── commercial-opportunity-scoring.md
│   ├── creative-strategy.md
│   ├── concept-development.md
│   └── design-quality-review.md
│
├── playbooks/               concrete, checkable tactical rules
│   ├── system-laws.md
│   ├── trademark-and-ip-stoplist.md
│   ├── niche-saturation-reality-check.md
│   ├── cutting-machine-thresholds.md
│   └── honest-diagnosis-pointers.md
│
├── prompts/                 prompt engineering & style templates
│   ├── prompt-engineering-framework.md
│   ├── svg-production-optimization.md
│   ├── prompt-refinement-guide.md
│   └── style-templates/
│
├── integration/
│   ├── etsy-seo-handoff.md
│   └── etsy-seo-engine/
│
├── examples/
│   └── worked-examples.md   full pipeline walkthrough with real scores
│
└── documentation/
    ├── glossary.md
    ├── architecture-decisions.md
    ├── usage-guide.md
    └── roadmap.md
```

---

## Complete Self-Contained Etsy System

ESVG-DIS is a **100% self-contained suite** that handles both product creation and full Etsy listing generation natively out-of-the-box.

For non-SVG physical/digital products (mugs, t-shirts, physical crafts), see the standalone companion repository [`etsy-seller-seo-system`](https://github.com/moiz-za/etsy-seller-seo-system).

---

## Community & Support

- **Report bugs & request features** — [Open a GitHub Issue](https://github.com/moiz-za/svg-design-intelligence-system/issues)
- **Contribute** — See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines
- **Star the repo** — Helps other sellers discover this project

---

## Author & Maintainer

Engineered and maintained by **Moiz Zoaib Ali**:

- **Personal Website:** [moiz.solutions](https://moiz.solutions)
- **AI Tools Directory:** [tools.moiz.solutions](https://tools.moiz.solutions)
- **GitHub Profile:** [@moiz-za](https://github.com/moiz-za)
- **Contact Email:** [193383930+moiz-za@users.noreply.github.com](mailto:193383930+moiz-za@users.noreply.github.com)

---

## License & Disclaimer

- **License:** Distributed under the **MIT License**. Copyright (c) 2026 Moiz Zoaib Ali. See [`LICENSE`](LICENSE) for details.
- **Disclaimer:** ESVG-DIS provides commercial analysis and trademark awareness risk screening, not legal advice. The seller remains responsible for final trademark verification and marketplace compliance. Not affiliated with Etsy, Inc.
