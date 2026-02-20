---
title: Moodle 5.2 developer update | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/devupdate
source: sitemap
fetched_at: 2026-02-17T15:46:42.690103-03:00
rendered_js: false
word_count: 251
summary: This document outlines key developer-facing changes in Moodle 5.2, focusing on the reorganization of the Badges API and new language string structures for Activity Chooser descriptions.
tags:
    - moodle-5-2
    - badges-api
    - activity-chooser
    - plugin-development
    - open-badges
    - api-updates
category: guide
---

This page highlights the important changes that are coming in Moodle 5.2 for developers.

## Badges API reorganisation[​](#badges-api-reorganisation "Direct link to Badges API reorganisation")

The Badges API is responsible for managing badges in Moodle, including their creation, management, and export to external platforms compliant with Open Badges standards. However, the current implementation has become complex and difficult to maintain, and can't be easily extended to support future versions of Open Badges.

To address these challenges, we're reorganising the API to significantly improve its structure and maintainability. Key changes include:

- Refactor JSON exporters to support multiple Open Badges schema versions ([MDL-85621](https://moodle.atlassian.net/browse/MDL-85621)). This will allow for seamless integration with different schema requirements.

More information about the Badges API can be found in the [Badges API documentation](https://moodledev.io/docs/5.2/apis/subsystems/badges).

## Activity chooser descriptions refinement[​](#activity-chooser-descriptions-refinement "Direct link to Activity chooser descriptions refinement")

The help descriptions within the Activity Chooser have been significantly updated for all core Activities and Resources to provide richer guidance:

- A new optional language string, `modulename_summary`, has been introduced to define a concise, single-paragraph introduction to the module.
- The existing `modulename_help` string has been refined to contain the detailed description, now structured with dedicated sections for:
  
  - **Key features** to highlight the module's primary functionalities.
  - **Ways to use it** to provide practical, application-focused examples.
- A new optional string, `modulename_tip`, is available for a supplemental section for best practices, advice, or effective usage tips.

Third-party activity modules and resources can adopt the same structure by adding these language strings (`modulename_summary`, `modulename_help`, and `modulename_tip`) to their plugin's language files. These strings should be placed in the plugin's language file, for example, `mod/pluginname/lang/en/pluginname.php`.