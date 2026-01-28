---
title: mitmproxy.flow
url: https://docs.mitmproxy.org/stable/api/mitmproxy/flow.html#Flow.timestamp_start
source: crawler
fetched_at: 2026-01-28T15:51:48.255506381-03:00
rendered_js: false
word_count: 3121
summary: This document defines the Error and Flow base classes for the mitmproxy framework, representing network connections and their associated data.
tags:
    - mitmproxy
    - network-flows
    - dataclasses
    - error-handling
    - serialization
    - tcp-udp-http
    - connection
category: reference
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/flow.py) View Source

```
  1from__future__import annotations
  2
  3importasyncio
  4importcopy
  5importtime
  6importuuid
  7fromdataclassesimport dataclass
  8fromdataclassesimport field
  9fromtypingimport Any
 10fromtypingimport ClassVar
 11
 12frommitmproxyimport connection
 13frommitmproxyimport exceptions
 14frommitmproxyimport version
 15frommitmproxy.coretypesimport serializable
 16
 17
 18@dataclass
 19classError(serializable.SerializableDataclass):
 20"""
 21    An Error.
 22
 23    This is distinct from an protocol error response (say, a HTTP code 500),
 24    which is represented by a normal `mitmproxy.http.Response` object. This class is
 25    responsible for indicating errors that fall outside of normal protocol
 26    communications, like interrupted connections, timeouts, or protocol errors.
 27    """
 28
 29    msg: str
 30"""Message describing the error."""
 31
 32    timestamp: float = field(default_factory=time.time)
 33"""Unix timestamp of when this error happened."""
 34
 35    KILLED_MESSAGE: ClassVar[str] = "Connection killed."
 36
 37    def__str__(self):
 38        return self.msg
 39
 40    def__repr__(self):
 41        return self.msg
 42
 43
 44classFlow(serializable.Serializable):
 45"""
 46    Base class for network flows. A flow is a collection of objects,
 47    for example HTTP request/response pairs or a list of TCP messages.
 48
 49    See also:
 50     - mitmproxy.http.HTTPFlow
 51     - mitmproxy.tcp.TCPFlow
 52     - mitmproxy.udp.UDPFlow
 53    """
 54
 55    client_conn: connection.Client
 56"""The client that connected to mitmproxy."""
 57
 58    server_conn: connection.Server
 59"""
 60    The server mitmproxy connected to.
 61
 62    Some flows may never cause mitmproxy to initiate a server connection,
 63    for example because their response is replayed by mitmproxy itself.
 64    To simplify implementation, those flows will still have a `server_conn` attribute
 65    with a `timestamp_start` set to `None`.
 66    """
 67
 68    error: Error | None = None
 69"""A connection or protocol error affecting this flow."""
 70
 71    intercepted: bool
 72"""
 73    If `True`, the flow is currently paused by mitmproxy.
 74    We're waiting for a user action to forward the flow to its destination.
 75    """
 76
 77    marked: str = ""
 78"""
 79    If this attribute is a non-empty string the flow has been marked by the user.
 80
 81    A string value will be used as the marker annotation. May either be a single character or a Unicode emoji name.
 82
 83    For example `:grapes:` becomes `🍇` in views that support emoji rendering.
 84    Consult the [Github API Emoji List](https://api.github.com/emojis) for a list of emoji that may be used.
 85    Not all emoji, especially [emoji modifiers](https://en.wikipedia.org/wiki/Miscellaneous_Symbols_and_Pictographs#Emoji_modifiers)
 86    will render consistently.
 87
 88    The default marker for the view will be used if the Unicode emoji name can not be interpreted.
 89    """
 90
 91    is_replay: str | None
 92"""
 93    This attribute indicates if this flow has been replayed in either direction.
 94
 95     - a value of `request` indicates that the request has been artifically replayed by mitmproxy to the server.
 96     - a value of `response` indicates that the response to the client's request has been set by server replay.
 97    """
 98
 99    live: bool
100"""
101    If `True`, the flow belongs to a currently active connection.
102    If `False`, the flow may have been already completed or loaded from disk.
103    """
104
105    timestamp_created: float
106"""
107    The Unix timestamp of when this flow was created.
108
109    In contrast to `timestamp_start`, this value will not change when a flow is replayed.
110    """
111
112    def__init__(
113        self,
114        client_conn: connection.Client,
115        server_conn: connection.Server,
116        live: bool = False,
117    ) -> None:
118        self.id = str(uuid.uuid4())
119        self.client_conn = client_conn
120        self.server_conn = server_conn
121        self.live = live
122        self.timestamp_created = time.time()
123
124        self.intercepted: bool = False
125        self._resume_event: asyncio.Event | None = None
126        self._backup: Flow | None = None
127        self.marked: str = ""
128        self.is_replay: str | None = None
129        self.metadata: dict[str, Any] = dict()
130        self.comment: str = ""
131
132    __types: dict[str, type[Flow]] = {}
133
134    type: ClassVar[
135        str
136    ]  # automatically derived from the class name in __init_subclass__
137"""The flow type, for example `http`, `tcp`, or `dns`."""
138
139    def__init_subclass__(cls, **kwargs):
140        cls.type = cls.__name__.removesuffix("Flow").lower()
141        Flow.__types[cls.type] = cls
142
143    defget_state(self) -> serializable.State:
144        state = {
145            "version": version.FLOW_FORMAT_VERSION,
146            "type": self.type,
147            "id": self.id,
148            "error": self.error.get_state() if self.error else None,
149            "client_conn": self.client_conn.get_state(),
150            "server_conn": self.server_conn.get_state(),
151            "intercepted": self.intercepted,
152            "is_replay": self.is_replay,
153            "marked": self.marked,
154            "metadata": copy.deepcopy(self.metadata),
155            "comment": self.comment,
156            "timestamp_created": self.timestamp_created,
157        }
158        state["backup"] = copy.deepcopy(self._backup) if self._backup != state else None
159        return state
160
161    defset_state(self, state: serializable.State) -> None:
162        assert state.pop("version") == version.FLOW_FORMAT_VERSION
163        assert state.pop("type") == self.type
164        self.id = state.pop("id")
165        if state["error"]:
166            if self.error:
167                self.error.set_state(state.pop("error"))
168            else:
169                self.error = Error.from_state(state.pop("error"))
170        else:
171            self.error = state.pop("error")
172        self.client_conn.set_state(state.pop("client_conn"))
173        self.server_conn.set_state(state.pop("server_conn"))
174        self.intercepted = state.pop("intercepted")
175        self.is_replay = state.pop("is_replay")
176        self.marked = state.pop("marked")
177        self.metadata = state.pop("metadata")
178        self.comment = state.pop("comment")
179        self.timestamp_created = state.pop("timestamp_created")
180        self._backup = state.pop("backup", None)
181        assert state == {}
182
183    @classmethod
184    deffrom_state(cls, state: serializable.State) -> Flow:
185        try:
186            flow_cls = Flow.__types[state["type"]]
187        except KeyError:
188            raise ValueError(f"Unknown flow type: {state['type']}")
189        client = connection.Client(peername=("", 0), sockname=("", 0))
190        server = connection.Server(address=None)
191        f = flow_cls(client, server)
192        f.set_state(state)
193        return f
194
195    defcopy(self):
196"""Make a copy of this flow."""
197        f = super().copy()
198        f.live = False
199        return f
200
201    defmodified(self):
202"""
203        `True` if this file has been modified by a user, `False` otherwise.
204        """
205        if self._backup:
206            return self._backup != self.get_state()
207        else:
208            return False
209
210    defbackup(self, force=False):
211"""
212        Save a backup of this flow, which can be restored by calling `Flow.revert()`.
213        """
214        if not self._backup:
215            self._backup = self.get_state()
216
217    defrevert(self):
218"""
219        Revert to the last backed up state.
220        """
221        if self._backup:
222            self.set_state(self._backup)
223            self._backup = None
224
225    @property
226    defkillable(self):
227"""*Read-only:* `True` if this flow can be killed, `False` otherwise."""
228        return self.live and not (self.error and self.error.msg == Error.KILLED_MESSAGE)
229
230    defkill(self):
231"""
232        Kill this flow. The current request/response will not be forwarded to its destination.
233        """
234        if not self.killable:
235            raise exceptions.ControlException("Flow is not killable.")
236        # TODO: The way we currently signal killing is not ideal. One major problem is that we cannot kill
237        #  flows in transit (https://github.com/mitmproxy/mitmproxy/issues/4711), even though they are advertised
238        #  as killable. An alternative approach would be to introduce a `KillInjected` event similar to
239        #  `MessageInjected`, which should fix this issue.
240        self.error = Error(Error.KILLED_MESSAGE)
241        self.intercepted = False
242        self.live = False
243
244    defintercept(self):
245"""
246        Intercept this Flow. Processing will stop until resume is
247        called.
248        """
249        if self.intercepted:
250            return
251        self.intercepted = True
252        if self._resume_event is not None:
253            self._resume_event.clear()
254
255    async defwait_for_resume(self):
256"""
257        Wait until this Flow is resumed.
258        """
259        if not self.intercepted:
260            return
261        if self._resume_event is None:
262            self._resume_event = asyncio.Event()
263        await self._resume_event.wait()
264
265    defresume(self):
266"""
267        Continue with the flow – called after an intercept().
268        """
269        if not self.intercepted:
270            return
271        self.intercepted = False
272        if self._resume_event is not None:
273            self._resume_event.set()
274
275    @property
276    deftimestamp_start(self) -> float:
277"""
278        *Read-only:* Start time of the flow.
279        Depending on the flow type, this property is an alias for
280        `mitmproxy.connection.Client.timestamp_start` or `mitmproxy.http.Request.timestamp_start`.
281        """
282        return self.client_conn.timestamp_start
283
284
285__all__ = [
286    "Flow",
287    "Error",
288]
```

class Flow(mitmproxy.coretypes.serializable.Serializable): View Source

[](#Flow)

```
 45classFlow(serializable.Serializable):
 46"""
 47    Base class for network flows. A flow is a collection of objects,
 48    for example HTTP request/response pairs or a list of TCP messages.
 49
 50    See also:
 51     - mitmproxy.http.HTTPFlow
 52     - mitmproxy.tcp.TCPFlow
 53     - mitmproxy.udp.UDPFlow
 54    """
 55
 56    client_conn: connection.Client
 57"""The client that connected to mitmproxy."""
 58
 59    server_conn: connection.Server
 60"""
 61    The server mitmproxy connected to.
 62
 63    Some flows may never cause mitmproxy to initiate a server connection,
 64    for example because their response is replayed by mitmproxy itself.
 65    To simplify implementation, those flows will still have a `server_conn` attribute
 66    with a `timestamp_start` set to `None`.
 67    """
 68
 69    error: Error | None = None
 70"""A connection or protocol error affecting this flow."""
 71
 72    intercepted: bool
 73"""
 74    If `True`, the flow is currently paused by mitmproxy.
 75    We're waiting for a user action to forward the flow to its destination.
 76    """
 77
 78    marked: str = ""
 79"""
 80    If this attribute is a non-empty string the flow has been marked by the user.
 81
 82    A string value will be used as the marker annotation. May either be a single character or a Unicode emoji name.
 83
 84    For example `:grapes:` becomes `🍇` in views that support emoji rendering.
 85    Consult the [Github API Emoji List](https://api.github.com/emojis) for a list of emoji that may be used.
 86    Not all emoji, especially [emoji modifiers](https://en.wikipedia.org/wiki/Miscellaneous_Symbols_and_Pictographs#Emoji_modifiers)
 87    will render consistently.
 88
 89    The default marker for the view will be used if the Unicode emoji name can not be interpreted.
 90    """
 91
 92    is_replay: str | None
 93"""
 94    This attribute indicates if this flow has been replayed in either direction.
 95
 96     - a value of `request` indicates that the request has been artifically replayed by mitmproxy to the server.
 97     - a value of `response` indicates that the response to the client's request has been set by server replay.
 98    """
 99
100    live: bool
101"""
102    If `True`, the flow belongs to a currently active connection.
103    If `False`, the flow may have been already completed or loaded from disk.
104    """
105
106    timestamp_created: float
107"""
108    The Unix timestamp of when this flow was created.
109
110    In contrast to `timestamp_start`, this value will not change when a flow is replayed.
111    """
112
113    def__init__(
114        self,
115        client_conn: connection.Client,
116        server_conn: connection.Server,
117        live: bool = False,
118    ) -> None:
119        self.id = str(uuid.uuid4())
120        self.client_conn = client_conn
121        self.server_conn = server_conn
122        self.live = live
123        self.timestamp_created = time.time()
124
125        self.intercepted: bool = False
126        self._resume_event: asyncio.Event | None = None
127        self._backup: Flow | None = None
128        self.marked: str = ""
129        self.is_replay: str | None = None
130        self.metadata: dict[str, Any] = dict()
131        self.comment: str = ""
132
133    __types: dict[str, type[Flow]] = {}
134
135    type: ClassVar[
136        str
137    ]  # automatically derived from the class name in __init_subclass__
138"""The flow type, for example `http`, `tcp`, or `dns`."""
139
140    def__init_subclass__(cls, **kwargs):
141        cls.type = cls.__name__.removesuffix("Flow").lower()
142        Flow.__types[cls.type] = cls
143
144    defget_state(self) -> serializable.State:
145        state = {
146            "version": version.FLOW_FORMAT_VERSION,
147            "type": self.type,
148            "id": self.id,
149            "error": self.error.get_state() if self.error else None,
150            "client_conn": self.client_conn.get_state(),
151            "server_conn": self.server_conn.get_state(),
152            "intercepted": self.intercepted,
153            "is_replay": self.is_replay,
154            "marked": self.marked,
155            "metadata": copy.deepcopy(self.metadata),
156            "comment": self.comment,
157            "timestamp_created": self.timestamp_created,
158        }
159        state["backup"] = copy.deepcopy(self._backup) if self._backup != state else None
160        return state
161
162    defset_state(self, state: serializable.State) -> None:
163        assert state.pop("version") == version.FLOW_FORMAT_VERSION
164        assert state.pop("type") == self.type
165        self.id = state.pop("id")
166        if state["error"]:
167            if self.error:
168                self.error.set_state(state.pop("error"))
169            else:
170                self.error = Error.from_state(state.pop("error"))
171        else:
172            self.error = state.pop("error")
173        self.client_conn.set_state(state.pop("client_conn"))
174        self.server_conn.set_state(state.pop("server_conn"))
175        self.intercepted = state.pop("intercepted")
176        self.is_replay = state.pop("is_replay")
177        self.marked = state.pop("marked")
178        self.metadata = state.pop("metadata")
179        self.comment = state.pop("comment")
180        self.timestamp_created = state.pop("timestamp_created")
181        self._backup = state.pop("backup", None)
182        assert state == {}
183
184    @classmethod
185    deffrom_state(cls, state: serializable.State) -> Flow:
186        try:
187            flow_cls = Flow.__types[state["type"]]
188        except KeyError:
189            raise ValueError(f"Unknown flow type: {state['type']}")
190        client = connection.Client(peername=("", 0), sockname=("", 0))
191        server = connection.Server(address=None)
192        f = flow_cls(client, server)
193        f.set_state(state)
194        return f
195
196    defcopy(self):
197"""Make a copy of this flow."""
198        f = super().copy()
199        f.live = False
200        return f
201
202    defmodified(self):
203"""
204        `True` if this file has been modified by a user, `False` otherwise.
205        """
206        if self._backup:
207            return self._backup != self.get_state()
208        else:
209            return False
210
211    defbackup(self, force=False):
212"""
213        Save a backup of this flow, which can be restored by calling `Flow.revert()`.
214        """
215        if not self._backup:
216            self._backup = self.get_state()
217
218    defrevert(self):
219"""
220        Revert to the last backed up state.
221        """
222        if self._backup:
223            self.set_state(self._backup)
224            self._backup = None
225
226    @property
227    defkillable(self):
228"""*Read-only:* `True` if this flow can be killed, `False` otherwise."""
229        return self.live and not (self.error and self.error.msg == Error.KILLED_MESSAGE)
230
231    defkill(self):
232"""
233        Kill this flow. The current request/response will not be forwarded to its destination.
234        """
235        if not self.killable:
236            raise exceptions.ControlException("Flow is not killable.")
237        # TODO: The way we currently signal killing is not ideal. One major problem is that we cannot kill
238        #  flows in transit (https://github.com/mitmproxy/mitmproxy/issues/4711), even though they are advertised
239        #  as killable. An alternative approach would be to introduce a `KillInjected` event similar to
240        #  `MessageInjected`, which should fix this issue.
241        self.error = Error(Error.KILLED_MESSAGE)
242        self.intercepted = False
243        self.live = False
244
245    defintercept(self):
246"""
247        Intercept this Flow. Processing will stop until resume is
248        called.
249        """
250        if self.intercepted:
251            return
252        self.intercepted = True
253        if self._resume_event is not None:
254            self._resume_event.clear()
255
256    async defwait_for_resume(self):
257"""
258        Wait until this Flow is resumed.
259        """
260        if not self.intercepted:
261            return
262        if self._resume_event is None:
263            self._resume_event = asyncio.Event()
264        await self._resume_event.wait()
265
266    defresume(self):
267"""
268        Continue with the flow – called after an intercept().
269        """
270        if not self.intercepted:
271            return
272        self.intercepted = False
273        if self._resume_event is not None:
274            self._resume_event.set()
275
276    @property
277    deftimestamp_start(self) -> float:
278"""
279        *Read-only:* Start time of the flow.
280        Depending on the flow type, this property is an alias for
281        `mitmproxy.connection.Client.timestamp_start` or `mitmproxy.http.Request.timestamp_start`.
282        """
283        return self.client_conn.timestamp_start
```

The client that connected to mitmproxy.

The server mitmproxy connected to.

Some flows may never cause mitmproxy to initiate a server connection, for example because their response is replayed by mitmproxy itself. To simplify implementation, those flows will still have a `server_conn` attribute with a `timestamp_start` set to `None`.

error: [Error](#Error) | None = None

A connection or protocol error affecting this flow.

intercepted: bool

If `True`, the flow is currently paused by mitmproxy. We're waiting for a user action to forward the flow to its destination.

marked: str = ''

If this attribute is a non-empty string the flow has been marked by the user.

A string value will be used as the marker annotation. May either be a single character or a Unicode emoji name.

For example `:grapes:` becomes `🍇` in views that support emoji rendering. Consult the [Github API Emoji List](https://api.github.com/emojis) for a list of emoji that may be used. Not all emoji, especially [emoji modifiers](https://en.wikipedia.org/wiki/Miscellaneous_Symbols_and_Pictographs#Emoji_modifiers) will render consistently.

The default marker for the view will be used if the Unicode emoji name can not be interpreted.

is\_replay: str | None

This attribute indicates if this flow has been replayed in either direction.

- a value of `request` indicates that the request has been artifically replayed by mitmproxy to the server.
- a value of `response` indicates that the response to the client's request has been set by server replay.

live: bool

If `True`, the flow belongs to a currently active connection. If `False`, the flow may have been already completed or loaded from disk.

timestamp\_created: float

The Unix timestamp of when this flow was created.

In contrast to `timestamp_start`, this value will not change when a flow is replayed.

type: ClassVar\[str]

The flow type, for example `http`, `tcp`, or `dns`.

def copy(self): View Source

```
196    defcopy(self):
197"""Make a copy of this flow."""
198        f = super().copy()
199        f.live = False
200        return f
```

Make a copy of this flow.

def modified(self): View Source

```
202    defmodified(self):
203"""
204        `True` if this file has been modified by a user, `False` otherwise.
205        """
206        if self._backup:
207            return self._backup != self.get_state()
208        else:
209            return False
```

`True` if this file has been modified by a user, `False` otherwise.

def backup(self, force=False): View Source

```
211    defbackup(self, force=False):
212"""
213        Save a backup of this flow, which can be restored by calling `Flow.revert()`.
214        """
215        if not self._backup:
216            self._backup = self.get_state()
```

Save a backup of this flow, which can be restored by calling `Flow.revert()`.

def revert(self): View Source

```
218    defrevert(self):
219"""
220        Revert to the last backed up state.
221        """
222        if self._backup:
223            self.set_state(self._backup)
224            self._backup = None
```

Revert to the last backed up state.

killable View Source

```
226    @property
227    defkillable(self):
228"""*Read-only:* `True` if this flow can be killed, `False` otherwise."""
229        return self.live and not (self.error and self.error.msg == Error.KILLED_MESSAGE)
```

*Read-only:* `True` if this flow can be killed, `False` otherwise.

def kill(self): View Source

```
231    defkill(self):
232"""
233        Kill this flow. The current request/response will not be forwarded to its destination.
234        """
235        if not self.killable:
236            raise exceptions.ControlException("Flow is not killable.")
237        # TODO: The way we currently signal killing is not ideal. One major problem is that we cannot kill
238        #  flows in transit (https://github.com/mitmproxy/mitmproxy/issues/4711), even though they are advertised
239        #  as killable. An alternative approach would be to introduce a `KillInjected` event similar to
240        #  `MessageInjected`, which should fix this issue.
241        self.error = Error(Error.KILLED_MESSAGE)
242        self.intercepted = False
243        self.live = False
```

Kill this flow. The current request/response will not be forwarded to its destination.

def intercept(self): View Source

```
245    defintercept(self):
246"""
247        Intercept this Flow. Processing will stop until resume is
248        called.
249        """
250        if self.intercepted:
251            return
252        self.intercepted = True
253        if self._resume_event is not None:
254            self._resume_event.clear()
```

Intercept this Flow. Processing will stop until resume is called.

async def wait\_for\_resume(self): View Source

```
256    async defwait_for_resume(self):
257"""
258        Wait until this Flow is resumed.
259        """
260        if not self.intercepted:
261            return
262        if self._resume_event is None:
263            self._resume_event = asyncio.Event()
264        await self._resume_event.wait()
```

Wait until this Flow is resumed.

def resume(self): View Source

```
266    defresume(self):
267"""
268        Continue with the flow – called after an intercept().
269        """
270        if not self.intercepted:
271            return
272        self.intercepted = False
273        if self._resume_event is not None:
274            self._resume_event.set()
```

Continue with the flow – called after an intercept().

timestamp\_start: float View Source

```
276    @property
277    deftimestamp_start(self) -> float:
278"""
279        *Read-only:* Start time of the flow.
280        Depending on the flow type, this property is an alias for
281        `mitmproxy.connection.Client.timestamp_start` or `mitmproxy.http.Request.timestamp_start`.
282        """
283        return self.client_conn.timestamp_start
```

@dataclass

class Error(mitmproxy.coretypes.serializable.SerializableDataclass): View Source

[](#Error)

```
19@dataclass
20classError(serializable.SerializableDataclass):
21"""
22    An Error.
23
24    This is distinct from an protocol error response (say, a HTTP code 500),
25    which is represented by a normal `mitmproxy.http.Response` object. This class is
26    responsible for indicating errors that fall outside of normal protocol
27    communications, like interrupted connections, timeouts, or protocol errors.
28    """
29
30    msg: str
31"""Message describing the error."""
32
33    timestamp: float = field(default_factory=time.time)
34"""Unix timestamp of when this error happened."""
35
36    KILLED_MESSAGE: ClassVar[str] = "Connection killed."
37
38    def__str__(self):
39        return self.msg
40
41    def__repr__(self):
42        return self.msg
```

An Error.

This is distinct from an protocol error response (say, a HTTP code 500), which is represented by a normal `mitmproxy.http.Response` object. This class is responsible for indicating errors that fall outside of normal protocol communications, like interrupted connections, timeouts, or protocol errors.

msg: str

Message describing the error.

timestamp: float

Unix timestamp of when this error happened.

KILLED\_MESSAGE: ClassVar\[str] = 'Connection killed.'