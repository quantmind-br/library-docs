---
title: Overview | liteLLM
url: https://docs.litellm.ai/docs/search/
source: sitemap
fetched_at: 2026-01-21T19:54:24.98674559-03:00
rendered_js: false
word_count: 250
summary: This document explains how to use LiteLLM to perform search operations using its Python SDK and AI Gateway across multiple providers like Perplexity, Tavily, and Exa. It details configuration, request parameters, response formats, and implementation of search load balancing.
tags:
    - litellm
    - search-api
    - python-sdk
    - api-gateway
    - perplexity-ai
    - load-balancing
    - web-search
category: guide
---

FeatureSupportedSupported Providers`perplexity`, `tavily`, `parallel_ai`, `exa_ai`, `google_pse`, `dataforseo`, `firecrawl`, `searxng`, `linkup`Cost Tracking✅Logging✅Load Balancing❌

info

Supported from LiteLLM v1.78.7+

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start[​](#quick-start "Direct link to Quick Start")

Basic Search

```
from litellm import search
import os

os.environ["PERPLEXITYAI_API_KEY"]="pplx-..."

response = search(
    query="latest AI developments in 2024",
    search_provider="perplexity",
    max_results=5
)

# Access search results
for result in response.results:
print(f"{result.title}: {result.url}")
print(f"Snippet: {result.snippet}\n")
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

Async Search

```
from litellm import asearch
import os, asyncio

os.environ["PERPLEXITYAI_API_KEY"]="pplx-..."

asyncdefsearch_async():
    response =await asearch(
        query="machine learning research papers",
        search_provider="perplexity",
        max_results=10,
        search_domain_filter=["arxiv.org","nature.com"]
)

# Access search results
for result in response.results:
print(f"{result.title}: {result.url}")
print(f"Snippet: {result.snippet}")

asyncio.run(search_async())
```

### Optional Parameters[​](#optional-parameters "Direct link to Optional Parameters")

Search with Options

```
response = search(
    query="AI developments",
    search_provider="perplexity",
# Unified parameters (work across all providers)
    max_results=10,# Maximum number of results (1-20)
    search_domain_filter=["arxiv.org"],# Filter to specific domains
    country="US",# Country code filter
    max_tokens_per_page=1024# Max tokens per page
)
```

## **LiteLLM AI Gateway Usage**[​](#litellm-ai-gateway-usage "Direct link to litellm-ai-gateway-usage")

LiteLLM provides a Perplexity API compatible `/search` endpoint for search calls.

**Setup**

Add this to your litellm proxy config.yaml

config.yaml

```
model_list:
-model_name: gpt-4
litellm_params:
model: gpt-4
api_key: os.environ/OPENAI_API_KEY

search_tools:
-search_tool_name: perplexity-search
litellm_params:
search_provider: perplexity
api_key: os.environ/PERPLEXITYAI_API_KEY

-search_tool_name: tavily-search
litellm_params:
search_provider: tavily
api_key: os.environ/TAVILY_API_KEY
```

Start litellm

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### Test Request[​](#test-request "Direct link to Test Request")

**Option 1: Search tool name in URL (Recommended - keeps body Perplexity-compatible)**

cURL Request

```
curl http://0.0.0.0:4000/v1/search/perplexity-search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI developments 2024",
    "max_results": 5,
    "search_domain_filter": ["arxiv.org", "nature.com"],
    "country": "US"
  }'
```

**Option 2: Search tool name in body**

cURL Request with search\_tool\_name in body

```
curl http://0.0.0.0:4000/v1/search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "search_tool_name": "perplexity-search",
    "query": "latest AI developments 2024",
    "max_results": 5
  }'
```

### Load Balancing[​](#load-balancing "Direct link to Load Balancing")

Configure multiple search providers for automatic load balancing and fallbacks:

config.yaml with load balancing

```
search_tools:
-search_tool_name: my-search
litellm_params:
search_provider: perplexity
api_key: os.environ/PERPLEXITYAI_API_KEY

-search_tool_name: my-search
litellm_params:
search_provider: tavily
api_key: os.environ/TAVILY_API_KEY

-search_tool_name: my-search
litellm_params:
search_provider: exa_ai
api_key: os.environ/EXA_API_KEY

router_settings:
routing_strategy: simple-shuffle  # or 'least-busy', 'latency-based-routing'
```

Test with load balancing:

```
curl http://0.0.0.0:4000/v1/search/my-search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "AI developments",
    "max_results": 10
  }'
```

## **Request/Response Format**[​](#requestresponse-format "Direct link to requestresponse-format")

### Example Request[​](#example-request "Direct link to Example Request")

Search Request

```
{
"query":"latest AI developments 2024",
"max_results":10,
"search_domain_filter":["arxiv.org","nature.com"],
"country":"US",
"max_tokens_per_page":1024
}
```

### Request Parameters[​](#request-parameters "Direct link to Request Parameters")

ParameterTypeRequiredDescription`query`string or arrayYesSearch query. Can be a single string or array of strings`search_provider`stringYes (SDK)The search provider to use: `"perplexity"`, `"tavily"`, `"parallel_ai"`, `"exa_ai"`, `"google_pse"`, `"dataforseo"`, `"firecrawl"`, `"searxng"`, or `"linkup"``search_tool_name`stringYes (Proxy)Name of the search tool configured in `config.yaml``max_results`integerNoMaximum number of results to return (1-20). Default: 10`search_domain_filter`arrayNoList of domains to filter results (max 20 domains)`max_tokens_per_page`integerNoMaximum tokens per page to process. Default: 1024`country`stringNoCountry code filter (e.g., `"US"`, `"GB"`, `"DE"`)

**Query Format Examples:**

```
# Single query
query ="AI developments"

# Multiple queries
query =["AI developments","machine learning trends"]
```

### Response Format[​](#response-format "Direct link to Response Format")

The response follows Perplexity's search format with the following structure:

Search Response

```
{
"object":"search",
"results":[
{
"title":"Latest Advances in Artificial Intelligence",
"url":"https://arxiv.org/paper/example",
"snippet":"This paper discusses recent developments in AI...",
"date":"2024-01-15"
},
{
"title":"Machine Learning Breakthroughs",
"url":"https://nature.com/articles/ml-breakthrough",
"snippet":"Researchers have achieved new milestones...",
"date":"2024-01-10"
}
]
}
```

#### Response Fields[​](#response-fields "Direct link to Response Fields")

FieldTypeDescription`object`stringAlways `"search"` for search responses`results`arrayList of search results`results[].title`stringTitle of the search result`results[].url`stringURL of the search result`results[].snippet`stringText snippet from the result`results[].date`stringOptional publication or last updated date

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

ProviderEnvironment Variable`search_provider` ValuePerplexity AI`PERPLEXITYAI_API_KEY``perplexity`Tavily`TAVILY_API_KEY``tavily`Exa AI`EXA_API_KEY``exa_ai`Parallel AI`PARALLEL_AI_API_KEY``parallel_ai`Google PSE`GOOGLE_PSE_API_KEY`, `GOOGLE_PSE_ENGINE_ID``google_pse`DataForSEO`DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD``dataforseo`Firecrawl`FIRECRAWL_API_KEY``firecrawl`SearXNG`SEARXNG_API_BASE` (required)`searxng`Linkup`LINKUP_API_KEY``linkup`

See the individual provider documentation for detailed setup instructions and provider-specific parameters.