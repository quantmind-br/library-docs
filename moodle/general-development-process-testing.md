---
title: Testing | Moodle Developer Resources
url: https://moodledev.io/general/development/process/testing
source: sitemap
fetched_at: 2026-02-17T16:00:29.687154-03:00
rendered_js: false
word_count: 521
summary: This document provides a comprehensive overview of the manual and automated testing processes and tools used throughout the Moodle development lifecycle to ensure code quality and functionality.
tags:
    - moodle-development
    - manual-testing
    - automated-testing
    - phpunit
    - behat-testing
    - qa-process
    - regression-testing
    - unit-tests
category: concept
---

This page is the top level page regarding all testing activities around the Moodle project. Testing is essential to make sure that developed code does what it is meant to do, without causing new problems.

## Manual testing[​](#manual-testing "Direct link to Manual testing")

### Code testing[​](#code-testing "Direct link to Code testing")

Code is tested as part of reviewing at some key parts of the [Moodle development process](https://moodledev.io/general/development/process).

- `Development`. The developer of some code should test their own work on a wide variety of environments for correctness and performance
- `Peer review`. Developers often test each others work early in the development process
- `Integration review`. The integration team tests code weekly while they are evaluating suitability for integration into Moodle.

### Integration functional testing[​](#integration-functional-testing "Direct link to Integration functional testing")

Moodle has a dedicated team of testers who perform most of the manual testing for integration issues. Developers submitting patches **should always cover the patch with unit tests and/or Behat behavioural tests**.

### QA testing[​](#qa-testing "Direct link to QA testing")

Once all major features for a new Moodle release have landed, Moodle performs a Quality Assurance test cycle. This test cycle is typically performed by volunteers from the Moodle community who systematically test each available feature to ensure that it still works as intended. This process typically lasts 4-6 weeks and happens once per Major release.

More info

We recommend that you follow the [QA testing guide](https://moodledev.io/general/development/process/testing/qa) to know more about the Quality Assurance test cycle.

For major theme changes, additional manual tests may be run.

## Automated testing[​](#automated-testing "Direct link to Automated testing")

### Unit tests[​](#unit-tests "Direct link to Unit tests")

PHPUnit tests are supported as part of the code from Moodle 2.3 onwards. These are automated tests of very low-level code functionality that a developer should write as part of any new code.

More info

We recommend that you follow [PHPUnit integration](https://docs.moodle.org/dev/PHPUnit_integration) to help you run and write unit tests.

### Acceptance tests[​](#acceptance-tests "Direct link to Acceptance tests")

Moodle uses a framework called Behat to automatically test the user-interface. Tests can be written for each plugin, and for Moodle core.

- To run the existing tests, read [Running acceptance test](https://moodledev.io/general/development/tools/behat/running). You really need to do this first.
- To write new tests, read [Writing acceptance tests](https://moodledev.io/general/development/tools/behat/writing).
- To define new steps that can you used when writing tests, see [Writing new acceptance test step definitions](https://moodledev.io/general/development/tools/behat/writing#writing-new-acceptance-test-step-definitions).

tip

Because Behat tests work through the Moodle user interface, they are a bit slow. Therefore, you should probably also use PHPUnit to test the detailed edge cases in your code.

### Continuous integration testing[​](#continuous-integration-testing "Direct link to Continuous integration testing")

As soon as code is added to the integration repository, the continuous integration server tests the new code for:

- Coding guidelines
- PHPUnit tests
- SimpleTest unit tests on older versions of Moodle
- Detect unresolved merge conflicts
- Compare databases upgraded from previous versions
- Check the version.php is correct

A failure here notifies the integrators that the build has failed.

### Regression testing[​](#regression-testing "Direct link to Regression testing")

Every day, an automated build in a test server runs a large number of tests concerning key functions of Moodle, to make sure that everything still works and that some new fix in Moodle hasn't caused problems elsewhere.

These tests must pass completely before a new release can be made.

- [Unit tests](https://docs.moodle.org/dev/Unit_tests) using the PHPUnit framework
- [Acceptance testing](https://moodledev.io/general/development/tools/behat) using the Behat framework
- Performance testing using JMeter.

note

Moodle uses a sponsored version of [BrowserStack](https://www.browserstack.com/) for testing on multiple browsers.