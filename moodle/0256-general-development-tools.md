---
title: Development tools | Moodle Developer Resources
url: https://moodledev.io/general/development/tools
source: sitemap
fetched_at: 2026-02-17T16:00:49.675797-03:00
rendered_js: false
word_count: 201
summary: This document outlines the essential development tools for Moodle, focusing on PHP linting, JavaScript and CSS build processes, and general workflow enhancements. It aims to help developers maintain coding standards and increase efficiency through tools like PHPCodeSniffer, Grunt, and MDK.
tags:
    - moodle-development
    - php-coding-style
    - grunt-task-runner
    - linting-tools
    - moodle-development-kit
    - workflow-automation
category: guide
---

A range of tools are available to make your life as a Moodle developer easier, and your development faster. These range from editor and IDE integrations, to linting tools which helps your code meet Moodle's [Coding style](https://moodledev.io/general/development/policies/codingstyle), to build tools essential to the build process.

These tools are discussed and summarised here.

## PHP[​](#php "Direct link to PHP")

Moodle's primary development language is PHP, and all code should pass basic PHP linting checks as a minimum, however all new PHP code must also meet the Moodle [Coding style rules](https://moodledev.io/general/development/policies/codingstyle). To make this task easier tools such as the [PHPCodeSniffer](https://moodledev.io/general/development/tools/phpcs) are available.

## JavaScript and CSS[​](#javascript-and-css "Direct link to JavaScript and CSS")

Moodle's JavaScript development relies upon a set of build tools written in JavaScript, and controlled using a task runner called `grunt`. In addition to building JavaScript files, grunt also controls building of theme CSS from SCSS, and stylistic linting checks of CSS.

See the [NodeJS and Grunt](https://moodledev.io/general/development/tools/nodejs) for more information on these build tools.

## Development workflow[​](#development-workflow "Direct link to Development workflow")

Along with language-specific tools, several tools have been created to make your day-to-date life as a developer easier. Perhaps the most widely used of these amongst those regularly contributing to the core Moodle project is the [Moodle Development Kit](https://moodledev.io/general/development/tools/mdk), or MDK as it is typically known.