---
title: Using ChatLiteLLM() - Langchain | liteLLM
url: https://docs.litellm.ai/docs/langchain/
source: sitemap
fetched_at: 2026-01-21T19:45:33.716706976-03:00
rendered_js: false
word_count: 251
summary: This document provides a guide on integrating LangChain's ChatLiteLLM with various observability tools and implementing advanced metadata tagging for LLM request tracking.
tags:
    - litellm
    - langchain
    - observability
    - mlflow
    - metadata-tagging
    - llm-monitoring
    - cost-tracking
category: guide
---

## Pre-Requisites[​](#pre-requisites "Direct link to Pre-Requisites")

```
!pip install litellm langchain
```

## Quick Start[​](#quick-start "Direct link to Quick Start")

- OpenAI
- Anthropic
- Replicate
- Cohere

```
import os
from langchain_community.chat_models import ChatLiteLLM
from langchain_core.prompts import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

os.environ['OPENAI_API_KEY']=""
chat = ChatLiteLLM(model="gpt-3.5-turbo")
messages =[
    HumanMessage(
        content="what model are you"
)
]
chat.invoke(messages)
```

## Use Langchain ChatLiteLLM with MLflow[​](#use-langchain-chatlitellm-with-mlflow "Direct link to Use Langchain ChatLiteLLM with MLflow")

MLflow provides open-source observability solution for ChatLiteLLM.

To enable the integration, simply call `mlflow.litellm.autolog()` before in your code. No other setup is necessary.

```
import mlflow

mlflow.litellm.autolog()
```

Once the auto-tracing is enabled, you can invoke `ChatLiteLLM` and see recorded traces in MLflow.

```
import os
from langchain.chat_models import ChatLiteLLM

os.environ['OPENAI_API_KEY']="sk-..."

chat = ChatLiteLLM(model="gpt-4o-mini")
chat.invoke("Hi!")
```

## Use Langchain ChatLiteLLM with Lunary[​](#use-langchain-chatlitellm-with-lunary "Direct link to Use Langchain ChatLiteLLM with Lunary")

```
import os
from langchain.chat_models import ChatLiteLLM
from langchain.schema import HumanMessage
import litellm

os.environ["LUNARY_PUBLIC_KEY"]=""# from https://app.lunary.ai/settings
os.environ['OPENAI_API_KEY']="sk-..."

litellm.success_callback =["lunary"]
litellm.failure_callback =["lunary"]

chat = ChatLiteLLM(
  model="gpt-4o"
  messages =[
    HumanMessage(
        content="what model are you"
)
]
chat(messages)
```

