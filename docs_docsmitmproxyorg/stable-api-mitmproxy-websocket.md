---
title: mitmproxy.websocket
url: https://docs.mitmproxy.org/stable/api/mitmproxy/websocket.html
source: crawler
fetched_at: 2026-01-28T15:01:16.530016179-03:00
rendered_js: false
word_count: 1878
summary: This document explains the WebSocket message handling in mitmproxy, including the WebSocketMessage class and WebSocketData container.
tags:
    - websocket
    - mitmproxy
    - network-protocol
    - message-handling
    - api-reference
category: reference
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/websocket.py)

Mitmproxy used to have its own WebSocketFlow type until mitmproxy 6, but now WebSocket connections now are represented as HTTP flows as well. They can be distinguished from regular HTTP requests by having the `mitmproxy.http.HTTPFlow.websocket` attribute set.

This module only defines the classes for individual `WebSocketMessage`s and the `WebSocketData` container.

View Source

```
  1"""
  2Mitmproxy used to have its own WebSocketFlow type until mitmproxy 6, but now WebSocket connections now are represented
  3as HTTP flows as well. They can be distinguished from regular HTTP requests by having the
  4`mitmproxy.http.HTTPFlow.websocket` attribute set.
  5
  6This module only defines the classes for individual `WebSocketMessage`s and the `WebSocketData` container.
  7"""
  8
  9importtime
 10importwarnings
 11fromdataclassesimport dataclass
 12fromdataclassesimport field
 13
 14fromwsproto.frame_protocolimport Opcode
 15
 16frommitmproxy.coretypesimport serializable
 17
 18WebSocketMessageState = tuple[int, bool, bytes, float, bool, bool]
 19
 20
 21classWebSocketMessage(serializable.Serializable):
 22"""
 23    A single WebSocket message sent from one peer to the other.
 24
 25    Fragmented WebSocket messages are reassembled by mitmproxy and then
 26    represented as a single instance of this class.
 27
 28    The [WebSocket RFC](https://tools.ietf.org/html/rfc6455) specifies both
 29    text and binary messages. To avoid a whole class of nasty type confusion bugs,
 30    mitmproxy stores all message contents as `bytes`. If you need a `str`, you can access the `text` property
 31    on text messages:
 32
 33    >>> if message.is_text:
 34    >>>     text = message.text
 35    """
 36
 37    from_client: bool
 38"""True if this messages was sent by the client."""
 39    type: Opcode
 40"""
 41    The message type, as per RFC 6455's [opcode](https://tools.ietf.org/html/rfc6455#section-5.2).
 42
 43    Mitmproxy currently only exposes messages assembled from `TEXT` and `BINARY` frames.
 44    """
 45    content: bytes
 46"""A byte-string representing the content of this message."""
 47    timestamp: float
 48"""Timestamp of when this message was received or created."""
 49    dropped: bool
 50"""True if the message has not been forwarded by mitmproxy, False otherwise."""
 51    injected: bool
 52"""True if the message was injected and did not originate from a client/server, False otherwise"""
 53
 54    def__init__(
 55        self,
 56        type: int | Opcode,
 57        from_client: bool,
 58        content: bytes,
 59        timestamp: float | None = None,
 60        dropped: bool = False,
 61        injected: bool = False,
 62    ) -> None:
 63        self.from_client = from_client
 64        self.type = Opcode(type)
 65        self.content = content
 66        self.timestamp: float = timestamp or time.time()
 67        self.dropped = dropped
 68        self.injected = injected
 69
 70    @classmethod
 71    deffrom_state(cls, state: WebSocketMessageState):
 72        return cls(*state)
 73
 74    defget_state(self) -> WebSocketMessageState:
 75        return (
 76            int(self.type),
 77            self.from_client,
 78            self.content,
 79            self.timestamp,
 80            self.dropped,
 81            self.injected,
 82        )
 83
 84    defset_state(self, state: WebSocketMessageState) -> None:
 85        (
 86            typ,
 87            self.from_client,
 88            self.content,
 89            self.timestamp,
 90            self.dropped,
 91            self.injected,
 92        ) = state
 93        self.type = Opcode(typ)
 94
 95    def_format_ws_message(self) -> bytes:
 96        if self.from_client:
 97            return b"[OUTGOING] " + self.content
 98        else:
 99            return b"[INCOMING] " + self.content
100
101    def__repr__(self):
102        if self.type == Opcode.TEXT:
103            return repr(self.content.decode(errors="replace"))
104        else:
105            return repr(self.content)
106
107    @property
108    defis_text(self) -> bool:
109"""
110        `True` if this message is assembled from WebSocket `TEXT` frames,
111        `False` if it is assembled from `BINARY` frames.
112        """
113        return self.type == Opcode.TEXT
114
115    defdrop(self):
116"""Drop this message, i.e. don't forward it to the other peer."""
117        self.dropped = True
118
119    defkill(self):  # pragma: no cover
120"""A deprecated alias for `.drop()`."""
121        warnings.warn(
122            "WebSocketMessage.kill() is deprecated, use .drop() instead.",
123            DeprecationWarning,
124            stacklevel=2,
125        )
126        self.drop()
127
128    @property
129    deftext(self) -> str:
130"""
131        The message content as text.
132
133        This attribute is only available if `WebSocketMessage.is_text` is `True`.
134
135        *See also:* `WebSocketMessage.content`
136        """
137        if self.type != Opcode.TEXT:
138            raise AttributeError(
139                f"{self.type.name.title()} WebSocket frames do not have a 'text' attribute."
140            )
141
142        return self.content.decode()
143
144    @text.setter
145    deftext(self, value: str) -> None:
146        if self.type != Opcode.TEXT:
147            raise AttributeError(
148                f"{self.type.name.title()} WebSocket frames do not have a 'text' attribute."
149            )
150
151        self.content = value.encode()
152
153
154@dataclass
155classWebSocketData(serializable.SerializableDataclass):
156"""
157    A data container for everything related to a single WebSocket connection.
158    This is typically accessed as `mitmproxy.http.HTTPFlow.websocket`.
159    """
160
161    messages: list[WebSocketMessage] = field(default_factory=list)
162"""All `WebSocketMessage`s transferred over this connection."""
163
164    closed_by_client: bool | None = None
165"""
166    `True` if the client closed the connection,
167    `False` if the server closed the connection,
168    `None` if the connection is active.
169    """
170    close_code: int | None = None
171"""[Close Code](https://tools.ietf.org/html/rfc6455#section-7.1.5)"""
172    close_reason: str | None = None
173"""[Close Reason](https://tools.ietf.org/html/rfc6455#section-7.1.6)"""
174
175    timestamp_end: float | None = None
176"""*Timestamp:* WebSocket connection closed."""
177
178    def__repr__(self):
179        return f"<WebSocketData ({len(self.messages)} messages)>"
180
181    def_get_formatted_messages(self) -> bytes:
182        return b"\n".join(m._format_ws_message() for m in self.messages)
```

