---
title: Firecrawl + n8n - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/workflow-automation/n8n
source: sitemap
fetched_at: 2026-03-23T07:27:25.586085-03:00
rendered_js: false
word_count: 1097
summary: This guide provides instructions on how to integrate Firecrawl with n8n to automate web scraping workflows without programming knowledge, including account setup and service configuration.
tags:
    - web-scraping
    - workflow-automation
    - firecrawl
    - n8n
    - data-extraction
    - no-code
    - integration
category: guide
---

## [​](#firecrawl-%E3%81%A8-n8n-%E3%81%AE%E7%B4%B9%E4%BB%8B) Firecrawl と n8n の紹介

Webスクレイピングの自動化は、現代のビジネスに不可欠です。競合価格の監視、コンテンツの集約、リード獲得、リアルタイムデータでAIアプリを駆動する場合でも、Firecrawl と n8n の組み合わせなら、プログラミング知識なしで強力なソリューションを実現できます。 ![Firecrawl and n8n integration](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=cb863000a893ef260cfe023e2455c88c) **n8n とは？** n8n は、さまざまなツールやサービスを連携できるオープンソースのワークフロー自動化プラットフォームです。キャンバス上にノードをドラッグ＆ドロップして接続し、自動化フローを組み立てるビジュアルな開発環境と捉えてください。400以上の連携により、n8n はコードを書かずに高度な自動化を構築できます。

## [​](#%E3%81%AA%E3%81%9C-n8n-%E3%81%A8-firecrawl-%E3%82%92%E4%BD%B5%E7%94%A8%E3%81%99%E3%82%8B%E3%81%AE%E3%81%8B%EF%BC%9F) なぜ n8n と Firecrawl を併用するのか？

従来のウェブスクレイピングには多くの課題があります。サイト構造が変わるとカスタムスクリプトはすぐに壊れます。ボット対策で自動リクエストはブロックされがちです。JavaScript 依存のサイトは正しくレンダリングされません。インフラは常時メンテナンスが必要です。 Firecrawl はスクレイピングに伴う技術的な複雑さを引き受け、n8n は自動化の基盤を提供します。組み合わせることで、次のような本番運用に耐えるワークフローを構築できます。

- あらゆるウェブサイトから安定してデータを抽出
- 取得データをほかの業務ツールへ連携
- スケジュール実行やイベントトリガーに対応
- 単純なタスクから複雑なパイプラインまでスケール可能

このガイドでは、両プラットフォームのセットアップと、最初のスクレイピングワークフローをゼロから構築する手順を説明します。

## [​](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%97-1-firecrawl-%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B) ステップ 1: Firecrawl アカウントを作成する

Firecrawl はワークフロー向けに Web スクレイピング機能を提供します。アカウントを作成し、API 認証情報を取得しましょう。

### [​](#firecrawl-%E3%81%AB%E3%82%B5%E3%82%A4%E3%83%B3%E3%82%A2%E3%83%83%E3%83%97) Firecrawl にサインアップ

