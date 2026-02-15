---
title: canvas | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas
source: sitemap
fetched_at: 2026-02-15T09:11:03.409887-03:00
rendered_js: false
word_count: 20771
summary: This document defines the schema and property details for various database tables within the Canvas Data 2 system, including access tokens, accounts, and assessment questions. It provides a technical overview of data types, primary keys, and entity relationships to facilitate data extraction and analysis.
tags:
    - canvas-data-2
    - database-schema
    - data-dictionary
    - learning-management-system
    - metadata-reference
    - access-tokens
category: reference
---

Stores the access tokens for a user and developer tools.

This table in Canvas Data 2 will only share developer tool specific token metadata. All users have an option to create an access token based on their role and level of data access.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for an access token record.
- **developer\_key\_id** ([developer\_keys](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.developer_keys)) - The unique identifier of a developer key.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of the user the token acts as.
- **real\_user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - If the token was created while masquerading, this is the real user doing the masquerading. Used for auditing.
- **last\_used\_at** (datetime | None) - Timestamp of last access using this access token.
- **expires\_at** (datetime | None) - The expiration date/time for this token. This may be a NULL value.
- **purpose** (Annotated\[str, MaxLength(255)] | None) - For user-generated tokens, purpose can be manually set. For app-generated tokens, this should be generated based on the scope defined in the authentication process.
- **created\_at** (datetime) - Timestamp of when an `access_tokens` record was created.
- **updated\_at** (datetime) - Timestamp of when an `access_tokens` record was updated.
- **scopes** (json | None) - A list of scopes that can be applied to access tokens. i.e.: courses.

Join table for accounts, users and roles.

Contains users' roles within an account (this table includes the account admins).

**Properties:**

- **id** (int64) - `primary key` The unique identifier for the users account association record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp of when an `account_users` record was created.
- **updated\_at** (datetime) - Timestamp of when an `account_users` record was updated.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - The unique ID of an account.
- **role\_id** ([roles](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.roles)) - The unique ID of a role.

Stores data about account objects in the Canvas system.

Accounts are most often used to represent a hierarchy of colleges, schools, departments, campuses.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - The display name of the account.
- **id** (int64) - `primary key` The ID of the Account object.
- **deleted\_at** (datetime | None) - Timestamp of when the account was deleted. Will only ever be NULL for end customers.
- **parent\_account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | None) - The account's parent ID, or NULL if this is the root account.
- **current\_sis\_batch\_id** (int64 | None) - The ID of the currently processing SIS (Student Information System) batch (if submitted via UI, not API).
- **storage\_quota** (int64 | None) - The storage quote for the account, in megabytes.
- **default\_storage\_quota** (int64 | None) - The storage quota for children accounts in megabytes, if not otherwise specified.
- **default\_locale** (Annotated\[str, MaxLength(255)] | None) - Language for the account.
- **default\_user\_storage\_quota** (int64 | None) - The default storage quota for users in the account in megabytes, if not otherwise specified.
- **default\_group\_storage\_quota** (int64 | None) - The storage quota for a group in the account in megabytes, if not otherwise specified.
- **integration\_id** (Annotated\[str, MaxLength(255)] | None) - The account's identifier in the Student Information System.
- **lti\_context\_id** (Annotated\[str, MaxLength(255)] | None) - UUID of the Canvas context in LTI standard. Secondary ID for this context, could be used in API to identify resource as well.
- **consortium\_parent\_account\_id** (int64 | None) - The root account of the consortium account, if this root account is part of a consortium.
- **course\_template\_id** (int64 | None) - The course selected as a template for new courses created in this account. 0 if a template should not be used, nor inherited.
- **created\_at** (datetime) - Timestamp of when the account was created.
- **updated\_at** (datetime) - Timestamp of when the account was updated.
- **uuid** (Annotated\[str, MaxLength(255)] | None) - The UUID of the account.
- **sis\_source\_id** (Annotated\[str, MaxLength(255)] | None) - Correlated id for the record for this course in the SIS system (assuming SIS integration is configured)

## assessment\_question\_banks

Stores data about question banks.

Question Banks are a place to house questions that can be added to quizzes across courses or accounts.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for the question bank.
- **deleted\_at** (datetime | None) - The time the question bank was deleted. If the question bank has not been deleted the value will be NULL.
- **created\_at** (datetime) - The time the question bank was created.
- **updated\_at** (datetime) - The time the question bank was last updated.
- **context\_id** (None | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier for the question bank's context (account or course).
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported this question bank.
- **title** (bounded\_str | None) - The title for the question bank.

Stores attributes of a question associated with a quiz.

The column `question_data` stores a variety of question data related points such as:

- `question_type` denotes the type of the question. Possible values are:
  
  - `fill_in_multiple_blanks_question`
  - `multiple_answers_question`
  - `multiple_dropdowns_question`
- `question_text` is the text of the question.
- `regrade_option` denotes if regrading is available for the question. Possible values are: `available` and `unavailable` for question types `multiple_answers_question`, `multiple_choice_question`, `true_false_question`, and NULL for others. Defaults to `available` for the allowed question types, and NULL for the rest.
- `correct_comments` are comments to be displayed if the student answers the question correctly.
- `incorrect_comments` are comments to be displayed if the student answers the question incorrectly.
- `neutral_comments` are comments to be displayed regardless of how the student answers the question.
- `answers` is a JSON array of all possible answers.

**Properties:**

- **name** (bounded\_str | None) - Name of the question.
- **id** (int64) - `primary key` The unique identifier for the Assessment Question.
- **deleted\_at** (datetime | None) - The time the question was deleted. If the question has not been deleted the value will be NULL.
- **created\_at** (datetime | None) - Time when the quiz question was created.
- **updated\_at** (datetime | None) - Time when the quiz question was last updated.
- **context\_id** (int64 | None) - The unique identifier for the question bank's context (account or course). No longer used as Canvas delegates to `context_id` of the associated AssessmentQuestion.
- **context\_type** (Annotated\[str, MaxLength(255)] | None) - The type of context the question bank is associated with. No longer used as Canvas delegates to the context of the associated AssessmentQuestion.
- **question\_data** (json | None) - A variety of question data related points.
- **assessment\_question\_bank\_id** ([assessment\_question\_banks](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assessment_question_banks) | None) - The unique identifier for the assessment question bank this question is associated with.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported this assessment question.
- **position** (int32 | None) - The position of the question.

Stores rules associated with an assignment group.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - The name of the assignment group.
- **id** (int64) - `primary key` The ID of the assignment group.
- **created\_at** (datetime) - The time when the assignment group was created.
- **updated\_at** (datetime) - The time when the assignment group was updated.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier for the assignments group context (course).
- **default\_assignment\_name** (Annotated\[str, MaxLength(255)] | None) - The default title for an assignment when it is created in this assignment group.
- **group\_weight** (float64 | None) - The weight of the assignment group.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported this assignment group.
- **sis\_source\_id** (Annotated\[str, MaxLength(255)] | None) - The Student Information System source ID of the assignment group.
- **position** (int32 | None) - The position of the assignment group.

## assignment\_override\_students

Stores measures related to ad hoc users for whom an assignment override exists.

**Properties:**

- **id** (int64) - `primary key` The ID of the Assignment Override Student.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - Identifies the user.
- **created\_at** (datetime) - Timestamp of when the `assignment_override_student` record was created.
- **updated\_at** (datetime) - Timestamp of when the `assignment_override_student` was last updated.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - Identifies the assignment the override is associated with.
- **quiz\_id** ([quizzes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quizzes) | None) - Identifies the quiz the override is associated with.

Stores records for assignment due date overrides.

There may be many records in this table for each assignment. Use the data in this table to calculate actual due, all day, lock and unlock dates/times.

**Properties:**

- **id** (int64) - `primary key` The ID of the `assignment_override`.
- **created\_at** (datetime) - Timestamp of when the `assignment_override` was created.
- **updated\_at** (datetime) - Timestamp of when the `assignment_override` was last updated.
- **due\_at** (datetime | None) - The new *due at* date-time for this group of users.
- **unlock\_at** (datetime | None) - The new *unlock at* date-time for this group of users.
- **lock\_at** (datetime | None) - The new *lock at* date-time for this group of users.
- **all\_day** (bool | None) - Indicates if the `all_day` field overrides the original `all_day` field in the table `assignment` for this group of users.
- **assignment\_version** (int32 | None) - The version of the assignment this override is applied to.
- **due\_at\_overridden** (bool) - Indicates if the `unlock_at` field overrides the original.
- **unlock\_at\_overridden** (bool) - Indicates if the `unlock_at` field overrides the original `unlock_at` field in the table `assignment` for this group of users.
- **lock\_at\_overridden** (bool) - Indicates if the `lock_at` field overrides the original `lock_at` field in the table `assignment` for this group of users.
- **quiz\_id** ([quizzes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quizzes) | None) - Identifies the quiz the override is associated with.
- **quiz\_version** (int32 | None) - The version of the quiz this override is applied to.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - Identifies the assignment the override is associated with.
- **all\_day\_date** (date | None) - The new date version of the due date if the `all_day` flag is true.
- **title** (Annotated\[str, MaxLength(255)]) - The title for this `assignment_override`.

This table stores attributes for assignments.

There is one record in this table for each assignment.

**Properties:**

- **integration\_id** (Annotated\[str, MaxLength(255)] | None) - Third Party unique identifier for Assignments.
- **lti\_context\_id** (bounded\_str | None) - UUID of the Canvas context in LTI standard. Secondary ID for this context, could be used in API to identify resource as well.
- **created\_at** (datetime | None) - The time at which this assignment was originally created.
- **updated\_at** (datetime | None) - The time at which this assignment was last modified.
- **due\_at** (datetime | None) - The due date for the assignment. Returns NULL if not present.
- **unlock\_at** (datetime | None) - The unlock date, meaning that the assignment is unlocked after this date. Returns NULL if not present.
- **lock\_at** (datetime | None) - The lock date, meaning that the assignment is locked after this date. Returns NULL if not present.
- **points\_possible** (float64 | None) - The maximum points possible for the assignment.
- **assignment\_group\_id** ([assignment\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignment_groups) | None) - Identifies which assignment grouping the particular assignment is part of (assignment groups may have a scoring weight to determine how much of the assignment group contributes to the total grade).
- **grading\_standard\_id** ([grading\_standards](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.grading_standards) | None) - The ID of the grading standard being applied to this assignment. Valid if `grading_type` is `letter_grade` or `gpa_scale`.
- **submissions\_downloads** (int32) - Number of times submissions have been downloaded in a zip bundle.
- **peer\_review\_count** (int32) - Represents the amount of reviews each user is assigned. NOTE: This key is NOT present unless you have automatic\_peer\_reviews set to true.
- **peer\_reviews\_due\_at** (datetime | None) - Timestamp for when peer reviews should be completed.
- **peer\_reviews\_assigned** (bool) - True if all peer reviews have been assigned.
- **peer\_reviews** (bool) - Indicates if peer reviews are required for this assignment.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of the object this assignment belongs to. Typically course.
- **automatic\_peer\_reviews** (bool) - Indicates if peer reviews are assigned automatically. If false, the teacher is expected to manually assign peer reviews.
- **all\_day** (bool) - True if a specific time for when the assignment is due was not given. The effective due time will be 11:59pm.
- **all\_day\_date** (date | None) - The date version of the due date if the `all_day` flag is true.
- **could\_be\_locked** (bool) - True if the assignment is under a module that can be locked.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported this assignment. For assignments which have been imported via a content migration, an opaque identifier for the assignment in its source. This field is used by Canvas to identify when an assignment is being re-imported, and can also be used to identify multiple assignments that have been copied from the same source.
- **grade\_group\_students\_individually** (bool) - If this is a group assignment, boolean flag indicating whether or not students will be graded individually.
- **anonymous\_peer\_reviews** (bool) - If true, hide the identities of peer-reviewing and peer-reviewed students. Only relevant if `peer_reviews` is true.
- **turnitin\_enabled** (bool) - Flag indicating whether or not Turnitin has been enabled for the assignment. NOTE: This flag will not appear unless your account has the Turnitin plugin available.
- **allowed\_extensions** (Annotated\[str, MaxLength(255)] | None) - Allowed file extensions, which take effect if `submission_types` includes `online_upload`.
- **group\_category\_id** ([group\_categories](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.group_categories) | None) - The ID of the assignment's group set, if this is a group assignment. For group discussions, set `group_category_id` on the discussion topic, not the linked assignment.
- **freeze\_on\_copy** (bool) - Indicates if assignment will be frozen when it is copied. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account.
- **only\_visible\_to\_overrides** (bool) - Indicates whether the assignment is only visible to overrides.
- **post\_to\_sis** (bool) - Present if Sync Grades to Student Information System feature is enabled.
- **moderated\_grading** (bool) - Indicates if the assignment is moderated.
- **grades\_published\_at** (datetime | None) - For assignments with moderated grading, a timestamp identifying when provisional grades were published.
- **omit\_from\_final\_grade** (bool) - If true, the assignment will be omitted from the student's final grade.
- **intra\_group\_peer\_reviews** (bool) - Indicates whether or not members from within the same group on a group assignment can be assigned to peer review their own group's work.
- **vericite\_enabled** (bool) - Flag indicating whether or not VeriCite has been enabled for the assignment. NOTE: This flag will not appear unless your account has the VeriCite plugin available.
- **anonymous\_instructor\_annotations** (bool) - Flag indicating whether instructor annotations in document submissions for this assignment should be anonymous.
- **duplicate\_of\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - If the assignment is a duplicate, the ID of the original assignment.
- **anonymous\_grading** (bool) - Indicates if the assignment is graded anonymously. If true, graders cannot see student identities.
- **graders\_anonymous\_to\_graders** (bool) - Indicates if provisional graders' identities are hidden from other provisional graders. Only relevant for moderated assignments with grader\_comments\_visible\_to\_graders set to true.
- **grader\_count** (int32) - The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors.
- **grader\_comments\_visible\_to\_graders** (bool) - Indicates if provisional graders' comments are visible to other provisional graders. Only relevant for moderated assignments.
- **grader\_section\_id** ([course\_sections](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.course_sections) | None) - Graders for an assignment with anonymous moderated marking are assigned from this section if provided, or all sections otherwise.
- **final\_grader\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - User ID of the final grader.
- **grader\_names\_visible\_to\_final\_grader** (bool) - Indicates if provisional grader identities are visible to the final grader. Only relevant for moderated assignments.
- **allowed\_attempts** (int32 | None) - The number of submission attempts a student can make for this assignment. -1 is considered unlimited.
- **sis\_source\_id** (bounded\_str | None) - ID for the correlated record for the assignment in the Student Information System. It can be NULL.
- **annotatable\_attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - For an `Annotated Document` type assignment, the ID of the annotatable attachment.
- **important\_dates** (bool) - Indicates if the assignment has important dates.
- **description** (bounded\_str | None) - The assignment description in an HTML fragment.
- **position** (int32 | None) - The sorting order of the assignment in the group.
- **id** (int64) - `primary key` Primary key for this record in the Canvas assignments table.
- **title** (Annotated\[str, MaxLength(255)] | None) - Title of the assignment.
- **parent\_assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - Parent of assignment.
- **has\_sub\_assignments** (bool | None) - Indicates if this assignment has sub assignments.

Links user files to an assignment to allow grader to see the student's submission.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of an attachment associations record.
- **attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - The unique identifier of an attachment record.

Describes files in Canvas.

**Properties:**

- **deleted\_at** (datetime | None) - Timestamp showing when this record was deleted. If the record has not been deleted the value will be NULL.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime | None) - Timestamp showing when an attachments record was created.
- **updated\_at** (datetime | None) - Timestamp showing when an attachments record was updated.
- **unlock\_at** (datetime | None) - The date-time to unlock the file at.
- **lock\_at** (datetime | None) - The date-time to lock the file at.
- **folder\_id** ([folders](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.folders) | None) - The unique identifier of a folder record.
- **filename** (bounded\_str | None) - The name of the actual file.
- **locked** (bool) - Flag if file is locked or available.
- **media\_entry\_id** (Annotated\[str, MaxLength(255)] | None) - The ID of a Kaltura/Notorious media entry associated with the file.
- **md5** (Annotated\[str, MaxLength(255)] | None) - A hash of the file. Historically this was MD5 in Canvas Data 1 and API but newer records store a SHA512 in this column.
- **replacement\_attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - The unique identifier of the attachment that this record replaced.
- **usage\_rights\_id** (usage\_rights | None) - The unique identifier for the `usage_rights` record.
- **modified\_at** (datetime | None) - Timestamp showing when an attachment record was updated.
- **viewed\_at** (datetime | None) - Timestamp showing when an attachment record was last viewed.
- **could\_be\_locked** (bool | None) - True if the file is in a lockable module item.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - Only applicable for files which have been imported via a content migration, an opaque identifier for the file in its source. This field is used by Canvas to identify when a file is being re-imported, and can also be used to identify multiple files that have been copied from the same source.
- **namespace** (Annotated\[str, MaxLength(255)] | None) - The asset string of the root account associated with the file's storage.
- **id** (int64) - `primary key` The unique identifier of an attachment record.
- **size** (int64 | None) - The size of the file in bytes.
- **display\_name** (bounded\_str | None) - The attachment name that is displayed.
- **content\_type** (Annotated\[str, MaxLength(255)] | None) - MIME type of the associated file.
- **uuid** (Annotated\[str, MaxLength(255)] | None) - The UUID of the attachment.
- **root\_attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - Identifier of the source file from which this file was copied and created. Defaults to `NULL` when this is the only copy.

