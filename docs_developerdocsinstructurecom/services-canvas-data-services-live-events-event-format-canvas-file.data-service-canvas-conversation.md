---
title: Conversation | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_conversation
source: sitemap
fetched_at: 2026-02-15T09:06:03.994818-03:00
rendered_js: false
word_count: 198
summary: This document defines the event schemas and triggers for conversation-related activities in Canvas LMS, including conversation creation, forwarding, and message generation.
tags:
    - canvas-lms
    - event-schemas
    - conversations
    - data-streaming
    - integration
    - json-metadata
category: reference
---

**Definition:** The event is emitted anytime a new conversation is initiated by the sender.

**Trigger:** Triggered when a new conversation is created.

```
{
"metadata":{
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000000123",
"user_login":"inewton@example.com",
"user_sis_id":"456-T45",
"time_zone":"America/Denver",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"client_ip":"93.184.216.34",
"url":"http://oxana.instructure.com/conversations",
"referrer":"http://oxana.instructure.com/conversations",
"producer":"canvas",
"event_name":"conversation_created",
"event_time":"2020-03-24T16:55:59.973Z"
},
"body":{
"conversation_id":"123456789",
"updated_at":"2018-09-24T06:00:00Z"
}
}
```

The Canvas id of the conversation.

The time this conversation was updated.

**Definition:** The event is emitted when a conversation is updated.

**Trigger:** Triggered when a new user is added to a conversation

```
{
  "metadata": {
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000123",
    "user_login": "inewton@example.com",
    "user_sis_id": "456-T45",
    "time_zone": "America/Denver",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "client_ip": "93.184.216.34",
    "url": "http://oxana.instructure.com/conversations/11/add_message",
    "referrer": "http://oxana.instructure.com/conversations",
    "producer": "canvas",
    "event_name": "conversation_forwarded",
    "event_time": "2020-03-27T17:30:26.715Z"
  },
  "body": {
    "conversation_id": "11",
    "updated_at": "2020-03-30T11:18:51-06:00"
  }
}
```

The Canvas id of the conversation.

The time this conversation was updated.

### conversation\_message\_created

**Definition:** The event is emitted anytime a new conversation message is added to a conversation.

**Trigger:** Triggered when a new conversation mesage is created.

```
{
"metadata":{
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000000123",
"user_login":"inewton@example.com",
"user_sis_id":"456-T45",
"time_zone":"America/Denver",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"client_ip":"93.184.216.34",
"url":"http://oxana.instructure.com/conversations/53/add_message",
"referrer":"http://oxana.instructure.com/conversations",
"producer":"canvas",
"event_name":"conversation_message_created",
"event_time":"2020-03-24T21:42:38.385Z"
},
"body":{
"author_id":"2",
"conversation_id":"53",
"created_at":"2020-03-24T21:42:37Z",
"message_id":"45"
}
}
```

The Canvas id of the author.

The Canvas id of the conversation.

The time this conversation message was created.

The Canvas id of the conversation message.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).