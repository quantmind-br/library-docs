---
title: 如何自定义 BMad
url: https://docs.bmad-method.org/zh-cn/how-to/customize-bmad/
source: sitemap
fetched_at: 2026-04-08T11:33:09.565926517-03:00
rendered_js: false
word_count: 95
summary: 本文档详细介绍了如何使用 `.customize.yaml` 文件来深度定制智能体（agent）的行为、角色设定、长期记忆、自定义菜单项以及启动时执行的关键动作。通过修改此配置文件，用户可以精确控制智能体的个性化表现和工作流程。
tags:
    - customization-guide
    - agent-configuration
    - yaml-editing
    - persona-setting
    - workflow-integration
    - metadata
category: guide
---

使用 `.customize.yaml` 文件，自定义智能体（agent）的行为、角色（persona）和菜单，同时在后续更新中保留你的改动。

- 你想修改智能体名称、身份设定或沟通风格
- 你需要让智能体长期记住项目约束和背景信息
- 你希望增加自定义菜单项，触发自己的工作流或提示
- 你希望智能体每次启动都先执行固定动作

安装完成后，每个已安装智能体都会在下面目录生成一个 `.customize.yaml`：

```text

_bmad/_config/agents/
├── core-bmad-master.customize.yaml
├── bmm-dev.customize.yaml
├── bmm-pm.customize.yaml
└── ...（每个已安装智能体一个文件）
```

打开目标智能体的 `.customize.yaml`。各段都可选，只改你需要的部分即可。

部分作用方式用途`agent.metadata`覆盖覆盖智能体显示名称`persona`覆盖设置角色、身份、风格和原则`memories`追加添加智能体长期记忆的上下文`menu`追加增加指向工作流或提示的菜单项`critical_actions`追加定义智能体启动时要执行的动作`prompts`追加创建可复用提示，供菜单 `action` 引用

标记为 **覆盖** 的部分会完全替换默认配置；标记为 **追加** 的部分会在默认配置基础上累加。

**智能体名称（`agent.metadata`）**

修改智能体的显示名称：

```yaml

agent:
metadata:
name: 'Spongebob'# 默认值："Amelia"
```

**角色（`persona`）**

替换智能体的人设、职责和沟通风格：

```yaml

persona:
role: 'Senior Full-Stack Engineer'
identity: 'Lives in a pineapple (under the sea)'
communication_style: 'Spongebob annoying'
principles:
- 'Never Nester, Spongebob Devs hate nesting more than 2 levels deep'
- 'Favor composition over inheritance'
```

`persona` 会覆盖默认整段配置，所以启用时请把四个字段都填全。

**记忆（`memories`）**

添加智能体会长期记住的上下文：

```yaml

memories:
- 'Works at Krusty Krab'
- 'Favorite Celebrity: David Hasselhoff'
- 'Learned in Epic 1 that it is not cool to just pretend that tests have passed'
```

**菜单项（`menu`）**

给智能体菜单添加自定义项。每个条目都需要 `trigger`、目标（`workflow` 路径或 `action` 引用）和 `description`：

```yaml

menu:
- trigger: my-workflow
workflow: 'my-custom/workflows/my-workflow.yaml'
description: My custom workflow
- trigger: deploy
action: '#deploy-prompt'
description: Deploy to production
```

**启动关键动作（`critical_actions`）**

定义智能体启动时执行的指令：

```yaml

critical_actions:
- 'Check the CI Pipelines with the XYZ Skill and alert user on wake if anything is urgently needing attention'
```

**可复用提示（`prompts`）**

创建可复用提示，菜单项可通过 `action="#id"` 调用：

```yaml

prompts:
- id: deploy-prompt
content: |
Deploy the current branch to production:
1. Run all tests
2. Build the project
3. Execute deployment script
```

编辑完成后，重新安装以应用配置：

安装程序会识别现有安装，并给出以下选项：

选项作用**Quick Update**更新所有模块到最新版本，并应用你的自定义配置**Modify BMad Installation**进入完整安装流程，用于增删模块

如果只是调整 `.customize.yaml`，优先选 **Quick Update**。

**改动没有生效？**

- 运行 `npx bmad-method install` 并选择 **Quick Update** 以应用更改
- 检查 YAML 语法是否正确（尤其是缩进）
- 确认你编辑的是目标智能体对应的 `.customize.yaml`

**智能体无法加载？**

- 使用在线 YAML 验证器检查 YAML 语法错误
- 确保取消注释后没有遗留空字段
- 可先回退到模板，再逐项恢复自定义配置

**需要重置某个智能体？**

- 清空或删除智能体的 `.customize.yaml` 文件
- 运行 `npx bmad-method install` 并选择 **Quick Update** 以恢复默认设置

对现有 BMad Method 工作流和技能的深度自定义能力即将推出。

关于构建扩展模块和自定义现有模块的指南即将推出。

- [文档分片指南](https://docs.bmad-method.org/zh-cn/how-to/shard-large-documents/) - 了解如何管理超长文档
- [命令参考](https://docs.bmad-method.org/zh-cn/reference/commands/) - 查看可用命令和工作流入口