# Prompt Engineering Framework

Used in **State 10 — Prompt Engineering**, converting an approved
concept into a generation prompt. For style-specific templates, see
`prompts/style-templates/`. For the IP check that follows this stage,
see State 10A in `workflow/02-ip-gates.md`. For SVG-specific technical
depth beyond what's here, see `prompts/svg-production-optimization.md`.

---

## 1. Purpose

Convert approved concepts into high-performance AI image-generation
prompts. The objective is not "create a beautiful image" — it's create
unique commercial artwork that is SVG-friendly, traceable, and
production-ready. A gorgeous image that can't be cleanly vectorized has
failed the actual job.

---

## 2. Philosophy

A professional SVG prompt is not a description — it's a technical
creative specification.

- Weak: "Create a Halloween witch SVG."
- Strong: "Create a premium monochrome vector-style Halloween witch
  emblem designed for Cricut SVG conversion with clean closed shapes,
  balanced composition, strong silhouette, flat black lines, and
  original storytelling elements."

The difference isn't length for its own sake — every added detail in
the strong version constrains the output toward something that will
actually vectorize cleanly.

---

## 3. Prompt Architecture

Every final prompt should contain: Subject + Concept + Audience +
Style + Composition + SVG Requirements + Technical Restrictions +
Originality Requirements + Negative Prompt.

---

## 4. Subject Definition

Define the main object, supporting objects, symbolism, and the
relationship between elements — not just a label.

- Weak: "Dog design"
- Strong: "A loyal golden retriever represented as a vintage adventure
  companion emblem with symbolic outdoor elements."

---

## 5. SVG Technical Requirements

Every SVG-oriented prompt should include:

```
black and white only
flat vector appearance
clean outlines
consistent line weight
closed shapes
high contrast
trace-friendly
minimal unnecessary detail
no gradients
no shadows
no realistic textures
```

---

## 6. Composition Requirements

Define balance, hierarchy, spacing, silhouette clarity, and focal
point. E.g.: "centered composition, strong readable silhouette,
professional badge layout, balanced negative space."

---

## 7. Originality Requirements

Instruct the model to avoid: generic stock imagery, common marketplace
layouts, existing characters, brand references, copied designs,
predictable symbols.

Instruct it to pursue: unique interpretation, unexpected symbolism,
original composition, premium collectible appearance.

This is where the Originality Layers from
`knowledge/ip-risk-and-originality.md` §5 actually get translated into
prompt language — don't just say "make it original," specify which
layers (concept, symbolic, composition, detail) you want pushed.

---

## 8. Negative Prompt Framework

Every generation prompt should include negative instructions:

```
Avoid:
color
gradients
photorealism
3D rendering
shadows
watermarks
logos
copyrighted characters
messy details
AI artifacts
uneven lines
complex backgrounds
```

Note: "copyrighted characters" and "logos" belong in the negative
prompt as a preventive instruction to the model — but this is not a
substitute for the actual Prompt IP Validation gate (State 10A). The
gate checks the prompt text itself for risk; the negative prompt is
one input to generation, not a review step.

---

## 9. Multi-Tool Engine Optimization Architecture

Different AI engines (Google Gemini, Midjourney, ChatGPT/DALL-E, Flux) interpret vector prompts differently. To prevent Gemini paper textures or DALL-E prompt-rewriting from adding shadows/gradients, **State 10 must output a Multi-Tool Prompt Package tailored for the user's specific engine** (see `prompts/engine-tuning-guide.md` for deep technical tuning):

```markdown
### 🎨 Multi-Tool AI Generation Prompts

#### Option A: Google Gemini / Imagen 3 (Anti-Shadow & Anti-Texture Tuned)
"Pure 2D flat black ink graphic vector on a solid stark white background #FFFFFF. Zero shadows, zero drop shadows, zero paper texture, zero 3D embossing, zero gray shading. High-contrast single-color flat black artwork only. [Insert Subject, Composition & Style Details]."

#### Option B: Midjourney v6 (Parameter Tuned)
"Flat 2D monochrome vector illustration, [Insert Subject, Composition & Style Details], bold black outlines on clean white background, high contrast, SVG trace ready --no color, shading, gradients, shadows, 3d, realistic textures, paper texture, drop shadows --style raw --v 6.0 --ar 1:1"

#### Option C: ChatGPT / DALL-E 3 (Anti-Rewrite Directive)
"DALL-E Instruction: Do not alter or embellish the technical vector constraints. Generate a flat 2D graphic design vector outline of [Insert Subject, Composition & Style Details]. Solid black ink artwork on pure stark white background. No color, no gradients, no shadows, no 3D effects, no paper background texture."

#### Option D: Flux 1.1 / Flux Pro (Precision Line Art)
"A sharp 2D vector silhouette cut file of [Insert Subject, Composition & Style Details], featuring uniform bold black strokes on a clean white background. High contrast, fully closed paths, zero gradients, zero shadows, zero paper grain."
```

---

## 10. Prompt Quality Checklist

Before delivering a prompt, verify:

```
✓ Commercial purpose defined
✓ Buyer identified
✓ Design is differentiated
✓ SVG requirements included
✓ Prompt-level IP risks addressed (see State 10A gate)
✓ Production limitations considered
✓ Negative prompt included
```
