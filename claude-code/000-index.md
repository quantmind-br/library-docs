---
description: Auto-generated documentation index
generated: 2026-04-26T11:14:16.975196+00:00
source: https://code.claude.com/docs/llms.txt
total_docs: 117
categories: 7
---

# Claude Code Documentation Index

> Organized for AI agent consumption. Files numbered following a logical learning sequence.

## Summary

| Property | Value |
|----------|-------|
| Source | https://code.claude.com/docs/llms.txt |
| Generated | 2026-04-26T11:14:16.975196+00:00 |
| Total Documents | 117 |
| Categories | Quick Start & Installation, Tutorials & Guides, Concepts & Fundamentals, Configuration, API Reference, Troubleshooting, Changelog & Releases |

---

## Document Index

### 2. Quick Start & Installation (001–004)
*Installation, setup, and first steps*

| # | File | Title | Summary | Tags |
|---|------|-------|---------|------|
| 001 | `001-agent-sdk-quickstart.md` | Quickstart | This document provides a foundational guide for developers to install and use the Claude Agent SDK to build autonomous a... | agent-sdk, python, typescript, code-remediation, automation, api-integration |
| 002 | `002-desktop-quickstart.md` | Get started with the desktop app | This document provides instructions for installing the Claude Code desktop application and initiating your first coding ... | claude-code, desktop-app, installation-guide, coding-assistant, getting-started, software-development |
| 003 | `003-quickstart.md` | Quickstart | This document provides an interactive setup guide for installing Claude Code across various platforms, including termina... | claude-code, installation, quickstart, developer-tools, cli, ide-plugins |
| 004 | `004-web-quickstart.md` | Get started with Claude Code on the web | This document provides an overview of Claude Code on the web, explaining how to run coding tasks in browser-based cloud ... | claude-code, cloud-development, github-integration, web-interface, remote-development, environment-configuration |

### 3. Tutorials & Guides (005–072)
*Step-by-step guides and how-to documentation*

