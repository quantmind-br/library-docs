---
title: Manage Courses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_manage_courses
source: sitemap
fetched_at: 2026-02-15T09:01:37.304778-03:00
rendered_js: false
word_count: 518
summary: This document defines the permissions and account settings required for managing courses, syncing blueprint data, and accessing administrative features within the Canvas LMS.
tags:
    - canvas-lms
    - permissions
    - course-management
    - blueprint-courses
    - account-administration
    - user-access
category: reference
---

Allows user to add new courses to an account.

Allows user to sync Blueprint Courses.

Allows user to view Blueprint Sync history.

Allows user to view and manage courses in the account.

Allows user to view the Course Setup Checklist button.

Allows user to access the Navigation tab.

Allows user to edit course image, name, course code, time zone, subaccount, term, and other options in Course Details tab.

Allows user to access Student View (test student), Copy this Course, and Permanently Delete Course buttons.

Allows user to view student context cards in announcement and discussion replies.

Allows user to view the Conclude Course button.

Allows user to view the Delete this Course button.

Allows user to view the Publish Course and Unpublish Course buttons in the Course Home page. Allows user to view the Publish button in a course card for an unpublished course (Card View Dashboard).

Allows user to view the Reset Course Content button.

### Additional Considerations

If Courses - manage is enabled, but Blueprint Courses - add / edit / associate / delete is not enabled, users can still sync Blueprint Courses and view Sync history.

#### Courses - Account Settings

To access the Courses link in Account Navigation, Courses - view list must be enabled.

To add a course, Courses - add must also be enabled.

To restore a deleted course, Courses - delete, Courses - undelete, and Course Content - view must also be enabled.

To manage course content, Courses - manage and Course Content - add / edit / delete must be enabled.

To view Choose Home Page and Course Setup Checklist buttons, Courses - manage and Course Content - view must also be enabled. (Teachers, designers, and TAs can set the home page of a course, regardless of their permissions.)

The Courses - delete permission affects viewing the Permanently Delete this Course button, which only appears for manually created courses.

To cross-list a section, Courses - manage and Manage Course Sections - edit must also be enabled.

To edit the course SIS ID, Courses - manage and SIS Data - manage must also be enabled.

The Courses - Reset permission resets course content for both manually created and SIS-managed courses. (For SIS-managed courses, the SIS Data - manage permission does not apply.)

#### Courses - Account Navigations

To access the Courses link in Account Navigation, Courses - manage and Courses - view list must be enabled.

To view grades in a course, Courses - manage and Grades - view all grades must also be enabled.

The Courses - publish permission allows the user to publish courses that do not contain modules. To publish/unpublish module content, Course Content - add / edit / delete must be enabled.

Student context cards must be enabled for an account by an admin. If Courses - manage is not enabled, users can still view context cards through the Gradebook.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).