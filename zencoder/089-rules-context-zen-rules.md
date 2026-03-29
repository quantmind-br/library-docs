---
title: Zen Rules - Zencoder Docs
url: https://docs.zencoder.ai/rules-context/zen-rules
source: crawler
fetched_at: 2026-01-23T09:28:11.861718446-03:00
rendered_js: false
word_count: 1363
summary: Explains how to use and configure Zen Rules to provide hierarchical project context and coding standards for Zencoder's AI agents.
tags:
    - zencoder
    - zen-rules
    - ai-configuration
    - context-management
    - coding-standards
    - markdown-files
category: guide
---

## Rules Organization and Hierarchy

Zencoder uses a hierarchical system of rules and instructions to provide the most relevant context. Understanding this hierarchy helps you choose the right approach for your needs:

### How Each Level Works

- **Zen Rules**: Project-based markdown files that provide custom context to Zencoder’s AI agents. Unlike global AI instructions, they’re committed to your codebase for team sharing and can be applied always (`alwaysApply: true`) or conditionally based on glob patterns. Perfect for team standards, architecture guidelines, and project-specific conventions.
- **Instructions for AI**: Your personal, global preferences managed through Zencoder’s three-dot menu → `Instructions for AI`. These apply across all your projects and are ideal for general coding style preferences or tone of voice the agent is using to respond to you.
- [**Repo Info**](https://docs.zencoder.ai/features/repo-info-agent): Generated context about your repository structure, technologies, and patterns (requires running the `/repo-info` agent). This runs with `alwaysApply: true` to help all agents understand your project better.

## Getting Started

### 1. Locate the Rules Directory

Your Zen Rules live in the `.zencoder/rules` directory at your project root. When you upgrade to the latest version of Zencoder, this directory is created automatically with proper migrations handled for you.

### 2. Create Your First Rule

To create a new Zen rule, you can use the built-in rule creator directly from the chat interface:

1. Click the `@` sign in the chat input box
2. Select `Zen Rules` from the dropdown menu
3. Click on `+ New rule...` at the top of the rules list

![Zen Rules dropdown showing the New rule option highlighted at the top of the rules list](https://mintcdn.com/forgoodaiinc/QfspiLow5vUmEnCP/images/rules-new-rules.png?fit=max&auto=format&n=QfspiLow5vUmEnCP&q=85&s=77ef21fd7cba842ec22ba57169efb5c5) This will open a template with the proper markdown structure for you to fill in. The template includes the necessary frontmatter and placeholders for your rule content.

#### Rule Template Structure

When you create a new rule, you’ll work with this template structure:

```
---
description: "Brief description of what this rule covers"
globs: ["*.md", "*.mdx"]  # Optional: file patterns where this rule applies
alwaysApply: false         # Optional: set to true if rule should always be active
---

# Your Rule Title

## Section 1

Your guidelines, instructions, and examples go here.

## Section 2

Additional context, best practices, or specific requirements.
```

#### Example Rule

Here’s an example of a complete rule for markdown writing styles:

```
---
description: "Markdown writing style"
globs: ["*.md", "*.mdx"]
alwaysApply: false
---

# Markdown Style Guide

## Formatting Rules

- Use ATX-style headers (# ## ###) instead of underline style
- Separate headers from content with one blank line
- Use **bold** for emphasis, *italic* for subtle emphasis
- End files with a single newline

## Best Practices

- Keep line length under 100 characters when possible
- Use meaningful link text instead of "click here"
- Include alt text for all images
- Use consistent bullet point style (-)
```

### 3. Reference Rules in Chat

You can manually include any rule by @mentioning it in your chat. Type `@` and then select `Zen Rules` from the dropdown, then choose from the list of available rules: ![Zen Rules mentioning interface showing @ dropdown with Zen Rules option and list of available rules](https://mintcdn.com/forgoodaiinc/27PjYbRg8KyUQ0DD/images/zen-rules-mentioning.png?fit=max&auto=format&n=27PjYbRg8KyUQ0DD&q=85&s=146c7334ff1f14c731852c7783e06838) This allows you to apply specific rules on-demand, in addition to rules that are automatically applied based on `alwaysApply: true` or matching glob patterns as described earlier.

### 4. View Applied Rules

You can now see which rules are currently active in your chat by clicking on the rules icon in the toolbar. The icon displays a badge showing the number of applied rules, and when clicked, reveals a panel listing all currently applied rules: ![Rules selector showing auto-applied Zen rules with repo.md marked as Always active](https://mintcdn.com/forgoodaiinc/QfspiLow5vUmEnCP/images/rules-selector.png?fit=max&auto=format&n=QfspiLow5vUmEnCP&q=85&s=ba1768451b9a4eead6634748b0860dc4)

## Rule File Format

Each rule file follows this structure:

```
---
description: "Brief description of what this rule covers"
globs: ["*.ts", "*.tsx", "src/**/*.js"]  # Optional: file patterns
alwaysApply: false                        # Optional: default is false
---

# Rule Content

Your markdown content here with guidelines, examples, and instructions.
```

### Frontmatter Fields

FieldRequiredDescription`description`**Yes**Brief description of the rule’s purpose. Displayed in chat when @mentioning rules and used by agents to understand rule relevance. Example: `"TypeScript coding guidelines and best practices"``globs`NoArray of file patterns that trigger this rule. Rule is automatically included when working with matching files. Examples: `["*.ts", "*.tsx"]`, `["src/**/*.js"]`, `["*.md", "*.mdx"]``alwaysApply`NoBoolean (default: false). When `true`, rule is included in every request regardless of file context. Note: When `true`, the `globs` field is ignored

## Practical Examples

Here are two complete examples showing different types of rules and how they’re structured:

## How Zen Rules Work

When you send a message to Zencoder, the system automatically includes relevant rules in the context:

1. **Always applied rules** are included in every request when you set `alwaysApply: true` in the frontmatter. That’s the case with `repo.md`, for example.
2. **Pattern matched rules** are automatically included when you’re working with files that match their glob patterns
3. **Manually referenced rules** are added when you @mention them in your chat for that specific request

### Why This Matters

This hierarchical system provides essential benefits for modern development workflows. **Team collaboration** becomes seamless when consistent coding standards are committed to your repository, ensuring everyone follows the same patterns. **Project-specific context** tailors AI responses to your unique codebase and architecture, making suggestions more relevant and accurate. **Conditional logic** allows you to apply different rules based on file types or directories, giving you precise control over when and where specific guidelines are enforced.

## Choosing the Right Approach

Understanding when to use repo.md (and Repo Info agent) versus custom rules helps you organize context effectively.

### repo.md

- **Project structure** and architecture patterns
- **Build commands** and development workflows (especially in non-monorepo projects)
- **Technology stack** and framework configurations
- **Dependencies** and package management details

### Custom rules

- **Coding standards** and style guidelines
- **File-specific conventions** (using globs to target specific file types)
- **Team processes** and review requirements
- **Conditional logic** that applies only to certain directories or file patterns

## Configuring Rule Folders

Zencoder always searches for rules in the `.zencoder/rules` folder by default. However, you can configure additional folders where Zencoder will look for AI rules (`*.md` and `*.mdc` files). This is particularly useful if:

- You’re switching from another AI coding tool and want to keep using your existing rules
- Your team has established rules in different locations
- You want to organize rules across multiple directories

### Setting Up Additional Rule Folders

- VS Code
- JetBrains

To configure rule folders in VS Code:

1. Go to the Zencoder `⋯` (three-dot menu)
2. Click on `Settings` from the dropdown menu
3. In the sidebar, scroll down to find `Zencoder: Rule Folders`
4. You’ll see predefined folders for common AI tools:
   
   - `.ai/rules`
   - `.cursor/rules`
   - `.clinerules`
   - `.windsurf/rules`
   - `.continue/rules`
5. Click the `Add Item` button to add custom folders

![VS Code Zencoder Rule Folders settings showing predefined folders and Add Item button](https://mintcdn.com/forgoodaiinc/IesoNnxgT6AbeKxy/images/rules-vsc.png?fit=max&auto=format&n=IesoNnxgT6AbeKxy&q=85&s=3b03b3c7820c1af40208045282057ce6)

To configure rule folders in JetBrains IDEs:

1. Open `Settings` (`Cmd+,` on macOS or `Ctrl+Alt+S` on Windows/Linux)
2. Navigate to `Tools` then select `Zencoder`
3. Find the `AI Rules Configuration` section
4. You’ll see a note that `.zencoder/rules` folder is always included
5. Below that, you can see and manage additional folders:
   
   - `.ai/rules`
   - `.cursor/rules`
   - `.clinerules`
   - `.windsurf/rules`
   - `.continue/rules`
6. Click the `+` button to add custom folders

![JetBrains Zencoder settings showing AI Rules Configuration section with predefined folders](https://mintcdn.com/forgoodaiinc/IesoNnxgT6AbeKxy/images/rules-jb.png?fit=max&auto=format&n=IesoNnxgT6AbeKxy&q=85&s=e2b94226a0369165f25897ef5203dc0d)

### Why This Matters

**Seamless migration** in cases where you’re switching from Cursor, Windsurf, Cline, Continue, or other AI tools - you don’t need to move or duplicate your existing rules. Zencoder will read them from their original locations. **Team flexibility** matters and different team members might use different AI tools. By supporting multiple rule folders, everyone can contribute rules using their preferred tool’s conventions. **Backward compatibility** is made easier if your existing workflows and rule structures remain intact while gaining access to Zencoder’s capabilities.

### How It Works

When processing a request, Zencoder:

1. Always includes rules from `.zencoder/rules` (the default location)
2. Searches all configured additional folders for `*.md` and `*.mdc` files
3. Applies rules based on their frontmatter configuration (`alwaysApply`, `globs`, etc.)

## Best Practices

Good rules are focused, actionable, and scoped to specific concerns. Think of them as internal documentation that guides both your team and the AI.

### Writing Effective Rules

**Keep it concise and specific.** Aim for under 300 lines per rule and avoid broad instructions like “write good code” - the AI already knows general best practices. Instead, focus on your project’s specific requirements and patterns. **Use clear formatting.** Structure your rules with bullet points, numbered lists, and markdown headers. This makes them easier for the AI to parse and follow:

```
# API Standards
- Use plural nouns for endpoints: `/users`, `/products`
- Version with prefix: `/api/v1/users`
- Always return consistent JSON structure
```

**Group related concepts.** In addition to markdown headers, HTML-like XML tags can help organize similar rules together:

```
<error_handling>
- Use appropriate HTTP status codes
- Include descriptive error messages
- Log errors with request context
</error_handling>
```

### Organization Tips

**Split large rules** into multiple, composable files rather than creating monolithic documents. Use descriptive filenames like `typescript-standards.md` instead of generic names. **Use globs effectively** to target specific directories or file types. This allows you to apply rules only where they are relevant, reducing noise in the AI’s context. **Turn repetitive prompts into rules** - if you find yourself writing the same prompts over and over again, consider creating a rule file to capture that knowledge. **For complex workflows**, if you’re facing increasingly complex and repeatable prompts that need to use different tools and MCPs, consider exploring [Custom Agents](https://docs.zencoder.ai/features/custom-agents) for more advanced automation.

### Team Workflow

Treat rule changes like code changes with proper review processes. Use clear descriptions in your frontmatter so team members understand each rule’s purpose and scope.