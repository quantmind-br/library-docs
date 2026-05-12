---
title: Agent | Firecrawl
url: https://docs.firecrawl.dev/ja/features/agent
source: sitemap
fetched_at: 2026-03-23T07:23:07.70468-03:00
rendered_js: false
word_count: 281
summary: This document explains the Firecrawl /agent API, which automates web research and structured data extraction through autonomous navigation and search.
tags:
    - firecrawl
    - web-scraping
    - data-extraction
    - ai-agent
    - api-documentation
    - structured-data
category: api
---

Firecrawl の `/agent` は、検索・ナビゲーション・データ収集を自動で行い、最も幅広い種類の Web サイトからでも、通常はアクセスしづらい場所のデータを見つけ出し、他のどの API にもできない方法でデータを発見する魔法のような API です。人間なら何時間もかかるエンドツーエンドのデータ収集を、スクリプトや手作業なしで数分で完了させます。 単一のデータポイントが欲しい場合でも、大規模なデータセット全体が必要な場合でも、Firecrawl の `/agent` がデータ取得を代わりに行います。 **`/agent` は、あらゆる場所にあるデータに対する「ディープリサーチ」と考えてください！**

Agent は `/extract` の優れた点をすべて引き継ぎつつ、さらに強化しています:

- **URL 不要**: 必要な内容を `prompt` パラメータで記述するだけでよく、URL は任意です
- **ディープ Web 検索**: サイト内を自律的に検索・巡回し、必要なデータを深部まで探索
- **高い信頼性と正確性**: 幅広い種類のクエリやユースケースで安定して動作
- **高速**: 複数ソースを並列処理して結果を素早く取得

必須パラメータは `prompt` のみです。どのようなデータを抽出したいかを記述してください。構造化された出力を得るには、JSON スキーマを指定してください。各 SDK は、型安全なスキーマ定義のために Pydantic (Python) と Zod (Node) をサポートしています：

### レスポンス

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

## URL を指定する場合 (任意)

エージェントの対象を特定のページに絞り込むために、任意で URL を指定できます。

## ジョブのステータスと完了

Agent ジョブは非同期で実行されます。ジョブの実行を開始すると、ステータス確認に使える Job ID が返されます：

- **デフォルトの方法**: `agent()` が完了まで待機し、最終結果を返します
- **開始してポーリング**: `start_agent` (Python) または `startAgent` (Node) で即座に Job ID を取得し、その後 `get_agent_status` / `getAgentStatus` でポーリングします

### 考えられるステータス

ステータス説明`processing`エージェントがリクエストを処理中です`completed`抽出が正常に完了しました`failed`抽出中にエラーが発生しました`cancelled`ジョブはユーザーによってキャンセルされました

#### 保留状態の例

```
{
  "success": true,
  "status": "processing",
  "expiresAt": "2024-12-15T00:00:00.000Z"
}
```

#### 完成例

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

Agent playground から、エージェントの実行を直接共有できます。共有リンクは公開されるため、リンクを知っている人なら誰でも実行結果とアクティビティを閲覧できます。また、アクセスを取り消してリンクをいつでも無効にできます。共有ページは検索エンジンにインデックスされません。

## モデルの選択

Firecrawl Agent では 2 種類のモデルが利用できます。**Spark 1 Mini はコストが 60% 低く**、デフォルトモデルです。ほとんどのユースケースに最適です。複雑なタスクで最高レベルの精度が必要な場合は Spark 1 Pro にアップグレードしてください。

ModelCostAccuracyBest For`spark-1-mini`**60% 安価**標準ほとんどのタスク (デフォルト)`spark-1-pro`標準より高い複雑なリサーチ、重要度の高い抽出

### Spark 1 Mini (デフォルト)

`spark-1-mini` は効率的なモデルで、シンプルなデータ抽出タスクに最適です。 **Mini を使うのに適したケース:**

- 単純なデータ項目 (連絡先情報、価格情報など) を抽出するとき
- 構造が整理された Web サイトを扱うとき
- コスト効率を重視するとき
- 大量の抽出ジョブを実行するとき

### Spark 1 Pro

`spark-1-pro` は、複雑な抽出タスクで最大限の精度を発揮するよう設計された、当社のフラッグシップモデルです。 **次のような場合は Pro を使用してください:**

- 複雑な競合分析を行う場合
- 深い推論が必要なデータを抽出する場合
- 精度がユースケースにおいて極めて重要な場合
- あいまい、または取得が難しいデータを扱う場合

### モデルの指定

使用するモデルは、`model` パラメーターで指定します。

## パラメータ

