---
title: 3 docs tagged with "Course" | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/tags/course
source: sitemap
fetched_at: 2026-02-17T15:30:04.400712-03:00
rendered_js: false
word_count: 131
summary: This document provides an overview of specific Moodle developer APIs and subsystems, including course overview integration, custom fields for data entry, and user group management.
tags:
    - moodle-api
    - custom-fields
    - groups-api
    - plugin-development
    - course-management
category: reference
---

## [Course overview integration](https://moodledev.io/docs/5.1/apis/plugintypes/mod/courseoverview)

Summary

## [Custom fields](https://moodledev.io/docs/5.1/apis/plugintypes/customfield)

Custom fields allow you to create field types to be used for custom fields. Instances of these field types can be added to the respective areas that implement Custom fields API. Currently in Moodle core only courses implement this API, however custom fields are also used in addon plugins for other areas. For example, if you want to display radio buttons on the course edit page, then you can add an instance of a radio custom field plugin to the Course custom fields configuration.

## [Groups API](https://moodledev.io/docs/5.1/apis/subsystems/group)

Moodle Groups are a way of expressing collections of users within a course. They may be defined by the teacher in the course participants page, or created automatically during a bulk user upload (for example, from a text file).