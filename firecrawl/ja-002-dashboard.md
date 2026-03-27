---
title: ダッシュボード | Firecrawl
url: https://docs.firecrawl.dev/ja/dashboard
source: sitemap
fetched_at: 2026-03-23T07:26:28.02004-03:00
rendered_js: false
word_count: 76
summary: This document provides an overview of the Firecrawl dashboard, explaining its various features including the playground, browser sessions, agent tools, activity logs, and team management settings.
tags:
    - firecrawl
    - dashboard-guide
    - web-scraping
    - api-management
    - team-administration
    - usage-tracking
category: guide
---

[Firecrawlダッシュボード](https://www.firecrawl.dev/app)では、アカウントの管理、エンドポイントのテスト、使用状況の監視を行えます。以下では、各セクションを簡単に紹介します。

## プレイグラウンド

プレイグラウンドでは、Firecrawl のエンドポイントをコードに統合する前に、ブラウザ上で直接試すことができます。

- [**Scrape**](https://www.firecrawl.dev/app/playground?endpoint=scrape) — 単一のページからコンテンツを抽出します。
- [**Search**](https://www.firecrawl.dev/app/playground?endpoint=search) — Web を検索し、スクレイピングされた結果を取得します。
- [**Crawl**](https://www.firecrawl.dev/app/playground?endpoint=crawl) — Web サイト全体をクロールし、各ページからコンテンツを抽出します。
- [**Map**](https://www.firecrawl.dev/app/playground?endpoint=map) — Web サイト上のすべての URL を検出します。

## ブラウザ

[ブラウザセッションをライブで使ってwebを操作](https://www.firecrawl.dev/app/browser)できます。永続的なプロファイルを作成し、アクションを実行し、スクリーンショットを取得できます。認証や複雑な操作が必要なページで便利です。

## Agent

[Agent](https://www.firecrawl.dev/app/agent) は、AI を活用したリサーチツールで、Web を自律的に閲覧し、リンクをたどり、プロンプトに基づいて構造化データを抽出できます。

## アクティビティログ

[アクティビティログ](https://www.firecrawl.dev/app/logs) では、ステータス、所要時間、消費されたクレジットを含む、最近のAPIリクエストの履歴を確認できます。

## 使用状況

[使用状況](https://www.firecrawl.dev/app/usage) ページでは、クレジット消費量の推移と現在の課金サイクルの合計を確認できます。

## APIキー

[APIキー](https://www.firecrawl.dev/app/api-keys) ページでは、チームのAPIキーを作成、確認、無効化できます。

## 設定

[設定](https://www.firecrawl.dev/app/settings) ページには、3 つのタブがあります。

- **Team** — メンバーの招待、ロールの割り当て、チームの管理を行います。詳しくは、以下の [Team management & roles](#team-management--roles) を参照してください。
- **課金** — 現在のプラン、請求書、自動チャージ設定の確認や、クーポンの適用を行います。あわせて [課金](https://docs.firecrawl.dev/ja/billing) も参照してください。
- **Advanced** — webhook 署名シークレットとチーム削除。

* * *

## チーム管理とロール

Firecrawl では、共有アカウント上で共同作業するためにチームメンバーを招待できます。設定の **Team** タブから、メンバーの招待、ロールの割り当て、チームの管理を行えます。

### ロール

各チームメンバーには、**Admin** または **Member** のいずれかのロールが割り当てられます。ロールは招待を送信する際に選択します。

機能AdminMember**一般**チームの API キーと共有リソースを使用する✓✓**チーム管理**チームメンバー一覧を表示する✓✓チームから脱退する✓✓新しいチームメンバーを招待する✓✗チームメンバーを削除する✓✗メンバーのロールを変更する✓✗保留中の招待を取り消す✓✗チーム名を編集する✓✗**課金**請求書と利用状況を表示する✓✓クレジットクーポンを適用する✓✓サブスクリプションと課金ポータルを管理する✓✗**設定**webhook 署名シークレットを表示する✓✓webhook 署名シークレットを再生成する✓✗チームを削除する✓✗

要するに、**Admins** はチーム管理、課金、設定を完全に管理できます。一方、**Members** はチームのリソースを使用したり、利用状況を確認したり、クーポンを適用したりできますが、チームやサブスクリプションを変更することはできません。