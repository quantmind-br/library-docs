---
title: Stage Management · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/index.md
source: llms
fetched_at: 2026-01-24T15:36:17.981780127-03:00
rendered_js: false
word_count: 536
summary: This document explains how to use Cloudflare RealtimeKit's stage management APIs to control participant media publishing and permissions in webinar scenarios.
tags:
    - cloudflare-realtimekit
    - webrtc
    - stage-management
    - webinar-apis
    - host-controls
    - participant-permissions
category: guide
---

This guide explains how to use stage management APIs for Webinar (WebRTC) use cases in Cloudflare RealtimeKit.

Instead of a traditional publish-subscribe model, where a user can publish their media and others can choose to subscribe, RealtimeKit comes with an optional managed configuration. In this managed configuration, a less privileged user can be configured with a default behavior to not publish media. The user can then request permission to be allowed to publish their media, where a privileged user can choose to grant or deny access.

Using RealtimeKit's stage management APIs, a user can perform actions such as:

* Leave and join stage
* Manage stage requests and permissions
* Kick participants

## Access the Stage APIs

The stage module can be accessed under the `meeting.stage` namespace.

## Properties

### Status

The `meeting.stage.status` property returns the current stage status of the local user.

**Possible status values:**

* **`ON_STAGE`** - The user is currently on the stage and sharing audio and video.
* **`OFF_STAGE`** - The user is viewing the session but is not on the stage and is not sharing audio or video.
* **`REQUESTED_TO_JOIN_STAGE`** - The user has a pending request to join the stage and share audio and video. This status remains until the host accepts or rejects the request.
* **`ACCEPTED_TO_JOIN_STAGE`** - The host has accepted the user's request to join the stage.

Note

A user with permission to join stage directly can only assume `ON_STAGE` and `ACCEPTED_TO_JOIN_STAGE` status values.

## Host Controls

RealtimeKit's stage management APIs allow hosts to receive and manage stage requests as well as leave and join the stage.

### Join Stage

This method connects the user to the media room, enabling them to interact with other peers in the meeting.

### Leave Stage

By employing this method, the user will be disconnected from the media room and subsequently unable to communicate with their peers. Additionally, their audio and video will no longer be visible to others in the room.

### Grant Access

A privileged user can grant access to stage for a set of users with the `grantAccess` method.

**Parameters:**

### Deny Access

A privileged user can deny access to stage for a set of users with the `denyAccess` method.

**Parameters:**

### Kick Users

A privileged user can remove a set of users from stage using the `kick` method.

**Parameters:**

## Participant Controls

RealtimeKit's stage management APIs allow participants to request and manage stage access.

### Request Access

This method is used to create a new stage request which can be approved by the host. Each user (viewer or host) must call this method in order to join the stage.

When the host calls this method, their status will be updated to `ACCEPTED_TO_JOIN_STAGE`.

### Cancel Access Request

You can call this method to cancel your stage request.

## Events

The `meeting.stage` module emits the following events:

### Stage Access Requests Updated

Emitted when there is an update to stage access requests.

### Stage Access Request Accepted

Emitted when the host accepts the join stage request or invites a user directly to stage.

### Stage Status Updated

Emitted when the local user's stage status changes.

### New Stage Request

Emitted when a new participant requests to join the stage.

### Stage Request Approved

Emitted when a stage request is approved by the host.

### Stage Request Rejected

Emitted when the host rejects a stage request.