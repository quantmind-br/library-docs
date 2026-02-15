---
title: Users - view list | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_read_roster
source: sitemap
fetched_at: 2026-02-15T09:00:08.855319-03:00
rendered_js: false
word_count: 348
summary: This document outlines specific user and administrative permissions within the Canvas LMS, detailing access rights for admin tools, activity logs, and user management features.
tags:
    - canvas-lms
    - user-permissions
    - admin-tools
    - access-control
    - account-management
    - logging-activity
category: reference
---

Allows user to access the People link in Account Navigation.

#### Admin Tools (Logging tab)

Allows user to view login/logout activity of users in Admin Tools.

Allows user to search grade change logs by grader or student in Admin Tools.

Allows user to differentiate assignments to individual students.

Allows user to view and add users in a collaboration.

Allows user to send a message in Conversations without selecting a course.

Allows user to view the People link in Course Navigation.

Allows user to view groups in a course.

Allows user to view list of users in the account.

Allows user to view list of users in the course People page.

Allows user to view the Prior Enrollments button in the course People page.

Not available at the subaccount level.

### Additional Considerations

To view account-level groups, Groups - manage must also be enabled.

#### Admin Tools (Logging tab)

To generate login/logout activity in Admin Tools, Users - manage login details or Statistics - view must also be enabled.

To generate grade change logs in Admin Tools, Grades - view change logs must also be enabled.

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

To add groups, Groups - add must also be enabled.

To delete groups, Groups - delete must also be enabled.

To edit groups, Groups - manage must also be enabled.

To edit user details, modify login details, or change user passwords, Users - manage login details must also be enabled.

To view user page views, Statistics - view must also be enabled.

To act as other users, Users - act as must also be enabled.

To edit a user’s section, the appropriate Users permission (e.g. Users - Teachers), Users - allow administrative actions in courses, and Conversations - send to individual course members must also be enabled.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).