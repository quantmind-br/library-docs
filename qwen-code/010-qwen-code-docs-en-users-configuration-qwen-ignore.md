---
title: Ignoring Files
url: https://qwenlm.github.io/qwen-code-docs/en/users/configuration/qwen-ignore
source: github_pages
fetched_at: 2026-04-09T09:04:16.100880981-03:00
rendered_js: true
word_count: 259
summary: This document details the Qwen Ignore (`.qwenignore`) feature, which allows users to specify paths and files that should be excluded from operations within Qwen Code, similar to how `.gitignore` functions.
tags:
    - qwen-code
    - ignore-file
    - git-ignore
    - path-exclusion
    - glob-patterns
category: guide
---

This document provides an overview of the Qwen Ignore (`.qwenignore`) feature of Qwen Code.

Qwen Code includes the ability to automatically ignore files, similar to `.gitignore` (used by Git). Adding paths to your `.qwenignore` file will exclude them from tools that support this feature, although they will still be visible to other services (such as Git).

## How it works[](#how-it-works)

When you add a path to your `.qwenignore` file, tools that respect this file will exclude matching files and directories from their operations. For example, when you use the [`read_many_files`](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/multi-file/) command, any paths in your `.qwenignore` file will be automatically excluded.

For the most part, `.qwenignore` follows the conventions of `.gitignore` files:

- Blank lines and lines starting with `#` are ignored.
- Standard glob patterns are supported (such as `*`, `?`, and `[]`).
- Putting a `/` at the end will only match directories.
- Putting a `/` at the beginning anchors the path relative to the `.qwenignore` file.
- `!` negates a pattern.

You can update your `.qwenignore` file at any time. To apply the changes, you must restart your Qwen Code session.

## How to use `.qwenignore`[](#how-to-use-qwenignore)

StepDescription**Enable .qwenignore**Create a file named `.qwenignore` in your project root directory**Add ignore rules**Open `.qwenignore` file and add paths to ignore, example: `/archive/` or `apikeys.txt`

### `.qwenignore` examples[](#qwenignore-examples)

You can use `.qwenignore` to ignore directories and files:

```
# Exclude your /packages/ directory and all subdirectories
/packages/

# Exclude your apikeys.txt file
apikeys.txt
```

You can use wildcards in your `.qwenignore` file with `*`:

```
# Exclude all .md files
*.md
```

Finally, you can exclude files and directories from exclusion with `!`:

```
# Exclude all .md files except README.md
*.md
!README.md
```

To remove paths from your `.qwenignore` file, delete the relevant lines.

Last updated on March 31, 2026

[Model Providers](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/ "Model Providers")[Trusted Folders](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/trusted-folders/ "Trusted Folders")