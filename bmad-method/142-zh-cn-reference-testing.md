---
title: 测试选项
url: https://docs.bmad-method.org/zh-cn/reference/testing/
source: sitemap
fetched_at: 2026-04-08T11:33:31.111229258-03:00
rendered_js: false
word_count: 140
summary: 'This document compares two testing approaches within BMad: the built-in QA workflow, which quickly generates runnable tests for smaller projects, and the advanced TEA (Test Architect) module, designed for large, regulated enterprises requiring structured governance and detailed traceability.'
tags:
    - bmad
    - qa-workflow
    - test-architecture
    - e2e-testing
    - testing-strategy
    - automation
category: guide
---

BMad 有两条测试路径：

- **内置 QA workflow**：快速生成可运行测试
- **TEA（可选模块）**：企业级测试策略与治理能力

维度内置 QATEA 模块最适合中小项目、快速补覆盖大型项目、受监管或复杂业务安装成本无需额外安装（BMM 内置）需通过安装器单独选择方法先生成测试，再迭代先定义策略，再执行并追溯测试类型API + E2EAPI、E2E、ATDD、NFR 等风险策略快乐路径 + 关键边界P0-P3 风险优先级workflow 数量1（Automate）9（设计/自动化/审查/追溯等）

内置 QA workflow（`bmad-qa-generate-e2e-tests`）是 BMM 模块的一部分，通过 Developer 智能体调用。目标是用你现有测试栈快速落地测试，不要求额外配置。

**触发方式：**

- 菜单触发器：`QA`（通过 Developer 智能体）
- skill：`bmad-qa-generate-e2e-tests`

QA Automate 流程通常包含 5 步：

1. 检测现有测试框架（如 Jest、Vitest、Playwright、Cypress）
2. 确认待测功能（手动指定或自动发现）
3. 生成 API 测试（状态码、结构、主路径与错误分支）
4. 生成 E2E 测试（语义定位器 + 可见结果断言）
5. 执行并修复基础失败项

**默认风格：**

- 仅使用标准框架 API
- UI 测试优先语义定位器（角色、标签、文本）
- 测试互相独立，不依赖顺序
- 避免硬编码等待/休眠

<!--THE END-->

- 要快速补齐某个功能的测试覆盖
- 团队希望先获得可运行基线，再逐步增强
- 项目暂不需要完整测试治理体系

## TEA（Test Architect）模块

[Section titled “TEA（Test Architect）模块”](#teatest-architect%E6%A8%A1%E5%9D%97)

TEA 提供专家测试 agent（Murat）与 9 个结构化 workflow，覆盖策略、执行、审查、追溯和发布门控。

**外部资源（英文）：**

- 文档: [TEA Module Docs](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)
- npm: [`bmad-method-test-architecture-enterprise`](https://www.npmjs.com/package/bmad-method-test-architecture-enterprise)

**安装：** `npx bmad-method install` 后选择 TEA 模块。

### TEA 的 9 个 workflow

[Section titled “TEA 的 9 个 workflow”](#tea-%E7%9A%84-9-%E4%B8%AA-workflow)

Workflow用途Test Design按需求建立测试策略ATDD基于验收标准驱动测试设计Automate使用高级模式生成自动化测试Test Review评估测试质量与覆盖完整性Traceability建立“需求—测试”追溯链路NFR Assessment评估性能/安全等非功能需求CI Setup配置 CI 中的测试执行Framework Scaffolding搭建测试工程基础结构Release Gate基于数据做发布/不发布决策

- 需要合规、审计或强追溯能力
- 需要跨功能做风险优先级管理
- 发布前存在明确质量门控流程
- 业务复杂，必须先建策略再写测试

按 BMad workflow-map，测试位于阶段 4（实施）：

1. epic 内逐个 story：开发（`DS` / `bmad-dev-story`）+ 代码审查（`CR` / `bmad-code-review`）
2. epic 完成后：用 `QA`（通过 Developer 智能体）或 TEA 的 Automate 统一生成/补齐测试
3. 最后执行复盘（`bmad-retrospective`）

内置 QA workflow 主要依据代码直接生成测试；TEA 可结合上游规划产物（如 PRD、architecture）实现更强追溯。

- [官方模块](https://docs.bmad-method.org/zh-cn/reference/modules/)
- [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)
- [智能体参考](https://docs.bmad-method.org/zh-cn/reference/agents/)