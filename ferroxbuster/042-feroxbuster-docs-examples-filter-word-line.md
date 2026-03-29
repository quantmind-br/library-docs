---
title: Filter by Word/Line Count
url: https://epi052.github.io/feroxbuster-docs/examples/filter-word-line
source: github_pages
fetched_at: 2026-02-06T10:55:34.449867902-03:00
rendered_js: true
word_count: 136
summary: This document explains how to filter scan results based on the number of lines and words in the response body using specific command-line arguments. It also describes how these filters correspond to the information displayed in the tool's output bar.
tags:
    - feroxbuster
    - command-line-interface
    - response-filtering
    - word-count
    - line-count
    - http-responses
category: guide
---

## Filter Response by Word Count & Line Count

[Section titled “Filter Response by Word Count & Line Count”](#filter-response-by-word-count--line-count)

In addition to filtering on the size of a response, version 1.6.0 added the ability to filter out responses based on the number of lines and/or words contained within the response body. This change drove a change to the information displayed to the user as well. This section will detail the new information and how to make use of it with the new filters provided.

## Relevant CLI options

[Section titled “Relevant CLI options”](#relevant-cli-options)

```

-N, --filter-lines <LINES>...
Filter out messages of a particular line count (ex: -N 20 -N 31,30)
-W, --filter-words <WORDS>...
Filter out messages of a particular word count (ex: -W 312 -W 91,82)
```

## How output relates to filters

[Section titled “How output relates to filters”](#how-output-relates-to-filters)

![response-bar-explained](https://epi052.github.io/feroxbuster-docs/images/interpreting-results/response-bar-explained.png)

Filters that correspond to the output above:

- **Response status code**: filtered with `-C|--filter-status`
- **# of lines**: filtered with `-N|--filter-lines`
- **# of words**: filtered with `-W|--filter-words`
- **# of chars (bytes)**: filtered with `-S|--filter-size`