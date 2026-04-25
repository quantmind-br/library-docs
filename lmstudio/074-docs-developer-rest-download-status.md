---
title: Get download status
url: https://lmstudio.ai/docs/developer/rest/download-status
source: sitemap
fetched_at: 2026-04-07T21:30:29.440009337-03:00
rendered_js: false
word_count: 146
summary: This document details the structure and parameters for a GET request endpoint used to check the current status of a background download job.
tags:
    - api-endpoint
    - download-status
    - rest-api
    - job-tracking
category: reference
---

`GET /api/v1/models/download/status/:job_id`

**Path parameters**

job\_id : string

The unique identifier of the download job. `job_id` is returned by the [download](https://lmstudio.ai/docs/developer/rest/download) endpoint when a download is initiated.

**Response fields**

Returns a single download job status object. The response varies based on the download status.

job\_id : string

Unique identifier for the download job.

status : "downloading" | "paused" | "completed" | "failed"

Current status of the download.

bytes\_per\_second (optional) : number

Current download speed in bytes per second. Present when `status` is `downloading`.

estimated\_completion (optional) : string

Estimated completion time in ISO 8601 format. Present when `status` is `downloading`.

completed\_at (optional) : string

Download completion time in ISO 8601 format. Present when `status` is `completed`.

total\_size\_bytes (optional) : number

Total size of the download in bytes.

downloaded\_bytes (optional) : number

Number of bytes downloaded so far.

started\_at (optional) : string

Download start time in ISO 8601 format.