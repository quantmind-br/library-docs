---
title: Overview
url: https://epi052.github.io/feroxbuster-docs/overview
source: github_pages
fetched_at: 2026-02-06T10:57:04.220731111-03:00
rendered_js: true
word_count: 279
summary: This document introduces feroxbuster, a tool for forced browsing and directory enumeration, while providing a critical security warning regarding official download sources.
tags:
    - feroxbuster
    - forced-browsing
    - directory-enumeration
    - web-security
    - security-notice
    - penetration-testing
category: guide
---

## ⚠️ **Security Notice – Domain Impersonation**

[Section titled “⚠️ Security Notice – Domain Impersonation”](#%EF%B8%8F-security-notice--domain-impersonation)

The domain **feroxbuster.com** is **NOT affiliated** with this project, its maintainers, or any official feroxbuster releases.

Official feroxbuster downloads are distributed **ONLY** through:

- [https://github.com/epi052/feroxbuster](https://github.com/epi052/feroxbuster/releases)
- package repositories listed in this README
- package repositories listed in the [installation docs](https://epi052.github.io/feroxbuster-docs/installation/android/)

We do **not** distribute software from feroxbuster.com, and we cannot vouch for the authenticity or safety of files hosted there.

If you downloaded feroxbuster from any other domain, we strongly recommend deleting it and reinstalling from an official source.

## What the heck is a ferox anyway?

[Section titled “What the heck is a ferox anyway?”](#what-the-heck-is-a-ferox-anyway)

Ferox is short for Ferric Oxide. Ferric Oxide, simply put, is rust. The name rustbuster was taken, so I decided on a variation.

## What’s it do tho?

[Section titled “What’s it do tho?”](#whats-it-do-tho)

`feroxbuster` is a tool designed to perform [Forced Browsing](https://owasp.org/www-community/attacks/Forced_browsing).

Forced browsing is an attack where the aim is to enumerate and access resources that are not referenced by the web application, but are still accessible by an attacker.

`feroxbuster` uses brute force combined with a wordlist to search for unlinked content in target directories. These resources may store sensitive information about web applications and operational systems, such as source code, credentials, internal network addressing, etc…

This attack is also known as Predictable Resource Location, File Enumeration, Directory Enumeration, and Resource Enumeration.

![demo](https://epi052.github.io/feroxbuster-docs/images/overview/demo.gif)

- [Installation](https://epi052.github.io/feroxbuster-docs/installation/): Make with the scanning already
- [Configuration](https://epi052.github.io/feroxbuster-docs/configuration/): Learn about the different tweaks you can make to your scans
- [Interpreting Results](https://epi052.github.io/feroxbuster-docs/interpreting-results/): Learn how to interpret the results displayed by feroxbuster
- [Examples](https://epi052.github.io/feroxbuster-docs/examples/): See examples and demos of feroxbuster’s available features
- [Frequently Asked Questions](https://epi052.github.io/feroxbuster-docs/faq/): Get answers to common questions and issues