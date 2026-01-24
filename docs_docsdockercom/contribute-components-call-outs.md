---
title: Callouts
url: https://docs.docker.com/contribute/components/call-outs/
source: llms
fetched_at: 2026-01-24T14:06:32.020484212-03:00
rendered_js: false
word_count: 472
summary: This document explains how to implement and format callouts, alerts, and feature summary bars within documentation using specific markdown syntax and configuration files.
tags:
    - documentation-formatting
    - markdown-syntax
    - callouts
    - alerts
    - summary-bars
    - shortcodes
category: guide
---

Table of contents

* * *

We support these broad categories of callouts:

- Alerts: Note, Tip, Important, Warning, Caution

We also support summary bars, which represent a feature's required subscription, version, or Adminstrator role. To add a summary bar:

Add the feature name to the `/data/summary.yaml` file. Use the following attributes:

AttributeDescriptionPossible values`subscription`Notes the subscription required to use the featureAll, Personal, Pro, Team, Business`availability`Notes what product development stage the feature is inExperimental, Beta, Early Access, GA, Retired`requires`Notes what minimum version is required for the featureNo specific value, use a string to describe the version and link to relevant release notes`for`Notes if the feature is intended for IT AdministratorsAdministrators

Then, add the `summary-bar` shortcode on the page you want to add the summary bar to. Note, the feature name is case sensitive. The icons that appear in the summary bar are automatically rendered.

## [Examples](#examples)

Subscription: Business

Requires: Docker Desktop [4.36](https://docs.docker.com/desktop/release-notes/#4360) and later

For: Administrators

> Note
> 
> Note the way the `get_hit_count` function is written. This basic retry loop lets us attempt our request multiple times if the redis service is not available. This is useful at startup while the application comes online, but also makes our application more resilient if the Redis service needs to be restarted anytime during the app's lifetime. In a cluster, this also helps handling momentary connection drops between nodes.

> Tip
> 
> For a smaller base image, use `alpine`.

> Important
> 
> Treat access tokens like your password and keep them secret. Store your tokens securely (for example, in a credential manager).

> Warning
> 
> Removing Volumes
> 
> By default, named volumes in your compose file are NOT removed when running `docker compose down`. If you want to remove the volumes, you will need to add the `--volumes` flag.
> 
> The Docker Desktop Dashboard does not remove volumes when you delete the app stack.

> Caution
> 
> Here be dragons.

For both of the following callouts, consult [the Docker release lifecycle](https://docs.docker.com/release-lifecycle) for more information on when to use them.

## [Formatting](#formatting)

```
{{< summary-bar feature_name="PKG installer" >}}
```

```
> [!NOTE]
>
> Note the way the `get_hit_count` function is written. This basic retry
> loop lets us attempt our request multiple times if the redis service is
> not available. This is useful at startup while the application comes
> online, but also makes our application more resilient if the Redis
> service needs to be restarted anytime during the app's lifetime. In a
> cluster, this also helps handling momentary connection drops between
> nodes.
> [!TIP]
>
> For a smaller base image, use `alpine`.
> [!IMPORTANT]
>
> Treat access tokens like your password and keep them secret. Store your
> tokens securely (for example, in a credential manager).
> [!WARNING]
>
> Removing Volumes
>
> By default, named volumes in your compose file are NOT removed when running
> `docker compose down`. If you want to remove the volumes, you will need to add
> the `--volumes` flag.
>
> The Docker Desktop Dashboard does not remove volumes when you delete the app stack.
> [!CAUTION]
>
> Here be dragons.
```