---
title: Ads API Guides | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/guides#build-a-campaign
source: crawler
fetched_at: 2026-02-27T23:40:09.157806-03:00
rendered_js: true
word_count: 4366
summary: This document explains the hierarchical structure of Spotify Ads Manager accounts and provides instructions for managing campaigns, ad sets, and creative assets via the Ads API.
tags:
    - spotify-ads-api
    - campaign-management
    - object-hierarchy
    - ad-targeting
    - asset-management
    - advertising-platform
category: guide
---

## Object Hierarchy

Your [Ads Manager](https://ads.spotify.com/en-US/how-it-works/) account comprises sets of related objects organized in a hierarchy. The Ads API gives you direct, programmatic access to these objects. From top to bottom, the objects that build the structure of your account include:

- Businesses
- Ad Accounts
- Campaigns
- Ad Sets
- Ads
- Assets

!["Ads Manager Platform Structure"](https://developer-assets.spotifycdn.com/images/products/ads-api/ads-manager-account-structure.png)

### Businesses

When you create an account in Spotify Ads Manager, a business account and an associated ad account will automatically be created for you. A business is an object used to centrally manage multiple ad accounts.

### Ad Accounts

You must have an ad account before you can create advertisers, campaigns, ad sets, or ads. Use the [Get Ad Account by ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAllAdAccountsInBusiness) endpoint to view information about your account after it has been set up.

### Campaigns

A campaign is an object that contains and organizes one or more ad sets. Also, you need a campaign *before* you can create an ad set. Use the [Create Campaign](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCampaign) endpoint to create a campaign under your ad account.

### Ad Sets

An ad set is the core component of your Ads Manager campaign. It is a child of a campaign object and contains all the essential information Ads Manager needs to execute your campaign. For example, an ad set contains:

- Information about how, when, and where your campaign runs (e.g., start and end dates, bids, budgets, targeting, etc).
- One or more ads.

See the [Create Ad Set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet) endpoint for more information or to add an ad set to a campaign.

### Ads

An ad is an object that contains an image asset along with either an audio or video asset. Each ad must be linked to an ad set but a given ad cannot be linked to multiple ad sets. See the eponymous [Create Ad](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAd) endpoint to get started.

### Assets

The Ads Manager platform supports audio, video, and image assets. These assets are required to create an ad. The asset endpoints help you upload and manage these items. Use the following endpoints to first create and then upload an asset:

- [Create Asset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAsset)
- [Upload Asset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/uploadAsset)

## Campaign Management

### Overview

The Campaign Management API allows you to create and manage campaigns, ad sets, and ads at scale. It also includes endpoints to estimate audience size and bid amount based on your targeting specifications (set at the ad set level).

### Eligibility Criteria

As of August 2023, the Campaign Management API is generally available ("GA") and no longer requires a manual allowlisting process to gain access. As soon as you have [set up your application](https://developer.spotify.com/documentation/ads-api/documentation/ads-api/quick-start#initialize-your-new-ads-api-application), your client ID will be able to access these endpoints automatically.

Please note that the Campaign Management API is only available for advertisers with a Spotify [Ads Manager](https://adsmanager.spotify.com/) account.

### Differences from the UI

Most features available in the Ads Manager UI are also available via the Ads API, with a few exceptions:

FeatureSupported in Spotify Ads Manager UISupported in Spotify Ads APICreate new ad accountyesyes - as of v3Manage usersyesnoManage billing/paymentyesnoVoiceover generationyesno[Real-time context targeting](https://ads.spotify.com/en-US/help-center/targeting-ad-studio/#real_time_context_targeting)yesyes - Referred to as [playlist](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getPlaylistTargets) targeting[Fan targeting](https://ads.spotify.com/en-US/help-center/targeting-ad-studio/#fan_targeting)yesyes - Referred to as [artist](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getArtistTargets) targetingMOAT viewability tracking set upyesno - Only IAS is available

### Build a campaign

Follow these steps to build your first end-to-end campaign with the Ads API. NOTE: The below sample curl requests do not reflect every request parameter available.

#### Step 1: Retrieve your business & ad account ID

If you're unsure of your business ID, you can call the [Get Businesses for Current User](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getBusinesses) endpoint to return a list of all businesses available to the current authenticated user.

`1`

`curl --request GET \`

`2`

`--url https://api-partner.spotify.com/ads/v3/businesses \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>'`

You can then use the business ID to retrieve a list of all ad accounts under the business that the current authenticated user has access to via the [Get Ad Accounts for Current User by Business ID](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAllAdAccountsInBusiness) endpoint.

`1`

`curl --request GET \`

`2`

`--url https://api-partner.spotify.com/ads/v3/businesses/<BUSINESS_ID>/ad_accounts \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>'`

#### Step 2: [Create a campaign](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCampaign)

`1`

`curl --request POST \`

`2`

`--url https://api-partner.spotify.com/ads/v3/ad_accounts/<AD_ACCOUNT_ID>/campaigns \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>' \`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"name": "My Test Campaign",`

`7`

`"objective": "EVEN_IMPRESSION_DELIVERY"`

`8`

`}'`

Upon success, the API will return an ID for the newly created campaign. Store this ID for use in Step 5 (Create an ad set).

#### Step 3: Define targeting specifications

Use the /targets endpoints to understand/retrieve the available targeting options -- supported categories include:

- [artist](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getArtistTargets)
- [genre](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getGenreTargets)
- [playlist](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getPlaylistTargets)
- [interest](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getInterestTargets)
- [language](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getLanguageTargets)
- [geographic location](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getGeoTargets) (country, region, DMA, city, and postal code)
- [podcast episode topics](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getEpisodeTopicTargets)
- [sensitive topic targets](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getSensitiveTopicTargets)

#### Step 4: \[Optional] Estimate audience size and recommended bid amount

In order to help plan your campaign, we recommend using the /estimates endpoints to help forecast estimated audience size and recommended bid amount based on your targeting specifications (NOTE: Estimates are NOT a guarantee of performance).

[Retrieve a recommended bid range](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateBid):

`1`

`curl --request POST \`

`2`

`--url https://api-partner.spotify.com/ads/v3/estimates/bid \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>' \`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"start_date": "2025-09-23T04:00:00Z",`

`7`

`"end_date": "2025-10-23T04:00:00Z",`

`8`

`"bid_strategy": "MAX_BID",`

`9`

`"asset_format": "AUDIO",`

`10`

`"currency": "USD",`

`11`

`"targets": {`

`12`

`"age_ranges": [`

`13`

`{`

`14`

`"min": 18,`

`15`

`"max": 65`

`16`

`}`

`17`

`],`

`18`

`"playlist_ids": [`

`19`

`"holidays",`

`20`

`"cooking"`

`21`

`],`

`22`

`"genders": [`

`23`

`"MALE"`

`24`

`],`

`25`

`"geo_targets": {`

`26`

`"dma_ids": [`

`27`

`"501"`

`28`

`],`

`29`

`"region_ids": [`

`30`

`"5279468"`

`31`

`],`

`32`

`"city_ids": [`

`33`

`"4174700"`

`34`

`]`

`35`

`},`

`36`

`"genre_ids": [`

`37`

`"rock",`

`38`

`"blues"`

`39`

`],`

`40`

`"platforms": [`

`41`

`"IOS"`

`42`

`],`

`43`

`"placements": [`

`44`

`"PODCAST",`

`45`

`"MUSIC"`

`46`

`]`

`47`

`},`

`48`

`"objective": "EVEN_IMPRESSION_DELIVERY"`

`49`

`}'`

[Retrieve an audience estimate](https://developer.spotify.com/documentation/ads-api/reference/v3.0/estimateAudience):

`1`

`curl --request POST \`

`2`

`--url https://api-partner.spotify.com/ads/v3/estimates/audience \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>' \`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"ad_account_id": "<AD_ACCOUNT_ID>",`

`7`

`"start_date": "2025-09-23T04:00:00Z",`

`8`

`"end_date": "2025-10-23T04:00:00Z",`

`9`

`"bid_strategy": "MAX_BID",`

`10`

`"asset_format": "AUDIO",`

`11`

`"targets": {`

`12`

`"age_ranges": [`

`13`

`{`

`14`

`"min": 18,`

`15`

`"max": 65`

`16`

`}`

`17`

`],`

`18`

`"playlist_ids": [`

`19`

`"holidays",`

`20`

`"cooking"`

`21`

`],`

`22`

`"platforms": [`

`23`

`"IOS"`

`24`

`],`

`25`

`"genders": [`

`26`

`"MALE"`

`27`

`],`

`28`

`"language": "en",`

`29`

`"geo_targets": {`

`30`

`"country_code": "US",`

`31`

`"dma_ids": [`

`32`

`"501"`

`33`

`],`

`34`

`"region_ids": [`

`35`

`"5279468"`

`36`

`],`

`37`

`"city_ids": [`

`38`

`"4174700"`

`39`

`]`

`40`

`},`

`41`

`"genre_ids": [`

`42`

`"rock",`

`43`

`"blues"`

`44`

`],`

`45`

`"placements": [`

`46`

`"PODCAST",`

`47`

`"MUSIC"`

`48`

`]`

`49`

`}`

`50`

`},`

`51`

`"objective": "EVEN_IMPRESSION_DELIVERY",`

`52`

`"budget": {`

`53`

`"micro_amount": 25000000,`

`54`

`"type": "DAILY",`

`55`

`"currency": "USD"`

`56`

`}`

`57`

`}'`

#### Step 5: [Create an ad set](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAdSet)

`1`

`curl --request POST \`

`2`

`--url https://api-partner.spotify.com/ads/v3/ad_accounts/<AD_ACCOUNT_ID>/ad_sets \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>' \`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"name": "My Test Ad Set",`

`7`

`"start_time": "2025-10-23T00:00:00Z",`

`8`

`"end_time": "2025-10-30T00:00:00Z",`

`9`

`"frequency_caps": [`

`10`

`{`

`11`

`"frequency_unit": "DAY",`

`12`

`"max_impressions": 3,`

`13`

`"frequency_period": 1`

`14`

`},`

`15`

`{`

`16`

`"frequency_unit": "WEEK",`

`17`

`"max_impressions": 5,`

`18`

`"frequency_period": 1`

`19`

`},`

`20`

`{`

`21`

`"frequency_unit": "MONTH",`

`22`

`"max_impressions": 15,`

`23`

`"frequency_period": 1`

`24`

`}`

`25`

`],`

`26`

`"bid_micro_amount": 5000000,`

`27`

`"category": "ADV_1_1",`

`28`

`"budget": {`

`29`

`"micro_amount": 15000000,`

`30`

`"type": "DAILY"`

`31`

`},`

`32`

`"targets": {`

`33`

`"age_ranges": [`

`34`

`{`

`35`

`"min": 18,`

`36`

`"max": 65`

`37`

`}`

`38`

`],`

`39`

`"playlist_ids": [`

`40`

`"holidays",`

`41`

`"cooking"`

`42`

`],`

`43`

`"genders": [`

`44`

`"MALE"`

`45`

`],`

`46`

`"geo_targets": {`

`47`

`"dma_ids": [`

`48`

`"501"`

`49`

`],`

`50`

`"region_ids": [`

`51`

`"5279468"`

`52`

`],`

`53`

`"city_ids": [`

`54`

`"4174700"`

`55`

`]`

`56`

`},`

`57`

`"genre_ids": [`

`58`

`"rock",`

`59`

`"blues"`

`60`

`],`

`61`

`"platforms": [`

`62`

`"IOS"`

`63`

`],`

`64`

`"placements": [`

`65`

`"PODCAST",`

`66`

`"MUSIC"`

`67`

`]`

`68`

`},`

`69`

`"bid_strategy": "MAX_BID",`

`70`

`"campaign_id": "<CAMPAIGN_ID>",`

`71`

`"asset_format": "AUDIO"`

`72`

`}'`

Upon success, the API will return an ID for the newly created ad set. Store this ID for use in Step 7 (Create an ad).

TIP: If you want to ensure your ad set is not trafficked while you are still finalizing details, you can set the "delivery" to "OFF" until you are ready to have it go live.

#### Step 6: Create & Upload assets

First, [create an asset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAsset) (the below example is for creating a companion image asset):

`1`

`curl --request POST \`

`2`

`--url https://api-partner.spotify.com/ads/v3/ad_accounts/<AD_ACCOUNT_ID>/assets \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>' \`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"asset_type": "IMAGE",`

`7`

`"name": "myImage.png"`

`8`

`}'`

Upon success, the API will return an ID for the newly created image asset.

Next, [upload](https://developer.spotify.com/documentation/ads-api/reference/v3.0/uploadAsset) your file to the newly created asset:

`1`

`curl -X 'POST' \`

`2`

`'https://api-partner.spotify.com/ads/v3/ad_accounts/<AD_ACCOUNT_ID>/assets/<ASSET_ID>/upload' \`

`3`

`-H 'accept: application/json' \`

`4`

`-H 'Authorization: Bearer <ACCESS_TOKEN>' \`

`5`

`-H 'Content-Type: multipart/form-data' \`

`6`

`-F 'media=@"<FILE_PATH>";type=image/"<FILE_TYPE>"' \`

`7`

`-F 'asset_type="IMAGE"'`

TIP: You can confirm the asset has been processed successfully by calling the [Get Asset](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAsset) endpoint and referring to 'status' in the response:

`1`

`curl --request GET \`

`2`

`--url https://api-partner.spotify.com/ads/v3/ad_accounts/<AD_ACCOUNT_ID>/assets/<ASSET_ID> \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>'`

Repeat the above upload process for either an audio or a video asset and then proceed to Step 7. There are endpoints available to do a [chunked upload](https://developer.spotify.com/documentation/ads-api/reference/v3.0/startUploadChunkedAsset) for larger audio or video files.

#### Step 7: [Create an ad](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createAd)

All ads must include either an audio asset or a video asset, in addition to a companion image asset.

`1`

`curl --request POST \`

`2`

`--url https://api-partner.spotify.com/ads/v3/ad_accounts/<AD_ACCOUNT_ID>/ads \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>' \`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"advertiser_name": "My Advertiser",`

`7`

`"assets": {`

`8`

`"asset_id": "<AUDIO_OR_VIDEO_ASSET_ID>",`

`9`

`"companion_asset_id": "<IMAGE_ASSET_ID>"`

`10`

`},`

`11`

`"call_to_action": {`

`12`

`"clickthrough_url": "https://www.spotify.com"`

`13`

`},`

`14`

`"name": "My Test Ad",`

`15`

`"tagline": "Music for everyone",`

`16`

`"ad_set_id": "<AD_SET_ID>"`

`17`

`}'`

Upon success, the API will return an ID for the newly created ad.

TIP: If you want to ensure your ad is not trafficked while you are still finalizing details, you can set the "delivery" to "OFF" until you are ready to have it go live.

Congratulations on creating your first full campaign! Once your campaign has been approved through the review process and goes live, you can track its performance using the [Get Aggregate Report by Ad Account Id endpoint](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAggregateReport) endpoint.

## Reporting

### Overview

The Reporting API allows advertisers to access real-time performance data for campaigns created via Ads Manager UI or via third party platforms integrated with Spotify Campaign Management API based on custom queries. You can find definitions of the available metrics (aka “fields”) in the [Metrics Glossary](https://developer.spotify.com/documentation/ads-api/guides#Metrics-Glossary) section.

### Eligibility Criteria

As of November 2022, the Reporting API is generally available ("GA") and no longer requires a manual allowlisting process to gain access. As soon as you have [set up your application](https://developer.spotify.com/documentation/ads-api/documentation/ads-api/quick-start#initialize-your-new-ads-api-application), your client ID will be able to access these endpoints automatically.

Please note that the Reporting API is only available for advertisers with a Spotify [Ads Manager](https://adsmanager.spotify.com/) account.

### Differences from the UI (Reporting)

MetricSpotify Ads Manager UISpotify Ads APIBudgets and Spend“Budget Spent” metric (available at the ad set level only) will never exceed the budget amount set by the advertiser – overdelivery is only reflected in the ‘Pacing’ column`SPEND` field is not capped based on budget set by advertiser - in the event of overdelivery, `SPEND` may exceed the budget amount set by the advertiser but **advertisers will only be billed up to their budget amount**

## Metrics Glossary

This section includes definitions for all the metrics (referred to as `fields`) that are available via the Reports endpoints.

**NOTE**: Where we have a Metric/Field name that looks like the following:

> New Listener Streams (`"NEW_LISTENER_STREAMS"`/`"AVG_STREAMS_PER_NEW_LISTENER"`)

We have the same exact metrics labeled differently across our synchronous and asynchronous reporting endpoints. We are currently working on creating consistency between these.

### Delivery Metrics

Metric/FieldDefinitionFrequency of Ads Served(`"FREQUENCY"`)The average number of times each person heard or viewed your ad (#).Impressions(`"IMPRESSIONS"`)The number of times an ad has been served (#).Streamed Impressions (`"STREAMED_IMPRESSIONS"`)The number of times an ad has been streamed (#).Downloaded Impressions (`"OFF_SPOTIFY_IMPRESSIONS"`)The number of times an ad has been downloaded (#). *NOTE: This field will soon be renamed `"DOWNLOADED_IMPRESSIONS"` to match it's definition*Reach of Ads Served (`"REACH"`)The number of unique users who received your ad (#).Amount Spent (`"SPEND"`)The total amount spent in this campaign (#).Starts (`“STARTS”`)The number of times a user starts hearing/viewing your ad (#).

### Auction Metrics

Metric/FieldDefinitionCost per Mille (`"CPM"`)The cost per 1,000 impressions

### Performance Metrics

Metric/FieldDefinitionFirst Quartiles (`"FIRST_QUARTILES"`)The number of ads within the ad set served that played at least 25% of way through (#). - *NOTE: This will soon be replaced with `"Ad played to 25%"`*Midpoints (`"MIDPOINTS"`)The number of ads within the ad set served that played at least 50% of way through (#). - *NOTE: This will soon be replaced with `"Ad played to 50%"`*Third Quartiles (`"THIRD_QUARTILES"`)The number of ads within the ad set served that played at least 75% of way through (#). - *NOTE: This will soon be replaced with `"Ad played to 75%"`*Completes (`"COMPLETES"`)The number of ads within the ad set served that were played to the end (see also: Completion rate) (#). - *NOTE: This will soon be replaced with `"Ad played to 100%"`*Clicks (`"CLICKS"`)The number of times in which your ad was clicked (#).Completion Rate (`"COMPLETION_RATE"`)The percentage of ads played to completion (%).Click Through Rate (`"CTR"`)The percentage of ads that were clicked (%).Video Views (`"VIDEO_VIEWS"`)The number of times your video played for at least 3 seconds\** (#).Video Expands (`"VIDEO_EXPANDS"`)The number of times someone tapped your ad to expand it\** (#).Video Expand Rate (`"VIDEO_EXPAND_RATE"`)The number ad expands divided by the number of impressions\** (%).Unmutes (`"UNMUTES"`)The number of times a user unmutes an ad (#).Effective Cost per Click (`“E_CPC”`)The average cost per click if this campaign were billed on clicks* (fraction). -- NOTE: all campaigns are currently billed on cost per 1000 impressions

- "\*" Metrics only available at the Ad Set report level.
- "\*\*" Metrics only available for campaigns with the video views objective (i.e. for opt-in video ads).

### Streaming Conversion Metrics

Metric/FieldDefinitionUnique Listeners(`"LISTENERS"`)The number of unique Spotify users who streamed at least 30 seconds of the promoted content within 14 days of seeing or hearing your ad. (#)Listener Conversion Rate (`"CONVERSION_RATE"`/`"LISTENER_CONVERSION_RATE"`)The percentage of listeners who streamed your content after seeing or hearing your ad. (%)New Listeners (`"NEW_LISTENERS"`)The number of listeners who had not streamed your content in the 28 days before seeing or hearing your ad. (#)New Listeners Conversion Rate (`"NEW_LISTENER_CONVERSION_RATE"`)The percentage of new listeners who streamed your content after seeing or hearing your ad. (%)Streams (`"STREAMS"`)The number of times listeners streamed your content for at least 30 seconds within 14 days of seeing or hearing your ads. (#)New Listener Streams (`"NEW_LISTENER_STREAMS"`/`"AVG_STREAMS_PER_NEW_LISTENER"`)The number of streams from new listeners who heard or saw your ad. (#)Average Streams per Listener (`"STREAMS_PER_USER"`/`"AVG_STREAMS_PER_LISTENER"`)The average number of times each listener streamed your content after seeing or hearing your ad. (#)Average Streams per New Listener (`"STREAMS_PER_NEW_LISTENER"`)The average number of times each new listener streamed your content after seeing or hearing your ad. (#)

### Conversion Measurement

Description: We've updated our attribution methodology with improved data resolution, which helps us provide a deterministic understanding of the customers who take action after seeing or hearing an ad on Spotify. The following information is applicable to campaigns with a start date of Dec 3, 2024 or earlier. Learn more about the updated attribution methodology

Metric/FieldDefinitionPage Views (`"PAGE_VIEWS"`)The total number of page views attributed to your ads within a 30-day window. Page views are counted when a webpage loads in the browser based on information received from your data sources connected to Spotify (#).Leads (`"LEADS"`)The number of lead events attributed to your ads within a 30-day window. Lead events are defined by the user when setting up the data source and connecting it to Spotify (#).Adds to Cart (`"ADD_TO_CART"`)The number of add to cart events attributed to your ads within a 30-day window. Add to cart events are defined by the user when setting up the data source and connecting it to Spotify (#).Purchases (`"PURCHASES"`)The number of purchase events attributed to your ads within a 30-day window. Purchase events are defined by the user when setting up the data source and connecting it to Spotify (#).Attributed Revenue (`"REVENUE"`)The total amount of revenue attributed from purchase or lead events based on information received from data sources connected to Spotify. Revenue tracking events must include currency and value parameters (#).Average Order Value (AOV) (`"AVERAGE_ORDER_VALUE"`)The average value per transaction made by a customer based on attributed revenue and the count of purchase and lead events received from data sources connected to Spotify. To calculate this metric, data sources must be sending revenue tracking events, like purchases or leads, including value and currency parameters (#).Return on Ad Spend (ROAS) (`"RETURN_ON_AD_SPEND"`)The total return on ad spend (ROAS) from attributed purchases. This is based on the value of purchase or lead events received from data sources connected to Spotify. Data sources must be passing revenue tracking events, like purchases or leads, with value and currency parameters (#).Customer Acquisition Cost (CAC) (`"CUSTOMER_ACQUISITION_COST"`)The cost of acquiring a new customer, calculated by dividing campaign spend by the number of purchases or leads attributed to Spotify-connected data sources. Data sources must be passing revenue tracking events, like purchases or leads, with value and currency parameters (#).Cost per Lead (`"COST_PER_LEAD"`)The cost of acquiring a lead, calculated by dividing campaign spend by the number of leads attributed to information received by Spotify-connected data sources (#).Start Checkouts (`"START_CHECKOUT"`)The number of start checkout events attributed to your ads within a 30-day window. Start checkout events are defined by the user when setting up the data source and connecting it to Spotify (#).Product Views (`"PRODUCTS"`)The number of product view events attributed to your ads within a 30-day window. Product view events are defined by the advertiser when setting up the data source and connecting it to Spotify (#).Sign-ups (`"SIGN_UPS"`)The number of sign-up events attributed to your ads within a 30-day window. Sign-up events are defined by the user when setting up the data source and connecting it to Spotify (#).Custom Event 1 (`"CUSTOM_EVENT_1"`)The number of custom events attributed to your ads within a 30-day window. Custom events are defined by the user when setting up and connecting the data source to Spotify and can't be renamed (#).Custom Event 2 (`"CUSTOM_EVENT_2"`)The number of custom events attributed to your ads within a 30-day window. Custom events are defined by the user when setting up and connecting the data source to Spotify and can't be renamed (#).Custom Event 3 (`"CUSTOM_EVENT_3"`)The number of custom events attributed to your ads within a 30-day window. Custom events are defined by the user when setting up and connecting the data source to Spotify and can't be renamed (#).Custom Event 4 (`"CUSTOM_EVENT_4"`)The number of custom events attributed to your ads within a 30-day window. Custom events are defined by the user when setting up and connecting the data source to Spotify and can't be renamed (#).Custom Event 5 (`"CUSTOM_EVENT_5"`)The number of custom events attributed to your ads within a 30-day window. Custom events are defined by the user when setting up and connecting the data source to Spotify and can't be renamed (#).

### Legacy Metrics

Description: Legacy metrics are metrics that are currently deprecated. They will soon be sunset or no longer supported by Spotify Ads Manager, but they are currently maintained for historical reporting purposes. All legacy metrics will be removed from future major versions and no longer supported in the Ads API.

Metric/FieldDefinitionEffective Cost per Mille (`"E_CPM"`)The average cost per 1,000 impressions (#). *NOTE: Please use `"CPM"` instead.*Effective Cost per Completed Listen (`"E_CPCL"`/`"CPCL"`)The average cost per 1,000 completed listens (#). -- NOTE: Applies to active audio/CPCL campaigns onlyIntent Rate (`"INTENT_RATE"`)The percentage of listeners who took actions showing intent to stream your content again in the future (%). Actions include saving your content (by tapping the + icon or “save”) or adding it to a playlist.(%)Ad Completes (`"AD_COMPLETES"`)The number of listens for a CPCL campaign where a user did NOT skip the ad (#). -- NOTE: Applies to active audio/CPCL campaigns only.Paid Listens (`"PAID_LISTENS"`)The number of listens for a CPCL campaign where a user did NOT skip the ad (#). -- NOTE: Applies to active audio/CPCL campaigns only.Frequency of Paid Listens (`"PAID_LISTENS_FREQUENCY"`/`"FREQUENCY_OF_AD_COMPLETES"`)The average frequency for listens on a CPCL campaign (#). -- NOTE: Applies to CPCL campaigns only.Reach of Paid Listens (`"PAID_LISTENS_REACH"`/`"REACH_OF_AD_COMPLETES"`)The number of unique users who had a paid listen for this CPCL campaign (#). -- NOTE: Applies to active audio/CPCL campaigns only.Skips(`"SKIPS"`)The number of times a user skips an ad -- NOTE: Skippable ads are currently supported in AU only (#).Modeled Add to Cart (`"MODELED_ADD_TO_CART"`)The number of attributed add-to-cart events by modeled (not IP-matched) households (#).Modeled Leads (`"MODELED_LEAD"`)The number of attributed lead events by modeled (not IP-matched) households (#).Modeled Page Views (`"MODELED_PAGE_VIEWS"`)The number of attributed website page views by modeled (not IP-matched) households (#).Modeled Purchases (`"MODELED_PURCHASES"`)The number of attributed purchase events by modeled (not IP-matched) households (#).Unmodeled Add to Cart (`"UNMODELED_ADD_TO_CART"`)The number of attributed add-to-cart events by IP-matched households (#).Unmodeled Leads (`"UNMODELED_LEADS"`)The number of attributed lead events by IP-matched households (#).Unmodeled Page Views (`"UNMODELED_PAGE_VIEWS"`)The number of attributed website page views by IP-matched households (#).Unmodeled Purchases (`"UNMODELED_PURCHASES"`)The number of attributed purchase events by IP-matched households (#).

### App Conversion Metrics

These metrics track the actions users take with your app after interacting with your ad, helping you to understand how your advertising influences behavior associated with your app.

Metric/FieldDefinitionApp Installs (AppsFlyer) (`“APPSFLYER_APP_INSTALLS”`)An attributed app install is counted when the downloaded app is opened. This data is provided to Spotify by your mobile measurement provider. (#)App Installs (Kochava) (`“KOCHAVA_APP_INSTALLS”`)An attributed app install is counted when the downloaded app is opened. This data is provided to Spotify by your mobile measurement provider. (#)SKAdNetwork App Installs (`“SKAD_APP_INSTALLS”`)An attributed app install is counted when the downloaded app is opened. This data is provided to Spotify by your mobile measurement provider. (#)

## Conversions API

Spotify’s Conversions API ("CAPI") is a tagless attribution tool that enables you to directly pass online and offline conversion events to Spotify. The Conversions API is designed to provide comprehensive, high-fidelity attribution to help you understand the performance of your campaigns on Spotify. See [here](https://adshelp.spotify.com/s/article/Spotify-Conversions-API-US) for more info.

### CAPI Setup Guide

This guide walks you through the steps to integrate with CAPI -- including how to obtain credentials, construct requests, and send and validate conversion event data.

#### Step 1: Create a Connection ID (`capi_connection_id`)

In order to send requests to CAPI you’ll need a Connection ID. The Connection ID is a unique key assigned to your organization that allows you to access CAPI when used with the token.

Via the UI: In the Ads Manager UI, go to Events → Connect Data Source → Conversions API. When you submit the form, the UI will show the newly created Connection ID (a UUID) for your CAPI integration.

Via the API: Call the [Create CAPI Integration](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCapiIntegration) endpoint to generate a new `capi_connection_id` which will be used in Step 2:

`1`

`curl --request POST \`

`2`

`--url https://api-partner.spotify.com/ads/v3/businesses/<BUSINESS_ID>/capi \`

`3`

`--header 'Authorization: Bearer <ADS_API_ACCESS_TOKEN>`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"name": "Retail Sales",`

`7`

`"dataset_id": "<DATASET_ID>"`

`8`

`}'`

#### Step 2: Get a CAPI auth token

**NOTE**: The endpoint to submit conversion events to CAPI uses a long-lived token, which is different the [auth token](https://developer.spotify.com/documentation/ads-api/quick-start#authenticate-your-ad-studio-account) used by other Ads API endpoints. You will be able to generate up to 3 CAPI tokens at a time. After your third token is created you will need to delete a previous token to generate a new one. Your token will not expire and can be used indefinitely.

Via the UI: In the Ads Manager UI, go to Events → Connect Data Source → Conversions API → Generate Token.

Via the API: Call the Get [CAPI Auth Token](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiAuthTokens) endpoint to generate a token:

`1`

`curl --request GET \`

`2`

`--url https://api-partner.spotify.com/ads/v3/businesses/<BUSINESS_ID>/capi/<CAPI_CONNECTION_ID>/tokens \`

`3`

`--header 'Authorization: Bearer <ADS_API_ACCESS_TOKEN>'`

#### Step 3: Send events to CAPI

**NOTE**: CAPI currently accepts four (4) identifier types: IP address, device ID, hashed email address, and hashed phone number. At least one type of identifier must be passed. As a best practice, include both IP and device ID when possible.

`1`

`curl --request POST \`

`2`

`--url https://capi.spotify.com/capi-direct/events/ \`

`3`

`--header 'Authorization: Bearer <CAPI_ACCESS_TOKEN>`

`4`

`--header 'Content-Type: application/json' \`

`5`

`--data '{`

`6`

`"conversion_events": {`

`7`

`"capi_connection_id": "<CAPI_CONNECTION_ID>",`

`8`

`"events": [`

`9`

`{`

`10`

`"event_name": "PURCHASE",`

`11`

`"event_id": "order-0001-20260123",`

`12`

`"event_time": "2026-01-23T12:34:56.000Z",`

`13`

`"user_data": {`

`14`

`"device_id": "rawdeviceid123xyz",`

`15`

`"ip_address": "203.0.113.12",`

`16`

`"hashed_emails": ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"]`

`17`

`},`

`18`

`"event_details": {`

`19`

`"content_category": "35",`

`20`

`"currency": "USD",`

`21`

`"amount": 100.0`

`22`

`}`

`23`

`}`

`24`

`]`

`25`

`}`

`26`

`}`

`27`

`'`

##### Request body fields

- `capi_connection_id` \[Required] — the UUID for your data source (from Ads Manager).
- `event_name` \[Required]
  
  - Allowed values: `VIEW`, `PRODUCT`, `CHECK_OUT`, `ADD_TO_CART`, `PURCHASE`, `LEAD`, `SIGN_UP`, `CUSTOM_EVENT_1`, `CUSTOM_EVENT_2`, `CUSTOM_EVENT_3`, `CUSTOM_EVENT_4`, `CUSTOM_EVENT_5`
- `event_id` \[Required] — a unique id for the event (recommended for deduplication if the same event is also reported by pixel/browser).
- `event_time` \[Required] — ISO 8601 timestamp (UTC recommended). Use precise times for deduplication and correct attribution.
- `user_data` \[Required]— one or more identifiers; hashed email/phone must be SHA-256.
  
  - `ip_address` (client IP)
  - `device_id` (raw device id)
  - `hashed_emails` (SHA256 hashed email)
  - `hashed_phone_number` (SHA256 hashed phone)
- `event_details` \[Optional] — freeform details about the event.
  
  - `currency`
  - `amount`
  - `content_category`
  - `content_name`
- `event_source_url` \[Optional] — The URL where the event occurred, must start with "http://" or "https://".
- `action_source` \[Optional] — The medium through which the conversion was made.
  
  - Allowed values:`WEB`, `APP`, `OFFLINE`
- `opt_out_targeting` \[Optional] — If true, the event will not be used for retargeting, only for attribution.

### CAPI Best Practices

- **Deduplicate**: Include `event_id` when you send the same event from browser pixel + server so Spotify can dedupe.
- **Hash & normalize**: Trim + lowercase email/phone before SHA-256 hashing. Partners’ guides instruct using SHA-256 for hashed identifiers.
- **IP address + device id**: Include both where possible to improve match rates.
- **Time format**: Use precise ISO 8601 UTC timestamps for `event_time`. (Ads docs reference standard time formats across Ads API.)
- **Error handling**: Retry on transient 5xx with backoff; for 4xx inspect payload and auth. Log response body (Spotify returns structured error messages).

### Additional CAPI Resources

- [Conversions API detailed overview](https://adshelp.spotify.com/s/article/Spotify-Conversions-API-US)
- Partner integration guides for practical hashing & mapping examples:
  
  - [Freshpaint](https://documentation.freshpaint.io/integrations/destinations/direct-response-ads/spotify-conversions-api-early-access/spotify-conversions-api-reference)
- Related endpoints in Ads API reference
  
  - [Create CAPI Integration](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCapiIntegration)
  - [Get CAPI Integration](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiIntegrationById)
  - [Update CAPI Integration](https://developer.spotify.com/documentation/ads-api/reference/v3.0/updateCapiIntegrationById)
  - [Create CAPI Auth Token](https://developer.spotify.com/documentation/ads-api/reference/v3.0/createCapiAuthToken)
  - [Get CAPI Auth Token](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getCapiAuthTokens)
  - [Delete CAPI Auth Token](https://developer.spotify.com/documentation/ads-api/reference/v3.0/deleteCapiAuthToken)