WebSocketMessageState = tuple\[int, bool, bytes, float, bool, bool]

[](#WebSocketMessageState)

class WebSocketMessage(mitmproxy.coretypes.serializable.Serializable): View Source

[](#WebSocketMessage)

```
 22classWebSocketMessage(serializable.Serializable):
 23"""
 24    A single WebSocket message sent from one peer to the other.
 25
 26    Fragmented WebSocket messages are reassembled by mitmproxy and then
 27    represented as a single instance of this class.
 28
 29    The [WebSocket RFC](https://tools.ietf.org/html/rfc6455) specifies both
 30    text and binary messages. To avoid a whole class of nasty type confusion bugs,
 31    mitmproxy stores all message contents as `bytes`. If you need a `str`, you can access the `text` property
 32    on text messages:
 33
 34    >>> if message.is_text:
 35    >>>     text = message.text
 36    """
 37
 38    from_client: bool
 39"""True if this messages was sent by the client."""
 40    type: Opcode
 41"""
 42    The message type, as per RFC 6455's [opcode](https://tools.ietf.org/html/rfc6455#section-5.2).
 43
 44    Mitmproxy currently only exposes messages assembled from `TEXT` and `BINARY` frames.
 45    """
 46    content: bytes
 47"""A byte-string representing the content of this message."""
 48    timestamp: float
 49"""Timestamp of when this message was received or created."""
 50    dropped: bool
 51"""True if the message has not been forwarded by mitmproxy, False otherwise."""
 52    injected: bool
 53"""True if the message was injected and did not originate from a client/server, False otherwise"""
 54
 55    def__init__(
 56        self,
 57        type: int | Opcode,
 58        from_client: bool,
 59        content: bytes,
 60        timestamp: float | None = None,
 61        dropped: bool = False,
 62        injected: bool = False,
 63    ) -> None:
 64        self.from_client = from_client
 65        self.type = Opcode(type)
 66        self.content = content
 67        self.timestamp: float = timestamp or time.time()
 68        self.dropped = dropped
 69        self.injected = injected
 70
 71    @classmethod
 72    deffrom_state(cls, state: WebSocketMessageState):
 73        return cls(*state)
 74
 75    defget_state(self) -> WebSocketMessageState:
 76        return (
 77            int(self.type),
 78            self.from_client,
 79            self.content,
 80            self.timestamp,
 81            self.dropped,
 82            self.injected,
 83        )
 84
 85    defset_state(self, state: WebSocketMessageState) -> None:
 86        (
 87            typ,
 88            self.from_client,
 89            self.content,
 90            self.timestamp,
 91            self.dropped,
 92            self.injected,
 93        ) = state
 94        self.type = Opcode(typ)
 95
 96    def_format_ws_message(self) -> bytes:
 97        if self.from_client:
 98            return b"[OUTGOING] " + self.content
 99        else:
100            return b"[INCOMING] " + self.content
101
102    def__repr__(self):
103        if self.type == Opcode.TEXT:
104            return repr(self.content.decode(errors="replace"))
105        else:
106            return repr(self.content)
107
108    @property
109    defis_text(self) -> bool:
110"""
111        `True` if this message is assembled from WebSocket `TEXT` frames,
112        `False` if it is assembled from `BINARY` frames.
113        """
114        return self.type == Opcode.TEXT
115
116    defdrop(self):
117"""Drop this message, i.e. don't forward it to the other peer."""
118        self.dropped = True
119
120    defkill(self):  # pragma: no cover
121"""A deprecated alias for `.drop()`."""
122        warnings.warn(
123            "WebSocketMessage.kill() is deprecated, use .drop() instead.",
124            DeprecationWarning,
125            stacklevel=2,
126        )
127        self.drop()
128
129    @property
130    deftext(self) -> str:
131"""
132        The message content as text.
133
134        This attribute is only available if `WebSocketMessage.is_text` is `True`.
135
136        *See also:* `WebSocketMessage.content`
137        """
138        if self.type != Opcode.TEXT:
139            raise AttributeError(
140                f"{self.type.name.title()} WebSocket frames do not have a 'text' attribute."
141            )
142
143        return self.content.decode()
144
145    @text.setter
146    deftext(self, value: str) -> None:
147        if self.type != Opcode.TEXT:
148            raise AttributeError(
149                f"{self.type.name.title()} WebSocket frames do not have a 'text' attribute."
150            )
151
152        self.content = value.encode()
```

A single WebSocket message sent from one peer to the other.

Fragmented WebSocket messages are reassembled by mitmproxy and then represented as a single instance of this class.

The [WebSocket RFC](https://tools.ietf.org/html/rfc6455) specifies both text and binary messages. To avoid a whole class of nasty type confusion bugs, mitmproxy stores all message contents as `bytes`. If you need a `str`, you can access the `text` property on text messages:

```
>>> if message.is_text:
>>>     text = message.text
```

WebSocketMessage( type: int | wsproto.frame\_protocol.Opcode, from\_client: bool, content: bytes, timestamp: float | None = None, dropped: bool = False, injected: bool = False) View Source

```
55    def__init__(
56        self,
57        type: int | Opcode,
58        from_client: bool,
59        content: bytes,
60        timestamp: float | None = None,
61        dropped: bool = False,
62        injected: bool = False,
63    ) -> None:
64        self.from_client = from_client
65        self.type = Opcode(type)
66        self.content = content
67        self.timestamp: float = timestamp or time.time()
68        self.dropped = dropped
69        self.injected = injected
```

from\_client: bool

True if this messages was sent by the client.

content: bytes

A byte-string representing the content of this message.

timestamp: float

Timestamp of when this message was received or created.

dropped: bool

True if the message has not been forwarded by mitmproxy, False otherwise.

injected: bool

True if the message was injected and did not originate from a client/server, False otherwise

is\_text: bool View Source

```
108    @property
109    defis_text(self) -> bool:
110"""
111        `True` if this message is assembled from WebSocket `TEXT` frames,
112        `False` if it is assembled from `BINARY` frames.
113        """
114        return self.type == Opcode.TEXT
```

`True` if this message is assembled from WebSocket `TEXT` frames, `False` if it is assembled from `BINARY` frames.

def drop(self): View Source

```
116    defdrop(self):
117"""Drop this message, i.e. don't forward it to the other peer."""
118        self.dropped = True
```

Drop this message, i.e. don't forward it to the other peer.

def kill(self): View Source

```
120    defkill(self):  # pragma: no cover
121"""A deprecated alias for `.drop()`."""
122        warnings.warn(
123            "WebSocketMessage.kill() is deprecated, use .drop() instead.",
124            DeprecationWarning,
125            stacklevel=2,
126        )
127        self.drop()
```

A deprecated alias for `.drop()`.

text: str View Source

```
129    @property
130    deftext(self) -> str:
131"""
132        The message content as text.
133
134        This attribute is only available if `WebSocketMessage.is_text` is `True`.
135
136        *See also:* `WebSocketMessage.content`
137        """
138        if self.type != Opcode.TEXT:
139            raise AttributeError(
140                f"{self.type.name.title()} WebSocket frames do not have a 'text' attribute."
141            )
142
143        return self.content.decode()
```

The message content as text.

This attribute is only available if `WebSocketMessage.is_text` is `True`.

*See also:* `WebSocketMessage.content`

@dataclass

class WebSocketData(mitmproxy.coretypes.serializable.SerializableDataclass): View Source

[](#WebSocketData)

```
155@dataclass
156classWebSocketData(serializable.SerializableDataclass):
157"""
158    A data container for everything related to a single WebSocket connection.
159    This is typically accessed as `mitmproxy.http.HTTPFlow.websocket`.
160    """
161
162    messages: list[WebSocketMessage] = field(default_factory=list)
163"""All `WebSocketMessage`s transferred over this connection."""
164
165    closed_by_client: bool | None = None
166"""
167    `True` if the client closed the connection,
168    `False` if the server closed the connection,
169    `None` if the connection is active.
170    """
171    close_code: int | None = None
172"""[Close Code](https://tools.ietf.org/html/rfc6455#section-7.1.5)"""
173    close_reason: str | None = None
174"""[Close Reason](https://tools.ietf.org/html/rfc6455#section-7.1.6)"""
175
176    timestamp_end: float | None = None
177"""*Timestamp:* WebSocket connection closed."""
178
179    def__repr__(self):
180        return f"<WebSocketData ({len(self.messages)} messages)>"
181
182    def_get_formatted_messages(self) -> bytes:
183        return b"\n".join(m._format_ws_message() for m in self.messages)
```

A data container for everything related to a single WebSocket connection. This is typically accessed as `mitmproxy.http.HTTPFlow.websocket`.

WebSocketData( messages: list\[[WebSocketMessage](#WebSocketMessage)] = &lt;factory&gt;, closed\_by\_client: bool | None = None, close\_code: int | None = None, close\_reason: str | None = None, timestamp\_end: float | None = None)

messages: list\[[WebSocketMessage](#WebSocketMessage)]

All `WebSocketMessage`s transferred over this connection.

closed\_by\_client: bool | None = None

`True` if the client closed the connection, `False` if the server closed the connection, `None` if the connection is active.

close\_code: int | None = None

close\_reason: str | None = None

timestamp\_end: float | None = None

*Timestamp:* WebSocket connection closed.