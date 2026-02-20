---
title: Moodle 5.0.5 | Moodle Developer Resources
url: https://moodledev.io/general/releases/5.0/5.0.5
source: sitemap
fetched_at: 2026-02-17T16:17:18.517282-03:00
rendered_js: false
word_count: 90
summary: This document provides a critical warning regarding a breaking change in a minor software release that affects site administration access for specific third-party themes. It advises affected users to skip this version and upgrade directly to a version where the issue is resolved.
tags:
    - release-notes
    - breaking-change
    - software-update
    - theme-compatibility
    - moodle
    - bug-fix
category: other
---

Please note that sites using third-party themes that modify the core admin renderer (such as Moove) are recommended **not** to upgrade to this minor version, as there is a known breaking change which affects access to site administration. Sites using Boost, Classic or other themes which do not modify site administration rendering are not affected, and it is safe to upgrade (for more information, see [MDL-87892](https://moodle.atlassian.net/browse/MDL-87892)).

This bug was fixed in version [5.0.6](https://moodledev.io/general/releases/5.0/5.0.6), so affected sites are recommended to skip this release and upgrade directly to the newest available version.