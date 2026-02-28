---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAsyncReport
source: crawler
fetched_at: 2026-02-27T23:40:08.280075-03:00
rendered_js: true
word_count: 120
summary: This document describes an API endpoint for retrieving the processing status and download URL of a previously requested asynchronous CSV report.
tags:
    - ads-api
    - csv-reports
    - async-reporting
    - report-status
    - spotify-ads
category: api
---

Ads API •References / reports / Get CSV Report Status by ID

## Get CSV Report Status by ID

Returns the status of a CSV report and its download URL (once available). The `report_id` can be found in the response from calling the Create Async Report endpoint.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for a report ID.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

The status of a CSV report and its download URL (once available).

- The status that represents the state of the report.
  
  Allowed values: `"PROCESSING"`, `"READY"`, `"EXPIRED"`, `"FAILED"`Example: `"READY"`
- submitted\_atstring \[date-time]
  
  Time is in ISO 8601 format.
  
  Example: `"2021-01-23T04:56:07Z"`
- completed\_atstring \[date-time]
  
  Time is in ISO 8601 format.
  
  Example: `"2021-01-23T04:57:07Z"`
- Example: `"https://storage.googleapis.com/ads-selfserve-reports-export/11f57421-1234-5678-a203-6cd9695987e2/e8da1819-38ab-9876-5432-682fccd08700/Report_12345.csv"`

```
curl --request GET \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/async_reports/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"status": "READY","submitted_at": "2021-01-23T04:56:07Z","completed_at": "2021-01-23T04:57:07Z","report_url": "https://storage.googleapis.com/ads-selfserve-reports-export/11f57421-1234-5678-a203-6cd9695987e2/e8da1819-38ab-9876-5432-682fccd08700/Report_12345.csv"}
```