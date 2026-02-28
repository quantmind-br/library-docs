---
title: Variant Models | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/launch/variant-models
source: crawler
fetched_at: 2026-02-27T23:41:56.941564-03:00
rendered_js: true
word_count: 372
summary: This document outlines the requirements and procedures for certifying product variants of Spotify Connect devices based on a previously approved model. It explains hardware and firmware eligibility criteria and provides step-by-step instructions for submission and auto-approval.
tags:
    - spotify-connect
    - device-certification
    - variant-model
    - hardware-requirements
    - firmware-compliance
    - certomato
category: guide
---

Before launching a product variant with Spotify Connect, all devices must be certified by Spotify. The **Variant Model certification** process lets partners quickly certify devices that are minor variations of an already approved model.

For example, if you have multiple devices that share the same firmware and no major hardware differences, only one device must go through full certification. All others can rely on that certification and be submitted as variant models.

Please do the following:

**1**. **Complete certification for the base model.**

If your base model has not yet been certified, follow the full [Spotify Connect certification process](https://certomato.spotify.com) before submitting any variant models.

* * *

**2**. **Confirm variant eligibility.**

A product can qualify as a variant if the differences from the certified model are **minor**.

**Allowed hardware changes:**

- Different color options
- Remote control or button layout changes  
  (no Spotify-specific buttons may be added)
- CD outlets
- Adding or removing a screen  
  (if a new screen is added, provide a video showing correct display of long strings)
- Different input or output sources

**Firmware requirements:**

- The **music playback firmware** must remain identical to the certified model.
- The **eSDK version** may only differ by a patch update:
  
  - Acceptable: `3.203.235 → 3.203.239`
  - Not acceptable: `3.202.356 → 3.203.239`
- If the product is built by a **system integrator**, the device must come from the **same partner** — cross-brand variants are not allowed.

* * *

**3**. **Ensure prerequisites are met.**

Before submitting a variant model for certification:

- Add the variant models in the **New Product Application form**(This can be found in Certomato [here](https://certomato.spotify.com/product-application/)).
- The original (base) model must already have passed certification in [Certomato](https://certomato.spotify.com).
- Open a [support ticket](https://spotify-service-desk.atlassian.net/servicedesk/customer/portal/3) and provide a **comparison table** outlining the exact differences between the base model and the variant.  
  This table must be **reviewed and approved by Spotify** before submission.
- Each variant model must have its **own unique product ID**.

* * *

**4**. **Submit the variant model in Certomato.**

Once the base model is certified:

- Go to **Certomato** and press **"Start new certification."**
- Select **"Variant model v1.0."**
- Choose the previously certified model as your base.
- Select your new model and click **"Start new certification."**

The model is now submitted as a variant and is immediately **auto-approved**!

* * *

That's it!

Your variant model is now approved and ready for launch under the existing Spotify Connect certification.