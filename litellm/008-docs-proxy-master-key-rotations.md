---
title: Rotating Master Key | liteLLM
url: https://docs.litellm.ai/docs/proxy/master_key_rotations
source: sitemap
fetched_at: 2026-01-21T19:52:55.537609389-03:00
rendered_js: false
word_count: 133
summary: This document outlines the step-by-step procedure for rotating the master key used to encrypt models within the Proxy_ModelTable database.
tags:
    - master-key-rotation
    - database-encryption
    - litellm
    - security-management
    - key-regeneration
category: guide
---

Here are our recommended steps for rotating your master key.

**1. Backup your DB** In case of any errors during the encryption/de-encryption process, this will allow you to revert back to current state without issues.

**2. Call `/key/regenerate` with the new master key**

This will re-encrypt any models in your Proxy\_ModelTable with the new master key.

Expect to start seeing decryption errors in logs, as your old master key is no longer able to decrypt the new values.

**3. Update LITELLM\_MASTER\_KEY**

In your environment variables update the value of LITELLM\_MASTER\_KEY to the new\_master\_key from Step 2.

This ensures the key used for decryption from db is the new key.

**4. Test it**

Make a test request to a model stored on proxy with a litellm key (new master key or virtual key) and see if it works

```
 curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "model": "gpt-4o-mini", # 👈 REPLACE with 'public model name' for any db-model
    "messages": [
        {
            "content": "Hey, how's it going",
            "role": "user"
        }
    ],
}'
```