---
title: mitmproxy.contentviews
url: https://docs.mitmproxy.org/stable/api/mitmproxy/contentviews.html
source: crawler
fetched_at: 2026-01-28T15:03:23.69386336-03:00
rendered_js: false
word_count: 1410
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/contentviews/__init__.py)

mitmproxy includes a set of content views which can be used to format/decode/highlight/reencode data. While they are mostly used for HTTP message bodies, the may be used in other contexts, e.g. to decode WebSocket messages.

See "Custom Contentviews" in the mitmproxy documentation for examples.

View Source

```
  1"""
  2mitmproxy includes a set of content views which can be used to
  3format/decode/highlight/reencode data. While they are mostly used for HTTP message
  4bodies, the may be used in other contexts, e.g. to decode WebSocket messages.
  5
  6See "Custom Contentviews" in the mitmproxy documentation for examples.
  7"""
  8
  9importlogging
 10importsys
 11importtraceback
 12importwarnings
 13fromdataclassesimport dataclass
 14
 15from..addonmanagerimport cut_traceback
 16from._apiimport Contentview
 17from._apiimport InteractiveContentview
 18from._apiimport Metadata
 19from._apiimport SyntaxHighlight
 20from._compatimport get  # noqa: F401
 21from._compatimport LegacyContentview
 22from._compatimport remove  # noqa: F401
 23from._registryimport ContentviewRegistry
 24from._utilsimport ContentviewMessage
 25from._utilsimport get_data
 26from._utilsimport make_metadata
 27from._view_cssimport css
 28from._view_dnsimport dns
 29from._view_graphqlimport graphql
 30from._view_http3import http3
 31from._view_imageimport image
 32from._view_javascriptimport javascript
 33from._view_jsonimport json_view
 34from._view_mqttimport mqtt
 35from._view_multipartimport multipart
 36from._view_queryimport query
 37from._view_rawimport raw
 38from._view_socketioimport socket_io
 39from._view_urlencodedimport urlencoded
 40from._view_wbxmlimport wbxml
 41from._view_xml_htmlimport xml_html
 42from.baseimport View
 43importmitmproxy_rs.contentviews
 44frommitmproxyimport flow
 45frommitmproxy.utilsimport strutils
 46
 47logger = logging.getLogger(__name__)
 48
 49
 50@dataclass
 51classContentviewResult:
 52    text: str
 53    syntax_highlight: SyntaxHighlight
 54    view_name: str | None
 55    description: str
 56
 57
 58registry = ContentviewRegistry()
 59
 60
 61defprettify_message(
 62    message: ContentviewMessage,
 63    flow: flow.Flow,
 64    view_name: str = "auto",
 65    registry: ContentviewRegistry = registry,
 66) -> ContentviewResult:
 67    data, enc = get_data(message)
 68    if data is None:
 69        return ContentviewResult(
 70            text="Content is missing.",
 71            syntax_highlight="error",
 72            description="",
 73            view_name=None,
 74        )
 75
 76    # Determine the correct view
 77    metadata = make_metadata(message, flow)
 78    view = registry.get_view(data, metadata, view_name)
 79
 80    # Finally, we can pretty-print!
 81    try:
 82        ret = ContentviewResult(
 83            text=view.prettify(data, metadata),
 84            syntax_highlight=view.syntax_highlight,
 85            view_name=view.name,
 86            description=enc,
 87        )
 88    except Exception as e:
 89        logger.debug(f"Contentview {view.name!r} failed: {e}", exc_info=True)
 90        if view_name == "auto":
 91            # If the contentview was chosen as the best matching one, fall back to raw.
 92            ret = ContentviewResult(
 93                text=raw.prettify(data, metadata),
 94                syntax_highlight=raw.syntax_highlight,
 95                view_name=raw.name,
 96                description=f"{enc}[failed to parse as {view.name}]",
 97            )
 98        else:
 99            # Cut the exception traceback for display.
100            exc, value, tb = sys.exc_info()
101            tb_cut = cut_traceback(tb, "prettify_message")
102            if (
103                tb_cut == tb
104            ):  # If there are no extra frames, just skip displaying the traceback.
105                tb_cut = None
106            # If the contentview has been set explicitly, we display a hard error.
107            err = "".join(traceback.format_exception(exc, value=value, tb=tb_cut))
108            ret = ContentviewResult(
109                text=f"Couldn't parse as {view.name}:\n{err}",
110                syntax_highlight="error",
111                view_name=view.name,
112                description=enc,
113            )
114
115    ret.text = strutils.escape_control_characters(ret.text)
116    return ret
117
118
119defreencode_message(
120    prettified: str,
121    message: ContentviewMessage,
122    flow: flow.Flow,
123    view_name: str,
124) -> bytes:
125    metadata = make_metadata(message, flow)
126    view = registry[view_name.lower()]
127    if not isinstance(view, InteractiveContentview):
128        raise ValueError(f"Contentview {view.name} is not interactive.")
129    return view.reencode(prettified, metadata)
130
131
132_views: list[Contentview] = [
133    css,
134    dns,
135    graphql,
136    http3,
137    image,
138    javascript,
139    json_view,
140    mqtt,
141    multipart,
142    query,
143    raw,
144    socket_io,
145    urlencoded,
146    wbxml,
147    xml_html,
148]
149for view in _views:
150    registry.register(view)
151for name in mitmproxy_rs.contentviews.__all__:
152    if name.startswith("_"):
153        continue
154    cv = getattr(mitmproxy_rs.contentviews, name)
155    if isinstance(cv, Contentview) and not isinstance(cv, type):
156        registry.register(cv)
157
158
159defadd(contentview: Contentview | type[Contentview]) -> None:
160"""
161    Register a contentview for use in mitmproxy.
162
163    You may pass a `Contentview` instance or the class itself.
164    When passing the class, its constructor will be invoked with no arguments.
165    """
166    if isinstance(contentview, View):
167        warnings.warn(
168            f"`mitmproxy.contentviews.View` is deprecated since mitmproxy 12, "
169            f"migrate {contentview.__class__.__name__} to `mitmproxy.contentviews.Contentview` instead.",
170            stacklevel=2,
171        )
172        contentview = LegacyContentview(contentview)
173    registry.register(contentview)
174
175
176# hack: docstring where pdoc finds it.
177SyntaxHighlight = SyntaxHighlight
178"""
179Syntax highlighting formats currently supported by mitmproxy.
180Note that YAML is a superset of JSON; so if you'd like to highlight JSON, pick the YAML highlighter.
181
182*If you have a concrete use case for additional formats, please open an issue.*
183"""
184
185
186__all__ = [
187    # Public Contentview API
188    "Contentview",
189    "InteractiveContentview",
190    "SyntaxHighlight",
191    "add",
192    "Metadata",
193]
```