The model for calendar events in Canvas.

These can be manually created, or automatically generated from other items like Assignments with a date attached.

**Properties:**

- **deleted\_at** (datetime | None) - Timestamp when this record was deleted. If the record has not been deleted the value will be NULL.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp of when a `calendar_events` record was created.
- **updated\_at** (datetime) - Timestamp of when a `calendar_events` record was updated.
- **location\_address** (bounded\_str | None) - The address where the event is taking place.
- **start\_at** (datetime | None) - The start date for the calendar event, if applicable.
- **end\_at** (datetime | None) - The end date for the calendar event, if applicable.
- **context\_code** (Annotated\[str, MaxLength(255)] | None) - The context code of the calendar this event belongs to (course, user or group).
- **time\_zone\_edited** (Annotated\[str, MaxLength(255)] | None) - Time zone of the user editing the event.
- **parent\_calendar\_event\_id** ([calendar\_events](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.calendar_events) | None) - Normally NULL. If this is a reservation (see the Appointment Groups API), the ID will indicate the time slot it is for. If this is a section-level event, this will be the course-level parent event.
- **effective\_context\_code** (Annotated\[str, MaxLength(255)] | None) - If specified, it indicates which calendar this event should be displayed on. For example, a section-level event would have the course's context code here, while the section's context code would be returned above.
- **participants\_per\_appointment** (int32 | None) - If the event is a time slot, this is the participant limit.
- **comments** (bounded\_str | None) - Comments associate with this reservation.
- **web\_conference\_id** ([web\_conferences](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.web_conferences) | None) - The ID of a web conference associated with the calendar event.
- **all\_day** (bool | None) - Indicates whether this is an all-day event (midnight to midnight).
- **all\_day\_date** (date | None) - The date of this event.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported this calendar event.
- **important\_dates** (bool) - Indicates if the calendar event has important dates.
- **location\_name** (bounded\_str | None) - The location name of the event.
- **description** (bounded\_str | None) - The HTML description of the event.
- **id** (int64) - `primary key` The unique identifier for a calendar event record.
- **title** (Annotated\[str, MaxLength(255)] | None) - The title of the calendar event.

## canvadocs\_annotation\_contexts

Launch context associated with DocViewer when assignment is of type `Annotated_Document`.

**Properties:**

- **created\_at** (datetime) - When this record was created.
- **updated\_at** (datetime) - When this record was last updated.
- **attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments)) - The attachment that this DocViewer launch is owned by.
- **submission\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions)) - The submission this DocViewer launch is associated with.
- **launch\_id** (bounded\_str) - The ID that differentiates a DocViewer launch from another using the same attachment.
- **submission\_attempt** (int32 | None) - The submission attempt associated with the launch\_id.
- **id** (int64) - `primary key` The ID of this record.

This table contains attributes related to collaborations.

**Properties:**

- **id** (int64) - `primary key` The ID of the collaboration.
- **collaboration\_type** (Annotated\[str, MaxLength(255)] | None) - The type of the collaboration.
- **document\_id** (Annotated\[str, MaxLength(255)] | None) - The ID of the document.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the user.
- **url** (Annotated\[str, MaxLength(255)] | None) - The URL of the collaboration.
- **uuid** (Annotated\[str, MaxLength(255)] | None) - The UUID of the collaboration.
- **data** (json | None) - The data of the collaboration.
- **created\_at** (datetime) - The date this collaboration was created.
- **updated\_at** (datetime) - The date this collaboration was updated.
- **description** (bounded\_str | None) - The description of the collaboration.
- **title** (Annotated\[str, MaxLength(255)]) - The title of the collaboration.
- **workflow\_state** (Annotated\[str, MaxLength(255)]) - The workflow state of the collaboration.
- **deleted\_at** (datetime | None) - The date this collaboration was deleted.
- **context\_code** (Annotated\[str, MaxLength(255)] | None) - The context code of the collaboration.
- **type** (Annotated\[str, MaxLength(255)] | None) - The type of the collaboration.
- **resource\_link\_lookup\_uuid** (Annotated\[str, MaxLength(255)] | None) - The UUID of the resource

Stores user comments that have been added to the comment bank.

**Properties:**

- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The ID of the user who created the comment bank item.
- **created\_at** (datetime) - Timestamp of when the comment\_bank\_item record was created.
- **updated\_at** (datetime) - Timestamp of when the comment\_bank\_item record was updated.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - Identifies the course.
- **id** (int64) - `primary key` The ID of the comment bank item.
- **comment** (bounded\_str) - The text of the comment bank item.

Channels through which a user receives Canvas notifications.

Examples include an email address, a phone number, a mobile device token for push notifications, etc.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a user communication channel record.
- **path** (Annotated\[str, MaxLength(255)]) - The address of the communication channel e.g. an email address or a phone number.
- **path\_type** (Annotated\[str, MaxLength(255)]) - The type of communication channel being described. This field determines the type of value seen in `address`.
- **pseudonym\_id** ([pseudonyms](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.pseudonyms) | None) - The unique ID of a user's pseudonym record.
- **bounce\_count** (int32) - The number of times a communication channel has bounced when trying to deliver messages.
- **confirmation\_code\_expires\_at** (datetime | None) - The date-time when the issued confirmation code will expire.
- **confirmation\_sent\_count** (int32) - The number of confirmations sent for the channel.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp of when a `communication_channels` record was created.
- **updated\_at** (datetime) - Timestamp of when a `communication_channels` record was updated.
- **position** (int32 | None) - The position of this communication channel relative to the user's other channels when they are ordered.

Saves data about what and when was added to a course through a course copy or import.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a content migration record.
- **attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - The unique ID of the package being imported.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp showing when a `content_migrations` record was created.
- **updated\_at** (datetime) - Timestamp of when a `content_migrations` record was updated.
- **overview\_attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - The unique ID of the packages overview.json file.
- **exported\_attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - The unique ID of the resulting exported package.
- **source\_course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The course to copy from for a course copy migration (required if doing course copy).
- **migration\_type** (Annotated\[str, MaxLength(255)] | None) - The type of the migration. Use the Migrator endpoint to see all available migrators. Examples include: `academic_benchmark_importer`, `angel_exporter`, `blackboard_exporter`, `canvas_cartridge_importer`, `common_cartridge_importer`, `course_copy_importer`, `d2l_exporter`, `master_course_import`, `moodle_converter`, `qti_converter`, `webct_scraper`,`zip_file_importer`, `context_external_tool_1234`.
- **migration\_settings** (json | None) - Ruby hash of settings that determine what data will get imported for this migration.
- **started\_at** (datetime | None) - Timestamp showing when a content migration started.
- **finished\_at** (datetime | None) - Timestamp showing when a content migration finished.
- **progress** (float64 | None) - Current migration progress. 100 indicates done at 100%.

## content\_participation\_counts

Shows students a count of the number of submissions they have that have something unread.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a content participation count record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp showing when a content\_participation\_counts record was created.
- **updated\_at** (datetime) - Timestamp showing when a content\_participation\_counts record was updated.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The unique identifier of a content\_participation\_counts's context (course).
- **unread\_count** (int32) - The number of unread actions for this user on this course.

Stores data related to students submission updates or feedback.

Examples include new grade, new excused status, or new score.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a content participation record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of a user.
- **content\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions)) - The unique identifier of a content record.

Provides a link to a content export from a sender to a receiver.

The receiver can use this link to import the content export into any of their courses.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)]) - Name of the content item being shared.
- **id** (int64) - `primary key` The unique identifier of a content share.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The ID of the user who owns the content share.
- **created\_at** (datetime) - Timestamp showing when a `content_share` record was created.
- **updated\_at** (datetime) - Timestamp showing when a `content_share` record was updated.
- **content\_export\_id** (content\_exports) - The ID of the ContentExport containing the content of the share.
- **sender\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the user who sent the content share. Only populated for ReceivedContentShare.

In the context of LTI, joins `context_external_tools` to either `assignments` or to `context_modules`.

Some of the ways to use this table would be to: identify the external tool that is used to submit an assignment, identify the items that are in modules (the IDs in this table are also referred to as `module_item_id`), identify the learning outcome group that an outcome is part of.

**Properties:**

- **created\_at** (datetime) - Timestamp of when a `content_tags` record was created.
- **updated\_at** (datetime) - Timestamp of when a `content_tags` record was updated.
- **context\_type** ([content\_tags\_\_context\_type](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.content_tags__context_type)) - The type of the object represented by `context_id`, typically `Course` or `Account` or `User`.
- **context\_code** (Annotated\[str, MaxLength(255)] | None) - An asset string describing the content tag context (for example: `assignment_3`).
- **comments** (bounded\_str | None) - Comments associated with the tag.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The ID of the migration that created the content tag.
- **context\_module\_id** ([context\_modules](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.context_modules) | None) - The ID of the context module the content tag belongs to (if `tag_type` is `context_module`).
- **learning\_outcome\_id** ([learning\_outcomes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.learning_outcomes) | None) - Has a value if `tag_type` is `learning_outcome`, indicates that the content (`content_type`, `content_id`) is aligned with the given LearningOutcome.
- **mastery\_score** (float64 | None) - when `tag_type` is `learning_outcome` and `content_type` is `AssessmentQuestionBank`, indicates the required score on a set of bank questions to show mastery.
- **rubric\_association\_id** (int64 | None) - (deprecated) when `tag_type` is `learning_outcome` and `content_type` is `Assignment`, indicates the *RubricAssociation* which aligns the *LearningOutcome* to the *Assignment*.
- **associated\_asset\_id** ([learning\_outcome\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.learning_outcome_groups) | None) - Associated asset, whose use varies by ContentTag use. When `tag_type` is `learning_outcome_association`, then `content_type` is `LearningOutcome` and `associated_asset_type` is `learning_outcome_group` and indicates the *LearningOutcome* (`content_id`) is displayed within the *LearningOutcomeGroup* (`associated_asset_id`). When `content_type` is `ContextExternalTool` and `associated_asset_type` is `Lti::ResourceLink`, indicates the resource link associated with an LTI tool link.
- **associated\_asset\_type** ([content\_tags\_\_associated\_asset\_type](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.content_tags__associated_asset_type) | None) - when `tag_type` is `learning_outcome_association`, then `content_type` is `LearningOutcome` and `associated_asset_type` is `learning_outcome_group` and indicates the *LearningOutcome* (`content_id`) is displayed within the *LearningOutcomeGroup* (`associated_asset_id`).
- **link\_settings** (Annotated\[bounded\_str, JsonStringToJsonObject()] | None) - Settings for LTI links associated with the content tag (for example, tool iframe width and height).
- **new\_tab** (bool | None) - Whether or not the content should open in a new tab.
- **position** (int32 | None) - The position of the content tag relative to other content tags when listed in a UI.
- **id** (int64) - `primary key` The unique identifier for a content tag record.
- **content\_type** ([content\_tags\_\_content\_type](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.content_tags__content_type) | None) - The type of the tag's content. Corresponds to the tables that `content_id` is a foreign key for, the exceptions being: `Announcement` (for which `content_id` references the `discussion_topics` table) and `ContextModuleSubheader` and `ExternalUrl` (which have no tables).
- **url** (bounded\_str | None) - The URL of the content where applicable (for example: the launch URL of a context\_external\_tool). Applicable when `content_type` is `ExternalUrl`, `ContextExternalTool` or `Lti::MessageHandler`.
- **title** (bounded\_str | None) - The title of the content tag.

Stores data about installed LTI 1 and 1.3 tools.

**Properties:**

