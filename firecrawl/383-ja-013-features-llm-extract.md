---
title: JSONモード | Firecrawl
url: https://docs.firecrawl.dev/ja/features/llm-extract
source: sitemap
fetched_at: 2026-03-23T07:22:55.749583-03:00
rendered_js: false
word_count: 117
summary: This document explains how to use the Firecrawl API to extract structured data from web pages using JSON mode and custom schemas or natural language prompts.
tags:
    - firecrawl
    - web-scraping
    - json-extraction
    - ai-data-extraction
    - api-guide
    - structured-data
category: guide
---

FirecrawlはAIを用いて、ウェブページから構造化データを3ステップで取得します:

1. **スキーマを設定（任意）:** 取得したいデータを指定するために（OpenAIの形式の）JSONスキーマを定義するか、厳密なスキーマが不要な場合はウェブページのURLと`prompt`だけを指定します。
2. **リクエストを送信:** URLとスキーマを、JSONモードを用いて/scrape エンドポイントに送ります。詳しくはこちら: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
3. **データを取得:** スキーマに一致するクリーンな構造化データが返ってきます。すぐに利用できます。

これにより、必要なフォーマットでウェブデータを素早く簡単に取得できます。

### /scrape による JSONモード

スクレイピングしたページから構造化データを抽出するために使用します。

出力:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI対応のウェブスクレイピングとデータ抽出",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI対応のウェブスクレイピングとデータ抽出",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI対応のウェブスクレイピングとデータ抽出",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### スキーマ不要の構造化データ

エンドポイントに `prompt` を渡すだけで、スキーマなしで抽出できます。データの構造は LLM が決定します。

出力:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI搭載のウェブスクレイピングとデータ抽出",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI搭載のウェブスクレイピングとデータ抽出",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI搭載のウェブスクレイピングとデータ抽出",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

以下は、ウェブサイトから構造化された企業情報を抽出する包括的な例です：

出力：

```
{
  "success": true,
  "data": {
    "json": {
      "company_mission": "WebサイトをLLM対応データに変換",
      "supports_sso": true,
      "is_open_source": true,
      "is_in_yc": true
    }
  }
}
```

### JSON フォーマットのオプション

v2 で JSONモード を使用する場合、`formats` にスキーマを直接埋め込んだオブジェクトを含めます: `formats: [{ type: 'json', schema: { ... }, prompt: '...' }]` パラメータ:

- `schema`: 取得したい構造化出力を記述する JSON Schema（スキーマベースの抽出では必須）。
- `prompt`: 抽出をガイドするための任意のプロンプト（スキーマなしの抽出でも使用）。

**重要:** v1 と異なり、v2 には個別の `jsonOptions` パラメータはありません。スキーマは `formats` 配列内のフォーマットオブジェクトに直接含める必要があります。

JSON 抽出の結果が一貫しなかったり不完全だったりする場合、次のベストプラクティスが役立ちます。

- **プロンプトは短く、焦点を絞る。** 多くのルールを含む長いプロンプトはばらつきを増やします。具体的な制約 (許可される値など) はプロンプトではなくスキーマ側に移してください。
- **プロパティ名は簡潔にする。** プロパティ名の中に指示や列挙リストを埋め込まないでください。`"installation_type"` のような短いキーを使い、許可される値は `enum` 配列に入れます。
- **制約されたフィールドには `enum` 配列を追加する。** フィールドが固定の値セットを持つ場合、それらを `enum` に列挙し、ページ上に表示されているテキストと完全に一致させてください。
- **フィールドの説明に null ハンドリングを含める。** モデルが欠損値を推測しないよう、各フィールドの `description` に `"Return null if not found on the page."` を追加してください。
- **場所のヒントを追加する。** モデルにページ上のどこからデータを取得するかを伝えます (例: `"Flow rate in GPM from the Specifications table."`) 。
- **大きなスキーマは小さなリクエストに分割する。** フィールド数が多いスキーマ (例: 30 項目以上) は結果の一貫性が下がります。10〜15 フィールドずつ、2〜3 個のリクエストに分割してください。

**よく構造化されたスキーマの例:**

```
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": ["string", "null"],
      "description": "Full descriptive product name as shown on the page. Return null if not found."
    },
    "installation_type": {
      "type": ["string", "null"],
      "description": "Installation type from the Specifications section. Return null if not found.",
      "enum": ["Deck-mount", "Wall-mount", "Countertop", "Drop-in", "Undermount"]
    },
    "flow_rate_gpm": {
      "type": ["string", "null"],
      "description": "Flow rate in GPM from the Specifications section. Return null if not found."
    }
  }
}
```

> AI エージェントで、Firecrawl API キーが必要ですか？自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。