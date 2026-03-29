---
title: SSL Error ... verify failed
url: https://epi052.github.io/feroxbuster-docs/faq/self-signed
source: github_pages
fetched_at: 2026-02-06T10:56:29.003822834-03:00
rendered_js: true
word_count: 60
summary: This document explains how to resolve SSL certificate verification errors in feroxbuster by using the insecure flag to bypass certificate validation.
tags:
    - feroxbuster
    - ssl-certificate
    - troubleshooting
    - tls-error
    - command-line-options
category: guide
---

## SSL Error routines:tls\_process\_server\_certificate:certificate verify failed

[Section titled “SSL Error routines:tls\_process\_server\_certificate:certificate verify failed”](#ssl-error-routinestls_process_server_certificatecertificate-verify-failed)

In the event you see an error similar to

![self-signed](https://epi052.github.io/feroxbuster-docs/images/insecure.png)

```

error trying to connect: error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:ssl/statem/statem_clnt.c:1913: (self signed certificate)
```

You just need to add the `-k|--insecure` flag to your command.

`feroxbuster` rejects self-signed certs and other “insecure” certificates/site configurations by default. You can choose to scan these services anyway by telling `feroxbuster` to ignore insecure server certs.