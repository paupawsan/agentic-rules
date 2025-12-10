# 設定構成

## 概要

設定は、agenticルールの有効化と動作を制御します。各ルールカテゴリに独自の設定ファイルがあり、グローバル設定ファイルが全体的な動作を調整します。

## 構成階層

```
global-settings.json (メインコントロール)
├── memory-rules/settings.json
├── critical-thinking-rules/settings.json
└── rag-rules/settings.json
```

## グローバル設定

### ルールカテゴリ
- **memory_rules**: 永続的な理解ストレージを制御
- **critical_thinking_rules**: 検証と推論動作を管理
- **rag_rules**: 情報処理最適化を処理

### プラットフォームサポート
- **cursor_support**: Cursor IDE統合
- **vscode_support**: Visual Studio Code統合
- **ci_systems_support**: CI/CDパイプライン統合
- **custom_platforms**: サードパーティのagenticシステム

## ルール固有の設定

### メモリールール設定
```json
{
  "memory_rules": {
    "enabled": true,
    "storage_path": "./memory",
    "max_entries_per_category": 100,
    "categories": {
      "technical": {"enabled": true},
      "behavioral": {"enabled": true},
      "contextual": {"enabled": true}
    }
  }
}
```

### 批判的思考ルール設定
```json
{
  "critical_thinking_rules": {
    "enabled": true,
    "verification_level": "standard",
    "error_admission": {"enabled": true},
    "ground_check": {"enabled": true}
  }
}
```

### RAGルール設定
```json
{
  "rag_rules": {
    "enabled": true,
    "context_window_optimization": {"enabled": true},
    "hierarchical_reading": {"enabled": true},
    "log_analysis": {"enabled": true}
  }
}
```

## 使用手順

1. **ルールの有効化/無効化**: global-settings.jsonまたは個別のルール設定で`enabled: true/false`を設定
2. **パラメータ調整**: それぞれの設定ファイルの値を変更
3. **プラットフォーム適応**: 関連するプラットフォームサポートフラグを有効化
4. **パフォーマンス監視**: システム能力に基づいて制限を調整

## 安全機能

- **緊急シャットダウン**: 競合が検出された場合に自動的にルールを無効化
- **ユーザー上書き**: 必要に応じて手動制御を許可
- **競合解決**: 優先順位ベースのルール競合処理
- **バックアップ**: 変更前に自動設定バックアップ

## ログ記録

`logging_enabled: true`の場合、すべてのルール適用がログに記録されます。ログには以下が含まれます：
- ルールの有効化/無効化イベント
- パラメータ変更
- パフォーマンス指標
- エラー条件

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. MIT Licenseの下でライセンスされています（LICENSEファイルを参照してください）。