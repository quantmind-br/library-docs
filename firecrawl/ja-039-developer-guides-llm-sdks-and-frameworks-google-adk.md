---
title: Agent Development Kit（ADK） - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/llm-sdks-and-frameworks/google-adk
source: sitemap
fetched_at: 2026-03-23T07:35:20.655658-03:00
rendered_js: false
word_count: 107
summary: This document provides instructions for integrating Firecrawl with Google's Agent Development Kit (ADK) using the Model Context Protocol (MCP) to enable advanced web scraping and data extraction capabilities in AI agents.
tags:
    - firecrawl
    - google-adk
    - mcp
    - web-scraping
    - ai-agents
    - data-extraction
    - api-integration
category: guide
---

Model Context Protocol（MCP）経由で Firecrawl を Google の Agent Development Kit（ADK）と統合し、ウェブスクレイピング機能を備えた強力な AI エージェントを構築します。

## 概要

Firecrawl は MCP サーバーを提供しており、Google の ADK とシームレスに統合して、エージェントがあらゆるウェブサイトから効率的にスクレイピング、クロール、構造化データの抽出を行えるようにします。この統合は、パフォーマンス最適化のためにストリーミング対応の HTTP を備えた、クラウド版およびセルフホスト版の Firecrawl インスタンスの両方をサポートします。

## 機能

- あらゆるウェブサイトに対する効率的なスクレイピング、クロール、コンテンツ発見
- 高度な検索機能と賢いコンテンツ抽出
- 深掘り調査と大規模バッチスクレイピング
- 柔軟なデプロイ（クラウドまたはセルフホスト）
- ストリーミング対応HTTPを活用するモダンなウェブ環境向けに最適化

## 前提条件

- [firecrawl.dev](https://firecrawl.dev) で Firecrawl の API キーを取得する
- Google ADK をインストールする

## セットアップ

ツール名称説明スクレイプツール`firecrawl_scrape`高度なオプションで単一のURLからコンテンツをスクレイピングしますバッチスクレイプツール`firecrawl_batch_scrape`レート制限と並列処理を備え、複数のURLを効率的にスクレイピングしますバッチステータスの確認`firecrawl_check_batch_status`バッチ処理のステータスを確認しますマップツール`firecrawl_map`サイト内のインデックス済みURLを網羅的に把握するためにサイト構造をマッピングしますサーチツール`firecrawl_search`ウェブを検索し、必要に応じて検索結果からコンテンツを抽出しますクローラーツール`firecrawl_crawl`高度なオプションで非同期クローリングを開始しますクローラーステータスの確認`firecrawl_check_crawl_status`クローリングジョブのステータスを確認します抽出ツール`firecrawl_extract`LLMを用いてウェブページから構造化された情報を抽出します

## 構成

### 必須設定

**FIRECRAWL\_API\_KEY**: Firecrawl の API キー

- クラウド API を使用する場合は必須（デフォルト）
- FIRECRAWL\_API\_URL を指定したセルフホスト環境を使用する場合は任意

### 任意の設定

**Firecrawl API URL（セルフホスト環境向け）**:

- `FIRECRAWL_API_URL`: カスタム API エンドポイント
- 例: `https://firecrawl.your-domain.com`
- 指定がない場合はクラウド API を使用します

**リトライ設定**:

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: 最大リトライ回数（既定値: 3）
- `FIRECRAWL_RETRY_INITIAL_DELAY`: 初期待機時間（ミリ秒）（既定値: 1000）
- `FIRECRAWL_RETRY_MAX_DELAY`: 最大待機時間（ミリ秒）（既定値: 10000）
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: 指数バックオフ係数（既定値: 2）

**クレジット使用量の監視**:

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: 警告閾値（既定値: 1000）
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: 重大閾値（既定値: 100）

## 例：Web Research Agent

```
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

FIRECRAWL_API_KEY = "YOUR-API-KEY"

# リサーチエージェントを作成
research_agent = Agent(
    model="gemini-2.5-pro",
    name="research_agent",
    description='Webコンテンツをスクレイピング・分析してトピックを調査するAIエージェント',
    instruction='''あなたはリサーチアシスタントです。トピックや質問が与えられた場合:
    1. 検索ツールを使用して関連するWebサイトを検索
    2. 最も関連性の高いページをスクレイピングして詳細情報を取得
    3. 必要に応じて構造化データを抽出
    4. 包括的で出典が明確な回答を提供''',
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp",
            ),
        )
    ],
)

# エージェントを使用
response = research_agent.run("Python 3.13の最新機能は何ですか?")
print(response)
```

## ベストプラクティス

1. **用途に合ったツールを使う**:
   
   - まず関連ページを見つける必要がある場合は `firecrawl_search`
   - 単一ページには `firecrawl_scrape`
   - 既知の複数URLには `firecrawl_batch_scrape`
   - サイト全体の探索とスクレイピングには `firecrawl_crawl`
2. **利用状況を監視する**: 想定外の利用を防ぐためにクレジットのしきい値を設定する
3. **エラーを適切に処理する**: ユースケースに応じてリトライ設定を行う
4. **パフォーマンスを最適化する**: 複数のURLをスクレイピングする場合はバッチ処理を使用する

* * *