---
title: 2 docs tagged with "Custom field" | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/tags/custom-field
source: sitemap
fetched_at: 2026-02-17T15:06:46.597853-03:00
rendered_js: false
word_count: 93
summary: This document provides an overview of Moodle's Custom fields API and plugin types, detailing how to create and implement custom field types for various application areas like courses.
tags:
    - moodle-development
    - custom-fields
    - api-overview
    - plugin-types
    - core-apis
category: api
---

## [Custom fields](https://moodledev.io/docs/4.5/apis/plugintypes/customfield)

Custom fields allow you to create field types to be used for custom fields. Instances of these field types can be added to the respective areas that implement Custom fields API. Currently in Moodle core only courses implement this API, however custom fields are also used in addon plugins for other areas. For example, if you want to display radio buttons on the course edit page, then you can add an instance of a radio custom field plugin to the Course custom fields configuration.

## [Custom fields API](https://moodledev.io/docs/4.5/apis/core/customfields)

Custom fields API overview