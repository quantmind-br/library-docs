---
title: Cancelling Predictions
url: https://lmstudio.ai/docs/python/llm-prediction/cancelling-predictions
source: sitemap
fetched_at: 2026-04-07T21:31:05.026760417-03:00
rendered_js: false
word_count: 53
summary: This document explains how using a streaming API allows developers to cancel a prediction request based on custom, application-specific conditions beyond standard configuration limits.
tags:
    - streaming-api
    - request-cancellation
    - prediction-control
    - llm-interaction
category: guide
---

One benefit of using the streaming API is the ability to cancel the prediction request based on criteria that can't be represented using the `stopStrings` or `maxPredictedTokens` configuration settings.

The following snippet illustrates cancelling the request in response to an application specification cancellation condition (such as polling an event set by another thread).

```
import lmstudio as lms
model = lms.llm()

prediction_stream = model.respond_stream("What is the meaning of life?")
cancelled = False
for fragment in prediction_stream:
    if ...: # Cancellation condition will be app specific
        cancelled = True
        prediction_stream.cancel()
        # Note: it is recommended to let the iteration complete,
        # as doing so allows the partial result to be recorded.
        # Breaking the loop *is* permitted, but means the partial result
        # and final prediction stats won't be available to the client
# The stream allows the prediction result to be retrieved after iteration
if not cancelled:
    print(prediction_stream.result())
```