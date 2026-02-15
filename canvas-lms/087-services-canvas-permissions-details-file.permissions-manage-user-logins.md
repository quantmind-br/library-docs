---
title: Users - manage login details | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_manage_user_logins
source: sitemap
fetched_at: 2026-02-15T08:59:31.574396-03:00
rendered_js: false
word_count: 239
summary: This document outlines the administrative permissions and requirements for managing user accounts, login details, and activity reports within the Canvas LMS platform.
tags:
    - canvas-lms
    - user-management
    - administrative-permissions
    - access-control
    - account-administration
category: reference
---

## Users - manage login details

Allows user to create accounts for new users.

Allows user to remove and merge users in an account.

Allows user to modify user account details.

Allows user to view and modify login information for a user.

#### Admin Tools (Logging tab)

Allows user to generate login/logout activity report in Admin Tools.

### Additional Considerations

#### Admin Tools (Logging tab)

If Users - manage login details or Statistics - view is enabled, the user will be able to generate login/logout activity in Admin Tools. To hide the login/logout activity option in Admin Tools, both of these permissions need to be disabled.

To view users and user account details, Users - view list must be enabled.

To change user passwords, Users - view must also be enabled.

To view a user’s SIS ID, SIS Data - manage or SIS Data - read must also be enabled.

To view a user’s Integration ID, SIS Data - manage must also be enabled.

To merge users, the Self Service User Merge feature option must also be enabled.

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

Not available at the subaccount level.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).