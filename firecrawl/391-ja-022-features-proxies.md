---
title: プロキシ | Firecrawl
url: https://docs.firecrawl.dev/ja/features/proxies
source: sitemap
fetched_at: 2026-03-23T07:22:45.507673-03:00
rendered_js: false
word_count: 54
summary: This document explains how to configure proxy settings and geographic locations in Firecrawl to optimize web scraping performance and reliability.
tags:
    - web-scraping
    - proxy-configuration
    - firecrawl-api
    - data-extraction
    - location-settings
    - enhanced-mode
category: configuration
---

Firecrawl は、複雑さが異なるウェブサイトのスクレイピングを支援するために、複数のプロキシタイプを提供しています。プロキシタイプは `proxy` パラメータで指定できます。

> 既定では、プロキシタイプやロケーションを指定しなくても、信頼性とアクセス性を確保するために、Firecrawl はすべてのリクエストをプロキシ経由でルーティングします。

## ロケーションベースのプロキシ選択

Firecrawl は、指定または自動検出されたロケーションに基づいて最適なプロキシを自動的に選択します。これにより、スクレイピングのパフォーマンスと信頼性が向上します。ただし、現時点ではすべてのロケーションに対応しているわけではありません。利用可能なロケーションは次のとおりです:

国コード国名ベーシックプロキシ対応拡張プロキシ対応AEアラブ首長国連邦ありなしAUオーストラリアありなしBRブラジルありなしCAカナダありなしCN中国ありなしCZチェコありなしDEドイツありなしEEエストニアありなしEGエジプトありなしESスペインありなしFRフランスありなしGB英国ありなしGRギリシャありなしHUハンガリーありなしIDインドネシアありなしILイスラエルありなしINインドありなしITイタリアありなしJP日本ありなしMYマレーシアありなしNOノルウェーありなしPLポーランドありなしPTポルトガルありなしQAカタールありなしSGシンガポールありなしUSアメリカ合衆国ありありVNベトナムありなし

上記にないロケーションのプロキシが必要な場合は、[こちらからご連絡](mailto:help@firecrawl.com)のうえ、要件をお知らせください。 プロキシやロケーションを指定しない場合、Firecrawl は自動的に US のプロキシを使用します。

## プロキシのロケーション指定方法

リクエストで `location.country` パラメータを設定すると、特定のプロキシロケーションを指定できます。たとえば、ブラジルのプロキシを使う場合は `location.country` に `BR` を指定します。 詳細は [APIリファレンスの `location.country`](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location) を参照してください。

## プロキシタイプ

Firecrawl は3種類のプロキシをサポートしています：

- **basic**: ほとんどのサイトをスクレイピングするためのプロキシ。高速で、通常は問題なく動作します。
- **enhanced**: プライバシーを維持しながら複雑なサイトをスクレイピングするための強化プロキシ。速度は遅くなりますが、特定のサイトではより信頼性があります。[Enhanced Mode の詳細はこちら →](https://docs.firecrawl.dev/ja/features/enhanced-mode)
- **auto**: basic プロキシが失敗した場合、Firecrawl は自動的に強化プロキシでスクレイピングを再試行します。強化プロキシでの再試行が成功した場合、そのスクレイピングには5クレジットが請求されます。最初の basic での試行が成功した場合は、通常のコストのみが請求されます。

* * *

> **Note:** クレジットコストや再試行戦略を含む強化プロキシの詳細な使用方法については、[Enhanced Mode のドキュメント](https://docs.firecrawl.dev/ja/features/enhanced-mode)を参照してください。

> Firecrawl API キーが必要な AI agent ですか？ 自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。