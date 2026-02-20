---
title: Brute-forcing login | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/bruteforcing-login
source: sitemap
fetched_at: 2026-02-17T15:59:30.713308-03:00
rendered_js: false
word_count: 203
summary: This document explains how Moodle prevents brute-force login attacks through account lockout mechanisms and password complexity settings for administrators and developers.
tags:
    - moodle-security
    - brute-force-prevention
    - account-lockout
    - authentication-security
    - password-policy
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

Evil Hacker wants to break into your Moodle site by stealing the account of a registered user.

They write a script that automatically tries logging in with a range of common passwords, for example, `admin / admin`, `admin / apple`, `admin / 1234`, .... It only takes one user with we weak password that Evil Hacker can guess, and your site is compromised.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

A lockout system is present in Moodle 2.5 onwards, you just need to turn it on at **Administration &gt; Site administration &gt; Security &gt; Site security settings &gt; Account lockout threshold (`$CFG->lockoutthreshold`)**.

Moodle also counts failed login attempts, and can alert the administrator by email when there are too many.

There are admin settings to enforce a minimum level of complexity for passwords, for example, by insisting on a minimum number of characters.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- If you are writing an authentication plugin, ensure that all failed logins are logged correctly.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- Consider turning on the options for reporting login failures.
- Consider turning on the settings that ensure password complexity.

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)
- [Brute force attack in OWASP](https://owasp.org/www-community/attacks/Brute_force_attack)