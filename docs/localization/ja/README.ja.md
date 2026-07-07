# 🤖 Agentic Rules Framework (日本語)

あらゆるプラットフォームでインテリジェントなAIエージェントの動作を構造化するプラグアンドプレイフレームワーク。

## 🌍 ローカライズ / Localization / Pelokalan

<details open>
<summary>📚 多言語ドキュメント / Documentation available in multiple languages / Dokumentasi tersedia dalam berbagai bahasa</summary>

### English (英語)
<details>
<summary>🇺🇸 English Documentation / 英語ドキュメント</summary>

- **[Main Page / メインページ](../../../README.md)** - Framework overview and quick start
- **[Documentation Index / 説明書の目次](../../INDEX.md)** - Complete documentation overview
- **[User Guide / ユーザーガイド](../../USER-GUIDE.md)** - Step-by-step setup for beginners
- **[Developer Guide / 開発者ガイド](../../DEVELOPER-GUIDE.md)** - Technical implementation details
- **[System Overview / システムの説明](../../SYSTEM-OVERVIEW.md)** - Complete system architecture
- **[Extension Manual / 拡張マニュアル](../../EXTENSION-MANUAL.md)** - Plugin development guide
- **[Troubleshooting / トラブルシューティング](../../TROUBLESHOOTING.md)** - Problem solving guide

</details>

### Indonesian (インドネシア語)
<details>
<summary>🇮🇩 Indonesian Documentation / インドネシア語ドキュメント</summary>

- **[メインページ / Halaman Utama](../id/README.id.md)** - Ikhtisar framework dan mulai cepat
- **[Indeks Dokumentasi / 説明書の目次](../id/INDEX.id.md)** - Ringkasan dokumentasi
- **[Panduan Pengguna / ユーザーガイド](../id/USER-GUIDE.id.md)** - Panduan untuk pemula
- **[Panduan Pengembang / 開発者ガイド](../id/DEVELOPER-GUIDE.id.md)** - Detail teknis untuk insinyur
- **[Ikhtisar Sistem / システムの説明](../id/SYSTEM-OVERVIEW.id.md)** - Detail arsitektur
- **[Manual Ekstensi / 拡張マニュアル](../id/EXTENSION-MANUAL.id.md)** - Pengembangan plugin
- **[Panduan Pemecahan Masalah / トラブルシューティング](../id/TROUBLESHOOTING.id.md)** - Panduan penyelesaian masalah

</details>

</details>

## 🧩 Claude Codeで使う（プラグイン）

**Claude Code**を使っている場合、フレームワークはネイティブプラグインとしてインストールできます。`setup.html`もブートストラップも不要です。**プラグインを有効にすること自体がアクティベーションです。** Claude Codeは数あるアダプターの一つにすぎません。プラグインはすべて[claude-code/](../../../claude-code/)内に収まっており、プラットフォーム非依存のコア（`modules/`）には一切手を加えません。

```bash
# 1. このリポジトリをプラグインマーケットプレイスとして追加
/plugin marketplace add paupawsan/agentic-rules

# 2. マーケットプレイスからプラグインをインストール
/plugin install agentic-rules@agentic-rules
```

Claude Code内から管理します:

```bash
/plugin                 # 有効化/無効化、オプション編集
/agentic-rules:status   # 有効なモジュールを表示
/agentic-rules:help     # 概要
```

**得られるもの**

- 4つのルールモジュールが、関連する場面で自動的に読み込まれる**スキル**として提供されます（メモリ、RAG/コンテキスト、批判的思考、エージェント相互作用ユニットテスト）。
- 任意の**常時オン**モード（`always_on_injection`）。有効なルールを毎セッションに注入します — `CLAUDE.md`に最も近い動作です。
- 任意の**ナレッジグラフ**MCPサーバー。`kg_mcp_url`にエンドポイントを設定します（未設定でもメモリ/RAGは支障なく動作します）。
- **重複なし** — スキルもインジェクターも、正規の`modules/`ルールファイル（`ja`/`id`などフレームワーク同梱の全言語）を直接読み込みます。上流の変更は再同期なしで反映されます。