| # | File | Title | Summary | Tags |
|---|------|-------|---------|------|
| 005 | `005-discover-plugins.md` | Discover and install prebuilt plugins through marketplaces | This document explains how to discover, manage, and install plugins for Claude Code using marketplace catalogs, includin... | claude-code, plugin-management, marketplaces, code-intelligence, mcp-servers, developer-tools |
| 006 | `006-agent-sdk-overview.md` | Agent SDK overview | This document provides an overview and installation guide for the Claude Agent SDK, enabling developers to build autonom... | claude-agent-sdk, ai-agents, python, typescript, autonomous-agents, software-development |
| 007 | `007-features-overview.md` | Extend Claude Code | This guide provides an overview of the extension features available in Claude Code, including skills, subagents, hooks, ... | claude-code, extensibility, developer-tools, agentic-workflow, automation, configuration |
| 008 | `008-admin-setup.md` | Set up Claude Code for your organization | This document provides a decision framework for administrators to deploy Claude Code, detailing how to manage organizati... | claude-code, enterprise-deployment, policy-management, api-integration, admin-guide, security-configuration |
| 009 | `009-agent-sdk-cost-tracking.md` | Track cost and usage | This guide explains how to track token usage, estimate costs, and monitor per-step performance using the Claude Agent SD... | token-usage, cost-tracking, sdk-development, performance-monitoring, claude-agent-sdk |
| 010 | `010-agent-sdk-custom-tools.md` | Give Claude custom tools | This guide explains how to define and register custom tools using the Claude Agent SDK and in-process MCP servers, enabl... | claude-agent-sdk, mcp-server, custom-tools, api-integration, python, typescript |
| 011 | `011-agent-sdk-file-checkpointing.md` | Rewind file changes with checkpointing | This document explains how to utilize file checkpointing in the Claude Agent SDK to track file modifications and revert ... | file-checkpointing, sdk-guide, version-control, file-management, agent-development, state-recovery |
| 012 | `012-agent-sdk-hooks.md` | Intercept and control agent behavior with hooks | This document explains how to use hooks to intercept, monitor, and control agent behavior at various stages of the execu... | agent-sdk, event-hooks, tool-control, security-compliance, callback-functions, event-driven-architecture |
| 013 | `013-agent-sdk-hosting.md` | Hosting the Agent SDK | This guide outlines the architectural requirements, infrastructure needs, and deployment patterns for hosting Claude Age... | agent-sdk, production-deployment, sandboxing, containerization, infrastructure, system-requirements |
| 014 | `014-agent-sdk-mcp.md` | Connect to external tools with MCP | This document explains how to configure and integrate Model Context Protocol (MCP) servers with AI agents to access exte... | mcp, ai-agents, tool-integration, sdk-configuration, security-permissions, server-transport |
| 015 | `015-agent-sdk-modifying-system-prompts.md` | Modifying system prompts | This document explains how to customize the behavior of Claude using the Agent SDK through three primary methods: CLAUDE... | claude-sdk, system-prompts, configuration, agent-behavior, claude-md, customization |
| 016 | `016-agent-sdk-observability.md` | Observability with OpenTelemetry | This guide explains how to configure the Agent SDK to export telemetry data, including traces, metrics, and logs, to obs... | opentelemetry, observability, agent-sdk, telemetry-export, monitoring |
| 017 | `017-agent-sdk-plugins.md` | Plugins in the SDK | This document explains how to extend Claude Code by loading and using local plugins via the Agent SDK to add custom skil... | claude-code, agent-sdk, plugins, skills, mcp-servers, custom-commands |
| 018 | `018-agent-sdk-secure-deployment.md` | Securely deploying AI agents | This document outlines best practices and technical strategies for securely deploying AI agents, focusing on isolation t... | ai-security, agent-deployment, threat-modeling, sandbox-isolation, least-privilege, network-security |
| 019 | `019-agent-sdk-sessions.md` | Work with sessions | This document explains how to manage conversation history using sessions, detailing methods for continuing, resuming, an... | conversation-history, session-management, agent-sdk, persistence, context-tracking |
| 020 | `020-agent-sdk-skills.md` | Agent Skills in the SDK | This document explains how to configure and use Agent Skills within the Claude Agent SDK to provide Claude with speciali... | agent-sdk, claude-skills, filesystem-discovery, tool-configuration, sdk-integration |
| 021 | `021-agent-sdk-slash-commands.md` | Slash Commands in the SDK | This document explains how to interact with and extend Claude Code sessions using slash commands within the Agent SDK, i... | slash-commands, claude-sdk, agent-automation, context-management, custom-skills |
| 022 | `022-agent-sdk-streaming-output.md` | Stream responses in real-time | This document explains how to enable and process real-time streaming of text and tool calls using the Agent SDK by confi... | sdk-streaming, real-time-responses, partial-messages, event-handling, content-block-delta |
| 023 | `023-agent-sdk-streaming-vs-single-mode.md` | Streaming Input | This guide details the two input modes available in the Claude Agent SDK, comparing the persistent, feature-rich streami... | claude-agent-sdk, streaming-input, single-message-input, agent-development, session-management, api-guide |
| 024 | `024-agent-sdk-structured-outputs.md` | Get structured output from agents | This document explains how to configure agent workflows to return validated, type-safe JSON data using JSON Schema, Zod,... | structured-output, json-schema, type-safety, zod, pydantic, agent-workflows |
| 025 | `025-agent-sdk-subagents.md` | Subagents in the SDK | This guide explains how to define and utilize subagents within the Claude Agent SDK to isolate context, enable parallel ... | claude-sdk, subagents, agent-orchestration, context-isolation, parallel-processing, sdk-configuration |
| 026 | `026-agent-sdk-todo-tracking.md` | Todo Lists | This document explains how to utilize the Claude Agent SDK's built-in todo functionality to track, monitor, and display ... | claude-agent-sdk, task-management, todo-tracking, workflow-automation, sdk-integration |
| 027 | `027-agent-sdk-tool-search.md` | Scale to many tools with tool search | This document explains how to implement and configure tool search in the Claude SDK, allowing agents to dynamically disc... | tool-search, agent-development, context-optimization, mcp-servers, sdk-configuration, ai-agents |
| 028 | `028-agent-sdk-user-input.md` | Handle approvals and user input | This guide explains how to implement the canUseTool callback in the Claude SDK to intercept and handle requests for user... | claude-sdk, user-input, tool-approval, callback-handlers, agent-development, permission-management |
| 029 | `029-agent-teams.md` | Orchestrate teams of Claude Code sessions | This document explains how to set up and coordinate multiple Claude Code instances as an agent team for collaborative ta... | agent-teams, multi-agent-orchestration, parallel-processing, workflow-automation, claude-code, experimental-features |
| 030 | `030-amazon-bedrock.md` | Claude Code on Amazon Bedrock | This document provides instructions for configuring Claude Code to work with Amazon Bedrock, covering prerequisites, AWS... | amazon-bedrock, claude-code, aws-configuration, iam-permissions, model-setup |
| 031 | `031-analytics.md` | Track team usage with analytics | This document explains how to access and configure analytics dashboards for Claude Code to track usage patterns, develop... | analytics, usage-metrics, github-integration, contribution-tracking, developer-productivity, dashboard |
| 032 | `032-authentication.md` | Authentication | This document provides instructions for authenticating with Claude Code using various methods, including individual acco... | authentication, claude-code, login, cloud-providers, credential-management, sso |
| 033 | `033-best-practices.md` | Best Practices for Claude Code | This guide outlines effective patterns and best practices for working with the Claude Code agentic environment, focusing... | claude-code, agentic-workflow, prompt-engineering, context-management, developer-productivity |
| 034 | `034-channels.md` | Push events into a running session with channels | This document explains how to configure and use channels in Claude Code to push external messages, alerts, and webhooks ... | claude-code, mcp-servers, channels, automation, event-driven, plugins |
| 035 | `035-chrome.md` | Use Claude Code with Chrome (beta) | This document explains how to integrate Claude Code with the Chrome browser to automate web tasks, perform live debuggin... | browser-automation, claude-code, web-testing, cli-tools, workflow-automation, debugging |
| 036 | `036-claude-code-on-the-web.md` | Use Claude Code on the web | This document provides an overview of using Claude Code in cloud-based environments, covering setup, GitHub authenticati... | claude-code, cloud-environment, github-integration, session-management, setup-configuration |
| 037 | `037-code-review.md` | Code Review | This document explains how to set up and use the Claude automated code review service, which utilizes multi-agent analys... | automated-code-review, github-integration, pull-request-analysis, static-analysis, ci-cd-workflow, code-quality |
| 038 | `038-common-workflows.md` | Common workflows | This document provides practical workflows and guidance for using Claude Code to perform common development tasks such a... | claude-code, workflow-automation, code-refactoring, debugging-guide, ai-subagents, development-productivity |
| 039 | `039-computer-use.md` | Let Claude use your computer from the CLI | This guide explains how to configure and use the computer-use feature in the Claude Code CLI, allowing Claude to interac... | claude-code, computer-use, cli-automation, macos-gui, ui-testing, mcp-server |
| 040 | `040-costs.md` | Manage costs effectively | This document provides guidance on monitoring, managing, and optimizing token consumption and costs associated with usin... | cost-management, token-usage, billing, rate-limits, context-optimization, claude-code |
| 041 | `041-debug-your-config.md` | Debug your configuration | This guide provides instructions for diagnosing and troubleshooting issues where Claude Code configurations, such as CLA... | configuration, debugging, troubleshooting, cli-commands, mcp-servers, settings-management |
| 042 | `042-desktop-scheduled-tasks.md` | Schedule recurring tasks in Claude Code Desktop | This document explains how to set up and manage local recurring tasks within Claude Code Desktop to automate workflows l... | claude-code, automation, desktop-app, scheduled-tasks, workflow-optimization, routines |
| 043 | `043-desktop.md` | Use Claude Code Desktop | This document provides a comprehensive guide to using the Claude Code Desktop application, covering installation, sessio... | claude-desktop, software-development, agentic-workflow, permission-modes, session-management, ide-integration |
| 044 | `044-devcontainer.md` | Development containers | This document provides an overview of the Claude Code development container, explaining how to set up, configure, and se... | development-containers, claude-code, security-isolation, vs-code, environment-setup, network-firewall |
| 045 | `045-fast-mode.md` | Speed up responses with fast mode | This document explains how to use fast mode in Claude Code to optimize Opus 4.6 for lower latency, including configurati... | claude-code, fast-mode, opus-4.6, latency-optimization, configuration, cost-management |
| 046 | `046-github-actions.md` | Claude Code GitHub Actions | This document provides a guide for integrating Claude Code into GitHub workflows using GitHub Actions to automate code r... | github-actions, automation, workflow-integration, claude-code, devops, ci-cd |
| 047 | `047-gitlab-ci-cd.md` | Claude Code GitLab CI/CD | This document provides a guide for integrating Claude Code into GitLab CI/CD pipelines to automate development tasks suc... | gitlab, ci-cd, claude-code, automation, devops, enterprise-ai |
| 048 | `048-google-vertex-ai.md` | Claude Code on Google Vertex AI | This guide provides instructions for configuring and authenticating Claude Code to run on Google Cloud Platform using Ve... | claude-code, google-cloud-platform, vertex-ai, setup-guide, cloud-configuration |
| 049 | `049-headless.md` | Run Claude Code programmatically | This document explains how to use the Claude Code CLI and Agent SDK to execute tasks programmatically, including options... | cli, automation, agent-sdk, scripting, ci-cd, structured-output |
| 050 | `050-hooks-guide.md` | Automate workflows with hooks | This document explains how to configure and use lifecycle hooks in Claude Code to automatically execute shell commands b... | automation, cli-tools, workflow-optimization, shell-scripts, configuration, development-tools |
| 051 | `051-jetbrains.md` | JetBrains IDEs | This document provides instructions for installing, configuring, and using the Claude Code plugin within JetBrains IDEs ... | jetbrains, ide-integration, plugin-setup, claude-code, developer-tools, remote-development |
| 052 | `052-mcp.md` | Connect Claude Code to tools via MCP | This document describes how to integrate external tools, databases, and APIs with Claude Code using the Model Context Pr... | mcp, claude-code, tool-integration, api-registry, model-context-protocol |
| 053 | `053-memory.md` | How Claude remembers your project | This document explains how to maintain persistent project context and agent knowledge using CLAUDE.md instruction files ... | claude-code, persistent-memory, configuration-management, project-setup, context-window, developer-productivity |
| 054 | `054-microsoft-foundry.md` | Claude Code on Microsoft Foundry | This document provides instructions for setting up and configuring Claude Code to run on Microsoft Foundry, including re... | claude-code, microsoft-foundry, azure, configuration, deployment, authentication |
| 055 | `055-permission-modes.md` | Choose a permission mode | This document explains how to configure and use permission modes to control the frequency and scope of interaction promp... | permission-management, cli-configuration, security-settings, auto-approval, user-controls, workflow-automation |
| 056 | `056-platforms.md` | Platforms and integrations | This document provides an overview of the various platforms, IDE integrations, and connectivity options available for Cl... | claude-code, development-environment, ide-integration, cli-tools, automation, workflow-optimization |
| 057 | `057-plugin-dependencies.md` | Constrain plugin dependency versions | This guide explains how to define and constrain version dependencies for Claude Code plugins to ensure stability against... | plugin-development, dependency-management, version-constraints, semver, claude-code, marketplace |
| 058 | `058-plugin-marketplaces.md` | Create and distribute a plugin marketplace | This guide explains how to create, host, and manage a plugin marketplace to distribute Claude Code extensions, including... | plugin-development, marketplace-distribution, claude-code, plugin-manifest, git-hosting, automation |
| 059 | `059-plugins.md` | Create plugins | This guide explains how to develop, structure, and test custom plugins for Claude Code to extend functionality through s... | claude-code, plugin-development, custom-skills, extensibility, software-configuration |
| 060 | `060-remote-control.md` | Continue local sessions from any device with Remote Control | This document explains how to set up and use Claude Code Remote Control to access and manage local coding sessions from ... | remote-control, claude-code, session-management, cross-device, local-development, server-configuration |
| 061 | `061-routines.md` | Automate work with routines | This document explains how to configure and manage automated routines in Claude Code, which allow tasks to run autonomou... | automation, claude-code, cloud-computing, routines, workflow-integration, mcp-connectors |
| 062 | `062-scheduled-tasks.md` | Run prompts on a schedule | This document explains how to use the /loop command in Claude Code to execute prompts on a repeating schedule for tasks ... | claude-code, task-scheduling, automation, cli-tools, cron, workflow-optimization |
| 063 | `063-setup.md` | Advanced setup | This document provides system requirements, installation methods for various platforms, and initial configuration steps ... | installation, setup, system-requirements, claude-code, configuration, authentication |
| 064 | `064-skills.md` | Extend Claude with skills | This document explains how to extend Claude Code's functionality by creating and managing custom skills, which are struc... | claude-code, automation, agent-skills, custom-commands, developer-tools, workflow-optimization |
| 065 | `065-slack.md` | Claude Code in Slack | This document explains how to set up and use Claude Code within Slack to delegate coding tasks, manage repositories, and... | claude-code, slack-integration, development-workflow, collaboration, automation, repository-management |
| 066 | `066-statusline.md` | Customize your status line | This document explains how to configure and customize the persistent status line in Claude Code by writing shell scripts... | claude-code, configuration, status-bar, automation, shell-scripting, terminal |
| 067 | `067-sub-agents.md` | Create custom subagents | This document explains how to create and manage specialized subagents in Claude Code to handle specific tasks, preserve ... | claude-code, subagents, ai-delegation, context-management, workflow-automation, agent-configuration |
| 068 | `068-third-party-integrations.md` | Enterprise deployment overview | This document provides an overview of enterprise deployment options for Claude Code, highlighting the differences betwee... | enterprise-deployment, claude-teams, claude-enterprise, deployment-options, subscription-management |
| 069 | `069-ultraplan.md` | Plan in the cloud with ultraplan | Ultraplan is a feature for Claude Code that allows users to offload task planning from their local CLI to a web-based in... | claude-code, ultraplan, cloud-planning, cli-tools, workflow-automation, remote-execution |
| 070 | `070-ultrareview.md` | Find bugs with ultrareview | This document explains the ultrareview feature in Claude Code, which utilizes a multi-agent cloud-based sandbox to perfo... | code-review, claude-code, bug-detection, cli-tools, software-quality, remote-sandbox |
| 071 | `071-voice-dictation.md` | Voice dictation | This document explains how to use and configure voice dictation in the Claude Code CLI, including mode switching, langua... | voice-dictation, cli-tools, speech-to-text, configuration, keyboard-shortcuts, claude-code |
| 072 | `072-vs-code.md` | Use Claude Code in VS Code | This guide explains how to install, configure, and use the Claude Code extension for VS Code to access AI-powered coding... | claude-code, vs-code, extension, ai-coding, developer-tools, editor-integration |

