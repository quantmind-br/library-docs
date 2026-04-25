---
title: Established Projects FAQ
url: https://docs.bmad-method.org/explanation/established-projects-faq/
source: sitemap
fetched_at: 2026-04-08T11:29:57.074820579-03:00
rendered_js: false
word_count: 299
summary: This document provides answers to frequently asked questions regarding the BMad Method (BMM), advising on best practices for working with established codebases, including when to run `document-project` and using Quick Flow.
tags:
    - bmad-method
    - quick-flow
    - established-projects
    - codebase-guidance
    - documentation-practices
category: guide
---

Quick answers to common questions about working on established projects with the BMad Method (BMM).

- [Do I have to run document-project first?](#do-i-have-to-run-document-project-first)
- [What if I forget to run document-project?](#what-if-i-forget-to-run-document-project)
- [Can I use Quick Flow for established projects?](#can-i-use-quick-flow-for-established-projects)
- [What if my existing code doesn’t follow best practices?](#what-if-my-existing-code-doesnt-follow-best-practices)

### Do I have to run document-project first?

[Section titled “Do I have to run document-project first?”](#do-i-have-to-run-document-project-first)

Highly recommended, especially if:

- No existing documentation
- Documentation is outdated
- AI agents need context about existing code

You can skip it if you have comprehensive, up-to-date documentation including `docs/index.md` or will use other tools or techniques to aid in discovery for the agent to build on an existing system.

### What if I forget to run document-project?

[Section titled “What if I forget to run document-project?”](#what-if-i-forget-to-run-document-project)

Don’t worry about it - you can do it at any time. You can even do it during or after a project to help keep docs up to date.

### Can I use Quick Flow for established projects?

[Section titled “Can I use Quick Flow for established projects?”](#can-i-use-quick-flow-for-established-projects)

Yes! Quick Flow works great for established projects. It will:

- Auto-detect your existing stack
- Analyze existing code patterns
- Detect conventions and ask for confirmation
- Generate context-rich spec that respects existing code

Perfect for bug fixes and small features in existing codebases.

### What if my existing code doesn’t follow best practices?

[Section titled “What if my existing code doesn’t follow best practices?”](#what-if-my-existing-code-doesnt-follow-best-practices)

Quick Flow detects your conventions and asks: “Should I follow these existing conventions?” You decide:

- **Yes** → Maintain consistency with current codebase
- **No** → Establish new standards (document why in spec)

BMM respects your choice — it won’t force modernization, but it will offer it.

**Have a question not answered here?** Please [open an issue](https://github.com/bmad-code-org/BMAD-METHOD/issues) or ask in [Discord](https://discord.gg/gk8jAdXWmj) so we can add it!