---
title: Mobile Access via Secure Tunneling | goose
url: https://block.github.io/goose/docs/experimental/mobile-access
source: github_pages
fetched_at: 2026-01-22T22:13:18.826593599-03:00
rendered_js: true
word_count: 324
summary: This document provides instructions for setting up and using the experimental mobile access feature to connect an iOS device to goose Desktop via a secure tunnel.
tags:
    - mobile-access
    - ios-app
    - remote-access
    - secure-tunneling
    - goose-desktop
    - setup-guide
category: guide
---

Mobile access lets you connect to goose remotely from an iOS mobile device using secure tunneling.

Experimental Feature

Mobile access is a preview feature in active development. Behavior and configuration may change in future releases.

## How Mobile Access Works[​](#how-mobile-access-works "Direct link to How Mobile Access Works")

Mobile access connects your iOS device to goose Desktop through a secure tunnel. After you install and configure the **goose AI** app, you can access goose from anywhere.

**Key details:**

- Uses [Lapstone](https://github.com/michaelneale/lapstone-tunnel), a public HTTPS tunnel service provided by Mic Neale
- Easy setup using a QR code with a unique secret key to secure the connection
- Your tunnel URL remains the same across sessions, so you only need to configure your mobile app once
- The connection requires your computer to be awake with goose Desktop running
- Automatically reconnects if interrupted and restarts when you launch goose Desktop

## Setup[​](#setup "Direct link to Setup")

### Install the App[​](#install-the-app "Direct link to Install the App")

1. Install the **goose AI** app on your iOS mobile device from the [App Store](https://apps.apple.com/app/goose-ai/id6752889295)

App Store QR Code

Follow the steps below to open the `Remote Access` section, then click "scan QR code" in the info box for quick access to the App Store.

### Start the Tunnel[​](#start-the-tunnel "Direct link to Start the Tunnel")

1. Open goose Desktop
2. Click the button in the top-left to open the sidebar
3. Click `Settings` in the sidebar
4. Click `App`
5. Scroll down to the `Remote Access` section and click `Start Tunnel`

Once the tunnel starts, you'll see a `Remote Access Connection` QR code for configuring the app.

info

Click `Stop Tunnel` at any time to close the connection.

### Connect the App[​](#connect-the-app "Direct link to Connect the App")

1. Open the **goose AI** app on your iOS mobile device
2. Scan the `Remote Access Connection` QR code displayed in goose Desktop
3. The app will automatically configure the connection

You can now access goose Desktop from your mobile device.

## What You Can Do[​](#what-you-can-do "Direct link to What You Can Do")

The mobile app gives you full access to goose:

- Start new conversations or continue existing sessions
- Use all your goose extensions and configurations
- Work from anywhere while your computer handles the processing

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")