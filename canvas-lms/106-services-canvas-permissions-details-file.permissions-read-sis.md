---
title: SIS Data - read | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_read_sis
source: sitemap
fetched_at: 2026-02-15T08:59:23.97029-03:00
rendered_js: false
word_count: 317
summary: This document outlines the specific permissions and administrative rules required for users to view and manage SIS IDs within courses, subaccounts, and user profiles.
tags:
    - sis-id
    - permissions
    - access-control
    - canvas-lms
    - user-management
    - subaccount-administration
category: reference
---

Allows user to view a course’s SIS ID.

Allows user to view the SIS ID in a user’s login details.

Allows user to view user SIS IDs in a course People page.

Allows user to view the user SIS ID column in the Quiz Item Analysis CSV file.

Governs account-related SIS IDs (i.e., subaccount SIS ID).

### Additional Considerations

Users and terms are located at the account, so the SIS endpoint always confirms the user’s permissions according to account.

Subaccounts only have ownership of courses and sections; they do not own user data. Subaccount admins are not able to view SIS information unless they are also granted an instructor role in a course.

Subaccount admins are not able to view SIS information unless they are also granted an instructor role in a course.

Subaccount admins cannot view SIS information without the course association, as the instructor role has permission to read SIS data at the account level.

To view a user’s login details, Users - view list and Modify login details for users must also both be enabled.

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

To manage SIS data, SIS Data - manage must be enabled.

If SIS Data - manage is enabled and SIS Data - read is disabled, the account permission overrides the course permission.

If SIS Data - manage is disabled and SIS Data - read is enabled, users can only view course, user, and subaccount SIS IDs.

To disallow users from viewing any SIS IDs at the course level, SIS Data - manage and SIS Data - read must both be disabled.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).