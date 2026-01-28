---
title: mitmproxy.net.server_spec
url: https://docs.mitmproxy.org/stable/api/mitmproxy/net/server_spec.html
source: crawler
fetched_at: 2026-01-28T16:21:26.033587-03:00
rendered_js: false
word_count: 96
summary: This document defines the `ServerSpec` data structure used to describe upstream proxies or servers, and provides the Python implementation of a `parse` function for interpreting various server specification strings.
tags:
    - server-specifications
    - parsing
    - network-proxy
    - mitmproxy
    - scheme-host-port
    - data-structure
category: reference
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/net/server_spec.py)

Server specs are used to describe an upstream proxy or server.

View Source

```
 1"""
 2Server specs are used to describe an upstream proxy or server.
 3"""
 4
 5importre
 6fromfunctoolsimport cache
 7fromtypingimport Literal
 8
 9frommitmproxy.netimport check
10
11ServerSpec = tuple[
12    Literal["http", "https", "http3", "tls", "dtls", "tcp", "udp", "dns", "quic"],
13    tuple[str, int],
14]
15
16server_spec_re = re.compile(
17r"""
18        ^
19        (?:(?P<scheme>\w+)://)?  # scheme is optional
20        (?P<host>[^:/]+|\[.+\])  # hostname can be DNS name, IPv4, or IPv6 address.
21        (?::(?P<port>\d+))?  #  port is optional
22        /?  #  we allow a trailing backslash, but no path
23        $
24        """,
25    re.VERBOSE,
26)
27
28
29@cache
30defparse(server_spec: str, default_scheme: str) -> ServerSpec:
31"""
32    Parses a server mode specification, e.g.:
33
34     - http://example.com/
35     - example.org
36     - example.com:443
37
38    *Raises:*
39     - ValueError, if the server specification is invalid.
40    """
41    m = server_spec_re.match(server_spec)
42    if not m:
43        raise ValueError(f"Invalid server specification: {server_spec}")
44
45    if m.group("scheme"):
46        scheme = m.group("scheme")
47    else:
48        scheme = default_scheme
49    if scheme not in (
50        "http",
51        "https",
52        "http3",
53        "tls",
54        "dtls",
55        "tcp",
56        "udp",
57        "dns",
58        "quic",
59    ):
60        raise ValueError(f"Invalid server scheme: {scheme}")
61
62    host = m.group("host")
63    # IPv6 brackets
64    if host.startswith("[") and host.endswith("]"):
65        host = host[1:-1]
66    if not check.is_valid_host(host):
67        raise ValueError(f"Invalid hostname: {host}")
68
69    if m.group("port"):
70        port = int(m.group("port"))
71    else:
72        try:
73            port = {
74                "http": 80,
75                "https": 443,
76                "quic": 443,
77                "http3": 443,
78                "dns": 53,
79            }[scheme]
80        except KeyError:
81            raise ValueError(f"Port specification missing.")
82    if not check.is_valid_port(port):
83        raise ValueError(f"Invalid port: {port}")
84
85    return scheme, (host, port)  # type: ignore
```

ServerSpec = tuple\[typing.Literal\['http', 'https', 'http3', 'tls', 'dtls', 'tcp', 'udp', 'dns', 'quic'], tuple\[str, int]]

[](#ServerSpec)

server\_spec\_re = re.compile('\\n ^\\n (?:(?P&lt;scheme&gt;\\\\w+)://)? # scheme is optional\\n (?P&lt;host&gt;\[^:/]+|\\\\\[.+\\\\]) # hostname can be DNS name, IPv4, or IPv6 address.\\n (?::(?P&lt;port&gt;\\\\d+))? # port is op, re.VERBOSE)

[](#server_spec_re)

@cache

def parse( server\_spec: str, default\_scheme: str) -&gt; tuple\[typing.Literal\['http', 'https', 'http3', 'tls', 'dtls', 'tcp', 'udp', 'dns', 'quic'], tuple\[str, int]]: View Source

[](#parse)

```
30@cache
31defparse(server_spec: str, default_scheme: str) -> ServerSpec:
32"""
33    Parses a server mode specification, e.g.:
34
35     - http://example.com/
36     - example.org
37     - example.com:443
38
39    *Raises:*
40     - ValueError, if the server specification is invalid.
41    """
42    m = server_spec_re.match(server_spec)
43    if not m:
44        raise ValueError(f"Invalid server specification: {server_spec}")
45
46    if m.group("scheme"):
47        scheme = m.group("scheme")
48    else:
49        scheme = default_scheme
50    if scheme not in (
51        "http",
52        "https",
53        "http3",
54        "tls",
55        "dtls",
56        "tcp",
57        "udp",
58        "dns",
59        "quic",
60    ):
61        raise ValueError(f"Invalid server scheme: {scheme}")
62
63    host = m.group("host")
64    # IPv6 brackets
65    if host.startswith("[") and host.endswith("]"):
66        host = host[1:-1]
67    if not check.is_valid_host(host):
68        raise ValueError(f"Invalid hostname: {host}")
69
70    if m.group("port"):
71        port = int(m.group("port"))
72    else:
73        try:
74            port = {
75                "http": 80,
76                "https": 443,
77                "quic": 443,
78                "http3": 443,
79                "dns": 53,
80            }[scheme]
81        except KeyError:
82            raise ValueError(f"Port specification missing.")
83    if not check.is_valid_port(port):
84        raise ValueError(f"Invalid port: {port}")
85
86    return scheme, (host, port)  # type: ignore
```

Parses a server mode specification, e.g.:

- [http://example.com/](http://example.com/)
- example.org
- example.com:443

*Raises:*

- ValueError, if the server specification is invalid.