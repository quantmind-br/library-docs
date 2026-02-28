---
title: Quota modes | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/concepts/quota-modes
source: crawler
fetched_at: 2026-02-27T23:38:15.790813-03:00
rendered_js: true
word_count: 579
summary: This document explains the two application states for Spotify developers, detailing the limitations of development mode and the eligibility requirements for transitioning to extended quota mode.
tags:
    - spotify-api
    - development-mode
    - extended-quota
    - quota-limits
    - app-management
    - developer-dashboard
    - allowlisting
category: guide
---

The quota mode refers to the mode in which an app can be: **development mode** or **extended quota mode**.

You can check the current mode of your app by checking the *App Status* value in the *App Settings*:

![App status](https://developer-assets.spotifycdn.com/images/documentation/web-api/appstatus.png)

## Development mode

Newly-created apps begin in **development mode**. This mode is perfect for apps that are under construction and apps that have been built for accessing or managing data in a single Spotify account.

**Note:** The app owner must have a Spotify Premium account for apps in development mode to function.

Up to 5 authenticated Spotify users can use an app that is in development mode — so you can share your app with beta testers, friends, or with fellow developers who are working on the app. Each Spotify user who installs your app will need to be added to your app's allowlist before they can use it.

### Adding a user to your app's allowlist

Allow another user to use your development mode app by following these steps:

1. Log in to the [Developer Dashboard](https://developer.spotify.com/dashboard)
2. Tap on the name of your app
3. Tap on the *Settings* button
4. Tap on the *Users Management* tab ![Users and Access](https://developer-assets.spotifycdn.com/images/documentation/web-api/users-and-access.png)
5. Tap on the *Add new user* button and enter the name and Spotify email address of the user that you want to enable to use your app
6. Invite the new user to install and use your app

Users may be able to log into a development mode app without having been allowlisted by the developer. However, API requests with an access token associated to that user and app will receive a 403 status code error

## Extended quota mode

Extended quota mode is for Spotify apps that are ready for a wider audience. Apps in this category can be installed by an unlimited number of users and the allowlist in development mode no longer applies. Extended quota mode apps also have access to a higher [rate limit](https://developer.spotify.com/documentation/web-api/concepts/rate-limits) than development mode apps do.

### Quota Extension Request for New Potential Partners

Please note that as of May 15th 2025, Spotify only accepts applications only from organizations (not individuals). For more information on this update, read [here](https://developer.spotify.com/blog/2025-04-15-updating-the-criteria-for-web-api-extended-access).

Application must be sent through a company email **by using [this form](https://docs.google.com/forms/d/1O87xdPP1zWUDyHnduwbEFpcjA57JOaefCgBShKjAqlo)**. Check out the implementation requirements below to make sure your company is compatible before submitting your application.

Implementation requirements:

1. Established Business Entity (legally registered business or organisation)
2. Operating an active, and Launched Service
3. Maintaining a minimum of active users (at least 250k MAUs)
4. Being available in key Spotify markets
5. Commercial Viability
6. Adherence to Terms

### Moving from development mode into extended quota mode

If your Partner Application form is approved, you can ask Spotify to move your app from development mode into extended quota mode. Spotify's app review team will take a look at your app and evaluate it for compliance with our [Developer Policy](https://developer.spotify.com/policy).

1. Log in to the [Developer Dashboard](https://developer.spotify.com/dashboard)
2. Tap on the name of your app
3. Tap on the *Settings* button
4. Tap on the *Quota extension Request* tab ![Request Extension link](https://developer-assets.spotifycdn.com/images/documentation/web-api/request-a-quota-extension.png)
5. Tell us about your app by filling out the provided questionnaire (4 steps)
6. Tap Submit

When you have successfully submitted your app for review you should see the word 'Sent' in blue on your app detail page. The app review team will review the information that you have provided, test out your app and send you feedback by email, to the email address associated with your Spotify account. This review process can take up to six weeks.