---
title: キュー状況 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:13:02.929824-03:00
rendered_js: false
word_count: 20
summary: This document provides the API endpoint details and authentication requirements for retrieving real-time status metrics of a team's web scraping job queue.
tags:
    - api-reference
    - job-queue
    - scraping-metrics
    - firecrawl-api
    - authentication
    - concurrency-limits
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/queue-status \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "jobsInQueue": 123,
  "activeJobsInQueue": 123,
  "waitingJobsInQueue": 123,
  "maxConcurrency": 123,
  "mostRecentSuccess": "2023-11-07T05:31:56Z"
}

curl --request GET \
  --url https://api.firecrawl.dev/v2/team/queue-status \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "jobsInQueue": 123,
  "activeJobsInQueue": 123,
  "waitingJobsInQueue": 123,
  "maxConcurrency": 123,
  "mostRecentSuccess": "2023-11-07T05:31:56Z"
}
```

チームのスクレイプキューに関するメトリクスです。

> Firecrawl APIキーが必要なAIエージェントですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### レスポンス

ご利用プランごとの同時実行可能なアクティブジョブ数の上限