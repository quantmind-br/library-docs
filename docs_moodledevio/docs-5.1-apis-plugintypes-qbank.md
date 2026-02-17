---
title: Question bank plugins | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/plugintypes/qbank
source: sitemap
fetched_at: 2026-02-17T15:35:26.821492-03:00
rendered_js: false
word_count: 123
summary: This document explains how to extend the functionality of the Moodle Question bank through plugins and provides a list of customizable features.
tags:
    - moodle
    - question-bank
    - plugin-development
    - php
    - core-question
category: guide
---

Version: 5.1

Question bank plugins allow you to extend the functionality of the Moodle Question bank. They just one of the plugin types used by core\_question. To see how they fit in, please read [this overview of the question subsystems](https://moodledev.io/docs/5.1/apis/subsystems/question).

Question bank plugins can extend the question bank in many ways, including:

- Table columns
- Action menu items
- Bulk actions
- Navigation node (tabs)
- Question preview additions (via callback)
- [Question filters](https://moodledev.io/docs/5.1/apis/plugintypes/qbank/filters)

The place to start implementing most of these is with a class `classes/plugin_features.php` in your plugin, that declares which features you want to add to the question bank. Until more documentation is written, looking at the examples of the plugins in Moodle core should give you a good idea what you need to do.