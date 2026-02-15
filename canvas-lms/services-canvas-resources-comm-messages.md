---
title: CommMessages | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/comm_messages
source: sitemap
fetched_at: 2026-02-15T09:05:38.131458-03:00
rendered_js: false
word_count: 139
summary: This document describes the API endpoint for retrieving a paginated list of communication messages, such as emails and SMS, sent to users in Canvas LMS. It outlines the CommMessage object structure and provides information on request parameters for filtering by user and date range.
tags:
    - canvas-lms
    - api-endpoint
    - comm-messages
    - communication
    - user-data
    - pagination
category: api
---

API for accessing the messages (emails, sms, etc) that have been sent to a user.

**A CommMessage object looks like:**

```
{
  // The ID of the CommMessage.
"id": 42,
  // The date and time this message was created
"created_at": "2013-03-19T21:00:00Z",
  // The date and time this message was sent
"sent_at": "2013-03-20T22:42:00Z",
  // The workflow state of the message. Possible values: 'created' : The message
  // has been created, but not yet processed. 'staged' : The message is queued for
  // sending. 'sending' : The message is being sent currently. 'sent' : The
  // message has been successfully sent. 'bounced' : An error occurred during the
  // sending of the message.'dashboard' : The message has been sent to the
  // dashboard. 'closed' :  The message has been sent and closed, typically for
  // dashboard messages or messages sent to deleted users. 'cancelled' : The
  // message was cancelled before it could be sent.
"workflow_state": "sent",
  // The address that was put in the 'from' field of the message
"from": "notifications@example.com",
  // The display name for the from address
"from_name": "Instructure Canvas",
  // The address the message was sent to:
"to": "someone@example.com",
  // The reply_to header of the message
"reply_to": "notifications+specialdata@example.com",
  // The message subject
"subject": "example subject line",
  // The plain text body of the message
"body": "This is the body of the message",
  // The HTML body of the message.
"html_body": "<html><body>This is the body of the message</body></html>"
}
```

[CommMessagesApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/comm_messages_api_controller.rb)

`GET /api/v1/comm_messages`

**Scope:** `url:GET|/api/v1/comm_messages`

Retrieve a paginated list of messages sent to a user.

**Request Parameters:**

The user id for whom you want to retrieve CommMessages

The beginning of the time range you want to retrieve message from. Up to a year prior to the current date is available.

The end of the time range you want to retrieve messages for. Up to a year prior to the current date is available.

Returns a list of [CommMessage](https://developerdocs.instructure.com/services/canvas/resources/comm_messages#commmessage) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).