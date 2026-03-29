---
title: Models
url: https://docs.mistral.ai/api/endpoint/models
source: crawler
fetched_at: 2026-01-29T07:33:18.871003241-03:00
rendered_js: false
word_count: 182
summary: This document provides a comprehensive reference for Mistral AI's Model Management API endpoints, including functionality for listing, retrieving, updating, and deleting models. It details request methods, parameters, and response structures with code examples in Python, JavaScript, and cURL.
tags:
    - mistral-ai
    - api-reference
    - model-management
    - fine-tuning
    - rest-api
    - python-sdk
    - javascript-sdk
category: api
---

![Fireflies](https://docs.mistral.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ffireflies.7a626bd6.gif&w=2048&q=100&dpl=dpl_pYiSt9fwKq5aTueGqtK85uu9quQV)

## Models Endpoints

Model Management API

### Examples

Real world code examples

## **GET** /v1/models

List all models available to the user.

Successful Response

##### data

array&lt;[BaseModelCard](#operation-list_models_v1_models_get_responses_200_application-json_data_basemodelcard)|[FTModelCard](#operation-list_models_v1_models_get_responses_200_application-json_data_ftmodelcard)&gt;

##### object

string

*Default Value:* `"list"`

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.list();console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.list();console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.list()# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.list()# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/models \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
curl https://api.mistral.ai/v1/models \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
[{"id":"<model_id>","capabilities":{"completion_chat":true,"completion_fim":false,"function_calling":false,"fine_tuning":false,"vision":false,"classification":false},"job":"<job_id>","root":"open-mistral-7b","object":"model","created":1756746619,"owned_by":"<owner_id>","name":null,"description":null,"max_context_length":32768,"aliases":[],"deprecation":null,"deprecation_replacement_model":null,"default_model_temperature":null,"TYPE":"fine-tuned","archived":false}]
```

```
[{"id":"<model_id>","capabilities":{"completion_chat":true,"completion_fim":false,"function_calling":false,"fine_tuning":false,"vision":false,"classification":false},"job":"<job_id>","root":"open-mistral-7b","object":"model","created":1756746619,"owned_by":"<owner_id>","name":null,"description":null,"max_context_length":32768,"aliases":[],"deprecation":null,"deprecation_replacement_model":null,"default_model_temperature":null,"TYPE":"fine-tuned","archived":false}]
```

## **GET** /v1/models/{model\_id}

Retrieve information about a model.

The ID of the model to retrieve.

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.retrieve({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.retrieve({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.retrieve(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.retrieve(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/models/{model_id} \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
curl https://api.mistral.ai/v1/models/{model_id} \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
{"id":"<your_model_id>","capabilities":{"completion_chat":true,"completion_fim":false,"function_calling":false,"fine_tuning":false,"vision":false,"classification":false},"job":"<job_id>","root":"open-mistral-7b","object":"model","created":1756746619,"owned_by":"<owner_id>","name":null,"description":null,"max_context_length":32768,"aliases":[],"deprecation":null,"deprecation_replacement_model":null,"default_model_temperature":null,"TYPE":"fine-tuned","archived":false}
```

```
{"id":"<your_model_id>","capabilities":{"completion_chat":true,"completion_fim":false,"function_calling":false,"fine_tuning":false,"vision":false,"classification":false},"job":"<job_id>","root":"open-mistral-7b","object":"model","created":1756746619,"owned_by":"<owner_id>","name":null,"description":null,"max_context_length":32768,"aliases":[],"deprecation":null,"deprecation_replacement_model":null,"default_model_temperature":null,"TYPE":"fine-tuned","archived":false}
```

## **DELETE** /v1/models/{model\_id}

Delete a fine-tuned model.

The ID of the model to delete.

Successful Response

##### deleted

boolean

*Default Value:* `true`

The ID of the deleted model.

##### object

string

*Default Value:* `"model"`

The object type that was deleted

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.delete({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.delete({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.delete(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.delete(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/models/{model_id} \
 -X DELETE \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
curl https://api.mistral.ai/v1/models/{model_id} \
 -X DELETE \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
{"id":"ft:open-mistral-7b:587a6b29:20240514:7e773925","object":"model","deleted":true}
```

```
{"id":"ft:open-mistral-7b:587a6b29:20240514:7e773925","object":"model","deleted":true}
```

## **PATCH** /v1/fine\_tuning/models/{model\_id}

Update a model name or description.

The ID of the model to update.

OK

#### CompletionFTModelOut

{object}

#### ClassifierFTModelOut

{object}

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.update({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",    updateFTModelIn:{},});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.update({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",    updateFTModelIn:{},});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.update(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.update(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/models/{model_id} \
 -X PATCH \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json' \
 -d '{}'
```

```
curl https://api.mistral.ai/v1/fine_tuning/models/{model_id} \
 -X PATCH \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json' \
 -d '{}'
```

```
{"archived":false,"capabilities":{},"created":87,"id":"ipsum eiusmod","job":"consequat do","owned_by":"reprehenderit ut dolore","root":"occaecat dolor sit","root_version":"nostrud","workspace_id":"aute aliqua aute commodo"}
```

```
{"archived":false,"capabilities":{},"created":87,"id":"ipsum eiusmod","job":"consequat do","owned_by":"reprehenderit ut dolore","root":"occaecat dolor sit","root_version":"nostrud","workspace_id":"aute aliqua aute commodo"}
```

## **POST** /v1/fine\_tuning/models/{model\_id}/archive

Archive a fine-tuned model.

The ID of the model to archive.

OK

##### archived

boolean

*Default Value:* `true`

##### object

"model"

*Default Value:* `"model"`

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.archive({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.archive({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.archive(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.archive(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/models/{model_id}/archive \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
curl https://api.mistral.ai/v1/fine_tuning/models/{model_id}/archive \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
{"id":"ipsum eiusmod"}
```

```
{"id":"ipsum eiusmod"}
```

*Unarchive Fine Tuned Model*

## **DELETE** /v1/fine\_tuning/models/{model\_id}/archive

Un-archive a fine-tuned model.

The ID of the model to unarchive.

OK

##### archived

boolean

*Default Value:* `false`

##### object

"model"

*Default Value:* `"model"`

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.unarchive({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.models.unarchive({    modelId:"ft:open-mistral-7b:587a6b29:20240514:7e773925",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.unarchive(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.models.unarchive(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/models/{model_id}/archive \
 -X DELETE \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
curl https://api.mistral.ai/v1/fine_tuning/models/{model_id}/archive \
 -X DELETE \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
{"id":"ipsum eiusmod"}
```

```
{"id":"ipsum eiusmod"}
```