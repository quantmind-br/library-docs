---
title: Data-loss | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/dataloss
source: sitemap
fetched_at: 2026-02-17T15:59:39.910057-03:00
rendered_js: false
word_count: 177
summary: This document outlines security and design best practices for preventing accidental or malicious data loss within Moodle development, emphasizing confirmation steps and risk assessment.
tags:
    - moodle-security
    - data-loss-prevention
    - secure-coding
    - user-interface-design
    - risk-management
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

This is more a symptom or other vulnerabilities, than a vulnerability in its own right.

For example, Evil Hacker can use cross-site request forgery or SQL injection to maliciously destroy lots of your data. Or the fact that someone has permission to destroy a lot of data may indicate that the code is not performing sufficient authorisation checks.

However, it is also possible for users to accidentally destroy lots of data if the user-interface is badly designed and confusing.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

- Writing secure code so that data cannot be destroyed maliciously.
- Trying to design clear interfaces, so that users understand the effects of their actions.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- Actions that destroy a significant amount of data should have a confirmation step.
  
  - Capabilities that let people destroy a lot of information should have `RISK_DATALOSS`.
- Follow the guidelines for avoiding:
  
  - [Unauthorised access](https://moodledev.io/general/development/policies/security/unauthorised-access)
  - [Cross-site request forgery (XSRF)](https://moodledev.io/general/development/policies/security/crosssite-request-forgery)
  - [SQL injection](https://moodledev.io/general/development/policies/security/sql-injection)
  - [Command-line injection](https://moodledev.io/general/development/policies/security/commandline-injection)
  - and so on.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- Be careful!

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)