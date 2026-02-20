---
title: Moodle 5.1 | Moodle Developer Resources
url: https://moodledev.io/general/releases/5.1
source: sitemap
fetched_at: 2026-02-17T16:17:22.058688-03:00
rendered_js: false
word_count: 166
summary: This document explains the necessary web server configuration changes and plugin migration steps required for upgrading to Moodle 5.1 due to the new public directory structure and routing engine.
tags:
    - moodle-upgrade
    - server-configuration
    - directory-structure
    - routing-engine
    - plugin-migration
category: guide
---

After upgrading to Moodle 5.1, some administrators may find that their site no longer loads correctly and instead shows directory listings or error messages.

This usually occurs because Moodle 5.1 introduces a new **"/public"** directory. Your web server now needs to be configured so that its document root points to this /public directory, rather than the main Moodle folder.

Moodle 5.1 also includes a new **Routing Engine**, which improves how requests are handled and enables cleaner URLs. While routing is strongly recommended, **it is not compulsory**. A compatibility layer is included to maintain backwards compatibility.

**Important note about plugins:**

After the upgrade, plugins previously installed will still be in their original locations above the /public folder. To have them function correctly, they will need to be manually moved into the appropriate location within the /public directory.

For detailed instructions and configuration examples, please refer to our [upgrading guide](https://docs.moodle.org/501/en/Upgrading#Code_directories_restructure) for configuring your webserver, and our [routing page](https://docs.moodle.org/501/en/Configuring_the_Router). These pages contain all of the information about these topics.