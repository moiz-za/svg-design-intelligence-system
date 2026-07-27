# Universal SVG Prompt Template

Used in **State 10 — Prompt Engineering**. This is the primary,
default template — reach for the style-specific templates in this
folder (`vintage.md`, `minimalist.md`, `character.md`,
`typography.md`, `bundle-creation.md`) only when the Creative Strategy
calls for that specific direction.

---

## Model Independence

ESVG-DIS works with any capable AI image-generation system — it does
not depend on a single provider. Supported tools may include ChatGPT
Images, Gemini Image Generation, Midjourney, Flux, Ideogram, Leonardo,
and future AI image models. These templates are intentionally
model-independent: the same template structure works across all of
them without tool-specific syntax.

The goal of a template isn't to force identical outputs across tools —
it's to make sure every generation request carries the strategic and
technical information commercial SVG production actually needs,
regardless of which tool executes it.

---

## The Template

```
Create a premium commercial SVG design.

DESIGN SUBJECT:
[Main subject]

CONCEPT:
[Unique creative direction]

TARGET BUYER:
[Buyer persona]

EMOTIONAL PURPOSE:
[Why customers connect with this design]

STYLE:
[Visual style]

COMPOSITION:
[Layout and structure]

SVG REQUIREMENTS:
- solid flat black artwork on pure stark white background #FFFFFF
- zero shadows, zero drop shadows, zero 3D embossing, zero paper background texture
- clean flat 2D vector appearance with zero gray shading
- strong readable silhouette
- clear fully closed shapes and smooth outer outlines
- consistent line thickness (min 2-3pt for Cricut vinyl cutting)
- suitable for vector tracing and laser cutting
- feature size limit >= 1/40th width (no fragile micro-dots or floating shapes)

ORIGINALITY REQUIREMENTS:
- create a unique interpretation
- avoid common marketplace designs
- avoid copied compositions
- include distinctive symbolic elements

QUALITY REQUIREMENTS:
- professional commercial artwork
- balanced composition
- premium appearance
- clean edges

NEGATIVE REQUIREMENTS:
Avoid:
- color
- gradients
- shadows and drop shadows
- paper texture and parchment texture
- realistic rendering
- photographs
- 3D effects and beveling
- logos
- trademarks
- copyrighted characters
- watermarks
- messy AI artifacts
```

Every bracketed field above should be filled from the Creative Brief
(`knowledge/creative-strategy.md`) and the selected Concept
(`knowledge/concept-development.md`) — don't leave any field generic
if the upstream stages produced something specific.
