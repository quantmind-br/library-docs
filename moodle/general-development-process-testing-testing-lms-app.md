---
title: Testing LMS issues in the mobile app | Moodle Developer Resources
url: https://moodledev.io/general/development/process/testing/testing-lms-app
source: sitemap
fetched_at: 2026-02-17T16:00:44.496395-03:00
rendered_js: false
word_count: 277
summary: This document explains how to install and access the Moodle mobile app using various platforms and methods to facilitate the testing of LMS issues and local site developments.
tags:
    - moodle-app
    - mobile-testing
    - lms-development
    - app-installation
    - docker
    - testing-environment
category: guide
---

## Introduction[​](#introduction "Direct link to Introduction")

There are several ways an LMS issue (integrated or in development on your local site) can be tested using the Moodle mobile app.

In some cases, it might be necessary to use ngrok to expose your site to the Internet.

## Different ways the Moodle mobile app can be installed or accessed[​](#different-ways-the-moodle-mobile-app-can-be-installed-or-accessed "Direct link to Different ways the Moodle mobile app can be installed or accessed")

### Installation in a mobile device via Google Play or Apple App store[​](#installation-in-a-mobile-device-via-google-play-or-apple-app-store "Direct link to Installation in a mobile device via Google Play or Apple App store")

This is the most common way, just install the app on your mobile device and connect to your local development site using ngrok or using its local network IP address.

### Windows 11 or macOS (Apple silicon)[​](#windows-11-or-macos-apple-silicon "Direct link to Windows 11 or macOS (Apple silicon)")

Android apps can be installed on Windows 11, it will require you to install the Amazon Appstore application (so the Android subsystem is installed) and then follow any guide on the internet such as [this one](https://www.androidauthority.com/how-to-run-android-apps-on-windows-11-3048569/). The .apk version of the app is [downloadable here](https://download.moodle.org/mobile).

For macOS (Apple silicon only) follow [this guideline](https://www.macrumors.com/how-to/install-any-ios-app-m1-mac/).

### Hosted version (aka webapp)[​](#hosted-version-aka-webapp "Direct link to Hosted version (aka webapp)")

In a [Chromium-based browser](https://moodledev.io/general/app/development/setup/app-in-browser) (launched with special flags that disable the web security), you can access your site using the hosted versions of the app in [latest.apps.moodledemo.net](https://latest.apps.moodledemo.net) (the latest stable version) and [main.apps.moodledemo.net](https://main.apps.moodledemo.net) (development version).

Once installed, to connect to your local site you can use its local ip address or hostname (localhost should work).

### Docker images[​](#docker-images "Direct link to Docker images")

[Moodle HQ](https://moodle.com/) provides a couple of Docker images that contain the Moodle App ready for use. You can search all the available versions in [Docker Hub](https://hub.docker.com/r/moodlehq/moodleapp/tags).

Please check this [document for details](https://moodledev.io/general/app/development/setup/docker-images).

Once installed and running, to connect to your local site you can use its local ip address or hostname (localhost should work).

## See also[​](#see-also "Direct link to See also")

- [Debugging network requests in the Moodle App](https://moodledev.io/general/app/development/network-debug)