---
title: 7 docs tagged with "Web Services" | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/tags/web-services
source: sitemap
fetched_at: 2026-02-17T15:33:34.980092-03:00
rendered_js: false
word_count: 127
summary: This document outlines the technical requirements and procedures for implementing external services in Moodle, including function definitions, security, and file handling.
tags:
    - moodle-development
    - external-api
    - web-services
    - api-security
    - function-declaration
    - unit-testing
category: api
---

## [File handling](https://moodledev.io/docs/5.1/apis/subsystems/external/files)

Moodle provides two ways to fetch and upload files:

## [Function Declarations](https://moodledev.io/docs/5.1/apis/subsystems/external/description)

Before they can be used, all functions must be declared to Moodle, and their inputs and outputs must be defined.

## [Function Definitions](https://moodledev.io/docs/5.1/apis/subsystems/external/functions)

An External function definition is the class, and collection of functions, used to define:

## [Security](https://moodledev.io/docs/5.1/apis/subsystems/external/security)

Before operating on any data in an external function, you must ensure that the user:

## [Service creation](https://moodledev.io/docs/5.1/apis/subsystems/external/advanced/custom-services)

Moodle comes with two built-in services that your functions can be attached to.

## [Unit Testing](https://moodledev.io/docs/5.1/apis/subsystems/external/testing)

Unit tests are the best way of checking the behaviour of your external services and can help you to:

## [Writing a new service](https://moodledev.io/docs/5.1/apis/subsystems/external/writing-a-service)

This documentation covers the creation of a new external service for use in a web service of a fictional local plugin, local\_groupmanager.