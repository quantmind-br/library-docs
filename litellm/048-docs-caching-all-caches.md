---
title: Caching - In-Memory, Redis, s3, gcs, Redis Semantic Cache, Disk | liteLLM
url: https://docs.litellm.ai/docs/caching/all_caches
source: sitemap
fetched_at: 2026-01-21T19:44:13.143725819-03:00
rendered_js: false
word_count: 350
summary: This document provides a comprehensive guide on implementing caching in LiteLLM using various backends like Redis, S3, and GCS. It explains how to initialize, configure, and customize cache behavior through environment variables, per-call controls, and custom logic.
tags:
    - litellm
    - caching
    - redis-cache
    - semantic-cache
    - performance-optimization
    - python-sdk
    - cloud-storage
category: guide
---

[**See Code**](https://github.com/BerriAI/litellm/blob/main/litellm/caching/caching.py)

info

- For Proxy Server? Doc here: [Caching Proxy Server](https://docs.litellm.ai/docs/proxy/caching)
- For OpenAI/Anthropic Prompt Caching, go [here](https://docs.litellm.ai/docs/completion/prompt_caching)

## Initialize Cache - In Memory, Redis, s3 Bucket, gcs Bucket, Redis Semantic, Disk Cache, Qdrant Semantic[​](#initialize-cache---in-memory-redis-s3-bucket-gcs-bucket-redis-semantic-disk-cache-qdrant-semantic "Direct link to Initialize Cache - In Memory, Redis, s3 Bucket, gcs Bucket, Redis Semantic, Disk Cache, Qdrant Semantic")

- redis-cache
- gcs-cache
- s3-cache
- azure-blob-cache
- redis-semantic cache
- qdrant-semantic cache
- in memory cache
- disk cache

Install redis

For the hosted version you can setup your own Redis DB here: [https://redis.io/try-free/](https://redis.io/try-free/)

**Basic Redis Cache**

```
import litellm
from litellm import completion
from litellm.caching.caching import Cache

litellm.cache = Cache(type="redis", host=<host>, port=<port>, password=<password>)

# Make completion calls
response1 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}]
)
response2 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}]
)

# response1 == response2, response 1 is cached
```

**GCP IAM Redis Authentication**

For GCP Memorystore Redis with IAM authentication:

```
pip install google-cloud-iam
```

```
import litellm
from litellm import completion
# For Redis Cluster with GCP IAM
from litellm.caching.redis_cluster_cache import RedisClusterCache

litellm.cache = RedisClusterCache(
    startup_nodes=[
{"host":"10.128.0.2","port":6379},
{"host":"10.128.0.2","port":11008},
],
    gcp_service_account="projects/-/serviceAccounts/your-sa@project.iam.gserviceaccount.com",
    ssl=True,
    ssl_cert_reqs=None,
    ssl_check_hostname=False,
)

# Make completion calls
response1 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}]
)
response2 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}]
)

# response1 == response2, response 1 is cached
```

**Environment Variables for GCP IAM Redis**

You can also set these as environment variables:

```
export REDIS_HOST="10.128.0.2"
export REDIS_PORT="6379"
export REDIS_GCP_SERVICE_ACCOUNT="projects/-/serviceAccounts/your-sa@project.iam.gserviceaccount.com"
export REDIS_SSL="False"
```

Then simply initialize:

```
litellm.cache = Cache(type="redis")
```

info

Use `REDIS_*` environment variables as the primary mechanism for configuring all Redis client library parameters. This approach automatically maps environment variables to Redis client kwargs and is the suggested way to toggle Redis settings.

warning

If you need to pass non-string Redis parameters (integers, booleans, complex objects), avoid `REDIS_*` environment variables as they may fail during Redis client initialization. Instead, pass them directly as kwargs to the `Cache()` constructor.

## Switch Cache On / Off Per LiteLLM Call[​](#switch-cache-on--off-per-litellm-call "Direct link to Switch Cache On / Off Per LiteLLM Call")

LiteLLM supports 4 cache-controls:

- `no-cache`: *Optional(bool)* When `True`, Will not return a cached response, but instead call the actual endpoint.
- `no-store`: *Optional(bool)* When `True`, Will not cache the response.
- `ttl`: *Optional(int)* - Will cache the response for the user-defined amount of time (in seconds).
- `s-maxage`: *Optional(int)* Will only accept cached responses that are within user-defined range (in seconds).

[Let us know if you need more](https://github.com/BerriAI/litellm/issues/1218)

- No-Cache
- No-Store
- ttl
- s-maxage

Example usage `no-cache` - When `True`, Will not return a cached response

```
response = litellm.completion(
        model="gpt-3.5-turbo",
        messages=[
{
"role":"user",
"content":"hello who are you"
}
],
        cache={"no-cache":True},
)
```

## Cache Context Manager - Enable, Disable, Update Cache[​](#cache-context-manager---enable-disable-update-cache "Direct link to Cache Context Manager - Enable, Disable, Update Cache")

Use the context manager for easily enabling, disabling & updating the litellm cache

### Enabling Cache[​](#enabling-cache "Direct link to Enabling Cache")

Quick Start Enable

Advanced Params

```
litellm.enable_cache(
type: Optional[Literal["local","redis","s3","gcs","disk"]]="local",
    host: Optional[str]=None,
    port: Optional[str]=None,
    password: Optional[str]=None,
    supported_call_types: Optional[
        List[Literal["completion","acompletion","embedding","aembedding","atranscription","transcription"]]
]=["completion","acompletion","embedding","aembedding","atranscription","transcription"],
**kwargs,
)
```

### Disabling Cache[​](#disabling-cache "Direct link to Disabling Cache")

Switch caching off

### Updating Cache Params (Redis Host, Port etc)[​](#updating-cache-params-redis-host-port-etc "Direct link to Updating Cache Params (Redis Host, Port etc)")

Update the Cache params

```
litellm.update_cache(
type: Optional[Literal["local","redis","s3","gcs","disk"]]="local",
    host: Optional[str]=None,
    port: Optional[str]=None,
    password: Optional[str]=None,
    supported_call_types: Optional[
        List[Literal["completion","acompletion","embedding","aembedding","atranscription","transcription"]]
]=["completion","acompletion","embedding","aembedding","atranscription","transcription"],
**kwargs,
)
```

## Custom Cache Keys:[​](#custom-cache-keys "Direct link to Custom Cache Keys:")

Define function to return cache key

```
# this function takes in *args, **kwargs and returns the key you want to use for caching
defcustom_get_cache_key(*args,**kwargs):
# return key to use for your cache:
    key = kwargs.get("model","")+str(kwargs.get("messages",""))+str(kwargs.get("temperature",""))+str(kwargs.get("logit_bias",""))
print("key for cache", key)
return key

```

Set your function as litellm.cache.get\_cache\_key

```
from litellm.caching.caching import Cache

cache = Cache(type="redis", host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], password=os.environ['REDIS_PASSWORD'])

cache.get_cache_key = custom_get_cache_key # set get_cache_key function for your cache

litellm.cache = cache # set litellm.cache to your cache 

```

## How to write custom add/get cache functions[​](#how-to-write-custom-addget-cache-functions "Direct link to How to write custom add/get cache functions")

### 1. Init Cache[​](#1-init-cache "Direct link to 1. Init Cache")

```
from litellm.caching.caching import Cache
cache = Cache()
```

### 2. Define custom add/get cache functions[​](#2-define-custom-addget-cache-functions "Direct link to 2. Define custom add/get cache functions")

```
defadd_cache(self, result,*args,**kwargs):
  your logic

defget_cache(self,*args,**kwargs):
  your logic
```

### 3. Point cache add/get functions to your add/get functions[​](#3-point-cache-addget-functions-to-your-addget-functions "Direct link to 3. Point cache add/get functions to your add/get functions")

```
cache.add_cache = add_cache
cache.get_cache = get_cache
```

## Cache Initialization Parameters[​](#cache-initialization-parameters "Direct link to Cache Initialization Parameters")

```
def__init__(
    self,
type: Optional[Literal["local","redis","redis-semantic","s3","gcs","disk"]]="local",
    supported_call_types: Optional[
        List[Literal["completion","acompletion","embedding","aembedding","atranscription","transcription"]]
]=["completion","acompletion","embedding","aembedding","atranscription","transcription"],
    ttl: Optional[float]=None,
    default_in_memory_ttl: Optional[float]=None,

# redis cache params
    host: Optional[str]=None,
    port: Optional[str]=None,
    password: Optional[str]=None,
    namespace: Optional[str]=None,
    default_in_redis_ttl: Optional[float]=None,
    redis_flush_size=None,

# GCP IAM Redis authentication params
    gcp_service_account: Optional[str]=None,
    gcp_ssl_ca_certs: Optional[str]=None,
    ssl: Optional[bool]=None,
    ssl_cert_reqs: Optional[Union[str,None]]=None,
    ssl_check_hostname: Optional[bool]=None,

# redis semantic cache params
    similarity_threshold: Optional[float]=None,
    redis_semantic_cache_embedding_model:str="text-embedding-ada-002",
    redis_semantic_cache_index_name: Optional[str]=None,

# s3 Bucket, boto3 configuration
    s3_bucket_name: Optional[str]=None,
    s3_region_name: Optional[str]=None,
    s3_api_version: Optional[str]=None,
    s3_path: Optional[str]=None,# if you wish to save to a specific path
    s3_use_ssl: Optional[bool]=True,
    s3_verify: Optional[Union[bool,str]]=None,
    s3_endpoint_url: Optional[str]=None,
    s3_aws_access_key_id: Optional[str]=None,
    s3_aws_secret_access_key: Optional[str]=None,
    s3_aws_session_token: Optional[str]=None,
    s3_config: Optional[Any]=None,

# disk cache params
    disk_cache_dir=None,

# qdrant cache params
    qdrant_api_base: Optional[str]=None,
    qdrant_api_key: Optional[str]=None,
    qdrant_collection_name: Optional[str]=None,
    qdrant_quantization_config: Optional[str]=None,
    qdrant_semantic_cache_embedding_model="text-embedding-ada-002",

**kwargs
):
```

## Logging[​](#logging "Direct link to Logging")

Cache hits are logged in success events as `kwarg["cache_hit"]`.

Here's an example of accessing it:

```
import litellm
from litellm.integrations.custom_logger import CustomLogger
from litellm import completion, acompletion, Cache

# create custom callback for success_events
classMyCustomHandler(CustomLogger):
asyncdefasync_log_success_event(self, kwargs, response_obj, start_time, end_time):
print(f"On Success")
print(f"Value of Cache hit: {kwargs['cache_hit']"})

asyncdeftest_async_completion_azure_caching():
# set custom callback
  customHandler_caching = MyCustomHandler()
  litellm.callbacks =[customHandler_caching]

# init cache 
  litellm.cache = Cache(type="redis", host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], password=os.environ['REDIS_PASSWORD'])
  unique_time = time.time()
  response1 =await litellm.acompletion(model="azure/chatgpt-v-2",
                          messages=[{
"role":"user",
"content":f"Hi 👋 - i'm async azure {unique_time}"
}],
                          caching=True)
await asyncio.sleep(1)
print(f"customHandler_caching.states pre-cache hit: {customHandler_caching.states}")
  response2 =await litellm.acompletion(model="azure/chatgpt-v-2",
                          messages=[{
"role":"user",
"content":f"Hi 👋 - i'm async azure {unique_time}"
}],
                          caching=True)
await asyncio.sleep(1)# success callbacks are done in parallel
```