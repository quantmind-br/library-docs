---
title: エージェントモデル | Firecrawl
url: https://docs.firecrawl.dev/ja/features/models
source: sitemap
fetched_at: 2026-03-23T07:23:02.929562-03:00
rendered_js: false
word_count: 85
summary: This document provides a guide for choosing between the Spark 1 Mini and Spark 1 Pro models within Firecrawl Agent based on requirements for cost efficiency and extraction accuracy.
tags:
    - firecrawl-agent
    - model-selection
    - data-extraction
    - cost-optimization
    - api-configuration
    - ai-models
category: guide
---

Firecrawl Agent では、用途の異なる 2 つのモデルを用意しています。抽出処理の複雑さとコスト要件に応じて、適切なモデルを選択してください。

## 利用可能なモデル

ModelCostAccuracyBest For`spark-1-mini`**コスト60%削減**標準ほとんどのタスク (デフォルト)`spark-1-pro`標準高精度複雑なリサーチ、重要な抽出処理

## Spark 1 Mini (デフォルト)

`spark-1-mini` は高効率なモデルで、シンプルなデータ抽出タスクに最適です。 **Mini を使う場面:**

- シンプルなデータポイント (連絡先情報、価格情報など) を抽出するとき
- 構造がしっかりしたウェブサイトを扱うとき
- コスト効率を優先したいとき
- 大量の抽出ジョブを実行するとき

**ユースケース例:**

- EC サイトから商品価格を抽出する
- 企業ページから連絡先情報を収集する
- 記事から基本的なメタデータを取得する
- シンプルなデータポイントを検索・取得する

## Spark 1 Pro

`spark-1-pro` は、複雑な抽出タスクで最高レベルの精度を発揮するよう設計されたフラッグシップモデルです。 **Pro を使うべきケース:**

- 複雑な競合分析を行うとき
- 高度な推論を必要とするデータを抽出するとき
- ユースケースにおいて精度が極めて重要なとき
- あいまいまたは見つけにくいデータを扱うとき

**ユースケース例:**

- 複数ドメインにまたがる競合分析
- 推論を必要とする複雑なリサーチタスク
- 複数の情報源からニュアンスを含む情報を抽出する場合
- 重要なビジネスインテリジェンスの収集

## モデルの指定

使用するモデルを選択するには、`model` パラメーターを指定します。

## モデル比較

機能Spark 1 MiniSpark 1 Pro**コスト**60%低コスト標準**精度**標準高い**速度**高速高速**最適な用途**ほとんどのタスク複雑なタスク**推論性能**標準高度**マルチドメイン対応**良好優秀

## モデル別の料金

どちらのモデルも、タスクの複雑さに応じてスケールする動的なクレジットベースの料金体系を採用しています。

- **Spark 1 Mini**: 同等のタスクを Pro と比べて約 60% 少ないクレジットで実行可能
- **Spark 1 Pro**: 最高精度を実現するための標準的なクレジット消費量

## 適切なモデルの選択

```
                    ┌─────────────────────────────────┐
                    │   どのようなタスク?              │
                    └─────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  シンプル/直接  │           │ 複雑/リサーチ    │
          │  抽出           │           │ マルチドメイン  │
          └─────────────────┘           └─────────────────┘
                    │                             │
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  spark-1-mini   │           │  spark-1-pro    │
          │  (60%低コスト)  │           │  (高精度)        │
          └─────────────────┘           └─────────────────┘
```

## API リファレンス

完全なパラメータのドキュメントについては、[Agent API Reference](https://docs.firecrawl.dev/ja/api-reference/endpoint/agent) を参照してください。 どのモデルを使用するべきか迷っていますか？ [help@firecrawl.com](mailto:help@firecrawl.com) までメールでお問い合わせください。

> Firecrawl API キーが必要な AI エージェントですか？ 自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。