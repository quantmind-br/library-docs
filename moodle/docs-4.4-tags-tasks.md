---
title: 3 docs tagged with "Tasks" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/tasks
source: sitemap
fetched_at: 2026-02-17T15:01:19.293-03:00
rendered_js: false
word_count: 104
summary: This document introduces the Moodle Tasks API, detailing the differences between adhoc tasks for immediate or one-off background processing and scheduled tasks for regular execution.
tags:
    - moodle-development
    - task-api
    - adhoc-tasks
    - scheduled-tasks
    - background-processing
category: concept
---

## [Adhoc tasks](https://moodledev.io/docs/4.4/apis/subsystems/task/adhoc)

Adhoc tasks are typically used when you need to queue something to run in the background either immediately, where they would be executed as soon as possible, or as a one-off task at some future point in time.

## [Scheduled tasks](https://moodledev.io/docs/4.4/apis/subsystems/task/scheduled)

Scheduled tasks are tasks that will run on a regular schedule. A default schedule can be set, but administrators have the ability to change the default schedule if required.

## [Task API](https://moodledev.io/docs/4.4/apis/subsystems/task)

The Moodle Tasks API is a comprehensive API to support the scheduling and running of tasks. Tasks are individual activities which are to be performed, and come in two primary forms: