---
title: Users | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/users
source: sitemap
fetched_at: 2026-02-15T08:56:49.18266-03:00
rendered_js: false
word_count: 5725
summary: This document defines the schemas and access protocols for user-related data in the Canvas API, including profiles, avatars, and page views.
tags:
    - canvas-api
    - user-management
    - api-schemas
    - user-profiles
    - data-structures
    - canvas-lms
category: api
---

API for accessing information on the current and other users.

Throughout this API, the `:user_id` parameter can be replaced with `self` as a shortcut for the id of the user accessing the API. For instance, `users/:user_id/page_views` can be accessed as `users/self/page_views` to access the current user's page views.

API for manipulating course nicknames

Course nicknames are alternate names for courses that are unique to each user. They are useful when the course's name is too long or less meaningful. If a user defines a nickname for a course, that name will be returned by the API in place of the course's actual name.

**An User object looks like:**

```
// A Canvas user, e.g. a student, teacher, administrator, observer, etc.
{
  // The ID of the user.
"id": 2,
  // The name of the user.
"name": "Sheldon Cooper",
  // The name of the user that is should be used for sorting groups of users, such
  // as in the gradebook.
"sortable_name": "Cooper, Sheldon",
  // The last name of the user.
"last_name": "Cooper",
  // The first name of the user.
"first_name": "Sheldon",
  // A short name the user has selected, for use in conversations or other less
  // formal places through the site.
"short_name": "Shelly",
  // The SIS ID associated with the user.  This field is only included if the user
  // came from a SIS import and has permissions to view SIS information.
"sis_user_id": "SHEL93921",
  // The id of the SIS import.  This field is only included if the user came from
  // a SIS import and has permissions to manage SIS information.
"sis_import_id": 18,
  // The integration_id associated with the user.  This field is only included if
  // the user came from a SIS import and has permissions to view SIS information.
"integration_id": "ABC59802",
  // The unique login id for the user.  This is what the user uses to log in to
  // Canvas.
"login_id": "sheldon@caltech.example.com",
  // If avatars are enabled, this field will be included and contain a url to
  // retrieve the user's avatar.
"avatar_url": "https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g",
  // Optional: If avatars are enabled and caller is admin, this field can be
  // requested and will contain the current state of the user's avatar.
"avatar_state": "approved",
  // Optional: This field can be requested with certain API calls, and will return
  // a list of the users active enrollments. See the List enrollments API for more
  // details about the format of these records.
"enrollments": null,
  // Optional: This field can be requested with certain API calls, and will return
  // the users primary email address.
"email": "sheldon@caltech.example.com",
  // Optional: This field can be requested with certain API calls, and will return
  // the users locale in RFC 5646 format.
"locale": "tlh",
  // Optional: This field is only returned in certain API calls, and will return a
  // timestamp representing the last time the user logged in to canvas.
"last_login": "2012-05-30T17:45:25Z",
  // Optional: This field is only returned in certain API calls, and will return
  // the IANA time zone name of the user's preferred timezone.
"time_zone": "America/Denver",
  // Optional: The user's bio.
"bio": "I like the Muppets.",
  // Optional: This field is only returned if pronouns are enabled, and will
  // return the pronouns of the user.
"pronouns": "he/him"
}
```

**An UserDisplay object looks like:**

```
// This mini-object is used for secondary user responses, when we just want to
// provide enough information to display a user.
{
  // The ID of the user.
  "id": 2,
  // A short name the user has selected, for use in conversations or other less
  // formal places through the site.
  "short_name": "Shelly",
  // If avatars are enabled, this field will be included and contain a url to
  // retrieve the user's avatar.
  "avatar_image_url": "https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g",
  // URL to access user, either nested to a context or directly.
  "html_url": "https://school.instructure.com/courses/:course_id/users/:user_id"
}
```

**An AnonymousUserDisplay object looks like:**

```
// This mini-object is returned in place of UserDisplay when returning student
// data for anonymous assignments, and includes an anonymous ID to identify a
// user within the scope of a single assignment.
{
  // A unique short ID identifying this user within the scope of a particular
  // assignment.
  "anonymous_id": "xn29Q",
  // A URL to retrieve a generic avatar.
  "avatar_image_url": "https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g",
  // The anonymized display name for the student.
  "display_name": "Student 2"
}
```

**A Profile object looks like:**

```
// Profile details for a Canvas user.
{
  // The ID of the user.
  "id": 1234,
  // Sample User
  "name": "Sample User",
  // Sample User
  "short_name": "Sample User",
  // user, sample
  "sortable_name": "user, sample",
  "title": null,
  "bio": null,
  // Name pronunciation
  "pronunciation": "Sample name pronunciation",
  // sample_user@example.com
  "primary_email": "sample_user@example.com",
  // sample_user@example.com
  "login_id": "sample_user@example.com",
  // sis1
  "sis_user_id": "sis1",
  "lti_user_id": null,
  // The avatar_url can change over time, so we recommend not caching it for more
  // than a few hours
  "avatar_url": "..url..",
  "calendar": null,
  // Optional: This field is only returned in certain API calls, and will return
  // the IANA time zone name of the user's preferred timezone.
  "time_zone": "America/Denver",
  // The users locale.
  "locale": null,
  // Optional: Whether or not the user is a K5 user. This field is nil if the user
  // settings are not for the user making the request.
  "k5_user": true,
  // Optional: Whether or not the user should see the classic font on the
  // dashboard. Only applies if k5_user is true. This field is nil if the user
  // settings are not for the user making the request.
  "use_classic_font_in_k5": false
}
```

**An Avatar object looks like:**

```
// Possible avatar for a user.
{
  // ['gravatar'|'attachment'|'no_pic'] The type of avatar record, for
  // categorization purposes.
  "type": "gravatar",
  // The url of the avatar
  "url": "https://secure.gravatar.com/avatar/2284...",
  // A unique representation of the avatar record which can be used to set the
  // avatar with the user update endpoint. Note: this is an internal
  // representation and is subject to change without notice. It should be consumed
  // with this api endpoint and used in the user update endpoint, and should not
  // be constructed by the client.
  "token": "<opaque_token>",
  // A textual description of the avatar record.
  "display_name": "user, sample",
  // ['attachment' type only] the internal id of the attachment
  "id": 12,
  // ['attachment' type only] the content-type of the attachment.
  "content-type": "image/jpeg",
  // ['attachment' type only] the filename of the attachment
  "filename": "profile.jpg",
  // ['attachment' type only] the size of the attachment
  "size": 32649
}
```

**A PageView object looks like:**

```
// The record of a user page view access in Canvas
{
  // A UUID representing the page view.  This is also the unique request id
  "id": "3e246700-e305-0130-51de-02e33aa501ef",
  // If the request is from an API request, the app that generated the access
  // token
  "app_name": "Canvas for iOS",
  // The URL requested
  "url": "https://canvas.instructure.com/conversations",
  // The type of context for the request
  "context_type": "Course",
  // The type of asset in the context for the request, if any
  "asset_type": "Discussion",
  // The rails controller that handled the request
  "controller": "discussions",
  // The rails action that handled the request
  "action": "index",
  // This field is deprecated, and will always be false
  "contributed": false,
  // An approximation of how long the user spent on the page, in seconds
  "interaction_seconds": 7.21,
  // When the request was made
  "created_at": "2013-10-01T19:49:47Z",
  // A flag indicating whether the request was user-initiated, or automatic (such
  // as an AJAX call)
  "user_request": true,
  // How long the response took to render, in seconds
  "render_time": 0.369,
  // The user-agent of the browser or program that made the request
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1",
  // True if the request counted as participating, such as submitting homework
  "participated": false,
  // The HTTP method such as GET or POST
  "http_method": "GET",
  // The origin IP address of the request
  "remote_ip": "173.194.46.71",
  // The page view links to define the relationships
  "links": {"user":1234,"account":1234}
}
```