- **developer\_key\_id** ([developer\_keys](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.developer_keys) | None) - The client ID of the tool provider. LTI 1.3 only.
- **created\_at** (datetime) - Timestamp when the activation was created.
- **updated\_at** (datetime) - The time at which the tool was last updated.
- **context\_id** (None | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of the context the tool is deployed to. Identifies either a course (`courses`.`id` if `context_type` is `Course`) or an account (`accounts`.`id` if `context_type` is `Account`).
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported the tool.
- **consumer\_key** (bounded\_str) - A key used by the tool for validation at launch time. This value is set by the Canvas user who installs the tool.
- **cloned\_item\_id** (int64 | None) - The Id of the item in which this context\_external\_tool was cloned from.
- **tool\_id** (Annotated\[str, MaxLength(255)] | None) - The tool ID received from the external tool. May be missing if the tool does not send an ID.
- **not\_selectable** (bool | None) - true - tool is selectable in all scenarios. false - not selectable for assignment or module selection menu.
- **allow\_membership\_service\_access** (bool) - Indicates that the tool has access to the legacy membership service. LTI 1 only. This setting is set by the Canvas user who installs the tool.
- **description** (bounded\_str | None) - The description of the tool activation as entered by the user.
- **name** (Annotated\[str, MaxLength(255)]) - The name of tool activation as entered by the user.
- **id** (int64) - `primary key` Primary key for this record in the `context_external_tools` table in the Canvas database.
- **domain** (Annotated\[str, MaxLength(255)] | None) - The domain for the tool launch URL (optional field). Canvas uses this domain to lookup the correct tool to launch when the tool ID is unknown.
- **url** (Annotated\[str, MaxLength(4096)] | None) - The URL to where the tool may launch to (if this value is NULL, use the `domain` field).
- **unified\_tool\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the tool.

## context\_module\_progressions

Shows which items a student has completed, started and not started in a module.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a user module progression record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp showing when a context\_module\_progressions record was created.
- **updated\_at** (datetime) - Timestamp showing when a context\_module\_progressions record was updated.
- **requirements\_met** (json | None) - Object indicating which requirements have been met.
- **collapsed** (bool | None) - Flag indicating whether modules items are collapsed for user.
- **current\_position** (int32 | None) - For sequential access, this is the current position of the module item (ContentTag).
- **completed\_at** (datetime | None) - Timestamp showing when this user completed this module progression.
- **current** (bool | None) - Flag indicating that this progression is current and not outdated.
- **evaluated\_at** (datetime | None) - Timestamp showing when this progression was last evaluated for completion, lock, or unlock.
- **incomplete\_requirements** (json | None) - Object that contains incomplete requirements related to min\_score.
- **context\_module\_id** ([context\_modules](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.context_modules) | None) - The unique identifier of a associated context\_module.
- **lock\_version** (int32) - Lock version of the module progression.

Modules in Canvas.

A place to link items so that students can proceed through course content in order.

**Properties:**

- **name** (bounded\_str | None) - The name of the module that shows up in the UI.
- **id** (int64) - `primary key` The unique identifier of a module record.
- **deleted\_at** (datetime | None) - Timestamp showing when this record was deleted. If the record has not been deleted, the value will be NULL.
- **created\_at** (datetime) - Timestamp showing when a `context_modules` record was created.
- **updated\_at** (datetime) - Timestamp showing when a `context_modules` record was updated.
- **unlock\_at** (datetime | None) - Module can be locked until this date.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier for the context of `context_modules` (`courses`.`id` if `context_type` is `Course`).
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - An identifier used by the Blueprint system to match with the blueprint content.
- **prerequisites** (json | None) - An object indicating which module(s) must be completed before accessing this one. Has value if course module has prerequisites; field contains ids (context\_modules.id), type and name of prerequisites.
- **completion\_requirements** (json | None) - An object indicating the requirements to complete this module. Contains ids and types (the action required). Requirements can be "must\_mark\_done" , "must\_view", or "must\_contribute".
- **require\_sequential\_progress** (bool | None) - Indicates whether requirements must be completed in sequential order.
- **completion\_events** (bounded\_str | None) - Events that can trigger module completion in CSV format: publish\_final\_grade.
- **requirement\_count** (int32 | None) - The number of requirements to be completed before marking module as complete: can be 1 or NULL for all.
- **position** (int32 | None) - Where the module should fall in the list of modules.

## conversation\_message\_participants

The participants in a certain message in a Conversation.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a conversation recipients record.
- **deleted\_at** (datetime | None) - Timestamp when this record was deleted. If the record has not been deleted the value will be NULL.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **conversation\_message\_id** ([conversation\_messages](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.conversation_messages) | None) - Identifies the messages dataset for the associated message.
- **conversation\_participant\_id** ([conversation\_participants](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.conversation_participants) | None) - Identifies the conversations dataset for the associated conversation.
- **tags** (bounded\_str | None) - Tags used to identify multiple contexts such as course, group, etc.

The messages that belong to a certain Conversation, these are in the *Inbox*.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a conversation message record.
- **created\_at** (datetime | None) - Timestamp of when a `conversation_messages` record was created.
- **context\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | None) - The unique identifier for the context of `conversation_messages` (account, course, user).
- **conversation\_id** ([conversations](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.conversations) | None) - The unique identifier for the conversation.
- **author\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - User ID of the author of the message.
- **generated** (bool | None) - This attribute is true if the system generated this message (e.g. "John was added to this conversation").
- **forwarded\_message\_ids** (bounded\_str | None) - The IDs of any messages that were created as a forward of the current message.
- **media\_comment\_id** (Annotated\[str, MaxLength(255)] | None) - Media comment ID of an audio of video file to be associated with this message.
- **asset\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions) | None) - The ID of an attached asset, such as a submission.
- **attachment\_ids** (bounded\_str | None) - Comma-separated list of attachments ids. These must be files that have been previously uploaded to the sender's "conversation attachments" folder.
- **has\_attachments** (bool | None) - True if the message has attachments.
- **has\_media\_objects** (bool | None) - True if the message has media objects.
- **body** (bounded\_str | None) - The HTML content of the message.

## conversation\_participants

The participants in a Conversation.

**Properties:**

- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of a user.
- **updated\_at** (datetime | None) - Timestamp of when a `conversation_participants` record was updated.
- **has\_attachments** (bool) - If the conversation has attachments.
- **has\_media\_objects** (bool) - If the conversation has media objects associated.
- **last\_message\_at** (datetime | None) - The timestamp of the latest message.
- **subscribed** (bool) - Indicates whether the current user is subscribed to the conversation.
- **message\_count** (int32) - The number of messages in the conversation.
- **label** (Annotated\[str, MaxLength(255)] | None) - Any label applied to the conversation, such as *starred*.
- **id** (int64) - `primary key` The unique identifier for a conversation message participants record.
- **tags** (bounded\_str | None) - Tags used to identify multiple contexts such as course, group, etc.

Conversation threads from the Canvas Inbox.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a conversations record. Links to `conversation_messages.conversation_id`.
- **updated\_at** (datetime | None) - Timestamp of when a conversations record was updated.
- **context\_id** (None | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | [groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.groups)) - The unique identifier for the conversations's context (account, course, user). ID associated with the `context_type`.
- **has\_attachments** (bool) - If the conversation has attachments.
- **has\_media\_objects** (bool) - If the conversation has media objects associated.
- **subject** (Annotated\[str, MaxLength(255)] | None) - The subject line of the conversation.
- **tags** (bounded\_str | None) - Tags used to identify multiple contexts such as course, group, etc. Contains a comma-delimited list of IDs of the course or group if the conversation is associated with a course or group. The format of the values are `course_12345` or `group_12345`.

## course\_account\_associations

An explicit place to keep track of all the the accounts in the account hierarchy that a course belongs to.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a course account association record.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - Identifies the course.
- **created\_at** (datetime) - Timestamp of when the record was created.
- **updated\_at** (datetime) - Timestamp of when the record was updated.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - Identifies the accounts dataset. Points to the account associated with the course. Could be Canvas root account or sub-account ID.
- **course\_section\_id** ([course\_sections](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.course_sections) | None) - Identifies the course section.
- **depth** (int32) - How many steps in the account chain are between the courses' direct account (`course`.`account_id`) and the `account_id` of the association.

Stores attributes for a section of a course.

Sections are a group of students that have been organized for administrative purposes. When users are enrolled in a course, they are actually enrolled in one of the sections of that course. It is possible to place more than one section in course, but it is not possible to put sections within sections. All sections of a course share the same content. If a course is taught by one instructor, sections can remain under one course. However, if each section is taught by a different instructor, those sections will need to be housed under separate courses. Each section can have its own varied due dates for assignments, quizzes, and discussions. For example, a course may have sections that meet on different days of the week or in different formats (online vs. face-to-face). Sections are also beneficial when Teacher Assistants are assigned to help manage courses and oversee grading for a portion of a course enrollment. As part of SIS or manual enrollments, you can limit students to only see students in their section. Instructors can also limit students if you allow them to manually enroll users in their own courses.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)]) - The name of the section.
- **id** (int64) - `primary key` The unique identifier for the section.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique Canvas identifier for the course in which the section belongs.
- **integration\_id** (Annotated\[str, MaxLength(255)] | None) - The integration ID of the section. This field is only included if there is an integration set up between CanvaS and SIS.
- **created\_at** (datetime) - Timestamp for when this section was entered into the system.
- **updated\_at** (datetime) - Timestamp for when the last time the section was updated.
- **sis\_batch\_id** (sis\_batches | None) - The unique identifier for the SIS import if created through SIS.
- **start\_at** (datetime | None) - The start date for the section, if applicable. When a user is allowed to participate in a course, enrollment term dates, course dates, and course section dates flow together in all aspects of Canvas. Various dates allow different users to participate in the course. The hierarchy of dates are: course section dates override course dates, course dates override term dates.
- **end\_at** (datetime | None) - The end date for the section, if applicable. When a user is allowed to participate in a course.
- **sis\_source\_id** (Annotated\[str, MaxLength(255)] | None) - Id for the correlated record for the section in the SIS (assuming SIS integration has been properly configured).
- **default\_section** (bool | None) - True if this is the default section.
- **accepting\_enrollments** (bool | None) - True if this section is open for enrollment.
- **restrict\_enrollments\_to\_section\_dates** (bool | None) - Restrict user enrollments to the start and end dates of the section. True when "Users can only participate in the course between these dates" is checked.
- **nonxlist\_course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The unique identifier of the original course of a cross-listed section.
- **enrollment\_term\_id** ([enrollment\_terms](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.enrollment_terms) | None) - Identifies the associated enrollment term.

Stores attributes for a course.

**Properties:**

- **storage\_quota** (int64 | None) - The total amount of storage space (in bytes) allowed to be used by files in the course.
- **integration\_id** (Annotated\[str, MaxLength(255)] | None) - the integration identifier for the course, if defined.
- **lti\_context\_id** (Annotated\[str, MaxLength(255)] | None) - UUID of the Canvas context in LTI standard. secondary ID for this context, could be used in API to identify resource as well.
- **sis\_batch\_id** (int64 | None) - The unique identifier for the SIS import.
- **created\_at** (datetime) - The date the course was created.
- **updated\_at** (datetime) - The time the course was last updated.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - Points to the account associated with the course.
- **grading\_standard\_id** ([grading\_standards](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.grading_standards) | None) - The grading standard associated with the course.
- **start\_at** (datetime | None) - The start date for the course, if applicable. If NULL, then use `start_at` value from `enrollment_terms` table. Enrollment term dates, course dates, and course section dates flow together in all aspects of Canvas. Various dates allow different users to participate in the course. The hierarchy of dates are: course section dates override course dates, course dates override term dates.
- **sis\_source\_id** (Annotated\[str, MaxLength(255)] | None) - The SIS identifier for the course, if defined.
- **group\_weighting\_scheme** (Annotated\[str, MaxLength(255)] | None) - Whether final grades will be weighted based on the `group_weight` value of assignment groups `percent` if weighted `equal` or NULL otherwise.
- **conclude\_at** (datetime | None) - The end date for the course, if applicable. If NULL, then use `start_at` value from `enrollment_terms` table.
- **is\_public** (bool | None) - True if the course is publicly visible.
- **allow\_student\_wiki\_edits** (bool | None) - Whether Pages in the course can be created and are editable by students.
- **syllabus\_body** (bounded\_str | None) - User-generated HTML for the course syllabus.
- **default\_wiki\_editing\_roles** (Annotated\[str, MaxLength(255)] | None) - Comma-separated list used as the default `editing_roles` value for new `wiki_pages` in the course.
- **wiki\_id** ([wikis](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.wikis) | None) - Foreign key to the `wikis` dataset.
- **allow\_student\_organized\_groups** (bool) - Whether students are able to organize their own groups.
- **course\_code** (Annotated\[str, MaxLength(255)] | None) - The course code.
- **default\_view** (Annotated\[str, MaxLength(255)] | None) - the type of page that users will see when they first visit the course - `feed`: Recent Activity Dashboard - `wiki`: Wiki Front Page - `modules`: Course Modules/Sections Page - `assignments`: Course Assignments List - `syllabus`: Course Syllabus Page other types may be added in the future.
- **abstract\_course\_id** (abstract\_courses | None) - Foreign key to the `abstract_courses` table.
- **enrollment\_term\_id** ([enrollment\_terms](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.enrollment_terms)) - The enrollment term associated with the course.
- **open\_enrollment** (bool | None) - Whether the course has enabled open enrollment.
- **tab\_configuration** (Annotated\[bounded\_str, YamlStringToJsonObject(), SpecialConversion()] | None) - A JSON serialized list detailing the order and visibility status of tabs in the left-hand navigation for the course.
- **turnitin\_comments** (bounded\_str | None) - Comments to be shown to students when submitting a Turnitin-enabled assignment.
- **self\_enrollment** (bool | None) - Whether the course has enabled self enrollment.
- **license** (Annotated\[str, MaxLength(255)] | None) - The default license for content in the course; `private`: Private (Copyrighted), `public_domain`: Public Domain, `cc_by`: CC Attribution, `cc_by_sa`: CC Attribution Share Alike, `cc_by_nc`: CC Attribution Noncommercial, `cc_by_nc_sa`: CC Attribution Noncommercial Share Alike, `cc_by_nd`: CC Attribution No Derivatives, `cc_by_nc_nd`: CC Attribution Noncommercial No Derivatives.
- **indexed** (bool | None) - Whether the course is included in the public course index.
- **restrict\_enrollments\_to\_course\_dates** (bool | None) - Whether the course's start and end dates will override dates from the term when determining user access.
- **template\_course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - If set, this course was originally created via SIS when a section was marked to be cross listed to a non-existent course, using attributes from the original section's course and setting that course ID here.
- **replacement\_course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The ID of the course created to replace this one when it had its content reset.
- **public\_description** (bounded\_str | None) - The public description of the course.
- **self\_enrollment\_code** (Annotated\[str, MaxLength(255)] | None) - The alpha-numeric code students can use to enroll in the course through self enrollment.
- **self\_enrollment\_limit** (int32 | None) - The number of students that can enroll in the course through self enrollment.
- **turnitin\_id** (int64 | None) - A unique identifier for use with Turnitin.
- **show\_announcements\_on\_home\_page** (bool | None) - Whether announcements will be shown on the course home page.
- **home\_page\_announcement\_limit** (int32 | None) - The maximum number of announcements to show on the course home page.
- **latest\_outcome\_import\_id** (int64 | None) - The ID of the most recent Outcome Import for the course.
- **grade\_passback\_setting** (Annotated\[str, MaxLength(255)] | None) - The grade\_passback\_setting set on the course.
- **template** (bool) - Course is marked as a template for accounts to use.
- **homeroom\_course** (bool) - Course is marked as a homeroom course.
- **sync\_enrollments\_from\_homeroom** (bool) - Enrollments for this course will be synced from the associated homeroom.
- **homeroom\_course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - Points to the homeroom course from which this course receives its enrollments.
- **locale** (Annotated\[str, MaxLength(255)] | None) - The course-set locale, if applicable.
- **name** (Annotated\[str, MaxLength(255)] | None) - The full name of the course.
- **id** (int64) - `primary key` The unique identifier for the course.
- **time\_zone** (Annotated\[str, MaxLength(255)] | None) - The course's IANA time zone name.
- **uuid** (Annotated\[str, MaxLength(255)] | None) - The UUID of the course.
- **settings** (Annotated\[[courses\_\_settings](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.courses__settings), YamlStringToJsonObject()] | None) - Miscellaneous settings for the course.

