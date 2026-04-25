---
title: 既有项目常见问题
url: https://docs.bmad-method.org/zh-cn/explanation/established-projects-faq/
source: sitemap
fetched_at: 2026-04-08T11:32:51.280715631-03:00
rendered_js: false
word_count: 98
summary: This document addresses frequently asked questions regarding the application of the BMad Method within existing software projects, providing guidance on when to run documentation workflows, using Quick Flow, handling code that deviates from best practices, and knowing when to escalate from a quick approach to the full method.
tags:
    - bmad-method
    - established-projects
    - quick-flow
    - development-workflow
    - coding-guidelines
category: guide
---

关于在 established projects（既有项目）中使用 BMad Method 的高频问题，快速说明如下。

- [我必须先运行文档梳理工作流吗？](#%E6%88%91%E5%BF%85%E9%A1%BB%E5%85%88%E8%BF%90%E8%A1%8C%E6%96%87%E6%A1%A3%E6%A2%B3%E7%90%86%E5%B7%A5%E4%BD%9C%E6%B5%81%E5%90%97)
- [如果我忘了运行文档梳理怎么办？](#%E5%A6%82%E6%9E%9C%E6%88%91%E5%BF%98%E4%BA%86%E8%BF%90%E8%A1%8C%E6%96%87%E6%A1%A3%E6%A2%B3%E7%90%86%E6%80%8E%E4%B9%88%E5%8A%9E)
- [既有项目可以直接用 Quick Flow 吗？](#%E6%97%A2%E6%9C%89%E9%A1%B9%E7%9B%AE%E5%8F%AF%E4%BB%A5%E7%9B%B4%E6%8E%A5%E7%94%A8-quick-flow-%E5%90%97)
- [如果现有代码不符合最佳实践怎么办？](#%E5%A6%82%E6%9E%9C%E7%8E%B0%E6%9C%89%E4%BB%A3%E7%A0%81%E4%B8%8D%E7%AC%A6%E5%90%88%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E6%80%8E%E4%B9%88%E5%8A%9E)
- [什么时候该从 Quick Flow 切到完整方法？](#%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E8%AF%A5%E4%BB%8E-quick-flow-%E5%88%87%E5%88%B0%E5%AE%8C%E6%95%B4%E6%96%B9%E6%B3%95)

不绝对必须，但通常强烈建议先运行 `bmad-document-project`，尤其当：

- 项目文档缺失或明显过时
- 新成员或智能体难以快速理解现有系统
- 你希望后续 `workflow` 基于真实现状而不是猜测执行

如果你已有完整且最新的文档（包含 `docs/index.md`），并且能通过其他方式提供足够上下文，也可以跳过。

可以随时补跑，不影响你继续推进当前任务。很多团队会在迭代中期或里程碑后再运行一次，用来把”代码现状”回写到文档里。

### 既有项目可以直接用 Quick Flow 吗？

[Section titled “既有项目可以直接用 Quick Flow 吗？”](#%E6%97%A2%E6%9C%89%E9%A1%B9%E7%9B%AE%E5%8F%AF%E4%BB%A5%E7%9B%B4%E6%8E%A5%E7%94%A8-quick-flow-%E5%90%97)

可以。Quick Flow（例如 `bmad-quick-dev`）在既有项目里通常很高效，尤其适合：

- 小功能增量
- 缺陷修复
- 风险可控的局部改动

它会尝试识别现有技术栈、代码模式和约定，并据此生成更贴近现状的实现方案。

### 如果现有代码不符合最佳实践怎么办？

[Section titled “如果现有代码不符合最佳实践怎么办？”](#%E5%A6%82%E6%9E%9C%E7%8E%B0%E6%9C%89%E4%BB%A3%E7%A0%81%E4%B8%8D%E7%AC%A6%E5%90%88%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E6%80%8E%E4%B9%88%E5%8A%9E)

工作流会优先问你：“是否沿用当前约定？”你可以主动选择：

- **沿用**：优先保持一致性，降低短期改动风险
- **升级**：建立新标准，并在 tech-spec 或架构中写明迁移理由与范围

BMad Method 不会强制“立即现代化”，而是把决策权交给你。

### 什么时候该从 Quick Flow 切到完整方法？

[Section titled “什么时候该从 Quick Flow 切到完整方法？”](#%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E8%AF%A5%E4%BB%8E-quick-flow-%E5%88%87%E5%88%B0%E5%AE%8C%E6%95%B4%E6%96%B9%E6%B3%95)

当任务出现以下信号时，建议从 Quick Flow 升级到完整 BMad Method：

- 改动跨多个 `epic` 或多个子系统
- 需要明确 `architecture` 决策，否则容易冲突
- 涉及较大协作面、较高回归风险或复杂验收要求

如果你不确定，先让 `bmad-help` 判断当前阶段更稳妥的 workflow。

**还有问题？** 欢迎在 [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) 或 [Discord](https://discord.gg/gk8jAdXWmj) 提问。

如果你想了解这套接入方式的操作步骤，可继续阅读 [How-to：既有项目](https://docs.bmad-method.org/zh-cn/how-to/established-projects/) 与 [How-to：项目上下文](https://docs.bmad-method.org/zh-cn/how-to/project-context/)。想理解快速流程在方法论中的定位，可参见 [快速开发](https://docs.bmad-method.org/zh-cn/explanation/quick-dev/)。

- [既有项目（How-to）](https://docs.bmad-method.org/zh-cn/how-to/established-projects/)
- [项目上下文（Explanation）](https://docs.bmad-method.org/zh-cn/explanation/project-context/)
- [管理项目上下文（How-to）](https://docs.bmad-method.org/zh-cn/how-to/project-context/)