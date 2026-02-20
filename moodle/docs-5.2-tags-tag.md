---
title: One doc tagged with "Tag" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/tag
source: sitemap
fetched_at: 2026-02-17T15:42:20.452302-03:00
rendered_js: false
word_count: 96
summary: This document provides an overview of the Moodle Tag API, explaining how to create, manage, and search labels for organizing platform content. It highlights key classes and file locations necessary for implementing tag functionality within Moodle systems.
tags:
    - moodle
    - tag-api
    - metadata-management
    - subsystem-api
    - labels
category: api
---

## [Tag API](https://moodledev.io/docs/5.2/apis/subsystems/tag)

The Tag API allows you to assign labels to information in Moodle. This makes finding this information easier and also facilitates the grouping of similar information. The Tag API allows you to create, modify, delete and search tags in the Moodle system. The main tag related functions can be found in the tag/classes/tag.php file. For a thorough overview of all of the functions available for working with Tags please see methods in coretagtag, coretagcollection and coretagarea classes, however, the following examples should give you a general understanding of how to get started with tags.