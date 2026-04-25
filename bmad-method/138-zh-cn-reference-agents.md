---
title: 智能体
url: https://docs.bmad-method.org/zh-cn/reference/agents/
source: sitemap
fetched_at: 2026-04-08T11:33:25.496120146-03:00
rendered_js: false
word_count: 89
summary: This page lists the default intelligent agents provided by the BMad Method (Agile suite), detailing their skill IDs, menu trigger codes, and primary workflows.
tags:
    - bmad-method
    - intelligent-agents
    - workflow-triggers
    - skill-ids
    - product-management
    - development
category: reference
---

本页列出 BMad Method 默认提供的 BMM（Agile 套件）智能体，包括它们的 skill ID、菜单触发器和主要 workflow。

智能体Skill ID触发器主要 workflowAnalyst (Mary)`bmad-analyst``BP`、`RS`、`CB`、`DP`Brainstorm、Research、Create Brief、Document ProjectProduct Manager (John)`bmad-pm``CP`、`VP`、`EP`、`CE`、`IR`、`CC`Create/Validate/Edit PRD、Create Epics and Stories、Implementation Readiness、Correct CourseArchitect (Winston)`bmad-architect``CA`、`IR`Create Architecture、Implementation ReadinessDeveloper (Amelia)`bmad-agent-dev``DS`、`QD`、`QA`、`CR`、`SP`、`CS`、`ER`Dev Story、Quick Dev、QA Test Generation、Code Review、Sprint Planning、Create Story、Epic RetrospectiveUX Designer (Sally)`bmad-ux-designer``CU`Create UX DesignTechnical Writer (Paige)`bmad-tech-writer``DP`、`WD`、`US`、`MG`、`VD`、`EC`Document Project、Write Document、Update Standards、Mermaid Generate、Validate Doc、Explain Concept

- `Skill ID` 是直接调用该智能体的名称（例如 `bmad-agent-dev`）
- 触发器是进入智能体会话后可使用的菜单短码
- QA 测试生成由 `bmad-qa-generate-e2e-tests` workflow skill 处理，通过 Developer 智能体调用；完整 TEA 能力位于独立模块

### 工作流触发器（通常不需要额外参数）

[Section titled “工作流触发器（通常不需要额外参数）”](#%E5%B7%A5%E4%BD%9C%E6%B5%81%E8%A7%A6%E5%8F%91%E5%99%A8%E9%80%9A%E5%B8%B8%E4%B8%8D%E9%9C%80%E8%A6%81%E9%A2%9D%E5%A4%96%E5%8F%82%E6%95%B0)

多数触发器会直接启动结构化 workflow。你只需输入触发码，然后按流程提示提供信息。

示例：`CP`（Create PRD）、`DS`（Dev Story）、`CA`（Create Architecture）、`QD`（Quick Dev）

部分触发器进入自由对话模式，需要你在触发码后描述需求。

智能体触发器你需要提供的内容Technical Writer (Paige)`WD`要撰写的文档主题与目标Technical Writer (Paige)`US`要补充到标准中的偏好/规范Technical Writer (Paige)`MG`图示类型与图示内容描述Technical Writer (Paige)`VD`待验证文档与关注点Technical Writer (Paige)`EC`需要解释的概念名称

示例：

```text

WD 写一份 Docker 部署指南
MG 画一个认证流程的时序图
EC 解释模块系统如何运作
```

- [技能（Skills）参考](https://docs.bmad-method.org/zh-cn/reference/commands/)
- [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)
- [核心工具参考](https://docs.bmad-method.org/zh-cn/reference/core-tools/)