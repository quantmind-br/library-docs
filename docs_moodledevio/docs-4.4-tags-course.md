---
title: 2 docs tagged with "Course" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/course
source: sitemap
fetched_at: 2026-02-17T14:58:39.038681-03:00
rendered_js: false
word_count: 127
summary: This document provides an overview of Moodle's Custom fields and Groups APIs, explaining how to extend course metadata and manage user collections within courses.
tags:
    - moodle-api
    - custom-fields
    - groups-api
    - course-management
    - user-grouping
category: reference
---

## [Custom fields](https://moodledev.io/docs/4.4/apis/plugintypes/customfield)

Custom fields allow you to create field types to be used for custom fields. Instances of these field types can be added to the respective areas that implement Custom fields API. Currently in Moodle core only courses implement this API, however custom fields are also used in addon plugins for other areas. For example, if you want to display radio buttons on the course edit page, then you can add an instance of a radio custom field plugin to the Course custom fields configuration.

## [Groups API](https://moodledev.io/docs/4.4/apis/subsystems/group)

Moodle Groups are a way of expressing collections of users within a course. They may be defined by the teacher in the course participants page, or created automatically during a bulk user upload (for example, from a text file).