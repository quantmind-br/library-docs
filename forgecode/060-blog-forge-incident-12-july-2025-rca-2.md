---
title: 'ForgeCode Performance RCA: Root Cause Analysis of Quality Degradation on July 12, 2025'
url: https://forgecode.dev/blog/forge-incident-12-july-2025-rca-2/
source: sitemap
fetched_at: 2026-03-29T14:48:09.235383967-03:00
rendered_js: false
word_count: 364
summary: This document explains how a cost optimization feature that compacted conversation context caused quality degradation in the ForgeCode AI agent, leading to a rollback and plans for improved multi-turn evaluation testing.
tags:
    - ai-agent
    - quality-control
    - conversation-context
    - cost-optimization
    - feature-rollback
    - multi-turn-evaluation
    - llm-costs
category: guide
---

On July 12, 2025, we released v0.99.0, which included [PR #1068](https://github.com/antinomyhq/forge/pull/1068) introducing aggressive conversation compaction to reduce LLM costs. While successful at cutting costs by 40-50%, it significantly degraded response quality by removing crucial conversation context.

Users reported quality issues within 2 days. After internal testing confirmed the problem, we immediately released v0.100.0 on July 14 with the compaction feature reverted.

**Our evaluation system only tested single prompts, missing multi-turn conversation quality.**

The compaction feature triggered after every user message (`on_turn_end: true`), stripping context that our models needed for quality responses. In multi-turn scenarios (where users provide additional feedback after the agent completes work), the conversation context was getting compacted away, leading to poor quality responses.

Our evals never caught this because they focused on single prompts and judged the results of the agent loop, not ongoing conversations where users give feedback in the same conversation and context accumulation is critical.

Higher than expected early access signups created cost pressure. Rather than implementing waitlists, we chose aggressive optimization to keep the service open to all users. The feature worked perfectly for its intended purpose, just at the cost of quality we didn't anticipate.

- **Immediate**: Reverted the feature in v0.100.0 (2 days after user reports)
- **Long-term**: Building multi-turn evaluation system to catch these issues before deployment

<!--THE END-->

1. **Multi-turn evals** - Testing conversation quality across 3-5 message exchanges, not just single responses
2. **Quality gates** - Conversation quality scores must pass thresholds before any context affecting feature ships
3. **Gradual rollouts** - Canary releases for any feature touching core conversation logic

<!--THE END-->

- Bash terminal still has issues on windows, but we are working on it.

We messed up by prioritizing cost optimization over quality validation. The latest ForgeCode version (v0.100.5) has the issue fixed plus significant stability improvements.

**Please give ForgeCode another shot.** We've learned our lesson about shipping features that affect conversation quality without proper testing coverage.

* * *

*Questions? Reach out through our community channels. We're committed to transparency about what went wrong and how we're fixing it.*

- [ForgeCode v0.98.0 Release Article: Major Performance and Feature Updates](https://forgecode.dev/blog/forge-v0.98.0-release-article/)
- [AI Agent Best Practices: Maximizing Productivity with ForgeCode](https://forgecode.dev/blog/ai-agent-best-practices/)
- [MCP Security Prevention: Practical Strategies for AI Development - Part 2](https://forgecode.dev/blog/prevent-attacks-on-mcp-part2/)