---
title: IAB Transparency & Consent Framework Compliance · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/consent-management/iab-tcf-compliance/index.md
source: llms
fetched_at: 2026-01-24T15:34:43.558992183-03:00
rendered_js: false
word_count: 103
summary: This document explains how to enable and configure IAB Transparency & Consent Framework compliance within the Zaraz Consent Management Platform to meet regulatory requirements.
tags:
    - zaraz
    - consent-management
    - iab-tcf
    - cloudflare-dashboard
    - privacy-compliance
    - ad-serving
category: guide
---

The Zaraz Consent Management Platform is compliant with the IAB Transparency & Consent Framework. Enabling this feature [could be required](https://blog.google/products/adsense/new-consent-management-platform-requirements-for-serving-ads-in-the-eea-and-uk/) in order to serve Google Ads in the EEA and the UK.

The CMP ID of the approval is 433 and be can seen in the [IAB Europe](https://iabeurope.eu/cmp-list/) website.

Using the Zaraz Consent Management Platform in IAB TCF Compliance Mode is is opt-in.

1. In the Cloudflare dashboard, go to the **Consent** page.

   [Go to **Consent**](https://dash.cloudflare.com/?to=/:account/tag-management/consent)

2. Check the **Use IAB TCF compliant modal** option.

3. Under the **Assign purposes to tools** section, add vendor details to every tool that was not automatically assigned.

4. Press **Save**.