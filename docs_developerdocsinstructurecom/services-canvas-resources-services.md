---
title: Services | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/services
source: sitemap
fetched_at: 2026-02-15T09:08:29.334277-03:00
rendered_js: false
word_count: 165
summary: This document provides API documentation for retrieving Kaltura plugin configuration and starting new Kaltura sessions within the Canvas LMS.
tags:
    - canvas-lms
    - kaltura-api
    - video-integration
    - plugin-configuration
    - session-management
    - rest-api
category: api
---

[ServicesApiController#show\_kaltura\_configarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/services_api_controller.rb)

`GET /api/v1/services/kaltura`

**Scope:** `url:GET|/api/v1/services/kaltura`

Return the config information for the Kaltura plugin in json format.

**API response field:**

Enabled state of the Kaltura plugin

Main domain of the Kaltura instance (This is the URL where the Kaltura API resides)

Kaltura URL for grabbing thumbnails and other resources

Hostname to be used for RTMP recording

Partner ID used for communicating with the Kaltura instance

**Example Response:**

```
# ForanenabledKalturaplugin:
{
'domain': 'kaltura.example.com',
'enabled': true,
'partner_id': '123456',
'resource_domain': 'cdn.kaltura.example.com',
'rtmp_domain': 'rtmp.example.com'
}
# ForadisabledorunconfiguredKalturaplugin:
{
'enabled': false
}
```

[ServicesApiController#start\_kaltura\_sessionarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/services_api_controller.rb)

`POST /api/v1/services/kaltura_session`

**Scope:** `url:POST|/api/v1/services/kaltura_session`

Start a new Kaltura session, so that new media can be recorded and uploaded to this Canvas instance’s Kaltura instance.

**API response field:**

The kaltura session id, for use in the kaltura v3 API. This can be used in the uploadtoken service, for instance, to upload a new media file into kaltura.

**Example Response:**

```
{
'ks': '1e39ad505f30c4fa1af5752b51bd69fe'
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).