### 4. Concepts & Fundamentals (073–080)
*Core concepts and architectural understanding*

| # | File | Title | Summary | Tags |
|---|------|-------|---------|------|
| 073 | `073-agent-sdk-agent-loop.md` | How the agent loop works | This document explains the architecture and lifecycle of the agent loop within the Claude Agent SDK, detailing how promp... | agent-sdk, agentic-loop, message-lifecycle, tool-execution, sdk-architecture |
| 074 | `074-checkpointing.md` | Checkpointing | This document explains how the checkpointing feature automatically tracks file edits and conversation states, allowing u... | checkpointing, session-management, version-recovery, context-window, undo-operations, code-workflow |
| 075 | `075-context-window.md` | Explore the context window | This document explains the lifecycle of Claude Code's context window by simulating how system prompts, files, memory, an... | context-window, token-usage, claude-code, system-prompts, mcp-tools, hooks |
| 076 | `076-data-usage.md` | Data usage | This document outlines Anthropic's data usage, training policies, retention practices, and security measures for Claude ... | data-privacy, security-compliance, model-training, data-retention, encryption, claude-code |
| 077 | `077-how-claude-code-works.md` | How Claude Code works | This document outlines the architecture of Claude Code, explaining its agentic loop, core toolset, and the operational c... | agentic-loop, claude-code, terminal-assistant, automation, ai-tools, architecture-overview |
| 078 | `078-sandboxing.md` | Sandboxing | This document explains how Claude Code uses OS-level sandboxing to provide secure, isolated environments for bash comman... | sandboxing, security-isolation, bash-execution, filesystem-security, network-isolation, autonomous-agents |
| 079 | `079-security.md` | Security | This document outlines the security architecture, built-in protection mechanisms, and best practices for using Claude Co... | security-best-practices, permission-management, threat-mitigation, data-privacy, mcp-security, cloud-execution |
| 080 | `080-zero-data-retention.md` | Zero data retention | This document outlines the Zero Data Retention (ZDR) policy for Claude Code on Claude for Enterprise, detailing its scop... | zero-data-retention, claude-code, enterprise-security, data-privacy, compliance, policy-management |

