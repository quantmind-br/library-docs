---
title: Manage Assignments and Quizzes | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_manage_assignments_and_quizzes
source: sitemap
fetched_at: 2026-02-15T09:01:51.290184-03:00
rendered_js: false
word_count: 575
summary: This document outlines the specific permissions and dependencies required to manage assignments, quizzes, and question banks within a course. It details the capabilities for adding, editing, and deleting these items and explains how they interact with other course settings like rubrics and blueprint courses.
tags:
    - canvas-lms
    - assignment-management
    - quiz-management
    - permissions
    - user-roles
    - course-administration
category: reference
---

## Manage Assignments and Quizzes

#### Assignments and Quizzes - add

Allows user to add assignments in a course.

Allows user to add assignment groups in a course.

Allows user to duplicate assignments in a course.

Allows user to add new assignments to a module.

Allows user to add new question banks to a course or account.

Allows user to add new questions to new or existing question banks in a course or account.

Allows user to add quizzes in a course.

Allows user to duplicate quizzes in a course.

#### Assignments and Quizzes - edit

Allows user to edit and publish/unpublish assignments.

Allows user to manage assignment settings.

Allows user to weight assignment groups.

Allows user to edit lock settings on the Assignments and Quizzes index pages.

Allows user to share an assignment to Commons.

Allows user to share a quiz to Commons.

Determines visibility and management of the Question Banks link in Account Navigation.

Allows user to edit and publish/unpublish quizzes.

Allows user to edit question banks in a course or account.

#### Assignments and Quizzes - delete

Allows user to delete assignments in a course.

Allows user to delete assignment groups in a course.

Allows user to delete quizzes in a course.

Allows user to delete question banks in a course or account.

### Additional Considerations

To access the Assignments Index Page, Course Content - view must be enabled.

To differentiate assignments to individual students, Users - view list must also be enabled.

To edit lock settings from the Assignments index page, Blueprint Courses - add / edit / associate / delete and Courses - manage must also be enabled.

If Blueprint Courses - add / edit / associate / delete and Courses - manage are enabled, but Assignments and Quizzes - edit is not enabled, blueprint lock settings for an assignment can be managed from the assignment’s details page.

To edit lock settings on an individual quiz, or on the Quizzes index page, Blueprint Courses - add / edit / associate / delete and Courses - manage must also be enabled.

To import assignments and quizzes using the Course Import Tool, Course Content - add / edit / delete must be enabled.

These permissions do not manage Discussions. Discussions are managed via individual Discussion permissions.

To edit assignment details on individual discussions, Discussions - manage must also be enabled.

To manage moderated grading, Grades - Select final grade for moderation must also be enabled.

To access the Quizzes Index Page, Course Content - view must be enabled.

To moderate a quiz, Grades - edit must also be enabled.

To access item banks for a course or account, Item Banks - manage account must also be enabled.

Disabling the Assignments and Quizzes - add permission will override (if enabled) the Rubrics - add / edit / delete permission, preventing user from creating rubrics for an individual assignment.

Disabling the Assignments and Quizzes - edit permission will override (if enabled) the Rubrics - add / edit / delete permission, preventing users from editing rubrics from an individual assignment.

Disabling the Assignments and Quizzes - delete permission will override (if enabled) the Rubrics - add / edit / delete permission, preventing user from deleting rubrics for an individual assignment.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).