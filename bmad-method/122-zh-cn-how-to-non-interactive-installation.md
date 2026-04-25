---
title: 非交互式安装
url: https://docs.bmad-method.org/zh-cn/how-to/non-interactive-installation/
source: sitemap
fetched_at: 2026-04-08T11:33:17.748545884-03:00
rendered_js: false
word_count: 137
summary: This document details how to perform non-interactive installations of BMad using command-line arguments, which is useful for automation and scripting. It specifies available parameters like `--directory`, `--modules`, and `--tools`, along with rules for handling invalid inputs.
tags:
    - non-interactive-install
    - command-line-arguments
    - automated-deployment
    - bmad-setup
    - api-flags
category: guide
---

## 非交互式安装

使用命令行参数（flags）以非交互方式安装 BMad。适用于以下场景：

- 自动化部署和 CI/CD 流水线
- 脚本化安装
- 跨多个项目的批量安装
- 使用已知配置的快速安装

参数描述示例`--directory <path>`安装目录`--directory ~/projects/myapp``--modules <modules>`逗号分隔的模块 ID`--modules bmm,bmb``--tools <tools>`逗号分隔的工具/IDE ID（使用 `none` 跳过）`--tools claude-code,cursor` 或 `--tools none``--action <type>`对现有安装的操作：`install`（默认）、`update` 或 `quick-update``--action quick-update`

参数描述默认值`--user-name <name>`智能体使用的名称系统用户名`--communication-language <lang>`智能体通信语言英语`--document-output-language <lang>`文档输出语言英语`--output-folder <path>`输出文件夹路径\_bmad-output

参数描述`-y, --yes`接受所有默认值并跳过提示`-d, --debug`启用清单生成的调试输出

`--modules` 参数可用的模块 ID：

- `bmm` — BMad Method Master
- `bmb` — BMad Builder

查看 [BMad 注册表](https://github.com/bmad-code-org) 获取可用的外部模块。

`--tools` 参数可用的工具 ID：

**推荐：** `claude-code`、`cursor`

运行一次 `npx bmad-method install` 交互式安装以查看完整的当前支持工具列表，或查看 [平台代码配置](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml)。

模式描述示例完全非交互式提供所有参数以跳过所有提示`npx bmad-method install --directory . --modules bmm --tools claude-code --yes`半交互式提供部分参数；BMad 提示其余部分`npx bmad-method install --directory . --modules bmm`仅使用默认值使用 `-y` 接受所有默认值`npx bmad-method install --yes`不包含工具跳过工具/IDE 配置`npx bmad-method install --modules bmm --tools none`

```bash

#!/bin/bash
npxbmad-methodinstall\
--directory"${GITHUB_WORKSPACE}"\
--modulesbmm\
--toolsclaude-code\
--user-name"CI Bot"\
--communication-languageEnglish\
--document-output-languageEnglish\
--output-folder_bmad-output\
--yes
```

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionupdate\
--modulesbmm,bmb,custom-module
```

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionquick-update
```

- 项目中完全配置的 `_bmad/` 目录
- 为所选模块和工具配置的智能体和工作流
- 用于生成产物的 `_bmad-output/` 文件夹

BMad 会验证你提供的所有参数：

- **目录** — 必须是具有写入权限的有效路径
- **模块** — 对无效的模块 ID 发出警告（但不会失败）
- **工具** — 对无效的工具 ID 发出警告（但不会失败）
- **操作** — 必须是以下之一：`install`、`update`、`quick-update`

无效值将：

1. 显示错误并退出（对于目录等关键选项）
2. 显示警告并跳过（对于可选项目）
3. 回退到交互式提示（对于缺失的必需值）

### 安装失败，提示 `Invalid directory`

[Section titled “安装失败，提示 Invalid directory”](#%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5%E6%8F%90%E7%A4%BA-invalid-directory)

- 目录路径必须存在（或其父目录必须存在）
- 您需要写入权限
- 路径必须是绝对路径或相对于当前目录的正确相对路径

<!--THE END-->

- 验证模块 ID 是否正确
- 外部模块必须在注册表中可用