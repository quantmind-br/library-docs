---
title: ePortfolios | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/e_portfolios
source: sitemap
fetched_at: 2026-02-15T09:07:24.813465-03:00
rendered_js: false
word_count: 230
summary: This document defines the schema for ePortfolio objects and outlines API endpoints for managing, retrieving, and moderating user ePortfolios and their associated pages.
tags:
    - canvas-lms
    - eportfolios
    - api-endpoints
    - content-moderation
    - user-data
    - rest-api
category: api
---

**An ePortfolio object looks like:**

```
{
  // The database ID of the ePortfolio
"id": 1,
  // The user ID to which the ePortfolio belongs
"user_id": 1,
  // The name of the ePortfolio
"name": "My Academic Journey",
  // Whether or not the ePortfolio is visible without authentication
"public": true,
  // The creation timestamp for the ePortfolio
"created_at": "2021-09-20T18:59:37Z",
  // The timestamp of the last time any of the ePortfolio attributes changed
"updated_at": "2021-09-20T18:59:37Z",
  // The state of the ePortfolio. Either 'active' or 'deleted'
"workflow_state": "active",
  // The timestamp when the ePortfolio was deleted, or else null
"deleted_at": "2021-09-20T18:59:37Z",
  // A flag indicating whether the ePortfolio has been
  // flagged or moderated as spam. One of 'flagged_as_possible_spam',
  // 'marked_as_safe', 'marked_as_spam', or null
"spam_status": null
}
```

**An ePortfolioPage object looks like:**

```
{
  // The database ID of the ePortfolio
  "id": 1,
  // The ePortfolio ID to which the entry belongs
  "eportfolio_id": 1,
  // The positional order of the entry in the list
  "position": 1,
  // The name of the ePortfolio
  "name": "My Academic Journey",
  // The user entered content of the entry
  "content": "A long time ago...",
  // The creation timestamp for the ePortfolio
  "created_at": "2021-09-20T18:59:37Z",
  // The timestamp of the last time any of the ePortfolio attributes changed
  "updated_at": "2021-09-20T18:59:37Z"
}
```

[EportfoliosApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

`GET /api/v1/users/:user_id/eportfolios`

**Scope:** `url:GET|/api/v1/users/:user_id/eportfolios`

Get a list of all ePortfolios for the specified user.

**Request Parameters:**

- deleted
  
  Include deleted ePortfolios. Only available to admins who can

moderate\_user\_content.

Allowed values: `deleted`

Returns a list of [ePortfolio](https://developerdocs.instructure.com/services/canvas/resources/e_portfolios#eportfolio) objects.

[EportfoliosApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

`GET /api/v1/eportfolios/:id`

**Scope:** `url:GET|/api/v1/eportfolios/:id`

Get details for a single ePortfolio.

Returns an [ePortfolio](https://developerdocs.instructure.com/services/canvas/resources/e_portfolios#eportfolio) object.

[EportfoliosApiController#deletearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

`DELETE /api/v1/eportfolios/:id`

**Scope:** `url:DELETE|/api/v1/eportfolios/:id`

Mark an ePortfolio as deleted.

Returns an [ePortfolio](https://developerdocs.instructure.com/services/canvas/resources/e_portfolios#eportfolio) object.

[EportfoliosApiController#pagesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

`GET /api/v1/eportfolios/:eportfolio_id/pages`

**Scope:** `url:GET|/api/v1/eportfolios/:eportfolio_id/pages`

Get details for the pages of an ePortfolio

Returns a list of [ePortfolioPage](https://developerdocs.instructure.com/services/canvas/resources/e_portfolios#eportfoliopage) objects.

[EportfoliosApiController#moderatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

`PUT /api/v1/eportfolios/:eportfolio_id/moderate`

**Scope:** `url:PUT|/api/v1/eportfolios/:eportfolio_id/moderate`

Update the spam\_status of an eportfolio. Only available to admins who can moderate\_user\_content.

**Request Parameters:**

The spam status for the ePortfolio

Allowed values: `marked_as_spam`, `marked_as_safe`

Returns an [ePortfolio](https://developerdocs.instructure.com/services/canvas/resources/e_portfolios#eportfolio) object.

[EportfoliosApiController#moderate\_allarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

`PUT /api/v1/users/:user_id/eportfolios`

**Scope:** `url:PUT|/api/v1/users/:user_id/eportfolios`

Update the spam\_status for all active eportfolios of a user. Only available to admins who can moderate\_user\_content.

**Request Parameters:**

The spam status for all the ePortfolios

Allowed values: `marked_as_spam`, `marked_as_safe`

[EportfoliosApiController#restorearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

`PUT /api/v1/eportfolios/:eportfolio_id/restore`

**Scope:** `url:PUT|/api/v1/eportfolios/:eportfolio_id/restore`

Restore an ePortfolio back to active that was previously deleted. Only available to admins who can moderate\_user\_content.

Returns an [ePortfolio](https://developerdocs.instructure.com/services/canvas/resources/e_portfolios#eportfolio) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).