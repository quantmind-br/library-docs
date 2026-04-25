---
title: 防止智能体冲突
url: https://docs.bmad-method.org/zh-cn/explanation/preventing-agent-conflicts/
source: sitemap
fetched_at: 2026-04-08T11:32:55.249588823-03:00
rendered_js: false
word_count: 138
summary: 本文档阐述了在多个AI智能体并行开发系统中，提前进行架构设计（architecture）的重要性，它通过统一关键技术决策、制定共识和标准协议，来避免不同模块之间出现接口不一致、命名冲突或状态管理碎片化等问题，从而确保集成流畅性。
tags:
    - system-architecture
    - ai-agent
    - design-patterns
    - technical-debt
    - solutioning
    - api-consistency
category: guide
---

当多个 AI 智能体并行实现系统时，冲突并不罕见。`architecture` 的作用，就是在 `solutioning` 阶段先统一关键决策，避免到 `epic/story` 实施时才暴露分歧。

没有架构约束时：

- 智能体 A 使用 REST，路径是 `/users/{id}`
- 智能体 B 使用 GraphQL mutations
- 结果：接口模式不一致，调用方和集成层都变复杂

有架构约束时：

- ADR 明确规定：“客户端与服务端统一使用 GraphQL”
- 所有智能体遵循同一套 API 规则

没有架构约束时：

- 智能体 A 使用 `snake_case` 列名
- 智能体 B 使用 `camelCase` 列名
- 结果：schema 不一致，查询与迁移成本上升

有架构约束时：

- 标准文档统一命名约定和迁移策略
- 所有智能体按同一模式实现

没有架构约束时：

- 智能体 A 使用 Redux
- 智能体 B 使用 React Context
- 结果：状态层碎片化，维护复杂度增加

有架构约束时：

- ADR 明确状态管理方案
- 不同 `story` 的实现保持一致

## architecture 如何前置消解冲突

[Section titled “architecture 如何前置消解冲突”](#architecture-%E5%A6%82%E4%BD%95%E5%89%8D%E7%BD%AE%E6%B6%88%E8%A7%A3%E5%86%B2%E7%AA%81)

每个关键技术选择都至少包含：

- 背景（为什么要做这个决策）
- 备选方案（有哪些选择）
- 最终决策（采用什么）
- 理由（为什么这样选）
- 后果（接受哪些权衡）

### 2. 把 FR/NFR 映射到技术实现

[Section titled “2. 把 FR/NFR 映射到技术实现”](#2-%E6%8A%8A-frnfr-%E6%98%A0%E5%B0%84%E5%88%B0%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0)

`architecture` 不是抽象原则清单，而是把需求落到可执行方案：

- FR-001（用户管理）→ GraphQL mutations
- FR-002（移动端性能）→ 查询裁剪与缓存策略

至少覆盖以下共识：

- 目录结构
- 命名约定
- 代码组织方式
- 测试策略

## architecture 是所有 epic 的共享上下文

[Section titled “architecture 是所有 epic 的共享上下文”](#architecture-%E6%98%AF%E6%89%80%E6%9C%89-epic-%E7%9A%84%E5%85%B1%E4%BA%AB%E4%B8%8A%E4%B8%8B%E6%96%87)

把架构文档看作每个智能体在实施前都要阅读的“公共协议”：

```text

PRD: "做什么"
↓
architecture: "如何做"
↓
智能体 A 读 architecture → 实现 Epic 1
智能体 B 读 architecture → 实现 Epic 2
智能体 C 读 architecture → 实现 Epic 3
↓
结果：实现一致、集成顺畅
```

主题示例决策API 风格GraphQL vs REST vs gRPC数据存储PostgreSQL vs MongoDB认证机制JWT vs Session状态管理Redux vs Context vs Zustand样式方案CSS Modules vs Tailwind vs Styled Components测试体系Jest + Playwright vs Vitest + Cypress

如需先理解为什么要在实施前做 solutioning，可阅读 [为什么解决方案设计很重要](https://docs.bmad-method.org/zh-cn/explanation/why-solutioning-matters/)；如果你想把这些约束落地到项目执行，可继续看 [项目上下文](https://docs.bmad-method.org/zh-cn/explanation/project-context/)。流程全景见 [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)。

- [为什么解决方案阶段很重要](https://docs.bmad-method.org/zh-cn/explanation/why-solutioning-matters/)
- [项目上下文](https://docs.bmad-method.org/zh-cn/explanation/project-context/)
- [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)