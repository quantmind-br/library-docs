---
title: Conferences | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/conferences
source: sitemap
fetched_at: 2026-02-15T09:05:41.742641-03:00
rendered_js: false
word_count: 181
summary: This document outlines the API endpoints and data schemas for retrieving information about conferences and their recordings within the Canvas LMS platform. It provides details on listing conferences for specific courses, groups, or all contexts associated with a user.
tags:
    - canvas-lms
    - conferences
    - rest-api
    - web-conferencing
    - recordings
    - api-reference
category: api
---

API for accessing information on conferences.

**A ConferenceRecording object looks like:**

```
{
"duration_minutes": 0,
"title": "course2: Test conference 3 [170]_0",
"updated_at": "2013-12-12T16:09:33.903-07:00",
"created_at": "2013-12-12T16:09:09.960-07:00",
"playback_url": "http://example.com/recording_url"
}
```

**A Conference object looks like:**

```
{
  // The id of the conference
"id": 170,
  // The type of conference
"conference_type": "AdobeConnect",
  // The 3rd party's ID for the conference
"conference_key": "abcdjoelisgreatxyz",
  // The description for the conference
"description": "Conference Description",
  // The expected duration the conference is supposed to last
"duration": 60,
  // The date that the conference ended at, null if it hasn't ended
"ended_at": "2013-12-13T17:23:26Z",
  // The date the conference started at, null if it hasn't started
"started_at": "2013-12-12T23:02:17Z",
  // The title of the conference
"title": "Test conference",
  // Array of user ids that are participants in the conference
"users": [1,7,8,9,10],
  // Array of user ids that are invitees in the conference
"invitees": [1,7,8,9,10],
  // Array of user ids that are attendees in the conference
"attendees": [1,7,8,9,10],
  // True if the conference type has advanced settings.
"has_advanced_settings": false,
  // If true the conference is long running and has no expected end time
"long_running": false,
  // A collection of settings specific to the conference type
"user_settings": {"record":true},
  // A List of recordings for the conference
"recordings": null,
  // URL for the conference, may be null if the conference type doesn't set it
"url": null,
  // URL to join the conference, may be null if the conference type doesn't set it
"join_url": null,
  // The type of this conference's context, typically 'Course' or 'Group'.
"context_type": null,
  // The ID of this conference's context.
"context_id": null
}
```

[ConferencesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conferences_controller.rb)

`GET /api/v1/courses/:course_id/conferences`

**Scope:** `url:GET|/api/v1/courses/:course_id/conferences`

`GET /api/v1/groups/:group_id/conferences`

**Scope:** `url:GET|/api/v1/groups/:group_id/conferences`

Retrieve the paginated list of conferences for this context

This API returns a JSON object containing the list of conferences, the key for the list of conferences is “conferences”

**Example Request:**

```
curl'https://<canvas>/api/v1/courses/<course_id>/conferences'\
-H"Authorization: Bearer <token>"
curl'https://<canvas>/api/v1/groups/<group_id>/conferences'\
-H"Authorization: Bearer <token>"
```

Returns a list of [Conference](https://developerdocs.instructure.com/services/canvas/resources/conferences#conference) objects.

[ConferencesController#for\_userarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conferences_controller.rb)

`GET /api/v1/conferences`

**Scope:** `url:GET|/api/v1/conferences`

Retrieve the paginated list of conferences for all courses and groups the current user belongs to

This API returns a JSON object containing the list of conferences. The key for the list of conferences is “conferences”.

**Request Parameters:**

If set to “live”, returns only conferences that are live (i.e., have started and not finished yet). If omitted, returns all conferences for this user’s groups and courses.

**Example Request:**

```
curl'https://<canvas>/api/v1/conferences'\
-H"Authorization: Bearer <token>"
```

Returns a list of [Conference](https://developerdocs.instructure.com/services/canvas/resources/conferences#conference) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).