## custom\_gradebook\_column\_data

Contains per-user data for the custom columns defined in custom\_gradebook\_columns.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a custom gradebook column data record.
- **content** (Annotated\[str, MaxLength(255)]) - The particular value of the specified column for the user denoted by user\_id.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of the user to whom this data record applies.

Contains configuration information for custom Gradebook columns defined for specific courses.

**Properties:**

- **created\_at** (datetime) - Timestamp of when a custom\_gradebook\_columns record was created.
- **updated\_at** (datetime) - Timestamp of when a custom\_gradebook\_columns record was updated.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of the course that defines this column.
- **teacher\_notes** (bool) - True if this column represents the predefined *Notes* column in Gradebook.
- **position** (int32) - The ordering of this column among the columns defined for this course.
- **id** (int64) - `primary key` The unique identifier for a custom Gradebook column data definition.
- **read\_only** (bool) - If true, the contents of this column cannot be edited from Gradebook.
- **title** (Annotated\[str, MaxLength(255)]) - The title of the column, as displayed in Gradebook.

## developer\_key\_account\_bindings

Joins the accounts table to developer\_keys.

Describes if the associated developer key is "on" or "off" for the associated account.

**Properties:**

- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - Points to the account associated with the course. Could be Canvas root account or sub-account ID.
- **created\_at** (datetime) - Timestamp of when a developer\_key\_account\_bindings record was created.
- **updated\_at** (datetime) - Timestamp of when a developer\_key\_account\_bindings record was updated.
- **developer\_key\_id** ([developer\_keys](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.developer_keys)) - The ID of the associated developer key.
- **id** (int64) - `primary key` The unique identifier for a developer key and account association record.

A table representing a set of credentials used for API access.

Contains both normal API keys and the LTI keys used in LTI 1.3 apps.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - The name of the developer key.
- **id** (int64) - `primary key` The unique identifier for a developer key record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp of when a `developer_keys` record was created.
- **updated\_at** (datetime) - Timestamp of when a `developer_keys` record was updated.
- **scopes** (json | None) - The list of scopes the developer key's access tokens may use.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | None) - Points to the account associated with the course. Could be Canvas root account or sub-account ID.
- **redirect\_uri** (Annotated\[str, MaxLength(255)] | None) - (legacy) The valid redirect URI for the developer key.
- **icon\_url** (Annotated\[str, MaxLength(255)] | None) - A URL pointing to the icon of the developer key.
- **redirect\_uris** (List\[Annotated\[str, MaxLength(255)]]) - The list of valid redirect URIs for the developer key.
- **notes** (bounded\_str | None) - Any notes added to the developer key.
- **access\_token\_count** (int32) - The number of times the developer key has been used.
- **require\_scopes** (bool) - Whether or not access token for the developer key are required to be scoped.
- **test\_cluster\_only** (bool) - If true, the developer key's access tokens are only valid on Canvas test and beta instances.
- **public\_jwk** (bounded\_str | None) - The public key (in JWK format) for the developer key. Used if the developer key is associated with an LTI 1.3 tool.
- **allow\_includes** (bool) - If true, requests made with this key's access token can use "includes" parameters to retrieve additional data in each request.
- **is\_lti\_key** (bool) - If true, the developer key is intended to be used with LTI 1.3 tools.
- **client\_credentials\_audience** (bounded\_str | None) - The intended audience of client credentials issued by the developer key. If internal (default), credentials will be verified by Canvas; if external, credentials will be verified by other parties using Canvas' public key.
- **email** (Annotated\[str, MaxLength(255)] | None) - The email address of the developer key's owner.
- **user\_name** (Annotated\[str, MaxLength(255)] | None) - the login ID of the user who originated developer key.

Stores attributes for discussion entries.

Discussion entries are replies in a discussion topic.

**Properties:**

- **message** (bounded\_str | None) - The content of the entry. Contains html tags.
- **id** (int64) - `primary key` The unique identifier for the entry.
- **attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - Representation of the attachment for the entry, if any. Present only if there is an attachment.
- **deleted\_at** (datetime | None) - Timestamp when the discussion entry was deleted.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique identifier for the author of the entry.
- **created\_at** (datetime) - The creation time of the entry.
- **updated\_at** (datetime) - The updated time of the entry, in ISO8601 format.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported the entry.
- **discussion\_topic\_id** ([discussion\_topics](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.discussion_topics) | None) - The ID of the discussion topic that this entry is part of.
- **parent\_id** ([discussion\_entries](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.discussion_entries) | None) - The parent discussion entry ID of this discussion entry. Has a value if the entry is a reply to another entry.
- **editor\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique user ID of the person to last edit the entry, if different than user\_id.
- **root\_entry\_id** ([discussion\_entries](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.discussion_entries) | None) - The root discussion entry ID that this entry is a part of. Has a value if the entry is a reply to another entry.
- **depth** (int32 | None) - Reply depth for this entry.
- **rating\_count** (int32 | None) - Rating count is the amount of people who have submitted a rating on a given discussion with the only rating being "like".
- **rating\_sum** (int32 | None) - The rating sum is the sum of the ratings which occurred.

## discussion\_entry\_participants

Tracks who has read a particular entry.

**Properties:**

- **id** (int64) - `primary key` The Id of the discussion entry participant.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The ID of the user who participated in this discussion entry.
- **forced\_read\_state** (bool | None) - Allows for users to force a discussion entry to be unread.
- **discussion\_entry\_id** ([discussion\_entries](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.discussion_entries)) - The ID of the discussion entry that this participant participated in.
- **rating** (int32 | None) - It is a number of 0 or 1 that indicates the rating providing to the linked entry.

## discussion\_topic\_participants

Links discussion topics to the users who have posted in them.

If a user has posted to a discussion topic, there will be a row in this table.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a discussion topic participants record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of a user.
- **subscribed** (bool | None) - Flag indicating that user is subscribed to discussion and will receive notifications for new comments.
- **unread\_entry\_count** (int32) - The count of discussion entries that this user has not yet read.
- **discussion\_topic\_id** ([discussion\_topics](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.discussion_topics)) - The unique identifier of a discussion topic record.

This table stores attributes for discussion topics in Canvas.

Discussion topics are logical discussion threads. They can have many discussion entries. They also have their own message text for the message that started the topic.

**Properties:**

- **message** (bounded\_str | None) - The HTML content of the message body.
- **id** (int64) - `primary key` The ID of this topic.
- **attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - Has a value if the discussion topic is associated with an attachment (file).
- **deleted\_at** (datetime | None) - Timestamp when the discussion topic was deleted.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The username of the topic creator.
- **created\_at** (datetime) - The date the discussion topic was made.
- **updated\_at** (datetime) - The date the discussion topic was updated.
- **lock\_at** (datetime | None) - The datetime to lock the topic (if ever).
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | [groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.groups)) - The ID of the context that this discussion is used in, e.g. `courses`.`id` if `context_type` is `Course`.
- **locked** (bool) - Whether or not the discussion is *closed for comments*.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - The unique identifier of the assignment if the topic is for grading, otherwise NULL.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported this discussion topic.
- **group\_category\_id** ([group\_categories](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.group_categories) | None) - The unique identifier of the group category if the topic is a group discussion, otherwise NULL.
- **cloned\_item\_id** (cloned\_items | None) - The ID of the item in which this discussion topic was cloned from.
- **last\_reply\_at** (datetime | None) - The datetime for when the last reply was in the topic.
- **delayed\_post\_at** (datetime | None) - The datetime to publish the topic (if not right away).
- **posted\_at** (datetime | None) - The datetime the topic was posted. If it is NULL it hasn't been posted yet.
- **root\_topic\_id** ([discussion\_topics](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.discussion_topics) | None) - If the topic is for grading and a group assignment this will point to the original topic in the course.
- **old\_assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - the assignment ID after you change a topic from graded to ungraded, then restores the old one if it goes back to graded.
- **subtopics\_refreshed\_at** (datetime | None) - The time at which the subtopics for a group category discussion was refreshed at.
- **external\_feed\_id** (external\_feeds | None) - The ID of the external feed that this discussion topic was created from.
- **podcast\_enabled** (bool) - Boolean to determine if the podcast is enabled.
- **podcast\_has\_student\_posts** (bool) - If true, the podcast will include posts from students as well. Implies podcast\_enabled.
- **require\_initial\_post** (bool) - If true then a user may not respond to other replies until that user has made an initial reply.
- **editor\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the editor of the discussion.
- **pinned** (bool) - Whether or not the discussion has been *pinned* by an instructor.
- **allow\_rating** (bool) - Whether or not users can rate entries in this topic.
- **only\_graders\_can\_rate** (bool) - Whether or not grade permissions are required to rate entries.
- **sort\_by\_rating** (bool) - Whether or not entries should be sorted by rating.
- **todo\_date** (datetime | None) - Date in which discussion topic will show up in the student planner feature.
- **is\_section\_specific** (bool) - Boolean distinguishing if the topic is a section specific topic or not.
- **position** (int32 | None) - The position on the discussions index page under pinned items.
- **title** (Annotated\[str, MaxLength(255)] | None) - The topic title.

## enrollment\_dates\_overrides

Supports allowing certain roles to have access to a term outside of term date boundaries.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for an enrollment date override record.
- **created\_at** (datetime) - Timestamp of when a enrollment\_dates\_overrides record was created.
- **updated\_at** (datetime) - Timestamp of when an enrollment\_dates\_overrides record was updated.
- **context\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - The unique ID of main Canvas account, always a root account ID in this table.
- **start\_at** (datetime | None) - The start time of the enrollment.
- **end\_at** (datetime | None) - The end datetime for the enrollment date override, if applicable.
- **enrollment\_term\_id** ([enrollment\_terms](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.enrollment_terms) | None) - The unique identifier for the enrollment term.

Stores the state of an enrollment.

**Properties:**

- **updated\_at** (datetime | None) - Timestamp of when an `enrollment_states` record was updated.
- **state\_is\_current** (bool) - Indicates if the enrollment state is current or needs recalculation.
- **state\_started\_at** (datetime | None) - Indicates the date that the enrollment state should take effect.
- **state\_valid\_until** (datetime | None) - Indicates the date that the enrollment state becomes stale.
- **restricted\_access** (bool) - Indicates if the enrollment is allowed to view the course.
- **access\_is\_current** (bool) - Indicates if the state is within the start and valid until bounds.
- **enrollment\_id** (int64) - `primary key` The ID of the enrollment.

Stores enrollment term records that describe the term or semester associated with courses (e.g. Fall 2013).

Use the dates in this table as a proxy for the course start/end dates if the `start_at` and `end_at` fields in the courses table are NULL.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - The name of the term.
- **id** (int64) - `primary key` The unique identifier for the enrollment term.
- **integration\_id** (Annotated\[str, MaxLength(255)] | None) - The ID of the enrollment term in the external tools or SIS, this ID usually gets populated via API or SIS import.
- **created\_at** (datetime) - Timestamp of when the enrollment term was created.
- **updated\_at** (datetime) - Timestamp of when the enrollment term was last updated.
- **sis\_batch\_id** (sis\_batches | None) - The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information.
- **start\_at** (datetime | None) - The datetime of the start of the term. Set up by the administrator. Enrollment term dates, course dates, and course section dates flow together in all aspects of Canvas; various dates allow different users to participate in the course. The hierarchy of dates are: course section dates override course dates, course dates override term dates.
- **end\_at** (datetime | None) - The datetime of the end of the term. Set up by the administrator.
- **sis\_source\_id** (Annotated\[str, MaxLength(255)] | None) - The SIS ID of the term. Only included if the user has permission to view SIS information.
- **term\_code** (Annotated\[str, MaxLength(255)] | None) - Enrollment term code as viewed in the UI.

This table stores user enrollments.

An enrollment represents a user's association with a specific course and section. There may be multiple records associated with a `course_id` and `user_id` combination (records are unique on: `course_id`, `user_id`, `course_section_id`, `role_id`, `workflow_state`, `associated_user_id`).

**Properties:**