**A PageViewLinks object looks like:**

```
// The links of a page view access in Canvas
{
  // The ID of the user for this page view
  "user": 1234,
  // The ID of the context for the request (course id if context_type is Course,
  // etc)
  "context": 1234,
  // The ID of the asset for the request, if any
  "asset": 1234,
  // The ID of the actual user who made this request, if the request was made by a
  // user who was masquerading
  "real_user": 1234,
  // The ID of the account context for this page view
  "account": 1234
}
```

**An AsyncApiErrorResponse object looks like:**

```
// Error response structure returned by the API when validation or processing
// failures occur
{
  // Array of error messages describing what went wrong with the request
  "errors": ["start_date and end_date must be the first day of the month", "end_date must be after start_date", "end_date cannot be in a future month", "The requested data cannot be older than %d months"]
}
```

**An AsyncQueryResponse object looks like:**

```
// Response returned when successfully initiating a page views query
{
  // URL endpoint to poll for query status updates
  "poll_url": "/api/v1/users/123/page_views/query/550e8400-e29b-41d4-a716-446655440000"
}
```

**An AsyncQueryStatusResponse object looks like:**

```
// Response containing the current status of a page views query
{
  // The UUID of the query being polled
  "query_id": "550e8400-e29b-41d4-a716-446655440000",
  // Current processing status of the query
  "status": "finished",
  // The format that results will be returned in
  "format": "csv",
  // URL to retrieve query results. Only present when status is 'finished'
  "results_url": "/api/v1/users/123/page_views/query/550e8400-e29b-41d4-a716-446655440000/results"
}
```

**An AsyncQueryResultsResponse object looks like:**

```
// File download response containing page views query results
{
  // The query results data in the requested format (CSV or JSON)
  "content": null,
  // Suggested filename for the downloaded results
  "filename": "550e8400-e29b-41d4-a716-446655440000.csv",
  // MIME type of the response content
  "content_type": "text/csv",
  // Content encoding if the response is compressed
  "content_encoding": "gzip"
}
```

**A CourseNickname object looks like:**

```
{
  // the ID of the course
  "course_id": 88,
  // the actual name of the course
  "name": "S1048576 DPMS1200 Intro to Newtonian Mechanics",
  // the calling user's nickname for the course
  "nickname": "Physics"
}
```

