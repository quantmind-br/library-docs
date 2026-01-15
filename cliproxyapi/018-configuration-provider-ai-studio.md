---
title: AI Studio Instructions | CLIProxyAPI
url: https://help.router-for.me/configuration/provider/ai-studio
source: crawler
fetched_at: 2026-01-14T22:09:59.39778873-03:00
rendered_js: false
word_count: 173
summary: This document explains how to configure the connection and authentication settings for the CLIProxyAPI service when integrating it with an AI Studio App.
tags:
    - aistudio-app
    - cliproxyapi
    - connection
    - authentication
    - configuration
category: configuration
---

You can use this service as a backend for [this AI Studio App](https://aistudio.google.com/apps/drive/1CPW7FpWGsDZzkaYgYOyXQ_6FWgxieLmL). Follow the steps below to configure it:

1. **Start the CLIProxyAPI Service**: Ensure your CLIProxyAPI instance is running, either locally or remotely.
2. **Access the AI Studio App**: Log in to your Google account in your browser, then open the following link:
   
   - [https://aistudio.google.com/apps/drive/1CPW7FpWGsDZzkaYgYOyXQ\_6FWgxieLmL](https://aistudio.google.com/apps/drive/1CPW7FpWGsDZzkaYgYOyXQ_6FWgxieLmL)

## Connection Configuration [​](#connection-configuration)

By default, the AI Studio App attempts to connect to a local CLIProxyAPI instance at `ws://127.0.0.1:8317`.

- **Connecting to a Remote Service**: If you need to connect to a remotely deployed CLIProxyAPI, modify the `config.ts` file in the AI Studio App to update the `WEBSOCKET_PROXY_URL` value.
  
  - Use the `wss://` protocol if your remote service has SSL enabled.
  - Use the `ws://` protocol if SSL is not enabled.

## Authentication Configuration [​](#authentication-configuration)

By default, WebSocket connections to CLIProxyAPI do not require authentication.

- **Enable Authentication on the CLIProxyAPI Server**: In your `config.yaml` file, set `ws_auth` to `true`.
- **Configure Authentication on the AI Studio Client**: In the `config.ts` file of the AI Studio App, set the `JWT_TOKEN` value to your authentication token.