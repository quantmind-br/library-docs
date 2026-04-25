---
title: 既有项目
url: https://docs.bmad-method.org/zh-cn/how-to/established-projects/
source: sitemap
fetched_at: 2026-04-08T11:33:10.674410708-03:00
rendered_js: false
word_count: 96
summary: This guide provides instructions for using the BMad Method when working on an existing or legacy codebase, detailing steps like creating a project context and suggesting workflows based on the scope of changes.
tags:
    - bmad-method
    - existing-project
    - codebase-integration
    - project-context
    - workflow-guidance
category: guide
---

当你在现有项目或遗留代码库上工作时，本指南帮助你更稳妥地使用 BMad Method。

如果你是从零开始的新项目，建议先看[快速入门](https://docs.bmad-method.org/zh-cn/tutorials/getting-started/)；本文主要面向既有项目接入场景。

如果你通过 BMad 流程完成了所有 PRD 史诗和用户故事，请清理这些文件。归档它们、删除它们，或者在需要时依赖版本历史。不要将这些文件保留在：

- `docs/`
- `_bmad-output/planning-artifacts/`
- `_bmad-output/implementation-artifacts/`

## 步骤 2：创建项目上下文（project context）

[Section titled “步骤 2：创建项目上下文（project context）”](#%E6%AD%A5%E9%AA%A4-2%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE%E4%B8%8A%E4%B8%8B%E6%96%87project-context)

运行生成项目上下文工作流：

```bash

bmad-generate-project-context
```

这将扫描你的代码库以识别：

- 技术栈和版本
- 代码组织模式
- 命名约定
- 测试方法
- 框架相关模式

你可以先审阅并完善生成内容；如果更希望手动维护，也可以直接在 `_bmad-output/project-context.md` 创建并编辑。

[了解更多关于项目上下文](https://docs.bmad-method.org/zh-cn/explanation/project-context/)

你的 `docs/` 文件夹应包含简洁、组织良好的文档，准确代表你的项目：

- 意图和业务理由
- 业务规则
- 架构
- 任何其他相关的项目信息

对于复杂项目，可考虑使用 `bmad-document-project` 工作流。它会扫描整个项目并记录当前真实状态。

**当你不确定下一步做什么时，随时运行 `bmad-help`。** 这个智能指南会：

- 检查项目当前状态，识别哪些工作已经完成
- 根据你安装的模块给出可行选项
- 理解自然语言查询

```plaintext

bmad-help 我有一个现有的 Rails 应用，我应该从哪里开始？
bmad-help Quick Flow 和完整方法有什么区别？
bmad-help 显示我当前有哪些可用工作流
```

BMad-Help 还会在**每个工作流结束时自动运行**，明确告诉你下一步该做什么。

根据变更范围，你有两个主要选项：

范围推荐方法**小型更新或新增**运行 `bmad-quick-dev`，在单个工作流中完成意图澄清、规划、实现与审查。完整四阶段 BMad Method 往往过重。**重大变更或新增**从完整 BMad Method 开始，再按项目风险和协作需求调整流程严谨度。

在创建简报或直接进入 PRD 时，确保智能体：

- 查找并分析你现有的项目文档
- 读取与你当前系统匹配的项目上下文（project context）

你可以显式补充指令，但核心目标是让新功能与现有 architecture 和代码约束自然融合。

UX 工作是可选项。是否需要进入 UX 流程，不取决于“项目里有没有 UX”，而取决于：

- 你是否真的在做 UX 层面的变更
- 是否需要新增重要的 UX 设计或交互模式

如果本次只是对现有页面做小幅调整，通常不需要完整 UX 流程。

### 架构考量（architecture）

[Section titled “架构考量（architecture）”](#%E6%9E%B6%E6%9E%84%E8%80%83%E9%87%8Farchitecture)

在进行架构工作时，确保架构师：

- 使用正确且最新的文档输入
- 扫描并理解现有代码库

这一点非常关键：可避免“重复造轮子”，也能减少与现有架构冲突的设计决策。

- [**快速修复**](https://docs.bmad-method.org/zh-cn/how-to/quick-fixes/) - 错误修复和临时变更
- [**既有项目 FAQ**](https://docs.bmad-method.org/zh-cn/explanation/established-projects-faq/) - 关于在既有项目上工作的常见问题