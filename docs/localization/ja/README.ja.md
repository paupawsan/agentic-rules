# 🤖 Agentic Rules Framework (日本語)

あらゆるプラットフォームでインテリジェントなAIエージェントの動作を構造化するプラグアンドプレイフレームワーク。

## 🌍 ローカライズ / Localization / Pelokalan

<details open>
<summary>📚 多言語ドキュメント / Documentation available in multiple languages / Dokumentasi tersedia dalam berbagai bahasa</summary>

### English (英語)
<details>
<summary>🇺🇸 English Documentation / 英語ドキュメント</summary>

- **[Main Page / メインページ](README.md)** - Framework overview and quick start
- **[Documentation Index / 説明書の目次](docs/INDEX.md)** - Complete documentation overview
- **[User Guide / ユーザーガイド](docs/USER-GUIDE.md)** - Step-by-step setup for beginners
- **[Developer Guide / 開発者ガイド](docs/DEVELOPER-GUIDE.md)** - Technical implementation details
- **[System Overview / システムの説明](docs/SYSTEM-OVERVIEW.md)** - Complete system architecture
- **[Extension Manual / 拡張マニュアル](docs/EXTENSION-MANUAL.md)** - Plugin development guide
- **[Troubleshooting / トラブルシューティング](docs/TROUBLESHOOTING.md)** - Problem solving guide

</details>

### Indonesian (インドネシア語)
<details>
<summary>🇮🇩 Indonesian Documentation / インドネシア語ドキュメント</summary>

- **[メインページ / Halaman Utama](../id/README.id.md)** - Ikhtisar framework dan mulai cepat
- **[Indeks Dokumentasi / 説明書の目次](docs/localization/id/INDEX.id.md)** - Ringkasan dokumentasi
- **[Panduan Pengguna / ユーザーガイド](docs/localization/id/USER-GUIDE.id.md)** - Panduan untuk pemula
- **[Panduan Pengembang / 開発者ガイド](docs/localization/id/DEVELOPER-GUIDE.id.md)** - Detail teknis untuk insinyur
- **[Ikhtisar Sistem / システムの説明](docs/localization/id/SYSTEM-OVERVIEW.id.md)** - Detail arsitektur
- **[Manual Ekstensi / 拡張マニュアル](docs/localization/id/EXTENSION-MANUAL.id.md)** - Pengembangan plugin
- **[Panduan Pemecahan Masalah / トラブルシューティング](docs/localization/id/TROUBLESHOOTING.id.md)** - Panduan penyelesaian masalah

</details>

</details>

## 🎯 フレームワーク概要

**Agentic Rules Framework**は、3つの専門ルールシステムを通じてAIエージェントの能力を強化します：

### 🧠 **メモリルール**
📖 **[プラグイン詳細](modules/memory-rules/README.md)** - 10の専門カテゴリによる永続的なコンテキスト、学習、およびパーソナライズをセッション間で実現

### 📚 **RAGルール**
📖 **[プラグイン詳細](modules/rag-rules/README.md)** - スマートな読み取り戦略、コンテキスト最適化、および関連性スコアリングによる効率的な知識活用

### 🤔 **批判的思考ルール**
📖 **[プラグイン詳細](modules/critical-thinking-rules/README.md)** - エラー防止、仮定検証、および証拠ベースの意思決定による体系的な推論強化

**主な利点：**
- **🔌 プラグアンドプレイ**: エージェント動作を変更せずにルールを有効/無効化
- **🌍 マルチプラットフォーム**: Cursor、VSCode、およびカスタムエージェントシステムに対応
- **📦 自己完結型**: 埋め込み設定を含む単一HTMLファイル
- **🛠️ ツール不可知**: エージェントは利用可能なツールを使用してルール要件を実装
- **🌐 汎用性**: 構造化されたガイドラインに従うことができる任意のAIエージェントに適用可能
- **🌍 多言語**: 18以上の言語でローカライズされたルールテンプレート対応

## 🚀 クイックスタート

経験レベルを選択してください：

### 👥 **すべての人向け** (技術知識不要)
📖 **[ユーザーガイド](USER-GUIDE.ja.md)** - ステップバイステップのセットアップ手順

### 🔧 **エンジニア・開発者向け**
📖 **[開発者ガイド](DEVELOPER-GUIDE.ja.md)** - サーバーセットアップ、自動化、およびAPI使用

### 🔌 **プラグイン開発者向け**
📖 **[拡張マニュアル](EXTENSION-MANUAL.ja.md)** - 新しいプラグインの作成方法

## 📋 要件

- **Python 3.8+** (サーバーモードの場合)
- **Webブラウザ** (HTMLインターフェースの場合)
- **対応AIプラットフォーム**: Cursor, VSCode, Claude, Gemini, カスタムエージェント

## 🛠️ インストール

### オプション1: HTMLインターフェース (推奨)
```bash
# リポジトリをクローンまたはダウンロード
git clone https://github.com/paupawsan/agentic-rules.git
cd agentic-rules

# setup.htmlをダブルクリックして起動
# ブラウザでインタラクティブなセットアップを実行
```

### オプション2: サーバーモード
```bash
# Python環境を準備
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係をインストール
pip install flask  # 追加の依存関係が必要な場合

# サーバーを起動
python setup-launcher.py

# ブラウザで http://localhost:8001 にアクセス
```

## 📚 ドキュメント

### 🌍 多言語ドキュメント
- **[English Documentation](../../../README.md)** - 英語版ドキュメント
- **[Dokumentasi Indonesia](../id/README.id.md)** - インドネシア語版ドキュメント

### 📖 主要ドキュメント
- **[システムの概要](SYSTEM-OVERVIEW.ja.md)** - アーキテクチャと仕組み
- **[拡張マニュアル](EXTENSION-MANUAL.ja.md)** - プラグイン開発ガイド
- **[トラブルシューティング](TROUBLESHOOTING.ja.md)** - 問題解決ガイド

### 🏗️ 開発者向け
- **[開発者ガイド](DEVELOPER-GUIDE.ja.md)** - 技術実装の詳細
- **[コアルール](CORE-RULES.ja.md)** - フレームワークの基本ルール

## 🤝 貢献

貢献を歓迎します！

### 貢献の仕方
1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチをプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

### 開発参加
- **バグ報告**: [Issues](../../issues) を使用
- **機能リクエスト**: [Issues](../../issues) で提案
- **コード貢献**: プルリクエスト歓迎
- **翻訳**: 多言語ドキュメントの改善

## 📄 ライセンス

Copyright (c) 2025 Paulus Ery Wasito Adhi

MIT Licenseの下でライセンスされています。LICENSEファイルを参照してください。

---

**🎉 Agentic Rules Framework v1.0.0 が本番環境対応になりました！**

**ダウンロード:** [GitHub Releases](https://github.com/paupawsan/agentic-rules/releases/tag/v1.0.0)

**クイックスタート:** `python setup.py` を実行して開始！

---

*AIエージェントコミュニティのために❤️で構築*