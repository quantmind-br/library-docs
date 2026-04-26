---
title: Mistral AI Crawlers | Mistral Docs
url: https://docs.mistral.ai/robots
source: sitemap
fetched_at: 2026-04-26T04:11:47.537322203-03:00
rendered_js: false
word_count: 234
summary: This document outlines the usage of specific robots.txt user agents for Mistral AI, detailing how the company performs web indexing and assists user queries while excluding generative AI training.
tags:
    - mistral-ai
    - web-crawlers
    - robots-txt
    - user-agents
    - indexing
    - web-management
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral AI uses specific `robots.txt` user agents for product tasks and web indexing, separate from generative AI training.

## MistralAI-User

For **user actions in Le Chat** — when users ask questions, Le Chat may visit web pages to include source links in responses.

- Governs which sites user requests can be made to
- **Not used for automatic web crawling or generative AI training**

**Full user-agent string:**
```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)
```

Published IP addresses: (contact legal for list)

## MistralAI-Index

For **automated web crawling** for **indexing purposes only** — feeds Mistral AI's search engine used to answer user questions in Le Chat.

- Content crawled is **not used for generative AI training of any kind**

**Full user-agent string:**
```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-Index/1.0; +https://docs.mistral.ai/robots)
```

Published IP addresses: (contact legal for list)

> [!info]
> For generative AI training crawler policies, see the [Mistral AI Legal Center](https://legal.mistral.ai/). #web-crawlers #robots-txt #user-agents