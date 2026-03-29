---
title: Calendar Integration | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/calendar-integration
source: sitemap
fetched_at: 2026-01-24T13:35:21.36871641-03:00
rendered_js: false
word_count: 131
summary: This document provides instructions for synchronizing CalDAV-compatible calendars with a dashboard using vdirsyncer and khal on Linux systems. It covers installation, account configuration, automated sync scheduling, and troubleshooting common authentication issues.
tags:
    - calendar-sync
    - caldav
    - vdirsyncer
    - khal
    - dashboard-integration
    - linux-configuration
category: guide
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

Sync your CalDAV-compatible calendar (Google Calendar, Office365, etc.) for dashboard integration.

warning

Setting up khal and vdirsyncer is very user-unfriendly and convoluted, in a future release this integration will be replaced with DankCalendar.

tip

Fore more details, view the [khal](https://khal.readthedocs.io/en/latest/) documentation directly. DMS will automatically pick up khal events once configured.

## Installation[​](#installation "Direct link to Installation")

Install the required dependencies for calendar synchronization:

### Arch & Derivatives[​](#arch--derivatives "Direct link to Arch & Derivatives")

```
sudo pacman -S vdirsyncer khal python-aiohttp-oauthlib
```

### Fedora & Derivatives[​](#fedora--derivatives "Direct link to Fedora & Derivatives")

```
sudo dnf install python3-vdirsyncer khal python3-aiohttp-oauthlib
```

## Configuration[​](#configuration "Direct link to Configuration")

### 1. Configure vdirsyncer[​](#1-configure-vdirsyncer "Direct link to 1. Configure vdirsyncer")

Create `~/.vdirsyncer/config`:

```
[general]
status_path = "~/.calendars/status"

[pair personal_sync]
a = "personal"
b = "personallocal"
collections = ["from a", "from b"]
conflict_resolution = "a wins"
metadata = ["color"]

[storage personal]
type = "google_calendar"
token_file = "~/.vdirsyncer/google_calendar_token"
client_id = "your_client_id"
client_secret = "your_client_secret"

[storage personallocal]
type = "filesystem"
path = "~/.calendars/Personal"
fileext = ".ics"
```

### 2. Initial Sync[​](#2-initial-sync "Direct link to 2. Initial Sync")

Run the initial synchronization and configure khal:

```
vdirsyncer sync
khal configure
```

### 3. Auto-sync (Optional)[​](#3-auto-sync-optional "Direct link to 3. Auto-sync (Optional)")

Set up automatic synchronization every 5 minutes using cron:

Add the following line:

```
*/5 * * * * /usr/bin/vdirsyncer sync
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Calendar not syncing[​](#calendar-not-syncing "Direct link to Calendar not syncing")

Check vdirsyncer credentials and network connectivity:

### Missing calendar events[​](#missing-calendar-events "Direct link to Missing calendar events")

Verify khal is configured correctly:

### Authentication issues[​](#authentication-issues "Direct link to Authentication issues")

For Google Calendar, ensure your OAuth client ID and secret are correct. You may need to re-authenticate:

```
rm ~/.vdirsyncer/google_calendar_token
vdirsyncer sync
```