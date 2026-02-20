---
title: 7 docs tagged with "Web Services" | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/tags/web-services
source: sitemap
fetched_at: 2026-02-17T15:10:32.75589-03:00
rendered_js: false
word_count: 127
summary: This document provides an overview of Moodle's external services API, covering function declarations, security requirements, and the creation of web services. It guides developers through the lifecycle of external functions, from definition and file handling to unit testing and service implementation.
tags:
    - moodle-development
    - external-services
    - web-services
    - api-integration
    - file-handling
    - security-protocols
    - unit-testing
category: api
---

## [File handling](https://moodledev.io/docs/4.5/apis/subsystems/external/files)

Moodle provides two ways to fetch and upload files:

## [Function Declarations](https://moodledev.io/docs/4.5/apis/subsystems/external/description)

Before they can be used, all functions must be declared to Moodle, and their inputs and outputs must be defined.

## [Function Definitions](https://moodledev.io/docs/4.5/apis/subsystems/external/functions)

An External function definition is the class, and collection of functions, used to define:

## [Security](https://moodledev.io/docs/4.5/apis/subsystems/external/security)

Before operating on any data in an external function, you must ensure that the user:

## [Service creation](https://moodledev.io/docs/4.5/apis/subsystems/external/advanced/custom-services)

Moodle comes with two built-in services that your functions can be attached to.

## [Unit Testing](https://moodledev.io/docs/4.5/apis/subsystems/external/testing)

Unit tests are the best way of checking the behaviour of your external services and can help you to:

## [Writing a new service](https://moodledev.io/docs/4.5/apis/subsystems/external/writing-a-service)

This documentation covers the creation of a new external service for use in a web service of a fictional local plugin, local\_groupmanager.