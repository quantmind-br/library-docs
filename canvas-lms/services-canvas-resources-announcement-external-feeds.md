---
title: Announcement External Feeds | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/announcement_external_feeds
source: sitemap
fetched_at: 2026-02-15T09:07:27.857989-03:00
rendered_js: false
word_count: 182
summary: This document details the Announcement External Feeds API, explaining how to manage RSS and Atom feeds that automatically generate announcements for Canvas courses and groups.
tags:
    - canvas-lms
    - announcements
    - rss-feeds
    - external-feeds
    - rest-api
category: api
---

## Announcement External Feeds API

External feeds represent RSS feeds that can be attached to a Course or Group, in order to automatically create announcements for each new item in the feed.

**An ExternalFeed object looks like:**

```
{
  // The ID of the feed
"id": 5,
  // The title of the feed, pulled from the feed itself. If the feed hasn't yet
  // been pulled, a temporary name will be synthesized based on the URL
"display_name": "My Blog",
  // The HTTP/HTTPS URL to the feed
"url": "http://example.com/myblog.rss",
  // If not null, only feed entries whose title contains this string will trigger
  // new posts in Canvas
"header_match": "pattern",
  // When this external feed was added to Canvas
"created_at": "2012-06-01T00:00:00-06:00",
  // The verbosity setting determines how much of the feed's content is imported
  // into Canvas as part of the posting. 'link_only' means that only the title and
  // a link to the item. 'truncate' means that a summary of the first portion of
  // the item body will be used. 'full' means that the full item body will be
  // used.
"verbosity": "truncate"
}
```

[ExternalFeedsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_feeds_controller.rb)

`GET /api/v1/courses/:course_id/external_feeds`

**Scope:** `url:GET|/api/v1/courses/:course_id/external_feeds`

`GET /api/v1/groups/:group_id/external_feeds`

**Scope:** `url:GET|/api/v1/groups/:group_id/external_feeds`

Returns the paginated list of External Feeds this course or group.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/external_feeds \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [ExternalFeed](https://developerdocs.instructure.com/services/canvas/resources/announcement_external_feeds#externalfeed) objects.

[ExternalFeedsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_feeds_controller.rb)

`POST /api/v1/courses/:course_id/external_feeds`

**Scope:** `url:POST|/api/v1/courses/:course_id/external_feeds`

`POST /api/v1/groups/:group_id/external_feeds`

**Scope:** `url:POST|/api/v1/groups/:group_id/external_feeds`

Create a new external feed for the course or group.

**Request Parameters:**

The url to the external rss or atom feed

If given, only feed entries that contain this string in their title will be imported

Defaults to “full”

Allowed values: `full`, `truncate`, `link_only`

**Example Request:**

```
curlhttps://<canvas>/api/v1/courses/<course_id>/external_feeds\
-Furl='http://example.com/rss.xml'\
-Fheader_match='news flash!'\
-Fverbosity='full'\
-H'Authorization: Bearer <token>'
```

Returns an [ExternalFeed](https://developerdocs.instructure.com/services/canvas/resources/announcement_external_feeds#externalfeed) object.

[ExternalFeedsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_feeds_controller.rb)

`DELETE /api/v1/courses/:course_id/external_feeds/:external_feed_id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/external_feeds/:external_feed_id`

`DELETE /api/v1/groups/:group_id/external_feeds/:external_feed_id`

**Scope:** `url:DELETE|/api/v1/groups/:group_id/external_feeds/:external_feed_id`

Deletes the external feed.

**Example Request:**

```
curl-XDELETEhttps://<canvas>/api/v1/courses/<course_id>/external_feeds/<feed_id>\
-H'Authorization: Bearer <token>'
```

Returns an [ExternalFeed](https://developerdocs.instructure.com/services/canvas/resources/announcement_external_feeds#externalfeed) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).