@typing.runtime\_checkable

class Contentview(typing.Protocol): View Source

[](#Contentview)

```
24@typing.runtime_checkable
25classContentview(typing.Protocol):
26"""
27    Base class for all contentviews.
28    """
29
30    @property
31    defname(self) -> str:
32"""
33        The name of this contentview, e.g. "XML/HTML".
34        Inferred from the class name by default.
35        """
36        return type(self).__name__.removesuffix("Contentview")
37
38    @property
39    defsyntax_highlight(self) -> SyntaxHighlight:
40"""Optional syntax highlighting that should be applied to the prettified output."""
41        return "none"
42
43    @abstractmethod
44    defprettify(
45        self,
46        data: bytes,
47        metadata: Metadata,
48    ) -> str:
49"""
50        Transform raw data into human-readable output.
51        May raise an exception (e.g. `ValueError`) if data cannot be prettified.
52        """
53
54    defrender_priority(
55        self,
56        data: bytes,
57        metadata: Metadata,
58    ) -> float:
59"""
60        Return the priority of this view for rendering `data`.
61        If no particular view is chosen by the user, the view with the highest priority is selected.
62        If this view does not support the given data, return a float < 0.
63        """
64        return 0
65
66    def__lt__(self, other):
67        return self.name.__lt__(other.name)
```

Base class for all contentviews.

name: str View Source

```
30    @property
31    defname(self) -> str:
32"""
33        The name of this contentview, e.g. "XML/HTML".
34        Inferred from the class name by default.
35        """
36        return type(self).__name__.removesuffix("Contentview")
```

The name of this contentview, e.g. "XML/HTML". Inferred from the class name by default.

syntax\_highlight: [SyntaxHighlight](#SyntaxHighlight) View Source

```
38    @property
39    defsyntax_highlight(self) -> SyntaxHighlight:
40"""Optional syntax highlighting that should be applied to the prettified output."""
41        return "none"
```

Optional syntax highlighting that should be applied to the prettified output.

@abstractmethod

def prettify(self, data: bytes, metadata: [Metadata](#Metadata)) -&gt; str: View Source

```
43    @abstractmethod
44    defprettify(
45        self,
46        data: bytes,
47        metadata: Metadata,
48    ) -> str:
49"""
50        Transform raw data into human-readable output.
51        May raise an exception (e.g. `ValueError`) if data cannot be prettified.
52        """
```

Transform raw data into human-readable output. May raise an exception (e.g. `ValueError`) if data cannot be prettified.

def render\_priority( self, data: bytes, metadata: [Metadata](#Metadata)) -&gt; float: View Source

```
54    defrender_priority(
55        self,
56        data: bytes,
57        metadata: Metadata,
58    ) -> float:
59"""
60        Return the priority of this view for rendering `data`.
61        If no particular view is chosen by the user, the view with the highest priority is selected.
62        If this view does not support the given data, return a float < 0.
63        """
64        return 0
```

Return the priority of this view for rendering `data`. If no particular view is chosen by the user, the view with the highest priority is selected. If this view does not support the given data, return a float &lt; 0.

@typing.runtime\_checkable

class InteractiveContentview([mitmproxy.contentviews.Contentview](#Contentview), typing.Protocol): View Source

[](#InteractiveContentview)

```
70@typing.runtime_checkable
71classInteractiveContentview(Contentview, typing.Protocol):
72"""A contentview that prettifies raw data and allows for interactive editing."""
73
74    @abstractmethod
75    defreencode(
76        self,
77        prettified: str,
78        metadata: Metadata,
79    ) -> bytes:
80"""
81        Reencode the given (modified) `prettified` output into the original data format.
82        May raise an exception (e.g. `ValueError`) if reencoding failed.
83        """
```

A contentview that prettifies raw data and allows for interactive editing.

@abstractmethod

def reencode( self, prettified: str, metadata: [Metadata](#Metadata)) -&gt; bytes: View Source

```
74    @abstractmethod
75    defreencode(
76        self,
77        prettified: str,
78        metadata: Metadata,
79    ) -> bytes:
80"""
81        Reencode the given (modified) `prettified` output into the original data format.
82        May raise an exception (e.g. `ValueError`) if reencoding failed.
83        """
```

Reencode the given (modified) `prettified` output into the original data format. May raise an exception (e.g. `ValueError`) if reencoding failed.

type SyntaxHighlight = Literal\['css', 'javascript', 'xml', 'yaml', 'none', 'error']

[](#SyntaxHighlight)

Syntax highlighting formats currently supported by mitmproxy. Note that YAML is a superset of JSON; so if you'd like to highlight JSON, pick the YAML highlighter.

*If you have a concrete use case for additional formats, please open an issue.*

def add( contentview: [Contentview](#Contentview) | type\[[Contentview](#Contentview)]) -&gt; None: View Source

[](#add)

```
160defadd(contentview: Contentview | type[Contentview]) -> None:
161"""
162    Register a contentview for use in mitmproxy.
163
164    You may pass a `Contentview` instance or the class itself.
165    When passing the class, its constructor will be invoked with no arguments.
166    """
167    if isinstance(contentview, View):
168        warnings.warn(
169            f"`mitmproxy.contentviews.View` is deprecated since mitmproxy 12, "
170            f"migrate {contentview.__class__.__name__} to `mitmproxy.contentviews.Contentview` instead.",
171            stacklevel=2,
172        )
173        contentview = LegacyContentview(contentview)
174    registry.register(contentview)
```

Register a contentview for use in mitmproxy.

You may pass a `Contentview` instance or the class itself. When passing the class, its constructor will be invoked with no arguments.

@dataclass

class Metadata: View Source

[](#Metadata)

```
 86@dataclass
 87classMetadata:
 88"""
 89    Metadata about the data that is being prettified.
 90
 91    Do not rely on any given attribute to be present.
 92    """
 93
 94    flow: Flow | None = None
 95"""The flow that the data belongs to, if any."""
 96
 97    content_type: str | None = None
 98"""The HTTP content type of the data, if any."""
 99    http_message: http.Message | None = None
100"""The HTTP message that the data belongs to, if any."""
101    tcp_message: tcp.TCPMessage | None = None
102"""The TCP message that the data belongs to, if any."""
103    udp_message: udp.UDPMessage | None = None
104"""The UDP message that the data belongs to, if any."""
105    websocket_message: WebSocketMessage | None = None
106"""The websocket message that the data belongs to, if any."""
107    dns_message: DNSMessage | None = None
108"""The DNS message that the data belongs to, if any."""
109
110    protobuf_definitions: Path | None = None
111"""Path to a .proto file that's used to resolve Protobuf field names."""
112
113    original_data: bytes | None = None
114"""When reencoding: The original data that was prettified."""
```

Metadata about the data that is being prettified.

Do not rely on any given attribute to be present.

content\_type: str | None = None

The HTTP content type of the data, if any.