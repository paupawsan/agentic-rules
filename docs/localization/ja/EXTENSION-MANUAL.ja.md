# フレームワーク拡張マニュアル (日本語)

このマニュアルでは、新しいルールでエージェントルールフレームワークを拡張するための包括的なガイドを提供します。フレームワークには、迅速な開発のための自動プラグインスキャフォールディングツールが含まれています。

## クイックスタート: 自動プラグイン作成

**🎯 推奨アプローチ**: 即時プラグイン作成のために自動スキャフォールドジェネレーターを使用！

### オプション1: インタラクティブプラグイン作成
```bash
python generate_plugin_scaffold.py
```
**機能:**
- ガイド付きウィザードインターフェース
- 自動ファイル生成
- 多言語サポート
- `plugins.json`でのプラグイン登録

### オプション2: コマンドラインプラグイン作成
```bash
# ゼロから作成
python generate_plugin_scaffold.py --name my-plugin --description "My awesome plugin"

# 既存プラグインテンプレートから作成（説明不要）
python generate_plugin_scaffold.py --template memory-rules --name my-memory-plugin

# 多言語プラグイン（説明必須）
python generate_plugin_scaffold.py --name my-plugin --description "Multi-language plugin example" --langs en,ja,id,zh

# 高度: デフォルトで無効化
python generate_plugin_scaffold.py --name experimental-plugin --no-enable --description "Experimental features"
```

### スキャフォールドジェネレーターが作成するもの
```
my-plugin/
├── README.md              # 包括的なプラグインドキュメント
├── RULES.md.en           # 安全フレームワーク付き英語ルールアルゴリズム
├── RULES.md.ja           # 日本語ローカライズテンプレート（リクエスト時）
├── RULES.md.id           # インドネシア語ローカライズテンプレート（リクエスト時）
├── RULES.md.zh           # 中国語ローカライズテンプレート（リクエスト時）
├── settings.json         # 適切なデフォルト付き完全設定
├── setup.json           # ローカライズ付きWebインターフェース設定
└── [plugins.jsonに自動登録されるプラグイン]
```

**✅ 利点:**
- ⚡ **即時**: 数秒で完全プラグイン
- 🎯 **フレームワーク対応**: すべての統合ポイントが設定済み
- 🌍 **多言語**: リクエストされたすべての言語のテンプレート
- 🔧 **Web統合**: setup.htmlに自動表示
- 📚 **文書化**: 使用例とトラブルシューティングを含む
- 🛡️ **安全**: 安全対策と検証を含む

**🔄 高度なローカライズのため:**
スキャフォールド生成後、基本テンプレートを超えたカスタムローカライズ文字列が必要な場合：
```bash
# カスタム文字列でlocalization.jsonを編集
# 次にsetup.htmlを自動更新
python update_localization.py
```

---

## 手動プラグイン開発（高度）

フルコントロールが必要な上級ユーザー、またはフレームワーク内部を理解したい場合、これらの手動ステップに従ってください。RAGルールの追加を例として使用します。

## プラグイン検出メカニズムの理解

### CLI vs Webインターフェース検出

フレームワークには**2つの異なるプラグイン検出メカニズム**があります：

#### CLI (`setup.py`) - 動的検出
- **自動**: `-rules`で終わるディレクトリをスキャン
- **リアルタイム**: `RULES.md.*`ファイルを確認してプラグインを検索
- **柔軟**: 任意の言語に対応、フォールバックをサポート
- **登録不要**: ディレクトリとファイルを作成するだけ

#### Web (`setup.html`) - 静的マニフェスト
- **マニフェストベース**: `plugins.json`ファイルから読み取り
- **プリコンパイル**: `generate_simple_setup.py`を使用して設定を埋め込み
- **構造化**: 各プラグインに`setup.json`ファイルが必要
- **登録必須**: `plugins.json`に追加してジェネレーターを実行

### なぜ2つのシステムか？
- **CLI**: 即時プラグイン検出が必要な開発者とパワーユーザー向け
- **Web**: シンプルなダブルクリック体験が必要なエンドユーザー向け
- **両方**: すべての使用シナリオで完全互換性を確保

## Bootstrap構造の理解

拡張前に、bootstrapコンポーネントを理解してください：

```json
{
  "entry_points": {
    "global_config": "settings/global-settings.json",
    "rag_config": "rag-rules/settings.json",        // 高優先度: 最初に読み込み
    "memory_config": "memory-rules/settings.json",   // 中優先度: 2番目に読み込み
    // 新しいルール設定をここに追加
    "critical_thinking_config": "critical-thinking-rules/settings.json"  // 高優先度
  },
  "loading_sequence": [
    // 優先度ベース読み込み順序（ステップ番号が低い = 高優先度）
    // 1. ユーザー同意とグローバル設定（常に最初）
    // 2. 高優先度ルール（コンテキスト最適化のためのRAG）
    // 3. 中優先度ルール（RAGで強化されたメモリ）
    // 4. 高優先度ルール（検証のためのCritical Thinking）
  ],
  "rule_interconnections": {
    // ルールが相互に通信する方法
  },
  "platform_adapters": {
    // プラットフォーム固有設定
  },
  "framework_validation": {
    // ファイル検証要件
  }
}
```

## ステップバイステップ: RAGルールの追加（使用例）

### ステップ1: ルールディレクトリ構造を作成
```bash
mkdir -p rag-rules
```

### ステップ2: ルールアルゴリズム仕様を作成
サポートされるすべての言語でルールアルゴリズムファイルを作成：

**メインアルゴリズムファイル:** [`../rag-rules/RAG-RULES.md`](../rag-rules/RAG-RULES.md) (英語 - 主要参照)

**ローカライズルールファイル:**
- [`rag-rules/RULES.md.en`](../rag-rules/RULES.md.en) - 英語版（RAG-RULES.mdと同一）
- [`rag-rules/RULES.md.ja`](../rag-rules/RULES.md.ja) - 日本語版
- [`rag-rules/RULES.md.id`](../rag-rules/RULES.md.id) - インドネシア語版

### ステップ3: 設定ファイルを作成

### ステップ4: 統合を更新

### ステップ5: テストと検証

## 高度な拡張トピック

### ルール相互接続

### プラットフォーム適応

### テストと検証

---

**🔧 拡張開発者**: このフレームワークは、新しいAI動作でエージェントシステムを強化するための完全な柔軟性を提供します。

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. MIT Licenseの下でライセンスされています（LICENSEファイルを参照してください）。