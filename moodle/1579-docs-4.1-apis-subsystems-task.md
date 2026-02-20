---
title: Task API | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/subsystems/task
source: sitemap
fetched_at: 2026-02-17T14:56:57.987026-03:00
rendered_js: false
word_count: 859
summary: This document provides an overview of the Moodle Tasks API, explaining how to implement and manage scheduled and adhoc background tasks. it covers key technical considerations including error handling, caching, security, and the transition from legacy cron systems.
tags:
    - moodle-api
    - scheduled-tasks
    - adhoc-tasks
    - background-processing
    - cron-jobs
    - error-handling
category: api
---

The Moodle Tasks API is a comprehensive API to support the scheduling and running of tasks. Tasks are individual activities which are to be performed, and come in two primary forms:

- Scheduled tasks - tasks which run regularly and according to a schedule set by the administrator, with the same configuration each time; and
- Adhoc tasks - tasks which are queued by developers, capable of having multiple concurrent executions, and with individual configuration.

Good uses for tasks include:

- running a slow operation in the background
- running a maintenance task on a regular schedule

In general any operation that takes more than a few seconds might be a candidate for a task.

## Benefits[​](#benefits "Direct link to Benefits")

- Better user experience (give the user feedback immediately, that their task has been queued)
- Prevent browser timeouts
- Better performance for clusters (tasks can be run on separate, non-user-facing cluster nodes, tasks can run in parallel)
- Failed tasks will be retried
- A better user interface will prevent users queuing multiple tasks, because they thought it had "got stuck".

note

Tasks will only run as often as cron is run in Moodle. It is recommended that cron be run at least once per minute to get the most benefit from the task scheduling.

## Types of task[​](#types-of-task "Direct link to Types of task")

### Scheduled tasks[​](#scheduled-tasks "Direct link to Scheduled tasks")

Scheduled tasks are tasks that will run on a regular schedule. A default schedule can be set, but administrators have the ability to change the default schedule if required.

See the [scheduled tasks](https://moodledev.io/docs/4.1/apis/subsystems/task/scheduled) page for more information on creating scheduled tasks.

### Adhoc tasks[​](#adhoc-tasks "Direct link to Adhoc tasks")

Adhoc tasks are typically used when you need to queue something to run in the background either immediately, where they would be executed as soon as possible, or as a one-off task at some future point in time.

Each adhoc task can be called multiple times, with each having its own custom data, and the ability to run as a different user.

Adhoc tasks are great for situations such as:

- perform a pre-configured backup
- migrate large quantities of data between different formats
- send forum posts as an e-mail

## Usage[​](#usage "Direct link to Usage")

### Failures[​](#failures "Direct link to Failures")

A task, either scheduled or adhoc, can sometimes fail. An example would be updating an RSS field when the network is temporarily down. This is handled by the task system automatically - all the failing task needs to do is throw an exception. The task will be retried after 1 minute. If the task keeps failing, the retry algorithm will add more time between each successive attempts up to a max of 24 hours.

### Caches[​](#caches "Direct link to Caches")

Historically many Moodle APIs have used static caches. Whilst many of these have been replaced by the [Moodle Universal Cache](https://docs.moodle.org/dev/Cache_API), which can be cleared between runs, it is not possible to guarantee that this is always the case.

When working with long-running tasks, you may need to consider caching - this applies to both scheduled, and adhoc, tasks. This is particularly true for tasks related to enrolment.

After a long-running task completes, the next task in the queue may suffer because various API's in moodle use static caching to speed up requests, but assume that the data will not change much between the start and end of the request. In this case, you can force the task runner to exit after completing a task that has performed many changes. The next task run will take place shortly after, and will have all static caches cleared because it takes place in a new process.

You can enable this behaviour by making a call to `\core\task\manager::clear_static_caches()` at the end of your task.

### Security[​](#security "Direct link to Security")

When scheduling a task to run in the background, or creating a scheduled task, the task will run as the cron user (see `cron_setup_user()`). If you need to perform access checks in your background task, you should do so as the user that the checks relate to.

In the case of an adhoc task, you can call the [`set_userid`](https://moodledev.io/docs/4.1/apis/subsystems/task/adhoc#running-as-a-specific-user) function when queueing the task.

For scheduled tasks you should either pass the ID of the user to the `require_capability()` function, or use the `cron_setup_user()` function to switch to that user.

### Legacy cron[​](#legacy-cron "Direct link to Legacy cron")

The older syntax of cron.php or modname\_cron() is still supported, and will be removed in the near future. This is because:

- the legacy cron functions run serially - a long running cron in one plugin will hold up the other plugins crons
- the legacy cron functions are fragile - a failure in one cron in one plugin will prevent the cron in other functions from running at all
- the scheduling cannot be changed by administrators

### Generating output[​](#generating-output "Direct link to Generating output")

Since Moodle 3.5 it is safe to use the [Output API](https://moodledev.io/docs/4.1/apis/subsystems/output) in cron tasks. Prior to this there may be cases where the Output API has not been initialised.

In order to improve debugging information, it is good practice to call `mtrace` to log what's going on within a task execution:

```
classmy_taskextends\core\task\scheduled_task{
publicfunctionexecute(){
mtrace("My task started");

// Do some work.

mtrace("My task finished");
}
}
```

## For Administrators[​](#for-administrators "Direct link to For Administrators")

Several tools exist for administrators:

- The task log viewer allows administrators to view logs from both adhoc and scheduled task runs
- The scheduled task manager allows administrators to configure the time schedule for tasks
- The 'Tasks running now' tool allows administrators to view key details of any task currently running