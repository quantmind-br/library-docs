---
title: Filter expressions
url: https://docs.mitmproxy.org/stable/concepts/filters/
source: crawler
fetched_at: 2026-01-28T15:03:21.117230793-03:00
rendered_js: false
word_count: 259
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/concepts/filters.md)

Many commands in the mitmproxy tool make use of filter expressions. Filter expressions consist of the following operators:

~aMatch asset in response: CSS, JavaScript, images, fonts. ~allMatch all flows ~b regexBody ~bq regexRequest body ~bs regexResponse body ~c intHTTP response code ~comment regexFlow comment ~d regexDomain ~dnsMatch DNS flows ~dst regexMatch destination address ~eMatch error ~h regexHeader ~hq regexRequest header ~hs regexResponse header ~httpMatch HTTP flows ~m regexMethod ~markedMatch marked flows ~marker regexMatch marked flows with specified marker ~meta regexFlow metadata ~qMatch request with no response ~replayMatch replayed flows ~replayqMatch replayed client request ~replaysMatch replayed server response ~sMatch response ~src regexMatch source address ~t regexContent-type header ~tcpMatch TCP flows ~tq regexRequest Content-Type header ~ts regexResponse Content-Type header ~u regexURL ~udpMatch UDP flows ~websocketMatch WebSocket flows !unary not &and |or (...)grouping

- Regexes are Python-style.
- Regexes can be specified as quoted strings.
- Regexes are case-insensitive by default.[1](#fn:1)
- Header matching (~h, ~hq, ~hs) is against a string of the form “name: value”.
- Strings with no operators are matched against the request URL.
- The default binary operator is &.

## View flow selectors

In interactive contexts, mitmproxy has a set of convenient flow selectors that operate on the current view:

@allAll flows @focusThe currently focused flow @shownAll flows currently shown @hiddenAll flows currently hidden @markedAll marked flows @unmarkedAll unmarked flows

These are frequently used in commands and key bindings.

## Examples

URL containing “google.com”:

```
google\.com
```

Requests whose body contains the string “test”:

```
~q ~b test
```

Anything but requests with a text/html content type:

```
!(~q & ~t "text/html")
```

Replace entire GET string in a request (quotes required to make it work):

```
":~q ~m GET:.*:/replacement.html"
```