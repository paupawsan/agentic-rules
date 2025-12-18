# ドキュメント (日本語)

このフォルダーには、Agentic Rules Frameworkの詳しい説明書が入っています。

## 説明書の目次

### 📖 基本的な説明書
- **[README.ja.md](README.ja.md)** - フレームワークの簡単な説明と使い方のガイド
- **[../../localization/ja/CORE-RULES.ja.md](../../localization/ja/CORE-RULES.ja.md)** - フレームワークの基本ルールと仕組み
- **[SYSTEM-OVERVIEW.ja.md](SYSTEM-OVERVIEW.ja.md)** - システムの全体的な仕組みと設計

### 👥 ユーザーガイド
- **[USER-GUIDE.ja.md](USER-GUIDE.ja.md)** - 初心者向けの詳しいセットアップ手順
- **[DEVELOPER-GUIDE.ja.md](DEVELOPER-GUIDE.ja.md)** - 上級者向けのセットアップと技術的な実装
- **[TROUBLESHOOTING.ja.md](TROUBLESHOOTING.ja.md)** - よくある問題の解決方法と手動読み込み手順

### 🔧 機能追加と開発
- **[EXTENSION-MANUAL.ja.md](EXTENSION-MANUAL.ja.md)** - フレームワークに機能を追加する詳しい手順

### 📚 プラグインの説明書
- **[../../../modules/memory-rules/docs/localization/ja/README.ja.md](../../../modules/memory-rules/docs/localization/ja/README.ja.md)** - メモリールール：機能、使い方の例、設定
- **[../../../modules/rag-rules/docs/localization/ja/README.ja.md](../../../modules/rag-rules/docs/localization/ja/README.ja.md)** - RAGルール：機能、使い方の例、設定
- **[../../../modules/critical-thinking-rules/docs/localization/ja/README.ja.md](../../../modules/critical-thinking-rules/docs/localization/ja/README.ja.md)** - 批判的思考ルール：機能、使い方の例、設定

### ⚙️ 設定と技術
- **[../settings/README.md](../settings/README.md)** - 全体的な設定のやり方ガイド
- **[../memory-rules/MEMORY-RULES.md](../memory-rules/MEMORY-RULES.md)** - メモリーシステムの技術的な仕組み
- **[../critical-thinking-rules/CRITICAL-THINKING-RULES.md](../critical-thinking-rules/CRITICAL-THINKING-RULES.md)** - 考え方と確認の技術的な仕組み
- **[../rag-rules/RAG-RULES.md](../rag-rules/RAG-RULES.md)** - 情報処理の技術的な仕組み

## すぐに使えるガイド

### 初心者向け
1. [../../README.ja.md](../../README.ja.md)で全体の説明から始める
2. [../../../CORE-RULES.md](../../../CORE-RULES.md)で基本ルールを学ぶ
3. READMEの各プラットフォーム別の部分を確認

### 開発者向け
1. [EXTENSION-MANUAL.ja.md](EXTENSION-MANUAL.ja.md)でルール追加の方法を確認
2. 既存のルールの作り方を勉強
3. 機能追加のチェックリストに従う

### システム統合担当者向け
1. [`../bootstrap.json`](../bootstrap.json)を読み込んで技術的な設定を行う
2. [`../settings/global-settings.json`](../settings/global-settings.json)を設定
3. 必要に応じてプラットフォームの設定を調整

## 説明書の目的

- **フレームワークの説明書**（README、CORE-RULES）は、人間がシステムを理解するためのもの
- **ルールの説明書**（RULES.mdファイル）は、AIが従うアルゴリズムの仕様
- **設定**（JSONファイル）は、コンピュータが読めるセットアップ
- **拡張マニュアル**は、開発のための人間向けの詳しい手順ガイド

## 説明書への貢献

新しいルールや機能を追加する場合：

1. 関連する説明書ファイルを更新
2. この目次に項目を追加
3. 決められた形式と構造に従う
4. 例と問題解決を含める

## バージョン
この説明書はフレームワークバージョン1.0.0に対応しています。

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. MIT Licenseの下でライセンスされています（LICENSEファイルを参照してください）。