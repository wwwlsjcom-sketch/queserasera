# Queserasera

A Codex skill for generating self-contained, portrait HTML consulting reports with dense analysis, exhibit-style visuals, themed cover art, and print/PDF readiness.

This project is independent and is not affiliated with, endorsed by, or sponsored by McKinsey & Company.

## Standalone Skill Link

Use this link when installing or sharing the skill:

https://github.com/wwwlsjcom-sketch/queserasera/tree/main/skills/queserasera

In Codex, you can ask:

```text
$skill-installer install https://github.com/wwwlsjcom-sketch/queserasera/tree/main/skills/queserasera
```

Or install from GitHub with the helper script:

```bash
install-skill-from-github.py --url https://github.com/wwwlsjcom-sketch/queserasera/tree/main/skills/queserasera
```

Restart Codex after installing so the skill can be discovered.

## What It Does

- Produces single-file HTML reports suitable for browser reading and printing to PDF.
- Routes requests across six report templates:
  - classic consulting
  - board brief
  - market intelligence
  - investment memo
  - risk review
  - product strategy
- Uses exhibit-oriented report logic, including conclusion-led titles, numbered exhibits, source/assumption notes, and data-first visual modules.
- Includes a lightweight validator for generated HTML reports.

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
└── skills/
    └── queserasera/
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

## Usage

Ask Codex for a consulting-style HTML report, for example:

```text
Generate a board-ready HTML report on the 2026 outlook for enterprise AI adoption.
```

The skill will select a suitable template, choose exhibit modules, create a portrait report structure, and save a self-contained `.html` output.

## Validation

After generating a report, run:

```bash
python scripts/validate_report.py path/to/report.html
```

The validator checks for common delivery issues such as missing portrait print CSS, external dependencies, thin pages, missing contents sections, and insufficient exhibit-like modules.

## Notes

- Do not use this skill to imply affiliation with any consulting firm.
- The skill asks Codex to avoid fabricating precise data. Directional or illustrative exhibits should be labeled as such.
- Generated reports should be reviewed before external use, especially when they contain business, legal, financial, medical, or regulated-domain analysis.

## License

MIT. See [LICENSE](LICENSE).
