---
title: Plex
url: https://coolify.io/docs/services/plex.md
source: llms
fetched_at: 2026-02-17T14:47:16.246374-03:00
rendered_js: false
word_count: 68
summary: This document provides instructions for installing and configuring the Plex Media Server within the Coolify platform, including steps for using claim tokens and hardware transcoding.
tags:
    - plex
    - coolify
    - media-server
    - self-hosting
    - installation-guide
    - transcoding
category: guide
---

## What is Plex?

Available on almost any device, Plex is the first-and-only streaming platform to offer free ad-supported movies, shows, and live TV together.

## Installation

1. Create the service within Coolify.
2. BEFORE starting the service, set the `PLEX_CLAIM` variable. You can get a claim token here: https://plex.tv/claim
3. If your device supports it, enable hardware transcoding by uncommenting this section in the compose file:

```yaml
#devices:
# - "/dev/dri:/dev/dri"
```

## Screenshots

## Links

* [The official website](https://www.plex.tv/)
* [GitHub](https://github.com/plexinc/pms-docker)