---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/get-a-users-available-devices
source: crawler
fetched_at: 2026-02-27T23:38:44.857099-03:00
rendered_js: true
word_count: 163
summary: This document provides reference information for the Spotify Web API endpoint that retrieves a list of the user's available Spotify Connect devices and their current status.
tags:
    - spotify-api
    - web-api
    - player-api
    - spotify-connect
    - device-management
category: api
---

Web API •References / Player / Get Available Devices

## Get Available Devices

Get information about a user’s available Spotify Connect devices. Some device models are not supported and will not be listed in the API response.

## Request

## Response

A set of devices

- - The device ID. This ID is unique and persistent to some extent. However, this is not guaranteed and any cached `device_id` should periodically be cleared out and refetched as necessary.
  - If this device is the currently active device.
  - is\_private\_sessionboolean
    
    If this device is currently in a private session.
  - Whether controlling this device is restricted. At present if this is "true" then no Web API commands will be accepted by this device.
  - A human-readable name for the device. Some devices have a name that the user can configure (e.g. "Loudest speaker") and some devices have a generic name associated with the manufacturer or device model.
    
    Example: `"Kitchen speaker"`
  - Device type, such as "computer", "smartphone" or "speaker".
    
    Example: `"computer"`
  - The current volume in percent.
    
    Range: `0` - `100`Example: `59`
  - If this device can be used to set the volume.

## Response sample

```
{"devices": [{"id": "string","is_active": false,"is_private_session": false,"is_restricted": false,"name": "Kitchen speaker","type": "computer","volume_percent": 59,"supports_volume": false}]}
```