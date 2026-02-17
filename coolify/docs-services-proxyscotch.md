---
title: Proxyscotch
url: https://coolify.io/docs/services/proxyscotch.md
source: llms
fetched_at: 2026-02-17T14:47:29.027266-03:00
rendered_js: false
word_count: 176
summary: This document provides setup and configuration instructions for Proxyscotch, an open-source CORS proxy designed for self-hosted Hoppscotch instances.
tags:
    - proxyscotch
    - hoppscotch
    - cors-proxy
    - self-hosting
    - configuration-guide
    - environment-variables
category: guide
---

# Proxyscotch

## What is Proxyscotch

Tiny open-source CORS proxy made by Hoppscotch.

> Works well with Hoppscotch, but can be used standalone as well.

## Setup Instructions

> This is only needed for when setting up Proxyscotch for a selfhosted instance of Hoppscotch.

If you secure your proxy server ***(recommended & enabled by default)*** you will need to set some ENV vars for your Hoppscotch instance.

##### After you've set up your Proxyscotch instance:

* Go and find the token that Coolify generated for you.

* In the settings for your Hoppscotch instance on coolify, go to **Environment Variables**

* Add a new variable called `VITE_PROXYSCOTCH_ACCESS_TOKEN` and set it to the token you found before.

* Restart the Hoppscotch instance.

* Once it restarts, load the webui & navigate to **Settings > Interceptors**. - Then scroll down to **Proxy**

* Set the proxy URL to the URL of your Proxyscotch instance

> You might have to enable the Proxy via the switch in the dashboard first before you can modify the URL.

You should now have Hoppscotch set-up & working with your own CORS proxy!

## Links

* [Official Documentation](https://github.com/hoppscotch/proxyscotch?utm_source=coolify.io)