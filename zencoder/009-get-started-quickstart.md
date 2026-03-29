---
title: Quickstart - Zencoder Docs
url: https://docs.zencoder.ai/get-started/quickstart
source: crawler
fetched_at: 2026-01-23T09:28:00.865930226-03:00
rendered_js: false
word_count: 421
summary: This document provides comprehensive instructions for installing Zencoder across various platforms, setting up custom AI agents and Zen Rules, and navigating model selection and shortcuts.
tags:
    - zencoder-setup
    - ide-integration
    - ai-agents
    - zen-rules
    - installation-guide
    - keyboard-shortcuts
    - model-comparison
category: guide
---

## Install Zencoder

- Zenflow app
- Visual Studio Code
- JetBrains IDEs

<!--THE END-->

1. Visit [zencoder.ai](https://zencoder.ai) and click **Get Started**
2. Download and run the installer for your operating system
3. Launch Zenflow once installation finishes
4. Sign in or create account

[Read full documentation →](https://docs.zencoder.ai/zenflow/quickstart)

1. Open VS Code
2. Press `Cmd+Shift+X` (Mac) / `Ctrl+Shift+X` (Windows/Linux)
3. Search for “Zencoder”
4. Click **Install**
5. Sign in or create account

[Full installation details →](https://docs.zencoder.ai/get-started/introduction)

## First Steps

### Use Different Agents

## Quick Customization

### Create a Custom Agent (5 minutes)

1. Click three dots menu (⋮) → **Agents**
2. Click **Add custom agent**
3. Configure:
   
   - Name: “Code Reviewer”
   - Command: `/review`
   - Instructions: “Review for bugs and best practices”
   - Tools: Enable File Search, Full Text Search
4. Click **Save**

[Learn about custom agents →](https://docs.zencoder.ai/features/ai-agents)

### Create a Zen Rule (3 minutes)

1. In chat, type `@`
2. Select **Zen Rules**
3. Click **+ New rule…**
4. Add your coding standards:
   
   ```
   ---
   description: "API endpoint standards"
   globs: ["**/api/*.py"]
   ---
   
   # API Standards
   - Add input validation
   - Include error handling
   - Add logging
   ```

[Learn about Zen Rules →](https://docs.zencoder.ai/rules-context/zen-rules)

## Integrations

[Integrations guide →](https://docs.zencoder.ai/features/integrations-and-mcp)

## Common Workflows

## Keyboard Shortcuts

ActionMacWindows/LinuxOpen agent selector`Cmd+.``Ctrl+.`Send to chat`Cmd+L``Ctrl+L`Accept completion`Tab``Tab`

## Model Selection

Click the model selector in chat to choose:

- **Auto** (1×) - Best balance
- **Auto+** (2.5×) - Superior performance
- **Grok Code Fast 1** (0.25×) - Most cost-efficient
- **GPT-5.1-Codex-mini** (0.5×) - Cost-efficient code generation
- **Sonnet 4** (2×) - High quality
- **Gemini Pro 3.0** (2×) - Balanced capability
- **Opus 4.1** (10×) - High capability (Advanced+ plans)
- **Opus 4.5 Parallel Thinking** (5×) - Most capable reasoning (Advanced+ plans)

[Learn more about models →](https://docs.zencoder.ai/features/models)

1. Open your IDE (IntelliJ, PyCharm, WebStorm, etc.)
2. Go to **File &gt; Settings** (or **Preferences** on macOS)
3. Select **Plugins**
4. Search for “Zencoder”
5. Click **Install** and restart
6. Sign in or create account

[Full installation details →](https://docs.zencoder.ai/get-started/introduction)

## First Steps

### Use Different Agents

## Quick Customization

### Create a Custom Agent (5 minutes)

1. Click three dots menu (⋮) → **Agents**
2. Click **Add custom agent**
3. Configure:
   
   - Name: “Code Reviewer”
   - Command: `/review`
   - Instructions: “Review for bugs and best practices”
   - Tools: Enable File Search, Full Text Search
4. Click **Save**

[Learn about custom agents →](https://docs.zencoder.ai/features/ai-agents)

### Create a Zen Rule (3 minutes)

1. In chat, type `@`
2. Select **Zen Rules**
3. Click **+ New rule…**
4. Add your coding standards:
   
   ```
   ---
   description: "API endpoint standards"
   globs: ["**/api/*.py"]
   ---
   
   # API Standards
   - Add input validation
   - Include error handling
   - Add logging
   ```

[Learn about Zen Rules →](https://docs.zencoder.ai/rules-context/zen-rules)

## Integrations

[Integrations guide →](https://docs.zencoder.ai/features/integrations-and-mcp)

## Common Workflows

## Keyboard Shortcuts

ActionMacWindows/LinuxOpen agent selector`Cmd+.``Ctrl+.`Send to chat`Cmd+L``Ctrl+L`Accept completion`Tab``Tab`

## Model Selection

Click the model selector in chat to choose:

- **Auto** (1×) - Best balance
- **Auto+** (2.5×) - Superior performance
- **Grok Code Fast 1** (0.25×) - Most cost-efficient
- **GPT-5.1-Codex-mini** (0.5×) - Cost-efficient code generation
- **Sonnet 4** (2×) - High quality
- **Gemini Pro 3.0** (2×) - Balanced capability
- **Opus 4.1** (10×) - High capability (Advanced+ plans)
- **Opus 4.5 Parallel Thinking** (5×) - Most capable reasoning (Advanced+ plans)

[Learn more about models →](https://docs.zencoder.ai/features/models)