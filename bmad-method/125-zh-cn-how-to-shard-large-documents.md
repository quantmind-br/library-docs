---
title: 文档分片指南
url: https://docs.bmad-method.org/zh-cn/how-to/shard-large-documents/
source: sitemap
fetched_at: 2026-04-08T11:33:21.864883442-03:00
rendered_js: false
word_count: 57
summary: This guide explains the `bmad-shard-doc` workflow, which splits large Markdown documents into smaller, chapter-organized files to reduce context window pressure for AI models.
tags:
    - markdown-splitting
    - context-management
    - workflow-guide
    - document-parsing
category: guide
---

## 文档分片指南

当单个 Markdown 文档过大、影响模型读取时，可使用 `bmad-shard-doc` 工作流把文档拆成按章节组织的小文件，降低上下文压力。

- 你确认当前工具/模型在关键步骤无法一次读入完整文档
- 文档体量已明显影响工作流稳定性或响应质量
- 你需要保留原文结构，但希望按 `##` 章节拆分维护

文档分片会按二级标题（`## Heading`）把大型 Markdown 文件拆成多个子文件，并生成一个 `index.md` 作为入口。

```text

分片前：
_bmad-output/planning-artifacts/
└── PRD.md（大型 50k token 文件）
分片后：
_bmad-output/planning-artifacts/
└── prd/
├── index.md                    # 带有描述的目录
├── overview.md                 # 第 1 节
├── user-requirements.md        # 第 2 节
├── technical-requirements.md   # 第 3 节
└── ...                         # 其他章节
```

### 1. 运行 `bmad-shard-doc` 工作流

[Section titled “1. 运行 bmad-shard-doc 工作流”](#1-%E8%BF%90%E8%A1%8C-bmad-shard-doc-%E5%B7%A5%E4%BD%9C%E6%B5%81)

```text

智能体：你想分片哪个文档？
用户：docs/PRD.md
智能体：默认目标位置：docs/prd/
接受默认值？[y/n]
用户：y
智能体：正在分片 PRD.md...
✓ 已创建 12 个章节文件
✓ 已生成 index.md
✓ 完成！
```

BMad 工作流使用**双重发现机制**：

1. **先查完整文档** - 查找 `document-name.md`
2. **再查分片入口** - 查找 `document-name/index.md`
3. **优先级规则** - 若两者并存，默认优先完整文档；若你要强制使用分片版本，请删除或重命名完整文档

<!--THE END-->

- 原始完整文档（可保留，但不建议与分片长期并存；并存时默认优先读取完整文档）
- 分片目录（如 `document-name/index.md` + 各章节文件）
- 对工作流透明的自动识别行为（无需额外配置）

<!--THE END-->

- [如何自定义 BMad](https://docs.bmad-method.org/zh-cn/how-to/customize-bmad/) - 了解高级配置与工作流定制边界
- [如何升级到 v6](https://docs.bmad-method.org/zh-cn/how-to/upgrade-to-v6/) - 在迁移过程中处理文档与目录结构变化