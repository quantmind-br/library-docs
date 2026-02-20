---
title: Moodle 4.5.9 | Moodle Developer Resources
url: https://moodledev.io/general/releases/4.5/4.5.9
source: sitemap
fetched_at: 2026-02-17T16:17:08.274883-03:00
rendered_js: false
word_count: 90
summary: This document warns users about a breaking change in a specific minor version upgrade that affects site administration for sites using certain third-party themes. It recommends skipping the affected release and upgrading directly to version 4.5.10 to avoid access issues.
tags:
    - moodle-upgrade
    - breaking-changes
    - theme-compatibility
    - site-administration
    - release-notes
    - bug-fix
category: reference
---

Please note that sites using third-party themes that modify the core admin renderer (such as Moove) are recommended **not** to upgrade to this minor version, as there is a known breaking change which affects access to site administration. Sites using Boost, Classic or other themes which do not modify site administration rendering are not affected, and it is safe to upgrade (for more information, see [MDL-87892](https://moodle.atlassian.net/browse/MDL-87892)).

This bug was fixed in version [4.5.10](https://moodledev.io/general/releases/4.5/4.5.10), so affected sites are recommended to skip this release and upgrade directly to the newest available version.