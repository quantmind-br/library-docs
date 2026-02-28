---
title: Ads API Quickstart | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/quick-start
source: crawler
fetched_at: 2026-02-27T23:39:26.230372-03:00
rendered_js: true
word_count: 598
summary: This document provides step-by-step instructions for setting up, initializing, and authenticating an application with the Spotify Ads API using OAuth 2.0. It covers prerequisites, obtaining access tokens, and managing refresh tokens to ensure persistent API connectivity.
tags:
    - spotify-ads-api
    - oauth-authentication
    - access-token
    - refresh-token
    - ads-manager
    - api-setup
category: guide
---

## Account prerequisites

The Spotify Ads API uses [OAuth](https://oauth.net/2/) for authentication and access. Your API client will need an access token and secret before making API calls. Make sure you have the following before proceeding:

1. A valid [Spotify account](https://www.spotify.com/us/signup) depending on your usage (e.g. personal development, work, etc.).
2. A valid [Ads Manager account](https://adsmanager.spotify.com/signup/form).

## Initialize your new Ads API application

Setting up your Ads API app is a one-time process. Follow these steps to get started:

1. Create an application at [developer.spotify.com](https://developer.spotify.com/) to get a client ID and client secret (check out the [App Settings page](https://developer.spotify.com/documentation/web-api/concepts/apps) for a bit more on this). The client ID will be referred to as `<CLIENT_ID>` in further steps below.
2. Configure a redirect URI for the application (e.g., `http://127.0.0.1:8080/callback`). This will be referred to as `<REDIRECT_URI>` in further steps below.
3. Select "Ads API" for the question asking which APIs are you planning to use
4. Accept the API Terms with your client ID in [Ads Manager](https://adsmanager.spotify.com/api-terms). NOTE: It can take up to one hour for your client ID to be allowlisted once you have signed the terms.

## Authenticate your Ads Manager account

Account authentication is the next step after you set up your application. Follow these steps to get started:

1. In a web browser, copy the URL below into the address bar. Replace your client ID and properly escaped redirect URI with the values you registered with the app.
   
   `https://accounts.spotify.com/authorize/?client_id=<CLIENT_ID>&response_type=code&redirect_uri=<REDIRECT_URI>`
   
   I.e., concretely, in the URL, replace:
   
   - `<CLIENT_ID>` with your client ID.
   - `<REDIRECT_URI>` with your callback URL.
   
   After you replace the values, navigate to that URL
2. Log in your Spotify account and authorize your application. Clicking **Login** returns a 404 error, but that’s ok.
3. Check the browser address bar for the parameter `code=XXXXXXXX`. The Xs are placeholders for your access code. The access code is valid for 10 minutes. Save the code for Step 5.
4. Open a terminal window and run the command shown below. In this command, replace `<CLIENT_ID>` and `<CLIENT_SECRET>` with your real client ID and secret. Save the output for Step 5.
   
   `echo -n <CLIENT_ID>:<CLIENT_SECRET> | base64`
5. Run the command shown below to generate an access token. A valid token is required to make API requests.
   
   `1`
   
   `curl -H "Authorization: Basic <BASE64_OUTPUT_FROM_STEP_4>" \`
   
   `2`
   
   `-d grant_type=authorization_code \`
   
   `3`
   
   `-d code=<CODE_FROM_STEP_3> \`
   
   `4`
   
   `-d redirect_uri=<REDIRECT_URI> \`
   
   `5`
   
   `https://accounts.spotify.com/api/token`
   
   In this command, replace:
   
   - `<BASE64_OUTPUT_FROM_STEP_4>` with the code from Step 4.
   - `<CODE_FROM_STEP_3>` with the code from Step 3.
   - `<REDIRECT_URI>` (after `redirect_uri=`) with your callback URL.

### Authentication results

You should now see a response that looks similar to this:

`1`

`{`

`2`

`"access_token": "XXXXXXXXXXXXX",`

`3`

`"token_type": "Bearer",`

`4`

`"expires_in": 3600,`

`5`

`"refresh_token": "XXXXXXXXXXXX",`

`6`

`"scope": ""`

`7`

`}`

The access (bearer) token give you access to the API endpoints for 1 hour. Save the *refresh* token in a safe place.

## Using the refresh token

Your refresh token is used to request new, short lived access tokens.

Run the following command in a terminal window when you need to renew API access with your refresh token:

`1`

`curl -H "Authorization: Basic <BASE64_OUTPUT_FROM_STEP_4>" \`

`2`

`-d grant_type=refresh_token \`

`3`

`-d refresh_token=<REFRESH_TOKEN_FROM_RESULTS> \`

`4`

`https://accounts.spotify.com/api/token`

In this command, replace:

- `<BASE64_OUTPUT_FROM_STEP_4>` with the output from Step 4 above.
- `<REFRESH_TOKEN_FROM_RESULTS>` with the value of the refresh token returned by the response shown in the Authentication Results section above.

The refresh operation above outputs a new short-lived access token, which you can now use to make API requests as shown below:

`1`

`curl --request GET \`

`2`

`--url https://api-partner.spotify.com/ads/v3/businesses \`

`3`

`--header 'Authorization: Bearer <ACCESS_TOKEN>'`

In this command, replace:

- `<ACCESS_TOKEN>` with the value of the access token returned by the response in the section above.