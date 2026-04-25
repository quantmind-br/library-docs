---
title: Agent Skills
url: https://qwenlm.github.io/qwen-code-docs/en/users/features/skills
source: github_pages
fetched_at: 2026-04-09T09:03:54.026842072-03:00
rendered_js: true
word_count: 665
summary: This guide explains how to create, manage, and utilize Agent Skills within Qwen Code, detailing the structure required for a Skill directory, writing the necessary SKILL.md file, and best practices for ensuring model invocation.
tags:
    - qwen-code
    - agent-skills
    - skill-creation
    - model-extension
    - project-workflow
    - metadata-guidance
category: guide
---

> Create, manage, and share Skills to extend Qwen Code’s capabilities.

This guide shows you how to create, use, and manage Agent Skills in **Qwen Code**. Skills are modular capabilities that extend the model’s effectiveness through organized folders containing instructions (and optionally scripts/resources).

## Prerequisites[](#prerequisites)

- Qwen Code (recent version)
- Basic familiarity with Qwen Code ([Quickstart](https://qwenlm.github.io/qwen-code-docs/en/users/quickstart/))

## What are Agent Skills?[](#what-are-agent-skills)

Agent Skills package expertise into discoverable capabilities. Each Skill consists of a `SKILL.md` file with instructions that the model can load when relevant, plus optional supporting files like scripts and templates.

### How Skills are invoked[](#how-skills-are-invoked)

Skills are **model-invoked** — the model autonomously decides when to use them based on your request and the Skill’s description. This is different from slash commands, which are **user-invoked** (you explicitly type `/command`).

If you want to invoke a Skill explicitly, use the `/skills` slash command:

Use autocomplete to browse available Skills and descriptions.

### Benefits[](#benefits)

- Extend Qwen Code for your workflows
- Share expertise across your team via git
- Reduce repetitive prompting
- Compose multiple Skills for complex tasks

## Create a Skill[](#create-a-skill)

Skills are stored as directories containing a `SKILL.md` file.

### Personal Skills[](#personal-skills)

Personal Skills are available across all your projects. Store them in `~/.qwen/skills/`:

```
mkdir -p ~/.qwen/skills/my-skill-name
```

Use personal Skills for:

- Your individual workflows and preferences
- Skills you’re developing
- Personal productivity helpers

### Project Skills[](#project-skills)

Project Skills are shared with your team. Store them in `.qwen/skills/` within your project:

```
mkdir -p .qwen/skills/my-skill-name
```

Use project Skills for:

- Team workflows and conventions
- Project-specific expertise
- Shared utilities and scripts

Project Skills can be checked into git and automatically become available to teammates.

## Write `SKILL.md`[](#write-skillmd)

Create a `SKILL.md` file with YAML frontmatter and Markdown content:

```
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
Provide clear, step-by-step guidance for Qwen Code.

## Examples
Show concrete examples of using this Skill.
```

### Field requirements[](#field-requirements)

Qwen Code currently validates that:

- `name` is a non-empty string
- `description` is a non-empty string

Recommended conventions (not strictly enforced yet):

- Use lowercase letters, numbers, and hyphens in `name`
- Make `description` specific: include both **what** the Skill does and **when** to use it (key words users will naturally mention)

## Add supporting files[](#add-supporting-files)

Create additional files alongside `SKILL.md`:

```
my-skill/
├── SKILL.md (required)
├── reference.md (optional documentation)
├── examples.md (optional examples)
├── scripts/
│   └── helper.py (optional utility)
└── templates/
    └── template.txt (optional template)
```

Reference these files from `SKILL.md`:

````
For advanced usage, see [reference.md](reference.md).

Run the helper script:

```bash
python scripts/helper.py input.txt
```
````

## View available Skills[](#view-available-skills)

Qwen Code discovers Skills from:

- Personal Skills: `~/.qwen/skills/`
- Project Skills: `.qwen/skills/`
- Extension Skills: Skills provided by installed extensions

### Extension Skills[](#extension-skills)

Extensions can provide custom skills that become available when the extension is enabled. These skills are stored in the extension’s `skills/` directory and follow the same format as personal and project skills.

Extension skills are automatically discovered and loaded when the extension is installed and enabled.

To see which extensions provide skills, check the extension’s `qwen-extension.json` file for a `skills` field.

To view available Skills, ask Qwen Code directly:

```
What Skills are available?
```

Or inspect the filesystem:

```
# List personal Skills
ls ~/.qwen/skills/

# List project Skills (if in a project directory)
ls .qwen/skills/

# View a specific Skill's content
cat ~/.qwen/skills/my-skill/SKILL.md
```

## Test a Skill[](#test-a-skill)

After creating a Skill, test it by asking questions that match your description.

Example: if your description mentions “PDF files”:

```
Can you help me extract text from this PDF?
```

The model autonomously decides to use your Skill if it matches the request — you don’t need to explicitly invoke it.

## Debug a Skill[](#debug-a-skill)

If Qwen Code doesn’t use your Skill, check these common issues:

### Make the description specific[](#make-the-description-specific)

Too vague:

```
description: Helps with documents
```

Specific:

```
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDFs, forms, or document extraction.
```

### Verify file path[](#verify-file-path)

- Personal Skills: `~/.qwen/skills/<skill-name>/SKILL.md`
- Project Skills: `.qwen/skills/<skill-name>/SKILL.md`

```
# Personal
ls ~/.qwen/skills/my-skill/SKILL.md

# Project
ls .qwen/skills/my-skill/SKILL.md
```

### Check YAML syntax[](#check-yaml-syntax)

Invalid YAML prevents the Skill metadata from loading correctly.

```
cat SKILL.md | head -n 15
```

Ensure:

- Opening `---` on line 1
- Closing `---` before Markdown content
- Valid YAML syntax (no tabs, correct indentation)

### View errors[](#view-errors)

Run Qwen Code with debug mode to see Skill loading errors:

You can share Skills through project repositories:

1. Add the Skill under `.qwen/skills/`
2. Commit and push
3. Teammates pull the changes

```
git add .qwen/skills/
git commit -m "Add team Skill for PDF processing"
git push
```

## Update a Skill[](#update-a-skill)

Edit `SKILL.md` directly:

```
# Personal Skill
code ~/.qwen/skills/my-skill/SKILL.md

# Project Skill
code .qwen/skills/my-skill/SKILL.md
```

Changes take effect the next time you start Qwen Code. If Qwen Code is already running, restart it to load the updates.

## Remove a Skill[](#remove-a-skill)

Delete the Skill directory:

```
# Personal
rm -rf ~/.qwen/skills/my-skill

# Project
rm -rf .qwen/skills/my-skill
git commit -m "Remove unused Skill"
```

## Best practices[](#best-practices)

### Keep Skills focused[](#keep-skills-focused)

One Skill should address one capability:

- Focused: “PDF form filling”, “Excel analysis”, “Git commit messages”
- Too broad: “Document processing” (split into smaller Skills)

### Write clear descriptions[](#write-clear-descriptions)

Help the model discover when to use Skills by including specific triggers:

```
description: Analyze Excel spreadsheets, create pivot tables, and generate charts. Use when working with Excel files, spreadsheets, or .xlsx data.
```

### Test with your team[](#test-with-your-team)

- Does the Skill activate when expected?
- Are the instructions clear?
- Are there missing examples or edge cases?