---
title: Users - allow administrative actions in courses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_allow_course_admin_actions
source: sitemap
fetched_at: 2026-02-15T08:59:38.89084-03:00
rendered_js: false
word_count: 208
summary: This document outlines the permissions and requirements for performing administrative actions on users within courses, including viewing login IDs, managing roles, and understanding necessary prerequisite permissions.
tags:
    - canvas-lms
    - user-management
    - permissions
    - administrative-actions
    - course-administration
    - user-roles
category: reference
---

## Users - allow administrative actions in courses

Allows user to view login ID information for users.

Allows user to view user details for course users.

Allows user to edit a user’s section or role (if not added via SIS).

### Additional Considerations

To edit user details, modify login details, or change user passwords, Users - manage login details must also be enabled.

To view the People page, Courses - view list must be enabled.

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

To view SIS IDs, SIS Data - read must be enabled.

To edit a user’s section, Conversations - send to individual course members must be enabled.

To link an observer to a student, Users - manage login details and Conversations - send to individual course members must be enabled.

To generate a pairing code on behalf of a student to share with an observer, Users - Generate observer pairing code for students must also be enabled.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).