# Cover Art Direction

## Goal

Every complete report must have a topic-specific portrait cover background image or an equivalent self-contained visual background. The cover is part of the report's analytical positioning: it should immediately signal industry, report type, and decision context while keeping the overall tone professional and McKinsey-style inspired.

Do not use McKinsey logos, proprietary report covers, stock-photo handshakes, generic business people, decorative blobs, unrelated atmospheric imagery, or a plain blue corporate gradient.

## Required Cover Workflow

1. Identify the report topic, industry, audience, and report type.
2. Generate or construct a portrait cover background image that reflects the subject.
3. Ensure the image has deliberate negative space for the title.
4. Place title text according to the image composition:
   - Use left-aligned title when visual density sits on the right.
   - Use right-aligned title when visual density sits on the left.
   - Use centered title only when the image has balanced negative space and low central contrast.
5. Add a dark or light overlay gradient to preserve legibility without hiding the image.
6. Embed the image in the final HTML as a local/base64 asset. Do not rely on remote images.
7. Choose a cover palette from the subject, not from the default template. Blue is allowed only when it fits the subject; otherwise use another dominant hue family.

If image generation is unavailable, create a self-contained CSS/SVG thematic cover background with the same art-direction rules. This fallback must include at least three topic-specific motifs, such as industry asset silhouettes, data overlays, workflow maps, product UI fragments, market landscape shapes, risk/control grids, energy/load curves, clinical pathway traces, or customer journey paths. Do not fall back to a plain gradient, a generic blue network, or an abstract grid unless the user explicitly asks for a minimal cover.

## Palette Direction

Select a non-default palette before designing the cover:

- Strategy / operating model: ink, warm gray, signal red or amber, restrained blue only as secondary.
- Board / governance: charcoal, ivory, burgundy or brass, muted steel.
- Market intelligence: forest, teal, coral, warm neutral, or category-specific retail colors.
- Investment memo: graphite, parchment, emerald, brass, muted red for risk.
- Risk review: graphite, oxblood, amber, slate, small green mitigation accents.
- Product / SaaS: ink, violet, cyan, lime, or product-specific accent, with neutral UI grays.
- Healthcare: deep teal, clinical green, white, slate, restrained blue as secondary.
- Manufacturing / infrastructure: steel, graphite, safety yellow, teal, rust, or grid green.

Avoid one-note palettes. If more than half of visible accents are blue, revise the palette.

## Cover Prompt Pattern

Use this pattern when generating a raster cover asset:

```text
Use case: productivity-visual
Asset type: portrait consulting report cover background
Primary request: create a high-end consulting-style cover background for <topic>.
Scene/backdrop: <industry-specific environment, systems, assets, data signals>.
Style/medium: premium editorial business report background, photorealistic-abstract hybrid, refined consulting aesthetic.
Composition/framing: portrait cover background, strong negative space on <left/right/center> for large report title, visual density on <opposite area>, no text.
Lighting/mood: professional, precise, restrained, high signal.
Color palette: <industry palette>; do not default to a generic corporate cool palette unless the subject calls for it.
Constraints: no words, no numbers, no logos, no watermark, no people, no cartoon style, no stock-photo cliche, no decorative blobs.
```

## Industry Visual Directions

- Industrial / manufacturing: production systems, robotic lines, MES/SCADA signal traces, machine vision overlays, steel gray, deep navy, cyan accents.
- Finance / investment / risk: institutional architecture, audit trails, secure data vaults, document layers, risk grids, graphite, parchment, emerald, brass, oxblood, small amber accents.
- Healthcare / life sciences: clinical workflows, diagnostic interfaces, care pathways, lab or imaging textures, clean blue/green palette, high trust and clarity.
- Consumer / retail: demand signals, category shelves, customer journey traces, basket economics, warm but restrained accents.
- Technology / SaaS: product workflows, API/data layers, usage telemetry, modular interface geometry, violet/cyan/lime with neutral UI gray.
- Energy / infrastructure: grid, load curves, generation assets, field infrastructure, dark teal/green-blue palette, operational resilience.

## Cover QA

- The cover should read as a professional report cover, not a marketing hero section.
- The first viewport must signal the actual topic, not only a decorative mood.
- Title and subtitle must be readable at desktop, mobile, and print sizes.
- The cover image must not contain generated text or fake numbers.
- The title placement should visibly differ across different report topics when the image composition differs.
- The cover must not look like the default template. If it could fit any industry, redesign it with more subject-specific visual evidence.
