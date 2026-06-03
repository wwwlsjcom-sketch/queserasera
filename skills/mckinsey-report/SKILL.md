---
name: mckinsey-report
description: >-
  生成竖屏、麦肯锡风格、内容丰富、带主题封面、高信息密度页面和 Exhibit 图表的单文件 HTML 咨询报告。
  Use for 麦肯锡风格HTML报告、竖屏咨询报告、高管汇报、董事会报告、
  数据分析报告、战略分析、行业研究、市场研究、投资分析、产品分析、
  风险分析、经营复盘、可打印PDF的HTML报告, and English requests for
  McKinsey-style HTML consulting reports, executive reports, board-ready HTML,
  strategy/data/market/industry/investment/product/risk reports, printable
  browser reports, or exhibit-rich consulting deliverables. Supports six
  report templates and 24 exhibit modules, producing self-contained portrait
  HTML with topic-specific cover art, long-form analysis, data-first
  visualization, responsive design, and print/PDF readiness.
---

# McKinsey Report

## Purpose

生成一份**竖屏、纵向滚动、单文件自包含的 HTML 咨询报告**，风格接近专业咨询公司交付物：内容分析要有厚度，逻辑要清晰，图表要 Exhibit 化，页面要适合浏览器阅读和打印成 PDF。

不要生成横屏 PPT、16:9 slide-like 页面、营销 landing page 或纯 dashboard，除非用户明确要求。

## Required References

生成 HTML 前必须读取：

- `references/html-consulting-report.md`：报告结构、Exhibit、视觉系统和质量清单。
- `references/template-router.md` 和 `references/template-matrix.yaml`：根据报告类型、行业、受众和数据密度选择 6 个模板之一。
- `references/exhibit-router.md` 和 `references/exhibit-library.md`：根据分析任务和数据形态选择 24 个 Exhibit 模块。
- `references/cover-art-direction.md`：主题封面背景图、行业视觉差异化和标题排版规则。
- `references/page-density-standard.md`：每页信息密度、证据密度和页面 QA 标准。

从零生成完整报告时，先从 `assets/templates/` 选择一个模板母版，再以 `assets/html-report-template.html` 作为 HTML/CSS 视觉基线，不要完全自由发挥版式。

## Workflow

1. 阅读用户提供的所有材料，判断报告主题、受众、使用场景和决策问题。
2. 使用 `template-router.md` 和 `template-matrix.yaml` 选择报告模板与主题配色系统：classic-consulting、board-brief、market-intelligence、investment-memo、risk-review、product-strategy。配色必须根据行业、主题和受众变化，不能默认使用蓝色主导。
3. 提炼核心结论、支撑证据、关键矛盾、风险、情景和可能的决策含义。
4. 使用 `exhibit-router.md` 和 `exhibit-library.md` 选择 Exhibit 模块：普通报告 5-8 个，数据密集报告 8-12 个，且优先匹配真实数据形态。
5. 如果材料里有大量数据，先规划图表再写正文；遇到对比、趋势、排名、百分比、增速、份额、评分、概率、KPI 时，优先图表化，不要把数据埋在长表里。
6. 为封面生成或构造一张与主题、行业、报告类型匹配的背景图。优先使用生成式 raster image，并嵌入为 base64 data URI；若不能生成图片，则必须用自包含 CSS/SVG 构造主题背景，至少包含 3 个与主题相关的视觉元素，例如行业资产轮廓、数据纹理、流程/网络结构、地理/设备/场景线索。不能只用纯色、渐变、抽象网格或通用蓝色几何。标题排版必须根据图像留白和视觉重心调整。
7. 生成竖屏 portrait HTML：封面、执行摘要、独立目录页、3-6 个分析正文部分，以及适合主题的决策导向收束。
8. 每页都要有足够信息密度：至少包含结论、证据、解释、图表/表格/结构化模块中的多个元素；避免大片空白、单一卡片页、只有一张图和一句话的薄页面。
9. 每个主体章节都要有足够正文厚度：说明结论是什么、为什么成立、对受众意味着什么、需要注意哪些信号或限制。
10. 使用 McKinsey-style exhibit 图表：结论式标题、Exhibit 编号、清晰图例/轴线/注释。完整报告在材料支持时应包含关系/结构图、趋势/对比图、风险/优先级/选项图。
11. 在需要解释 “so what” 的地方加入管理层含义、证据面板、观察点、尽调清单、来源/假设注释或早停信号，避免报告只有图表和卡片。
12. 输出一个自包含 `.html` 文件，CSS、SVG/HTML 图表和封面图片都内嵌；不要依赖外部库、CDN、远程字体、远程图片或品牌 logo。
13. 交付前按 `references/html-consulting-report.md`、`references/page-density-standard.md` 的质量清单检查；能运行脚本时，运行 `scripts/validate_report.py <output.html>`。

## Non-Negotiables

- 必须是竖屏/portrait 报告页面，不是横屏幻灯片。
- 必须先选择 6 个模板之一，并根据内容选择 24 个 Exhibit 模块中的合适组合。
- 完整报告封面必须有主题背景图或同等质量的主题视觉背景，不允许只有纯色/渐变封面。
- 封面标题布局必须适配背景图留白，不能机械固定居中。
- 整体配色必须进行主题化选择，不能让蓝色/蓝灰成为默认主色。蓝色只能作为候选强调色之一；每份报告应选择 1 个主色、1 个辅助色、1 个风险/机会强调色和中性色系统。
- 必须有足够分析正文，不能只做薄摘要、卡片集合或表格集合。
- 每页都必须有足够信息密度，不能出现只有一个标题、一张图或少量卡片的大空白页面。
- 完整报告必须有独立目录页。
- 指标卡片和原始表格不能单独算作足够的图表多样性。
- 必须使用 Exhibit 逻辑：编号、结论式标题、清晰轴线/图例、主题化克制配色、来源/假设说明。
- 需要解释时必须加入管理层含义、证据面板、观察点或类似 “so what” 模块。
- 保留大卡片和细腻背景质感，但装饰不能压过分析内容。
- 不编造精确数据；推断型图表必须标注 qualitative / directional / illustrative / index-based。
- 图表文字不能裁切，节点不能被截断，表格不能造成横向溢出，移动端和打印版必须可读。

## Output

最终保存为描述性 `.html` 文件。用户提供目标路径时写入目标路径；否则保存到当前工作区并告知文件路径。
