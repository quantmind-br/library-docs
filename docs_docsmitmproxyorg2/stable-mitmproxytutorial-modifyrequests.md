---
title: Modify Requests
url: https://docs.mitmproxy.org/stable/mitmproxytutorial-modifyrequests/
source: crawler
fetched_at: 2026-01-28T15:10:57.968306884-03:00
rendered_js: false
word_count: 288
summary: This tutorial demonstrates how to modify intercepted HTTP requests in mitmproxy before forwarding them to their destination.
tags:
    - mitmproxy
    - http-interception
    - request-modification
    - cli-tutorial
    - flow-editing
    - network-debugging
    - man-in-the-middle
category: tutorial
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/cli-tutorials/cli-03-modify-requests.md)

In the previous step we resumed intercepted requests without changes. The full power of interceptions comes to play when we modify an intercepted request before forwarding it to its destination. You can continue with the window and the already configured interception rule from the previous step.

Video Content

[Welcome to the mitmproxy tutorial. In this lesson we cover the modification of intercepted requests.  
\
00:00](#)

[We configure and use the same interception rule as in the last tutorial.  
\
00:16](#)

[Press `i` to prepopulate mitmproxy’s command prompt, enter the flow filter `~u /Dunedin & ~q`, and press `ENTER`.  
\
00:22](#)

[Let’s generate a request using `curl` in a separate terminal.  
\
00:40](#)

[We now want to modify the intercepted request.  
\
01:08](#)

[Put the focus (`>>`) on the intercepted flow. This is already the case in our example.  
\
01:12](#)

[Press `ENTER` to open the details view for the intercepted flow.  
\
01:19](#)

[Press `e` to edit the intercepted flow.  
\
01:25](#)

[mitmproxy asks which part to modify.  
\
01:29](#)

[Select `path` by using your arrow keys and press `ENTER`.  
\
01:33](#)

[mitmproxy shows all path components line by line, in our example its just `Dunedin`.  
\
01:41](#)

[Press `ENTER` to modify the selected path component.  
\
01:48](#)

[Replace `Dunedin` with `Innsbruck`.  
\
01:54](#)

[Press `ESC` to confirm your change.  
\
02:04](#)

[Press `q` to go back to the flow details view.  
\
02:08](#)

[Press `a` to resume the intercepted flow.  
\
02:13](#)

[You see that the request URL was modified and `wttr.in` replied with the weather report for `Innsbruck`.  
\
02:19](#)

[In the next lesson you will learn to replay flows.  
\
02:27](#)

In the next lesson, you will learn to replay previous flows.