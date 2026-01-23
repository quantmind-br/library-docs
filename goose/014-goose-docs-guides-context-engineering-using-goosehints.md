---
title: Providing Hints to goose | goose
url: https://block.github.io/goose/docs/guides/context-engineering/using-goosehints
source: github_pages
fetched_at: 2026-01-22T22:13:42.801461178-03:00
rendered_js: true
word_count: 1023
summary: This document explains how to use .goosehints files to provide persistent context and custom instructions to the goose developer tool. It covers the setup of global and local hint files, hierarchical loading logic, and strategies for optimizing AI communication.
tags:
    - goosehints
    - ai-context
    - configuration-files
    - developer-workflow
    - custom-instructions
    - project-management
category: guide
---

`.goosehints` is a text file used to provide additional context about your project and improve the communication with goose. The use of `.goosehints` ensures that goose understands your requirements better and can execute tasks more effectively.

goose Hints Video Walkthrough

A good time to consider adding a `.goosehints` file is when you find yourself repeating prompts, or providing the same kind of instructions multiple times. It's also a great way to provide a lot of context which might be better suited in a file.

This guide will walk you through creating and using `.goosehints` files to streamline your workflow with custom instructions and context.

Developer extension required

To make use of the hints file, you need to have the `Developer` extension [enabled](https://block.github.io/goose/docs/getting-started/using-extensions).

## Creating Your Hints File[​](#creating-your-hints-file "Direct link to Creating Your Hints File")

goose supports two types of hint files:

- **Global hints file** - These hints will apply to all your sessions with goose, regardless of directory. Global hints are stored in `~/.config/goose/.goosehints`.
- **Local hints files** - These hints will only apply when working in a specific directory or directory hierarchy.

You can use both global and local hints at the same time. When both exist, goose will consider both your global preferences and project-specific requirements. If the instructions in your local hints file conflict with your global preferences, goose will prioritize the local hints.

Custom Context Files

You can use other agent rule files with goose by using the [`CONTEXT_FILE_NAMES` environment variable](#custom-context-files).

- goose Desktop
- Manual

#### Global hints file[​](#global-hints-file "Direct link to Global hints file")

1. Create a `.goosehints` file in `~/.config/goose`

#### Local hints file[​](#local-hints-file "Direct link to Local hints file")

1. Click the directory path at the bottom of the app and open the directory where you want to create the file
2. Click the button in the top-left to open the sidebar
3. Click `Settings` in the sidebar
4. Click `Chat`
5. Scroll down to the `Project Hints (.goosehints)` section and click `Configure`
6. Enter your local hints in the text area
7. Click `Save`
8. Restart your session so goose can read the updated `.goosehints`

If a `.goosehints` file already exists in the given directory, you can edit your existing hints.

The `.goosehints` file can include any instructions or contextual details relevant to your projects.

## Setting Up Hints[​](#setting-up-hints "Direct link to Setting Up Hints")

The `.goosehints` file supports natural language. Write clear, specific instructions using direct language that goose can easily understand and follow. Include relevant context about your project and workflow preferences, and prioritize your most important guidelines first.

goosehints are loaded at the start of your session and become part of the system prompt sent with every request. This means the content of `.goosehints` contributes to token usage, so keeping it concise can save both cost and processing time.

### Example Global `.goosehints` File[​](#example-global-goosehints-file "Direct link to example-global-goosehints-file")

```
Always use TypeScript for new Next.js projects.

@coding-standards.md  # Contains our coding standards
docs/contributing.md  # Contains our pull request process

Follow the [Google Style Guide](https://google.github.io/styleguide/pyguide.html) for Python code.

Run unit tests before committing any changes.

Prefer functional programming patterns where applicable.
```

### Example Local `.goosehints` File[​](#example-local-goosehints-file "Direct link to example-local-goosehints-file")

```
This is a simple example JavaScript web application that uses the Express.js framework. View [Express documentation](https://expressjs.com/) for extended guidance.

Go through the @README.md for information on how to build and test it as needed.

Make sure to confirm all changes with me before applying.

Run tests with `npm run test` ideally after each change.
```

These examples show two ways to reference other files:

- **`@` syntax**: Automatically includes the file content in goose's immediate context
- **Plain reference**: Points goose to files to review when needed (use for optional or very large files)

### Nested `.goosehints` Files[​](#nested-goosehints-files "Direct link to nested-goosehints-files")

goose supports hierarchical local hints in git repositories. All `.goosehints` files from your current directory up to the root directory are automatically loaded and combined. If you're not working in a git repository, goose only loads the `.goosehints` file from the current directory.

As a best practice, `.goosehints` at each level should only include hints relevant to that scope:

- **Root level**: Include project-wide standards, build processes, and general guidelines
- **Module/feature level**: Add specific requirements for that area of the codebase
- **Directory level**: Include very specific context like local testing procedures or component patterns

**Example Project Structure:**

```
my-project/
├── .git/
├── .goosehints              # Project-wide hints
├── frontend/
│   ├── .goosehints          # Frontend-specific hints
│   └── components/
│       ├── .goosehints      # Component-specific hints
│       └── Button.tsx
└── backend/
    ├── .goosehints          # Backend-specific hints
    └── api/
        └── routes.py
```

When working in `frontend/components/` in this example project, goose loads hints from directories higher up the hierarchy in the following order:

1. `my-project/.goosehints` (project root)
2. `frontend/.goosehints`
3. `frontend/components/.goosehints` (current directory)

## Common Use Cases[​](#common-use-cases "Direct link to Common Use Cases")

Here are some ways people have used hints to provide additional context to goose:

- **Decision-Making**: Specify if goose should autonomously make changes or confirm actions with you first.
- **Validation Routines**: Provide test cases or validation methods that goose should perform to ensure changes meet project specifications.
- **Feedback Loop**: Include steps that allow goose to receive feedback and iteratively improve its suggestions.
- **Point to more detailed documentation**: Indicate important files like `README.md`, `docs/setup-guide.md`, or others that goose should consult for detailed explanations.
- **Organize with @-mentions**: For frequently-needed documentation, use `@filename.md` or `@relative/path/testing.md` to automatically include file content in your current context instead of just referencing it. This ensures goose has immediate access to important information. Include core documentation (like API schemas or coding standards) with @-mentions for immediate context, but use plain references (without `@`) for optional or very large files.

Like prompts, this is not an extensive list to shape your `.goosehints` file. You can include as much context as you need.

## Best Practices[​](#best-practices "Direct link to Best Practices")

- **Keep files updated**: Regularly update the `.goosehints` files to reflect any changes in project protocols or priorities.
- **Be concise**: Make sure the content is straightforward and to the point, ensuring goose can quickly parse and act on the information.
- **Start small**: Create a small set of clear, specific hints and gradually expand them based on your needs. This makes it easier to understand how goose interprets and applies your instructions.
- **Reference other files**: Point goose to relevant files like /docs/style.md or /scripts/validation.js to reduce repetition and keep instructions lightweight.

## Custom Context Files[​](#custom-context-files "Direct link to Custom Context Files")

goose looks for `AGENTS.md` then `.goosehints` files by default, but you can configure a different filename or multiple context files using the `CONTEXT_FILE_NAMES` environment variable. This is useful for:

- **Tool compatibility**: Use conventions from other AI tools (e.g. `CLAUDE.md`)
- **Organization**: Separate frequently-used rules into multiple files that load automatically
- **Project conventions**: Use context files from your project's established toolchain (`.cursorrules`)

Here's how it works:

1. goose looks for each configured filename in both global (~/.config/goose/) and local (current directory) locations
2. All found files are loaded and combined into the context

### Configuration[​](#configuration "Direct link to Configuration")

Set the `CONTEXT_FILE_NAMES` environment variable to a JSON array of filenames. The default is `["AGENTS.md", ".goosehints"]`.

```
# Single custom file
export CONTEXT_FILE_NAMES='["AGENTS.md"]'

# Project toolchain files
export CONTEXT_FILE_NAMES='[".cursorrules", "AGENTS.md"]'

# Multiple files
export CONTEXT_FILE_NAMES='["CLAUDE.md", ".goosehints", "project_rules.txt"]'
```