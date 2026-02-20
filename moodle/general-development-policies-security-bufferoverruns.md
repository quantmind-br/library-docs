---
title: Buffer overruns and other platform weaknesses | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/bufferoverruns
source: sitemap
fetched_at: 2026-02-17T15:59:31.118998-03:00
rendered_js: false
word_count: 148
summary: This document explains the risks of buffer overruns at the server level for Moodle installations and outlines maintenance responsibilities for administrators to ensure system security.
tags:
    - security
    - buffer-overrun
    - server-administration
    - vulnerability-management
    - moodle-security
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

Buffer overruns do not affect PHP code, since PHP is a high-level language that automatically manages memory allocation.

However, Moodle runs on a server which runs an operating system, a web server, a database and the PHP interpreter. All these are complex pieces of software, and security problems are often found with them. Thus, a Moodle server can be attacked, even if there are no security problems with Moodle.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

There is very little that Moodle can do about this.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- There is nothing you can do about this from PHP code.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- Keep all components of your server up-to-date.
- Subscribe to security mailing lists for all the products you use, so you are notified promptly about potential problems, and new versions.

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)