---
title: Example usages | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/guides/javascript/comboboxsearch/examples
source: sitemap
fetched_at: 2026-02-17T15:28:39.641835-03:00
rendered_js: false
word_count: 103
summary: This document explains how to implement the Moodle core search dropdown component in modules and details its migration within grade reports for a consistent user experience.
tags:
    - moodle
    - core-components
    - search-dropdown
    - plugin-development
    - ui-ux
category: guide
---

Several grade report modules have been migrated to use the new core search dropdown component. This migration provides a more consistent user experience across different grade report modules and allows for easier maintenance and updates.

Whilst working on [MDL-77991](https://moodle.atlassian.net/browse/MDL-77991), the Moodle development team also migrated the following third party plugin to use the new core search dropdown component as a proof of concept:

To use the core components in your own Moodle module, you can follow these steps:

```
$searchdropdows=newcomboboxsearch(
true,
'Trigger button content',
null,
'parent-class',
'trigger-button-class',
'search-dropdown-class',
null,
false,
);
$data['templatevalue']=$searchdropdown->export_for_template(\renderer_base);
```

This will output the HTML for the search dropdown component with the specified options. You can customize the options to fit your specific use case.