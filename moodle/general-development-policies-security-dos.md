---
title: Denial of service | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/dos
source: sitemap
fetched_at: 2026-02-17T15:59:39.953416-03:00
rendered_js: false
word_count: 263
summary: This document outlines strategies for preventing and mitigating denial of service attacks in Moodle through logging, performance optimization, and server monitoring.
tags:
    - denial-of-service
    - security-best-practices
    - moodle-development
    - server-performance
    - logging
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

A malicious user tries to overload your server, so it crashes or becomes very slow for legitimate users.

Or there may be some other way that they can make it impossible for legitimate users to use your site. For example, by using a cross-site scripting vulnerability to include the JavaScript `window.close()` in a forum post.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

This is a very difficult type of attack to defend against, if the attacker is determined.

However, most of the really expensive operations in Moodle (for example completing a quiz) are only available to authenticated users, so by logging all requests from authenticated users,Moodle helps administrators identify culprits.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- There is very little you can do from PHP code.
- However, every page access should be logged. This will help investigate who is to blame, if a problem arises. Call `add_to_log` from your scripts.
- Follow general performance good practice, so your code does not consume more resources than necessary.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- There are various tools you can use (for example, firewalls, proxies) to try to limit the number of requests coming into your server. If you have a problem, look into them, but there is not space space for a detailed description here.
- Know how to use the logs to investigate problems.
- Monitor performance on your servers, so you know what normal load looks like, and that you have enough hardware to cope with normal fluctuations in load.

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)
- [Denial of service in OWASP](https://owasp.org/www-community/attacks/Denial_of_Service)