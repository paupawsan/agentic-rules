# {{display_name}}

{{description}}

## 概要

これはAgentic Rules Framework用のカスタムプラグインで、{{plugin_name_kebab}}機能をAIエージェントに提供します。

## 機能

- **アルゴリズム実装**: {{plugin_name_kebab}}操作のための構造化されたアルゴリズムを提供
- **構成管理**: `settings.json`経由の柔軟な設定
- **多言語対応**: 複数の言語でテンプレートが利用可能
- **フレームワーク統合**: Agentic Rules Frameworkとのシームレスな統合

## インストール

1. このプラグインディレクトリをagentic-rules Frameworkにコピー
2. プラグイン名を`plugins.json`に追加（オプション、Webインターフェース用）
3. Web構成を更新するために`python generate_simple_setup.py`を実行
4. `python setup.py`でプラグインを有効化

## 構成

### 基本設定（`settings.json`）

```json
{
  "{{plugin_key}}": {
    "enabled": true,
    "config": {
      "example_setting": "example_value",
      "max_entries": 100,
      "cleanup_days": 90
    },
    "advanced": {
      "debug_mode": false,
      "performance_mode": "balanced"
    }
  }
}
```

### 設定説明

- `enabled`: プラグインの有効化/無効化
- `config.max_entries`: 管理するエントリの最大数
- `config.cleanup_days`: クリーンアップ前のデータ保存日数
- `advanced.debug_mode`: デバッグログの有効化
- `advanced.performance_mode`: パフォーマンス最適化モード

## 使用方法

1. **プラグイン有効化**: `settings.json`で`enabled: true`を設定
2. **ルール有効化**: `python setup.py`を使用してルールデータを生成
3. **統合**: 生成されたルールデータ（例: `AGENTS.md`）をプロジェクトにコピー
4. **構成**: `{{plugin_name}}/settings.json`の設定を調整

## ルールアルゴリズム

このプラグインは以下のアルゴリズムを実装します：

### {{pascal_case_name}}初期化プロセス
- {{plugin_name_kebab}}システムを初期化
- 構成を検証
- 必要なデータ構造を設定

### {{pascal_case_name}}メインプロセス
- ユーザーインタラクションを処理
- {{plugin_name_kebab}}ロジックを適用
- 処理された結果を返す

### {{pascal_case_name}}クリーンアッププロセス
- 定期的なクリーンアップを実行
- ユーザー同意を要求
- データの整合性を維持

## ファイル構造

```
{{plugin_name}}/
├── README.md              # このドキュメント
├── RULES.md.en           # 英語版ルールテンプレート
├── RULES.md.ja           # 日本語テンプレート（要求された場合）
├── RULES.md.id           # インドネシア語テンプレート（要求された場合）
├── settings.json         # デフォルト設定
└── setup.json           # Webインターフェース構成
```

## 開発

### 新しい言語の追加

1. 翻訳されたテンプレートで`RULES.md.{{language_code}}`を作成
2. `setup.json`にローカライズを追加
3. 必要に応じて`settings.json`を更新

### アルゴリズムのカスタマイズ

アルゴリズムと動作を変更するには、`RULES.md.*`ファイルを編集してください。

### テスト

1. 設定でプラグインを有効化
2. `setup.py`を実行してルールデータを生成
3. 生成されたルールをAIエージェントでテスト

## トラブルシューティング

### プラグインが認識されない
- プラグインディレクトリが存在することを確認
- 少なくとも1つの`RULES.md.*`ファイルが存在することを確認
- Webインターフェース用の`plugins.json`にプラグイン名が含まれていることを確認

### 構成エラー
- `settings.json`の構文を確認
- 必要な設定がすべて存在することを確認
- ファイル権限が正しいことを確認

### ルール有効化が失敗
- プラグインが設定で有効化されていることを確認
- `setup.py`が正常に完了したことを確認
- 生成されたルールデータが正しくコピーされたことを確認

## ライセンス

Copyright (c) {{current_year}} {{author_name}}

MITライセンスの下でライセンスされています。詳細についてはLICENSEファイルを参照してください。

## 貢献

貢献を歓迎します！お願い：

1. リポジトリをフォーク
2. 機能ブランチを作成
3. 変更を加える
4. 徹底的にテスト
5. プルリクエストを提出

大きな変更の場合は、まず提案された変更を議論するためにIssueを開いてください。
