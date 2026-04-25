---
title: 快速开发
url: https://docs.bmad-method.org/zh-cn/explanation/quick-dev/
source: sitemap
fetched_at: 2026-04-08T11:32:59.796375085-03:00
rendered_js: false
word_count: 67
summary: Quick Dev是一种旨在最小化“意图到代码”人机往返轮次的开发流程设计，它通过在关键节点保留人工判断和放大模型自主执行时间，平衡了速度与质量，核心在于将人类注意力从低价值确认转移至高价值决策。
tags:
    - quick-dev
    - workflow-design
    - ai-assisted-development
    - human-in-the-loop
    - process-optimization
category: guide
---

`bmad-quick-dev` 的目标很直接：在保证质量边界的前提下，把“意图到代码”的人机往返轮次降到最低。

![快速开发工作流图](https://docs.bmad-method.org/diagrams/quick-dev-diagram.png)

纯人工频繁盯流程会拖慢速度，纯自动又容易偏航。Quick Dev 做的是中间解：

- 在关键节点保留人工判断
- 在可控区间放大模型自主执行时长
- 通过规范与审查把偏航风险收回来

无论输入来自几句话、issue 链接、计划稿，还是 `epics.md` 的 `story`，都要先压缩成一个可执行目标。  
目标不清晰时，后续自动化越强，偏差成本越高。

目标明确后，workflow 会判断：

- 是不是“零爆炸半径”的 one-shot 变更
- 还是必须先走 planning 再实现

原则是：能走短路径就不走长路径，但不能为了快跳过必要边界。

当目标与规范足够清晰，模型会承担更长段的连续实现。  
这一步省下的是“重复确认成本”，不是“质量成本”。

Quick Dev 会区分问题来源：

- **意图层问题**：需求理解本身不对
- **规范层问题**：tech-spec 边界不够强
- **实现层问题**：本地代码缺陷

只有实现层问题才直接补代码；上层问题要回到对应层级重做。

人类主要在三个高杠杆时刻介入：

- 意图澄清
- 规范确认
- 最终结果审查

Quick Dev 不追求“全自动”，而是追求“最少但有效的人类判断”。  
它把人工注意力从大量低价值确认，转移到少量高价值决策。

Quick Dev 是执行节奏设计；`adversarial review` 是审查策略。二者经常配合：

- Quick Dev 负责高效推进实现
- 对抗性评审负责提高问题发现率并做分诊

也就是说，Quick Dev 解决“怎么更快且更稳地跑”，对抗性评审解决“怎么更狠地查问题”。

**适合：**

- 目标可定义、可验收的实现任务
- 希望减少流程摩擦但不放弃质量门

**不适合：**

- 目标长期模糊且频繁变化
- 团队尚未接受“先规格后长时执行”的工作方式

想进一步理解审查策略，可继续阅读 [对抗性评审](https://docs.bmad-method.org/zh-cn/explanation/adversarial-review/)；需要对已有输出进行第二轮推理时，可参考 [高级启发](https://docs.bmad-method.org/zh-cn/explanation/advanced-elicitation/)。若要查看它在完整流程中的位置，请参见 [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)。

- [对抗性评审](https://docs.bmad-method.org/zh-cn/explanation/adversarial-review/)
- [高级启发](https://docs.bmad-method.org/zh-cn/explanation/advanced-elicitation/)
- [工作流地图](https://docs.bmad-method.org/zh-cn/reference/workflow-map/)