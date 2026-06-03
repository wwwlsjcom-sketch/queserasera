# HTML Consulting Report Standard

## Goal / 目标

Generate a vertical, self-contained, McKinsey-style HTML consulting report from any substantial analysis material: strategy, market, industry, investment, product, risk, operations, research, or data analysis. The output should be readable in a browser, printable as A4 portrait PDF, and rich enough to function as a professional deliverable. It should have a topic-specific cover visual and high information density on every page.

目标是生成**竖屏、纵向滚动、单文件自包含的 HTML 咨询报告**。它应该像专业咨询交付物，而不是横屏 PPT、营销页或普通 dashboard。

完整报告必须有主题化封面背景图或同等质量的主题视觉背景。封面图根据报告主题、行业和报告类型生成或构造，标题排版根据图像留白和视觉重心调整。

Before drafting, route the report through one of six templates and select exhibit modules from the 24-module library. Use `template-router.md`, `template-matrix.yaml`, `exhibit-router.md`, and `exhibit-library.md`.

## Report Structure / 报告结构

Use this delivery standard unless the selected template clearly requires a different order:

1. **Cover**: title, subtitle, date/context, 2-3 headline judgments.
2. **Executive summary**: long-form thesis plus 3-5 key metrics or judgments.
3. **Contents**: numbered report sections.
4. **Body sections**: 3-6 sections with conclusion-led headings, narrative analysis, exhibits, and implications.
5. **Risks/scenarios**: include when the subject involves uncertainty, investment, strategy, or execution.
6. **Decision-oriented close**: choose the right ending for the analysis, such as recommendations, strategic options, watch points, decision questions, early-warning indicators, next analyses, or an implementation agenda.
7. **Source note**: input materials, assumptions, and data caveats.

Do not create a marketing landing page. The first screen should feel like a report cover, not a hero page.

不要做成 landing page。第一屏应像报告封面，而不是网站 hero 区。

Cover should not be a plain gradient unless the user explicitly requests minimalism. See `cover-art-direction.md`.

## Template Routing / 模板路由

Select exactly one template for each full report:

- `classic-consulting`: general strategy, transformation, operating model, market-entry, mixed consulting report.
- `board-brief`: board, CEO, executive committee, governance decision.
- `market-intelligence`: industry research, market research, category landscape, competition, entry opportunity.
- `investment-memo`: investment analysis, M&A, funding round, capital allocation.
- `risk-review`: risk, compliance, regulation, cybersecurity, operational resilience.
- `product-strategy`: product strategy, growth, roadmap, funnel, SaaS/product review.

The template determines the body architecture and default exhibit mix, but not the final content. Adapt sections to the user's material and decision question.

## Exhibit Routing / Exhibit 路由

Select exhibits from the 24-module library in `exhibit-library.md`. Normal reports need 5-8 modules. Data-heavy reports need 8-12 modules and at least five distinct visual types.

Do not use the same module mix for every report. Select modules from data shape and analytical purpose:

- Time series -> `market-trend-index`, `small-multiples`.
- Category comparison -> `ranking-bar`, `grouped-bar`.
- Market/competition -> `market-map`, `competitor-positioning`, `opportunity-matrix`.
- Structure/causality -> `value-chain`, `ecosystem-map`, `driver-tree`, `causal-map`.
- Risk/uncertainty -> `risk-heatmap`, `scenario-grid`, `watch-point-tracker`.
- Investment -> `thesis-scorecard`, `unit-economics-bridge`, `waterfall-bridge`.
- Product/growth -> `funnel-analysis`, `customer-journey`, `feature-priority-matrix`.
- Execution -> `implementation-roadmap`, `watch-point-tracker`.

## Minimum Completeness Standard / 最低完整度标准

A full report must include:

