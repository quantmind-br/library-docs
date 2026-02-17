---
title: 18 docs tagged with "Testing" | Moodle Developer Resources
url: https://moodledev.io/general/tags/testing
source: sitemap
fetched_at: 2026-02-17T15:51:51.576879-03:00
rendered_js: false
word_count: 528
summary: This document provides a comprehensive directory of resources for testing Moodle core and the mobile app, covering automated functional testing, unit testing, and quality assurance processes.
tags:
    - behat
    - phpunit
    - moodle-app
    - automated-testing
    - quality-assurance
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

## [Generator tool](https://moodledev.io/general/development/tools/generator)

The Generator tool is a Moodle administration tool that allows you to generate test data for your Moodle site. It is helpful for testing and development purposes, as it can create a large number of users, courses, and other entities in a short time.

## [Moodle App Acceptance Tests Upgrade Guide](https://moodledev.io/general/app/upgrading/acceptance-tests-upgrade-guide)

In the following guide, you will learn how to upgrade your plugins' acceptance tests to support newer versions of the app.

## [Penetration testing](https://moodledev.io/general/development/process/security/penetration-testing)

This is information for people who want to performing a penetration test of their Moodle instance as well as information for pen testers.

## [PHPUnit](https://moodledev.io/general/development/tools/phpunit)

PHPUnit by Sebastian Bergmann is an advanced unit testing framework for PHP. It is installed as Composer dependency and is not part of Moodle installation. To run PHPUnit tests, you have to manually install it on your development computer or test server.

## [PHPUnit 11 Upgrade](https://moodledev.io/general/development/tools/phpunit/upgrading-11)

Moodle 5.0 updated the version of PHPUnit from version 9.6 to version 11.

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

## [Unit testing for the Moodle App](https://moodledev.io/general/app/development/testing/unit-testing)

Unit tests are written in JavaScript using Jest. If you want to create a new one, Jest is already configured and you only need to create a file ending with .test.ts within the project. If you're going to do so, remember to follow the file location conventions.

## [Working combinations of OS+Browser+selenium](https://moodledev.io/general/development/tools/behat/browsers/supportedbrowsers)

As OS, Browsers and Selenium keeps updating, some combination might fail on different Moodle releases.

## [Writing acceptance tests](https://moodledev.io/general/development/tools/behat/writing)

This documentation gives some hints on writing behat tests for Moodle core, and for plugins. The focus of the documentation is on behat tests for plugins. Behat Features and Scenarios are written in a natural language, and should