### 5. Configuration (081–096)
*Settings and customization options*

| # | File | Title | Summary | Tags |
|---|------|-------|---------|------|
| 081 | `081-overview.md` | Claude Code overview | This document provides an installation and configuration guide for Claude Code, an agentic coding tool that integrates w... | claude-code, agentic-coding, installation-guide, cli-tools, ide-integration |
| 082 | `082-agent-sdk-claude-code-features.md` | Use Claude Code features in the SDK | This document explains how to configure filesystem-based settings and project instructions for agents using the Claude S... | agent-sdk, claude-code, filesystem-settings, project-configuration, claude-md, sdk-configuration |
| 083 | `083-agent-sdk-permissions.md` | Configure permissions | This document explains how to configure tool permissions in the Claude Agent SDK, detailing the evaluation hierarchy of ... | agent-sdk, permission-control, tool-access, security-configuration, access-management, development-guide |
| 084 | `084-auto-mode-config.md` | Configure auto mode | This document provides configuration instructions for the auto-mode classifier, enabling users to define trusted infrast... | configuration, auto-mode, security-policy, infrastructure-trust, permission-management, claude-code |
| 085 | `085-fullscreen.md` | Fullscreen rendering | This document explains how to enable and use the fullscreen rendering mode in the Claude Code CLI, which optimizes termi... | claude-code, terminal-interface, rendering-mode, cli-configuration, user-experience, mouse-support |
| 086 | `086-github-enterprise-server.md` | Claude Code with GitHub Enterprise Server | This document provides instructions for administrators to integrate Claude Code with self-hosted GitHub Enterprise Serve... | github-enterprise, claude-code, admin-setup, integration, web-sessions, code-review |
| 087 | `087-keybindings.md` | Customize keyboard shortcuts | This document explains how to customize keyboard shortcuts in Claude Code by defining custom keybindings within a config... | claude-code, keyboard-shortcuts, configuration, keybindings, user-interface, cli-tools |
| 088 | `088-llm-gateway.md` | LLM gateway configuration | This document provides technical instructions for configuring Claude Code to connect with LLM gateway services, detailin... | llm-gateway, proxy-configuration, api-authentication, litellm, model-routing, environment-variables |
| 089 | `089-model-config.md` | Model configuration | This document explains how to configure and manage model selection in Claude Code, including the use of model aliases, e... | claude-code, model-configuration, model-aliases, enterprise-settings, environment-variables, api-integration |
| 090 | `090-monitoring-usage.md` | Monitoring | This document provides instructions on how to enable and configure OpenTelemetry for tracking usage and performance metr... | opentelemetry, monitoring, telemetry-configuration, claude-code, otlp, system-administration |
| 091 | `091-network-config.md` | Enterprise network configuration | This document provides instructions for configuring Claude Code in enterprise network environments, including support fo... | enterprise-network, proxy-configuration, tls-authentication, certificate-authority, mtls, network-security |
| 092 | `092-output-styles.md` | Output styles | This document explains how to configure and customize output styles in Claude Code to modify the assistant's persona, to... | claude-code, output-styles, system-prompt, configuration, personalization, customization |
| 093 | `093-permissions.md` | Configure permissions | This document explains how to configure fine-grained permissions and security modes in Claude Code to control agent acce... | security-configuration, permission-management, access-control, claude-code, shell-security, policy-enforcement |
| 094 | `094-server-managed-settings.md` | Configure server-managed settings | This document explains how administrators can centrally configure Claude Code settings via the web-based admin console f... | claude-code, server-managed-settings, administration, configuration, access-control, centralized-management |
| 095 | `095-settings.md` | Claude Code settings | This document explains the hierarchical configuration system for Claude Code, detailing how settings are applied across ... | configuration, claude-code, settings-management, scope-precedence, system-administration, deployment |
| 096 | `096-terminal-config.md` | Configure your terminal for Claude Code | This guide provides instructions for configuring various terminal emulators and environment tools to ensure optimal func... | terminal-configuration, claude-code, command-line-interface, keyboard-shortcuts, terminal-emulators, tmux |

