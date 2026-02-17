---
title: Moodle 5.0.6 | Moodle Developer Resources
url: https://moodledev.io/general/releases/5.0/5.0.6
source: sitemap
fetched_at: 2026-02-17T16:17:21.876914-03:00
rendered_js: false
word_count: 110
summary: This document details the release of Moodle 5.0.6, which addresses a specific bug affecting site administration access for third-party themes.
tags:
    - moodle-release
    - release-notes
    - bug-fix
    - theme-compatibility
    - software-update
category: reference
---

Release date: 11 February 2026

Here is [the full list of fixed issues in 5.0.6](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%225.0.6%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

This release specifically addresses a bug in version 5.0.5 which caused site administration access issues on sites using third-party themes that modify the core admin renderer (such as Moove). Sites using the Boost or Classic theme (or other themes which do not modify site administration rendering) were not affected by this bug.

## General fixes and improvements[​](#general-fixes-and-improvements "Direct link to General fixes and improvements")

- [MDL-87892](https://moodle.atlassian.net/browse/MDL-87892) - Additional parameter for core\_admin\_renderer function added in [MDL-87352](https://moodle.atlassian.net/browse/MDL-87352) breaks many custom themes

## Security fixes[​](#security-fixes "Direct link to Security fixes")

No security fixes were included in this release. For details about the most recently fixed security bugs, please see the [5.0.5 release notes](https://moodledev.io/general/releases/5.0/5.0.5#security-fixes).