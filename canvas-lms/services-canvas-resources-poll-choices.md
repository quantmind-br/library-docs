---
title: PollChoices | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/poll_choices
source: sitemap
fetched_at: 2026-02-15T09:09:26.312645-03:00
rendered_js: false
word_count: 201
summary: This document provides technical documentation for the Canvas LMS PollChoices API, detailing endpoints for listing, retrieving, creating, updating, and deleting poll options.
tags:
    - canvas-lms
    - polling
    - api-endpoints
    - poll-choices
    - rest-api
    - resource-management
category: api
---

Manage choices for polls

**A PollChoice object looks like:**

```
{
  // The unique identifier for the poll choice.
"id": 1023,
  // The id of the poll this poll choice belongs to.
"poll_id": 1779,
  // Specifies whether or not this poll choice is a 'correct' choice.
"is_correct": true,
  // The text of the poll choice.
"text": "Choice A",
  // The order of the poll choice in relation to it's sibling poll choices.
"position": 1
}
```

[Polling::PollChoicesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_choices_controller.rb)

`GET /api/v1/polls/:poll_id/poll_choices`

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_choices`

Returns the paginated list of PollChoices in this poll.

**Example Response:**

```
{
  "poll_choices": [PollChoice]
}
```

[Polling::PollChoicesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_choices_controller.rb)

`GET /api/v1/polls/:poll_id/poll_choices/:id`

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_choices/:id`

Returns the poll choice with the given id

**Example Response:**

```
{
  "poll_choices": [PollChoice]
}
```

[Polling::PollChoicesController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_choices_controller.rb)

`POST /api/v1/polls/:poll_id/poll_choices`

**Scope:** `url:POST|/api/v1/polls/:poll_id/poll_choices`

Create a new poll choice for this poll

**Request Parameters:**

The descriptive text of the poll choice.

`poll_choices[][is_correct]`

Whether this poll choice is considered correct or not. Defaults to false.

The order this poll choice should be returned in the context it’s sibling poll choices.

**Example Response:**

```
{
  "poll_choices": [PollChoice]
}
```

[Polling::PollChoicesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_choices_controller.rb)

`PUT /api/v1/polls/:poll_id/poll_choices/:id`

**Scope:** `url:PUT|/api/v1/polls/:poll_id/poll_choices/:id`

Update an existing poll choice for this poll

**Request Parameters:**

The descriptive text of the poll choice.

`poll_choices[][is_correct]`

Whether this poll choice is considered correct or not. Defaults to false.

The order this poll choice should be returned in the context it’s sibling poll choices.

**Example Response:**

```
{
"poll_choices": [PollChoice]
}
```

[Polling::PollChoicesController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_choices_controller.rb)

`DELETE /api/v1/polls/:poll_id/poll_choices/:id`

**Scope:** `url:DELETE|/api/v1/polls/:poll_id/poll_choices/:id`

**204 No Content** response code is returned if the deletion was successful.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).