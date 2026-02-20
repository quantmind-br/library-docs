---
title: 26 docs tagged with "Plugins" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/plugins
source: sitemap
fetched_at: 2026-02-17T15:00:34.955496-03:00
rendered_js: false
word_count: 719
summary: This document provides an overview and index of Moodle 4.4 APIs, plugin types, and common configuration files used to extend the platform's functionality.
tags:
    - moodle-development
    - plugin-architecture
    - moodle-api
    - core-apis
    - extension-points
    - moodle-4-4
category: reference
---

## [Advanced grading API](https://moodledev.io/docs/4.4/apis/core/grading)

Advanced grading was introduced in Moodle 2.2 for grading of assignments. It is intended to be used for grading of other types of activities in the later versions.

## [Antivirus plugins](https://moodledev.io/docs/4.4/apis/plugintypes/antivirus)

Integrate your preferred Antivirus tool to with Moodle to automatically check new file uploads.

## [Block plugins](https://moodledev.io/docs/4.4/apis/plugintypes/blocks)

Block plugins allow you to show supplemental information, and features, within different parts of Moodle.

## [Common files](https://moodledev.io/docs/4.4/apis/commonfiles)

This page describes the common files which may be present in any Moodle subsystem or plugin type. Some of these files are mandatory and must exist within a component, whilst others are optional.

## [Course format](https://moodledev.io/docs/4.4/apis/plugintypes/format)

Course formats are plugins that determine the layout of course resources.

## [db/tasks.php](https://moodledev.io/docs/4.4/apis/commonfiles/db-tasks.php)

A description of the plugin scheduled task configuration file

## [Defaults for new questions](https://moodledev.io/docs/4.4/apis/plugintypes/qtype/newquestiondefaults)

A way for question types to remember a user's preferred settings for creating questions of a given type.

## [Enrolment plugins](https://moodledev.io/docs/4.4/apis/plugintypes/enrol)

Moodle provides a number of ways of managing course enrolment, called enrolment plugins. Each course can decide its enabled enrolment plugins instances and any enrolment plugin can define a workflow the user must follow in order to enrol in the course.

## [Filter plugins](https://moodledev.io/docs/4.4/apis/plugintypes/filter)

Filters are a way to automatically transform content before it is output. Filters may be used to:

## [Fonts](https://moodledev.io/docs/4.4/apis/plugintypes/theme/fonts)

CSS3 standard introduced the possibility to specify custom fonts, see CSS web fonts tutorial.

## [Images and icons in themes](https://moodledev.io/docs/4.4/apis/plugintypes/theme/images)

One of the theme features is the ability to override any of the standard images within Moodle when your theme is in use. At this point, let's explore how to utilize your own images within your theme and how to override the images being used by Moodle.

## [Layout](https://moodledev.io/docs/4.4/apis/plugintypes/theme/layout)

All themes are required to define the layouts they wish to be responsible for as well as create; however, many layout files are required by those layouts. If the theme is overriding another theme then it is a case of deciding which layouts this new theme should override. If the theme is a completely fresh start then you will need to define a layout for each of the different possibilities.

## [Local plugins](https://moodledev.io/docs/4.4/apis/plugintypes/local)

The recommended way to add new functionality to Moodle is to create a new standard plugin (for example, activity, block, authentication, enrol). The local plugin-type is mostly suitable for things that do not fit into these standard plugin types.

## [Message API](https://moodledev.io/docs/4.4/apis/core/message)

What is this document?

## [Migrating 3.11 formats](https://moodledev.io/docs/4.4/apis/plugintypes/format/migration)

The new course editor introduced in Moodle 4.0 reimplements most of the previous webservices, AMD modules, and internal logic of the course rendering. However, all formats since 3.11 will use the previous libraries by default until its final deprecation in Moodle 4.3. This document collects the main adaptations any 3.11 course format will require to continue working when this happens.

## [Plugin types](https://moodledev.io/docs/4.4/apis/plugintypes)

Moodle is a powerful, and very extensible, Learning Management System. One of its core tenets is its extensibility, and this is primarily achieved through the development of plugins.

## [Plugin Upgrades](https://moodledev.io/docs/4.4/guides/upgrade)

The Upgrade API is a core API which allows your plugin to manage features of its own installation, and upgrade. Every plugin includes a version which allows the Upgrade API to apply only the required changes.

## [Question bank filters](https://moodledev.io/docs/4.4/apis/plugintypes/qbank/filters)

Question bank plugins allow you to define new filters for the question bank view and random question sets.

## [Question bank plugins](https://moodledev.io/docs/4.4/apis/plugintypes/qbank)

Question bank plugins allow you to extend the functionality of the Moodle Question bank.

## [Question type plugins](https://moodledev.io/docs/4.4/apis/plugintypes/qtype)

Question type plugins implement the different types of question that the core Question subsystem can handle.

## [Repository plugins](https://moodledev.io/docs/4.4/apis/plugintypes/repository)

Repository plugin allow Moodle to bring contents into Moodle from external repositories.

## [Styles](https://moodledev.io/docs/4.4/apis/plugintypes/theme/styles)

Let's begin by exploring the various locations within Moodle from which CSS can be included:

## [tag.php](https://moodledev.io/docs/4.4/apis/commonfiles/tag.php)

A description of the library tag.php file, describing what plugins have tags where their callbacks are located.

## [Theme plugins](https://moodledev.io/docs/4.4/apis/plugintypes/theme)

A Moodle theme allows users to customize the appearance and functionality of their Moodle site, from overall design to specific activities. Users can create their own themes or modify existing ones, leveraging CSS and JavaScript for customization. The theme architecture ensures smooth fallbacks for minimal changes, fostering flexibility and ease of use.

## [version.php](https://moodledev.io/docs/4.4/apis/commonfiles/version.php)

A description of the plugin version.php file, describing the various features

## [Writing a new service](https://moodledev.io/docs/4.4/apis/subsystems/external/writing-a-service)

This documentation covers the creation of a new external service for use in a web service of a fictional local plugin, local\_groupmanager.