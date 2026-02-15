---
title: Additional Notes | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dataset/dataset-additional-notes
source: sitemap
fetched_at: 2026-02-15T09:10:45.519239-03:00
rendered_js: false
word_count: 389
summary: This document provides technical clarification on specific data structures in Canvas LMS, including course tab configuration mapping, relationships between learning outcomes, and recent updates to user pseudonym records.
tags:
    - canvas-lms
    - database-schema
    - learning-outcomes
    - pseudonyms
    - data-modeling
    - course-settings
category: guide
---

## Understanding the `tab_configuration` Column in the Courses Table in Canvas Namespace

There have been several questions around the `tab_configuration` column in the **CD2 courses table**, and this note want to clarify how it works and what the values represent. This additional context should help improve understanding and make it easier to work with this data.

### Mapping of `id` Values to Tabs

The latest list of tab IDs can be found in the [Canvas LMS source codearrow-up-right](https://github.com/instructure/canvas-lms/blob/4ec7485b1b20513ec9335aa61f5ee0a68a5c3503/app/models/course.rb#L3174C3-L3194C18). Here’s the 2025-02-14 version:

### Example JSON in `tab_configuration` Column:

```
[
  { "id": 0 },
  { "id": "context_external_tool_8923" },
  { "id": 14, "hidden": true },
  { "id": 5, "hidden": true },
  { "id": 1, "hidden": false }
]
```

- `"id": 3` refers to the **Assignments** tab.
- `"id": "context_external_tool_8923"` refers to an **LTI app** (in this case, **Studio**). You can look up this `id` in the `context_external_tools` table to retrieve its friendly name from the `name` column.

#### Logic Behind Tab Visibility

While the `tab_configuration` column provides raw data, it’s important to note that there is **significant logic in the Canvas LMS** that determines whether these tabs are actually visible to a specific user. This logic depends on various factors, such as user roles and permissions.

#### Understanding `hidden: true/false`

- `"hidden": true` means the tab is currently **not visible** in the course interface.
- `"hidden": false` (or if `hidden` is not present) means the tab is **visible**.

* * *

## Connecting Learning Outcomes with Learning Outcome Groups

To connect `learning_outcomes` with their respective `learning_outcome_groups`, you should utilize the `content_tags` table. Below is guidance and examples to clarify how these associations work.

The relationship between `learning_outcomes` and `learning_outcome_groups` is established within the `content_tags` table as follows:

- If `content_tags.content_type` is `"LearningOutcome"`, then:
  
  - `content_tags.content_id` → `learning_outcomes.id`
- If `content_tags.associated_asset_type` is `"LearningOutcomeGroup"`, then:
  
  - `content_tags.associated_asset_id` → `learning_outcome_groups.id`

* * *

## What Are the Extra Pseudonyms That Now (2nd Half of 2025) Show up in Canvas?

The backend of the Canvas authentication system is being updated to improve its security, reliability, and performance. These updates include adding an extra Pseudonym record for each Canvas user in the [`canvas` namespaces' `pseudonyms`](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas) table. Initially, these pseudonyms will be inactive and not used during the user's authentication process. However, these pseudonyms will eventually be crucial in enabling new, improved, and more secure authentication methods for Instructure products. These records can be excluded from reports if they cause any issues. We apologize for any inconvenience this may cause.

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).