---
title: Adversarial Review
url: https://docs.bmad-method.org/explanation/adversarial-review/
source: sitemap
fetched_at: 2026-04-08T11:29:49.113361656-03:00
rendered_js: false
word_count: 365
summary: This document explains the concept of Adversarial Review, a rigorous review technique where the reviewer is mandated to find issues rather than approving content easily. It also warns users that AI-driven adversarial reviews may generate false positives requiring human filtering.
tags:
    - adversarial-review
    - code-review
    - quality-assurance
    - human-filtering
    - analysis-technique
category: concept
---

Force deeper analysis by requiring problems to be found.

## What is Adversarial Review?

[Section titled “What is Adversarial Review?”](#what-is-adversarial-review)

A review technique where the reviewer *must* find issues. No “looks good” allowed. The reviewer adopts a cynical stance - assume problems exist and find them.

This isn’t about being negative. It’s about forcing genuine analysis instead of a cursory glance that rubber-stamps whatever was submitted.

**The core rule:** You must find issues. Zero findings triggers a halt - re-analyze or explain why.

Normal reviews suffer from confirmation bias. You skim the work, nothing jumps out, you approve it. The “find problems” mandate breaks this pattern:

- **Forces thoroughness** - Can’t approve until you’ve looked hard enough to find issues
- **Catches missing things** - “What’s not here?” becomes a natural question
- **Improves signal quality** - Findings are specific and actionable, not vague concerns
- **Information asymmetry** - Run reviews with fresh context (no access to original reasoning) so you evaluate the artifact, not the intent

Adversarial review appears throughout BMad workflows - code review, implementation readiness checks, spec validation, and others. Sometimes it’s a required step, sometimes optional (like advanced elicitation or party mode). The pattern adapts to whatever artifact needs scrutiny.

## Human Filtering Required

[Section titled “Human Filtering Required”](#human-filtering-required)

Because the AI is *instructed* to find problems, it will find problems - even when they don’t exist. Expect false positives: nitpicks dressed as issues, misunderstandings of intent, or outright hallucinated concerns.

**You decide what’s real.** Review each finding, dismiss the noise, fix what matters.

Instead of:

> “The authentication implementation looks reasonable. Approved.”

An adversarial review produces:

> 1. **HIGH** - `login.ts:47` - No rate limiting on failed attempts
> 2. **HIGH** - Session token stored in localStorage (XSS vulnerable)
> 3. **MEDIUM** - Password validation happens client-side only
> 4. **MEDIUM** - No audit logging for failed login attempts
> 5. **LOW** - Magic number `3600` should be `SESSION_TIMEOUT_SECONDS`

The first review might miss a security vulnerability. The second caught four.

## Iteration and Diminishing Returns

[Section titled “Iteration and Diminishing Returns”](#iteration-and-diminishing-returns)

After addressing findings, consider running it again. A second pass usually catches more. A third isn’t always useless either. But each pass takes time, and eventually you hit diminishing returns - just nitpicks and false findings.