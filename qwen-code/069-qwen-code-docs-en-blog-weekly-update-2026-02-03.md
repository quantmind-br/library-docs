---
title: 'Qwen Code Weekly: LSP Support, Batch Runner, New Languages'
url: https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-02-03
source: github_pages
fetched_at: 2026-04-09T09:05:34.063124257-03:00
rendered_js: true
word_count: 484
summary: This weekly blog post details the latest updates to Qwen Code, highlighting major new features such as a comprehensive Extension System, native Language Server Protocol (LSP) support for advanced code intelligence, and a batch-runner tool for efficient testing. It also covers UI architecture unification and international language additions.
tags:
    - qwen-code
    - lsp-support
    - extension-system
    - batch-testing
    - ai-agent
    - software-update
category: blog
---

[Blog](https://qwenlm.github.io/qwen-code-docs/en/blog/ "Blog")

Qwen Code Weekly: LSP Support, Batch Runner, New Languages

This week we released v0.8.1, v0.8.2 stable versions and v0.9.0 preview, adding LSP support, batch-runner evaluation tool, unified UI architecture, and Japanese & Portuguese language support.

- Released two stable versions (v0.8.1, v0.8.2) and one preview version (v0.9.0), fixing 5+ core issues and adding several new features
- TypeScript SDK v0.1.4 released, positioned as CodeAgent as a Service
- Total Stars reached 17984, topping GitHub Trending Ranking #10 last Friday

## ✨ New Features[](#-new-features)

### New Extension System[](#new-extension-system)

Qwen Code introduces a brand new Extension system that supports packaging prompts, MCP servers, subagents, skills, and custom commands. Even more exciting, plugins from Gemini CLI Extensions Gallery and Claude Code Marketplace can be directly installed into Qwen Code!

Supports installation from multiple sources: Git repositories, local paths, Claude Code Marketplace, and Gemini CLI Extensions Gallery.

**Available Extension Management Commands:**

CommandDescription`/extensions` or `/extensions list`List all installed extensions`/extensions install <source>`Install extension (supports git URL, local path, marketplace)`/extensions uninstall <name>`Uninstall specified extension`/extensions enable <name>`Enable extension`/extensions disable <name>`Disable extension`/extensions update <name>`Update specified extension`/extensions update --all`Update all extensions`/extensions detail <name>`View extension details`/extensions explore [source]`Open extension marketplace page

👇 Installation and practice demo

### New LSP Support[](#new-lsp-support)

Introduced native Language Server Protocol (LSP) support, enabling advanced code intelligence. This implementation allows AI agents to understand code semantically, not just rely on text-based search.

Can be launched via `qwen --experimental-lsp`, see PR [#1401](https://github.com/QwenLM/qwen-code/pull/1401) 

![](https://gw.alicdn.com/imgextra/i1/O1CN01kxCAnu1c0SPDCZsUt_!!6000000003538-2-tps-1694-948.png)

### New batch-runner Batch Evaluation Tool[](#new-batch-runner-batch-evaluation-tool)

Added a Python-based concurrent executor that runs multiple Qwen Code tasks in parallel using isolated git worktrees. This enables efficient multi-task batch testing and benchmarking across multiple models. Evaluation artifacts and trajectories can be saved locally and viewed online.

See PR [#1640](https://github.com/QwenLM/qwen-code/pull/1640) 

![](https://gw.alicdn.com/imgextra/i1/O1CN01u4j9r41kwde3UBP5X_!!6000000004748-2-tps-3372-1026.png)

### New Unified UI Architecture, `@qwen-code/webui`[](#new-unified-ui-architecture-qwen-codewebui)

Extracted from VSCode IDE Companion into a shared `@qwen-code/webui` package, introducing a unified UI architecture. This allows UI components to be reused across VSCode, Chrome extensions, Web interfaces, and Share features.

See PR [#1543](https://github.com/QwenLM/qwen-code/pull/1543) 

![](https://gw.alicdn.com/imgextra/i3/O1CN01TCL20a1z4KvCdwzf4_!!6000000006660-2-tps-2002-1222.png)

### Enhanced Internationalization, Japanese & Portuguese Support[](#enhanced-internationalization-japanese--portuguese-support)

Community-driven addition of Japanese and Portuguese support. Users in these regions can now have their native language set as the default UI display and LLM output language upon first installation.

See PR [#1616](https://github.com/QwenLM/qwen-code/pull/1616) 

![](https://gw.alicdn.com/imgextra/i3/O1CN01Dgc5oS1Qp2lDyfC7S_!!6000000002024-2-tps-1468-406.png)

### Community Ecosystem: Zed, Skills Officially Integrate Qwen Code[](#community-ecosystem-zed-skills-officially-integrate-qwen-code)

- [ACP Registry PR #15](https://github.com/agentclientprotocol/registry/pull/15)
- [Vercel Skills PR #99](https://github.com/vercel-labs/skills/pull/99)

![](https://gw.alicdn.com/imgextra/i3/O1CN01w2ee3M1i2BaxOb2hr_!!6000000004354-2-tps-3082-1238.png)

## 🔧 Important Fixes[](#-important-fixes)

- **Multimodal Input Support** ([#1564](https://github.com/QwenLM/qwen-code/pull/1564) ) - Support for images, PDFs, audio, and other input formats
- **Security Fixes** ([#1638](https://github.com/QwenLM/qwen-code/pull/1638) , [#1601](https://github.com/QwenLM/qwen-code/pull/1601) ) - Fixed command injection vulnerabilities
- **Anthropic SDK Fix** ([#1663](https://github.com/QwenLM/qwen-code/pull/1663) ) - Avoid passing undici agent
- **React Version Consistency** ([#1659](https://github.com/QwenLM/qwen-code/pull/1659) ) - Fixed version inconsistencies in package.json and lockfile
- **ACP Sub-agent Streaming Fix** ([#1626](https://github.com/QwenLM/qwen-code/pull/1626) ) - Fixed streaming of text and reasoning blocks

**Upgrade**: Run `npm i @qwen-code/qwen-code@latest -g` to upgrade to the latest version.

For questions or suggestions, welcome to [GitHub Issues](https://github.com/QwenLM/qwen-code/issues) !

Last updated on March 31, 2026

[Announcing Qwen Code: An AI Coding Agent That Thinks Like a Programmer](https://qwenlm.github.io/qwen-code-docs/en/blog/thinks-like-a-programmer/ "Announcing Qwen Code: An AI Coding Agent That Thinks Like a Programmer")[Qwen Code Weekly: Agent Skills GA, One-Click Install, Session Export](https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-02-09/ "Qwen Code Weekly: Agent Skills GA, One-Click Install, Session Export")