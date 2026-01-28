---
title: Intercept Requests
url: https://docs.mitmproxy.org/stable/mitmproxytutorial-interceptrequests/
source: crawler
fetched_at: 2026-01-28T15:58:54.73950668-03:00
rendered_js: false
word_count: 122
summary: Tutorial demonstrating how to intercept and modify HTTP requests using browser developer tools and programming techniques.
tags:
    - network
    - developer-tools
    - debugging
    - request-interception
    - browser
    - http
category: tutorial
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/cli-tutorials/cli-02-intercept-requests.md)

A powerful feature of mitmproxy is the interception of requests. An intercepted request is paused so that the user can modify (or discard) the request before sending it to the server. mitmproxy’s `set intercept` command configures interceptions. The command is bound to shortcut `i` by default.

Intercepting *all* requests is usually not desired as it constantly interrupts your browsing. Thus, mitmproxy expects a [flow filter expression](https://docs.mitmproxy.org/stable/concepts/filters/) as the first argument to `set intercept` to selectively intercept requests. In the tutorial below we use the flow filter `~u <regex>` that filters flows by matching the regular expressing on the URL of the request.

In the next lesson, you will learn to modify intercepted flows before sending them to the server.