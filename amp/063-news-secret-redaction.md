---
title: Secret Redaction
url: https://ampcode.com/news/secret-redaction
source: crawler
fetched_at: 2026-02-06T02:08:47.434136927-03:00
rendered_js: false
word_count: 29
summary: This document explains Amp's automated secret redaction feature, which identifies and masks sensitive information to prevent exposure to language models and external tools.
tags:
    - security
    - secret-redaction
    - data-privacy
    - llm-security
    - information-protection
category: reference
---

Amp now identifies secrets and redacts them with markers like `[REDACTED:aws-access-key-id]`, so they are not exposed to the LLM, other tools, or ampcode.com. See [Amp Security Reference](https://ampcode.com/security#secret-redaction) for details.