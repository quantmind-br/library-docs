---
title: 2 docs tagged with "Unit testing" | Moodle Developer Resources
url: https://moodledev.io/general/tags/unit-testing
source: sitemap
fetched_at: 2026-02-17T15:52:05.974441-03:00
rendered_js: false
word_count: 96
summary: This document outlines the unit testing frameworks used for Moodle development, specifically detailing PHPUnit for the core platform and Jest for the mobile application.
tags:
    - phpunit
    - jest
    - unit-testing
    - moodle-development
    - php
    - javascript
category: guide
---

## [PHPUnit](https://moodledev.io/general/development/tools/phpunit)

PHPUnit by Sebastian Bergmann is an advanced unit testing framework for PHP. It is installed as Composer dependency and is not part of Moodle installation. To run PHPUnit tests, you have to manually install it on your development computer or test server.

## [Unit testing for the Moodle App](https://moodledev.io/general/app/development/testing/unit-testing)

Unit tests are written in JavaScript using Jest. If you want to create a new one, Jest is already configured and you only need to create a file ending with .test.ts within the project. If you're going to do so, remember to follow the file location conventions.