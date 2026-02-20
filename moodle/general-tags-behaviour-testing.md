---
title: 6 docs tagged with "Behaviour testing" | Moodle Developer Resources
url: https://moodledev.io/general/tags/behaviour-testing
source: sitemap
fetched_at: 2026-02-17T15:47:29.325467-03:00
rendered_js: false
word_count: 199
summary: This document provides an overview and resources for performing automated functional testing of the Moodle App and Moodle core using the Behat framework.
tags:
    - moodle-app
    - behat
    - acceptance-testing
    - automated-testing
    - browser-testing
    - selenium
    - functional-testing
category: guide
---

## [Acceptance testing for the Moodle App](https://moodledev.io/general/app/development/testing/acceptance-testing)

In order to run tests that carry out automated functionality testing for the Moodle App, you can write Acceptance tests. This can be useful if you want to test plugins that are compatible with the app, or you're contributing to the app core. Behat tests for the app work the same way as tests for Moodle core, but they are not run as part of a normal Behat execution and there are some differences that we'll go through in this page.

## [Behat](https://moodledev.io/general/development/tools/behat)

This page describes the internals of Behat and the integration with Moodle.

## [Browsers](https://moodledev.io/general/development/tools/behat/browsers)

This page complements Behat providing info about how to run the acceptance tests suite in different browsers.

## [Running acceptance tests](https://moodledev.io/general/development/tools/behat/running)

Moodle uses Behat, a php framework for automated functional testing, as part of a suite of testing tools.

## [Working combinations of OS+Browser+selenium](https://moodledev.io/general/development/tools/behat/browsers/supportedbrowsers)

As OS, Browsers and Selenium keeps updating, some combination might fail on different Moodle releases.

## [Writing acceptance tests](https://moodledev.io/general/development/tools/behat/writing)

This documentation gives some hints on writing behat tests for Moodle core, and for plugins. The focus of the documentation is on behat tests for plugins. Behat Features and Scenarios are written in a natural language, and should