**設定**（`/plugin`で指定）

| オプション | デフォルト | 用途 |
|--------|---------|---------|
| `language` | `en` | 注入されるルールテキストの言語（`en` / `ja` / `id`） |
| `memory_path` | — | メモリストアのルートディレクトリ |
| `enable_memory` / `enable_rag` / `enable_critical_thinking` | 有効 | ルールモジュールの切り替え |
| `enable_agent_unit_test` | 無効 | 会話の監査（明示的に呼び出す） |
| `always_on_injection` | 無効 | 毎セッション注入 vs オンデマンドのスキル |
| `kg_mcp_url` | — | ナレッジグラフMCPエンドポイント（空欄で無効） |

📖 **[Claude Codeプラグインガイド（英語）](../../CLAUDE_CODE_PLUGIN.md)** — コンポーネントの対応関係、ルールの提供方法、`setup.html`との違いの詳細。

> 以下のセクション（`setup.html`、ブートストラップ）は**他のプラットフォーム**（Cursor、VSCode、カスタムエージェントシステム）向けです。Claude Codeユーザーはスキップできます。

---

## 🚀 クイックスタート - 初回セットアップ（他のプラットフォーム）

### ⚠️ **ステップ1: セットアップインターフェースを実行（重要！）**
**まず`setup.html`を実行してルールを設定し、必要なファイルを生成してください！**

1. **GitHubからダウンロード** フレームワークファイルをダウンロード
2. **ダブルクリック** `setup.html`でウェブインターフェースを起動
3. **ルールを設定** 希望するルール（メモリ、RAG、批判的思考）を選択
4. **設定ファイルを生成** 構成ファイルを生成

> 💡 **なぜsetup.htmlを最初に？** ウェブインターフェースはブートストラップシステムが必要とする構成ファイルとルールファイルを作成します。このステップなしでは、フレームワークが適切に初期化されない可能性があります。
>
> 🔧 **エンジニア/開発者向け**: より優れた機能を備えたPythonランチャーを使用してください - 直接ファイル作成とサーバーコントロールを提供します。セットアップ自動化オプションについては[開発者ガイド](DEVELOPER-GUIDE.ja.md)を参照してください。

---

### ⚡ **ステップ2: Agentic Rulesシステムの初期化**
**setup.htmlの後、この1回限りのブートストラップ初期化を完了してください！**

1. **AIエージェントに伝える**: `agentic rules systemを/path/to/your/agentic-rulesフォルダで初期化してください。setup.htmlは既に完了しているので、bootstrap初期化だけを実行してください。`
2. **プロンプトが表示されたら権限を付与** してフレームワークを有効化
3. **設定を確認** メモリ、RAG、批判的思考ルールの設定
4. **フレームワークがアクティブ** - エージェントが拡張機能を備えました！

> 💡 **なぜこのステップが必要か？** フレームワークはAI環境との適切な統合を確保するために初期ブートストラップ設定が必要です。この1回限りのセットアップで全フレームワーク機能を有効化します。

---

## 🎯 フレームワーク概要

**Agentic Rules Framework**は、4つの専門ルールシステムを通じてAIエージェントの能力を強化します：

### 🧠 **メモリルール**（ローカルメモリシステム）
📖 **[プラグイン詳細](../../../modules/memory-rules/docs/localization/ja/README.ja.md)** - **ローカルで人間が読めるメモリ**システム、10の専門カテゴリによる永続的なコンテキスト、学習、およびパーソナライズをセッション間で実現。AIエージェントのメモリデータに対する完全な可視性と制御。

### 📚 **RAGルール**
📖 **[プラグイン詳細](../../../modules/rag-rules/docs/localization/ja/README.ja.md)** - スマートな読み取り戦略、コンテキスト最適化、関連性スコアリング、そして**自動ナレッジグラフ構築**によるプロジェクト理解と関係性マッピング

