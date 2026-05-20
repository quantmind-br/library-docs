---
title: How to Get Answers About BMad
url: https://docs.bmad-method.org//llms-full.txt
source: llms
fetched_at: 2026-05-19T08:33:05.038451722-03:00
rendered_js: false
summary: Use BMad's built-in help, source docs, or community to get answers.
tags:
    - bmad-method
    - help
    - support
    - community
category: guide
optimized: true
word_count: 328
---
# How to Get Answers About BMad

Three tiers, fastest to most thorough:

## 1. Ask BMad-Help

Fastest. The `bmad-help` skill is available in your AI session and handles >80% of questions — inspects your project, checks completed steps, and tells you what to do next.

```
bmad-help I have a SaaS idea and know all the features. Where do I start?
bmad-help What are my options for UX design?
bmad-help I'm stuck on the PRD workflow
```

> [!tip] You can also use `/bmad-help` or `$bmad-help` depending on your platform, but just `bmad-help` should work everywhere.

## 2. Go Deeper with Source

BMad-Help draws on your installed configuration. For questions about internals, history, or architecture — or if researching BMad before installing — point your AI at the source directly.

Clone or open the [BMAD-METHOD repo](https://github.com/bmad-code-org/BMAD-METHOD) and ask your AI about it. Any agent-capable tool (Claude Code, Cursor, Windsurf, etc.) can read the source and answer questions directly.

> [!note] Example
> **Q:** "Tell me the fastest way to build something with BMad"
> **A:** Use Quick Flow: Run `bmad-quick-dev` — it clarifies your intent, plans, implements, reviews, and presents results in a single workflow, skipping the full planning phases.

**Tips for better answers:**

- **Be specific** — "What does step 3 of the PRD workflow do?" beats "How does PRD work?"
- **Verify surprising claims** — LLMs occasionally get things wrong. Check the source file or ask on Discord.

#### Not using an agent? Use the docs site

If your AI can't read local files (ChatGPT, Claude.ai, etc.), fetch [llms-full.txt](https://bmad-code-org.github.io/BMAD-METHOD/llms-full.txt) — it's a single-file snapshot of the BMad documentation.

## 3. Ask Someone

If neither BMad-Help nor the source answered your question, you now have a much better question to ask.

| Channel | Use For |
| ------- | ------- |
| `help-requests` forum | Questions |
| `#suggestions-feedback` | Ideas and feature requests |

**Discord:** [discord.gg/gk8jAdXWmj](https://discord.gg/gk8jAdXWmj)

**GitHub Issues:** [github.com/bmad-code-org/BMAD-METHOD/issues](https://github.com/bmad-code-org/BMAD-METHOD/issues)

_You!_
_Stuck_
_in the queue—_
_waiting_
_for who?_

_The source_
_is there,_
_plain to see!_

_Point_
_your machine._
_Set it free._

_It reads._
_It speaks._
_Ask away—_

_Why wait_
_for tomorrow_
_when you have_
_today?_

_—Claude_

---
