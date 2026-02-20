---
title: 14 docs tagged with "core" | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/tags/core
source: sitemap
fetched_at: 2026-02-17T14:58:22.035836-03:00
rendered_js: false
word_count: 474
summary: This document provides an overview and index of core Moodle developer APIs, focusing primarily on the Form API for interface elements and the Data Manipulation Language (DML) API for database interactions. It outlines essential tools for form creation, data handling, and plugin development within the Moodle ecosystem.
tags:
    - moodle-development
    - core-apis
    - form-api
    - dml-api
    - database-management
    - plugin-architecture
    - web-development
category: api
---

## [Advanced elements](https://moodledev.io/docs/4.4/apis/subsystems/form/advanced/advanced-elements)

Form elements can be marked as 'advanced'. This has the effect that they are hidden initially.

## [Checkbox controller](https://moodledev.io/docs/4.4/apis/subsystems/form/advanced/checkbox-controller)

The checkbox controller allows developers to group checkboxes together and add a link or button to check, or uncheck, all of the checkboxes at once.

## [Core APIs](https://moodledev.io/docs/4.4/apis/core)

Moodle provides a series of Core APIs which can be used by any part of Moodle.

## [Data definition API](https://moodledev.io/docs/4.4/apis/core/dml/ddl)

In this page you'll access to the available functions under Moodle to be able to handle DB structures (tables, fields, indexes...).

## [Data manipulation API](https://moodledev.io/docs/4.4/apis/core/dml)

This page describes the functions available to access data in the Moodle database. You should exclusively use these functions in order to retrieve or modify database content because these functions provide a high level of abstraction and guarantee that your database manipulation will work against different RDBMSes.

## [DML drivers](https://moodledev.io/docs/4.4/apis/core/dml/drivers)

A number of native drivers are included with Moodle, including those with support for:

## [DML exceptions](https://moodledev.io/docs/4.4/apis/core/dml/exceptions)

The DML API uses a selection of exceptions to indicate errors.

## [Form Usage](https://moodledev.io/docs/4.4/apis/subsystems/form/usage)

Moodle's Form API is an extension of the Pear HTMLQuickForm API, which is no longer supported. Some documentation for the upstream library is available in the PEAR package page, including a short tutorial. A longer tutorial is also available, courtesy of the Internet Archive.

## [Forms API](https://moodledev.io/docs/4.4/apis/subsystems/form)

Form are created using the Form API. The Form API supports most standard HTML elements, including checkboxes, radio buttons, text boxes, and so on, adding additional accessibility and security features to them.

## [Hooks API](https://moodledev.io/docs/4.4/apis/core/hooks)

This page describes the Hooks API which is a replacement for some of the lib.php based one-to-many

## [No submit button](https://moodledev.io/docs/4.4/apis/subsystems/form/advanced/no-submit-button)

The moodleform 'nosubmitbutton\_pressed()' method allows you to detect if a button on your form has been pressed that is a submit button but that has been defined as a button that doesn't result in a processing of all the form data but will result in some form 'sub action' and then having the form redisplayed. This is useful for example to have an 'Add' button to add some option to a select box in the form etc. You define a button as a no submit button as in the example below (in definition()). This example adds a text box and a submit button in a group.

## [Plugin types](https://moodledev.io/docs/4.4/apis/plugintypes)

Moodle is a powerful, and very extensible, Learning Management System. One of its core tenets is its extensibility, and this is primarily achieved through the development of plugins.

## [Repeat elements](https://moodledev.io/docs/4.4/apis/subsystems/form/advanced/repeat-elements)

The Form API includes the ability to repeat a group of form elements. This is useful where you need to have an unknown quantity of item data, for example possible answers in a quiz question.

## [Transactions](https://moodledev.io/docs/4.4/apis/core/dml/delegated-transactions)

Moodle allows data manipulation to take place within a database transaction, known as a Delegated transaction. This allows you to perform CRUD operations, and roll them back if a failure takes place.