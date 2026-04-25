---
title: 工作流地图
url: https://docs.bmad-method.org/zh-cn/reference/workflow-map/
source: sitemap
fetched_at: 2026-04-08T11:33:32.070893851-03:00
rendered_js: false
word_count: 71
summary: This document outlines the BMad Method (BMM), a phased workflow map designed to guide AI agents through developing complex projects by ensuring they understand the goal, rationale, and implementation steps at each stage. It details specific workflows for brainstorming, product definition, solutioning, and iterative development.
tags:
    - bmad-method
    - workflow-guide
    - ai-development
    - project-planning
    - agent-workflow
    - solutioning
category: guide
---

BMad Method（BMM）通过分阶段 workflow 逐步构建上下文，让智能体始终知道“做什么、为什么做、如何做”。这张地图用于快速查阅阶段目标、关键 workflow 和对应产出。

如果你不确定下一步，优先运行 `bmad-help`。它会基于你当前项目状态和已安装模块给出实时建议。

[在新标签页打开图表 ↗](https://docs.bmad-method.org/workflow-map-diagram.html)

在正式规划前，先验证问题空间与关键假设。

Workflow目的产出`bmad-brainstorming`通过引导式创意方法扩展方案空间`brainstorming-report.md``bmad-domain-research`、`bmad-market-research`、`bmad-technical-research`验证领域、市场与技术假设研究发现`bmad-create-product-brief`沉淀产品方向与战略愿景`product-brief.md`

定义“为谁做、做什么”。

Workflow目的产出`bmad-create-prd`明确 FR/NFR 与范围边界`PRD.md``bmad-create-ux-design`在 UX 复杂场景下补齐交互与体验方案`ux-spec.md`

## 阶段 3：解决方案设计（Solutioning）

[Section titled “阶段 3：解决方案设计（Solutioning）”](#%E9%98%B6%E6%AE%B5-3%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88%E8%AE%BE%E8%AE%A1solutioning)

定义“如何实现”并拆分可交付工作单元。

Workflow目的产出`bmad-create-architecture`显式记录技术决策与架构边界`architecture.md`（含 ADR）`bmad-create-epics-and-stories`将需求拆分为可实施的 epics/storiesepics 文件与 story 条目`bmad-check-implementation-readiness`实施前 gate 检查PASS / CONCERNS / FAIL 结论

按 story 节奏持续交付与校验。

Workflow目的产出`bmad-sprint-planning`初始化迭代追踪（通常每项目一次）`sprint-status.yaml``bmad-create-story`准备下一个可实施 story`story-[slug].md``bmad-dev-story`按规范实现 story可运行代码与测试`bmad-code-review`验证实现质量通过或变更请求`bmad-correct-course`处理中途重大方向调整更新后的计划或重路由`bmad-sprint-status`跟踪冲刺与 story 状态状态更新`bmad-retrospective`epic 完成后复盘经验与改进项

当任务范围小且目标清晰时，可跳过阶段 1-3 直接推进：

Workflow目的产出`bmad-quick-dev`统一快流：意图澄清、规划、实现、审查、呈现`spec-*.md` + 代码变更

每个阶段产出都会成为下一阶段输入：PRD 约束架构，架构约束开发，story 约束实现。没有这条链路，智能体更容易在跨 story 时出现不一致决策。

**创建方式：**

- **手动创建**：在 `_bmad-output/project-context.md` 记录项目规则
- **自动生成**：运行 `bmad-generate-project-context` 从架构或代码库提取

<!--THE END-->

- [命令与技能参考](https://docs.bmad-method.org/zh-cn/reference/commands/)
- [智能体参考](https://docs.bmad-method.org/zh-cn/reference/agents/)
- [核心工具参考](https://docs.bmad-method.org/zh-cn/reference/core-tools/)
- [项目上下文说明](https://docs.bmad-method.org/zh-cn/explanation/project-context/)