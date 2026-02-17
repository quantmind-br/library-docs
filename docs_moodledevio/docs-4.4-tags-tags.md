---
title: 2 docs tagged with "Tags" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/tags
source: sitemap
fetched_at: 2026-02-17T15:01:16.115534-03:00
rendered_js: false
word_count: 114
summary: This document provides an overview of Moodle's Tag API, detailing how to create, modify, and search labels for information across the system through core classes and specific PHP files.
tags:
    - moodle-development
    - tag-api
    - metadata-management
    - php-library
    - labeling-system
category: api
---

## [Tag API](https://moodledev.io/docs/4.4/apis/subsystems/tag)

The Tag API allows you to assign labels to information in Moodle. This makes finding this information easier and also facilitates the grouping of similar information. The Tag API allows you to create, modify, delete and search tags in the Moodle system. The main tag related functions can be found in the tag/classes/tag.php file. For a thorough overview of all of the functions available for working with Tags please see methods in coretagtag, coretagcollection and coretagarea classes, however, the following examples should give you a general understanding of how to get started with tags.

## [tag.php](https://moodledev.io/docs/4.4/apis/commonfiles/tag.php)

A description of the library tag.php file, describing what plugins have tags where their callbacks are located.