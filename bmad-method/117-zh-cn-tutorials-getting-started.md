---
title: 快速入门
url: https://docs.bmad-method.org/zh-cn/tutorials/getting-started/
source: sitemap
fetched_at: 2026-04-08T11:33:35.237273075-03:00
rendered_js: false
word_count: 229
summary: This document provides a comprehensive guide to using the BMad framework, detailing a structured, AI-driven workflow for software development. It explains how specialized agents and workflows guide users through planning, architecture design, feature breakdown, and iterative implementation across different project complexities.
tags:
    - ai-development
    - software-workflow
    - bmad-method
    - agent-guidance
    - project-lifecycle
    - sprint-planning
category: guide
---

使用 AI 驱动的工作流更快地构建软件，通过专门的智能体引导你完成规划、架构设计和实现。

- 为新项目安装并初始化 BMad Method
- 使用 **BMad-Help** —— 你的智能向导，它知道下一步该做什么
- 根据项目规模选择合适的规划路径
- 从需求到可用代码，逐步推进各个阶段
- 有效使用智能体和工作流

## 认识 BMad-Help：你的智能向导

[Section titled “认识 BMad-Help：你的智能向导”](#%E8%AE%A4%E8%AF%86-bmad-help%E4%BD%A0%E7%9A%84%E6%99%BA%E8%83%BD%E5%90%91%E5%AF%BC)

**BMad-Help 是开始使用 BMad 的最快方式。** 你不需要记住工作流或阶段 —— 只需询问，BMad-Help 就会：

- **检查你的项目**，看看已经完成了什么
- **根据你安装的模块显示你的选项**
- **推荐下一步** —— 包括第一个必需任务
- **回答问题**，比如”我有一个 SaaS 想法，应该从哪里开始？“

在你的 AI IDE 中直接调用技能名：

也可以带着问题一起调用，获得更贴合上下文的建议：

```plaintext

bmad-help 我有一个 SaaS 产品的想法，我已经知道我想要的所有功能。我应该从哪里开始？
```

BMad-Help 将回应：

- 针对你的情况推荐什么
- 第一个必需任务是什么
- 其余流程是什么样的

BMad-Help 不仅回答问题 —— **它会在每个工作流结束时自动运行**，告诉你确切地下一步该做什么。无需猜测，无需搜索文档 —— 只需对下一个必需工作流的清晰指导。

BMad 通过带有专门 AI 智能体的引导工作流帮助你构建软件。该过程遵循四个阶段：

阶段名称发生什么1分析头脑风暴、研究、产品简报 *（可选）*2规划创建需求（PRD 或技术规范）3解决方案设计设计架构 *（仅适用于 BMad Method/Enterprise）*4实现逐个史诗、逐个故事地构建

[**打开工作流地图**](https://docs.bmad-method.org/zh-cn/reference/workflow-map/) 以探索阶段、工作流和上下文管理。

根据项目的复杂性，BMad 提供三种规划路径：

路径最适合创建的文档**Quick Flow**错误修复、简单功能、范围清晰（1-15 个故事）仅技术规范**BMad Method**产品、平台、复杂功能（10-50+ 个故事）PRD + 架构 + UX**Enterprise**合规、多租户系统（30+ 个故事）PRD + 架构 + 安全 + DevOps

在项目目录中打开终端并运行：

如果你想使用最新预发布版本（而不是默认发布通道），可以改用 `npx bmad-method@next install`。

当提示选择模块时，选择 **BMad Method**。

安装程序会创建两个文件夹：

- `_bmad/` — 智能体、工作流、任务和配置
- `_bmad-output/` — 目前为空，但这是你的工件将被保存的地方

完成阶段 1-3。**为每个工作流使用新对话。**

此阶段中的所有工作流都是可选的：

- **头脑风暴**（`bmad-brainstorming`） — 引导式构思
- **研究**（`bmad-market-research` / `bmad-domain-research` / `bmad-technical-research`） — 市场、领域和技术研究
- **创建产品简报**（`bmad-create-product-brief`） — 推荐的基础文档

**对于 BMad Method 和 Enterprise 路径：**

1. 在新对话中调用 **PM 智能体**（`bmad-agent-pm`）
2. 运行 `bmad-create-prd` 工作流（`bmad-create-prd`）
3. 输出：`PRD.md`

**对于 Quick Flow 路径：**

- 运行 `bmad-quick-dev` —— 它会在一个工作流里同时处理规划与实现，可直接进入实现阶段

### 阶段 3：解决方案设计（BMad Method/Enterprise）

[Section titled “阶段 3：解决方案设计（BMad Method/Enterprise）”](#%E9%98%B6%E6%AE%B5-3%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88%E8%AE%BE%E8%AE%A1bmad-methodenterprise)

**创建架构**

1. 在新对话中调用 **Architect 智能体**（`bmad-agent-architect`）
2. 运行 `bmad-create-architecture`（`bmad-create-architecture`）
3. 输出：包含技术决策的架构文档

**创建史诗和故事**

1. 在新对话中调用 **PM 智能体**（`bmad-agent-pm`）
2. 运行 `bmad-create-epics-and-stories`（`bmad-create-epics-and-stories`）
3. 工作流使用 PRD 和架构来创建技术信息丰富的故事

**实现就绪检查** *（强烈推荐）*

1. 在新对话中调用 **Architect 智能体**（`bmad-agent-architect`）
2. 运行 `bmad-check-implementation-readiness`（`bmad-check-implementation-readiness`）
3. 验证所有规划文档之间的一致性

规划完成后，进入实现阶段。**每个工作流应该在新对话中运行。**

调用 **Developer 智能体**（`bmad-agent-dev`）并运行 `bmad-sprint-planning`（`bmad-sprint-planning`）。这会创建 `sprint-status.yaml` 来跟踪所有史诗和故事。

对于每个故事，使用新对话重复此周期：

步骤智能体工作流命令目的1DEV`bmad-create-story``bmad-create-story`从史诗创建故事文件2DEV`bmad-dev-story``bmad-dev-story`实现故事3DEV`bmad-code-review``bmad-code-review`质量验证 *（推荐）*

完成史诗中的所有故事后，调用 **Developer 智能体**（`bmad-agent-dev`）并运行 `bmad-retrospective`（`bmad-retrospective`）。

你已经学习了使用 BMad 构建的基础：

- 安装了 BMad 并为你的 IDE 进行了配置
- 使用你选择的规划路径初始化了项目
- 创建了规划文档（PRD、架构、史诗和故事）
- 了解了实现的构建周期

你的项目现在拥有：

```text

your-project/
├── _bmad/                                   # BMad 配置
├── _bmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md                           # 你的需求文档
│   │   ├── architecture.md                  # 技术决策
│   │   └── epics/                           # 史诗和故事文件
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml               # 冲刺跟踪
│   └── project-context.md                   # 实现规则（可选）
└── ...
```

工作流命令智能体目的**`bmad-help`** ⭐`bmad-help`任意**你的智能向导 —— 随时询问任何问题！**`bmad-create-prd``bmad-create-prd`PM创建产品需求文档`bmad-create-architecture``bmad-create-architecture`Architect创建架构文档`bmad-generate-project-context``bmad-generate-project-context`Analyst创建项目上下文文件`bmad-create-epics-and-stories``bmad-create-epics-and-stories`PM将 PRD 分解为史诗`bmad-check-implementation-readiness``bmad-check-implementation-readiness`Architect验证规划一致性`bmad-sprint-planning``bmad-sprint-planning`DEV初始化冲刺跟踪`bmad-create-story``bmad-create-story`DEV创建故事文件`bmad-dev-story``bmad-dev-story`DEV实现故事`bmad-code-review``bmad-code-review`DEV审查已实现的代码

**我总是需要架构吗？** 仅对于 BMad Method 和 Enterprise 路径。Quick Flow 从技术规范跳转到实现。

**我可以稍后更改我的计划吗？** 可以。`bmad-correct-course` 工作流用于处理实现过程中的范围变化。

**如果我想先进行头脑风暴怎么办？** 在开始 PRD 之前，调用 Analyst 智能体（`bmad-agent-analyst`）并运行 `bmad-brainstorming`（`bmad-brainstorming`）。

**我需要遵循严格的顺序吗？** 不一定。一旦你了解了流程，你可以使用上面的快速参考直接运行工作流。

- **在工作流期间** — 智能体通过问题和解释引导你
- **社区** — [Discord](https://discord.gg/gk8jAdXWmj) (#bmad-method-help, #report-bugs-and-issues)

准备好开始了吗？安装 BMad，运行 `bmad-help`，让你的智能向导为你引路。