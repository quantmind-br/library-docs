---
title: Forum | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/caliper-ims-1.1/file.data_service_caliper_forum
source: sitemap
fetched_at: 2026-02-15T09:12:48.159913-03:00
rendered_js: false
word_count: 178
summary: This document defines the triggers and data structures for discussion-related events in Canvas LMS, including replies and new topic creations formatted according to Caliper standards.
tags:
    - canvas-lms
    - caliper-analytics
    - discussion-events
    - event-schema
    - lms-integration
    - message-events
category: reference
---

**Definition:** The event is emitted anytime an end user or a system replies to a discussion topic or thread.

**Trigger:** Triggered when a user replies to the discussion topic or thread.

**data\[0].group.extensions\["com.instructure.canvas"].context\_type**

Canvas context type where the action took place e.g context\_type = Course.

**data\[0].group.extensions\["com.instructure.canvas"].entity\_id**

**data\[0].object.extensions\["com.instructure.canvas"].entity\_id**

Canvas global ID of the object affected by the event

```
{
"sensor":"http://oxana.instructure.com/",
"sendTime":"2019-11-16T02:09:04.044Z",
"dataVersion":"http://purl.imsglobal.org/ctx/caliper/v1p1",
"data":[
{
"@context":"http://purl.imsglobal.org/ctx/caliper/v1p1",
"id":"urn:uuid:9cc50e7d-2cf0-4ba7-a35f-c299cc7a6ca3",
"type":"MessageEvent",
"actor":{
"id":"urn:instructure:canvas:user:21070000000098765",
"type":"Person",
"extensions":{
"com.instructure.canvas":{
"user_login":"oxana@example.com",
"user_sis_id":"456-T45",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"entity_id":"21070000000098765"
}
}
},
"action":"Posted",
"object":{
"id":"urn:instructure:canvas:discussionEntry:2134567",
"type":"Message",
"extensions":{
"com.instructure.canvas":{
"entity_id":"2134567"
}
},
"isPartOf":{
"id":"urn:instructure:canvas:discussion:123456",
"type":"Thread"
},
"body":"<p>test this discussion</p>"
},
"eventTime":"2019-11-01T19:11:03.933Z",
"referrer":"https://oxana.instructure.com/courses/2982/discussion_topics/123456",
"edApp":{
"id":"http://oxana.instructure.com/",
"type":"SoftwareApplication"
},
"group":{
"id":"urn:instructure:canvas:course:21070000000000565",
"type":"CourseOffering",
"extensions":{
"com.instructure.canvas":{
"context_type":"Course",
"entity_id":"21070000000000565"
}
}
},
"membership":{
"id":"urn:instructure:canvas:course:21070000000000565:Learner:21070000000098765",
"type":"Membership",
"member":{
"id":"urn:instructure:canvas:user:21070000000098765",
"type":"Person"
},
"organization":{
"id":"urn:instructure:canvas:course:21070000000000565",
"type":"CourseOffering"
},
"roles":[
"Learner"
]
},
"session":{
"id":"urn:instructure:canvas:session:ef686f8ed684abf78cbfa1f6a58112b5",
"type":"Session"
},
"extensions":{
"com.instructure.canvas":{
"hostname":"oxana.instructure.com",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"client_ip":"93.184.216.34",
"request_url":"https://oxana.instructure.com/api/v1/courses/452/discussion_topics/123456/entries/62152/replies",
"version":"1.0.0"
}
}
}
]
}
```

**Definition:** The event is emitted anytime an new discussion topic is created by an end user or API request.

**Trigger:** Triggered when a new discussion topic is created in a course. Also triggered when a new course announcement is created with `is_announcement` set to TRUE.

**data\[0].group.extensions\["com.instructure.canvas"].context\_type**

Canvas context type where the action took place e.g context\_type = Course.

**data\[0].group.extensions\["com.instructure.canvas"].entity\_id**

**data\[0].object.extensions\["com.instructure.canvas"].entity\_id**

Canvas global ID of the object affected by the event

**data\[0].object.extensions\["com.instructure.canvas"].is\_announcement**

true if this topic was posted as an announcement, false otherwise

```
{
  "sensor": "http://oxana.instructure.com/",
  "sendTime": "2019-11-21T23:47:22.279Z",
  "dataVersion": "http://purl.imsglobal.org/ctx/caliper/v1p1",
  "data": [
    {
      "@context": "http://purl.imsglobal.org/ctx/caliper/v1p1",
      "id": "urn:uuid:2cdf5feb-c60c-4fbe-af47-ba48308a89ec",
      "type": "ThreadEvent",
      "actor": {
        "id": "urn:instructure:canvas:user:21070000000000001",
        "type": "Person",
        "extensions": {
          "com.instructure.canvas": {
            "user_login": "oxana",
            "user_sis_id": "456-T45",
            "root_account_id": "21070000000000001",
            "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
            "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
            "entity_id": "21070000000000001"
          }
        }
      },
      "action": "Created",
      "object": {
        "id": "urn:instructure:canvas:discussion:140000002236385",
        "type": "Thread",
        "name": "Week 10: Sin, cos, and tan",
        "extensions": {
          "com.instructure.canvas": {
            "is_announcement": true,
            "entity_id": "140000002236385"
          }
        }
      },
      "eventTime": "2019-11-01T19:11:15.491Z",
      "referrer": "https://oxana.instructure.com/courses/565/discussion_topics/new?is_announcement=true",
      "edApp": {
        "id": "http://oxana.instructure.com/",
        "type": "SoftwareApplication"
      },
      "group": {
        "id": "urn:instructure:canvas:course:565",
        "type": "CourseOffering",
        "extensions": {
          "com.instructure.canvas": {
            "context_type": "Course",
            "entity_id": "565"
          }
        }
      },
      "membership": {
        "id": "urn:instructure:canvas:course:565:Instructor:21070000000000001",
        "type": "Membership",
        "member": {
          "id": "urn:instructure:canvas:user:21070000000000001",
          "type": "Person"
        },
        "organization": {
          "id": "urn:instructure:canvas:course:565",
          "type": "CourseOffering"
        },
        "roles": [
          "Instructor"
        ]
      },
      "session": {
        "id": "urn:instructure:canvas:session:ef686f8ed684abf78cbfa1f6a58112b5",
        "type": "Session"
      },
      "extensions": {
        "com.instructure.canvas": {
          "hostname": "oxana.instructure.com",
          "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
          "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
          "client_ip": "93.184.216.34",
          "request_url": "https://oxana.instructure.com/api/v1/courses/565/discussion_topics",
          "version": "1.0.0"
        }
      }
    }
  ]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).