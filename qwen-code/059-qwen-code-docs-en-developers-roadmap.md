---
title: Qwen Code RoadMap
url: https://qwenlm.github.io/qwen-code-docs/en/developers/roadmap
source: github_pages
fetched_at: 2026-04-09T09:04:32.063995835-03:00
rendered_js: true
word_count: 413
summary: This document provides a comprehensive, phased overview of Claude Code's evolving product capabilities, detailing completed features, planned enhancements, and core functional areas from user experience to administrative tools.
tags:
    - product-roadmap
    - feature-tracking
    - ai-tooling
    - development-lifecycle
    - qwen-code
    - capability-matrix
category: reference
---

> **Objective**: Catch up with Claude Code’s product functionality, continuously refine details, and enhance user experience.

CategoryPhase 1Phase 2User Experience✅ Terminal UI  
✅ Support OpenAI Protocol  
✅ Settings  
✅ OAuth  
✅ Cache Control  
✅ Memory  
✅ Compress  
✅ ThemeBetter UI  
OnBoarding  
LogView  
✅ Session  
Permission  
🔄 Cross-platform Compatibility  
✅ Coding Plan  
✅ Anthropic Provider  
✅ Multimodal Input  
✅ Unified WebUICoding Workflow✅ Slash Commands  
✅ MCP  
✅ PlanMode  
✅ TodoWrite  
✅ SubAgent  
✅ Multi Model  
✅ Chat Management  
✅ Tools (WebFetch, Bash, TextSearch, FileReadFile, EditFile)🔄 Hooks  
✅ Skill  
✅ Headless Mode  
✅ Tools (WebSearch)  
✅ LSP Support  
✅ Concurrent RunnerBuilding Open Capabilities✅ Custom Commands✅ QwenCode SDK  
✅ Extension SystemIntegrating Community Ecosystem✅ VSCode Plugin  
✅ ACP/Zed  
✅ GHAAdministrative Capabilities✅ Stats  
✅ FeedbackCosts  
Dashboard  
✅ User Feedback Dialog

> For more details, please see the list below.

## Features[](#features)

#### Completed Features[](#completed-features)

FeatureVersionDescriptionCategoryPhase**Coding Plan**`V0.10.0`Alibaba Cloud Coding Plan authentication & modelsUser Experience2Unified WebUI`V0.9.0`Shared WebUI component library for VSCode/CLIUser Experience2Export Chat`V0.8.0`Export sessions to Markdown/HTML/JSON/JSONLUser Experience2Extension System`V0.8.0`Full extension management with slash commandsBuilding Open Capabilities2LSP Support`V0.7.0`Experimental LSP service (`--experimental-lsp`)Coding Workflow2Anthropic Provider`V0.7.0`Anthropic API provider supportUser Experience2User Feedback Dialog`V0.7.0`In-app feedback collection with fatigue mechanismAdministrative Capabilities2Concurrent Runner`V0.6.0`Batch CLI execution with Git integrationCoding Workflow2Multimodal Input`V0.6.0`Image, PDF, audio, video input supportUser Experience2Skill`V0.6.0`Extensible custom AI skills (experimental)Coding Workflow2Github Actions`V0.5.0`qwen-code-action and automationIntegrating Community Ecosystem1VSCode Plugin`V0.5.0`VSCode extension pluginIntegrating Community Ecosystem1QwenCode SDK`V0.4.0`Open SDK for third-party integrationBuilding Open Capabilities1Session`V0.4.0`Enhanced session managementUser Experience1i18n`V0.3.0`Internationalization and multilingual supportUser Experience1Headless Mode`V0.3.0`Headless mode (non-interactive)Coding Workflow1ACP/Zed`V0.2.0`ACP and Zed editor integrationIntegrating Community Ecosystem1Terminal UI`V0.1.0+`Interactive terminal user interfaceUser Experience1Settings`V0.1.0+`Configuration management systemUser Experience1Theme`V0.1.0+`Multi-theme supportUser Experience1Support OpenAI Protocol`V0.1.0+`Support for OpenAI API protocolUser Experience1Chat Management`V0.1.0+`Session management (save, restore, browse)Coding Workflow1MCP`V0.1.0+`Model Context Protocol integrationCoding Workflow1Multi Model`V0.1.0+`Multi-model support and switchingCoding Workflow1Slash Commands`V0.1.0+`Slash command systemCoding Workflow1Tool: Bash`V0.1.0+`Shell command execution tool (with is\_background param)Coding Workflow1Tool: FileRead/EditFile`V0.1.0+`File read/write and edit toolsCoding Workflow1Custom Commands`V0.1.0+`Custom command loadingBuilding Open Capabilities1Feedback`V0.1.0+`Feedback mechanism (/bug command)Administrative Capabilities1Stats`V0.1.0+`Usage statistics and quota displayAdministrative Capabilities1Memory`V0.0.9+`Project-level and global memory managementUser Experience1Cache Control`V0.0.9+`Prompt caching control (Anthropic, DashScope)User Experience1PlanMode`V0.0.14`Task planning modeCoding Workflow1Compress`V0.0.11`Chat compression mechanismUser Experience1SubAgent`V0.0.11`Dedicated sub-agent systemCoding Workflow1TodoWrite`V0.0.10`Task management and progress trackingCoding Workflow1Tool: TextSearch`V0.0.8+`Text search tool (grep, supports .qwenignore)Coding Workflow1Tool: WebFetch`V0.0.7+`Web content fetching toolCoding Workflow1Tool: WebSearch`V0.0.7+`Web search tool (using Tavily API)Coding Workflow1OAuth`V0.0.5+`OAuth login authentication (Qwen OAuth)User Experience1

#### Features to Develop[](#features-to-develop)

FeaturePriorityStatusDescriptionCategoryBetter UIP1PlannedOptimized terminal UI interactionUser ExperienceOnBoardingP1PlannedNew user onboarding flowUser ExperiencePermissionP1PlannedPermission system optimizationUser ExperienceCross-platform CompatibilityP1In ProgressWindows/Linux/macOS compatibilityUser ExperienceLogViewP2PlannedLog viewing and debugging featureUser ExperienceHooksP2In ProgressExtension hooks systemCoding WorkflowCostsP2PlannedCost tracking and analysisAdministrative CapabilitiesDashboardP2PlannedManagement dashboardAdministrative Capabilities

#### Distinctive Features to Discuss[](#distinctive-features-to-discuss)

FeatureStatusDescriptionHome SpotlightResearchProject discovery and quick launchCompetitive ModeResearchCompetitive modePulseResearchUser activity pulse analysis (OpenAI Pulse reference)Code WikiResearchProject codebase wiki/documentation system

Last updated on March 31, 2026

[Architecture](https://qwenlm.github.io/qwen-code-docs/en/developers/architecture/ "Architecture")[Contributing Guide](https://qwenlm.github.io/qwen-code-docs/en/developers/contributing/ "Contributing Guide")