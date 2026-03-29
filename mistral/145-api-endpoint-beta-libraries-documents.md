---
title: Beta Libraries Documents
url: https://docs.mistral.ai/api/endpoint/beta/libraries/documents
source: crawler
fetched_at: 2026-01-29T07:33:22.423299552-03:00
rendered_js: false
word_count: 316
summary: A collection of documents and resources pertaining to the development, testing, and implementation of beta-phase software libraries.
tags:
    - beta
    - libraries
    - software development
    - documentation
    - testing
category: technical documentation
---

*List documents in a given library.*

## **GET** /v1/libraries/{library\_id}/documents

Given a library, lists the document that have been uploaded to that library.

## **POST** /v1/libraries/{library\_id}/documents

Given a library, upload a new document to that library. It is queued for processing, it status will change it has been processed. The processing has to be completed in order be discoverable for the library search

*Retrieve the metadata of a specific document.*

## **GET** /v1/libraries/{library\_id}/documents/{document\_id}

Given a library and a document in this library, you can retrieve the metadata of that document.

*Update the metadata of a specific document.*

## **PUT** /v1/libraries/{library\_id}/documents/{document\_id}

Given a library and a document in that library, update the name of that document.

## **DELETE** /v1/libraries/{library\_id}/documents/{document\_id}

Given a library and a document in that library, delete that document. The document will be deleted from the library and the search index.

*Retrieve the text content of a specific document.*

## **GET** /v1/libraries/{library\_id}/documents/{document\_id}/text\_content

Given a library and a document in that library, you can retrieve the text content of that document if it exists. For documents like pdf, docx and pptx the text content results from our processing using Mistral OCR.

*Retrieve the processing status of a specific document.*

## **GET** /v1/libraries/{library\_id}/documents/{document\_id}/status

Given a library and a document in that library, retrieve the processing status of that document.

*Retrieve the signed URL of a specific document.*

## **GET** /v1/libraries/{library\_id}/documents/{document\_id}/signed-url

Given a library and a document in that library, retrieve the signed URL of a specific document.The url will expire after 30 minutes and can be accessed by anyone with the link.

*Retrieve the signed URL of text extracted from a given document.*

## **GET** /v1/libraries/{library\_id}/documents/{document\_id}/extracted-text-signed-url

Given a library and a document in that library, retrieve the signed URL of text extracted. For documents that are sent to the OCR this returns the result of the OCR queries.

## **POST** /v1/libraries/{library\_id}/documents/{document\_id}/reprocess

Given a library and a document in that library, reprocess that document, it will be billed again.