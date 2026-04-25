---
title: 技能（Skills）
url: https://docs.bmad-method.org/zh-cn/reference/commands/
source: sitemap
fetched_at: 2026-04-08T11:33:27.985457674-03:00
rendered_js: false
word_count: 129
summary: This document explains how BMad generates and utilizes 'skills' after module installation, detailing various ways to invoke these skills—such as direct input or menu triggers—and categorizing skill types for agent actions, structured processes, and standalone tasks.
tags:
    - bmad-skill-system
    - module-installation
    - agent-invocation
    - cli-usage
    - task-automation
category: guide
---

每次运行 `npx bmad-method install`，BMad 会基于你选择的模块生成一组 **skills**。你可以直接输入 skill 名称调用 workflow、任务、工具或智能体角色。

机制调用方式适用场景**Skill**直接输入 skill 名（如 `bmad-help`）你已明确要运行哪个功能**智能体菜单触发器**先加载智能体，再输入短触发码（如 `DS`）你在智能体会话内连续切换任务

菜单触发器依赖“已激活的智能体会话”；skill 可独立运行。

安装程序会读取已选模块，为每个 agent / workflow / task / tool 生成一个 skill 目录，目录中包含 `SKILL.md` 入口文件。

Skill 类型生成行为Agent launcher加载角色设定并激活菜单Workflow skill加载 workflow 配置并执行步骤Task skill执行独立任务Tool skill执行独立工具

IDE / CLISkills 目录Claude Code`.claude/skills/`Cursor`.cursor/skills/`Windsurf`.windsurf/skills/`其他 IDE以安装器输出路径为准

示例（Claude Code）：

```text

.claude/skills/
├── bmad-help/
│   └── SKILL.md
├── bmad-create-prd/
│   └── SKILL.md
├── bmad-agent-dev/
│   └── SKILL.md
└── ...
```

skill 目录名就是调用名，例如 `bmad-agent-dev/` 对应 skill `bmad-agent-dev`。

- 在 IDE 中直接输入 `bmad-` 前缀查看补全候选
- 运行 `bmad-help` 获取基于当前项目状态的下一步建议
- 打开 skills 目录查看完整清单（这是最权威来源）

### 智能体技能（Agent Skills）

[Section titled “智能体技能（Agent Skills）”](#%E6%99%BA%E8%83%BD%E4%BD%93%E6%8A%80%E8%83%BDagent-skills)

加载一个角色化智能体，并保持其 persona 与菜单上下文。

示例 skill角色用途`bmad-agent-dev`Developer（Amelia）按规范实现 story`bmad-pm`Product Manager（John）创建与校验 PRD`bmad-architect`Architect（Winston）架构设计与约束定义

完整列表见 [智能体参考](https://docs.bmad-method.org/zh-cn/reference/agents/)。

无需先加载 agent，直接运行结构化流程。

示例 skill用途`bmad-create-prd`创建 PRD`bmad-create-architecture`创建架构方案`bmad-create-epics-and-stories`拆分 epics/stories`bmad-dev-story`实现指定 story`bmad-code-review`代码评审`bmad-quick-dev`快速流程（澄清→规划→实现→审查→呈现）

按阶段查看见 [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)。

### Task / Tool Skills

[Section titled “Task / Tool Skills”](#task--tool-skills)

独立任务，不依赖特定智能体上下文。

**`bmad-help`** 是最常用入口：它会读取项目状态并给出“下一步建议 + 对应 skill”。

更多核心任务和工具见 [核心工具参考](https://docs.bmad-method.org/zh-cn/reference/core-tools/)。

所有技能统一以 `bmad-` 开头，后接语义化名称（如 `bmad-agent-dev`、`bmad-create-prd`、`bmad-help`）。

**安装后看不到 skills：** 某些 IDE 需要手动启用 skills，或重启 IDE 才会刷新。

**缺少预期 skill：** 可能模块未安装或安装时未勾选。重新运行安装程序并确认模块选择。

**已移除模块的 skills 仍存在：** 安装器不会自动清理历史目录。手动删除旧 skill 目录后再重装可获得干净结果。

- [智能体参考](https://docs.bmad-method.org/zh-cn/reference/agents/)
- [核心工具参考](https://docs.bmad-method.org/zh-cn/reference/core-tools/)
- [模块参考](https://docs.bmad-method.org/zh-cn/reference/modules/)