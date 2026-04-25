---
title: Approval Mode
url: https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode
source: github_pages
fetched_at: 2026-04-09T09:03:57.954656681-03:00
rendered_js: true
word_count: 979
summary: This document outlines the four distinct permission modes available in Qwen Code—Plan, Default, Auto-Edit, and YOLO—to allow users to control the level of AI interaction with code and system resources based on task risk.
tags:
    - permission-modes
    - ai-coding-control
    - code-safety
    - development-workflow
    - command-line
category: guide
---

Qwen Code offers three distinct permission modes that allow you to flexibly control how AI interacts with your code and system based on task complexity and risk level.

## Permission Modes Comparison[](#permission-modes-comparison)

ModeFile EditingShell CommandsBest ForRisk Level**Plan**​❌ Read-only analysis only❌ Not executed• Code exploration  
• Planning complex changes  
• Safe code reviewLowest**Default**​✅ Manual approval required✅ Manual approval required• New/unfamiliar codebases  
• Critical systems  
• Team collaboration  
• Learning and teachingLow**Auto-Edit**​✅ Auto-approved❌ Manual approval required• Daily development tasks  
• Refactoring and code improvements  
• Safe automationMedium**YOLO**​✅ Auto-approved✅ Auto-approved• Trusted personal projects  
• Automated scripts/CI/CD  
• Batch processing tasksHighest

### Quick Reference Guide[](#quick-reference-guide)

- **Start in Plan Mode**: Great for understanding before making changes
- **Work in Default Mode**: The balanced choice for most development work
- **Switch to Auto-Edit**: When you’re making lots of safe code changes
- **Use YOLO sparingly**: Only for trusted automation in controlled environments

**Tip**

You can quickly cycle through modes during a session using **Shift+Tab** (or **Tab** on Windows). The terminal status bar shows your current mode, so you always know what permissions Qwen Code has.

## 1. Use Plan Mode for safe code analysis[](#1-use-plan-mode-for-safe-code-analysis)

Plan Mode instructs Qwen Code to create a plan by analyzing the codebase with **read-only** operations, perfect for exploring codebases, planning complex changes, or reviewing code safely.

### When to use Plan Mode[](#when-to-use-plan-mode)

- **Multi-step implementation**: When your feature requires making edits to many files
- **Code exploration**: When you want to research the codebase thoroughly before changing anything
- **Interactive development**: When you want to iterate on the direction with Qwen Code

### How to use Plan Mode[](#how-to-use-plan-mode)

**Turn on Plan Mode during a session**

You can switch into Plan Mode during a session using **Shift+Tab** (or **Tab** on Windows) to cycle through permission modes.

If you are in Normal Mode, **Shift+Tab** (or **Tab** on Windows) first switches into `auto-edits` Mode, indicated by `⏵⏵ accept edits on` at the bottom of the terminal. A subsequent **Shift+Tab** (or **Tab** on Windows) will switch into Plan Mode, indicated by `⏸ plan mode`.

**Start a new session in Plan Mode**

To start a new session in Plan Mode, use the `/approval-mode` then select `plan`

**Run “headless” queries in Plan Mode**

You can also run a query in Plan Mode directly with `-p` or `prompt`:

```
qwen --prompt "What is machine learning?"
```

### Example: Planning a complex refactor[](#example-planning-a-complex-refactor)

```
I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
```

Qwen Code analyzes the current implementation and create a comprehensive plan. Refine with follow-ups:

```
What about backward compatibility?
How should we handle database migration?
```

### Configure Plan Mode as default[](#configure-plan-mode-as-default)