1. ウェブブラウザで [firecrawl.dev](https://firecrawl.dev) にアクセスする
2. 「Get Started」または「Sign Up」ボタンをクリックする
3. メールアドレスまたは GitHub でアカウントを作成する
4. 指示が表示されたら、メールを確認して認証する

### [​](#api%E3%82%AD%E3%83%BC%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B) APIキーを取得する

サインイン後、Firecrawl を n8n に接続するには API キーが必要です:

1. Firecrawl のダッシュボードを開く
2. [API Keys ページ](https://www.firecrawl.dev/app/api-keys)へ移動
3. 「Create New API Key」をクリック
4. キーにわかりやすい名前を付ける (例：「n8n Integration」)
5. 生成された API キーをコピーして安全な場所に保存する

![Firecrawl api key section](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-api-key-creation-dashboard.gif?s=2c04559b9027dfe825e3ba7d78af8527)

API キーはパスワードのようなものです。安全に保管し、公開しないでください。次のセクションでこのキーが必要になります。

Firecrawl はサインアップ時に無料クレジットを付与しており、ワークフローのテストや本チュートリアルの完了に十分です。

## [​](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%97-2-n8n-%E3%82%92%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%E3%81%99%E3%82%8B) ステップ 2: n8n をセットアップする

n8n にはクラウド版とセルフホスト版の 2 つのデプロイ方法があります。はじめての方には、クラウド版が最も手早く始められる方法です。

### [​](#%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B-n8n-%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%82%92%E9%81%B8%E6%8A%9E) 使用する n8n バージョンを選択

**n8n Cloud (初心者におすすめ) ：**

- インストール不要
- 無料プランあり
- マネージドなインフラ
- 自動アップデート

**セルフホスト：**

- データを完全にコントロール
- 自前のサーバーで実行
- Docker のインストールが必要
- 特定のセキュリティ要件がある上級ユーザー向け

ニーズに合ったオプションを選んでください。どちらの方法でも同じワークフローエディタのインターフェースにたどり着きます。

### [​](#%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3a%EF%BC%9An8n-cloud-%E5%88%9D%E5%BF%83%E8%80%85%E3%81%AB%E3%81%8A%E3%81%99%E3%81%99%E3%82%81) オプションA：n8n Cloud (初心者におすすめ)

1. [n8n.cloud](https://n8n.cloud) にアクセス
2. 「Start Free」または「Sign Up」をクリック
3. メールアドレスまたは GitHub で登録
4. 本人確認 (認証) を完了
5. n8n のダッシュボードに移動します

![サインアップオプションが表示された n8n Cloud のホームページ](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7965f6fab8bd1d48b81db7c1dbed1e7f) 無料プランには、ワークフローの構築とテストに必要なものが一通り揃っています。実行時間の拡張や高度な機能が必要になった場合は、後からアップグレードできます。

### [​](#%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3b-docker-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E3%82%BB%E3%83%AB%E3%83%95%E3%83%9B%E3%82%B9%E3%83%88) オプションB: Docker を使ったセルフホスト

自社インフラ上で n8n を実行したい場合は、Docker を使って迅速にセットアップできます。 **前提条件:**

- コンピューターに [Docker Desktop](https://www.docker.com/products/docker-desktop/) がインストールされていること
- コマンドライン／ターミナルの基本的な知識

**インストール手順:**

1. ターミナルまたはコマンドプロンプトを開く
2. ワークフロー データを永続化するための Docker ボリュームを作成します:

```
docker volume create n8n_data
```

このボリュームは、コンテナを再起動してもデータが保持されるよう、ワークフロー、クレデンシャル、実行履歴を保存します。

3. n8n の Docker コンテナを実行します:

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

![n8n の起動とともに Docker コマンドが実行されているターミナル](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-docker-self-hosted-installation.gif?s=4968ecd0996ef3e76dc0abb886ae52ca)

4. n8n の起動を待ちます。サーバーが稼働していることを示す出力が表示されます
5. ブラウザで `http://localhost:5678` にアクセスします
6. メールアドレスで登録して n8n アカウントを作成します

![localhost:5678 の n8n セルフホスト版のウェルカム画面](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=163949933d76425a68ec728639e767ea) セルフホストの n8n インスタンスがローカルで稼働しました。インターフェースは n8n Cloud と同一なので、どちらのオプションでもこのガイドの残りを同様に進められます。

`--rm` フラグは停止時にコンテナを自動削除しますが、データは `n8n_data` ボリュームに安全に保持されます。本番環境へのデプロイについては、より高度な設定オプションを含む [n8n self-hosting documentation](https://docs.n8n.io/hosting/) を参照してください。

### [​](#n8n-%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%95%E3%82%A7%E3%83%BC%E3%82%B9%E3%82%92%E7%90%86%E8%A7%A3%E3%81%99%E3%82%8B) n8n のインターフェースを理解する

n8n に初めてログインすると、メインダッシュボードが表示されます。 ![n8n dashboard showing the workflow list view with "Create new workflow" button](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5d92092b94fd021c2cebf163c2ef4d01) 主なインターフェース要素:

- **Workflows**: 保存したワークフローが表示されます
- **Executions**: ワークフロー実行の履歴
- **Credentials**: 保存済みの API キーと認証トークン
- **Settings**: アカウントとワークスペースの設定

「Create New Workflow」をクリックして、ワークフローエディタを開きます。

### [​](#%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%90%E3%82%B9) ワークフローキャンバス

ワークフローエディタは自動化を構築する場所です。 ![中央に「+」ボタンが表示された空の n8n ワークフローキャンバス](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7508078e88b57ccedc2a4d4a258fddf8) 重要な要素:

- **キャンバス**: ノードを配置して接続するメインエリア
- **ノード追加ボタン (+)** : クリックしてワークフローに新しいノードを追加
- **ノードパネル**: 「+」をクリックすると開き、利用可能なノードが一覧表示される
- **ワークフローの実行**: テストのためにワークフローを手動で実行
- **保存**: ワークフローの設定を保存

Firecrawl ノードを追加して、最初のワークフローを作成しましょう。

## [​](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%97-3-firecrawl-%E3%83%8E%E3%83%BC%E3%83%89%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E8%A8%AD%E5%AE%9A) ステップ 3: Firecrawl ノードのインストールと設定

n8n は Firecrawl をネイティブにサポートしています。ノードをインストールし、先ほど作成した API キーを使って Firecrawl アカウントに接続します。

### [​](#%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC%E3%81%AB-firecrawl-%E3%83%8E%E3%83%BC%E3%83%89%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%99%E3%82%8B) ワークフローに Firecrawl ノードを追加する

1. 新しいワークフローのキャンバスで、中央の「**+**」ボタンをクリックします
2. 右側にノード選択パネルが開きます
3. 上部の検索ボックスに「**Firecrawl**」と入力します
4. 検索結果に Firecrawl ノードが表示されます

<!--THE END-->

![「+」ボタンをクリックし、検索で「Firecrawl」と入力し、Firecrawl ノードが表示される様子](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-search-install-firecrawl-node.gif?s=6d81f8bf967429cfaf2bcf22c3976fbf)

5. Firecrawl ノードの横にある「**Install**」をクリックします
6. インストールが完了するまで待ちます (数秒かかります)
7. インストール後、Firecrawl ノードをクリックしてキャンバスに追加します

![Firecrawl ノードがキャンバスに追加され、Firecrawl ロゴ付きのボックスとして表示されている様子](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-node-added-canvas.gif?s=d7480ebf8ef357fba9a0c5ee5123ffc8) Firecrawl ノードは、Firecrawl ロゴ付きのボックスとしてキャンバスに表示されます。このノードは、ワークフロー内の単一の Firecrawl オペレーションを表します。

### [​](#firecrawl-api%E3%82%AD%E3%83%BC%E3%82%92%E6%8E%A5%E7%B6%9A%E3%81%99%E3%82%8B) Firecrawl APIキーを接続する

Firecrawlノードを使用する前に、APIキーで認証する必要があります。

1. Firecrawlノードのボックスをクリックして、右側の設定パネルを開きます
2. 上部に「Credential to connect with」のドロップダウンが表示されます
3. 初めての場合は「**Create New Credential**」をクリックします

<!--THE END-->

![Firecrawl node configuration panel showing the credentials dropdown with "Create New Credential" option](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-api-credentials-setup.gif?s=547bda13daeb17dd963160a8ef4bbf48)

4. 資格情報の設定ウィンドウが開きます
5. この資格情報の名前を入力します (例：「My Firecrawl Account」)
6. 「API Key」フィールドにFirecrawlのAPIキーを貼り付けます
7. 画面下部の「**Save**」をクリックします

資格情報はn8nに保存されました。今後のFirecrawlノードではAPIキーを再入力する必要はありません。

### [​](#%E6%8E%A5%E7%B6%9A%E3%82%92%E3%83%86%E3%82%B9%E3%83%88%E3%81%99%E3%82%8B) 接続をテストする

Firecrawl ノードが正しく接続されているか確認します：

1. Firecrawl ノードを選択したまま、設定パネルを確認します
2. 「Resource」ドロップダウンで「Scrape a url and get its content」を選択します
3. 「URL」フィールドに次を入力します：`https://firecrawl.dev`
4. 他の設定はひとまずデフォルトのままにします
5. ノード右下の「Test step」ボタンをクリックします

![Scrape 操作を選択し、example.com の URL を入力して、Test step ボタンをクリックする](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-test-connection-scrape.gif?s=a5a832a971778744a6ceaf9d2ff0cdb1) すべてが正しく設定されていれば、ノード下部の出力パネルに example.com からスクレイプしたコンテンツが表示されます。 おめでとうございます！Firecrawl ノードは正常に接続され、動作しています。

## [​](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%97-4-telegram-%E3%83%9C%E3%83%83%E3%83%88%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B) ステップ 4: Telegram ボットを作成する

最初のワークフローを構築する前に、通知を受け取るための Telegram ボットが必要です。Telegram の BotFather を使えば、無料かつ簡単にボットを作成できます。

### [​](#botfather%E3%81%A7%E3%83%9C%E3%83%83%E3%83%88%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B) BotFatherでボットを作成する

1. スマートフォンまたはデスクトップでTelegramを開く
2. 「**@BotFather**」 (Telegramの公式ボット) を検索する
3. 「**Start**」をクリックしてBotFatherとのチャットを開始する
4. 新しいボットを作成するためにコマンド `/newbot` を送信する
5. BotFatherからボット名の入力を求められる (ユーザーに表示される名前)
6. 「**My Firecrawl Bot**」のような名前を入力する
7. 次にボットのユーザー名を選ぶ。末尾は必ず「bot」で終わる必要がある (例：「**my\_firecrawl\_updates\_bot**」)
8. ユーザー名が利用可能であれば、BotFatherがボットを作成し、ボットトークンを含むメッセージを送信する

![BotFatherでボットを作成する手順。会話の流れ全体を表示](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=45ee39deae96fbc3eac5fdb2eeba2e0b)

ボットトークンは安全に保管してください。このトークンは、n8nがあなたのボットとしてメッセージを送信できるようにするパスワードのようなものです。絶対に公開しないでください。

### [​](#%E3%83%81%E3%83%A3%E3%83%83%E3%83%88id%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B) チャットIDを取得する

自分宛てにメッセージを送るには、Telegram のチャットIDが必要です：

1. Webブラウザを開き、次のURLにアクセスします (`YOUR_BOT_TOKEN` を実際のボットトークンに置き換えてください) :
   
   ```
   https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
   ```
2. このブラウザタブは開いたままにしておく
3. Telegram でボットのユーザー名 (先ほど作成したもの) を検索する
4. 「**Start**」をクリックしてボットとのチャットを開始する
5. ボットに任意のメッセージを送る (例：「hello」)
6. ブラウザタブに戻ってページを更新する
7. JSON レスポンス内の `"chat":{"id":` フィールドを探す
8. `"id":` の横にある数値がチャットID (例：`123456789`)
9. 後で使えるようにこのチャットIDを保存しておく

![Browser showing Telegram API getUpdates response with chat ID highlighted](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-api-get-chat-id-browser.gif?s=e074ecf1a659bdfa7284e86c923be06f)

チャットIDは、ボットとの会話を一意に識別するIDです。n8nがどこにメッセージを送るか指定するために使用します。

これで、Telegram を n8n のワークフローに統合する準備が整いました。

## [​](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%975-telegram-%E3%81%A7%E5%AE%9F%E8%B7%B5%E7%9A%84%E3%81%AA%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B) ステップ5: Telegram で実践的なワークフローを構築する

ここでは、情報をあなたの Telegram に直接送信する3つの実用的なワークフローを構築します。これらの例では、Firecrawl のさまざまな操作と、それらを Telegram 通知に統合する方法を示します。

### [​](#%E4%BE%8B-1-%E6%AF%8E%E6%97%A5%E3%81%AE-firecrawl-%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%E3%83%87%E3%83%BC%E3%83%88%E8%A6%81%E7%B4%84) 例 1: 毎日の Firecrawl プロダクトアップデート要約

毎朝、Telegram に Firecrawl のプロダクトアップデート要約を配信します。 **作成するもの:**

- 毎日午前9時に Firecrawl のプロダクトアップデートブログをスクレイピング
- コンテンツの要約を AI で生成
- 要約を Telegram に送信

**手順:**

1. n8n で新しいワークフローを作成
2. **Schedule Trigger** ノードを追加:
   
   - キャンバス上の「**+**」ボタンをクリック
   - 「**Schedule Trigger**」を検索
   - 設定: 毎日 午前9:00

<!--THE END-->

![Schedule Trigger configured for daily 9 AM execution](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-schedule-trigger-daily-cron.gif?s=ae68cd74cdf14a1d012861df8319b245)

3. **Firecrawl** ノードを追加:
   
   - Schedule Trigger の横の「**+**」をクリック
   - 「**Firecrawl**」を検索して追加
   - Firecrawl の認証情報を選択
   - 設定:
     
     - **Resource**: URL をスクレイプしてコンテンツを取得
     - **URL**: `https://www.firecrawl.dev/blog/category/product-updates`
     - **Formats**: 「Summary」を選択

<!--THE END-->

![Adding and configuring Firecrawl node with the blog URL and Summary format selected](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-scrape-blog-summary.gif?s=ad1684f165aacd7ab5d1530cdac73962)

4. **Telegram** ノードを追加:
   
   - Firecrawl の横の「**+**」をクリック
   - 「**Telegram**」を検索
   - 「**Send a text message**」をクリックしてキャンバスに追加
5. Telegram の認証情報を設定:
   
   - Telegram ノードをクリックして設定を開く
   - 「Credential to connect with」ドロップダウンで「**Create New Credential**」をクリック
   - BotFather で取得したボットトークンを貼り付け
   - 「**Save**」をクリック

<!--THE END-->

![Telegram credential configuration with bot token field](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-telegram-bot-token-credentials.gif)

6. Telegram メッセージを設定:
   
   - **Operation**: Send Message
   - **Chat ID**: 自分のチャット ID を入力
   - **Text**: ひとまず「hello」のままにする
   - Firecrawl から要約を受け取りつつ、メッセージ送信をテストするため「**Execute step**」をクリック。

<!--THE END-->

![Configuring Telegram node and mapping the summary field to the message text](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-test-telegram-message-firecrawl.gif)

- Firecrawl の要約構造に合わせ、Firecrawl ノードの出力から `summary` フィールドをドラッグしてメッセージ本文に追加します。

<!--THE END-->

7. ワークフローをテスト:
   
   - 「**Execute Workflow**」をクリック
   - Telegram で要約メッセージを確認

<!--THE END-->

![Complete workflow showing Schedule Trigger → Firecrawl → Telegram with all nodes connected](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=1c3eacbcb705c21c6265ae3ecbd59d59)

8. 「**Active**」スイッチを切り替えてワークフローを有効化

これで Telegram ボットが、毎朝午前9時に Firecrawl のプロダクトアップデート要約を送信します。

### [​](#%E4%BE%8B-2-ai%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E6%A4%9C%E7%B4%A2%E3%81%8B%E3%82%89telegram%E3%81%B8) 例 2: AIニュース検索からTelegramへ

このワークフローでは、FirecrawlのSearch操作を使ってAIニュースを検索し、整形した結果をTelegramに送信します。 **例 1 からの主な違い:**

- スケジュールではなく**Manual Trigger**を使用 (オンデマンド実行)
- Scrapeの代わりに**Search**操作を使用
- 複数の結果を整形するために**Code**ノードを追加

**ワークフローの構築:**

1. 新しいワークフローを作成し、**Manual Trigger**ノードを追加
2. 次の設定で**Firecrawl**ノードを追加:
   
   - **Resource**: 検索し、必要に応じて検索結果をスクレイプ
   - **Query**: `ai news`
   - **Limit**: 5

<!--THE END-->

![Firecrawl Search node configuration with "ai news" query](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-search-ai-news-results.gif?s=23eb224783b0b3155d179a0342839621)

3. 検索結果を整形するために**Code**ノードを追加:
   
   - 「Run Once for All Items」を選択
   - 次のコードを貼り付け:

```
const results = $input.all();
let message = "最新のAIニュース:\n\n";

results.forEach((item) => {
  const webData = item.json.data.web;
  webData.forEach((article, index) => {
    message += `${index + 1}. ${article.title}\n`;
    message += `${article.description}\n`;
    message += `${article.url}\n\n`;
  });
});

return [{ json: { message } }];
```

![Code ノードを追加し、フォーマット用スクリプトを貼り付ける](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-code-node-format-news-articles.gif?s=cafb96e0b7f2ef27a09ae2957390799b)

4. **Telegram** ノードを更新 (保存済みの認証情報を使用) :
   
   - **Text**: Code ノードの `message` フィールドをドラッグ

![AI ニュースが Telegram に送信されたワークフロー実行の完了](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-execute-workflow-telegram-delivery.gif)

Manual Trigger を Schedule Trigger に置き換えると、設定した間隔で AI ニュースを自動更新できます。

### [​](#%E4%BE%8B-3-ai-%E3%82%92%E6%B4%BB%E7%94%A8%E3%81%97%E3%81%9F%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E8%A6%81%E7%B4%84) 例 3: AI を活用したニュース要約

このワークフローは Example 2 に AI を追加し、OpenAI を使って最新の AI ニュースを Telegram に送信する前に賢く要約を生成します。 **Example 2 からの主な変更点:**

- **OpenAI の認証情報**の設定を追加
- Code と Telegram の間に **AI Agent** ノードを追加
- AI Agent がニュース記事を分析し、的確に要約
- Telegram は生のニュース一覧ではなく、AI 生成の要約を受け取る

**ワークフローの変更点:**

1. **OpenAI API キーを取得**:
   
   - [platform.openai.com/api-keys](https://platform.openai.com/api-keys) にアクセス
   - サインインするかアカウントを作成
   - 「**Create new secret key**」をクリック
   - 名前を付ける (例: 「n8n Integration」)
   - すぐに API キーをコピー (後からは表示されません)

<!--THE END-->

![OpenAI ダッシュボードでの API キー作成](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/openai-api-key-creation-dashboard.gif?s=8222a339a403f85272102256fa91fc27)

2. **AI Agent ノードを追加して接続**:
   
   - Code ノードの後で「**+**」をクリック
   - 「**Basic LLM Chain**」または「**AI Agent**」を検索
   - Code ノードの `message` フィールドを AI Agent の入力プロンプト欄にドラッグ
   - LLM プロバイダーとして **OpenAI** を選択

<!--THE END-->

![AI Agent ノードの追加、Code ノードからの入力ドラッグ、OpenAI を LLM として接続](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-agent-openai-llm-setup.gif)

3. **OpenAI の認証情報を追加**:
   
   - OpenAI で「**Create New Credential**」をクリック
   - OpenAI API キーを貼り付け
   - モデルを選択: **gpt-5-mini** (コスト効率重視) または **gpt-5** (高性能)
   - 「**Save**」をクリック

<!--THE END-->

![AI Agent ノードに OpenAI の認証情報を追加](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-openai-credentials-gpt-model.gif?s=c97249f572e8d530583918ebc3357d53)

4. **AI Agent にシステムプロンプトを追加**:
   
   - AI Agent ノードで、次のシステムプロンプトを追加:

```
あなたはAIニュースアナリストです。提供されたAIニュース記事を分析し、最も重要な開発動向とトレンドを強調した簡潔で洞察力のある要約を作成してください。
関連するトピックをまとめ、これらの開発がなぜ重要なのかについて背景情報を提供してください。
要約は会話調で魅力的なものとし、3〜4段落程度にまとめてください。
```

![AI Agent ノードへの system prompt の追加](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-ai-agent-system-prompt-configuration.gif?s=45c34c7010aa6319f8d4dde84c6e5ab9)

5. **Telegram ノードを更新してテスト**:
   
   - Telegram ノードを更新:
     
     - **Text**: AI Agent の出力 (生成された要約) をドラッグ
     - Code ノードの message への旧マッピングを削除
   - 「**Execute Workflow**」をクリックしてテスト
   - AI がすべてのニュース記事を解析し、要約を作成
   - Telegram で AI 生成の要約を確認

![AI 生成の要約が Telegram に送信されたワークフローの実行完了](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-summary-telegram-workflow-execution.gif)

AI Agent は整形済みのニュース記事をすべて受け取り、賢く要約を生成します。これにより、トレンドや重要な動向をひと目で把握しやすくなります。

## [​](#firecrawl%E3%81%AE%E3%82%AA%E3%83%9A%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E7%90%86%E8%A7%A3%E3%81%99%E3%82%8B) Firecrawlのオペレーションを理解する

いくつかワークフローを作成したところで、n8nで利用できるFirecrawlの各種オペレーションを見ていきましょう。各オペレーションは、特定のWebスクレイピングのユースケースに合わせて設計されています。

### [​](#url%E3%82%92%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0%E3%81%97%E3%81%A6%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B) URLをスクレイピングしてコンテンツを取得する

単一のウェブページからコンテンツを抽出し、さまざまなフォーマットで返します。 **機能:**

- 単一のURLをスクレイピング
- クリーンなMarkdown、HTML、またはAI生成の要約を返す
- スクリーンショットの取得やリンクの抽出に対応

**適した用途:**

- 記事の抽出
- 商品ページの監視
- ブログ記事のスクレイピング
- ページ要約の生成

**使用例:** 毎日のブログ要約 (上の例1のように)

### [​](#%E6%A4%9C%E7%B4%A2%E3%81%97%E3%80%81%E5%BF%85%E8%A6%81%E3%81%AB%E5%BF%9C%E3%81%98%E3%81%A6%E7%B5%90%E6%9E%9C%E3%82%92%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0) 検索し、必要に応じて結果をスクレイピング

ウェブ検索を実行し、必要に応じてコンテンツをスクレイピングした結果を返します。 **機能:**

- ウェブ、ニュース、画像の検索
- タイトル、説明、URLの返却
- 必要に応じて結果の全文をスクレイピング

**適した用途:**

- リサーチの自動化
- ニュースのモニタリング
- トレンドの発見
- 関連コンテンツの発見

**使用例:** AIニュースアグリゲーション (上記のExample 2のように)

### [​](#%E3%82%A6%E3%82%A7%E3%83%96%E3%82%B5%E3%82%A4%E3%83%88%E3%82%92%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B) ウェブサイトをクロールする

ウェブサイト上の複数ページを再帰的に検出してスクレイピングします。 **機能:**

- リンクを自動追跡
- 複数ページを一度にスクレイピング
- パターンによるURLフィルタリング

**適した用途:**

- ドキュメントの一括抽出
- サイトアーカイブ
- 複数ページのデータ収集

### [​](#%E3%82%A6%E3%82%A7%E3%83%96%E3%82%B5%E3%82%A4%E3%83%88%E3%82%92%E3%83%9E%E3%83%83%E3%83%97%E3%81%97%E3%81%A6-url-%E3%82%92%E5%8F%96%E5%BE%97) ウェブサイトをマップして URL を取得

コンテンツをスクレイピングせずに、サイトで見つかったすべての URL を返します。 **機能:**

- サイト内のすべてのリンクを検出
- クリーンな URL リストを返す
- 高速・軽量

**最適な用途:**

- URL のディスカバリー
- サイトマップ生成
- 大規模クロールの計画

### [​](#%E3%83%87%E3%83%BC%E3%82%BF%E6%8A%BD%E5%87%BA) データ抽出

カスタムプロンプトやスキーマに基づき、AIで構造化情報を抽出します。 **機能:**

- AIによるデータ抽出
- 指定した形式でデータを返す
- 複数ページに対応

**適している用途:**

- カスタムデータ抽出
- データベースの構築
- 構造化情報の収集

### [​](#%E3%83%90%E3%83%83%E3%83%81%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%97) バッチスクレイプ

複数のURLを並行で効率的にスクレイピングします。 **機能:**

- 複数URLを一括処理
- ループより高効率
- 結果をまとめて返す

**適した用途:**

- URLリストの一括処理
- 大量データの収集
- 大規模なスクレイピングプロジェクト

### [​](#agent) Agent

自然言語プロンプトに基づいて、AI エージェントが自律的にウェブサイトを閲覧し、データを抽出します。 **機能概要:**

- 必要なデータの内容を説明するプロンプトを受け取る
- AI エージェントが自律的にページを移動しながら情報を抽出する
- **Sync** モード (結果が返るまで待機) と **Async** モード (すぐにジョブ ID を返却) が利用可能
- Async モード使用時は **Get Agent Status** を使って結果をポーリングする

**適している用途:**

- プロンプトに基づいて行う、複雑で複数ページにまたがるデータ収集
- 正確なページ構造が分からない状態での情報抽出
- 複数ページをまたいでナビゲーションが必要となるリサーチタスク

**Sync と Async の違い:**

- **Agent (Sync)** はジョブを開始し、1 ステップで結果が返ってくるため、ほとんどのユースケースで最もシンプルです。**Max Wait Time** パラメータは、タイムアウトするまでノードが結果をポーリングする時間を制御します (デフォルト: 300 秒、最大: 600 秒) 。Agent ジョブの所要時間がこれを超える場合、Firecrawl 側ではジョブが完了する可能性があっても、ノードはタイムアウト status を返します。10 分を超える可能性があるジョブについては、代わりに Async モードを使用してください。
- **Agent (Async)** はすぐにジョブ ID を返します。ジョブ完了後に結果を取得するために、**Get Agent Status** オペレーションを持つ 2 つ目の Firecrawl ノードを追加してください。

Agent 機能の詳細は、[Agent documentation](https://docs.firecrawl.dev/ja/features/agent) を参照してください。

## [​](#%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC%E3%81%AE%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%A8%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB) ワークフローのテンプレートとサンプル

ゼロから構築する代わりに、あらかじめ用意されたテンプレートから始められます。n8nコミュニティは、コピーしてカスタマイズできる多数のFirecrawlワークフローを作成しています。

### [​](#%E6%B3%A8%E7%9B%AE%E3%81%AE%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88) 注目のテンプレート

### [​](#%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88%E6%96%B9%E6%B3%95) テンプレートのインポート方法

n8n コミュニティのテンプレートを使用するには:

1. ワークフローテンプレートのリンクをクリック
2. テンプレートページで「**Import template to localhost:5678 self-hosted instance**」ボタンをクリック
3. n8n インスタンスでワークフローが開きます
4. 各ノードの認証情報を設定
5. ユースケースに合わせて設定をカスタマイズ
6. ワークフローを有効化

![n8n.io からテンプレートをインポートし、インポートボタンと n8n に表示されたワークフローを示す](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-import.gif?s=5bd77d25fa2dc525e0032a483803fd00)

## [​](#%E3%83%99%E3%82%B9%E3%83%88%E3%83%97%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%82%B9) ベストプラクティス

信頼性が高く効率的なワークフローを構築するには、次のガイドラインに従ってください。

### [​](#%E3%83%86%E3%82%B9%E3%83%88%E3%81%A8%E3%83%87%E3%83%90%E3%83%83%E3%82%B0) テストとデバッグ

- スケジュールを有効にする前に、必ずワークフローを手動でテストする
- フロー全体をテストするには「**Execute Workflow**」ボタンを使う
- 各ノードで出力データを確認して正確性を検証する
- 過去の実行を確認して問題をデバッグするには「**Executions**」タブを使う

![タイムスタンプとステータス付きのワークフロー実行履歴を表示する Executions タブ](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-debugging.gif?s=2962335b6f72ea39cf6cb68cb6ed83c3)

### [​](#%E3%82%A8%E3%83%A9%E3%83%BC%E5%87%A6%E7%90%86) エラー処理

- 失敗を検知して処理するために Error Trigger ノードを追加する
- ワークフロー失敗時の通知を設定する
- 重要度の低いノードには「**Continue On Fail**」設定を使う
- ワークフローの実行を定期的に監視する

### [​](#%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E6%9C%80%E9%81%A9%E5%8C%96) パフォーマンス最適化

- 複数のURLにはループではなくBatch Scrapeを使う
- 対象サイトに過度な負荷をかけないよう、適切なレート制限を設定する
- 不要なリクエストを減らすため、可能な場合はデータをキャッシュする
- 高負荷なワークフローはオフピーク時間に実行するようスケジュールする

### [​](#%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3) セキュリティ

- ワークフロー設定で API キーを絶対に公開しない
- 認証情報は n8n のクレデンシャル機能で安全に保管する
- ワークフローを公開共有する際は注意する
- 対象サイトの利用規約および robots.txt を順守する

## [​](#%E6%AC%A1%E3%81%AE%E3%82%B9%E3%83%86%E3%83%83%E3%83%97) 次のステップ

これで Firecrawl と n8n を使ってウェブスクレイピングの自動化を構築するための基礎は身につきました。ここからの学習の進め方は次のとおりです：

### [​](#%E9%AB%98%E5%BA%A6%E3%81%AA%E6%A9%9F%E8%83%BD%E3%82%92%E6%8E%A2%E3%82%8B) 高度な機能を探る

- リアルタイム処理のための Webhook 設定を学ぶ
- プロンプトとスキーマを使った AI ベースの抽出を試す
- 分岐ロジックを備えた複雑なマルチステップのワークフローを構築する

### [​](#%E3%82%B3%E3%83%9F%E3%83%A5%E3%83%8B%E3%83%86%E3%82%A3%E3%81%AB%E5%8F%82%E5%8A%A0) コミュニティに参加

- [Firecrawl Discord](https://discord.gg/firecrawl) - Firecrawlの質問やウェブスクレイピングの議論に参加
- [n8n Community Forum](https://community.n8n.io/) - ワークフロー自動化に関する質問はこちら
- ワークフローを共有して、コミュニティから学びましょう

### [​](#%E6%8E%A8%E5%A5%A8%E5%AD%A6%E7%BF%92%E3%83%91%E3%82%B9) 推奨学習パス

1. このガイドの例示ワークフローを一通り実行する
2. コミュニティライブラリのテンプレートをカスタマイズする
3. 業務の実課題を解決するワークフローを構築する
4. Firecrawl の高度な操作を学ぶ
5. 他のユーザーのために自作テンプレートを公開する

**お困りですか？** 行き詰まったり質問がある場合は、Firecrawl と n8n のコミュニティが活発で頼りになります。自動化を構築する際は、遠慮せずにガイダンスを求めてください。

## [​](#%E8%BF%BD%E5%8A%A0%E3%83%AA%E3%82%BD%E3%83%BC%E3%82%B9) 追加リソース

- [Firecrawl API ドキュメント](https://docs.firecrawl.dev/ja/api-reference/v2-introduction)
- [n8n ドキュメント](https://docs.n8n.io/)
- [Webスクレイピングのベストプラクティス](https://www.firecrawl.dev/blog)