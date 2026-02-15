---
title: SIS Data - manage | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_manage_sis
source: sitemap
fetched_at: 2026-02-15T09:00:43.646502-03:00
rendered_js: false
word_count: 229
summary: This document defines the permissions and requirements for managing Student Information System (SIS) data, including importing records and editing SIS IDs for courses and users within Canvas LMS.
tags:
    - sis-import
    - canvas-lms
    - user-permissions
    - account-management
    - sis-id
    - data-integration
category: reference
---

Determines visibility of SIS Import link in Account Navigation.

Allows user to view the previous SIS import dates, errors, and imported items.

Allows user to edit the course SIS ID.

Allows user to view and edit the SIS ID and Integration ID in a user’s Login Details.

Allows user to edit the course SIS ID.

Allows user to view and insert data in the SIS ID field.

### Additional Considerations

To edit course settings, Courses - manage must be enabled.

To view or edit a user’s SIS ID or Integration ID, Users - view list and Users - manage login details must also both be enabled.

If this permission is enabled, users do not need the SIS Data - read permission enabled. The account permission overrides the course permission.

To disallow users from managing SIS IDs at the course level, SIS Data - manage and SIS Data - read must both be disabled.

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

To import SIS data, SIS Data - import must also be enabled.

Not available at the subaccount level.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).