<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="すごいClaude Codeモッド">
</p>

<h1 align="center">すごいClaude Codeモッド</h1>

<p align="center"><b>Claude Codeのモッド、プラグイン、およびそれらが変更するより深い挙動を、証拠に基づいて評価するインデックスです。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-585-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **公開中のインデックス** · 最終同期: `2026-10-13T06:19:35+08:00` (UTC+8)
> · エントリ数: **585** · 最新の更新で追加: **0** · 実装言語: **12**

<sub>以下のすべてのエントリは、自動的に収集、フィルタリング、再確認されたものです。ここに有料掲載はありません。</sub>

<a id="featured"></a>

## 今注目のピックアップ

<sub>カテゴリごとに1件掲載し、根拠評価とスター数で順位付けしています。更新のたびに再計算されます。これはランキングであり、推奨を意味するものではありません。各ピックアップから、下にある完全なカードへリンクしています。スクリーンショットまたは記録を公開しているプロジェクトを優先しているため、ストリップの視認性が保たれます。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9486 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2543 · Python · 👁️ observed</sub>
<sub>Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74439 · TypeScript · 👁️ observed</sub>
<sub>🌊 元祖 agent harness。インテリジェントなマルチプレイヤースウォームをデプロイし、自律ワークフローを調整し、対話型 AI システムを構築します。適応型メモリ、自己学習インテリジェンス、フェデレーション、vector RAG 統合、ネイティブの Claude Code / Codex / Hermes…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## 目次

