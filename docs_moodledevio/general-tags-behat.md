---
title: 8 docs tagged with "Behat" | Moodle Developer Resources
url: https://moodledev.io/general/tags/behat
source: sitemap
fetched_at: 2026-02-17T15:47:26.591844-03:00
rendered_js: false
word_count: 293
summary: This document provides a comprehensive overview of automated acceptance testing for the Moodle App, detailing the use of Behat, continuous integration, and environment configuration.
tags:
    - moodle-app
    - behat
    - acceptance-testing
    - continuous-integration
    - automated-testing
    - quality-assurance
category: guide
---

## [Acceptance testing for the Moodle App](https://moodledev.io/general/app/development/testing/acceptance-testing)

In order to run tests that carry out automated functionality testing for the Moodle App, you can write Acceptance tests. This can be useful if you want to test plugins that are compatible with the app, or you're contributing to the app core. Behat tests for the app work the same way as tests for Moodle core, but they are not run as part of a normal Behat execution and there are some differences that we'll go through in this page.

## [Behat](https://moodledev.io/general/development/tools/behat)

This page describes the internals of Behat and the integration with Moodle.

## [Browsers](https://moodledev.io/general/development/tools/behat/browsers)

This page complements Behat providing info about how to run the acceptance tests suite in different browsers.

## [Continuous Integration for the Moodle App](https://moodledev.io/general/app/development/testing/continuous-integration)

Tests can be useful during development, but a good test suite really shines with CI processes in place. Running tests and other checks on a regular basis can be helpful to maintain good quality assurance, and catch regressions as early as possible.

## [Generator tool](https://moodledev.io/general/development/tools/generator)

The Generator tool is a Moodle administration tool that allows you to generate test data for your Moodle site. It is helpful for testing and development purposes, as it can create a large number of users, courses, and other entities in a short time.

## [Running acceptance tests](https://moodledev.io/general/development/tools/behat/running)

Moodle uses Behat, a php framework for automated functional testing, as part of a suite of testing tools.

## [Working combinations of OS+Browser+selenium](https://moodledev.io/general/development/tools/behat/browsers/supportedbrowsers)

As OS, Browsers and Selenium keeps updating, some combination might fail on different Moodle releases.

## [Writing acceptance tests](https://moodledev.io/general/development/tools/behat/writing)

This documentation gives some hints on writing behat tests for Moodle core, and for plugins. The focus of the documentation is on behat tests for plugins. Behat Features and Scenarios are written in a natural language, and should