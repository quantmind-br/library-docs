---
title: '`lms clone`'
url: https://lmstudio.ai/docs/cli/develop-and-publish/clone
source: sitemap
fetched_at: 2026-04-07T21:27:59.74716308-03:00
rendered_js: false
word_count: 74
summary: This document explains the usage of the `lms clone` command, which is used to copy an artifact from LM Studio Hub to a local machine.
tags:
    - lms-clone
    - artifact-copying
    - command-line-tool
    - hub-integration
category: guide
---

Use `lms clone` to copy an artifact from LM Studio Hub onto your machine.

### Flags[](#flags)

&lt;artifact&gt; : string

Artifact identifier in the form owner/name

\[path] (optional) : string

Destination folder. Defaults to a new folder named after the artifact.

If no path is provided, `lms clone owner/name` creates a folder called `name` in the current directory. The command exits if the target path already exists.

### Clone the latest revision[](#clone-the-latest-revision)

```

lms clone alice/sample-plugin
```

### Clone into a specific directory[](#clone-into-a-specific-directory)

```

lms clone alice/sample-plugin ./my-folder
```