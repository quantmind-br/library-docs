---
title: Submissions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/submissions
source: sitemap
fetched_at: 2026-02-15T08:56:45.32963-03:00
rendered_js: false
word_count: 3672
summary: This document provides the API specification for accessing and creating student assignment submissions within a course or section. it defines data models for submissions and comments while detailing endpoint requirements for various submission types like text, URLs, and file uploads.
tags:
    - assignment-submissions
    - api-reference
    - submission-objects
    - student-records
    - canvas-lms
    - data-models
category: api
---

API for accessing and updating submissions for an assignment. The submission id in these URLs is the id of the student in the course, there is no separate submission id exposed in these APIs.

All submission actions can be performed with either the course id, or the course section id. SIS ids can be used, prefixed by "sis\_course\_id:" or "sis\_section\_id:" as described in the API documentation on SIS IDs.

**A MediaComment object looks like:**

```
{
"content-type": "audio/mp4",
"display_name": "something",
"media_id": "3232",
"media_type": "audio",
"url": "http://example.com/media_url"
}
```

**A SubmissionComment object looks like:**

```
{
"id": 37,
"author_id": 134,
"author_name": "Toph Beifong",
  // Abbreviated user object UserDisplay (see users API).
"author": "{}",
"comment": "Well here's the thing...",
"created_at": "2012-01-01T01:00:00Z",
"edited_at": "2012-01-02T01:00:00Z",
"media_comment": null
}
```

**A Submission object looks like:**

```
{
  // The submission's assignment id
  "assignment_id": 23,
  // The submission's assignment (see the assignments API) (optional)
  "assignment": null,
  // The submission's course (see the course API) (optional)
  "course": null,
  // This is the submission attempt number.
  "attempt": 1,
  // The content of the submission, if it was submitted directly in a text field.
  "body": "There are three factors too...",
  // The grade for the submission, translated into the assignment grading scheme
  // (so a letter grade, for example).
  "grade": "A-",
  // A boolean flag which is false if the student has re-submitted since the
  // submission was last graded.
  "grade_matches_current_submission": true,
  // URL to the submission. This will require the user to log in.
  "html_url": "http://example.com/courses/255/assignments/543/submissions/134",
  // URL to the submission preview. This will require the user to log in.
  "preview_url": "http://example.com/courses/255/assignments/543/submissions/134?preview=1",
  // The raw score
  "score": 13.5,
  // Associated comments for a submission (optional)
  "submission_comments": null,
  // The types of submission ex:
  // ('online_text_entry'|'online_url'|'online_upload'|'online_quiz'|'media_record
  // ing'|'student_annotation')
  "submission_type": "online_text_entry",
  // The timestamp when the assignment was submitted
  "submitted_at": "2012-01-01T01:00:00Z",
  // The URL of the submission (for 'online_url' submissions).
  "url": null,
  // The id of the user who created the submission
  "user_id": 134,
  // The id of the user who graded the submission. This will be null for
  // submissions that haven't been graded yet. It will be a positive number if a
  // real user has graded the submission and a negative number if the submission
  // was graded by a process (e.g. Quiz autograder and autograding LTI tools). 
  // Specifically autograded quizzes set grader_id to the negative of the quiz id.
  // Submissions autograded by LTI tools set grader_id to the negative of the tool
  // id.
  "grader_id": 86,
  "graded_at": "2012-01-02T03:05:34Z",
  // The submissions user (see user API) (optional)
  "user": null,
  // Whether the submission was made after the applicable due date
  "late": false,
  // Whether the assignment is visible to the user who submitted the assignment.
  // Submissions where `assignment_visible` is false no longer count towards the
  // student's grade and the assignment can no longer be accessed by the student.
  // `assignment_visible` becomes false for submissions that do not have a grade
  // and whose assignment is no longer assigned to the student's section.
  "assignment_visible": true,
  // Whether the assignment is excused.  Excused assignments have no impact on a
  // user's grade.
  "excused": true,
  // Whether the assignment is missing.
  "missing": true,
  // The status of the submission in relation to the late policy. Can be late,
  // missing, extended, none, or null.
  "late_policy_status": "missing",
  // The amount of points automatically deducted from the score by the
  // missing/late policy for a late or missing assignment.
  "points_deducted": 12.3,
  // The amount of time, in seconds, that an submission is late by.
  "seconds_late": 300,
  // The current state of the submission
  "workflow_state": "submitted",
  // Extra submission attempts allowed for the given user and assignment.
  "extra_attempts": 10,
  // A unique short ID identifying this submission without reference to the owning
  // user. Only included if the caller has administrator access for the current
  // account.
  "anonymous_id": "acJ4Q",
  // The date this submission was posted to the student, or nil if it has not been
  // posted.
  "posted_at": "2020-01-02T11:10:30Z",
  // The read status of this submission for the given user (optional). Including
  // read_status will mark submission(s) as read.
  "read_status": "read",
  // This indicates whether the submission has been reassigned by the instructor.
  "redo_request": true
}
```

[SubmissionsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_controller.rb)

`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions`

`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions`

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions`

Make a submission for an assignment. You must be actively enrolled as a student in the course/section to do this. Concluded and pending enrollments are not permitted.

All online turn-in submission types are supported in this API. However, there are a few things that are not yet supported:

- Files can be submitted based on a file ID of a user or group file or through the [file upload API](https://developerdocs.instructure.com/services/canvas/resources/submissions#method.submissions_api.create_file). However, there is no API yet for listing the user and group files.
- Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
- Integration with Google Docs is not yet supported.

**Request Parameters:**

Include a textual comment with the submission.

`submission[group_comment]`

Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text\_comment is provided.

`submission[submission_type]`

The type of submission being made. The assignment submission\_types must include this submission type as an allowed option, or the submission will be rejected with a 400 error.

The submission\_type given determines which of the following parameters is used. For instance, to submit a URL, `submission[submission_type]` must be set to “online\_url”, otherwise the `submission[url]` parameter will be ignored.

“basic\_lti\_launch” requires the assignment submission\_type “online” or “external\_tool”

Allowed values: `online_text_entry`, `online_url`, `online_upload`, `media_recording`, `basic_lti_launch`, `student_annotation`

Submit the assignment as an HTML document snippet. Note this HTML snippet will be sanitized using the same ruleset as a submission made from the Canvas web UI. The sanitized HTML will be returned in the response as the submission body. Requires a submission\_type of “online\_text\_entry”.

Submit the assignment as a URL. The URL scheme must be “http” or “https”, no “ftp” or other URL schemes are allowed. If no scheme is given (e.g. “[www.example.comarrow-up-right](https://developerdocs.instructure.com/services/canvas/resources/www.example.com)”) then “http” will be assumed. Requires a submission\_type of “online\_url” or “basic\_lti\_launch”.

Submit the assignment as a set of one or more previously uploaded files residing in the submitting user’s files section (or the group’s files section, for group assignments).

To upload a new file to submit, see the submissions [Upload a file API](https://developerdocs.instructure.com/services/canvas/resources/submissions#method.submissions_api.create_file).

Requires a submission\_type of “online\_upload”.

`submission[media_comment_id]`

The media comment id to submit. Media comment ids can be submitted via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.

Requires a submission\_type of “media\_recording”.

`submission[media_comment_type]`

The type of media comment being submitted.

Allowed values: `audio`, `video`

Submit on behalf of the given user. Requires grading permission.

`submission[annotatable_attachment_id]`

The Attachment ID of the document being annotated. This should match the annotatable\_attachment\_id on the assignment.

Requires a submission\_type of “student\_annotation”.

Choose the time the submission is listed as submitted at. Requires grading permission.

[SubmissionsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions`

A paginated list of all existing submissions for an assignment.

**Request Parameters:**

Associations to include with the group. “group” will add group\_id and group\_name.

Allowed values: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `assignment`, `visibility`, `course`, `user`, `group`, `read_status`, `student_entered_score`

If this argument is true, the response will be grouped by student groups.

**API response field:**

The unique identifier for the assignment.

The id of the user who submitted the assignment.

The id of the user who graded the submission. This will be null for submissions that haven’t been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz autograder and autograding LTI tools). Specifically autograded quizzes set grader\_id to the negative of the quiz id. Submissions autograded by LTI tools set grader\_id to the negative of the tool id.

The id for the canvadoc document associated with this submission, if it was a file upload.

The timestamp when the assignment was submitted, if an actual submission has been made.

The raw score for the assignment submission.

If multiple submissions have been made, this is the attempt number.

The content of the submission, if it was submitted directly in a text field.

The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example).

- grade\_matches\_current\_submission

A boolean flag which is false if the student has re-submitted since the submission was last graded.

Link to the URL in canvas where the submission can be previewed. This will require the user to log in.

