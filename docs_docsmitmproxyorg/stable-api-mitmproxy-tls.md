---
title: mitmproxy.tls
url: https://docs.mitmproxy.org/stable/api/mitmproxy/tls.html
source: crawler
fetched_at: 2026-01-28T15:01:15.913878751-03:00
rendered_js: false
word_count: 1821
summary: This document explains the ClientHello class in mitmproxy, which parses and handles TLS ClientHello messages, including properties like cipher suites, SNI, and ALPN protocols.
tags:
    - tls-clienthello
    - mitmproxy
    - sni
    - alpn
    - dtls
    - cipher-suites
category: reference
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/tls.py) View Source

```
  1importio
  2fromdataclassesimport dataclass
  3
  4fromkaitaistructimport KaitaiStream
  5fromOpenSSLimport SSL
  6
  7frommitmproxyimport connection
  8frommitmproxy.contrib.kaitaistructimport dtls_client_hello
  9frommitmproxy.contrib.kaitaistructimport tls_client_hello
 10frommitmproxy.netimport check
 11frommitmproxy.proxyimport context
 12
 13
 14classClientHello:
 15"""
 16    A TLS ClientHello is the first message sent by the client when initiating TLS.
 17    """
 18
 19    _raw_bytes: bytes
 20
 21    def__init__(self, raw_client_hello: bytes, dtls: bool = False):
 22"""Create a TLS ClientHello object from raw bytes."""
 23        self._raw_bytes = raw_client_hello
 24        if dtls:
 25            self._client_hello = dtls_client_hello.DtlsClientHello(
 26                KaitaiStream(io.BytesIO(raw_client_hello))
 27            )
 28        else:
 29            self._client_hello = tls_client_hello.TlsClientHello(
 30                KaitaiStream(io.BytesIO(raw_client_hello))
 31            )
 32
 33    defraw_bytes(self, wrap_in_record: bool = True) -> bytes:
 34"""
 35        The raw ClientHello bytes as seen on the wire.
 36
 37        If `wrap_in_record` is True, the ClientHello will be wrapped in a synthetic TLS record
 38        (`0x160303 + len(chm) + 0x01 + len(ch)`), which is the format expected by some tools.
 39        The synthetic record assumes TLS version (`0x0303`), which may be different from what has been sent over the
 40        wire. JA3 hashes are unaffected by this as they only use the TLS version from the ClientHello data structure.
 41
 42        A future implementation may return not just the exact ClientHello, but also the exact record(s) as seen on the
 43        wire.
 44        """
 45        if isinstance(self._client_hello, dtls_client_hello.DtlsClientHello):
 46            raise NotImplementedError
 47
 48        if wrap_in_record:
 49            return (
 50                # record layer
 51                b"\x16\x03\x03"
 52                + (len(self._raw_bytes) + 4).to_bytes(2, byteorder="big")
 53                +
 54                # handshake header
 55                b"\x01"
 56                + len(self._raw_bytes).to_bytes(3, byteorder="big")
 57                +
 58                # ClientHello as defined in https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2.
 59                self._raw_bytes
 60            )
 61        else:
 62            return self._raw_bytes
 63
 64    @property
 65    defcipher_suites(self) -> list[int]:
 66"""The cipher suites offered by the client (as raw ints)."""
 67        return self._client_hello.cipher_suites.cipher_suites
 68
 69    @property
 70    defsni(self) -> str | None:
 71"""
 72        The [Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication),
 73        which indicates which hostname the client wants to connect to.
 74        """
 75        if ext := getattr(self._client_hello, "extensions", None):
 76            for extension in ext.extensions:
 77                is_valid_sni_extension = (
 78                    extension.type == 0x00
 79                    and len(extension.body.server_names) == 1
 80                    and extension.body.server_names[0].name_type == 0
 81                    and check.is_valid_host(extension.body.server_names[0].host_name)
 82                )
 83                if is_valid_sni_extension:
 84                    return extension.body.server_names[0].host_name.decode("ascii")
 85        return None
 86
 87    @property
 88    defalpn_protocols(self) -> list[bytes]:
 89"""
 90        The application layer protocols offered by the client as part of the
 91        [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) TLS extension.
 92        """
 93        if ext := getattr(self._client_hello, "extensions", None):
 94            for extension in ext.extensions:
 95                if extension.type == 0x10:
 96                    return list(x.name for x in extension.body.alpn_protocols)
 97        return []
 98
 99    @property
100    defextensions(self) -> list[tuple[int, bytes]]:
101"""The raw list of extensions in the form of `(extension_type, raw_bytes)` tuples."""
102        ret = []
103        if ext := getattr(self._client_hello, "extensions", None):
104            for extension in ext.extensions:
105                body = getattr(extension, "_raw_body", extension.body)
106                ret.append((extension.type, body))
107        return ret
108
109    def__repr__(self):
110        return f"ClientHello(sni: {self.sni}, alpn_protocols: {self.alpn_protocols})"
111
112
113@dataclass
114classClientHelloData:
115"""
116    Event data for `tls_clienthello` event hooks.
117    """
118
119    context: context.Context
120"""The context object for this connection."""
121    client_hello: ClientHello
122"""The entire parsed TLS ClientHello."""
123    ignore_connection: bool = False
124"""
125    If set to `True`, do not intercept this connection and forward encrypted contents unmodified.
126    """
127    establish_server_tls_first: bool = False
128"""
129    If set to `True`, pause this handshake and establish TLS with an upstream server first.
130    This makes it possible to process the server certificate when generating an interception certificate.
131    """
132
133
134@dataclass
135classTlsData:
136"""
137    Event data for `tls_start_client`, `tls_start_server`, and `tls_handshake` event hooks.
138    """
139
140    conn: connection.Connection
141"""The affected connection."""
142    context: context.Context
143"""The context object for this connection."""
144    ssl_conn: SSL.Connection | None = None
145"""
146    The associated pyOpenSSL `SSL.Connection` object.
147    This will be set by an addon in the `tls_start_*` event hooks.
148    """
149    is_dtls: bool = False
150"""
151    If set to `True`, indicates that it is a DTLS event.
152    """
```

