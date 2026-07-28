# Etsy SVG Design Intelligence System (ESVG-DIS) 🎨⚡

> **An honest, research-first AI skill for creating original, high-converting, and production-ready SVG product concepts for Etsy — before any image generation happens.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](CHANGELOG.md)
[![Workflow States](https://img.shields.io/badge/workflow_states-13-blue.svg)](workflow/01-canonical-state-machine.md)
[![IP Gates](https://img.shields.io/badge/IP_gates-4-green.svg)](workflow/02-ip-gates.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Supported Tools](https://img.shields.io/badge/compatibility-Claude%20%7C%20ChatGPT%20%7C%20Gemini%20%7C%20Grok-orange.svg)](#using-this-for-free-no-paid-account-needed)

---

## 🎯 What Is ESVG-DIS?

Most AI tools for Etsy sellers jump straight from **Keyword ➔ Image Prompt**. This reckless approach causes digital sellers to create generic artwork, untraceable vector shapes, or trademark-infringing designs that get shop accounts suspended or earn 1-star reviews from Cricut buyers.

**ESVG-DIS flips the script: Strategy & IP Verification First, Image Generation Last.**

It functions as an expert **commercial product strategist, IP risk reviewer, buyer psychologist, and vector production specialist** combined — providing the intelligence layer before you generate a single prompt.

> **💡 This is a modular AI skill, not a paid SaaS app.** No subscription, no API keys, no hosted service. It consists of open-source knowledge frameworks and state engines you load into Claude, ChatGPT, Gemini, or Grok.

---

## 🚀 Key System Features

| Feature | Description |
| :--- | :--- |
| 🛡️ **4-Stage IP Risk Gates** | Hard legal checkpoints (Keyword, Concept, Prompt, Final Artwork). **IP is a binary gate (PASS/MODIFY/BLOCK)** — high commercial scores can *never* override legal risk. |
| 🌐 **Dual-Mode Research** | Uses **Live Etsy Search** when web browsing is enabled; falls back to qualitative reasoning with an explicit `Data Source` tag on free/offline models. |
| 📊 **3-Level Scoring Architecture** | Evaluates **Opportunity Score** (State 6), **Concept Score** (State 9), and **Quality Score** (State 12) across weighted commercial dimensions. |
| ✂️ **Cricut & Vector Ready** | Enforces vector production thresholds (min detail ≥ 1/40th width, no tiny floating shapes, closed outlines, controlled line weight). |
| 🎭 **Buyer Psychology Layer** | Maps purchase motivations (Identity, Gift, Hobby, Emotion) and layers micro-niches to bypass oversaturated broad keywords. |
| 🎨 **Model-Agnostic Prompts** | Engineered prompts optimized for **ChatGPT Images, Midjourney, Flux, Ideogram, Leonardo, and Gemini** using `prompts/engine-tuning-guide.md`. |
| 🏷️ **Native 2026 Etsy SEO Engine** | Embedded complete listing creation engine in State 13 (140-char title, 13 search tags ≤20 chars, pricing, description, and Etsy AI Creation Disclosure). |
| 🆓 **100% Free Tier Compatible** | Full single-file portable edition available for free ChatGPT, Claude, Gemini, and Grok users. |

---

## 🔄 The Canonical 13-State Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           1. INTAKE (State 1)                           │
│      Collect product idea, target customer, product type, & style       │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     2. MARKET RESEARCH (State 2)                        │
│         Analyze demand, buyer intent, trends, & market gaps             │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│               3. KEYWORD IP SCREENING (State 3) [GATE 1]                │
│    Check against Trademark/Copyright Stoplist ➔ PASS / MODIFY / BLOCK   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │ (Pass)
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   4. BUYER PSYCHOLOGY (State 4)                         │
│           Identify buyer personas, identity layers, & micro-niches      │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    5. COMPETITION ANALYSIS (State 5)                    │
│             Extract market weaknesses & differentiation angles          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    6. OPPORTUNITY SCORING (State 6)                     │
│         Calculate Level 1 Score across 6 commercial dimensions          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │ (Score >= 7.5)
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│               7. CREATIVE STRATEGY & CONCEPT DEV (States 7-9)           │
│     Build 30-50 concepts ➔ [GATE 2: Concept IP] ➔ Score & Rank Level 2  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   10. PROMPT ENGINEERING (State 10)                     │
│   Build Vector-Optimized Prompt Package ➔ [GATE 3: Prompt IP Screening] │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│               11. ARTWORK & VECTOR PRODUCTION (States 11-13)            │
│   User Generates ➔ [GATE 4: Final IP] ➔ State 12 Review ➔ State 13 SEO  │
│   (Native 140-Char Title, 13 Search Tags ≤20 Chars, Pricing, & Disclosure)│
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Quick Start & Installation

### Option A — Claude Code / Cowork (Paid, Recommended)

Fastest setup for Claude Code or Cowork users:

1. Download **`esvg-dis.skill`** from the repository root.
2. Unzip into your skills folder:
   ```bash
   mkdir -p ~/.claude/skills/svg-design-intelligence-system
   unzip esvg-dis.skill -d ~/.claude/skills/svg-design-intelligence-system
   ```
3. Restart Claude Code/Cowork. The skill activates automatically when you ask about Etsy SVG product research!

### Option B — Any AI Model, Free or Paid (No Setup Needed)

Works on **ChatGPT (Free/Plus), Claude.ai (Free/Pro), Gemini (Free/Advanced), or Grok**:

1. Open [`portable/ESVG-DIS-Instructions.md`](portable/ESVG-DIS-Instructions.md).
2. Copy the entire file content (or upload it as a document in a new chat).
3. Paste the activation prompt found at the bottom of the file.
4. Describe your initial product keyword!

*(See [`INSTALL.md`](INSTALL.md) for detailed per-tool setup and troubleshooting.)*

---

## ⚖️ Why ESVG-DIS Beats Generic Prompting

| Dimension | Typical AI Prompting | ESVG-DIS System |
| :--- | :--- | :--- |
| **Workflow Starting Point** | Keyword ➔ Instant Image Generation | Research ➔ IP Gate ➔ Strategy ➔ Concept ➔ Prompt |
| **IP Protection** | Ignored or checked post-generation | **4 Mandatory Binary Gates** (Never averaged into a score) |
| **Commercial Intent** | Optimizes for visual aesthetics only | Evaluates Demand, Buyer Persona, Giftability, & Saturation |
| **Concept Variety** | Single prompt generation | Generates **30-50 concepts** scored across 5 dimensions |
| **Vector Production** | Complex gradients & untraceable textures | Enforces closed paths, flat fills, & cutting machine thresholds |
| **Cost / Platform** | Often tied to specific paid SaaS tools | **100% Free Tier Compatible** (Claude, ChatGPT, Gemini, Grok) |

---

## 📦 Repository Structure

```
svg-design-intelligence-system/
├── README.md                          you're here
├── SYSTEM_INSTRUCTIONS.md             entry point for full multi-file version
├── INSTALL.md                         setup instructions (free and paid)
├── CHANGELOG.md                       version history
├── LICENSE                            MIT License
├── CONTRIBUTING.md                    contribution guidelines
├── esvg-dis.skill                     packaged Claude Skill distribution archive
│
├── skill/
│   ├── SKILL.md                       Claude Skill execution engine (17 phases)
│   └── scripts/
│       └── bootstrap.py               state initializer (~/esvg-research/)
│
├── portable/
│   └── ESVG-DIS-Instructions.md       single-file edition for free-tier users
│
├── workflow/                          process logic, IP gates, & scoring
│   ├── 00-intake-and-interview.md
│   ├── 01-canonical-state-machine.md
│   ├── 02-ip-gates.md
│   ├── 03-scoring-architecture.md
│   └── 04-retry-and-halt-logic.md
│
├── knowledge/                         subject-matter frameworks
│   ├── market-intelligence.md         live search + reasoning fallback
│   ├── competition-intelligence.md    live search + reasoning fallback
│   ├── buyer-psychology.md
│   ├── ip-risk-and-originality.md
│   ├── commercial-opportunity-scoring.md
│   ├── creative-strategy.md
│   ├── concept-development.md
│   └── design-quality-review.md
│
├── playbooks/                         concrete, checkable tactical rules
│   ├── trademark-and-ip-stoplist.md   checkable wordlist & visual IP rules
│   ├── niche-saturation-reality-check.md 4-criteria saturation warning
│   ├── cutting-machine-thresholds.md   physical feature size limits (1/40th rule)
│   └── honest-diagnosis-pointers.md   diagnostic table for repeated failures
│
├── prompts/                           prompt engineering & style templates
│   ├── prompt-engineering-framework.md
│   ├── svg-production-optimization.md
│   ├── prompt-refinement-guide.md
│   └── style-templates/               universal, vintage, minimalist, etc.
│
├── integration/
│   ├── etsy-seo-handoff.md            native listing engine & single-pass execution
│   └── etsy-seo-engine/               native 2026 Etsy SEO rulebooks (seo-guide, listing-guide, policies, playbooks)
│
├── examples/
│   └── worked-examples.md             full pipeline walkthrough with real scores
│
└── documentation/
    ├── glossary.md
    ├── architecture-decisions.md      ADR records & design choices
    ├── usage-guide.md                 practical seller workflow
    └── roadmap.md
```

---

## 🏷️ Complete Self-Contained Etsy System

ESVG-DIS is a **100% self-contained suite** that handles both product creation and full Etsy listing generation natively out-of-the-box.

For non-SVG physical/digital products (mugs, t-shirts, physical crafts), a standalone companion repository [`etsy-seller-seo-system`](https://github.com/moiz-za/etsy-seller-seo-system) is also available.

---

## 📜 License & Disclaimer

* **License:** Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
* **Disclaimer:** ESVG-DIS provides commercial analysis and trademark awareness risk screening, not legal advice. The seller remains responsible for final trademark verification and marketplace compliance. Not affiliated with Etsy, Inc.
