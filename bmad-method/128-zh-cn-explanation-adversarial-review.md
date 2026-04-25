---
title: 对抗性评审
url: https://docs.bmad-method.org/zh-cn/explanation/adversarial-review/
source: sitemap
fetched_at: 2026-04-08T11:32:43.338815044-03:00
rendered_js: false
word_count: 52
summary: 对抗性评审是一种系统性的代码或方案审查方法，其核心要求是评审者必须主动寻找可验证的问题点而非仅确认无误，从而提高发现问题的召回率和深度。
tags:
    - adversarial-review
    - code-review
    - quality-assurance
    - problem-finding
    - evaluation-method
category: concept
---

对抗性评审（adversarial review）是一种“强制找问题”的评审方法：不允许直接“Looks good”，必须给出可验证发现，或者明确解释为什么没有发现。

常规评审容易落入确认偏差：快速扫一遍，没有明显报错，就批准。  
对抗性评审反过来要求评审者先假设“问题存在”，再去定位证据。

核心规则：

- 必须产出问题发现或明确的无发现理由
- 发现要具体、可追溯、可操作
- 评审对象是工件本身，而不是作者意图

<!--THE END-->

- 强制深入阅读，减少“浏览式批准”
- 更容易发现“缺了什么”，不只看“写错了什么”
- 发现通常更结构化，便于后续分诊与修复
- 在新上下文评审时，能降低“先入为主”偏差

它不是某个单一 workflow 独占，而是一种可复用评审模式，常见于：

- 代码评审
- 规范/方案评审
- 实施就绪检查
- 高风险改动复核

因为系统被要求“必须找问题”，它会提高召回率，也会提高误报率。  
你会看到：

- 吹毛求疵型发现
- 语义误解型发现
- 偶发幻觉型发现

所以它本质上是**高召回、需人工分诊**的策略，而不是“自动真理机”。

如果你想把该策略放进快速实现节奏中，可参见 [快速开发](https://docs.bmad-method.org/zh-cn/explanation/quick-dev/)；若要做多轮推理补强，可参见 [高级启发](https://docs.bmad-method.org/zh-cn/explanation/advanced-elicitation/)。整体流程位置请见 [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)。

`bmad-quick-dev` 关注执行效率与边界控制；对抗性评审关注问题发现质量。  
一个解决“跑得稳不稳”，一个解决“看得深不深”，两者互补而非替代。

普通评审可能是：

> “实现基本没问题，先过。”

对抗性评审更像：

> 1. HIGH：`login.ts` 缺失失败重试限流
> 2. HIGH：会话令牌存储在 `localStorage`，存在 XSS 风险
> 3. MEDIUM：失败登录缺少审计日志
> 4. LOW：魔法数字 `3600` 建议替换为命名常量

重点不是“更凶”，而是“更可执行”。

- [快速开发](https://docs.bmad-method.org/zh-cn/explanation/quick-dev/)
- [高级启发](https://docs.bmad-method.org/zh-cn/explanation/advanced-elicitation/)
- [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)