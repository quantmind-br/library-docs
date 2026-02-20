---
title: 17 docs tagged with "Plugins" | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/tags/plugins
source: sitemap
fetched_at: 2026-02-17T14:53:36.633564-03:00
rendered_js: false
word_count: 443
summary: This document provides a directory and brief descriptions of various Moodle 4.1 core APIs, plugin types, and common system files used for platform development and extension.
tags:
    - moodle-development
    - plugin-architecture
    - core-apis
    - backend-framework
    - moodle-4-1
    - extension-points
category: reference
---

## [Advanced grading API](https://moodledev.io/docs/4.1/apis/core/grading)

Advanced grading was introduced in Moodle 2.2 for grading of assignments. It is intended to be used for grading of other types of activities in the later versions.

## [Antivirus plugins](https://moodledev.io/docs/4.1/apis/plugintypes/antivirus)

Integrate your preferred Antivirus tool to with Moodle to automatically check new file uploads.

## [Block plugins](https://moodledev.io/docs/4.1/apis/plugintypes/blocks)

Block plugins allow you to show supplemental information, and features, within different parts of Moodle.

## [Common files](https://moodledev.io/docs/4.1/apis/commonfiles)

This page describes the common files which may be present in any Moodle subsystem or plugin type. Some of these files are mandatory and must exist within a component, whilst others are optional.

## [Course format](https://moodledev.io/docs/4.1/apis/plugintypes/format)

Course formats are plugins that determine the layout of course resources.

## [db/tasks.php](https://moodledev.io/docs/4.1/apis/commonfiles/db-tasks.php)

A description of the plugin scheduled task configuration file

## [Enrolment plugins](https://moodledev.io/docs/4.1/apis/plugintypes/enrol)

Moodle provides a number of ways of managing course enrolment, called enrolment plugins. Each course can decide its enabled enrolment plugins instances and any enrolment plugin can define a workflow the user must follow in order to enrol in the course.

## [Filter plugins](https://moodledev.io/docs/4.1/apis/plugintypes/filter)

Filters are a way to automatically transform content before it is output. Filters may be used to:

## [Local plugins](https://moodledev.io/docs/4.1/apis/plugintypes/local)

The recommended way to add new functionality to Moodle is to create a new standard plugin (for example, activity, block, authentication, enrol). The local plugin-type is mostly suitable for things that do not fit into these standard plugin types.

## [Migrating 3.11 formats](https://moodledev.io/docs/4.1/apis/plugintypes/format/migration)

The new course editor introduced in Moodle 4.0 reimplements most of the previous webservices, AMD modules, and internal logic of the course rendering. However, all formats since 3.11 will use the previous libraries by default until its final deprecation in Moodle 4.3. This document collects the main adaptations any 3.11 course format will require to continue working when this happens.

## [Plugin types](https://moodledev.io/docs/4.1/apis/plugintypes)

Moodle is a powerful, and very extensible, Learning Management System. One of its core tenets is its extensibility, and this is primarily achieved through the development of plugins.

## [Plugin Upgrades](https://moodledev.io/docs/4.1/guides/upgrade)

The Upgrade API is a core API which allows your plugin to manage features of its own installation, and upgrade. Every plugin includes a version which allows the Upgrade API to apply only the required changes.

## [Question Bank plugins](https://moodledev.io/docs/4.1/apis/plugintypes/qbank)

Question type plugins allow you to extend the functionality of the Moodle Question bank.

## [Repository plugins](https://moodledev.io/docs/4.1/apis/plugintypes/repository)

Repository plugin allow Moodle to bring contents into Moodle from external repositories.

## [tag.php](https://moodledev.io/docs/4.1/apis/commonfiles/tag.php)

A description of the library tag.php file, describing what plugins have tags where their callbacks are located.

## [version.php](https://moodledev.io/docs/4.1/apis/commonfiles/version.php)

A description of the plugin version.php file, describing the various features

## [Writing a new service](https://moodledev.io/docs/4.1/apis/subsystems/external/writing-a-service)

This documentation covers the creation of a new external service for use in a web service of a fictional local plugin, local\_groupmanager.