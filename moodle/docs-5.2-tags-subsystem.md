---
title: 9 docs tagged with "Subsystem" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/subsystem
source: sitemap
fetched_at: 2026-02-17T15:42:19.776506-03:00
rendered_js: false
word_count: 328
summary: This document provides an overview of various core Moodle developer APIs and subsystems, including task management, caching, backup and restore, and user groups. It serves as a central reference for developers to understand the different components available for extending Moodle functionality.
tags:
    - moodle-development
    - api-reference
    - moodle-subsystems
    - task-api
    - backup-and-restore
    - cache-api
    - moodle-core
category: api
---

## [Adhoc tasks](https://moodledev.io/docs/5.2/apis/subsystems/task/adhoc)

Adhoc tasks are typically used when you need to queue something to run in the background either immediately, where they would be executed as soon as possible, or as a one-off task at some future point in time.

## [Backup API](https://moodledev.io/docs/5.2/apis/subsystems/backup)

The Backup API provides a way to include your plugin's in the course backup. See Restore API for the part that takes care of restoring data.

## [Cache API](https://moodledev.io/docs/5.2/apis/subsystems/muc)

This document provides an in-depth overview of the Cache API, also known as MUC (Moodle Universal Cache), a fundamental caching system within Moodle.

## [Common files](https://moodledev.io/docs/5.2/apis/commonfiles)

This page describes the common files which may be present in any Moodle subsystem or plugin type. Some of these files are mandatory and must exist within a component, whilst others are optional.

## [Groups API](https://moodledev.io/docs/5.2/apis/subsystems/group)

Moodle Groups are a way of expressing collections of users within a course. They may be defined by the teacher in the course participants page, or created automatically during a bulk user upload (for example, from a text file).

## [Questions API](https://moodledev.io/docs/5.2/apis/subsystems/question)

The question subsystem in Moodle manages the creation, editing and management of interactive questions, and then enables those questions to be presented to users so they can be attempted. It is useful to consider these as separate subcomponents.

## [Restore API](https://moodledev.io/docs/5.2/apis/subsystems/backup/restore)

The Restore API provides a way to restore your plugin's data from a backup file created in Moodle 2.0 or later. For the information on how backup files are created, see Backup API. For the information on how to support restoring data from backup files created in Moodle 1.x, see Backup conversion API.

## [Scheduled tasks](https://moodledev.io/docs/5.2/apis/subsystems/task/scheduled)

Scheduled tasks are tasks that will run on a regular schedule. A default schedule can be set, but administrators have the ability to change the default schedule if required.

## [Task API](https://moodledev.io/docs/5.2/apis/subsystems/task)

The Moodle Tasks API is a comprehensive API to support the scheduling and running of tasks. Tasks are individual activities which are to be performed, and come in two primary forms: