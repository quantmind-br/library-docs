---
title: Pricing · Cloudflare Images docs
url: https://developers.cloudflare.com/images/pricing/index.md
source: llms
fetched_at: 2026-01-24T15:15:10.780531946-03:00
rendered_js: false
word_count: 964
summary: This document explains the pricing structure and billing metrics for Cloudflare Images, detailing the usage limits and costs associated with image transformation, storage, and delivery across free and paid plans.
tags:
    - cloudflare-images
    - pricing
    - billing-metrics
    - image-transformation
    - image-storage
    - image-delivery
category: reference
---

By default, all users are on the Images Free plan. The Free plan includes access to the transformations feature, which lets you optimize images stored outside of Images, like in R2.

The Paid plan allows transformations, as well as access to storage in Images.

Pricing is dependent on which features you use. The table below shows which metrics are used for each use case.

| Use case | Metrics | Availability |
| - | - | - |
| Optimize images stored outside of Images | Images Transformed | Free and Paid plans |
| Optimized images that are stored in Cloudflare Images | Images Stored, Images Delivered | Only Paid plans |

## Images Free

On the Free plan, you can request up to 5,000 unique transformations each month for free.

Once you exceed 5,000 unique transformations:

* Existing transformations in cache will continue to be served as expected.
* New transformations will return a `9422` error. If your source image is from the same domain where the transformation is served, then you can use the [`onerror` parameter](https://developers.cloudflare.com/images/transform-images/transform-via-url/#onerror) to redirect to the original image.
* You will not be charged for exceeding the limits in the Free plan.

To request more than 5,000 unique transformations each month, you can purchase an Images Paid plan.

## Images Paid

When you purchase an Images Paid plan, you can choose your own storage or add storage in Images.

| Metric | Pricing |
| - | - |
| Images Transformed | First 5,000 unique transformations included + $0.50 / 1,000 unique transformations / month |
| Images Stored | $5 / 100,000 images stored / month |
| Images Delivered | $1 / 100,000 images delivered / month |

If you optimize an image stored outside of Images, then you will be billed only for Images Transformed.

Alternatively, Images Stored and Images Delivered apply only to images that are stored in your Images bucket. When you optimize an image that is stored in Images, then this counts toward Images Delivered — not Images Transformed.

## Metrics

### Images Transformed

A unique transformation is a request to transform an original image based on a set of [supported parameters](https://developers.cloudflare.com/images/transform-images/transform-via-url/#options). This metric is used only when optimizing images that are stored outside of Images.

For example, if you transform `thumbnail.jpg` as 100x100, then this counts as 1 unique transformation. If you transform the same `thumbnail.jpg` as 200x200, then this counts as a separate unique transformation.

You are billed for the number of unique transformations that are counted during each billing period.

Unique transformations are counted over a 30-day sliding window. For example, if you request `width=100/thumbnail.jpg` on June 30, then this counts once for that billing period. If you request the same transformation on July 1, then this will not count as a billable request, since the same transformation was already requested within the last 30 days.

The `format` parameter counts as only 1 billable transformation, even if multiple copies of an image are served. In other words, if `width=100,format=auto/thumbnail.jpg` is served to some users as AVIF and to others as WebP, then this counts as 1 unique transformation instead of 2.

#### Example #1

If you serve 2,000 remote images in five different sizes each month, then this results in 10,000 unique transformations. Your estimated cost for the month would be:

| | Usage | Included | Billable quantity | Price |
| - | - | - | - | - |
| Transformations | 10,000 unique transformations [1](#user-content-fn-5) | 5,000 | 5,000 | $2.50 [2](#user-content-fn-6) |

#### Example #2

If you use [R2](https://developers.cloudflare.com/r2/) for storage then your estimated monthly costs will be the sum of your monthly Images costs and monthly [R2 costs](https://developers.cloudflare.com/r2/pricing/#storage-usage).

For example, if you upload 5,000 images to R2 with an average size of 5 MB, and serve 2,000 of those images in five different sizes, then your estimated cost for the month would be:

| | Usage | Included | Billable quantity | Price |
| - | - | - | - | - |
| Storage | 25 GB [3](#user-content-fn-1) | 10 GB | 15 GB | $0.22 [4](#user-content-fn-7) |
| Class A operations | 5,000 writes [5](#user-content-fn-2) | 1 million | 0 | $0.00 [6](#user-content-fn-8) |
| Class B operations | 10,000 reads [7](#user-content-fn-3) | 10 million | 0 | $0.00 [8](#user-content-fn-9) |
| Transformations | 10,000 unique transformations [9](#user-content-fn-4) | 5,000 | 5,000 | $2.50 [10](#user-content-fn-10) |
| **Total** | | | | **$2.72** |

### Images Stored

Storage in Images is available only with an Images Paid plan. You can purchase storage in increments of $5 for every 100,000 images stored per month.

You can create predefined variants to specify how an image should be resized, such as `thumbnail` as 100x100 and `hero` as 1600x500.

Only uploaded images count toward Images Stored; defining variants will not impact your storage limit.

### Images Delivered

For images that are stored in Images, you will incur $1 for every 100,000 images delivered per month. This metric does not include transformed images that are stored in remote sources.

Every image requested by the browser counts as 1 billable request.

#### Example

A retail website has a product page that uses Images to serve 10 images. If the page was visited 10,000 times this month, then this results in 100,000 images delivered — or $1.00 in billable usage.

## Footnotes

1. 2,000 original images × 5 sizes [↩](#user-content-fnref-5)

2. (5,000 transformations / 1,000) × $0.50 [↩](#user-content-fnref-6)

3. 5,000 objects × 5 MB per object [↩](#user-content-fnref-1)

4. 15 GB × $0.015 / GB-month [↩](#user-content-fnref-7)

5. 5,000 objects × 1 write per object [↩](#user-content-fnref-2)

6. 0 × $4.50 / million requests [↩](#user-content-fnref-8)

7. 2,000 objects × 5 reads per object [↩](#user-content-fnref-3)

8. 0 × $0.36 / million requests [↩](#user-content-fnref-9)

9. 2,000 original images × 5 sizes [↩](#user-content-fnref-4)

10. (5,000 transformations / 1,000) × $0.50 [↩](#user-content-fnref-10)