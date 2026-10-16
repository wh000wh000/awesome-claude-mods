<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="すごいClaude Codeモッド">
</p>

<h1 align="center">すごいClaude Codeモッド</h1>

<p align="center"><b>Claude Codeのモッド、プラグイン、およびそれらが変更するより深い挙動を、証拠に基づいて評価するインデックスです。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-607-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **公開中のインデックス** · 最終同期: `2026-10-16T17:05:57+08:00` (UTC+8)
> · エントリ数: **607** · 最新の更新で追加: **0** · 実装言語: **17**

<sub>以下のすべてのエントリは、自動的に収集、フィルタリング、再確認されたものです。ここに有料掲載はありません。</sub>

<a id="featured"></a>

## 今注目のピックアップ

<sub>カテゴリごとに1件掲載し、根拠評価とスター数で順位付けしています。更新のたびに再計算されます。これはランキングであり、推奨を意味するものではありません。各ピックアップから、下にある完全なカードへリンクしています。スクリーンショットまたは記録を公開しているプロジェクトを優先しているため、ストリップの視認性が保たれます。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9530 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2573 · Python · 👁️ observed</sub>
<sub>ゴーストトークンを見つけ出す。修正する。コンパクションを生き延びる。コンテキスト品質の低下を避ける。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐75341 · TypeScript · 👁️ observed</sub>
<sub>🌊 元祖 agent harness。インテリジェントなマルチプレイヤースウォームをデプロイし、自律ワークフローを調整し、対話型 AI システムを構築します。適応型メモリ、自己学習インテリジェンス、フェデレーション、vector RAG 統合、ネイティブの Claude Code / Codex / Hermes…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐16 · 👁️ observed</sub>
</td>
</tr>
</table>

## 目次