- Portrait cover.
- Topic-specific cover background image or equivalent self-contained visual cover.
- Executive summary with a real thesis, not only metric cards.
- Dedicated contents page when the report has more than 3 sections.
- 3-6 analytical body sections.
- At least 5 exhibit modules for an ordinary analytical report; 8-12 for data-heavy reports.
- At least 2 management-implication, evidence, watch-point, or "why it matters" panels when the material supports interpretation.
- At least 1 relationship/structure exhibit.
- At least 1 trend, comparison, or distribution exhibit.
- At least 1 risk, priority, scenario, option, or decision exhibit when relevant.
- A decision-oriented close appropriate to the subject.
- Source, assumption, or limitation note.
- Page-level information density: each major page should combine analysis, evidence, structured visuals, and implication. See `page-density-standard.md`.

Metric cards and raw tables alone do not satisfy exhibit diversity.

## Analytical Depth Standard / 正文厚度标准

Each major body section should contain enough narrative to stand on its own. Avoid sections that are only a chart plus a one-line caption.

For each major section, answer as many of these as the material supports:

- What is the conclusion?
- What evidence or logic supports it?
- Why does it matter for the target audience?
- What trade-offs, caveats, or uncertainties should be considered?
- What signals should be monitored next?

As a practical baseline, each major section should usually include 2-4 substantive paragraphs plus at least one exhibit, evidence panel, table, or structured visual. If a section is intentionally short, make that a deliberate editorial choice, not the default.

正文厚度是硬要求。不要只输出卡片、表格和一句话说明；主体章节必须有能够支撑判断的分析段落。

## Page Density Standard / 页面信息密度标准

Every major page should feel information-rich but readable. The goal is professional density, not clutter.

Each major page should usually include at least three of these elements:

- Conclusion-led page heading.
- 1-3 substantive analytical paragraphs.
- One exhibit, chart, table, scorecard, matrix, or structured diagram.
- Evidence, management implication, watch-point, assumption, caveat, or diligence panel.
- Source/methodology/data-quality note.
- Compact list of drivers, risks, criteria, decision questions, or validation steps.

Avoid low-density pages:

- Only one large title and one chart.
- Metric cards without interpretation.
- Large decorative whitespace after the cover.
- Repeated divider pages with little content.
- One visual and no "so what."

页面信息密度是硬要求。文字上限只用于防止图表标签、节点、卡片标题溢出，不能压缩正文分析和证据说明。

## Writing Style

- Use a consulting voice: concise, evidence-led, and decision-oriented.
- Put the conclusion before the explanation.
- Use full-sentence section titles and exhibit titles where possible.
- Explain why each exhibit matters.
- Keep enough long-form prose for real analysis; do not reduce the report to cards.
- Avoid brand/logo usage or copying proprietary report text. Use “consulting-style” or “McKinsey-style inspired” design language only.

## Data-First Visualization Rule / 数据优先图表化规则

When the input contains substantial numeric, categorical, time-series, financial, operational, survey, benchmark, or KPI data, convert as much of it as reasonably possible into exhibit-style visualizations instead of prose or raw tables.

Prefer charts over tables when:

- Data compares categories, segments, products, regions, competitors, roles, or customer groups.
- Data includes dates, periods, cohorts, before/after states, quarters, or years.
- Data includes percentages, rankings, scores, changes, deltas, growth rates, shares, probabilities, or confidence levels.
- Data supports a strategic conclusion or decision.
- A table has more than 4 rows or more than 3 numeric columns.

Use tables only when exact lookup matters more than pattern recognition, or when the data is sparse, textual, or highly multidimensional.

## Chart Selection Rules / 图表选择规则

- Time series -> line chart, stacked area chart, grouped bar chart.
- Category comparison -> horizontal bar chart, grouped bar chart.
- Ranking -> horizontal bar chart, Pareto-style chart.
- Part-to-whole -> stacked bar chart; donut/pie only for few categories.
- Before/after -> paired bars, waterfall, delta badges.
- Survey responses -> stacked bar, diverging bar.
- Risk scoring -> heatmap, 2x2 matrix.
- Portfolio/opportunity analysis -> bubble chart, 2x2 matrix.
- KPI overview -> metric cards plus mini charts.
- Positive/negative impact -> diverging bar chart.
- Funnel/conversion -> funnel or step flow.
- Relationship/dependency -> network map, value chain, or system map.

