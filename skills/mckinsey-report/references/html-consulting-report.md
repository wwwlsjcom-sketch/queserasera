# HTML Consulting Report Standard

## Goal / 目标

Generate a vertical, self-contained, consulting-style HTML report from substantial analysis material: strategy, market, industry, investment, product, risk, operations, research, or data analysis. The output should be readable in a browser, printable as A4 portrait PDF, and rich enough to function as a professional deliverable.

目标是生成竖屏、纵向滚动、单文件自包含的 HTML 咨询报告。它应该像专业咨询交付物，而不是横屏 PPT、营销页或普通 dashboard。

Before drafting, route the report through one of six templates and select exhibit modules from the 24-module library. Use `template-router.md`, `template-matrix.yaml`, `exhibit-router.md`, and `exhibit-library.md`.

## Report Structure

Use this delivery standard unless the selected template clearly requires a different order:

1. Cover: title, subtitle, date/context, 2-3 headline judgments.
2. Executive summary: long-form thesis plus 3-5 key metrics or judgments.
3. Contents: numbered report sections.
4. Body sections: 3-6 sections with conclusion-led headings, narrative analysis, exhibits, and implications.
5. Risks/scenarios: include when the subject involves uncertainty, investment, strategy, or execution.
6. Decision-oriented close: recommendations, strategic options, watch points, decision questions, early-warning indicators, next analyses, or implementation agenda.
7. Source note: input materials, assumptions, and data caveats.

Do not create a marketing landing page. The first screen should feel like a report cover, not a hero page. Cover should not be a plain gradient unless the user explicitly requests minimalism. See `cover-art-direction.md`.

## Template Routing

Select exactly one template for each full report:

- `classic-consulting`: general strategy, transformation, operating model, market entry, mixed consulting report.
- `board-brief`: board, CEO, executive committee, governance decision.
- `market-intelligence`: industry research, market research, category landscape, competition, entry opportunity.
- `investment-memo`: investment analysis, M&A, funding round, capital allocation.
- `risk-review`: risk, compliance, regulation, cybersecurity, operational resilience.
- `product-strategy`: product strategy, growth, roadmap, funnel, SaaS/product review.

## Exhibit Routing

Normal reports need 5-8 modules. Data-heavy reports need 8-12 modules and at least five distinct visual types.

- Time series -> `market-trend-index`, `small-multiples`.
- Category comparison -> `ranking-bar`, `grouped-bar`.
- Market/competition -> `market-map`, `competitor-positioning`, `opportunity-matrix`.
- Structure/causality -> `value-chain`, `ecosystem-map`, `driver-tree`, `causal-map`.
- Risk/uncertainty -> `risk-heatmap`, `scenario-grid`, `watch-point-tracker`.
- Investment -> `thesis-scorecard`, `unit-economics-bridge`, `waterfall-bridge`.
- Product/growth -> `funnel-analysis`, `customer-journey`, `feature-priority-matrix`.
- Execution -> `implementation-roadmap`, `watch-point-tracker`.

## Minimum Completeness Standard

A full report must include:

- Portrait cover with topic-specific visual background or equivalent self-contained visual cover.
- Executive summary with a real thesis, not only metric cards.
- Dedicated contents page when the report has more than 3 sections.
- 3-6 analytical body sections.
- At least 5 exhibit modules for ordinary reports; 8-12 for data-heavy reports.
- At least 2 management-implication, evidence, watch-point, or "why it matters" panels when the material supports interpretation.
- At least 1 relationship/structure exhibit.
- At least 1 trend, comparison, or distribution exhibit.
- At least 1 risk, priority, scenario, option, or decision exhibit when relevant.
- Decision-oriented close appropriate to the subject.
- Source, assumption, or limitation note.

Metric cards and raw tables alone do not satisfy exhibit diversity.

## Analytical Depth and Page Density

Each major body section should usually include 2-4 substantive paragraphs plus at least one exhibit, evidence panel, table, or structured visual. Avoid sections that are only a chart plus a one-line caption.

Every major page should usually include at least three of these elements:

- Conclusion-led page heading.
- 1-3 substantive analytical paragraphs.
- One exhibit, chart, table, scorecard, matrix, or structured diagram.
- Evidence, management implication, watch-point, assumption, caveat, or diligence panel.
- Source/methodology/data-quality note.
- Compact list of drivers, risks, criteria, decision questions, or validation steps.

## Data-First Visualization Rule

When input contains substantial numeric, categorical, time-series, financial, operational, survey, benchmark, or KPI data, convert as much of it as reasonably possible into exhibit-style visualizations instead of prose or raw tables.

Use tables only when exact lookup matters more than pattern recognition, or when the data is sparse, textual, or highly multidimensional.

## Data Integrity

- Do not invent precise data.
- Preserve user-provided numbers exactly.
- If a chart is based on qualitative interpretation, label it clearly: `Qualitative score`, `Illustrative index`, `Directional assessment`, or `Index, base year = 100`.
- If data is incomplete, visualize what is available and explain limitations in a note.
- Do not disguise assumptions as measured data.

## Visual System

Use a restrained consulting palette, but do not default to blue. Before writing CSS, choose a palette system from the report topic and industry. Each report should define:

- `--accent`: the dominant analytical color.
- `--accent-2`: a secondary contrast color.
- `--accent-warm`: a risk, urgency, or opportunity accent.
- `--deep`: the dark cover/report color.
- neutral ink, paper, line, and muted text colors.

Blue is only one possible accent. If the report subject is not naturally blue-coded, choose another dominant family such as emerald, teal, burgundy, graphite/brass, forest/coral, violet/lime, rust/steel, or oxblood/amber. Avoid one-note palettes where most charts, headings, borders, and cover elements use the same hue.

Use large serif titles for cover and section headings, sans-serif body text, crisp chart lines, and readable labels. Avoid logos, copied proprietary designs, decorative blobs, stock-like hero layouts, generic blue network covers, and over-rounded components.

## HTML Implementation

- Produce one `.html` file.
- Embed all CSS in `<style>`.
- Use HTML/CSS/SVG for charts.
- Embed generated cover images as local/base64 assets when used. If image generation is unavailable, build a self-contained CSS/SVG cover with topic-specific motifs; a gradient-only cover is not sufficient.
- Do not use external JavaScript libraries, CDNs, remote fonts, or external images unless the user explicitly provides assets.
- Use responsive media queries so charts stack on narrow screens.
- Use A4 portrait print CSS:

```css
@media print {
  @page { size: A4 portrait; margin: 0; }
}
```

## Quality Checklist

Before delivery, verify:

- The report is a vertical HTML report, not a slide deck or landing page.
- The file is self-contained.
- The cover has a topic-specific visual background or equivalent self-contained image-like visual.
- The palette is visibly topic-specific and not dominated by a default corporate cool-color system.
- Cover title placement follows the background image composition and remains readable.
- The content is substantial and analytical.
- Each major page has sufficient information density.
- Major sections have enough narrative depth, not just charts/cards.
- Data-heavy inputs are visualized, not buried in long tables.
- Exhibit types are diverse; tables and metric cards are not the only visuals.
- Management implication or evidence panels explain the "so what" where needed.
- Exhibits have conclusion-led titles and notes.
- No chart text is clipped.
- No horizontal page overflow on desktop or mobile.
- Print CSS is portrait.
- No placeholder markers, unresolved variables, invalid numeric values, or draft text remains.
- Assumptions and illustrative data are labeled.
