---
title: Providers | Walker
url: https://benz.gitbook.io/walker/providers
source: sitemap
fetched_at: 2026-02-01T13:48:36.762235482-03:00
rendered_js: false
word_count: 113
summary: Explains Elephant's modular architecture and how to configure data providers for Walker using Elephant-Providers.
tags:
    - elephant
    - walker
    - providers
    - modular-design
    - configuration
category: guide
---

By default Elephant doesn't actually provide any data to Walker. You can install any of these Elephant-Providers in order to "feed" Walker with the according information:

This modular design allows you to only install what you want, without bloating up your system with other things.

By default, Walker provides many preconfigured prefixes for these providers out-of-the-box. Please refer to the default config.

Each provider has it's own documentation. You can get a complete configuration markdown file by running `elephant generatedoc`.

This will provide you with documentation for every provider you have installed.

Elephant has a [community repoarrow-up-right](https://github.com/abenz1267/elephant-community).

Custom Menus from this repository can be installed via `elephant community`.

Last updated 2 months ago