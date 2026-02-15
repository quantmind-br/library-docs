---
title: Users - Observers | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_manage_course_observer_enrollments
source: sitemap
fetched_at: 2026-02-15T08:59:58.754148-03:00
rendered_js: false
word_count: 177
summary: This document outlines the permissions and requirements for managing course observers, including adding, removing, and deactivating enrollments via the account Courses page. It also explains how these actions interact with account settings like Open Registration and SIS data management.
tags:
    - canvas-lms
    - observer-management
    - course-permissions
    - enrollment-administration
    - sis-integration
    - account-settings
category: reference
---

Allows user to add observers to a course from the account Courses page.

Allows user to add observers to a course.

Allows user to remove observers from a course.

Allows user to deactivate observers in a course.

### Additional Considerations

If the Open Registration account setting is enabled, users with this permission can add observers to a course from the Courses page via email address or login ID even if an observer does not already have a Canvas account.

To add a user via SIS ID, SIS Data - manage must also be enabled.

To access the account Courses page, Courses - view list must be enabled.

If an enrollment is created via SIS, only admins can remove the enrollment from a course.

To remove a user via SIS ID, SIS Data - manage must also be enabled.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).