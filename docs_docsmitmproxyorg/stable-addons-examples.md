---
title: Examples
url: https://docs.mitmproxy.org/stable/addons/examples/
source: crawler
fetched_at: 2026-01-28T15:01:12.973508693-03:00
rendered_js: false
word_count: 1094
summary: This document provides a collection of addon examples for mitmproxy, demonstrating various functionalities such as request/response modification, custom commands, and WebSocket handling.
tags:
    - mitmproxy
    - addon-examples
    - http-modification
    - websocket-handling
    - custom-commands
    - proxy-configuration
    - stream-processing
category: guide
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/addons/examples.md)

## Addon Examples

### Dedicated Example Addons

- [http-redirect-requests.py](#http-redirect-requests) — Redirect HTTP requests to another server.
- [commands-flows.py](#commands-flows) — Handle flows as command arguments.
- [options-simple.py](#options-simple) — Add a new mitmproxy option.
- [http-stream-modify.py](#http-stream-modify) — Modify a streamed response.
- [anatomy2.py](#anatomy-) — An addon using the abbreviated scripting syntax.
- [contentview.py](#contentview)
- [commands-paths.py](#commands-paths) — Handle file paths as command arguments.
- [io-write-flow-file.py](#io-write-flow-file) — Generate a mitmproxy dump file.
- [http-modify-query-string.py](#http-modify-query-string) — Modify HTTP query parameters.
- [websocket-inject-message.py](#websocket-inject-message) — Inject a WebSocket message into a running connection.
- [http-trailers.py](#http-trailers) — This script simply prints all received HTTP Trailers.
- [filter-flows.py](#filter-flows) — Use mitmproxy’s filter pattern in scripts.
- [internet-in-mirror.py](#internet-in-mirror) — Mirror all web pages.
- [contentview-interactive.py](#contentview-interactive)
- [io-read-saved-flows.py](#io-read-saved-flows) — Read a mitmproxy dump file.
- [duplicate-modify-replay.py](#duplicate-modify-replay) — Take incoming HTTP requests and replay them with modified parameters.
- [commands-simple.py](#commands-simple) — Add a custom command to mitmproxy’s command prompt.
- [options-configure.py](#options-configure) — React to configuration changes.
- [websocket-simple.py](#websocket-simple) — Process individual messages from a WebSocket connection.
- [anatomy.py](#anatomy) — Basic skeleton of a mitmproxy addon.
- [dns-simple.py](#dns-simple) — Spoof DNS responses.
- [nonblocking.py](#nonblocking) — Make events hooks non-blocking using async or @concurrent.
- [http-reply-from-proxy.py](#http-reply-from-proxy) — Send a reply from the proxy without sending the request to the remote server.
- [http-add-header.py](#http-add-header) — Add an HTTP header to each response.
- [shutdown.py](#shutdown) — A simple way of shutting down the mitmproxy instance to stop everything.
- [wsgi-flask-app.py](#wsgi-flask-app) — Host a WSGI app in mitmproxy.
- [http-stream-simple.py](#http-stream-simple) — Select which responses should be streamed.
- [tcp-simple.py](#tcp-simple) — Process individual messages from a TCP connection.
- [http-modify-form.py](#http-modify-form) — Modify an HTTP form submission.
- [log-events.py](#log-events) — Post messages to mitmproxy’s event log.

### Built-In Addons

Much of mitmproxy’s own functionality is defined in [a suite of built-in addons](https://github.com/mitmproxy/mitmproxy/tree/main/mitmproxy/addons), implementing everything from functionality like anticaching and sticky cookies to our onboarding webapp. The built-in addons make for instructive reading, and you will quickly see that quite complex functionality can often boil down to a very small, completely self-contained modules.

Additional examples contributed by the mitmproxy community can be found [on GitHub](https://github.com/mitmproxy/mitmproxy/tree/main/examples/contrib).

* * *

### Example: http-redirect-requests.py

```
"""Redirect HTTP requests to another server."""
from mitmproxy import http
def request(flow: http.HTTPFlow) -> None:
    # pretty_host takes the "Host" header of the request into account,
    # which is useful in transparent mode where we usually only have the IP
    # otherwise.
    if flow.request.pretty_host == "example.org":
        flow.request.host = "mitmproxy.org"
```

### Example: commands-flows.py

```
"""Handle flows as command arguments."""
import logging
from collections.abc import Sequence
from mitmproxy import command
from mitmproxy import flow
from mitmproxy import http
from mitmproxy.log import ALERT
class MyAddon:
    @command.command("myaddon.addheader")
    def addheader(self, flows: Sequence[flow.Flow]) -> None:
        for f in flows:
            if isinstance(f, http.HTTPFlow):
                f.request.headers["myheader"] = "value"
        logging.log(ALERT, "done")
addons = [MyAddon()]
```

### Example: options-simple.py

```
"""
Add a new mitmproxy option.
Usage:
    mitmproxy -s options-simple.py --set addheader=true
"""
from mitmproxy import ctx
class AddHeader:
    def __init__(self):
        self.num = 0
    def load(self, loader):
        loader.add_option(
            name="addheader",
            typespec=bool,
            default=False,
            help="Add a count header to responses",
        )
    def response(self, flow):
        if ctx.options.addheader:
            self.num = self.num + 1
            flow.response.headers["count"] = str(self.num)
addons = [AddHeader()]
```

### Example: http-stream-modify.py

```
"""
Modify a streamed response.
Generally speaking, we recommend *not* to stream messages you need to modify.
Modifying streamed responses is tricky and brittle:
    - If the transfer encoding isn't chunked, you cannot simply change the content length.
    - If you want to replace all occurrences of "foobar", make sure to catch the cases
      where one chunk ends with [...]foo" and the next starts with "bar[...].
"""
from collections.abc import Iterable
def modify(data: bytes) -> bytes | Iterable[bytes]:
    """
    This function will be called for each chunk of request/response body data that arrives at the proxy,
    and once at the end of the message with an empty bytes argument (b"").
    It may either return bytes or an iterable of bytes (which would result in multiple HTTP/2 data frames).
    """
    return data.replace(b"foo", b"bar")
def responseheaders(flow):
    flow.response.stream = modify
```

### Example: anatomy2.py

```
"""An addon using the abbreviated scripting syntax."""
def request(flow):
    flow.request.headers["myheader"] = "value"
```

### Example: contentview.py

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

### Example: commands-paths.py

```
"""Handle file paths as command arguments."""
import logging
from collections.abc import Sequence
from mitmproxy import command
from mitmproxy import flow
from mitmproxy import http
from mitmproxy import types
from mitmproxy.log import ALERT
class MyAddon:
    @command.command("myaddon.histogram")
    def histogram(
        self,
        flows: Sequence[flow.Flow],
        path: types.Path,
    ) -> None:
        totals: dict[str, int] = {}
        for f in flows:
            if isinstance(f, http.HTTPFlow):
                totals[f.request.host] = totals.setdefault(f.request.host, 0) + 1
        with open(path, "w+") as fp:
            for cnt, dom in sorted((v, k) for (k, v) in totals.items()):
                fp.write(f"{cnt}: {dom}\n")
        logging.log(ALERT, "done")
addons = [MyAddon()]
```

### Example: io-write-flow-file.py

```
"""
Generate a mitmproxy dump file.
This script demonstrates how to generate a mitmproxy dump file,
as it would also be generated by passing `-w` to mitmproxy.
In contrast to `-w`, this gives you full control over which
flows should be saved and also allows you to rotate files or log
to multiple files in parallel.
"""
import os
import random
from typing import BinaryIO
from mitmproxy import http
from mitmproxy import io
class Writer:
    def __init__(self) -> None:
        # We are using an environment variable to keep the example as simple as possible,
        # consider implementing this as a mitmproxy option instead.
        filename = os.getenv("MITMPROXY_OUTFILE", "out.mitm")
        self.f: BinaryIO = open(filename, "wb")
        self.w = io.FlowWriter(self.f)
    def response(self, flow: http.HTTPFlow) -> None:
        if random.choice([True, False]):
            self.w.add(flow)
    def done(self):
        self.f.close()
addons = [Writer()]
```

### Example: http-modify-query-string.py

```
"""Modify HTTP query parameters."""
from mitmproxy import http
def request(flow: http.HTTPFlow) -> None:
    flow.request.query["mitmproxy"] = "rocks"
```

### Example: websocket-inject-message.py

```
"""
Inject a WebSocket message into a running connection.
This example shows how to inject a WebSocket message into a running connection.
"""
import asyncio
from mitmproxy import ctx
from mitmproxy import http
# Simple example: Inject a message as a response to an event
def websocket_message(flow: http.HTTPFlow):
    assert flow.websocket is not None  # make type checker happy
    last_message = flow.websocket.messages[-1]
    if last_message.is_text and "secret" in last_message.text:
        last_message.drop()
        ctx.master.commands.call(
            "inject.websocket", flow, last_message.from_client, b"ssssssh"
        )
# Complex example: Schedule a periodic timer
async def inject_async(flow: http.HTTPFlow):
    msg = "hello from mitmproxy! "
    assert flow.websocket is not None  # make type checker happy
    while flow.websocket.timestamp_end is None:
        ctx.master.commands.call("inject.websocket", flow, True, msg.encode())
        await asyncio.sleep(1)
        msg = msg[1:] + msg[:1]
tasks = set()
def websocket_start(flow: http.HTTPFlow):
    # we need to hold a reference to the task, otherwise it will be garbage collected.
    t = asyncio.create_task(inject_async(flow))
    tasks.add(t)
    t.add_done_callback(tasks.remove)
```

### Example: http-trailers.py

```
"""
This script simply prints all received HTTP Trailers.
HTTP requests and responses can contain trailing headers which are sent after
the body is fully transmitted. Such trailers need to be announced in the initial
headers by name, so the receiving endpoint can wait and read them after the
body.
"""
from mitmproxy import http
from mitmproxy.http import Headers
def request(flow: http.HTTPFlow):
    if flow.request.trailers:
        print("HTTP Trailers detected! Request contains:", flow.request.trailers)
    if flow.request.path == "/inject_trailers":
        if flow.request.is_http10:
            # HTTP/1.0 doesn't support trailers
            return
        elif flow.request.is_http11:
            if not flow.request.content:
                # Avoid sending a body on GET requests or a 0 byte chunked body with trailers.
                # Otherwise some servers return 400 Bad Request.
                return
            # HTTP 1.1 requires transfer-encoding: chunked to send trailers
            flow.request.headers["transfer-encoding"] = "chunked"
        # HTTP 2+ supports trailers on all requests/responses
        flow.request.headers["trailer"] = "x-my-injected-trailer-header"
        flow.request.trailers = Headers([(b"x-my-injected-trailer-header", b"foobar")])
        print("Injected a new request trailer...", flow.request.headers["trailer"])
def response(flow: http.HTTPFlow):
    assert flow.response
    if flow.response.trailers:
        print("HTTP Trailers detected! Response contains:", flow.response.trailers)
    if flow.request.path == "/inject_trailers":
        if flow.request.is_http10:
            return
        elif flow.request.is_http11:
            if not flow.response.content:
                return
            flow.response.headers["transfer-encoding"] = "chunked"
        flow.response.headers["trailer"] = "x-my-injected-trailer-header"
        flow.response.trailers = Headers([(b"x-my-injected-trailer-header", b"foobar")])
        print("Injected a new response trailer...", flow.response.headers["trailer"])
```

### Example: filter-flows.py

```
"""
Use mitmproxy's filter pattern in scripts.
"""
from __future__ import annotations
import logging
from mitmproxy import flowfilter
from mitmproxy import http
from mitmproxy.addonmanager import Loader
class Filter:
    filter: flowfilter.TFilter
    def configure(self, updated):
        if "flowfilter" in updated:
            self.filter = flowfilter.parse(".")
    def load(self, loader: Loader):
        loader.add_option("flowfilter", str, "", "Check that flow matches filter.")
    def response(self, flow: http.HTTPFlow) -> None:
        if flowfilter.match(self.filter, flow):
            logging.info("Flow matches filter:")
            logging.info(flow)
addons = [Filter()]
```

### Example: internet-in-mirror.py

```
"""
Mirror all web pages.
Useful if you are living down under.
"""
from mitmproxy import http
def response(flow: http.HTTPFlow) -> None:
    if flow.response and flow.response.content:
        flow.response.content = flow.response.content.replace(
            b"</head>", b"<style>body {transform: scaleX(-1);}</style></head>"
        )
```

### Example: contentview-interactive.py

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

### Example: io-read-saved-flows.py

```
#!/usr/bin/env python
"""
Read a mitmproxy dump file.
"""
import pprint
import sys
from mitmproxy import http
from mitmproxy import io
from mitmproxy.exceptions import FlowReadException
with open(sys.argv[1], "rb") as logfile:
    freader = io.FlowReader(logfile)
    pp = pprint.PrettyPrinter(indent=4)
    try:
        for f in freader.stream():
            print(f)
            if isinstance(f, http.HTTPFlow):
                print(f.request.host)
            pp.pprint(f.get_state())
            print("")
    except FlowReadException as e:
        print(f"Flow file corrupted: {e}")
```

### Example: duplicate-modify-replay.py

```
"""Take incoming HTTP requests and replay them with modified parameters."""
from mitmproxy import ctx
def request(flow):
    # Avoid an infinite loop by not replaying already replayed requests
    if flow.is_replay == "request":
        return
    flow = flow.copy()
    # Only interactive tools have a view. If we have one, add a duplicate entry
    # for our flow.
    if "view" in ctx.master.addons:
        ctx.master.commands.call("view.flows.duplicate", [flow])
    flow.request.path = "/changed"
    ctx.master.commands.call("replay.client", [flow])
```

### Example: commands-simple.py

```
"""Add a custom command to mitmproxy's command prompt."""
import logging
from mitmproxy import command
class MyAddon:
    def __init__(self):
        self.num = 0
    @command.command("myaddon.inc")
    def inc(self) -> None:
        self.num += 1
        logging.info(f"num = {self.num}")
addons = [MyAddon()]
```

### Example: options-configure.py

```
"""React to configuration changes."""
from typing import Optional
from mitmproxy import ctx
from mitmproxy import exceptions
class AddHeader:
    def load(self, loader):
        loader.add_option(
            name="addheader",
            typespec=Optional[int],
            default=None,
            help="Add a header to responses",
        )
    def configure(self, updates):
        if "addheader" in updates:
            if ctx.options.addheader is not None and ctx.options.addheader > 100:
                raise exceptions.OptionsError("addheader must be <= 100")
    def response(self, flow):
        if ctx.options.addheader is not None:
            flow.response.headers["addheader"] = str(ctx.options.addheader)
addons = [AddHeader()]
```

### Example: websocket-simple.py

```
"""Process individual messages from a WebSocket connection."""
import logging
import re
from mitmproxy import http
def websocket_message(flow: http.HTTPFlow):
    assert flow.websocket is not None  # make type checker happy
    # get the latest message
    message = flow.websocket.messages[-1]
    # was the message sent from the client or server?
    if message.from_client:
        logging.info(f"Client sent a message: {message.content!r}")
    else:
        logging.info(f"Server sent a message: {message.content!r}")
    # manipulate the message content
    message.content = re.sub(rb"^Hello", b"HAPPY", message.content)
    if b"FOOBAR" in message.content:
        # kill the message and not send it to the other endpoint
        message.drop()
```

### Example: anatomy.py

```
"""
Basic skeleton of a mitmproxy addon.
Run as follows: mitmproxy -s anatomy.py
"""
import logging
class Counter:
    def __init__(self):
        self.num = 0
    def request(self, flow):
        self.num = self.num + 1
        logging.info("We've seen %d flows" % self.num)
addons = [Counter()]
```

### Example: dns-simple.py

```
"""
Spoof DNS responses.
In this example, we fiddle with IPv6 (AAAA) records:
 - For example.com, `::1` is returned.
   (domain is hosted on localhost)
 - For example.org, an NXDOMAIN error is returned.
   (domain does not exist)
 - For all other domains, return a non-error response without any records.
   (domain exists, but has no IPv6 configured)
"""
import ipaddress
import logging
from mitmproxy import dns
def dns_request(flow: dns.DNSFlow) -> None:
    q = flow.request.question
    if q and q.type == dns.types.AAAA:
        logging.info(f"Spoofing IPv6 records for {q.name}...")
        if q.name == "example.com":
            flow.response = flow.request.succeed(
                [
                    dns.ResourceRecord(
                        name="example.com",
                        type=dns.types.AAAA,
                        class_=dns.classes.IN,
                        ttl=dns.ResourceRecord.DEFAULT_TTL,
                        data=ipaddress.ip_address("::1").packed,
                    )
                ]
            )
        elif q.name == "example.org":
            flow.response = flow.request.fail(dns.response_codes.NXDOMAIN)
        else:
            flow.response = flow.request.succeed([])
```

### Example: nonblocking.py

```
"""
Make events hooks non-blocking using async or @concurrent.
"""
import asyncio
import logging
import time
from mitmproxy.script import concurrent
# Toggle between asyncio and thread-based alternatives.
if True:
    # Hooks can be async, which allows the hook to call async functions and perform async I/O
    # without blocking other requests. This is generally preferred for new addons.
    async def request(flow):
        logging.info(f"handle request: {flow.request.host}{flow.request.path}")
        await asyncio.sleep(5)
        logging.info(f"start  request: {flow.request.host}{flow.request.path}")
else:
    # Another option is to use @concurrent, which launches the hook in its own thread.
    # Please note that this generally opens the door to race conditions and decreases performance if not required.
    @concurrent  # Remove this to make it synchronous and see what happens
    def request(flow):
        logging.info(f"handle request: {flow.request.host}{flow.request.path}")
        time.sleep(5)
        logging.info(f"start  request: {flow.request.host}{flow.request.path}")
```

### Example: http-reply-from-proxy.py

```
"""Send a reply from the proxy without sending the request to the remote server."""
from mitmproxy import http
def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "http://example.com/path":
        flow.response = http.Response.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"},  # (optional) headers
        )
```

```
"""Add an HTTP header to each response."""
class AddHeader:
    def __init__(self):
        self.num = 0
    def response(self, flow):
        self.num = self.num + 1
        flow.response.headers["count"] = str(self.num)
addons = [AddHeader()]
```

### Example: shutdown.py

```
"""
A simple way of shutting down the mitmproxy instance to stop everything.
Usage:
    mitmproxy -s shutdown.py
    and then send a HTTP request to trigger the shutdown:
    curl --proxy localhost:8080 http://example.com/path
"""
import logging
from mitmproxy import ctx
from mitmproxy import http
def request(flow: http.HTTPFlow) -> None:
    # a random condition to make this example a bit more interactive
    if flow.request.pretty_url == "http://example.com/path":
        logging.info("Shutting down everything...")
        ctx.master.shutdown()
```

### Example: wsgi-flask-app.py

```
"""
Host a WSGI app in mitmproxy.
This example shows how to graft a WSGI app onto mitmproxy. In this
instance, we're using the Flask framework (http://flask.pocoo.org/) to expose
a single simplest-possible page.
"""
from flask import Flask
from mitmproxy.addons import asgiapp
app = Flask("proxapp")
@app.route("/")
def hello_world() -> str:
    return "Hello World!"
addons = [
    # Host app at the magic domain "example.com" on port 80. Requests to this
    # domain and port combination will now be routed to the WSGI app instance.
    asgiapp.WSGIApp(app, "example.com", 80),
    # TLS works too, but the magic domain needs to be resolvable from the mitmproxy machine due to mitmproxy's design.
    # mitmproxy will connect to said domain and use its certificate but won't send any data.
    # By using `--set upstream_cert=false` and `--set connection_strategy_lazy` the local certificate is used instead.
    # asgiapp.WSGIApp(app, "example.com", 443),
]
```

### Example: http-stream-simple.py

```
"""
Select which responses should be streamed.
Enable response streaming for all HTTP flows.
This is equivalent to passing `--set stream_large_bodies=1` to mitmproxy.
"""
def responseheaders(flow):
    """
    Enables streaming for all responses.
    This is equivalent to passing `--set stream_large_bodies=1` to mitmproxy.
    """
    flow.response.stream = True
```

### Example: tcp-simple.py

```
"""
Process individual messages from a TCP connection.
This script replaces full occurrences of "foo" with "bar" and prints various details for each message.
Please note that TCP is stream-based and *not* message-based. mitmproxy splits stream contents into "messages"
as they are received by socket.recv(). This is pretty arbitrary and should not be relied on.
However, it is sometimes good enough as a quick hack.
Example Invocation:
    mitmdump --tcp-hosts ".*" -s examples/tcp-simple.py
"""
import logging
from mitmproxy import tcp
from mitmproxy.utils import strutils
def tcp_message(flow: tcp.TCPFlow):
    message = flow.messages[-1]
    message.content = message.content.replace(b"foo", b"bar")
    logging.info(
        f"tcp_message[from_client={message.from_client}), content={strutils.bytes_to_escaped_str(message.content)}]"
    )
```

### Example: http-modify-form.py

```
"""Modify an HTTP form submission."""
from mitmproxy import http
def request(flow: http.HTTPFlow) -> None:
    if flow.request.urlencoded_form:
        # If there's already a form, one can just add items to the dict:
        flow.request.urlencoded_form["mitmproxy"] = "rocks"
    else:
        # One can also just pass new form data.
        # This sets the proper content type and overrides the body.
        flow.request.urlencoded_form = [("foo", "bar")]  # type: ignore[assignment]
```

### Example: log-events.py

```
"""Post messages to mitmproxy's event log."""
import logging
from mitmproxy.addonmanager import Loader
from mitmproxy.log import ALERT
logger = logging.getLogger(__name__)
def load(loader: Loader):
    logger.info("This is some informative text.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")
    logger.log(
        ALERT,
        "This is an alert. It has the same urgency as info, but will also pop up in the status bar.",
    )
```