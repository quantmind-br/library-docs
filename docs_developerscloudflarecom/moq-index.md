---
title: Overview · Cloudflare MoQ docs
url: https://developers.cloudflare.com/moq/index.md
source: llms
fetched_at: 2026-01-24T15:16:45.937301426-03:00
rendered_js: false
word_count: 242
summary: This document provides an overview of Cloudflare's implementation of the Media over QUIC (MoQ) protocol, including current specification support, browser compatibility details, and known technical discrepancies.
tags:
    - moq
    - media-over-quic
    - quic-transport
    - webtransport
    - cloudflare
    - live-streaming
category: reference
---

MoQ (Media over QUIC) is a protocol for delivering live media content using QUIC transport. It provides efficient, low-latency media streaming by leveraging QUIC's multiplexing and connection management capabilities.

MoQ is designed to be an Internet infrastructure level service that provides media delivery to applications, similar to how HTTP provides content delivery and WebRTC provides real-time communication.

Cloudflare's implementation of MoQ currently supports a subset of the [draft-07 MoQ Transport specfication](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-07).

For the most up-to-date documentation on the protocol, please visit the IETF working group documentation.

## Frequently Asked Questions

* What about Safari?

  Safari does not yet have fully functional WebTransport support. Apple never publicly commits to timelines for new features like this. However, Apple has indicated their [intent to support WebTransport](https://github.com/WebKit/standards-positions/issues/18#issuecomment-1495890122). An Apple employee is even a co-author of the [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/) draft. Since Safari 18.4 (2025-03-31), an early (not yet fully functional) implementation of the WebTransport API has been available for testing behind a developer-mode / advanced settings feature flag (including on iOS).

  Until Safari has a fully functional WebTransport implementation, some MoQ use cases may require a fallback to WebRTC, or, in some cases, WebSockets.

## Known Issues

* Extra Subgroup header field

  The current implementation includes a `subscribe_id` field in Subgroup Headers which [`draft-ietf-moq-transport-07`](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-07) omits.

  In section 7.3.1, `draft-ietf-moq-transport-07` [specifies](https://www.ietf.org/archive/id/draft-ietf-moq-transport-07.html#section-7.3.1):

  ```txt
  STREAM_HEADER_SUBGROUP Message {
    Track Alias (i),
    Group ID (i),
    Subgroup ID (i),
    Publisher Priority (8),
  }
  ```

  Whereas our implementation expects and produces:

  ```txt
  STREAM_HEADER_SUBGROUP Message {
    Subscribe ID (i),
    Track Alias (i),
    Group ID (i),
    Subgroup ID (i),
    Publisher Priority (8),
  }
  ```

  This was erroroneously left over from a previous draft version and will be fixed in a future release. Thank you to [@yuki-uchida](https://github.com/yuki-uchida) for reporting.