- **sis\_batch\_id** (sis\_batches | None) - The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of the user.
- **created\_at** (datetime) - The created time of the enrollment.
- **updated\_at** (datetime) - The updated time of the enrollment.
- **role\_id** ([roles](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.roles)) - The ID of the enrollment role.
- **start\_at** (datetime | None) - The start time of the enrollment, in ISO8601 format.
- **end\_at** (datetime | None) - The end time of the enrollment, in ISO8601 format.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique ID of the course.
- **completed\_at** (datetime | None) - Enrollment completed date.
- **course\_section\_id** ([course\_sections](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.course_sections)) - The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information.
- **grade\_publishing\_status** (Annotated\[str, MaxLength(255)]) - Used internally with grade passback functionality.
- **associated\_user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of the associated user. Will be NULL unless type is ObserverEnrollment.
- **self\_enrolled** (bool | None) - Enrollment was created via self-enrollment.
- **limit\_privileges\_to\_course\_section** (bool) - User can only access his or her own course section.
- **last\_activity\_at** (datetime | None) - The last activity time of the user for the enrollment. This time stamp updates when a user navigates through the course using the Course Navigation menu, replies to a discussion or submits an assignment or quiz, and when they access course files and pages (does not include mobile interactions or group participation).
- **total\_activity\_time** (int32 | None) - The total activity time of the user for the enrollment, in seconds. If user is viewing a page and is enrolled in that particular course, then the time is incremented. Requires at least 2 minutes, but not more than 10 (e.g. if a student just checks their grade or due date and was on the page for less than 2 min, it doesn't get counted). May not be incremented for page views through mobile app (will get incremented for page views through mobile browser); does not include group activity or page views for videos that do not include intermediate page requests, such as a half-hour recorded lecture.
- **sis\_pseudonym\_id** ([pseudonyms](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.pseudonyms) | None) - If enrolled via SIS import, which pseudonym was referenced to create this enrollment. It is the user ID that was referenced when an enrollment was created via SIS. it's used for some LTI calls to try and send consistent IDs. also used for splitting accidentally-merged-users to decide which way the enrollments should go.
- **last\_attended\_at** (datetime | None) - The last attended date of the user for the enrollment in a course. The UI facing field that could be set by an end user or API call.
- **id** (int64) - `primary key` The ID of the enrollment.

A record of items that a user has favorited, such as a Course.

This affects how items are displayed in places like the Dashboard.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a favorite record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp of when a favorites record was created.
- **updated\_at** (datetime) - Timestamp of when a favorites record was updated.
- **context\_id** (None | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | [groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.groups)) - The unique identifier for the favorites's context (account, course, user).
- **context\_type** ([favorites\_\_context\_type](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.favorites__context_type)) - The type of the object represented by `context_id`, typically `Course` or `Account` or `User`.

A collection of files (attachments).

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - Name of the folder.
- **id** (int64) - `primary key` The unique identifier for a folder record.
- **full\_name** (bounded\_str | None) - Full path of the folder.
- **deleted\_at** (datetime | None) - Timestamp when this record was deleted. If the record has not been deleted the value will be NULL.
- **created\_at** (datetime) - Timestamp of when a folders record was created.
- **updated\_at** (datetime) - Timestamp of when a folders record was updated.
- **workflow\_state** ([folders\_\_workflow\_state](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.folders__workflow_state)) - In this context the workflow state indicates the visibility of the folder.
- **unlock\_at** (datetime | None) - Indicates the date at which this folder should become accessible.
- **lock\_at** (datetime | None) - Indicates the date at which this folder should no longer be accessible.
- **locked** (bool | None) - Indicates if the folder is currently accessible \[NULL=false].
- **cloned\_item\_id** (cloned\_items | None) - Unique identifier of the folder that this folder was cloned from.
- **submission\_context\_code** (Annotated\[str, MaxLength(255)] | None) - A value indicating the context to which this folder should be submitted if it is for a submission.
- **parent\_folder\_id** ([folders](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.folders) | None) - Id of the parent folder.
- **unique\_type** ([folders\_\_unique\_type](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.folders__unique_type) | None) - Value indicating what kind of files are stored in this folder. NULL is the most common value, meaning this is a standard folder. `media` is a special case where media files are stored.
- **position** (int32 | None) - An integer value used for sorting the order in which the folder is listed.

Stores attributes for grading period groups, which are a group of grading periods.

**Properties:**

- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | None) - Points to the account associated with the group.
- **created\_at** (datetime) - Timestamp when record was created.
- **updated\_at** (datetime) - Timestamp when record was last updated.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - Identifies the course.
- **weighted** (bool | None) - Whether to weight individual grading periods within this grading group.
- **display\_totals\_for\_all\_grading\_periods** (bool) - If set, shows the option to display the totals for all grading periods within this group on the student grades page and the gradebook.
- **id** (int64) - `primary key` Primary key for the grading period groups.
- **title** (Annotated\[str, MaxLength(255)] | None) - The title for this grading period group.

Stores attributes for grading period.

A Grading period is like a "term", essentially used for splitting up the grade book into "periods".

**Properties:**

- **created\_at** (datetime) - Timestamp when record was created.
- **updated\_at** (datetime) - Timestamp when record was last updated.
- **start\_date** (datetime) - The start date of the grading period.
- **end\_date** (datetime) - The end date of the grading period.
- **close\_date** (datetime | None) - Grades can only be changed before this close date of the grading period.
- **id** (int64) - `primary key` The unique identifier for the grading period.
- **title** (Annotated\[str, MaxLength(255)] | None) - The title for the grading period.
- **weight** (float64 | None) - A weight value that contributes to the overall weight of a grading period set, used to calculate how much assignments in this period contribute to the total grade.

Contains data for grading schemes defined for a course or account.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a grading standard record.
- **version** (int32 | None) - Either 1 or 2, as noted in the definition of `data`.
- **context\_code** (Annotated\[str, MaxLength(255)] | None) - A value in string form representing the associated context (e.g., `course_5`).
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the user who created this grading standard.
- **created\_at** (datetime) - Timestamp of when a `grading_standards` record was created.
- **updated\_at** (datetime) - Timestamp of when a `grading_standards` record was updated.
- **context\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of the account or course to which this grading standard belongs.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The ID of the associated migration, if this grading standard was created via a content migration.
- **title** (Annotated\[str, MaxLength(255)] | None) - The name for this grading standard.
- **data** (json | None) - A stringified array representing the content of this grading standard. If the `version` column is 1, each element is a tuple containing a letter grade and the maximum value for that letter grade. If the `version` column is 2, each element is a tuple containing a letter grade and the minimum value for that letter grade.

A container for a set of groups, since often you want everyone to be in exactly one group in a set.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - The display name of the group category.
- **id** (int64) - `primary key` The unique identifier for a group category record.
- **deleted\_at** (datetime | None) - Timestamp when this record was deleted. If the record has not been deleted the value will be NULL.
- **created\_at** (datetime | None) - Timestamp of when a `group_categories` record was created.
- **updated\_at** (datetime | None) - Timestamp of when a `group_categories` record was updated.
- **sis\_batch\_id** (sis\_batches | None) - The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information.
- **context\_id** (None | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier for the context of `group_categories` (account, course, user).
- **sis\_source\_id** (bounded\_str | None) - The unique identifier for this group in the customer SIS.
- **role** ([group\_categories\_\_role](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.group_categories__role) | None) - Certain types of group categories have special role designations. Currently, these include: `communities`, `student_organized`, and `imported`. Regular course/account group categories have a role of NULL.
- **self\_signup** (Annotated\[str, MaxLength(255)] | None) - If the group category allows users to join a group themselves, thought they may only be a member of one group per group category at a time. Values include `restricted`, `enabled`, and NULL. `enabled` allows students to assign themselves to a group, `restricted` restricts them to only joining a group in their section, NULL disallows students from joining groups.
- **group\_limit** (int32 | None) - If self-signup is enabled, this field can be set to cap the number of users in each group. If NULL, there is no limit.
- **auto\_leader** (Annotated\[str, MaxLength(255)] | None) - Gives instructors the ability to automatically have group leaders assigned. Values include `random`, `first`, and NULL; `random` picks a student from the group at random as the leader, `first` sets the first student to be assigned to the group as the leader.
- **non\_collaborative** (bool | None) - Whether or not is collaborative.

A join table of users and groups. Like enrollments, but for groups instead of courses.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a group membership record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The ID of the user object to which the membership belongs.
- **created\_at** (datetime) - Timestamp of when a `group_memberships` record was created.
- **updated\_at** (datetime) - Timestamp of when a `group_memberships` record was updated.
- **sis\_batch\_id** (sis\_batches | None) - The ID of the SIS import if created through SIS. Only included if the user has permission to manage SIS information.
- **group\_id** ([groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.groups)) - The ID of the group object to which the membership belongs.
- **moderator** (bool | None) - Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate).
- **uuid** (Annotated\[str, MaxLength(255)]) - UUID for a membership record.

Stores attributes for groups in canvas.

Groups contain two or more students enrolled in a particular course working on an assignment or project together.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - The display name of the group.
- **id** (int64) - `primary key` The ID of the group.
- **deleted\_at** (datetime | None) - Timestamp when the group was deleted.
- **storage\_quota** (int64 | None) - The storage quota for the group.
- **lti\_context\_id** (Annotated\[str, MaxLength(255)] | None) - UUID of the Canvas context in LTI standard. secondary ID for this context, could be used in API to identify resource as well.
- **created\_at** (datetime) - Timestamp when the group was first saved in the system.
- **updated\_at** (datetime) - Timestamp when the group was last updated in the system.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - Identifies the associated account, groups could be owned by sub-accounts.
- **sis\_batch\_id** (sis\_batches | None) - The ID of the SIS import if created through SIS.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - The ID of the context (account or course) this group belongs too. See also: context\_type.
- **context\_type** ([groups\_\_context\_type](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.groups__context_type)) - The course or account that the group belongs to. The pattern here is that whatever the `context_type` is, there will be an `_id` field named after that type. So if instead `context_type` was `account`, the `course_id` field would be replaced by an `account_id` field.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported this group.
- **sis\_source\_id** (Annotated\[str, MaxLength(255)] | None) - The SIS ID of the group.
- **is\_public** (bool | None) - Whether or not the group is public. Currently only community groups can be made public. Also, once a group has been set to public, it cannot be changed back to private.
- **wiki\_id** ([wikis](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.wikis) | None) - The ID of an associated wiki page.
- **max\_membership** (int32 | None) - The maximum number of participating users in the group.
- **join\_level** (Annotated\[str, MaxLength(255)] | None) - How people are allowed to join the group. For all groups except for community groups, the user must share the group's parent course or account. For student organized or community groups, where a user can be a member of as many or few as they want, the applicable levels are `parent_context_auto_join`, `parent_context_request`, and `invitation_only`. For class groups, where students are divided up and should only be part of one group of the category, this value will always be `invitation_only`, and is not relevant. If `parent_context_auto_join`, anyone can join and will be automatically accepted. If `parent_context_request`, anyone can request to join, which must be approved by a group moderator. If `invitation_only`, only those how have received an invitation my join the group, by accepting that invitation.
- **avatar\_attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - Foreign key to the `attachments` table for the avatar of this group.
- **leader\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - Foreign key to the `users` table for the leader of this group.
- **description** (bounded\_str | None) - A description of the group.
- **uuid** (Annotated\[str, MaxLength(255)]) - The UUID of the group.
- **non\_collaborative** (bool | None) - Whether or not is collaborative.

Contains late/missing policy configurations for courses.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a late policy record.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of the course this late policy references.
- **created\_at** (datetime) - Timestamp of when a `late_policies` record was created.
- **updated\_at** (datetime) - Timestamp of when a `late_policies` record was updated.
- **missing\_submission\_deduction\_enabled** (bool) - Whether to apply a deduction for submissions that have not been submitted as of their due date.
- **missing\_submission\_deduction** (Annotated\[Decimal, Precision(5, 2)]) - The amount to award for a missing submission, expressed as a percentage (from 0 to 100) of the assignment's possible points.
- **late\_submission\_deduction\_enabled** (bool) - Whether to apply a deduction for submissions submitted late.
- **late\_submission\_deduction** (Annotated\[Decimal, Precision(5, 2)]) - The amount to deduct from the submission for each interval it is late, expressed as a percentage (from 0 to 100) of the assignment's possible points.
- **late\_submission\_interval** (Annotated\[str, MaxLength(16)]) - The interval at which points should be deducted: valid values are `day` and `hour`.
- **late\_submission\_minimum\_percent\_enabled** (bool) - True if the points deducted for lateness should be capped.
- **late\_submission\_minimum\_percent** (Annotated\[Decimal, Precision(5, 2)]) - If late\_submission\_minimum\_percent\_enabled is true, prevents late deductions from bringing a submission below this percentage of the total points. A value between 0 and 100.

Learning outcome groups organize outcomes hierarchically within a context, such as an account, course or the global context.

