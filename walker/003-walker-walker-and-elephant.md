---
title: Walker and Elephant | Walker
url: https://benz.gitbook.io/walker/walker-and-elephant
source: sitemap
fetched_at: 2026-02-01T13:48:44.648412875-03:00
rendered_js: false
word_count: 94
summary: This document explains the relationship between Walker and Elephant, describing their separate responsibilities in the system and how they work together. It also lists the default providers implemented by Walker.
tags:
    - frontend-backend
    - walker
    - elephant
    - default-providers
    - system-architecture
category: reference
---

Walker is a frontend program that allows you to interact with a backend: Elephant.

Elephant handles:

- what data should be shown
- how things are executed

Walker handles:

- deciding what is queried
- how to run actions

Therefore the overall Walker-Experience has to be configured for those two programs separately.

## [hashtag](#your-friends) Your Friends:

```
walker --help
elephant --help
elephant generatedoc
```

## [hashtag](#providers-implemented-by-walker-per-default) Providers implemented by Walker per default

Walker implements a bunch of Elephant providers by default, these are:

- bluetooth
- archlinux packages
- calc
- providerlist
- websearch
- desktopapplications
- files
- todo
- runner
- symbols
- unicode
- clipboard
- menus

[PreviousWalker - Multi-Purpose Launcherchevron-left](https://benz.gitbook.io/walker)[NextInstallation and Launchingchevron-right](https://benz.gitbook.io/walker/installation-and-launching)

Last updated 3 months ago