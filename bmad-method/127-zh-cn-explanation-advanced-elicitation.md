---
title: 高级启发
url: https://docs.bmad-method.org/zh-cn/explanation/advanced-elicitation/
source: sitemap
fetched_at: 2026-04-08T11:32:41.218585029-03:00
rendered_js: false
word_count: 33
summary: This document explains the advanced elicitation technique, which involves having a large language model re-examine its own output using specified structured reasoning frameworks instead of simple iterative refinement. It details methods like pre-mortem and first principles to pressure test assumptions and find loopholes in existing drafts.
tags:
    - advanced-elicitation
    - reasoning-frameworks
    - llm-review
    - critical-thinking
    - pre-mortem
    - structured-output
category: guide
---

高级启发（advanced elicitation）是“第二轮思考”机制：不是笼统地让模型“再来一次”，而是让它按指定推理方法重审自己的输出。

你先有一版输出（方案、文案、分析或规范），再通过某种推理框架做二次审视，例如：

- 事前复盘（Pre-mortem）
- 第一性原理
- 逆向思维（Inversion）
- 红队/蓝队
- 苏格拉底式追问

这种“带方法名的重审”通常比“再优化一下”更有效，因为它会强制模型从特定角度进攻已有答案。

- 你已有可用初稿，但怀疑还不够扎实
- 你想压力测试关键假设或找潜在漏洞
- 你面对高风险内容，需要更高置信度
- 你想要替代解法，而不是同义改写

<!--THE END-->

1. 模型先给出若干与你内容相关的方法候选
2. 你选择一种（或重抽）
3. 模型按该方法重审并展示改进
4. 你决定采纳、丢弃、继续下一轮或结束

如果你还处在方向发散阶段，可先用 [头脑风暴](https://docs.bmad-method.org/zh-cn/explanation/brainstorming/)；如果你需要多角色权衡讨论，可用 [派对模式](https://docs.bmad-method.org/zh-cn/explanation/party-mode/)。在进入实现前做问题发现时，可结合 [对抗性评审](https://docs.bmad-method.org/zh-cn/explanation/adversarial-review/)。

模式核心目标典型输入典型输出`advanced elicitation`二次推理与补强已有初稿/方案风险更清晰、论证更完整的改进版`bmad-brainstorming`发散创意并收敛目标模糊或方向开放想法池与行动方向`bmad-party-mode`多角色讨论权衡需要跨角色协同判断多视角共识或争议点

- 它不能替代原始输入质量：初稿太空，二次推理也会受限
- 它会产出更多“可疑问题”，需要你做人工判别
- 连续多轮会出现收益递减，建议在关键决策点使用

<!--THE END-->

- [头脑风暴](https://docs.bmad-method.org/zh-cn/explanation/brainstorming/)
- [派对模式](https://docs.bmad-method.org/zh-cn/explanation/party-mode/)
- [对抗性评审](https://docs.bmad-method.org/zh-cn/explanation/adversarial-review/)