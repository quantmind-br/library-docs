---
title: GeoIP & Proxy Support | Camoufox
url: https://camoufox.com/python/geoip/
source: crawler
fetched_at: 2026-02-14T14:05:44.094319-03:00
rendered_js: true
word_count: 146
summary: This document explains how to use the Camoufox GeoIP feature to automatically spoof geographic and regional browser metadata based on a proxy or target IP address.
tags:
    - camoufox
    - geoip-spoofing
    - proxy-integration
    - browser-fingerprinting
    - python-automation
    - webrtc-spoofing
category: guide
---

By passing `geoip=True`, or passing in a target IP address, Camoufox will automatically use the target IP's longitude, latitude, timezone, country, locale, & spoof the WebRTC IP address.

It will also calculate and spoof the browser's language based on the distribution of language speakers in the target region.

![](https://camoufox.com/static/proxy-leak-demo.png)

* * *

## [#](#installation)Installation

Install Camoufox with the `geoip` extra:

```

pip install -U "camoufox[geoip]"
```

* * *

## [#](#usage)Usage

Pass in `geoip=True` with Playwright's `proxy` parameter. For example, with [Thordata](https://www.thordata.com/?ls=Browser&lk=camoufox1) proxies:

```

with Camoufox(
    geoip=True,
    proxy={
        'server': 'http://thordata.com:8080',
        'username': 'username',
        'password': 'password'
    }
) as browser:
    page = browser.new_page()
    page.goto("https://www.browserscan.net")
```

**Check out Thordata's residential proxies!**

### Sponsor

[![Thordata Banner](https://camoufox.com/static/thordata.png)](https://www.thordata.com/?ls=Browser&lk=camoufox1)

[Thordata](https://www.thordata.com/?ls=Browser&lk=camoufox1) - Your First Plan is on Us! 💰 Get 100% of your first residential proxy purchase back as wallet balance, up to $900.

#### [#](#-why-thordata)**⚡ Why Thordata?**

🌍 190+ real residential & ISP IP locations  
🔐 Fully encrypted, ultra-secure connections  
🚀 Optimized for web scraping, ad verification & automation workflows

🔥 Don't wait - this is your **best time to start** with [Thordata](https://www.thordata.com/?ls=Browser&lk=camoufox1) and experience the safest, fastest proxy network.