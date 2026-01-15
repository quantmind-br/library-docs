---
title: Droid Shield Plus - Factory Documentation
url: https://docs.factory.ai/cli/account/droid-shield-plus
source: sitemap
fetched_at: 2026-01-13T19:04:32.529609399-03:00
rendered_js: false
word_count: 293
summary: Explains the features and functionality of Droid Shield Plus, an advanced AI-powered security layer that protects against prompt injection and data exposure.
tags:
    - security
    - ai-safety
    - data-loss-prevention
    - git-scanning
    - prompt-injection
category: guide
---

## What is Droid Shield Plus?

Droid Shield Plus is an advanced AI-powered security layer that provides real-time protection against prompt injection attacks, sensitive data exposure, and other security threats. Unlike the standard [Droid Shield](https://docs.factory.ai/cli/account/droid-shield) which uses pattern-based detection, Droid Shield Plus leverages [**Palo Alto Networks Prisma AIRS**](https://docs.paloaltonetworks.com/ai-runtime-security) (AI Runtime Security) to provide intelligent, context-aware security scanning.

* * *

## Key Features

* * *

## How Droid Shield Plus Works

Droid Shield Plus provides two layers of protection:

### 1. Prompt Security Scanning

Every prompt you send to Droid is automatically scanned before processing. If a threat is detected, the prompt is blocked and you’re notified:

```
Droid Shield Plus has blocked this prompt due to detected: prompt injection, sensitive data.

If you believe this is a false positive, you can disable Droid Shield Plus in settings.
```

**Detected threat categories:**

- **Prompt Injection** — Attempts to manipulate AI instructions
- **Sensitive Data (DLP)** — PII, credentials, or confidential information
- **Toxic Content** — Harmful or inappropriate content
- **Malicious Code** — Suspicious code patterns

### 2. Git Commit Scanning

When you perform `git commit` or `git push` operations through Droid, Droid Shield Plus scans your staged changes using AI-powered analysis:

```
Droid Shield Plus has detected potential secrets in your staged changes.

If you would like to override, you can either:
1. Perform the commit/push yourself manually
2. Disable Droid Shield Plus in settings
```

This provides significantly more accurate detection than regex-based scanning, catching:

- Obfuscated or encoded secrets
- Context-aware credential detection
- Custom secret formats
- Secrets embedded in complex code structures

* * *

FeatureDroid ShieldDroid Shield Plus**Detection Method**Pattern/Regex matchingAI-powered analysis**Prompt Scanning**NoYes**Git Commit Scanning**YesYes**Prompt Injection Detection**NoYes**Sensitive Data (DLP)**LimitedComprehensive**Toxic Content Detection**NoYes**Malicious Code Detection**NoYes**False Positive Rate**HigherLower**Availability**All usersEnterprise**Powered By**Built-in patternsPalo Alto Networks Prisma AIRS

* * *

## Enabling Droid Shield Plus

* * *

## Handling Blocked Prompts

When Droid Shield Plus blocks a prompt or git operation:

* * *

## Security & Privacy

Droid Shield Plus is powered by [**Palo Alto Networks Prisma AIRS**](https://docs.paloaltonetworks.com/ai-runtime-security), a leading AI runtime security platform:

- **Real-time Analysis** — Prompts and code are scanned in real-time with minimal latency
- **Enterprise-Grade Security** — Built on Palo Alto Networks’ industry-leading security infrastructure
- **Graceful Degradation** — If the security service is temporarily unavailable, Droid continues to function while logging the issue

* * *

### Prisma AIRS Documentation

* * *

## Get Droid Shield Plus