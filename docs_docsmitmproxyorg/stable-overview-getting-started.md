---
title: Getting Started
url: https://docs.mitmproxy.org/stable/overview/getting-started/
source: crawler
fetched_at: 2026-01-28T15:58:45.19047833-03:00
rendered_js: false
word_count: 239
summary: This guide explains how to install and configure mitmproxy tools to intercept and inspect web traffic, including setting up a browser proxy and installing the certificate authority.
tags:
    - proxy-interception
    - traffic-inspection
    - tls-interception
    - browser-configuration
    - certificate-installation
category: tutorial
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/overview/getting-started.md)

We assume you have already [installed](https://docs.mitmproxy.org/stable/overview/installation/) mitmproxy on your machine.

You can start any of our three tools from the command line / terminal.

- **mitmproxy** gives you an interactive command-line interface
- **mitmweb** gives you a browser-based GUI
- **mitmdump** gives you non-interactive terminal output

## Configure your browser or device

Mitmproxy starts as a [regular HTTP proxy](https://docs.mitmproxy.org/stable/concepts/modes/#regular-proxy) by default and listens on `http://localhost:8080`.

You need to configure your browser or device to route all traffic through mitmproxy. Browser versions and configurations options frequently change, so we recommend to simply search the web on how to configure an HTTP proxy for your system. Some operating system have a global settings, some browser have their own, other applications use environment variables, etc.

You can check that your web traffic is going through mitmproxy by browsing to [http://mitm.it](http://mitm.it) - it should present you with a [simple page](https://docs.mitmproxy.org/stable/concepts/certificates/#quick-setup) to install the mitmproxy Certificate Authority - which is also the next step. Follow the instructions for your OS / system and install the CA.

## Verifying everything works

At this point your running mitmproxy instance should already show the first HTTP flows from your client. You can test that all TLS-encrypted web traffic is working as expected by browsing to [https://mitmproxy.org](https://mitmproxy.org) - it should show up as new flow and you can inspect it.

## Resources

- [**GitHub**](https://github.com/mitmproxy/mitmproxy): If you want to ask usage questions, contribute to mitmproxy, or submit a bug report, please use GitHub.