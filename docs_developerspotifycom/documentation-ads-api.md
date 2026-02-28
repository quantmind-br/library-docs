---
title: Ads API | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api
source: crawler
fetched_at: 2026-02-27T23:38:06.502272-03:00
rendered_js: true
word_count: 7284
summary: This document introduces the Spotify Ads API, outlining its core design principles, rate limiting policies, versioning strategy, and the criteria for breaking versus non-breaking changes.
tags:
    - spotify-ads-api
    - api-design
    - rate-limiting
    - versioning
    - api-lifecycle
    - breaking-changes
category: concept
---

## About

The Spotify Ads API lets you build, manage, and report on [Ads Manager](https://adsmanager.spotify.com) campaigns. This guide can help you get started. Topics include:

- Getting started requirements and instructions
- An Ads Manager overview
- Descriptions of available endpoints
- Help and support information

### Next steps

If you're not sure what to do now, try these recommendations:

- New to the Ads API? See the [Quickstart](https://developer.spotify.com/documentation/ads-api/quick-start) section. It provides instructions about how to set up an account to work with our API.
- Already using the Ads API? Great! Check the [Release Notes section](https://developer.spotify.com/documentation/ads-api#release-notes) for information on the latest changes, or browse the available methods below.

### Support

To report a bug or ask questions about this service, contact the Ads API team at [ads-api-support@spotify.com](mailto:ads-api-support@spotify.com). NOTE: Please be sure to include info such as your client ID and a copy of the request and response (including the sp\_trace\_id) if relevant.

### Subscribe to Newsletter

Sign up for our monthly Ads API newsletter [here](http://eepurl.com/h-NAHz) if you want to receive updates about new releases, testing opportunities, and more!

## API Design

This section covers important design elements that affect how the Ads API works. Take a moment to review this information.

### Rate Limiting

Rate limiting caps the number of API calls a user or app can make within a set period of time. The Ads API applies RPS rate limits on a per-user basis for each calling app, regardless of the number of simultaneous app users. These limits help Spotify provide API access equitably to all our engineering partners.

In addition, there is also a cap on the reporting endpoints that takes precedence over the general cap on the client ID + user ID key since these specific endpoints are most at risk for high-request volumes, oftentimes due to bad or malformed requests.

Note: If our API returns status code 429, it means that you have sent too many requests. When this happens, check the headers for the following info:

- `X-RateLimit-Remaining`: The count of requests remaining in the rate limit window
- `X-RateLimit-Limit`: The maximum number of requests allowed within the rate limit window
- `X-RateLimit-Reset`: The number of seconds left until the rate limit resets and you can retry your request again

Rate Limit OnRate Limit RequestWindow (seconds)Sustained Requests per second (RPS) limitClient ID + User ID (as a single key)150030s50 RPSClient ID + User ID (as a single key) on Reporting Endpoints15030s50 RPS

### Breaking v. Non-Breaking Changes Policy

This section provides a more detailed list of what Ads API considers to be a "Breaking" change, and what is considered a "Non-Breaking" change (i.e. backwards compatible change). The API defines these terms in the following way:

1. **Breaking Changes**: Any alteration in the API that causes existing integrations to fail or function incorrectly from the perspective of the Ads API customers / users. Integrations built on the previous version of the API would not continue to function as expected after these changes are implemented, and would thus require immediate attention and modification.
2. **Non-Breaking/Backwards Compatible Changes**: Updates or enhancements to the API that do not disrupt existing integrations. Integrations built on the previous version of the API continue to function as expected, even after these changes are implemented.

#### Breaking Changes

- Removing an existing operation/endpoint
- **Request**
  
  - Headers
    
    - Removing or renaming an existing header
    - Adding a new required header
    - Making a previously optional header required
    - Changing the type of a header
    - Changing the default value of a header
  - Body
    
    - Removing or renaming an existing field
    - Adding or increasing restrictions to the accepted values for an existing non-enum field
    - Removing enum options from an existing enum-type field
    - Adding a new required request field
    - Making a previously optional request field required
    - Changing the type of an existing request field
    - Changing the default value of an existing field
  - Query/Path Parameters
    
    - Removing or renaming an existing parameter
    - Adding or increasing restrictions to the accepted values for an existing non-enum parameter
    - Removing enum options from an existing enum-type parameter
    - Adding a new required parameter
    - Making a previously optional parameter required
    - Changing the type of an existing parameter
    - Changing the default value of a parameter
- **Response**
  
  - Body
    
    - Removing or renaming an existing field
    - Removing enum values/options from an existing enum-type field
    - Changing the type of an existing field
- Adding a new validation rule to an existing parameter or making an existing validation rule more restrictive
- Changing the value of what is being returned behind the scenes
- Changing authentication or authorization requirements

#### Non-Breaking/Backwards Compatible Changes

- Updating documentation, both internally and externally facing
- Adding a new operation/endpoint
- **Request**
  
  - Headers
    
    - Adding a new optional header
    - Making a previously required header optional
  - Request Body
    
    - Adding a new optional field
    - Making a previously required field optional
    - Adding enum values to an existing enum type field
    - Marking an existing field as deprecated to warn of future remove, but not removing it
  - Query/Path Parameters
    
    - Adding a new optional parameter
    - Making a previously required parameter optional
    - Adding enum values to an existing enum type parameter
    - Marking an existing parameter as deprecated to warn of future remove, but not removing it
- **Response**
  
  - Headers
    
    - Adding a new header
  - Body
    
    - Adding a new field
    - Changing the order of properties in existing API responses
    - Adding enum values to an existing enum type field
    - Marking an existing field as deprecated to warn of future remove, but not removing it
- Any bug fixes that don’t fall into the breaking changes category
- Codebase improvements that don't fall into the breaking changes category (e.g. Testing Improvements, Performance Improvements, etc.)
- Marking an existing endpoint as deprecated to warn of future remove, but not removing it

### Versioning

The most recent version of the Ads API is v3.

All endpoints are versioned with a version number in the URI. Version numbers are integers and the version number is a prefix of the URI.

In accordance with semantic versioning, versions are bumped when there is a backwards-incompatible change that necessitates it, such as significant schema changes.

Updates that do not break existing consumers will be deployed to the current version as patch releases.

*Patch* releases:

- Non-Breaking Changes

*Major* releases, e.g. `/v3/` to `/v4/`:

- Major Breaking/Backwards Compatible Changes

For each of these releases, the API team will communicate with clients and detail the changes in the API Release Notes.

### Release Calendar

In order to maintain a healthy evolution of fixes and improvements to the API, in January 2024 the Ads API began to follow a lifecycle of sunsetting its currently latest version approximately every year. From v2 onwards, the API team will maintain 3 versions (e.g., v2, v3, and v4 will be maintained at the same time). Within about 12 months, the current version is considered deprecated. Deprecation means that a newer version is now available and the flagged version will soon be sunset. After another 6 months, the version is sunset and will no longer be accessible.

For example, the current latest version (v3) of the API will be deprecated ~12 months from January 2025 in Q1 2026 then sunset ~Q3 2026:

!["Ads API Version Lifecycle"](https://developer-assets.spotifycdn.com/images/blog/ads-api-release-calendar.png)

To summarize the release policy:

- **Deprecations**: The existing version is typically deprecated when a new version is released. Once deprecated, new features will not be added to the version, and non-critical bugs will not be resolved. In rare exceptions, critical bug fixes will still be made to the version until it's sunset.
- **Sunset**: The Ads API team will give a **6 month notice** before a version becomes sunset, meaning HTTP requests can no longer be made.
- **Release Notes**: The Ads API team will continue to post monthly updates (see more in the Release Notes section).
- **Monthly Newsletter**: The newsletter includes a summarized version of the release notes (see more in the Monthly Newsletter section).

### Past Versions

For historical reasons, here's a table of previous API versions:

API VersionRelease DateDeprecation DateSunset Datev3January 2025TBATBAv2August 2023January 21, 2025August 5, 2025v1.4November 2022November 13, 2023November 27, 2023v1.3July 2022November 13, 2023November 27, 2023v1.2December 2021August 25, 2022November 27, 2023v1.1June 2019August 25, 2022November 27, 2023v1.0March 2019July 1, 2022November 27, 2023

### Time Format

Times are always recorded in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format as [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/UTC_offset) with a [zero offset](https://en.wikipedia.org/wiki/UTC_offset): `YYYY-MM-DDTHH:MM:SSZ`.

Most list endpoints support paging the dataset by taking an offset and limit as query parameters.

- `limit` specifies the number of results to be returned from the call. If not specified, the default value is 50. The max allowed value is also 50.
- `offset` specifies the starting position of the first result.

If you specify a `limit` of 5, the API will return 5 results. On the next page you’d put an offset of 6 to retrieve results 6 through 10. We return the total number of results along with the page size in the `paging` object.

The [reporting endpoints](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAggregateReport) are an exception and use continuation tokens for paging instead of `offset`. The reporting response will include a continuation token that can then be sent in a subsequent reporting request to access the next page of results. When sending a request with a continuation token included, no other fields should be specified. If the continuation token returned in the response is null, that means there are no more pages available.

Continuation tokens are base64 encoded and encrypted strings that look like the following: `AMC-fuxpGRIqFcOUEzDEdWQsM5Iy7mkRThKFo94mEys6RF1lzeKyq1sOlWU4RsdjSsgDWR2D7An1nFgLXNBU9hocKnWQ9jRsps6kCLqKd7Q77zNEhHm_Xlb6J_Fci6kK7tXVM3U6H8OajjcTA18eFcr-kv0etZJZBWlMhtP84xj4WiVDZnPWaMo7AL3jRrHH32grJ3eRA2PAoZmhg80%3D`

## Release Notes

This section documents changes to the Ads API, including all patch updates, bug fixes, new version releases, version deprecations, version sunsets, etc.

### September 2025

The following updates have been made to the latest version (v3 ) of the Ads API.

#### What’s New

- Campaign Management
  
  - New Web Traffic & App Install campaign objectives available!
    
    - Web Traffic: The Website traffic objective enables advertisers with the Spotify Pixel installed to go beyond clicks and optimize their campaign towards people most likely to view their website
      
      - New enum value `WEB_TRAFFIC` now available under the `objective` field when [creating a campaign](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCampaign)
    - App Installs: The app installs objective enables advertisers to show ads to people likely to click and download their app (NOTE: Advertisers will need to have an existing integration with an MMP – currently, Kochava and Appsflyer are accepted mobile measurement partners)
      
      - New enum value `APP_INSTALLS` now available under the `objective` field when [creating a campaign](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCampaign)
      - New field `mobile_app_id` is now available when [creating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet) – this is required when using the `APP_INSTALLS` campaign objective
  - Introducing support for Cost Per Result bid strategy: This new bid strategy lets you set a target cost per click (CPC) when using the Clicks campaign objective. Spotify’s ad server will then work to reach people more likely to click on your ad, staying at or near your target CPC.
    
    - New enum value `COST_PER_RESULT` is now available under the `bid_strategy` field when [creating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet)
    - Currently this is only compatible with the `CLICKS` campaign objective – when used with the `CLICKS` campaign objective, `bid_micro_amount` will behave as a target cost per click amount
- Measurement
  
  - Ability to set up conversion measurement for an ad set via new optional field `dataset_id` when [creating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet)
  - New endpoints to manage pixels:
    
    - [Get Pixels by Business ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getPixelsByBusinessId)
    - [Create Pixel](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createPixelInBusiness)
    - [Get Pixel by ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getPixelById)
    - [Update Pixel](https://developer.spotify.com/documentation/ads-api/reference/v3.0/updatePixelById)
  - New endpoints to manage mobile apps:
    
    - [Get Mobile Apps by Business ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getMobileAppsByBusinessId)
    - [Create Mobile App](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createMobileAppInBusiness)
    - [Get Mobile App by ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getMobileAppByBusinessAndId)
    - [Update Mobile App](https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateMobileAppByBusinessAndId)
    - [Get Mobile Apps by Ad Account ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getMobileAppsByBusinessIdAndAdAccountId)
    - [Share Mobile App with Ad Account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/shareBusinessMobileAppWithAdAccount)
    - [Unshare Mobile App with Ad Account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/unshareBusinessMobileAppWithAdAccount)
  - New endpoints to manage measurement datasets:
    
    - [Get Datasets by Business ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getDatasetsByBusinessId)
    - [Create Dataset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createDataset)
    - [Get Dataset by ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getDatasetById)
    - [Update Dataset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateDatasetById)
    - [Remove Integration from Dataset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/removeIntegrationFromDataset)
    - [Get Datasets by Ad Account ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getDatasetsByAdAccountId)
    - [Get Diagnostics for Dataset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getDiagnosticsByDatasetId)
    - [Share Dataset with Ad Account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/shareBusinessDatasetWithAdAccount)
    - [Unshare Dataset with Ad Account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/unshareBusinessDatasetWithAdAccount)
  - New endpoints to manage Conversion API (“CAPI”) integrations:
    
    - [Get CAPI Integration by Business ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiIntegrationsByBusinessId)
    - [Create CAPI Integration](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCapiIntegration)
    - [Get CAPI Integration by ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiIntegrationById)
    - [Update CAPI Integration](https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateCapiIntegrationById)
    - [Get CAPI Auth Token](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiAuthTokens)
    - [Create CAPI Auth Token](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCapiAuthToken)
    - [Delete CAPI Auth Token](https://developer.spotify.com/documentation/ads-api/reference/v3.0/deleteCapiAuthToken)

#### Other Non-Breaking Changes

- Campaign Management
  
  - New read-only fields are now available on the ad set entity to more clearly reflect when an ad set is paused to due the ad account status –
    
    - `is_paused`: Derived boolean field indicating if the ad set is currently paused. Returns true if either the user has manually paused the ad set (delivery: OFF) or if the ad account is greylisted/suspended, causing the ad set to be force-paused.
    - `pause_reason`: Indicates the reason why the ad set is paused, if applicable. Only present when is\_paused is true. Allowed enum values --
      
      - `USER_PAUSED`
      - `ACCOUNT_GREYLISTED`
      - `ACCOUNT_SUSPENDED`
  - New `key` value now available under the `call_to_action` object when [creating an ad](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAd): `ORDER_NOW`
  - Option to filter by campaign `statuses` is now available on the [Get Campaigns by Ad Account ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCampaigns) endpoint
- Estimates
  
  - [Estimate Audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateAudience) endpoint now returns an estimated CPM range to improve cost transparency for advertisers using the Maximum Bid strategy: New fields `estimated_cpm_min` and `estimated_cpm_max` are now included in the response body for this endpoint
    
    - Estimated CPM range will not be available for the Cost per result bid strategy
- Ad Accounts
  
  - New enum values available under the `industry` field when [creating an ad account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdAccountForBusiness):
    
    - `AGENCY`
    - `AUTO`
    - `BUSINESS_SERVICES_INDUSTRIALS`
    - `FINANCE`
    - `FOOD_DINING_SERVICES`
    - `GAMING`
    - `HEALTH_WELLNESS`
    - `JOBS_EDUCATION`
    - `LAW_GOVERNMENT_POLITICAL_NON_PROFIT`
    - `OTHER`
    - `RETAIL`
    - `TELECOM`
    - `TRAVEL_TOURISM`

#### Breaking Changes/Deprecations

- v2 of the Ads API was sunset on August 5, 2025 – the v2 endpoints are no longer available and any partners that have yet to migrate to v3 should do so as soon as possible
- Deprecated fields (to be removed in the next version release):
  
  - `category` on the ad set entity

### July 2025

#### ANNOUNCEMENT: v2 Sunset Deadline Extended

**v2 of the Ads API will now be sunset on August 5, 2025.** All partners are required to update their integration to v3 by this date in order to avoid disruption to their integrations.

#### What’s New

- Introducing new custom and lookalike audience capabilities!
  
  - New endpoints under “Audiences”:
    
    - [Get Audiences by Ad Account ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/batchGetAudiences)
    - [Create an Audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAudience)
    - [Get an Audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAudience)
    - [Delete an Audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/deleteAudience)
    - [Edit an Audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/editAudience)
    - [Get Signed GCS upload URL to upload a user list file](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createUploadUrl)
    - [Get Signed GCS upload URL to upload a user list file for an existing audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/replaceUploadUrl)
  - New fields `audience_ids` and `audience_ids_exclusions` are now available under `targets` object when [creating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet)
- New display format is now available – to create a display ad:
  
  - When [creating the ad set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet), set `asset_format` to `IMAGE`
  - When [creating the ad](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAd), specify an image asset under `asset_id`

#### Other Non-Breaking Changes

- Ad Accounts
  
  - New optional field `website` is available when [creating an ad account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdAccountForBusiness)
  - New read-only fields on the [ad account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAdAccount) entity:
    
    - `legal_entity_name`
    - `status`
    - `status_reason`
    - `currency_code`
- Ad Sets
  
  - Update to the default behavior for platform targeting: If no platform targeting is passed, `["ANDROID", "DESKTOP", "IOS"]` will now be targeted by default (previously this would default to an empty value)
- Ads
  
  - Support for new call-to-action language options when [creating an ad](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAd):
    
    - `DANISH`
    - `DUTCH`
    - `FINNISH`
    - `NORWEGIAN`
    - `SWEDISH`
    - `JAPANESE`
- Assets
  
  - Support for filtering by asset IDs under [Get Assets](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAssetsByAdAccount) via new optional filter asset\_ids
- Reports
  
  - New reporting field `STREAMED_IMPRESSIONS` now available under the reporting endpoints

#### Breaking Changes/Deprecations

- v2 of the Ads API will be sunset on August 5, 2025. All partners are required to update their integration to v3 by this date in order to avoid disruption to their integrations.

### January 2025

All of the following updates are included under a new major version (v3) released on January 21, 2025.

#### v2 Deprecation Timeline

**v2 of the Ads API will be deprecated on July 22, 2025.** All partners are required to update their integration to v3 by this date in order to avoid disruption to their integrations.

#### What’s New

- Introducing business and ad account management capabilities!
  
  - New endpoints under “Businesses”:
    
    - [Get Businesses for Current User](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getBusinesses)
    - [Get Business by ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getBusiness)
    - [Create Business](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createBusiness)
    - [Update Business](https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateBusiness)
  - New endpoints under “Ad Accounts”:
    
    - [Create Ad Account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdAccountForBusiness)
    - [Update Ad Account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateAdAccount)
    - [Get Ad Accounts for Current User by Business ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAdAccountsInBusiness)
      
      - \[Breaking Change] This endpoint is intended to replace the v2 [Get Ad Accounts for Current User](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAdAccounts) endpoint, which has been deprecated and removed
  - Changes under ad account entity:
    
    - New field `business_id`
    - New field `legal_entity_name`
    - \[Breaking change] `display_name` is now nested under `billing_address` object and renamed to `name`
    - \[Breaking change] `statusReason` renamed to `status_reason`
    - \[Breaking] `address` renamed to `billing_address`
- Support for video views and podcast streams campaign objectives
  
  - New enum values available for objective under the [Campaign](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCampaign) entity: `VIDEO_VIEWS` and `PODCAST_STREAMS`
  - Also added to the [Estimate Audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateAudience) and [Estimate Bid](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateBid) endpoints
- Support for new opt-in video format
  
  - New optional field in [Create Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet), [Estimate Audience](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateAudience), and [Estimate Bid](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateBid) endpoints: `video_delivery_formats`
    
    - This field is only applicable for video ad sets. It specifies the allowed delivery formats of the ad set, which define how the ads within them will be shown to users.
    - Allowed values:
      
      - `IN_STREAM`
      - `OPT_IN`
      - For video views campaigns, the only allowed value (and default value) is `OPT_IN`
      - For clicks campaigns, the only allowed value (and default value) is `IN_STREAM`
      - For all other campaigns with video ad sets, the default is both `OPT_IN` and `IN_STREAM`
- Expanded support for third-party tracking tags: New enum value `UNSET` supported for the `measurement_partner` field under the `third_party_tracking` object on the [Ad](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAd) entity – `UNSET` should be used for any partners aside from DCM or IAS

#### Other Non-Breaking Changes

- Campaigns
  
  - New filters under [Get Campaigns by Ad Account ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCampaigns):
    
    - `name`
    - `ad_set_statuses`
- Ad Sets
  
  - New filters under [Get Ad Sets by Ad Account ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAdSetsByAdAccountId):
    
    - `name`
    - `statuses`
- Ads
  
  - New filters and sort fields under [Get Ads by Ad Account ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAds):
    
    - Filter by:
      
      - `name`
      - `statuses`
      - `asset_ids`
    - Sort by:
    - `name`
    - `status`
    - `budget`
    - `start_date_time`
    - `end_date_time`
  - Added new field `key` to the `call_to_action` object in the response body which represents the un-localized CTA key (the localized equivalent is still returned via the existing `text` field)
- Assets
  
  - New fields under the Asset entity:
  - `asset_subtypes`
  - `aspect_ratios`
  - New filters and sort fields under [Get Assets by Ad Account](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAssetsByAdAccount):
    
    - Filter by:
      
      - `asset_subtypes`
      - `aspect_ratios`
      - `statuses`
    - Sort by:
      
      - `sort_direction` (allowed values: `ASC`, `DESC`)
      - `sort_field` (allowed values: `CREATED_AT`, `NAME`)
- Reporting
  
  - New async reporting endpoints:
    
    - [Create A CSV Report Asynchronously](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAsyncReport) New metrics supported:
      
      - `MODELED_LEADS`
      - `MODELED_PAGE_VIEWS`
      - `MODELED_PURCHASES`
      - `UNMODELED_ADD_TO_CART`
      - `UNMODELED_LEADS`
      - `UNMODELED_PAGE_VIEWS`
      - `UNMODELED_PURCHASES`
    - [Get CSV Report Status by ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAsyncReport)
  - [Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAggregateReport):
    
    - New metrics supported:
      
      - `UNMUTES`
      - `COMPLETION_RATE`
      - Removed `ACTIVE` from list of filterable ad statuses
- Targets
  
  - [Get Geo Targets](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getGeoTargets)
    
    - `country_code` validation relaxed: Users are no longer required to input a `country_code` when specifying an id or list of ids

#### Breaking Changes/Deprecations

- Ad Sets
  
  - `exclude_placements` has been removed and replaced with new required field `placements` – when calling [Create Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet), users will now specify placements to include (as opposed to exclude)
    
    - Allowed enum values:
      
      - `MUSIC`
      - `PODCAST` (NOTE: only available for certain markets and cannot be specified on its own)
  - `sensitive_topic_exclusion_ids` from under the `targets` objects has been removed – users should instead use `sensitive_topic_exclusions` object to specify sensitive topic exclusion targeting
- Assets
  
  - `assetType` in the [asset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAsset) response body has been reformatted to `asset_type`
  - Data type for `aspect_ratio` in the [asset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAsset) response body is now a string enum (was previously a double) – supported values are:
    
    - `HORIZONTAL_16_9`
    - `HORIZONTAL_1_91_1`
    - `SQUARE`
    - `VERTICAL_9_16`
  - Removal of `imageType` parameter: Users are no longer required to specify `imageType` when [creating](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAsset) an image asset – `imageType` has been removed from the response body
  - In the [Create Asset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAsset) request body, new field called `asset_subtype` field is required for asset type `AUDIO`
    
    - Allowed values:
      
      - `COMPANION`
      - `LOGO`
      - `USER_UPLOADED_IMAGE`
  - Estimates
    
    - `start_date` and `end_date` removed from request body for [Estimate Bid](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateBid)
    - `exclude_placements` has been removed and replaced with new required field `placements` – users will now specify placements to include (as opposed to exclude)
      
      - Allowed enum values:
        
        - `MUSIC`
        - `PODCAST` (NOTE: only available for certain markets and cannot be specified on its own)
- Reports
  
  - [Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAggregateReport) endpoint:
    
    - Change to timestamp behavior for the `report_start` and `report_end` fields: timestamps are now inclusive for the minutes and seconds values (previously in v2, users were instructed to express all timestamps as whole hours, e.g., 2021-01-23T00:00:00Z because the minutes and seconds values were not inclusive, but now in v3 they are inclusive)
    - Added new `warnings` field to the response body: this field will now notify users who specify both a continuation token and query params in the same request that the `continuation_token` will take precedence and the query params will be ignored
  - Removed `limit` and `continuation_token` fields from [Get Insight Report](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAudienceInsightReport) endpoint
- Targets
  
  - Under the [Get Interest Targets](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getInterestTargets) endpoint, the `interests` object has been removed and replaced with `interests_with_subtargets`
    
    - New nested object `subtargets` shows the granular sub-interests that comprise the audience

#### Documentation Updates

- [Object hierarchy](https://developer.spotify.com/documentation/ads-api/guides#object-hierarchy) section under “Guides” now includes reference to the business entity
- Updated [Versioning](https://developer.spotify.com/documentation/ads-api#versioning) & Release Calendar sections to reflect v3 availability
- Updated [Build a Campaign](https://developer.spotify.com/documentation/ads-api/guides#build-a-campaign) guide to reflect v3 updates

### March 2024

The following updates have been made to the latest version (v2) of the Ads API.

#### What's New

- New campaign objective `"PODCAST_STREAMS"` is now available when [creating](https://developer.spotify.com/documentation/ads-api/reference/v2.0/createCampaign) or [updating](https://developer.spotify.com/documentation/ads-api/reference/v2.0/updateCampaign) a campaign: The new Podcast Streams objective enables podcasters of all sizes easily promote their shows to listeners who are more likely to stream podcasts on Spotify -- learn more [here](https://ads.spotify.com/en-US/news-and-insights/podcast-streams-objective/)
- New read-only field `display_name` under the ad account entity: This is an optional nickname that a user can give to an ad account; it is referred to as the ad account nickname in the UI and is specific to a user

#### Documentation Updates

- Update to [Rate Limiting](https://developer.spotify.com/documentation/ads-api#rate-limiting):
  
  - Replaced IP-level rate limit with a user-level rate limit
  - Added info on new rate limiting headers:
    
    - `X-RateLimit-Remaining`: The count of requests remaining in the rate limit window
    - `X-RateLimit-Limit`: The maximum number of requests allowed within the rate limit window
    - `X-RateLimit-Reset`: The number of seconds left until the rate limit resets and you can retry your request again
- Update to [Pagination](https://developer.spotify.com/documentation/ads-api#pagination): Added documentation to reflect that reporting endpoints use `continuation_token` for paging instead of `offset`

### February 2024

The following updates have been made to the latest version (v2) of the Ads API.

#### What's New

- Reporting updates:
  
  - Support for ad account-level breakdowns: a new enum value `"AD_ACCOUNT"` is now available under the `entity_type` parameter for the [Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAggregateReport) endpoint
    
    - Ad account-level breakdowns are not supported for the [Get Insight Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAudienceInsightReport) endpoint
    - The following fields/filters **cannot** be used when requesting an ad account-level breakdown:
      
      - `entity_id` - the ID of the ad account specified in the endpoint path will be used to filter the request
      - `entity_id_type`
      - `include_parent_entity`- cannot be set to `true`
      - `statuses`
      - `entity_status_type`
- Campaign Management updates:
  
  - New [Canvas](https://ads.spotify.com/en-US/news-and-insights/introducing-canvas-for-ads/) feature available! When creating or updating an audio ad, users now have the option to include a visual companion asset (an image or a video) that will play on a loop in full-screen when listeners are in-focus
    
    - To use Canvas via the Ads API: When sending a request to the [Create](https://developer.spotify.com/documentation/ads-api/reference/v2.0/createAd) or [Update](https://developer.spotify.com/documentation/ads-api/reference/v2.0/updateAd) Ad endpoints, specify an image or video asset ID under the optional field `canvas_asset_id` (nested under the `assets` object)
    - This feature is only available for ads created under ad sets where the `format` is `"AUDIO"` (not available for `"VIDEO"`)
  - Relaxation of ad set start/end date validation logic: The validation logic under the [Update Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v2.0/updateAdSet) endpoint has been relaxed so that users may now shorten the schedule of an ad set (previously it could only be extended)
  - Relaxation of requirements when creating or updating an image asset: If a user calls the [Create](https://developer.spotify.com/documentation/ads-api/reference/v2.0/createAsset) or [Update](https://developer.spotify.com/documentation/ads-api/reference/v2.0/updateAsset) Asset endpoints and specifies the `asset_type` as `"IMAGE"`, they are no longer required to specify `asset_subtype` as well
    
    - Previously, users were required to specify `asset_subtype` as either `"LOGO"` or `"COMPANION"` when creating an image asset, but now `asset_subtype` will automatically default to `"USER_UPLOADED_IMAGE"` for all image assets and is not required in the request to create an image asset
    - Requests that continue to specify `"LOGO"` or `"COMPANION"` under the `asset_subtype` field will continue to work, but these values will be automatically overriden with `"USER_UPLOADED_IMAGE"`

### January 2024

The following updates have been made to the latest version (v2) of the Ads API.

#### What's New

- Reporting updates:
  
  - New metrics `VIDEO_EXPANDS` and `VIDEO_EXPAND_RATE` available under the [Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAggregateReport) endpoint for campaigns using the Video Views objective
- Campaign Management updates:
  
  - New call-to-action text enum value`"WATCH NOW"` is now available under the [Ad](https://developer.spotify.com/documentation/ads-api/reference/v2.0/createAd) entity
  - Support for bulk postal code upload: Users can now search for up to 1000 postal codes via the `ids` field under [Get Geo Targets](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getGeoTargets) (previously this was limited to 50 postal codes)

#### Documentation Updates

- Updates to our [Versioning](https://developer.spotify.com/documentation/ads-api#versioning) policy:
  
  - Added new release calendar to provide context on our release cadence
  - Removed reference to minor versions -- all new version releases will be released as new major versions moving forward

### December 2023

The following updates have been made to the latest version (v2) of the Ads API.

#### What's New

- Update to [Create Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v2.0/createAdSet) endpoint: New optional parameter `pacing` has been added with the following allowed values – these are immutable after ad set creation:
  
  - `PACING_ASAP`: Deliver ads at an accelerated pace. Delivery stops when daily or lifetime budget is spent
  - `PACING_EVEN`: Deliver ads throughout your selected schedule at a standard pace.
- Update to [Create Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v2.0/createAdSet), [Update Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v2.0/updateAdSet), [Estimate Bid](https://developer.spotify.com/documentation/ads-api/reference/v2.0/estimateBid), and [Estimate Audience](https://developer.spotify.com/documentation/ads-api/reference/v2.0/estimateAudience) endpoints:
  
  - The max allowed targeted age has been increased to 99 (was previously 65)
  - The parameter `sensitive_topic_exclusion_ids` under the `targets` object has been marked as deprecated in v2 and will be sunset in the next version bump (timing TBD) – it is being replaced with new optional parameter `sensitive_topic_exclusions` which allows users to specify separate filter levels for individual sensitive topic ids, or a single global filter to be applied to all sensitive topics
    
    - Allowed values for the new `filter_option` parameter (nested under `sensitive_topic_exclusions`):
      
      - `STANDARD` (default): Provides the full breadth of podcasts eligible for ads.
      - `PARTIAL`: May include audio of “real-world” alcohol/tobacco use, or dramatic depictions or educational coverage of alcohol/tobacco use; may include dramatic and non-graphic depiction, edu-tainment, op-ed coverage, or breaking news of crime/violence or weapons; may include dramatic depictions or discussion of drug use for entertainment or journalistic purposes (including discussion of addiction recovery); may include depictions of recreational gambling or news coverage of gambling legislation; may include dramatic or graphic depictions of hate speech/acts in an entertainment context, or audio of “real-world” hate speech for discussion purposes; may include dramatic and non-graphic depictions of sexual acts in an entertainment context; may include discussion or discussion or references to past terrorist events/groups, without graphic details.
      - `LIMITED`: May include informal mentions of alcohol brands/use, drug use, gambling, smoking/tobacco products, or weapons; as well as educational or informative discussions of criminal reform/past unlawful criminal activity, hate speech/acts, sexual relationships/sexuality or terrorism.
      - `RESTRICTED`: Avoid placements that contain any reference to the sensitive topic(s). Total exclusion of the sensitive topic(s) is not guaranteed.

#### Breaking Changes/Deprecations

- \[Breaking Change] Update to the [Update Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v2.0/updateAdSet) and [Update Campaign](https://developer.spotify.com/documentation/ads-api/reference/v2.0/updateCampaign) endpoints: we’re removing support for archiving ad sets and campaigns – effective December 12th, 2023, the API will return a validation error when users attempt to set the `status` parameter to `ARCHIVED` for an ad set or a campaign
- \[Breaking Change] Update to [Estimate Audience](https://developer.spotify.com/documentation/ads-api/reference/v2.0/estimateAudience) endpoint: the parameter `bid_micro_amount` will be required starting on December 17th, 2023 -- impacted partners have been sent direct communications to update their integrations
- \[Non-Breaking Change, Deprecation] Update to [Estimate Bid](https://developer.spotify.com/documentation/ads-api/reference/v2.0/estimateBid) endpoint: `start_date` and `end_date` have been marked as deprecated and are no longer required – in the next version bump, these parameters removed from under this endpoint
- v1 to v1.4 of the Ads API was sunset on November 27, 2023 – these endpoints are no longer available and any partners that have still yet to migrate to v2 should do so

#### Documentation Updates

- Added a new section on [Breaking v. Non-Breaking Changes Policy](https://developer.spotify.com/documentation/ads-api#breaking-v-non-breaking-changes-policy) to our API Design documentation which provides specific examples of breaking vs non-breaking changes

### November 2023

The following updates have been made to the latest version (v2) of the Ads API.

#### What's New

- Reporting updates:
  
  - Updates to [Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAggregateReport) endpoint:
    
    - We’ve restored support for filtering by multiple `entity_ids` (campaign/ad set/ad IDs) in a single call when requesting daily and hourly granularity
      
      - NOTE: A maximum of 50 `entity_ids` can be included in a single request
    - Users may now filter ads by campaign IDs when requesting lifetime granularity – previously, requests with `entity_type=CAMPAIGN` and `entity_ids_type=AD` would result in a validation error
  - Update to [Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAggregateReport) and [Get Insight Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAudienceInsightReport) endpoints: We’ve removed the validation rule that previously required `report_start` and `report_end` to be in the past – requests where `report_start` and/or `report_end` are in the future will no longer result in a validation error
    
    - This means that users requesting `granularity=DAY` under Get Aggregate Report are now able to request data for the current day by setting `report_end` to tomorrow’s date (e.g., if today is November 14, 2023 in UTC, `report_end` should be set to `2023-11-15T00:00:00Z` to return data up to today)
- The ability to query by IDs has been added to the [Get Podcast Episode Topic Targets](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getEpisodeTopicTargets), [Get Sensitive Topic Targets](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getSensitiveTopicTargets), [Get Genre Targets](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getGenreTargets), Get Playlist Targets, and [Get Podcast Shows](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getPodcastShows)) endpoints
- Update to [Get Geo Targets](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getGeoTargets) endpoint: `country_code` is no longer required when requesting `types=COUNTRY`
  
  - This means that users can now retrieve a list of all allowed country geo targets by requesting `types=COUNTRY` and leaving all other query parameters blank

#### Breaking Changes/Deprecations

- \[ACTION REQUIRED] v1-v1.4 of the Ads API was deprecated on November 13, 2023. All v1-v1.4 endpoints will be sunset on November 27, 2023, at which point calls to v1-v1.4 endpoints will fail. All partners must migrate to v2 by this date in order to avoid disruptions to their integrations.

#### Documentation Updates

- Update to our [Versioning](https://developer.spotify.com/documentation/ads-api#versioning) policy: Effective November 15, 2023, the Ads API team will consider adding new enum fields as a non-breaking change and we expect our consumers to adjust their code to allow for this convention. Previously, we had not defined the expected behavior for this type of change.

### October 2023

The following updates have been made to the latest version (v2) of the Ads API.

#### What's New

- Launch of the new video views campaign objective:
  
  - New value `VIDEO_VIEWS` is now available for the `objective` parameter under the [Create Campaign](https://developer.spotify.com/documentation/ads-api/reference/v2.0/createCampaign) endpoint
  - New field (i.e., metric) called `VIDEO_VIEWS` is now available under the [Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAggregateReport) and [Get Insights Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAudienceInsightReport) endpoints
- Other reporting updates:
  
  - When requesting `entity_type` = `AD_SET` or `AD` and `granularity` = `LIFETIME`, any entity can now be used for filtering (e.g., at lifetime granularity, users can now filter Ads by Campaign IDs whereas previously they were only able to filter Ads by Ad IDs).
    
    - NOTE: If requesting `entity_type` = `CAMPAIGN`, only Campaign IDs can be used for filtering
  - Restored support for requesting `report_start` and `report_end` when requesting `LIFETIME` granularity (NOTE: The date range specified for report start/end must be 90 days or less, as is already the case for `HOUR` and `DAY` granularity requests)
  - Improved 400 error messaging to more clearly explain the underlying issue with the request for several scenarios
- Other campaign management updates:
  
  - Added new parameter `campaign_ids` to Get Ad Sets endpoint to enable filtering by one or more campaign IDs
  - Added new parameter `ad_set_ids` to Get Ads endpoint to enable filtering by one or more ad set IDs
  - Create & Update Ad Set:
    
    - When creating or updating an ad set, the start date must now only be 1 hour in the future (previously we required it to start at least 24 hrs in the future)
    - \[Bug Fix] The minimum allowed lifetime budget is now ~$250 regardless of targeted country; previous issue where an error was sometimes returned when setting a lifetime budget over ~$250 has been resolved
- New endpoints:
  
  - Get Sensitive Topic targets: Retrieve allowed sensitive topic target values, used for excluding sensitive podcast topics from possible ad placements
  - Get Podcast Episode Topic targets: Retrieve allowed podcast episode target values, used for targeting relevant podcast episode topics

#### Breaking Changes/Deprecations

- \[ACTION REQUIRED] Upcoming deprecation deadline: v1 through v1.4 of the Ads API will be deprecated on November 13th, 2023. All partners must migrate to v2 by this date in order to avoid disruptions to their integrations.

#### Documentation Updates

- Added more detailed descriptions to reporting endpoint parameters to clarify expected behavior

### September 2023

The following updates have been made to the latest version (v2) of the Ads API.

#### What's New

- Updates to reporting endpoints ([Get Aggregate Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAggregateReport) & [Get Insights Report](https://developer.spotify.com/documentation/ads-api/reference/v2.0/getAudienceInsightReport)) in effect as of September 7th, 2023:
  
  - Zero-stat campaigns (i.e., campaigns that have not yet been trafficked) are now automatically included in reports
  - Updates to the `SPEND` field:
    
    - `SPEND` is now capped based on billable impressions; this means that any spend tied to delivery over the specified budget is now filtered out in order to match the Ad Studio UI’s logic
    - `SPEND` is now reported in standard units instead of in micro amounts (e.g., 1800 dollars and 31 cents is now reported as `1800.31` instead of `1800310000` as previously)
  - Updates relevant for Get Aggregate Report by Ad Account ID endpoint only:
    
    - The parameters `entity_ids` and `entity_ids_type` are now required when requesting `DAY` or `HOUR` granularity
    - Removed support for filtering by multiple entity IDs when `DAY` or `HOUR` granularity is requested -- these requests must be filtered by a single entity ID
    - When requesting `HOUR` granularity, the API will only return data for the last 14 days
    - When requesting `DAY` granularity:
      
      - The maximum allowed difference between `report_start` and `report_end` is 90 days – there is no limit on how far back in time `report_start` and `report_end` can go though
      - The timestamps for `report_start` and `report_end` must be rounded to the nearest day (e.g., `2023-09-15T00:00:00Z`)

#### Breaking Changes/Deprecations

- \[ACTION REQUIRED] Upcoming deprecation deadline: v1 through v1.4 of the Ads API will be deprecated on November 13th, 2023 and sunset on November 27, 2023. All partners must migrate to v2 by this date in order to avoid disruptions to their integrations.

### August 2023

#### Announcing Ads API v2!

All of the following updates are included under a new major version (v2) released on August 8, 2023.

#### What's Changing

#### General

- The Campaign Management API is now generally available! These endpoints no longer require a manual allowlisting process to access.
- \[Breaking Change] The following entities have been deprecated from the API:
  
  - `advertiser`: All references to advertiser, including advertiser endpoints, have been removed
  - `organization`: All references to organization have been removed
  - `ad_set_links`: All references to ad\_set\_links, including Ad Set Link endpoints, have been removed
- \[Breaking Change] All resource names now follow snake\_case convention (previously in v1, camelCase was used for path resources)
- \[Breaking Change] All `update` requests now use the PATCH method to support partial data updates (previously in v1, PUT was used even though the resource is not fully replaced)

#### Paging

- \[Breaking Change] `page_size` has been renamed to `limit` in all instances (previously in v1, both `page_size` and `limit` were used)
- \[New] `paging` object is now returned if pagination is specified. Example:

`1`

`"paging": {`

`2`

`"page_size": 50,`

`3`

`"total_results": 17,`

`4`

`"offset": 0`

`5`

`}`

#### Ad Accounts

- Endpoint to query a single ad account by ID called `Get an Ad Account` is now available
- Get Ad Accounts endpoint path has been shortened to GET /ad\_accounts (was previously GET /currentUser/adAccounts)
- \[Breaking Change] The following parameters have been deprecated from the ad account entity:
  
  - `organization_id`
  - `ad_studio_lead`
  - `description`
- \[Breaking Change] The following parameters have been renamed under the ad account entity:
  
  - `last_modified` is now `updated_at`
  - `iso_country_code` is now `country_code`

#### Campaigns

- \[New] The following parameters have been added to the campaign entity:
  
  - `updated_at`: When the campaign was last updated (read only)
  - `purchase_order`: Intended for organizational purposes; if specified, it will be displayed on invoices (optional for Create Campaign requests and cannot be updated)
  - `objective`: The objective of the campaign, previously referred to as `bid_optimization_goal` at the ad set level (required for Create Campaign requests and cannot be updated)
- \[Breaking Change] The following parameters have been deprecated from the campaign entity:
  
  - `description`
  - `advertiser_id`
  - `landing_page_domain`
  - `version`
  - `ad_set_ids`
- \[Breaking Change] The following endpoints have been deprecated:
  
  - Update Campaign Status
  - Get Campaigns (users can continue to call Get Campaigns by Ad Account ID and Get Campaigns by ID endpoints to retrieve campaigns)
- \[Breaking Change] The following filters under Get Campaigns by Ad Account ID endpoint have been deprecated:
  
  - `ids` (ability to query by a single campaign ID still supported under Get Campaign by ID endpoint, but querying by an array of IDs is no longer supported)
  - `advertiser_ids`
  - `statuses`
  - `name`
- \[Breaking Change] The following parameters have been renamed under the campaign entity:
  
  - `created_on` is now `created_at`

#### Ad Sets

- \[New] The following parameters have been added to the ad set entity:
  
  - `updated_at`: When the campaign was last updated (read only)
  - \[Breaking Change] `category`: A category that most closely matches the content of the ad(s); certain categories may be subject to restrictions (required for Create Ad Set requests and can be updated)
  - `podcast_episode_topics`: Podcast episode topics to target (optional for Create Ad Set requests and can be updated)
  - `sensitive_topic_exclusions`: Sensitive podcast episode topics to exclude from ad placements (optional for Create Ad Set requests and can be updated)
  - `language`: Languages to target; languages are based on the language users use on Spotify (optional for Create Ad Set requests and cannot be updated)
  - `interests`: Interests to target; interests are based on listening habits and playlist preferences (optional for Create Ad Set requests and can be updated)
  - `exclude_placements`: When targeting a market where podcast ads are supported, placements will automatically default to include both podcast and music; users can set this parameter to `PODCAST` in order to limit their ad placement to music only (optional for Create Ad Set requests and can be updated)
  - `delivery`: Use to pause/resume ad set delivery; if set to `ON`, ad set will be served (once ad review is passed and start date occurs) and if set to `OFF`, ad set will not be served (optional for Create Ad Set requests and can be updated)
- \[Breaking Change] The following parameters have been deprecated from the ad set entity:
  
  - `advertiser_id`
  - `ad_ids` (ability to link an ad to an ad set is still supported at the ad entity level)
  - `active_status`
  - `ad_set_links`
  - `custom_audience_ids`
  - `serving_issues`
  - `version`
- \[Breaking Change] The following parameters have had schema changes or been renamed under the ad set entity:
  
  - `targeting has been renamed to`targets\`
  - `budget` object added to the Create Ad Set request in order to match response schema:
    
    - `budget_micro_amount` in the Create Ad Set request is now nested under the `budget` object and renamed to `micro_amount` (previously `budget_micro_amount` was a root-level parameter)
    - `type` parameter has been added to specify a `DAILY` or `LIFETIME` budget (required for Create Ad Set requests)
    - `country_code` has been renamed to `currency` (read only)
  - Names of the following targeting parameters have been simplified:
    
    - `gender_names` is now `genders`
    - `platform_names` is now `platforms`
  - Geo targeting parameters (`country_code`, `regions`, `dmas`, `cities`, `postal_codes`) are now nested within a new - `geo_targets` object under `targets`
    
    - All geo target IDs are now string data type (previously they were integers \[int32])
  - Metadata (e.g., `name`) is no longer returned with targeting parameters in Get Ad Set by Ad Account ID response – objects have been flattened into arrays where only the target ID(s) are included now
    
    - Metadata is still included in Get Ad Set by Ad Set ID response
  - `artist_promotion` has been renamed to `promotion`
    
    - `name` parameter under `artist_promotion` has been removed
    - `artist_promotion_goal` has been renamed to `promotion_goal`
    - Changes to the following promotion goal enum values:
      
      - `ARTIST_CONTENT` has been removed (artist targeting is now allowed for any ad set)
      - `PODCAST_PROMO` has been added (for promoting a podcast)
    - `artist_promotion_target` object has been removed and replaced with `promotion_target_id` parameter
  - `bid_optimization_goal` has been moved to the campaign entity level and renamed `objective`
  - `format` has been moved out of the `targeting` object and is now a root-level parameter, and has been renamed to - `asset_format`
- \[Breaking Change] The following endpoints have been deprecated:
  
  - Update Ad Set Status (ability to update campaign status has been consolidated into Create and Update Ad Set endpoints in v2)
  - Get Ad Sets (users can continue to call Get Campaigns by Ad Account ID and Get Campaigns by ID endpoints to retrieve campaigns)
  - Get Ad Set Links
  - Get Ad Sets by Campaign
  - Update Ad Set Link Status
  - Get Ad Set Serving Status
- \[Breaking Change] The following filters under Get Ad Sets by Ad Account ID endpoint have been deprecated:
  
  - ids (ability to query by a single ad set ID still supported under Get Ad Set by ID endpoint, but querying by an array of IDs is no longer supported)
    
    - `advertiser_ids`
    - `campaign_ids`
    - `ad_ids`
    - `active_statuses`
    - `statuses`
    - `ad_stauses`
    - `name`
- \[Breaking Change] The following validation logic has been added:
  
  - Minimum budget amount
  - Minimum bid amount

#### Ads

- \[New] The following parameters have been added to the ad entity:
  
  - updated\_at: When the ad was last updated (read only)
  - call to action: The metadata for the behavior of the call-to-action button
    
    - `text`: The text used for the call-to-action button -- currently defaults to `LEARN MORE` but option to configure is coming soon (by end of August 2023)
    - `clickthrough_url`: The link to the ads desired landing page.
    - `language`: The language in which the call-to-action text is presented -- currently defaults to "ENGLISH" but option to configure is coming soon (by end of August 2023)
  - `delivery`: Use to pause/resume ad delivery; if set to `ON`, ad will be served (once ad review is passed and start date occurs) and if set to `OFF`, ad will not be served (optional for Create Ad requests and can be updated)
  - `ad_preview_url`: Link to view a preview of the ad
  - `ad_set_id`: The ID of the ad set to which the ad belongs
  - `logo_image_asset`: Part of `assets` object; logo image for the ad (optional for Create Ad requests and can be updated)
- \[Breaking Change] The following parameters have been deprecated from the ad entity:
  
  - `advertiser_id`
  - `landing_page_domain`
  - `version`
- \[Breaking Change] The following endpoints have been deprecated:
  
  - Get Ads (users can continue to call Get Ads by Ad Account ID and Get Ads by ID endpoints to retrieve campaigns)
- \[Breaking Change] The following parameters have had schema changes or been renamed under the ad entity:
  
  - `created` has been renamed to `created_at`
  - `brand_name` has been renamed to `advertiser_name`
  - `clickthrough_url` is now nested under the `call_to_action` object
  - `assets` object has been simplified to contain the following parameters:
    
    - `asset_id`: ID of an audio or video asset (required on Create Ad requests and can be updated)
    - `companion_asset_id`: ID of a companion image asset (required on Create Ad requests and can be updated)
    - `logo_asset_id`: Nested under `assets` object - ID of a logo image asset (optional on Create Ad requests and can be updated)
  - `third_party_viewability_tracking` has been renamed to `third_party_tracking` and contains the following parameters:
    
    - `measurement_partner`: Name of the third-party measurement partner; `DCM` is now supported along with `IAS`
    - `url`: Third-party tracking URL
- \[Breaking Change] The following filters have been deprecated under Get Ads by Ad Account ID endpoint:
  
  - `ids` (ability to query by a single ad ID still supported under Get Ad by ID endpoint, but querying by an array of IDs is no longer supported)
  - `ad_set_ids`
  - `statuses`
  - `name`

#### Assets

- \[Breaking Change] Get Audio Assets, Get Video Assets, and Get Image Assets endpoints have been deprecated and replaced with a single endpoint called `Get Assets by Asset Type and Ad Account`
- \[Breaking Change] Get Audio Asset, Get Video Asset, and Get Image Asset endpoints have been deprecated and replaced with a single endpoint called `Get Asset`
- \[Breaking Change] Get Fullmix Upload Url, Get Video Upload Url, and Get Image Upload Url endpoints have been deprecated and replaced with a single `Create Asset` endpoint
- \[New] The following endpoints have been added to enable asset upload:
  
  - Upload Asset: Upload image, audio, or video assets that are 25 MB or smaller
  - Start Upload Chunked Asset: Start a chunked upload session for image, audio, or video assets (required for files that are 25 MB or larger)
  - Transfer Chunked Asset: Continues the upload session of a chunked asset by transferring one section of binary media data
  - Complete Upload Chunked Asset: Completes the upload session of a chunked asset
- \[New] Endpoint to update an asset called `Update Asset` is now available

#### Targets

- \[New] Support for the following new targeting types has been added:
  
  - Postal codes: Postal code IDs can be retrieved via Get Geo Targets endpoint and input as an optional parameter in ‘targeting’ under ad sets entities
  - Interests: Interests can be retrieved via new endpoint Get Interest Targets and input as an optional parameter in ‘targeting’ under ad sets entities
  - Languages: Languages can be retrieved via new endpoint Get Language Targets and input as an optional parameter in ‘targeting’ under ad sets entities
  - Podcast episode topics: Only available for markets where podcast ads are supported – podcast episode topics can be retrieved via new endpoint Get Podcast Episode Targets and input as an optional parameter in ‘targeting’ under ad sets entities
  - Podcast sensitive episode topic exclusion: Only available for markets where podcast ads are supported – podcast sensitive episode topics can be retrieved via new endpoint Get Interest Targets and input as an optional parameter in ‘targeting’ under ad sets entities
- \[Breaking Change] Consolidation of previous v1 targeting endpoints:
  
  - Get Artist Targets and Search Artist Targets have been consolidated into a single endpoint Get Artist Targets
  - Get Genre Targets and Search Genre Targets have been consolidated into a single endpoint Get Genre Targets
    
    - Querying by ids is no longer supported
  - Get Playlist Targets and Search Playlist Targets have been consolidated into a single endpoint Get Playlist Targets
    
    - Querying by ids is no longer supported
  - Get Geo Targets and Search Geo Targets have been consolidated into a single endpoint Get Geo Targets
    
    - New parameter `parent_geo_name` added to geo target entity
    - Renamed `id` and `type` parameters to `geo_id` and `geo_type` under geo target entity

#### Reporting

- \[Breaking Change] Create Report and Create Report by Ad Account have been deprecated and replaced with the following endpoints:
  
  - Get Aggregate Report by Ad Account Id: Returns aggregated ad campaign metrics based on requested fields and dimensions
  - Get Insight Report by Ad Account Id: Returns ad campaign metrics broken out by audience insights (e.g., age, gender, genre) based on requested fields – available only as ad set level breakdown at lifetime granularity and does not support report start/end time filtering
- \[Breaking Change] The following `dimensions` values have been deprecated:
  
  - `YEAR`
  - `MONTH`
  - `CURRENCY`
  - `COST_TYPE`
  - `ADVERTISER`
  - `DMA`
  - `REGION`
- \[Breaking Change] The following `fields` values have been deprecated:
  
  - `FETCHES`
  - `RENDER_RATIO`
  - `FETCH_REACH`
  - `SERVES`
  - `ERRORS`
  - `COMPLETION_RATE`
- \[Breaking Change] The following fields have been renamed:
  
  - `SERVE_REACH` is now `REACH`
  - `SERVE_FREQ` is now `FREQUENCY`
- \[Breaking Change] The following filters have been deprecated:
  
  - `advertiser_ids`
  - `country_isos`
  - `region_ids`
  - `dma_ids`
  - `platforms`
  - `ad_set_start_dates`
  - `ad_set_end_dates`
  - `cost_type_filters`
  - `organization_ids`
  - `ad_account_ids` (all reports must now include a single ad account ID in the path but filtering by multiple ad account IDs is no longer supported)
- \[Breaking Change] Filtering by campaign, ad set, or ad ID(s) has been consolidated into two generic fields (previously this was supported via separate filters for each entity type):
  
  - entity\_ids: A list of one or more campaign, ad set, or ad IDs by which to filter reporting
  - entity\_ids\_type: The entity type of IDs contained in the entity\_ids field – if entity\_ids is set, this field is required.
- \[Breaking Change] Filtering by campaign, ad set, or ad ID status(es) has been consolidated into two generic fields:
  
  - entity\_status\_type: The entity type of statuses contained in the statuses field
  - statuses: A list of one or more campaign, ad set, or ad statuses by which to filter reporting – If this field is set, the entity\_status\_type field is required
- \[New] The following audience insight dimensions have been added and are available under the Get Insight Report by Ad Account ID endpoint:
  
  - `AGE`
  - `GENDER`
  - `GENRE`
- \[New] The following updates will go into effect on September 1, 2023:
  
  - Data refresh cadence will be increased to hourly (vs every few hours in v1-v1.4) – this will result in a discrepancy between UI and API stats for those who have not yet updated their integration to v2
  - Zero-stat campaigns (i.e., campaigns that have not yet been trafficked) will automatically be included in reports
  - SPEND field will be capped based on billable impressions; this means that spend tied to delivery over the specified budget will now be filtered out in order to match the UI’s logic

#### Estimates

- Estimate Bid (formerly known as `Get Bid Estimate`)
  
  - \[Breaking Change] Get Bid Estimate endpoint has been shortened to POST `/estimates/bid` (was previously POST `/adAccounts/{ad_account_id}/estimate/bid`)
  - \[Breaking Change] `budget_micro_amount` is no longer required in the request body
  - \[Breaking Change] The following parameters are now required when fetching a bid estimate:
    
    - `start_date`
    - `end_date`
    - `asset_format`
    - `bid_strategy`
    - `currency`
  - \[Breaking Change] `bid_optimization_goal` has been renamed to `objective`
  - \[New] The following optional request body parameters have been added:
    
    - frequency\_caps
    - Under `targets` object:
      
      - `postal_code_ids` (nested under geo\_targets)
      - `podcast_episode_topic_ids`
      - `sensitive_topic_exclusion_ids`
      - `language`
      - `interest_ids`
      - `exclude_placements`
- Estimate Audience (formerly known as `Get Audience Estimate`)
  
  - \[Breaking Change] Get Bid Estimate endpoint has been shortened to POST `/estimates/audience` (was previously POST `/adAccounts/{ad_account_id}/estimate/audience`)
  - \[Breaking Change] ad\_account\_id is now a request body parameter (was previously a path parameter)
  - \[Breaking Change] The following parameters are now required when fetching a bid estimate:
    
    - `start_date`
    - `end_date`
    - `asset_format`
    - `bid_strategy`
    - `budget` (type & micro\_amount)
  - \[Breaking Change] `bid_optimization_goal` has been renamed to `objective`
  - \[New] The following optional request body parameters have been added:
    
    - frequency\_caps
    - Under `targets` object:
      
      - `postal_code_ids` (nested under geo\_targets)
      - `podcast_episode_topic_ids`
      - `sensitive_topic_exclusion_ids`
      - `language`
      - `interest_ids`
      - `exclude_placements`
  - \[New] The following parameters have been added to the response body:
    
    - `estimated_frequency_min`
    - `estimated_frequency_max`
    - forecast\_type: The time granularity of the forecast -- if a "LIFETIME" budget type is specified, the API will return a single "LIFETIME" forecast type and if a "DAILY" budget type is specified, the API will return "DAILY", "WEEKLY" and "MONTHLY" forecast types
    - likely\_to\_deliver\_budget: Indicates the likelihood of spending most of the budget

#### Ad Categories \[New]

- Get Ad Categories endpoint: Ad categories can be retrieved via this endpoint and input under the `ad_category` parameter in the Create Ad Set request

#### Podcast Shows \[New]

- Get Podcast Shows endpoint: Available for podcast promotion use only (not for targeting) – podcast shows can be retrieved via this endpoint and input under the `promotion_target_id` parameter in the Create Ad Set request

#### Documentation Updates

- Now that the Campaign Management API is in GA, mention of manual allowlisting process and closed beta requirements have been removed
- Versioning policy has been simplified and schedule has been updated to reflect November 13, 2023 deprecation date for v1.3-v1.4
- Filtering and Querying section has been removed
- Slicing section has been removed
- Object Hierarchy has been updated to reflect v2 changes
- Build a Campaign Guide has been updated based on new v2 specs
- Metrics Glossary has been updated to only reflect metrics included in v2

### November 2022

#### Announcing Ads API v1.4

All of the following updates are included under a new minor version (v1.4) released on November 29, 2022.

**What's New**

- Introducing new Click objective with accompanying Call-to-Action (“CTA”) card format
  
  - Spotify Ad Studio advertisers are now able to set up a click optimization goal for their campaigns along with reach and impressions goals introduced this year. Ads with click goal will be accompanied by a Call-to-Action card: a clickable ad experience consisting of an advertiser's companion image, a name and a call-to-action button. After the initial ad is served, the message will resurface across the Spotify app making it easier for listeners to remember and take action.
  - New enum value `CLICKS` is available under the `bid_optimization_goal` parameter when [creating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v1.4/post_ad_set), [updating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v1.4/put_ad_set), and [retrieving bid/audience estimates](https://developer.spotify.com/documentation/ads-api/reference/v1.4/get_bid_estimate)
  - CTA cards will be enabled for music ads only (not video) – [create ad](https://developer.spotify.com/documentation/ads-api/reference/v1.4/post_ad) endpoint now includes:
    
    - New required parameter `brand_name`: Displayed in ad
    - New optional parameter `tagline`: Displayed in CTA card, max 140 characters
    - These two parameters are included in the response when retrieving ads
  - Enforcing new validation logic, see Breaking Changes/Deprecations section below for details

**Breaking Changes/Deprecations**

- New parameter `brand_name` is now required when creating an ad
- Removed and replaced `slot_type` with `format` under ad sets/estimates targeting object
- Removed `country_codes` (array of string) under ad sets/estimates `targeting` object and replaced with `country_code` (string)
- Validation rules added:
  
  - Ad set start and end dates must be in the future
  - Max ad set duration of 365 days
  - Minimum length of 2 characters and maximum of 120 characters for campaigns, ad sets and ads entity names
  - Only one country may be targeted per ad set

### August 2022

All of the following updates are included under the current version of the API v1.3:

- New enum value `ARTIST_CONTENT` is available under the `artist_promotion_goal` parameter when [creating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v1.3/post_ad_set) or [updating an ad set](https://developer.spotify.com/documentation/ads-api/reference/v1.3/put_ad_set): Users can now specify when they are promoting an artist's merch or concert by selecting this option (NOTE: `ARTIST_BOOST` should continue to be used when promoting an artist's music on Spotify).

### July 2022 - v1.3

#### Announcing Ads API v1.3

All of the following updates are included under a new minor version (v1.3) released July 2022.

**What's New**

- New minor version v1.3 released. *Note: v1.1 and v1.2 will be fully deprecated on August 25, 2022. See [Versioning](https://developer.spotify.com/documentation/ads-api#versioning) section for version schedules.*
- Addition of effective cost per mille and completed listen fields, `ECPM` and `ECPCL`, to [reporting](https://developer.spotify.com/documentation/ads-api/reference/v1.4/get_report) endpoints. See [Metrics Glossary](https://developer.spotify.com/documentation/ads-api/guides#campaign-performance-metrics) for detailed definitions. **Note:** `ECPM` is deprecated and will be removed in Ads API v4. Please use `CPM` instead.
- Ad sets and Estimates requests have been updated to use an auction pricing model, see "Breaking Changes/Deprecations" below for details
- `frequency_caps` is no longer a required parameter for [create ad sets](https://developer.spotify.com/documentation/ads-api/reference/v1.4/post_ad_set) requests; it is now optional. If `frequency_caps` is not specified, API will default to the maximum allowed values:
  
  - 5 per day
  - 35 per week
  - 50 per month

**Breaking Changes/Deprecations**

- Addition of `bid_optimization_goal`, `bid_strategy`, and `bid_micro_amount` to ad sets output responses, as *required* fields to [create ad sets](https://developer.spotify.com/documentation/ads-api/reference/v1.4/post_ad_set) requests, and as *optional* fields to [update ad sets](https://developer.spotify.com/documentation/ads-api/reference/v1.4/put_ad_set) requests
  
  - Allowed values for `bid_optimization_goal` are:
    
    - `EVEN_IMPRESSION_DELIVERY`: We’ll aim to deliver as many impressions as possible to your target audience. Not available for active audio (CPCL) ad sets.
    - `REACH`: We’ll aim to reach as many unique listeners as possible with your message.
    - `AD_COMPLETES`: We’ll aim to deliver as many impressions as possible to your target audience. Available for active audio (CPCL) ad sets only.
  - Allowed values for `bid_strategy` are:
    
    - `MAX_BID`: The bid you specify will act as a ceiling/cap.
- The following fields under the ad sets objects have been renamed:
  
  - `optimization` is now `artist_promotion`
  - `optimization_goal` is now `artist_promotion_goal`
  - `optimization_target` is now `artist_promotion_target`
  - `optimization_target_type` is now `artist_promotion_target_type`
- The previous `/estimate` endpoints are deprecated and replaced with two new ones ([Get Bid Estimate](https://developer.spotify.com/documentation/ads-api/reference/v1.4/get_bid_estimate) and [Get Audience Estimate](https://developer.spotify.com/documentation/ads-api/reference/v1.4/get_audience_estimate)) that allow users to specify bid details:
  
  - `POST /v1.3/adAccounts/{ad_account_id}/estimate/audience` is replacing `POST /v1.2/estimate`
  - `POST /v1.3/adAccounts/{ad_account_id}/estimate/bid` is replacing `POST /v1.2/adAccounts/{ad_account_id}/estimate/cost`

**Documentation Updates**

- Migrated documentation to main portal [Spotify for Developers](https://developer.spotify.com/)

### December 2021 - v1.2

#### Announcing Ads API v1.2

All of the following updates are included under a new minor version (v1.2) released December 2021.

**What's New**

- New minor version v1.2 released
- Added new [pricing estimate endpoint](https://developer.spotify.com/documentation/ads-api/reference/v1.2/get_cost_estimate) to estimate your CPM/CLCL/CPCV based on specified targeting parameters
  
  - `POST /adAccounts/{ad_account_id}/estimate/cost`
- Added `custom_audience_ids` under the `targeting` parameter for ad sets
  
  - You now have the option to specify custom audiences to target when creating/updating an ad set
- Added `third_party_viewability_tracking` for ads
  
  - You now have the ability to set up third-party viewability tracking when creating/updating an ad
  - NOTE: This is currently only supported for measurement partner `IAS`

**Breaking Changes/Deprecations**

- “Flights” have been renamed “Ad Sets”
  
  - We have renamed all instances of these entities in v1.2 in order to match the nomenclature used in the Ad Studio UI
- “Creatives” have been renamed “Ads”
  
  - We have renamed all instances of these entities in v1.2 in order to match the nomenclature used in the Ad Studio UI
- Removed parameter “unit\_cost\_micro\_amount” from [Create Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v1.2/post_ad_set) and [Update Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v1.2/put_ad_set) (fka Flight) endpoints

**Documentation Updates**

- Added new sections: “Metrics Glossary” and “Release Notes”
- Added additional detail on the expected behavior of the `report_datetime_range` filter under the [Reporting API](https://developer.spotify.com/documentation/ads-api/guides#reporting-open-beta)
- Updates to “Versioning” section - added version release/sunset schedule

### November 2021 - v1.1

- Added support for podcast ad performance data to the Reporting API
  
  - Ads served to podcast listeners on Spotify will automatically be reflected without making any updates to your integration
  - To capture the impressions served off Spotify, you will need to update your integration by adding the new metric called `OFF_SPOTIFY_IMPRESSIONS`
  - There are no breaking changes associated with this launch, however, we recommend that you complete this update as soon as possible in order to accurately reflect podcast ad performance

### June 2019 - v1.1

#### Announcing Ads API v1.1

v1.1 was released June 2019

**What's New**

- Combined the `/geo` and `/geos` endpoints into just `/geos`. See docs [here](https://developer.spotify.com/documentation/ads-api/reference/v1.4/get_targets_geo)
- `/geos` endpoint now allows you to specify a type of geo you are searching for as a filter in a query param.

### April 2019 - v1.0

- Renamed the landing\_page\_url field to be landing\_page\_domain so it is consistent across the API
- Renamed arrays on GET targets and GET campaigns to be consistent with rest of API
- Refactored statuses on flight endpoint
- Pausing status for flight and flight links
  
  - Previously, you had to pause a flight on the update flight request. Now, there is a separate endpoint to pause / activate / archive a flight. You are no longer able to change the status on the update flight request.
- Added Flight Links endpoints
  
  - Flight links are a connection between flights and creatives that ensure the creative(s) and its contents are compatible with the flight’s targeting
- Added serving status endpoint
  
  - The new serving status endpoint indicates whether your flight is serving or not

### March 2019 - v1.0

- Added Campaign Status Endpoint
  
  - The available statuses for campaigns are ACTIVE, PAUSED, and ARCHIVED
- Removed CANCELLED as a status on campaigns
  
  - Campaigns can now only be archived, not cancelled
  - Archiving will permanently pause a campaign, you cannot unarchive a campaign
  - Archiving a campaign will prevent delivery across all associated flights
- Removed ability to update campaign status on PUT
  
  - Use the campaign status endpoint
- Added support for slicing on all GET LIST requests for creatives, flights, and campaigns
  
  - Slicing is the ability to specify what fields you want returned
  - How it works: GET LIST endpoints, there is a query parameter called `fields` where you can specify a comma-separated list of fields you want returned
- Added support for filtering on all the GET LIST requests for creatives, flights, and campaigns
  
  - Filtering is the ability to filter your results based on specific criteria (e.g., Get Flights for a specific Advertiser ID)
  - How it works: On the GET LIST endpoints, there are optional query parameters to specify the filter
- Added support for ordering by a specific field on GET LIST requests for creatives, campaigns, and flights
  
  - How it works: There are optional query parameters to specify the ordering field, ascending or descending based on the field