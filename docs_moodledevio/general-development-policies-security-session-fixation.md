---
title: Session fixation | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/session-fixation
source: sitemap
fetched_at: 2026-02-17T15:59:48.001641-03:00
rendered_js: false
word_count: 193
summary: This document explains session fixation attacks and outlines how Moodle mitigates these risks, providing security guidance for both developers and administrators.
tags:
    - session-fixation
    - security-best-practices
    - moodle-development
    - session-management
    - vulnerability-prevention
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

Session fixation definition from OWASP

**Session fixation** is an attack that permits an attacker to hijack a valid user session. \[...] The attack consists of obtaining a valid session ID (for example, by connecting to the application), inducing a user to authenticate himself with that session ID, and then hijacking the user-validated session by the knowledge of the used session ID. The attacker has to provide a legitimate Web application session ID and try to make the victim's browser use it. \[...] The session fixation attack is a class of **session hijacking**, which steals the established session between the client and the Web Server after the user logs in. Instead, the session fixation attack fixes an established session on the victim's browser, so the attack starts before the user logs in.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)
- [Session fixation in OWASP](https://owasp.org/www-community/attacks/Session_fixation)

<!--THE END-->

- [What is the danger?](#what-is-the-danger)
- [How Moodle avoids this problem](#how-moodle-avoids-this-problem)
- [What you need to do in your code](#what-you-need-to-do-in-your-code)
- [What you need to do as an administrator](#what-you-need-to-do-as-an-administrator)
- [See also](#see-also)