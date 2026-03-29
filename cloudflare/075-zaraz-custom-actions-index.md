---
title: Create a third-party tool action · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/custom-actions/index.md
source: llms
fetched_at: 2026-01-24T15:34:50.160547284-03:00
rendered_js: false
word_count: 143
summary: This document explains how to configure actions and triggers in Cloudflare Zaraz to control the behavior and execution of third-party tools.
tags:
    - cloudflare-zaraz
    - custom-actions
    - automatic-actions
    - triggers
    - event-management
category: guide
---

Tools on Zaraz must have actions configured in order to do something. Often, using Automatic Actions is enough for configuring a tool. But you might want to use Custom Actions to create a more customized setup, or perhaps you are using a tool that does not support Automatic Actions. In these cases, you will need to configure Custom Actions manually.

Every action has firing triggers assigned to it. When the conditions of the firing triggers are met, the action will start. An action can be anything the tool can do - sending analytics information, showing a widget, adding a script and much more.

To start using actions, first [create a trigger](https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/) to determine when this action will start. If you have already set up a trigger, or if you are using one of the built-in triggers, follow these steps to [create an action](https://developers.cloudflare.com/zaraz/custom-actions/create-action/).