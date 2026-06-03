#!/usr/bin/env python3
"""Basic QA gate for self-contained portrait consulting HTML reports."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def strip_tags(html: str) -> str:
    html = re.sub(r"<script\b[^>]*>.*?</script>", " ", html, flags=re.I | re.S)
    html = re.sub(r"<style\b[^>]*>.*?</style>", " ", html, flags=re.I | re.S)
    return re.sub(r"<[^>]+>", " ", html)


def count_chinese_chars(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def page_blocks(html: str) -> list[str]:
    blocks = re.findall(r'<section\b[^>]*class="[^"]*\b(?:page|cover)\b[^"]*"[^>]*>.*?</section>', html, flags=re.I | re.S)
    return blocks or [html]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_report.py <report.html>")
        return 2

    path = Path(sys.argv[1])
    html = path.read_text(encoding="utf-8")
    lower = html.lower()
    issues: list[str] = []

    if re.search(r"https?://|//cdn|<script\b[^>]*\bsrc=|<link\b[^>]*\bhref=", html, flags=re.I):
        issues.append("Report appears to use external URLs, scripts, or linked stylesheets.")

    if "@page" not in html or "portrait" not in lower:
        issues.append("Missing A4 portrait print CSS.")

    if not re.search(r"\b(contents|目录)\b", html, flags=re.I):
        issues.append("Missing dedicated contents/目录 section.")

    exhibit_count = len(re.findall(r"Exhibit\s+\d+|class=\"[^\"]*\bexhibit\b|class=\"[^\"]*\bchart-block\b", html, flags=re.I))
    if exhibit_count < 5:
        issues.append(f"Only {exhibit_count} exhibit-like modules found; complete reports usually need at least 5.")

    if not re.search(r"source|来源|assumption|假设|caveat|限制|口径", html, flags=re.I):
        issues.append("Missing source/assumption/caveat language.")

    if not re.search(r"background-image|url\(|data:image|cover-art|cover-image", html, flags=re.I):
        issues.append("No cover background image or image-like background detected.")

    placeholders = re.findall(r"<!--|TODO|placeholder|REPLACE_WITH|lorem|占位|未填写|待补", html, flags=re.I)
    if placeholders:
        issues.append("Placeholder or draft markers remain.")

    blocks = page_blocks(html)
    thin_pages = []
    for index, block in enumerate(blocks, start=1):
        if "cover" in block[:300].lower():
            continue
        text = strip_tags(block)
        chars = count_chinese_chars(text)
        has_exhibit = bool(re.search(r"Exhibit|exhibit|chart-block|table|svg", block, flags=re.I))
        if chars < 120 and not has_exhibit:
            thin_pages.append(str(index))
    if thin_pages:
        issues.append("Low-density pages detected: " + ", ".join(thin_pages))

    if issues:
        print("Report QA failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Report QA passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
