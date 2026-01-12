# Cursor 2.0マルチエージェント統合ガイド

## 概要

このガイドでは、Orchestratorとサブエージェント設定を含む、Cursor 2.0のマルチエージェントシステムでAgentic Rules Frameworkを使用する方法を説明します。

## 前提条件

### Cursor 2.0の設定

1. **Nightlyチャネルを有効化**:
   - `Cursor Settings` > `Beta`に移動
   - Update Channelを`Nightly`に設定
   - Cursorを再起動

2. **Agentモードを有効化**:
   - Composerを開く（`Cmd + I`または`Ctrl + I`）
   - **Agent**モードに切り替え（「Chat」だけでなく）

3. **フレームワークの初期化**:
   - Agentic Rules Frameworkが初期化されていることを確認
   - `.agentic_initialized`マーカーが存在することを確認
   - `bootstrap.json`でフレームワーク設定を確認

## アーキテクチャ

### マルチエージェント構造

```
Orchestrator Agent（プライマリ）
├── Memory Specialist Agent
├── RAG Specialist Agent
├── Critical Thinking Specialist Agent
├── Documentation Specialist Agent
└── Testing Specialist Agent
```

### フレームワーク統合

- **Orchestrator**: フレームワークルールを使用してサブエージェントを調整
- **サブエージェント**: 特定のフレームワークモジュールを使用する専門エージェント
- **ルールベースの調整**: オーケストレーションに`bootstrap.json`を使用
- **メモリ共有**: サブエージェントがMemory Rulesを通じてコンテキストを共有
- **品質保証**: Critical Thinking Rulesがすべての出力を検証

## エージェント設定

### setup.htmlによる自動生成

**すべてのエージェント設定は`setup.html`によって自動生成されます**。ユーザーが手動でファイルを作成する必要はありません。

#### セットアッププロセス

1. **setup.htmlを開く**: ブラウザで`setup.html`を開く
2. **デプロイターゲットを選択**: 「Cursor 2.0 Multi-Agent」を選択
3. **言語を選択**: エージェントの言語を選択（英語、インドネシア語、または日本語）
4. **ルールを選択**: 有効にするフレームワークモジュールを選択
5. **ファイルを生成**: 「設定ファイルを生成」をクリック
6. **プロジェクトにコピー**: 生成された`.cursor/agents/*.md`ファイルをプロジェクトの`.cursor/agents/`ディレクトリにコピー

#### 生成されるファイル

生成後、以下のファイルが作成されます：

```
.cursor/agents/
├── orchestrator.md              # プライマリOrchestrator
├── memory-agent.md              # メモリ操作スペシャリスト
├── rag-agent.md                 # 情報取得スペシャリスト
├── critical-thinking-agent.md   # 品質保証スペシャリスト
├── docs-agent.md                # ドキュメントスペシャリスト
├── test-agent.md                # テストスペシャリスト
└── README.md                    # クイックスタートガイド
```

**注意**: これらのファイルは**gitにコミットされません**（既に`.gitignore`に含まれています）。各ユーザーが自分のプロジェクト用に生成します。

### エージェントの役割

#### Orchestrator Agent
- **目的**: タスク分解とサブエージェント調整
- **フレームワーク**: 調整のためにすべてのフレームワークモジュールを使用
- **委任**: 専門サブエージェントにタスクを割り当て
- **統合**: サブエージェントの出力を結合

#### Memory Specialist Agent
- **目的**: コンテキスト取得と知識の永続化
- **フレームワークモジュール**: Memory Rules
- **機能**: メモリストレージ、取得、ナレッジグラフ統合

#### RAG Specialist Agent
- **目的**: 情報取得とコンテキスト最適化
- **フレームワークモジュール**: RAG Rules
- **機能**: セマンティック検索、コンテキスト最適化、ナレッジグラフクエリ

#### Critical Thinking Specialist Agent
- **目的**: 品質保証と検証
- **フレームワークモジュール**: Critical Thinking Rules
- **機能**: エラー検出、仮定チャレンジ、検証

#### Documentation Specialist Agent
- **目的**: ドキュメント生成とメンテナンス
- **フレームワークモジュール**: すべてのルール（強化されたドキュメント）
- **機能**: コードドキュメント、アーキテクチャドキュメント、ユーザーガイド

#### Testing Specialist Agent
- **目的**: テスト作成と品質検証
- **フレームワークモジュール**: Critical Thinking Rules、Memory Rules
- **機能**: ユニットテスト、統合テスト、カバレッジ分析

## 使用パターン

### 基本オーケストレーション

1. **Composerを開く**: `Cmd + I`（Mac）または`Ctrl + I`（Windows/Linux）を押す
2. **Agentモードを有効化**: Agentモードに切り替え
3. **計画モードを使用**: 技術計画のために`Shift + Tab`を押す
4. **グローバルコンテキスト**: 完全なプロジェクト理解のために`@Codebase`を使用
5. **タスクを委任**: Orchestratorが自動的にサブエージェントに委任

### 並列実行

Cursor 2.0は並列エージェント実行にGit Worktreesを使用します：

1. **並列タスクを起動**: Orchestratorが独立したタスクを委任
2. **Worktree作成**: Cursorが自動的にworktreeを作成
3. **進捗を監視**: `git worktree list`でworktreeを確認
4. **変更を適用**: UIの「Apply」ボタンを使用して結果をマージ

### Best-of-N戦略

重要なタスクには、複数のモデルを使用します：

1. **複数のモデルを選択**: モデルセレクターで2-3つのモデルを選択
2. **プロンプトを送信**: 1つのプロンプトが並列エージェントを起動
3. **結果を比較**: エージェント「タブ」間で切り替え
4. **最良を選択**: 最もエレガントなソリューションを選択
5. **適用**: 選択したソリューションをマージ

## フレームワーク調整

### ルールベースの委任

Orchestratorは委任にフレームワークルールを使用します：

- **メモリタスク**: コンテキスト取得が必要な場合、Memory Specialistに委任
- **情報タスク**: 複雑な検索のためにRAG Specialistに委任
- **品質タスク**: 検証のためにCritical Thinking Specialistに委任
- **ドキュメントタスク**: Documentation Specialistに委任
- **テストタスク**: Testing Specialistに委任

## 参照

- **フレームワークドキュメント**: `docs/CORE-RULES.md`
- **ブートストラップガイド**: `Bootstrap.md`
- **エージェント設定ジェネレーター**: `setup.html` (`.cursor/agents/*.md`ファイルを生成)
- **アダプター設定**: `settings/cursor-2.0-multi-agent-adapter.json`
- **ブートストラップ設定**: `bootstrap.json`

**注意**: エージェント設定ファイル（`.cursor/agents/*.md`）は`setup.html`によって自動生成されます。ユーザーは手動で作成するのではなく、インストーラーを使用して生成する必要があります。

---

**フレームワークバージョン**: 1.3.0  
**Cursorバージョン**: 2.0+  
**統合モデル**: distributed_per_rule  
**最終更新**: 2026-01-12
