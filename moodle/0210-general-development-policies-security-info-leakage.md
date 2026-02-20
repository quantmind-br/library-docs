---
title: Confidential information leakage | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/info-leakage
source: sitemap
fetched_at: 2026-02-17T15:59:43.741506-03:00
rendered_js: false
word_count: 184
summary: This document provides guidance on protecting personal user information in Moodle through appropriate permission checks, security vulnerability prevention, and administrative role configuration.
tags:
    - moodle-security
    - data-privacy
    - personal-information
    - access-control
    - risk-personal
    - data-protection
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

Again, this is more a symptom of [Unauthorised access](https://moodledev.io/general/development/policies/security/unauthorised-access) and other problems, rather than a problem in its own right. However, Moodle handles a lot of personal information about its users, and some countries have laws about how that information is handled, so it is worth having a separate section to consider how we protect the personal information we have about our users.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

Moodle now has enough capabilities that it can be configures to comply with various jurisdictions' privacy laws, while also being used in more permissive ways in other situations.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- Think about the type of information you are displaying when deciding which permissions checks to perform.
  
  - When a capability lets a user see more personal information about another user than normal, consider marking it as `RISK_PERSONAL`.
- Make sure you protect against [Unauthorised access](https://moodledev.io/general/development/policies/security/unauthorised-access), [Cross-site scripting](https://moodledev.io/general/development/policies/security/crosssite-scripting), and other problems that allow sensitive information to leak.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- Consider privacy issues when defining roles, and changing other settings.

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)