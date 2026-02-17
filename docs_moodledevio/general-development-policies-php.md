---
title: PHP | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/php
source: sitemap
fetched_at: 2026-02-17T15:59:26.375272-03:00
rendered_js: false
word_count: 0
summary: This document outlines the policy for determining minimum and maximum supported PHP versions for Moodle releases and the requirements for upgrading between Long Term Support (LTS) versions.
tags:
    - moodle
    - php-compatibility
    - versioning-policy
    - lts-upgrades
    - software-requirements
    - branch-management
category: reference
---

```
{panel:title=Policy: PHP & Moodle supported versions|borderStyle=dashed|borderColor=#cccccc|titleBGColor=#f7d6c1|bgColor=#ffffce}
Since Moodle 3.5 (MDL-59159), these rules apply to decide Minimum PHP and Moodle versions supported:
 # A LTS will always require the previous LTS (or later) for upgrading.
 # The maximum PHP version supported for a branch will be the max one achieved along the life of the branch. Usually with .0 releases but may happen later (we added support for php80 with 3.11.8, or support for php81 with 4.1.2, for example).
 # The minimum PHP version supported for a branch will be *the lower of*:
 -- The [minimum version supported in any way by php|http://php.net/supported-versions.php] that is under support for at least 12 more months when the new Moodle version gets released (so we provide slow, progressive increments).
 -- The maximum PHP version supported by the previous LTS branch (so we guarantee jumping between LTS is possible without upgrading PHP at the same time).{panel}
```