### 9. API Reference (097–110)
*API documentation and technical references*

| # | File | Title | Summary | Tags |
|---|------|-------|---------|------|
| 097 | `097-agent-sdk-python.md` | Agent SDK reference - Python | This document provides a technical reference for the Python Agent SDK, outlining how to interact with Claude Code using ... | python-sdk, api-reference, agent-development, mcp-tools, claude-code |
| 098 | `098-agent-sdk-typescript-v2-preview.md` | TypeScript SDK V2 interface (preview) | Introduces the V2 TypeScript Agent SDK, which simplifies multi-turn conversations by replacing async generators with dis... | typescript, sdk, claude-agent, api-interface, multi-turn, session-management |
| 099 | `099-agent-sdk-typescript.md` | Agent SDK reference - TypeScript | This document provides the API reference for the TypeScript Agent SDK, detailing functions for interacting with Claude, ... | typescript, sdk-reference, agent-sdk, mcp-tools, api-documentation, claude-code |
| 100 | `100-channels-reference.md` | Channels reference | This reference provides instructions on building custom MCP-based channel servers to push external events, such as webho... | mcp-server, claude-code, webhook-integration, event-driven-architecture, node-js, stdio-transport |
| 101 | `101-claude-directory.md` | Explore the .claude directory | This document describes the structure, purpose, and configuration files used by Claude Code to manage project-specific s... | configuration, project-setup, mcp, workflow-automation, claude-code |
| 102 | `102-cli-reference.md` | CLI reference | This document provides a comprehensive reference for the Claude Code command-line interface, detailing available command... | claude-code, cli-reference, command-line, developer-tools, authentication, session-management |
| 103 | `103-commands.md` | Commands | This document provides a comprehensive reference guide to the built-in commands and bundled skills available for interac... | cli-commands, claude-code, terminal-tooling, developer-productivity, command-reference |
| 104 | `104-env-vars.md` | Environment variables | This document provides a comprehensive reference for the environment variables used to configure and control the behavio... | environment-variables, configuration, claude-code, api-settings, authentication, proxy-settings |
| 105 | `105-errors.md` | Error reference | This document provides a comprehensive lookup table for common runtime error messages encountered in Claude Code, offeri... | error-handling, troubleshooting, claude-code, runtime-errors, cli-reference, api-errors |
| 106 | `106-hooks.md` | Hooks reference | This document provides a technical reference for Claude Code hooks, detailing event lifecycles, configuration schemas, a... | claude-code, automation-hooks, event-driven-architecture, configuration-schema, lifecycle-events, agentic-workflow |
| 107 | `107-interactive-mode.md` | Interactive mode | This document provides a comprehensive reference for the keyboard shortcuts, input controls, and terminal navigation com... | keyboard-shortcuts, terminal-commands, claude-code, user-interface, navigation, configuration |
| 108 | `108-legal-and-compliance.md` | Legal and compliance | This document outlines the legal, compliance, and security requirements for using Claude Code, including licensing agree... | legal-agreements, compliance, security-policy, authentication, baa, usage-policy |
| 109 | `109-plugins-reference.md` | Plugins reference | This document serves as a technical reference for the Claude Code plugin system, outlining the specifications for creati... | plugin-system, technical-reference, cli-commands, event-hooks, subagents, schema-definition |
| 110 | `110-tools-reference.md` | Tools reference | This document provides a comprehensive reference for the built-in tools available to Claude Code, detailing their functi... | claude-code, tool-reference, automation, permissions-management, mcp-integration |