This table contains dimensions for learning outcome groups.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a learning outcome group record.
- **created\_at** (datetime) - Timestamp of when a learning\_outcome\_groups record was created.
- **updated\_at** (datetime) - Timestamp of when a learning\_outcome\_groups record was updated.
- **context\_id** (None | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier for the learning\_outcome\_groups's context (account, course).
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - A GUID used to resolve outcomes during import and migration.
- **learning\_outcome\_group\_id** ([learning\_outcome\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.learning_outcome_groups) | None) - ID associated with the parent of this group (NULL if it does not have parent). Refers to a learning\_outcome\_group record.
- **root\_learning\_outcome\_group\_id** ([learning\_outcome\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.learning_outcome_groups) | None) - ID associated with the root group in the group hierarchy (NULL if it is the root). Refers to a learning\_outcome\_group record.
- **vendor\_guid** (Annotated\[str, MaxLength(255)] | None) - A custom GUID for the learning standard.
- **outcome\_import\_id** (outcome\_imports | None) - Foreign key to the outcome import associated with this outcome group, if this group was imported.
- **source\_outcome\_group\_id** ([learning\_outcome\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.learning_outcome_groups) | None) - Foreign key to the learning outcome group that the group was copied from.
- **description** (bounded\_str | None) - Description of the learning outcome group.
- **title** (Annotated\[str, MaxLength(255)]) - Title of the learning outcome group.

## learning\_outcome\_question\_results

Attributes for the results of answered questions which have been associated with a learning outcome.

**Properties:**

- **created\_at** (datetime) - Timestamp of when a learning\_outcome\_question\_results record was created.
- **updated\_at** (datetime) - Timestamp of when a learning\_outcome\_question\_results record was updated.
- **learning\_outcome\_id** ([learning\_outcomes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.learning_outcomes) | None) - Foreign key to the learning outcome this record is associated with.
- **associated\_asset\_id** ([assessment\_questions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assessment_questions) | None) - Polymorphic foreign key to the associated asset (currently always Assessment Question) used to generate this result.
- **score** (float64 | None) - The student's score.
- **possible** (float64 | None) - Total number of points possible.
- **mastery** (bool | None) - Boolean indicating whether user achieved mastery.
- **attempt** (int32 | None) - The total number of attempts, or submissions.
- **original\_score** (float64 | None) - Score on the first attempt.
- **original\_possible** (float64 | None) - Possible points on the first attempt.
- **original\_mastery** (bool | None) - Boolean indicating whether user achieved mastery.
- **assessed\_at** (datetime | None) - Time when answer was assessed.
- **submitted\_at** (datetime | None) - Time when answer was submitted.
- **id** (int64) - `primary key` The unique identifier for a learning outcome question result record.
- **percent** (float64 | None) - Score's percent of maximum points possible for outcome, scaled to reflect any custom mastery levels that differ from the learning outcome.
- **title** (bounded\_str | None) - Title for identifying the question result.

Learning outcome results are a student's mastery score on a given outcome.

This table contains dimensions for learning outcome results.

**Properties:**

- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user who made the submission.
- **created\_at** (datetime) - Timestamp of when a learning\_outcome\_results record was created.
- **updated\_at** (datetime) - Timestamp of when a learning\_outcome\_results record was updated.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The unique identifier for the learning\_outcome\_results's context (account, course, user).
- **context\_code** (Annotated\[str, MaxLength(255)] | None) - Alternate specification of learning outcome result context as single string.
- **learning\_outcome\_id** ([learning\_outcomes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.learning_outcomes) | None) - Identifies the learning outcome this result is associated with.
- **score** (float64 | None) - The student's score.
- **possible** (float64 | None) - Total number of points possible.
- **mastery** (bool | None) - Boolean indicating whether user achieved mastery.
- **attempt** (int32 | None) - The total number of attempts, or submissions.
- **original\_score** (float64 | None) - Score on the first attempt.
- **original\_possible** (float64 | None) - Possible points on the first attempt.
- **original\_mastery** (bool | None) - Boolean indicating whether user achieved mastery.
- **assessed\_at** (datetime | None) - Time when the result was assessed.
- **submitted\_at** (datetime | None) - Time when the submission was submitted.
- **content\_tag\_id** ([content\_tags](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.content_tags) | None) - Foreign key to the content tag representing the learning outcome alignment this result is associated with.
- **user\_uuid** (Annotated\[str, MaxLength(255)] | None) - The uuid of the user who made the submission.
- **hide\_points** (bool) - Boolean indicating if outcome result points should be hidden in the Learning Mastery Gradebook and reports. If enabled, replace points with the description of the highest scoring outcome criterion rating.
- **hidden** (bool) - Boolean indicating if outcome result should be hidden from the Learning Mastery Gradebook and reports.
- **id** (int64) - `primary key` The unique identifier for a learning outcome result record.
- **percent** (float64 | None) - Percent of maximum points possible for an outcome, scaled to reflect any custom mastery levels that differ from the learning outcome.
- **title** (Annotated\[str, MaxLength(255)] | None) - Title for identifying the result.

Learning outcomes are measurable statements that express student knowledge or a student skill.

This table contains dimensions for learning outcomes.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a learning outcome record.
- **display\_name** (Annotated\[str, MaxLength(255)] | None) - Optional friendly name for reporting.
- **context\_code** (Annotated\[str, MaxLength(255)] | None) - Alternate specification of learning outcome context as single string. Combination of `context_type` and `context_id` (e.g. `course_34416`).
- **created\_at** (datetime) - Timestamp of when a `learning_outcomes` record was created.
- **updated\_at** (datetime) - Timestamp of when a `learning_outcomes` record was updated.
- **context\_id** (None | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier for the context of `learning_outcomes` (account, course, user), may be NULL for global outcomes.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - A GUID used to resolve outcomes during import and migration.
- **vendor\_guid** (Annotated\[str, MaxLength(255)] | None) - A custom GUID for the learning standard.
- **outcome\_import\_id** (outcome\_imports | None) - Foreign key to the outcome import associated with this outcome, if this outcome was imported.
- **calculation\_int** (int16 | None) - Defines the variable value used by the calculation\_method. included only if `calculation_method` uses it.
- **short\_description** (Annotated\[str, MaxLength(255)]) - Title of the outcome.
- **description** (bounded\_str | None) - Description of the outcome.
- **data** (json | None) - YAML data specifying the scoring method and rubric criteria for this outcome.

Represents a line item from the IMS Assignment and Grade service.

LTI 1.3 tools that have been authorized by an admin may manage this table.

See [Learning Tools Interoperability (LTI) Assignment and Grade Services Specificationarrow-up-right](https://www.imsglobal.org/spec/lti-ags/v2p0#line-item-service).

**Properties:**

- **created\_at** (datetime) - Timestamp of when a lti\_line\_items record was created.
- **updated\_at** (datetime) - Timestamp of when a lti\_line\_items record was updated.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments)) - The ID of the assignment associated with the line item.
- **client\_id** (int64) - The client ID used to create the line item (developer key global id).
- **coupled** (bool) - True if the line item is the default one created when a user created an assignment; false if the line item was created via the API (regardless if it is the default line item or not).
- **score\_maximum** (float64) - The maximum score for the line item.
- **resource\_id** (bounded\_str | None) - A Tool Provider specified ID for the Line Item. Multiple line items may share the same resourceId within a given context.
- **lti\_resource\_link\_id** ([lti\_resource\_links](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.lti_resource_links) | None) - The resource link ID associated with the line item. This ID matches the associated assignments "lti\_context\_id".
- **label** (bounded\_str) - The label of the line item.
- **id** (int64) - `primary key` The unique identifier for an lti line item record.
- **extensions** (Annotated\[bounded\_str, JsonStringToJsonObject()]) - Contains canvas-specific line item extensions. For example: submission\_type.
- **tag** (bounded\_str | None) - A value used to qualify a line Item beyond its ids. Line Items may be queried by this value in the List endpoint. Multiple line items can share the same tag within a given context.

Joins `context_external_tools` to other resources in Canvas (assignments for example).

Only used with LTI 1.3 `context_external_tools`.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for an lti resource link record.
- **created\_at** (datetime) - Timestamp of when a lti\_resource\_links record was created.
- **updated\_at** (datetime) - Timestamp of when a lti\_resource\_links record was updated.
- **context\_external\_tool\_id** ([context\_external\_tools](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.context_external_tools)) - The ID of the context\_external\_tool associated to the resource.
- **custom** (bounded\_str | None) - Custom parameters that will be added to the LTI launch. These are custom parameters returned from a Deep Linking response. These are merged with tool/placement-level custom parameters, if any.
- **resource\_link\_uuid** (UUID) - A UUID identifying the resource link.
- **lookup\_uuid** (UUID) - Used to identify the resource link to use in order to lookup custom parameters in some scenarios, such as a link added from Deep Linking into a Rich Content Editor.

Represents a result from the IMS Assignment and Grade service

See [IMS Globalarrow-up-right](https://www.imsglobal.org/spec/lti-ags/v2p0#result-service). LTI 1.3 tools that have been authorized by an admin may read records from this table via API.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for an lti result record.
- **extensions** (bounded\_str) - Platform-specific extensions for the result.
- **comment** (bounded\_str | None) - Comment visible to the student about the result (LTI AGS).
- **submission\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions) | None) - the ID of the associated submission.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp of when a `lti_results` record was created.
- **updated\_at** (datetime) - Timestamp of when a `lti_results` record was updated.
- **result\_score** (float64 | None) - The score given for the the student (LTI AGS).
- **result\_maximum** (float64 | None) - The maximum score for the student (LTI AGS).
- **activity\_progress** (bounded\_str | None) - Indication to Canvas of the status of the user towards the activity's completion. Must be one of Initialized, Started, InProgress, Submitted, Completed (LTI AGS).
- **grading\_progress** (bounded\_str | None) - Indication to Canvas of the status of the grading process. A value of PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded (LTI AGS).
- **lti\_line\_item\_id** ([lti\_line\_items](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.lti_line_items)) - The ID of the associated line item.

## master\_courses\_child\_content\_tags

Links imported course content to the child subscription and keeps track of changes made to content.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a master courses child content tag record.
- **migration\_id** (bounded\_str | None) - An identifier used by the Blueprint system to match with the blueprint content.
- **downstream\_changes** (json | None) - The columns changed on the associated content.

## master\_courses\_child\_subscriptions

Saves data about which child courses are linked to which master blueprint courses.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a master courses child subscription record.
- **created\_at** (datetime) - Timestamp showing when a master\_courses\_child\_subscriptions record was created.
- **updated\_at** (datetime) - Timestamp showing when a master\_courses\_child\_subscriptions record was updated.
- **use\_selective\_copy** (bool) - Whether the associated course can receive partial exports from the blueprint course for subsequent sync events.
- **child\_course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of an associated course.

## master\_courses\_master\_content\_tags

Links blueprint course content to the template and keeps track of their locked status.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a master courses master content tag record.
- **migration\_id** (bounded\_str | None) - An identifier used by the Blueprint system to match with associated content.
- **restrictions** (json | None) - The locked status of the associated content object.
- **use\_default\_restrictions** (bool) - Whether the content is using defaults set by the course or has been individually configured.

## master\_courses\_master\_migrations

Represents a blueprint course sync event.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a master courses master migrations record.
- **comment** (bounded\_str | None) - An optional message to be displayed with the sync event.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp showing when a master\_courses\_master\_migrations record was created.
- **updated\_at** (datetime) - Timestamp showing when a master\_courses\_master\_migrations record was updated.
- **migration\_settings** (json | None) - Optional settings for the sync event (such as whether to include course settings).
- **export\_results** (json | None) - Record of which associated courses received full exports and which ones received partial (selective) ones.
- **exports\_started\_at** (datetime | None) - Timestamp showing when exports started being generated from the blueprint course.
- **imports\_queued\_at** (datetime | None) - Timestamp showing when imports started being queued into the associated courses.
- **imports\_completed\_at** (datetime | None) - Timestamp showing when all imports into associated courses completed.
- **send\_notification** (bool) - Whether to generate notifications around the sync event.

## master\_courses\_master\_templates

Stores blueprint course specific data and links a course with all other blueprint models.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a master courses template record.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of a blueprint course record.
- **created\_at** (datetime) - Timestamp showing when a master\_courses\_templates record was created.
- **updated\_at** (datetime) - Timestamp showing when a master\_courses\_templates record was updated.
- **full\_course** (bool) - Whether all blueprint content in the course should be synced (always true for the time being).
- **default\_restrictions** (json | None) - The default locked status for all blueprint course content (unless using restrictions by type).
- **use\_default\_restrictions\_by\_type** (bool) - Whether to use default\_restrictions\_by\_type to determine content locked status.
- **default\_restrictions\_by\_type** (json | None) - The default locked status for all blueprint course content depending on the type of content (unless not using restrictions by type).

## master\_courses\_migration\_results

Stores results for individual associated courses for a blueprint sync event.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a master courses migration result record.
- **content\_migration\_id** ([content\_migrations](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.content_migrations)) - The ID of a relevant import record on the associated course.
- **results** (json | None) - Relevant results of the import (e.g. items that were not synced because they were modified by the associated course).

Represents an "originality score" for a submission.

Rows in this table are managed solely by LTI 2 tool providers that leverage the Canvas plagiarism detection platform.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for an originality report record.
- **error\_message** (bounded\_str | None) - The error message provided by the tool provider. Only set if there was an error processing the submission.
- **attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - The is of the attachment associated with the originality report.
- **submission\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions)) - ID of the submission associated with the originality report.
- **created\_at** (datetime) - Timestamp of when an `originality_reports` record was created.
- **updated\_at** (datetime) - Timestamp of when an `originality_reports` record was updated.
- **originality\_score** (float64 | None) - A number ranging from 0-100 indicating the level of potential plagiarism.
- **originality\_report\_url** (bounded\_str | None) - The url pointing to the originality report from the tool provider.
- **originality\_report\_lti\_url** (bounded\_str | None) - The LTI launch URL that allows a user to view the originality report in the tool.
- **link\_id** (bounded\_str | None) - Resource link ID of the assignment associated with the submission.
- **submission\_time** (datetime | None) - Time the submission was submitted.

Outcome proficiencies, or learning mastery proficiency ratings, define a set of ratings, which together create a point scale and a mastery level.

**Properties:**

- **created\_at** (datetime) - Timestamp of when an `outcome_proficiencies` record was created.
- **updated\_at** (datetime) - Timestamp of when an `outcome_proficiencies` record was updated.
- **context\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier for the context (account or course) of the outcome proficiency.
- **id** (int64) - `primary key` The unique identifier for an outcome proficiency record.

## outcome\_proficiency\_ratings

Outcome proficiency ratings define the individual tiers of outcome proficiencies.

**Properties:**

- **created\_at** (datetime) - Timestamp of when an outcome\_proficiency\_ratings record was created.
- **updated\_at** (datetime) - Timestamp of when an outcome\_proficiency\_ratings record was updated.
- **mastery** (bool) - Indicates the rating where mastery is first achieved.
- **points** (float64) - A non-negative number of points for the rating.
- **outcome\_proficiency\_id** ([outcome\_proficiencies](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.outcome_proficiencies)) - Unique ID of proficiency collection to which this rating belongs.
- **color** (bounded\_str) - The hex color code of the rating.
- **description** (Annotated\[str, MaxLength(255)]) - The description of the rating.
- **id** (int64) - `primary key` The unique identifier for an outcome proficiency ratings record.

Contains post policy configurations for courses and individual assignments.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a post policy record.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The ID of the course referenced by this policy. Note that this is always set even if the policy refers to a specific assignment within a course.
- **created\_at** (datetime) - Timestamp of when a `post_policies` record was created.
- **updated\_at** (datetime) - Timestamp of when a `post_policies` record was updated.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - The ID of the assignment referenced by this policy, or NULL if the policy refers to a course at large.
- **post\_manually** (bool) - For post policies associated with an assignment, whether submissions receiving grades or comments should be posted to the student automatically. For post policies associated with a course, this value will be applied by default to assignments created in the course.

This table stores user pseudonyms.

Pseudonyms are login profiles associated with users. Contains user / account relationship (may contain multiple records per `user_id` if that `user_id` is associated with multiple accounts); note: not all users can be found in the pseudonyms table.

**Properties:**

- **id** (int64) - `primary key` Primary key for this pseudonym in the the Canvas database.
- **deleted\_at** (datetime | None) - Timestamp when the pseudonym was deleted (NULL if the pseudonym is still active).
- **integration\_id** (Annotated\[str, MaxLength(255)] | None) - The `integration_id` associated with the user.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - Id for the user associated with this pseudonym.
- **created\_at** (datetime) - Timestamp when this pseudonym was created in Canvas.
- **updated\_at** (datetime) - Timestamp when this pseudonym was last updated in Canvas.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - Identifies the account associated with this pseudonym. Typically root account ID unless account user belongs to trust/consortium based Canvas accounts.
- **sis\_batch\_id** (sis\_batches | None) - The ID of the SIS import.
- **unique\_id** (Annotated\[str, MaxLength(255)]) - The unique login ID for the user. This is what the user uses to log in to Canvas.
- **login\_count** (int32) - The count of all user logins.
- **failed\_login\_count** (int32) - Only applies to accounts that use Canvas authentication settings.
- **last\_request\_at** (datetime | None) - Timestamp of when the user last logged in with this pseudonym.
- **last\_login\_at** (datetime | None) - Timestamp of last time a user logged in with this pseudonym.
- **current\_login\_at** (datetime | None) - Timestamp of when the user logged in.
- **last\_login\_ip** (Annotated\[str, MaxLength(255)] | None) - IP address recorded the last time a user logged in with this pseudonym.
- **current\_login\_ip** (Annotated\[str, MaxLength(255)] | None) - IP address of user's previous login id, this value could be the same as last\_login\_ip.
- **sis\_user\_id** (Annotated\[str, MaxLength(255)] | None) - The SIS ID associated with the user.
- **authentication\_provider\_id** (authentication\_providers | None) - The authentication provider this login is associated with. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider).
- **position** (int32 | None) - Position of user's login credentials.

This table stores attributes for quiz group.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)] | None) - The name of the question group.
- **id** (int64) - `primary key` The ID of the question group.
- **created\_at** (datetime) - Time when the quiz question was created.
- **updated\_at** (datetime) - Time when the quiz question was last updated.
- **assessment\_question\_bank\_id** ([assessment\_question\_banks](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assessment_question_banks) | None) - The ID of the Assessment question bank to pull questions from.
- **quiz\_id** ([quizzes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quizzes)) - The ID of the Quiz the question group belongs to.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported the quiz group.
- **pick\_count** (int32 | None) - The number of questions to pick from the group to display to the student.
- **question\_points** (float64 | None) - The amount of points allotted to each question in the group.
- **position** (int32 | None) - The order in which the question group will be retrieved and displayed.

