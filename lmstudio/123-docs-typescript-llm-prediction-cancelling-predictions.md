---
title: Cancelling Predictions
url: https://lmstudio.ai/docs/typescript/llm-prediction/cancelling-predictions
source: sitemap
fetched_at: 2026-04-07T21:31:44.82699465-03:00
rendered_js: false
word_count: 137
summary: 'This document explains two methods for halting a running text prediction process using lmstudio-js: calling `.cancel()` on the prediction object or utilizing an existing `AbortController` signal.'
tags:
    - prediction-cancellation
    - lmstudio-js
    - abortcontroller
    - streaming-output
    - api-methods
category: guide
---

Sometimes you may want to halt a prediction before it finishes. For example, the user might change their mind or your UI may navigate away. `lmstudio-js` provides two simple ways to cancel a running prediction.

## 1. Call `.cancel()` on the prediction[](#1-call-cancel-on-the-prediction "Link to '1. Call ,[object Object], on the prediction'")

Every prediction method returns an `OngoingPrediction` instance. Calling `.cancel()` stops generation and causes the final `stopReason` to be `"userStopped"`. In the example below we schedule the cancel call on a timer:

## 2. Use an `AbortController`[](#2-use-an-abortcontroller "Link to '2. Use an ,[object Object]'")

If your application already uses an `AbortController` to propagate cancellation, you can pass its `signal` to the prediction method. Aborting the controller stops the prediction with the same `stopReason`:

Both approaches halt generation immediately, and the returned stats indicate that the prediction ended because you stopped it.