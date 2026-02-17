---
title: Adhoc tasks | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/subsystems/task/adhoc
source: sitemap
fetched_at: 2026-02-17T14:56:59.543977-03:00
rendered_js: false
word_count: 578
summary: This document explains how to create, queue, and manage adhoc background tasks for asynchronous processing, including setting custom data and execution times. It details how to extend the base task class and utilize the task manager for features like duplicate detection and rescheduling.
tags:
    - adhoc-tasks
    - background-processing
    - task-management
    - asynchronous-execution
    - queue-management
    - php-development
category: guide
---

Adhoc tasks are typically used when you need to queue something to run in the background either immediately, where they would be executed as soon as possible, or as a one-off task at some future point in time.

Each adhoc task can be called multiple times, with each having its own custom data, and the ability to run as a different user.

Adhoc tasks are great for situations such as:

- perform a pre-configured backup
- migrate large quantities of data between different formats
- send forum posts as an e-mail

## Creating adhoc tasks[​](#creating-adhoc-tasks "Direct link to Creating adhoc tasks")

To create a new adhoc task you should:

1. create a new class which extends the `\core\task\adhoc_task` class;
2. queue the task

### Task class[​](#task-class "Direct link to Task class")

The class for your scheduled task, which extends the `\core\task\scheduled_task` class, should be in the `classes/task` directory of your plugin.

View example adhoc task

```
namespacemod_example\task;

/**
 * An example of a adhoc task.
 */
classdo_somethingextends\core\task\adhoc_task{

/**
     * Execute the task.
     */
publicfunctionexecute(){
// Call your own api
}
}
```

### Queueing the task for execution[​](#queueing-the-task-for-execution "Direct link to Queueing the task for execution")

The processing of adhoc tasks is handled by the task manager. Typically you will instantiate a copy of your class, setting any relevant data, and then use the manager to queue the task, for example:

```
// Create the instance
$mytask=new\mod_example\task\do_something();

// Run this task as a specific user:
$mytask->set_userid($someuser->id);

// Set some custom data.
// Note: This data must be serialiable.
$mytask->set_custom_data([
'documentation'=>'present',
'correct'=>true,
])

// Queue the task.
\core\task\manager::queue_adhoc_task($mytask);
```

### Task features[​](#task-features "Direct link to Task features")

Adhoc tasks include a number of useful features which are important to be aware of.

#### Running as a specific user[​](#running-as-a-specific-user "Direct link to Running as a specific user")

Unless otherwise specified, all tasks will run as the CLI admin user. This is often undesirable and, where relevant, you should specify a userid to run the task as.

```
// Run this task as a specific user:
$mytask->set_userid($someuser->id);
```

#### Set a task to run at a future time[​](#set-a-task-to-run-at-a-future-time "Direct link to Set a task to run at a future time")

You may need to plan to run a task at a future time - for example you may queue a forum digest task to run at a particular time. This can be accomplished using the `set_next_run_time()` function before queueing the task, for example:

```
$task=newmy_future_task();
$task->set_next_run_time($futuretime);
\core\task\manager::queue_adhoc_task($task);
```

note

The `set_next_run_time()` function takes a unix time stamp. Tasks are not *guaranteed* to run at a specific time, but they will not be run *before* that time.

#### Ignore duplicate adhoc tasks[​](#ignore-duplicate-adhoc-tasks "Direct link to Ignore duplicate adhoc tasks")

In some situations you may only wish to queue an adhoc task if an identical adhoc task does not already exist. This can be useful in situations where you are adding a set of items to a bucket for later processing and only wish to process all items once.

When requested, the `queue_adhoc_task()` function will ignore any task where all of the following match an existing task in the queue:

- `classname` - the class defining the task to be processed
- `component` - the component that the task belongs
- `customdata` - any custom data for this instance
- `userid` - the user that the task will be run as

Duplicate adhoc task detection can be enabled by passing a truthy value as the second argument to `queue_adhoc_task()`, for example:

```
\core\task\manager::queue_adhoc_task($task,true);
```

Custom data

If creating tasks which will contain a subset of data which will also be run by another instance of the same task type, you should put the data into a database table rather than the task custom data.

#### Rescheduling an adhoc task[​](#rescheduling-an-adhoc-task "Direct link to Rescheduling an adhoc task")

Similar to [ignoring duplicate adhoc tasks](#ignore-duplicate-adhoc-tasks) there are situations which require you re\_schedule_ a matching task instead. This may happen, for example, in a situation where there is too much churn of your source data.

The `reschedule_or_queue_adhoc_task()` function will locate any existing task matching the following fields, and update its time with the time from the new entry:

- `classname` - the class defining the task to be processed
- `component` - the component that the task belongs
- `customdata` - any custom data for this instance
- `userid` - the user that the task will be run as

```
\core\task\manager::reschedule_or_queue_adhoc_task($task);
```