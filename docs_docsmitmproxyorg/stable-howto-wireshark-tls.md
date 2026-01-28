---
title: Wireshark and SSL/TLS
url: https://docs.mitmproxy.org/stable/howto/wireshark-tls/
source: crawler
fetched_at: 2026-01-28T15:51:27.318736092-03:00
rendered_js: false
word_count: 167
summary: This document explains how to enable SSL/TLS master key logging in mitmproxy for external packet decryption tools like Wireshark.
tags:
    - ssl-tls
    - decryption
    - wireshark
    - environment-variables
    - proxy
    - network-traffic
category: tutorial
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/docs/src/content/howto/wireshark-tls.md)

## Wireshark and SSL/TLS Master Secrets

The SSL/TLS master keys can be logged by mitmproxy so that external programs can decrypt SSL/TLS connections both from and to the proxy. Recent versions of Wireshark can use these log files to decrypt packets. See the [Wireshark wiki](https://wiki.wireshark.org/TLS#using-the-pre-master-secret) for more information.

Key logging is enabled by setting the environment variable `SSLKEYLOGFILE` so that it points to a writable text file:

```
SSLKEYLOGFILE="$PWD/.mitmproxy/sslkeylogfile.txt" mitmproxy
```

You can also `export` this environment variable to make it persistent for all applications started from your current shell session.

You can specify the key file path in Wireshark via `Edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename`. If your SSLKEYLOGFILE does not exist yet, just create an empty text file, so you can select it in Wireshark (or run mitmproxy to create and collect master secrets).

Note that `SSLKEYLOGFILE` is respected by other programs as well, e.g., Firefox and Chrome. If this creates any issues, you can use `MITMPROXY_SSLKEYLOGFILE` instead without affecting other applications.