### 13. Troubleshooting (111–111)
*Problem solving and FAQ*

| # | File | Title | Summary | Tags |
|---|------|-------|---------|------|
| 111 | `111-troubleshooting.md` | Troubleshooting | This document provides a comprehensive troubleshooting guide for resolving common installation and configuration errors ... | troubleshooting, installation-guide, cli-tools, path-configuration, network-connectivity, error-resolution |

### 15. Changelog & Releases (112–117)
*Version history and release notes*

| # | File | Title | Summary | Tags |
|---|------|-------|---------|------|
| 112 | `112-whats-new-2026-w15.md` | Week 15 · April 6–10, 2026 | This document provides an overview of the April 2026 feature releases for Claude Code, introducing tools for cloud plann... | claude-code, developer-tools, automation, cli-commands, cloud-planning, release-notes |
| 113 | `113-whats-new-2026-w14.md` | Week 14 · March 30 – April 3, 2026 | This document outlines the software updates for Claude Code versions 2.1.86 through 2.1.91, introducing features like CL... | cli, mcp, computer-use, terminal-tools, software-release, plugin-development |
| 114 | `114-whats-new-2026-w13.md` | Week 13 · March 23–27, 2026 | This document provides an overview of new features and improvements released in Claude Code versions 2.1.83 through 2.1.... | release-notes, claude-code, automation, computer-use, cli-tools, productivity-features |
| 115 | `115-release-notes-overview.md` | What's new | This document serves as a weekly digest archive for Claude Code, highlighting new features, tool updates, and system imp... | release-notes, weekly-digest, claude-code, feature-updates, product-changelog |
| 116 | `116-changelog.md` | Changelog | This document provides the release notes for Claude Code, detailing recent feature additions, improvements, configuratio... | changelog, release-notes, claude-code, software-updates, version-history |
| 117 | `117-agent-sdk-migration-guide.md` | Migrate to Claude Agent SDK | This document provides instructions for migrating from the deprecated Claude Code SDK to the Claude Agent SDK, including... | migration-guide, sdk-update, claude-agent-sdk, typescript, python, breaking-changes |

---

## Quick Search

| Topic | Files |
|-------|-------|
| Quickstart | 001–004 |
| Agent SDK | 001, 006–028, 073, 097–099 |
| Configuration | 008, 082–096 |
| API Reference | 097–110 |
| Troubleshooting | 111 |
| Changelog | 112–117 |

## Learning Path

- **Foundation** — files 001–004 (intro, quickstart)
- **Core** — files 005–028, 073–096 (concepts, configuration)
- **Practice** — files 029–072 (tutorials, features)
- **Reference** — files 097–117 (API, changelog)

*Auto-generated. Files numbered sequentially following a content-driven learning progression.*