For data-heavy reports, aim for 8-12 exhibits. For ordinary analytical reports, aim for 5-8 exhibits. Include at least one exhibit in each major section when possible.

## Exhibit Requirements / Exhibit 要求

Each exhibit should include:

- `Exhibit N` numbering.
- A conclusion-led title, not a generic label.
- A short caption explaining what the reader should see.
- Clear legend, axis labels, or category labels.
- Notes for assumptions, sources, or illustrative scoring.
- Nearby implication text explaining why the exhibit matters.

Recommended exhibit types:

- Key judgment scorecard or bar chart.
- Driver structure stacked bar.
- Opportunity bubble chart.
- Scenario/value release line chart.
- Risk heatmap.
- Strategic option diverging bar.
- Relationship/network map.
- Roadmap or milestone flow.

## Required Exhibit Mix / 图表多样性要求

For a complete report, include at least four types when the material supports them:

- Relationship/structure exhibit: value chain, system map, capability map, dependency map, ecosystem map, or causal network.
- Trend/comparison exhibit: line, bar, stacked bar, ranking, grouped bar, or before/after chart.
- Risk/priority/decision exhibit: heatmap, 2x2 matrix, scenario grid, prioritization matrix, or option scorecard.
- Action/roadmap/options exhibit: roadmap, milestone flow, diverging bar, strategic option map, or decision tree.

For data-heavy reports, use at least five exhibit types and prioritize chart forms with axes, legends, scales, deltas, bubbles, or structured matrices. Metric cards and tables can support the story, but they should not be the only visual language.

数据多时必须尽量图表化。指标卡片和表格可以保留，但不能成为唯一的视觉表达。

## Management Implication Panels / 管理层含义与证据面板

Use evidence panels to explain the "so what." These panels prevent the report from becoming a sequence of visuals without interpretation.

Good panel titles include:

- Management implication.
- Why this matters.
- Decision implication.
- Key evidence.
- Watch points.
- Early-warning signals.
- Evidence gap.
- What would change the conclusion.

Use at least two such panels in a full report when the analysis is complex, uncertain, strategic, or data-heavy.

## Scenario and Uncertainty Modules / 情景与不确定性模块

When the topic involves uncertainty, investment, strategy, market timing, product bets, risk, regulation, or execution, include a scenario or uncertainty module. Choose a form that fits the material:

- Upside / base / downside.
- Optimistic / base / conservative.
- High / medium / low adoption.
- Best case / base case / stress case.
- Key uncertainties and watch points.
- Early-stop or escalation signals.

## Data Integrity / 数据诚信

- Do not invent precise data.
- Preserve user-provided numbers exactly.
- If a chart is based on qualitative interpretation, label it clearly: `Qualitative score`, `Illustrative index`, `Directional assessment`, or `Index, base year = 100`.
- If data is incomplete, visualize what is available and explain limitations in a note.
- Do not disguise assumptions as measured data.

## Decision-Oriented Close / 决策导向收束

End the report with a decision-oriented close that fits the analysis. Do not force a fixed 7/30/90-day action plan unless the user asks for implementation planning or the topic naturally requires one.

Choose the closing format based on the material:

- Strategy reports: strategic options, trade-offs, decision questions.
- Investment reports: thesis, watch points, triggers, downside risks.
- Risk reports: early-warning indicators, stop-loss conditions, mitigation options.
- Product reports: roadmap implications, prioritization, experience risks.
- Market reports: scenarios, entry timing, competitive watch points.
- Operational reports: actions, owners, milestones, KPI follow-up.
- Research reports: open questions, evidence gaps, next analyses.

## Visual System / 视觉系统

Use a restrained consulting palette:

