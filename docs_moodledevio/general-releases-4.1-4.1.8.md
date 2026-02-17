---
title: Moodle 4.1.8 | Moodle Developer Resources
url: https://moodledev.io/general/releases/4.1/4.1.8
source: sitemap
fetched_at: 2026-02-17T16:15:40.813287-03:00
rendered_js: false
word_count: 116
summary: This document provides release notes for Moodle version 4.1.8, detailing specific regression fixes for JavaScript requests and Grade API changes introduced in previous versions.
tags:
    - moodle
    - release-notes
    - regression-fixes
    - software-update
    - version-history
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 22 December 2023

Here is [the full list of fixed issues in 4.1.8](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%224.1.8%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

Moodle 4.1.8 has been released outside of the normal release schedule, primarily to address two regressions that were introduced in 4.1.7. A minor release will still take place in February 2024, as scheduled.

## Regression fixes[​](#regression-fixes "Direct link to Regression fixes")

- [MDL-80393](https://moodle.atlassian.net/browse/MDL-80393) - Ensure JavaScript requests that require current language have access to it
- [MDL-80394](https://moodle.atlassian.net/browse/MDL-80394) - Backwards-incompatible Grade API changes committed to stable branches in [MDL-68652](https://moodle.atlassian.net/browse/MDL-68652)

## Security fixes[​](#security-fixes "Direct link to Security fixes")

There are no security fixes included in this release.