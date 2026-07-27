# AI Engine Tuning & Anti-Shadow Guide

This guide provides technical prompt engineering rules for major AI image generation engines (Google Gemini / Imagen 3, Midjourney v6, ChatGPT / DALL-E 3, Flux 1.1 / Flux Pro, and Ideogram 2.0) to ensure generated art vectorizes cleanly without shadows, paper textures, 3D embossing, or unwanted gray shading.

---

## 1. Google Gemini / Imagen 3 (Gemini Canvas)

### Quirks & Behavioral Traps
- **Paper & Canvas Textures:** Gemini frequently renders black-and-white line art on textured parchment, vintage paper, or mottled backgrounds.
- **Drop Shadows & 3D Depth:** Gemini tends to add soft drop shadows, bevels, or subtle ambient occlusion around black line strokes.
- **Negative Prompt Blindness:** Gemini often ignores negative lists placed at the very end of a prompt.

### Recommended Solution
Use **positive inline enforcement commands** placed at the very start of the prompt:

```text
Pure 2D flat black ink graphic vector on a solid stark white background #FFFFFF. Zero shadows, zero drop shadows, zero paper texture, zero 3D embossing, zero gray shading. High-contrast single-color flat black artwork only, clean closed outlines, vector cutout style.
[Insert Subject & Composition Details Here]
```

---

## 2. Midjourney v6

### Quirks & Behavioral Traps
- Midjourney loves photorealistic rendering, soft lighting, and artistic depth unless explicitly restricted using parameter flags.

### Recommended Solution
Use `--style raw` combined with strict `--no` negative parameter flags:

```text
Flat 2D monochrome vector illustration, [Subject & Composition], bold black outlines on clean white background, high contrast, SVG trace ready --no color, shading, gradients, shadows, 3d, realistic textures, paper texture, drop shadows --style raw --v 6.0 --ar 1:1
```

---

## 3. ChatGPT / DALL-E 3

### Quirks & Behavioral Traps
- DALL-E 3 automatically expands and re-writes user prompts under the hood, often adding descriptive adjectives like "soft lighting", "subtle shadows", or "artistic texture".

### Recommended Solution
Inject an explicit directive preventing DALL-E from altering the technical vector constraints:

```text
DALL-E Instruction: Do not alter or embellish the technical vector constraints.
Generate a flat 2D graphic design vector outline of [Subject & Composition]. Solid black ink artwork on pure stark white background. No color, no gradients, no shadows, no 3D effects, no paper background texture. Sharp high-contrast line work suitable for Cricut vinyl cutting.
```

---

## 4. Flux 1.1 / Flux Pro

### Quirks & Behavioral Traps
- Flux responds exceptionally well to natural language descriptions, but can produce hairline strokes if line weight is not specified.

### Recommended Solution
Specify exact stroke weight and high contrast:

```text
A sharp 2D vector silhouette cut file of [Subject & Composition], featuring uniform bold black strokes on a clean white background. High contrast, fully closed paths, zero gradients, zero shadows, zero paper grain. Clean vector graphic.
```

---

## 5. Ideogram 2.0

### Quirks & Behavioral Traps
- Ideogram excels at typography and crisp vector cutouts. Use its native `Design` or `Vector` style preset if available.

### Recommended Solution
```text
Flat vector graphic logo of [Subject & Composition], crisp black linework on pure white background, high contrast, clean typography, zero drop shadow, zero 3D effect.
```
