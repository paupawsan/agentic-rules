# 🔧 開発者ガイド - Agentic Rules Framework (日本語)

## エンジニア・開発者向け（高度なセットアップ）

このガイドでは、高度な使用法、自動化、技術実装の詳細を説明します。

## 🚀 高度なセットアップオプション

### オプションA: 拡張サーバーモード（推奨）

**自動化による完全なファイルシステムアクセス：**

```bash
# 拡張サーバーを起動（推奨）
python setup-launcher.py

# 8000が使用中の場合はカスタムポート
python setup-launcher.py --port 8080

# 基本モード（ダウンロードダイアログ）
python setup-launcher.py --web
```

**拡張モードの利点：**
- ✅ **4つの保存オプション**: コピー、保存（ダイアログ）、ダウンロード、直接作成
- ✅ **直接ファイル作成** - 手動配置不要
- ✅ **自動クリーンアップ** - 競合ファイルタイプを削除
- ✅ **リアルタイムフィードバック** - 即時ファイル操作
- ✅ **サーバーコントロール** - Webインターフェースからのクリーンシャットダウン

### オプションB: コマンドラインインターフェース

**完全なプログラム制御：**

```bash
# インタラクティブセットアップ
python setup.py

# 引数付き非インタラクティブ
python setup.py --lang ja --rules memory,rag --file-type GEMINI.md
```

## 📋 完全セットアッププロセス

### 1. インターフェースの起動

**拡張モード（エンジニア向け）：**
```bash
python setup-launcher.py
```
完全なファイルシステムアクセスでhttp://localhost:8000/setup.htmlを開きます。

**基本モード（誰でも）：**
```bash
open setup.html  # macOS
start setup.html  # Windows
xdg-open setup.html  # Linux
```
ダウンロード/保存ダイアログでsetup.htmlを開きます。

### 2. 設定の構成

- **エージェント言語**: 生成ファイルの言語を選択（EN/JA/IDコア、プラグイン用に15以上の拡張）
- **ファイルタイプ**: AGENTS.md（標準）、GEMINI.md（Gemini）、CLAUDE.md（Claude）
- **ルール選択**: 必要なAI動作を有効化

### 3. ファイルの生成

「設定ファイルを生成」をクリックして作成：
- ルート `AGENTS.md`/`GEMINI.md`/`CLAUDE.md`
- サブディレクトリのルール固有ファイル
- 有効化された各ルールの `settings.json` ファイル

### 4. 保存方法

#### 💾 保存（推奨）
- ネイティブファイル保存ダイアログを開く
- 正確な保存場所を選択
- ドキュメントフォルダから開始
- モダンブラウザ: 完全ファイルシステムAPI
- レガシーブラウザ: ダウンロードにフォールバック

#### 📥 ダウンロード
- 直接ダウンロードフォルダにダウンロード
- 従来のブラウザダウンロード動作
- 手動ファイル配置が必要

#### 📋 コピー
- コンテンツをクリップボードにコピー
- 手動貼り付けと保存
- ファイル命名/場所の完全制御

#### 📁 作成（拡張モードのみ）
- サーバー上の直接ファイル作成
- 自動ファイル配置
- ユーザーダイアログ不要
- `python setup-launcher.py` モードでのみ利用可能

## 🔧 技術アーキテクチャ

### ファイル構造
```
agentic-rules/
├── setup.html              # メインWebインターフェース
├── setup.py               # CLIセットアップスクリプト
├── setup-launcher.py      # 拡張サーバーランチャー
├── localization.json      # UI翻訳
├── bootstrap.json         # フレームワーク設定
├── CORE-RULES.md         # フレームワーク概要
└── [rule-name]/          # ルールディレクトリ
    ├── RULES.md.*        # ルールテンプレート (EN/JA/IDコア言語)
    ├── settings.json     # デフォルト設定
    └── setup.json       # ルール設定
```

### ルール統合プロセス

1. **Bootstrap読み込み**: `bootstrap.json`がフレームワーク構造を定義
2. **ルール有効化**: ユーザーが有効化するルールを選択
3. **テンプレート処理**: ルールテンプレートをローカライズして処理
4. **ファイル生成**: エージェント固有の設定ファイルを作成
5. **エージェント統合**: エージェント読み込みのためにプロジェクトにファイルを配置

## 🛠️ APIリファレンス

### setup-launcher.py

**コマンドラインオプション:**
```bash
python setup-launcher.py [OPTIONS]

Options:
  --port PORT    サーバー実行ポート (デフォルト: 8000)
  --web         基本モードで起動 (ダウンロードダイアログ)
  --help        ヘルプメッセージを表示
```

**サーバーエンドポイント (拡張モード):**
- `GET /` - 静的ファイルを提供
- `POST /api/create-file` - 直接ファイルを作成
- `POST /api/cleanup-files` - 競合ファイルを削除
- `POST /api/shutdown` - サーバーを正常にシャットダウン

### setup.py

**コマンドラインオプション:**
```bash
python setup.py [OPTIONS]

Options:
  --ui-lang {en,ja,id}        インターフェース言語 (en, ja, id)
  --agent-lang {en,ja,id}     エージェントテンプレート言語 (en, ja, id)
  --agent-file-type {AGENTS.md,GEMINI.md,CLAUDE.md}
                               生成するエージェントファイルタイプ
  --lang {en,ja,id}           UIとエージェント言語の両方を設定 (en, ja, id)
  --rules RULES               有効化するルールのコンマ区切りリスト、または "all"
  --help                      ヘルプメッセージを表示
```

**注意:** `setup.py`は現在コア3言語をサポート。18以上の言語の完全サポートには、Webインターフェース（`setup.html`）またはスキャフォールドジェネレーター（`generate_plugin_scaffold.py`）を使用してください。

## 🔌 統合例

### Cursor統合
```javascript
// Cursor設定で
{
  "agentic-rules": {
    "enabled": true,
    "rules": ["memory", "rag"],
    "language": "en"
  }
}
```

### VSCode拡張
```json
// settings.json
{
  "agenticRules.enabled": true,
  "agenticRules.rules": ["memory", "critical-thinking"],
  "agenticRules.fileType": "AGENTS.md"
}
```

### カスタムエージェント統合
```python
# エージェントルールを読み込み
import json

# Bootstrap設定を読み込み
with open('bootstrap.json', 'r') as f:
    bootstrap = json.load(f)

# 有効化されたルールを読み込み
enabled_rules = ['memory-rules', 'rag-rules']
for rule in enabled_rules:
    rule_file = f"{rule}/AGENTS.md"
    settings_file = f"{rule}/settings.json"

    # ルール設定を読み込んで適用
    with open(rule_file, 'r') as f:
        rule_content = f.read()

    with open(settings_file, 'r') as f:
        rule_settings = json.load(f)
```

## 🔍 デバッグとトラブルシューティング

### サーバーが起動しない
```bash
# ポートが利用可能か確認
lsof -i :8000

# 別のポートを試す
python setup-launcher.py --port 8081
```

### ファイルが生成されない
```bash
# ファイル権限を確認
ls -la setup.html setup.py

# Pythonインストールを確認
python --version
python -c "import json; print('JSON working')"
```

### ブラウザの問題
```bash
# ブラウザキャッシュをクリア
# シークレット/プライベートモードを試す
# エラーの場合はブラウザコンソールを確認
```

### ルール競合
- 各エージェントファイルタイプ（AGENTS.md/GEMINI.md/CLAUDE.md）は相互排他的
- 拡張モードは自動的に競合ファイルをクリーンアップ
- 基本モードでは手動クリーンアップが必要になる場合あり

## 🚀 高度な使用法

### カスタムルール開発
- [拡張マニュアル](EXTENSION-MANUAL.md)を参照
- 新しいルールディレクトリを作成
- settings.jsonとテンプレートファイルを定義
- bootstrap.json設定に追加

### 自動デプロイメント
```bash
#!/bin/bash
# 自動セットアップスクリプト
python setup-launcher.py --port 9000 &
sleep 2
curl -X POST http://localhost:9000/api/shutdown
```

### CI/CD統合
```yaml
# GitHub Actions例
- name: Setup Agentic Rules
  run: |
    python setup.py --lang en --rules memory,rag --file-type AGENTS.md
    cp -r generated-files/* ./ai-project/
```

## 📊 パフォーマンス考慮事項

### メモリ使用量
- ルールテンプレートは生成中にメモリに読み込まれる
- 大規模ルールセットはより多くのRAMを必要とする場合あり
- ユースケースに基づいてルール選択を検討

### ファイルシステム操作
- 拡張モードは直接ファイル書き込みを実行
- ターゲットディレクトリの適切な権限を確保
- バックアップファイルは自動的に作成される

### ブラウザ互換性
- モダンブラウザ: 完全File System APIサポート
- レガシーブラウザ: ダウンロードダイアログにフォールバック
- モバイルブラウザ: 機能制限あり

## 🔐 セキュリティノート

- `setup.html`使用時はフレームワークはクライアントサイドで実行
- 拡張モードはローカルサーバーを必要（ユーザー信頼が必要）
- データは外部に送信されない
- すべてのファイル操作はユーザーシステムにローカル

## 📞 サポートと貢献

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: フレームワーク設計と実装
- **Contributing**: 貢献ガイドラインについてはメインREADMEを参照

---

**🔧 上級ユーザー**: このフレームワークは、あらゆるエージェントシステムに構造化されたAI動作を統合するための最大限の柔軟性を提供します。

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. MIT Licenseの下でライセンスされています（LICENSEファイルを参照してください）。