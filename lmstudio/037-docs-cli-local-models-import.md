---
title: '`lms import`'
url: https://lmstudio.ai/docs/cli/local-models/import
source: sitemap
fetched_at: 2026-04-07T21:28:27.371524169-03:00
rendered_js: false
word_count: 171
summary: This document explains the usage and various flags available for the `lms import` command, detailing how to bring an existing model file into LM Studio under different conditions.
tags:
    - lms-import
    - model-management
    - command-flags
    - file-operations
category: guide
---

Use `lms import` to bring an existing model file into LM Studio without downloading it.

### Flags[](#flags)

&lt;file-path&gt; : string

Path to the model file to import

--user-repo (optional) : string

Set the target folder as /. Skips the categorization prompts.

-y, --yes (optional) : flag

Skip confirmations and try to infer the model location from the file name

-c, --copy (optional) : flag

Copy the file instead of moving it

-L, --hard-link (optional) : flag

Create a hard link instead of moving or copying the file

-l, --symbolic-link (optional) : flag

Create a symbolic link instead of moving or copying the file

--dry-run (optional) : flag

Do not perform the import, just show what would be done

Only one of `--copy`, `--hard-link`, or `--symbolic-link` can be used at a time. If none is provided, `lms import` moves the file by default.

### Import a model file[](#import-a-model-file)

```

lms import ~/Downloads/model.gguf
```

### Keep the original file[](#keep-the-original-file)

```

lms import ~/Downloads/model.gguf --copy
```

### Pick the target folder yourself[](#pick-the-target-folder-yourself)

Use `--user-repo` to skip prompts and place the model in the chosen namespace:

```

lms import ~/Downloads/model.gguf --user-repo my-user/custom-models
```

### Dry run before importing[](#dry-run-before-importing)

```

lms import ~/Downloads/model.gguf --dry-run
```