---
title: Example usages | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/guides/javascript/comboboxsearch/examples
source: sitemap
fetched_at: 2026-02-17T15:46:54.994103-03:00
rendered_js: false
word_count: 103
summary: This document explains the migration of Moodle grade report modules to a standardized core search dropdown component and provides a code example for implementing it in custom modules.
tags:
    - moodle
    - search-dropdown
    - comboboxsearch
    - ui-components
    - frontend-development
    - php-api
category: tutorial
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