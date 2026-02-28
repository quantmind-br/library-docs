---
title: Application Fingerprints | Spotify for Developers
url: https://developer.spotify.com/documentation/android/tutorials/application-fingerprints
source: crawler
fetched_at: 2026-02-27T23:42:00.382794-03:00
rendered_js: true
word_count: 227
summary: This document provides instructions on how to generate SHA1 fingerprints for Android applications and register them in the Spotify Developer Dashboard for authentication.
tags:
    - android
    - spotify-api
    - authentication
    - sha1-fingerprint
    - app-registration
    - keytool
category: guide
---

Fingerprints are used for authentication between your Android Application and the Spotify service. You'll need to generate a fingerprint for your app and register it in your [Dashboard](https://developer.spotify.com/dashboard).

## Create a Development Fingerprint

1. Run the following command in your Terminal and add a password when required:
   
   `1`
   
   `# On Bash style shells`
   
   `2`
   
   `$ keytool -alias androiddebugkey -keystore ~/.android/debug.keystore -list -v | grep SHA1`
   
   `3`
   
   `4`
   
   `# On Windows Powershell`
   
   `5`
   
   `$ keytool -alias androiddebugkey -keystore %HOMEPATH%\.android\debug.keystore -list -v | grep SHA1`
   
   You should receive a fingerprint that looks like this: `SHA1: E7:47:B5:45:71:A9:B4:47:EA:AD:21:D7:7C:A2:8D:B4:89:1C:BF:75`
2. Copy the fingerprint and your package name and enter it in the Spotify Developer Dashboard, under the "Edit settings" section. Don't forget to click **Save** after you add the fingerprint.
   
   ![Android Packages](https://developer-assets.spotifycdn.com/images/documentation/android/AndroidPackages.png)

## Create a Release Fingerprint

The development and production versions of your application usually have different certificates for security reasons.

1. Run the following command in your Terminal (no password):
   
   `1`
   
   `# On Bash style shells`
   
   `2`
   
   `$ keytool -alias <RELEASE_KEY_ALIAS> -keystore <RELEASE_KEYSTORE_PATH> -list -v | grep SHA1`
   
   `3`
   
   `4`
   
   `# On Windows Powershell`
   
   `5`
   
   `$ keytool -alias <RELEASE_KEY_ALIAS> -keystore <RELEASE_KEYSTORE_PATH> -list -v | grep SHA1`
   
   You should receive a fingerprint that looks like this: `SHA1: E7:47:B5:45:71:A9:B4:47:EA:AD:21:D7:7C:A2:8D:B4:89:1C:BF:75`
2. Copy the fingerprint and your package name and enter it in the Spotify Developer Dashboard. Don't forget to click **Save** after you added the fingerprints in the dashboard.