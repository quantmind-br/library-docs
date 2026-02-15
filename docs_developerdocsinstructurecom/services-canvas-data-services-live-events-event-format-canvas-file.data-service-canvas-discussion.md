---
title: Discussion | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_discussion
source: sitemap
fetched_at: 2026-02-15T09:06:10.775136-03:00
rendered_js: false
word_count: 629
summary: This document defines the structure and triggers for discussion-related events in Canvas, providing schema details for topic creation, updates, and entry submissions. It explains the conditions under which these events are emitted and describes the metadata and body fields included in each payload.
tags:
    - canvas-lms
    - event-stream
    - discussion-topics
    - discussion-entries
    - api-reference
    - webhook-events
category: reference
---

**Definition:** The event is emitted anytime an end user or a system replies to a discussion topic or thread.

**Trigger:** Triggered when a user replies to the discussion topic or thread.

```
{
"metadata":{
"client_ip":"93.184.216.34",
"context_account_id":"21070000000000079",
"context_id":"21070000000000565",
"context_role":"StudentEnrollment",
"context_sis_source_id":"2017.100.101.101-1",
"context_type":"Course",
"event_name":"discussion_entry_created",
"event_time":"2019-11-01T19:11:03.933Z",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"producer":"canvas",
"referrer":"https://oxana.instructure.com/courses/2982/discussion_topics/123456",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"time_zone":"America/New_York",
"url":"https://oxana.instructure.com/api/v1/courses/452/discussion_topics/123456/entries/62152/replies",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000098765",
"user_login":"oxana@example.com",
"user_sis_id":"456-T45"
},
"body":{
"created_at":"2019-07-03T23:12:34Z",
"discussion_entry_id":"2134567",
"discussion_topic_id":"123456",
"parent_discussion_entry_id":"62152",
"text":"<p>test this discussion</p>",
"user_id":"98765"
}
}
```

The time at which this entry was created.

The Canvas id of the newly added entry.

The Canvas id of the topic the entry was added to.

**parent\_discussion\_entry\_id**

If this was a reply, the Canvas id of the parent entry.

The text of the post. NOTE: This field will be truncated to only include the first 8192 characters.

The Canvas id of the user being that created the entry.

### discussion\_entry\_submitted

**Definition:** The event is emitted anytime a user or system replies to a graded discussion topic.

**Trigger:** Triggered when a user replies to a graded discussion topic or discussion thread.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_role": "StudentEnrollment",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "event_name": "discussion_entry_submitted",
    "event_time": "2019-11-01T19:11:04.081Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/8720/discussion_topics/189",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": null,
    "url": "https://oxana.instructure.com/api/v1/courses/26612/discussion_topics/189/entries/59/replies",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000023481",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "assignment_id": "649",
    "created_at": "2019-07-03T23:12:34Z",
    "discussion_entry_id": "92",
    "discussion_topic_id": "189",
    "parent_discussion_entry_id": "59",
    "submission_id": "567",
    "text": "<p>test this discussion</p>",
    "user_id": "23481"
  }
}
```

The Canvas id of the assignment if the discussion topic is graded.

The time at which this entry was created.

The Canvas id of the newly added entry.

The Canvas id of the topic the entry was added to.

**parent\_discussion\_entry\_id**

If this was a reply, the Canvas id of the parent entry.

The Canvas id of the submission if the discussion topic is graded.

The text of the post. NOTE: This field will be truncated to only include the first 8192 characters.

The Canvas id of the user being that created the entry.

**Definition:** The event is emitted anytime an new discussion topic is created by an end user or API request.

**Trigger:** Triggered when a new discussion topic is created in a course. Also triggered when a new course announcement is created with `is_announcement` set to TRUE.

```
{
  "metadata": {
    "event_name": "discussion_topic_created",
    "event_time": "2019-11-01T19:11:18.208Z",
    "job_id": "1020020528469291",
    "job_tag": "Canvas::Migration::Worker::CourseCopyWorker#perform",
    "producer": "canvas",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
  },
  "body": {
    "assignment_id": "1234010",
    "body": "<h3>Discuss this</h3> What do you think?",
    "context_id": "1234560",
    "context_type": "Course",
    "discussion_topic_id": "120000001234567",
    "is_announcement": false,
    "lock_at": "2019-11-05T13:38:00.218Z",
    "title": "Sample discussion",
    "updated_at": "2019-11-05T13:38:00.218Z",
    "workflow_state": "active"
  }
}
```

The Canvas id of the topic's associated assignment

Body of the topic. NOTE: This field will be truncated to only include the first 8192 characters.

The Canvas id of the topic's context.

The type of the topic's context (usually Course or Group)

The Canvas id of the new discussion topic.

true if this topic was posted as an announcement, false otherwise.

The lock date (discussion is locked after this date), or null.

Title of the topic. NOTE: This field will be truncated to only include the first 8192 characters.

The time at which this topic was last modified in any way

The state of the discussion topic (active, deleted, post\_delayed, unpublished).

**Definition:** The event is emitted anytime a discussion topic or course announcement is updated by an end user or API request. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when a discussion topic is modified in a course. Also triggered when a course announcement is modified in a course.

```
{
"metadata":{
"client_ip":"93.184.216.34",
"context_account_id":"21070000000000079",
"context_id":"21070000000000565",
"context_role":"TeacherEnrollment",
"context_sis_source_id":"2017.100.101.101-1",
"context_type":"Course",
"event_name":"discussion_topic_updated",
"event_time":"2019-11-04T13:57:43.295Z",
"hostname":"oxana.instructure.com",
"http_method":"PUT",
"producer":"canvas",
"referrer":"https://oxana.instructure.com/courses/565/discussion_topics",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"time_zone":"America/Los_Angeles",
"url":"https://oxana.instructure.com/api/v1/courses/565/discussion_topics/66871",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000000001",
"user_login":"oxana@example.com",
"user_sis_id":"456-T45"
},
"body":{
"assignment_id":"1234010",
"body":"<h3>Discuss this</h3> What do you think?",
"context_id":"565",
"context_type":"Course",
"discussion_topic_id":"21070000000066871",
"is_announcement":false,
"lock_at":"2019-11-05T13:38:00.218Z",
"title":"Sample discussion",
"updated_at":"2019-11-05T13:38:00.218Z",
"workflow_state":"active"
}
}
```

The local Canvas id of the assignment.

Body of the topic. NOTE: This field will be truncated to only include the first 8192 characters.

The Canvas id of the topic's context.

The type of context the discussion\_topicis used in.

The Canvas id of the new discussion topic.

true if this topic was posted as an announcement, false otherwise.

The lock date (discussion is locked after this date), or null.

Title of the topic. NOTE: This field will be truncated to only include the first 8192 characters.

The time at which this discussion was last modified in any way.

The state of the discussion topic (active, deleted, post\_delayed, unpublished).

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).