---
title: Event Hooks
url: https://docs.mitmproxy.org/stable/api/events.html
source: crawler
fetched_at: 2026-01-28T15:01:12.738487829-03:00
rendered_js: false
word_count: 1152
summary: This document explains the various event hooks available in mitmproxy addons, detailing their lifecycle, HTTP, DNS, TCP, UDP, QUIC, TLS, WebSocket, SOCKS5, and advanced lifecycle events.
tags:
    - mitmproxy
    - addons
    - event-hooks
    - http-events
    - tls-events
    - websocket
    - network-protocol
    - proxy
category: reference
---

Addons hook into mitmproxy’s internal mechanisms through event hooks. These are implemented on addons as methods with a set of well-known names. Many events receive `Flow` objects as arguments - by modifying these objects, addons can change traffic on the fly. For instance, here is an addon that adds a response header with a count of the number of responses seen:

The following addons list all available event hooks.

Lifecycle Events

[](#LifecycleEvents)

Called when an addon is first loaded. This event receives a Loader object, which contains methods for adding options and commands. This method is where the addon configures itself.

def running():

Called when the proxy is completely up and running. At this point, you can expect all addons to be loaded and all options to be set.

def configure(updated: set\[str]):

Called when configuration changes. The updated argument is a set-like object containing the keys of all changed options. This event is called during startup with all options in the updated set.

def done():

Called when the addon shuts down, either by being removed from the mitmproxy instance, or when mitmproxy itself shuts down. On shutdown, this event is called after the event loop is terminated, guaranteeing that it will be the final event an addon sees. Note that log handlers are shut down at this point, so calls to log functions will produce no output.

Connection Events

[](#ConnectionEvents)

A client has connected to mitmproxy. Note that a connection can correspond to multiple HTTP requests.

Setting client.error kills the connection.

A client connection has been closed (either by us or the client).

Mitmproxy is about to connect to a server. Note that a connection can correspond to multiple requests.

Setting data.server.error kills the connection.

Mitmproxy has connected to a server.

A server connection has been closed (either by us or the server).

Mitmproxy failed to connect to a server.

Every server connection will receive either a server\_connected or a server\_connect\_error event, but not both.

HTTP Events

[](#HTTPEvents)

The full HTTP request has been read.

Note: If request streaming is active, this event fires after the entire body has been streamed. HTTP trailers, if present, have not been transmitted to the server yet and can still be modified. Enabling streaming may cause unexpected event sequences: For example, `response` may now occur before `request` because the server replied with "413 Payload Too Large" during upload.

The full HTTP response has been read.

Note: If response streaming is active, this event fires after the entire body has been streamed. HTTP trailers, if present, have not been transmitted to the client yet and can still be modified.

An HTTP error has occurred, e.g. invalid server responses, or interrupted connections. This is distinct from a valid server HTTP error response, which is simply a response with an HTTP error code.

Every flow will receive either an error or an response event, but not both.

An HTTP CONNECT request was received. This event can be ignored for most practical purposes.

This event only occurs in regular and upstream proxy modes when the client instructs mitmproxy to open a connection to an upstream host. Setting a non 2xx response on the flow will return the response to the client and abort the connection.

CONNECT requests are HTTP proxy instructions for mitmproxy itself and not forwarded. They do not generate the usual HTTP handler events, but all requests going over the newly opened connection will.

An HTTP CONNECT request is about to be sent to an upstream proxy. This event can be ignored for most practical purposes.

This event can be used to set custom authentication headers for upstream proxies.

CONNECT requests do not generate the usual HTTP handler events, but all requests going over the newly opened connection will.

HTTP CONNECT was successful

*Warning*

This may fire before an upstream connection has been established if `connection_strategy` is set to `lazy` (default)

HTTP CONNECT has failed. This can happen when the upstream server is unreachable or proxy authentication is required. In contrast to the `error` hook, `flow.error` is not guaranteed to be set.

DNS Events

[](#DNSEvents)

A DNS query has been received.

A DNS response has been received or set.

A DNS error has occurred.

TCP Events

[](#TCPEvents)

A TCP connection has started.

A TCP connection has received a message. The most recent message will be flow.messages\[-1]. The message is user-modifiable.

A TCP connection has ended.

A TCP error has occurred.

Every TCP flow will receive either a tcp\_error or a tcp\_end event, but not both.

UDP Events

[](#UDPEvents)

A UDP connection has started.

A UDP connection has received a message. The most recent message will be flow.messages\[-1]. The message is user-modifiable.

A UDP connection has ended.

A UDP error has occurred.

Every UDP flow will receive either a udp\_error or a udp\_end event, but not both.

QUIC Events

[](#QUICEvents)

def quic\_start\_client(data: mitmproxy.proxy.layers.quic.\_hooks.QuicTlsData):

TLS negotiation between mitmproxy and a client over QUIC is about to start.

An addon is expected to initialize data.settings. (by default, this is done by `mitmproxy.addons.tlsconfig`)

def quic\_start\_server(data: mitmproxy.proxy.layers.quic.\_hooks.QuicTlsData):

TLS negotiation between mitmproxy and a server over QUIC is about to start.

An addon is expected to initialize data.settings. (by default, this is done by `mitmproxy.addons.tlsconfig`)

TLS Events

[](#TLSEvents)

Mitmproxy has received a TLS ClientHello message.

This hook decides whether a server connection is needed to negotiate TLS with the client (data.establish\_server\_tls\_first)

TLS negotation between mitmproxy and a client is about to start.

An addon is expected to initialize data.ssl\_conn. (by default, this is done by `mitmproxy.addons.tlsconfig`)

TLS negotation between mitmproxy and a server is about to start.

An addon is expected to initialize data.ssl\_conn. (by default, this is done by `mitmproxy.addons.tlsconfig`)

The TLS handshake with the client has been completed successfully.

The TLS handshake with the server has been completed successfully.

The TLS handshake with the client has failed.

The TLS handshake with the server has failed.

WebSocket Events

[](#WebSocketEvents)

A WebSocket connection has commenced.

Called when a WebSocket message is received from the client or server. The most recent message will be flow.messages\[-1]. The message is user-modifiable. Currently there are two types of messages, corresponding to the BINARY and TEXT frame types.

A WebSocket connection has ended. You can check `flow.websocket.close_code` to determine why it ended.

SOCKS5 Events

[](#SOCKS5Events)

def socks5\_auth(data: mitmproxy.proxy.layers.modes.Socks5AuthData):

Mitmproxy has received username/password SOCKS5 credentials.

This hook decides whether they are valid by setting `data.valid`.

Advanced Lifecycle Events

[](#AdvancedLifecycleEvents)

def next\_layer(data: mitmproxy.proxy.layer.NextLayer):

Network layers are being switched. You may change which layer will be used by setting data.layer.

(by default, this is done by mitmproxy.addons.NextLayer)

Update is called when one or more flow objects have been modified, usually from a different addon.

def add\_log(entry: mitmproxy.log.LogEntry):

**Deprecated:** Starting with mitmproxy 9, users should use the standard Python logging module instead, for example by calling `logging.getLogger().addHandler()`.

Called whenever a new log entry is created through the mitmproxy context. Be careful not to log from this event, which will cause an infinite loop!