Get more details [here](https://docs.litellm.ai/docs/observability/lunary_integration)

## Use LangChain ChatLiteLLM + Langfuse[​](#use-langchain-chatlitellm--langfuse "Direct link to Use LangChain ChatLiteLLM + Langfuse")

Checkout this section [here](https://docs.litellm.ai/docs/observability/langfuse_integration#use-langchain-chatlitellm--langfuse) for more details on how to integrate Langfuse with ChatLiteLLM.

Tags are a powerful feature in LiteLLM that allow you to categorize, filter, and track your LLM requests. When using LangChain with LiteLLM, you can pass tags through the `extra_body` parameter in the metadata.

### Basic Tag Usage[​](#basic-tag-usage "Direct link to Basic Tag Usage")

- OpenAI
- Anthropic
- LiteLLM Proxy

```
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ['OPENAI_API_KEY']="sk-your-key-here"

chat = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    extra_body={
"metadata":{
"tags":["production","customer-support","high-priority"]
}
}
)

messages =[
    SystemMessage(content="You are a helpful customer support assistant."),
    HumanMessage(content="How do I reset my password?")
]

response = chat.invoke(messages)
print(response)
```

### Advanced Tag Patterns[​](#advanced-tag-patterns "Direct link to Advanced Tag Patterns")

#### Dynamic Tags Based on Context[​](#dynamic-tags-based-on-context "Direct link to Dynamic Tags Based on Context")

```
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

defcreate_chat_with_tags(user_type:str, feature:str):
"""Create a chat instance with dynamic tags based on context"""

# Build tags dynamically
    tags =["langchain-integration"]

if user_type =="premium":
        tags.extend(["premium-user","high-priority"])
elif user_type =="enterprise":
        tags.extend(["enterprise","custom-sla"])
else:
        tags.append("standard-user")

# Add feature-specific tags
if feature =="code-review":
        tags.extend(["development","code-analysis"])
elif feature =="content-gen":
        tags.extend(["marketing","content-creation"])

return ChatOpenAI(
        openai_api_base="http://localhost:4000",
        model="gpt-4o",
        temperature=0.7,
        extra_body={
"metadata":{
"tags": tags,
"user_type": user_type,
"feature": feature,
"trace_user_id":f"user-{user_type}-{feature}"
}
}
)

# Usage examples
premium_chat = create_chat_with_tags("premium","code-review")
enterprise_chat = create_chat_with_tags("enterprise","content-gen")

messages =[HumanMessage(content="Help me with this task")]
response = premium_chat.invoke(messages)
```

#### Tags for Cost Tracking and Analytics[​](#tags-for-cost-tracking-and-analytics "Direct link to Tags for Cost Tracking and Analytics")

```
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Tags for cost tracking
cost_tracking_chat = ChatOpenAI(
    openai_api_base="http://localhost:4000",
    model="gpt-4o",
    temperature=0.7,
    extra_body={
"metadata":{
"tags":[
"cost-center-marketing",
"budget-q4-2024",
"project-launch-campaign",
"high-cost-model"# Flag for expensive models
],
"department":"marketing",
"project_id":"campaign-2024-q4",
"cost_threshold":"high"
}
}
)

messages =[
    SystemMessage(content="You are a marketing copywriter."),
    HumanMessage(content="Create compelling ad copy for our new product launch.")
]

response = cost_tracking_chat.invoke(messages)
```

#### Tags for A/B Testing[​](#tags-for-ab-testing "Direct link to Tags for A/B Testing")

```
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import random

defcreate_ab_test_chat(test_variant:str=None):
"""Create chat instance for A/B testing with appropriate tags"""

if test_variant isNone:
        test_variant = random.choice(["variant-a","variant-b"])

return ChatOpenAI(
        openai_api_base="http://localhost:4000",
        model="gpt-4o",
        temperature=0.7if test_variant =="variant-a"else0.9,# Different temp for variants
        extra_body={
"metadata":{
"tags":[
"ab-test-experiment-1",
f"variant-{test_variant}",
"temperature-test",
"user-experience"
],
"experiment_id":"ab-test-001",
"variant": test_variant,
"test_group":"temperature-optimization"
}
}
)

# Run A/B test
variant_a_chat = create_ab_test_chat("variant-a")
variant_b_chat = create_ab_test_chat("variant-b")

test_message =[HumanMessage(content="Explain quantum computing in simple terms")]

response_a = variant_a_chat.invoke(test_message)
response_b = variant_b_chat.invoke(test_message)
```

### Tag Best Practices[​](#tag-best-practices "Direct link to Tag Best Practices")

#### 1. **Consistent Naming Convention**[​](#1-consistent-naming-convention "Direct link to 1-consistent-naming-convention")

```
# ✅ Good: Consistent, descriptive tags
tags =["production","api-v2","customer-support","urgent"]

# ❌ Avoid: Inconsistent or unclear tags
tags =["prod","v2","support","urgent123"]
```

#### 2. **Hierarchical Tags**[​](#2-hierarchical-tags "Direct link to 2-hierarchical-tags")

```
# ✅ Good: Hierarchical structure
tags =["env:production","team:backend","service:api","priority:high"]

# This allows for easy filtering and grouping
```

#### 3. **Include Context Information**[​](#3-include-context-information "Direct link to 3-include-context-information")

```
extra_body={
"metadata":{
"tags":["production","user-onboarding"],
"user_id":"user-12345",
"session_id":"session-abc123",
"feature_flag":"new-onboarding-flow",
"environment":"production"
}
}
```

#### 4. **Tag Categories**[​](#4-tag-categories "Direct link to 4-tag-categories")

Consider organizing tags into categories:

- **Environment**: `production`, `staging`, `development`
- **Team/Service**: `backend`, `frontend`, `api`, `worker`
- **Feature**: `authentication`, `payment`, `notification`
- **Priority**: `critical`, `high`, `medium`, `low`
- **User Type**: `premium`, `enterprise`, `free`

### Using Tags with LiteLLM Proxy[​](#using-tags-with-litellm-proxy "Direct link to Using Tags with LiteLLM Proxy")

When using tags with LiteLLM Proxy, you can:

1. **Filter requests** based on tags
2. **Track costs** by tags in spend reports
3. **Apply routing rules** based on tags
4. **Monitor usage** with tag-based analytics

#### Example Proxy Configuration with Tags[​](#example-proxy-configuration-with-tags "Direct link to Example Proxy Configuration with Tags")

```
# config.yaml
model_list:
-model_name: gpt-4o
litellm_params:
model: gpt-4o
api_key: your-key

# Tag-based routing rules
tag_routing:
-tags:["premium","high-priority"]
models:["gpt-4o","claude-3-opus"]
-tags:["standard"]
models:["gpt-3.5-turbo","claude-3-haiku"]
```

### Monitoring and Analytics[​](#monitoring-and-analytics "Direct link to Monitoring and Analytics")

Tags enable powerful analytics capabilities:

```
# Example: Get spend reports by tags
import requests

response = requests.get(
"http://localhost:4000/global/spend/report",
    headers={"Authorization":"Bearer sk-your-key"},
    params={
"start_date":"2024-01-01",
"end_date":"2024-12-31",
"group_by":"tags"
}
)

spend_by_tags = response.json()
```

This documentation covers the essential patterns for using tags effectively with LangChain and LiteLLM, enabling better organization, tracking, and analytics of your LLM requests.