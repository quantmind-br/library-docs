---
title: Replay Requests
url: https://docs.mitmproxy.org/stable/mitmproxytutorial-replayrequests/
source: crawler
fetched_at: 2026-01-28T15:10:59.386671459-03:00
rendered_js: false
word_count: 89
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/cli-tutorials/cli-04-replay-requests.md)

Another powerful feature of mitmproxy is replaying previous flows. Two types of replays are supported:

- **Client-side Replay:** mitmproxy replays previous client requests, i.e., sends the same request to the server again.
- **Server-side Replay:** mitmproxy replays server responses for requests that match an earlier recorded request.

In this tutorial we focus on the more common use case of client-side replays. See the docs for more info on [server-side replay](https://docs.mitmproxy.org/stable/overview/features/#server-side-replay).

You are almost done with this tutorial. In the last step you find more mitmproxy-related resources to discover.