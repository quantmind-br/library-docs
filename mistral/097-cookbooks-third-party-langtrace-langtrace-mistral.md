---
title: RAG Observability with Mistral AI and Langtrace - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-langtrace-langtrace_mistral
source: crawler
fetched_at: 2026-01-29T07:33:53.010386948-03:00
rendered_js: false
word_count: 175
---

This Notebook shows the instructions for setting up OpenTelemetry based tracing for Mistral with Langtrace AI.

The Goal for this notebook to showcase a simple RAG app where you can chat with the United states consititution pdf.

## Imports & Initialize clients

## Use Langchain to split pdf into chunks

## Setup Chroma & Insert pdf chunks

Create a chroma collection, specifying the default embedding function which will be used in our RAG when inserting pdf chunks

## Query Collection

1. take query from user, get nearest 3 results from chunked pdf
2. construct a prompt structure
3. Give query and prompt to mistral for the actual response

## Run everything together and monitor using Langtrace.

That's it! Now you should be able to see the traces for all your inference calls on Langtrace!

## First Two Screenshots showcase the Trace and span structure of the whole RAG App.

![Trace 1](https://docs.mistral.ai/cookbooks/third_party/Langtrace/TraceTree1.png)

![Trace 2](https://docs.mistral.ai/cookbooks/third_party/Langtrace/TraceTree2.png)

## Second Two Screenshots are details of Mistral's Run.

- You can see what prompt is specfically fetched from chromadb and sent to mistral as well as the response

![Trace 1](https://docs.mistral.ai/cookbooks/third_party/Langtrace/mistral-langtrace1.png)

![Trace 2](https://docs.mistral.ai/cookbooks/third_party/Langtrace/mistral-langtrace2.png)