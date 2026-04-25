---
title: 为什么解决方案阶段很重要
url: https://docs.bmad-method.org/zh-cn/explanation/why-solutioning-matters/
source: sitemap
fetched_at: 2026-04-08T11:33:01.426858679-03:00
rendered_js: false
word_count: 104
summary: This document explains the importance of the 'solutioning' phase, which translates high-level planning into concrete technical architectures and work breakdowns. It highlights that failing to do this upfront leads to integration conflicts and rework, while proper execution ensures consistency across all development stories.
tags:
    - solutioning-process
    - technical-architecture
    - epic-story
    - conflict-prevention
    - development-lifecycle
category: guide
---

Phase 3（solutioning）把“要做什么”（planning 产出）转成“如何实现”（`architecture` 设计 + 工作拆分）。它的核心价值是：在开发前先把跨 `epic` 的关键技术决策写清楚，让后续 `story` 实施保持一致。

## 不做 solutioning 会出现什么问题

[Section titled “不做 solutioning 会出现什么问题”](#%E4%B8%8D%E5%81%9A-solutioning-%E4%BC%9A%E5%87%BA%E7%8E%B0%E4%BB%80%E4%B9%88%E9%97%AE%E9%A2%98)

```text

智能体 1 使用 REST API 实现 Epic 1
智能体 2 使用 GraphQL 实现 Epic 2
结果：API 设计不一致，集成成本暴涨
```

当多个智能体在没有共享 `architecture` 指南的前提下并行实现不同 `epic`，它们会各自做局部最优决策，最后在集成阶段发生冲突。

## 做了 solutioning 后会发生什么

[Section titled “做了 solutioning 后会发生什么”](#%E5%81%9A%E4%BA%86-solutioning-%E5%90%8E%E4%BC%9A%E5%8F%91%E7%94%9F%E4%BB%80%E4%B9%88)

```text

architecture 工作流先定规则："所有 API 使用 GraphQL"
所有智能体按同一套决策实现 story
结果：实现一致，集成顺滑
```

solutioning 的本质不是“多写一份文档”，而是把高冲突风险决策前置，作为所有 `story` 的共享上下文。

## solutioning 与 planning 的边界

[Section titled “solutioning 与 planning 的边界”](#solutioning-%E4%B8%8E-planning-%E7%9A%84%E8%BE%B9%E7%95%8C)

方面Planning（阶段 2）Solutioning（阶段 3）核心问题做什么，为什么做？如何做，再如何拆分工作？输出物FRs/NFRs（需求）`architecture` + `epic/story` 拆分主导角色PMArchitect → PM受众利益相关者开发人员文档PRD（FRs/NFRs）架构文档 + epics 文件决策层级业务目标与范围技术策略与实现边界

**让跨 `epic` 的关键技术决策显式、可追溯、可复用。**

这能直接降低：

- API 风格冲突（REST vs GraphQL）
- 数据模型与命名约定不一致
- 状态管理方案分裂
- 安全策略分叉
- 中后期返工成本

## 什么时候需要 solutioning

[Section titled “什么时候需要 solutioning”](#%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E9%9C%80%E8%A6%81-solutioning)

流程需要 solutioning？Quick Flow否 - 完全跳过BMad Method Simple可选BMad Method Complex是Enterprise是

## 跳过 solutioning 的代价

[Section titled “跳过 solutioning 的代价”](#%E8%B7%B3%E8%BF%87-solutioning-%E7%9A%84%E4%BB%A3%E4%BB%B7)

在复杂项目中跳过该阶段，常见后果是：

- **集成问题**在冲刺中期暴露
- **返工**由实现冲突引发
- **整体研发周期拉长**
- **技术债务**因模式不一致持续累积

想进一步理解冲突是如何发生并被架构约束消除的，可继续阅读 [防止智能体冲突](https://docs.bmad-method.org/zh-cn/explanation/preventing-agent-conflicts/)。如果你要把这些约束落到执行层，请结合 [项目上下文](https://docs.bmad-method.org/zh-cn/explanation/project-context/) 与 [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/) 一起阅读。

- [防止智能体冲突](https://docs.bmad-method.org/zh-cn/explanation/preventing-agent-conflicts/)
- [项目上下文](https://docs.bmad-method.org/zh-cn/explanation/project-context/)
- [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)