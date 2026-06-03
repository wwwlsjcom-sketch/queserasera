# Template Router

Use this router before writing the HTML. The goal is professional fit: the report should keep a consistent portrait consulting standard while changing structure, cover direction, exhibit mix, and decision close according to the user's analysis task.

## Required Routing Steps

1. Identify `report_type`: classic-consulting, board-brief, market-intelligence, investment-memo, risk-review, product-strategy.
2. Identify `industry`: financial-services, healthcare, consumer-retail, manufacturing, technology-saas, energy-infrastructure, or general.
3. Identify `audience`: executive team, board, investment committee, strategy team, product leadership, risk/compliance, operators.
4. Identify `data_density`: light, normal, data-heavy.
5. Select one template from `template-matrix.yaml`.
6. Select 5-8 exhibit modules for normal reports or 8-12 for data-heavy reports from `exhibit-library.md`.
7. Select cover art direction from `cover-art-direction.md`.
8. Generate a portrait HTML report using the selected template and modules.

If the user explicitly names a report type, use that unless the content clearly conflicts. If ambiguous, choose the template that best fits the decision question.

## Six Templates

### classic-consulting

Use for general strategy, transformation, market entry, operating model, or mixed executive consulting reports.

Typical architecture:

1. Executive thesis.
2. Situation diagnosis.
3. Driver analysis.
4. Strategic options.
5. Recommended path and decision implications.

Default modules:

- `ranking-bar`
- `stacked-share`
- `driver-tree`
- `market-trend-index`
- `option-scorecard`
- `implementation-roadmap`

### board-brief

Use for board-ready decisions, executive committee updates, CEO briefings, and governance-oriented reports.

Typical architecture:

1. Decision required.
2. Facts that matter.
3. Options and trade-offs.
4. Risk and mitigations.
5. Board questions and next gates.

Default modules:

- `decision-brief`
- `option-scorecard`
- `risk-heatmap`
- `watch-point-tracker`
- `scenario-grid`

### market-intelligence

Use for industry research, market sizing, category landscape, competition, market entry, and growth opportunity reports.

Typical architecture:

1. Market thesis.
2. Demand trajectory.
3. Segment and competitive landscape.
4. Value-chain pressure points.
5. Opportunity spaces and entry implications.

Default modules:

- `market-trend-index`
- `market-map`
- `value-chain`
- `competitor-positioning`
- `opportunity-matrix`

### investment-memo

Use for investment analysis, M&A screening, Series A/B/C review, strategic acquisition, or capital allocation.

Typical architecture:

1. Investment stance.
2. Value creation drivers.
3. Unit economics and scalability.
4. Downside risk and scenarios.
5. Watch points and decision gates.

Default modules:

- `thesis-scorecard`
- `unit-economics-bridge`
- `market-trend-index`
- `scenario-grid`
- `watch-point-tracker`

### risk-review

Use for risk, compliance, regulation, cybersecurity, operational resilience, project risk, or risk committee reports.

Typical architecture:

1. Risk posture.
2. Exposure and transmission mechanisms.
3. Impact/severity prioritization.
4. Mitigation options.
5. Early-warning indicators and escalation gates.

Default modules:

- `risk-heatmap`
- `causal-map`
- `scenario-grid`
- `implementation-roadmap`
- `watch-point-tracker`

### product-strategy

Use for product strategy, growth strategy, user funnel, roadmap, prioritization, customer experience, or SaaS/product operating reviews.

Typical architecture:

1. Product thesis.
2. User/customer problem and journey.
3. Funnel or adoption diagnosis.
4. Feature and roadmap priorities.
5. Growth, risk, and operating implications.

Default modules:

- `funnel-analysis`
- `customer-journey`
- `feature-priority-matrix`
- `implementation-roadmap`

## Template Fit Rules

- Do not force the same section sequence across report types.
- Keep the cover, contents, executive summary, exhibits, and source notes as delivery standards, but adapt the body architecture.
- Use the template's default modules as a starting set, then swap modules based on actual data shape.
- A module should appear because it supports a conclusion, not because a page slot exists.
