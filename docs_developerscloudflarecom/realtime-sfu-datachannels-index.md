---
title: DataChannels · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/sfu/datachannels/index.md
source: llms
fetched_at: 2026-01-24T15:37:03.819109005-03:00
rendered_js: false
word_count: 335
summary: This document explains how Cloudflare Realtime DataChannels facilitate low-latency transfer of arbitrary data from a publisher to multiple subscribers. It covers implementation steps and the unidirectional nature of the architecture.
tags:
    - webrtc
    - datachannels
    - cloudflare-realtime
    - sfu
    - real-time-data
    - pub-sub
category: guide
---

DataChannels are a way to send arbitrary data, not just audio or video data, between client in low latency. DataChannels are useful for scenarios like chat, game state, or any other data that doesn't need to be encoded as audio or video but still needs to be sent between clients in real time.

While it is possible to send audio and video over DataChannels, it's not optimal because audio and video transfer includes media specific optimizations that DataChannels do not have, such as simulcast, forward error correction, better caching across the Cloudflare network for retransmissions.

```mermaid
graph LR
    A[Publisher] -->|Arbitrary data| B[Cloudflare Realtime SFU]
    B -->|Arbitrary data| C@{ shape: procs, label: "Subscribers"}
```

DataChannels on Cloudflare Realtime can scale up to many subscribers per publisher, there is no limit to the number of subscribers per publisher.

### How to use DataChannels

1. Create two Realtime sessions, one for the publisher and one for the subscribers.
2. Create a DataChannel by calling /datachannels/new with the location set to "local" and the dataChannelName set to the name of the DataChannel.
3. Create a DataChannel by calling /datachannels/new with the location set to "remote" and the sessionId set to the sessionId of the publisher.
4. Use the DataChannel to send data from the publisher to the subscribers.

### Unidirectional DataChannels

Cloudflare Realtime SFU DataChannels are one way only. This means that you can only send data from the publisher to the subscribers. Subscribers cannot send data back to the publisher. While regular MediaStream WebRTC DataChannels are bidirectional, this introduces a problem for Cloudflare Realtime because the SFU does not know which session to send the data back to. This is especially problematic for scenarios where you have multiple subscribers and you want to send data from the publisher to all subscribers at scale, such as distributing game score updates to all players in a multiplayer game.

To send data in a bidirectional way, you can use two DataChannels, one for sending data from the publisher to the subscribers and one for sending data the opposite direction.

## Example

An example of DataChannels in action can be found in the [Realtime Examples github repo](https://github.com/cloudflare/calls-examples/tree/main/echo-datachannels).