---
title: Configure scan from raw request
url: https://epi052.github.io/feroxbuster-docs/examples/raw-request
source: github_pages
fetched_at: 2026-02-06T10:55:57.428133334-03:00
rendered_js: true
word_count: 261
summary: This document explains how to initiate feroxbuster scans using raw request files and details how command-line parameters interact with, append to, or override the data provided in those files.
tags:
    - feroxbuster
    - raw-request
    - command-line-interface
    - web-security
    - request-parsing
    - configuration-management
category: configuration
---

## Configure a scan from a raw request (e.g. burp or similar)

[Section titled “Configure a scan from a raw request (e.g. burp or similar)”](#configure-a-scan-from-a-raw-request-eg-burp-or-similar)

Version 2.11.0 introduces the ability to begin a scan by passing in a raw request file.

The following table outlines the behavior of raw request and cli interactions. See the ‘with cli parameters’ example below for further details.

uniquenot uniqueheadersappendedoverridden by climethodsappendedignoreduser-agentn/aoverridden by clicookiesappendedoverridden by cliquery parametersappendedoverridden by cli

## Example: no additional parameters

[Section titled “Example: no additional parameters”](#example-no-additional-parameters)

Given the following command and raw request file

```

feroxbuster --request-file raw.request
```

```

POST / HTTP/1.1
Accept: */*
Host: localhost.com
User-Agent: feroxbuster/custom-raw
Cookie: derp=tronic; super=duper
Connection: keep-alive
body
```

We get the following feroxbuster configuration.

```

───────────────────────────┬──────────────────────
🎯  Target Url            │ https://localhost.com/
🚀  Threads               │ 50
📖  Wordlist              │ /wordlists/seclists/Discovery/Web-Content/common.txt
👌  Status Codes          │ All Status Codes!
💥  Timeout (secs)        │ 7
🦡  User-Agent            │ feroxbuster/custom-raw
🔒  Default Protocol      │ https
💉  Config File           │ /home/epi/feroxbuster/ferox-config.toml
🤯  Header                │ Accept: */*
🤯  Header                │ Host: localhost.com
🤯  Header                │ Cookie: derp=tronic; super=duper
🤯  Header                │ Connection: keep-alive
🔎  Extract Links         │ true
🏁  HTTP methods          │ [GET, POST]
💣  HTTP Body             │ body
🔃  Recursion Depth       │ 4
🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
```

## Example: with cli parameters

[Section titled “Example: with cli parameters”](#example-with-cli-parameters)

Given the same raw request file, we can alter the scan’s configuration with feroxbuster’s cli options. Depending on the context of the raw request and the option provided, the resulting configuration value may be ‘in addition to’ or ‘complete override’.

We’ll craft an example with two headers: one that doesn’t exist in the raw request and one that does.

```

feroxbuster --request-file raw.request --headers thedude:abides Host:overridden.com
```

```

POST / HTTP/1.1
Accept: */*
Host: localhost.com
User-Agent: feroxbuster/custom-raw
Cookie: derp=tronic; super=duper
Connection: keep-alive
body
```

Take note that `thedude` header is added to the existing list of headers, while `Host` has its value replaced with what was provided on the command line.

```

───────────────────────────┬──────────────────────
🎯  Target Url            │ https://overridden.com/
🚀  Threads               │ 50
📖  Wordlist              │ /wordlists/seclists/Discovery/Web-Content/common.txt
👌  Status Codes          │ All Status Codes!
💥  Timeout (secs)        │ 7
🦡  User-Agent            │ feroxbuster/custom-raw
🔒  Default Protocol      │ https
💉  Config File           │ /home/epi/feroxbuster/ferox-config.toml
🤯  Header                │ thedude: abides
🤯  Header                │ Host: overridden.com
🤯  Header                │ Accept: */*
🤯  Header                │ Connection: keep-alive
🤯  Header                │ Cookie: derp=tronic; super=duper
🔎  Extract Links         │ true
🏁  HTTP methods          │ [GET, POST]
💣  HTTP Body             │ body
🔃  Recursion Depth       │ 4
🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
```

## Example: using —protocol

[Section titled “Example: using —protocol”](#example-using-protocol)

Within a raw request, it’s typical to not have an associated protocol within the `Host` header.

```

GET / HTTP/1.1
Host: localhost.com
```

`feroxbuster` uses the `--protocol` option to designate what should be placed in front of the domain. By default, it’s `https`, but can be changed to `http` if needed.

```

feroxbuster --request-file raw.request --protocol http
```

Note the `Target Url` field is now `http` instead of `https`, as seen in previous examples.

```

───────────────────────────┬──────────────────────
🎯  Target Url            │ http://localhost.com/
🚀  Threads               │ 50
📖  Wordlist              │ /wordlists/seclists/Discovery/Web-Content/common.txt
👌  Status Codes          │ All Status Codes!
💥  Timeout (secs)        │ 7
🦡  User-Agent            │ feroxbuster/2.11.0
🔓  Default Protocol      │ http
💉  Config File           │ /home/epi/feroxbuster/ferox-config.toml
🤯  Header                │ Host: localhost.com
🔎  Extract Links         │ true
🏁  HTTP methods          │ [GET]
🔃  Recursion Depth       │ 4
🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
```