This table stores attributes of a question associated with a quiz.

**Properties:**

- **id** (int64) - `primary key` The ID of the quiz question.
- **created\_at** (datetime | None) - Time when the quiz question was created.
- **updated\_at** (datetime | None) - Time when the quiz question was last updated.
- **quiz\_id** ([quizzes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quizzes) | None) - The ID of the Quiz the question belongs to.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported the quiz question.
- **quiz\_group\_id** ([quiz\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quiz_groups) | None) - Identifies the quiz group.
- **assessment\_question\_version** (int32 | None) - Version of the assessment question associated with the quiz question.
- **position** (int32 | None) - The order in which the question will be retrieved and displayed.

Stores attributes for the last submitted quiz.

This tables persists one record per `user_id` and `quiz_id`.

**Properties:**

- **id** (int64) - `primary key` The ID of the quiz submission.
- **submission\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions) | None) - The ID of the Submission the quiz submission represents.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the Student that made the quiz submission.
- **created\_at** (datetime) - Time when the quiz submission was created.
- **updated\_at** (datetime) - Time when the quiz submission was last updated.
- **quiz\_id** ([quizzes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quizzes)) - The ID of the Quiz the quiz submission belongs to.
- **quiz\_version** (int32 | None) - The version of the quiz this submission is related to.
- **started\_at** (datetime | None) - The time at which the student started the quiz submission.
- **finished\_at** (datetime | None) - The time at which the student submitted the quiz submission.
- **end\_at** (datetime | None) - The time at which the quiz submission will be overdue, and be flagged as a late submission.
- **score** (float64 | None) - The score of the quiz submission, if graded.
- **attempt** (int32 | None) - For quizzes that allow multiple attempts, this field specifies the quiz submission attempt number.
- **submission\_data** (Annotated\[bounded\_str, YamlStringToJsonObject(), SpecialConversion()] | None) - Student answers to quiz, it shares JSON array of answers for only graded quiz submissions, it has NULL if quiz hasn't been graded yet. Contains the `question_id`, whether the question was answered correctly, the `answer_id` and answer text.
- **kept\_score** (float64 | None) - For quizzes that allow multiple attempts, this is the score that will be used, which might be the score of the latest, or the highest, quiz submission.
- **fudge\_points** (float64) - Number of points the quiz submissions score was fudged by.
- **quiz\_points\_possible** (float64 | None) - The amount of points possible for the quiz.
- **extra\_attempts** (int32 | None) - Number of times the student was allowed to retake the quiz over the multiple-attempt limit.
- **temporary\_user\_code** (Annotated\[str, MaxLength(255)] | None) - Construct for previewing a quiz.
- **extra\_time** (int32 | None) - Amount of extra time allowed for the quiz submission, in minutes.
- **manually\_scored** (bool | None) - Indicates if this submission was graded by the teacher.
- **manually\_unlocked** (bool | None) - The student can take the quiz even if it's locked for everyone else.
- **was\_preview** (bool | None) - Indicates if this submission was created from a teacher preview.
- **score\_before\_regrade** (float64 | None) - The original score of the quiz submission prior to any re-grading.
- **has\_seen\_results** (bool | None) - Whether the student has viewed their results to the quiz.

Stores attributes for quizzes.

Quizzes can also be assignments (`assignment_id` field will have a value).

**Properties:**

- **deleted\_at** (datetime | None) - Timestamp when the quiz was deleted.
- **created\_at** (datetime) - Time when the quiz was created.
- **updated\_at** (datetime) - Time when the quiz was last updated.
- **workflow\_state** ([quizzes\_\_workflow\_state](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.quizzes__workflow_state)) - Denotes where the quiz is in the workflow. Possible values are `unpublished`, `published` and `deleted`. Defaults to `unpublished`.
- **due\_at** (datetime | None) - when the quiz is due.
- **unlock\_at** (datetime | None) - when to unlock the quiz.
- **lock\_at** (datetime | None) - when to lock the quiz.
- **points\_possible** (float64 | None) - The total point value given to the quiz.
- **assignment\_group\_id** ([assignment\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignment_groups) | None) - the ID of the quizzes assignment group.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of the context (account or course) this group belongs too. See also: `context_type`.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - Identifies the assignment the quiz belongs to (NULL if not an assignment).
- **could\_be\_locked** (bool) - Dictates if the quiz can be locked or not. Possible values are `allow_locking` and `disallow_locking`. Defaults to `disallow_locking`.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - The unique identifier of the migration that imported the quiz.
- **only\_visible\_to\_overrides** (bool) - This indicates the quiz is not visible to everyone in the course, but only to those with an override.
- **allowed\_attempts** (int32 | None) - how many times a student can take the quiz -1 = unlimited attempts.
- **published\_at** (datetime | None) - whether the quiz has a published or unpublished draft state.
- **shuffle\_answers** (bool) - shuffle answers for students.
- **show\_correct\_answers** (bool) - show which answers were correct when results are shown? only valid if `hide_results` is NULL.
- **time\_limit** (int32 | None) - quiz time limit in minutes.
- **scoring\_policy** (Annotated\[str, MaxLength(255)] | None) - which quiz score to keep (only if `allowed_attempts` != 1) possible values: `keep_highest`, `keep_latest`.
- **access\_code** (Annotated\[str, MaxLength(255)] | None) - access code to restrict quiz access.
- **question\_count** (int32 | None) - the number of questions in the quiz.
- **anonymous\_submissions** (bool) - Dictates whether students are allowed to submit the quiz anonymously.
- **hide\_results** (Annotated\[str, MaxLength(255)] | None) - let students see their quiz responses? possible values: NULL, `always`, `until_after_last_attempt`.
- **ip\_filter** (Annotated\[str, MaxLength(255)] | None) - IP address or range that quiz access is limited to.
- **require\_lockdown\_browser** (bool) - Dictates whether the browser has locked-down when the quiz is being taken. Possible values are `required` and `not_required`. Defaults to `not_required`.
- **require\_lockdown\_browser\_for\_results** (bool) - Dictates whether the browser has to be locked-down to display the results. Is valid only if `hide_results` is set to `never` or `until_after_last_attempt` (for the results to be displayed after the last attempt). Possible values are `required` and `not_required`. Defaults to `not_required`.
- **one\_question\_at\_a\_time** (bool) - show one question at a time?
- **cant\_go\_back** (bool) - lock questions after answering? only valid if `one_question_at_a_time` is true.
- **show\_correct\_answers\_at** (datetime | None) - when should the correct answers be visible by students? only valid if `show_correct_answers` is true.
- **hide\_correct\_answers\_at** (datetime | None) - prevent the students from seeing correct answers after the specified date has passed. only valid if `show_correct_answers` is true.
- **require\_lockdown\_browser\_monitor** (bool) - Dictates whether a browser lockdown monitor is required. Possible values are `required` and `not_required`. Defaults to `not_required`.
- **one\_time\_results** (bool) - prevent the students from seeing their results more than once (right after they submit the quiz).
- **show\_correct\_answers\_last\_attempt** (bool) - restrict the show\_correct\_answers option above to apply only to the last submitted attempt of a quiz that allows multiple attempts. only valid if `show_correct_answers` is true and `allowed_attempts` &gt; 1.
- **unpublished\_question\_count** (int32) - The number of questions that have not been published.
- **description** (bounded\_str | None) - the description of the quiz.
- **id** (int64) - `primary key` the ID of the quiz.
- **title** (Annotated\[str, MaxLength(255)] | None) - the title of the quiz.

A customization to the default permissions granted by a role.

**Properties:**

- **id** (int64) - `primary key` unique identifier of a role permission.
- **permission** (Annotated\[str, MaxLength(255)] | None) - Permission assigned to a role, see the dictionary of permissions keyed by name in Canvas Roles API documentation.
- **created\_at** (datetime | None) - Timestamp of when this record was created.
- **updated\_at** (datetime | None) - Timestamp of last update to this record.
- **role\_id** ([roles](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.roles)) - Unique ID of a role.
- **context\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - The unique identifier for the folders's context (account, course, user).
- **locked** (bool) - Whether the permission is locked by this role.
- **enabled** (bool) - Whether the role has the permission.
- **applies\_to\_self** (bool) - Whether the permission applies to the account this role is in. Only present if enabled is true.
- **applies\_to\_descendants** (bool) - Whether the permission cascades down to sub accounts of the account this role is in. Only present if enabled is true.

A user is assigned a role which grants all the permissions associated with that role.

Roles have a few implicit permissions and a large set of default permissions, which can be customized with RoleOverrides.

**Properties:**

- **name** (Annotated\[str, MaxLength(255)]) - The name of the role.
- **id** (int64) - `primary key` The unique identifier for a user role record.
- **deleted\_at** (datetime | None) - Timestamp when this record was deleted. If the record has not been deleted the value will be NULL.
- **created\_at** (datetime) - Timestamp of when a roles record was created.
- **updated\_at** (datetime) - Timestamp of when a roles record was updated.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | None) - Points to the account associated with the course. Could be Canvas root account or sub-account ID.
- **base\_role\_type** ([roles\_\_base\_role\_type](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.roles__base_role_type)) - The role type that is being used as a base for this role. For account-level roles, this is `AccountMembership`. For course-level roles, it is an enrollment type.

Shows the data that a teacher has entered in to a rubric while grading a student.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a rubric assessment record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp showing when a `rubric_assessment` record was created.
- **updated\_at** (datetime) - Timestamp showing when a `rubric_assessment` record was updated.
- **rubric\_association\_id** ([rubric\_associations](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.rubric_associations) | None) - The ID of a rubric association (which links the rubric to an assignment that uses the rubric).
- **artifact\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions) | [assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | moderated\_grading\_provisional\_grades) - The submission or assignment identifier.
- **hide\_points** (bool) - Flag indicating a non-scoring rubric assessment.
- **score** (float64 | None) - Score of the assessment.
- **rubric\_id** ([rubrics](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.rubrics)) - The unique ID of a rubric.
- **assessor\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user who assessed the submission.
- **artifact\_attempt** (int32 | None) - The current number of attempts made on the object of the assessment.
- **data** (json | None) - Object containing all data related to assessment including score-break down and comments for each criterion.

Links a rubric to an assignment.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a rubric association record.
- **purpose** (Annotated\[str, MaxLength(255)]) - Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context. Values will be grading or bookmark.
- **created\_at** (datetime) - Timestamp showing when a `rubric_associations` record was created.
- **updated\_at** (datetime) - Timestamp showing when a `rubric_associations` record was updated.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - The unique identifier for the context of `rubric_associations` (account, course).
- **hide\_points** (bool) - Flag indication whether to hide points from rubric.
- **rubric\_id** ([rubrics](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.rubrics)) - The unique identifier of a rubric tied to this association.
- **use\_for\_grading** (bool | None) - Whether or not the associated rubric is used for grade calculation.
- **summary\_data** (json | None) - Object that stores reusable comments made during assessments.
- **hide\_score\_total** (bool | None) - Flag indicating whether to hide the score total for assessment results.
- **bookmarked** (bool) - Flag indication whether rubric is bookmarked.
- **hide\_outcome\_results** (bool) - Flag indicating to not post Outcomes results to Learning Mastery Gradebook.
- **title** (Annotated\[str, MaxLength(255)] | None) - The name of the object this rubric is associated with.

List of criteria that describe how an assignment should be graded.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a rubric record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp showing when a rubrics record was created.
- **updated\_at** (datetime) - Timestamp showing when a rubrics record was updated.
- **points\_possible** (float64 | None) - Total points possible for the rubric.
- **context\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts) | [courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The unique identifier of a rubric's context (account, course).
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - An identifier used by the Blueprint system to match with the blueprint content.
- **hide\_score\_total** (bool | None) - Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading.
- **association\_count** (int32) - The number of associated objects (accounts, courses, assignments).
- **free\_form\_criterion\_comments** (bool | None) - Whether or not you can write custom comments in the ratings field for a rubric.
- **title** (Annotated\[str, MaxLength(255)] | None) - The Rubric name or title.
- **data** (json | None) - The data containing all the information for the rubric including each criterion.

This table stores aggregate statistics for scores on individual assignments.

**Properties:**

- **created\_at** (datetime) - The date this statistics object was created.
- **updated\_at** (datetime) - The date this statistics object was updated.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments)) - The ID of the assignment referred to by this object.
- **mean** (float64) - The mean score for all graded submissions on this assignment.
- **count** (int32) - The number of submissions that have been graded for this assignment, excluding excused submissions.
- **minimum** (float64) - The lowest score for any graded submission on this assignment.
- **id** (int64) - `primary key` The ID of the statistics object.
- **maximum** (float64) - The highest score for any graded submission on this assignment.

This table stores assignment group and course grades for students enrolled in a course.

**Properties:**

- **id** (int64) - `primary key` The ID of the score.
- **created\_at** (datetime | None) - Time when the score was created.
- **updated\_at** (datetime | None) - Time when the score was updated.
- **assignment\_group\_id** ([assignment\_groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignment_groups) | None) - The ID of the assignment group this score refers to, or NULL if it does not refer to a particular assignment group.
- **enrollment\_id** ([enrollments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.enrollments)) - The ID of the enrollment object this score refers to.
- **grading\_period\_id** ([grading\_periods](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.grading_periods) | None) - The ID of the grading period covered by this score, or NULL if it does not apply to a specific grading period. If this is NULL, this is the overall score for the course.
- **current\_score** (float64 | None) - The current score for the assignments represented by this Score object.
- **final\_score** (float64 | None) - The final score for the assignments represented by this Score object, calculated by treating ungraded assignments as though they received zero points.
- **course\_score** (bool) - True if this score does not refer to a particular grading period or assignment group (in other words, if it represents the overall score for the course referred to in the enrollment).
- **unposted\_current\_score** (float64 | None) - The current score, with muted/unposted assignments included.
- **unposted\_final\_score** (float64 | None) - The final score, with muted/unposted assignments included.
- **current\_points** (float64 | None) - The number of points earned over all assignments covered by this score, with dropped assignments excluded.
- **unposted\_current\_points** (float64 | None) - The total number of points earned over all assignments covered by this score, including muted/unposted assignments.
- **final\_points** (float64 | None) - The number of points earned over all assignments covered by this score, with dropped assignments excluded and unposted submissions treated as 0.
- **unposted\_final\_points** (float64 | None) - The number of points earned over all assignments covered by this score, with dropped assignments excluded and unposted submissions treated as 0, including muted/unposted assignments.
- **override\_score** (float64 | None) - The override score, if one has been set.

This table contains attributes related to the submission comments feature in Canvas.

**Properties:**

