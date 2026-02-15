---
title: Announcements | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/announcements
source: sitemap
fetched_at: 2026-02-15T09:07:32.645256-03:00
rendered_js: false
word_count: 348
summary: This document specifies the Canvas LMS API endpoint for retrieving a paginated list of announcements for specific courses, including details on request parameters and authentication scopes.
tags:
    - canvas-lms
    - announcements-api
    - rest-api
    - lms-integration
    - course-management
category: api
---

API for retrieving announcements. This API is Announcement-specific. See also the Discussion Topics API, which operates on Announcements also.

[AnnouncementsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/announcements_api_controller.rb)

`GET /api/v1/announcements`

**Scope:** `url:GET|/api/v1/announcements`

Returns the paginated list of announcements for the given courses and date range. Note that a `context_code` field is added to the responses so you can tell which course each announcement belongs to.

**Request Parameters:**

List of context\_codes to retrieve announcements for (for example, `course_123`). Only courses are presently supported. The call will fail unless the caller has View Announcements permission in all listed courses.

Only return announcements posted since the start\_date (inclusive). Defaults to 14 days ago. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.

Only return announcements posted before the end\_date (inclusive). Defaults to 28 days from start\_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Announcements scheduled for future posting will only be returned to course administrators.

Only return announcements having locked\_at nil or after available\_after (exclusive). The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Effective only for students (who don’t have moderate forum right).

Only return active announcements that have been published. Applies only to requesting users that have permission to view unpublished items. Defaults to false for users with access to view unpublished items, otherwise true and unmodifiable.

Only return the latest announcement for each associated context. The response will include at most one announcement for each specified context in the context\_codes\[] parameter. Defaults to false.

Optional list of resources to include with the response. May include a string of the name of the resource. Possible values are: “sections”, “sections\_user\_count” if “sections” is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If “sections\_user\_count” is passed, then:

```
(a) If sections were asked for and the topic is specific to certain
    course sections sections, includes the number of users in each
    section. (as part of the section json asked for above)
(b) Else, includes at the root level the total number of users in the
    topic's context (group or course) that the topic applies to.
```

**Example Request:**

```
curl https://<canvas>/api/v1/announcements?context_codes[]=course_1&context_codes[]=course_2 \
     -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
[{
  "id": 1,
  "title": "Hear ye",
  "message": "Henceforth, all assignments must be...",
  "posted_at": "2017-01-31T22:00:00Z",
  "delayed_post_at": null,
  "context_code": "course_2",
  ...
}]
```

Returns a list of [DiscussionTopic](https://developerdocs.instructure.com/services/canvas/resources/discussion_topics#discussiontopic) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).