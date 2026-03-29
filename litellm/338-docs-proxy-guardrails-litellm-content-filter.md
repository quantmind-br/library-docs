---
title: LiteLLM Content Filter (Built-in Guardrails) | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/litellm_content_filter
source: sitemap
fetched_at: 2026-01-21T19:52:19.471945069-03:00
rendered_js: false
word_count: 893
summary: This document explains how to implement LiteLLM's built-in content filter guardrail to detect and filter sensitive information using regex and keyword matching. It provides detailed instructions for configuration via UI and YAML, covering PII protection, custom patterns, and real-time streaming support.
tags:
    - litellm
    - content-filtering
    - guardrails
    - pii-protection
    - data-masking
    - regex-patterns
    - llm-security
category: guide
---

**Built-in guardrail** for detecting and filtering sensitive information using regex patterns and keyword matching. No external dependencies required.

**When to use?** Good for cases which do not require an ML model to detect sensitive information.

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionOn-device guardrail for detecting and filtering sensitive information using regex patterns and keyword matching. Built into LiteLLM with no external dependencies.Guardrail Name`litellm_content_filter`Detection MethodsPrebuilt regex patterns, custom regex, keyword matchingActions`BLOCK` (reject request), `MASK` (redact content)Supported Modes`pre_call`, `post_call`, `during_call` (streaming)PerformanceFast - runs locally, no external API calls

## Quick Start[​](#quick-start "Direct link to Quick Start")

## LiteLLM UI[​](#litellm-ui "Direct link to LiteLLM UI")

### Step 1: Select LiteLLM Content Filter[​](#step-1-select-litellm-content-filter "Direct link to Step 1: Select LiteLLM Content Filter")

Click "Add New Guardrail" and select "LiteLLM Content Filter" as your guardrail provider.

![Select LiteLLM Content Filter](https://docs.litellm.ai/assets/images/create_guard-f4e4ee364411cd75d5b09bcac9f35e6e.gif)

### Step 2: Configure Pattern Detection[​](#step-2-configure-pattern-detection "Direct link to Step 2: Configure Pattern Detection")

Select the prebuilt entities you want to block or mask. In this example, we select "Email" to detect and block email addresses.

If you need to block a custom entity, you can add a custom regex pattern by clicking "Add custom regex".

![Select prebuilt entities or add custom regex](https://docs.litellm.ai/assets/images/add_Guard2-fd53a24d9f5b85eebcc6cade06d9e5d5.gif)

### Step 3: Add Blocked Keywords[​](#step-3-add-blocked-keywords "Direct link to Step 3: Add Blocked Keywords")

Enter specific keywords you want to block. This is useful if you have policies to block certain words or phrases.

![Add blocked keywords](https://docs.litellm.ai/assets/images/create_guard3-a8c891192a37ca78ac56c12486eece92.gif)

### Step 4: Test Your Guardrail[​](#step-4-test-your-guardrail "Direct link to Step 4: Test Your Guardrail")

After creating the guardrail, navigate to "Test Playground" to test it. Select the guardrail you just created.

Test examples:

- **Blocked keyword test**: Entering "hi blue" will trigger the block since we set "blue" as a blocked keyword
- **Pattern detection test**: Entering "Hi [ishaan@berri.ai](mailto:ishaan@berri.ai)" will trigger the email pattern detector

![Test guardrail in playground](https://docs.litellm.ai/assets/images/add_guard5-46f34fd458f334fff0c2266f62e89de6.gif)

## LiteLLM Config.yaml Setup[​](#litellm-configyaml-setup "Direct link to LiteLLM Config.yaml Setup")

### Step 1: Define Guardrails in config.yaml[​](#step-1-define-guardrails-in-configyaml "Direct link to Step 1: Define Guardrails in config.yaml")

- Harmful Content Detection
- PII Protection
- Combined

config.yaml

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"harmful-content-filter"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"

# Enable harmful content categories
categories:
-category:"harmful_self_harm"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

-category:"harmful_violence"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

-category:"harmful_illegal_weapons"
enabled:true
action:"BLOCK"
severity_threshold:"medium"
```

### Step 2: Start LiteLLM Gateway[​](#step-2-start-litellm-gateway "Direct link to Step 2: Start LiteLLM Gateway")

```
litellm --config config.yaml
```

### Step 3: Test Request[​](#step-3-test-request "Direct link to Step 3: Test Request")

- SSN Blocked
- Email Masked

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "My SSN is 123-45-6789"}
    ],
    "guardrails": ["content-filter-pre"]
  }'
```

**Response: HTTP 400 Error**

```
{
"error":{
"message":{
"error":"Content blocked: us_ssn pattern detected",
"pattern":"us_ssn"
},
"code":"400"
}
}
```

## Configuration[​](#configuration "Direct link to Configuration")

### Supported Modes[​](#supported-modes "Direct link to Supported Modes")

- **`pre_call`** - Run before LLM call, filters input messages
- **`post_call`** - Run after LLM call, filters output responses
- **`during_call`** - Run during streaming, filters each chunk in real-time

### Actions[​](#actions "Direct link to Actions")

- **`BLOCK`** - Reject the request with HTTP 400 error
- **`MASK`** - Replace sensitive content with redaction tags (e.g., `[EMAIL_REDACTED]`)

## Prebuilt Patterns[​](#prebuilt-patterns "Direct link to Prebuilt Patterns")

### Available Patterns[​](#available-patterns "Direct link to Available Patterns")

Pattern NameDescriptionExample`us_ssn`US Social Security Numbers`123-45-6789``email`Email addresses`user@example.com``phone`Phone numbers`+1-555-123-4567``visa`Visa credit cards`4532-1234-5678-9010``mastercard`Mastercard credit cards`5425-2334-3010-9903``amex`American Express cards`3782-822463-10005``aws_access_key`AWS access keys`AKIAIOSFODNN7EXAMPLE``aws_secret_key`AWS secret keys`wJalrXUtnFEMI/K7MDENG/bPxRfi...``github_token`GitHub tokens`example-github-token-123`

### Using Prebuilt Patterns[​](#using-prebuilt-patterns "Direct link to Using Prebuilt Patterns")

config.yaml

```
guardrails:
-guardrail_name:"pii-filter"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"
patterns:
-pattern_type:"prebuilt"
pattern_name:"us_ssn"
action:"BLOCK"

-pattern_type:"prebuilt"
pattern_name:"email"
action:"MASK"

-pattern_type:"prebuilt"
pattern_name:"aws_access_key"
action:"BLOCK"
```

## Custom Regex Patterns[​](#custom-regex-patterns "Direct link to Custom Regex Patterns")

Define your own regex patterns for domain-specific sensitive data:

config.yaml

```
guardrails:
-guardrail_name:"custom-patterns"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"
patterns:
# Custom employee ID format
-pattern_type:"regex"
pattern:'\b[A-Z]{3}-\d{4}\b'
name:"employee_id"
action:"MASK"

# Custom project code format
-pattern_type:"regex"
pattern:'PROJECT-\d{6}'
name:"project_code"
action:"BLOCK"
```

## Keyword Filtering[​](#keyword-filtering "Direct link to Keyword Filtering")

Block or mask specific keywords:

config.yaml

```
guardrails:
-guardrail_name:"keyword-filter"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"
blocked_words:
-keyword:"confidential"
action:"BLOCK"
description:"Internal confidential information"

-keyword:"proprietary"
action:"MASK"
description:"Proprietary company data"

-keyword:"secret_project"
action:"BLOCK"
```

### Loading Keywords from File[​](#loading-keywords-from-file "Direct link to Loading Keywords from File")

For large keyword lists, use a YAML file:

config.yaml

```
guardrails:
-guardrail_name:"keyword-file-filter"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"
blocked_words_file:"/path/to/sensitive_keywords.yaml"
```

sensitive\_keywords.yaml

```
blocked_words:
-keyword:"project_apollo"
action:"BLOCK"
description:"Confidential project codename"

-keyword:"internal_api"
action:"MASK"
description:"Internal API references"

-keyword:"customer_database"
action:"BLOCK"
description:"Protected database name"
```

## Streaming Support[​](#streaming-support "Direct link to Streaming Support")

Content filter works with streaming responses by checking each chunk:

config.yaml

```
guardrails:
-guardrail_name:"streaming-filter"
litellm_params:
guardrail: litellm_content_filter
mode:"during_call"# Check each streaming chunk
patterns:
-pattern_type:"prebuilt"
pattern_name:"email"
action:"MASK"
```

```
import openai

client = openai.OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me about yourself"}],
    stream=True,
    extra_body={"guardrails":["streaming-filter"]}
)

for chunk in response:
print(chunk.choices[0].delta.content)
# Emails automatically masked in real-time
```

## Image Content Filtering[​](#image-content-filtering "Direct link to Image Content Filtering")

Content filter can analyze images by generating descriptions and applying filters to the text descriptions.

warning

This can introduce significant latency to the request - depending on the speed of the vision-capable model.

This is because, each request containing images will be sent to the vision-capable model to generate a description.

### Configuration[​](#configuration-1 "Direct link to Configuration")

config.yaml

```
model_list:
-model_name: gpt-4-vision
litellm_params:
model: openai/gpt-4-vision-preview
api_key: os.environ/OPENAI_API_KEY

guardrails:
-guardrail_name:"image-filter"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"
image_model:"gpt-4-vision"# value is `model_name` of the vision-capable model

# Apply same filters to image descriptions
categories:
-category:"harmful_violence"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

patterns:
-pattern_type:"prebuilt"
pattern_name:"email"
action:"MASK"
```

### How It Works[​](#how-it-works "Direct link to How It Works")

1. Image is sent to the vision model to generate a text description
2. Content filters are applied to the description
3. If harmful content is detected, request is blocked with context about the image

**Example:**

```
import openai

client = openai.OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

response = client.chat.completions.create(
    model="gpt-4-vision",
    messages=[{
"role":"user",
"content":[
{"type":"text","text":"What's in this image?"},
{"type":"image_url","image_url":{"url":"https://example.com/image.jpg"}}
]
}],
    extra_body={"guardrails":["image-filter"]}
)
```

If the image description contains filtered content, you'll get:

```
{
"error":"Content blocked: harmful_violence category keyword 'weapon' detected (severity: high) (Image description): The image shows..."
}
```

When using the `MASK` action, sensitive content is replaced with redaction tags. You can customize how these tags appear.

### Default Behavior[​](#default-behavior "Direct link to Default Behavior")

**Patterns:** Each pattern type gets its own tag based on the pattern name

```
Input:  "My email is john@example.com and SSN is 123-45-6789"
Output: "My email is [EMAIL_REDACTED] and SSN is [US_SSN_REDACTED]"
```

**Keywords:** All keywords use the same generic tag

```
Input:  "This is confidential and proprietary information"
Output: "This is [KEYWORD_REDACTED] and [KEYWORD_REDACTED] information"
```

### Customizing Tags[​](#customizing-tags "Direct link to Customizing Tags")

Use `pattern_redaction_format` and `keyword_redaction_tag` to change the redaction format:

config.yaml

```
guardrails:
-guardrail_name:"custom-redaction"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"
pattern_redaction_format:"***{pattern_name}***"# Use {pattern_name} placeholder
keyword_redaction_tag:"***REDACTED***"
patterns:
-pattern_type:"prebuilt"
pattern_name:"email"
action:"MASK"
-pattern_type:"prebuilt"
pattern_name:"us_ssn"
action:"MASK"
blocked_words:
-keyword:"confidential"
action:"MASK"
```

**Output:**

```
Input:  "Email john@example.com, SSN 123-45-6789, confidential data"
Output: "Email ***EMAIL***, SSN ***US_SSN***, ***REDACTED*** data"
```

**Key Points:**

- `pattern_redaction_format` must include `{pattern_name}` placeholder
- Pattern names are automatically uppercased (e.g., `email` → `EMAIL`)
- `keyword_redaction_tag` is a fixed string (no placeholders)

## Content Categories[​](#content-categories "Direct link to Content Categories")

Prebuilt categories use **keyword matching** to detect harmful content, bias, and inappropriate advice. Keywords are matched with word boundaries (single words) or as substrings (multi-word phrases), case-insensitive.

### Available Categories[​](#available-categories "Direct link to Available Categories")

CategoryDescription**Harmful Content**`harmful_self_harm`Self-harm, suicide, eating disorders`harmful_violence`Violence, criminal planning, attacks`harmful_illegal_weapons`Illegal weapons, explosives, dangerous materials**Bias Detection**`bias_gender`Gender-based discrimination, stereotypes`bias_sexual_orientation`LGBTQ+ discrimination, homophobia, transphobia`bias_racial`Racial/ethnic discrimination, stereotypes`bias_religious`Religious discrimination, stereotypes**Denied Advice**`denied_financial_advice`Personalized financial advice, investment recommendations`denied_medical_advice`Medical advice, diagnosis, treatment recommendations`denied_legal_advice`Legal advice, representation, legal strategy

Bias Detection Considerations

Bias detection is **complex and context-dependent**. Rule-based systems catch explicit discriminatory language but may generate false positives on legitimate discussions. Start with **high severity thresholds** and test thoroughly. For mission-critical bias detection, consider combining with AI-based guardrails (e.g., HiddenLayer, Lakera).

### Configuration[​](#configuration-2 "Direct link to Configuration")

config.yaml

```
guardrails:
-guardrail_name:"content-filter"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"

categories:
-category:"harmful_self_harm"
enabled:true
action:"BLOCK"
severity_threshold:"medium"# Blocks medium+ severity

-category:"bias_gender"
enabled:true
action:"BLOCK"
severity_threshold:"high"# Only explicit discrimination

-category:"denied_financial_advice"
enabled:true
action:"BLOCK"
severity_threshold:"medium"
```

**Severity Thresholds:**

- `"high"` - Only blocks high severity items
- `"medium"` - Blocks medium and high severity (default)
- `"low"` - Blocks all severity levels

### Custom Category Files[​](#custom-category-files "Direct link to Custom Category Files")

Override default categories with custom keyword lists:

config.yaml

```
categories:
-category:"harmful_self_harm"
enabled:true
action:"BLOCK"
severity_threshold:"medium"
category_file:"/path/to/custom.yaml"
```

custom.yaml

```
category_name:"harmful_self_harm"
description:"Custom self-harm detection"
default_action:"BLOCK"

keywords:
-keyword:"suicide"
severity:"high"
-keyword:"harm myself"
severity:"high"

exceptions:
-"suicide prevention"
-"mental health"
```

## Use Cases[​](#use-cases "Direct link to Use Cases")

### 1. Harmful Content Detection[​](#1-harmful-content-detection "Direct link to 1. Harmful Content Detection")

Block or detect requests containing harmful, illegal, or dangerous content:

```
categories:
-category:"harmful_self_harm"
enabled:true
action:"BLOCK"
severity_threshold:"medium"
-category:"harmful_violence"
enabled:true
action:"BLOCK"
severity_threshold:"high"
-category:"harmful_illegal_weapons"
enabled:true
action:"BLOCK"
severity_threshold:"medium"
```

### 2. Bias and Discrimination Detection[​](#2-bias-and-discrimination-detection "Direct link to 2. Bias and Discrimination Detection")

Detect and block biased, discriminatory, or hateful content across multiple dimensions:

```
categories:
# Gender-based discrimination
-category:"bias_gender"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

# LGBTQ+ discrimination
-category:"bias_sexual_orientation"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

# Racial/ethnic discrimination
-category:"bias_racial"
enabled:true
action:"BLOCK"
severity_threshold:"high"# Only explicit to reduce false positives

# Religious discrimination
-category:"bias_religious"
enabled:true
action:"BLOCK"
severity_threshold:"medium"
```

**Sensitivity Tuning:**

For bias detection, severity thresholds are critical to balance safety and legitimate discourse:

```
# Conservative (low false positives, may miss subtle bias)
categories:
-category:"bias_racial"
severity_threshold:"high"# Only blocks explicit discriminatory language

# Balanced (recommended)
categories:
-category:"bias_gender"
severity_threshold:"medium"# Blocks stereotypes and explicit discrimination

# Strict (high safety, may have more false positives)
categories:
-category:"bias_sexual_orientation"
severity_threshold:"low"# Blocks all potentially problematic content
```

### 3. PII Protection[​](#3-pii-protection "Direct link to 3. PII Protection")

Block or mask personally identifiable information before sending to LLMs:

```
patterns:
-pattern_type:"prebuilt"
pattern_name:"us_ssn"
action:"BLOCK"
-pattern_type:"prebuilt"
pattern_name:"email"
action:"MASK"
```

### 2. Credential Detection[​](#2-credential-detection "Direct link to 2. Credential Detection")

Prevent API keys and secrets from being exposed:

```
patterns:
-pattern_type:"prebuilt"
pattern_name:"aws_access_key"
action:"BLOCK"
-pattern_type:"prebuilt"
pattern_name:"github_token"
action:"BLOCK"
```

### 3. Sensitive Internal Data Protection[​](#3-sensitive-internal-data-protection "Direct link to 3. Sensitive Internal Data Protection")

Block or mask references to confidential internal projects, codenames, or proprietary information:

```
blocked_words:
-keyword:"project_titan"
action:"BLOCK"
description:"Confidential project codename"
-keyword:"internal_api"
action:"MASK"
description:"Internal system references"
```

For large lists of sensitive terms, use a file:

```
blocked_words_file:"/path/to/sensitive_terms.yaml"
```

### 4. Safe AI for Consumer Applications[​](#4-safe-ai-for-consumer-applications "Direct link to 4. Safe AI for Consumer Applications")

Combining harmful content and bias detection for consumer-facing AI:

```
guardrails:
-guardrail_name:"safe-consumer-ai"
litellm_params:
guardrail: litellm_content_filter
mode:"pre_call"

categories:
# Harmful content - strict
-category:"harmful_self_harm"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

-category:"harmful_violence"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

# Bias detection - balanced
-category:"bias_gender"
enabled:true
action:"BLOCK"
severity_threshold:"high"# Avoid blocking legitimate gender discussions

-category:"bias_sexual_orientation"
enabled:true
action:"BLOCK"
severity_threshold:"medium"

-category:"bias_racial"
enabled:true
action:"BLOCK"
severity_threshold:"high"# Education and news may discuss race
```

**Perfect for:**

- Chatbots and virtual assistants
- Educational AI tools
- Customer service AI
- Content generation platforms
- Public-facing AI applications

### 5. Compliance[​](#5-compliance "Direct link to 5. Compliance")

Ensure regulatory compliance by filtering sensitive data types:

```
# Categories checked first (high priority)
# Category keywords are matched first
categories:
-category:"harmful_self_harm"
severity_threshold:"high"

# Then regex patterns
patterns:
-pattern_type:"prebuilt"
pattern_name:"visa"
action:"BLOCK"
-pattern_type:"prebuilt"
pattern_name:"us_ssn"
action:"BLOCK"
```