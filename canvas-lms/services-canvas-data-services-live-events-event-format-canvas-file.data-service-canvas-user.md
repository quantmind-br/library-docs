---
title: User | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_user
source: sitemap
fetched_at: 2026-02-15T09:06:52.545683-03:00
rendered_js: false
word_count: 301
summary: This document defines the event schemas and triggers for user-related actions in Canvas LMS, covering account associations, user creation, and profile updates.
tags:
    - canvas-lms
    - event-stream
    - user-management
    - json-schema
    - webhooks
    - data-integration
category: reference
---

### user\_account\_association\_created

**Definition:** The event is emitted anytime a user is created in an account.

**Trigger:** Triggered when a user is added to an account.

```
{
"metadata":{
"event_name":"user_account_association_created",
"event_time":"2019-11-01T19:11:11.717Z",
"job_id":"1020020528469291",
"job_tag":"SIS::CSV::ImportRefactored#run_parallel_importer",
"producer":"canvas",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
},
"body":{
"account_id":"21070000000000079",
"account_uuid":"5CaqE03jAic6wjkvgbjaerkucZtFyIvYnsW1t62H",
"created_at":"2019-11-01T19:11:11.717Z",
"is_admin":false,
"updated_at":"2019-11-01T19:11:11.717Z",
"user_id":"21070000000000712"
}
}
```

The Canvas id of the account for this association.

The unique id of the account for this association.

The time at which this association was created.

Is user an administrator?

The time at which this association was last modified.

The Canvas id of the user for this association.

**Definition:** The event is emitted anytime a user is added to an account.

**Trigger:** Triggered when a new user is created.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Account",
    "developer_key_id": "170000000056",
    "event_name": "user_created",
    "event_time": "2019-11-01T19:11:11.964Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": null,
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/Denver",
    "url": "https://oxana.instructure.com/api/v1/accounts/1625/users",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "created_at": "2019-05-09T19:32:25Z",
    "name": "test user",
    "short_name": "test user",
    "updated_at": "2019-05-09T19:32:25Z",
    "user_id": "21070000000025999",
    "user_login": "test",
    "user_sis_id": "456-T45",
    "uuid": "kDfqdZrVWAxrI6RmFBNqipEGKozQR0sYolwPfsvM",
    "workflow_state": "pre_registered"
  }
}
```

The time at which this user was created.

The time at which this user was last modified in any way.

The login of the current user.

**Definition:** The event is emitted anytime a user details are updated. Only changes to the fields included in the body of the event payload will emit the `updated` event. The metadata of the event payload will list a user or process that updated the user profile details and the body of the event will list a user details that were updated.

**Trigger:** Triggered when a user record is updated.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_role": "TeacherEnrollment",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "event_name": "user_updated",
    "event_time": "2019-11-01T19:11:01.163Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/2635/gradebook",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": null,
    "url": "https://oxana.instructure.com/api/v1/courses/16175/gradebook_settings",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000025999",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "created_at": "2019-05-01T19:32:25Z",
    "name": "test user 1",
    "short_name": "test user 1",
    "updated_at": "019-11-01T19:11:01.163Z",
    "user_id": "21070000000025999",
    "user_login": "test",
    "user_sis_id": "456-T45",
    "uuid": "kDfqdZrVWAxrI6RmFBNqipEGKozQR0sYolwPfsvM",
    "workflow_state": "registered"
  }
}
```

The time at which this user was created.

The time at which this user was last modified in any way.

The login of the current user.

State of the user. (deleted, pre\_registered, registered)

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).