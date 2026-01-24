---
title: Indexing · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/configuration/indexing/index.md
source: llms
fetched_at: 2026-01-24T14:00:16.770863983-03:00
rendered_js: false
word_count: 267
summary: This document explains the automated and manual indexing processes for AI Search, detailing how data is converted into vector embeddings and managed via jobs and controls.
tags:
    - ai-search
    - indexing
    - vector-embeddings
    - data-sync
    - performance-optimization
category: guide
---

AI Search automatically indexes your data into vector embeddings optimized for semantic search. Once a data source is connected, indexing runs continuously in the background to keep your knowledge base fresh and queryable.

## Jobs

AI Search automatically monitors your data source for updates and reindexes your content every **6 hours**. During each cycle, new or modified files are reprocessed to keep your Vectorize index up to date.

You can monitor the status and history of all indexing activity in the Jobs tab, including real-time logs for each job to help you troubleshoot and verify successful syncs.

## Controls

You can control indexing behavior through the following actions on the dashboard:

* **Sync Index**: Force AI Search to scan your data source for new or modified files and initiate an indexing job to update the associated Vectorize index. A new indexing job can be initiated every 30 seconds.
* **Pause Indexing**: Temporarily stop all scheduled indexing checks and reprocessing. Useful for debugging or freezing your knowledge base.

## Performance

The total time to index depends on the number and type of files in your data source. Factors that affect performance include:

* Total number of files and their sizes
* File formats (for example, images take longer than plain text)
* Latency of Workers AI models used for embedding and image processing

## Best practices

To ensure smooth and reliable indexing:

* Make sure your files are within the [**size limit**](https://developers.cloudflare.com/ai-search/platform/limits-pricing/#limits) and in a supported format to avoid being skipped.
* Keep your Service API token valid to prevent indexing failures.
* Regularly clean up outdated or unnecessary content in your knowledge base to avoid hitting [Vectorize index limits](https://developers.cloudflare.com/vectorize/platform/limits/).