[UsersController#api\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/accounts/:account_id/users`

**Scope:** `url:GET|/api/v1/accounts/:account_id/users`

A paginated list of users associated with this account.

```
@example_request
  curl https://<canvas>/api/v1/accounts/self/users?search_term=<search value> \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

**Request Parameters:**

The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.

Note that the API will prefer matching on canonical user ID if the ID has a numeric form. It will only search against other fields if non-numeric in form, or if the numeric value doesn’t yield any matches. Queries by administrative users will search on SIS ID, Integration ID, login ID, name, or email address

When set, only return users enrolled with the specified course-level base role. This can be a base role type of ‘student’, ‘teacher’, ‘ta’, ‘observer’, or ‘designer’.

The column to sort results by. For efficiency, use `id` if you intend to retrieve many pages of results. In the future, other sort options may be rate-limited after 50 pages.

Allowed values: `username`, `email`, `sis_id`, `integration_id`, `last_login`, `id`

The order to sort the given column by.

Allowed values: `asc`, `desc`

When set to true and used with an account context, returns users who have deleted pseudonyms for the context

When set, only return users with the specified UUIDs. UUIDs after the first 100 are ignored.

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[UsersController#activity\_streamarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/self/activity_stream`

**Scope:** `url:GET|/api/v1/users/self/activity_stream`

`GET /api/v1/users/activity_stream`

**Scope:** `url:GET|/api/v1/users/activity_stream`

Returns the current user’s global activity stream, paginated.

There are many types of objects that can be returned in the activity stream. All object types have the same basic set of shared attributes:

```
{
  'created_at': '2011-07-13T09:12:00Z',
  'updated_at': '2011-07-25T08:52:41Z',
  'id': 1234,
  'title': 'Stream Item Subject',
  'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
  'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
  'read_state': false,
  'context_type': 'course', // course|group
  'course_id': 1,
  'group_id': null,
  'html_url': "http://..." // URL to the Canvas web UI for this stream item
}
```

In addition, each item type has its own set of attributes available.

DiscussionTopic:

```
{
  'type': 'DiscussionTopic',
  'discussion_topic_id': 1234,
  'total_root_discussion_entries': 5,
  'require_initial_post': true,
  'user_has_posted': true,
  'root_discussion_entries': {
    ...
  }
}
```

For DiscussionTopic, the message is truncated at 4kb.

Announcement:

```
{
  'type': 'Announcement',
  'announcement_id': 1234,
  'total_root_discussion_entries': 5,
  'require_initial_post': true,
  'user_has_posted': null,
  'root_discussion_entries': {
    ...
  }
}
```

For Announcement, the message is truncated at 4kb.

Conversation:

```
{
  'type': 'Conversation',
  'conversation_id': 1234,
  'private': false,
  'participant_count': 3,
}
```

Message:

```
{
  'type': 'Message',
  'message_id': 1234,
  'notification_category': 'Assignment Graded'
}
```

Submission:

Returns an [Submission](https://developerdocs.instructure.com/services/canvas/resources/submissions#Submission) with its Course and Assignment data.

Conference:

```
{
  'type': 'Conference',
  'web_conference_id': 1234
}
```

Collaboration:

```
{
  'type': 'Collaboration',
  'collaboration_id': 1234
}
```

AssessmentRequest:

```
{
  'type': 'AssessmentRequest',
  'assessment_request_id': 1234
}
```

**Request Parameters:**

If true, will only return objects for courses the user is actively participating in

[UsersController#activity\_stream\_summaryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/self/activity_stream/summary`

**Scope:** `url:GET|/api/v1/users/self/activity_stream/summary`

Returns a summary of the current user’s global activity stream.

**Request Parameters:**

If true, will only return objects for courses the user is actively participating in

**Example Response:**

```
[
  {
    "type": "DiscussionTopic",
    "unread_count": 2,
    "count": 7
  },
  {
    "type": "Conversation",
    "unread_count": 0,
    "count": 3
  }
]
```

[UsersController#todo\_itemsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/self/todo`

**Scope:** `url:GET|/api/v1/users/self/todo`

A paginated list of the current user’s list of todo items.

There is a limit to the number of items returned.

The ‘ignore\` and \`ignore\_permanently\` URLs can be used to update the user’s preferences on what items will be displayed. Performing a DELETE request against the ‘ignore\` URL will hide that item from future todo item requests, until the item changes. Performing a DELETE request against the \`ignore\_permanently\` URL will hide that item forever.

**Request Parameters:**

- “ungraded\_quizzes”
  
  Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list. These will be returned under a quiz key instead of an assignment key in response elements.

Allowed values: `ungraded_quizzes`

**Example Response:**

```
[
  {
    'type': 'grading',        // an assignment that needs grading
    'assignment': { .. assignment object .. },
    'ignore': '.. url ..',
    'ignore_permanently': '.. url ..',
    'html_url': '.. url ..',
    'needs_grading_count': 3, // number of submissions that need grading
    'context_type': 'course', // course|group
    'course_id': 1,
    'group_id': null,
  },
  {
    'type' => 'submitting',   // an assignment that needs submitting soon
    'assignment' => { .. assignment object .. },
    'ignore' => '.. url ..',
    'ignore_permanently' => '.. url ..',
    'html_url': '.. url ..',
    'context_type': 'course',
    'course_id': 1,
  },
  {
    'type' => 'submitting',   // a quiz that needs submitting soon
    'quiz' => { .. quiz object .. },
    'ignore' => '.. url ..',
    'ignore_permanently' => '.. url ..',
    'html_url': '.. url ..',
    'context_type': 'course',
    'course_id': 1,
  },
]
```

[UsersController#todo\_item\_countarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/self/todo_item_count`

**Scope:** `url:GET|/api/v1/users/self/todo_item_count`

Counts of different todo items such as the number of assignments needing grading as well as the number of assignments needing submitting.

There is a limit to the number of todo items this endpoint will count. It will only look at the first 100 todo items for the user. If the user has more than 100 todo items this count may not be reliable. The largest reliable number for both counts is 100.

**Request Parameters:**

- “ungraded\_quizzes”
  
  Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list. These will be returned under a quiz key instead of an assignment key in response elements.

Allowed values: `ungraded_quizzes`

**Example Response:**

```
{
  needs_grading_count: 32,
  assignments_needing_submitting: 10
}
```

[UsersController#upcoming\_eventsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/self/upcoming_events`

**Scope:** `url:GET|/api/v1/users/self/upcoming_events`

A paginated list of the current user’s upcoming events.

**Example Response:**

```
[
  {
    "id"=>597,
    "title"=>"Upcoming Course Event",
    "description"=>"Attendance is correlated with passing!",
    "start_at"=>"2013-04-27T14:33:14Z",
    "end_at"=>"2013-04-27T14:33:14Z",
    "location_name"=>"Red brick house",
    "location_address"=>"110 Top of the Hill Dr.",
    "all_day"=>false,
    "all_day_date"=>nil,
    "created_at"=>"2013-04-26T14:33:14Z",
    "updated_at"=>"2013-04-26T14:33:14Z",
    "workflow_state"=>"active",
    "context_code"=>"course_12938",
    "child_events_count"=>0,
    "child_events"=>[],
    "parent_event_id"=>nil,
    "hidden"=>false,
    "url"=>"http://www.example.com/api/v1/calendar_events/597",
    "html_url"=>"http://www.example.com/calendar?event_id=597&include_contexts=course_12938"
  },
  {
    "id"=>"assignment_9729",
    "title"=>"Upcoming Assignment",
    "description"=>nil,
    "start_at"=>"2013-04-28T14:47:32Z",
    "end_at"=>"2013-04-28T14:47:32Z",
    "all_day"=>false,
    "all_day_date"=>"2013-04-28",
    "created_at"=>"2013-04-26T14:47:32Z",
    "updated_at"=>"2013-04-26T14:47:32Z",
    "workflow_state"=>"published",
    "context_code"=>"course_12942",
    "assignment"=>{
      "id"=>9729,
      "name"=>"Upcoming Assignment",
      "description"=>nil,
      "points_possible"=>10,
      "due_at"=>"2013-04-28T14:47:32Z",
      "assignment_group_id"=>2439,
      "automatic_peer_reviews"=>false,
      "grade_group_students_individually"=>nil,
      "grading_standard_id"=>nil,
      "grading_type"=>"points",
      "group_category_id"=>nil,
      "lock_at"=>nil,
      "peer_reviews"=>false,
      "position"=>1,
      "unlock_at"=>nil,
      "course_id"=>12942,
      "submission_types"=>["none"],
      "needs_grading_count"=>0,
      "html_url"=>"http://www.example.com/courses/12942/assignments/9729"
    },
    "url"=>"http://www.example.com/api/v1/calendar_events/assignment_9729",
    "html_url"=>"http://www.example.com/courses/12942/assignments/9729"
  }
]
```

[UsersController#missing\_submissionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/:user_id/missing_submissions`

**Scope:** `url:GET|/api/v1/users/:user_id/missing_submissions`

A paginated list of past-due assignments for which the student does not have a submission. The user sending the request must either be the student, an admin or a parent observer using the parent app

**Request Parameters:**

Return missing submissions for the given observed user. Must be accompanied by course\_ids\[]. The user making the request must be observing the observed user in all the courses specified by course\_ids\[].

- “planner\_overrides”
  
  Optionally include the assignment’s associated planner override, if it exists, for the current user. These will be returned under a planner\_override key
- “course”
  
  Optionally include the assignments’ courses

Allowed values: `planner_overrides`, `course`

- “submittable”
  
  Only return assignments that the current user can submit (i.e. filter out locked assignments)
- “current\_grading\_period”
  
  Only return missing assignments that are in the current grading period

Allowed values: `submittable`, `current_grading_period`

Optionally restricts the list of past-due assignments to only those associated with the specified course IDs. Required if observed\_user\_id is passed.

Returns a list of [Assignment](https://developerdocs.instructure.com/services/canvas/resources/assignments#assignment) objects.

[UsersController#ignore\_stream\_itemarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`DELETE /api/v1/users/self/activity_stream/:id`

**Scope:** `url:DELETE|/api/v1/users/self/activity_stream/:id`

Hide the given stream item.

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/activity_stream/<stream_item_id> \
   -X DELETE \
   -H 'Authorization: Bearer <token>'
```

**Example Response:**

[UsersController#ignore\_all\_stream\_itemsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`DELETE /api/v1/users/self/activity_stream`

**Scope:** `url:DELETE|/api/v1/users/self/activity_stream`

Hide all stream items for the user

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/activity_stream \
   -X DELETE \
   -H 'Authorization: Bearer <token>'
```

**Example Response:**

[UsersController#create\_filearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`POST /api/v1/users/:user_id/files`

**Scope:** `url:POST|/api/v1/users/:user_id/files`

Upload a file to the user’s personal files section.

This API endpoint is the first step in uploading a file to a user’s files. See the [File Upload Documentation](https://developerdocs.instructure.com/services/canvas/basics/file.file_uploads) for details on the file upload workflow.

Note that typically users will only be able to upload files to their own files section. Passing a user\_id of `self` is an easy shortcut to specify the current user.

[UsersController#api\_showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/:id`

**Scope:** `url:GET|/api/v1/users/:id`

Shows details for user.

Also includes an attribute “permissions”, a non-comprehensive list of permissions for the user. Example:

```
"permissions": {
 "can_update_name": true, // Whether the user can update their name.
 "can_update_avatar": false, // Whether the user can update their avatar.
 "limit_parent_app_web_access": false // Whether the user can interact with Canvas web from the Canvas Parent app.
}
```

**Request Parameters:**

Array of additional information to include on the user record. “locale”, “avatar\_url”, “permissions”, “email”, and “effective\_locale” will always be returned

Allowed values: `uuid`, `last_login`

**Example Request:**

```
curl https://<canvas>/api/v1/users/self \
    -X GET \
    -H 'Authorization: Bearer <token>'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UsersController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`POST /api/v1/accounts/:account_id/users`

**Scope:** `url:POST|/api/v1/accounts/:account_id/users`

Create and return a new user and pseudonym for an account.

- DEPRECATED (for self-registration only)
  
  If you don’t have the “Modify

login details for users“ permission, but self-registration is enabled on the account, you can still use this endpoint to register new users. Certain fields will be required, and others will be ignored (see below).

**Request Parameters:**

The full name of the user. This name will be used by teacher for grading. Required if this is a self-registration.

User’s name as it will be displayed in discussions, messages, and comments.

User’s name as used to sort alphabetically in lists.

The user’s preferred language, from the list of languages Canvas supports. This is in RFC-5646 format.

Whether the user accepts the terms of use. Required if this is a self-registration and this canvas instance requires users to accept the terms (on by default).

If this is true, it will mark the user as having accepted the terms of use.

Automatically mark the user as registered.

If this is true, it is recommended to set `"pseudonym[send_confirmation]"` to true as well. Otherwise, the user will not receive any messages about their account creation.

The users communication channel confirmation can be skipped by setting `"communication_channel[skip_confirmation]"` to true as well.

User’s login ID. If this is a self-registration, it must be a valid email address.

User’s password. Cannot be set during self-registration.

SIS ID for the user’s account. To set this parameter, the caller must be able to manage SIS permissions.

`pseudonym[integration_id]`

Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions. The Integration ID is a secondary identifier useful for more complex SIS integrations.

`pseudonym[send_confirmation]`

Send user notification of account creation if true. Automatically set to true during self-registration.

`pseudonym[force_self_registration]`

Send user a self-registration style email if true. Setting it means the users will get a notification asking them to “complete the registration process” by clicking it, setting a password, and letting them in. Will only be executed on if the user does not need admin approval. Defaults to false unless explicitly provided.

`pseudonym[authentication_provider_id]`

The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider).

`communication_channel[type]`

The communication channel type, e.g. ‘email’ or ‘sms’.

`communication_channel[address]`

The communication channel address, e.g. the user’s email address.

`communication_channel[confirmation_url]`

Only valid for account admins. If true, returns the new user account confirmation URL in the response.

`communication_channel[skip_confirmation]`

Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel.

If this is true, it is recommended to set `"pseudonym[send_confirmation]"` to true as well. Otherwise, the user will not receive any messages about their account creation.

If true, validations are performed on the newly created user (and their associated pseudonym) even if the request is made by a privileged user like an admin. When set to false, or not included in the request parameters, any newly created users are subject to validations unless the request is made by a user with a ‘manage\_user\_logins’ right. In which case, certain validations such as ‘require\_acceptance\_of\_terms’ and ‘require\_presence\_of\_name’ are not enforced. Use this parameter to return helpful json errors while building users with an admin request.

When true, will first try to re-activate a deleted user with matching sis\_user\_id if possible. This is commonly done with `user[skip_registration]` and `communication_channel[skip_confirmation]` so that the default communication\_channel is also restored.

If you’re setting the password for the newly created user, you can provide this param with a valid URL pointing into this Canvas installation, and the response will include a destination field that’s a URL that you can redirect a browser to and have the newly created user automatically logged in. The URL is only valid for a short time, and must match the domain this request is directed to, and be for a well-formed path that Canvas can recognize.

‘observer\` if doing a self-registration with a pairing code. This allows setting the password during user creation.

If provided and valid, will link the new user as an observer to the student’s whose pairing code is given.

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UsersController#create\_self\_registered\_userarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`POST /api/v1/accounts/:account_id/self_registration`

**Scope:** `url:POST|/api/v1/accounts/:account_id/self_registration`

Self register and return a new user and pseudonym for an account.

If self-registration is enabled on the account, you can use this endpoint to self register new users.

**Request Parameters:**

The full name of the user. This name will be used by teacher for grading.

User’s name as it will be displayed in discussions, messages, and comments.

User’s name as used to sort alphabetically in lists.

The user’s preferred language, from the list of languages Canvas supports. This is in RFC-5646 format.

Whether the user accepts the terms of use.

User’s login ID. Must be a valid email address.

`communication_channel[type]`

The communication channel type, e.g. ‘email’ or ‘sms’.

`communication_channel[address]`

The communication channel address, e.g. the user’s email address.

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UsersController#settingsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/:id/settings`

**Scope:** `url:GET|/api/v1/users/:id/settings`

`PUT /api/v1/users/:id/settings`

**Scope:** `url:PUT|/api/v1/users/:id/settings`

Update an existing user’s settings.

**Request Parameters:**

If true, require user to manually mark discussion posts as read (don’t auto-mark as read).

`release_notes_badge_disabled`

If true, hide the badge for new release notes.

If true, the user’s page loads with the global navigation collapsed

If true, the user’s course pages will load with the course navigation collapsed.

`hide_dashcard_color_overlays`

If true, images on course cards will be presented without being tinted to match the course color.

`comment_library_suggestions_enabled`

If true, suggestions within the comment library will be shown.

`elementary_dashboard_disabled`

If true, will display the user’s preferred class Canvas dashboard view instead of the canvas for elementary view.

`widget_dashboard_user_preference`

If true, enables the widget dashboard for the user. Only applies when the widget\_dashboard feature is enabled at the account level. Defaults to true when the feature becomes available.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/settings \
  -X PUT \
  -F 'manual_mark_as_read=true'
  -H 'Authorization: Bearer <token>'
```

[UsersController#get\_custom\_colorsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/:id/colors`

**Scope:** `url:GET|/api/v1/users/:id/colors`

Returns all custom colors that have been saved for a user.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/colors/ \
  -X GET \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "custom_colors": {
    "course_42": "#abc123",
    "course_88": "#123abc"
  }
}
```

[UsersController#get\_custom\_colorarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/:id/colors/:asset_string`

**Scope:** `url:GET|/api/v1/users/:id/colors/:asset_string`

Returns the custom colors that have been saved for a user for a given context.

The asset\_string parameter should be in the format ‘context\_id’, for example ‘course\_42’.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/colors/<asset_string> \
  -X GET \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

[UsersController#set\_custom\_colorarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`PUT /api/v1/users/:id/colors/:asset_string`

**Scope:** `url:PUT|/api/v1/users/:id/colors/:asset_string`

Updates a custom color for a user for a given context. This allows colors for the calendar and elsewhere to be customized on a user basis.

The asset string parameter should be in the format ‘context\_id’, for example ‘course\_42’

**Request Parameters:**

The hexcode of the color to set for the context, if you choose to pass the hexcode as a query parameter rather than in the request body you should NOT include the ‘#’ unless you escape it first.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/colors/<asset_string> \
  -X PUT \
  -F 'hexcode=fffeee'
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

[UsersController#set\_text\_editor\_preferencearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`PUT /api/v1/users/:id/text_editor_preference`

**Scope:** `url:PUT|/api/v1/users/:id/text_editor_preference`

Updates a user’s default choice for text editor. This allows the Choose an Editor propmts to preload the user’s preference.

**Request Parameters:**

The identifier for the editor.

Allowed values: `block_editor`, `rce`, \`\`

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/prefered_editor \
  -X PUT \
  -F 'text_editor_preference=rce'
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "text_editor_preference": "rce"
}
```

[UsersController#set\_files\_ui\_version\_preferencearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`PUT /api/v1/users/:id/files_ui_version_preference`

**Scope:** `url:PUT|/api/v1/users/:id/files_ui_version_preference`

Updates a user’s default choice for files UI version. This allows the files UI to preload the user’s preference.

**Request Parameters:**

The identifier for the files UI version.

Allowed values: `v1`, `v2`

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/files_ui_version_preference \
  -X PUT \
  -F 'files_ui_version=v2'
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "files_ui_version": "v2"
}
```

[UsersController#get\_dashboard\_positionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/:id/dashboard_positions`

**Scope:** `url:GET|/api/v1/users/:id/dashboard_positions`

Returns all dashboard positions that have been saved for a user.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/dashboard_positions/ \
  -X GET \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "dashboard_positions": {
    "course_42": 2,
    "course_88": 1
  }
}
```

[UsersController#set\_dashboard\_positionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`PUT /api/v1/users/:id/dashboard_positions`

**Scope:** `url:PUT|/api/v1/users/:id/dashboard_positions`

Updates the dashboard positions for a user for a given context. This allows positions for the dashboard cards and elsewhere to be customized on a per user basis.

The asset string parameter should be in the format ‘context\_id’, for example ‘course\_42’

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/dashboard_positions/ \
  -X PUT \
  -F 'dashboard_positions[course_42]=1' \
  -F 'dashboard_positions[course_53]=2' \
  -F 'dashboard_positions[course_10]=3' \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "dashboard_positions": {
    "course_10": 3,
    "course_42": 1,
    "course_53": 2
  }
}
```

[UsersController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`PUT /api/v1/users/:id`

**Scope:** `url:PUT|/api/v1/users/:id`

Modify an existing user. To modify a user’s login, see the documentation for logins.

**Request Parameters:**

The full name of the user. This name will be used by teacher for grading.

User’s name as it will be displayed in discussions, messages, and comments.

User’s name as used to sort alphabetically in lists.

The default email address of the user.

The user’s preferred language, from the list of languages Canvas supports. This is in RFC-5646 format.

A unique representation of the avatar record to assign as the user’s current avatar. This token can be obtained from the user avatars endpoint. This supersedes the `user[avatar][url]` argument, and if both are included the url will be ignored. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.

To set the user’s avatar to point to an external url, do not include a token and instead pass the url here. Warning: For maximum compatibility, please use 128 px square images.

To set the state of user’s avatar. Only valid for account administrator.

Allowed values: `none`, `submitted`, `approved`, `locked`, `reported`, `re_reported`

Sets a title on the user profile. (See [Get user profile](https://developerdocs.instructure.com/services/canvas/resources/users#method.profile.settings).) Profiles must be enabled on the root account.

Sets a bio on the user profile. (See [Get user profile](https://developerdocs.instructure.com/services/canvas/resources/users#method.profile.settings).) Profiles must be enabled on the root account.

Sets name pronunciation on the user profile. (See [Get user profile](https://developerdocs.instructure.com/services/canvas/resources/users#method.profile.settings).) Profiles and name pronunciation must be enabled on the root account.

Sets pronouns on the user profile. Passing an empty string will empty the user’s pronouns Only Available Pronouns set on the root account are allowed Adding and changing pronouns must be enabled on the root account.

Suspends or unsuspends all logins for this user that the calling user has permission to

Allowed values: `suspend`, `unsuspend`

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/133' \
     -X PUT \
     -F 'user[name]=Sheldon Cooper' \
     -F 'user[short_name]=Shelly' \
     -F 'user[time_zone]=Pacific Time (US & Canada)' \
     -F 'user[avatar][token]=<opaque_token>' \
     -H "Authorization: Bearer <token>"
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UsersController#terminate\_sessionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`DELETE /api/v1/users/:id/sessions`

**Scope:** `url:DELETE|/api/v1/users/:id/sessions`

Terminates all sessions for a user. This includes all browser-based sessions and all access tokens, including manually generated ones. The user can immediately re-authenticate to access Canvas again if they have the current credentials. All integrations will need to be re-authorized.

[UsersController#expire\_mobile\_sessionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`DELETE /api/v1/users/mobile_sessions`

**Scope:** `url:DELETE|/api/v1/users/mobile_sessions`

`DELETE /api/v1/users/:id/mobile_sessions`

**Scope:** `url:DELETE|/api/v1/users/:id/mobile_sessions`

Permanently expires any active mobile sessions, forcing them to re-authorize.

The route that takes a user id will expire mobile sessions for that user. The route that doesn’t take a user id will expire mobile sessions for **all** users in the institution (except for account administrators if `skip_admins` is given).

**Request Parameters:**

If true, will not expire mobile sessions for account administrators.

[UsersController#merge\_intoarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`PUT /api/v1/users/:id/merge_into/:destination_user_id`

**Scope:** `url:PUT|/api/v1/users/:id/merge_into/:destination_user_id`

`PUT /api/v1/users/:id/merge_into/accounts/:destination_account_id/users/:destination_user_id`

**Scope:** `url:PUT|/api/v1/users/:id/merge_into/accounts/:destination_account_id/users/:destination_user_id`

Merge a user into another user. To merge users, the caller must have permissions to manage both users. This should be considered irreversible. This will delete the user and move all the data into the destination user.

User merge details and caveats: The from\_user is the user that was deleted in the user\_merge process. The destination\_user is the user that remains, that is being split.

Avatars: When both users have avatars, only the destination\_users avatar will remain. When one user has an avatar, it will end up on the destination\_user.

Terms of Use: If either user has accepted terms of use, it will be be left as accepted.

Communication Channels: All unique communication channels moved to the destination\_user. All notification preferences are moved to the destination\_user.

Enrollments: All unique enrollments are moved to the destination\_user. When there is an enrollment that would end up making it so that a user would be observing themselves, the enrollment is not moved over. Everything that is tied to the from\_user at the course level relating to the enrollment is also moved to the destination\_user.

Submissions: All submissions are moved to the destination\_user. If there are enrollments for both users in the same course, we prefer submissions that have grades then submissions that have work in them, and if there are no grades or no work, they are not moved.

Other notes: Access Tokens are moved on merge. Conversations are moved on merge. Favorites are moved on merge. Courses will commonly use LTI tools. LTI tools reference the user with IDs that are stored on a user object. Merging users deletes one user and moves all records from the deleted user to the destination\_user. These IDs are kept for all enrollments, group\_membership, and account\_users for the from\_user at the time of the merge. When the destination\_user launches an LTI tool from a course that used to be the from\_user’s, it doesn’t appear as a new user to the tool provider. Instead it will send the stored ids. The destination\_user’s LTI IDs remain as they were for the courses that they originally had. Future enrollments for the destination\_user will use the IDs that are on the destination\_user object. LTI IDs that are kept and tracked per context include lti\_context\_id, lti\_id and uuid. APIs that return the LTI ids will return the one for the context that it is called for, except for the user uuid. The user UUID will display the destination\_users uuid, and when getting the uuid from an api that is in a context that was recorded from a merge event, an additional attribute is added as past\_uuid.

When finding users by SIS ids in different accounts the destination\_account\_id is required.

The account can also be identified by passing the domain in destination\_account\_id.

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/merge_into/<destination_user_id> \
     -X PUT \
     -H 'Authorization: Bearer <token>'
```

```
curl https://<canvas>/api/v1/users/<user_id>/merge_into/accounts/<destination_account_id>/users/<destination_user_id> \
     -X PUT \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UsersController#splitarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`POST /api/v1/users/:id/split`

**Scope:** `url:POST|/api/v1/users/:id/split`

Merged users cannot be fully restored to their previous state, but this will attempt to split as much as possible to the previous state. To split a merged user, the caller must have permissions to manage all of the users logins. If there are multiple users that have been merged into one user it will split each merge into a separate user. A split can only happen within 180 days of a user merge. A user merge deletes the previous user and may be permanently deleted. In this scenario we create a new user object and proceed to move as much as possible to the new user. The user object will not have preserved the name or settings from the previous user. Some items may have been deleted during a user\_merge that cannot be restored, and/or the data has become stale because of other changes to the objects since the time of the user\_merge.

Split users details and caveats:

The from\_user is the user that was deleted in the user\_merge process. The destination\_user is the user that remains, that is being split.

Avatars: When both users had avatars, both will be remain. When from\_user had an avatar and destination\_user did not have an avatar, the destination\_user’s avatar will be deleted if it still matches what was there are the time of the merge. If the destination\_user’s avatar was changed at anytime after the merge, it will remain on the destination user. If the from\_user had an avatar it will be there after split.

Terms of Use: If from\_user had not accepted terms of use, they will be prompted again to accept terms of use after the split. If the destination\_user had not accepted terms of use, hey will be prompted again to accept terms of use after the split. If neither user had accepted the terms of use, but since the time of the merge had accepted, both will be prompted to accept terms of use. If both had accepted terms of use, this will remain.

Communication Channels: All communication channels are restored to what they were prior to the merge. If a communication channel was added after the merge, it will remain on the destination\_user. Notification preferences remain with the communication channels.

Enrollments: All enrollments from the time of the merge will be moved back to where they were. Enrollments created since the time of the merge that were created by sis\_import will go to the user that owns that sis\_id used for the import. Other new enrollments will remain on the destination\_user. Everything that is tied to the destination\_user at the course level relating to an enrollment is moved to the from\_user. When both users are in the same course prior to merge this can cause some unexpected items to move.

Submissions: Unlike other items tied to a course, submissions are explicitly recorded to avoid problems with grades. All submissions were moved are restored to the spot prior to merge. All submission that were created in a course that was moved in enrollments are moved over to the from\_user.

Other notes: Access Tokens are moved back on split. Conversations are moved back on split. Favorites that existing at the time of merge are moved back on split. LTI ids are restored to how they were prior to merge.

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/split \
     -X POST \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[UsersController#pandata\_events\_tokenarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`POST /api/v1/users/self/pandata_events_token`

**Scope:** `url:POST|/api/v1/users/self/pandata_events_token`

Returns a jwt auth and props token that can be used to send events to Pandata.

NOTE: This is currently only available to the mobile developer keys.

**Request Parameters:**

The pandata events appKey for this mobile app

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/pandata_events_token \
     -X POST \
     -H 'Authorization: Bearer <token>'
     -F 'app_key=MOBILE_APPS_KEY' \
```

**Example Response:**

```
{
  "url": "https://example.com/pandata/events"
  "auth_token": "wek23klsdnsoieioeoi3of9deeo8r8eo8fdn",
  "props_token": "paowinefopwienpfiownepfiownepfownef",
  "expires_at": 1521667783000,
}
```

[UsersController#user\_graded\_submissionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb)

`GET /api/v1/users/:id/graded_submissions`

**Scope:** `url:GET|/api/v1/users/:id/graded_submissions`

Returns a list of the user’s most recently graded submissions.

**Request Parameters:**

Associations to include with the group

Allowed values: `assignment`

Returns submissions for only currently active enrollments

`only_published_assignments`

Returns submissions for only published assignments

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/graded_submissions \
     -X POST \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Submission](https://developerdocs.instructure.com/services/canvas/resources/what_if_grades#submission) objects.

[ProfileController#settingsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/profile_controller.rb)

`GET /api/v1/users/:user_id/profile`

**Scope:** `url:GET|/api/v1/users/:user_id/profile`

Returns user profile data, including user id, name, and profile pic.

When requesting the profile for the user accessing the API, the user’s calendar feed URL and LTI user id will be returned as well.

Returns a [Profile](https://developerdocs.instructure.com/services/canvas/resources/users#profile) object.

[ProfileController#profile\_picsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/profile_controller.rb)

`GET /api/v1/users/:user_id/avatars`

**Scope:** `url:GET|/api/v1/users/:user_id/avatars`

A paginated list of the possible user avatar options that can be set with the user update endpoint. The response will be an array of avatar records. If the ‘type’ field is ‘attachment’, the record will include all the normal attachment json fields; otherwise it will include only the ‘url’ and ‘display\_name’ fields. Additionally, all records will include a ‘type’ field and a ‘token’ field. The following explains each field in more detail

- type
  
  “gravatar”|“attachment”|“no\_pic”
  
  The type of avatar record, for categorization purposes.
- “gravatar”|“attachment”|“no\_pic”
  
  The type of avatar record, for categorization purposes.
- “gravatar”|“attachment”|“no\_pic”
  
  The type of avatar record, for categorization purposes.

url

The url of the avatar

token

A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.

display\_name

A textual description of the avatar record

id

- ‘attachment’ type only
  
  the internal id of the attachment

content-type

- ‘attachment’ type only
  
  the content-type of the attachment

filename

- ‘attachment’ type only
  
  the filename of the attachment

size

- ‘attachment’ type only
  
  the size of the attachment

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/1/avatars.json' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

```
[
  {
    "type":"gravatar",
    "url":"https://secure.gravatar.com/avatar/2284...",
    "token":<opaque_token>,
    "display_name":"gravatar pic"
  },
  {
    "type":"attachment",
    "url":<url to fetch thumbnail of attachment>,
    "token":<opaque_token>,
    "display_name":"profile.jpg",
    "id":12,
    "content-type":"image/jpeg",
    "filename":"profile.jpg",
    "size":32649
  },
  {
    "type":"no_pic",
    "url":"https://<canvas>/images/dotted_pic.png",
    "token":<opaque_token>,
    "display_name":"no pic"
  }
]
```

Returns a list of [Avatar](https://developerdocs.instructure.com/services/canvas/resources/users#avatar) objects.

[PageViewsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/page_views_controller.rb)

`GET /api/v1/users/:user_id/page_views`

**Scope:** `url:GET|/api/v1/users/:user_id/page_views`

Return a paginated list of the user’s page view history in json format, similar to the available CSV download. Page views are returned in descending order, newest to oldest.

**Disclaimer**: The data is a best effort attempt, and is not guaranteed to be complete or wholly accurate. This data is meant to be used for rollups and analysis in the aggregate, not in isolation for auditing, or other high-stakes analysis involving examining single users or small samples. Page Views data is generated from the Canvas logs files, not a transactional database, there are many places along the way data can be lost and/or duplicated (though uncommon). Additionally, given the size of this data, our processes ensure that errors can be rectified at any point in time, with corrections integrated as soon as they are identified and processed.

**Request Parameters:**

The beginning of the time range from which you want page views.

The end of the time range from which you want page views.

Returns a list of [PageView](https://developerdocs.instructure.com/services/canvas/resources/users#pageview) objects.

[PageViewsController#queryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/page_views_controller.rb)

`POST /api/v1/users/:user_id/page_views/query`

**Scope:** `url:POST|/api/v1/users/:user_id/page_views/query`

Initiates an asynchronous query for user page views data within a specified date range. This method enqueues a background job to process the page views query and returns a polling URL that can be used to check the query status and retrieve results when ready.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

**Request Parameters:**

The start date for the page views query in YYYY-MM-DD format. Must be the first day of a month.

The end date for the page views query in YYYY-MM-DD format. Must be the first day of a month and after start\_date.

The desired format for the query results. Supported formats: “csv”, “jsonl”

**Example Request:**

```
curl https://<canvas>/api/v1/users/:user_id/page_views/query \
  -X POST \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "start_date": "2023-01-01",
    "end_date": "2023-02-01",
    "results_format": "csv"
  }'
```

**Example Response:**

```
201
{
  "poll_url": "/api/v1/users/123/page_views/query/550e8400-e29b-41d4-a716-446655440000"
}
```

```
400
{
  "error": "Page Views received an invalid or malformed request."
}
```

```
429
{
  "error": "Page Views rate limit exceeded. Please wait and try again."
}
```

Returns an [AsyncQueryResponse](https://developerdocs.instructure.com/services/canvas/resources/users#asyncqueryresponse) object.

[PageViewsController#poll\_queryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/page_views_controller.rb)

`GET /api/v1/users/:user_id/page_views/query/:query_id`

**Scope:** `url:GET|/api/v1/users/:user_id/page_views/query/:query_id`

Checks the status of a previously initiated page views query. Returns the current processing status and provides a result URL when the query is complete.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

**Request Parameters:**

The UUID of the query to check status for

**Example Request:**

```
curl https://<canvas>/api/v1/users/:user_id/page_views/query/:query_id \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
200
{
  "query_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "finished",
  "format": "csv",
  "results_url": "/api/v1/users/123/page_views/query/550e8400-e29b-41d4-a716-446655440000/results"
}
```

```
200
{
  "query_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "processing",
  "format": "csv",
  "results_url": null
}
```

```
400
{
  "error": "Invalid query ID"
}
```

```
404
{
  "error": "The query was not found."
}
```

Returns an [AsyncQueryStatusResponse](https://developerdocs.instructure.com/services/canvas/resources/users#asyncquerystatusresponse) object.

[PageViewsController#query\_resultsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/page_views_controller.rb)

`GET /api/v1/users/:user_id/page_views/query/:query_id/results`

**Scope:** `url:GET|/api/v1/users/:user_id/page_views/query/:query_id/results`

Retrieves the results of a completed page views query. Returns the data in the format specified when the query was initiated (CSV or JSON). The response may be compressed with gzip encoding.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

**Request Parameters:**

The UUID of the completed query to retrieve results for

**Example Request:**

```
curl https://<canvas>/api/v1/users/:user_id/page_views/query/:query_id/results \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
200
# Returns file download with appropriate Content-Type header
# Content-Type: text/csv (for CSV format)
# Content-Type: application/jsonl (for JSON lines format)
# Content-Encoding: gzip (if compressed)
# Content-Disposition: attachment; filename="550e8400-e29b-41d4-a716-446655440000.csv"
```

```
204
# No Content - Query completed but produced no results
```

```
400
{
  "error": "Query results are not in a valid state for download"
}
```

```
404
{
  "error": "The result for query was not found."
}
```

```
500
{
  "error": "An unexpected error occurred."
}
```

[CustomDataController#set\_dataarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_data_controller.rb)

`PUT /api/v1/users/:user_id/custom_data(/*scope)`

**Scope:** `url:PUT|/api/v1/users/:user_id/custom_data(/*scope)`

Store arbitrary user data as JSON.

Arbitrary JSON data can be stored for a User. A typical scenario would be an external site/service that registers users in Canvas and wants to capture additional info about them. The part of the URL that follows `/custom_data/` defines the scope of the request, and it reflects the structure of the JSON data to be stored or retrieved.

The value `self` may be used for `user_id` to store data associated with the calling user. In order to access another user’s custom data, you must be an account administrator with permission to manage users.

A namespace parameter, `ns`, is used to prevent custom\_data collisions between different apps. This parameter is required for all custom\_data requests.

A request with Content-Type multipart/form-data or Content-Type application/x-www-form-urlencoded can only be used to store strings.

Example PUT with multipart/form-data data:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
  -X PUT \
  -F 'ns=com.my-organization.canvas-app' \
  -F 'data=555-1234' \
  -H 'Authorization: Bearer <token>'
```

Response:

Subscopes (or, generated scopes) can also be specified by passing values to `data`\[`subscope`].

Example PUT specifying subscopes:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \
  -X PUT \
  -F 'ns=com.my-organization.canvas-app' \
  -F 'data[waist]=32in' \
  -F 'data[inseam]=34in' \
  -F 'data[chest]=40in' \
  -H 'Authorization: Bearer <token>'
```

Response:

```
{
  "data": {
    "chest": "40in",
    "waist": "32in",
    "inseam": "34in"
  }
}
```

Following such a request, subsets of the stored data to be retrieved directly from a subscope.

Example [GET](https://developerdocs.instructure.com/services/canvas/resources/users#method.users.get_custom_data) from a generated scope

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \
  -X GET \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

Response:

If you want to store more than just strings (i.e. numbers, arrays, hashes, true, false, and/or null), you must make a request with Content-Type application/json as in the following example.

Example PUT with JSON data:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{
        "ns": "com.my-organization.canvas-app",
        "data": {
          "a-number": 6.02e23,
          "a-bool": true,
          "a-string": "true",
          "a-hash": {"a": {"b": "ohai"}},
          "an-array": [1, "two", null, false]
        }
      }' \
  -H 'Authorization: Bearer <token>'
```

Response:

```
{
  "data": {
    "a-number": 6.02e+23,
    "a-bool": true,
    "a-string": "true",
    "a-hash": {
      "a": {
        "b": "ohai"
      }
    },
    "an-array": [1, "two", null, false]
  }
}
```

If the data is an Object (as it is in the above example), then subsets of the data can be accessed by including the object’s (possibly nested) keys in the scope of a GET request.

Example [GET](https://developerdocs.instructure.com/services/canvas/resources/users#method.users.get_custom_data) with a generated scope:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \
  -X GET \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

Response:

On success, this endpoint returns an object containing the data that was stored.

Responds with status code 200 if the scope already contained data, and it was overwritten by the data specified in the request.

Responds with status code 201 if the scope was previously empty, and the data specified in the request was successfully stored there.

Responds with status code 400 if the namespace parameter, `ns`, is missing or invalid, or if the `data` parameter is missing.

Responds with status code 409 if the requested scope caused a conflict and data was not stored. This happens when storing data at the requested scope would cause data at an outer scope to be lost. e.g., if `/custom_data` was {“fashion\_app”: {“hair”: “blonde”}}, but you tried to ‘PUT /custom\_data/fashion\_app/hair/style -F data=buzz\`, then for the request to succeed,the value of `/custom_data/fashion_app/hair` would have to become a hash, and its old string value would be lost. In this situation, an error object is returned with the following format:

```
{
  "message": "write conflict for custom_data hash",
  "conflict_scope": "fashion_app/hair",
  "type_at_conflict": "String",
  "value_at_conflict": "blonde"
}
```

**Request Parameters:**

The namespace under which to store the data. This should be something other Canvas API apps aren’t likely to use, such as a reverse DNS for your organization.

The data you want to store for the user, at the specified scope. If the data is composed of (possibly nested) JSON objects, scopes will be generated for the (nested) keys (see examples).

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/food_app' \
  -X PUT \
  -F 'ns=com.my-organization.canvas-app' \
  -F 'data[weight]=81kg' \
  -F 'data[favorites][meat]=pork belly' \
  -F 'data[favorites][dessert]=pistachio ice cream' \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "data": {
    "weight": "81kg",
    "favorites": {
      "meat": "pork belly",
      "dessert": "pistachio ice cream"
    }
  }
}
```

[CustomDataController#get\_dataarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_data_controller.rb)

`GET /api/v1/users/:user_id/custom_data(/*scope)`

**Scope:** `url:GET|/api/v1/users/:user_id/custom_data(/*scope)`

Load custom user data.

Arbitrary JSON data can be stored for a User. This API call retrieves that data for a (optional) given scope. See [Store Custom Data](https://developerdocs.instructure.com/services/canvas/resources/users#method.users.set_custom_data) for details and examples.

On success, this endpoint returns an object containing the data that was requested.

Responds with status code 400 if the namespace parameter, `ns`, is missing or invalid, or if the specified scope does not contain any data.

**Request Parameters:**

The namespace from which to retrieve the data. This should be something other Canvas API apps aren’t likely to use, such as a reverse DNS for your organization.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/food_app/favorites/dessert' \
  -X GET \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "data": "pistachio ice cream"
}
```

[CustomDataController#delete\_dataarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_data_controller.rb)

`DELETE /api/v1/users/:user_id/custom_data(/*scope)`

**Scope:** `url:DELETE|/api/v1/users/:user_id/custom_data(/*scope)`

Delete custom user data.

Arbitrary JSON data can be stored for a User. This API call deletes that data for a given scope. Without a scope, all custom\_data is deleted. See [Store Custom Data](https://developerdocs.instructure.com/services/canvas/resources/users#method.users.set_custom_data) for details and examples of storage and retrieval.

As an example, we’ll store some data, then delete a subset of it.

Example [PUT](https://developerdocs.instructure.com/services/canvas/resources/users#method.users.set_custom_data) with valid JSON data:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
  -X PUT \
  -F 'ns=com.my-organization.canvas-app' \
  -F 'data[fruit][apple]=so tasty' \
  -F 'data[fruit][kiwi]=a bit sour' \
  -F 'data[veggies][root][onion]=tear-jerking' \
  -H 'Authorization: Bearer <token>'
```

Response:

```
{
  "data": {
    "fruit": {
      "apple": "so tasty",
      "kiwi": "a bit sour"
    },
    "veggies": {
      "root": {
        "onion": "tear-jerking"
      }
    }
  }
}
```

Example DELETE:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \
  -X DELETE \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

Response:

Example [GET](https://developerdocs.instructure.com/services/canvas/resources/users#method.users.get_custom_data) following the above DELETE:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
  -X GET \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

Response:

```
{
  "data": {
    "fruit": {
      "apple": "so tasty"
    },
    "veggies": {
      "root": {
        "onion": "tear-jerking"
      }
    }
  }
}
```

Note that hashes left empty after a DELETE will get removed from the custom\_data store. For example, following the previous commands, if we delete /custom\_data/veggies/root/onion, then the entire /custom\_data/veggies scope will be removed.

Example DELETE that empties a parent scope:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \
  -X DELETE \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

Response:

```
{
  "data": "tear-jerking"
}
```

Example [GET](https://developerdocs.instructure.com/services/canvas/resources/users#method.users.get_custom_data) following the above DELETE:

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
  -X GET \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

Response:

```
{
  "data": {
    "fruit": {
      "apple": "so tasty"
    }
  }
}
```

On success, this endpoint returns an object containing the data that was deleted.

Responds with status code 400 if the namespace parameter, `ns`, is missing or invalid, or if the specified scope does not contain any data.

**Request Parameters:**

The namespace from which to delete the data. This should be something other Canvas API apps aren’t likely to use, such as a reverse DNS for your organization.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \
  -X DELETE \
  -F 'ns=com.my-organization.canvas-app' \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
!!!javascript
{
  "data": "a bit sour"
}
```

[CourseNicknamesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_nicknames_controller.rb)

`GET /api/v1/users/self/course_nicknames`

**Scope:** `url:GET|/api/v1/users/self/course_nicknames`

Returns all course nicknames you have set.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/course_nicknames \
  -H 'Authorization: Bearer <token>'
```

Returns a list of [CourseNickname](https://developerdocs.instructure.com/services/canvas/resources/users#coursenickname) objects.

[CourseNicknamesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_nicknames_controller.rb)

`GET /api/v1/users/self/course_nicknames/:course_id`

**Scope:** `url:GET|/api/v1/users/self/course_nicknames/:course_id`

Returns the nickname for a specific course.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/course_nicknames/<course_id> \
  -H 'Authorization: Bearer <token>'
```

Returns a [CourseNickname](https://developerdocs.instructure.com/services/canvas/resources/users#coursenickname) object.

[CourseNicknamesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_nicknames_controller.rb)

`PUT /api/v1/users/self/course_nicknames/:course_id`

**Scope:** `url:PUT|/api/v1/users/self/course_nicknames/:course_id`

Set a nickname for the given course. This will replace the course’s name in output of API calls you make subsequently, as well as in selected places in the Canvas web user interface.

**Request Parameters:**

The nickname to set. It must be non-empty and shorter than 60 characters.

**Example Request:**

```
curl'https://<canvas>/api/v1/users/self/course_nicknames/<course_id> \
  -X PUT \
  -F 'nickname=Physics' \
  -H 'Authorization:Bearer<token>'
```

Returns a [CourseNickname](https://developerdocs.instructure.com/services/canvas/resources/users#coursenickname) object.

[CourseNicknamesController#deletearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_nicknames_controller.rb)

`DELETE /api/v1/users/self/course_nicknames/:course_id`

**Scope:** `url:DELETE|/api/v1/users/self/course_nicknames/:course_id`

Remove the nickname for the given course. Subsequent course API calls will return the actual name for the course.

**Example Request:**

```
curl'https://<canvas>/api/v1/users/self/course_nicknames/<course_id> \
  -X DELETE \
  -H 'Authorization:Bearer<token>'
```

Returns a [CourseNickname](https://developerdocs.instructure.com/services/canvas/resources/users#coursenickname) object.

[CourseNicknamesController#cleararrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_nicknames_controller.rb)

`DELETE /api/v1/users/self/course_nicknames`

**Scope:** `url:DELETE|/api/v1/users/self/course_nicknames`

Remove all stored course nicknames.

**Example Request:**

```
curl'https://<canvas>/api/v1/users/self/course_nicknames \
  -X DELETE \
  -H 'Authorization:Bearer<token>'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).