```
// .qwen/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

## 2. Use Default Mode for Controlled Interaction[](#2-use-default-mode-for-controlled-interaction)

Default Mode is the standard way to work with Qwen Code. In this mode, you maintain full control over all potentially risky operations - Qwen Code will ask for your approval before making any file changes or executing shell commands.

### When to use Default Mode[](#when-to-use-default-mode)

- **New to a codebase**: When you’re exploring an unfamiliar project and want to be extra cautious
- **Critical systems**: When working on production code, infrastructure, or sensitive data
- **Learning and teaching**: When you want to understand each step Qwen Code is taking
- **Team collaboration**: When multiple people are working on the same codebase
- **Complex operations**: When the changes involve multiple files or complex logic

### How to use Default Mode[](#how-to-use-default-mode)

**Turn on Default Mode during a session**

You can switch into Default Mode during a session using **Shift+Tab**​ (or **Tab** on Windows) to cycle through permission modes. If you’re in any other mode, pressing **Shift+Tab** (or **Tab** on Windows) will eventually cycle back to Default Mode, indicated by the absence of any mode indicator at the bottom of the terminal.

**Start a new session in Default Mode**

Default Mode is the initial mode when you start Qwen Code. If you’ve changed modes and want to return to Default Mode, use:

**Run “headless” queries in Default Mode**

When running headless commands, Default Mode is the default behavior. You can explicitly specify it with:

```
qwen --prompt "Analyze this code for potential bugs"
```

### Example: Safely implementing a feature[](#example-safely-implementing-a-feature)

```
I need to add user profile pictures to our application. The pictures should be stored in an S3 bucket and the URLs saved in the database.
```

Qwen Code will analyze your codebase and propose a plan. It will then ask for approval before:

1. Creating new files (controllers, models, migrations)
2. Modifying existing files (adding new columns, updating APIs)
3. Running any shell commands (database migrations, dependency installation)

You can review each proposed change and approve or reject it individually.

### Configure Default Mode as default[](#configure-default-mode-as-default)

```
// .qwen/settings.json
{
  "permissions": {
"defaultMode": "default"
  }
}
```

## 3. Auto Edits Mode[](#3-auto-edits-mode)

Auto-Edit Mode instructs Qwen Code to automatically approve file edits while requiring manual approval for shell commands, ideal for accelerating development workflows while maintaining system safety.

### When to use Auto-Accept Edits Mode[](#when-to-use-auto-accept-edits-mode)

- **Daily development**: Ideal for most coding tasks
- **Safe automation**: Allows AI to modify code while preventing accidental execution of dangerous commands
- **Team collaboration**: Use in shared projects to avoid unintended impacts on others

### How to switch to this mode[](#how-to-switch-to-this-mode)

```
# Switch via command
/approval-mode auto-edit

# Or use keyboard shortcut
Shift+Tab (or Tab on Windows) # Switch from other modes
```

### Workflow Example[](#workflow-example)

1. You ask Qwen Code to refactor a function
2. AI analyzes the code and proposes changes
3. **Automatically**​ applies all file changes without confirmation
4. If tests need to be run, it will **request approval**​ to execute `npm test`

## 4. YOLO Mode - Full Automation[](#4-yolo-mode---full-automation)

YOLO Mode grants Qwen Code the highest permissions, automatically approving all tool calls including file editing and shell commands.

### When to use YOLO Mode[](#when-to-use-yolo-mode)

- **Automated scripts**: Running predefined automated tasks
- **CI/CD pipelines**: Automated execution in controlled environments
- **Personal projects**: Rapid iteration in fully trusted environments
- **Batch processing**: Tasks requiring multi-step command chains

**Warning**

**Use YOLO Mode with caution**: AI can execute any command with your terminal permissions. Ensure:

1. You trust the current codebase
2. You understand all actions AI will perform
3. Important files are backed up or committed to version control

### How to enable YOLO Mode[](#how-to-enable-yolo-mode)

```
# Temporarily enable (current session only)
/approval-mode yolo

# Set as project default
/approval-mode yolo --project

# Set as user global default
/approval-mode yolo --user
```

### Configuration Example[](#configuration-example)

```
// .qwen/settings.json
{
  "permissions": {
"defaultMode": "yolo",
"confirmShellCommands": false,
"confirmFileEdits": false
  }
}
```

### Automated Workflow Example[](#automated-workflow-example)

```
# Fully automated refactoring task
qwen --prompt "Run the test suite, fix all failing tests, then commit changes"

# Without human intervention, AI will:
# 1. Run test commands (auto-approved)
# 2. Fix failed test cases (auto-edit files)
# 3. Execute git commit (auto-approved)
```

## Mode Switching & Configuration[](#mode-switching--configuration)

### Keyboard Shortcut Switching[](#keyboard-shortcut-switching)

During a Qwen Code session, use **Shift+Tab**​ (or **Tab** on Windows) to quickly cycle through the three modes:

```
Default Mode → Auto-Edit Mode → YOLO Mode → Plan Mode → Default Mode
```

### Persistent Configuration[](#persistent-configuration)

```
// Project-level: ./.qwen/settings.json
// User-level: ~/.qwen/settings.json
{
  "permissions": {
"defaultMode": "auto-edit",  // or "plan" or "yolo"
"confirmShellCommands": true,
"confirmFileEdits": true
  }
}
```

### Mode Usage Recommendations[](#mode-usage-recommendations)

1. **New to codebase**: Start with **Plan Mode**​ for safe exploration
2. **Daily development tasks**: Use **Auto-Accept Edits**​ (default mode), efficient and safe
3. **Automated scripts**: Use **YOLO Mode**​ in controlled environments for full automation
4. **Complex refactoring**: Use **Plan Mode**​ first for detailed planning, then switch to appropriate mode for execution