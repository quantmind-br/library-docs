---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateSurveyQuestion
source: crawler
fetched_at: 2026-02-27T23:40:41.478619-03:00
rendered_js: true
word_count: 69
summary: This document provides the technical specification for updating the text of a survey question within an advertising experiment using the Ads API. It details the required identifiers for accounts, experiments, and questions, along with a sample PATCH request.
tags:
    - ads-api
    - survey-questions
    - experiments
    - api-reference
    - patch-request
    - ad-accounts
category: api
---

Ads API •References / experiments / Update survey question.

## Update survey question.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- experiment\_idstring \[uuid]
  
  A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- survey\_question\_idstring \[uuid]
  
  The unique identifier for the survey question.
  
  Example: `f47ac10b-58cc-4372-a567-0e02b2c3d479`

Request model for updating a survey question.

- The survey question text.
  
  Example: `"Which of the following..."`

## Response

Successfully updated the survey question.

```
curl --request PATCH \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/experiments/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/questions/f47ac10b-58cc-4372-a567-0e02b2c3d479 \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "question_text": "Which of the following..."
}'
```

* * *

## Response sample

```
empty response
```