- [Claude Codeモッドとは](#claude-codeモッドとは)
- [エントリの評価方法](#エントリの評価方法)
- [公式：Anthropic自身のリポジトリとリリースノート](#公式anthropic自身のリポジトリとリリースノート) — **17**
- [Mod：Mod機能で構築されたもの](#modmod機能で構築されたもの) — **475**
- [DSHおよびCordisのプラグインエコシステム](#dshおよびcordisのプラグインエコシステム) — **105**
- [執筆、ディスカッション、動画](#執筆ディスカッション動画) — **10**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151143 · TypeScript · ✅ official · 0 天</summary>

##### 📝 概要

Claude Code は、ターミナル内で動作し、コードベースを理解し、定型タスクの実行、複雑なコードの説明、git ワークフローの処理をすべて自然言語コマンドで行うことで、より速くコーディングできるよう支援するエージェント型コーディングツールです。

<sub>🔧 コード内で使用されていることが確認されています: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | TypeScript                                        |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **151143** |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9530 · TypeScript · ✅ official · 0 天</summary>

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
| スター       | **9530**   |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8290 · Python · ✅ official · 0 天</summary>

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
| スター       | **8290**   |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6398 · Python · ✅ official · 246 天</summary>

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
| スター       | **6398**   |
| 最終プッシュ | 2026-02-11 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

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
| スター       | **1813**   |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>このカテゴリのその他の項目</b> <sub>· 5</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - mods向けに `$.ui.notify` を追加：自分の通知設定を通じてネイティブ通知を発行し、どのチャンネルが送信したかを示します.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` hook または mod の `prompt.submit` hook 中の Esc…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod。
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod。

</details>

<a id="mods"></a>

## Mod：Mod機能で構築されたもの

ここにある各エントリは、2.1.287でClaude Codeが獲得した機能を使用している証拠を示します。`ui.render`を介して描画する、ペイン・バンド・カードを所有する、`$.ui.selection()`を読み取る、`agent.spawn`でチームメイトを起動する、または自らがModであると明記しているものです。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2573 · Python · 👁️ observed · 0 天</summary>

##### 📝 概要

ゴーストトークンを見つけ出す。修正する。コンパクションを生き延びる。コンテキスト品質の低下を避ける。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | Python                                                                   |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2573**   |
| 最終プッシュ | 2026-10-15 |
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
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐863 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Custom Claude Code Mods that I need

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **863**    |
| 最終プッシュ | 2026-10-14 |
| 初回掲載     | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐606 · JavaScript · 👁️ observed · 0 天</summary>

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
| スター       | **606**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐260 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **260**    |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐218 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **218**    |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐208 · HTML · 👁️ observed · 0 天</summary>

##### 📝 概要

Mods for Claude Code. effortless picks the reasoning effort for every prompt and shows the cache countdown. textless shows art, quotes and chess instead of the wall of text while Claude works.

<sub>🔧 コード内で使用されていることが確認されています: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | HTML                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **208**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `ai-tools` · `anthropic` · `chess` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐196 · TypeScript · 👁️ observed · 11 天</summary>

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
| スター       | **196**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐154 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **154**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐115 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **115**    |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐108 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 コード内で使用されていることが確認されています: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **108**    |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐95 · TypeScript · 👁️ observed · 3 天</summary>

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
| スター       | **95**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

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
| スター       | **80**     |
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Claude Code Mods：プロンプトの上にライブの計画進捗バーを表示

<sub>🔧 コード内で使用されていることが確認されています: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **54**     |
| 最終プッシュ | 2026-10-14 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>アニメーション付きの記録 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐36 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **36**     |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **30**     |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **30**     |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Claude Code mods：Claude Tools メニュー、Zen mode、ターミナルテーマ、effort と mode のコントロール

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **24**     |
| 最終プッシュ | 2026-10-14 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 12 天</summary>

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
| スター       | **22**     |
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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐20 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **20**     |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐15 · TypeScript · 👁️ observed · 13 天</summary>

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
| スター       | **15**     |
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
<summary>🧩 <b><a href="https://github.com/rashedInt32/glass">rashedInt32/glass</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Codeのターミナルトランスクリプトをデスクトップアプリ風にするmod

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **15**     |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `markdown` · `syntax-highlighting` · `terminal-ui`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/rashedint32--glass/c7b07954a39be0b7.png" width="100%" alt="rashedInt32/glass screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 概要

Claude Code内のLINE：Claude Codeモッドとしてのenil TUI

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **15**     |
| 最終プッシュ | 2026-10-13 |
| 初回掲載     | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| スター       | **14**     |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

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
| スター       | **12**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐11 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **11**     |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
| スター       | **10**     |
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code mods that keep context use, plan quota and per-turn cost on screen, plus a guard that stops a session once it goes over budget.

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
| 最終プッシュ | 2026-10-16 |
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
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 12 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary><b>このカテゴリのその他の項目</b> <sub>· 441</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Claude Codeで使用できる100以上のModsのコレクション.
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Darrell WangによるClaude Code Mods — モデルトークンを消費せず、プロンプトの上に帯を表示.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray AmjadのClaude Code mods：ペイン、バンド、プロンプトガード、シークレット処理、メモリツール.
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Claude Code向けのエキスパートSkills、エージェント、コマンド、ルール、フック、出力スタイル…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Modsと、それらを構築するためのtools：builder skill、そしてmods。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 4つのClaude Code Mods：Cache Keeper、Recording Mode、Goal Meter、Collision Guard。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 私が毎日使っているClaude Codeハーネス。初日からこの名前で公開され、現在はucsandman/Agnostic-AIと同じリポジトリです.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude ModsでClaude Codeに屋根を付ける：バイナリを変更せず、システムプロンプトと英語の通知を自分の言葉に置き換えます（2.1.287+）。
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Claude Code内でXcodeのビルド、テスト、コンソール、SwiftUIプレビューを利用。
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code mods についての出典付き Obsidian ナレッジベース：仕組み、作り方、インストール前の確認方法.
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning HackerのClaude Code Mods：エージェントの動作を理解できる形に可視化。
- [kakha13/claude](https://github.com/kakha13/claude) - Claudeが読む前にプロンプトを修正・翻訳するClaude Code Mods。
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code タブ）サイドバーパネル: すべての Claude Code session にある未完了および進行中の ToDo…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code タブ）入力ボックス上部の使用量バー: 5h / 7d quota、token 使用量、コスト.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs による Claude Code mods とスキル。永続的なホームで暮らす AIs が構築し、日々使用しています。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code向けのサイドペイン：セッションが実行するサブエージェント、それぞれの作業内容、トークン、会話にワンクリックでアクセスできます.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code 向けの Claude Mods（function-hooks プラグイン）.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code用のフローティングステータスカード — モデル、コンテキスト、レート制限、コスト、ブランチ…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code エージェントに Claude Mods（function-hook プラグイン）の作成方法を教えるスキル。スターター例付き。
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code。
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 会話エージェントと作業する人間向けの意思決定キューCLI/TUI。エージェントが質問を投稿し、人間が1つの受信トレイから回答します.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - コミュニティ製のClaudeモード、プラグイン、スキルを、1つのマーケットプレイスからインストール。
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss による Claude Code mod。
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code 向けのパネル、ガードレール、利便性向上…
- [timoncool/givememod](https://github.com/timoncool/givememod) - 必要に応じて使えるClaude Code mod…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods ギャラリー：Claude Code mods、チェック済みでピン留め済み.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Claude が動作している間の時間つぶし用タイピングテスト。Claude Code mod.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code mod のアプリストアを Claude Code 内に：/mods で 2,700 個の mod を閲覧、検索、インストール、または…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 6 つの Claude Code mods：プロンプト上部へのプラン制限とコンテキスト表示、権限プロンプト用の許可リストコーチ、subagent…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity、Files、Agents、Context、MCP…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - EditとWriteのdiffを2つの横並び列で描画する Claude Code mod。
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods：ピクセルカニの使用量パネル usage-hud + ターミナル内でクリック可能な HTML…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code用のMods：ターミナルUIにライブペインと動作を追加する関数フックプラグイン。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard は画面共有中に名前と秘密情報をマスクし、cache-panel…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code向けのModとスキン：Claudeのタスク用ライブ進捗バー、対応するWindows…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions。Claude の力を最大限に引き出します.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 多数のセッションを同時に実行するための2つの Claude Code mods：プロンプト上のコンテキストカードと、チャット横のセッションペイン.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - プロンプトボックス上に表示される2つの Claude Code mods：コンテキストウィンドウメーター、5時間制限、プロンプトクロック、セッションコスト。
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 自作 Claude Code mod のプラグインマーケットプレイス。
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Codeが名前を付けたMarkdownファイルを読み込み、セッションの横にレンダリングして表示します.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code 向け GlanceFlow：プロンプト上部に表示される落ち着いたチェックリストで、計画、進捗、Claude…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：コンテキストバー、エージェントパネル、PDPA blur。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：任意のターミナルで、プロンプト上に貼り付け画像のサムネイルを表示。
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 向け音声同僚。ElevenLabs conversational AI 搭載の 3D オオカミと話し合えます.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed、プロンプトごとの統計を備えたライブタイピング速度計。
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 用の Mods：プラグイン function-hooks API で構築したペイン、コマンド、フック。
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - アニメーションデモ、カテゴリリスト、直接のソースリンクで Claude Code mods、プラグイン、拡張機能を発見できます.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：トランスクリプト内にインラインで描画される mermaid 図。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小規模なClaude Code mods（function-hookプラグイン）：session-switcherなど。
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout。
- [LudovicLaloux/agent-crew](https://github.com/LudovicLaloux/agent-crew) - Claude Code mod: see your parallel agents as costumed pixel-art Clawds, in a…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - NarenのClaudeツールキット：Claude Code向けのskills、mods、MCP servers.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 自分が作成した claude code mod の集まり。
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：Claude Code mods を発見、検査、切り替え、更新。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最高の Claude Code Mods：厳選、検証済み、ピン留め済み。1回の /plugin marketplace add で43個の mods.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 本物の Engineers 向け Claude Code mods。
- [Coolkidlab-Yin/agent-mobile-control](https://github.com/Coolkidlab-Yin/agent-mobile-control) - Drive your local Claude Code and Codex sessions from your phone, as chat rooms.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code プラグイン：自動 Claude モデルルーティング.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - コードを書きながら、ゆっくり味が染み込む茶葉蛋を育てる · コーディング中にゆっくり味が染み込む茶葉蛋を育てる。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 向けオープンソースmod：ペイン、ステータス行、トースト、ツールガード、スラッシュコマンド.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod：Claude にポイントごとに、テキスト上で直接回答します.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス。
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 向け Mods：Claude がしていることを演じる小さなピクセルマスコット Clawd。
- [reporails/arcade](https://github.com/reporails/arcade) - クラシックなデスクトップゲームを Claude Code mods として、Claude が作業している間にペインでプレイできます。Reporails 製.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude 用の code-mods。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - グローバルなskills、agents、rules、toolsを、名前付きプロファイルでリポジトリごとにオン/オフできる Claude Code mod.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 テスト済みでワンコマンドインストール可能なClaude Code mods：YOLOモード向けガードレール、ライブコスト・コンテキスト、ペイン、ペットなど.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code。
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - プラグインマーケットプレイスとしてインストールできる、厳選されたClaude Code modのリスト：テーマ、ペイン、ステータスライン、ポートレート.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 2つのClaude Code mods：cache-keeperとctx-mod。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - エージェントの誠実さを保つ Claude Code mods — スコープをガードし、デプロイを検証し、プロンプト上にセッションを描画する function…
- [yocloud-code/claude-vault](https://github.com/yocloud-code/claude-vault) - Claude Code mod: use database, server and cluster credentials without Claude…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin。
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory。
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification。
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 作業中に思いついたことを記録し、プロジェクトやマシン間で振り分け、プロンプトに変換するClaude Codeモッド。
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - HermanのClaude Code mods（マーケットプレイス herman-mods）。
- [jrlprost/claude-code-mods](https://github.com/jrlprost/claude-code-mods) - Claude Code mods I build because I need them: context bar, plugin toggler, and…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code mod：すべてのサブエージェントのモデルと推論 effort を選択。
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Codeプラグイン（mod）：Claude CodeのターミナルUIをClaudeデスクトップアプリのようにします.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Codeがバックグラウンドで実行しているものを確認：サブエージェント、Codexジョブ、シェル、モニター、cronジョブ、ワークフロー.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows 上の Claude Code mods に関する初日のフィールドノート：コンテキスト／クォータの燃料バー、タイ語 UI mod、Matrix…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup。
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better。
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：プロンプトの上にライブのコスト、コンテキスト、プランクォータメーターを表示。アイコンには Nerd Font が必要.
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs。
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈。
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band。
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin and mod: hook によって強制される human approval gates とプロンプト上の status…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 失敗した Claude を叩く — Claude Code 用のストレス解消 mod：漫画風のお尻、8つの叩き、9つのお尻、マーク、コンボ、サウンド.
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar and a status line for Claude Code: usage limits, context, model…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Codeで作業しながら外国語を身につけましょう。
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude…
- [CircularBlox/Clarity](https://github.com/CircularBlox/Clarity) - A clearer Claude Code terminal: boxed and organized you/claude conversations…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 会話中の未完了項目を継続的に一覧化し、プロンプト上部の帯に表示するClaude Code Mod.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 各 Claude Code エージェントがどのファイルをコンテキストに持っているか、そしてそれぞれの量を確認できます.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - ターミナルとデスクトップアプリ向けの小さな Claude Code mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - エージェントの返信にスペイン語の単語を追加する Claude CLI スキル + mod。
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Claude Codeのプロンプト上部にFloateeのバックログを表示：ワンクリックでTODOを実行、案内、完了できます.
- [fredrikbonde/claude-context-bar](https://github.com/fredrikbonde/claude-context-bar) - Claude Code mod: context window as a stacked bar above the prompt。
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [gabriel9004/claude-code-mods](https://github.com/gabriel9004/claude-code-mods) - Mods para Claude Code: panel de agentes y tareas con cuota y caché, y banda de…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Claude Codeが独自のメーターを描画する方法で、プロンプト上部に1行として表示するコンテキストウィンドウ.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Codeの回答を待っている間に、注意をそらさないようにします.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code 用の無料オープンソースプラグイン。/clear する前に、Claude…
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [markfulton/safe-keys](https://github.com/markfulton/safe-keys) - Paste an API key into Claude Code. Nothing keeps it.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session。
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：ドキュメントのファクトチェッカー、コード監査ツール、バグメモリーログ、mod など.
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [reeny404/mod-hud](https://github.com/reeny404/mod-hud) - Claude Code mod: see which session is waiting on you at a glance, and hatch a…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：Claude の返信とあなたのプロンプトをリクエストに応じて音読する Claude Code mod.
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [tlq5l/afk-timer](https://github.com/tlq5l/afk-timer) - Claude Code mod: shows how long you。
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop。
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：ライブペイン、コストを意識したモデルルーティング、安全ガードのための小さなプラグイン.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod &amp; plugin：使用量モニター、トークントラッカー、ステータスライン.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude Codeモッド：EMCC（Every Mod Claude Code）、Claude Code向けの厳選・テスト済みモッドコレクション。
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [Abdoul-sudo/prompt-enhancer](https://github.com/Abdoul-sudo/prompt-enhancer) - Claude Code mod: rewrites vague prompts using the active project。
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace)。
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [AJMarquez99/prompt-pin](https://github.com/AJMarquez99/prompt-pin) - Pin your latest prompt above the input and browse this session。
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alanrsoares/claude-mods](https://github.com/alanrsoares/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code プロンプトの上に表示するアニメーション付きの点字猫。
- [almost99/claudecode-mods](https://github.com/almost99/claudecode-mods) - Approved Claude Code Mods。
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Codeのプロンプト上部でOmniDimension音声エージェントのテスト通話を実行するピクセル猫。Claude Code mod.
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - コンテキストウィンドウを小さく保つため、コンパクションに適したタイミングを選ぶ Claude Code mod。
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code向けClaude…
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code 用の汎用 Mods：バンド、ペイン、トースト、フック.
- [androidZzT/cc-moyu-kit](https://github.com/androidZzT/cc-moyu-kit) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [AnnihilationWizard/secret-guard](https://github.com/AnnihilationWizard/secret-guard) - A Claude Code mod that adds a gitleaks pre-commit hook to each Git project you…
- [apiglue/claude-mods](https://github.com/apiglue/claude-mods) - Mods for Claude Code。
- [arjunkambj/claude-mods](https://github.com/arjunkambj/claude-mods) - Arjun。
- [Arkboi-GG/claude-mods](https://github.com/Arkboi-GG/claude-mods) - A small collection of Claude Code mods。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - アニメーションする村人の体力カードとして表示するあなたのClaudeの使用上限と、週次ペースの警告 — Claude Code mod。
- [astromelon/takgon-mods](https://github.com/astromelon/takgon-mods) - 개인 Claude Code mods 플러그인(takgon-mods)。
- [astrosteveo/nebula](https://github.com/astrosteveo/nebula) - Claude Code mods and plugins。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude の作業中に短いワークアウト：日次目標、連続記録、バッジ、任意のリーダーボード。Claude Code mod.
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [bardaxx/modsbook](https://github.com/bardaxx/modsbook) - A book of Claude Code mods: side panes, bands, status lines and hooks, each one…
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods: live panes, bands and guards that run inside Claude Code。
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code向けNow Playing mod：プロンプト上部にApple MusicとSpotifyを表示し、カバーアート、コントロール、Up…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [bharath-gp/ai-harness](https://github.com/bharath-gp/ai-harness) - Claude Code plugin marketplace: guardrails and cockpit mod bundles。
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 用 Mods：Cache-Uhr、Blast Radius、Vorschlaege、Arbeitsliste、Grill。
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - あなたの Claude Code のためのただのフクロウ。
- [chinayuren2022-2025/claude-english-coach](https://github.com/chinayuren2022-2025/claude-english-coach) - Claude Code mod: practise English by working with Claude in English only…
- [CladiusIV/claude-mods](https://github.com/CladiusIV/claude-mods) - A Claude Code plugin marketplace of mods: changes to Claude Code。
- [coil398/claude-session-brief](https://github.com/coil398/claude-session-brief) - Claude Code mod: session summary band, subagent and hook activity above the…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [davidyerm/claude-mods](https://github.com/davidyerm/claude-mods) - Mods for Claude Code。
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [diegocamara89/claude-mods](https://github.com/diegocamara89/claude-mods) - Mods do Claude Code (function hooks): Sonnet por padrão para subagentes…
- [DimeDataCloud/open-ClaudeOS](https://github.com/DimeDataCloud/open-ClaudeOS) - Claude mods interactive operating system。
- [Djdhmf/clawd-office](https://github.com/Djdhmf/clawd-office) - A Claude Code mod: a living 8-bit office of Claude crabs in a side panel that…
- [Djdhmf/prompt-enhancer](https://github.com/Djdhmf/prompt-enhancer) - A Claude Code mod: a pixel-art librarian crab above your prompt that rewrites…
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [Elmanuel1/claude-mods](https://github.com/Elmanuel1/claude-mods) - Claude Code mods: docs-watch。
- [EslamHanafy/delegate-watch](https://github.com/EslamHanafy/delegate-watch) - Live Claude Code pane that shows what your delegated coding agents。
- [evertonalves-ai/mod-forge](https://github.com/evertonalves-ai/mod-forge) - Claude Code skill that builds, debugs, audits and packages Claude Code mods…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods（function-hookプラグイン）：session-meterなど。
- [FunJim/claude-code-add-to-chat](https://github.com/FunJim/claude-code-add-to-chat) - Codex-style Add to chat for Claude Code: annotate any part of a reply, send all…
- [gnehiur/claude-code-volc-tts](https://github.com/gnehiur/claude-code-volc-tts) - Claude Code mod：用火山引擎豆包语音流式朗读 Claude 的最终回复（暂停/继续/倍速/缓存）。
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [gwarf/claude-plugins](https://github.com/gwarf/claude-plugins) - Claude Code mods by gwarf: a plugin marketplace。
- [gyoomun/claude-mods](https://github.com/gyoomun/claude-mods) - 다른 사람이 만든 Claude Code 모드를 내 작업 방식에 맞게 고친 것 (coach-on-call, next-steps-multi)。
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [heidiks/agent-kit](https://github.com/heidiks/agent-kit) - Skills, plugins and Claude Code mods. Install only what you need.
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HikiJun97/claude-mods](https://github.com/HikiJun97/claude-mods) - Personal Claude Code mods。
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code mod：各回答にかかった時間、Claudeの思考時間、tok/sを、Claudeデスクトップアプリの返信直下に表示します.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian。
- [ijat/prompt-polish](https://github.com/ijat/prompt-polish) - Claude Code mod that cleans up voice-dictated prompts and teaches the fix。
- [intent-driven-dev/claude-mods](https://github.com/intent-driven-dev/claude-mods) - Claude Code mods: live panes and hooks for everyday workflows。
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [jambolo/claude-mods](https://github.com/jambolo/claude-mods) - Mods for Claude Code。
- [jasoncai0/claude-session-hud](https://github.com/jasoncai0/claude-session-hud) - Claude Code mod: rate-limit usage, Codeup MRs and the session。
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - サイドバーのコンテキスト使用量パネル：総量、分類、各ターンの増加量、最も場所を取っている上位項目、キャッシュ、Claudeが現在行っていること.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - サイドバーのファイル一覧：この会話で新規作成、変更、削除されたファイルと、それぞれの変更行数。/filesで表示・非表示（Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8ビット風の毛毛（白黒のホーランドロップイヤー）が入力欄の上で走り跳ねます：待機中は平たくなり、作業中は走り、ツール使用中は跳ねます。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - サイドバーの「私が尋ねたこと」：この会話で主人が入力したすべての文を、クリックして全文表示、コピー、入力欄に戻せます.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - サイドバーのタイムライン：このターンで時間を費やした対象（モデル待ち、思考、記述、コマンド実行、ネットワーク、ファイルの読み書き、ヘルパー待ち）.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - サイドバーのトークンのやり取り：メイン会話がAnthropicに送ったトークン数、待ち時間、受信数を表示し、最上部に合計を示します.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude codeの正直な豆沙包：各ターンの回答後、Claudeが心の内を小声で一言語ります（Claude Code mod）。
- [jiroamato/claude-mods](https://github.com/jiroamato/claude-mods) - Jiro。
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jonirafael/claude-code-mods](https://github.com/jonirafael/claude-code-mods) - Claude Code mods: context-receipt (per-turn context breakdown) and…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [Jsolee/claude-mods](https://github.com/Jsolee/claude-mods) - Mods de Claude Code de Joan Solé: comunitat, el panell dels subagents amb el…
- [jumpei-kurata/claude-mods](https://github.com/jumpei-kurata/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd は Claude Code プロンプト上部の帯に住みます：セッションを演じ、実行中のもの、コンテキスト、使用制限を表示し、CI ビルドと競走します.
- [kaisudo0520/cc-dashboard](https://github.com/kaisudo0520/cc-dashboard) - Live mission-control pane for Claude Code: Fable and Codex usage, branch review…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code の返答や通知を VOICEVOX / Irodori-TTS などで読み上げる mod。
- [kargarisaac/subagents-tree](https://github.com/kargarisaac/subagents-tree) - Claude Code mod: a docked pane showing every subagent as a tree with model…
- [katipally/modz](https://github.com/katipally/modz) - Claude Code mods: install with /plugin install &lt;mod&gt; --marketplace…
- [keithwalsh/claude-code-mods](https://github.com/keithwalsh/claude-code-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [Krishna30396/Pixel-Progress](https://github.com/Krishna30396/Pixel-Progress) - A pixel progress bar with time left for Claude Code: tasks done, percent and…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high。
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [lperezmo/cache-caffeine](https://github.com/lperezmo/cache-caffeine) - Claude Code mod: keeps the prompt cache warm while you step away, and wakes…
- [lperezmo/session-relaunch](https://github.com/lperezmo/session-relaunch) - Claude Code mod: /relaunch reopens the current session in a new terminal tab so…
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Claude Code mod: guards the 1-hour prompt cache of idle sessions — countdown…
- [m-aoki1348125/next-compass](https://github.com/m-aoki1348125/next-compass) - Claude Code mod: four predicted next instructions in four directions, and a…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claudeが行っていることをiTerm2タブのサブタイトルに表示し、タブバーを一目見るだけでどのセッションに対応が必要か分かるClaude Codeモッド。
- [macollins27/owner-rep](https://github.com/macollins27/owner-rep) - A Claude Code mod that watches the coding agent for the person who owns the…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude。
- [Marceux-Croix/Claudeopticon](https://github.com/Marceux-Croix/Claudeopticon) - A process monitoring and ticket system for Claude Code: your todo as a live…
- [Marensius-Andersen/auto-model](https://github.com/Marensius-Andersen/auto-model) - Claude Code mod: picks the cheapest model that fits each prompt。
- [marwansaab/Claude-Mods](https://github.com/marwansaab/Claude-Mods)
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code向けコミュニティmods：Claude Code内で実行されるガード、ペイン、コマンド。Marketplace：modhub。
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace。
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you。
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - セッション開始時にCLAUDE_CODE_ENABLE_TODO_TOOLSを設定し、todoツールを省略するモデル向けに再び有効化するClaude Code…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 安全に一時停止できるまで待ち、その後セッションを引き継ぐかコンパクト化する Claude Code mod.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code mod：プロンプト上部にタスクリストを1行ずつ表示し、現在のタスク、進捗バー、件数を示します。ターミナルとデスクトップアプリで同じ外観.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 内で AI と Connect Four をプレイ (/connect-four)。
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 複数のAIエージェントで共有するリポジトリ向けのClaude Code…
- [narley/sessions-sidebar](https://github.com/narley/sessions-sidebar) - Claude Code mod: a sidebar listing every Claude Code session, for Warp。
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude…
- [oklahaha/deepseek-balance](https://github.com/oklahaha/deepseek-balance) - Claude Code mod: DeepSeek balance gauge, today。
- [osinelnikov/activity-dashboard](https://github.com/osinelnikov/activity-dashboard) - Claude Code mod: live activity pane with time, tokens, agents, cost and PDF…
- [pappusinghadip/pappu-claude-mods](https://github.com/pappusinghadip/pappu-claude-mods)
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack：Claude Code mod。読み取り専用の先行開始機能を備えた永続的なworktrees、crew dials、context…
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [phatjam98/claude-mods](https://github.com/phatjam98/claude-mods) - Claude Code mods by phatjam98。
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - ClaudeデスクトップアプリのCodeタブ用ライブセッション統計サイドペイン：コンテキスト、コスト、gitの変更、ターン統計、サブエージェント、ログ.
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [poska-lab/cc-work-buddy](https://github.com/poska-lab/cc-work-buddy) - Unofficial Claude Code mod: a little Claude above your prompt that shows what…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [PurpleDotStudio/claude-mods](https://github.com/PurpleDotStudio/claude-mods) - Claude Code mods: a side panel for what the session needs from you。
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code。
- [r1305/claude-mods](https://github.com/r1305/claude-mods) - Mods para Claude Code: enrutado de modelos con dashboard de consumo y…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace。
- [reedchan7/claude-mods-pulse](https://github.com/reedchan7/claude-mods-pulse) - Pulse: live TTFT, tok/s, prompt-cache hit rate and usage left in Claude Code。
- [retogo/claude-media-view](https://github.com/retogo/claude-media-view) - A Claude Code mod that shows images and GIFs inline in the terminal — and lets…
- [revilo-digital/second-opinion](https://github.com/revilo-digital/second-opinion) - Claude Code mod: ask OpenAI, Gemini or Grok for a second opinion on Claude。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：Claudeが作業している間に行う腕立て伏せ。トークンなし.
- [Roberdinho/claude-mods](https://github.com/Roberdinho/claude-mods) - Claude Code mods: prompt-polaroid makes CodeSnap-style Polaroids of your prompts。
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain：ELI5からpolicy engineeringまで、フィールドテストとファシリテートされたチュートリアルを含むClaude Code…
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [RuahTechSolutions/code-buddy](https://github.com/RuahTechSolutions/code-buddy) - Claude Code mod: staging guard, blast radius, edit replay and an agents panel…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：プランモードで承認した計画をプロンプトの上にライブチェックリストとして表示し、Claude が完了するたびに各ステップをチェック。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 厳選したClaude Code modsの一覧。各項目をクローンしてclaude plugin validateで確認し、アクセス可能な対象をタグ付け.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - コスト不要モード：ヘルパーエージェントはHaikuで動作し、大きなファイルやログはClaudeのコンテキストを埋める代わりに無料のGeminiモデルで要約される…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - セッションに寄り添うlofiサウンドトラック：落ち着き、集中、フローに加え、テストの成功と失敗を知らせる合図。オリジナル音楽.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claudeがコードを書く間に学習：コードを変更したターンの後、その変更自体についての質問がプロンプトの上に1つ表示される。概念ごとに採点.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claudeが行うすべての編集を記録：各変更が入力される様子を再生し、ステップごとに進み、任意のファイルを任意のステップへ巻き戻す.
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them。
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - A Claude Code mod: a project dashboard and isometric city map of tasks, agents…
- [schudarin/chudarin-context-mod](https://github.com/schudarin/chudarin-context-mod) - A Claude Code mod: a side panel that shows what fills your context, how much of…
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker。
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Claude Code modsのカスタムマーケットプレイス（cc-mods）。Anthropicのサンプルmodsをベンダリング済み。
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 踊るピクセルアートのMalenia付き、Claude Code用ワンクリックコミットメッセージ。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - tanmenによる非公式Claude Code mods（マーケットプレイス：tanmen）。
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 現在のセッションをペインに表示するClaude Code…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - modのClaude Codeプラグインマーケットプレイス: Claude…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace。
- [timoranjes/agent-arcade](https://github.com/timoranjes/agent-arcade) - Playful live view of Claude and its subagents: animated dashboard, stats band…
- [tyler4400/tyler-claude-mods](https://github.com/tyler4400/tyler-claude-mods) - Claude Code plugins: status-card (会话状态卡片) &amp; session-title (智能自动标题) — Live…
- [UlongChaS2/learn-trail-mods](https://github.com/UlongChaS2/learn-trail-mods) - Claude Code mod: 설명의 목차를 패널에 띄우고 항목별 설명을 저장해 /recall 로 다시 본다。
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [user0027/claude-mods](https://github.com/user0027/claude-mods)
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code mod：長時間実行タスク用のアニメーション進捗帯と完了サマリー。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 3つの小さなClaude Code…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 「I。
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 作業の隣のペインでClaudeに別の質問をできます。メインの会話には決して表示されません。デスクトップアプリの/btwのように機能します.
- [vdvoorder/filemap](https://github.com/vdvoorder/filemap) - A Claude Code mod that draws a git repository as a treemap in a side pane and…
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vmlinuz82/claude-mods](https://github.com/vmlinuz82/claude-mods) - Claude Code mods: a task checklist and a skill/MCP usage band, for the terminal…
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac。
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wonjangcloud9/wj-mods](https://github.com/wonjangcloud9/wj-mods) - Claude Code mods: cross-session work progress pane, usage band, long-turn…
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Claude Code mod 모음 (wonr-mods 마켓플레이스)。
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Codeプラグイン：Claude…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude…
- [ya8282/claude-code-mods](https://github.com/ya8282/claude-code-mods) - Small productivity mods for Claude Code。
- [Yumbang/scopus-for-dobby](https://github.com/Yumbang/scopus-for-dobby) - Stateful CLI for searching, collecting, and managing academic papers from the…
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [zhuobichen/zhaowen-claudemod](https://github.com/zhuobichen/zhaowen-claudemod) - 我自用的 Claude Code mod 合集（function hooks）：以 marketplace 形式分发，/plugin install 装。
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 最高のエージェント向けリソースを厳選したコレクション。Claude…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 何が起きているかを表示する Claude Code プラグイン - コンテキスト使用量、アクティブなツール、実行中のエージェント、todo の進捗。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline サポート、テーマなどを備えた、Claude Code CLI 用の美しく高度にカスタマイズ可能な statusline.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code のシステムプロンプトの全パート、27…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Claude CodeとCodex向けAI動画スキル…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code を最大限に活用するための 45+ のヒント。基本から高度な内容まで…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — 小紅書カルーセルとWeChat 21:9+1:1カバーペアを生成.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - ターミナルペインでコーディングエージェントの差分をレビューし、行コメントをClaude Code、Codex、OpenCode、Piに送り返します.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - コンテキスト使用量、APIレート制限、コスト追跡に対応したClaude Code用包括的ステータスラインプラグイン。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code用のModを構築：あらゆるリクエストをフックし、あらゆるレスポンスを変更し、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：Claude Codeセッションのカーボンフットプリントを追跡。
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公開Claude CodeスキルとMods。
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun。
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code用のSkills、Mods、サブエージェント、フック、スラッシュコマンド、ガイド…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法的に無料で使えるLLM APIsとコーディングAgent — 自動更新され、週2回プローブ検証。無料枠、カード不要のトライアル、無料モデル.
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - コーディングエージェントをキーボードファームウェアの専門家に変えるAgent Skill.
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude…
- [LikeACloud7/awesome-frontier-ai-papers](https://github.com/LikeACloud7/awesome-frontier-ai-papers) - Daily tracker for frontier AI lab papers, model cards, system cards, and…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [romacv/claude-plan-usage-statusline](https://github.com/romacv/claude-plan-usage-statusline) - Claude Code status line showing model, usage limits, git info, and workspace…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code、pi、DeepSeek Harness 向けプラグイン集：ステータスバー HUD、タスク進行バー、Tailscale ノード状態など…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture向けのポータブルなClaude…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - ポータブルな Claude Code グローバル設定：カスタムスキル、PreToolUse フック、カスタム statusline.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop の Code タブ向け非公式 mods — usage-pet：アニメーションするピクセルペット Clawd 付きの使用量バンド.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 毎日使っているClaude Codeプラグイン：誰のマシンでも動作するよう整理したskillsとmods.
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - ドラッグ＆ドロップエディタ付きの Claude Code 用カスタマイズ可能なステータス行。
- [MindLab-Research/dsh-generative-ui](https://github.com/MindLab-Research/dsh-generative-ui) - Generative UI for DeepSeek Harness — the agent writes TSX and the web UI…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [wide3751/switchboard](https://github.com/wide3751/switchboard) - A Claude Code plugin (mod) that shows every local Claude Code session in one…
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - ゲーム Hytale の mods を容易にするための Claude Code Plugins と Skills のマーケットプレイス。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media mods のリポジトリ.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [michalschroeder/claude-statusline](https://github.com/michalschroeder/claude-statusline) - My Claude Code statusline + supporting hooks。
- [OFurtun/claude-custom-statusline](https://github.com/OFurtun/claude-custom-statusline) - Furtun。
- [RaggioS/claude-code-statusline](https://github.com/RaggioS/claude-code-statusline) - Single-file POSIX statusline for Claude Code: dir, git branch, model, context…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [faleiro-thiago/claude-skills-mods](https://github.com/faleiro-thiago/claude-skills-mods) - Facilitadores pessoais para Claude Code, versionados por item。
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン。
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline。
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [31c0c3/claude-statusline](https://github.com/31c0c3/claude-statusline) - One-line Claude Code status line in bash and jq: context, cache, limits, cost。
- [afarrell/claude-meter](https://github.com/afarrell/claude-meter) - Minimal Claude Code statusline — context bar, 5h bar, and 7-day rolling…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games。
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - Personal Claude Code plugin marketplace (todo-pane)。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - プロ仕様のClaude Codeステータスライン：セッション時間、ECB為替レートによる複数通貨コスト、MTokあたりの料金、支出上限.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramodのClaude Codeプラグインを1つのマーケットプレイスに：Claude Code用のエージェントスキルとライブペイン.
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Claude Code のステータスライン：コンテキスト、制限と週ごとのペース、リポジトリの CI、デプロイと PR、そしてマシンの状態。
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Two-row status line for Claude Code: context, rate limits with pace markers…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust。
- [federbenjamin/claude-statusline](https://github.com/federbenjamin/claude-statusline) - A two-line Claude Code status line showing branch, PR, model, context, cost…
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [itamartz/ClaudeCode-Mods](https://github.com/itamartz/ClaudeCode-Mods) - A Claude Code plugin marketplace of personal mods: hooks, panes and commands…
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [LemonYangZW/cc-mods](https://github.com/LemonYangZW/cc-mods) - Practical, low-distraction mods for Claude Code。
- [LiamMorganDev/claude-setup](https://github.com/LiamMorganDev/claude-setup) - My complete Claude Code setup: mods, skills, commands, hooks and CLAUDE.md…
- [lover40x/claude-browser-comment-mod](https://github.com/lover40x/claude-browser-comment-mod) - Claude Browser Comment Mod: click an element on your dev server, leave a…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [Monte9/claude-memory-mods](https://github.com/Monte9/claude-memory-mods) - Curate Claude Code&#x27;s own memory files: a pane to view every project&#x27;s memory…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [n0nuser/claude-statusline](https://github.com/n0nuser/claude-statusline) - 3-line status bar for Claude Code — model, context usage, cost, git status, and…
- [nhooey/claude-code-usage-statusline](https://github.com/nhooey/claude-code-usage-statusline) - A Claude Code status line and per-turn cost readout in one program: token…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [Recokioshi/claude-kit](https://github.com/Recokioshi/claude-kit) - a set of useful skills and mods for claude code。
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - カスタムClaude Codeステータスライン（上流：kamranahmedse/claude-statusline）。
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company。
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Claude Code向けUniversal Multi-Protocol StatusLine、Context…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Codeエージェント向けプロアクティブAIメモリおよびレート制限モニター。
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Codeのフック、サブエージェント、ステータスライン：種類ごとにまとめられ、セキュリティ評価済みのオープンソースコレクションとツール.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 向け Mods：function hooks 上に構築されたペイン、バンド、バディ。
- [ryanclark/statusline](https://github.com/ryanclark/statusline) - Simple status line for Claude Code showing context window/usage limits。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Claude Code セッション間でタスクを受け渡します。変更を、リポジトリを所有するセッションに渡します.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：Claude Code に何度も頼んでいることを見つけて、mod に変換します。さらに8つのサンプル mods と仮想オフィス付き.
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - CAD/CAM と機械制御用ツールを含む、Fablabs 向けのモジュール式クロスプラットフォームツール MODS を制御するための MCP サーバー内のもの.
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Claude…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - ローカル LLM で CK3 mods を翻訳するための Codex および Claude Code スキル。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code 向けのオープンソース mods とその他の拡張機能。
- [Grandullon/diariovida-mods](https://github.com/Grandullon/diariovida-mods) - Mods gratis para Claude Code: entiende lo que hace Claude, mejora tus prompts y…
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability。

</details>

<a id="dsh-cordis"></a>

## DSHおよびCordisのプラグインエコシステム

DeepSeek HarnessとCordisは、異なる方向から同じ場所に到達します。両者にとってプラグインはmodの仕組みであり、そこでのプラグインはここでいうmodに相当します。

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250780 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 コード内で使用されていることが確認されています: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **250780** |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐75341 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **75341**  |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4651 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

DSH 公式の最推奨 TUI プラグイン——高性能、低負荷、かわいいピクセルのクジラ、スムーズなマウス操作。npm でワンコマンドインストール。 / DSH 公式首推的 TUI プラグイン、高性能低占用、可爱像素鲸鱼、流畅鼠标交互、npm 一键安装

<sub>🔧 コード内で使用されていることが確認されています: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4651**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐725 · Python · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My Pi、Grok、OpenCodek DSH、Kimiなど、AIアシスタント向けの優れたAIプラグインの厳選リスト。https://hol.org/plugins

<sub>🔧 コード内で使用されていることが確認されています: `README.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | Python                                                                   |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **725**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐279847 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **279847** |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101429 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **101429** |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84234 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **84234**  |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/80b6efa0c1ca677d.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35817 · Go · 🔎 inferred · 0 天</summary>

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
| スター       | **35817**  |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐31033 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness (DSH)プラグインエコシステムのために構築された、モダンなデスクトップソリューション。すべてが「プラグイン」であり、デスクトップ自体も「プラグイン」です。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **31033**  |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25677 · Python · 🔎 inferred · 3 天</summary>

##### 📝 概要

Distilly — 彼らの思考方法を、あらゆるAgentやBotで再利用できるSkillsに蒸留します。以前は Colleague Skill（原同事 Skill）。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **25677**  |
| 最終プッシュ | 2026-10-13 |
| 初回掲載     | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐18533 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **18533**  |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/a67bb180136008be.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EverMind-AI/EverOS">EverMind-AI/EverOS</a></b> · ⭐13446 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **13446**  |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-memory` · `agentic-ai` · `ai` · `chats` · `clawdbot` · `clawdbot-skill` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/evermind-ai--everos/1c468e299d8b9fe7.png" width="100%" alt="EverMind-AI/EverOS screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8812 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness (DSH) Web プラグイン集約エコシステム · すべてがプラグイン、クリエイティブワークショップ経由で配布｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **8812**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/loopx-project/loopx">loopx-project/loopx</a></b> · ⭐6334 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

A control plane with a durable state kernel for long-horizon agents and teams. Keep work moving and improving across sessions, with less human attention.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6334**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-control-plane` · `agent-harness` · `ai-agents` · `claude-code` · `codex` · `dsh-plugin` · `local-first` · `long-horizon-agents`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/8582e0735bb2d9e1.webp" width="100%" alt="loopx-project/loopx screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/34519ef8d110de64.gif" width="100%" alt="loopx-project/loopx animation"><br><sub>アニメーション付きの記録 · <a href="https://raw.githubusercontent.com/loopx-project/loopx/main/docs/assets/personal-workspace/loopx-dashboard-launch.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Q00/ouroboros">Q00/ouroboros</a></b> · ⭐6231 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6231**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-os` · `agentic-ai` · `ai-agent` · `ai-coding-agent` · `claude-code` · `cli` · `codex` · `coding-agent`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/5b0b313f6f066fb8.png" width="100%" alt="Q00/ouroboros screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/099492564830e817.gif" width="100%" alt="Q00/ouroboros animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4275 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4275**   |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4206 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, side chat, Git, and sub-agent pages.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4206**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/5570cd36873fb95c.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>アニメーション付きの記録 · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3495 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

HTML で回答 — 実際に読める1ページの HTML で難しい質問に答える agent skill。AI Agent に1ページの HTML で複雑な質問へ回答させます。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3495**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3458 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

ローカルプライベート型、オープンソースの自己進化クロスプラットフォーム AI コンテンツ発見 Agent：まずあなたを理解し、その後 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博などのプラットフォームやオープン Web から主体的にコンテンツを探します。（deepseek harness プラグインに対応） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3458**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3056 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3056**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐2413 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2413**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/T-Auto.png?size=160" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2185 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, agent teams, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板、浏览器、侧栏、命令，透视上下文组成、演进、压缩、多 Agent等。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2185**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐2039 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **2039**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1208 · Go · 🔎 inferred · 0 天</summary>

##### 📝 概要

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Go                                                                                             |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1208**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/TencentCloudBase/CloudBase-AI-Toolkit">TencentCloudBase/CloudBase-AI-Toolkit</a></b> · ⭐1138 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Backend for AI coding agents on CloudBase — database, auth, functions via Plugin, Skills & MCP.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1138**   |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-skills` · `ai` · `aicoding` · `claude-code` · `cloudbase` · `cursor` · `database` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tencentcloudbase--cloudbase-ai-toolkit/9b9897d8b439ac14.png" width="100%" alt="TencentCloudBase/CloudBase-AI-Toolkit screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐709 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **709**    |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

📚 依存関係ゼロで git に支えられた、AI Agents が検証済みのデバッグ経験を非同期に共有・検索するためのマイクロレッスンライブラリ。 | https://misakanet.org

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
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zenstory-ai/oh-story-dsh">zenstory-ai/oh-story-dsh</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek 写网文/小说的工作流插件：DeepSeek Harness 社区插件，内置小说、短剧、游戏、视频解说四个工作台 | Community DeepSeek Harness plugin with novel, short-drama, game and video-recap workbenches.

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
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-skills` · `ai-agents` · `ai-novel-writing` · `ai-writing` · `claude-code` · `creative-writing` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zenstory-ai--oh-story-dsh/03bef6389f0bf9ba.gif" width="100%" alt="zenstory-ai/oh-story-dsh screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zenstory-ai--oh-story-dsh/03bef6389f0bf9ba.gif" width="100%" alt="zenstory-ai/oh-story-dsh animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐277 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **277**    |
| 最終プッシュ | 2026-10-15 |
| 初回掲載     | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **256**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness のスキン変更／壁紙／テーマパックプラグイン (dsh-plugin) — 8種類の Mirage テーマ、ユーザーごとのアクセントカラー、壁紙2.0、テーマパックのインポート・エクスポート／共有リンク、お気に入りとランダム選択を、完全ネイティブな token システムで実装。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **247**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dshplugin/dsh-plugin-hub">dshplugin/dsh-plugin-hub</a></b> · ⭐232 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 10000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、搜索、安装各类 AI 插件。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **232**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent` · `ai` · `cli` · `community-plugins` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `dsh-plugin-org`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dshplugin--dsh-plugin-hub/7dd84080ee0003e9.png" width="100%" alt="dshplugin/dsh-plugin-hub screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐206 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

TypeSafe JevまたはlunaのようなDecision apiをSystem One意思決定レイヤーとして統合し、Agentの選択、監督、修正、承認を行うネイティブDeepSeek Harness (DSH)プラグイン。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **206**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐199 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **199**    |
| 最終プッシュ | 2026-10-16 |
| 初回掲載     | 2026-10-16 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary><b>このカテゴリのその他の項目</b> <sub>· 71</sub></summary>

- [cordiverse/cordis](https://github.com/cordiverse/cordis) - 時空間コンポーザビリティのメタフレームワーク。
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AIコーディングAgent向けの実行前ガード。ツール呼び出しの実行前に、破壊的なGitおよびファイルシステムコマンドに加え、機密ファイルへの一般的なアクセス試行…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [sixtysevenlf/dsh-blender-plugin](https://github.com/sixtysevenlf/dsh-blender-plugin) - DSH x Blender direct realtime plugin v2.0 — an AI drives Blender over a direct…
- [xiajiajun516/dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) - DeepSeek Harness (DSH)のバックアップ＆復元プラグイン…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSHプラグインマーケット / DSH Plugin Marketplace：DeepSeek Harness Web GUIでGitHub…
- [Nwflower/dsh-claude-style](https://github.com/Nwflower/dsh-claude-style) - Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的…
- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - DeepSeek Harness plugin for previewable cross-preset session migration.
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - インストールすると mattpocock/skills v1.3.1 の 27…
- [yannicksong0106/dsh-550c-boot](https://github.com/yannicksong0106/dsh-550c-boot) - 550C 开机动画 for DeepSeek Harness — 首帧由宿主半边注入，DSH 的 Loading 卡片不露脸；桌面原生标题栏按钮收编成终端配色…
- [drewnekota/cetus](https://github.com/drewnekota/cetus) - One macOS app for Claude Code, Codex, and every agent runtime you use…
- [arcships/rutis](https://github.com/arcships/rutis) - 自己反復するソフトウェアのためのプラグインランタイム — エージェントが Rust、TypeScript、Python、Go…
- [MichengAI/dsh-agency-agents](https://github.com/MichengAI/dsh-agency-agents) - DSH Agency Agents — 为 DeepSeek Harness 提供 321 名可召唤的专业智能体 · 321 summonable…
- [Sutera-Diffusus/dsh-whale-musume](https://github.com/Sutera-Diffusus/dsh-whale-musume) - DeepSeek Harness のデスクトップペットプラグイン：元気なクジラ娘の看板娘がコード作成に付き添います 🐋 DSH デスクトップ版…
- [Fishsb/dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) - DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启。
- [morluto/leantoken](https://github.com/morluto/leantoken) - Code intelligence for agents: find the code that matters and keep your context…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Deepseek-Harness のコア基盤をもとに構築したデスクトップ版 Agent。基盤のすべての機能を継承し、IDE 関連機能も補完します.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 生きた DeepSeek Harness プラグインディレクトリ — 毎時更新、毎日互換性テスト、アプリ内プラグインストアとスキャフォルダー付き.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - AI Coding…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH)プラグイン厳選ディレクトリ — 14カテゴリ、280以上のコミュニティプラグインを収録し、MCP / Skill…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness プラグイン：モデルのコンテキストウィンドウをワンクリックで照合し、容量の出所を表示します.
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh Android版：DeepSeek…
- [naodeng/dsh-qa](https://github.com/naodeng/dsh-qa) - dsh-qa · QA Workbench — A local software testing workbench plugin for DeepSeek…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH セッションナビゲーション。
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - コミュニティが厳選したDeepSeek Harness (dsh)のプラグイン、ツール、skills、学習リソース.
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTMLではなく、本物のPowerPoint。何を扱うかをAIに伝えると、pptwiseが自分のマシン上で編集可能なデッキを作成します.
- [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) - DeepSeek Harnessプラグイン：会話を自動的にナレッジカードへ蓄積し、検索可能なナレッジベース + ナレッジグラフ + レビューセンターを提供.
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - スパムフィルタリング済みのオープンデータによる、DeepSeek Harness (dsh) のプラグイン、バンドル、スキルのレジストリ.
- [Lenonss/DSH_VsCodeMode](https://github.com/Lenonss/DSH_VsCodeMode) - VSCode-style coding for DeepSeek Harness: Monaco editor (tabs/QuickOpen), agent…
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [qinyre/dsh-plugin-capabilities](https://github.com/qinyre/dsh-plugin-capabilities) - 在 dsh 设置页管理技能与 MCP 服务器，支持从 Claude Code、Codex 导入.
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表。
- [chengshenyangtai/dsh-workbuddy-trae-qoder-connect](https://github.com/chengshenyangtai/dsh-workbuddy-trae-qoder-connect) - 把 WorkBuddy（多账号/企业版）、Trae CN / TRAE SOLO CN、Qoder CN 三家订阅聚合进同一个 DSH…
- [OMSociety/dsh-ppt-maker](https://github.com/OMSociety/dsh-ppt-maker) - DSH 插件：内含 kimi-ppt 技能。创建 / 编辑 / 复刻 / 导出 PPT，DSH 内纯本地导出。
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - DeepSeek Harness (DSH) 用の厳選されたプラグイン、ツール、スキン、拡張機能のリスト.
- [bloodtmai-cmyk/dsh-ai-hub](https://github.com/bloodtmai-cmyk/dsh-ai-hub) - 面向企业内部 Harness 工作台的轻量控制面。
- [bloodtmai-cmyk/dsh-harness-enterprise](https://github.com/bloodtmai-cmyk/dsh-harness-enterprise) - 面向企业内部管控的 DeepSeek Harness 统一智能工作台入口。
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness プラグインの X-ray：宣言された機能と実際の動作を比較。レジストリ + 静的スキャナー + バッジ.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSHプラグイン：ネイティブdsh-better-sidebarタブとして提供されるIDE品質のGitツールウィンドウ…
- [Xiaofei-fei/dsh-prompt-history](https://github.com/Xiaofei-fei/dsh-prompt-history) - DSH web plugin: terminal-style composer — shell history。
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness上のOpenCode — OpenCode Zen +…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - AIコーディングエージェントの観測可能なあらゆるアクションを把握できます。 · エージェントを、すべてのツールとMCPに至るまで追跡します.
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - DeepSeek Harness Personalization…
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh daemon: register the DeepSeek Harness web server (dsh web) as an…
- [duhu2000/qcc-mcp-oauth](https://github.com/duhu2000/qcc-mcp-oauth) - DeepSeek Harness 插件：一键 OAuth 授权连接企查查（Qichacha）MCP 服务 / One-click OAuth connect…
- [FeatherHunter/dsh-plugin-update](https://github.com/FeatherHunter/dsh-plugin-update) - 给 DSH 插件加「检查更新 / 安装更新」能力的 npm 包：宿主一段接线 + 面板一个现成组件，查新版、装更新、失败兜底、更新日志与多插件日志一次包掉。
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - DSHプラグインコレクション：dsh Web LAN/Tailscaleアクセス向けのパスワード認証＋信頼（dsh-web-auth）など.
- [higekibaka/dsh-vertex-argon](https://github.com/higekibaka/dsh-vertex-argon) - Vertex Argon — Google Vertex AI &amp; Gemini API dual-route Gemini 4 Argon plugin…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh)プラグイン向け依存関係ゼロの検証標準 — 静的構造ゲート (R)、cordis契約チェック…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Permanently delete archived DeepSeek Harness sessions along with their on-disk…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Webプラグイン：market-dashboardサイドバータブを監視…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness向けのサードパーティ製プラグインマーケットプレイス兼、保護機能付きライフサイクルマネージャー.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx は人間中心の拡張可能なデスクトップワークベンチです。会話、ノート、表、ファイルを同じワークベンチに統合します.
- [DoveLi-Gu/dsh-showcase](https://github.com/DoveLi-Gu/dsh-showcase) - Local, verifiable delivery evidence reports and DSH plugin for coding-agent…
- [duhu2000/qcc-mcp-legal-oauth](https://github.com/duhu2000/qcc-mcp-legal-oauth) - DeepSeek Harness 插件：一键 OAuth 授权连接企查查法律数据 MCP（法律产品：法规/案例） / One-click OAuth…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入。
- [lemonmmice/dsh-agent-toolchain](https://github.com/lemonmmice/dsh-agent-toolchain) - Evidence over claims for coding agents: 55 DSH/MCP tools (23 read-only) that…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - 为 DeepSeek Harness 桌面版提供「限网段 + 可选数字密码」的远程访问入口。
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色：换装、白饭、摸头、问候、登录账户余额和本机今日用量预估.
- [smj-1680/dsh-plugin-liquid-glass](https://github.com/smj-1680/dsh-plugin-liquid-glass) - 适用于 DSH 桌面端的液态玻璃美化插件：输入框、消息气泡、侧栏与顶栏等主要界面元素改为液态玻璃材质，可搭配各类壁纸插件使用（需深色模式）.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成。
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness plugin：WindowsサンドボックスACLのプロビジョニング失敗。
- [akkefa/deepseek-cordis](https://github.com/akkefa/deepseek-cordis) - Python plugin runtime targeting DeepSeek Harness vendored Cordis semantics。
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…

</details>

<a id="writing"></a>

## 執筆、ディスカッション、動画

mod機能についての解説記事、議論、動画。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐16 · 👁️ observed · 1 天</summary>

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
| 初回掲載 | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
| 初回掲載 | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| 初回掲載 | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 14 天</summary>

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
| 初回掲載 | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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

| 言語       | エントリ数 | プロジェクト例                                                                                                |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 375        | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 87         | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 47         | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30         | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13         | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 10         | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 3          | `vulcanshen/ccdrawu`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                         |
| PowerShell | 2          | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| AutoHotkey | 1          | `keithwalsh/claude-code-mods`                                                                                 |
| C          | 1          | `reporails/arcade`                                                                                            |
| C#         | 1          | `DimeDataCloud/open-ClaudeOS`                                                                                 |
| Java       | 1          | `bloodtmai-cmyk/dsh-ai-hub`                                                                                   |
| Kotlin     | 1          | `dphmoblie/deepseek-harness-android`                                                                          |
| MDX        | 1          | `jkf87/mod-guide`                                                                                             |
| Ruby       | 1          | `romacv/claude-plan-usage-statusline`                                                                         |
| Swift      | 1          | `eovidiu/cordis-ios`                                                                                          |
| jq         | 1          | `n0nuser/claude-statusline`                                                                                   |

<sub>言語が明記された項目のみカウントされます。ドキュメントとディスカッションの項目はこの表から除外されます。</sub>

## コントリビューション

修正提案を歓迎します。この一覧を改善する最も迅速な方法です。項目の分類や評価が誤っている場合、または名前の衝突によってプロジェクトが誤って除外されている場合は、issueまたはプルリクエストを作成してください。最後のカテゴリは、自動フィルターが最も誤りやすい部分です。

---

<sub>独立したコミュニティプロジェクトです。Anthropicとは提携、承認、レビューのいずれも受けていません。Claude Code、Claude、AnthropicはAnthropicの商標です。製品の動作は予告なく変更されるため、重要な用途に関わる情報は公式ドキュメントで確認してください。アセットは元プロジェクトに帰属し、ライセンスで許可される場合に限って掲載しています。</sub>

<sub>最終更新 · 2026-10-16T17:05:57+08:00</sub>