### 🤔 **批判的思考ルール**
📖 **[プラグイン詳細](../../../modules/critical-thinking-rules/docs/localization/ja/README.ja.md)** - エラー防止、仮定検証、および証拠ベースの意思決定による体系的な推論強化

### 🧪 **エージェントインタラクションユニットテスト**（デフォルトで無効）
📖 **[プラグイン詳細](../../../modules/agent-interaction-unit-test/docs/localization/ja/README.ja.md)** - グラウンドチェック要件、Chain of Thoughtログ、エージェントデバッグ分析を備えた、エージェント会話のテストフレームワーク。

**主な利点：**
- **🔌 プラグアンドプレイ**: エージェント動作を変更せずにルールを有効/無効化
- **🖥️ マルチプラットフォーム**: Cursor、VSCode、およびカスタムエージェントシステムに対応
- **📦 自己完結型**: 埋め込み設定を含む単一HTMLファイル
- **🛠️ ツール不可知**: エージェントは利用可能なツールを使用してルール要件を実装
- **🌐 汎用性**: 構造化されたガイドラインに従うことができる任意のAIエージェントに適用可能
- **🌍 多言語**: コアフレームワークにはen/ja/idが標準搭載。プラグインテンプレートシステムはカスタム拡張向けに18以上の追加言語に対応

## 🧠 **ナレッジグラフ統合**
デフォルトで有効 — プロジェクト理解のための自動KG構築と活用。

