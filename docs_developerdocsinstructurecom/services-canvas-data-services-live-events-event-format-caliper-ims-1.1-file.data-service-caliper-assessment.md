---
title: Assessment | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/caliper-ims-1.1/file.data_service_caliper_assessment
source: sitemap
fetched_at: 2026-02-15T09:14:07.171957-03:00
rendered_js: false
word_count: 92
summary: This document defines the schema and trigger conditions for the Canvas LMS quiz submission event, detailing the structure and metadata fields of the emitted AssessmentEvent.
tags:
    - canvas-lms
    - quiz-submission
    - caliper-events
    - assessment-event
    - event-schema
    - lms-integration
category: reference
---

**Definition:** The event is emitted anytime a user submits a quiz assignment in Canvas \[old quizzes].

**Trigger:** Triggered when a user submits a quiz assignment \[old quizzes].

**data\[0].group.extensions\["com.instructure.canvas"].context\_type**

Canvas context type where the action took place e.g context\_type = Course.

**data\[0].group.extensions\["com.instructure.canvas"].entity\_id**

**data\[0].object.extensions\["com.instructure.canvas"].entity\_id**

Canvas global ID of the object affected by the event

```
{
"sensor":"http://oxana.instructure.com/",
"sendTime":"2019-11-21T21:45:17.503Z",
"dataVersion":"http://purl.imsglobal.org/ctx/caliper/v1p1",
"data":[
{
"@context":"http://purl.imsglobal.org/ctx/caliper/v1p1",
"id":"urn:uuid:06e01cb6-fdde-4327-b3f0-4c47a95d0f52",
"type":"AssessmentEvent",
"actor":{
"id":"urn:instructure:canvas:user:21070000000987123",
"type":"Person",
"extensions":{
"com.instructure.canvas":{
"user_login":"oxana",
"user_sis_id":"1243245",
"root_account_id":"21070000000000123",
"root_account_lti_guid":"f63324b4e2a0841cbbe2b48abbccedb453becf36.oxana.instructure.com",
"root_account_uuid":"01314161-1afc-0f2f-ffbf-1f31f5f0f972",
"entity_id":"21070000000987123"
}
}
},
"action":"Submitted",
"object":{
"id":"urn:instructure:canvas:submission:11210000013995723",
"type":"Attempt",
"extensions":{
"com.instructure.canvas":{
"entity_id":"11210000013995723"
}
},
"assignee":{
"id":"urn:instructure:canvas:user:21070000000987123",
"type":"Person"
},
"assignable":{
"id":"urn:instructure:canvas:quiz:11210000002223333",
"type":"Assessment"
}
},
"eventTime":"2019-11-01T19:11:33.388Z",
"referrer":"https://oxana.instructure.com/courses/100123/quizzes/2223333/take/questions/47464543",
"edApp":{
"id":"http://oxana.instructure.com/",
"type":"SoftwareApplication"
},
"group":{
"id":"urn:instructure:canvas:course:21070000000100123",
"type":"CourseOffering",
"extensions":{
"com.instructure.canvas":{
"context_type":"Course",
"entity_id":"21070000000100123"
}
}
},
"membership":{
"id":"urn:instructure:canvas:course:21070000000100123:Learner:21070000000987123",
"type":"Membership",
"member":{
"id":"urn:instructure:canvas:user:21070000000987123",
"type":"Person"
},
"organization":{
"id":"urn:instructure:canvas:course:21070000000100123",
"type":"CourseOffering"
},
"roles":[
"Learner"
]
},
"session":{
"id":"urn:instructure:canvas:session:dc29809b38908fe0890a8098b8982211",
"type":"Session"
},
"extensions":{
"com.instructure.canvas":{
"hostname":"oxana.instructure.com",
"request_id":"11394325-4220-4a39-8237-f198d193d393",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"client_ip":"93.184.216.34",
"request_url":"https://oxana.instructure.com/courses/100123/quizzes/2223333/submissions?user_id=987123",
"version":"1.0.0"
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