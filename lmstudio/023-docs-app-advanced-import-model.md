---
title: Import Models
url: https://lmstudio.ai/docs/app/advanced/import-model
source: sitemap
fetched_at: 2026-04-07T21:29:35.43971885-03:00
rendered_js: false
word_count: 122
summary: This document explains how to import external GGUF models into LM Studio using the experimental `lms import` command and details the required directory structure for managing downloaded models.
tags:
    - gguf-models
    - lm-studio
    - model-importing
    - directory-structure
    - command-line
category: guide
---

You can use compatible models you've downloaded outside of LM Studio by placing them in the expected directory structure.

* * *

### Use `lms import` (experimental)[](#use-lms-import-experimental)

To import a `GGUF` model you've downloaded outside of LM Studio, run the following command in your terminal:

```

lms import <path/to/model.gguf>
```

###### Follow the interactive prompt to complete the import process.

### LM Studio's expected models directory structure[](#lm-studios-expected-models-directory-structure)

![undefined](https://lmstudio.ai/assets/docs/reveal-models-dir.png)

Manage your models directory in the My Models tab

LM Studio aims to preserves the directory structure of models downloaded from Hugging Face. The expected directory structure is as follows:

```

~/.lmstudio/models/
└── publisher/
    └── model/
        └── model-file.gguf
```

For example, if you have a model named `ocelot-v1` published by `infra-ai`, the structure would look like this:

```

~/.lmstudio/models/
└── infra-ai/
    └── ocelot-v1/
        └── ocelot-v1-instruct-q4_0.gguf
```

* * *

Chat with other LM Studio users, discuss LLMs, hardware, and more on the [LM Studio Discord server](https://discord.gg/aPQfnNkxGC).