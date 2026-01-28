---
title: mitmproxy.connection
url: https://docs.mitmproxy.org/stable/api/mitmproxy/connection.html
source: crawler
fetched_at: 2026-01-28T15:03:23.229922489-03:00
rendered_js: false
word_count: 3983
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/connection.py) View Source

```
  1importdataclasses
  2importtime
  3importuuid
  4importwarnings
  5fromabcimport ABCMeta
  6fromcollections.abcimport Sequence
  7fromdataclassesimport dataclass
  8fromdataclassesimport field
  9fromenumimport Flag
 10fromtypingimport Literal
 11
 12frommitmproxyimport certs
 13frommitmproxy.coretypesimport serializable
 14frommitmproxy.netimport server_spec
 15frommitmproxy.proxyimport mode_specs
 16frommitmproxy.utilsimport human
 17
 18
 19classConnectionState(Flag):
 20"""The current state of the underlying socket."""
 21
 22    CLOSED = 0
 23    CAN_READ = 1
 24    CAN_WRITE = 2
 25    OPEN = CAN_READ | CAN_WRITE
 26
 27
 28TransportProtocol = Literal["tcp", "udp"]
 29
 30# https://docs.openssl.org/master/man3/SSL_get_version/#return-values
 31TlsVersion = Literal[
 32    "SSLv3",
 33    "TLSv1",
 34    "TLSv1.1",
 35    "TLSv1.2",
 36    "TLSv1.3",
 37    "DTLSv0.9",
 38    "DTLSv1",
 39    "DTLSv1.2",
 40    "QUICv1",
 41]
 42
 43# practically speaking we may have IPv6 addresses with flowinfo and scope_id,
 44# but type checking isn't good enough to properly handle tuple unions.
 45# this version at least provides useful type checking messages.
 46Address = tuple[str, int]
 47
 48
 49@dataclass(kw_only=True)
 50classConnection(serializable.SerializableDataclass, metaclass=ABCMeta):
 51"""
 52    Base class for client and server connections.
 53
 54    The connection object only exposes metadata about the connection, but not the underlying socket object.
 55    This is intentional, all I/O should be handled by `mitmproxy.proxy.server` exclusively.
 56    """
 57
 58    peername: Address | None
 59"""The remote's `(ip, port)` tuple for this connection."""
 60    sockname: Address | None
 61"""Our local `(ip, port)` tuple for this connection."""
 62
 63    state: ConnectionState = field(
 64        default=ConnectionState.CLOSED, metadata={"serialize": False}
 65    )
 66"""The current connection state."""
 67
 68    # all connections have a unique id. While
 69    # f.client_conn == f2.client_conn already holds true for live flows (where we have object identity),
 70    # we also want these semantics for recorded flows.
 71    id: str = field(default_factory=lambda: str(uuid.uuid4()))
 72"""A unique UUID to identify the connection."""
 73    transport_protocol: TransportProtocol = field(default="tcp")
 74"""The connection protocol in use."""
 75    error: str | None = None
 76"""
 77    A string describing a general error with connections to this address.
 78
 79    The purpose of this property is to signal that new connections to the particular endpoint should not be attempted,
 80    for example because it uses an untrusted TLS certificate. Regular (unexpected) disconnects do not set the error
 81    property. This property is only reused per client connection.
 82    """
 83
 84    tls: bool = False
 85"""
 86    `True` if TLS should be established, `False` otherwise.
 87    Note that this property only describes if a connection should eventually be protected using TLS.
 88    To check if TLS has already been established, use `Connection.tls_established`.
 89    """
 90    certificate_list: Sequence[certs.Cert] = ()
 91"""
 92    The TLS certificate list as sent by the peer.
 93    The first certificate is the end-entity certificate.
 94
 95    > [RFC 8446] Prior to TLS 1.3, "certificate_list" ordering required each
 96    > certificate to certify the one immediately preceding it; however,
 97    > some implementations allowed some flexibility.  Servers sometimes
 98    > send both a current and deprecated intermediate for transitional
 99    > purposes, and others are simply configured incorrectly, but these
100    > cases can nonetheless be validated properly.  For maximum
101    > compatibility, all implementations SHOULD be prepared to handle
102    > potentially extraneous certificates and arbitrary orderings from any
103    > TLS version, with the exception of the end-entity certificate which
104    > MUST be first.
105    """
106    alpn: bytes | None = None
107"""The application-layer protocol as negotiated using
108    [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation)."""
109    alpn_offers: Sequence[bytes] = ()
110"""The ALPN offers as sent in the ClientHello."""
111    # we may want to add SSL_CIPHER_description here, but that's currently not exposed by cryptography
112    cipher: str | None = None
113"""The active cipher name as returned by OpenSSL's `SSL_CIPHER_get_name`."""
114    cipher_list: Sequence[str] = ()
115"""Ciphers accepted by the proxy server on this connection."""
116    tls_version: TlsVersion | None = None
117"""The active TLS version."""
118    sni: str | None = None
119"""
120    The [Server Name Indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication) sent in the ClientHello.
121    """
122
123    timestamp_start: float | None = None
124    timestamp_end: float | None = None
125"""*Timestamp:* Connection has been closed."""
126    timestamp_tls_setup: float | None = None
127"""*Timestamp:* TLS handshake has been completed successfully."""
128
129    @property
130    defconnected(self) -> bool:
131"""*Read-only:* `True` if Connection.state is ConnectionState.OPEN, `False` otherwise."""
132        return self.state is ConnectionState.OPEN
133
134    @property
135    deftls_established(self) -> bool:
136"""*Read-only:* `True` if TLS has been established, `False` otherwise."""
137        return self.timestamp_tls_setup is not None
138
139    def__eq__(self, other):
140        if isinstance(other, Connection):
141            return self.id == other.id
142        return False
143
144    def__hash__(self):
145        return hash(self.id)
146
147    def__repr__(self):
148        attrs = {
149            # ensure these come first.
150            "id": None,
151            "address": None,
152        }
153        for f in dataclasses.fields(self):
154            val = getattr(self, f.name)
155            if val != f.default:
156                if f.name == "cipher_list":
157                    val = f"<{len(val)} ciphers>"
158                elif f.name == "id":
159                    val = f"…{val[-6:]}"
160                attrs[f.name] = val
161        return f"{type(self).__name__}({attrs!r})"
162
163    @property
164    defalpn_proto_negotiated(self) -> bytes | None:  # pragma: no cover
165"""*Deprecated:* An outdated alias for Connection.alpn."""
166        warnings.warn(
167            "Connection.alpn_proto_negotiated is deprecated, use Connection.alpn instead.",
168            DeprecationWarning,
169            stacklevel=2,
170        )
171        return self.alpn
172
173
174@dataclass(eq=False, repr=False, kw_only=True)
175classClient(Connection):  # type: ignore[override]
176"""A connection between a client and mitmproxy."""
177
178    peername: Address
179"""The client's address."""
180    sockname: Address
181"""The local address we received this connection on."""
182
183    mitmcert: certs.Cert | None = None
184"""
185    The certificate used by mitmproxy to establish TLS with the client.
186    """
187
188    proxy_mode: mode_specs.ProxyMode = field(
189        default=mode_specs.ProxyMode.parse("regular")
190    )
191"""The proxy server type this client has been connecting to."""
192
193    timestamp_start: float = field(default_factory=time.time)
194"""*Timestamp:* TCP SYN received"""
195
196    def__str__(self):
197        if self.alpn:
198            tls_state = f", alpn={self.alpn.decode(errors='replace')}"
199        elif self.tls_established:
200            tls_state = ", tls"
201        else:
202            tls_state = ""
203        state = self.state.name
204        assert state
205        return f"Client({human.format_address(self.peername)}, state={state.lower()}{tls_state})"
206
207    @property
208    defaddress(self):  # pragma: no cover
209"""*Deprecated:* An outdated alias for Client.peername."""
210        warnings.warn(
211            "Client.address is deprecated, use Client.peername instead.",
212            DeprecationWarning,
213            stacklevel=2,
214        )
215        return self.peername
216
217    @address.setter
218    defaddress(self, x):  # pragma: no cover
219        warnings.warn(
220            "Client.address is deprecated, use Client.peername instead.",
221            DeprecationWarning,
222            stacklevel=2,
223        )
224        self.peername = x
225
226    @property
227    defcipher_name(self) -> str | None:  # pragma: no cover
228"""*Deprecated:* An outdated alias for Connection.cipher."""
229        warnings.warn(
230            "Client.cipher_name is deprecated, use Client.cipher instead.",
231            DeprecationWarning,
232            stacklevel=2,
233        )
234        return self.cipher
235
236    @property
237    defclientcert(self) -> certs.Cert | None:  # pragma: no cover
238"""*Deprecated:* An outdated alias for Connection.certificate_list[0]."""
239        warnings.warn(
240            "Client.clientcert is deprecated, use Client.certificate_list instead.",
241            DeprecationWarning,
242            stacklevel=2,
243        )
244        if self.certificate_list:
245            return self.certificate_list[0]
246        else:
247            return None
248
249    @clientcert.setter
250    defclientcert(self, val):  # pragma: no cover
251        warnings.warn(
252            "Client.clientcert is deprecated, use Client.certificate_list instead.",
253            DeprecationWarning,
254            stacklevel=2,
255        )
256        if val:
257            self.certificate_list = [val]
258        else:
259            self.certificate_list = []
260
261
262@dataclass(eq=False, repr=False, kw_only=True)
263classServer(Connection):
264"""A connection between mitmproxy and an upstream server."""
265
266    address: Address | None  # type: ignore
267"""
268    The server's `(host, port)` address tuple.
269
270    The host can either be a domain or a plain IP address.
271    Which of those two will be present depends on the proxy mode and the client.
272    For explicit proxies, this value will reflect what the client instructs mitmproxy to connect to.
273    For example, if the client starts off a connection with `CONNECT example.com HTTP/1.1`, it will be `example.com`.
274    For transparent proxies such as WireGuard mode, this value will be an IP address.
275    """
276
277    peername: Address | None = None
278"""
279    The server's resolved `(ip, port)` tuple. Will be set during connection establishment.
280    May be `None` in upstream proxy mode when the address is resolved by the upstream proxy only.
281    """
282    sockname: Address | None = None
283
284    timestamp_start: float | None = None
285"""
286    *Timestamp:* Connection establishment started.
287
288    For IP addresses, this corresponds to sending a TCP SYN; for domains, this corresponds to starting a DNS lookup.
289    """
290    timestamp_tcp_setup: float | None = None
291"""*Timestamp:* TCP ACK received."""
292
293    via: server_spec.ServerSpec | None = None
294"""An optional proxy server specification via which the connection should be established."""
295
296    def__str__(self):
297        if self.alpn:
298            tls_state = f", alpn={self.alpn.decode(errors='replace')}"
299        elif self.tls_established:
300            tls_state = ", tls"
301        else:
302            tls_state = ""
303        if self.sockname:
304            local_port = f", src_port={self.sockname[1]}"
305        else:
306            local_port = ""
307        state = self.state.name
308        assert state
309        return f"Server({human.format_address(self.address)}, state={state.lower()}{tls_state}{local_port})"
310
311    def__setattr__(self, name, value):
312        if name in ("address", "via"):
313            connection_open = (
314                self.__dict__.get("state", ConnectionState.CLOSED)
315                is ConnectionState.OPEN
316            )
317            # assigning the current value is okay, that may be an artifact of calling .set_state().
318            attr_changed = self.__dict__.get(name) != value
319            if connection_open and attr_changed:
320                raise RuntimeError(f"Cannot change server.{name} on open connection.")
321        return super().__setattr__(name, value)
322
323    @property
324    defip_address(self) -> Address | None:  # pragma: no cover
325"""*Deprecated:* An outdated alias for `Server.peername`."""
326        warnings.warn(
327            "Server.ip_address is deprecated, use Server.peername instead.",
328            DeprecationWarning,
329            stacklevel=2,
330        )
331        return self.peername
332
333    @property
334    defcert(self) -> certs.Cert | None:  # pragma: no cover
335"""*Deprecated:* An outdated alias for `Connection.certificate_list[0]`."""
336        warnings.warn(
337            "Server.cert is deprecated, use Server.certificate_list instead.",
338            DeprecationWarning,
339            stacklevel=2,
340        )
341        if self.certificate_list:
342            return self.certificate_list[0]
343        else:
344            return None
345
346    @cert.setter
347    defcert(self, val):  # pragma: no cover
348        warnings.warn(
349            "Server.cert is deprecated, use Server.certificate_list instead.",
350            DeprecationWarning,
351            stacklevel=2,
352        )
353        if val:
354            self.certificate_list = [val]
355        else:
356            self.certificate_list = []
357
358
359__all__ = ["Connection", "Client", "Server", "ConnectionState"]
```

