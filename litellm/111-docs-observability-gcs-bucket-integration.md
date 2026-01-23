---
title: Google Cloud Storage Buckets | liteLLM
url: https://docs.litellm.ai/docs/observability/gcs_bucket_integration
source: sitemap
fetched_at: 2026-01-21T19:46:03.945654075-03:00
rendered_js: false
word_count: 114
summary: This document provides step-by-step instructions for configuring LiteLLM to log request and response data directly to Google Cloud Storage (GCS) buckets.
tags:
    - litellm
    - google-cloud-storage
    - logging
    - callbacks
    - gcs-bucket
    - cloud-logging
category: tutorial
---

Log LLM Logs to [Google Cloud Storage Buckets](https://cloud.google.com/storage?hl=en)

### Usage[​](#usage "Direct link to Usage")

1. Add `gcs_bucket` to LiteLLM Config.yaml

```
model_list:
-litellm_params:
api_base: https://openai-function-calling-workers.tasslexyz.workers.dev/
api_key: my-fake-key
model: openai/my-fake-model
model_name: fake-openai-endpoint

litellm_settings:
callbacks:["gcs_bucket"]# 👈 KEY CHANGE # 👈 KEY CHANGE
```

2. Set required env variables

```
GCS_BUCKET_NAME="<your-gcs-bucket-name>"
GCS_PATH_SERVICE_ACCOUNT="/Users/ishaanjaffer/Downloads/adroit-crow-413218-a956eef1a2a8.json" # Add path to service account.json
```

3. Start Proxy

```
litellm --config /path/to/config.yaml
```

4. Test it!

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "fake-openai-endpoint",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ],
    }
'
```

## Expected Logs on GCS Buckets[​](#expected-logs-on-gcs-buckets "Direct link to Expected Logs on GCS Buckets")

### Fields Logged on GCS Buckets[​](#fields-logged-on-gcs-buckets "Direct link to Fields Logged on GCS Buckets")

[**The standard logging object is logged on GCS Bucket**](https://docs.litellm.ai/docs/proxy/logging)

## Getting `service_account.json` from Google Cloud Console[​](#getting-service_accountjson-from-google-cloud-console "Direct link to getting-service_accountjson-from-google-cloud-console")

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Search for IAM & Admin
3. Click on Service Accounts
4. Select a Service Account
5. Click on 'Keys' -&gt; Add Key -&gt; Create New Key -&gt; JSON
6. Save the JSON file and add the path to `GCS_PATH_SERVICE_ACCOUNT`

## Support & Talk to Founders[​](#support--talk-to-founders "Direct link to Support & Talk to Founders")

- [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
- [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
- Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
- Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)