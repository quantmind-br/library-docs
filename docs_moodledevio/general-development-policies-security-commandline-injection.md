---
title: Command-line injection | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/commandline-injection
source: sitemap
fetched_at: 2026-02-17T15:59:34.632668-03:00
rendered_js: false
word_count: 156
summary: This document explains the risks of command-line injection in Moodle and provides best practices for preventing it, such as using PHP libraries instead of shell commands and correctly escaping user input.
tags:
    - security
    - moodle-development
    - command-injection
    - input-validation
    - php-security
    - web-security
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

This is very like SQL injection, except that it arises when we execute a command-line program rather than when we do a database query.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

Always try to avoid using command-line tools if at all possible. Look for equivalent PHP libraries.

However, when there is no other option, it is the standard approach of cleaning the input, and then escaping the values that came from the user before including them in the command-line.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- Try to avoid using shell commands if at all possible.
  
  - Many utilities are available as PHP libraries.
- If you can't avoid shell commands, use `escapeshellcmd` and `escapeshellarg`.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- This is not something you can do much about.
- However, turn off Moodle features that use shell commands (for example, the LaTeX filter) unless you actually need them.

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)