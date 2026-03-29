---
title: Annotations | Mistral Docs
url: https://docs.mistral.ai/capabilities/document_ai/annotations
source: crawler
fetched_at: 2026-01-29T07:33:33.846435886-03:00
rendered_js: false
word_count: 152
---

Here is an example of how to use our BBox Annotation functionalities.

First, define the response formats for `BBox Annotation`, using either Pydantic or Zod schemas for our SDKs, or a JSON schema for a curl API call.

Pydantic/Zod/JSON schemas accept nested objects, arrays, enums, etc...

You can also provide a description for each entry, the description will be used as detailed information and instructions during the annotation; for example:

Next, make a request and ensure the response adheres to the defined structures using `bbox_annotation_format` set to the corresponding schemas:

The BBox Annotation feature allows to extract data and annotate images that were extracted from the original document, below you have one of the images of a document extracted by our OCR Processor.

![bbox-image](https://docs.mistral.ai/img/img-1.jpeg)

The Image extracted is provided in a base64 encoded format.

And you can annotate the image with the model schema you want, below you have an example output.