If the submission was reassigned

If the submission was made as a URL.

Whether the submission was made after the applicable due date.

Whether this assignment is visible to the user who submitted the assignment.

The current status of the submission. Possible values: “submitted”, “unsubmitted”, “graded”, “pending\_review”

Returns a list of [Submission](https://developerdocs.instructure.com/services/canvas/resources/what_if_grades#submission) objects.

[SubmissionsApiController#for\_studentsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/students/submissions`

**Scope:** `url:GET|/api/v1/courses/:course_id/students/submissions`

`GET /api/v1/sections/:section_id/students/submissions`

**Scope:** `url:GET|/api/v1/sections/:section_id/students/submissions`

A paginated list of all existing submissions for a given set of students and assignments.

**Request Parameters:**

List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id “all” will return submissions for all students in the course/section as appropriate.

List of assignments to return submissions for. If none are given, submissions for all assignments are returned.

If this argument is present, the response will be grouped by student, rather than a flat array of submissions.

If this argument is set to true, the response will only include submissions for assignments that have the post\_to\_sis flag set to true and user enrollments that were added through sis.

If this argument is set, the response will only include submissions that were submitted after the specified date\_time. This will exclude submissions that do not have a submitted\_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.

If this argument is set, the response will only include submissions that were graded after the specified date\_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.

The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account)

The current status of the submission

Allowed values: `submitted`, `unsubmitted`, `graded`, `pending_review`

The current state of the enrollments. If omitted will include all enrollments that are not deleted.

Allowed values: `active`, `concluded`

If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow\_state for the enrollments. The argument is ignored unless enrollment\_state argument is also passed.

The order submissions will be returned in. Defaults to “id”. Doesn’t affect results for “grouped” mode.

Allowed values: `id`, `graded_at`

Determines whether ordered results are returned in ascending or descending order. Defaults to “ascending”. Doesn’t affect results for “grouped” mode.

Allowed values: `ascending`, `descending`

Associations to include with the group. ‘total\_scores`requires the`grouped`argument.</p> Allowed values:`submission\_history`,`submission\_comments`,`submission\_html\_comments`,`rubric\_assessment`,`assignment`,`total\_scores`,`visibility`,`course`,`user`,`sub\_assignment\_submissions`,`peer\_review\_submissions`,`student\_entered\_score\`

**Example Response:**

```
# Without grouped:
[
  { "assignment_id": 100, grade: 5, "user_id": 1, ... },
  { "assignment_id": 101, grade: 6, "user_id": 2, ... }
# With grouped:
[
  {
    "user_id": 1,
    "submissions": [
      { "assignment_id": 100, grade: 5, ... },
      { "assignment_id": 101, grade: 6, ... }
    ]
  }
]
```

[SubmissionsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

Get a single submission, based on user id.

**Request Parameters:**

Associations to include with the group.

Allowed values: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `full_rubric_assessment`, `visibility`, `course`, `user`, `read_status`, `student_entered_score`

[SubmissionsApiController#show\_anonymousarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

Get a single submission, based on the submission’s anonymous id.

**Request Parameters:**

Associations to include with the group.

Allowed values: `submission_history`, `submission_comments`, `rubric_assessment`, `full_rubric_assessment`, `visibility`, `course`, `user`, `read_status`

[SubmissionsApiController#create\_filearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/files`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/files`

`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/files`

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/files`

Upload a file to a submission.

This API endpoint is the first step in uploading a file to a submission as a student. See the [File Upload Documentation](https://developerdocs.instructure.com/services/canvas/basics/file.file_uploads) for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data, including the new file id. The caller can then POST to submit the `online_upload` assignment with these file ids.

[SubmissionsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

Comment on and/or update the grading for a student’s assignment submission. If any submission or rubric\_assessment arguments are provided, the user must have permission to manage grades in the appropriate context (course or section).

**Request Parameters:**

Add a textual comment to the submission.

The attempt number (starts at 1) to associate the comment with.

Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text\_comment is provided.

`comment[media_comment_id]`

Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.

`comment[media_comment_type]`

The type of media comment being added.

Allowed values: `audio`, `video`

Attach files to this comment that were previously uploaded using the Submission Comment API’s files action

Associations to include with the submission. “submission\_comments” is always included by default.

- “submission\_comments”: Comments on the submission (always included)
- “visibility”: Whether the assignment is visible to the owner of the submission
- “sub\_assignment\_submissions”: Sub-assignment submissions for discussion checkpoints
- “peer\_review\_submissions”: Peer review submission data when peer review allocation and grading is enabled
- “provisional\_grades”: Provisional grades (only available for moderated assignments)
- “group”: Group information (id and name) for group assignments

Allowed values: `submission_comments`, `visibility`, `sub_assignment_submissions`, `peer_review_submissions`, `provisional_grades`, `group`

`prefer_points_over_scheme`

Treat posted\_grade as points if the value matches a grading scheme value

Assign a score to the submission, updating both the “score” and “grade” fields on the submission record. This parameter can be passed in a few different formats:

- points
  
  A floating point or integral value, such as “13.5”. The grade

```
will be interpreted directly as the score of the assignment.
Values above assignment.points_possible are allowed, for awarding
extra credit.
```

- percentage
  
  A floating point value appended with a percent sign, such as

```
"40%". The grade will be interpreted as a percentage score on the
assignment, where 100% == assignment.points_possible. Values above 100%
are allowed, for awarding extra credit.
```

- letter grade
  
  A letter grade, following the assignment’s defined letter

```
grading scheme. For example, "A-". The resulting score will be the high
end of the defined range for the letter grade. For instance, if "B" is
defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
letter grade will be rejected if the assignment does not have a defined
letter grading scheme. For more fine-grained control of scores, pass in
points or percentage rather than the letter grade.
```

- “pass/complete/fail/incomplete”
  
  A string value of “pass” or “complete”

```
will give a score of 100%. "fail" or "incomplete" will give a score of
0.
```

Note that assignments with grading\_type of “pass\_fail” can only be assigned a score of 0 or assignment.points\_possible, nothing inbetween. If a posted\_grade in the “points” or “percentage” format is sent, the grade will only be accepted if the grade equals one of those two values.

Sets the “excused” status of an assignment.

`submission[late_policy_status]`

Sets the late policy status to either “late”, “missing”, “extended”, “none”, or null.

```
NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on
```

Sets the sticker for the submission.

Allowed values: `apple`, `basketball`, `bell`, `book`, `bookbag`, `briefcase`, `bus`, `calendar`, `chem`, `design`, `pencil`, `beaker`, `paintbrush`, `computer`, `column`, `pen`, `tablet`, `telescope`, `calculator`, `paperclip`, `composite_notebook`, `scissors`, `ruler`, `clock`, `globe`, `grad`, `gym`, `mail`, `microscope`, `mouse`, `music`, `notebook`, `page`, `panda1`, `panda2`, `panda3`, `panda4`, `panda5`, `panda6`, `panda7`, `panda8`, `panda9`, `presentation`, `science`, `science2`, `star`, `tag`, `tape`, `target`, `trophy`

`submission[seconds_late_override]`

Sets the seconds late if late policy status is “late”

When true, updates the peer review sub assignment submission instead of the parent assignment submission. The parent assignment must have peer reviews enabled, the peer\_review\_allocation\_and\_grading feature flag must be enabled for the course, and the assignment must have an associated peer review sub assignment. If any of these conditions are not met, the API will return a 422 error.

Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:

The points awarded for this row.

```
rubric_assessment[criterion_id][points]
```

The rating id for the row.

```
rubric_assessment[criterion_id][rating_id]
```

Comments to add for this row.

```
rubric_assessment[criterion_id][comments]
```

For example, if the assignment rubric is (in JSON format):

```
[
  {
    'id': 'crit1',
    'points': 10,
    'description': 'Criterion 1',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Good', 'points': 10 },
      { 'id': 'rat2', 'description': 'Poor', 'points': 3 }
    ]
  },
  {
    'id': 'crit2',
    'points': 5,
    'description': 'Criterion 2',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },
      { 'id': 'rat2', 'description': 'Complete', 'points': 5 },
      { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }
    ]
  }
]
```

Then a possible set of values for rubric\_assessment would be:

```
rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done.
```

[SubmissionsApiController#update\_anonymousarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

`PUT /api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

Comment on and/or update the grading for a student’s assignment submission, fetching the submission by anonymous id (instead of user id). If any submission or rubric\_assessment arguments are provided, the user must have permission to manage grades in the appropriate context (course or section).

**Request Parameters:**

Add a textual comment to the submission.

Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text\_comment is provided.

`comment[media_comment_id]`

Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.

`comment[media_comment_type]`

The type of media comment being added.

Allowed values: `audio`, `video`

Attach files to this comment that were previously uploaded using the Submission Comment API’s files action

Associations to include with the submission. “submission\_comments” is always included by default.

- “submission\_comments”: Comments on the submission (always included)
- “visibility”: Whether the assignment is visible to the owner of the submission
- “sub\_assignment\_submissions”: Sub-assignment submissions for discussion checkpoints
- “peer\_review\_submissions”: Peer review submission data when peer review allocation and grading is enabled
- “provisional\_grades”: Provisional grades (only available for moderated assignments)
- “group”: Group information (id and name) for group assignments

Allowed values: `submission_comments`, `visibility`, `sub_assignment_submissions`, `peer_review_submissions`, `provisional_grades`, `group`

Assign a score to the submission, updating both the “score” and “grade” fields on the submission record. This parameter can be passed in a few different formats:

- points
  
  A floating point or integral value, such as “13.5”. The grade

```
will be interpreted directly as the score of the assignment.
Values above assignment.points_possible are allowed, for awarding
extra credit.
```

- percentage
  
  A floating point value appended with a percent sign, such as

```
"40%". The grade will be interpreted as a percentage score on the
assignment, where 100% == assignment.points_possible. Values above 100%
are allowed, for awarding extra credit.
```

- letter grade
  
  A letter grade, following the assignment’s defined letter

```
grading scheme. For example, "A-". The resulting score will be the high
end of the defined range for the letter grade. For instance, if "B" is
defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
letter grade will be rejected if the assignment does not have a defined
letter grading scheme. For more fine-grained control of scores, pass in
points or percentage rather than the letter grade.
```

- “pass/complete/fail/incomplete”
  
  A string value of “pass” or “complete”

```
will give a score of 100%. "fail" or "incomplete" will give a score of
0.
```

Note that assignments with grading\_type of “pass\_fail” can only be assigned a score of 0 or assignment.points\_possible, nothing inbetween. If a posted\_grade in the “points” or “percentage” format is sent, the grade will only be accepted if the grade equals one of those two values.

Sets the “excused” status of an assignment.

`submission[late_policy_status]`

Sets the late policy status to either “late”, “missing”, “extended”, “none”, or null.

```
NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on
```

`submission[seconds_late_override]`

Sets the seconds late if late policy status is “late”

Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:

The points awarded for this row.

```
rubric_assessment[criterion_id][points]
```

The rating id for the row.

```
rubric_assessment[criterion_id][rating_id]
```

Comments to add for this row.

```
rubric_assessment[criterion_id][comments]
```

For example, if the assignment rubric is (in JSON format):

```
[
  {
    'id': 'crit1',
    'points': 10,
    'description': 'Criterion 1',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Good', 'points': 10 },
      { 'id': 'rat2', 'description': 'Poor', 'points': 3 }
    ]
  },
  {
    'id': 'crit2',
    'points': 5,
    'description': 'Criterion 2',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },
      { 'id': 'rat2', 'description': 'Complete', 'points': 5 },
      { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }
    ]
  }
]
```

Then a possible set of values for rubric\_assessment would be:

```
rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done.
```

[SubmissionsApiController#gradeable\_studentsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/gradeable_students`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/gradeable_students`

A paginated list of gradeable students for the assignment. The caller must have permission to view grades.

If anonymous grading is enabled for the current assignment and the allow\_new\_anonymous\_id parameter is passed, the returned data will not include any values identifying the student, but will instead include an assignment-specific anonymous ID for each student.

Section-limited instructors will only see students in their own sections.

**Request Parameters:**

Sort results by this field.

Allowed values: `name`

The sorting order. Defaults to ‘asc’.

Allowed values: `asc`, `desc`

Returns a list of [UserDisplay](https://developerdocs.instructure.com/services/canvas/resources/users#userdisplay) objects.

[SubmissionsApiController#multiple\_gradeable\_studentsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/gradeable_students`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/gradeable_students`

A paginated list of students eligible to submit a list of assignments. The caller must have permission to view grades for the requested course.

Section-limited instructors will only see students in their own sections.

**Request Parameters:**

Assignments being requested

**Example Response:**

```
A [UserDisplay] with an extra assignment_ids field to indicate what assignments
that user can submit
[
  {
    "id": 2,
    "display_name": "Display Name",
    "avatar_image_url": "http://avatar-image-url.jpeg",
    "html_url": "http://canvas.com",
    "assignment_ids": [1, 2, 3]
  }
]
```

[SubmissionsApiController#bulk\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`POST /api/v1/courses/:course_id/submissions/update_grades`

**Scope:** `url:POST|/api/v1/courses/:course_id/submissions/update_grades`

`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/update_grades`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/update_grades`

`POST /api/v1/sections/:section_id/submissions/update_grades`

**Scope:** `url:POST|/api/v1/sections/:section_id/submissions/update_grades`

`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/update_grades`

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/update_grades`

Update the grading and comments on multiple student’s assignment submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context (course or section).

**Request Parameters:**

`grade_data[<student_id>][posted_grade]`

`grade_data[<student_id>][excuse]`

`grade_data[<student_id>][rubric_assessment]`

See documentation for the rubric\_assessment argument in the [Submissions Update](https://developerdocs.instructure.com/services/canvas/resources/submissions#method.submissions_api.update) documentation

`grade_data[<student_id>][text_comment]`

`grade_data[<student_id>][group_comment]`

`grade_data[<student_id>][media_comment_id]`

`grade_data[<student_id>][media_comment_type]`

no description

Allowed values: `audio`, `video`

`grade_data[<student_id>][file_ids][]`

`grade_data[<assignment_id>][<student_id>]`

Specifies which assignment to grade. This argument is not necessary when using the assignment-specific endpoints.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/1/assignments/2/submissions/update_grades' \
     -X POST \
     -F 'grade_data[3][posted_grade]=88' \
     -F 'grade_data[4][posted_grade]=95' \
     -H "Authorization: Bearer <token>"
```

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[SubmissionsApiController#mark\_submission\_readarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/read.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

[SubmissionsApiController#mark\_submission\_unreadarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`DELETE /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

`DELETE /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

**Scope:** `url:DELETE|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/read.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

[SubmissionsApiController#mark\_bulk\_submissions\_as\_readarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/submissions/bulk_mark_read`

**Scope:** `url:PUT|/api/v1/courses/:course_id/submissions/bulk_mark_read`

`PUT /api/v1/sections/:section_id/submissions/bulk_mark_read`

**Scope:** `url:PUT|/api/v1/sections/:section_id/submissions/bulk_mark_read`

Accepts a string array of submission ids. Loops through and marks each submission as read

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/submissions/bulk_mark_read.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0" \
     -F 'submissionIds=['88']'
```

[SubmissionsApiController#mark\_submission\_item\_readarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read/:item`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read/:item`

`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read/:item`

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read/:item`

No request fields are necessary.

A submission item can be “grade”, “comment” or “rubric”

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/read/<item>.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

[SubmissionsApiController#submissions\_clear\_unreadarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/submissions/:user_id/clear_unread`

**Scope:** `url:PUT|/api/v1/courses/:course_id/submissions/:user_id/clear_unread`

`PUT /api/v1/sections/:section_id/submissions/:user_id/clear_unread`

**Scope:** `url:PUT|/api/v1/sections/:section_id/submissions/:user_id/clear_unread`

Site-admin-only endpoint.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/submissions/<user_id>/clear_unread.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

[SubmissionsApiController#rubric\_assessments\_read\_statearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_comments/read' \
     -H "Authorization: Bearer <token>"
# or
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_assessments/read' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

[SubmissionsApiController#mark\_rubric\_assessments\_readarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

Indicate that rubric comments/grading made on a submission have been read by the student being assessed. Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_comments/read' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
# or
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_assessments/read' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

**Example Response:**

[SubmissionsApiController#document\_annotations\_read\_statearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

Return whether annotations made on a submitted document have been read by the student

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/document_annotations/read' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

[SubmissionsApiController#mark\_document\_annotations\_readarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

Indicate that annotations made on a submitted document have been read by the student. Only the student who owns the submission can use this endpoint.

NOTE: Document annotations will be marked as read automatically when they are viewed in Canvas web.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/document_annotations/read' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

**Example Response:**

[SubmissionsApiController#submission\_summaryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/submission_summary`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submission_summary`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/submission_summary`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submission_summary`

Returns the number of submissions for the given assignment based on gradeable students that fall into three categories: graded, ungraded, not submitted.

**Request Parameters:**

If this argument is true, the response will take into account student groups.

If this argument is true, the response will include deactivated students in the summary (defaults to false).

**Example Response:**

```
{
  "graded": 5,
  "ungraded": 10,
  "not_submitted": 42
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).