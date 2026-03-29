---
title: Breakout Rooms · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/breakout-rooms/index.md
source: llms
fetched_at: 2026-01-24T15:36:03.593221459-03:00
rendered_js: false
word_count: 1003
summary: This document provides a comprehensive guide to implementing and managing breakout rooms in RealtimeKit, detailing participant roles, permission configurations, and the use of SDK APIs for meeting orchestration.
tags:
    - breakout-rooms
    - realtimekit
    - meeting-management
    - video-conferencing
    - participant-permissions
    - connected-meetings
category: guide
---

Note

The breakout rooms feature, also known as connected meetings, is currently in beta, which means it is still being tested and evaluated, and may undergo some changes.

Breakout rooms allow participants of a meeting to split into smaller groups for targeted discussions and collaboration. With the rise of remote work and online learning, breakout rooms have become an essential tool for enhancing engagement and building community in virtual settings. They are an ideal choice for workshops, online classrooms, or when you need to speak privately with select participants outside the main meeting.

Note

Breakout rooms are currently supported on web only.

In RealtimeKit, breakout rooms are created as a separate meeting. Each breakout room is an independent meeting and can be managed like any other RealtimeKit meeting. RealtimeKit provides a set of SDK APIs to create, manage, and switch between breakout rooms.

## Key features

The following are some of the key features of RealtimeKit's breakout rooms:

* Manage permissions and privileges of hosts and participants using presets
* Hosts can create breakout rooms, assign participants, start and close the breakout rooms, and switch between rooms
* Participants can start and stop video, interact with other participants using chat and polls, and mute/unmute audio
* Record all breakout sessions individually like any other RealtimeKit meeting

## Roles in a breakout room

Roles in the breakout room are managed by presets.

### Host

Hosts can create breakout rooms, assign participants, start and close the breakout rooms, and switch between rooms.

### Participants

As a participant in a breakout room, you can:

* **Switch to Parent Meeting** - Switch back to the main meeting (if you have the required permissions)
* **Switch Connected Meetings** - Move from the main meeting to smaller, focused discussion groups (breakout rooms) for collaboration
* **Collaborate** - Use tools such as chat and polls during breakout sessions

## Audio and video

Each breakout room functions as an independent meeting. When you switch to a breakout room from the main meeting, it automatically switches to the audio and video of the breakout session. You can mute or unmute your audio and start or stop your video at any time during the breakout session, just as you can in the main meeting.

When the breakout session ends, your audio and video automatically switch back to the main meeting.

* If your video was turned on during a breakout session, it will remain on when you return to the main session
* If your microphone was on during a breakout session, it will stay on when you return to the main session

## Recording breakout sessions

Each breakout session is a separate session. Each breakout session's recording is stored and managed separately, just like any other RealtimeKit meeting. For more information, refer to [Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/).

## Breakout rooms management

Breakout rooms allow the participants to split into separate sessions. The host can create breakout rooms, assign participants, start and close the breakout rooms.

### Create presets

A preset is a set of permissions and UI configurations that are applied to hosts and participants. They determine the look, feel, and behavior of the breakout room.

For breakout rooms, you must provide the following permissions for hosts and participants in Connected Meetings:

#### Host

The host preset should have **Full Access** permission in Connected Meetings. This allows the host to:

* Create breakout rooms
* Assign participants to rooms
* Start and close breakout rooms
* Switch between rooms

#### Participants

You can choose to provide the following permissions to participants:

* **Switch Connected Meetings** - Allows participants to move between breakout rooms
* **Switch to Parent Meeting** - Allows participants to return to the main meeting

### Save the preset

1. Once you have made all the changes to your preset, click **Save**
2. Enter a name for your preset and click **Save**
3. Your preset is listed - click **Edit** to make any changes

### Create a meeting

Create a RealtimeKit meeting using the [Create Meeting API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/). This API returns a unique identifier for your meeting.

### Add participants

After creating the meeting, add each participant using the [Add Participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/). The `presetName` created earlier must be passed in the body of the Add Participant API request.

### Validate permissions

Before creating breakout rooms, validate the permissions of the current participant to ensure that the participant has the required permissions to create breakout rooms. Incorrect permissions can lead to errors being thrown.

### Create breakout rooms

### Retrieve list of breakout rooms and their participants

If there are more than one host in the room creating breakouts, you can retrieve consolidated list of breakout rooms using the following API.

### Move participants to breakout rooms

Once you have created breakout rooms, assign participants to the rooms.

### Move participants, with a specific preset, to breakout rooms

Once you have created breakout rooms, assign participants to the rooms.

### Move local participant to breakout room

To move the local participant to a different breakout room or back to the parent meeting, use the same API as for moving other participants, but pass the local participant's ID. The local participant must have the appropriate permissions: `canSwitchConnectedMeetings` to switch between breakout rooms, or `canSwitchToParentMeeting` to return to the parent meeting, if the request was originated by the non-host local participant.

### Handle breakout room events

If a participant has been moved to a breakout room, the `changingMeeting` event is triggered, followed by the `meetingChanged` event. These events are also triggered when a participant switches between the main meeting and breakout rooms. Participants will autojoin the breakout room if they are assigned to it. You won't have to join meeting explicitly.

### Close breakout rooms

You can close/delete the breakout rooms. This will force participants in those meetings to come to the main room.

## Next steps

You have successfully integrated breakout rooms into your RealtimeKit application. Participants can now:

* Join the main meeting
* Be assigned to breakout rooms by the host
* Switch between the main meeting and breakout rooms
* Collaborate in smaller focused groups

For more advanced customization, explore the following:

* [UI Kit Components Library](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/component-library/) - Browse available components
* [UI Kit States](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/state-management/) - Learn how components synchronize
* [Build Your Own UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/) - Create custom meeting interfaces