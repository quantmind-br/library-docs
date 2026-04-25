---
title: Commands
url: https://qwenlm.github.io/qwen-code-docs/en/users/features/commands
source: github_pages
fetched_at: 2026-04-09T09:03:51.984074529-03:00
rendered_js: true
word_count: 968
summary: This document provides a comprehensive reference for all commands within Qwen Code, detailing how to manage sessions, customize the interface using slash commands, inject local files with @ commands, execute system shells with ! commands, and create custom shortcuts.
tags:
    - qwen-code
    - command-reference
    - slash-commands
    - file-injection
    - shell-execution
    - custom-shortcuts
category: reference
---

This document details all commands supported by Qwen Code, helping you efficiently manage sessions, customize the interface, and control its behavior.

Qwen Code commands are triggered through specific prefixes and fall into three categories:

Prefix TypeFunction DescriptionTypical Use CaseSlash Commands (`/`)Meta-level control of Qwen Code itselfManaging sessions, modifying settings, getting helpAt Commands (`@`)Quickly inject local file content into conversationAllowing AI to analyze specified files or code under directoriesExclamation Commands (`!`)Direct interaction with system ShellExecuting system commands like `git status`, `ls`, etc.

## 1. Slash Commands (`/`)[](#1-slash-commands-)

Slash commands are used to manage Qwen Code sessions, interface, and basic behavior.

### 1.1 Session and Project Management[](#11-session-and-project-management)

These commands help you save, restore, and summarize work progress.

CommandDescriptionUsage Examples`/init`Analyze current directory and create initial context file`/init``/summary`Generate project summary based on conversation history`/summary``/compress`Replace chat history with summary to save Tokens`/compress``/resume`Resume a previous conversation session`/resume``/restore`Restore files to state before tool execution`/restore` (list) or `/restore <ID>`

### 1.2 Interface and Workspace Control[](#12-interface-and-workspace-control)

Commands for adjusting interface appearance and work environment.

CommandDescriptionUsage Examples`/clear`Clear terminal screen content`/clear` (shortcut: `Ctrl+L`)`/theme`Change Qwen Code visual theme`/theme``/vim`Turn input area Vim editing mode on/off`/vim``/directory`Manage multi-directory support workspace`/dir add ./src,./tests``/editor`Open dialog to select supported editor`/editor`

### 1.3 Language Settings[](#13-language-settings)

Commands specifically for controlling interface and output language.

CommandDescriptionUsage Examples`/language`View or change language settings`/language`→ `ui [language]`Set UI interface language`/language ui zh-CN`→ `output [language]`Set LLM output language`/language output Chinese`

- Available built-in UI languages: `zh-CN` (Simplified Chinese), `en-US` (English), `ru-RU` (Russian), `de-DE` (German)
- Output language examples: `Chinese`, `English`, `Japanese`, etc.

### 1.4 Tool and Model Management[](#14-tool-and-model-management)

Commands for managing AI tools and models.

CommandDescriptionUsage Examples`/mcp`List configured MCP servers and tools`/mcp`, `/mcp desc``/tools`Display currently available tool list`/tools`, `/tools desc``/skills`List and run available skills`/skills`, `/skills <name>``/approval-mode`Change approval mode for tool usage`/approval-mode <mode (auto-edit)> --project`→`plan`Analysis only, no executionSecure review→`default`Require approval for editsDaily use→`auto-edit`Automatically approve editsTrusted environment→`yolo`Automatically approve allQuick prototyping`/model`Switch model used in current session`/model``/extensions`List all active extensions in current session`/extensions``/memory`Manage AI’s instruction context`/memory add Important Info`

### 1.5 Information, Settings, and Help[](#15-information-settings-and-help)

Commands for obtaining information and performing system settings.

CommandDescriptionUsage Examples`/help`Display help information for available commands`/help` or `/?``/about`Display version information`/about``/stats`Display detailed statistics for current session`/stats``/settings`Open settings editor`/settings``/auth`Change authentication method`/auth``/bug`Submit issue about Qwen Code`/bug Button click unresponsive``/copy`Copy last output content to clipboard`/copy``/quit`Exit Qwen Code immediately`/quit` or `/exit`

### 1.6 Common Shortcuts[](#16-common-shortcuts)

ShortcutFunctionNote`Ctrl/cmd+L`Clear screenEquivalent to `/clear``Ctrl/cmd+T`Toggle tool descriptionMCP tool management`Ctrl/cmd+C`×2Exit confirmationSecure exit mechanism`Ctrl/cmd+Z`Undo inputText editing`Ctrl/cmd+Shift+Z`Redo inputText editing

## 2. @ Commands (Introducing Files)[](#2--commands-introducing-files)

@ commands are used to quickly add local file or directory content to the conversation.

Command FormatDescriptionExamples`@<file path>`Inject content of specified file`@src/main.py Please explain this code``@<directory path>`Recursively read all text files in directory`@docs/ Summarize content of this document`Standalone `@`Used when discussing `@` symbol itself`@ What is this symbol used for in programming?`

Note: Spaces in paths need to be escaped with backslash (e.g., `@My\ Documents/file.txt`)

## 3. Exclamation Commands (`!`) - Shell Command Execution[](#3-exclamation-commands----shell-command-execution)

Exclamation commands allow you to execute system commands directly within Qwen Code.

Command FormatDescriptionExamples`!<shell command>`Execute command in sub-Shell`!ls -la`, `!git status`Standalone `!`Switch Shell mode, any input is executed directly as Shell command`!`(enter) → Input command → `!`(exit)

Environment Variables: Commands executed via `!` will set the `QWEN_CODE=1` environment variable.

## 4. Custom Commands[](#4-custom-commands)

Save frequently used prompts as shortcut commands to improve work efficiency and ensure consistency.

