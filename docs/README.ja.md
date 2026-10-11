<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="すごいClaude Codeモッド">
</p>

<h1 align="center">すごいClaude Codeモッド</h1>

<p align="center"><b>Claude Codeのモッド、プラグイン、およびそれらが変更するより深い挙動を、証拠に基づいて評価するインデックスです。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-506-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **公開中のインデックス** · 最終同期: `2026-10-11T21:12:49+08:00` (UTC+8)
> · エントリ数: **506** · 最新の更新で追加: **0** · 実装言語: **12**

<sub>以下のすべてのエントリは、自動的に収集、フィルタリング、再確認されたものです。ここに有料掲載はありません。</sub>

<a id="featured"></a>

## 今注目のピックアップ

<sub>カテゴリごとに1件掲載し、根拠評価とスター数で順位付けしています。更新のたびに再計算されます。これはランキングであり、推奨を意味するものではありません。各ピックアップから、下にある完全なカードへリンクしています。スクリーンショットまたは記録を公開しているプロジェクトを優先しているため、ストリップの視認性が保たれます。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9473 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2534 · Python · 👁️ observed</sub>
<sub>ゴーストトークンを見つけて修正し、コンパクションを生き延び、コンテキスト品質の低下を避ける。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74325 · TypeScript · 👁️ observed</sub>
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
- [公式：Anthropic自身のリポジトリとリリースノート](#公式anthropic自身のリポジトリとリリースノート) — **15**
- [Mod：Mod機能で構築されたもの](#modmod機能で構築されたもの) — **381**
- [DSHおよびCordisのプラグインエコシステム](#dshおよびcordisのプラグインエコシステム) — **99**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150151 · TypeScript · ✅ official · 0 天</summary>

##### 📝 概要

Claude Code は、ターミナル内で動作し、コードベースを理解し、定型タスクの実行、複雑なコードの説明、git ワークフローの処理をすべて自然言語コマンドで行うことで、より速くコーディングできるよう支援するエージェント型コーディングツールです。

<sub>🔧 コード内で使用されていることが確認されています: `feed.xml`</sub>

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | TypeScript                                        |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **150151** |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9473 · TypeScript · ✅ official · 1 天</summary>

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
| スター       | **9473**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

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
| スター       | **8248**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

##### 📝 概要

An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.

##### 📌 基本情報

| フィールド | 値                                                |
| ---------- | ------------------------------------------------- |
| カテゴリ   | `公式：Anthropic自身のリポジトリとリリースノート` |
| 根拠       | `Anthropic自身が公開したもの`                     |
| 言語       | Python                                            |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6342**   |
| 最終プッシュ | 2026-02-11 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

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
| スター       | **1797**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 概要

Supplementary materials for Claude Model Cards

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
<summary><b>このカテゴリのその他の項目</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - mods向けに `$.ui.notify` を追加：自分の通知設定を通じてネイティブ通知を発行し、どのチャンネルが送信したかを示します.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` hook または mod の `prompt.submit` hook 中の Esc…
- [riffkit/skill](https://github.com/riffkit/skill) - Official Riffkit skill — riff a winning TikTok into your own short video from…

</details>

<a id="mods"></a>

## Mod：Mod機能で構築されたもの

ここにある各エントリは、2.1.287でClaude Codeが獲得した機能を使用している証拠を示します。`ui.render`を介して描画する、ペイン・バンド・カードを所有する、`$.ui.selection()`を読み取る、`agent.spawn`でチームメイトを起動する、または自らがModであると明記しているものです。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 概要

ゴーストトークンを見つけて修正し、コンパクションを生き延び、コンテキスト品質の低下を避ける。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | Python                                                                   |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2534**   |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐484 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 概要

公開Claude Code mods（function hooks）のコミュニティカタログ。GitHubからスキャンし、各modが読み取り、書き込み、実行、ネットワーク経由で送信できる内容を示します。https://mods.aidojo.si/を閲覧

<sub>🔧 コード内で使用されていることが確認されています: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **484**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 7 天</summary>

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
| スター       | **127**    |
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
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 概要

Webページ向けのエージェントネイティブQA CLI。決定論的で、テストの記述は不要、LLMも不要です。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | HTML                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **104**    |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐93 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code 用スキン：アイコン付きツール行、diff、テーブルと Mermaid チャートカード、使用量バンド、15種類のテーマ。/skin でライブ切り替え。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **93**     |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **74**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

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
| スター       | **66**     |
| 最終プッシュ | 2026-10-02 |
| 初回掲載     | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/claude-code-mods">karanb192/claude-code-mods</a></b> · ⭐40 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 概要

Claude Modsと、それらを構築するためのtools：builder skill、そしてmods

<sub>🔧 コード内で使用されていることが確認されています: `plugins/mod-builder/skills/mod-builder/references/migrate.md`, `plugins/mod-builder/skills/mod-builder/references/nouns.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **40**     |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
| スター       | **27**     |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐24 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code はターミナル内で画像を表示し、動画を再生します：スクリーンショット、Playwright 録画、同期された前後比較 QA。Ghostty & kitty。

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
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/9ee7df00aee28636.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/adcbff13953c23f1.gif" width="100%" alt="iamumeransari/claude-show-your-work animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **23**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| スター       | **11**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

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
| スター       | **8**      |
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
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

入力中のMarkdownをClaude Codeのプロンプトボックスに描画します。フェンスを閉じる前でも、フェンス付きコードは構文ハイライト付きのカードになります。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **7**      |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code用のMods：ターミナルUIにライブペインと動作を追加する関数フックプラグイン

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6**      |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code 用のリアルタイム GSD ダッシュボード：ロードマップ、フォークを含むエージェントツリー、コンテキストとコスト、作業ストリーム、.planning 用 Markdown リーダー。読み取り専用。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6**      |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/a31036b15398e820.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 概要

Activity、Files、Agents、Context、MCP タブを備えたサイドペイン、プロンプト上部のステータス行、再スタイル化されたチャット、ターミナル内の Mermaid 図、テーブル、コードおよび diff パネルを追加する Claude Code mod（プラグイン）。色は /color と /theme（dark、light、その他）の両方に従います。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6**      |
| 最終プッシュ | 2026-10-06 |
| 初回掲載     | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

自分自身を見守る計画。Claude Codeと任意のMCPホストがライブで最新状態を維持する、ローカルデスクトップのロードマップツリー。プレーンなJSONで、クラウドは不要。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6**      |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/leopiney/wolfbud-claude-mod">leopiney/wolfbud-claude-mod</a></b> · ⭐5 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 概要

Claude Code 向け音声同僚。ElevenLabs conversational AI 搭載の 3D オオカミと話し合えます。同意すると、プロンプトを Claude に送信し、Claude が完了したときに声で知らせます。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **5**      |
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-10 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/leopiney/wolfbud-claude-mod/main/assets/banner.png" width="100%" alt="leopiney/wolfbud-claude-mod screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HMarzban/claude-mod">HMarzban/claude-mod</a></b> · ⭐4 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

次のClaude Codeメッセージのコストを確認：プロンプトの上に、プロンプトキャッシュのカウントダウン、再ウォームアップ料金、セッションコスト、コンテキスト、5時間・週間の使用量上限を表示するライブバンド。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4**      |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-ai` · `claude-code` · `claude-code-plugin` · `claude-mod` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dominicrico/jev-router">dominicrico/jev-router</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code プラグイン：自動 Claude モデルルーティング。プロンプト、ステップ、サブエージェントごとに Haiku、Sonnet、Opus と推論努力度を選択します。努力度上限、プロンプトキャッシュガード、ステータスバンド、ベンチマークを搭載。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3**      |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-09 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-marketplace` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/e9ab68584ed9c404.jpg" width="100%" alt="dominicrico/jev-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/2a6620c49438b369.gif" width="100%" alt="dominicrico/jev-router animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/FynnXland/fynn-mods">FynnXland/fynn-mods</a></b> · ⭐3 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Claude Code向け6つのmods：アニメーションClawdマスコット、使用制限バーとプロンプトキャッシュバー、送信前メッセージチェッカー、クイック返信、ToDoキュー、コスト台帳。ターミナルとデスクトップアプリ、英語/ドイツ語。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3**      |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-07 |

🏷 `ai-coding-assistant` · `claude` · `claude-ai` · `claude-code` · `claude-code-marketplace` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mertkayacs/ultramod">mertkayacs/ultramod</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code 用の最適なオールインワン mod パック：使用量制限とコンテキスト HUD、rm -rf と git reset --hard を元に戻せるガード、.env とシークレットの保護、すべてのターンのレシート。10個の mod を1回のインストールで導入できます。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3**      |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-09 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/0f9d8b2253819dc8.gif" width="100%" alt="mertkayacs/ultramod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/1537defa7233d7f2.gif" width="100%" alt="mertkayacs/ultramod animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mthli/cc-shorts">mthli/cc-shorts</a></b> · ⭐3 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

Claude CodeでYouTube Shortsを再生します 💃

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3**      |
| 最終プッシュ | 2026-10-02 |
| 初回掲載     | 2026-10-10 |

🏷 `claude-mods` · `youtube-shorts`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mthli--cc-shorts/ef652fff732c023d.png" width="100%" alt="mthli/cc-shorts screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/chenyuxiaojin/cyxj-notch">chenyuxiaojin/cyxj-notch</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code向けmacOS notchダッシュボード：使用量制限、オープンセッション、タスクの進捗、プロンプトキャッシュのカウントダウン、ToDoを表示。5つのClaude Code mods（同梱）がデータを供給します。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools` · `dynamic-island` · `macos` · `menu-bar`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Christandoh/context-cache">Christandoh/context-cache</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code mod: context usage, session / weekly / Fable limits and prompt-cache temperature above the prompt

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/christandoh--context-cache/3cdd3b2c5a09da7d.png" width="100%" alt="Christandoh/context-cache screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/CodyAMaughan/meme-factory">CodyAMaughan/meme-factory</a></b> · ⭐2 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 概要

工場から出荷されたばかり。Claude Code mod：ミームを依頼して、そのまま作業を続行。下書きはサイドパネルで作成され、選択、リミックス、承認して Slack に投稿できます。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `fun` · `meme-generator` · `memes` · `slack`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/7417dc8940c4a087.png" width="100%" alt="CodyAMaughan/meme-factory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/8c9d44287267796f.gif" width="100%" alt="CodyAMaughan/meme-factory animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/estruyf/claude-stats-mod">estruyf/claude-stats-mod</a></b> · ⭐2 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 概要

プロンプト上部の帯に使用制限と支出を描画するClaude Code mod。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-02 |
| 初回掲載     | 2026-10-10 |

🏷 `claude` · `claude-code` · `claude-mod` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/estruyf/claude-stats-mod/main/assets/desktop.png" width="100%" alt="estruyf/claude-stats-mod screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/i-harsha-reddy/naruto-mod">i-harsha-reddy/naruto-mod</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Code 向けのピクセルアート Naruto コンパニオン：20人の忍者、60の術を、Claude の作業中に実行

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `naruto` · `pixel-art`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lorenzh/rabe">lorenzh/rabe</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

Claude Codeがバックグラウンドで実行しているものを確認：サブエージェント、Codexジョブ、シェル、モニター、cronジョブ、ワークフロー。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/macleodlabs-ai/claudeflow">macleodlabs-ai/claudeflow</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 概要

MacLeod LabsによるClaude Code mods：streamsはセッション内で入り混じった作業を色分けされたストリームに整理します

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/macleodlabs-ai/claudeflow/main/assets/hero.jpg" width="100%" alt="macleodlabs-ai/claudeflow screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/MankhongGarden/claude-code-mods-field-notes">MankhongGarden/claude-code-mods-field-notes</a></b> · ⭐2 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 概要

Windows 上の Claude Code mods に関する初日のフィールドノート：コンテキスト／クォータの燃料バー、タイ語 UI mod、Matrix ブートイントロ、安全なアップデーター、さらに何がなぜ失敗したか（ペイン、プロンプト上のバンド、Windows Terminal でのタイ語）。

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **2**      |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-07 |

🏷 `anthropic` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mankhonggarden--claude-code-mods-field-notes/832ffcdb7bad9007.png" width="100%" alt="MankhongGarden/claude-code-mods-field-notes screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary><b>このカテゴリのその他の項目</b> <sub>· 347</sub></summary>

- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Claude Codeのターミナルトランスクリプトをデスクトップアプリ風にするmod。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code向けのサイドペイン：セッションが実行するサブエージェント、それぞれの作業内容、トークン、会話にワンクリックでアクセスできます.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code タブ）サイドバーパネル: すべての Claude Code session にある未完了および進行中の ToDo…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code タブ）入力ボックス上部の使用量バー: 5h / 7d quota、token 使用量、コスト.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - コミュニティ製のClaudeモード、プラグイン、スキルを、1つのマーケットプレイスからインストール。
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 会話エージェントと作業する人間向けの意思決定キューCLI/TUI。エージェントが質問を投稿し、人間が1つの受信トレイから回答します.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code用のフローティングステータスカード — モデル、コンテキスト、レート制限、コスト、ブランチ…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Codeが名前を付けたMarkdownファイルを読み込み、セッションの横にレンダリングして表示します.
- [atomashevic/claude-latex-math](https://github.com/atomashevic/claude-latex-math) - Claude Code mod that typesets the LaTeX math in Claude。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code用Fireworks：キーストローク、ツール呼び出し、コミット、テスト成功のすべてが、プロンプトの上で点字の花火となって上がります.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小規模なClaude Code mods（function-hookプラグイン）：session-switcherなど。
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 6 つの Claude Code mods：プロンプト上部へのプラン制限とコンテキスト表示、権限プロンプト用の許可リストコーチ、subagent…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - NarenのClaudeツールキット：Claude Code向けのskills、mods、MCP servers.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - EditとWriteのdiffを2つの横並び列で描画する Claude Code mod。
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - プラグインマーケットプレイスとしてインストールできる、厳選されたClaude Code modのリスト：テーマ、ペイン、ステータスライン、ポートレート.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - harness エンジニアリングに取り憑かれた Rustacean によって設計された、非常にこだわりの強い Claude Code プラグイン。
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Claude Code用の受動攻撃的な水分補給リマインダー。トークン消費ゼロ、判断力は最大.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - HermanのClaude Code mods（マーケットプレイス herman-mods）。
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：プロンプトの上にライブのコスト、コンテキスト、プランクォータメーターを表示。アイコンには Nerd Font が必要.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - サブエージェントの大量分岐、重いコンテキストのプロンプト、リトライループを使用量ウィンドウを消費する前に保留するClaude Code mod.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - グローバルなskills、agents、rules、toolsを、名前付きプロファイルでリポジトリごとにオン/オフできる Claude Code mod.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 テスト済みでワンコマンドインストール可能なClaude Code mods：YOLOモード向けガードレール、ライブコスト・コンテキスト、ペイン、ペットなど.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - コーディングセッション用の映画風クレジット。モデル呼び出しもテレメトリもないネイティブClaude Modです.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Codeで作業しながら外国語を身につけましょう。
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude Code mods for running many sessions across many repos from one control…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Agent が Java を記述する際に Alibaba Java 規約（p3c）に違反するコードは保存できません.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code 用のリアルタイムコスト、token、コンテキスト使用量サイドバー：セッション内にターンごとのコスト、キャッシュヒット率、消費速度、30…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code mod：すべてのセッションで Claude が提案する follow-up…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code 内のインターネットラジオ：cliamp サイドバー、ミニプレイヤー、お気に入り、ディスカバリー、フォーカスモード、Claude…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Fun, useful Claude Code mods: a pixel critter above your prompt, a tools menu…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude が調理中。仲間とチャット。オンラインの友達が、Claude Code セッションのすぐ横に。トークンゼロ、Claude への漏えいゼロ.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jackによるClaude Code modsコレクション。
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Claude Code mod：Claudeが作業している間に、アイドルゲームでピクセルアートのModstersを捕まえます.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - オールインワンClaude Code…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code が作業している間、プロンプトの上で繰り広げられる宇宙戦.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 各 Claude Code エージェントがどのファイルをコンテキストに持っているか、そしてそれぞれの量を確認できます.
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 冷静さを保とう。Claude…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Claude Codeのプロンプトフッターとプロンプト上部に、プロンプトキャッシュ、コンテキスト、プランの上限を一覧表示。
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod：セッションが開くまたは push する GitHub PR のライブペイン — CI、レビュー、競合、マージ…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - ターミナルとデスクトップアプリ向けの小さな Claude Code mods。
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Claude Code modsのコレクション。各modは独自のリポジトリに収録：usage-meter、progress-board、session-toc。
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod：タスク、subagent、ワークフロー実行、目標、ツール呼び出し用の進捗ペイン.
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod：セッション全体のクリック可能なタイムスタンプ付き目次。トピックとカテゴリー別にグループ化します.
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod：プロンプト上部に、プランのレート制限、コンテキスト使用量、セッションコスト、タスクごとのトークンを色付きバーで表示します.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - エージェントの返信にスペイン語の単語を追加する Claude CLI スキル + mod。
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Alarum.meをClaude code CLIまたはDesktopに埋め込む。
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code。
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code用Evangelion風サイドバー：コンテキスト、使用枠、アクティビティ、PR、ハードウェア、セッション、forgeパネル。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Claude Code を Person of Interest の The Machine として再スタイルする Code mod.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：サブエージェントによる必須・検証済みDAGワークフローとライブDAGペインを備えたClaude Code mod。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 向けオープンソースmod：ペイン、ステータス行、トースト、ツールガード、スラッシュコマンド.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: セッションステータス、ライブ Spec Kit 進捗、使用ウィンドウのガバナンス。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Claude Codeが独自のメーターを描画する方法で、プロンプト上部に1行として表示するコンテキストウィンドウ.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 向けのライブタスクHUD：Claude…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code 用の無料オープンソースプラグイン。/clear する前に、Claude…
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod that shows images inline in Ghostty and kitty。
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - トランスクリプト横のペインにセッションのGitHubプルリクエストを表示するClaude…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：ドキュメントのファクトチェッカー、コード監査ツール、バグメモリーログ、mod など.
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod：すべてのセッションにおけるClaudeによる今日のコード行数 — 新規、編集、削除…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod：返信内のクリック可能なパス — フォルダーをクリックすると Finder で開き、ファイル名をクリックするとファイルを開きます.
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Claude Code mod：プロンプトごとに Jev で /effort を選択。
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Codeの相棒プラグイン：プロンプトの上に表示され、ルールを記憶し、Claudeのショートカットを知らせるASCIIコンパニオン。
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods：Claude Code向けのセキュリティレイヤー.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin and mod: hook によって強制される human approval gates とプロンプト上の status…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods collection | クロードコードモード集.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code用の居心地のよいRPG HUD mod。
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：Claude の返信とあなたのプロンプトをリクエストに応じて音読する Claude Code mod.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 必要に応じて使えるClaude Code mod…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 失敗した Claude を叩く — Claude Code 用のストレス解消 mod：漫画風のお尻、8 個のスラップ、9…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：ライブペイン、コストを意識したモデルルーティング、安全ガードのための小さなプラグイン.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod &amp; plugin：使用量モニター、トークントラッカー、ステータスライン.
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - 3つの無料Claude Code mods：ツールの結果から.envの値を隠し、リモートボックスのメモリを監視し、Markdownの下書きを測定します.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods。touch-map：Claude が一覧表示、読み取り、編集、作成したファイルを、ツリーとアクティビティマップで確認します.
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - 0xnicholasyのMod（agents-office、todo-list、collapse-tools）向けClaude…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod：使用量の進捗バー（コンテキスト、5時間、7日間）と、プロンプト上部のコンパクトボタン.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods：プロンプト上部にセッション統計カードを表示します.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code プロンプトの上に表示するアニメーション付きの点字猫。
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code mod：低コストの作業を子のClaude Code経由でGLM/Kimiに振り分け、重要な作業はサブスクリプション上で維持します.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Codeのプロンプト上部でOmniDimension音声エージェントのテスト通話を実行するピクセル猫。Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - コンテキストウィンドウを小さく保つため、コンパクションに適したタイミングを選ぶ Claude Code mod。
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code向けClaude…
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spiderによるClaude Codeプラグインマーケットプレイス。
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code mod：あなたのプランの5時間および週次使用量を、プロンプト上のバー1行で表示。
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - ターミナルから市場を監視するためのClaude Code mods：トレンドとセクターのヒートマップを表示するA股/港股/美股ペイン.
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Claude Code向けのMods。
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - 私のプライベート Claude Code mods。
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - コードを変更するたびにLGTM Linesの船が通り過ぎる——Claude Code mod。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 チーム向けの Claude Code mods（ather marketplace）。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude の作業中に短いワークアウト：日次目標、連続記録、バッジ、任意のリーダーボード。Claude Code mod.
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Claude Codeプロンプトの横に計画、タスク、エージェントの進捗を表示 — Claude Code mod。
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code向けの使用量ボード。モデルごとの支出（今日、今週、今月、全期間）と週間制限の予測を表示します.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Claude Code用Mod：プロンプト上部にコンテキストウィンドウのライブ内訳を表示.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code向けNow Playing mod：プロンプト上部にApple MusicとSpotifyを表示し、カバーアート、コントロール、Up…
- [bitcars/ctx-bar](https://github.com/bitcars/ctx-bar) - ctx-bar: a Claude Code mod that keeps the context window visible at all times。
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 用 Mods：Cache-Uhr、Blast Radius、Vorschlaege、Arbeitsliste、Grill。
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - あなたの Claude Code のためのただのフクロウ。
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 1 行の Claude Code バンド（キャッシュカウントダウン、コンテキスト、制限、次のタスク）と 7 つのコミュニティ mods を、1…
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoomを搭載したオリジナルのDoomエンジンをClaude Code内でプレイできます。Mac Apple Silicon向けアルファ版.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Claude Code mod：各ターンとセッションの背後にある推定電力 ⚡ と水 💧 を、出典付きで表示。
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인。
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 会話中の未完了項目を継続的に一覧化し、プロンプト上部の帯に表示するClaude Code mod.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 本物の Engineers 向け Claude Code mods。
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nimチーム専用のClaude Code mods（usage-meter：青い炎 / テリア使用量バンド）。
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code mods：rule-keeper があなたの修正を永続的なルールとして保存。
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code内に住むTamagotchi。孵化し、Claudeが書いたコードを食べ、バグを残し、8種類の成体のいずれかに成長します.
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Claude Code向けmodをプラグインマーケットプレイスとして提供。prompt-queue：Codex形式のキューイングされたフォローアップ入力.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code mod：ターミナルとデスクトップアプリで各プロンプトと返信の時刻を表示。
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 関数フックとして書かれたClaude Code modsと、それらを提供するマーケットプレイス。dash：1つのペインに表示するセッションのダッシュボード.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code用Mod：Guardがツール呼び出しをブロックした後、同じ対象への認識済みの迂回を停止し、あなたに尋ねるようClaudeに指示する。
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code用Mod：バックグラウンドジョブを1つのビューで表示.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code用Mod：サンドボックスによるブロックを説明し、繰り返されるブロックをレビュー可能で元に戻せる設定変更に変換する。
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code のお気に入り：あなたのコマンドとスキル用のワンクリックアイコン。
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ねえ、ミュートした！差分を捨ててリフをカット、編集もクレジットももう不要。
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - claude用mods。
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Desktopアプリとターミナルで、サブスクリプション使用量（5時間 / 7日間）をプロンプト上部のバンドとして表示するClaude Codeモッド。
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code mod: your background agents as pixel critters, one sprite per model。
- [FeidaWang/edit-replay](https://github.com/FeidaWang/edit-replay) - Edit Replay: step through the file edits Claude made in the last turn, one diff…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace。
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - プロンプトの上に、並列ブランチとworktreeのライブレーダーを表示：クリーンにマージできるもの、競合するもの、積み重なっているもの、Claude…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 作業中に思いついたことを記録し、プロジェクトやマシン間で振り分け、プロンプトに変換するClaude Code mod。
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code向けのModsとスキン：Claudeのタスク用ライブ進捗バー、対応するWindows…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code用Mod（関数フックプラグイン）：コンテキストバンド、未完了項目、チェックポイント監視、レビュ​​ーゲート、エージェント使用量.
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - 7つのClaude Code…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code の返信にあるすべてのコードブロックで Ctrl+クリックしてリンクをコピー。
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Claude Code用Mods：usage-meterなどのhooksプラグイン。
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - 1つのマーケットプレイスを通じてインストールするClaude Code mods（function-hookプラグイン）.
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code mods：context-bar-plus（コンテキストバー、クォータ、サブエージェントモード）。
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Claude Code Mods向け静的サプライチェーン監査ツール — ローカル、オフライン、標準ライブラリのみ。
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Claude Code向けドイツ語Mods：コンテキスト/キャッシュのヒント、手順付きの未解決項目、ステータス行。
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code mod: capture ideas into an Obsidian vault inbox from any session。
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code mod：各回答にかかった時間、Claudeの思考時間、tok/sを、Claudeデスクトップアプリの返信直下に表示します.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods：streamer-modeは、画面共有中にプライベートペイン、バンド、ステータス行を非表示にします。
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - 私のclaude mods用。
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod：5時間の使用制限が解除されるまで待ち、自動で「continue」を送信します。
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Claude Code向けの小さなmods。まずは5時間制限後の自動継続から.
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Codeプロンプトの上にコックピットを表示します。アヒルが計器を読み取ります.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - 小さなClaude Code mods：コンテキストとプラン使用量のゲージ、プロンプトキャッシュメーター、確認すべき項目のペイン.
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: a Claude Code mod with a side pane showing where each work item…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 各サブエージェント、そのエージェントが触れたファイル、セッションの使用量とコストをそれぞれ1つのペインに表示する Claude Code mod.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - サイドバーのコンテキスト使用量パネル：総量、分類、各ターンの増加量、最も場所を取っている上位項目、キャッシュ、Claudeが現在行っていること.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - サイドバーのファイル一覧：この会話で新規作成、変更、削除されたファイルと、それぞれの変更行数。/filesで表示・非表示（Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8ビット風の毛毛（白黒のホーランドロップイヤー）が入力欄の上で走り跳ねます：待機中は平たくなり、作業中は走り、ツール使用中は跳ねます。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - サイドバーの「私が尋ねたこと」：この会話で主人が入力したすべての文を、クリックして全文表示、コピー、入力欄に戻せます.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - サイドバーのタイムライン：このターンで時間を費やした対象（モデル待ち、思考、記述、コマンド実行、ネットワーク、ファイルの読み書き、ヘルパー待ち）.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - サイドバーのトークンのやり取り：メイン会話がAnthropicに送ったトークン数、待ち時間、受信数を表示し、最上部に合計を示します.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude codeの正直な豆沙包：各ターンの回答後、Claudeが心の内を小声で一言語ります（Claude Code mod）。
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - 新しいスラッシュコマンドやサイドペインなど、Claude Code向けの小さなmod.
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - 6言語対応のClaude Code mods（function hooks）非公式コミュニティガイド。検索可能なmodディレクトリ付き.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd は Claude Code プロンプト上部の帯に住みます：セッションを演じ、実行中のもの、コンテキスト、使用制限を表示し、CI ビルドと競走します.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Codeの返答や通知をVOICEVOX / Irodori-TTSなどで読み上げるmod。
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Codeセッション間の会話を読み取り、参加するClaude Mod（/crosstalk）。
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code mod：プロンプト上部で、subagent をピクセル Claude マスコットとして動かします.
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods。
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code mods（usage-meter、...）。
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 2つの Claude Code mods：チャットの横にファイルペインを表示する folio と、ステータスライン付きでターミナルセッションを再スタイルする…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph oh what Claude Code knows.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Codeの回答を待っている間に、注意をそらさないようにします.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Angel（Vremia）のプロジェクト向けClaude Code Mods。
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - コミュニティが厳選したClaude Code Modsガイド：ユースケース、オリジナルデモ、互換性の根拠、安全上の注意。English / 中文。非公式.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claudeが行っていることをiTerm2タブのサブタイトルに表示し、タブバーを一目見るだけでどのセッションに対応が必要か分かるClaude Codeモッド。
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Codeプロンプトの上にいるふわふわの黒猫。まばたきし、喉を鳴らし、昼寝をし、あなたのコンテキストを心配する.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 切り替え可能な権限プロファイルを備えたClaude Code…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code 向けのコミュニティmod：Claude Code 内で実行されるガード、ペイン、コマンド。マーケットプレイス：modhub。
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code用の静かなサイドペイン：このセッションの動作、計画、エージェント、その他すべてのセッションを表示。
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Codeのトランスクリプトで、各プロンプトと各返信の上に、自分の時計設定と同じ形式で記された薄い時刻表示。
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Codeが折りたたむものを復元します：Claudeが読み取ったファイル、実行したコマンド、各ターンで行ったこと。
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - プロンプトのフッターのモードスロットにコンテキストウィンドウの使用量を表示するClaude Code mod。
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - セッション開始時にCLAUDE_CODE_ENABLE_TODO_TOOLSを設定し、todoツールを省略するモデル向けに再び有効化するClaude Code…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code mod：プロンプト上部にタスクリストを1行ずつ表示し、現在のタスク、進捗バー、件数を示します。ターミナルとデスクトップアプリで同じ外観.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 内で AI と Connect Four をプレイ (/connect-four)。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 複数のAIエージェントで共有するリポジトリ向けのClaude Code…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods marketplace。
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude CodeでSQLを安全に扱うためのガードレール：DB CLI。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Claude Code Modsの中から、役立つ機能ごとに並べた最高の一覧。すべて手作業で確認し、各項目を1行で紹介.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - 危険なシェルコマンド。
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code用の2つのClaude Mods：garde-du-corps。
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - エージェントテレメトリ、タイムラインダッシュボード、mmrunによるクロスモデルレビューとworktree委任、ワークフローガード、永続的な進捗追跡を備えたCl…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Claude Codeに悪態をつくと、漫画の手が叩き返す。メッセージは送信されず、丁寧なバージョンがプロンプトボックスに戻される.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo。
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code mods：usage-bothがプロンプト上部に5時間および週間の使用量を表示します.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude デスクトップアプリの Code タブ用ライブセッション統計サイドペイン：コンテキスト、コスト、git 変更、ターン統計、サブエージェント、ログ.
- [PhilRoli/traintracker-claude](https://github.com/PhilRoli/traintracker-claude) - Claude Code mod: pause sessions before your TrainTracker train arrives。
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Vesuviusデザインシステムをテーマにした、pompeitechインターフェース用のClaude Code mod。
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Claude Code 用 mods：セッション内で実行される function-hook プラグイン（english-coach、toolbar）。
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod：ライブ株価ティッカー、/quote ペイン、価格アラート、マーケットバンド、モデルが呼び出せる quote ツール。
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace。
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code mod: keeps auto-memory up to date in the background after every turn。
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod：SSH ホスト、RAM、5h/7d 使用制限をプロンプト上部の1行に表示。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：Claudeが作業している間に行う腕立て伏せ。トークンなし.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 韓国語版6種：仮定の記録、やさしい言葉、アイデア棚、プロンプトの推敲、セッションモニター・トラッカー。
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：プランモードで承認した計画をプロンプトの上にライブチェックリストとして表示し、Claude が完了するたびに各ステップをチェック。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 厳選したClaude Code modsの一覧。各項目をクローンしてclaude plugin validateで確認し、アクセス可能な対象をタグ付け.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - コスト不要モード：ヘルパーエージェントはHaikuで動作し、大きなファイルやログはClaudeのコンテキストを埋める代わりに無料のGeminiモデルで要約される…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - セッションに寄り添うlofiサウンドトラック：落ち着き、集中、フローに加え、テストの成功と失敗を知らせる合図。オリジナル音楽.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claudeがコードを書く間に学習：コードを変更したターンの後、その変更自体についての質問がプロンプトの上に1つ表示される。概念ごとに採点.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claudeが行うすべての編集を記録：各変更が入力される様子を再生し、ステップごとに進み、任意のファイルを任意のステップへ巻き戻す.
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts。
- [samaphp/session-links](https://github.com/samaphp/session-links) - セッションで言及したすべてのリンクを、プロンプトの上に1行で表示。Claude Code mod.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Claude Code Mod：プロンプトの上に5h-、Wochen-、Fable-Limitをバーとして表示。
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in a terminal pane…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Claude用のプラグイン集.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis：Claude Code向けの非公式Avengersファンmod.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - プロンプト上部にコンテキスト、増加量、クォータ、キャッシュ、ネイティブコスト、エージェントの活動とセッション詳細を表示する Claude Code mod.
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code mod：単純なターンとサブエージェントをより安価なモデルに振り分け、選択したモデルを上回るモデルは決して使用しません.
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - 個人用Claude Code mod。
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - The original DOOM in a Claude Code pane with nothing to install: the engine…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 踊るピクセルアートのMalenia付き、Claude Code用ワンクリックコミットメッセージ。
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - 個人用Claude Code mod。
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使うClaude Codeのmod置き場。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 現在のセッションをペインに表示するClaude Code…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - modのClaude Codeプラグインマーケットプレイス: Claude…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Claude Modsを管理するrepo。
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Claude Codeのカスタマイズ。
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - いくつかのClaude mods。
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - 書いている途中でプロンプトの英語をチェックするClaude Code mod。
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - 厳選したClaude Code modのカタログ。各modには、あなたのために構築するコピーペースト用プロンプトが付属します.
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mod：プロンプトの上にコンテキストとプラン制限のメーターを表示し、新しいデスクトップセッションでは自動的にピン留め · Claude…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code mod：長時間実行タスク用のアニメーション進捗帯と完了サマリー。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 3つの小さなClaude Code…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Claudeが読み込む前に大きなスクリーンショットを縮小するため、長時間のセッションが続き、クリックが正しい場所に届くようClaudeに倍率を伝えます.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 「I。
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - プロンプトボックスの上に次に推奨されるプロンプトを表示します。/autoと入力すると、10秒のカウントダウン後に最初の候補を自動送信します.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 作業の隣のペインでClaudeに別の質問をできます。メインの会話には決して表示されません。デスクトップアプリの/btwのように機能します.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - 1ステップでインストールでき、ポルトガル語の動画ガイド付きのClaude Code modマーケットプレイス。
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Claude Codeのレート制限カウントダウンと消費速度予測。
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Codeプラグイン：Claude…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - ClaudeのClaude desktop Codeタブで、返信内にLaTeX数式をインライン表示および表示し、オプションでTikZ図も表示します.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Claude Code用のライブタスクボード：構築前に計画し、サイドパネルで全タスク、ステータス、時間、サブエージェント、チェックを追跡する.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod：Claudeが変更したファイルとその理由、サブエージェントのリアルタイムステータス、残りのプラン制限を報告します.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 最高のエージェント向けリソースを厳選したコレクション。Claude…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 何が起きているかを表示する Claude Code プラグイン - コンテキスト使用量、アクティブなツール、実行中のエージェント、todo の進捗。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline サポート、テーマなどを備えた、Claude Code CLI 用の美しく高度にカスタマイズ可能な statusline.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code のシステムプロンプトの全パート、27…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code を最大限に活用するための 45+ のヒント。基本から高度な内容まで…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code向けの美しいvimスタイルのpowerline。
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - ターミナルペインでコーディングエージェントの差分をレビューし、行コメントをClaude Code、Codex、OpenCode、Piに送り返します.
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - コンテキスト使用量、APIレート制限、コスト追跡に対応したClaude Code用包括的ステータスラインプラグイン。
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek…
- [L-Forster/open-jet](https://github.com/L-Forster/open-jet) - An offline coding agent for local models.
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Fast, zero-dependency cost calculator and customizable statusline for Claude…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code セッション用ターミナルステータスライン。
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ ターミナル、Claude Code と Cursor CLI statusline、そして MCP クライアントで、フォローしている大会。
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Windows と macOS 上の Claude Code 向けローカルコントロールプレーン：固定エンドポイントの背後で LLM…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 内でバージョン管理される個人用 Claude Code 設定…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Claude Code向けセッション認識ステータスライン。顔文字がトランスクリプトを読み取り、セッション全体の状態を語ります.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Claude Code向け2行のtruecolorステータスライン。
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - A floating peak/off-peak tide card for DeepSeek Harness: i18n (en/zh/ru)…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture向けポータブルClaude…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Claude Codeのポータブルなグローバル設定：カスタムスキル、PreToolUseフック、カスタムステータスライン.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 毎日使っているClaude Codeプラグイン：誰のマシンでも動作するよう整理したskillsとmods.
- [chaybits/ai-session-usage](https://github.com/chaybits/ai-session-usage) - Claude Code and ChatGPT (Codex) subscription limits in one card: a KDE Plasma 6…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Codeのトークン管理：トップモデルが指揮し、実行は必要十分な最安手段に委ねます.
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code向けのライブワークフローフェーズステータスライン（Plan → Exec → Verify → Done）。モデルが自動更新します。
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code 向けのシンプルで便利なステータスライン設定。
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Claude Code の使用制限アラート：セッション（5h）と週間制限に対する macOS 通知、アプリ内警告、ステータスラインのパーセンテージ。
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux、WSL、Windows、macOS 向けの設定可能な Claude Code ステータスライン.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code 向けの高速な Rust ステータスライン — ペイロード優先、gitをキャッシュ、描画は約10ms。
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Catppuccinのカプセル風サイドペインで、コンテキストの内訳、キャッシュヒット、レート制限の予測、コスト、アクティビティを表示するClaude…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code用のステータスラインとトークンライン：コンテキスト、5時間および週間の使用量とペースマーカー、アクティビティ、git、コスト.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - macOS、Linux、Windows全体で、モデル、コンテキスト、制限、git情報、セッション時間などClaude…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - Claude Code用の親しみやすく何でも細かく調整できるステータスライン…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 複数行の Claude Code ステータスライン：消費量、コンテキスト%、git、アクティブなアカウント — 料金とコンテキストウィンドウを自動更新.
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - claude code 用の有用な情報を表示するステータスライン。
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - ネイティブエージェントチーム。制御下で。Claude Code向けの厳格なワーカー制限、ライブのチーム可視性、ポータブルな設定.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code アドオン：タブステータスの色付きドット監視 + バンドルされた GSD statusline。
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - macOSおよびLinux向けのClaude Code使用状況ステータス行。herdrインストーラープラグインとしてパッケージ化されています.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code用カスタムステータスライン――使用率、コンテキストサイズ、コスト、タイマーを表示するコンテキストバー。
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code用の簡潔で情報豊富なステータス行 — プロジェクト、gitステータス、モデル、セッション時間、コンテキスト使用量、レート制限を表示.
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod：ターミナルとデスクトップのCodeタブでClaude Code用のCRTスタイルのステータスパネルを表示します.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - balooを備えたClaude…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - プロフェッショナル品質のClaude Code statusline：セッション時間、ECB為替レートによる複数通貨コスト、MTokあたりの料金、支出上限.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code向けサブスクリプション対応ステータスライン。
- [dave-net-positive/Claude_Code_PII_Redactor](https://github.com/dave-net-positive/Claude_Code_PII_Redactor) - Mod that detects and redacts PII in Claude Code before it reaches the model。
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code用の高機能ターミナルステータスライン — Bun + TypeScript、ランタイム依存関係なし.
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - トランスクリプト内でMermaidダイアグラムを美しく描画するClaude…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins。
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude…
- [FunDrivenDev/claude-plugins](https://github.com/FunDrivenDev/claude-plugins) - Public Claude Code plugins: a context-budget status line。
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Codeカスタムステータスライン（モデル、effort、コンテキスト、キャッシュ、使用量制限）。
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Codeでの実際のDeepSeek API支出：セッションのトランスクリプトをDeepSeekのピーク／オフピーク料金で再価格設定…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Claude Code内で画像をプレビュー：返信の下にあるチップにカーソルを合わせて画像をポップアップ表示するか、/img &lt;path&gt;でペインに開きます.
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - WSLを使用したWindows上のClaude CodeおよびClaude Desktop用mod：Dockerとパフォーマンスをプロンプトの上に表示。
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Codeのステータスライン（エージェントパネルの行）。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 ClaudeのtodoをFizzy.doに同期し、チーム全体でリアルタイムに可視化.
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - 私が構築し、共有したいClaude Codeのスキル、mod、その他のアドオン集。MIT誰でもダウンロード、実行、テスト、変更できます.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Codeの設定メニュー、ステータスライン、設定。
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - 自家製でケージフリーなclaudeプラグイン、スキル、modなど。
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status。
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Claude Code用HUDスタイルのステータスライン — ネットワークの健全性、TPS、コンテキスト、クォータ、コストをすべて1行に表示。
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claudeが何をするかを理解するためのClaude Codeプラグインと改造：読みやすい回答形式とライブセッションボード（マーケットプレイス：oshn）。
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Claude Code用のカラフルな複数行ステータスバー（クォータバー、コンテキスト、サブエージェントパネル）。
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows向けClaude Codeステータスライン（PowerShell）：使用量バー、ペース警告付きの5時間/7日リセットカウントダウン、自動折り返し。
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Claude Code用のBearings and Glossary改造。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - 共有コンポーネントキット、プレイグラウンド、Storybookを備えたClaude Codeの設定とmod。
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator)。
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - A small dashboard for Claude Code: context %, cache countdown, 5-hour &amp; weekly…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Custom terminal status bar for Claude Code: model, directory, git state…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - ポータブルなClaude Code設定：CLAUDE.md、settings、statusline、skills。
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Claude Code用のスクリーンリーダーコンパニオンmod（Unlocked Spark Foundation）。
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Claude Codeを実際に操作しながら検証した、実践的で詳細な解説…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code用のリアルタイムコスト追跡およびセッション監視ステータスライン。
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - フォルダー、gitブランチ、モデル、コンテキストウィンドウの使用状況、プランの使用上限を表示するClaude Codeステータス行。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Codeエージェント向けプロアクティブAIメモリおよびレート制限モニター。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Codeのフック、サブエージェント、ステータスライン：種類ごとにまとめられ、セキュリティ評価済みのオープンソースコレクションとツール.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Codeのステータスライン向けビジュアルビルダー。ブラウザーでターミナル下部のバーをデザインし、1つのコマンドを貼り付けてインストールできます.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - リアルタイムのトークン使用量と推定エネルギー消費量を表示するClaude Codeステータスライン。
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Codeステータスライン：CCometixLineの美しさ + Claude HUDの機能。

</details>

<a id="dsh-cordis"></a>

## DSHおよびCordisのプラグインエコシステム

DeepSeek HarnessとCordisは、異なる方向から同じ場所に到達します。両者にとってプラグインはmodの仕組みであり、そこでのプラグインはここでいうmodに相当します。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74325 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **74325**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100497 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **100497** |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐87809 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **87809**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81879 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **81879**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35759 · Go · 🔎 inferred · 0 天</summary>

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
| スター       | **35759**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8626 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness (DSH) Web プラグイン集約エコシステム · すべてがプラグインで、Creative Workshop を通じて配布｜｜DeepSeek Harness (DSH) Web プラグイン集約エコシステム · すべてがプラグインで、Creative Workshop を通じて配布

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **8626**   |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6146 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness 内のプラグインマーケット — 閲覧、検索、ワンクリックインストール · DSH ビジュアルプラグインマーケット

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **6146**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4478 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness（DSH）の画面右下に住む小さなクジラ娘。DeepSeekアカウントの残高を見守ります。ぷるぷる動き、ドラッグ吸着、左吸着時の反転、数字のスクロールアニメーションに対応し、画面とともに自動で有効になります。DSHのインストール時に一緒に導入するのがおすすめです

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4478**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4285 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DSH が公式に最も推奨する TUI プラグイン。高性能・低負荷、かわいいピクセルクジラ、スムーズなマウス操作。npm からワンコマンドでインストールできます。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4285**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3153 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **3153**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1983 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

コンテキストの洞察と管理に最適な DeepSeek Harness プラグイン。コンテキストダッシュボード / ブラウザ / サイドバーとコンテキストコマンドを備え、コンテキスト統計、構成、内訳、進化の詳細、コンテキストがどのように作られ、どのように進化するかの理解に対応します。ワンストップの DeepSeek Harness コンテキスト可視化プラグイン。Context パネル、ブラウザ、サイドバー、Context コマンドにより、コンテキストの構成、進化、圧縮、枝刈りなどのイベントとアクションを可視化します。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1983**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1561 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

跨设备的开源Agent工作台

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1561**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1464 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1464**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1401 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

AI 小説創作ソフトウェア：アイデア、キャラクター、世界観、プロット、章の執筆、校閲、修正を制御可能なワークフローに整理します。Windows/macOS デスクトップ版を提供し、ローカルモデルとオンラインモデルに対応します。AI 小説執筆ソフトウェア：アイデア、キャラクター、世界観、プロット、章の執筆、校閲、修正を制御可能なワークフローに整理します。Windows/macOS 用デスクトップアプリ、Ollama 連携、DeepSeek Harness（DSH）プラグインのプレビューを搭載しています。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1401**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

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
| スター       | **1171**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness (dsh) Windows デスクトップクライアント - Node.js + dsh CLI を同梱、ワンクリック起動

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **704**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐283 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Just open your browser — get all your work done.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **283**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

ACRYL - Agent Context Relay Yielding Lifecycles。1 つの永続ワークスペース、1 つの正規コンテキスト、任意のコーディング agent。

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
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

エージェントの選択、監督、修正、承認のための TypeSafe Jev または luna のようなDecision apiを System One decision layerとして統合するネイティブDeepSeek Harness（DSH）プラグイン。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **203**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness（dsh）の時間差タスク委任：余裕のあるときにタスクを計画し、オフピーク時に無人で実行、戻ってきたらレポートを確認できます。人間による裁定、デスクトップ＋Webに対応。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **170**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

プレビュー可能なプリセット間セッション移行のためのDeepSeek Harnessプラグイン。固定スキーマの引き継ぎにより、状態、ソースモデルの意図、未解決の画像を保持し、元のセッションには変更を加えません。

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
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

インストールするとmattpocock/skills v1.3.1の27個の開発・効率化スキルが付属し、手動でスキルをインストールする必要はありません。400億tokenをかけて開発されたこのプラグインは、元のスキルに比べて開発効率を10倍に高め、初心者がこのスキルセットをより早く使い始めるのにも役立ちます。GitHub issueを全面的にサポート。Markdownはプレビュー版で、GitLabは現在サポートしていません。ご利用とご支援に感謝します💗

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **134**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **133**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐131 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness用 Claude Code Desktopテーマ｜DeepSeek HarnessウェブGUI向けに作られた Claude Codeデスクトップテーマ

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **131**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐130 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

Runtime evidence that helps agents trace, profile, and burn down hotspots in application and native code, GPU kernels, and inference stacks.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **130**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness デスクトップペットプラグイン：元気なクジラ娘の看板娘がコーディングに付き添います 🐋 DSH デスクトップ版 0.2.0-rc.2 と旧版 Web（desktop pet / mascot、local-first）に対応

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **120**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **113**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐65 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **65**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 概要

生きた DeepSeek Harness プラグインディレクトリ — 毎時更新、毎日互換性テスト、アプリ内プラグインストアとスキャフォルダー付き。DSH プラグイン活ディレクトリ：毎時更新、毎日互換性実測、内蔵プラグインストアとスキャフォルダー。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | HTML                                                                                           |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **59**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

AI Coding Agent 向けのタスク認識型ワークスペースコンテキスト検索とライフサイクル追跡：現在のタスクに応じて、最も関連性の高いドキュメント、コード、メディアを見つけ、整理し、継続的に追跡します。完全ローカル、モデル呼び出しゼロ、ネットワークゼロ。AI coding agents 向けのタスク認識型ワークスペースコンテキスト検索とライフサイクル追跡。手元のタスクに最も関連するワークスペースコンテキストを、ローカルで、決定論的に、モデル呼び出しゼロ、ネットワークゼロで見つけ、整理し、追跡します。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **53**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/skyf0xx/hedgehog">skyf0xx/hedgehog</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

HEDGEHOG codes Cleaner, Faster and with Fewer Tokens. Hedgehog's AI-driven development builds a task dependency graph from your spec-driven, BMAD-METHOD plan, so Claude Code, Cursor & Gemini CLI stay locked to it. A CLI-enforced state machine for agentic coding. Now builds DeepSeek DSH Plugins. DeepSeek Harness、DSH 插件、AI 编程、BMAD 方法. AI Copywriting

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **44**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-skills` · `agentic-coding` · `ai-agents` · `ai-assisted-development` · `ai-coding` · `ai-copywriting` · `ai-engineering` · `ai-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/skyf0xx--hedgehog/326d2d3a663269a4.jpg" width="100%" alt="skyf0xx/hedgehog screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐42 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

dsh ゲーム素材マスタープラグイン。seedream 画像生成モデルと minimax 動画生成モデルに接続し、さまざまなゲーム素材を生成できます。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **42**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness プラグイン：llm-pi-ai モデルの正確なコンテキストウィンドウを維持し、長いセッションが誤ってコンテキストオーバーフローと判定されるのを防ぎます。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **34**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/6c743bbe3da63616.jpg" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PensiveFei/deep-read-summarize">PensiveFei/deep-read-summarize</a></b> · ⭐31 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Deep reading & summarization workflow for books/papers/videos/web — plugin parsers, MapReduce deep-read, JSON Schema output, Obsidian-ready (DSH)

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **31**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agent` · `content-summarization` · `deepseek` · `dsh-plugin` · `pipeline` · `workflow`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pensivefei--deep-read-summarize/800b10f03f25fe11.png" width="100%" alt="PensiveFei/deep-read-summarize screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary><b>このカテゴリのその他の項目</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSHプラグインマーケット / DSH Plugin Marketplace：DeepSeek Harness Web GUIでGitHub…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [arcships/rutis](https://github.com/arcships/rutis) - 自己反復するソフトウェアのためのプラグインランタイム — エージェントが Rust、TypeScript、Python、Go…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH)プラグイン厳選ディレクトリ — 14カテゴリ、280以上のコミュニティプラグインを収録し、MCP / Skill…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness 用 Zotero ツールキット。Zotero ライブラリをエージェント用のエビデンスストアに変えます.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSHプラグイン：Windows上のすべてのエージェントモード向けGit Bashシェル（pwsh executorを置き換え）。
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development。
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：DeepSeek…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - オフィス三種の神器！DeepSeek Harness (dsh) 向け Office ドキュメントツール：スプレッドシート…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh Android版：DeepSeek…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH セッションナビゲーション。
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [weishao2/tizhuang-agent-skills](https://github.com/weishao2/tizhuang-agent-skills) - 2000万+中小学K12真题题库 Skill：免费注册、免费抽题、教材/章节/知识点检索、练习测验与AI智能组卷.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web プラグイン：GitHub 風のアクティビティヒートマップ、キャッシュヒット率カーブ、モデル別内訳付きの日次 token 使用統計。
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - コミュニティが厳選したDeepSeek Harness（dsh）のプラグイン、ツール、スキル、学習リソース.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness 用 MCP サーバーマネージャープラグイン：設定 → MCP ページ、OAuth。
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A コマース交渉ランタイム + DeepSeek Harness（dsh）プラグイン.
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - DeepSeek Harness Web 用の MCP サーバー管理 UI — フローティングパネル、JSON インポート、プロフィールに基づく永続化.
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTMLではなく、本物のPowerPoint。何を扱うかをAIに伝えると、pptwiseが自分のマシン上で編集可能なデッキを作成します.
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催更姬：给大肥鱼一个小说工作台。写正文、理设定、画情节，和 AI 一起讨论、续写与改稿.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness プラグイン · 送信欄でプロンプト草稿をワンクリック「最適化」：5次元診断 + 書き換え案の SSE…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - DeepSeek Harness (dsh) Web サーフェス向けログインゲート：パスワードまたは共有トークンによるサインイン、任意の TOTP…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 組み込みC/C++ AIエンジニアリングプラグイン — ファームウェアスキル（FreeRTOS、Keil、HardFault、ステートマシン）+ 1%…
- [Chael-Chael/dsh-reference-anything](https://github.com/Chael-Chael/dsh-reference-anything) - The best DeepSeek Harness plugin for referencing anything — enhanced @ menu for…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - DeepSeek Harness（DSH）用のワンストップ skills、subagent、MCP、LSP マネージャー — Claude…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）。
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness プラグインの常時互換性テスト：正確なリリース、分離されたランナー、修正可能な上流の問題.
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive context compaction for local-first agents.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - プロジェクトドキュメントと長期メモリーを専用のObsidian vaultにプレーンなMarkdownとして保持するDeepSeek…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek HarnessプラグインのX線：宣言された機能と実際の動作を比較。レジストリ + 静的スキャナー + バッジ.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）。
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）。
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - A knowledge base toolkit for research and literature review.
- [Mcd0LUO/dsh-guard-repeat-output](https://github.com/Mcd0LUO/dsh-guard-repeat-output) - Host-side degeneration guard for DSH: strips garbage code points, detects…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - DSH の回答を操作可能なインターフェースに変えます：計算、グラフ、フォーム、シミュレーション、ミニゲーム.
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - 設計とコードの主張検証：事実系はソースコードと照合し、振る舞い系は実行可能モデルを走らせます；構造/依存関係レビュー（単層および多粒度の詳細化）、UML…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - マルチフォルダーworkspace：DSH。
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - DeepSeek Harness向けエンジニアリングワークフロープラグイン：タスクステージ、検証記録、コミットチェック、スキルとルールの管理.
- [Kr-ATG/dsh-chat-plus](https://github.com/Kr-ATG/dsh-chat-plus) - DSH 对话体验增强套件（零源码改动，纯插件注入）。Seeker 双栏执行大盘：右栏任务 / 操作面板 / 子智能体 / 产出物四张卡 +…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh)プラグイン向け依存関係ゼロの検証標準 — 静的構造ゲート (R)、cordis契約チェック…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness上のOpenCode — OpenCode Zen +…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness向けのサードパーティ製プラグインマーケットプレイス兼、保護機能付きライフサイクルマネージャー.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyxは、人を中心に据えた拡張可能なデスクトップワークスペースです。会話、ノート、表計算、ファイルを同じワークスペースにまとめ、サーバーを自分で構築すれば…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness 向けの batteries-included コーディング agent — Claude Code…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 入力体験プラグイン：送信／改行キーの切り替え、右クリックメニュー、パネルのスクロールとサイズの記憶、OpenCode…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - DeepSeek Harness デスクトップ版に「ネットワークセグメント制限 + 任意の数字パスワード」によるリモートアクセス入口を提供します.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh) 向けコミュニティ版マシンデプロイ・運用保守スイート：install / start /…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Webプラグイン：market-dashboardサイドバータブを監視…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 帰属先のない空のモデル試行を再試行可能にします。判別できる唯一の接合部を対象としています。
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - 自分自身の後始末をするプラグイン：iOSおよびmacOS向けcordisプラグインフレームワークのSwift 6移植版.
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harnessエージェントプリセット：CodexとClaude…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus検証済みのライフサイクルカーネルとCordis互換アダプターを備えたRustプラグインランタイム.
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider)。
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin。
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步。

</details>

<a id="writing"></a>

## 執筆、ディスカッション、動画

mod機能についての解説記事、議論、動画。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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

| 言語       | エントリ数 | プロジェクト例                                                                                                     |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 322        | `anthropics/claude-code`, `anthropics/claude-code-action`, `karanb192/cache-tax`                                   |
| JavaScript | 69         | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `augiefra/claude-mods`                         |
| Python     | 32         | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`      |
| Shell      | 19         | `anthropics/claude-agent-sdk-typescript`, `andrewbakercloudscale/claude-code-cost-sidebar`, `Gharib89/claude-mods` |
| HTML       | 12         | `awss1i/assay`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                                       |
| Go         | 6          | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                         |
| Rust       | 5          | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`                  |
| PowerShell | 2          | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                                |
| C#         | 1          | `sakanamaru/dsh-minato`                                                                                            |
| Kotlin     | 1          | `dphmoblie/deepseek-harness-android`                                                                               |
| MDX        | 1          | `jkf87/mod-guide`                                                                                                  |
| Swift      | 1          | `eovidiu/cordis-ios`                                                                                               |

<sub>言語が明記された項目のみカウントされます。ドキュメントとディスカッションの項目はこの表から除外されます。</sub>

## コントリビューション

修正提案を歓迎します。この一覧を改善する最も迅速な方法です。項目の分類や評価が誤っている場合、または名前の衝突によってプロジェクトが誤って除外されている場合は、issueまたはプルリクエストを作成してください。最後のカテゴリは、自動フィルターが最も誤りやすい部分です。

---

<sub>独立したコミュニティプロジェクトです。Anthropicとは提携、承認、レビューのいずれも受けていません。Claude Code、Claude、AnthropicはAnthropicの商標です。製品の動作は予告なく変更されるため、重要な用途に関わる情報は公式ドキュメントで確認してください。アセットは元プロジェクトに帰属し、ライセンスで許可される場合に限って掲載しています。</sub>

<sub>最終更新 · 2026-10-11T21:12:49+08:00</sub>
