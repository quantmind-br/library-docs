---
title: Batch
url: https://docs.mistral.ai/api/endpoint/batch
source: crawler
fetched_at: 2026-01-29T07:33:19.002278334-03:00
rendered_js: false
word_count: 255
---

![Fireflies](https://docs.mistral.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ffireflies.7a626bd6.gif&w=2048&q=100&dpl=dpl_pYiSt9fwKq5aTueGqtK85uu9quQV)

### Examples

Real world code examples

## **GET** /v1/batch/jobs

Get a list of batch jobs for your organization and user.

OK

##### object

"list"

*Default Value:* `"list"`

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.list({});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.list({});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.list(page=0, page_size=100, created_by_me=False)# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.list(page=0, page_size=100, created_by_me=False)# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/batch/jobs \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
curl https://api.mistral.ai/v1/batch/jobs \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

## **POST** /v1/batch/jobs

Create a new batch job, it will be queued for processing.

In case you want to use a specific agent from the **deprecated** agents api for batch inference, you can specify the agent ID here.

##### endpoint

\*"/v1/chat/completions"|"/v1/embeddings"|"/v1/fim/completions"|"/v1/moderations"|"/v1/chat/moderations"|"/v1/ocr"|"/v1/classifications"|"/v1/chat/classifications"|"/v1/conversations"|"/v1/audio/transcriptions"

##### input\_files

\*array&lt;string&gt;

The list of input files to be used for batch inference, these files should be `jsonl` files, containing the input data corresponding to the bory request for the batch inference in a "body" field. An example of such file is the following: `json \{"custom_id": "0", "body": \{"max_tokens": 100, "messages": [\{"role": "user", "content": "What is the best French cheese?"\}]\}\} \{"custom_id": "1", "body": \{"max_tokens": 100, "messages": [\{"role": "user", "content": "What is the best French wine?"\}]\}\}`

The metadata of your choice to be associated with the batch inference job.

The model to be used for batch inference.

##### timeout\_hours

integer

*Default Value:* `24`

The timeout in hours for the batch inference job.

OK

##### completed\_requests

\*integer

##### input\_files

\*array&lt;string&gt;

##### object

"batch"

*Default Value:* `"batch"`

##### status

\*"QUEUED"|"RUNNING"|"SUCCESS"|"FAILED"|"TIMEOUT\_EXCEEDED"|"CANCELLATION\_REQUESTED"|"CANCELLED"

##### succeeded\_requests

\*integer

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.create({    inputFiles:["fe3343a2-3b8d-404b-ba32-a78dede2614a",],    endpoint:"/v1/classifications",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.create({    inputFiles:["fe3343a2-3b8d-404b-ba32-a78dede2614a",],    endpoint:"/v1/classifications",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.create(input_files=["fe3343a2-3b8d-404b-ba32-a78dede2614a",], endpoint="/v1/moderations", timeout_hours=24)# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.create(input_files=["fe3343a2-3b8d-404b-ba32-a78dede2614a",], endpoint="/v1/moderations", timeout_hours=24)# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/batch/jobs \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json' \
 -d '{
  "endpoint": "/v1/chat/completions",
  "input_files": [
    "ipsum eiusmod"
  ]
}'
```

```
curl https://api.mistral.ai/v1/batch/jobs \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json' \
 -d '{
  "endpoint": "/v1/chat/completions",
  "input_files": [
    "ipsum eiusmod"
  ]
}'
```

```
{"completed_requests":87,"created_at":14,"endpoint":"ipsum eiusmod","errors":[{"message":"consequat do"}],"failed_requests":56,"id":"reprehenderit ut dolore","input_files":["occaecat dolor sit"],"status":"QUEUED","succeeded_requests":91,"total_requests":32}
```

```
{"completed_requests":87,"created_at":14,"endpoint":"ipsum eiusmod","errors":[{"message":"consequat do"}],"failed_requests":56,"id":"reprehenderit ut dolore","input_files":["occaecat dolor sit"],"status":"QUEUED","succeeded_requests":91,"total_requests":32}
```

## **GET** /v1/batch/jobs/{job\_id}

Get a batch job details by its UUID.

OK

##### completed\_requests

\*integer

##### input\_files

\*array&lt;string&gt;

##### object

"batch"

*Default Value:* `"batch"`

##### status

\*"QUEUED"|"RUNNING"|"SUCCESS"|"FAILED"|"TIMEOUT\_EXCEEDED"|"CANCELLATION\_REQUESTED"|"CANCELLED"

##### succeeded\_requests

\*integer

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.get({    jobId:"4017dc9f-b629-42f4-9700-8c681b9e7f0f",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.get({    jobId:"4017dc9f-b629-42f4-9700-8c681b9e7f0f",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.get(job_id="4017dc9f-b629-42f4-9700-8c681b9e7f0f")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.get(job_id="4017dc9f-b629-42f4-9700-8c681b9e7f0f")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/batch/jobs/{job_id} \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
curl https://api.mistral.ai/v1/batch/jobs/{job_id} \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
{"completed_requests":87,"created_at":14,"endpoint":"ipsum eiusmod","errors":[{"message":"consequat do"}],"failed_requests":56,"id":"reprehenderit ut dolore","input_files":["occaecat dolor sit"],"status":"QUEUED","succeeded_requests":91,"total_requests":32}
```

```
{"completed_requests":87,"created_at":14,"endpoint":"ipsum eiusmod","errors":[{"message":"consequat do"}],"failed_requests":56,"id":"reprehenderit ut dolore","input_files":["occaecat dolor sit"],"status":"QUEUED","succeeded_requests":91,"total_requests":32}
```

## **POST** /v1/batch/jobs/{job\_id}/cancel

Request the cancellation of a batch job.

OK

##### completed\_requests

\*integer

##### input\_files

\*array&lt;string&gt;

##### object

"batch"

*Default Value:* `"batch"`

##### status

\*"QUEUED"|"RUNNING"|"SUCCESS"|"FAILED"|"TIMEOUT\_EXCEEDED"|"CANCELLATION\_REQUESTED"|"CANCELLED"

##### succeeded\_requests

\*integer

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.cancel({    jobId:"4fb29d1c-535b-4f0a-a1cb-2167f86da569",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.batch.jobs.cancel({    jobId:"4fb29d1c-535b-4f0a-a1cb-2167f86da569",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.cancel(job_id="4fb29d1c-535b-4f0a-a1cb-2167f86da569")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.batch.jobs.cancel(job_id="4fb29d1c-535b-4f0a-a1cb-2167f86da569")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/batch/jobs/{job_id}/cancel \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
curl https://api.mistral.ai/v1/batch/jobs/{job_id}/cancel \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
{"completed_requests":87,"created_at":14,"endpoint":"ipsum eiusmod","errors":[{"message":"consequat do"}],"failed_requests":56,"id":"reprehenderit ut dolore","input_files":["occaecat dolor sit"],"status":"QUEUED","succeeded_requests":91,"total_requests":32}
```

```
{"completed_requests":87,"created_at":14,"endpoint":"ipsum eiusmod","errors":[{"message":"consequat do"}],"failed_requests":56,"id":"reprehenderit ut dolore","input_files":["occaecat dolor sit"],"status":"QUEUED","succeeded_requests":91,"total_requests":32}
```