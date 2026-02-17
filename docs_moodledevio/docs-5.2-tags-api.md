---
title: 49 docs tagged with "API" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/api
source: sitemap
fetched_at: 2026-02-17T15:38:23.863978-03:00
rendered_js: false
word_count: 1401
summary: This document provides a comprehensive index and brief descriptions of the core APIs, subsystems, and plugin types available for Moodle development. It serves as a central reference point for understanding the various programmatic interfaces used to extend Moodle's functionality.
tags:
    - moodle-development
    - core-api
    - plugin-architecture
    - developer-reference
    - moodle-backend
    - system-extensibility
category: reference
---

## [Activity completion API](https://moodledev.io/docs/5.2/apis/core/activitycompletion)

There are changes to the completion API introduced in Moodle 3.11 to be incorporated to this page. Please refer to Student activity completion for details.

## [Activity modules](https://moodledev.io/docs/5.2/apis/plugintypes/mod)

Activity modules are a fundamental course feature and are usually the primary delivery method for learning content in Moodle.

## [Adhoc tasks](https://moodledev.io/docs/5.2/apis/subsystems/task/adhoc)

Adhoc tasks are typically used when you need to queue something to run in the background either immediately, where they would be executed as soon as possible, or as a one-off task at some future point in time.

## [Analytics API](https://moodledev.io/docs/5.2/apis/subsystems/analytics)

The Analytics API allows managers to use predictions to detect trends and predict student behaviour

## [Backup API](https://moodledev.io/docs/5.2/apis/subsystems/backup)

The Backup API provides a way to include your plugin's in the course backup. See Restore API for the part that takes care of restoring data.

## [Badges API](https://moodledev.io/docs/5.2/apis/subsystems/badges)

The Moodle Badges API facilitates the creation and management of site and course-specific badges, enabling their export to external Open Badges compliant platforms, often referred to as "backpacks".

## [Cache API](https://moodledev.io/docs/5.2/apis/subsystems/muc)

This document provides an in-depth overview of the Cache API, also known as MUC (Moodle Universal Cache), a fundamental caching system within Moodle.

## [Check API](https://moodledev.io/docs/5.2/apis/subsystems/check)

A Check is a runtime test to make sure that something is working well. You can think of Checks as similar and complimentary to the PHPUnit and Acceptance testing but the next layer around them, and performed at run time rather than development, or build time.

## [Common files](https://moodledev.io/docs/5.2/apis/commonfiles)

This page describes the common files which may be present in any Moodle subsystem or plugin type. Some of these files are mandatory and must exist within a component, whilst others are optional.

## [Core APIs](https://moodledev.io/docs/5.2/apis/core)

Moodle provides a series of Core APIs which can be used by any part of Moodle.

## [Course overview integration](https://moodledev.io/docs/5.2/apis/plugintypes/mod/courseoverview)

Summary

## [Data definition API](https://moodledev.io/docs/5.2/apis/core/dml/ddl)

In this page you'll access to the available functions under Moodle to be able to handle DB structures (tables, fields, indexes...).

## [Data manipulation API](https://moodledev.io/docs/5.2/apis/core/dml)

This page describes the functions available to access data in the Moodle database. You should exclusively use these functions in order to retrieve or modify database content because these functions provide a high level of abstraction and guarantee that your database manipulation will work against different RDBMSes.

## [DML drivers](https://moodledev.io/docs/5.2/apis/core/dml/drivers)

A number of native drivers are included with Moodle, including those with support for:

## [DML exceptions](https://moodledev.io/docs/5.2/apis/core/dml/exceptions)

The DML API uses a selection of exceptions to indicate errors.

## [External Services](https://moodledev.io/docs/5.2/apis/subsystems/external)

Moodle has a full-featured Web Service framework, allowing you to use and create web services for use in external systems.

## [Favourites API](https://moodledev.io/docs/5.2/apis/subsystems/favourites)

Overview

## [File Converters](https://moodledev.io/docs/5.2/apis/plugintypes/fileconverter)

File converters are an important tool to support other plugins with file conversion supported between a wide range of file formats. File converters are accessed using the File conversion API and are typically consumed by other plugins rather than by the user directly.

## [File Converters](https://moodledev.io/docs/5.2/apis/subsystems/files/converter)

Users are able to submit a wide range of files, and it is a common requirement to convert these to alternative formats.

## [Form Usage](https://moodledev.io/docs/5.2/apis/subsystems/form/usage)

Moodle's Form API is an extension of the Pear HTMLQuickForm API, which is no longer supported. Some documentation for the upstream library is available in the PEAR package page, including a short tutorial. A longer tutorial is also available, courtesy of the Internet Archive.

## [Forms API](https://moodledev.io/docs/5.2/apis/subsystems/form)

Form are created using the Form API. The Form API supports most standard HTML elements, including checkboxes, radio buttons, text boxes, and so on, adding additional accessibility and security features to them.

## [Function Declarations](https://moodledev.io/docs/5.2/apis/subsystems/external/description)

Before they can be used, all functions must be declared to Moodle, and their inputs and outputs must be defined.

## [Function Definitions](https://moodledev.io/docs/5.2/apis/subsystems/external/functions)

An External function definition is the class, and collection of functions, used to define:

## [Groups API](https://moodledev.io/docs/5.2/apis/subsystems/group)

Moodle Groups are a way of expressing collections of users within a course. They may be defined by the teacher in the course participants page, or created automatically during a bulk user upload (for example, from a text file).