@dataclass(kw\_only=True)

class Connection(mitmproxy.coretypes.serializable.SerializableDataclass): View Source

[](#Connection)

```
 50@dataclass(kw_only=True)
 51classConnection(serializable.SerializableDataclass, metaclass=ABCMeta):
 52"""
 53    Base class for client and server connections.
 54
 55    The connection object only exposes metadata about the connection, but not the underlying socket object.
 56    This is intentional, all I/O should be handled by `mitmproxy.proxy.server` exclusively.
 57    """
 58
 59    peername: Address | None
 60"""The remote's `(ip, port)` tuple for this connection."""
 61    sockname: Address | None
 62"""Our local `(ip, port)` tuple for this connection."""
 63
 64    state: ConnectionState = field(
 65        default=ConnectionState.CLOSED, metadata={"serialize": False}
 66    )
 67"""The current connection state."""
 68
 69    # all connections have a unique id. While
 70    # f.client_conn == f2.client_conn already holds true for live flows (where we have object identity),
 71    # we also want these semantics for recorded flows.
 72    id: str = field(default_factory=lambda: str(uuid.uuid4()))
 73"""A unique UUID to identify the connection."""
 74    transport_protocol: TransportProtocol = field(default="tcp")
 75"""The connection protocol in use."""
 76    error: str | None = None
 77"""
 78    A string describing a general error with connections to this address.
 79
 80    The purpose of this property is to signal that new connections to the particular endpoint should not be attempted,
 81    for example because it uses an untrusted TLS certificate. Regular (unexpected) disconnects do not set the error
 82    property. This property is only reused per client connection.
 83    """
 84
 85    tls: bool = False
 86"""
 87    `True` if TLS should be established, `False` otherwise.
 88    Note that this property only describes if a connection should eventually be protected using TLS.
 89    To check if TLS has already been established, use `Connection.tls_established`.
 90    """
 91    certificate_list: Sequence[certs.Cert] = ()
 92"""
 93    The TLS certificate list as sent by the peer.
 94    The first certificate is the end-entity certificate.
 95
 96    > [RFC 8446] Prior to TLS 1.3, "certificate_list" ordering required each
 97    > certificate to certify the one immediately preceding it; however,
 98    > some implementations allowed some flexibility.  Servers sometimes
 99    > send both a current and deprecated intermediate for transitional
100    > purposes, and others are simply configured incorrectly, but these
101    > cases can nonetheless be validated properly.  For maximum
102    > compatibility, all implementations SHOULD be prepared to handle
103    > potentially extraneous certificates and arbitrary orderings from any
104    > TLS version, with the exception of the end-entity certificate which
105    > MUST be first.
106    """
107    alpn: bytes | None = None
108"""The application-layer protocol as negotiated using
109    [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation)."""
110    alpn_offers: Sequence[bytes] = ()
111"""The ALPN offers as sent in the ClientHello."""
112    # we may want to add SSL_CIPHER_description here, but that's currently not exposed by cryptography
113    cipher: str | None = None
114"""The active cipher name as returned by OpenSSL's `SSL_CIPHER_get_name`."""
115    cipher_list: Sequence[str] = ()
116"""Ciphers accepted by the proxy server on this connection."""
117    tls_version: TlsVersion | None = None
118"""The active TLS version."""
119    sni: str | None = None
120"""
121    The [Server Name Indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication) sent in the ClientHello.
122    """
123
124    timestamp_start: float | None = None
125    timestamp_end: float | None = None
126"""*Timestamp:* Connection has been closed."""
127    timestamp_tls_setup: float | None = None
128"""*Timestamp:* TLS handshake has been completed successfully."""
129
130    @property
131    defconnected(self) -> bool:
132"""*Read-only:* `True` if Connection.state is ConnectionState.OPEN, `False` otherwise."""
133        return self.state is ConnectionState.OPEN
134
135    @property
136    deftls_established(self) -> bool:
137"""*Read-only:* `True` if TLS has been established, `False` otherwise."""
138        return self.timestamp_tls_setup is not None
139
140    def__eq__(self, other):
141        if isinstance(other, Connection):
142            return self.id == other.id
143        return False
144
145    def__hash__(self):
146        return hash(self.id)
147
148    def__repr__(self):
149        attrs = {
150            # ensure these come first.
151            "id": None,
152            "address": None,
153        }
154        for f in dataclasses.fields(self):
155            val = getattr(self, f.name)
156            if val != f.default:
157                if f.name == "cipher_list":
158                    val = f"<{len(val)} ciphers>"
159                elif f.name == "id":
160                    val = f"…{val[-6:]}"
161                attrs[f.name] = val
162        return f"{type(self).__name__}({attrs!r})"
163
164    @property
165    defalpn_proto_negotiated(self) -> bytes | None:  # pragma: no cover
166"""*Deprecated:* An outdated alias for Connection.alpn."""
167        warnings.warn(
168            "Connection.alpn_proto_negotiated is deprecated, use Connection.alpn instead.",
169            DeprecationWarning,
170            stacklevel=2,
171        )
172        return self.alpn
```

Base class for client and server connections.

The connection object only exposes metadata about the connection, but not the underlying socket object. This is intentional, all I/O should be handled by `mitmproxy.proxy.server` exclusively.

Connection( \*, peername: tuple\[str, int] | None, sockname: tuple\[str, int] | None, state: [ConnectionState](#ConnectionState) = &lt;[ConnectionState.CLOSED](#ConnectionState.CLOSED): 0&gt;, id: str = &lt;factory&gt;, transport\_protocol: Literal\['tcp', 'udp'] = 'tcp', error: str | None = None, tls: bool = False, certificate\_list: Sequence\[[mitmproxy.certs.Cert](https://docs.mitmproxy.org/stable/api/mitmproxy/certs.html#Cert)] = (), alpn: bytes | None = None, alpn\_offers: Sequence\[bytes] = (), cipher: str | None = None, cipher\_list: Sequence\[str] = (), tls\_version: Literal\['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3', 'DTLSv0.9', 'DTLSv1', 'DTLSv1.2', 'QUICv1'] | None = None, sni: str | None = None, timestamp\_start: float | None = None, timestamp\_end: float | None = None, timestamp\_tls\_setup: float | None = None)

peername: tuple\[str, int] | None

The remote's `(ip, port)` tuple for this connection.

sockname: tuple\[str, int] | None

Our local `(ip, port)` tuple for this connection.

state: [ConnectionState](#ConnectionState) = &lt;[ConnectionState.CLOSED](#ConnectionState.CLOSED): 0&gt;

The current connection state.

id: str

A unique UUID to identify the connection.

transport\_protocol: Literal\['tcp', 'udp'] = 'tcp'

The connection protocol in use.

error: str | None = None

A string describing a general error with connections to this address.

The purpose of this property is to signal that new connections to the particular endpoint should not be attempted, for example because it uses an untrusted TLS certificate. Regular (unexpected) disconnects do not set the error property. This property is only reused per client connection.

tls: bool = False

`True` if TLS should be established, `False` otherwise. Note that this property only describes if a connection should eventually be protected using TLS. To check if TLS has already been established, use `Connection.tls_established`.

The TLS certificate list as sent by the peer. The first certificate is the end-entity certificate.

> \[RFC 8446] Prior to TLS 1.3, "certificate\_list" ordering required each certificate to certify the one immediately preceding it; however, some implementations allowed some flexibility. Servers sometimes send both a current and deprecated intermediate for transitional purposes, and others are simply configured incorrectly, but these cases can nonetheless be validated properly. For maximum compatibility, all implementations SHOULD be prepared to handle potentially extraneous certificates and arbitrary orderings from any TLS version, with the exception of the end-entity certificate which MUST be first.

alpn: bytes | None = None

The application-layer protocol as negotiated using [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation).

alpn\_offers: Sequence\[bytes] = ()

The ALPN offers as sent in the ClientHello.

cipher: str | None = None

The active cipher name as returned by OpenSSL's `SSL_CIPHER_get_name`.

cipher\_list: Sequence\[str] = ()

Ciphers accepted by the proxy server on this connection.

tls\_version: Literal\['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3', 'DTLSv0.9', 'DTLSv1', 'DTLSv1.2', 'QUICv1'] | None = None

The active TLS version.

timestamp\_start: float | None = None

timestamp\_end: float | None = None

*Timestamp:* Connection has been closed.

timestamp\_tls\_setup: float | None = None

*Timestamp:* TLS handshake has been completed successfully.

connected: bool View Source

```
130    @property
131    defconnected(self) -> bool:
132"""*Read-only:* `True` if Connection.state is ConnectionState.OPEN, `False` otherwise."""
133        return self.state is ConnectionState.OPEN
```

*Read-only:* `True` if [Connection.state](#Connection.state) is [ConnectionState.OPEN](#ConnectionState.OPEN), `False` otherwise.

tls\_established: bool View Source

```
135    @property
136    deftls_established(self) -> bool:
137"""*Read-only:* `True` if TLS has been established, `False` otherwise."""
138        return self.timestamp_tls_setup is not None
```

*Read-only:* `True` if TLS has been established, `False` otherwise.

alpn\_proto\_negotiated: bytes | None View Source

```
164    @property
165    defalpn_proto_negotiated(self) -> bytes | None:  # pragma: no cover
166"""*Deprecated:* An outdated alias for Connection.alpn."""
167        warnings.warn(
168            "Connection.alpn_proto_negotiated is deprecated, use Connection.alpn instead.",
169            DeprecationWarning,
170            stacklevel=2,
171        )
172        return self.alpn
```

*Deprecated:* An outdated alias for [Connection.alpn](#Connection.alpn).

@dataclass(eq=False, repr=False, kw\_only=True)

class Client([Connection](#Connection)): View Source

[](#Client)

```
175@dataclass(eq=False, repr=False, kw_only=True)
176classClient(Connection):  # type: ignore[override]
177"""A connection between a client and mitmproxy."""
178
179    peername: Address
180"""The client's address."""
181    sockname: Address
182"""The local address we received this connection on."""
183
184    mitmcert: certs.Cert | None = None
185"""
186    The certificate used by mitmproxy to establish TLS with the client.
187    """
188
189    proxy_mode: mode_specs.ProxyMode = field(
190        default=mode_specs.ProxyMode.parse("regular")
191    )
192"""The proxy server type this client has been connecting to."""
193
194    timestamp_start: float = field(default_factory=time.time)
195"""*Timestamp:* TCP SYN received"""
196
197    def__str__(self):
198        if self.alpn:
199            tls_state = f", alpn={self.alpn.decode(errors='replace')}"
200        elif self.tls_established:
201            tls_state = ", tls"
202        else:
203            tls_state = ""
204        state = self.state.name
205        assert state
206        return f"Client({human.format_address(self.peername)}, state={state.lower()}{tls_state})"
207
208    @property
209    defaddress(self):  # pragma: no cover
210"""*Deprecated:* An outdated alias for Client.peername."""
211        warnings.warn(
212            "Client.address is deprecated, use Client.peername instead.",
213            DeprecationWarning,
214            stacklevel=2,
215        )
216        return self.peername
217
218    @address.setter
219    defaddress(self, x):  # pragma: no cover
220        warnings.warn(
221            "Client.address is deprecated, use Client.peername instead.",
222            DeprecationWarning,
223            stacklevel=2,
224        )
225        self.peername = x
226
227    @property
228    defcipher_name(self) -> str | None:  # pragma: no cover
229"""*Deprecated:* An outdated alias for Connection.cipher."""
230        warnings.warn(
231            "Client.cipher_name is deprecated, use Client.cipher instead.",
232            DeprecationWarning,
233            stacklevel=2,
234        )
235        return self.cipher
236
237    @property
238    defclientcert(self) -> certs.Cert | None:  # pragma: no cover
239"""*Deprecated:* An outdated alias for Connection.certificate_list[0]."""
240        warnings.warn(
241            "Client.clientcert is deprecated, use Client.certificate_list instead.",
242            DeprecationWarning,
243            stacklevel=2,
244        )
245        if self.certificate_list:
246            return self.certificate_list[0]
247        else:
248            return None
249
250    @clientcert.setter
251    defclientcert(self, val):  # pragma: no cover
252        warnings.warn(
253            "Client.clientcert is deprecated, use Client.certificate_list instead.",
254            DeprecationWarning,
255            stacklevel=2,
256        )
257        if val:
258            self.certificate_list = [val]
259        else:
260            self.certificate_list = []
```

A connection between a client and mitmproxy.

Client( \*, peername: tuple\[str, int], sockname: tuple\[str, int], state: [ConnectionState](#ConnectionState) = &lt;[ConnectionState.CLOSED](#ConnectionState.CLOSED): 0&gt;, id: str = &lt;factory&gt;, transport\_protocol: Literal\['tcp', 'udp'] = 'tcp', error: str | None = None, tls: bool = False, certificate\_list: Sequence\[[mitmproxy.certs.Cert](https://docs.mitmproxy.org/stable/api/mitmproxy/certs.html#Cert)] = (), alpn: bytes | None = None, alpn\_offers: Sequence\[bytes] = (), cipher: str | None = None, cipher\_list: Sequence\[str] = (), tls\_version: Literal\['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3', 'DTLSv0.9', 'DTLSv1', 'DTLSv1.2', 'QUICv1'] | None = None, sni: str | None = None, timestamp\_start: float = &lt;factory&gt;, timestamp\_end: float | None = None, timestamp\_tls\_setup: float | None = None, mitmcert: [mitmproxy.certs.Cert](https://docs.mitmproxy.org/stable/api/mitmproxy/certs.html#Cert) | None = None, proxy\_mode: [mitmproxy.proxy.mode\_specs.ProxyMode](https://docs.mitmproxy.org/stable/api/mitmproxy/proxy/mode_specs.html#ProxyMode) = ProxyMode.parse('regular'))

peername: tuple\[str, int]

The client's address.

sockname: tuple\[str, int]

The local address we received this connection on.

The certificate used by mitmproxy to establish TLS with the client.

The proxy server type this client has been connecting to.

timestamp\_start: float = None

*Timestamp:* TCP SYN received

address View Source

```
208    @property
209    defaddress(self):  # pragma: no cover
210"""*Deprecated:* An outdated alias for Client.peername."""
211        warnings.warn(
212            "Client.address is deprecated, use Client.peername instead.",
213            DeprecationWarning,
214            stacklevel=2,
215        )
216        return self.peername
```

*Deprecated:* An outdated alias for [Client.peername](#Client.peername).

cipher\_name: str | None View Source

```
227    @property
228    defcipher_name(self) -> str | None:  # pragma: no cover
229"""*Deprecated:* An outdated alias for Connection.cipher."""
230        warnings.warn(
231            "Client.cipher_name is deprecated, use Client.cipher instead.",
232            DeprecationWarning,
233            stacklevel=2,
234        )
235        return self.cipher
```

*Deprecated:* An outdated alias for [Connection.cipher](#Connection.cipher).

```
237    @property
238    defclientcert(self) -> certs.Cert | None:  # pragma: no cover
239"""*Deprecated:* An outdated alias for Connection.certificate_list[0]."""
240        warnings.warn(
241            "Client.clientcert is deprecated, use Client.certificate_list instead.",
242            DeprecationWarning,
243            stacklevel=2,
244        )
245        if self.certificate_list:
246            return self.certificate_list[0]
247        else:
248            return None
```

*Deprecated:* An outdated alias for [Connection.certificate\_list](#Connection.certificate_list)\[0].

@dataclass(eq=False, repr=False, kw\_only=True)

class Server([Connection](#Connection)): View Source

[](#Server)

```
263@dataclass(eq=False, repr=False, kw_only=True)
264classServer(Connection):
265"""A connection between mitmproxy and an upstream server."""
266
267    address: Address | None  # type: ignore
268"""
269    The server's `(host, port)` address tuple.
270
271    The host can either be a domain or a plain IP address.
272    Which of those two will be present depends on the proxy mode and the client.
273    For explicit proxies, this value will reflect what the client instructs mitmproxy to connect to.
274    For example, if the client starts off a connection with `CONNECT example.com HTTP/1.1`, it will be `example.com`.
275    For transparent proxies such as WireGuard mode, this value will be an IP address.
276    """
277
278    peername: Address | None = None
279"""
280    The server's resolved `(ip, port)` tuple. Will be set during connection establishment.
281    May be `None` in upstream proxy mode when the address is resolved by the upstream proxy only.
282    """
283    sockname: Address | None = None
284
285    timestamp_start: float | None = None
286"""
287    *Timestamp:* Connection establishment started.
288
289    For IP addresses, this corresponds to sending a TCP SYN; for domains, this corresponds to starting a DNS lookup.
290    """
291    timestamp_tcp_setup: float | None = None
292"""*Timestamp:* TCP ACK received."""
293
294    via: server_spec.ServerSpec | None = None
295"""An optional proxy server specification via which the connection should be established."""
296
297    def__str__(self):
298        if self.alpn:
299            tls_state = f", alpn={self.alpn.decode(errors='replace')}"
300        elif self.tls_established:
301            tls_state = ", tls"
302        else:
303            tls_state = ""
304        if self.sockname:
305            local_port = f", src_port={self.sockname[1]}"
306        else:
307            local_port = ""
308        state = self.state.name
309        assert state
310        return f"Server({human.format_address(self.address)}, state={state.lower()}{tls_state}{local_port})"
311
312    def__setattr__(self, name, value):
313        if name in ("address", "via"):
314            connection_open = (
315                self.__dict__.get("state", ConnectionState.CLOSED)
316                is ConnectionState.OPEN
317            )
318            # assigning the current value is okay, that may be an artifact of calling .set_state().
319            attr_changed = self.__dict__.get(name) != value
320            if connection_open and attr_changed:
321                raise RuntimeError(f"Cannot change server.{name} on open connection.")
322        return super().__setattr__(name, value)
323
324    @property
325    defip_address(self) -> Address | None:  # pragma: no cover
326"""*Deprecated:* An outdated alias for `Server.peername`."""
327        warnings.warn(
328            "Server.ip_address is deprecated, use Server.peername instead.",
329            DeprecationWarning,
330            stacklevel=2,
331        )
332        return self.peername
333
334    @property
335    defcert(self) -> certs.Cert | None:  # pragma: no cover
336"""*Deprecated:* An outdated alias for `Connection.certificate_list[0]`."""
337        warnings.warn(
338            "Server.cert is deprecated, use Server.certificate_list instead.",
339            DeprecationWarning,
340            stacklevel=2,
341        )
342        if self.certificate_list:
343            return self.certificate_list[0]
344        else:
345            return None
346
347    @cert.setter
348    defcert(self, val):  # pragma: no cover
349        warnings.warn(
350            "Server.cert is deprecated, use Server.certificate_list instead.",
351            DeprecationWarning,
352            stacklevel=2,
353        )
354        if val:
355            self.certificate_list = [val]
356        else:
357            self.certificate_list = []
```

A connection between mitmproxy and an upstream server.

Server( \*, peername: tuple\[str, int] | None = None, sockname: tuple\[str, int] | None = None, state: [ConnectionState](#ConnectionState) = &lt;[ConnectionState.CLOSED](#ConnectionState.CLOSED): 0&gt;, id: str = &lt;factory&gt;, transport\_protocol: Literal\['tcp', 'udp'] = 'tcp', error: str | None = None, tls: bool = False, certificate\_list: Sequence\[[mitmproxy.certs.Cert](https://docs.mitmproxy.org/stable/api/mitmproxy/certs.html#Cert)] = (), alpn: bytes | None = None, alpn\_offers: Sequence\[bytes] = (), cipher: str | None = None, cipher\_list: Sequence\[str] = (), tls\_version: Literal\['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3', 'DTLSv0.9', 'DTLSv1', 'DTLSv1.2', 'QUICv1'] | None = None, sni: str | None = None, timestamp\_start: float | None = None, timestamp\_end: float | None = None, timestamp\_tls\_setup: float | None = None, address: tuple\[str, int] | None, timestamp\_tcp\_setup: float | None = None, via: tuple\[Literal\['http', 'https', 'http3', 'tls', 'dtls', 'tcp', 'udp', 'dns', 'quic'], tuple\[str, int]] | None = None)

address: tuple\[str, int] | None

The server's `(host, port)` address tuple.

The host can either be a domain or a plain IP address. Which of those two will be present depends on the proxy mode and the client. For explicit proxies, this value will reflect what the client instructs mitmproxy to connect to. For example, if the client starts off a connection with `CONNECT example.com HTTP/1.1`, it will be `example.com`. For transparent proxies such as WireGuard mode, this value will be an IP address.

peername: tuple\[str, int] | None = None

The server's resolved `(ip, port)` tuple. Will be set during connection establishment. May be `None` in upstream proxy mode when the address is resolved by the upstream proxy only.

sockname: tuple\[str, int] | None = None

Our local `(ip, port)` tuple for this connection.

timestamp\_start: float | None = None

*Timestamp:* Connection establishment started.

For IP addresses, this corresponds to sending a TCP SYN; for domains, this corresponds to starting a DNS lookup.

timestamp\_tcp\_setup: float | None = None

*Timestamp:* TCP ACK received.

via: tuple\[Literal\['http', 'https', 'http3', 'tls', 'dtls', 'tcp', 'udp', 'dns', 'quic'], tuple\[str, int]] | None = None

An optional proxy server specification via which the connection should be established.

ip\_address: tuple\[str, int] | None View Source

```
324    @property
325    defip_address(self) -> Address | None:  # pragma: no cover
326"""*Deprecated:* An outdated alias for `Server.peername`."""
327        warnings.warn(
328            "Server.ip_address is deprecated, use Server.peername instead.",
329            DeprecationWarning,
330            stacklevel=2,
331        )
332        return self.peername
```

*Deprecated:* An outdated alias for `Server.peername`.

```
334    @property
335    defcert(self) -> certs.Cert | None:  # pragma: no cover
336"""*Deprecated:* An outdated alias for `Connection.certificate_list[0]`."""
337        warnings.warn(
338            "Server.cert is deprecated, use Server.certificate_list instead.",
339            DeprecationWarning,
340            stacklevel=2,
341        )
342        if self.certificate_list:
343            return self.certificate_list[0]
344        else:
345            return None
```

*Deprecated:* An outdated alias for `Connection.certificate_list[0]`.

class ConnectionState(enum.Flag): View Source

[](#ConnectionState)

```
20classConnectionState(Flag):
21"""The current state of the underlying socket."""
22
23    CLOSED = 0
24    CAN_READ = 1
25    CAN_WRITE = 2
26    OPEN = CAN_READ | CAN_WRITE
```

The current state of the underlying socket.

CLOSED = &lt;[ConnectionState.CLOSED](#ConnectionState.CLOSED): 0&gt;

CAN\_READ = &lt;[ConnectionState.CAN\_READ](#ConnectionState.CAN_READ): 1&gt;

CAN\_WRITE = &lt;[ConnectionState.CAN\_WRITE](#ConnectionState.CAN_WRITE): 2&gt;

OPEN = &lt;[ConnectionState.OPEN](#ConnectionState.OPEN): 3&gt;