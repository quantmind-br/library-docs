---
title: 项目上下文
url: https://docs.bmad-method.org/zh-cn/explanation/project-context/
source: sitemap
fetched_at: 2026-04-08T11:32:57.5228906-03:00
rendered_js: false
word_count: 125
summary: This document describes the purpose and structure of `project-context.md`, a file designed to explicitly store project-level constraints, technical preferences, and architectural boundaries for AI agents. Its goal is to ensure consistency across different workflows by providing rules that are not easily inferable from code alone.
tags:
    - project-context
    - ai-agent
    - architectural-constraints
    - technical-standards
    - consistency-rules
    - development-workflow
category: reference
---

`project-context.md` 是面向 AI 智能体的项目级上下文文件。它的定位不是教程步骤，而是“实现约束说明”：把你的技术偏好、架构边界和工程约定沉淀成可复用规则，让不同工作流、不同智能体在多个 `story` 中做出一致决策。

## project context 解决什么问题

[Section titled “project context 解决什么问题”](#project-context-%E8%A7%A3%E5%86%B3%E4%BB%80%E4%B9%88%E9%97%AE%E9%A2%98)

没有统一上下文时，智能体往往会：

- 套用通用最佳实践，而不是你的项目约定
- 在不同 `story` 中做出不一致实现
- 漏掉代码里不易推断的隐性约束

有 `project-context.md` 时，这些高频偏差会明显减少，因为关键规则在进入实现前已经被显式声明。

多数实现相关工作流会自动加载 `project-context.md`（若存在），并把它作为共享上下文参与决策。

**常见加载方包括：**

- `bmad-create-architecture`：在 solutioning 时纳入你的技术偏好
- `bmad-create-story`：按项目约定拆分和描述 story
- `bmad-dev-story`：约束实现路径和代码风格
- `bmad-code-review`：按项目标准做一致性校验
- `bmad-quick-dev`：在快速实现中避免偏离既有模式
- `bmad-sprint-planning`、`bmad-retrospective`、`bmad-correct-course`：读取项目级背景

场景建议时机目标**新项目（架构前）**在 `bmad-create-architecture` 前手动创建先声明技术偏好，避免架构偏航**新项目（架构后）**通过 `bmad-generate-project-context` 生成并补充把架构决策转成可执行规则**既有项目**先生成，再人工校对让智能体学习现有约定而非重造体系**Quick Flow 场景**在 `bmad-quick-dev` 前或过程中维护弥补跳过完整规划带来的上下文缺口

建议聚焦两类信息：**技术栈与版本**、**关键实现规则**。原则是记录“智能体不容易从代码片段直接推断”的内容。

```markdown

## Technology Stack & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand (not Redux)
- Testing: Vitest, Playwright, MSW
- Styling: Tailwind CSS with custom design tokens
```

```markdown

## Critical Implementation Rules
**TypeScript Configuration:**
- Strict mode enabled — no `any` types without explicit approval
- Use `interface` for public APIs, `type` for unions/intersections
**Code Organization:**
- Components in `/src/components/` with co-located `.test.tsx`
- API calls use the `apiClient` singleton — never fetch directly
**Testing Patterns:**
- Integration tests use MSW to mock API responses
- E2E tests cover critical user journeys only
```

- **误解 1：它是操作手册。**  
  不是。操作步骤请看 how-to；这里强调的是规则与边界。
- **误解 2：写得越全越好。**  
  不对。冗长且泛化的“最佳实践”会稀释有效约束。
- **误解 3：写一次就结束。**  
  这是动态文件。架构变化、约定变化后要同步更新。

默认位置是 `_bmad-output/project-context.md`。工作流优先在该位置查找，也会扫描项目内的 `**/project-context.md`。

如需可执行步骤说明，请阅读 [How-to：项目上下文](https://docs.bmad-method.org/zh-cn/how-to/project-context/)；如果你在既有项目落地这套机制，可参考 [既有项目常见问题](https://docs.bmad-method.org/zh-cn/explanation/established-projects-faq/)。整体流程定位见 [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)。

- [管理项目上下文（How-to）](https://docs.bmad-method.org/zh-cn/how-to/project-context/)
- [既有项目常见问题](https://docs.bmad-method.org/zh-cn/explanation/established-projects-faq/)
- [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)