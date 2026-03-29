---
title: PDF Summarization with Indexify and Mistral - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-indexify-pdf-summarization-pdf-summarization
source: crawler
fetched_at: 2026-01-29T07:34:08.045631323-03:00
rendered_js: false
word_count: 379
---

In this cookbook, we'll explore how to create a PDF summarization pipeline using Indexify and Mistral's large language models. By the end of the document, you should have a pipeline capable of ingesting 1000s of PDF documents, and using Mistral for summarization.

## Introduction

The summarization pipeline is going to be composed of two steps -

- PDF to Text extraction. We are going to use a pre-built extractor for this - `tensorlake/pdfextractor`.
- We use Mistral for summarization.

## Prerequisites

Before we begin, ensure you have the following:

- Create a virtual env with Python 3.9 or later
- `pip` (Python package manager)
- A Mistral API key
- Basic familiarity with Python and command-line interfaces

## Setup

### Install Indexify

First, let's install Indexify using the official installation script in a terminal:

Start the Indexify server:

This starts a long running server that exposes ingestion and retrieval APIs to applications.

Next, we'll install the necessary extractors in a new terminal:

Once the extractors are downloaded, you can start them:

The extraction graph defines the flow of data through our summarization pipeline. We'll create a graph that first extracts text from PDFs, then sends that text to Mistral for summarization.

Replace `'YOUR_MISTRAL_API_KEY'` with your actual Mistral API key.

## Implementing the Summarization Pipeline

Now that we have our extraction graph set up, we can upload files and make the pipeline generate summaries:

## Customization and Advanced Usage

You can customize the summarization process by modifying the `system_prompt` in the extraction graph. For example:

- To generate bullet-point summaries:
- To focus on specific aspects of the document:

You can also experiment with different Mistral models by changing the `model_name` parameter to find the best balance between speed and accuracy for your specific use case.

## Conclusion

While the example might look simple, there are some unique advantages of using Indexify for this -

1. **Scalable and Highly Availability**: Indexify server can be deployed on a cloud and it can process 1000s of PDFs uploaded into it, and if any step in the pipeline fails it automatically retries on another machine.
2. **Flexibility**: You can use any other [PDF extraction model](https://docs.getindexify.ai/usecases/pdf_extraction/) we used here doesn't work for the document you are using.

## Next Steps

- Learn more about Indexify on our docs - [https://docs.getindexify.ai](https://docs.getindexify.ai)
- Learn how to use Indexify and Mistral for [entity extraction from PDF documents](https://docs.mistral.ai/cookbooks/third_party-indexify-pdf-entity-extraction-pdf-entity-extraction)