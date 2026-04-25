---
title: 'Qwen Code Weekly: Token Limit Doubled, Real-time Usage Display, JetBrains Editor Support'
url: https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-03-20
source: github_pages
fetched_at: 2026-04-09T09:05:43.979497215-03:00
rendered_js: true
word_count: 870
summary: This blog post summarizes the latest features and bug fixes released for Qwen Code, highlighting key updates such as doubling the token limit to 16K, real-time token usage display, integration with JetBrains and Zed editors, and general stability improvements across various platforms.
tags:
    - qwen-code
    - ai-assistant
    - token-limit
    - editor-integration
    - software-updates
    - feature-release
category: blog
---

[Blog](https://qwenlm.github.io/qwen-code-docs/en/blog/ "Blog")

Qwen Code Weekly: Token Limit Doubled, Real-time Usage Display, JetBrains Editor Support

This week we released **v0.12.4** feature version and 2 bugfix releases, along with **v0.13.0-preview** preview version.

Want to try the preview features? Run `npm i @qwen-code/qwen-code@v0.13.0-preview.1 -g` to install.

After v0.12.0 launch, we received a lot of user feedback. This week we focused on fixing issues affecting user experience: Windows Chinese output encoding issues, interactive shell output loss, and API retry errors. On the feature side, we made comprehensive Token improvements: limit doubled to 16K, real-time usage display, and new `/context` command for detailed breakdown. We also added support for JetBrains and Zed editors.

## ✨ New Features[](#-new-features)

### Token Limit Doubled: Read More Context, Get More Information[](#token-limit-doubled-read-more-context-get-more-information)

Output Token limit increased from 8K to 16K, allowing AI to read more context and generate more complete responses. It also auto-detects model’s max\_tokens setting, no manual configuration needed.

**Use Cases:**

- AI can read more file content and understand larger project structures
- Generate more complete code and documents without piecing together segments
- Auto-adapt to different models’ Token limits without worrying about exceeding limits

See PR [#2411](https://github.com/QwenLM/qwen-code/pull/2411) , [#2356](https://github.com/QwenLM/qwen-code/pull/2356) , [#2362](https://github.com/QwenLM/qwen-code/pull/2362) 

### Real-time Token Usage Display (Preview)[](#real-time-token-usage-display-preview)

During AI thinking and generation, the interface shows Token consumption in real-time. No need to wait for conversation to end—know your Token usage anytime.

**Use Cases:**

- See Token consumption in real-time during conversations
- Adjust promptly when consumption is abnormal to avoid waste
- Compare Token costs of different tasks to optimize usage

See PR [#2445](https://github.com/QwenLM/qwen-code/pull/2445) 

![](https://gw.alicdn.com/imgextra/i2/O1CN01J3OhN228vlftWyHmx_!!6000000007995-1-tps-1280-720.gif)

### /context Command: View Token Usage Breakdown (Preview)[](#context-command-view-token-usage-breakdown-preview)

Use `/context` command to see detailed Token consumption in context window: which files are using how many Tokens, how much space is left—all at a glance.

**Use Cases:**

- View current conversation’s Token usage, know how much more content can fit
- Discover which files are using too many Tokens and decide if cleanup is needed
- Optimize context usage to keep AI focused on key content

See PR [#1835](https://github.com/QwenLM/qwen-code/pull/1835) 

![](https://gw.alicdn.com/imgextra/i3/O1CN01cekEKq1mRc3CM2AQd_!!6000000004951-1-tps-1280-720.gif)

### Zed and JetBrains Editor Integration[](#zed-and-jetbrains-editor-integration)

Besides VS Code, Qwen Code now supports Zed and JetBrains series editors (IntelliJ IDEA, PyCharm, WebStorm, etc.). See PR [#2372](https://github.com/QwenLM/qwen-code/pull/2372) .

**Use Cases:**

- Use Qwen Code directly in JetBrains IDEs without switching windows
- Zed editor users can also enjoy AI coding assistant
- Unified experience across different editors, no need to re-adapt when switching tools

Documentation:

- [JetBrains IDE | Qwen Code Docs](https://qwenlm.github.io/qwen-code-docs/en/users/integration-jetbrains/)
- [Zed Editor | Qwen Code Docs](https://qwenlm.github.io/qwen-code-docs/en/users/integration-zed/)

![](https://gw.alicdn.com/imgextra/i3/O1CN01rTE0X61tikAwLN7Zz_!!6000000005936-2-tps-2032-1386.png)

### Plan Mode: Rejected Plans Now Visible[](#plan-mode-rejected-plans-now-visible)

In Plan Mode, when AI’s proposal is rejected by you, the content doesn’t disappear. You can compare different proposals and choose the most suitable one.

**Use Cases:**

- Compare multiple proposals from AI and choose the best solution
- Review previous content after rejection without asking AI to regenerate
- More intuitive proposal comparison for more confident decisions

See PR [#2157](https://github.com/QwenLM/qwen-code/pull/2157) 

![](https://gw.alicdn.com/imgextra/i4/O1CN01rGEuoD1XpgdIQ8X2V_!!6000000002973-1-tps-860-584.gif)

### Support for .agents Directory (Preview)[](#support-for-agents-directory-preview)

Skill files can now be placed in project’s `.agents` directory, managed together with project code. Team members can use the same skill configuration after cloning the project.

**Use Cases:**

- Put project-related skills in `.agents` directory for version control with code
- Team members share skill configuration without manual setup one by one
- Different projects can have independent skill configurations without interference

See PR [#2202](https://github.com/QwenLM/qwen-code/pull/2202) 

![](https://gw.alicdn.com/imgextra/i3/O1CN01S3mZO01RMw4i66XNH_!!6000000002098-1-tps-1280-720.gif)

### Session Export with Metadata and Statistics (Preview)[](#session-export-with-metadata-and-statistics-preview)

When exporting sessions, metadata and statistics are now included: conversation time, Token consumption, message count, etc. Convenient for archiving and usage analysis.

**Use Cases:**

- Automatically record conversation time and Token consumption when exporting for easy review
- Analyze usage patterns statistically to understand your usage habits
- Archive important conversations with complete information

See PR [#2328](https://github.com/QwenLM/qwen-code/pull/2328) 

![](https://gw.alicdn.com/imgextra/i3/O1CN010xCLBN1txrFHqCjhG_!!6000000005969-2-tps-1264-589.png)

## 📊 Improvements[](#-improvements)

- **Shell Output No Longer Floods Screen**: Large output is automatically truncated, tool output is more concise, won’t slow down response due to lengthy output ([#2388](https://github.com/QwenLM/qwen-code/pull/2388) )
- **Slash Command Description Localization**: `/help` and other commands’ descriptions support multi-language display ([#2333](https://github.com/QwenLM/qwen-code/pull/2333) )

## 🔧 Important Fixes[](#-important-fixes)

PRVersionFixImpact[#2423](https://github.com/QwenLM/qwen-code/pull/2423) v0.12.5Fixed Windows non-ASCII output encoding issueChinese, Japanese and other non-English output no longer garbled on Windows[#2438](https://github.com/QwenLM/qwen-code/pull/2438) v0.12.6Improved max\_tokens handling with conservative defaultsAvoid errors from certain models due to excessive max\_tokens[#2024](https://github.com/QwenLM/qwen-code/pull/2024) v0.12.4Reject PDF files to prevent session corruptionOpening PDFs no longer causes session issues[#2389](https://github.com/QwenLM/qwen-code/pull/2389) v0.12.4Fixed interactive shell fast output lossCommand output no longer loses content[#2367](https://github.com/QwenLM/qwen-code/pull/2367) v0.12.4Fixed API retry errorsNo more mysterious API errors[#2280](https://github.com/QwenLM/qwen-code/pull/2280) v0.12.4Fixed Hooks JSON Schema type definitionNo more type errors when configuring Hooks

### Windows Platform Specific Fixes[](#windows-platform-specific-fixes)

PRFixImpact[#2423](https://github.com/QwenLM/qwen-code/pull/2423) Fixed non-ASCII output encoding issueChinese, Japanese and other non-English output displays correctly[#2286](https://github.com/QwenLM/qwen-code/pull/2286) Fixed extension installation failureInstalling extension via git clone no longer fails on Windows[#1904](https://github.com/QwenLM/qwen-code/pull/1904) Normalized Windows PATH environment variableMore stable environment variable handling during shell execution

### macOS Platform Specific Fixes[](#macos-platform-specific-fixes)

PRFixImpact[#2391](https://github.com/QwenLM/qwen-code/pull/2391) Fixed sandbox permission issueTerminal device access works properly in macOS sandbox environment

## 🎈 Other Improvements[](#-other-improvements)

- Added 7 new contributors: [@netbrah](https://github.com/netbrah) , [@chen893](https://github.com/chen893) , [@hs-ye](https://github.com/hs-ye) , [@drewd789](https://github.com/drewd789) , [@Sakuranda](https://github.com/Sakuranda) , [@kiri-chenchen](https://github.com/kiri-chenchen) , [@ShihaoShenDev](https://github.com/ShihaoShenDev)
- Added Docker sandbox runtime and Java usage documentation ([#1642](https://github.com/QwenLM/qwen-code/pull/1642) )
- Improved VS Code prompt cancellation and streaming race condition handling ([#2374](https://github.com/QwenLM/qwen-code/pull/2374) )

**How to Upgrade**:

- Stable version: `npm i @qwen-code/qwen-code@latest -g`
- Preview version: `npm i @qwen-code/qwen-code@v0.13.0-preview.1 -g`

If you have questions or suggestions, feel free to provide feedback on [GitHub Issues](https://github.com/QwenLM/qwen-code/issues) !

Last updated on March 31, 2026

[Qwen Code Weekly: Automated Workflows, Better Extension & MCP Management, VS Code Sidebar](https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-03-13/ "Qwen Code Weekly: Automated Workflows, Better Extension & MCP Management, VS Code Sidebar")[Qwen Code Weekly: AI Code Review, Ask Questions Without Losing Context, Custom Workflow Automation](https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-03-27/ "Qwen Code Weekly: AI Code Review, Ask Questions Without Losing Context, Custom Workflow Automation")