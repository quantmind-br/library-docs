---
title: Composer | Moodle Developer Resources
url: https://moodledev.io/general/development/tools/composer
source: sitemap
fetched_at: 2026-02-17T16:01:27.302881-03:00
rendered_js: false
word_count: 125
summary: This document explains how to use Composer to download Moodle and outlines the standard procedures for updating core dependencies and lock files to maintain environment stability.
tags:
    - moodle
    - composer
    - dependency-management
    - php
    - installation
    - testing-environment
category: guide
---

`Composer.json` now includes meta information and hence composer can be used to download the Moodle code base. You can do it by creating `composer.json` file with following information

```
{
"repositories":[
{
"type":"vcs",
"url":"https://github.com/moodle/moodle.git"
}
],
"require":{
"moodle/moodle":"v4.2.0"
}
}
```

There are a number of situations where we need to update the bundled [composer.json](https://github.com/moodle/moodle/blob/main/composer.json)] in core. When we upgrade, for a given branch, [the phpunit](https://moodle.atlassian.net/browse/MDL-71036) or [the behat-extension](https://moodle.atlassian.net/browse/MDL-70637) versions... we also have to update the [composer.lock](https://github.com/moodle/moodle/blob/main/composer.lock) file, in order to guarantee that all the tests will run in a stable, verified environment.

As far as there are a number of variables affecting how that lock file will be generated, here there are some standard steps to follow, in order to guarantee that any change to composer will be always applied in the same, standard and verified way.