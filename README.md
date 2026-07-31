<div align="center">

# Etsy SVG Design Intelligence System (ESVG-DIS)

### by [Moiz Solutions](https://tools.moiz.solutions)

[![Version](https://img.shields.io/badge/version-1.2.0-blue?style=flat-square)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/moiz-za/svg-design-intelligence-system?style=flat-square&label=stars)](https://github.com/moiz-za/svg-design-intelligence-system)
[![Last Commit](https://img.shields.io/github/last-commit/moiz-za/svg-design-intelligence-system?style=flat-square)](https://github.com/moiz-za/svg-design-intelligence-system/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/moiz-za/svg-design-intelligence-system?style=flat-square)](https://github.com/moiz-za/svg-design-intelligence-system)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Compatibility](https://img.shields.io/badge/compatibility-Claude%20%7C%20ChatGPT%20%7C%20Gemini%20%7C%20Grok-orange?style=flat-square)](#-installation)

**An honest, research-first AI skill for creating original, high-converting, and production-ready SVG product concepts for Etsy — before any image generation happens.**

**Strategy & IP verification first, image generation last.** No subscription, no API keys, no hosted service. Works on free tiers of Claude, ChatGPT, Gemini, or Grok.

---

</div>

## 📖 Table of Contents

- [Features](#-features)
- [Quick Demo](#-quick-demo)
- [How It Works](#-how-it-works)
- [Why ESVG-DIS Beats Generic Prompting](#-why-esvg-dis-beats-generic-prompting)
- [Installation](#-installation)
- [Repository Structure](#-repository-structure)
- [Companion Repository](#-companion-repository)
- [FAQ](#-faq)
- [Changelog](#-changelog)
- [Community & Support](#-community--support)
- [Author & Maintainer](#-author--maintainer)
- [License & Disclaimer](#-license--disclaimer)

---

## 🚀 Features

### 🦣 Caveman Output Mode
- Crisp, high-density, bullet-first default output — cuts token consumption by up to **70%**
- Full multi-column concept matrices, raw research data, and prompt rationale preserved in state — unlocked on demand (`"expand"`, `"full report"`)

### 📜 5 Immutable System Laws
Non-bypassable directives (`playbooks/system-laws.md`):
1. **Pipeline integrity** — all 13 states, 4 IP gates, and scoring run sequentially, zero skips
2. **Zero-hallucination evidence traceability** — empirical data or explicit `[Data Source: Reasoning Engine Fallback]` tagging
3. **Binary IP supremacy** — IP gates are hard PASS/MODIFY/BLOCK; commercial scores can *never* override legal risk
4. **Caveman output protocol** — concise by default, details on request
5. **Native listing engine mandate** — State 13 executes all 8 Etsy SEO phases in a single pass

### 🔒 4-Stage Binary IP Risk Gates
- Hard legal checkpoints: **Keyword, Concept, Prompt, Final Artwork**
- **IP is a gate, never a score** — high commercial scores can never override a BLOCK

### 🎯 3-Level Scoring Architecture
- **Opportunity Score** (State 6) · **Concept Score** (State 9) · **Quality Score** (State 12)
- IP deliberately excluded from all three — gate-only

### 🧠 Research-First Pipeline
- Live Etsy search + policy web verification when browsing is enabled
- Explicit `Data Source` tag fallback to qualitative reasoning on free/offline models
- **Buyer Psychology Layer** — maps Identity, Gift, Hobby, Emotion motivations + micro-niches to bypass oversaturated keywords

### 🖌️ Cricut & Vector Ready
- Enforced vector production thresholds: min detail ≥ 1/40th width, no tiny floating shapes, closed outlines, controlled line weight

### 🛠️ Multi-Tool Engine Prompts
- Engineered prompts optimized for **ChatGPT Images, Midjourney, Flux, Ideogram, Leonardo, and Gemini**

### 🏷️ Native 8-Phase Etsy SEO Engine (State 13)
- Policy check, keyword overlap scan, 140-char title, 13 search tags ≤20 chars, 5-surface indexing, 8-block description with Etsy AI disclosure, alt text & Pinterest block, research log sync
- **Strict title & tag guardrails** — 6–12 word limit (max 14), formula `[Primary Keyword] [Style Descriptor] | [Format]`, prohibited subjective words stoplist

### 🔄 Automated Dual-Repo Policy Sync
- `scripts/sync_etsy_policy.py` auto-syncs policy and engine rulebooks bidirectionally with `etsy-seller-seo-system` — zero drift

### 💸 100% Free-Tier Compatible
- Full single-file portable edition (`portable/ESVG-DIS-Instructions.md`) for free ChatGPT, Claude, Gemini, and Grok users

---

## 🖥️ Quick Demo

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

## ⚙️ How It Works

Most AI tools for Etsy sellers jump straight from **keyword → image prompt** — producing generic artwork, untraceable vector shapes, or trademark-infringing designs that get shop accounts suspended. ESVG-DIS flips the script: **Strategy & IP Verification First, Image Generation Last.**

It functions as an expert **commercial product strategist, IP risk reviewer, buyer psychologist, and vector production specialist** combined — providing the intelligence layer before you generate a single prompt.

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

Each state checks the previous output before proceeding. Failed states trigger retry logic (with escalation after the 3rd attempt). **IP is never negotiable** — any gate can BLOCK the pipeline regardless of commercial score. Generates **30–50 concepts** scored across 5 dimensions.

---

## 🏆 Why ESVG-DIS Beats Generic Prompting

| Dimension | Typical AI Prompting | ESVG-DIS System |
| :--- | :--- | :--- |
| **Workflow Starting Point** | Keyword → Instant Image Generation | Research → IP Gate → Strategy → Concept → Prompt |
| **IP Protection** | Ignored or checked post-generation | **4 Mandatory Binary Gates** (never averaged into a score) |
| **Commercial Intent** | Optimizes for visual aesthetics only | Evaluates Demand, Buyer Persona, Giftability, & Saturation |
| **Concept Variety** | Single prompt generation | Generates **30–50 concepts** scored across 5 dimensions |
| **Vector Production** | Complex gradients & untraceable textures | Enforces closed paths, flat fills, & cutting machine thresholds |
| **Cost / Platform** | Often tied to specific paid SaaS tools | **100% Free Tier Compatible** (Claude, ChatGPT, Gemini, Grok) |

---

## 🔧 Installation

### Option 1: Claude Code / Cowork (paid, recommended)

1. Download `esvg-dis.skill` from the repository root
2. Unzip into your skills folder:

```bash
mkdir -p ~/.claude/skills/svg-design-intelligence-system
unzip esvg-dis.skill -d ~/.claude/skills/svg-design-intelligence-system
```

3. Restart Claude Code/Cowork. The skill activates automatically when you ask about Etsy SVG product research.

### Option 2: Any AI model, free or paid (no setup needed)

Works on **ChatGPT (Free/Plus), Claude.ai (Free/Pro), Gemini (Free/Advanced), or Grok**:

1. Open [`portable/ESVG-DIS-Instructions.md`](portable/ESVG-DIS-Instructions.md)
2. Copy the entire file content (or upload it as a document in a new chat)
3. Paste the activation prompt found at the bottom of the file
4. Describe your initial product keyword

See [INSTALL.md](./INSTALL.md) for detailed per-tool setup and troubleshooting.

---

## 📦 Repository Structure

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
│       ├── bootstrap.py     state initializer (~/esvg-research/)
│       └── sync_etsy_policy.py  dual-repo policy sync engine
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

## 🤝 Companion Repository

ESVG-DIS is a **100% self-contained suite** that handles both product creation and full Etsy listing generation natively out-of-the-box.

For non-SVG physical/digital products (mugs, t-shirts, physical crafts), see the standalone companion repository [`etsy-seller-seo-system`](https://github.com/moiz-za/etsy-seller-seo-system).

- **ESVG-DIS System** creates the right *product*.
- **Etsy Seller SEO System** creates the right *listing*.

---

## ❓ FAQ

**Q: Is this a paid SaaS app?**  
A: No. It's a modular AI skill — open-source knowledge frameworks and state engines you load into Claude, ChatGPT, Gemini, or Grok. No subscription, no API keys, no hosted service.

**Q: Does it work on the free tier of my AI tool?**  
A: Yes. The full single-file portable edition (`portable/ESVG-DIS-Instructions.md`) works on free ChatGPT, Claude, Gemini, and Grok. Paid Claude Code/Cowork adds automatic state and cross-session memory.

**Q: Why is IP screening a hard gate instead of a score?**  
A: IP is a **binary gate (PASS/MODIFY/BLOCK)**. High commercial scores can *never* override legal risk — a design that's a trademark liability is blocked no matter how profitable it looks.

**Q: What happens when browsing is disabled (free/offline models)?**  
A: Research falls back to qualitative reasoning with an explicit `Data Source` tag, so estimates are never presented with false confidence.

**Q: What are the vector production requirements?**  
A: Min detail ≥ 1/40th of design width, no tiny floating shapes, closed outlines, and controlled line weight — so your designs actually cut on Cricut and similar machines.

**Q: Does this give legal advice?**  
A: No. ESVG-DIS provides commercial analysis and trademark awareness risk screening, not legal advice. The seller remains responsible for final trademark verification and marketplace compliance.

**Q: Is this affiliated with Etsy?**  
A: No. Not affiliated with Etsy, Inc.

---

## 📋 Changelog

Recent highlights:

| Version | Date | Summary |
|---------|------|---------|
| **v1.2.0** | 2026-07 | Caveman Output Mode + 5 Immutable System Laws, dual-repo policy sync |
| v1.1.0 | 2026-06 | Live research, August 2026 Etsy policy alignment, SKILL.md rewrite, packaged `.skill` archive |
| v1.0.0 | 2026-05 | Initial release — 13-state workflow, 4-gate IP architecture, 3-level scoring |

See full [CHANGELOG.md](./CHANGELOG.md) for details.

---

## 🤝 Community & Support

- **Report bugs & request features** — [Open a GitHub Issue](https://github.com/moiz-za/svg-design-intelligence-system/issues)
- **Contribute** — See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines
- **Star the repo** — Helps other sellers discover this project

---

## 👤 Author & Maintainer

Engineered and maintained by **Moiz Zoaib Ali**:
- **Personal Website:** [moiz.solutions](https://moiz.solutions)
- **AI Tools Directory:** [tools.moiz.solutions](https://tools.moiz.solutions)
- **GitHub Profile:** [@moiz-za](https://github.com/moiz-za)

---

## 📄 License & Disclaimer

- **License:** Distributed under the **MIT License**. Copyright (c) 2026 Moiz Zoaib Ali. See [`LICENSE`](./LICENSE) for details.
- **Disclaimer:** ESVG-DIS provides commercial analysis and trademark awareness risk screening, not legal advice. The seller remains responsible for final trademark verification and marketplace compliance. Not affiliated with Etsy, Inc.

---

<div align="center">

**Built by [Moiz Solutions](https://tools.moiz.solutions)** · Report issues on [GitHub](https://github.com/moiz-za/svg-design-intelligence-system/issues)

</div>
