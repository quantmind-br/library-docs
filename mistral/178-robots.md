---
title: Mistral AI Crawlers | Mistral Docs
url: https://docs.mistral.ai/robots
source: crawler
fetched_at: 2026-01-29T07:33:14.22750468-03:00
rendered_js: false
word_count: 144
summary: Documentation regarding Mistral AI's web crawlers, providing technical details on user agent identification and instructions for managing crawler access via robots.txt.
tags:
    - Mistral AI
    - crawlers
    - web bots
    - documentation
    - SEO
category: guide
---

Mistral AI employs web crawlers, aka "robots", and user agents to execute tasks for its products, either automatically or upon user request. To facilitate webmasters in managing how their sites and content interact with AI, Mistral AI utilizes specific robots.txt tags.

`MistralAI-User` is for **user actions in LeChat**. When users ask LeChat a question, it may **visit a web page** to help answer and **include a link to the source in its response**.

`MistralAI-User` governs which sites these user requests can be made to. It is **not used for crawling the web in any automatic fashion, nor to crawl content for generative AI training**.

For more information about Mistral AI's policy with regard to web crawlers employed for generative AI training, please refer to the [Mistral AI Legal Center](https://legal.mistral.ai/copyright).

Full user-agent string:

- `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)`

All published IP addresses: