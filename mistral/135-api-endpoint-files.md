---
title: Files
url: https://docs.mistral.ai/api/endpoint/files
source: crawler
fetched_at: 2026-01-29T07:33:17.992881678-03:00
rendered_js: false
word_count: 75
summary: A guide providing instructions on how to effectively manage, organize, and store digital files and folders.
tags:
    - file management
    - organization
    - digital storage
category: guide
---

## **GET** /v1/files

Returns a list of files that belong to the user's organization.

## **POST** /v1/files

Upload a file that can be used across various endpoints.

The size of individual files can be a maximum of 512 MB. The Fine-tuning API only supports .jsonl files.

Please contact us if you need to increase these storage limits.

## **GET** /v1/files/{file\_id}

Returns information about a specific file.

## **DELETE** /v1/files/{file\_id}

Delete a file.

## **GET** /v1/files/{file\_id}/content

Download a file

## **GET** /v1/files/{file\_id}/url