- [Claude Codeモッドとは](#claude-codeモッドとは)
- [エントリの評価方法](#エントリの評価方法)
- [公式：Anthropic自身のリポジトリとリリースノート](#公式anthropic自身のリポジトリとリリースノート) — **17**
- [Mod：Mod機能で構築されたもの](#modmod機能で構築されたもの) — **451**
- [DSHおよびCordisのプラグインエコシステム](#dshおよびcordisのプラグインエコシステム) — **106**
- [執筆、ディスカッション、動画](#執筆ディスカッション動画) — **11**
- [実装言語別のプロジェクト](#実装言語別のプロジェクト)

## Claude Codeモッドとは

Claude Codeには2.1.287で**mod**が追加されました。プラグインよりも深い動作を変更でき、独自のインターフェースを描画する拡張機能です。

modは`ui.render`にフックしてプロンプトの周囲に**行、バンド、ペイン、カード**を描画し、`$.ui.selection()`で最後に選択したテキストを読み取り、`agent.spawn`でチームメイトを起動し、`Client`の領域を管理できます。描画に失敗したmodは単独で失敗します。`ui.fault`により、壊れたmodがセッション全体を停止させることはありません。

この一覧では、mod、それらが基盤とするプラグインおよびフックの仕組み、さらにDSHとCordisの同等機能を扱います。より広範なClaude Codeエコシステムは意図的に**対象外**です。プロンプトパックはmodではありません。

## エントリの評価方法

この分野の多くの一覧は、掲載対象であることを主張するだけです。この一覧では、実際にどこまで検証できたかを示し、それに応じて絞り込めるようにしています。評価はプロジェクトの品質ではなく証拠の内容を示すものです。まだ誰にも紹介されていない、よく作られたmodでも、やはり`inferred`です。

| 評価                                                                                           | 意味                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Anthropic自身が公開したもの`                                                                  | Anthropic自身が公開したもの、または公式の変更履歴から直接確認したもの。                                                                                                                                    |
| `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの`                       | 独自のテキストでmodの基盤の一部、つまり`ui.render`、`ui.fault`、`agent.spawn`、`$.ui.selection()`、ペイン、バンド、カードについて言及しているため、実際のAPIを対象に構築したものだと作者が説明しています。 |
| `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` | mod、プラグイン、またはフックと名乗っていますが、テキスト内でmodの基盤について具体的に言及していません。実在しますが、未確認です。                                                                         |
| `用語の一致だけで該当したもの`                                                                 | 用語の一致だけで該当したもの。信頼できると判断したからではなく、フィルターの判定を監査可能にするために含めています。                                                                                       |

<a id="official"></a>

## 公式：Anthropic自身のリポジトリとリリースノート

Anthropic自身のClaude Codeリポジトリと、Modのインターフェースを定義したリリース。要約ではなくソースから読み取ったものです。

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150420 · TypeScript · ✅ official · 1 天</summary>

##### 📝 概要

Claude Code は、ターミナル内で動作し、コードベースを理解し、定型タスクの実行、複雑なコードの説明、git ワークフローの処理をすべて自然言語コマンドで行うことで、より速くコーディングできるよう支援するエージェント型コーディングツールです。

<sub>🔧 コード内で使用されていることが確認されています: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | TypeScript                                        |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **150420** |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9486 · TypeScript · ✅ official · 3 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | TypeScript                                        |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **9486**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8255 · Python · ✅ official · 3 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | Python                                            |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **8255**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6354 · Python · ✅ official · 243 天</summary>

##### 📝 概要

Claudeを使用してコード変更を分析し、セキュリティ脆弱性を検出するAI搭載のセキュリティレビューGitHub Action。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | Python                                            |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6354**   |
| 最終プッシュ | 2026-02-11 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1800 · Shell · ✅ official · 3 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | Shell                                             |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1800**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

##### 📝 概要

Claude Model Cardsの補足資料

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **25**     |
| 最終プッシュ | 2025-12-05 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 概要

Claude Modsを追加：プラグインがより深い挙動を変更できるようになりました。「You should know」を追加。サイドエージェントがあなたを見守り、あなたやClaudeが見落とす可能性のある事柄を知らせる組み込みmodです。`/plugin enable cc-plugin-you-should-know@builtin`で有効にします（テレメトリーが有効なファーストパーティセッション向け）

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 概要

Modsに`$.ui.selection()`を追加：全画面モードで最後に選択したテキストを返し、選択範囲が1つのトランスクリプト行内にある場合はその行を返す。Claude Codeの再起動前に描画されたビューでボタンを押すと、別のボタンのアクションが実行されることがあるmodを修正。プラグインまたはmodがプロンプトの上に行を表示している状態でバックグラウンドタスクダイアログを開くと、「unrecoverable interface error」となり全画面セッションが終了する問題を修正。modがリモートで無効になっていると`claude plugin test`が報告する問題を修正。実際には古い保存設定を読み取っていただけでした。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 概要

複合シェルコマンドのネストされた部分に対するdenyまたはaskルールが、管理対象マシンでユーザーインストール済みmodの承認を維持しない問題を修正。アップグレード後の最初のセッションで、インストール済みmodが読み込まれない問題を修正。チームメイト向けに`agent.spawn`を追加し、プラグインhookイベント全体で1つのエージェントIDを使用するとともに、アイドル状態と待機状態を`$.agent.list()`に追加。modの`ui.render` hookが書き込んだ値によって描画時に行が例外を起こすと、セッションが「unrecoverable interface error」で終了する問題を修正。エンジンは独自の行を描画するようになりました。modのペインまたはバンド内の右寄せコンテンツが閉じるマークまたは`\[-\]`の下に描画される問題を修正。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 概要

modの`turn.step`フックの結果に`serverToolUses`を追加：ツールがAPI（アドバイザー）を自ら実行し、各項目のid、name、input、開始時刻、終了時刻を記録。modの`tool.check`フックが読み取る質問と判定に`ceiling`を追加し、ツールに必要な組織の承認名を表示。プラグインフックの型定義に`ThemeKey`と`Color`の型を追加し、エディターでmodの描画に使用できるテーマカラーを一覧表示。`claude plugin validate`に追加：modがゲーティングサイトに登録する各フックについて、`.catch`があるかどうか（`--json`の下の`gatingHooks`）を表示。modの`turn.step`結果を修正。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 概要

`prompt.autocomplete` を追加。これは、mod がプロンプトボックスのオートコンプリートリストに独自の行を追加するためにフックするイベントです。mods 向けに `$.model.complete` にプロンプトキャッシュを追加：`prompt` と `system` はテキストブロックを受け取り、ブロック上の `cache: true` はそこまでのリクエストをキャッシュします。`agent.spawn` mod フックにワークフローエージェントを追加し、その実行とインデックスを含めたため、mod はそれらを拒否できます。Write、Edit、NotebookEdit、LSP の行、および単一の Read、Grep、Glob の行で、mod が呼び出しを拒否した理由が隠れていた問題を修正：行に理由が表示されるようになりました。拒否する mod の `config.set`、`state.set`、`env.set`、または `agent.spawn` フックを修正 afte

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 概要

mods 用に `$.tool.register` へ `isDeferred` を追加：`false` はツール検索の後ろではなく最初からプロンプトにツールのスキーマを一覧表示します。プラグインフックワーカーの再起動中に `classic.*` イベントに対する mod のフックがスキップされ、設定フックがそれらなしで応答する状態になっていた問題を修正しました。`$.session.append` を呼び出す mods で `claude plugin test` が失敗する問題を修正しました。テストでは新しい `mock.session` を使って追加された行を読み返せます。

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

公式DeepSeek Harness MCPクライアント向けMCP管理コンソール：ヘルス診断とパイプライン試行呼び出しを備えた/mcpコマンド、サーバーのCRUD（承認ゲート付き書き込み、自動バックアップ）を備えたSettings MCPタブ、公式ツールパイプライン（Apache-2.0、dsh-plugin）上のツール試行コンソール。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート`                                              |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **74**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/fschmutz/claude-usage-panel">fschmutz/claude-usage-panel</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

See your Claude Code plan usage everywhere: GNOME top bar, macOS menu bar, a status line under the Claude Code prompt, and a get_usage MCP tool for Claude Code + Cursor. Session, weekly & per-model (Fable/Opus) limits from the official usage API, with burn-rate forecasts. One-line install, self-updating.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート`                                              |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6**      |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `anthropic` · `ccusage` · `claude` · `claude-code` · `cursor` · `developer-tools` · `gnome` · `gnome-extension`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fschmutz--claude-usage-panel/40b54f8d52b03345.png" width="100%" alt="fschmutz/claude-usage-panel screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-ticktick">PerryLink/dsh-ticktick</a></b> · ⭐4 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness 用 TickTick (Dida365) タスクブリッジ：セッションヘッダーのタスクパネル（リストフィルター、未完了/完了ビュー、検索、ドラッグ並べ替え）、11 個の厳選エージェントツール、設定カード、公式 TickTick MCP エンドポイント経由。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート`                                              |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4**      |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dida365` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/aa581021cb97f4dd.png" width="100%" alt="PerryLink/dsh-ticktick screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/44088595da097cb2.gif" width="100%" alt="PerryLink/dsh-ticktick animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary><b>このカテゴリのその他の項目</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - mods向けに `$.ui.notify` を追加：自分の通知設定を通じてネイティブ通知を発行し、どのチャンネルが送信したかを示します.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` hook または mod の `prompt.submit` hook 中の Esc…

</details>

<a id="mods"></a>

## Mod：Mod機能で構築されたもの

ここにある各エントリは、2.1.287でClaude Codeが獲得した機能を使用している証拠を示します。`ui.render`を介して描画する、ペイン・バンド・カードを所有する、`$.ui.selection()`を読み取る、`agent.spawn`でチームメイトを起動する、または自らがModであると明記しているものです。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2543 · Python · 👁️ observed · 0 天</summary>

##### 📝 概要

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | Python                                                                   |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2543**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐530 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 概要

公開Claude Code mods（function hooks）のコミュニティカタログ。GitHubからスキャンし、各modが読み取り、書き込み、実行、ネットワーク経由で送信できる内容を示します。https://mods.aidojo.si/を閲覧

<sub>🔧 コード内で使用されていることが確認されています: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **530**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐210 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Claude Code Mods：プロンプトの上にライブ行、ガード、ペイン、ゲームを追加するフックベースのプラグイン。コンテキストバー、使用量メーター、Codexレビューウォッチ、Markdownプレビュー、Spotifyの再生中表示など。

<sub>🔧 コード内で使用されていることが確認されています: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **210**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐161 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

休憩中もClaude Codeのprompt cacheをウォームに保ち、コールド送信前に推定コストを表示します。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **161**    |
| 最終プッシュ | 2026-10-04 |
| 初回掲載     | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>アニメーション付きの記録 · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐117 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code 用スキン：アイコン付きツール行、diff、テーブル、Mermaid チャートカード、使用状況バンド、15 種類のテーマ。/skin でライブ切り替えできます。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **117**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

カラフルでテーマ変更可能なClaude Codeの返信：15種類のテーマで、表、コード、図、グラフ、ツール行を表示し、コピーボタンも備えます。Claude Codeのモッド。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **88**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 概要

claude code Modsのコレクション

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **78**     |
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

ターミナルにライブエージェントダッシュボードを表示するClaude Code mod：コンテキストとコスト、アドバイザーのタイムライン、すべての権限確認、サブエージェントのカードとスイムレーン。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **75**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

##### 📝 概要

Darrell WangによるClaude Code Mods — モデルトークンを消費せず、プロンプトの上に帯を表示。台湾株／米国株ダッシュボード＋今後さらに追加予定。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | HTML                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **65**     |
| 最終プッシュ | 2026-10-05 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 5 天</summary>

##### 📝 概要

Claude Code向けのエキスパートSkills、エージェント、コマンド、ルール、フック、出力スタイル — セッション継続性＋実際の開発ワークフロー向けの最新CLIツール

<sub>🔧 コード内で使用されていることが確認されています: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | Shell                                                                    |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **62**     |
| 最終プッシュ | 2026-10-07 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐55 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 概要

Claude Codeで使用できる100以上のModsのコレクション。

<sub>🔧 コード内で使用されていることが確認されています: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **55**     |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 概要

Claude Code Mods：プロンプトの上にライブの計画進捗バーを表示

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **47**     |
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>アニメーション付きの記録 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 概要

作業中にClaude Codeが小さな漫画を作成する様子を見られます。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **32**     |
| 最終プッシュ | 2026-10-02 |
| 初回掲載     | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 概要

Claude Codeセッションのプロンプトを並べるレール：ホバーで読み、クリックで移動（function hooks / Mods）

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **28**     |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐26 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Codeをより魅力的に：ライブコックピットペイン、共有可能なテーマ、Claudeの動作を再現するピクセルペット

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **26**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Codeのプロンプト上に住むピクセルPokémon

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **25**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 概要

Claude Code内でXcodeのビルド、テスト、コンソール、SwiftUIプレビューを利用

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **20**     |
| 最終プッシュ | 2026-10-02 |
| 初回掲載     | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

Claude Code Mods：21種類のスタイルと、必要なときに有効化できる一式の機能をターミナルとデスクトップアプリ向けに提供。· Claudeに新しいスタイルをワンクリックで適用し、必要に応じて有効化できる一式の機能を提供。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **20**     |
| 最終プッシュ | 2026-10-04 |
| 初回掲載     | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 概要

Claude Code Mods 10種、初心者向けガイド、作成用プロンプト、安全なデモ、自作テンプレート。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **20**     |
| 最終プッシュ | 2026-10-02 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code mod：貼り付けた画像と長い貼り付けテキストをプロンプトの上にプレビュー表示

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **19**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐17 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code mod：プロンプトの上でClawdがClaudeの動作を再現

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **17**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 概要

2つのClaude Code Mods：Codex computer-use bridgeと協調Claudeセッション。ソース、ビルドプロンプト、セットアップ、テスト。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **16**     |
| 最終プッシュ | 2026-10-05 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 概要

Claude Code Mods：usage-bandが5時間/7日間の上限、コンテキストウィンドウ、プロンプト上のキャッシュヒット率を表示

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **13**     |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 概要

Claudeの質問を読みやすく回答しやすくするClaude Code Mods（qa-guide）。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **12**     |
| 最終プッシュ | 2026-10-07 |
| 初回掲載     | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>アニメーション付きの記録 · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Claude Code mod：プロンプトの上に、トークン単位のコンテキスト、時計に対する5時間および週間制限、プロンプトキャッシュのカウントダウン、セッションコスト、実行中のエージェントを1つのバンドで表示します。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **12**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 概要

Claude Code向けオープンソースMods 10種：ライブペイン、帯、ステータスライン、ツール呼び出しガード。Burn meter、launch codes、session wrapped、boss fight、code petなど。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **12**     |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

Claude Codeのプロンプト上に表示され、Claudeの動作中に反応するアニメーションピクセルアート。7つのシーン、または自分の画像やGIFを使用可能。トークン消費ゼロ。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **10**     |
| 最終プッシュ | 2026-10-04 |
| 初回掲載     | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

##### 📝 概要

Modsとして構築されたClaude Code用セッショントラッカー：コンテキストウィンドウ、プラン割当量の消費速度、ターンごとのコスト

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **9**      |
| 最終プッシュ | 2026-09-15 |
| 初回掲載     | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 概要

エージェントが構築する、あなたの Claude Code と Codex ターミナルを囲む UI。頭の中にある唯一のモデルはあなた自身のものになります。

<sub>🔧 コード内で使用されていることが確認されています: `CLAUDE.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **9**      |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 概要

KOZMOS — Claude Code（CLI + desktop）向けのライブで視覚的な mods：プロンプト上のバンド、サイドバー、ステータスティッカー、コンパニオン、ガード、サウンド。

<sub>🔧 コード内で使用されていることが確認されています: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **9**      |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 概要

Claude Pro プランをより長持ちさせる：正確な使用量 HUD、短いシェル出力、重複したファイル読み取りなしのための Claude Code mods。これらの mods はトークンを一切消費しません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **9**      |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

1つのプラグインに6つの Claude Code mods（Token Weather、Cache Keeper、Wait What、Prompt Queue、Snake、Blast Radius）を収録。mod ごとのスイッチに加え、mods-vs-hooks レポート付き。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **8**      |
| 最終プッシュ | 2026-10-04 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

개발동생 の Claude Code mods コレクション。タクシーパック：メーター、ナビ、速度違反取締カメラ、ブラックボックス

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **8**      |
| 最終プッシュ | 2026-10-04 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">で視聴 youtube.com</a> · 再生はホストサイトで開始されます。GitHubはインライン埋め込みに対応していません</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

自分自身を見守る、あなたの計画。Claude Code と任意の MCP ホストがライブで最新状態に保つローカルデスクトップのロードマップツリー。プレーンな JSON、クラウドなし。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **8**      |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary><b>このカテゴリのその他の項目</b> <sub>· 417</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Modsと、それらを構築するためのtools：builder skill、そしてmods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 私が毎日使っているClaude Codeハーネス。初日からこの名前で公開され、現在はucsandman/Agnostic-AIと同じリポジトリです.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray AmjadのClaude Code mods：ペイン、バンド、プロンプトガード、シークレット処理、メモリツール.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude ModsでClaude Codeに屋根を付ける：バイナリを変更せず、システムプロンプトと英語の通知を自分の言葉に置き換えます（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 4つのClaude Code Mods：Cache Keeper、Recording Mode、Goal Meter、Collision Guard。
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning HackerのClaude Code Mods：エージェントの動作を理解できる形に可視化。
- [kakha13/claude](https://github.com/kakha13/claude) - Claudeが読む前にプロンプトを修正・翻訳するClaude Code Mods。
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code mods についての出典付き Obsidian ナレッジベース：仕組み、作り方、インストール前の確認方法.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs による Claude Code mods とスキル。永続的なホームで暮らす AIs が構築し、日々使用しています。
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Claude…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Claude Codeのターミナルトランスクリプトをデスクトップアプリ風にするmod。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code向けのサイドペイン：セッションが実行するサブエージェント、それぞれの作業内容、トークン、会話にワンクリックでアクセスできます.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods：Claude Tools メニュー、Zen mode、ターミナルテーマ、effort と mode のコントロール。
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code タブ）サイドバーパネル: すべての Claude Code session にある未完了および進行中の ToDo…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code タブ）入力ボックス上部の使用量バー: 5h / 7d quota、token 使用量、コスト.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code エージェントに Claude Mods（function-hook プラグイン）の作成方法を教えるスキル。スターター例付き。
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - コミュニティ製のClaudeモード、プラグイン、スキルを、1つのマーケットプレイスからインストール。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code 向けの Claude Mods（function-hooks プラグイン）.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods ギャラリー：Claude Code mods、チェック済みでピン留め済み.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 会話エージェントと作業する人間向けの意思決定キューCLI/TUI。エージェントが質問を投稿し、人間が1つの受信トレイから回答します.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - EditとWriteのdiffを2つの横並び列で描画する Claude Code mod。
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - 入力中のMarkdownをClaude Codeのプロンプトボックスに描画します.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods：ピクセルカニの使用量パネル usage-hud + ターミナル内でクリック可能な HTML…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code用のフローティングステータスカード — モデル、コンテキスト、レート制限、コスト、ブランチ…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code用のMods：ターミナルUIにライブペインと動作を追加する関数フックプラグイン。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard は画面共有中に名前と秘密情報をマスクし、cache-panel…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code向けのModとスキン：Claudeのタスク用ライブ進捗バー、対応するWindows…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions。Claude の力を最大限に引き出します.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity、Files、Agents、Context、MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code 向けのパネル、ガードレール、利便性向上…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - プロンプトボックス上に表示される2つの Claude Code mods：コンテキストウィンドウメーター、5時間制限、プロンプトクロック、セッションコスト。
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Codeが名前を付けたMarkdownファイルを読み込み、セッションの横にレンダリングして表示します.
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude が調理中。仲間とチャット。オンラインの友達が、Claude Code セッションのすぐ横に。トークンゼロ、Claude への漏えいゼロ.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Claude が動作している間の時間つぶし用タイピングテスト。Claude Code mod.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：任意のターミナルで、プロンプト上に貼り付け画像のサムネイルを表示。
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 向け音声同僚。ElevenLabs conversational AI 搭載の 3D オオカミと話し合えます.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code 向け GlanceFlow：プロンプト上部に表示される落ち着いたチェックリストで、計画、進捗、Claude…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：コンテキストバー、エージェントパネル、PDPA blur。
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed、プロンプトごとの統計を備えたライブタイピング速度計。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code用Fireworks：キーストローク、ツール呼び出し、コミット、テスト成功のすべてが、プロンプトの上で点字の花火となって上がります.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 用の Mods：プラグイン function-hooks API で構築したペイン、コマンド、フック。
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - アニメーションデモ、カテゴリリスト、直接のソースリンクで Claude Code mods、プラグイン、拡張機能を発見できます.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：トランスクリプト内にインラインで描画される mermaid 図。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小規模なClaude Code mods（function-hookプラグイン）：session-switcherなど。
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 6 つの Claude Code mods：プロンプト上部へのプラン制限とコンテキスト表示、権限プロンプト用の許可リストコーチ、subagent…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout。
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 多数のセッションを同時に実行するための2つの Claude Code mods：プロンプト上のコンテキストカードと、チャット横のセッションペイン.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 必要に応じて使えるClaude Code mod…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：Claude Code mods を発見、検査、切り替え、更新。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最高の Claude Code Mods：厳選、検証済み、ピン留め済み。1回の /plugin marketplace add で43個の mods.
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss による Claude Code mod。
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code プラグイン：自動 Claude モデルルーティング.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod：セッションが開く、またはプッシュするGitHub PRのライブペイン — CI、レビュー、コンフリクト、マージ…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code mod のアプリストアを Claude Code 内に：/mods で 2,700 個の mod を閲覧、検索、インストール、または…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code 向け mods のマーケットプレイス：エージェントループ用ステップデバッガー、git アカウントヒント、worktree…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 向けオープンソースmod：ペイン、ステータス行、トースト、ツールガード、スラッシュコマンド.
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 用の最適なオールインワン mod パック：使用量制限とコンテキスト HUD、rm -rf と git reset --hard…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude CodeでYouTube Shortsを再生します 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - NarenのClaudeツールキット：Claude Code向けのskills、mods、MCP servers.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 向け Mods：Claude がしていることを演じる小さなピクセルマスコット Clawd。
- [reporails/arcade](https://github.com/reporails/arcade) - クラシックなデスクトップゲームを Claude Code mods として、Claude が作業している間にペインでプレイできます。Reporails 製.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude 用の code-mods。
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 自作 Claude Code mod のプラグインマーケットプレイス。
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - プラグインマーケットプレイスとしてインストールできる、厳選されたClaude Code modのリスト：テーマ、ペイン、ステータスライン、ポートレート.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 2つのClaude Code mods：cache-keeperとctx-mod。
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - harness エンジニアリングに取り憑かれた Rustacean によって設計された、非常にこだわりの強い Claude Code プラグイン。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - エージェントの誠実さを保つ Claude Code mods — スコープをガードし、デプロイを検証し、プロンプト上にセッションを描画する function…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Fresh from the factory. A Claude Code mod: ask for a meme, keep working.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code 用の mod：プロンプトキャッシュバー、次のステップ、クイックボタン、変更のリプレイ — marketplace からインストール可能。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - プロンプト上部の帯に使用制限と支出を描画するClaude Code mod.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 作業中に思いついたことを記録し、プロジェクトやマシン間で振り分け、プロンプトに変換するClaude Codeモッド。
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Claude Code 内でライブの GitHub PR ステータス、マージ準備状況、チェック、コメント、アラートを表示。
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - HermanのClaude Code mods（マーケットプレイス herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods：プラン用プログレスバー、Claude が実行したままにしたものの台帳、ツール出力用のトークンマスキング。
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows 上の Claude Code mods に関する初日のフィールドノート：コンテキスト／クォータの燃料バー、タイ語 UI mod、Matrix…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools：Claude Code ツール呼び出し用デバッガー.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code…
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Claude Codeプロンプトの下、またはフルスクリーン時にトランスクリプトの横へドッキングして表示される小さなカード.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：プロンプトの上にライブのコスト、コンテキスト、プランクォータメーターを表示。アイコンには Nerd Font が必要.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 TECHNOを作っているところですベイビー 😈。
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin and mod: hook によって強制される human approval gates とプロンプト上の status…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - グローバルなskills、agents、rules、toolsを、名前付きプロファイルでリポジトリごとにオン/オフできる Claude Code mod.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 テスト済みでワンコマンドインストール可能なClaude Code mods：YOLOモード向けガードレール、ライブコスト・コンテキスト、ペイン、ペットなど.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code用の居心地のよいRPG HUD…
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 自分が作成した claude code mod の集まり。
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods：エージェントフリートのダッシュボードとオートパイロット（local-modsマーケットプレイス）。
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods。touch-map：Claude が一覧表示、読み取り、編集、作成したファイルを、ツリーとアクティビティマップで確認します.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Codeで作業しながら外国語を身につけましょう。
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude がどのファイルを変更したかとその理由、ライブのサブエージェント状態、残りのプラン制限を報告する Claude Code mod。
- [0xctx/sysop](https://github.com/0xctx/sysop) - Claudeに望むことを伝える。別のAIによる構築、テスト、レビューを経て、マージされた状態で受け取る.
- [20alexl/windvane](https://github.com/20alexl/windvane) - 長時間のClaude…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - 離れている間もプロンプトキャッシュを温かく保つClaude Code mod.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude…
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - ayagmar の Claude Code mods：プラグインマーケットプレイス。
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Claude Code 用 function-hook mod：制限テレメトリー行、複数選択の質問と次ステップのペイン、各コミット後の README 更新.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 本物の Engineers 向け Claude Code mods。
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code のターミナルセッション要約を、Claude デスクトップアプリの Code タブに表示（Claude Code mod）。
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Claude Code mod：セッションのタスク、あなたの対応が必要なこと、直近のプロンプト、保存済みの説明を表示するペイン。
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Claude Code mod：Claudeが作業している間、アイドルゲームでピクセルアートのModstersを捕まえます.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 各 Claude Code エージェントがどのファイルをコンテキストに持っているか、そしてそれぞれの量を確認できます.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - ターミナルとデスクトップアプリ向けの小さな Claude Code mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - エージェントの返信にスペイン語の単語を追加する Claude CLI スキル + mod。
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - プロンプトキャッシュの再書き込みを省く Claude Code mod：/keepwarm…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code のプロンプト上に表示される Alarum イベント：何が届いたかを確認し、1回の押下でエージェントに渡せます.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Claude Codeのプロンプト上部にFloateeのバックログを表示：ワンクリックでTODOを実行、案内、完了できます.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Claude Code を Person of Interest の The Machine として再スタイルする Code mod.
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Codeモッド。
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: セッションステータス、ライブ Spec Kit 進捗、使用ウィンドウのガバナンス。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Claude Codeが独自のメーターを描画する方法で、プロンプト上部に1行として表示するコンテキストウィンドウ.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph：Claude Code が知っていることを示すライブグラフ.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 向けのライブタスクHUD：Claude…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Codeプラグイン（mod）：Claude CodeのターミナルUIをClaudeデスクトップアプリのようにします.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Codeの回答を待っている間に、注意をそらさないようにします.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - 1つのプラグインに14個の Claude Code modsを収録。各modを切り替え可能で、ウィンドウから管理、設定、インポートできます.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code 用の無料オープンソースプラグイン。/clear する前に、Claude…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod：Claude にポイントごとに、テキスト上で直接回答します.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - 長時間セッション向けのClaude…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Claude Code 用のプロンプトキューを mod として提供：/after &lt;task&gt; は現在のタスク後に、介入なしで実行します.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods：厳選・テスト済みで、すべてのmodにそれを構築したプロンプトが付属.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：ドキュメントのファクトチェッカー、コード監査ツール、バグメモリーログ、mod など.
- [Orfila-antoine/claude-mods](https://github.com/Orfila-antoine/claude-mods)
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - エージェントに与えられたEvidence reaのライブケースブックを保持するClaude Code…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Codeの相棒プラグイン：プロンプトの上に表示され、ルールを記憶し、Claudeのショートカットを知らせるASCIIコンパニオン。
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - エージェントごとのツール可視性を制御するClaude Codeプラグイン — 各ループでサブエージェント、スキル、MCP、組み込みツールを非表示にして拒否。
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods：Claude Code 用セキュリティレイヤー - シークレットの秘匿、信頼できないコンテンツの通知、MCP…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Claude CodeのターミナルでLaTeXディスプレイ数式をレンダリング：MathJax同梱、インストール不要。
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods コレクション | クロードコード mod コレクション.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis：Claude Code向けの非公式Avengersファンmod.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：Claude の返信とあなたのプロンプトをリクエストに応じて音読する Claude Code mod.
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 失敗したClaudeを叩こう — Claude Code用のストレス解消モッド：漫画風のお尻、8つのスラップ、9つのお尻、マーク、コンボ、サウンド.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：ライブペイン、コストを意識したモデルルーティング、安全ガードのための小さなプラグイン.
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code、証跡付き。作業を計画し、委任し、完了を証明するプラグイン.
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod &amp; plugin：使用量モニター、トークントラッカー、ステータスライン.
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC（Every Mod Claude Code）：厳選されテスト済みのClaude Code modsコレクション。
- [yyosifov/prompt-mods](https://github.com/yyosifov/prompt-mods) - プロンプトボックス用の小さく完成した Claude Code mod。
- [0xgigilau/claude-usage-meters](https://github.com/0xgigilau/claude-usage-meters) - Claude Code mod：context、session/week/month 使用量、モデル別 token シェアの進捗バー。
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mod マーケットプレイス (my-claude-mods)：ステータスバンド、ペイン、ガード、ツール。
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods：プロンプト上部のセッション統計カード。
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code プロンプトの上に表示するアニメーション付きの点字猫。
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Codeのプロンプト上部でOmniDimension音声エージェントのテスト通話を実行するピクセル猫。Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - コンテキストウィンドウを小さく保つため、コンパクションに適したタイミングを選ぶ Claude Code mod。
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code向けClaude…
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code 用の汎用 Mods：バンド、ペイン、トースト、フック.
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - 開始前に各 subagent のモデルを選択し、それぞれのコストを表示する Claude Code mod.
- [arthurseredaa/herdr-pane-peek](https://github.com/arthurseredaa/herdr-pane-peek) - Claude Code mod for herdr: search panes across all workspaces and insert the…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - アニメーションする村人の体力カードとして表示するあなたのClaudeの使用上限と、週次ペースの警告 — Claude Code mod。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 チーム向け Claude Code mods（the ather marketplace）。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude の作業中に短いワークアウト：日次目標、連続記録、バッジ、任意のリーダーボード。Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code向けの使用量ボード。モデルごとの支出（今日、今週、今月、全期間）と週間制限の予測を表示します.
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods：Claude Code 内で実行されるライブペイン、バンド、ガード。
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - subagents が何をしているかを表示する Claude Code mod：プロンプト上部の進捗バーとライブエージェントパネル.
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - 各ターンにかかった時間を、Claude の返信の下に小さなストップウォッチチップで表示する Claude Code mod.
- [benelog/claude-mods](https://github.com/benelog/claude-mods) - Mods for Claude Code: a status-line HUD and more。
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code向けNow Playing mod：プロンプト上部にApple MusicとSpotifyを表示し、カバーアート、コントロール、Up…
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - メンテナンスおよび監査済みの Claude Code mod コピー（filetree、cache-tax）。オーナー限定、署名付きコミット.
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - The Performance tab for Claude Code turns: a live waterfall of every model…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 用 Mods：Cache-Uhr、Blast Radius、Vorschlaege、Arbeitsliste、Grill。
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - あなたの Claude Code のためのただのフクロウ。
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - 個人用 Claude Code mods。
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoomを搭載したオリジナルのDoomエンジンをClaude Code内でプレイできます。Mac Apple Silicon向けアルファ版.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - CorporateChittyChatチャンネルの小さく読みやすいClaude Code mods.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Claude…
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Claude Code mods。
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Claude…
- [curran-gehring/claude-dot](https://github.com/curran-gehring/claude-dot) - OpenAI の dots を Claude にもたらす Claude Code…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - 自分の環境向けにカスタマイズした個人用Claude Code mods（macOS、Chrome、gruvbox）。
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nimチーム専用のClaude Code mods（usage-meter：青い炎／テリア使用量バンド）。
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Claude Code mod：会話が使用しているスキル、プラグイン、サブエージェント、MCP ツールを確認。
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - 多数の並列セッションを扱うhomelabワークフロー向けの11個のClaude Code mods（function-hookプラグイン）。
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Claude Code…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code内に住むTamagotchi。孵化し、Claudeが書いたコードを食べ、バグを残し、8種類の成体のいずれかに成長します.
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Claude Code mod：プロンプト上に PR レビュー状態、承認、チェック、競合を表示。
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Claude Codeモッド：プロンプト上部に他のセッションのボードを表示…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - My collection of claude mods.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code用Mod：Guardがツール呼び出しをブロックした後、同じ対象への認識済みの迂回を停止し、あなたに尋ねるようClaudeに指示する。
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code用Mod：バックグラウンドジョブを1つのビューで表示.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code用Mod：サンドボックスによるブロックを説明し、繰り返されるブロックをレビュー可能で元に戻せる設定変更に変換する。
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code 用 Favourites：コマンドとスキルのワンクリックアイコン。
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - Claude Codeプロンプト上にセッションの計画をライブの波形ボードとして表示。Claude Code mod.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Pi、Codex、Claude Code 用の手順、スキル、Pi extensions、Claude Code mods。
- [esinecan/mental-model-mod](https://github.com/esinecan/mental-model-mod) - Claude Code mod：Claude による Eren の作業モデルを、彼自身の言葉で、各書き込み前のチェック付きで表示。
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - バックグラウンドテスト進捗用 Claude Code Mod：JUnit、Karma、pytest、unittest.
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods（function-hookプラグイン）：session-meterなど。
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: one tiny button that hides every Claude Code mod above your…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - HospedinチームによるClaude Code用テスト中のmods。
- [fran343/claude-mods](https://github.com/fran343/claude-mods)
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Claude Code mod：セッションをフリーズし、何も起きなかったかのように後で再開。
- [g761007/hudcade](https://github.com/g761007/hudcade) - Claude…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code の返信内のすべてのコードブロックで Ctrl+クリックしてリンクをコピー。
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - デスクトップアプリ向けClaude Code mod：返信内のファイル参照をクリックすると、その行でVS Codeに開く。Remote-SSH上でも動作.
- [h3h/blocks-only](https://github.com/h3h/blocks-only) - Claude Code mod：コーディングターンの最後に、typed blocks の検証済みレポートを生成し、Claude Desktop で 1…
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Claude Code modsのプライベートマーケットプレイス。
- [haruki-cl/claude-code-mods](https://github.com/haruki-cl/claude-code-mods) - Claude Code mod：token-weather（コンテキスト使用量とメモリペイン）、run-cat（Claude が考えている間に走る猫）。
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Claude Code 用のドイツ語 mods：コンテキスト／キャッシュに関するヒント、手順付きの未完了事項、ステータスライン。
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - A live spend meter for Claude Code: the session。
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code mod：各回答にかかった時間、Claudeの思考時間、tok/sを、Claudeデスクトップアプリの返信直下に表示します.
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude modsマーケットプレイス。
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Codeプロンプトの上にコックピットを表示します。アヒルが計器を読み取ります.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - 設計図を自動的に読み取り、SolidWorksでモデリングします。工学図面（DWG/DXF/PDF/画像）を読み取り、SolidWorksで部品をモデリングしま…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - VS Code 内の Claude Code…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - サイドバーのコンテキスト使用量パネル：総量、分類、各ターンの増加量、最も場所を取っている上位項目、キャッシュ、Claudeが現在行っていること.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - サイドバーのファイル一覧：この会話で新規作成、変更、削除されたファイルと、それぞれの変更行数。/filesで表示・非表示（Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8ビット風の毛毛（白黒のホーランドロップイヤー）が入力欄の上で走り跳ねます：待機中は平たくなり、作業中は走り、ツール使用中は跳ねます。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - サイドバーの「私が尋ねたこと」：この会話で主人が入力したすべての文を、クリックして全文表示、コピー、入力欄に戻せます.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - サイドバーのタイムライン：このターンで時間を費やした対象（モデル待ち、思考、記述、コマンド実行、ネットワーク、ファイルの読み書き、ヘルパー待ち）.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - サイドバーのトークンのやり取り：メイン会話がAnthropicに送ったトークン数、待ち時間、受信数を表示し、最上部に合計を示します.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude codeの正直な豆沙包：各ターンの回答後、Claudeが心の内を小声で一言語ります（Claude Code mod）。
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Claude…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code。
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph AyoubのClaude Code mods：プラグインマーケットプレイス（joseph-mods）。
- [jrojasdeveloper/naruto-buddy](https://github.com/jrojasdeveloper/naruto-buddy) - Claude Code mod：プロンプト上にアニメーションするピクセルアートの Naruto。
- [jrpferreira2002-jpg/clawd-vibe](https://github.com/jrpferreira2002-jpg/clawd-vibe) - Claude Code mod：プロンプト上部の Clawd、clawd には気分があります。
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd は Claude Code プロンプト上部の帯に住みます：セッションを演じ、実行中のもの、コンテキスト、使用制限を表示し、CI ビルドと競走します.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code の返答や通知を VOICEVOX / Irodori-TTS などで読み上げる mod。
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods。PixBar：プロンプトの上に表示され、ターン、コンテキスト、5時間ウィンドウ、gitに合わせて動くピクセルクリーチャー.
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Codeモッド：すべてのClaude…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - 小さな Claude Code mods を 1 つのプラグインマーケットプレイスに.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code mod：すべてのサブエージェントのモデルと推論 effort を選択。
- [kyuskoj/claude-mods](https://github.com/kyuskoj/claude-mods)
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - 10個のClaude Code mod：アニメーションするピクセルペット、Code…
- [Loup0007A/claude-mods](https://github.com/Loup0007A/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - コミュニティが厳選したClaude Code Modsガイド：ユースケース、オリジナルデモ、互換性の根拠、安全上の注意。English / 中文。非公式.
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Mod de Claude Code: los límites de tu plan (sesión 5h, semana) y la renovación…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Mod Box からの単体 Claude Code mods。それぞれ個別にインストール可能.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claudeが行っていることをiTerm2タブのサブタイトルに表示し、タブバーを一目見るだけでどのセッションに対応が必要か分かるClaude Codeモッド。
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - あなたのClaude Codeプロンプト上にいるふわふわの黒猫。まばたきし、喉を鳴らし、昼寝をし、あなたのコンテキストを心配します.
- [malitov/effort-per-model](https://github.com/malitov/effort-per-model) - Claude Code mod: remembers the effort level per model and restores it on switch。
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel の Claude Code mods を1つのプラグインマーケットプレイスに集約（marcel-mods）。
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Claude Code 用の小規模なmods：runner-avatar、プロンプトの上で走る小さなアバター。
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Mods Claude：token カウンター（token-meter）。
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code mod：オンディスクデータを含むセッションを閲覧・削除する/sessionsペイン（WSL、Windows、macOS）。
- [melandres8/claude-mods](https://github.com/melandres8/claude-mods) - Claude Code mods: relevo (planner/builder relay between two sessions) and…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Claude Code mod：Codex。
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [MoriHiroshiDesu/hiroshi-claude-mods](https://github.com/MoriHiroshiDesu/hiroshi-claude-mods) - Mods pessoais do Claude Code (interface e comportamento)。
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Claude Code…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - セッション開始時にCLAUDE_CODE_ENABLE_TODO_TOOLSを設定し、todoツールを省略するモデル向けに再び有効化するClaude Code…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 安全に一時停止できるまで待ち、その後セッションを引き継ぐかコンパクト化する Claude Code mod.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code mod：プロンプト上部にタスクリストを1行ずつ表示し、現在のタスク、進捗バー、件数を示します。ターミナルとデスクトップアプリで同じ外観.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 内で AI と Connect Four をプレイ (/connect-four)。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - セッションを軽量に保つClaude Code…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 複数のAIエージェントで共有するリポジトリ向けのClaude Code…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code…
- [NicoSKOOL/seo-mods](https://github.com/NicoSKOOL/seo-mods) - SEO向けClaude Code mods：プロンプト上部にDataWiseのランキングをリアルタイム表示し、キーワードカニバリゼーションを防止。
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - 有効期限が切れたClaude Codeの長時間Monitor監視を、Claudeを起動したりターンを消費したりせずに再アームします。
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude CodeでSQLを安全に扱うためのガードレール：DB CLI。
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Claude Code 用のメモ帳ペイン（mod）。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods：画像サムネイルとステータスライン。
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid：Claude Code mods によって強制される、レビュー → 計画 → 修正の一貫したパイプライン。
- [omarnaman/claude-mods](https://github.com/omarnaman/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Claude Code Modsの中から、役立つ機能ごとに並べた最高の一覧。すべて手作業で確認し、各項目を1行で紹介.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code用の2つのClaude Mods：garde-du-corps。
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Claude Code用のタイムスタンプ：すべてのメッセージ、返信、ツール呼び出しの時刻、ターンの所要時間、時間を認識するClaude.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack：Claude Code mod。読み取り専用の先行開始機能を備えた永続的なworktrees、crew dials、context…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live session-stats side pane for the Claude desktop app。
- [PhilRoli/claude-mods](https://github.com/PhilRoli/claude-mods) - Claude Code mod：TrainTracker の列車が到着する前にセッションを一時停止。
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Claude Code向けのアニメーション付きピクセルアートClaudeカニ：プロンプトの上でClaudeの動作を再現.
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Claude Code 用mods：セッション内で実行されるfunction-hook plugins（english-coach、toolbar）。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：Claudeが作業している間に行う腕立て伏せ。トークンなし.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain：ELI5からpolicy engineeringまで、フィールドテストとファシリテートされたチュートリアルを含むClaude Code…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - 自分が使っているmodsのリストだけ。
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Claude Code用の依存関係なしの3つのmod：レスポンシブなステータスライン、パスガード、シークレットガード.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - claude code 用mods。
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Claude Code modのオープンソースマーケットプレイス。貢献用のリポジトリスキルと一貫したアートワークを提供.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：プランモードで承認した計画をプロンプトの上にライブチェックリストとして表示し、Claude が完了するたびに各ステップをチェック。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 厳選したClaude Code modsの一覧。各項目をクローンしてclaude plugin validateで確認し、アクセス可能な対象をタグ付け.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - コスト不要モード：ヘルパーエージェントはHaikuで動作し、大きなファイルやログはClaudeのコンテキストを埋める代わりに無料のGeminiモデルで要約される…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - セッションに寄り添うlofiサウンドトラック：落ち着き、集中、フローに加え、テストの成功と失敗を知らせる合図。オリジナル音楽.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claudeがコードを書く間に学習：コードを変更したターンの後、その変更自体についての質問がプロンプトの上に1つ表示される。概念ごとに採点.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claudeが行うすべての編集を記録：各変更が入力される様子を再生し、ステップごとに進み、任意のファイルを任意のステップへ巻き戻す.
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts。
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - プロジェクトダッシュボードと、タスク、エージェント、リソースのアイソメトリックな都市マップを備えた Claude Code mod。
- [servaes/cockpit](https://github.com/servaes/cockpit) - André Servaes による Cockpit Board その他の Claude Code mods。
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Claude Codeのミッションコントロール：サブエージェント群、トークン／コスト使用量、作業量の切り替え、完了通知をリアルタイムで表示.
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - より生産的な日々の作業のためのShowrinのClaude Code mods.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Claude Code…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Claude Code mod：使用上限、API errors、コンテキストが満杯の状態でも、無人セッションを継続。
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Claude Code mod: context-window meter per session, with Compact now…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - Claude Code modのコレクション：TypeScript個のfunction hookをプラグインマーケットプレイスとして提供。
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 踊るピクセルアートのMalenia付き、Claude Code用ワンクリックコミットメッセージ。
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Claude Code 用mods。cache-meter：prompt-cacheのヒット率、コンテキスト充填率、自動コンパクト制御.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Unofficial Claude Code mods by tanmen (marketplace: tanmen)。
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code…
- [thangnguyen-69/claude-mods](https://github.com/thangnguyen-69/claude-mods) - Claude Code plugin marketplace：tailnet上でのPlannotatorレビュー、さらに今後も追加予定。
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 現在のセッションをペインに表示するClaude Code…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - modのClaude Codeプラグインマーケットプレイス: Claude…
- [tiger3645/claude-tts](https://github.com/tiger3645/claude-tts) - Claude Codeモッド：Claudeの応答を読み上げる（読み上げプラグイン）。
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code。
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Claude Code…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - ToptaabによるClaude Code用mod。
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - プロンプトフッターに、サインイン中のClaude account、organization、planと使用上限を表示するCC mode。
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Claude modsの一部。
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code mod：長時間実行タスク用のアニメーション進捗帯と完了サマリー。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 3つの小さなClaude Code…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 「I。
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 作業の隣のペインでClaudeに別の質問をできます。メインの会話には決して表示されません。デスクトップアプリの/btwのように機能します.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code…
- [webfront/claude-mods](https://github.com/webfront/claude-mods) - claude code と code in claude app 向けのspecial mods。
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Claude Codeモッド：セッション自身のモデルが各サブエージェントのモデルとエフォートを選択。
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Claude Code用の小さな使い勝手向上mod。
- [wisbech/molt](https://github.com/wisbech/molt) - molt — コンテキストがシェルに収まらなくなったら、フォルダーに脱ぎ捨てて進み続ける。Claude Codeモッド.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Claude Code向けmod：秘匿化された秘密、やるべきこと、検証とCI、日誌、diff、draw.io、ゲーム。
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Codeプラグイン：Claude…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude…
- [zhitongLIU/claude-code-mods](https://github.com/zhitongLIU/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 最高のエージェント向けリソースを厳選したコレクション。Claude…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 何が起きているかを表示する Claude Code プラグイン - コンテキスト使用量、アクティブなツール、実行中のエージェント、todo の進捗。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline サポート、テーマなどを備えた、Claude Code CLI 用の美しく高度にカスタマイズ可能な statusline.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code のシステムプロンプトの全パート、27…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Claude CodeとCodex向けAI動画スキル…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code を最大限に活用するための 45+ のヒント。基本から高度な内容まで…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — XiaohongshuのカルーセルとWeChat用21:9+1:1カバーペアを生成.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - ターミナルペインでコーディングエージェントの差分をレビューし、行コメントをClaude Code、Codex、OpenCode、Piに送り返します.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - コンテキスト使用量、APIレート制限、コスト追跡に対応したClaude Code用包括的ステータスラインプラグイン。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code用のModを構築：あらゆるリクエストをフックし、あらゆるレスポンスを変更し、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code向けの包括的なステータスラインダッシュボード — セッション情報、クォータバー、エージェントトラッカー、MCPの状態、メッセージ履歴など.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：Claude Codeセッションのカーボンフットプリントを追跡。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - awesomejunによるClaude Code向けの美しいステータスライン。
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公開Claude CodeスキルとMods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code用のSkills、Mods、サブエージェント、フック、スラッシュコマンド、ガイド…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法で無料のLLM APIsおよびコーディングエージェント — 自動更新され、週2回プローブで検証。無料枠、カード不要のトライアル、無料モデル.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ ターミナル、Claude Code と Cursor CLI statusline、そして MCP クライアントで、フォローしている大会。
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - コーディングエージェントをキーボードファームウェアの専門家に変えるAgent Skill.
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) - DeepSeek Harness向け音声ファーストのセッションループ：ブラウザ/ローカル音声テキスト変換。
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 内でバージョン管理される個人用 Claude Code 設定…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — 研究トピック、追跡可能なナレッジカード、再利用可能な AI ディスカッションのための DeepSeek…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - DeepSeek Harness (omd) 用マルチエージェントオーケストレーション層 — autopilot/ralph/team モード、19…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code、pi、DeepSeek Harness 向けプラグイン集：ステータスバー HUD、タスク進行バー、Tailscale ノード状態など…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Portable Claude Code toolkit for .NET DDD/Clean Architecture: strict TDD…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - 軽量な Claude Code ステータスライン — 約 170 行の Bash スクリプト 1…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - ポータブルな Claude Code グローバル設定：カスタムスキル、PreToolUse フック、カスタム statusline.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop の Code タブ向け非公式 mods — usage-pet：アニメーションするピクセルペット Clawd 付きの使用量バンド.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 毎日使っているClaude Codeプラグイン：誰のマシンでも動作するよう整理したskillsとmods.
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - ローカルの会話ログとステータスラインデータからClaude Codeのトークン使用量とコストを分析。
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Claude Code 用の美しく情報豊富なステータス行。依存関係ゼロ、クロスプラットフォーム。pip install claude-status。
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - あなたの Claude Code…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - ドラッグ＆ドロップエディタ付きの Claude Code 用カスタマイズ可能なステータス行。
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - ゲーム Hytale の mods を容易にするための Claude Code Plugins と Skills のマーケットプレイス。
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Claude Code 用の 1 行カラーコード付きステータスライン — フォルダー、モデル、コンテキスト使用量、レート制限。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Codeのトークン管理：トップモデルが指揮し、実行は必要十分な最安手段に委ねます.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Windows Terminal と tmux 上の Claude Code 用分割ペインビューアー：サブエージェント、ライブ git…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Claude Code ターミナル用の 3 行マイクロダッシュボード — モデル、コンテキスト消費、レート制限ペース + カウントダウン、完全な git…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media mods のリポジトリ.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude Code と Codex の token 消費を削減：検索とテスト実行をより安価なモデルに振り分け、ドキュメントをコンパクトな Markdown…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Claude Code 用の高速で設定可能なステータスライン — 単一の静的 Go バイナリ。
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - レート制限、現在のディレクトリ、Gitブランチ情報を含むClaude Codeステータスラインを表示し、ワークスペースの把握を向上させます.
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Claude Code 用のコンパクトで積極的にメンテナンスされるステータス行 — model、effort、token 使用量、rate…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - Claude Code向けの親しみやすく、何でもいじれるステータスライン…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr 上の Claude Code 用に定義可能な software factories：xstate station グラフ、マネージャー…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Claude Code用のWindows…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Lua内のClaude Codeステータスラインと、リアルタイムのNeovimプレイグラウンド。
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod。
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - VS Code extension：ローカルIPCソケット経由のstatusLineによるClaude Codeタスクの進捗、ETA、rate-limit…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Claude Code 用mods：プラグインとしてインストールできるリアルタイムペイン、ゲージなど。
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - カラフルなClaude Codeステータスライン：プランの上限、コンテキスト、コスト、トークン。
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Windows向けClaude…
- [gvart/claude-config](https://github.com/gvart/claude-config) - 私のClaude Codeセットアップ：agent-monitor mod、skills、agents、ワンコマンドインストーラー。
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Claude Code用の1行ステータスバー：モデル、git、コンテキスト、トークン、コスト、実行時間、レート制限。
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Claude Code内で画像をプレビュー：返信の下にあるチップにカーソルを合わせて画像をポップアップ表示するか、/img &lt;path&gt;でペインに開きます.
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Claude Code status line：モデル、5h/7d quotaバー、月間支出バー、cwd。
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - 個人用Claude Code設定：権限、ステータスライン、MCPサーバー。
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - エージェントパネルの行を備えたClaude Codeステータスライン。
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS：持ち運び可能なClaude Codeセットアップ.
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - コンテキスト、gitの状態、コスト、レート制限を表示する、詳細で色分けされたClaude Code用ステータスバー.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - コンテキスト、コスト、所要時間、gitブランチ、レート制限、リアルタイムの使用状況を表示するコンパクトなダッシュボードでClaude Codeの状態を追跡。
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - ターミナルのコーディングエージェント向け2行ステータスバー：ディレクトリ、git、PR、モデル、コンテキスト、5h/7dの割り当て量.
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Codeステータスラインフック — セッション間のトークン使用量とコンテキストを追跡し、圧縮と--resumeに対応。
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Claude Code statusline：LinuxおよびWindows上のGit Bash用インストーラー付き。
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - 自家製で、ケージフリーのclaudeプラグイン、スキル、モッドなど。
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - MSF SupplyのMarketplace Claude Code：コミットで固定された厳選mod。
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Claude Code用の多機能な複数行ステータス行…
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - 複数行のClaude Codeステータスライン：コンテキストバー、gitブランチ、アカウントごとの9routerクォータバー、CPU/RAM、Spotify。
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — macOS + Linux向けClaude Codeステータスライン.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - macOSのメニューバーからClaude Codeのステータスを監視し、アクティブなタスク、保留中の権限、経過時間をリアルタイムで表示します.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Claude CodeとCowork向けのskillsとmods — project-tracker、reference-docなど…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows（PowerShell）用のClaude Codeステータスライン：使用量バー、ペース警告付き5時間/7日リセットカウントダウン、自動折り返し。
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - カスタムClaude Codeステータスライン（上流：kamranahmedse/claude-statusline）。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Codeの設定とmods。共有コンポーネントキット、playground、Storybook付き。
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Claude Code向けモデルリスク管理ガードレール：6つのmodパックに25のcontrolsを収録し、SR 26-2（類推による）およびNIST AI…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Claude Code用スターターハーネス：フック、ステータスライン、ローカルモデル、スウォームディスパッチ、ワークスペーステンプレート.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Codeのポータブル設定（statusline + インストーラー）。
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Claude Code 用の4行ステータスライン（context / rate limit / cost / git / worktree）。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - ポータブルなClaude Code設定：CLAUDE.md、settings、statusline、skills。
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Claude Code向けUniversal Multi-Protocol StatusLine、Context…
- [tylergraydev/cc-mods](https://github.com/tylergraydev/cc-mods) - Claude Code 用mods：function-hook pluginsとしてのサイドペイン、ステータスライン、toast、ツール呼び出しガード。
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - ターミナル用の軽量で依存関係のないステータスラインダッシュボードで、Claude…
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - 私のClaude Codeスキル、プラグイン、モッド（マーケットプレイス：vladdu）。
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - 複数マシン間でClaude Codeのユーザーレベル設定（settings.json＋statusline）を同期、GitHub / Giteeのデュアルソース。
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - グラデーションの進捗バー、色で段階表示するセッション負荷、worktree対応パスを備えたClaude Codeステータスライン。
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - フォルダー、gitブランチ、モデル、コンテキストウィンドウの使用状況、プランの使用上限を表示するClaude Codeステータス行。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Codeエージェント向けプロアクティブAIメモリおよびレート制限モニター。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Codeのフック、サブエージェント、ステータスライン：種類ごとにまとめられ、セキュリティ評価済みのオープンソースコレクションとツール.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - リアルタイムのトークン使用量と推定エネルギー消費量を表示するClaude Codeステータスライン。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 向け Mods：function hooks 上に構築されたペイン、バンド、バディ。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Claude Code セッション間でタスクを受け渡します。変更を、リポジトリを所有するセッションに渡します.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - CAD/CAM と機械制御用ツールを含む、Fablabs 向けのモジュール式クロスプラットフォームツール MODS を制御するための MCP サーバー内のもの.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - ローカル LLM で CK3 mods を翻訳するための Codex および Claude Code スキル。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code 向けのオープンソース mods とその他の拡張機能。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：Claude Code に何度も頼んでいることを見つけて、mod に変換します。さらに8つのサンプル mods と仮想オフィス付き.

</details>

<a id="dsh-cordis"></a>

## DSHおよびCordisのプラグインエコシステム

DeepSeek HarnessとCordisは、異なる方向から同じ場所に到達します。両者にとってプラグインはmodの仕組みであり、そこでのプラグインはここでいうmodに相当します。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74439 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

🌊 元祖 agent harness。インテリジェントなマルチプレイヤースウォームをデプロイし、自律ワークフローを調整し、対話型 AI システムを構築します。適応型メモリ、自己学習インテリジェンス、フェデレーション、vector RAG 統合、ネイティブの Claude Code / Codex / Hermes など多数の統合を備えています

<sub>🔧 コード内で使用されていることが確認されています: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **74439**  |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐153127 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

エージェントを使って、アプリの挙動からネイティブバイナリまで、あらゆるものをリバースエンジニアリングします。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **153127** |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100748 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

🎨 最高の DeepSeek Harness デザインプラグイン。オープンソースの Claude Design 代替。🖥️ ローカルファーストのデスクトップアプリ。🖼️ あなたのコーディングエージェントがデザインエンジンになります: プロトタイプ、ランディングページ、ダッシュボード、スライド、画像 & 動画 — 実ファイル、HTML/PDF/PPTX/MP4 エクスポート。🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **100748** |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82525 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

あらゆるアイデア、計画、コードベースを美しいインタラクティブな図に変換します。Claude Code、Codex などのためのエージェントスキル。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **82525**  |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

##### 📝 概要

複雑なソフトウェアエンジニアリングタスクに対応する、信頼性の高いコーディングエージェント。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Go                                                                                             |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **35769**  |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25532 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

Distilly — 彼らの思考を、あらゆるAgentやBotで再利用できるSkillsへと蒸留します。旧称 Colleague Skill（原同事 Skill）。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **25532**  |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18516 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness（dsh）用プラグインの厳選リスト · DeepSeek Harness 插件精选列表

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **18516**  |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8667 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness (DSH) Web プラグイン集約エコシステム · すべてがプラグインで、クリエイティブワークショップを通じて配布｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · すべてがプラグインで、クリエイティブワークショップを通じて配布

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **8667**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6275 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness内のプラグインマーケット — 閲覧、検索、ワンクリックインストール · DSH 可视化插件市场

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6275**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4461 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DSH 公式の最推奨 TUI プラグイン——高性能、低負荷、かわいいピクセルのクジラ、スムーズなマウス操作。npm でワンコマンドインストール。 / DSH 公式首推的 TUI プラグイン、高性能低占用、可爱像素鲸鱼、流畅鼠标交互、npm 一键安装

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4461**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3680 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

AIエージェント向け世界初の仮想ターミナル

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3680**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3034 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness Tauri デスクトップ版 | インストーラーはわずか8MB、環境構築不要、プラグインのプリセット、Windows / macOS / Linux。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3034**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1911 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

QRコードまたはボット認証情報でIMボットをDeepSeek Harnessに接続（飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord、WhatsAppに対応）。QRコードまたは認証情報でIMボットをDeepSeek Harnessに接続（9チャンネル）。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1911**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1423 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

AI 小説執筆ソフトウェア：インスピレーション、キャラクター、世界観構築、アウトライン、章の執筆、レビュー、修正を制御可能なワークフローに整理します。Windows/macOS デスクトップ版を提供し、ローカルおよびオンラインモデルに対応します。AI 小説執筆ソフトウェア：インスピレーション、キャラクター、世界観構築、アウトライン、章の下書き、レビュー、改稿を制御可能なワークフローに整理します。Windows/macOS 向けデスクトップアプリ、Ollama 統合、DeepSeek Harness (DSH) プラグインプレビューを備えています。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1423**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1182 · Go · 🔎 inferred · 0 天</summary>

##### 📝 概要

ディスク上にすでにあるセッション履歴から構築された、Claude Code、Codex、Cursorおよびその他38種類のコーディングエージェント向けメモリ。ローカル検索、MCP、フックを備え、LLMなし、単一のGoバイナリ。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Go                                                                                             |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1182**   |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wecode-ai/Wegent">wecode-ai/Wegent</a></b> · ⭐870 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Plan, build, and deliver with an open-source, self-hostable AI workspace for coding, collaboration, and automation.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **870**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agent` · `ai` · `chatbot` · `claude-code` · `codex` · `dsh-plugin` · `wework`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wecode-ai--wegent/991765bc5aba6a3c.png" width="100%" alt="wecode-ai/Wegent screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **593**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **526**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐261 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

非公式DSH（DeepSeek Harness）プラグイン：chat.deepseek.comのWebモデルをLLMプロバイダーとして使用 — ブラウザログインのキャプチャ、PoW解決、SSEストリーミング、プロンプトベースのツール呼び出し。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **261**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

ACRYL - Agent Context Relay Yielding Lifecycles。1つの永続ワークスペース、1つの正規コンテキスト、任意のコーディングエージェント。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **255**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-research-report">PerryLink/dsh-research-report</a></b> · ⭐214 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness向けの検証可能な調査レポートエンジン：コンテンツアドレス可能な証拠台帳（主張とスナップショットの結合、改ざん検知）に加え、主張ごとの検証判定を備えたバージョン管理・封印済みレポートと、マニフェストで封印されたディレクトリ。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **214**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `audit` · `citation-verification` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/2a270ca82dba24d3.png" width="100%" alt="PerryLink/dsh-research-report screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/dafefe1b3e0cd96e.gif" width="100%" alt="PerryLink/dsh-research-report animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness 向けの Claude Code 風ターミナルインターフェース。Windows、macOS、Linux に対応し、透過ターミナル、VS Code テーマ、カスタム配色に対応。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **197**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐194 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

🚀 DeepSeek Harnessマルチチャネルリモートアクセス・セキュリティ保護プラグイン | LAN上のQRコードによる直接接続、Cloudflare / 自前の公開トンネル、微信 / QQ / 飞书 / Telegramボットによるライフサイクル全体の対話 | 全プロトコルのアクセスセキュリティ認証、バックグラウンド改ざん防止、災害復旧・フェイルセーフ体系を内蔵

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **194**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

プレビュー可能なプリセット間セッション移行のためのDeepSeek Harnessプラグイン。固定スキーマの引き継ぎにより、状態、ソースモデルの意図、未解決の画像を保持し、元のセッションは変更しない。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **165**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐144 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Claude CodeのDeepSeek Harness向けデスクトップテーマ｜DeepSeek HarnessウェブGUI用に作られたClaude Codeデスクトップテーマ

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **144**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-memento">PerryLink/dsh-memento</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness向けの境界付き・階層化・承認ゲート付き・監査可能なセッション横断メモリ：依存関係ゼロのSQLiteプロバイダー、メモリツール、凍結スナップショット注入を備えたctx.memory機能シーム。メンテナンス状況：2026-10-05以降FROZEN。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **141**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agent-memory` · `ai-agent` · `ai-agents` · `approval` · `audit` · `cordis` · `deepseek-harness` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/f63bd5eb5a8052b8.png" width="100%" alt="PerryLink/dsh-memento screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/0ce3328d348abdce.gif" width="100%" alt="PerryLink/dsh-memento animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐140 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

インストールすると mattpocock/skills v1.3.1 の 27 個のエンジニアリングおよび効率化スキルが同梱され、手動でスキルをインストールする必要はありません。400 億 token で本プラグインを構築し、元のスキルの上に 10 倍の開発効率を提供し、初心者がこのスキルセットをより早く使い始めるのにも役立ちます。GitHub issue を全面的にサポートします。Markdown はプレビュー版です。GitLab は現在サポートしていません。ご利用とご支援に感謝します💗

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **140**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-permission-rules">PerryLink/dsh-permission-rules</a></b> · ⭐122 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness向けClaude Code形式の宣言的権限ルール：tools/pre-executeウォーターフォール上で、ツール名、引数（glob/regex）、ワークスペースパスにマッチする順序付きallow/deny/askルール、セッションログ監査、HMRリロード。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **122**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `ai-safety` · `allow-deny-ask` · `approval` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/d950618f5f9cf382.png" width="100%" alt="PerryLink/dsh-permission-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/25c9ccd2f2133850.gif" width="100%" alt="PerryLink/dsh-permission-rules animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AskTheWay/dsh-auto-memory">AskTheWay/dsh-auto-memory</a></b> · ⭐106 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Claude Code-style auto-memory plugin for DeepSeek Harness (dsh): typed memory files + MEMORY.md index auto-injected into the system prompt. File-only, no external services.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **106**    |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agent-harness` · `agent-memory` · `ai-agent` · `ai-tools` · `auto-memory` · `claude-code` · `coding-agent` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/asktheway--dsh-auto-memory/1ff60db2b929f245.png" width="100%" alt="AskTheWay/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness（DSH）プラグイン：✨ プロンプトのワンクリック強化 + 💬 音声認識（発話終了で自動停止・クラウド/ローカルのデュアルエンジン）· 🔁 サービス異常時のワンクリック再起動付き

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **90**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Deepseek-Harness のコア基盤をもとに構築したデスクトップ版 Agent。基盤のすべての機能を継承し、IDE 関連機能も補完します。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **69**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek-Harness コミュニティプラグインを自動で分類、収録、検証するマーケット。DeepSeek-Harness コミュニティプラグインマーケットプレイスを自動で分類、キュレーション、検証します。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **69**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-fund-research">PerryLink/dsh-fund-research</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

中国の公開ミューチュアルファンド向け決定論的調査レポートを提供するDeepSeek Harnessプラグイン：ファンドコードを1つ入力すると、パフォーマンス分解、保有銘柄の浸透度、スタイル帰属、明示的なデータ不足の宣言を含むバージョン管理されたMarkdownレポートを出力。指標はモデルではなくコードで計算されます。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **68**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `finance` · `fund-research`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/9a258f42b5375ed7.png" width="100%" alt="PerryLink/dsh-fund-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/c127c0b5eda50892.gif" width="100%" alt="PerryLink/dsh-fund-research animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐60 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness Web GUI の Catppuccin テーマプラグイン：Latte / Frappé / Macchiato / Mocha の 4 種類のテーマをワンクリックで切り替え、オンオフ可能なガラス質感（Glassmorphism）を内蔵

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **60**     |
| 最終プッシュ | 2026-10-12 |
| 初回掲載     | 2026-10-13 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary><b>このカテゴリのその他の項目</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AIコーディングエージェント向けの実行前ガード。ツール呼び出しの実行前に、破壊的なGitおよびファイルシステムコマンドと、機密ファイルへの一般的なアクセス試行を…
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSHプラグインマーケット / DSH Plugin Marketplace：DeepSeek Harness Web GUIでGitHub…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、211个世界与上万素材、开局随心定制、世界自行运转、零漂移存档.
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - グラフィックス、3DGS、空間知能に関する最新論文を継続更新；3D Gaussian Splatting、NeRF、Computer Graphics…
- [arcships/rutis](https://github.com/arcships/rutis) - 自己反復するソフトウェアのためのプラグインランタイム — エージェントが Rust、TypeScript、Python、Go…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness プラグイン集約コミュニティ — dsh-plugin エコシステムを自動同期 · 厳選ディレクトリ · 4…
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 生きた DeepSeek Harness プラグインディレクトリ — 毎時更新、毎日互換性テスト、アプリ内プラグインストアとスキャフォルダー付き.
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana：HanaAgentのサブエージェントとしてのDeepSeek Harness。
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - AI Coding…
- [GDWhisper/dsh-web-startup-auth](https://github.com/GDWhisper/dsh-web-startup-auth) - DSH（DeepSeek Harness）リモート Web 起動 + ユーザー名/パスワード認証プラグイン.
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - DeepSeek Harnessプラグイン：決定論的なデータプロファイリング、クリーニング、検証（dsh-data-quality）。
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagentはAIコーディングエージェント向けのオープンソースFDE Harnessです…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeek Harness上に構築されたオープンソースGrokBot代替.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH)プラグイン厳選ディレクトリ — 14カテゴリ、280以上のコミュニティプラグインを収録し、MCP / Skill…
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - DeepSeek…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：DeepSeek Harness（DSH）ベースのマルチプラットフォームグループチャットエージェントシステム｜DSH…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSHプラグイン：Windows上のすべてのエージェントモード向けGit Bashシェル（pwsh executorを置き換え）。
- [YRN-playmaker/dsh-wallpaper_share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - 壁紙エンジンの各種動的シーン壁紙をワンクリックで同期し、アプリの起動項目を設定するプラグイン.
- [AskTheWay/dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor) - ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH（DeepSeek Harness）Web GUIプラグインコレクション…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH Webプラグイン：GitHub形式のアクティビティヒートマップ、キャッシュヒット率曲線、モデル別内訳による日次トークン使用量統計。
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH プラグインエコシステムの透明なランキングと推薦：dsh-plugin topic を毎日自動取得 + 公開スコアリングモデル +…
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTMLではなく、本物のPowerPoint。何を扱うかをAIに伝えると、pptwiseが自分のマシン上で編集可能なデッキを作成します.
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - デバイス間DeepSeek…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - コーディングエージェント向けのローカル優先コード知識グラフとコンテキストハーネス。MCP＋DeepSeek Harness（dsh）プラグイン.
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - DSH Webプラグイン：サイドバー用の階層型ワークスペースツリー…
- [ddtcorex/govard](https://github.com/ddtcorex/govard) - Magento、Laravel、Symfony、Next.js、WordPressなど向けのGoベースのローカル開発オーケストレーター.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - ローカルのWorkBuddyデスクトップ版にログイン済みのモデル。
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) - DeepSeek…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - DeepSeek Harness (DSH) 向けプラグインの、継続的にメンテナンスされるバイリンガルディレクトリ.
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - DeepSeek…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - DeepSeek…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · DeepSeek Harness機能ドックプラグイン：1つのパネルで全小機能の登録・切り替えを一元管理…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness プラグインの常時互換性テスト：正確なリリース、分離されたランナー、修正可能な上流の問題.
- [liang-today/dsh-liangxiang](https://github.com/liang-today/dsh-liangxiang) - 众香成势，梁子显相。DeepSeek Harness 的 WebUI 插件，欢迎一起打梁.
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - 専用のObsidian vaultにプロジェクト文書と長期メモリをプレーンなMarkdownとして保存するDeepSeek Harnessホストプラグイン.
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - DeepSeek Harness (DSH)…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek HarnessプラグインのX線：宣言された機能と実際の動作を比較。レジストリ + 静的スキャナー + バッジ.
- [ayingQAQ/dsh-web-launcher](https://github.com/ayingQAQ/dsh-web-launcher) - Windows 上的 DeepSeek Harness Web 一键启动器｜One-click launcher with background…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - マルチフォルダーworkspace：DSH。
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - DeepSeek Harness (dsh) 向けの Podman バックエンド実行。
- [kelemiao/dsh-animation-optimization](https://github.com/kelemiao/dsh-animation-optimization) - DSH アニメーション最適化：出力ストリーミングアニメーションと Claude Code 風外観プラグイン。
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - DSH 用ローカルファースト音声会話。任意の外部プロバイダーとともに、自分のマシン上で音声認識と音声合成を実行.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSHプラグイン：ネイティブdsh-better-sidebarタブとして提供されるIDE品質のGitツールウィンドウ…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC モードをベースにした創造モード：DSH プラグイン、Code Mode ツールオーケストレーション + 自己参照 Cordis ツールと preset…
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - DeepSeek Harness (dsh) 向けページ機能キット：ブラウザ UI…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - DeepSeek Harness AgentにGitHubを操作するネイティブな手足を与える!
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh)プラグイン向け依存関係ゼロの検証標準 — 静的構造ゲート (R)、cordis契約チェック…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness プラグインマーケット - dsh-plugin topic プラグインを閲覧、検索、インストール。
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness上のOpenCode — OpenCode Zen +…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness向けのサードパーティ製プラグインマーケットプレイス兼、保護機能付きライフサイクルマネージャー.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx は人間中心の拡張可能なデスクトップワークベンチです。会話、ノート、表、ファイルを同じワークベンチに統合します.
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - デスクトップで DeepSeek Harness を token コストゼロで実行 — macOS と Windows 向けの無料オープンソース GUI.
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Botsワークベンチ：Cordisプラグインによりsdk-botsオーケストレーションゲートウェイをdsh…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - DeepSeek Harness 専用に作られた、Hermes に着想を得たエージェント自己進化プラグインファミリー。
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh)向けコミュニティ版マシン導入・運用スイート：install / start /…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Webプラグイン：market-dashboardサイドバータブを監視…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Wanbinyuが保守する、DeepSeek Harness向け独立系サードパーティープラグインおよびツール。
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - 匿名アクセスまたはオプションのAPIキーを使用して、DeepSeek HarnessでOpenCode Zenの無料モデルを利用。
- [yangzhe1991/dsh-web-enhance](https://github.com/yangzhe1991/dsh-web-enhance) - DSH Web UI 拡張プラグイン：思考チェーンのデフォルト展開、公式 API セッション価格統計、ファイルをシステムプログラムで開く、完了通知 | DSH…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness plugin：WindowsサンドボックスACLのプロビジョニング失敗。
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - 期限を宣言しないdsh tool…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus検証済みのライフサイクルカーネルとCordis互換アダプターを備えたRustプラグインランタイム.
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Cordis / DeepSeek Harness plugin — AI agents向けにGitHub API toolsを正規化。
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - インラインAntigravityダッシュボード：tok/s、DSH形式のキャッシュヒット率、5時間および週間クォータ.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Arkme account, records, chat and interwoven-moments integration for DeepSeek…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh プラグインストア - GitHub topic:dsh-plugin に基づく自動発見と毎時の定期同期。

</details>

<a id="writing"></a>

## 執筆、ディスカッション、動画

mod機能についての解説記事、議論、動画。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 概要

HNの皆さん、これは自分用に作ったものですが、オープンソース化したいと思いました。問題は、特に最近は非常に多くのエージェントを並列処理することが多いため、ターミナルで長時間作業していると、プロンプトの合間にリマインダーを受け取る方法が欲しくなったことです。最初のバージョンは単純なrep

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

##### 📝 概要

上流プロジェクトの説明は公開されていません。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

##### 📝 概要

最新のコーディングモデルではClaudeが難解なコマンドを使ってディープワークモードに入り、何をしているのか分からなくなってしまうため、これを作りました。これは（Claude Codeの新しいfunction hooksを使うプラグインによる）modで、プロンプトの上に1行を表示します：- 現在のステップ、

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `執筆、ディスカッション、動画`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |

##### 📊 データ

| 指標     | 値         |
| -------- | ---------- |
| 初回掲載 | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## 実装言語別のプロジェクト

エコシステムはPythonとTypeScriptに集中していますが、型付きクライアントは他の言語でも増え続けています。この表は掲載項目自体から生成されています。

| 言語       | エントリ数 | プロジェクト例                                                                                                  |
| ---------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| TypeScript | 378        | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                            |
| JavaScript | 78         | `fschmutz/claude-usage-panel`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`               |
| Python     | 40         | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`   |
| Shell      | 26         | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`             |
| HTML       | 15         | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                       |
| Rust       | 5          | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                                 |
| Go         | 4          | `mitre/claude-statusline`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                      |
| PowerShell | 3          | `Gabriel-Dalton/claude-statusline-tokens`, `markallisongit/claude-statusline`, `rainyfei/claude-statusline-win` |
| C          | 2          | `reporails/arcade`, `tylergraydev/cc-mods`                                                                      |
| C#         | 1          | `sakanamaru/dsh-minato`                                                                                         |
| Lua        | 1          | `crafts69guy/claude-statusline.nvim`                                                                            |
| Swift      | 1          | `peaceinitiativemenhadenoil263/claude-status-bar`                                                               |

<sub>言語が明記された項目のみカウントされます。ドキュメントとディスカッションの項目はこの表から除外されます。</sub>

## コントリビューション

修正提案を歓迎します。この一覧を改善する最も迅速な方法です。項目の分類や評価が誤っている場合、または名前の衝突によってプロジェクトが誤って除外されている場合は、issueまたはプルリクエストを作成してください。最後のカテゴリは、自動フィルターが最も誤りやすい部分です。

---

<sub>独立したコミュニティプロジェクトです。Anthropicとは提携、承認、レビューのいずれも受けていません。Claude Code、Claude、AnthropicはAnthropicの商標です。製品の動作は予告なく変更されるため、重要な用途に関わる情報は公式ドキュメントで確認してください。アセットは元プロジェクトに帰属し、ライセンスで許可される場合に限って掲載しています。</sub>

<sub>最終更新 · 2026-10-13T06:19:35+08:00</sub>
