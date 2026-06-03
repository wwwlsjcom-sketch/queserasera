# mckinsey-report

A Codex skill for generating portrait, self-contained HTML consulting reports with dense analysis, exhibit-style visuals, themed cover art, and print/PDF readiness.

This skill is independent and is not affiliated with, endorsed by, or sponsored by McKinsey & Company.

## Install

Use this directory URL with `$skill-installer`:

```text
$skill-installer install https://github.com/wwwlsjcom-sketch/queserasera/tree/main/skills/mckinsey-report
```

Restart Codex after installing so the skill can be discovered as `mckinsey-report`.

## What This Skill Does

`mckinsey-report` helps Codex turn strategy, market, product, risk, investment, or operating materials into a polished single-file HTML report.

Core capabilities:

- Generates vertical portrait HTML reports, not slide decks or landing pages.
- Produces self-contained output with embedded CSS, SVG/HTML exhibits, and local/base64 cover visuals when used.
- Selects from six consulting report templates based on audience, decision context, industry, and data density.
- Uses 24 exhibit modules for trend, comparison, market landscape, risk, option, roadmap, funnel, unit economics, and scenario analysis.
- Requires topic-specific cover art or a subject-aware CSS/SVG visual fallback.
- Routes each report through a theme-specific color system instead of defaulting to blue.
- Adds source notes, assumptions, caveats, evidence panels, and management implications.
- Includes `scripts/validate_report.py` for lightweight delivery QA.

## Supported Report Types

| Report type | Best for | Typical ending | Default exhibit modules |
| --- | --- | --- | --- |
| `classic-consulting` | Strategy, transformation, operating model, market entry, mixed executive analysis | Recommended path, decision implications, next analyses | Ranking bar, stacked share, driver tree, trend index, option scorecard, roadmap |
| `board-brief` | Board reports, CEO briefings, executive committee decisions, governance updates | Board questions, decision gates, risk ownership | Decision brief, option scorecard, risk heatmap, scenario grid, watch-point tracker |
| `market-intelligence` | Industry research, market research, category landscape, competitive intelligence | Attractive segments, entry implications, watch points | Market trend index, market map, value chain, competitor positioning, opportunity matrix |
| `investment-memo` | Investment analysis, M&A screening, funding review, capital allocation | Investment stance, diligence questions, deal gates | Thesis scorecard, unit-economics bridge, trend index, scenario grid, watch-point tracker |
| `risk-review` | Risk assessment, compliance, regulation, cybersecurity, operational resilience | Mitigation options, escalation thresholds, early-warning indicators | Risk heatmap, causal map, scenario grid, roadmap, watch-point tracker |
| `product-strategy` | Product strategy, growth, roadmap, funnel, SaaS/product operating review | Roadmap implications, prioritization, operating cadence | Funnel analysis, customer journey, feature priority matrix, roadmap |

## Preview Style

The skill is designed to produce report pages with this structure:

```text
Portrait cover
├── Topic-specific visual background
├── Large report title and subtitle
└── 2-3 headline judgments

Executive summary
├── Conclusion-led thesis
├── Key evidence or judgment metrics
└── Compact diagnostic exhibit

Body sections
├── Section thesis
├── Analytical narrative
├── Exhibit block with source/assumption note
└── Management implication or watch-point panel

Decision close
├── Recommendation / options / scenarios
├── Risks and validation questions
└── Next analyses or action implications
```

Visual behavior:

- Portrait page width around 900-1000px.
- Topic-specific cover art rather than generic gradients.
- Large serif headings, restrained body typography, and dense but readable pages.
- Semantic CSS tokens such as `--accent`, `--accent-2`, `--accent-warm`, and `--deep`.
- Industry-sensitive palettes such as graphite/parchment/emerald for finance, forest/coral for retail, rust/steel/teal for manufacturing, and violet/cyan/lime for SaaS.
- Exhibit blocks with numbered captions, conclusion-led titles, assumptions, and nearby implication text.

## Example Prompts

```text
Generate a board-ready HTML report on the 2026 outlook for enterprise AI adoption.
```

```text
Create an investment memo HTML report for a Series B SaaS company, including market opportunity, unit economics, risk scenarios, and diligence questions.
```

```text
Turn these market research notes into a portrait consulting report with a market landscape, competitor positioning, opportunity matrix, and entry implications.
```

## Validation

After generating a report, run:

```bash
python scripts/validate_report.py path/to/report.html
```

The validator checks for common issues such as missing portrait print CSS, external dependencies, thin pages, missing contents sections, missing source/assumption language, and insufficient exhibit-like modules.

## Contents

```text
mckinsey-report/
├── SKILL.md
├── _meta.json
├── agents/
├── assets/
│   ├── html-report-template.html
│   └── templates/
├── references/
└── scripts/
    └── validate_report.py
```
