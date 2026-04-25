---
title: Zed Editor
url: https://qwenlm.github.io/qwen-code-docs/en/users/integration-zed
source: github_pages
fetched_at: 2026-04-09T09:03:49.128214991-03:00
rendered_js: true
word_count: 225
summary: This document details how to natively integrate and use Qwen Code AI coding assistants within the Zed Editor using the Agent Client Protocol (ACP). It provides step-by-step instructions for both recommended registry installation and manual configuration, along with troubleshooting tips.
tags:
    - zed-editor
    - ai-assistant
    - qwen-code
    - agent-client-protocol
    - installation-guide
    - ide-integration
category: guide
---

> Zed Editor provides native support for AI coding assistants through the Agent Client Protocol (ACP). This integration allows you to use Qwen Code directly within Zed’s interface with real-time code suggestions.

![Zed Editor Overview](https://img.alicdn.com/imgextra/i1/O1CN01aAhU311GwEoNh27FP_!!6000000000686-2-tps-3024-1898.png)

### Features[](#features)

- **Native agent experience**: Integrated AI assistant panel within Zed’s interface
- **Agent Client Protocol**: Full support for ACP enabling advanced IDE interactions
- **File management**: @-mention files to add them to the conversation context
- **Conversation history**: Access to past conversations within Zed

### Requirements[](#requirements)

- Zed Editor (latest version recommended)
- Qwen Code CLI installed

### Installation[](#installation)

#### Install from ACP Registry (Recommend)[](#install-from-acp-registry-recommend)

1. Install Qwen Code CLI:

```
npm install -g @qwen-code/qwen-code
```

2. Download and install [Zed Editor](https://zed.dev/)
3. In Zed, click the **settings button** in the top right corner, select **“Add agent”**, choose **“Install from Registry”**, find **Qwen Code**, then click **Install**.
   
   ![ACP Registry](https://img.alicdn.com/imgextra/i4/O1CN0186ybL61EeG35fHFjy_!!6000000000376-2-tps-3056-1705.png)
   
   ![Qwen Code ACP Installed](https://img.alicdn.com/imgextra/i1/O1CN01OXHhoR1J8irAvjs8F_!!6000000000984-2-tps-1247-703.png)

#### Manual Install[](#manual-install)

1. Install Qwen Code CLI:

```
npm install -g @qwen-code/qwen-code
```

2. Download and install [Zed Editor](https://zed.dev/)
3. In Zed, click the **settings button** in the top right corner, select **“Add agent”**, choose **“Create a custom agent”**, and add the following configuration:

```
"Qwen Code": {
  "type": "custom",
  "command": "qwen",
  "args": ["--acp"],
  "env": {}
}
```

![Qwen Code Integration](https://img.alicdn.com/imgextra/i1/O1CN013s61L91dSE1J7MTgO_!!6000000003734-2-tps-2592-1234.png)

## Troubleshooting[](#troubleshooting)

### Agent not appearing[](#agent-not-appearing)

- Run `qwen --version` in terminal to verify installation
- Check that the JSON configuration is valid
- Restart Zed Editor

### Qwen Code not responding[](#qwen-code-not-responding)

- Check your internet connection
- Verify CLI works by running `qwen` in terminal
- [File an issue on GitHub](https://github.com/qwenlm/qwen-code/issues)  if the problem persists

Last updated on March 31, 2026

[Visual Studio Code](https://qwenlm.github.io/qwen-code-docs/en/users/integration-vscode/ "Visual Studio Code")[JetBrains IDEs](https://qwenlm.github.io/qwen-code-docs/en/users/integration-jetbrains/ "JetBrains IDEs")