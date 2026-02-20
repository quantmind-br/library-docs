---
title: Configuration information leakage | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/configinfo-leakage
source: sitemap
fetched_at: 2026-02-17T15:59:35.623379-03:00
rendered_js: false
word_count: 363
summary: This document explains the security risks associated with revealing server software versions and technical details, offering guidance for developers and administrators to prevent information disclosure in Moodle.
tags:
    - security-best-practices
    - information-disclosure
    - moodle-security
    - server-hardening
    - error-handling
    - vulnerability-prevention
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

Suppose it is well know, at least by Evil Hacker and their friends, that certain versions of PHP have a critical security vulnerability. Suppose it is easy for Evil Hacker to find out which version of PHP (or Apache, Linux, Windows, Moodle, ...) you are running. Suppose you are running a version that is vulnerable, then you are big trouble.

For example, as I write this, the front page of MoodleDocs is announcing to the world (via the HTTP headers):

```
 HTTP/1.x 200 OK
 Date: Fri, 06 Nov 2009 15:15:29 GMT
 Server: Apache
 X-Powered-By: PHP/5.2.5
```

The `Server` line is good. Many web sites use Apache. We are not revealing much there. The `X-Powered-By` line is not following good practice. It is revealing the exact version of PHP being used.

One very common method that lets users learn a lot about how your server is set up is error messages. It is not only exact version numbers that can help an attacker. For example knowing where things are stored on the server's hard disc can also be useful information, and error messages often include file paths.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

Moodle makes it easy for you to hide error messages, or only have them sent to your log files.

There are warnings for administrators if errors are set to be displayed on-screen.

However, there are options in Moodle to display errors on-screen, for the benefit of developers working on development servers.

Similarly, Moodle provides easy access to the PHP info page, which reveals almost everything about your sever, but only if you are logged in as admin.

Moodle is naughty. With the standard theme, it is easy to find out exactly which version of Moodle is being used from the site home page.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- Only reveal technical information in the parts of error messages that go into the log files. The user-facing error message should describe the problem in more general terms.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- Configure your sever to only send out minimal information about which platform and Moodle version you are running.
- Make sure technical error messages are only sent to log files, not displayed on screen.

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)