---
title: Custom Contentviews
url: https://docs.mitmproxy.org/stable/addons/contentviews/
source: crawler
fetched_at: 2026-01-28T15:59:12.495441617-03:00
rendered_js: false
word_count: 174
summary: This guide explains how to create custom content views in mitmproxy for pretty-printing binary message data and implementing interactive content editing capabilities.
tags:
    - mitmproxy
    - contentviews
    - addon-development
    - pretty-print
    - custom-view
    - binary-data
    - interactive-editing
category: tutorial
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/addons/contentviews.md)

Contentviews pretty-print binary message data (e.g. HTTP response bodies) that would otherwise be hard to understand for humans. Some contentviews are also *interactive*, i.e. the pretty-printed representation can be edited and mitmproxy will re-encode it into a binary message.

## Simple Example

All contentviews implement the [Contentview](https://docs.mitmproxy.org/stable/api/mitmproxy/contentviews.html#Contentview) base class:

```
from mitmproxy import contentviews
class SwapCase(contentviews.Contentview):
    def prettify(self, data: bytes, metadata: contentviews.Metadata) -> str:
        return data.swapcase().decode()
    def render_priority(self, data: bytes, metadata: contentviews.Metadata) -> float:
        if metadata.content_type and metadata.content_type.startswith("text/example"):
            return 2  # return a value > 1 to make sure the custom view is automatically selected
        else:
            return 0
contentviews.add(SwapCase)
```

examples/addons/contentview.py

To use this contentview, load it as a regular addon:

```
mitmproxy -s examples/addons/contentview.py
```

Like all other mitmproxy addons, contentviews are hot-reloaded when their file contents change. mitmproxy (but not mitmweb) will automatically re-render the contentview as well.

For more details, see the [`mitmproxy.contentviews` API documentation](https://docs.mitmproxy.org/stable/api/mitmproxy/contentviews.html).

## Syntax Highlighting

Contentviews always return an unstyled `str`, but they can declare that their output matches one of the predefined [`SyntaxHighlight` formats](https://docs.mitmproxy.org/stable/api/mitmproxy/contentviews.html#Contentview.syntax_highlight). In particular, binary formats may prettify to YAML (or JSON) and use the YAML highlighter.

The list of supported formats is currently limited, but the implementation is based on [tree-sitter](https://tree-sitter.github.io/tree-sitter/) and easy to extend (see the [`mitmproxy-highlight` crate](https://github.com/mitmproxy/mitmproxy_rs/tree/main/mitmproxy-highlight/src)).

## Interactive Contentviews

The following example implements an interactive contentview that allows users to perform edits on the prettified representation:

```
from mitmproxy import contentviews
class InteractiveSwapCase(contentviews.InteractiveContentview):
    def prettify(
        self,
        data: bytes,
        metadata: contentviews.Metadata,
    ) -> str:
        return data.swapcase().decode()
    def reencode(
        self,
        prettified: str,
        metadata: contentviews.Metadata,
    ) -> bytes:
        return prettified.encode().swapcase()
contentviews.add(InteractiveSwapCase)
```

examples/addons/contentview-interactive.py