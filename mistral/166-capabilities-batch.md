---
title: Batch Inference | Mistral Docs
url: https://docs.mistral.ai/capabilities/batch
source: crawler
fetched_at: 2026-01-29T07:33:13.116066303-03:00
rendered_js: false
word_count: 603
summary: A guide on using Mistral AI's batch inference API to process large datasets asynchronously, optimizing for cost and throughput.
tags:
    - Mistral AI
    - batch inference
    - API
    - LLM
    - data processing
category: guide
---

Batching allows you to run inference on large inputs in parallel, reducing costs while running large workloads.

### Prepare and Upload your Batch

A batch is composed of a list of API requests. The structure of an individual request includes:

- A unique `custom_id` for identifying each request and referencing results after completion
- A `body` object with the raw request you would have when calling the original endpoint without batching

Here's an example of how to structure a batch request:

A batch `body` object can be any **valid request body for the endpoint** you are using. Below are examples of batches for different endpoints, they have their `body` match the endpoint's request body.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.

For large batches of up to 1M requests, you would create a .jsonl file with the above data. Once saved, you can upload your batch input file to ensure it is correctly referenced when initiating batch processes.

For batches with less than 10k requests, we support [inline batching](#inline-batching).

There are 2 main methods of uploading a batch file:

**A.** Via AI Studio:

- Upload your files here: [https://console.mistral.ai/build/files](https://console.mistral.ai/build/files)
  
  - Upload the file in the format described previously.
  - Set `purpose` to Batch Processing.
- Start and Manage your batches here: [https://console.mistral.ai/build/batches](https://console.mistral.ai/build/batches)
  
  - Create and start a job by providing the `files`, `endpoint` and `model`. You wont need to use the API to upload your files and/or create batching jobs.

**B.** Via the API, explained below:

To upload your batch file, you need to use the `files` endpoint.

### Create a new Batch Job

Create a new batch job, it will be queued for processing.

- Requests Data: The data for the requests to be batched. There are two options:
  
  - `input_files`: a list of the batch input file IDs, see how to use [file-batching](#file-batching).
  - `requests`: a list of the requests to be batched, see how to use [inline batching](#inline-batching).
- `model`: you can only use one model (e.g., `codestral-latest`) per batch. However, you can run multiple batches on the same files with different models if you want to compare outputs.
- `endpoint`: we currently support `/v1/embeddings`, `/v1/chat/completions`, `/v1/fim/completions`, `/v1/moderations`, `/v1/chat/moderations`, `/v1/ocr`, `/v1/classifications`, `/v1/conversations`, `/v1/audio/transcriptions`.
- `metadata`: optional custom metadata for the batch.

The standard batching approach relies on batch files containing all the requests to be processed. We support up to 1 million requests in a single batch, enabling efficient handling of large volumes of requests at a reduced cost. This is ideal for tasks with high throughput requirements but low latency sensitivity or priority.

For batches of fewer than 10,000 requests, we support inline batching. Instead of creating and uploading a `.jsonl` file with all the request data, you can include the request body directly in the job creation request. This is convenient for smaller-scale or less bulk-intensive tasks.

### Retrieve your Batch Job

Once batch sent, you will want to retrieve a lot of information such as:

- The status of the batch job
- The results of the batch job
- The list of batch jobs

You can retrieve the details of a batch job by its ID.

Once the batch job is completed, you can easily download the results.

You can view a list of your batch jobs and filter them by various criteria, including:

- Status: `QUEUED`, `RUNNING`, `SUCCESS`, `FAILED`, `TIMEOUT_EXCEEDED`, `CANCELLATION_REQUESTED` and `CANCELLED`
- Metadata: custom metadata key and value for the batch

### Cancel any Job

If you want to cancel a batch job, you can do so by sending a cancellation request.

Below is an end-to-end example of how to use the batch API from start to finish.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.