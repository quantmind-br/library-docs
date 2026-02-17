---
title: Moodle 5.1.2 | Moodle Developer Resources
url: https://moodledev.io/general/releases/5.1/5.1.2
source: sitemap
fetched_at: 2026-02-17T16:17:26.79676-03:00
rendered_js: false
word_count: 90
summary: This document provides an advisory regarding a breaking change in a specific software release that impacts site administration when using certain third-party themes.
tags:
    - release-notes
    - breaking-change
    - theme-compatibility
    - upgrade-advisory
    - moodle
category: reference
---

Please note that sites using third-party themes that modify the core admin renderer (such as Moove) are recommended **not** to upgrade to this minor version, as there is a known breaking change which affects access to site administration. Sites using Boost, Classic or other themes which do not modify site administration rendering are not affected, and it is safe to upgrade (for more information, see [MDL-87892](https://moodle.atlassian.net/browse/MDL-87892)).

This bug was fixed in version [5.1.3](https://moodledev.io/general/releases/5.1/5.1.3), so affected sites are recommended to skip this release and upgrade directly to the newest available version.