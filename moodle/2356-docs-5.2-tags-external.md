---
title: 8 docs tagged with "external" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/external
source: sitemap
fetched_at: 2026-02-17T15:39:49.731974-03:00
rendered_js: false
word_count: 149
summary: This document provides an overview of Moodle's web service framework, detailing how to declare, define, secure, and test external functions for integration with external systems.
tags:
    - moodle-api
    - web-services
    - external-functions
    - api-security
    - unit-testing
    - file-handling
category: api
---

## [External Services](https://moodledev.io/docs/5.2/apis/subsystems/external)

Moodle has a full-featured Web Service framework, allowing you to use and create web services for use in external systems.

## [File handling](https://moodledev.io/docs/5.2/apis/subsystems/external/files)

Moodle provides two ways to fetch and upload files:

## [Function Declarations](https://moodledev.io/docs/5.2/apis/subsystems/external/description)

Before they can be used, all functions must be declared to Moodle, and their inputs and outputs must be defined.

## [Function Definitions](https://moodledev.io/docs/5.2/apis/subsystems/external/functions)

An External function definition is the class, and collection of functions, used to define:

## [Security](https://moodledev.io/docs/5.2/apis/subsystems/external/security)

Before operating on any data in an external function, you must ensure that the user:

## [Service creation](https://moodledev.io/docs/5.2/apis/subsystems/external/advanced/custom-services)

Moodle comes with two built-in services that your functions can be attached to.

## [Unit Testing](https://moodledev.io/docs/5.2/apis/subsystems/external/testing)

Unit tests are the best way of checking the behaviour of your external services and can help you to:

## [Writing a new service](https://moodledev.io/docs/5.2/apis/subsystems/external/writing-a-service)

This documentation covers the creation of a new external service for use in a web service of a fictional local plugin, local\_groupmanager.