- **id** (int64) - `primary key` The ID of this submission comment.
- **comment** (bounded\_str | None) - The text of the submission comment.
- **submission\_id** ([submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.submissions) | None) - The ID of the associated submission.
- **created\_at** (datetime) - The date this comment was created.
- **updated\_at** (datetime) - The date this comment was updated.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The ID of the course this comment is associated with.
- **author\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the commenting user.
- **media\_comment\_id** (Annotated\[str, MaxLength(255)] | None) - For media comments, the ID of the associated media object.
- **attachment\_ids** (bounded\_str | None) - A comma-separated list of attachment IDs associated with this comment.
- **attempt** (int32 | None) - The particular attempt (on the associated submission) that this comment pertains to.
- **hidden** (bool) - True if this comment is not visible to the owner of the submission.
- **author\_name** (Annotated\[str, MaxLength(255)] | None) - The name of the commenting user.
- **group\_comment\_id** (Annotated\[str, MaxLength(255)] | None) - For group assignments, a value that is unique for all copies of this comment on submissions in the same group.
- **assessment\_request\_id** (assessment\_requests | None) - For peer-reviewed assignments, the ID of the Assessment Request this comment is associated with.
- **anonymous** (bool | None) - True if this is a peer-reviewed comment for an assignment with anonymous peer reviews enabled. Does not apply to instructor comments for anonymously-graded assignments.
- **teacher\_only\_comment** (bool) - Indicates whether the comment was provided by a teacher.
- **provisional\_grade\_id** (moderated\_grading\_provisional\_grades | None) - For moderated assignments, the provisional grade this comment is tied to.
- **draft** (bool) - True if this comment was saved as a draft.
- **edited\_at** (datetime | None) - The date this comment was last edited.

This table stores information describing previous versions of individual submission objects.

**Properties:**

- **id** (int64) - `primary key` The ID of this version object.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the submitter.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - The ID of the course this submission belongs to.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - The ID of the associated assignment.
- **version\_id** (versions | None) - The ID of the corresponding object in the versions table.

This table stores submission records for an assignment.

**Properties:**

- **id** (int64) - `primary key` Primary key of this record in the Canvas submissions dataset.
- **attachment\_id** ([attachments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.attachments) | None) - The ID of an attachment belonging to this submission if `submission_type` is `online_url`. Generally superseded by `attachment_ids`.
- **course\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses)) - The ID of the associated assignment's course.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The ID of the user who created the submission.
- **created\_at** (datetime | None) - Timestamp of when the submission was created.
- **updated\_at** (datetime | None) - Timestamp of when the submission was last updated.
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments)) - The ID of the associated assignment.
- **media\_comment\_id** (Annotated\[str, MaxLength(255)] | None) - For media comments, the ID of the media object associated with this comment, as a string.
- **attachment\_ids** (bounded\_str | None) - A comma-delimited string representing the IDs of attachments belonging to this submission.
- **posted\_at** (datetime | None) - The date this submission was posted to the student, or NULL if it has not been posted.
- **group\_id** ([groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.groups) | None) - Foreign key to the `groups` table.
- **score** (float64 | None) - The raw score.
- **attempt** (int32 | None) - The number of attempts made including this one.
- **submitted\_at** (datetime | None) - The timestamp when the assignment was submitted. Note: this date may be missing even though the assignment was submitted and graded (example scenarios: paper assignments, submissions through external tools, no submission required, etc.); additionally, if the student failed to submit an assignment by the due date, the assignment can be graded by the instructor (and will be missing a `submitted_at` date).
- **quiz\_submission\_id** ([quiz\_submissions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quiz_submissions) | None) - Foreign key to the `quiz_submissions` dataset (if `submission_type` is `online_quiz`). If this field contains a value it means that the assignment is a quiz.
- **extra\_attempts** (int32 | None) - Extra submission attempts allowed for the given user and assignment.
- **grading\_period\_id** ([grading\_periods](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.grading_periods) | None) - The ID of the grading period that this submission's assignment belongs to.
- **grade** (Annotated\[str, MaxLength(255)] | None) - Letter grade mapped from the score by the grading scheme.
- **processed** (bool | None) - Valid only when there is a file/attachment associated with the submission. By default, this attribute is set to *false* when making the assignment submission. When a submission has a file/attachment associated with it, upon submitting the assignment a snapshot is saved and its value is set to *true*. Defaults to NULL.
- **grade\_matches\_current\_submission** (bool | None) - A boolean flag which is false if the student has re-submitted since the submission was last graded. Valid only when a score has been assigned to a submission. This is set to *false* if a student makes a new submission to an already graded assignment. This is done to indicate that the current grade given by the teacher is not for the most recent submission by the student. It is set to *true* if a score has been given and there is no new submission. Defaults to NULL.
- **published\_score** (float64 | None) - The raw score (identical to score).
- **published\_grade** (Annotated\[str, MaxLength(255)] | None) - Valid only for a graded submission. The values are strings that reflect the grading type used. For example, a scoring method of `points` will show `4` if given a `4` out of `5`, and a scoring method of `letter grade` will show `B` for the same score (assuming a grading scale where 80-90% is a `B`). Defaults to NULL.
- **graded\_at** (datetime | None) - Timestamp of when the submission was graded.
- **student\_entered\_score** (float64 | None) - A "what-if" score that the student has entered for this submission.
- **grader\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the user who graded the submission. This will be NULL for submissions that haven't been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz auto-grader and auto-grading LTI tools). Specifically auto-graded quizzes set `grader_id` to the negative of the quiz ID. Submissions auto-graded by LTI tools set `grader_id` to the negative of the tool ID.
- **submission\_comments\_count** (int32 | None) - A count of the number of comments made on this submission.
- **media\_object\_id** (media\_objects | None) - The ID of the associated MediaObject.
- **turnitin\_data** (json | None) - A YAML string representing plagiarism data associated with this submission.
- **cached\_due\_date** (datetime | None) - The de-normalized cached due date for this submission.
- **excused** (bool | None) - Whether the assignment is excused. Excused assignments have no impact on a user's grade.
- **graded\_anonymously** (bool | None) - Denotes how the grading has been performed. Possible values are `graded_anonymously` and `not_graded_anonymously`.
- **late\_policy\_status** (Annotated\[str, MaxLength(16)] | None) - The status of the submission in relation to the late policy. Only reflects statuses manually applied by a grader. Can be late, missing, none, or NULL.
- **points\_deducted** (Annotated\[Decimal, Precision(6, 2)] | None) - The amount of points automatically deducted from the score by the missing/late policy for a late or missing assignment.
- **seconds\_late\_override** (int64 | None) - For late submissions, the amount of time (in seconds) the submission is late by.
- **lti\_user\_id** (bounded\_str | None) - The LTI context ID of the submitter.
- **anonymous\_id** (Annotated\[str, MaxLength(5)] | None) - A unique short ID identifying this submission without reference to the owning user.
- **last\_comment\_at** (datetime | None) - The date of the last non-draft comment on this submission by a user other than the submitter.
- **cached\_quiz\_lti** (bool) - True if the associated assignment is a Quizzes.Next assignment.
- **cached\_tardiness** (Annotated\[str, MaxLength(16)] | None) - The status of the submission in relation to the late policy, including automatically-applied statuses. Can be `late`, `missing` or NULL.
- **resource\_link\_lookup\_uuid** (UUID | None) - When the submission is from an LTI tool, the resource link lookup ID is assigned to the submission in order to recover the custom parameters.
- **redo\_request** (bool) - True if the assignment has been reassigned to the student for resubmission.
- **body** (bounded\_str | None) - The content of the submission, if it was submitted directly in a text field.
- **url** (Annotated\[str, MaxLength(255)] | None) - URL content for the submission.

## user\_account\_associations

Stores data about user and account relationship, how "close" a user is related to an account.

**Properties:**

- **id** (int64) - `primary key` The ID of a record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The foreign key for the users dataset.
- **created\_at** (datetime) - Timestamp of when the user association with an account was created.
- **updated\_at** (datetime) - Timestamp that shows the last time the record was updated.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.accounts)) - Identifies the account associated with this user.
- **depth** (int32 | None) - How "close" a user is related to an account. `1` if you have a pseudonym or enrollment in a course in that account. `2` if it's the parent account of a course you're enrolled in, etc.

This table stores attributes for users.

Some users are from other Canvas instances (`id` column being &gt; 10000000000000). Not all users are displayed in users list on UI.

**Properties:**

- **deleted\_at** (datetime | None) - Timestamp that shows when a user was deleted at.
- **storage\_quota** (int64 | None) - The storage quota for the users.
- **lti\_context\_id** (Annotated\[str, MaxLength(255)] | None) - UUID of the Canvas context in LTI standard. secondary ID for this context, could be used in API to identify resource as well.
- **created\_at** (datetime) - Timestamp when the user was created in the Canvas system.
- **updated\_at** (datetime) - Timestamp that shows the last time the record was updated.
- **sortable\_name** (Annotated\[str, MaxLength(255)] | None) - The name of the user that is should be used for sorting groups of users, such as in the gradebook. Format: "lastname, firstname".
- **avatar\_image\_url** (Annotated\[str, MaxLength(255)] | None) - If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar.
- **avatar\_image\_source** (Annotated\[str, MaxLength(255)] | None) - The source of a user avatar image.
- **avatar\_image\_updated\_at** (datetime | None) - Timestamp that shows the last time the avatar image was updated.
- **short\_name** (Annotated\[str, MaxLength(255)] | None) - A short name the user has selected, for use in conversations or other less formal places through the site.
- **last\_logged\_out** (datetime | None) - The last time the user explicitly logged out of Canvas.
- **pronouns** (bounded\_str | None) - stores a list of preferred gender pronouns i.e.: she/her; he/him; they/them.
- **merged\_into\_user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - If this user was merged into another one, this is the foreign key to that other user.
- **locale** (Annotated\[str, MaxLength(255)] | None) - The user's locale. This is an optional field and may not be entered by the user.
- **name** (Annotated\[str, MaxLength(255)] | None) - The name of the user ("firstname lastname" format).
- **id** (int64) - `primary key` The ID of the user.
- **time\_zone** (Annotated\[str, MaxLength(255)] | None) - This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone.
- **uuid** (Annotated\[str, MaxLength(255)] | None) - UUID of the user.
- **school\_name** (Annotated\[str, MaxLength(255)] | None) - Used in Trial Versions of Canvas, the school the user is associated with.
- **school\_position** (Annotated\[str, MaxLength(255)] | None) - Used in Trial Versions of Canvas, the position the user has at the school. E.g. Admin
- **public** (bool | None) - Used in Trial Versions of Canvas, the type of school the user is associated with.

## web\_conference\_participants

Links users to conferences they are invited to join.

**Properties:**

- **id** (int64) - `primary key` The ID of the web conference participant.
- **web\_conference\_id** ([web\_conferences](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.web_conferences) | None) - Foreign key to the `web_conferences` page.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - Identifies the user who is the conference participant.
- **created\_at** (datetime) - Timestamp when record was created.
- **updated\_at** (datetime) - Timestamp when record was updated.

Data model for Conferences in Canvas.

Integrates with external conferencing solutions like BigBlueButton.

**Properties:**

- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The ID of the user that created the conference.
- **created\_at** (datetime) - Timestamp when record was created.
- **updated\_at** (datetime) - Timestamp when record was updated.
- **start\_at** (datetime | None) - The date the conference started at, NULL if it hasn't started.
- **end\_at** (datetime | None) - The date that the conference ended at, NULL if it hasn't ended.
- **context\_code** (Annotated\[str, MaxLength(255)] | None) - A string identifying the context.
- **started\_at** (datetime | None) - The time at which this conference actually started at, NULL if it hasn't started.
- **user\_ids** (Annotated\[str, MaxLength(255)] | None) - Array of user ids that are participants in the conference.
- **ended\_at** (datetime | None) - The time at which this conference actually ended, NULL if it hasn't ended.
- **recording\_ready** (bool | None) - Whether the conference's recording has been processed.
- **conference\_key** (Annotated\[str, MaxLength(255)] | None) - The 3rd party's ID for the conference.
- **description** (bounded\_str | None) - The description for the conference.
- **duration** (float64 | None) - The expected duration the conference is supposed to last.
- **settings** (json | None) - Settings for the given conference.
- **id** (int64) - `primary key` The ID of the conference.
- **title** (Annotated\[str, MaxLength(255)]) - The title of the conference.
- **uuid** (Annotated\[str, MaxLength(255)] | None) - A unique ID used for integrations.

Stores text data that is linked to a wiki and a course.

Also known as Pages. Pages store content and educational resources that are part of a course or group but don't necessarily belong in an assignment. Pages can include text, video, and links to files and other course or group content. Pages can also be linked to other pages. They can also be used as a collaboration tool for course or group wikis where only specific users can have access. Canvas keeps the entire history of the page to account for changes over time.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a wiki page record.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of a user.
- **created\_at** (datetime) - Timestamp showing when a `wiki_pages` record was created.
- **updated\_at** (datetime) - Timestamp showing when a `wiki_pages` record was updated.
- **context\_id** ([courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | [groups](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.groups)) - The unique identifier for the context of `wiki_pages` (account, course, user).
- **assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - Assignment identifier when using `wiki_page` assignment type for an assignment.
- **migration\_id** (Annotated\[str, MaxLength(255)] | None) - An identifier used by the Blueprint system to match with the blueprint content.
- **wiki\_id** ([wikis](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.wikis)) - The unique identifier of an associated wiki record.
- **old\_assignment\_id** ([assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - An old assignment identifier.
- **todo\_date** (datetime | None) - Date to set when setting this page as student to-do.
- **editing\_roles** (Annotated\[str, MaxLength(255)] | None) - CSV list of the roles that are allowed to edit this page. Possible values are `teachers`, `students`, `public`.
- **revised\_at** (datetime | None) - Timestamp showing when page was last revised.
- **body** (bounded\_str | None) - The body of the wiki page record (includes html tags).
- **url** (bounded\_str | None) - The HTML body of the page.
- **title** (Annotated\[str, MaxLength(255)] | None) - The name of the wiki page record.
- **protected\_editing** (bool) - Editing protection for the wiki page. It is false by default.
- **could\_be\_locked** (bool | None) - True if the wiki page can be locked. This prevents it from being visible to others until ready.

Links a course to its wiki pages.

There's only ever one per course, it is not highly used any longer, Wiki pages object is linked directly to a course now.

**Properties:**

- **id** (int64) - `primary key` The unique identifier of a wiki record.
- **created\_at** (datetime) - Timestamp showing when a wikis record was created.
- **updated\_at** (datetime) - Timestamp showing when a wikis record was updated.
- **front\_page\_url** (bounded\_str | None) - Captures the URL of the front page (wiki page) record if one exists.
- **has\_no\_front\_page** (bool | None) - Flag to determine if a course's wiki has a front page or not. No front page == true.
- **title** (Annotated\[str, MaxLength(255)] | None) - The title of the wiki.

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).