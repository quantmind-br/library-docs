---
title: 7 docs tagged with "Subsystem" | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/tags/subsystem
source: sitemap
fetched_at: 2026-02-17T14:53:57.534091-03:00
rendered_js: false
word_count: 263
summary: This document provides a high-level overview of various Moodle developer APIs and subsystems, including task management, backup and restore procedures, and group handling.
tags:
    - moodle-development
    - task-api
    - backup-api
    - restore-api
    - groups-api
    - subsystems
category: reference
---

## [Adhoc tasks](https://moodledev.io/docs/4.1/apis/subsystems/task/adhoc)

Adhoc tasks are typically used when you need to queue something to run in the background either immediately, where they would be executed as soon as possible, or as a one-off task at some future point in time.

## [Backup API](https://moodledev.io/docs/4.1/apis/subsystems/backup)

The Backup API provides a way to include your plugin's in the course backup. See Restore API for the part that takes care of restoring data.

## [Common files](https://moodledev.io/docs/4.1/apis/commonfiles)

This page describes the common files which may be present in any Moodle subsystem or plugin type. Some of these files are mandatory and must exist within a component, whilst others are optional.

## [Groups API](https://moodledev.io/docs/4.1/apis/subsystems/group)

Moodle Groups are a way of expressing collections of users within a course. They may be defined by the teacher in the course participants page, or created automatically during a bulk user upload (for example, from a text file).

## [Restore API](https://moodledev.io/docs/4.1/apis/subsystems/backup/restore)

The Restore API provides a way to restore your plugin's data from a backup file created in Moodle 2.0 or later. For the information on how backup files are created, see Backup API. For the information on how to support restoring data from backup files created in Moodle 1.x, see Backup conversion API.

## [Scheduled tasks](https://moodledev.io/docs/4.1/apis/subsystems/task/scheduled)

Scheduled tasks are tasks that will run on a regular schedule. A default schedule can be set, but administrators have the ability to change the default schedule if required.

## [Task API](https://moodledev.io/docs/4.1/apis/subsystems/task)

The Moodle Tasks API is a comprehensive API to support the scheduling and running of tasks. Tasks are individual activities which are to be performed, and come in two primary forms: