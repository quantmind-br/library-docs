---
title: mitmproxy.proxy.mode_specs
url: https://docs.mitmproxy.org/stable/api/mitmproxy/proxy/mode_specs.html
source: crawler
fetched_at: 2026-01-28T15:51:23.410453591-03:00
rendered_js: false
word_count: 3163
summary: This module defines and parses proxy mode specifications for mitmproxy, including regular, reverse, transparent, and upstream modes with configurable listen addresses and ports.
tags:
    - proxy-mode
    - parsing
    - configuration
    - mitmproxy
    - socket
    - tcp
category: configuration
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/proxy/mode_specs.py)

This module is responsible for parsing proxy mode specifications such as `"regular"`, `"reverse:https://example.com"`, or `"socks5@1234"`. The general syntax is

```
mode [: mode_configuration] [@ [listen_addr:]listen_port]
```

For a full example, consider `reverse:https://[email protected]:443`. This would spawn a reverse proxy on port 443 bound to localhost. The mode is `reverse`, and the mode data is `https://example.com`. Examples:

```
mode = ProxyMode.parse("regular@1234")
assert mode.listen_port == 1234
assert isinstance(mode, RegularMode)

ProxyMode.parse("reverse:example.com@invalid-port")  # ValueError

RegularMode.parse("regular")  # ok
RegularMode.parse("socks5")  # ValueError
```

View Source

```
  1"""
  2This module is responsible for parsing proxy mode specifications such as
  3`"regular"`, `"reverse:https://example.com"`, or `"socks5@1234"`. The general syntax is
  4
  5    mode [: mode_configuration] [@ [listen_addr:]listen_port]
  6
  7For a full example, consider `reverse:https://[email protected]:443`.
  8This would spawn a reverse proxy on port 443 bound to localhost.
  9The mode is `reverse`, and the mode data is `https://example.com`.
 10Examples:
 11
 12    mode = ProxyMode.parse("regular@1234")
 13    assert mode.listen_port == 1234
 14    assert isinstance(mode, RegularMode)
 15
 16    ProxyMode.parse("reverse:example.com@invalid-port")  # ValueError
 17
 18    RegularMode.parse("regular")  # ok
 19    RegularMode.parse("socks5")  # ValueError
 20
 21"""
 22
 23from__future__import annotations
 24
 25importdataclasses
 26importplatform
 27importre
 28importsys
 29fromabcimport ABCMeta
 30fromabcimport abstractmethod
 31fromdataclassesimport dataclass
 32fromfunctoolsimport cache
 33fromtypingimport ClassVar
 34fromtypingimport Literal
 35
 36importmitmproxy_rs
 37frommitmproxy.coretypes.serializableimport Serializable
 38frommitmproxy.netimport server_spec
 39
 40if sys.version_info < (3, 11):
 41    fromtyping_extensionsimport Self  # pragma: no cover
 42else:
 43    fromtypingimport Self
 44
 45
 46@dataclass(frozen=True)  # type: ignore
 47classProxyMode(Serializable, metaclass=ABCMeta):
 48"""
 49    Parsed representation of a proxy mode spec. Subclassed for each specific mode,
 50    which then does its own data validation.
 51    """
 52
 53    full_spec: str
 54"""The full proxy mode spec as entered by the user."""
 55    data: str
 56"""The (raw) mode data, i.e. the part after the mode name."""
 57    custom_listen_host: str | None
 58"""A custom listen host, if specified in the spec."""
 59    custom_listen_port: int | None
 60"""A custom listen port, if specified in the spec."""
 61
 62    type_name: ClassVar[
 63        str
 64    ]  # automatically derived from the class name in __init_subclass__
 65"""The unique name for this proxy mode, e.g. "regular" or "reverse"."""
 66    __types: ClassVar[dict[str, type[ProxyMode]]] = {}
 67
 68    def__init_subclass__(cls, **kwargs):
 69        cls.type_name = cls.__name__.removesuffix("Mode").lower()
 70        assert cls.type_name not in ProxyMode.__types
 71        ProxyMode.__types[cls.type_name] = cls
 72
 73    def__repr__(self):
 74        return f"ProxyMode.parse({self.full_spec!r})"
 75
 76    @abstractmethod
 77    def__post_init__(self) -> None:
 78"""Validation of data happens here."""
 79
 80    @property
 81    @abstractmethod
 82    defdescription(self) -> str:
 83"""The mode description that will be used in server logs and UI."""
 84
 85    @property
 86    defdefault_port(self) -> int | None:
 87"""
 88        Default listen port of servers for this mode, see `ProxyMode.listen_port()`.
 89        """
 90        return 8080
 91
 92    @property
 93    @abstractmethod
 94    deftransport_protocol(self) -> Literal["tcp", "udp", "both"]:
 95"""The transport protocol used by this mode's server."""
 96
 97    @classmethod
 98    @cache
 99    defparse(cls, spec: str) -> Self:
100"""
101        Parse a proxy mode specification and return the corresponding `ProxyMode` instance.
102        """
103        head, _, listen_at = spec.rpartition("@")
104        if not head:
105            head = listen_at
106            listen_at = ""
107
108        mode, _, data = head.partition(":")
109
110        if listen_at:
111            if ":" in listen_at:
112                host, _, port_str = listen_at.rpartition(":")
113            else:
114                host = None
115                port_str = listen_at
116            try:
117                port = int(port_str)
118                if port < 0 or 65535 < port:
119                    raise ValueError
120            except ValueError:
121                raise ValueError(f"invalid port: {port_str}")
122        else:
123            host = None
124            port = None
125
126        try:
127            mode_cls = ProxyMode.__types[mode.lower()]
128        except KeyError:
129            raise ValueError(f"unknown mode")
130
131        if not issubclass(mode_cls, cls):
132            raise ValueError(f"{mode!r} is not a spec for a {cls.type_name} mode")
133
134        return mode_cls(
135            full_spec=spec, data=data, custom_listen_host=host, custom_listen_port=port
136        )
137
138    deflisten_host(self, default: str | None = None) -> str:
139"""
140        Return the address a server for this mode should listen on. This can be either directly
141        specified in the spec or taken from a user-configured global default (`options.listen_host`).
142        By default, return an empty string to listen on all hosts.
143        """
144        if self.custom_listen_host is not None:
145            return self.custom_listen_host
146        elif default is not None:
147            return default
148        else:
149            return ""
150
151    deflisten_port(self, default: int | None = None) -> int | None:
152"""
153        Return the port a server for this mode should listen on. This can be either directly
154        specified in the spec, taken from a user-configured global default (`options.listen_port`),
155        or from `ProxyMode.default_port`.
156        May be `None` for modes that don't bind to a specific address, e.g. local redirect mode.
157        """
158        if self.custom_listen_port is not None:
159            return self.custom_listen_port
160        elif default is not None:
161            return default
162        else:
163            return self.default_port
164
165    @classmethod
166    deffrom_state(cls, state):
167        return ProxyMode.parse(state)
168
169    defget_state(self):
170        return self.full_spec
171
172    defset_state(self, state):
173        if state != self.full_spec:
174            raise dataclasses.FrozenInstanceError("Proxy modes are immutable.")
175
176
177TCP: Literal["tcp", "udp", "both"] = "tcp"
178UDP: Literal["tcp", "udp", "both"] = "udp"
179BOTH: Literal["tcp", "udp", "both"] = "both"
180
181
182def_check_empty(data):
183    if data:
184        raise ValueError("mode takes no arguments")
185
186
187classRegularMode(ProxyMode):
188"""A regular HTTP(S) proxy that is interfaced with `HTTP CONNECT` calls (or absolute-form HTTP requests)."""
189
190    description = "HTTP(S) proxy"
191    transport_protocol = TCP
192
193    def__post_init__(self) -> None:
194        _check_empty(self.data)
195
196
197classTransparentMode(ProxyMode):
198"""A transparent proxy, see https://docs.mitmproxy.org/dev/howto-transparent/"""
199
200    description = "Transparent Proxy"
201    transport_protocol = TCP
202
203    def__post_init__(self) -> None:
204        _check_empty(self.data)
205
206
207classUpstreamMode(ProxyMode):
208"""A regular HTTP(S) proxy, but all connections are forwarded to a second upstream HTTP(S) proxy."""
209
210    description = "HTTP(S) proxy (upstream mode)"
211    transport_protocol = TCP
212    scheme: Literal["http", "https"]
213    address: tuple[str, int]
214
215    # noinspection PyDataclass
216    def__post_init__(self) -> None:
217        scheme, self.address = server_spec.parse(self.data, default_scheme="http")
218        if scheme != "http" and scheme != "https":
219            raise ValueError("invalid upstream proxy scheme")
220        self.scheme = scheme
221
222
223classReverseMode(ProxyMode):
224"""A reverse proxy. This acts like a normal server, but redirects all requests to a fixed target."""
225
226    description = "reverse proxy"
227    transport_protocol = TCP
228    scheme: Literal[
229        "http", "https", "http3", "tls", "dtls", "tcp", "udp", "dns", "quic"
230    ]
231    address: tuple[str, int]
232
233    # noinspection PyDataclass
234    def__post_init__(self) -> None:
235        self.scheme, self.address = server_spec.parse(self.data, default_scheme="https")
236        if self.scheme in ("http3", "dtls", "udp", "quic"):
237            self.transport_protocol = UDP
238        elif self.scheme in ("dns", "https"):
239            self.transport_protocol = BOTH
240        self.description = f"{self.description} to {self.data}"
241
242    @property
243    defdefault_port(self) -> int | None:
244        if self.scheme == "dns":
245            return 53
246        return super().default_port
247
248
249classSocks5Mode(ProxyMode):
250"""A SOCKSv5 proxy."""
251
252    description = "SOCKS v5 proxy"
253    default_port = 1080
254    transport_protocol = TCP
255
256    def__post_init__(self) -> None:
257        _check_empty(self.data)
258
259
260classDnsMode(ProxyMode):
261"""A DNS server."""
262
263    description = "DNS server"
264    default_port = 53
265    transport_protocol = BOTH
266
267    def__post_init__(self) -> None:
268        _check_empty(self.data)
269
270
271# class Http3Mode(ProxyMode):
272#     """
273#     A regular HTTP3 proxy that is interfaced with absolute-form HTTP requests.
274#     (This class will be merged into `RegularMode` once the UDP implementation is deemed stable enough.)
275#     """
276#
277#     description = "HTTP3 proxy"
278#     transport_protocol = UDP
279#
280#     def __post_init__(self) -> None:
281#         _check_empty(self.data)
282
283
284classWireGuardMode(ProxyMode):
285"""Proxy Server based on WireGuard"""
286
287    description = "WireGuard server"
288    default_port = 51820
289    transport_protocol = UDP
290
291    def__post_init__(self) -> None:
292        pass
293
294
295classLocalMode(ProxyMode):
296"""OS-level transparent proxy."""
297
298    description = "Local redirector"
299    transport_protocol = BOTH
300    default_port = None
301
302    def__post_init__(self) -> None:
303        # should not raise
304        mitmproxy_rs.local.LocalRedirector.describe_spec(self.data)
305
306
307classTunMode(ProxyMode):
308"""A Tun interface."""
309
310    description = "TUN interface"
311    default_port = None
312    transport_protocol = BOTH
313
314    def__post_init__(self) -> None:
315        invalid_tun_name = self.data and (
316            # The Rust side is Linux only for the moment, but eventually we may need this.
317            platform.system() == "Darwin" and not re.match(r"^utun\d+$", self.data)
318        )
319        if invalid_tun_name:  # pragma: no cover
320            raise ValueError(
321                f"Invalid tun name: {self.data}. "
322                f"On macOS, the tun name must be the form utunx where x is a number, such as utun3."
323            )
324
325
326classOsProxyMode(ProxyMode):  # pragma: no cover
327"""Deprecated alias for LocalMode"""
328
329    description = "Deprecated alias for LocalMode"
330    transport_protocol = BOTH
331    default_port = None
332
333    def__post_init__(self) -> None:
334        raise ValueError(
335            "osproxy mode has been renamed to local mode. Thanks for trying our experimental features!"
336        )
```

@dataclass(frozen=True)

class ProxyMode(mitmproxy.coretypes.serializable.Serializable): View Source

[](#ProxyMode)

```
 47@dataclass(frozen=True)  # type: ignore
 48classProxyMode(Serializable, metaclass=ABCMeta):
 49"""
 50    Parsed representation of a proxy mode spec. Subclassed for each specific mode,
 51    which then does its own data validation.
 52    """
 53
 54    full_spec: str
 55"""The full proxy mode spec as entered by the user."""
 56    data: str
 57"""The (raw) mode data, i.e. the part after the mode name."""
 58    custom_listen_host: str | None
 59"""A custom listen host, if specified in the spec."""
 60    custom_listen_port: int | None
 61"""A custom listen port, if specified in the spec."""
 62
 63    type_name: ClassVar[
 64        str
 65    ]  # automatically derived from the class name in __init_subclass__
 66"""The unique name for this proxy mode, e.g. "regular" or "reverse"."""
 67    __types: ClassVar[dict[str, type[ProxyMode]]] = {}
 68
 69    def__init_subclass__(cls, **kwargs):
 70        cls.type_name = cls.__name__.removesuffix("Mode").lower()
 71        assert cls.type_name not in ProxyMode.__types
 72        ProxyMode.__types[cls.type_name] = cls
 73
 74    def__repr__(self):
 75        return f"ProxyMode.parse({self.full_spec!r})"
 76
 77    @abstractmethod
 78    def__post_init__(self) -> None:
 79"""Validation of data happens here."""
 80
 81    @property
 82    @abstractmethod
 83    defdescription(self) -> str:
 84"""The mode description that will be used in server logs and UI."""
 85
 86    @property
 87    defdefault_port(self) -> int | None:
 88"""
 89        Default listen port of servers for this mode, see `ProxyMode.listen_port()`.
 90        """
 91        return 8080
 92
 93    @property
 94    @abstractmethod
 95    deftransport_protocol(self) -> Literal["tcp", "udp", "both"]:
 96"""The transport protocol used by this mode's server."""
 97
 98    @classmethod
 99    @cache
100    defparse(cls, spec: str) -> Self:
101"""
102        Parse a proxy mode specification and return the corresponding `ProxyMode` instance.
103        """
104        head, _, listen_at = spec.rpartition("@")
105        if not head:
106            head = listen_at
107            listen_at = ""
108
109        mode, _, data = head.partition(":")
110
111        if listen_at:
112            if ":" in listen_at:
113                host, _, port_str = listen_at.rpartition(":")
114            else:
115                host = None
116                port_str = listen_at
117            try:
118                port = int(port_str)
119                if port < 0 or 65535 < port:
120                    raise ValueError
121            except ValueError:
122                raise ValueError(f"invalid port: {port_str}")
123        else:
124            host = None
125            port = None
126
127        try:
128            mode_cls = ProxyMode.__types[mode.lower()]
129        except KeyError:
130            raise ValueError(f"unknown mode")
131
132        if not issubclass(mode_cls, cls):
133            raise ValueError(f"{mode!r} is not a spec for a {cls.type_name} mode")
134
135        return mode_cls(
136            full_spec=spec, data=data, custom_listen_host=host, custom_listen_port=port
137        )
138
139    deflisten_host(self, default: str | None = None) -> str:
140"""
141        Return the address a server for this mode should listen on. This can be either directly
142        specified in the spec or taken from a user-configured global default (`options.listen_host`).
143        By default, return an empty string to listen on all hosts.
144        """
145        if self.custom_listen_host is not None:
146            return self.custom_listen_host
147        elif default is not None:
148            return default
149        else:
150            return ""
151
152    deflisten_port(self, default: int | None = None) -> int | None:
153"""
154        Return the port a server for this mode should listen on. This can be either directly
155        specified in the spec, taken from a user-configured global default (`options.listen_port`),
156        or from `ProxyMode.default_port`.
157        May be `None` for modes that don't bind to a specific address, e.g. local redirect mode.
158        """
159        if self.custom_listen_port is not None:
160            return self.custom_listen_port
161        elif default is not None:
162            return default
163        else:
164            return self.default_port
165
166    @classmethod
167    deffrom_state(cls, state):
168        return ProxyMode.parse(state)
169
170    defget_state(self):
171        return self.full_spec
172
173    defset_state(self, state):
174        if state != self.full_spec:
175            raise dataclasses.FrozenInstanceError("Proxy modes are immutable.")
```

Parsed representation of a proxy mode spec. Subclassed for each specific mode, which then does its own data validation.

full\_spec: str

The full proxy mode spec as entered by the user.

data: str

The (raw) mode data, i.e. the part after the mode name.

custom\_listen\_host: str | None

A custom listen host, if specified in the spec.

custom\_listen\_port: int | None

A custom listen port, if specified in the spec.

type\_name: ClassVar\[str]

The unique name for this proxy mode, e.g. "regular" or "reverse".

description: str View Source

```
81    @property
82    @abstractmethod
83    defdescription(self) -> str:
84"""The mode description that will be used in server logs and UI."""
```

The mode description that will be used in server logs and UI.

default\_port: int | None View Source

```
86    @property
87    defdefault_port(self) -> int | None:
88"""
89        Default listen port of servers for this mode, see `ProxyMode.listen_port()`.
90        """
91        return 8080
```

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

transport\_protocol: Literal\['tcp', 'udp', 'both'] View Source

```
93    @property
94    @abstractmethod
95    deftransport_protocol(self) -> Literal["tcp", "udp", "both"]:
96"""The transport protocol used by this mode's server."""
```

The transport protocol used by this mode's server.

@classmethod

@cache

def parse(cls, spec: str) -&gt; Self: View Source

```
 98    @classmethod
 99    @cache
100    defparse(cls, spec: str) -> Self:
101"""
102        Parse a proxy mode specification and return the corresponding `ProxyMode` instance.
103        """
104        head, _, listen_at = spec.rpartition("@")
105        if not head:
106            head = listen_at
107            listen_at = ""
108
109        mode, _, data = head.partition(":")
110
111        if listen_at:
112            if ":" in listen_at:
113                host, _, port_str = listen_at.rpartition(":")
114            else:
115                host = None
116                port_str = listen_at
117            try:
118                port = int(port_str)
119                if port < 0 or 65535 < port:
120                    raise ValueError
121            except ValueError:
122                raise ValueError(f"invalid port: {port_str}")
123        else:
124            host = None
125            port = None
126
127        try:
128            mode_cls = ProxyMode.__types[mode.lower()]
129        except KeyError:
130            raise ValueError(f"unknown mode")
131
132        if not issubclass(mode_cls, cls):
133            raise ValueError(f"{mode!r} is not a spec for a {cls.type_name} mode")
134
135        return mode_cls(
136            full_spec=spec, data=data, custom_listen_host=host, custom_listen_port=port
137        )
```

Parse a proxy mode specification and return the corresponding `ProxyMode` instance.

def listen\_host(self, default: str | None = None) -&gt; str: View Source

```
139    deflisten_host(self, default: str | None = None) -> str:
140"""
141        Return the address a server for this mode should listen on. This can be either directly
142        specified in the spec or taken from a user-configured global default (`options.listen_host`).
143        By default, return an empty string to listen on all hosts.
144        """
145        if self.custom_listen_host is not None:
146            return self.custom_listen_host
147        elif default is not None:
148            return default
149        else:
150            return ""
```

Return the address a server for this mode should listen on. This can be either directly specified in the spec or taken from a user-configured global default (`options.listen_host`). By default, return an empty string to listen on all hosts.

def listen\_port(self, default: int | None = None) -&gt; int | None: View Source

```
152    deflisten_port(self, default: int | None = None) -> int | None:
153"""
154        Return the port a server for this mode should listen on. This can be either directly
155        specified in the spec, taken from a user-configured global default (`options.listen_port`),
156        or from `ProxyMode.default_port`.
157        May be `None` for modes that don't bind to a specific address, e.g. local redirect mode.
158        """
159        if self.custom_listen_port is not None:
160            return self.custom_listen_port
161        elif default is not None:
162            return default
163        else:
164            return self.default_port
```

Return the port a server for this mode should listen on. This can be either directly specified in the spec, taken from a user-configured global default (`options.listen_port`), or from `ProxyMode.default_port`. May be `None` for modes that don't bind to a specific address, e.g. local redirect mode.

TCP: Literal\['tcp', 'udp', 'both'] = 'tcp'

[](#TCP)

UDP: Literal\['tcp', 'udp', 'both'] = 'udp'

[](#UDP)

BOTH: Literal\['tcp', 'udp', 'both'] = 'both'

[](#BOTH)

class RegularMode([ProxyMode](#ProxyMode)): View Source

[](#RegularMode)

```
188classRegularMode(ProxyMode):
189"""A regular HTTP(S) proxy that is interfaced with `HTTP CONNECT` calls (or absolute-form HTTP requests)."""
190
191    description = "HTTP(S) proxy"
192    transport_protocol = TCP
193
194    def__post_init__(self) -> None:
195        _check_empty(self.data)
```

A regular HTTP(S) proxy that is interfaced with `HTTP CONNECT` calls (or absolute-form HTTP requests).

description = 'HTTP(S) proxy'

The mode description that will be used in server logs and UI.

transport\_protocol = 'tcp'

The transport protocol used by this mode's server.

type\_name: ClassVar\[str] = 'regular'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class TransparentMode([ProxyMode](#ProxyMode)): View Source

[](#TransparentMode)

```
198classTransparentMode(ProxyMode):
199"""A transparent proxy, see https://docs.mitmproxy.org/dev/howto-transparent/"""
200
201    description = "Transparent Proxy"
202    transport_protocol = TCP
203
204    def__post_init__(self) -> None:
205        _check_empty(self.data)
```

description = 'Transparent Proxy'

The mode description that will be used in server logs and UI.

transport\_protocol = 'tcp'

The transport protocol used by this mode's server.

type\_name: ClassVar\[str] = 'transparent'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class UpstreamMode([ProxyMode](#ProxyMode)): View Source

[](#UpstreamMode)

```
208classUpstreamMode(ProxyMode):
209"""A regular HTTP(S) proxy, but all connections are forwarded to a second upstream HTTP(S) proxy."""
210
211    description = "HTTP(S) proxy (upstream mode)"
212    transport_protocol = TCP
213    scheme: Literal["http", "https"]
214    address: tuple[str, int]
215
216    # noinspection PyDataclass
217    def__post_init__(self) -> None:
218        scheme, self.address = server_spec.parse(self.data, default_scheme="http")
219        if scheme != "http" and scheme != "https":
220            raise ValueError("invalid upstream proxy scheme")
221        self.scheme = scheme
```

A regular HTTP(S) proxy, but all connections are forwarded to a second upstream HTTP(S) proxy.

description = 'HTTP(S) proxy (upstream mode)'

The mode description that will be used in server logs and UI.

transport\_protocol = 'tcp'

The transport protocol used by this mode's server.

scheme: Literal\['http', 'https']

type\_name: ClassVar\[str] = 'upstream'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class ReverseMode([ProxyMode](#ProxyMode)): View Source

[](#ReverseMode)

```
224classReverseMode(ProxyMode):
225"""A reverse proxy. This acts like a normal server, but redirects all requests to a fixed target."""
226
227    description = "reverse proxy"
228    transport_protocol = TCP
229    scheme: Literal[
230        "http", "https", "http3", "tls", "dtls", "tcp", "udp", "dns", "quic"
231    ]
232    address: tuple[str, int]
233
234    # noinspection PyDataclass
235    def__post_init__(self) -> None:
236        self.scheme, self.address = server_spec.parse(self.data, default_scheme="https")
237        if self.scheme in ("http3", "dtls", "udp", "quic"):
238            self.transport_protocol = UDP
239        elif self.scheme in ("dns", "https"):
240            self.transport_protocol = BOTH
241        self.description = f"{self.description} to {self.data}"
242
243    @property
244    defdefault_port(self) -> int | None:
245        if self.scheme == "dns":
246            return 53
247        return super().default_port
```

A reverse proxy. This acts like a normal server, but redirects all requests to a fixed target.

description = 'reverse proxy'

The mode description that will be used in server logs and UI.

transport\_protocol = 'tcp'

The transport protocol used by this mode's server.

scheme: Literal\['http', 'https', 'http3', 'tls', 'dtls', 'tcp', 'udp', 'dns', 'quic']

default\_port: int | None View Source

```
243    @property
244    defdefault_port(self) -> int | None:
245        if self.scheme == "dns":
246            return 53
247        return super().default_port
```

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

type\_name: ClassVar\[str] = 'reverse'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class Socks5Mode([ProxyMode](#ProxyMode)): View Source

[](#Socks5Mode)

```
250classSocks5Mode(ProxyMode):
251"""A SOCKSv5 proxy."""
252
253    description = "SOCKS v5 proxy"
254    default_port = 1080
255    transport_protocol = TCP
256
257    def__post_init__(self) -> None:
258        _check_empty(self.data)
```

A SOCKSv5 proxy.

description = 'SOCKS v5 proxy'

The mode description that will be used in server logs and UI.

default\_port = 1080

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

transport\_protocol = 'tcp'

The transport protocol used by this mode's server.

type\_name: ClassVar\[str] = 'socks5'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class DnsMode([ProxyMode](#ProxyMode)): View Source

[](#DnsMode)

```
261classDnsMode(ProxyMode):
262"""A DNS server."""
263
264    description = "DNS server"
265    default_port = 53
266    transport_protocol = BOTH
267
268    def__post_init__(self) -> None:
269        _check_empty(self.data)
```

A DNS server.

description = 'DNS server'

The mode description that will be used in server logs and UI.

default\_port = 53

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

transport\_protocol = 'both'

The transport protocol used by this mode's server.

type\_name: ClassVar\[str] = 'dns'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class WireGuardMode([ProxyMode](#ProxyMode)): View Source

[](#WireGuardMode)

```
285classWireGuardMode(ProxyMode):
286"""Proxy Server based on WireGuard"""
287
288    description = "WireGuard server"
289    default_port = 51820
290    transport_protocol = UDP
291
292    def__post_init__(self) -> None:
293        pass
```

Proxy Server based on WireGuard

description = 'WireGuard server'

The mode description that will be used in server logs and UI.

default\_port = 51820

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

transport\_protocol = 'udp'

The transport protocol used by this mode's server.

type\_name: ClassVar\[str] = 'wireguard'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class LocalMode([ProxyMode](#ProxyMode)): View Source

[](#LocalMode)

```
296classLocalMode(ProxyMode):
297"""OS-level transparent proxy."""
298
299    description = "Local redirector"
300    transport_protocol = BOTH
301    default_port = None
302
303    def__post_init__(self) -> None:
304        # should not raise
305        mitmproxy_rs.local.LocalRedirector.describe_spec(self.data)
```

OS-level transparent proxy.

description = 'Local redirector'

The mode description that will be used in server logs and UI.

transport\_protocol = 'both'

The transport protocol used by this mode's server.

default\_port = None

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

type\_name: ClassVar\[str] = 'local'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class TunMode([ProxyMode](#ProxyMode)): View Source

[](#TunMode)

```
308classTunMode(ProxyMode):
309"""A Tun interface."""
310
311    description = "TUN interface"
312    default_port = None
313    transport_protocol = BOTH
314
315    def__post_init__(self) -> None:
316        invalid_tun_name = self.data and (
317            # The Rust side is Linux only for the moment, but eventually we may need this.
318            platform.system() == "Darwin" and not re.match(r"^utun\d+$", self.data)
319        )
320        if invalid_tun_name:  # pragma: no cover
321            raise ValueError(
322                f"Invalid tun name: {self.data}. "
323                f"On macOS, the tun name must be the form utunx where x is a number, such as utun3."
324            )
```

A Tun interface.

description = 'TUN interface'

The mode description that will be used in server logs and UI.

default\_port = None

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

transport\_protocol = 'both'

The transport protocol used by this mode's server.

type\_name: ClassVar\[str] = 'tun'

The unique name for this proxy mode, e.g. "regular" or "reverse".

class OsProxyMode([ProxyMode](#ProxyMode)): View Source

[](#OsProxyMode)

```
327classOsProxyMode(ProxyMode):  # pragma: no cover
328"""Deprecated alias for LocalMode"""
329
330    description = "Deprecated alias for LocalMode"
331    transport_protocol = BOTH
332    default_port = None
333
334    def__post_init__(self) -> None:
335        raise ValueError(
336            "osproxy mode has been renamed to local mode. Thanks for trying our experimental features!"
337        )
```

Deprecated alias for LocalMode

description = 'Deprecated alias for LocalMode'

The mode description that will be used in server logs and UI.

transport\_protocol = 'both'

The transport protocol used by this mode's server.

default\_port = None

Default listen port of servers for this mode, see `ProxyMode.listen_port()`.

type\_name: ClassVar\[str] = 'osproxy'

The unique name for this proxy mode, e.g. "regular" or "reverse".