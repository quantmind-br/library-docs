---
title: Manage Groups | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_manage_groups
source: sitemap
fetched_at: 2026-02-15T09:01:33.04282-03:00
rendered_js: false
word_count: 345
summary: This document outlines the permissions and functional capabilities required for managing account and course groups within the Canvas LMS platform.
tags:
    - canvas-lms
    - group-management
    - permissions
    - user-administration
    - course-settings
category: reference
---

Allows user to create account or course groups.

Allows user to add group members to account or course groups.

Allows user to add a group for a group assignment in a course.

Allows user to create course groups created by students.

Allows users to import groups in a course.

Allows user to delete account or course groups.

Allows user to remove students from account or course groups.

Allows user to move group members to another group in an account or course.

Allows user to assign a student group leader in an account or course.

Allows user to edit account and course groups.

Allows user to view the Clone Group Set button for an account or course group.

Allows user to randomly assign users to an account or course group.

Allows user to add users to an account or course group.

Allows user to move group members to another group in an account or course.

Allows user to assign a student group leader in an account or course.

### Additional Considerations

To add account level groups via CSV, SIS Data - import must also be enabled.

If this permission is disabled, at the account level, the user cannot view any existing account groups. At the course level, the user can view, but not access, any existing groups, including groups created by students.

To view account-level groups, Users - view list must also be enabled.

To view all student groups in a course, Groups - view all student groups must also be enabled.

By default, students can always create groups in a course. To restrict students from creating groups, Courses - manage must be enabled, and the Let students organize their own groups checkbox in Course Settings must not be selected.

To access the People page and view course groups, Users - view list must also be enabled.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).