ParameterTypeRequiredDescription`prompt`string**Yes**抽出したいデータを自然言語で記述した文字列 (最大 10,000 文字)`model`stringNo使用するモデル: `spark-1-mini` (デフォルト) または `spark-1-pro``urls`arrayNo抽出対象を絞り込むための任意の URL リスト`schema`objectNo構造化された出力のための任意の JSON スキーマ`maxCredits`numberNoこのエージェントタスクで使用するクレジットの最大数。設定しない場合、デフォルトは **2,500** です。ダッシュボードでは **2,500** までの値をサポートしています。これを超える上限を設定するには、API 経由で `maxCredits` を指定してください (2,500 を超える値は常に有料リクエストとして扱われます)。上限に達するとジョブは失敗し、**データは一切返されません** が、実行された作業で消費されたクレジットは請求されます。

項目Agent (新)ExtractURL の指定不要必要速度高速標準コスト低コスト標準信頼性高い標準クエリの柔軟性高い中程度

## 利用例

- **リサーチ**: 「有望なAIスタートアップ上位5社とその資金調達額を調べる」
- **競合分析**: 「SlackとMicrosoft Teamsの料金プランを比較する」
- **データ収集**: 「企業のWebサイトから連絡先情報を抽出する」
- **コンテンツ要約**: 「Webスクレイピングに関する最新のブログ記事を要約する」

## Agent Playground での CSV アップロード

[Agent Playground](https://www.firecrawl.dev/app/agent) は一括処理のための CSV アップロードに対応しています。CSV には 1 列以上の入力データを含めることができます。例えば、企業名だけの 1 列の CSV でもよいですし、企業名、プロダクト、Web サイトの URL など複数列を含めることもできます。各行は、エージェントが処理する 1 つのアイテムを表します。 入力データ (例: 企業名、URL、その他任意のエンティティ) を含む CSV をアップロードし、各行ごとにエージェントにどのようなデータを取得させたいかを説明するプロンプトを作成し、出力フィールドを定義して実行します。エージェントは各行を並列に処理し、結果を自動で入力します。

## APIリファレンス

詳しくは、[Agent API Reference](https://docs.firecrawl.dev/ja/api-reference/endpoint/agent) を参照してください。 フィードバックやサポートが必要な場合は、[help@firecrawl.com](mailto:help@firecrawl.com) までメールでご連絡ください。

## 料金

Firecrawl Agent は、データ抽出リクエストの複雑さに応じてスケールする **ダイナミックな課金モデル** を採用しています。実際に Agent が行った処理内容に基づいて支払う仕組みのため、単純なデータポイントの抽出でも、複数のソースからの複雑な構造化情報の抽出でも、公平な料金になります。

### Agentの料金の仕組み

Research Preview期間中、Agentの料金は**動的でクレジットベース**です：

- **シンプルな抽出** (1ページからの連絡先情報など) は、通常必要なクレジット数が少なく、コストも低くなります
- **複雑なリサーチタスク** (複数ドメインにわたる競合分析など) は、より多くのクレジットを使用しますが、必要な総工数を反映します
- **透明な利用状況**により、各リクエストで消費されたクレジット数を正確に確認できます
- **クレジット変換**により、Agentのクレジット使用量が自動的にクレジットへ変換され、請求処理が容易になります

### Parallel Agents の料金

Spark-1 Fast で複数のエージェントを並列実行する場合、料金はセルあたり 10 クレジットとなり、より料金の見通しが立てやすくなります。

### はじめに

**すべてのユーザー**は、Agent の機能を無料で試せるように、プレイグラウンドまたは API のいずれからでも利用できる**1 日あたり 5 回の無料実行**が付与されます。 それ以上の利用分は、クレジット消費量に応じて課金され、その分がクレジットに換算されます。

### コスト管理

Agent は高コストになることがありますが、コストを下げる方法がいくつかあります:

- **無料実行から始める**: 毎日 5 回の無料リクエストを使って料金感をつかむ
- **`maxCredits` パラメータを設定する**: 消費してもよいクレジットの最大数を設定して支出を制限します。ダッシュボードでは上限は 2,500 クレジットです。より高い上限を設定するには、API 経由で `maxCredits` パラメータを直接使用してください (注: 2,500 を超える値は常に有料リクエストとして課金されます)
- **プロンプトを最適化する**: より具体的なプロンプトほど、使用するクレジットが少なくなることが多い
- **利用状況を監視する**: ダッシュボードを通じて消費量を追跡する
- **期待値を設定する**: 複数ドメインにわたる複雑なリサーチは、単純な単一ページの抽出よりも多くのクレジットを使用します

Try Agent now at [firecrawl.dev/app/agent](https://www.firecrawl.dev/app/agent) で今すぐ Agent を試して、あなたの具体的なユースケースでクレジット使用量がどのようにスケールするかを確認してください。

> Firecrawl API キーが必要な AI agent ですか? 自動オンボーディング手順については [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。