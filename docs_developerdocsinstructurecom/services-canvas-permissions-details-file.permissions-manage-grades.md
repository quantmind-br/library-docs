---
title: Grades - edit | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/permissions/details/file.permissions_manage_grades
source: sitemap
fetched_at: 2026-02-15T09:02:36.798265-03:00
rendered_js: false
word_count: 300
summary: This document outlines the specific permissions and prerequisite requirements for managing grades, logs, and student analytics within the Canvas LMS. It describes user capabilities regarding gradebooks, speedgrader, and administrative logging tools.
tags:
    - canvas-lms
    - gradebook-permissions
    - admin-tools
    - grading-schemes
    - user-access
    - analytics-management
category: reference
---

#### Admin Tools (Logging tab)

Allows user to search by course ID or assignment ID in grade change logs in Admin Tools (not available at the subaccount level.)

Allows user to view student-specific data in Analytics.

Allows user to view the course grading scheme.

Allows user to like discussion posts when the Only Graders Can Like checkbox is selected.

Allows user to add, edit, and update grades in the Gradebook.

Allows user to access Gradebook History. Allows user to access the Learning Mastery Gradebook (if enabled).

Allows user to create and modify grading schemes.

Allows user to moderate a quiz and view the quiz statistics page.

Allows user to edit grades and add comments in SpeedGrader.

### Additional Considerations

#### Admin Tools (Logging tab)

To search grade change logs, Grades - view change logs must also be enabled.

To view student analytics in course analytics, Analytics - view must also be enabled.

To edit course grading schemes, Courses - manage must also be enabled.

Gradebook and SpeedGrader will be inaccessible if both Grades - edit and Grades - view all grades are disabled.

To view student analytics, Users - view list and Analytics - view must also be enabled.

To moderate a quiz, Assignments and Quizzes - manage / edit must also be enabled.

To view the user SIS ID column in the Quiz Item Analysis CSV file, SIS Data - read must also be enabled.

To view the submission log, Quizzes - view submission log must also be enabled.

To access the Student Interactions report, Reports - manage must also be enabled.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).