---
title: PDF Entity Extraction with Indexify and Mistral - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-indexify-pdf-entity-extraction-pdf-entity-extraction
source: crawler
fetched_at: 2026-01-29T07:34:07.082097311-03:00
rendered_js: false
word_count: 399
summary: A tutorial on leveraging Indexify and Mistral AI models to perform automated entity extraction from PDF documents.
tags:
    - Mistral AI
    - Indexify
    - PDF extraction
    - entity extraction
    - NLP
category: guide
---

This cookbook demonstrates how to build a robust entity extraction pipeline for PDF documents using Indexify and Mistral's large language models. You will learn how to efficiently extract named entities from PDF files for various applications such as information retrieval, content analysis, and data mining.

## Introduction

Entity extraction, also known as named entity recognition (NER) involves identifying and classifying named entities in text into predefined categories such as persons, organizations, locations, dates, and more. By applying this technique to PDF documents, we can automatically extract structured information from unstructured text, making it easier to analyze and utilize the content of these documents.

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

The extraction graph defines the flow of data through our entity extraction pipeline. We'll create a graph that first extracts text from PDFs, then sends that text to Mistral for entity extraction.

Replace `'YOUR_MISTRAL_API_KEY'` with your actual Mistral API key.

Now that we have our extraction graph set up, we can upload files and retrieve the entities:

## Customization and Advanced Usage

You can customize the entity extraction process by modifying the `system_prompt` in the extraction graph. For example:

- To focus on specific entity types:
- To include entity relationships:

You can also experiment with different Mistral models by changing the `model_name` parameter to find the best balance between speed and accuracy for your specific use case.

## Conclusion

While the example might look simple, there are some unique advantages of using Indexify for this -

1. **Scalable and Highly Availability**: Indexify server can be deployed on a cloud and it can process 1000s of PDFs uploaded into it, and if any step in the pipeline fails it automatically retries on another machine.
2. **Flexibility**: You can use any other [PDF extraction model](https://docs.getindexify.ai/usecases/pdf_extraction/) we used here doesn't work for the document you are using.

## Next Steps

- Learn more about Indexify on our docs - [https://docs.getindexify.ai](https://docs.getindexify.ai)
- Go over an example, which uses Mistral for [building summarization at scale](https://docs.mistral.ai/cookbooks/third_party-indexify-pdf-summarization-pdf-summarization)