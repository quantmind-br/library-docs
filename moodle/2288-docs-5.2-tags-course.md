---
title: 3 docs tagged with "Course" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/course
source: sitemap
fetched_at: 2026-02-17T15:39:13.150422-03:00
rendered_js: false
word_count: 131
summary: This document provides an overview of Moodle developer APIs for course overview integration, custom field types, and the groups subsystem for managing user collections within courses.
tags:
    - moodle-development
    - custom-fields
    - groups-api
    - plugin-types
    - course-management
    - moodle-api
category: api
---

## [Course overview integration](https://moodledev.io/docs/5.2/apis/plugintypes/mod/courseoverview)

Summary

## [Custom fields](https://moodledev.io/docs/5.2/apis/plugintypes/customfield)

Custom fields allow you to create field types to be used for custom fields. Instances of these field types can be added to the respective areas that implement Custom fields API. Currently in Moodle core only courses implement this API, however custom fields are also used in addon plugins for other areas. For example, if you want to display radio buttons on the course edit page, then you can add an instance of a radio custom field plugin to the Course custom fields configuration.

## [Groups API](https://moodledev.io/docs/5.2/apis/subsystems/group)

Moodle Groups are a way of expressing collections of users within a course. They may be defined by the teacher in the course participants page, or created automatically during a bulk user upload (for example, from a text file).