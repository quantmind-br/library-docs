---
title: Look At This
url: https://ampcode.com/news/look-at
source: crawler
fetched_at: 2026-02-06T02:08:16.792031721-03:00
rendered_js: false
word_count: 107
summary: This document explains how Amp uses the look_at tool to process large media files via a separate model, minimizing main context window usage by extracting only the requested data.
tags:
    - amp-agent
    - media-processing
    - token-optimization
    - context-window
    - file-analysis
    - ai-tools
category: concept
---

Amp can now look at PDFs, images, and other media files with a *goal* in mind.

Using the new `look_at` tool, Amp sends the file to a separate model — one with its own context window — and gets back only the information it requested.

That means the main agent never has to process the full file, saving valuable tokens in the main context window.

To try it, just tell Amp to look at a media file [with a purpose](https://ampcode.com/threads/T-a7300c6a-82e4-4a62-868f-9c43038c5074), like extracting the structure of a binary file format from the *477-page* PDF spec defining it, and watch it distill the relevant bits out of the file.

![](https://static.ampcode.com/news/look-at-dwarf5.png?ts=1765377502)