---
title: mitmproxy.udp
url: https://docs.mitmproxy.org/stable/api/mitmproxy/udp.html
source: crawler
fetched_at: 2026-01-28T15:03:26.769126489-03:00
rendered_js: false
word_count: 393
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/udp.py) View Source

```
 1importtime
 2
 3frommitmproxyimport connection
 4frommitmproxyimport flow
 5frommitmproxy.coretypesimport serializable
 6
 7
 8classUDPMessage(serializable.Serializable):
 9"""
10    An individual UDP datagram.
11    """
12
13    def__init__(self, from_client, content, timestamp=None):
14        self.from_client = from_client
15        self.content = content
16        self.timestamp = timestamp or time.time()
17
18    @classmethod
19    deffrom_state(cls, state):
20        return cls(*state)
21
22    defget_state(self):
23        return self.from_client, self.content, self.timestamp
24
25    defset_state(self, state):
26        self.from_client, self.content, self.timestamp = state
27
28    def__repr__(self):
29        return "{direction}{content}".format(
30            direction="->" if self.from_client else "<-", content=repr(self.content)
31        )
32
33
34classUDPFlow(flow.Flow):
35"""
36    A UDPFlow is a representation of a UDP session.
37    """
38
39    messages: list[UDPMessage]
40"""
41    The messages transmitted over this connection.
42
43    The latest message can be accessed as `flow.messages[-1]` in event hooks.
44    """
45
46    def__init__(
47        self,
48        client_conn: connection.Client,
49        server_conn: connection.Server,
50        live: bool = False,
51    ):
52        super().__init__(client_conn, server_conn, live)
53        self.messages = []
54
55    defget_state(self) -> serializable.State:
56        return {
57            **super().get_state(),
58            "messages": [m.get_state() for m in self.messages],
59        }
60
61    defset_state(self, state: serializable.State) -> None:
62        self.messages = [UDPMessage.from_state(m) for m in state.pop("messages")]
63        super().set_state(state)
64
65    def__repr__(self):
66        return f"<UDPFlow ({len(self.messages)} messages)>"
67
68
69__all__ = [
70    "UDPFlow",
71    "UDPMessage",
72]
```

[](#UDPFlow)

```
35classUDPFlow(flow.Flow):
36"""
37    A UDPFlow is a representation of a UDP session.
38    """
39
40    messages: list[UDPMessage]
41"""
42    The messages transmitted over this connection.
43
44    The latest message can be accessed as `flow.messages[-1]` in event hooks.
45    """
46
47    def__init__(
48        self,
49        client_conn: connection.Client,
50        server_conn: connection.Server,
51        live: bool = False,
52    ):
53        super().__init__(client_conn, server_conn, live)
54        self.messages = []
55
56    defget_state(self) -> serializable.State:
57        return {
58            **super().get_state(),
59            "messages": [m.get_state() for m in self.messages],
60        }
61
62    defset_state(self, state: serializable.State) -> None:
63        self.messages = [UDPMessage.from_state(m) for m in state.pop("messages")]
64        super().set_state(state)
65
66    def__repr__(self):
67        return f"<UDPFlow ({len(self.messages)} messages)>"
```

A UDPFlow is a representation of a UDP session.

```
47    def__init__(
48        self,
49        client_conn: connection.Client,
50        server_conn: connection.Server,
51        live: bool = False,
52    ):
53        super().__init__(client_conn, server_conn, live)
54        self.messages = []
```

messages: list\[[UDPMessage](#UDPMessage)]

The messages transmitted over this connection.

The latest message can be accessed as `flow.messages[-1]` in event hooks.

type: ClassVar\[str] = 'udp'

The flow type, for example `http`, `tcp`, or `dns`.

class UDPMessage(mitmproxy.coretypes.serializable.Serializable): View Source

[](#UDPMessage)

```
 9classUDPMessage(serializable.Serializable):
10"""
11    An individual UDP datagram.
12    """
13
14    def__init__(self, from_client, content, timestamp=None):
15        self.from_client = from_client
16        self.content = content
17        self.timestamp = timestamp or time.time()
18
19    @classmethod
20    deffrom_state(cls, state):
21        return cls(*state)
22
23    defget_state(self):
24        return self.from_client, self.content, self.timestamp
25
26    defset_state(self, state):
27        self.from_client, self.content, self.timestamp = state
28
29    def__repr__(self):
30        return "{direction}{content}".format(
31            direction="->" if self.from_client else "<-", content=repr(self.content)
32        )
```

An individual UDP datagram.

UDPMessage(from\_client, content, timestamp=None) View Source

```
14    def__init__(self, from_client, content, timestamp=None):
15        self.from_client = from_client
16        self.content = content
17        self.timestamp = timestamp or time.time()
```