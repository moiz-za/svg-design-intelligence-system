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
- black and white only
- clean flat vector appearance
- strong silhouette
- clear closed shapes
- smooth outlines
- consistent line thickness
- suitable for tracing
- suitable for Cricut and cutting machines
- minimal unnecessary complexity

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
- shadows
- realistic rendering
- photographs
- 3D effects
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
