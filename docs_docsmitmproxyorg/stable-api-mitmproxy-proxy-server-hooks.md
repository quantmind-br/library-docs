---
title: mitmproxy.proxy.server_hooks
url: https://docs.mitmproxy.org/stable/api/mitmproxy/proxy/server_hooks.html
source: crawler
fetched_at: 2026-01-28T15:01:15.0611997-03:00
rendered_js: false
word_count: 31
summary: This document defines various dataclass hooks for handling client and server connection events in mitmproxy.
tags:
    - mitmproxy
    - connection-events
    - dataclass
    - server-hooks
    - client-hooks
category: reference
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/proxy/server_hooks.py) View Source

```
 1fromdataclassesimport dataclass
 2
 3from.import commands
 4frommitmproxyimport connection
 5
 6
 7@dataclass
 8classClientConnectedHook(commands.StartHook):
 9"""
10    A client has connected to mitmproxy. Note that a connection can
11    correspond to multiple HTTP requests.
12
13    Setting client.error kills the connection.
14    """
15
16    client: connection.Client
17
18
19@dataclass
20classClientDisconnectedHook(commands.StartHook):
21"""
22    A client connection has been closed (either by us or the client).
23    """
24
25    client: connection.Client
26
27
28@dataclass
29classServerConnectionHookData:
30"""Event data for server connection event hooks."""
31
32    server: connection.Server
33"""The server connection this hook is about."""
34    client: connection.Client
35"""The client on the other end."""
36
37
38@dataclass
39classServerConnectHook(commands.StartHook):
40"""
41    Mitmproxy is about to connect to a server.
42    Note that a connection can correspond to multiple requests.
43
44    Setting data.server.error kills the connection.
45    """
46
47    data: ServerConnectionHookData
48
49
50@dataclass
51classServerConnectedHook(commands.StartHook):
52"""
53    Mitmproxy has connected to a server.
54    """
55
56    data: ServerConnectionHookData
57
58
59@dataclass
60classServerDisconnectedHook(commands.StartHook):
61"""
62    A server connection has been closed (either by us or the server).
63    """
64
65    data: ServerConnectionHookData
66
67
68@dataclass
69classServerConnectErrorHook(commands.StartHook):
70"""
71    Mitmproxy failed to connect to a server.
72
73    Every server connection will receive either a server_connected or a server_connect_error event, but not both.
74    """
75
76    data: ServerConnectionHookData
```

@dataclass

class ServerConnectionHookData: View Source

[](#ServerConnectionHookData)

```
29@dataclass
30classServerConnectionHookData:
31"""Event data for server connection event hooks."""
32
33    server: connection.Server
34"""The server connection this hook is about."""
35    client: connection.Client
36"""The client on the other end."""
```

Event data for server connection event hooks.

The server connection this hook is about.

The client on the other end.