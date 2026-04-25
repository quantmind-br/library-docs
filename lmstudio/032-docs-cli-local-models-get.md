---
title: '`lms get`'
url: https://lmstudio.ai/docs/cli/local-models/get
source: sitemap
fetched_at: 2026-04-07T21:28:35.382001265-03:00
rendered_js: false
word_count: 208
summary: This document explains how to use the `lms get` command to search for and download various language models from online repositories, detailing available flags and usage options.
tags:
    - command-line
    - model-download
    - repository-search
    - flags
    - quantization
category: guide
---

The `lms get` command allows you to search and download models from online repositories. If no model is specified, it shows staff-picked recommendations.

Models you download via `lms get` will be stored in your LM Studio model directory.

### Flags[](#flags)

\[modelName] (optional) : string

The model to download. If omitted, staff picks are shown. For models with multiple quantizations, append '@' (e.g., 'llama-3.1-8b@q4\_k\_m').

--mlx (optional) : flag

Include only MLX models in search results. If either '--mlx' or '--gguf' is set, only matching formats are shown; otherwise results match installed runtimes.

--gguf (optional) : flag

Include only GGUF models in search results. If either '--mlx' or '--gguf' is set, only matching formats are shown; otherwise results match installed runtimes.

-n, --limit (optional) : number

Limit the number of model options shown.

--always-show-all-results (optional) : flag

Always prompt you to choose from search results, even when there's an exact match.

-a, --always-show-download-options (optional) : flag

Always prompt you to choose a quantization, even when an exact match is auto-selected.

## Download a model[](#download-a-model "Link to 'Download a model'")

Download a model by name:


### Specify quantization[](#specify-quantization)

Download a specific model quantization:

```

lms get llama-3.1-8b@q4_k_m
```

### Filter by format[](#filter-by-format)

Show only MLX or GGUF models:

```

lms get --mlx
lms get --gguf
```

### Control search results[](#control-search-results)

Limit the number of results:


Always show all options:

```

lms get --always-show-all-results
lms get --always-show-download-options
```