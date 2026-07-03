# 時間対応ナレッジグラフ — 導入前後の比較

> KG実装ガイドの[時間対応（バイテンポラル）ナレッジモデル](KG_IMPLEMENTATION_GUIDE.ja.md)
> セクションの補足ドキュメントです。本ドキュメントは、従来型（非時間対応）のKGと
> v1.5.0の時間対応モデルとの*振る舞い*の違いを、再現可能なA/Bテストと
> 実運用環境での検証によって示します。

## なぜこのドキュメントがあるのか

事実を*追加する*だけのKGは、やがて古くなった知識をその置き換え先より上位に
ランク付けしてしまいます。動機となった実際の障害はこうです：古くなった高優先度の
ルールノードが検索結果に浮上し続け、唯一の対処法はその内容を手作業で
「SUPERSEDED」と書き換え、優先度を手動で下げることでした — ランキングを回避する
ために履歴を書き換えていたのです。時間対応モデルはこれをデータ層で解決します。

## A/Bテスト

両サーバーには、それぞれの公開ツールを通じて、当該インシデントとまったく同じ形の
データを同一に投入しました：

- 優先度9の**古い事実** — `"The deploy target is ALPHA (set up in January)."`
- 優先度7の**その置き換え** — `"The deploy target is BETA since June — alpha was decommissioned."`
- 置き換えから古い事実への `supersedes` エッジ

その後、同じクエリを両方に対して実行しました。

### A — 従来型KG（導入前）

```
## Results for "… deploy target" (2 matches)

[fact:stale-example] (p:9, scope:project:compare)      ← STALE FACT RANKS FIRST
The deploy target is ALPHA (set up in January).

[fact:current-example] (p:7, scope:project:compare)
The deploy target is BETA since June — alpha was decommissioned.
-> supersedes: stale-example                            (edge exists but is ignored)
```

置き換え済みの事実が浮上するだけでなく、その高い優先度によって自身の置き換え先
**より上位**にランクされます。最上位の結果を信頼するエージェントは、古い知識に
基づいて行動してしまいます。

### B — 時間対応KG（導入後）

```
## Results for "… deploy target" (1 matches)

[fact:current-example] (p:7, scope:project:compare)     ← ONLY CURRENT KNOWLEDGE
The deploy target is BETA since June — alpha was decommissioned.
-> supersedes: stale-example [invalidated 2026-07-03]
```

古い事実はデフォルトの表示から隠され、`supersedes` エッジは、隠されたコンテンツを
再注入する代わりに注釈付きのポインタとして表示されます。

### B — 履歴は照会可能なまま（非破壊）

```
kg_query("… deploy target", include_expired=True)

[fact:stale-example] (p:9) [SUPERSEDED by current-example]
The deploy target is ALPHA (set up in January).

[fact:current-example] (p:7)
The deploy target is BETA since June — alpha was decommissioned.
```

```
kg_get_node("stale-example")

Status: superseded by current-example at 2026-07-03T21:42Z
Valid: 2026-07-03T21:42Z → 2026-07-03T21:42Z
Supersession chain: stale-example -> current-example (newest last)
```

何も削除されていません。古い事実は完全な内容を保持したまま、有効期間を持ち、
自身の後継を指し示します。

## 実運用環境での検証

時間対応モデルは、MCP経由で提供されている長期運用中の個人用KG（数百ノード規模）
に対して検証されました：

| チェック | 結果 |
|---------|------|
| インプレース移行（純粋な `ADD COLUMN`）：ノード／エッジ／埋め込みの件数は変化なし、全行に `valid_at = created_at` をバックフィル | ✅ |
| かつて手作業で優先度を下げた実際のノードを、1本の `supersedes` リンクで修復：デフォルトの検索から隠され、代わりに置き換え先が浮上 | ✅ |
| そのノードへの `kg_get_node` が、有効期間と supersession チェーン付きで `Status: superseded by … at …` を報告 | ✅ |
| タイムトラベル：`as_of` を旧有効期間内の日付に設定すると、そのノードを当時有効だったものとして返し、後継（当時はまだ有効でない）を隠す | ✅ |
| 後方互換性：時間対応化以前のすべてのツールシグネチャが変更なしで動作 | ✅ |

## 機能比較

| 機能 | 従来型KG | 時間対応KG（v1.5.0） |
|------|---------|---------------------|
| デフォルト結果内の古い知識 | 浮上する。置き換え先より上位になり得る | supersession 時に自動的に隠される |
| 事実の置き換え | 旧テキストの手編集＋優先度の手動降格（履歴の書き換え） | `kg_add(…, supersedes=old)` — 1回のアトミックな呼び出し |
| 「日付Xの時点で何を知っていたか？」 | 回答不能 | クエリ／コンテキストに `as_of=<ISO date>` を指定 |
| 履歴 | 手作業のテキスト規約のみ | 非破壊：`include_expired`、`[SUPERSEDED by …]` マーカー、supersession チェーン |
| 置き換えなしで終了する事実 | 削除または手編集 | `kg_retire`（invalid / expired / restore — 可逆） |
| 有効期間 | — | `valid_from` / `valid_until`（遡及的な事実にも対応） |
| 矛盾 | エッジ型は存在するが機能しない | どちらの側も隠さずに記録。解決は助言として提示 |
| 書き込み時の近似重複検出 | — | 埋め込みKNNによる助言が supersede／contradict を提案 |
| ランキングにおける鮮度 | — | 緩やかな新しさブースト（半減期90日、同点の判定のみ） |

## この比較を支えるテストカバレッジ

- **59チェックのローカルスイート**（実データベースのスクラッチコピーに対して実行）：
  冪等なインプレース移行、FTS／ベクタの rowid 整合、混在するタイムスタンプ形式の
  解析、旧シグネチャ互換性、アトミックな supersession、as-of の期間計算（5ケース）、
  retire／restore の往復、矛盾のセマンティクス、遡及的および将来の有効期間、
  上限付きの新しさブースト、そしてコンテキスト展開のゲート（`supersedes` エッジが
  隠されたコンテンツを再注入してはならない）。
- **6アサーションのA/Bハーネス**：従来型ベースライン（バージョン管理から取り出した
  以前のサーバー）が古い事実のインシデントを再現し、時間対応サーバーが履歴を
  失わずにそれを修正する。
- フレームワークのゲート：プラグイン静的スイートと `validate.py` はすべてグリーン。

## トレードオフ

履歴は蓄積されます — 何も削除されません（個人／プロジェクト規模では無視できる
程度です。グラフが非常に大きくなった場合は superseded なチェーンをアーカイブして
ください）。エージェントは*編集ではなく supersede*の原則に従う必要があります。
v1.5.0のルールと Claude Code の活性化プリアンブルがまさにそれを教えます。
[時間対応モデルを使うべき（使うべきでない）場面](KG_IMPLEMENTATION_GUIDE.ja.md)を参照してください。
