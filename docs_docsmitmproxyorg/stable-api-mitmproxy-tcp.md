---
title: mitmproxy.tcp
url: https://docs.mitmproxy.org/stable/api/mitmproxy/tcp.html
source: crawler
fetched_at: 2026-01-28T14:58:35.288595977-03:00
rendered_js: false
word_count: 450
summary: This document defines the TCPFlow and TCPMessage classes used by mitmproxy to represent and manage TCP sessions and their constituent data chunks.
tags:
    - mitmproxy
    - python
    - tcp-protocol
    - network-traffic
    - api-reference
category: api
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/tcp.py) View Source

```
 1importtime
 2
 3frommitmproxyimport connection
 4frommitmproxyimport flow
 5frommitmproxy.coretypesimport serializable
 6
 7
 8classTCPMessage(serializable.Serializable):
 9"""
10    An individual TCP "message".
11    Note that TCP is *stream-based* and not *message-based*.
12    For practical purposes the stream is chunked into messages here,
13    but you should not rely on message boundaries.
14    """
15
16    def__init__(self, from_client, content, timestamp=None):
17        self.from_client = from_client
18        self.content = content
19        self.timestamp = timestamp or time.time()
20
21    @classmethod
22    deffrom_state(cls, state):
23        return cls(*state)
24
25    defget_state(self):
26        return self.from_client, self.content, self.timestamp
27
28    defset_state(self, state):
29        self.from_client, self.content, self.timestamp = state
30
31    def__repr__(self):
32        return "{direction}{content}".format(
33            direction="->" if self.from_client else "<-", content=repr(self.content)
34        )
35
36
37classTCPFlow(flow.Flow):
38"""
39    A TCPFlow is a simplified representation of a TCP session.
40    """
41
42    messages: list[TCPMessage]
43"""
44    The messages transmitted over this connection.
45
46    The latest message can be accessed as `flow.messages[-1]` in event hooks.
47    """
48
49    def__init__(
50        self,
51        client_conn: connection.Client,
52        server_conn: connection.Server,
53        live: bool = False,
54    ):
55        super().__init__(client_conn, server_conn, live)
56        self.messages = []
57
58    defget_state(self) -> serializable.State:
59        return {
60            **super().get_state(),
61            "messages": [m.get_state() for m in self.messages],
62        }
63
64    defset_state(self, state: serializable.State) -> None:
65        self.messages = [TCPMessage.from_state(m) for m in state.pop("messages")]
66        super().set_state(state)
67
68    def__repr__(self):
69        return f"<TCPFlow ({len(self.messages)} messages)>"
70
71
72__all__ = [
73    "TCPFlow",
74    "TCPMessage",
75]
```

[](#TCPFlow)

```
38classTCPFlow(flow.Flow):
39"""
40    A TCPFlow is a simplified representation of a TCP session.
41    """
42
43    messages: list[TCPMessage]
44"""
45    The messages transmitted over this connection.
46
47    The latest message can be accessed as `flow.messages[-1]` in event hooks.
48    """
49
50    def__init__(
51        self,
52        client_conn: connection.Client,
53        server_conn: connection.Server,
54        live: bool = False,
55    ):
56        super().__init__(client_conn, server_conn, live)
57        self.messages = []
58
59    defget_state(self) -> serializable.State:
60        return {
61            **super().get_state(),
62            "messages": [m.get_state() for m in self.messages],
63        }
64
65    defset_state(self, state: serializable.State) -> None:
66        self.messages = [TCPMessage.from_state(m) for m in state.pop("messages")]
67        super().set_state(state)
68
69    def__repr__(self):
70        return f"<TCPFlow ({len(self.messages)} messages)>"
```

A TCPFlow is a simplified representation of a TCP session.

```
50    def__init__(
51        self,
52        client_conn: connection.Client,
53        server_conn: connection.Server,
54        live: bool = False,
55    ):
56        super().__init__(client_conn, server_conn, live)
57        self.messages = []
```

messages: list\[[TCPMessage](#TCPMessage)]

The messages transmitted over this connection.

The latest message can be accessed as `flow.messages[-1]` in event hooks.

type: ClassVar\[str] = 'tcp'

The flow type, for example `http`, `tcp`, or `dns`.

class TCPMessage(mitmproxy.coretypes.serializable.Serializable): View Source

[](#TCPMessage)

```
 9classTCPMessage(serializable.Serializable):
10"""
11    An individual TCP "message".
12    Note that TCP is *stream-based* and not *message-based*.
13    For practical purposes the stream is chunked into messages here,
14    but you should not rely on message boundaries.
15    """
16
17    def__init__(self, from_client, content, timestamp=None):
18        self.from_client = from_client
19        self.content = content
20        self.timestamp = timestamp or time.time()
21
22    @classmethod
23    deffrom_state(cls, state):
24        return cls(*state)
25
26    defget_state(self):
27        return self.from_client, self.content, self.timestamp
28
29    defset_state(self, state):
30        self.from_client, self.content, self.timestamp = state
31
32    def__repr__(self):
33        return "{direction}{content}".format(
34            direction="->" if self.from_client else "<-", content=repr(self.content)
35        )
```

An individual TCP "message". Note that TCP is *stream-based* and not *message-based*. For practical purposes the stream is chunked into messages here, but you should not rely on message boundaries.

TCPMessage(from\_client, content, timestamp=None) View Source

```
17    def__init__(self, from_client, content, timestamp=None):
18        self.from_client = from_client
19        self.content = content
20        self.timestamp = timestamp or time.time()
```