```css
--ink: #111318;
--muted: #5b6270;
--line: #d7dce4;
--paper: #f6f7f9;
--white: #ffffff;
--blue: #145cff;
--deep: #06162f;
--cyan: #20c7e6;
--amber: #ffb000;
--red: #c64036;
--green: #168565;
```

Design rules:

- Portrait page width around 900-1000px.
- White report pages on a light paper background.
- Topic-specific cover background image with readable overlay.
- Large serif titles for cover and section headings; cover title placement should follow the background image's negative space.
- Sans-serif body text.
- Keep large cards and subtle backgrounds when they improve scannability.
- Use dark exhibit panels sparingly for line charts or emphasis.
- Avoid decorative blobs, excessive gradients, stock-like hero layouts, and over-rounded components.
- Keep chart lines, axes, and labels crisp and simple.

## HTML Implementation / HTML 实现

- Produce one `.html` file.
- Embed all CSS in `<style>`.
- Use HTML/CSS/SVG for charts.
- If using a generated cover image, embed it as a local/base64 `data:image/...` asset or otherwise keep the HTML self-contained.
- Do not use external JavaScript libraries, CDNs, remote fonts, or external images unless the user explicitly provides assets.
- Ensure all chart labels fit. Avoid fixed absolute positioning for text-heavy graph nodes.
- Avoid `overflow:hidden` around node diagrams unless clipping is intentional and verified.
- Use responsive media queries so charts stack on narrow screens.
- Use A4 portrait print CSS:

```css
@media print {
  @page { size: A4 portrait; margin: 0; }
}
```

## Template Guidance / 模板使用

First select one template from `assets/templates/`, then use `assets/html-report-template.html` as the HTML/CSS starting point when generating a full report. Replace placeholder content, preserve the core CSS classes, and add or remove sections based on the selected template and user material.

生成完整报告时，优先使用模板骨架，避免从零自由发挥导致横屏化、卡片化或图表缺失。

Core classes to preserve when useful:

- `.cover`
- `.cover-copy`
- `.evidence-grid`
- `.density-panel`
- `.page`
- `.section-head`
- `.narrative`
- `.insight`
- `.chart-block`
- `.exhibit-svg`
- `.knowledge-map`
- `.dark-exhibit`
- `.diverging-chart`
- `.table-wrap`

Template files:

- `assets/templates/classic-consulting.html`
- `assets/templates/board-brief.html`
- `assets/templates/market-intelligence.html`
- `assets/templates/investment-memo.html`
- `assets/templates/risk-review.html`
- `assets/templates/product-strategy.html`

## Quality Checklist / 交付检查清单

Before delivery, verify:

- The report is a vertical HTML report, not a slide deck or landing page.
- 报告必须是竖屏 HTML，不是横屏 PPT、landing page 或纯 dashboard。
- The file is self-contained.
- The cover has a topic-specific visual background or equivalent self-contained image-like visual.
- Cover title placement follows the background image composition and remains readable.
- The content is substantial and analytical.
- Each major page has sufficient information density, not only a title, one chart, or a few cards.
- 主体章节必须有足够分析正文，不能只有图表和卡片。
- The report has a dedicated contents page when appropriate.
- Major sections have enough narrative depth, not just charts/cards.
- Data-heavy inputs are visualized, not buried in long tables.
- Exhibit types are diverse; tables and metric cards are not the only visuals.
- Relationship/structure, trend/comparison, and risk/priority/option exhibits appear when supported by the material.
- Management implication or evidence panels explain the "so what" where needed.
- The ending is decision-oriented and appropriate to the subject, without forcing an irrelevant action-plan template.
- Exhibits have conclusion-led titles and notes.
- No chart text is clipped.
- Node maps do not overflow or cut off labels.
- No horizontal page overflow on desktop or mobile.
- Print CSS is portrait.
- No placeholder markers, unresolved variables, invalid numeric values, or draft text remains.
- Assumptions and illustrative data are labeled.
