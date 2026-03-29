---
title: OCR at scale via Mistral's Batch API - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-ocr-batch_ocr
source: crawler
fetched_at: 2026-01-29T07:33:49.735753631-03:00
rendered_js: false
word_count: 398
summary: This guide demonstrates how to perform optical character recognition on image datasets using Mistral OCR, comparing standard sequential processing with cost-effective batch inference.
tags:
    - ocr
    - mistral-ai
    - batch-inference
    - image-to-text
    - data-extraction
category: tutorial
---

## Apply OCR to Convert Images into Text

Optical Character Recognition (OCR) allows you to retrieve text data from images. With Mistral OCR, you can do this extremely fast and effectively, extracting text from hundreds and thousands of images (or PDFs).

In this simple cookbook, we will extract text from a set of images using two methods:

- [Without Batch Inference](#scrollTo=qmXyB3rPlXQW): Looping through the dataset, extracting text from each image, and saving the result.
- [With Batch Inference](#scrollTo=jYfWYjzTmixB): Leveraging Batch Inference to extract text with a 50% cost reduction.

* * *

### Used

- OCR
- Batch Inference

### Setup

First, let's install `mistralai` and `datasets`

We can now set up our client. You can create an API key on our [Plateforme](https://console.mistral.ai/api-keys/).

## Without Batch

As an example, let's use Mistral OCR to extract text from multiple images.

We will use a dataset containing raw image data. To send this data via an image URL, we need to encode it in base64. For more information, please visit our [Vision Documentation](https://docs.mistral.ai/capabilities/vision/#passing-a-base64-encoded-image).

For this demo, we will use a simple dataset containing numerous documents and scans in image format. Specifically, we will use the `HuggingFaceM4/DocumentVQA` dataset, loaded via the `datasets` library.

We will download only 100 samples for this demonstration.

With our subset of 100 samples ready, we can loop through each image to extract the text.

We will save the results in a new dataset and export it as a JSONL file.

Perfect, we have extracted all text from the 100 samples. However, this process can be made more cost-efficient using Batch Inference.

## With Batch

To use Batch Inference, we need to create a JSONL file containing all the image data and request information for our batch.

Let's create a function called `create_batch_file` to handle this task by generating a file in the proper format.

The next step involves encoding the data of each image into base64 and saving the URL of each image that will be used.

We can now create our batch file.

With everything ready, we can upload it to the API.

The file is uploaded, but the batch inference has not started yet. To initiate it, we need to create a job.

Our batch is ready and running!

We can retrieve information using the following method:

Let's automate this feedback loop and download the results once they are ready!

Done! With this method, you can perform OCR tasks in bulk in a very cost-effective way.