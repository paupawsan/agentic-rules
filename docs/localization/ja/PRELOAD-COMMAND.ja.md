# 📥 Preload Agentic Rules コマンド

**Preload Agentic Rules** コマンドを使用すると、指定されたディレクトリからシステムルールと設定をエージェントの操作コンテキストに手動で読み込むことができます。

## 🎯 目的

このコマンドは次の場合に役立ちます：
- Cursorがネストされたエージェントルールを自動検出しない場合
- 別のディレクトリ位置からルールを読み込む必要がある場合
- 特定のシステム設定を明示的に読み込みたい場合
- エージェントが別のプロジェクトのフレームワークやルールセットを理解する必要がある場合

## 📋 コマンド構文

```
/agentic-rules/preload-agentic-rules [TARGET_DIRECTORY]
```

### パラメータ

- **`TARGET_DIRECTORY`** (オプション): システムルールファイルを含むディレクトリへのパス
  - 絶対パス: `/Users/username/Projects/my-agent-rules`
  - 相対パス: `../my-agent-rules` または `./subfolder/rules`
  - 省略した場合、コマンドは対話的にプロンプトを表示します

## 💡 使用例

### 例1: 絶対パスから読み込む
```bash
/agentic-rules/preload-agentic-rules /Users/yourname/projects/agentic-rules
```

### 例2: 相対パスから読み込む
```bash
# 現在のワークスペースに対する相対パス
/agentic-rules/preload-agentic-rules ../my-agent-rules

# 現在のディレクトリに対する相対パス
/agentic-rules/preload-agentic-rules ./config/rules
```

### 例3: 対話モード
```bash
# 引数なしで実行 - ディレクトリの入力を求めます
/agentic-rules/preload-agentic-rules
```

## 🔍 どのファイルが読み込まれるか？

コマンドは自動的に次のシステムルールファイルを検索して読み込みます：

- **`AGENTS.md`** - 汎用エージェント設定および動作ルール
- **`GEMINI.md`** - Google Gemini固有のシステム設定
- **`CLAUDE.md`** - Anthropic Claude固有のシステム設定

コマンドはターゲットディレクトリとすべてのサブディレクトリを再帰的に検索し、バックアップファイル（`.backup`で終わるファイル）を除外します。

## ✅ 期待される出力

ファイルが見つかった場合：
```
Scanning for system files in: /path/to/directory
Found 3 system file(s):
  - AGENTS.md
  - modules/memory-rules/AGENTS.md
  - modules/rag-rules/AGENTS.md

Loading system files...

=== LOADING: AGENTS.md ===
[ファイルの内容がここに表示されます]
--- END OF AGENTS.md ---

🎉 System loading complete!
System has been loaded from: /path/to/directory
```

ファイルが見つからなかった場合：
```
Scanning for system files in: /path/to/directory
No system files found in /path/to/directory

System directories typically contain:
- Agent configuration and behavior files
- Model-specific system configurations
- README.md or documentation files
- Configuration files (.json)
- Rule definition files (.md)
- System specification documents

🎉 System scan complete!
System has been scanned from: /path/to/directory
No system files were found to load.
```

## 🛡️ セキュリティ機能

- **明示的なユーザー操作が必要**: 明示的に要求された場合のみ読み込みます
- **自動読み込みなし**: ファイルを自動的に読み込んだり処理したりすることはありません
- **バックアップファイル保護**: `.backup`ファイルを自動的に除外します
- **ディレクトリ検証**: スキャン前にディレクトリの存在を確認します
- **読み取り専用操作**: ファイルを読み取るだけで、変更することはありません

## 📝 要件

- ターゲットディレクトリが存在する必要があります
- システムファイルは正確に命名する必要があります: `AGENTS.md`、`GEMINI.md`、または `CLAUDE.md`
- エージェントは指定されたディレクトリへの読み取りアクセス権が必要です
- ユーザーは明示的にコマンドを実行する必要があります

## 🔧 トラブルシューティング

### 問題: "Directory does not exist"
**解決策**: パスが正しいことを確認してください。相対パスが機能しない場合は絶対パスを使用してください。

### 問題: "No system files found"
**考えられる原因**:
- ファイルが正しく命名されていない（`AGENTS.md`、`GEMINI.md`、または`CLAUDE.md`である必要があります）
- ファイルがスキャンされなかったサブディレクトリにある
- ファイルに`.backup`拡張子がある

**解決策**: 
- ファイル名が正確に一致することを確認してください
- ファイルがターゲットディレクトリに存在することを確認してください
- 必要に応じて`.backup`拡張子を削除してください

### 問題: ファイルが見つかったが読み込まれない
**解決策**: 
- ファイルの権限を確認してください（エージェントは読み取りアクセス権が必要です）
- ファイルに有効なコンテンツが含まれていることを確認してください
- コマンドを再度実行してみてください

## 🔗 関連ドキュメント

- **[トラブルシューティングガイド](TROUBLESHOOTING.ja.md)** - 一般的な問題と手動読み込み手順
- **[ユーザーガイド](USER-GUIDE.ja.md)** - フレームワークのセットアップと使用方法の完全ガイド
- **[開発者ガイド](DEVELOPER-GUIDE.ja.md)** - 高度な設定と自動化

## 📚 ベストプラクティス

1. **絶対パスを使用**: 特に異なるディレクトリ間で作業する場合、相対パスよりも信頼性が高いです
2. **ルールを整理**: 管理を容易にするために、すべてのルールファイルを専用のディレクトリに保持します
3. **バージョン管理**: 一貫性を保つために、バージョン管理でルールファイルを追跡します
4. **読み込み後にテスト**: テスト質問をすることで、エージェントが読み込まれたルールを理解していることを確認します

---

**注**: このコマンドはAgentic Rules Frameworkとシームレスに連携するように設計されています。読み込み後、エージェントは読み込まれたシステムルールに従って理解し、動作します。

<!-- LICENSE: Copyright (c) 2025-2026 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->
