---
title: 如何安装 BMad
url: https://docs.bmad-method.org/zh-cn/how-to/install-bmad/
source: sitemap
fetched_at: 2026-04-08T11:33:14.923706646-03:00
rendered_js: false
word_count: 64
summary: 本指南详细介绍了如何在本地项目中安装 BMad 工具包，指导用户完成模块选择、AI 工具集成和项目结构的初步设置，并说明了后续使用 bmad-help 命令进行验证和获取下一步操作指引。
tags:
    - bmad
    - 项目-初始化
    - ai-工具链
    - 本地-安装
    - 命令行-指南
category: guide
---

使用 `npx bmad-method install` 在项目中安装 BMad，并按需选择模块和 AI 工具。

如果你需要在命令行里一次性传入全部安装参数（例如 CI/CD 场景），请阅读[非交互式安装指南](https://docs.bmad-method.org/zh-cn/how-to/non-interactive-installation/)。

- 使用 BMad 启动新项目
- 将 BMad 添加到现有代码库
- 更新现有的 BMad 安装

安装程序会询问在哪里安装 BMad 文件：

- 当前目录（如果你自己创建了目录并从该目录运行，推荐用于新项目）
- 自定义路径

选择你使用的 AI 工具：

- Claude Code
- Cursor
- 其他

每种工具都有自己的 skills 集成方式。安装程序会生成用于激活工作流和智能体的轻量提示文件，并放到该工具约定的位置。

安装程序会显示可用的模块。选择你需要的模块——大多数用户只需要 **BMad Method**（软件开发模块）。

安装程序会引导你完成剩余步骤——设置、工具集成等。

以下目录结构仅作示例。工具相关目录会随你选择的平台变化（例如可能是 `.claude/skills`、`.cursor/skills` 或 `.kiro/skills`），并不一定会同时出现。

```text

your-project/
├── _bmad/
│   ├── bmm/            # 你选择的模块
│   │   └── config.yaml # 模块设置（后续如需可修改）
│   ├── core/           # 必需核心模块
│   └── ...
├── _bmad-output/       # 生成产物
├── .claude/            # Claude Code skills（如使用 Claude Code）
│   └── skills/
│       ├── bmad-help/
│       ├── bmad-persona/
│       └── ...
└── .cursor/            # Cursor skills（如使用 Cursor）
└── skills/
└── ...
```

运行 `bmad-help` 来验证一切正常并查看下一步操作。

**BMad-Help 是你的智能向导**，它会：

- 确认你的安装正常工作
- 根据你安装的模块显示可用内容
- 推荐你的第一步

你也可以向它提问：

```plaintext

bmad-help 我刚安装完成，应该先做什么？
bmad-help 对于 SaaS 项目我有哪些选项？
```

**安装程序抛出错误**——将输出复制粘贴到你的 AI 助手中，让它来解决问题。

**安装程序工作正常但后续出现问题**——你的 AI 需要 BMad 上下文才能提供帮助。请参阅[如何获取关于 BMad 的答案](https://docs.bmad-method.org/zh-cn/how-to/get-answers-about-bmad/)了解如何将你的 AI 指向正确的来源。