## [Hooks API](https://moodledev.io/docs/5.2/apis/core/hooks)

This page describes the Hooks API which is a replacement for some of the lib.php based one-to-many

## [HTML Writer API](https://moodledev.io/docs/5.2/apis/core/htmlwriter)

Moodle has a class called HTML writer which allows you to output basic HTML tags. This is typically used within renderer functions, for example question/type/pluginname/renderer.php.

## [Lock API](https://moodledev.io/docs/5.2/apis/core/lock)

Locking is required whenever you need to prevent two, or more, processes accessing the same resource at the same time. The prime candidate for locking in Moodle is cron. Locking allows multiple cron processes to work on different parts of cron at the same time with no risk that they will conflict (work on the same job at the same time).

## [Machine learning backends](https://moodledev.io/docs/5.2/apis/plugintypes/mlbackend)

Machine learning backends process the datasets generated from the indicators and targets calculated by the Analytics API. They are used for machine learning training, prediction and models evaluation.

## [Message API](https://moodledev.io/docs/5.2/apis/core/message)

What is this document?

## [Module visibility and display](https://moodledev.io/docs/5.2/apis/plugintypes/mod/visibility)

Summary

## [Navigation API](https://moodledev.io/docs/5.2/apis/core/navigation)

The Navigation API allows for the manipulation of the navigation system used in Moodle.

## [Output API](https://moodledev.io/docs/5.2/apis/subsystems/output)

The Output API is responsible for visual aspects of Moodle content. This page explains how renderers, renderables, themes and templates all work together.

## [Plagiarism API](https://moodledev.io/docs/5.2/apis/subsystems/plagiarism)

Overview

## [Plugin types](https://moodledev.io/docs/5.2/apis/plugintypes)

Moodle is a powerful, and very extensible, Learning Management System. One of its core tenets is its extensibility, and this is primarily achieved through the development of plugins.

## [Plugin Upgrades](https://moodledev.io/docs/5.2/guides/upgrade)

The Upgrade API is a core API which allows your plugin to manage features of its own installation, and upgrade. Every plugin includes a version which allows the Upgrade API to apply only the required changes.

## [Preference API](https://moodledev.io/docs/5.2/apis/core/preference)

The Preference API is used for the storage and retrieval of user preferences. These preferences are stored in the database for users with an account, however for guests or users who are not currently logged in the preferences are stored in the Session.

## [Privacy API](https://moodledev.io/docs/5.2/apis/subsystems/privacy)

The General Data Protection Regulation (GDPR) is an EU directive that provides users with more control over their data and how it is processed. This regulation came into effect on 25th of May 2018 and covers any citizen or permanent resident of the European Union. The directive is respected by a number of other countries outside of the European Union.

## [Questions API](https://moodledev.io/docs/5.2/apis/subsystems/question)

The question subsystem in Moodle manages the creation, editing and management of interactive questions, and then enables those questions to be presented to users so they can be attempted. It is useful to consider these as separate subcomponents.

## [Restore API](https://moodledev.io/docs/5.2/apis/subsystems/backup/restore)

The Restore API provides a way to restore your plugin's data from a backup file created in Moodle 2.0 or later. For the information on how backup files are created, see Backup API. For the information on how to support restoring data from backup files created in Moodle 1.x, see Backup conversion API.

## [Scheduled tasks](https://moodledev.io/docs/5.2/apis/subsystems/task/scheduled)

Scheduled tasks are tasks that will run on a regular schedule. A default schedule can be set, but administrators have the ability to change the default schedule if required.

## [Security](https://moodledev.io/docs/5.2/apis/subsystems/external/security)

Before operating on any data in an external function, you must ensure that the user:

## [Service creation](https://moodledev.io/docs/5.2/apis/subsystems/external/advanced/custom-services)

Moodle comes with two built-in services that your functions can be attached to.

## [Tag API](https://moodledev.io/docs/5.2/apis/subsystems/tag)

The Tag API allows you to assign labels to information in Moodle. This makes finding this information easier and also facilitates the grouping of similar information. The Tag API allows you to create, modify, delete and search tags in the Moodle system. The main tag related functions can be found in the tag/classes/tag.php file. For a thorough overview of all of the functions available for working with Tags please see methods in coretagtag, coretagcollection and coretagarea classes, however, the following examples should give you a general understanding of how to get started with tags.

## [tag.php](https://moodledev.io/docs/5.2/apis/commonfiles/tag.php)

A description of the library tag.php file, describing what plugins have tags where their callbacks are located.

## [Task API](https://moodledev.io/docs/5.2/apis/subsystems/task)

The Moodle Tasks API is a comprehensive API to support the scheduling and running of tasks. Tasks are individual activities which are to be performed, and come in two primary forms:

## [Time API](https://moodledev.io/docs/5.2/apis/subsystems/time)

Internally Moodle always stores all times in unixtime format, which is a format independent of timezones.

## [Transactions](https://moodledev.io/docs/5.2/apis/core/dml/delegated-transactions)

Moodle allows data manipulation to take place within a database transaction, known as a Delegated transaction. This allows you to perform CRUD operations, and roll them back if a failure takes place.

## [Unit Testing](https://moodledev.io/docs/5.2/apis/subsystems/external/testing)

Unit tests are the best way of checking the behaviour of your external services and can help you to:

## [xAPI (Experience API)](https://moodledev.io/docs/5.2/apis/subsystems/xapi)

Overview