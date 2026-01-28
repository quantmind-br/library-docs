---
title: mitmproxy.proxy.context
url: https://docs.mitmproxy.org/stable/api/mitmproxy/proxy/context.html
source: crawler
fetched_at: 2026-01-28T14:58:34.401040694-03:00
rendered_js: false
word_count: 412
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/proxy/context.py) View Source

```
 1fromtypingimport TYPE_CHECKING
 2
 3frommitmproxyimport connection
 4frommitmproxy.optionsimport Options
 5
 6if TYPE_CHECKING:
 7    importmitmproxy.proxy.layer
 8
 9
10classContext:
11"""
12    The context object provided to each protocol layer in the proxy core.
13    """
14
15    client: connection.Client
16"""The client connection."""
17    server: connection.Server
18"""
19    The server connection.
20
21    For practical reasons this attribute is always set, even if there is not server connection yet.
22    In this case the server address is `None`.
23    """
24    options: Options
25"""
26    Provides access to options for proxy layers. Not intended for use by addons, use `mitmproxy.ctx.options` instead.
27    """
28    layers: list["mitmproxy.proxy.layer.Layer"]
29"""
30    The protocol layer stack.
31    """
32
33    def__init__(
34        self,
35        client: connection.Client,
36        options: Options,
37    ) -> None:
38        self.client = client
39        self.options = options
40        self.server = connection.Server(
41            address=None, transport_protocol=client.transport_protocol
42        )
43        self.layers = []
44
45    deffork(self) -> "Context":
46        ret = Context(self.client, self.options)
47        ret.server = self.server
48        ret.layers = self.layers.copy()
49        return ret
50
51    def__repr__(self):
52        return (
53            f"Context(\n"
54            f"  {self.client!r},\n"
55            f"  {self.server!r},\n"
56            f"  layers=[{self.layers!r}]\n"
57            f")"
58        )
```

class Context: View Source

[](#Context)

```
11classContext:
12"""
13    The context object provided to each protocol layer in the proxy core.
14    """
15
16    client: connection.Client
17"""The client connection."""
18    server: connection.Server
19"""
20    The server connection.
21
22    For practical reasons this attribute is always set, even if there is not server connection yet.
23    In this case the server address is `None`.
24    """
25    options: Options
26"""
27    Provides access to options for proxy layers. Not intended for use by addons, use `mitmproxy.ctx.options` instead.
28    """
29    layers: list["mitmproxy.proxy.layer.Layer"]
30"""
31    The protocol layer stack.
32    """
33
34    def__init__(
35        self,
36        client: connection.Client,
37        options: Options,
38    ) -> None:
39        self.client = client
40        self.options = options
41        self.server = connection.Server(
42            address=None, transport_protocol=client.transport_protocol
43        )
44        self.layers = []
45
46    deffork(self) -> "Context":
47        ret = Context(self.client, self.options)
48        ret.server = self.server
49        ret.layers = self.layers.copy()
50        return ret
51
52    def__repr__(self):
53        return (
54            f"Context(\n"
55            f"  {self.client!r},\n"
56            f"  {self.server!r},\n"
57            f"  layers=[{self.layers!r}]\n"
58            f")"
59        )
```

The context object provided to each protocol layer in the proxy core.

The server connection.

For practical reasons this attribute is always set, even if there is not server connection yet. In this case the server address is `None`.

layers: list\[mitmproxy.proxy.layer.Layer]

The protocol layer stack.