class ClientHello: View Source

[](#ClientHello)

```
 15classClientHello:
 16"""
 17    A TLS ClientHello is the first message sent by the client when initiating TLS.
 18    """
 19
 20    _raw_bytes: bytes
 21
 22    def__init__(self, raw_client_hello: bytes, dtls: bool = False):
 23"""Create a TLS ClientHello object from raw bytes."""
 24        self._raw_bytes = raw_client_hello
 25        if dtls:
 26            self._client_hello = dtls_client_hello.DtlsClientHello(
 27                KaitaiStream(io.BytesIO(raw_client_hello))
 28            )
 29        else:
 30            self._client_hello = tls_client_hello.TlsClientHello(
 31                KaitaiStream(io.BytesIO(raw_client_hello))
 32            )
 33
 34    defraw_bytes(self, wrap_in_record: bool = True) -> bytes:
 35"""
 36        The raw ClientHello bytes as seen on the wire.
 37
 38        If `wrap_in_record` is True, the ClientHello will be wrapped in a synthetic TLS record
 39        (`0x160303 + len(chm) + 0x01 + len(ch)`), which is the format expected by some tools.
 40        The synthetic record assumes TLS version (`0x0303`), which may be different from what has been sent over the
 41        wire. JA3 hashes are unaffected by this as they only use the TLS version from the ClientHello data structure.
 42
 43        A future implementation may return not just the exact ClientHello, but also the exact record(s) as seen on the
 44        wire.
 45        """
 46        if isinstance(self._client_hello, dtls_client_hello.DtlsClientHello):
 47            raise NotImplementedError
 48
 49        if wrap_in_record:
 50            return (
 51                # record layer
 52                b"\x16\x03\x03"
 53                + (len(self._raw_bytes) + 4).to_bytes(2, byteorder="big")
 54                +
 55                # handshake header
 56                b"\x01"
 57                + len(self._raw_bytes).to_bytes(3, byteorder="big")
 58                +
 59                # ClientHello as defined in https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2.
 60                self._raw_bytes
 61            )
 62        else:
 63            return self._raw_bytes
 64
 65    @property
 66    defcipher_suites(self) -> list[int]:
 67"""The cipher suites offered by the client (as raw ints)."""
 68        return self._client_hello.cipher_suites.cipher_suites
 69
 70    @property
 71    defsni(self) -> str | None:
 72"""
 73        The [Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication),
 74        which indicates which hostname the client wants to connect to.
 75        """
 76        if ext := getattr(self._client_hello, "extensions", None):
 77            for extension in ext.extensions:
 78                is_valid_sni_extension = (
 79                    extension.type == 0x00
 80                    and len(extension.body.server_names) == 1
 81                    and extension.body.server_names[0].name_type == 0
 82                    and check.is_valid_host(extension.body.server_names[0].host_name)
 83                )
 84                if is_valid_sni_extension:
 85                    return extension.body.server_names[0].host_name.decode("ascii")
 86        return None
 87
 88    @property
 89    defalpn_protocols(self) -> list[bytes]:
 90"""
 91        The application layer protocols offered by the client as part of the
 92        [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) TLS extension.
 93        """
 94        if ext := getattr(self._client_hello, "extensions", None):
 95            for extension in ext.extensions:
 96                if extension.type == 0x10:
 97                    return list(x.name for x in extension.body.alpn_protocols)
 98        return []
 99
100    @property
101    defextensions(self) -> list[tuple[int, bytes]]:
102"""The raw list of extensions in the form of `(extension_type, raw_bytes)` tuples."""
103        ret = []
104        if ext := getattr(self._client_hello, "extensions", None):
105            for extension in ext.extensions:
106                body = getattr(extension, "_raw_body", extension.body)
107                ret.append((extension.type, body))
108        return ret
109
110    def__repr__(self):
111        return f"ClientHello(sni: {self.sni}, alpn_protocols: {self.alpn_protocols})"
```

A TLS ClientHello is the first message sent by the client when initiating TLS.

ClientHello(raw\_client\_hello: bytes, dtls: bool = False) View Source

```
22    def__init__(self, raw_client_hello: bytes, dtls: bool = False):
23"""Create a TLS ClientHello object from raw bytes."""
24        self._raw_bytes = raw_client_hello
25        if dtls:
26            self._client_hello = dtls_client_hello.DtlsClientHello(
27                KaitaiStream(io.BytesIO(raw_client_hello))
28            )
29        else:
30            self._client_hello = tls_client_hello.TlsClientHello(
31                KaitaiStream(io.BytesIO(raw_client_hello))
32            )
```

Create a TLS ClientHello object from raw bytes.

def raw\_bytes(self, wrap\_in\_record: bool = True) -&gt; bytes: View Source

```
34    defraw_bytes(self, wrap_in_record: bool = True) -> bytes:
35"""
36        The raw ClientHello bytes as seen on the wire.
37
38        If `wrap_in_record` is True, the ClientHello will be wrapped in a synthetic TLS record
39        (`0x160303 + len(chm) + 0x01 + len(ch)`), which is the format expected by some tools.
40        The synthetic record assumes TLS version (`0x0303`), which may be different from what has been sent over the
41        wire. JA3 hashes are unaffected by this as they only use the TLS version from the ClientHello data structure.
42
43        A future implementation may return not just the exact ClientHello, but also the exact record(s) as seen on the
44        wire.
45        """
46        if isinstance(self._client_hello, dtls_client_hello.DtlsClientHello):
47            raise NotImplementedError
48
49        if wrap_in_record:
50            return (
51                # record layer
52                b"\x16\x03\x03"
53                + (len(self._raw_bytes) + 4).to_bytes(2, byteorder="big")
54                +
55                # handshake header
56                b"\x01"
57                + len(self._raw_bytes).to_bytes(3, byteorder="big")
58                +
59                # ClientHello as defined in https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2.
60                self._raw_bytes
61            )
62        else:
63            return self._raw_bytes
```

The raw ClientHello bytes as seen on the wire.

If `wrap_in_record` is True, the ClientHello will be wrapped in a synthetic TLS record (`0x160303 + len(chm) + 0x01 + len(ch)`), which is the format expected by some tools. The synthetic record assumes TLS version (`0x0303`), which may be different from what has been sent over the wire. JA3 hashes are unaffected by this as they only use the TLS version from the ClientHello data structure.

A future implementation may return not just the exact ClientHello, but also the exact record(s) as seen on the wire.

cipher\_suites: list\[int] View Source

```
65    @property
66    defcipher_suites(self) -> list[int]:
67"""The cipher suites offered by the client (as raw ints)."""
68        return self._client_hello.cipher_suites.cipher_suites
```

The cipher suites offered by the client (as raw ints).

sni: str | None View Source

```
70    @property
71    defsni(self) -> str | None:
72"""
73        The [Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication),
74        which indicates which hostname the client wants to connect to.
75        """
76        if ext := getattr(self._client_hello, "extensions", None):
77            for extension in ext.extensions:
78                is_valid_sni_extension = (
79                    extension.type == 0x00
80                    and len(extension.body.server_names) == 1
81                    and extension.body.server_names[0].name_type == 0
82                    and check.is_valid_host(extension.body.server_names[0].host_name)
83                )
84                if is_valid_sni_extension:
85                    return extension.body.server_names[0].host_name.decode("ascii")
86        return None
```

The [Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication), which indicates which hostname the client wants to connect to.

alpn\_protocols: list\[bytes] View Source

```
88    @property
89    defalpn_protocols(self) -> list[bytes]:
90"""
91        The application layer protocols offered by the client as part of the
92        [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) TLS extension.
93        """
94        if ext := getattr(self._client_hello, "extensions", None):
95            for extension in ext.extensions:
96                if extension.type == 0x10:
97                    return list(x.name for x in extension.body.alpn_protocols)
98        return []
```

The application layer protocols offered by the client as part of the [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) TLS extension.

extensions: list\[tuple\[int, bytes]] View Source

```
100    @property
101    defextensions(self) -> list[tuple[int, bytes]]:
102"""The raw list of extensions in the form of `(extension_type, raw_bytes)` tuples."""
103        ret = []
104        if ext := getattr(self._client_hello, "extensions", None):
105            for extension in ext.extensions:
106                body = getattr(extension, "_raw_body", extension.body)
107                ret.append((extension.type, body))
108        return ret
```

The raw list of extensions in the form of `(extension_type, raw_bytes)` tuples.

@dataclass

class ClientHelloData: View Source

[](#ClientHelloData)

```
114@dataclass
115classClientHelloData:
116"""
117    Event data for `tls_clienthello` event hooks.
118    """
119
120    context: context.Context
121"""The context object for this connection."""
122    client_hello: ClientHello
123"""The entire parsed TLS ClientHello."""
124    ignore_connection: bool = False
125"""
126    If set to `True`, do not intercept this connection and forward encrypted contents unmodified.
127    """
128    establish_server_tls_first: bool = False
129"""
130    If set to `True`, pause this handshake and establish TLS with an upstream server first.
131    This makes it possible to process the server certificate when generating an interception certificate.
132    """
```

Event data for `tls_clienthello` event hooks.

The context object for this connection.

client\_hello: [ClientHello](#ClientHello)

The entire parsed TLS ClientHello.

ignore\_connection: bool = False

If set to `True`, do not intercept this connection and forward encrypted contents unmodified.

establish\_server\_tls\_first: bool = False

If set to `True`, pause this handshake and establish TLS with an upstream server first. This makes it possible to process the server certificate when generating an interception certificate.

@dataclass

class TlsData: View Source

[](#TlsData)

```
135@dataclass
136classTlsData:
137"""
138    Event data for `tls_start_client`, `tls_start_server`, and `tls_handshake` event hooks.
139    """
140
141    conn: connection.Connection
142"""The affected connection."""
143    context: context.Context
144"""The context object for this connection."""
145    ssl_conn: SSL.Connection | None = None
146"""
147    The associated pyOpenSSL `SSL.Connection` object.
148    This will be set by an addon in the `tls_start_*` event hooks.
149    """
150    is_dtls: bool = False
151"""
152    If set to `True`, indicates that it is a DTLS event.
153    """
```

Event data for `tls_start_client`, `tls_start_server`, and `tls_handshake` event hooks.

The context object for this connection.

ssl\_conn: OpenSSL.SSL.Connection | None = None

The associated pyOpenSSL `SSL.Connection` object. This will be set by an addon in the `tls_start_*` event hooks.

is\_dtls: bool = False

If set to `True`, indicates that it is a DTLS event.