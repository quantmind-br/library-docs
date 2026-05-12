---
title: データ抽出ツールの選び方 | Firecrawl
url: https://docs.firecrawl.dev/ja/developer-guides/usage-guides/choosing-the-data-extractor
source: sitemap
fetched_at: 2026-03-23T07:30:04.833227-03:00
rendered_js: false
word_count: 267
summary: This document provides a comparative guide on the three approaches offered by Firecrawl for structured data extraction from web pages, helping users choose between the autonomous agent, extraction endpoint, and scraping tool based on specific use cases.
tags:
    - web-scraping
    - data-extraction
    - firecrawl
    - ai-agent
    - json-mode
    - data-gathering
    - web-automation
category: guide
---

Firecrawl は、ウェブページから構造化データを抽出するために 3 つのアプローチを提供します。各アプローチは、自動化と制御のバランスが異なり、用途に応じて使い分けられます。

## クイック比較

機能`/agent``/extract``/scrape` (JSONモード)**ステータス**稼働中`/agent` を使用稼働中**URL 必須**いいえ (任意)はい (ワイルドカード対応)はい (単一URL)**スコープ**Web全体の探索・発見複数ページ／ドメイン単一ページ**URL 発見**自動Web検索指定URLからクロール行わない**処理方式**非同期非同期同期**スキーマ必須**いいえ (プロンプトまたはスキーマ)いいえ (プロンプトまたはスキーマ)いいえ (プロンプトまたはスキーマ)**料金**動的 (1日あたり5回無料実行)トークンベース (1クレジット = 15トークン)1クレジット／ページ**最適な用途**リサーチ、探索、複雑な情報収集URL が分かっている場合の複数ページ抽出URL が分かっている単一ページ抽出

## 1. `/agent` エンドポイント

`/agent` エンドポイントは、`/extract` の後継となる Firecrawl の最も高度な機能です。AI エージェントを使用して、自律的にウェブを横断して検索・ナビゲートし、データを収集します。

### 主な特長

- **URL は任意**: `prompt` に必要な内容を記述するだけでよく、URL の指定は完全に任意です
- **自律ナビゲーション**: エージェントがサイトを深く検索・巡回し、必要なデータを見つけます
- **ディープウェブ検索**: 複数のドメインやページにまたがる情報を自律的に探索・発見します
- **並列処理**: 複数のソースを同時に処理し、高速に結果を返します
- **利用可能なモデル**: `spark-1-mini` (デフォルト、60% 低コスト) と `spark-1-pro` (高精度)

### 例

### 最適なユースケース: 自律的なリサーチと発見

**シナリオ**: Series A 資金調達を行った AI スタートアップについて、その創業者や調達額を含む情報を見つけたい。 **なぜ `/agent` なのか**: どのウェブサイトにその情報があるか分からない場合でも、Agent が自律的にウェブを検索し、関連する情報源 (Crunchbase、ニュースサイト、企業ページなど) にアクセスして、構造化データとして集約してくれる。 詳細については、[Agent のドキュメント](https://docs.firecrawl.dev/ja/features/agent)を参照してください。

* * *

`/extract` エンドポイントは、LLM を用いた抽出機能により、指定した URL やドメイン全体から構造化データを収集します。

### 主な特徴

- **通常は URL が必須**: 少なくとも 1 つの URL を指定する必要があります (`example.com/*` のようなワイルドカードに対応)
- **ドメインクロール**: ドメイン内で発見されたすべての URL をクロール・解析可能
- **ウェブ検索による拡張**: 指定ドメイン外のリンクをたどるオプション `enableWebSearch` を利用可能
- **スキーマは任意**: 厳密な JSON スキーマまたは自然言語プロンプトのどちらにも対応
- **非同期処理**: ステータス確認用のジョブ ID を返却

### URL の制約

`/extract` の根本的な課題は、通常は事前に URL を把握しておく必要があることです：

1. **発見のギャップ**: 「YC W24 の企業を探す」のようなタスクでは、どの URL にデータが含まれているか分かりません。`/extract` を呼び出す前に、別途検索ステップが必要になります。
2. **扱いづらい Web 検索**: `enableWebSearch` は存在しますが、指定した URL からしか開始できず、探索タスクには不自然なワークフローになります。
3. **`/agent` が作られた理由**: `/extract` は既知の場所からの抽出には向いていますが、データがどこに存在するかを見つける用途にはあまり向いていません。

### 使用例

**シナリオ**: 競合他社のドキュメントの URL があり、`docs.competitor.com/*` からすべての API エンドポイントを抽出したい場合。 **ここで `/extract` が有効だった理由**: 対象のドメインが正確に分かっていたためです。ただし、その場合でも、現在では URL を指定して `/agent` を使うほうが、一般的により良い結果が得られます。 詳細については、[Extract のドキュメント](https://docs.firecrawl.dev/ja/features/extract)を参照してください。

* * *

## 3. JSONモード付きの `/scrape` エンドポイント

JSONモード付きの `/scrape` エンドポイントは、最も制御しやすいアプローチです。特定の1つのURLから構造化データを抽出し、ページ内容をLLMでパースして、指定したスキーマに変換します。

### 主な特長

- **単一URLのみ**: 一度に特定の1ページからデータを抽出するよう設計されています
- **正確なURLが必要**: データを含む正確なURLを把握している必要があります
- **スキーマは任意**: JSON Schemaを使うことも、プロンプトだけを使うことも可能 (LLMが構造を選択)
- **同期処理**: データを即時に返します (ジョブのポーリングは不要)
- **追加フォーマット**: 1つのリクエストでJSON抽出をmarkdown、HTML、スクリーンショットと組み合わせ可能です

### 使用例

**シナリオ**: 価格監視ツールを構築しており、すでにURLがわかっている特定の商品ページから、価格・在庫状況・商品詳細を抽出する必要がある。 **なぜ `/scrape` と JSONモードなのか**: どのページにデータがあるかを正確に把握しており、単一ページから高精度に抽出したく、ジョブ管理のオーバーヘッドなしで同期的に結果を得たい場合に最適。 詳細については、[JSONモードのドキュメント](https://docs.firecrawl.dev/ja/features/llm-extract)を参照してください。

* * *

## 選択ガイド

**データを含む正確なURLが分かっていますか？**

- **いいえ** → `/agent` を使用 (自律的なWeb検索)
- **はい**
  
  - **単一ページ？** → `/scrape` をJSONモードで使用
  - **複数ページ？** → `/agent` をURLと共に使用 (または `/scrape` のバッチ処理)

### シナリオ別の推奨エンドポイント

シナリオ推奨エンドポイント「すべてのAIスタートアップとその資金調達情報を取得する」`/agent`「この特定のプロダクトページからデータを抽出する」`/scrape` (JSONモード)「competitor.com のすべてのブログ投稿を取得する」`/agent` (URL指定)「既知の複数のURLの価格をモニタリングする」`/scrape` (バッチ処理)「特定の業界の企業をリサーチする」`/agent`「既知の50社の企業ページから連絡先情報を抽出する」`/scrape` (バッチ処理)

* * *

## 料金

エンドポイントコスト備考`/scrape` (JSONモード)1クレジット/ページ固定で予測可能`/extract`トークンベース (1クレジット＝15トークン)コンテンツに応じて変動`/agent`動的1日あたり5回まで無料で実行可能、複雑さに応じて変動

### 例: 「Find the founders of Firecrawl」

Endpoint動作内容消費クレジット`/scrape`自分でURLを見つけて、その1ページをスクレイプする約1クレジット`/extract`URLを指定すると、構造化データを抽出する可変 (トークンベース)`/agent`プロンプトを送るだけで、エージェントが発見と抽出を行う約100–500クレジット

**トレードオフ**: `/scrape` は最も低コストだが、URLを事前に把握している必要がある。`/agent` はコストが高いものの、対象の発見を自動で行ってくれる。 詳細な料金については、[Firecrawl Pricing](https://firecrawl.dev/pricing) を参照してください。

* * *

現在 `/extract` を使用している場合、移行は容易です: **移行前 (extract) :**

```
result = app.extract(
    urls=["https://example.com/*"],
    prompt="製品情報を抽出",
    schema=schema
)
```

**変更後 (エージェント使用時) :**

```
result = app.agent(
    urls=["https://example.com"],  # オプション - 完全に省略可能
    prompt="Extract product information from example.com",
    schema=schema,
    model="spark-1-mini"  # より高精度な場合は "spark-1-pro"
)
```

主な利点は、`/agent` を使えば URL をまったく指定せずに、必要なことを言葉で伝えるだけでよい点です。

* * *

## 重要なポイント

1. **正確なURLがわかっている場合は？** `/scrape` を `JSONモード` で使用してください — 最も安価 (1クレジット/ページ) 、最速 (同期処理) 、かつ最も予測しやすいオプションです。
2. **自律的なリサーチが必要ですか？** `/agent` を使用してください — 自動で探索を行い、1日5回まで無料で利用でき、その後は複雑さに応じた動的な料金体系になります。
3. 新しいプロジェクトでは **`/extract` から `/agent` へ移行** してください — `/agent` は、より高機能な後継エンドポイントです。
4. **コストと利便性のトレードオフ**: URLが分かっている場合は `/scrape` が最もコスト効率に優れています。一方で `/agent` はコストが高くなりますが、URLの手動探索が不要になります。

* * *

## 関連ドキュメント

- [エージェント機能のドキュメント](https://docs.firecrawl.dev/ja/features/agent)
- [エージェントモデル](https://docs.firecrawl.dev/ja/features/models)
- [JSONモードのドキュメント](https://docs.firecrawl.dev/ja/features/llm-extract)
- [Extract 機能のドキュメント](https://docs.firecrawl.dev/ja/features/extract)
- [バッチスクレイピングのドキュメント](https://docs.firecrawl.dev/ja/features/batch-scrape)