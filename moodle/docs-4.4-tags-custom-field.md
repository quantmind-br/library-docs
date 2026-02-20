---
title: 2 docs tagged with "Custom field" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/custom-field
source: sitemap
fetched_at: 2026-02-17T14:58:39.828583-03:00
rendered_js: false
word_count: 93
summary: This document explains the purpose and implementation of custom fields in Moodle, detailing how different field types can be integrated into areas like course configuration.
tags:
    - moodle-development
    - custom-fields
    - custom-field-api
    - plugin-types
    - field-types
category: api
---

## [Custom fields](https://moodledev.io/docs/4.4/apis/plugintypes/customfield)

Custom fields allow you to create field types to be used for custom fields. Instances of these field types can be added to the respective areas that implement Custom fields API. Currently in Moodle core only courses implement this API, however custom fields are also used in addon plugins for other areas. For example, if you want to display radio buttons on the course edit page, then you can add an instance of a radio custom field plugin to the Course custom fields configuration.

## [Custom fields API](https://moodledev.io/docs/4.4/apis/core/customfields)

Custom fields API overview