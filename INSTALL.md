# Installation Guide

Two ways to install this system, depending on your account type and
tool.

---

## Option A — Claude Code / Cowork (paid: Claude Pro/Max)

```bash
git clone https://github.com/moiz-za/svg-design-intelligence-system.git
cp -r svg-design-intelligence-system ~/.claude/skills/svg-design-intelligence-system
```

Restart Claude Code or Cowork. The skill is discovered automatically
via `skill/SKILL.md`. This is the recommended path if you're on a paid
Claude plan — no copy-pasting between sessions, and all cross-file
references resolve correctly since the whole repo is present.

**Note:** copy the entire repository folder, not just the `skill/`
subfolder — see `skill/SKILL.md` for why.

---

## Option B — Any tool, free or paid: the portable document

This works identically on ChatGPT (free or Plus), Claude.ai (free or
Pro), Gemini (free or paid), or any other AI chat interface.

1. Open `portable/ESVG-DIS-Instructions.md` in this repository.
2. Copy the entire file contents, or download it and upload it as a
   single file attachment in a new chat.
3. Start a new conversation and paste the setup message from the end
   of that file (or from `README.md`).
4. Describe your product idea, keyword, or niche.

That's the whole setup. No account upgrade, no custom GPT, no Project
required.

---

## Per-Tool Notes

| Tool | Free tier | Notes |
|---|---|---|
| **Claude.ai (free)** | ✅ Works | Upload the portable doc as a file, or paste it, in a regular chat. Daily message cap applies. |
| **ChatGPT (free)** | ✅ Works | Same pattern — paste or upload the portable doc as your first message. |
| **Gemini (free)** | ✅ Works | Same pattern. Handles long instructions well. |
| **Grok (free)** | ✅ Works | Same pattern. |
| **Claude Pro (Projects)** | ✅ Works, improved | Upload the entire repository's markdown files to a Project's knowledge base — you get the full cross-referenced multi-file version instead of the condensed portable one. |
| **ChatGPT Plus (Custom GPT)** | ✅ Works, improved | Same idea: create a Custom GPT, upload the repo's `.md` files under Configure → Knowledge. |
| **Claude Code / Cowork** | Requires Claude Pro/Max | See Option A above — this is the only path that gets automatic skill discovery without manual setup each session. |

---

## What You Keep on the Free Path

- The complete workflow: research, IP screening, buyer psychology,
  competition analysis, opportunity scoring, concept development,
  prompt engineering.
- All four IP gates and the full scoring architecture.
- Everything in `portable/ESVG-DIS-Instructions.md` — it's a condensed
  version of the same system, not a stripped-down one.

## What You Lose on the Free Path

- Cross-session memory — you'll need to re-paste or re-upload the
  portable doc at the start of every new conversation.
- The deeper per-topic detail in the full `knowledge/` and `prompts/`
  files (the portable doc condenses these; the full multi-file version
  has more worked examples and edge-case guidance per topic).
- Automatic skill discovery (Claude Code/Cowork only recognize
  `SKILL.md`-based skills, which requires a paid plan to run at all).

If you're doing occasional research on 1-5 product ideas, the free
path is enough. If you're running this regularly across many niches,
the paid Claude Code/Cowork path removes the re-upload friction.

---

## Troubleshooting

**"The AI seems to skip straight to generating an image prompt."**
Make sure you pasted the full setup/activation message, not just the
document. The activation message is what tells the model to actually
follow the workflow instead of just treating the document as
background reading.

**"I'm not sure which knowledge file to reference."**
If you're using the portable doc, you don't need to — everything
essential is condensed into that one file. If you're using the full
multi-file version, start at `SYSTEM_INSTRUCTIONS.md`; it links to
everything else in the right order.
