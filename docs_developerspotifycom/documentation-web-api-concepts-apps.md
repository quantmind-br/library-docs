---
title: Apps | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/concepts/apps
source: crawler
fetched_at: 2026-02-27T23:37:53.296838-03:00
rendered_js: true
word_count: 418
summary: This document provides instructions for registering and configuring an application on the Spotify Developer Dashboard to obtain essential credentials like the Client ID and Client Secret. It covers setting up app details, managing redirect URIs for various platforms, and configuring application settings.
tags:
    - spotify-developer-dashboard
    - app-registration
    - client-id
    - client-secret
    - redirect-uri
    - app-configuration
    - authorization-flow
category: guide
---

The app provides, among others, the *Client ID* and *Client Secret* needed to implement any of the authorization flows.

To do so, go to your [Dashboard](https://developer.spotify.com/dashboard) and click on the *Create an App* button to open the following dialog box:

![Create App Dialog](https://developer-assets.spotifycdn.com/images/documentation/web-api/createappdialog.png)

Enter an *App Name* and *App Description* of your choice (they will be displayed to the user on the grant screen), put a tick in the *Developer Terms of Service* checkbox and finally click on *CREATE*. Your application is now registered, and you'll be redirected to the app overview page.

![App Overview](https://developer-assets.spotifycdn.com/images/documentation/web-api/app_overview.png)

The app overview page provides access to different elements:

- App metrics, such as daily and monthly active users or number of users per country. Note that the metrics are initially empty.
- App Status. By default, your app will be in *Development Mode* with limits on the number of users who can install it, and the number of API requests it can make. Note that you can request an extension of this quota if needed by clicking on the *Request Extension* link.
- App settings.
- Client ID, the unique identifier of your app.
- Client Secret, the key you will use to authorize your Web API or SDK calls.

It is time to configure our app. Click on *Edit Settings* to view and update your app settings. The following dialog will show up:

![Dashboard Settings](https://developer-assets.spotifycdn.com/images/documentation/web-api/dashboardeditsettings.png)

- Add a web domain or URL to the *Website* field. This will help users to obtain more information about your application.
- In *Redirect URIs* enter one or more addresses that you want to allowlist with Spotify. This URI enables the Spotify authentication service to automatically invoke your app every time the user logs in (e.g. [http://127.0.0.1:8080](http://127.0.0.1:8080))
  
  Note that on iOS apps, the redirect URI must follow these rules:
  
  - All the characters are lowercase.
  - The prefix *must* be unique to your application (It cannot be a general prefix like http).
  - The prefix must only be used by your application for authenticating Spotify. If you already have a URL scheme handled by your application for other uses, do not reuse it.
  - Include a path after the first pair of forward slashes.
  
  For example: If your app name is *My Awesome App*, a good candidate for the redirect URI could be `my-awesome-app-login://callback`.
- If you are developing an Android or iOS app, fill out the *Android Package* or *Bundle IDs* respectively.

Once you have finished updating the app settings, click on *SAVE*.

Finally, you can delete your app by clicking on the *DELETE* red button.