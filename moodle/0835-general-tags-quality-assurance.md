---
title: 18 docs tagged with "Quality Assurance" | Moodle Developer Resources
url: https://moodledev.io/general/tags/quality-assurance
source: sitemap
fetched_at: 2026-02-17T15:50:44.412004-03:00
rendered_js: false
word_count: 486
summary: This document serves as a comprehensive index for testing methodologies, tools, and processes used in Moodle and Moodle App development, covering acceptance, unit, and QA testing.
tags:
    - moodle-app
    - automated-testing
    - behat
    - phpunit
    - quality-assurance
    - continuous-integration
    - unit-testing
category: reference
---

## [Acceptance testing for the Moodle App](https://moodledev.io/general/app/development/testing/acceptance-testing)

In order to run tests that carry out automated functionality testing for the Moodle App, you can write Acceptance tests. This can be useful if you want to test plugins that are compatible with the app, or you're contributing to the app core. Behat tests for the app work the same way as tests for Moodle core, but they are not run as part of a normal Behat execution and there are some differences that we'll go through in this page.

## [Behat](https://moodledev.io/general/development/tools/behat)

This page describes the internals of Behat and the integration with Moodle.

## [Browsers](https://moodledev.io/general/development/tools/behat/browsers)

This page complements Behat providing info about how to run the acceptance tests suite in different browsers.

## [Continuous Integration for the Moodle App](https://moodledev.io/general/app/development/testing/continuous-integration)

Tests can be useful during development, but a good test suite really shines with CI processes in place. Running tests and other checks on a regular basis can be helpful to maintain good quality assurance, and catch regressions as early as possible.

## [Development process](https://moodledev.io/general/development/process)

A summary of the various development processes used in Moodle development.

## [Moodle App Development process](https://moodledev.io/general/development/process-moodleapp)

The development of new features and improvements in the Moodle App is organised in the following six phases:

## [Overview](https://moodledev.io/general/community)

This page gives an overview of the process of developing Moodle and outlines some of the basic concepts to better understand this Developer documentation.

## [PHPUnit](https://moodledev.io/general/development/tools/phpunit)

PHPUnit by Sebastian Bergmann is an advanced unit testing framework for PHP. It is installed as Composer dependency and is not part of Moodle installation. To run PHPUnit tests, you have to manually install it on your development computer or test server.

## [QA testing](https://moodledev.io/general/development/process/testing/qa)

All the information related to the Qualify Assurance tests during the Moodle development.

## [Running acceptance tests](https://moodledev.io/general/development/tools/behat/running)

Moodle uses Behat, a php framework for automated functional testing, as part of a suite of testing tools.

## [Testing](https://moodledev.io/general/development/process/testing)

All the information related to testing during the Moodle development.

## [Testing credits](https://moodledev.io/general/community/credits/testing)

The following people have helped with Quality Assurance (QA) testing:

## [Testing LMS issues in the mobile app](https://moodledev.io/general/development/process/testing/testing-lms-app)

Information related to mobile app testing of LMS issues

## [Testing of integrated issues](https://moodledev.io/general/development/process/testing/integrated-issues)

All the information related to the integration review process during the Moodle development.

## [Tracker introduction](https://moodledev.io/general/development/tracker)

A summary of the most common actions in Moodle tracker.

## [Unit testing for the Moodle App](https://moodledev.io/general/app/development/testing/unit-testing)

Unit tests are written in JavaScript using Jest. If you want to create a new one, Jest is already configured and you only need to create a file ending with .test.ts within the project. If you're going to do so, remember to follow the file location conventions.

## [Working combinations of OS+Browser+selenium](https://moodledev.io/general/development/tools/behat/browsers/supportedbrowsers)

As OS, Browsers and Selenium keeps updating, some combination might fail on different Moodle releases.

## [Writing acceptance tests](https://moodledev.io/general/development/tools/behat/writing)

This documentation gives some hints on writing behat tests for Moodle core, and for plugins. The focus of the documentation is on behat tests for plugins. Behat Features and Scenarios are written in a natural language, and should