### **できること**
- **🔍 自動発見**: 会話とコードベースをスキャンしてナレッジグラフを構築
- **🧷 スマートリンク**: 関連する概念、ファイル、アイデアを自動的に接続
- **💬 プロアクティブな活用**: 手動での有効化なしに会話でKGの知見を活用
- **⏳ 時間認識ナレッジ** *(v1.5.0)*: 知識が変化すると、古い事実は削除されず
  置き換えられます。デフォルトの検索は現在の知識のみを返しますが、
  履歴は問い合わせ可能なまま残ります（「X日時点で何を知っていたか？」）。
  エージェントメモリ向けにバイテンポラルなデータベースモデリングを応用したもので、
  [Zepの Graphiti](https://github.com/getzep/graphiti)に着想を得ています
  （概念のみを参考にし、コードは再利用していません）。モデルの詳細、
  データベースを用いた実装、使うべき/使うべきでない場面については
  [KG実装ガイド](KG_IMPLEMENTATION_GUIDE.ja.md)を、実際に何が変わるかについては
  [導入前後の比較](TEMPORAL_KG_COMPARISON.ja.md)を参照してください。

### **ユーザー向け**
- **ゼロ設定**: 標準セットアップだけでそのまま動作
- **強化された会話**: 応答に関連する過去のコンテキストが含まれることがあります
- **関係性の理解**: プロジェクトの構成要素同士のつながりを把握

### **エージェント開発者向け**
📖 **[KG実装ガイド](KG_IMPLEMENTATION_GUIDE.ja.md)** - KG機能のロジックとアルゴリズム擬似コード
📖 **[ユーザー向けKG統合](README_KG_INTEGRATION.ja.md)** - エンドユーザーから見たKG体験とメリット

## 🧪 **エージェントインタラクションユニットテスト - 効果的な形式**

`CORE-RULES.md`と`RULES.md`ファイルを通じたChain of Thoughtログ記録を用いた、構造化されたエージェント対話テストです。

### **ユニットテスト形式の例**
```
UNIT TEST: Agent Memory Retrieval
Framework: Agentic Rules v1.5.2
Task: Test basic agent Memory retrieval.

Instruction:
Sync your memory for current project.

Output:
I want unit test report in markdown format @debug
```

**フレームワークが提供するもの：**
- **🔍 グラウンドチェック検証**: 情報の主張をソースと突き合わせて検証
- **🛡️ 前提への問いかけ**: 暗黙の前提の検出と検証
- **⚡ ツールコール監査**: 関連性スコア付きのツール実行ログ
- **🎯 意思決定文書化**: 代替案を含む意思決定ポイントの監査証跡
- **📊 コンテキスト管理**: コンテキスト利用状況の監視と最適化
- **🔧 エージェントデバッグ分析**: エージェントの推論過程、ツール使用、パラメータ選択の分析
- **✅ コンプライアンス検証**: フレームワーク要件に対する自動チェック

## 📋 詳しく知る

#### 👥 **すべての人向け** (技術知識不要)
📖 **[ユーザーガイド](USER-GUIDE.ja.md)** - ステップバイステップのセットアップ手順

#### 🔧 **エンジニア・開発者向け**
📖 **[開発者ガイド](DEVELOPER-GUIDE.ja.md)** - サーバーセットアップ、自動化、およびAPI使用

#### 🛠️ **プラグイン開発者向け**
📖 **[拡張マニュアル](EXTENSION-MANUAL.ja.md)** - プラグイン開発とフレームワーク拡張

#### 📚 **システムアーキテクチャと技術詳細**
📖 **[システムの説明](SYSTEM-OVERVIEW.ja.md)** - 完全な技術アーキテクチャと設計思想

#### 🐛 **トラブルシューティングとFAQ**
📖 **[トラブルシューティング](TROUBLESHOOTING.ja.md)** - よくある問題の解決策と手動読み込み手順
🛠️ **クイックスキャフォールド**: `python generate_plugin_scaffold.py --help` - プラグインテンプレートを即座に生成

### 🔄 **フレームワークのライフサイクル**
- **初期化**: ユーザー同意のもとでの一回限りのセットアップ
- **自動アクティベーション**: 初回セットアップ後にフレームワークが自動的にロード
- **設定**: `settings/global-settings.json`で設定を変更
- **リセット**: `.agentic_initialized`ファイルを削除して再初期化を強制

## 🤝 貢献

**貢献を歓迎します！** 本プロジェクトはコミュニティの意見と協力によって発展しています。

- 📝 **問題の報告**: バグを見つけた、または提案がありますか？ [Issueを作成](https://github.com/paupawsan/agentic-rules/issues)
- 🔧 **プルリクエストの送信**: フレームワークの改善にご協力ください
- 💬 **ディスカッション**: エージェントシステムとAIの振る舞いについての議論に参加
- 📖 **ドキュメント**: ガイドとドキュメントの改善にご協力ください

## ⚠️ 重要な免責事項

**個人プロジェクト**: 本フレームワークは個人の時間とリソースを使って設計・開発されています。私はいかなる企業にも所属しておらず、これは公式な製品やサービスではありません。

**メンテナンスに関する注記**: 継続的な更新や迅速な保守を保証することはできません。フレームワークの機能性と安全性を維持するよう努めますが、更新は利用可能な時間とリソースに依存します。

**コミュニティサポート**: 皆さんの貢献、フィードバック、参加は本フレームワークの継続的な発展と改善にとって大きな意味を持ちます。コミュニティの関与が、プロジェクトの有用性と関連性を保つ助けになります。

**ベストエフォートでの動作**: 本フレームワークはコードレベルの強制ではなく、AIエージェントへの指示によって機能します。ルールが実際に守られるかどうか（主張のグラウンドチェック、メモリの想起、KGの活用など）は、使用する具体的なエディタ・エージェント・モデルの組み合わせに依存します — 動作はセットアップによって異なり、すべての環境で保証されるものではありません。

**自己責任でのご利用**: 本フレームワークは現状有姿で提供されます。利用者はご自身のユースケースへの適合性を評価し、適切なセキュリティ対策を実施してください。

---

Copyright (c) 2025-2026 Paulus Ery Wasito Adhi. MIT Licenseの下でライセンスされています（LICENSEファイルを参照）。