**Note**

Custom commands now use Markdown format with optional YAML frontmatter. TOML format is deprecated but still supported for backwards compatibility. When TOML files are detected, an automatic migration prompt will be displayed.

### Quick Overview[](#quick-overview)

FunctionDescriptionAdvantagesPriorityApplicable ScenariosNamespaceSubdirectory creates colon-named commandsBetter command organizationGlobal Commands`~/.qwen/commands/`Available in all projectsLowPersonal frequently used commands, cross-project useProject Commands`<project root directory>/.qwen/commands/`Project-specific, version-controllableHighTeam sharing, project-specific commands

Priority Rules: Project commands &gt; User commands (project command used when names are same)

### Command Naming Rules[](#command-naming-rules)

#### File Path to Command Name Mapping Table[](#file-path-to-command-name-mapping-table)

File LocationGenerated CommandExample Call`~/.qwen/commands/test.md``/test``/test Parameter``<project>/.qwen/commands/git/commit.md``/git:commit``/git:commit Message`

Naming Rules: Path separator (`/` or `\`) converted to colon (`:`)

### Markdown File Format Specification (Recommended)[](#markdown-file-format-specification-recommended)

Custom commands use Markdown files with optional YAML frontmatter:

```
---
description: Optional description (displayed in /help)
---

Your prompt content here.
Use {{args}} for parameter injection.
```

FieldRequiredDescriptionExample`description`OptionalCommand description (displayed in /help)`description: Code analysis tool`Prompt bodyRequiredPrompt content sent to modelAny Markdown content after the frontmatter

### TOML File Format (Deprecated)[](#toml-file-format-deprecated)

**Warning**

**Deprecated:** TOML format is still supported but will be removed in a future version. Please migrate to Markdown format.

FieldRequiredDescriptionExample`prompt`RequiredPrompt content sent to model`prompt = "Please analyze code: {{args}}"``description`OptionalCommand description (displayed in /help)`description = "Code analysis tool"`

### Parameter Processing Mechanism[](#parameter-processing-mechanism)

Processing MethodSyntaxApplicable ScenariosSecurity FeaturesContext-aware Injection`{{args}}`Need precise parameter controlAutomatic Shell escapingDefault Parameter ProcessingNo special markingSimple commands, parameter appendingAppend as-isShell Command Injection`!{command}`Need dynamic contentExecution confirmation required before

#### 1. Context-aware Injection (`{{args}}`)[](#1-context-aware-injection-args)

ScenarioTOML ConfigurationCall MethodActual EffectRaw Injection`prompt = "Fix: {{args}}"``/fix "Button issue"``Fix: "Button issue"`In Shell Command`prompt = "Search: !{grep {{args}} .}"``/search "hello"`Execute `grep "hello" .`

#### 2. Default Parameter Processing[](#2-default-parameter-processing)

Input SituationProcessing MethodExampleHas parametersAppend to end of prompt (separated by two line breaks)`/cmd parameter` → Original prompt + parameterNo parametersSend prompt as is`/cmd` → Original prompt

🚀 Dynamic Content Injection

Injection TypeSyntaxProcessing OrderPurposeFile Content`@{file path}`Processed firstInject static reference filesShell Commands`!{command}`Processed in middleInject dynamic execution resultsParameter Replacement`{{args}}`Processed lastInject user parameters

#### 3. Shell Command Execution (`!{...}`)[](#3-shell-command-execution-)

OperationUser Interaction1. Parse command and parameters-2. Automatic Shell escaping-3. Show confirmation dialog✅ User confirmation4. Execute command-5. Inject output to prompt-

Example: Git Commit Message Generation

````
---
description: Generate Commit message based on staged changes
---

Please generate a Commit message based on the following diff:

```diff
!{git diff --staged}
```
````

#### 4. File Content Injection (`@{...}`)[](#4-file-content-injection-)

File TypeSupport StatusProcessing MethodText Files✅ Full SupportDirectly inject contentImages/PDF✅ Multi-modal SupportEncode and injectBinary Files⚠️ Limited SupportMay be skipped or truncatedDirectory✅ Recursive InjectionFollow .gitignore rules

Example: Code Review Command

```
---
description: Code review based on best practices
---

Review {{args}}, reference standards:

@{docs/code-standards.md}
```

### Practical Creation Example[](#practical-creation-example)

#### ”Pure Function Refactoring” Command Creation Steps Table[](#pure-function-refactoring-command-creation-steps-table)

OperationCommand/Code1. Create directory structure`mkdir -p ~/.qwen/commands/refactor`2. Create command file`touch ~/.qwen/commands/refactor/pure.md`3. Edit command contentRefer to the complete code below.4. Test command`@file.js` → `/refactor:pure`

```
---
description: Refactor code to pure function
---

Please analyze code in current context, refactor to pure function.
Requirements:

1. Provide refactored code
2. Explain key changes and pure function characteristic implementation
3. Maintain function unchanged
```

### Custom Command Best Practices Summary[](#custom-command-best-practices-summary)

#### Command Design Recommendations Table[](#command-design-recommendations-table)

Practice PointsRecommended ApproachAvoidCommand NamingUse namespaces for organizationAvoid overly generic namesParameter ProcessingClearly use `{{args}}`Rely on default appending (easy to confuse)Error HandlingUtilize Shell error outputIgnore execution failureFile OrganizationOrganize by function in directoriesAll commands in root directoryDescription FieldAlways provide clear descriptionRely on auto-generated description

#### Security Features Reminder Table[](#security-features-reminder-table)

Security MechanismProtection EffectUser OperationShell EscapingPrevent command injectionAutomatic processingExecution ConfirmationAvoid accidental executionDialog confirmationError ReportingHelp diagnose issuesView error information