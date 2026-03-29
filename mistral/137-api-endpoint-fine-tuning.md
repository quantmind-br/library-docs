---
title: Fine Tuning
url: https://docs.mistral.ai/api/endpoint/fine-tuning
source: crawler
fetched_at: 2026-01-29T07:33:18.170392277-03:00
rendered_js: false
word_count: 309
---

![Fireflies](https://docs.mistral.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ffireflies.7a626bd6.gif&w=2048&q=100&dpl=dpl_pYiSt9fwKq5aTueGqtK85uu9quQV)

## Fine Tuning Endpoints

Fine-tuning API

### Examples

Real world code examples

## **GET** /v1/fine\_tuning/jobs

Get a list of fine-tuning jobs for your organization and user.

OK

##### object

"list"

*Default Value:* `"list"`

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.list({});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.list({});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.list(page=0, page_size=100, created_by_me=False)# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.list(page=0, page_size=100, created_by_me=False)# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

## **POST** /v1/fine\_tuning/jobs

Create a new fine-tuning job, it will be queued for processing.

- If `true` the job is not spawned, instead the query returns a handful of useful metadata for the user to perform sanity checks (see `LegacyJobMetadataOut` response).
- Otherwise, the job is started and the query returns the job ID along with some of the input parameters (see `JobOut` response).

This field will be required in a future release.

##### classifier\_targets

[array](#operation-jobs_api_routes_fine_tuning_create_fine_tuning_job_request_classifier_targets_classifiertargetin)&lt;[ClassifierTargetIn](#operation-jobs_api_routes_fine_tuning_create_fine_tuning_job_request_classifier_targets_classifiertargetin)&gt;|null

##### integrations

array&lt;[WandbIntegration](#operation-jobs_api_routes_fine_tuning_create_fine_tuning_job_request_integrations_wandbintegration)&gt;|null

A list of integrations to enable for your fine-tuning job.

##### invalid\_sample\_skip\_percentage

number

*Default Value:* `0`

##### job\_type

"completion"|"classifier"

##### model

\*"ministral-3b-latest"|"ministral-8b-latest"|"open-mistral-7b"|"open-mistral-nemo"|"mistral-small-latest"|"mistral-medium-latest"|"mistral-large-latest"|"pixtral-12b-latest"|"codestral-latest"

The name of the model to fine-tune.

##### repositories

array&lt;[GithubRepositoryIn](#operation-jobs_api_routes_fine_tuning_create_fine_tuning_job_request_repositories_githubrepositoryin)&gt;|null

A string that will be added to your fine-tuning model name. For example, a suffix of "my-great-model" would produce a model name like `ft:open-mistral-7b:my-great-model:xxx...`

##### training\_files

[array](#operation-jobs_api_routes_fine_tuning_create_fine_tuning_job_request_training_files_trainingfile)&lt;[TrainingFile](#operation-jobs_api_routes_fine_tuning_create_fine_tuning_job_request_training_files_trainingfile)&gt;

##### validation\_files

array&lt;string&gt;|null

A list containing the IDs of uploaded files that contain validation data. If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job. The same data should not be present in both train and validation files.

OK

#### CompletionJobOut

{object}

#### ClassifierJobOut

{object}

#### LegacyJobMetadataOut

{object}

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.create({    model:"Camaro",    hyperparameters:{      learningRate:0.0001,},});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.create({    model:"Camaro",    hyperparameters:{      learningRate:0.0001,},});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.create(model="Camaro", hyperparameters={"learning_rate":0.0001,}, invalid_sample_skip_percentage=0)# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.create(model="Camaro", hyperparameters={"learning_rate":0.0001,}, invalid_sample_skip_percentage=0)# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json' \
 -d '{
  "hyperparameters": {},
  "model": "ministral-3b-latest"
}'
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json' \
 -d '{
  "hyperparameters": {},
  "model": "ministral-3b-latest"
}'
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```

## **GET** /v1/fine\_tuning/jobs/{job\_id}

Get a fine-tuned job details by its UUID.

The ID of the job to analyse.

OK

#### CompletionDetailedJobOut

{object}

#### ClassifierDetailedJobOut

{object}

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.get({    jobId:"c167a961-ffca-4bcf-93ac-6169468dd389",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.get({    jobId:"c167a961-ffca-4bcf-93ac-6169468dd389",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.get(job_id="c167a961-ffca-4bcf-93ac-6169468dd389")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.get(job_id="c167a961-ffca-4bcf-93ac-6169468dd389")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs/{job_id} \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs/{job_id} \
 -X GET \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```

## **POST** /v1/fine\_tuning/jobs/{job\_id}/cancel

Request the cancellation of a fine tuning job.

The ID of the job to cancel.

OK

#### CompletionDetailedJobOut

{object}

#### ClassifierDetailedJobOut

{object}

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.cancel({    jobId:"6188a2f6-7513-4e0f-89cc-3f8088523a49",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.cancel({    jobId:"6188a2f6-7513-4e0f-89cc-3f8088523a49",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.cancel(job_id="6188a2f6-7513-4e0f-89cc-3f8088523a49")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.cancel(job_id="6188a2f6-7513-4e0f-89cc-3f8088523a49")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs/{job_id}/cancel \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs/{job_id}/cancel \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```

## **POST** /v1/fine\_tuning/jobs/{job\_id}/start

Request the start of a validated fine tuning job.

OK

#### CompletionDetailedJobOut

{object}

#### ClassifierDetailedJobOut

{object}

#### Playground

Test the endpoints **live**

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.start({    jobId:"56553e4d-0679-471e-b9ac-59a77d671103",});console.log(result);}run();
```

```
import{Mistral}from"@mistralai/mistralai";const mistral =newMistral({  apiKey:"MISTRAL_API_KEY",});asyncfunctionrun(){const result =await mistral.fineTuning.jobs.start({    jobId:"56553e4d-0679-471e-b9ac-59a77d671103",});console.log(result);}run();
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.start(job_id="56553e4d-0679-471e-b9ac-59a77d671103")# Handle responseprint(res)
```

```
from mistralai import Mistral
import os
with Mistral(    api_key=os.getenv("MISTRAL_API_KEY",""),)as mistral:    res = mistral.fine_tuning.jobs.start(job_id="56553e4d-0679-471e-b9ac-59a77d671103")# Handle responseprint(res)
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs/{job_id}/start \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
curl https://api.mistral.ai/v1/fine_tuning/jobs/{job_id}/start \
 -X POST \
 -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
 -H 'Content-Type: application/json'
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```

```
{"auto_start":false,"created_at":87,"hyperparameters":{},"id":"ipsum eiusmod","model":"ministral-3b-latest","modified_at":14,"status":"QUEUED","training_files":["consequat do"]}
```