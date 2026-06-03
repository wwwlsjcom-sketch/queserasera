# Queserasera

A Codex skill for generating self-contained, portrait HTML consulting reports with dense analysis, exhibit-style visuals, themed cover art, and print/PDF readiness.

The packaged skill is currently named `mckinsey-report` because its trigger language targets McKinsey-style consulting report requests. This project is independent and is not affiliated with, endorsed by, or sponsored by McKinsey & Company.

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

## Installation

Copy this folder into your Codex skills directory:

```powershell
# Windows PowerShell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills\mckinsey-report"
Copy-Item -Recurse -Force .\* "$env:USERPROFILE\.codex\skills\mckinsey-report\"
```

On macOS or Linux:

```bash
mkdir -p ~/.codex/skills/mckinsey-report
cp -R ./* ~/.codex/skills/mckinsey-report/
```

Restart Codex after installing so the skill can be discovered.

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
