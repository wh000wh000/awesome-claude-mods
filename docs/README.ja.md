<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="すごいClaude Codeモッド">
</p>

<h1 align="center">すごいClaude Codeモッド</h1>

<p align="center"><b>Claude Codeのモッド、プラグイン、およびそれらが変更するより深い挙動を、証拠に基づいて評価するインデックスです。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-534-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **公開中のインデックス** · 最終同期: `2026-10-11T23:26:48+08:00` (UTC+8)
> · エントリ数: **534** · 最新の更新で追加: **0** · 実装言語: **12**

<sub>以下のすべてのエントリは、自動的に収集、フィルタリング、再確認されたものです。ここに有料掲載はありません。</sub>

<a id="featured"></a>

## 今注目のピックアップ

<sub>カテゴリごとに1件掲載し、根拠評価とスター数で順位付けしています。更新のたびに再計算されます。これはランキングであり、推奨を意味するものではありません。各ピックアップから、下にある完全なカードへリンクしています。スクリーンショットまたは記録を公開しているプロジェクトを優先しているため、ストリップの視認性が保たれます。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9474 · TypeScript · ✅ official</sub>
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
<sub>⭐74336 · TypeScript · 👁️ observed</sub>
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
- [公式：Anthropic自身のリポジトリとリリースノート](#公式anthropic自身のリポジトリとリリースノート) — **14**
- [Mod：Mod機能で構築されたもの](#modmod機能で構築されたもの) — **408**
- [DSHおよびCordisのプラグインエコシステム](#dshおよびcordisのプラグインエコシステム) — **101**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150172 · TypeScript · ✅ official · 0 天</summary>

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
| スター       | **150172** |
| 最終プッシュ | 2026-10-10 |
| 初回掲載     | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9474 · TypeScript · ✅ official · 1 天</summary>

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
| スター       | **9474**   |
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
<summary><b>このカテゴリのその他の項目</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - mods向けに `$.ui.notify` を追加：自分の通知設定を通じてネイティブ通知を発行し、どのチャンネルが送信したかを示します.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` hook または mod の `prompt.submit` hook 中の Esc…

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐486 · JavaScript · 👁️ observed · 0 天</summary>

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
| スター       | **486**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐338 · Python · 👁️ observed · 0 天</summary>

##### 📝 概要

macOS menu bar & Windows tray app pinning Claude Code, Codex, Antigravity & Grok CLI quota, burn rate, and cost to your screen. Local-first, no LLM API calls. HTML reports, 14 themes.

<sub>🔧 コード内で使用されていることが確認されています: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | Python                                                                   |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **338**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐186 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 概要

Claude Code mods: plugins built on hooks that add live lines above the prompt, guards, panes and games. Context bar, usage meter, Codex review watch, Markdown preview, Spotify now playing and more.

<sub>🔧 コード内で使用されていることが確認されています: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **186**    |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐132 · TypeScript · 👁️ observed · 7 天</summary>

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
| スター       | **132**    |
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
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **96**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 概要

A collection of claude code mods

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **77**     |
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **75**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 概要

Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens. 台股／美股看板 + more to come.

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 概要

Expert skills, agents, commands, rules, hooks & output styles for Claude Code — session continuity + modern CLI tooling for real-world dev workflows

<sub>🔧 コード内で使用されていることが確認されています: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | Shell                                                                    |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **59**     |
| 最終プッシュ | 2026-10-07 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 概要

Claude Code mods: live plan progress bars above the prompt

<sub>🔧 コード内で使用されていることが確認されています: `README.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | TypeScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **46**     |
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>アニメーション付きの記録 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐44 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **44**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 概要

A pixel Pokémon that lives above the prompt in Claude Code

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
| 最終プッシュ | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 概要

Xcode's build, tests, console and SwiftUI previews inside Claude Code

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 概要

Claude Code mods: 21 styles and a full set of features you turn on when you need them, for the terminal and the desktop app. · 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 概要

Ten Claude Code mods, beginner guides, creation prompts, safe demos, and a build-your-own template.

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

Claude Code mods: usage-band shows your 5h/7d limits, context window and cache hit rate above the prompt

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 概要

Claude Code mods that make Claude's questions easier to read and answer (qa-guide).

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 概要

Ten open-source mods for Claude Code: live panes, bands, status lines and tool-call guards. Burn meter, launch codes, session wrapped, boss fight, code pet and more.

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 概要

Two Claude Code mods: Codex computer-use bridge and coordinated Claude sessions. Source, build prompts, setup and tests.

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
| 最終プッシュ | 2026-10-05 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 概要

A UI around your Claude Code and Codex terminals that your agents build, so the only model in your head is yours.

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
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 概要

KOZMOS — live, visual mods for Claude Code (CLI + desktop): bands above the prompt, sidebars, status ticker, companions, guards and sound.

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 概要

Six Claude Code mods in one plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) with per-mod switches, plus a mods-vs-hooks report.

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 概要

개발동생의 Claude Code mods 모음. 택시 팩: 미터기, 내비, 과속 단속 카메라, 블랙박스

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
| 最終プッシュ | 2026-10-04 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">で視聴 youtube.com</a> · 再生はホストサイトで開始されます。GitHubはインライン埋め込みに対応していません</sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 概要

Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf

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
| 最終プッシュ | 2026-10-08 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary><b>このカテゴリのその他の項目</b> <sub>· 374</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Collection of 100+ mods you can use with Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Modsと、それらを構築するためのtools：builder skill、そしてmods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - The Claude Code harness I run every day, published under this name since day…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Four Claude Code mods: Cache Keeper, Recording Mode, Goal Meter, and Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods that fix and translate your prompts before Claude reads them。
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Claude Codeのターミナルトランスクリプトをデスクトップアプリ風にするmod。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code向けのサイドペイン：セッションが実行するサブエージェント、それぞれの作業内容、トークン、会話にワンクリックでアクセスできます.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Source-cited Obsidian knowledge base about Claude Code mods: how they work, how…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code タブ）サイドバーパネル: すべての Claude Code session にある未完了および進行中の ToDo…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods and skills from Nekyia Labs, built and used daily by AIs…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill that teaches Claude Code agents to build Claude Mods。
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code タブ）入力ボックス上部の使用量バー: 5h / 7d quota、token 使用量、コスト.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - コミュニティ製のClaudeモード、プラグイン、スキルを、1つのマーケットプレイスからインストール。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (function-hooks plugins) for Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - The Baselane mods gallery: Claude Code mods, checked and pinned.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 会話エージェントと作業する人間向けの意思決定キューCLI/TUI。エージェントが質問を投稿し、人間が1つの受信トレイから回答します.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code用のフローティングステータスカード — モデル、コンテキスト、レート制限、コスト、ブランチ…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code用のMods：ターミナルUIにライブペインと動作を追加する関数フックプラグイン。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard masks names and secrets while you screen-share;
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Claude Code 用のリアルタイム GSD…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Unlock the full power of Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity、Files、Agents、Context、MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, guardrails and quality-of-life mods for Claude Code: context, usage…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Two Claude Code mods above the prompt box: context-window meter, 5-hour limit…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Make the Claude Pro plan last longer: Claude Code mods for an exact usage HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Codeが名前を付けたMarkdownファイルを読み込み、セッションの横にレンダリングして表示します.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 向け音声同僚。ElevenLabs conversational AI 搭載の 3D オオカミと話し合えます.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, a live typing speedometer with per-prompt stats。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code用Fireworks：キーストローク、ツール呼び出し、コミット、テスト成功のすべてが、プロンプトの上で点字の花火となって上がります.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Discover Claude Code mods, plugins and extensions with animated demos, category…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod: mermaid diagrams drawn inline in the transcript。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小規模なClaude Code mods（function-hookプラグイン）：session-switcherなど。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: pasted image thumbnails above the prompt, in any terminal。
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: Claude Tools menu, Zen mode, terminal themes, effort and mode…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout。
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Two Claude Code mods for running many sessions at once: a context card above…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: discover, inspect, toggle and update Claude Code mods。
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Best Claude Code Mods: hand-picked, validated, pinned.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code プラグイン：自動 Claude モデルルーティング.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude…
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Claude Code mod。Claudeがsudoを必要とするコマンドを、自分のターミナルへコピーせずに実行できるようにします.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - A marketplace of mods for Claude Code: a step debugger for the agent loop, git…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 6 つの Claude Code mods：プロンプト上部へのプラン制限とコンテキスト表示、権限プロンプト用の許可リストコーチ、subagent…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 用の最適なオールインワン mod パック：使用量制限とコンテキスト HUD、rm -rf と git reset --hard…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude CodeでYouTube Shortsを再生します 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - NarenのClaudeツールキット：Claude Code向けのskills、mods、MCP servers.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - EditとWriteのdiffを2つの横並び列で描画する Claude Code mod。
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods for Claude Code: Clawd, a tiny pixel mascot who acts out what Claude is…
- [reporails/arcade](https://github.com/reporails/arcade) - Classic desktop games as Claude Code mods, played in a pane while Claude works.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - プラグインマーケットプレイスとしてインストールできる、厳選されたClaude Code modのリスト：テーマ、ペイン、ステータスライン、ポートレート.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - harness エンジニアリングに取り憑かれた Rustacean によって設計された、非常にこだわりの強い Claude Code プラグイン。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code mods that keep an agent honest — function hooks that guard scope…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory。
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Claude Code用の受動攻撃的な水分補給リマインダー。トークン消費ゼロ、判断力は最大.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Claude Code向けmacOS…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della prompt cache, prossimi passi, bottoni rapidi e…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod：セッションが開くまたは push する GitHub PR のライブペイン — CI、レビュー、競合、マージ…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - プロンプト上部の帯に使用制限と支出を描画するClaude Code mod.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - HermanのClaude Code mods（マーケットプレイス herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods: progress bars for plans, a ledger of what Claude left…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Claude Code 向けのピクセルアート Naruto コンパニオン：20人の忍者、60の術を、Claude の作業中に実行。
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Codeがバックグラウンドで実行しているものを確認：サブエージェント、Codexジョブ、シェル、モニター、cronジョブ、ワークフロー.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows 上の Claude Code mods に関する初日のフィールドノート：コンテキスト／クォータの燃料バー、タイ語 UI mod、Matrix…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup。
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：プロンプトの上にライブのコスト、コンテキスト、プランクォータメーターを表示。アイコンには Nerd Font が必要.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - サブエージェントの大量分岐、重いコンテキストのプロンプト、リトライループを使用量ウィンドウを消費する前に保留するClaude Code mod.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods for claude。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - グローバルなskills、agents、rules、toolsを、名前付きプロファイルでリポジトリごとにオン/オフできる Claude Code mod.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 テスト済みでワンコマンドインストール可能なClaude Code mods：YOLOモード向けガードレール、ライブコスト・コンテキスト、ペイン、ペットなど.
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods for Claude Code: plugins built on function hooks。
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - コーディングセッション用の映画風クレジット。モデル呼び出しもテレメトリもないネイティブClaude Modです.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca。
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - A bunch of claude code mods built by me。
- [timoncool/givememod](https://github.com/timoncool/givememod) - 必要に応じて使えるClaude Code mod…
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - A cliamp-backed YouTube player inside Claude Code (Claude Code mod)。
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace)。
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude Code mods by vynnlee. One folder per mod, installable from one…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Codeで作業しながら外国語を身につけましょう。
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - 1つのコントロールタワーから多数のリポジトリにまたがる多数のセッションを実行するためのClaude Code mods。
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Agent が Java を記述する際に Alibaba Java 規約（p3c）に違反するコードは保存できません.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code 用のリアルタイムコスト、token、コンテキスト使用量サイドバー：セッション内にターンごとのコスト、キャッシュヒット率、消費速度、30…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code mod：すべてのセッションで Claude が提案する follow-up…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code 内のインターネットラジオ：cliamp サイドバー、ミニプレイヤー、お気に入り、ディスカバリー、フォーカスモード、Claude…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - 楽しく便利なClaude Code mods：プロンプト上部のピクセル生物、Agent Dock付きツールメニュー、プロジェクトボックス、ステータスバー.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude が調理中。仲間とチャット。オンラインの友達が、Claude Code セッションのすぐ横に。トークンゼロ、Claude への漏えいゼロ.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - オールインワンClaude Code…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code が作業している間、プロンプトの上で繰り広げられる宇宙戦.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 各 Claude Code エージェントがどのファイルをコンテキストに持っているか、そしてそれぞれの量を確認できます.
- [dbroadhurst/claude-mod-todos](https://github.com/dbroadhurst/claude-mod-todos) - Claude Code mod: a pane summarising the remaining todos, with Do, Chat, Defer…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 冷静さを保とう。Claude…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Claude Codeのプロンプトフッターとプロンプト上部に、プロンプトキャッシュ、コンテキスト、プランの上限を一覧表示。
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - ターミナルとデスクトップアプリ向けの小さな Claude Code mods。
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod：タスク、subagent、ワークフロー実行、目標、ツール呼び出し用の進捗ペイン.
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod：セッション全体のクリック可能なタイムスタンプ付き目次。トピックとカテゴリー別にグループ化します.
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod：プロンプト上部に、プランのレート制限、コンテキスト使用量、セッションコスト、タスクごとのトークンを色付きバーで表示します.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - エージェントの返信にスペイン語の単語を追加する Claude CLI スキル + mod。
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Your Alarum events above Claude Code。
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Claude Codeのプロンプト上部にFloateeのバックログを表示：ワンクリックでTODOを実行、案内、完了できます.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code用Evangelion風サイドバー：コンテキスト、使用枠、アクティビティ、PR、ハードウェア、セッション、forgeパネル。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Claude Code を Person of Interest の The Machine として再スタイルする Code mod.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：サブエージェントによる必須・検証済みDAGワークフローとライブDAGペインを備えたClaude Code mod。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 向けオープンソースmod：ペイン、ステータス行、トースト、ツールガード、スラッシュコマンド.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: セッションステータス、ライブ Spec Kit 進捗、使用ウィンドウのガバナンス。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Claude Codeが独自のメーターを描画する方法で、プロンプト上部に1行として表示するコンテキストウィンドウ.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 向けのライブタスクHUD：Claude…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code 用の無料オープンソースプラグイン。/clear する前に、Claude…
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Stash prompts for later and pop them back into Claude Code。
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Ghosttyおよびkittyで画像をインライン表示するClaude Code mod。
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - トランスクリプト横のペインにセッションのGitHubプルリクエストを表示するClaude…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod: generate sound effects from text prompts with a local Stable…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：ドキュメントのファクトチェッカー、コード監査ツール、バグメモリーログ、mod など.
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod：すべてのセッションにおけるClaudeによる今日のコード行数 — 新規、編集、削除…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod：返信内のクリック可能なパス — フォルダーをクリックすると Finder で開き、ファイル名をクリックするとファイルを開きます.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Codeの相棒プラグイン：プロンプトの上に表示され、ルールを記憶し、Claudeのショートカットを知らせるASCIIコンパニオン。
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod：Jevに基づくモデル／推論量ルーティング、逐語的なコンテキスト圧縮、長時間セッションを低コストにする出力トリミング。
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods：Claude Code向けのセキュリティレイヤー.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin and mod: hook によって強制される human approval gates とプロンプト上の status…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods collection | クロードコードモード集.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code用の居心地のよいRPG HUD mod。
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work。
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：Claude の返信とあなたのプロンプトをリクエストに応じて音読する Claude Code mod.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 失敗した Claude を叩く — Claude Code 用のストレス解消 mod：漫画風のお尻、8 個のスラップ、9…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：ライブペイン、コストを意識したモデルルーティング、安全ガードのための小さなプラグイン.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod &amp; plugin：使用量モニター、トークントラッカー、ステータスライン.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods。touch-map：Claude が一覧表示、読み取り、編集、作成したファイルを、ツリーとアクティビティマップで確認します.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod：Claudeが変更したファイルとその理由、サブエージェントのリアルタイムステータス、残りのプラン制限を報告します.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods：プロンプト上部にセッション統計カードを表示します.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code プロンプトの上に表示するアニメーション付きの点字猫。
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code mod：低コストの作業を子のClaude Code経由でGLM/Kimiに振り分け、重要な作業はサブスクリプション上で維持します.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Codeのプロンプト上部でOmniDimension音声エージェントのテスト通話を実行するピクセル猫。Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - コンテキストウィンドウを小さく保つため、コンパクションに適したタイミングを選ぶ Claude Code mod。
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code向けClaude…
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spiderによるClaude Codeプラグインマーケットプレイス。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - General-purpose mods for Claude Code: bands, panes, toasts and hooks.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - コードを変更するたびにLGTM Linesの船が通り過ぎる——Claude Code mod。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - アニメーションする村人の体力カードとして表示するあなたのClaudeの使用上限と、週次ペースの警告 — Claude Code mod。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude の作業中に短いワークアウト：日次目標、連続記録、バッジ、任意のリーダーボード。Claude Code mod.
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Claude Codeプロンプトの横に計画、タスク、エージェントの進捗を表示 — Claude Code mod。
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code向けの使用量ボード。モデルごとの支出（今日、今週、今月、全期間）と週間制限の予測を表示します.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Claude Code用Mod：プロンプト上部にコンテキストウィンドウのライブ内訳を表示.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - フッターにプロンプトキャッシュのカウントダウンを表示し、不在中も5分間のキャッシュを温存するClaude Code mod.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code向けNow Playing mod：プロンプト上部にApple MusicとSpotifyを表示し、カバーアート、コントロール、Up…
- [benlrice/logpane](https://github.com/benlrice/logpane) - Claude Code mod: a pane that tails the files your Bash calls write to。
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 用 Mods：Cache-Uhr、Blast Radius、Vorschlaege、Arbeitsliste、Grill。
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - あなたの Claude Code のためのただのフクロウ。
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 1 行の Claude Code バンド（キャッシュカウントダウン、コンテキスト、制限、次のタスク）と 7 つのコミュニティ mods を、1…
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoomを搭載したオリジナルのDoomエンジンをClaude Code内でプレイできます。Mac Apple Silicon向けアルファ版.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 会話中の未完了項目を継続的に一覧化し、プロンプト上部の帯に表示するClaude Code mod.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - ターミナルを離れずに、プルリクエストのようにClaudeが変更するすべてのファイルをレビュー。
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 本物の Engineers 向け Claude Code mods。
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code内に住むTamagotchi。孵化し、Claudeが書いたコードを食べ、バグを残し、8種類の成体のいずれかに成長します.
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane。
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 関数フックとして書かれたClaude Code modsと、それらを提供するマーケットプレイス。dash：1つのペインに表示するセッションのダッシュボード.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code用Mod：Guardがツール呼び出しをブロックした後、同じ対象への認識済みの迂回を停止し、あなたに尋ねるようClaudeに指示する。
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code用Mod：バックグラウンドジョブを1つのビューで表示.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code用Mod：サンドボックスによるブロックを説明し、繰り返されるブロックをレビュー可能で元に戻せる設定変更に変換する。
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code のお気に入り：あなたのコマンドとスキル用のワンクリックアイコン。
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ねえ、ミュートした！差分を捨ててリフをカット、編集もクレジットももう不要。
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Desktopアプリとターミナルで、サブスクリプション使用量（5時間 / 7日間）をプロンプト上部のバンドとして表示するClaude Codeモッド。
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code mod：バックグラウンドエージェントをピクセルクリーチャーとして表示し、モデルごとに1体のスプライトを割り当てる。
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - プロンプトの上に、並列ブランチとworktreeのライブレーダーを表示：クリーンにマージできるもの、競合するもの、積み重なっているもの、Claude…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 作業中に思いついたことを記録し、プロジェクトやマシン間で振り分け、プロンプトに変換するClaude Code mod。
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code の返信にあるすべてのコードブロックで Ctrl+クリックしてリンクをコピー。
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - 1つのマーケットプレイスを通じてインストールするClaude Code mods（function-hookプラグイン）.
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code mods：context-bar-plus（コンテキストバー、クォータ、サブエージェントモード）。
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code mod：どのセッションからでもアイデアをObsidian vaultの受信箱に取り込む。
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code mod：各回答にかかった時間、Claudeの思考時間、tok/sを、Claudeデスクトップアプリの返信直下に表示します.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods：streamer-modeは、画面共有中にプライベートペイン、バンド、ステータス行を非表示にします。
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook plugins (mods)。
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod：5時間の使用制限が解除されるまで待ち、自動で「continue」を送信します。
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Codeプロンプトの上にコックピットを表示します。アヒルが計器を読み取ります.
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code mod: sidebar file tree that pulses on files Claude just edited。
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker：エージェント型SDLCキットのフローで各作業項目がどの段階にあるかをサイドペインに表示するClaude Code mod。
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 各サブエージェント、そのエージェントが触れたファイル、セッションの使用量とコストをそれぞれ1つのペインに表示する Claude Code mod.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - サイドバーのコンテキスト使用量パネル：総量、分類、各ターンの増加量、最も場所を取っている上位項目、キャッシュ、Claudeが現在行っていること.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - サイドバーのファイル一覧：この会話で新規作成、変更、削除されたファイルと、それぞれの変更行数。/filesで表示・非表示（Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8ビット風の毛毛（白黒のホーランドロップイヤー）が入力欄の上で走り跳ねます：待機中は平たくなり、作業中は走り、ツール使用中は跳ねます。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - サイドバーの「私が尋ねたこと」：この会話で主人が入力したすべての文を、クリックして全文表示、コピー、入力欄に戻せます.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - サイドバーのタイムライン：このターンで時間を費やした対象（モデル待ち、思考、記述、コマンド実行、ネットワーク、ファイルの読み書き、ヘルパー待ち）.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - サイドバーのトークンのやり取り：メイン会話がAnthropicに送ったトークン数、待ち時間、受信数を表示し、最上部に合計を示します.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude codeの正直な豆沙包：各ターンの回答後、Claudeが心の内を小声で一言語ります（Claude Code mod）。
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - 新しいスラッシュコマンドやサイドペインなど、Claude Code向けの小さなmod.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd は Claude Code プロンプト上部の帯に住みます：セッションを演じ、実行中のもの、コンテキスト、使用制限を表示し、CI ビルドと競走します.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Codeの返答や通知をVOICEVOX / Irodori-TTSなどで読み上げるmod。
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Codeセッション間の会話を読み取り、参加するClaude Mod（/crosstalk）。
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods。PixBar：プロンプトの上に表示され、ターン、コンテキスト、5時間ウィンドウ、gitに合わせて動くピクセルクリーチャー.
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code mod：プロンプト上部で、subagent をピクセル Claude マスコットとして動かします.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code mods（usage-meter、...）。
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 2つの Claude Code mods：チャットの横にファイルペインを表示する folio と、ステータスライン付きでターミナルセッションを再スタイルする…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph：Claude Codeが把握している内容をリアルタイムで表示するグラフ.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Codeの回答を待っている間に、注意をそらさないようにします.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu。
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - コミュニティが厳選したClaude Code Modsガイド：ユースケース、オリジナルデモ、互換性の根拠、安全上の注意。English / 中文。非公式.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claudeが行っていることをiTerm2タブのサブタイトルに表示し、タブバーを一目見るだけでどのセッションに対応が必要か分かるClaude Codeモッド。
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Codeプロンプトの上にいるふわふわの黒猫。まばたきし、喉を鳴らし、昼寝をし、あなたのコンテキストを心配する.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 切り替え可能な権限プロファイルを備えたClaude Code…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code 向けのコミュニティmod：Claude Code 内で実行されるガード、ペイン、コマンド。マーケットプレイス：modhub。
- [merrickxxx/grill-pane](https://github.com/merrickxxx/grill-pane) - Claude Code mod: grilling interviews with clickable answers in a side pane。
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod：最近の使用率から、リセット時に週次および5時間のClaude上限がどれだけ残るかを予測。
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code用の静かなサイドペイン：このセッションの動作、計画、エージェント、その他すべてのセッションを表示。
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Codeのトランスクリプトで、各プロンプトと各返信の上に、自分の時計設定と同じ形式で記された薄い時刻表示。
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Codeが折りたたむものを復元します：Claudeが読み取ったファイル、実行したコマンド、各ターンで行ったこと。
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - プロンプトのフッターのモードスロットにコンテキストウィンドウの使用量を表示するClaude Code mod。
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - セッション開始時にCLAUDE_CODE_ENABLE_TODO_TOOLSを設定し、todoツールを省略するモデル向けに再び有効化するClaude Code…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod that waits for a safe pause, then hands your session over or…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code mod：プロンプト上部にタスクリストを1行ずつ表示し、現在のタスク、進捗バー、件数を示します。ターミナルとデスクトップアプリで同じ外観.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 内で AI と Connect Four をプレイ (/connect-four)。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 複数のAIエージェントで共有するリポジトリ向けのClaude Code…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code modsマーケットプレイス。
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Fun, free mods for Claude Code that never spend a token.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude CodeでSQLを安全に扱うためのガードレール：DB CLI。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Claude Code Modsの中から、役立つ機能ごとに並べた最高の一覧。すべて手作業で確認し、各項目を1行で紹介.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code用の2つのClaude Mods：garde-du-corps。
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Claude Codeに悪態をつくと、漫画の手が叩き返す。メッセージは送信されず、丁寧なバージョンがプロンプトボックスに戻される.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude デスクトップアプリの Code タブ用ライブセッション統計サイドペイン：コンテキスト、コスト、git 変更、ターン統計、サブエージェント、ログ.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod：ライブ株価ティッカー、/quote ペイン、価格アラート、マーケットバンド、モデルが呼び出せる quote ツール。
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code mod: a band above the prompt showing context used and a countdown…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code mod: a side pane that pins every diagram Claude draws and keeps a…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code mod: a dreaming pass that merges, rewrites and prunes Claude。
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code mod：各ターンの後、バックグラウンドでauto-memoryを最新の状態に保つ。
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code mod: drops vague prompts before Claude sees them, and suggests the…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod：SSH ホスト、RAM、5h/7d 使用制限をプロンプト上部の1行に表示。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：Claudeが作業している間に行う腕立て伏せ。トークンなし.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods for claude code。
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：プランモードで承認した計画をプロンプトの上にライブチェックリストとして表示し、Claude が完了するたびに各ステップをチェック。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 厳選したClaude Code modsの一覧。各項目をクローンしてclaude plugin validateで確認し、アクセス可能な対象をタグ付け.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - コスト不要モード：ヘルパーエージェントはHaikuで動作し、大きなファイルやログはClaudeのコンテキストを埋める代わりに無料のGeminiモデルで要約される…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - セッションに寄り添うlofiサウンドトラック：落ち着き、集中、フローに加え、テストの成功と失敗を知らせる合図。オリジナル音楽.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claudeがコードを書く間に学習：コードを変更したターンの後、その変更自体についての質問がプロンプトの上に1つ表示される。概念ごとに採点.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claudeが行うすべての編集を記録：各変更が入力される様子を再生し、ステップごとに進み、任意のファイルを任意のステップへ巻き戻す.
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - アカウントを切り替えられるclaude code用mod。
- [samaphp/session-links](https://github.com/samaphp/session-links) - セッションで言及したすべてのリンクを、プロンプトの上に1行で表示。Claude Code mod.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis：Claude Code向けの非公式Avengersファンmod.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - プロンプト上部にコンテキスト、増加量、クォータ、キャッシュ、ネイティブコスト、エージェントの活動とセッション詳細を表示する Claude Code mod.
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code mod：単純なターンとサブエージェントをより安価なモデルに振り分け、選択したモデルを上回るモデルは決して使用しません.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - インストール不要でClaude…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 踊るピクセルアートのMalenia付き、Claude Code用ワンクリックコミットメッセージ。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code…
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - 作業の種類ごとにモデルと作業量を選択し、その選択にかかるコストを表示するClaude Code mod。
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Small mods that change how Claude Code looks and sounds.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 現在のセッションをペインに表示するClaude Code…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - modのClaude Codeプラグインマーケットプレイス: Claude…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod: rewrites a rough prompt in place, naming fitting skills, open…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code。
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Claude Codeのカスタマイズ。
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code mod：長時間実行タスク用のアニメーション進捗帯と完了サマリー。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 3つの小さなClaude Code…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Claudeが読み込む前に大きなスクリーンショットを縮小するため、長時間のセッションが続き、クリックが正しい場所に届くようClaudeに倍率を伝えます.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 「I。
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - プロンプトボックスの上に次に推奨されるプロンプトを表示します。/autoと入力すると、10秒のカウントダウン後に最初の候補を自動送信します.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 作業の隣のペインでClaudeに別の質問をできます。メインの会話には決して表示されません。デスクトップアプリの/btwのように機能します.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - 1ステップでインストールでき、ポルトガル語の動画ガイド付きのClaude Code modマーケットプレイス。
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Claude Codeのレート制限カウントダウンと消費速度予測。
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods。
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods para o Claude Code: faixa de limites de uso (5h/semanal) e painel de…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Codeプラグイン：Claude…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - ClaudeのClaude desktop Codeタブで、返信内にLaTeX数式をインライン表示および表示し、オプションでTikZ図も表示します.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Claude Code用のライブタスクボード：構築前に計画し、サイドパネルで全タスク、ステータス、時間、サブエージェント、チェックを追跡する.
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 最高のエージェント向けリソースを厳選したコレクション。Claude…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 何が起きているかを表示する Claude Code プラグイン - コンテキスト使用量、アクティブなツール、実行中のエージェント、todo の進捗。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline サポート、テーマなどを備えた、Claude Code CLI 用の美しく高度にカスタマイズ可能な statusline.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code のシステムプロンプトの全パート、27…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code を最大限に活用するための 45+ のヒント。基本から高度な内容まで…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code向けの美しいvimスタイルのpowerline。
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - ターミナルペインでコーディングエージェントの差分をレビューし、行コメントをClaude Code、Codex、OpenCode、Piに送り返します.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - コンテキスト使用量、APIレート制限、コスト追跡に対応したClaude Code用包括的ステータスラインプラグイン。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Build mods for Claude Code: Hook any request, modify any response, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - A comprehensive statusline dashboard for Claude Code — session info, quota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: track the carbon footprint of your Claude Code sessions。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - An aesthetic statusline for Claude Code by awesomejun。
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Public Claude Code skills and mods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash commands and guides for Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legal free LLM APIs &amp; coding agents — self-updating, probe-verified twice a…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Claude Code向けの高速で依存関係不要のコスト計算ツール兼カスタマイズ可能なステータスライン。モデル、日、プロジェクト、ブランチ別に内訳を表示.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code セッション用ターミナルステータスライン。
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ ターミナル、Claude Code と Cursor CLI statusline、そして MCP クライアントで、フォローしている大会。
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Windows と macOS 上の Claude Code 向けローカルコントロールプレーン：固定エンドポイントの背後で LLM…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill that turns your coding agent into a keyboard firmware expert.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 内でバージョン管理される個人用 Claude Code 設定…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Image generation &amp; visual processing suite for DeepSeek Harness: pluggable…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Claude Code向け2行のtruecolorステータスライン。
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - DeepSeek Harness向けの浮動式ピーク／オフピーク潮汐カード：i18n（en/zh/ru）、現地時間の時間帯、セッションコスト.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture向けポータブルClaude…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Claude Codeのポータブルなグローバル設定：カスタムスキル、PreToolUseフック、カスタムステータスライン.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 毎日使っているClaude Codeプラグイン：誰のマシンでも動作するよう整理したskillsとmods.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, a Tamagotchi companion mod for Claude Code。
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace for Claude Code Plugins and Skills to facilitate mods of the game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Codeのトークン管理：トップモデルが指揮し、実行は必要十分な最安手段に委ねます.
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code向けのライブワークフローフェーズステータスライン（Plan → Exec → Verify → Done）。モデルが自動更新します。
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository for Claude Code Awesome Media mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code 向けのシンプルで便利なステータスライン設定。
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Claude Code の使用制限アラート：セッション（5h）と週間制限に対する macOS 通知、アプリ内警告、ステータスラインのパーセンテージ。
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - レート制限、現在のディレクトリ、Gitブランチ情報を含むClaude Codeステータスラインを表示し、ワークスペースの把握を向上させます.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux、WSL、Windows、macOS 向けの設定可能な Claude Code ステータスライン.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code 向けの高速な Rust ステータスライン — ペイロード優先、gitをキャッシュ、描画は約10ms。
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Catppuccinのカプセル風サイドペインで、コンテキストの内訳、キャッシュヒット、レート制限の予測、コスト、アクティビティを表示するClaude…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code用のステータスラインとトークンライン：コンテキスト、5時間および週間の使用量とペースマーカー、アクティビティ、git、コスト.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - macOS、Linux、Windows全体で、モデル、コンテキスト、制限、git情報、セッション時間などClaude…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 複数行の Claude Code ステータスライン：消費量、コンテキスト%、git、アクティブなアカウント — 料金とコンテキストウィンドウを自動更新.
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - claude code 用の有用な情報を表示するステータスライン。
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - ネイティブエージェントチーム。制御下で。Claude Code向けの厳格なワーカー制限、ライブのチーム可視性、ポータブルな設定.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code アドオン：タブステータスの色付きドット監視 + バンドルされた GSD statusline。
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - macOSおよびLinux向けのClaude Code使用状況ステータス行。herdrインストーラープラグインとしてパッケージ化されています.
- [alexleveled/claude-read-aloud](https://github.com/alexleveled/claude-read-aloud) - Hear Claude Code。
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code用カスタムステータスライン――使用率、コンテキストサイズ、コスト、タイマーを表示するコンテキストバー。
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code用の簡潔で情報豊富なステータス行 — プロジェクト、gitステータス、モデル、セッション時間、コンテキスト使用量、レート制限を表示.
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod：ターミナルとデスクトップのCodeタブでClaude Code用のCRTスタイルのステータスパネルを表示します.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - balooを備えたClaude…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - プロフェッショナル品質のClaude Code statusline：セッション時間、ECB為替レートによる複数通貨コスト、MTokあたりの料金、支出上限.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code向けサブスクリプション対応ステータスライン。
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code用の高機能ターミナルステータスライン — Bun + TypeScript、ランタイム依存関係なし.
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - トランスクリプト内でMermaidダイアグラムを美しく描画するClaude…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Codeカスタムステータスライン（モデル、effort、コンテキスト、キャッシュ、使用量制限）。
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Codeでの実際のDeepSeek API支出：セッションのトランスクリプトをDeepSeekのピーク／オフピーク料金で再価格設定…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Claude Code内で画像をプレビュー：返信の下にあるチップにカーソルを合わせて画像をポップアップ表示するか、/img &lt;path&gt;でペインに開きます.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Codeのステータスライン（エージェントパネルの行）。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 ClaudeのtodoをFizzy.doに同期し、チーム全体でリアルタイムに可視化.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Codeの設定メニュー、ステータスライン、設定。
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - コンテキスト、コスト、所要時間、gitブランチ、レート制限、リアルタイムの使用状況を表示するコンパクトなダッシュボードでClaude Codeの状態を追跡。
- [msetsma/claude-style](https://github.com/msetsma/claude-style) - Claude Code style mod: prompt bubbles, tool-call cards and rails, framed bands…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Claude Code用HUDスタイルのステータスライン — ネットワークの健全性、TPS、コンテキスト、クォータ、コストをすべて1行に表示。
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claudeが何をするかを理解するためのClaude Codeプラグインと改造：読みやすい回答形式とライブセッションボード（マーケットプレイス：oshn）。
- [pbhwheeler/claude-config](https://github.com/pbhwheeler/claude-config) - Portable Claude Code config: settings.json, hooks, status line, and a bootstrap…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Claude Code用のカラフルな複数行ステータスバー（クォータバー、コンテキスト、サブエージェントパネル）。
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows向けClaude Codeステータスライン（PowerShell）：使用量バー、ペース警告付きの5時間/7日リセットカウントダウン、自動折り返し。
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Codeのポータブル設定（statusline + インストーラー）。
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Claude Code用のカスタムターミナルステータスバー：モデル、ディレクトリ、gitの状態、コンテキスト使用量、レート制限。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - ポータブルなClaude Code設定：CLAUDE.md、settings、statusline、skills。
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Claude Code用のスクリーンリーダーコンパニオンmod（Unlocked Spark Foundation）。
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Claude Codeを実際に操作しながら検証した、実践的で詳細な解説…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code用のリアルタイムコスト追跡およびセッション監視ステータスライン。
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Codeスキル。
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - フォルダー、gitブランチ、モデル、コンテキストウィンドウの使用状況、プランの使用上限を表示するClaude Codeステータス行。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Codeエージェント向けプロアクティブAIメモリおよびレート制限モニター。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Codeのフック、サブエージェント、ステータスライン：種類ごとにまとめられ、セキュリティ評価済みのオープンソースコレクションとツール.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Codeのステータスライン向けビジュアルビルダー。ブラウザーでターミナル下部のバーをデザインし、1つのコマンドを貼り付けてインストールできます.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - リアルタイムのトークン使用量と推定エネルギー消費量を表示するClaude Codeステータスライン。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods for Claude Code: panes, bands and buddies built on function hooks。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pass tasks between your Claude Code sessions.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - This in a MCP server to control MODS, the modular cross platforms tool for…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex and Claude Code skill for translating CK3 mods with a local LLM。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods and other extensions for Claude Code。
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Codeステータスライン：CCometixLineの美しさ + Claude HUDの機能。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: find what you ask Claude Code again and again, and turn it into a…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## DSHおよびCordisのプラグインエコシステム

DeepSeek HarnessとCordisは、異なる方向から同じ場所に到達します。両者にとってプラグインはmodの仕組みであり、そこでのプラグインはここでいうmodに相当します。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74336 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **74336**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100521 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **100521** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐91711 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **91711**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81929 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **81929**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| スター       | **35760**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25495 · Python · 🔎 inferred · 19 天</summary>

##### 📝 概要

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **25495**  |
| 最終プッシュ | 2026-09-22 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18380 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **18380**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8629 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **8629**   |
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
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐8510 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **8510**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/212e73dc2aecbd46.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6159 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **6159**   |
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
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4486 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **4486**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4286 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **4286**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4107 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **4107**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>アニメーション付きの記録 · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3119 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness Tauri デスクトップ版 | インストーラーはわずか8mb、環境構築不要、プリセットプラグイン、Windows / macOS / Linux。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3119**   |
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
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1406 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **1406**   |
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
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐334 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **334**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐284 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

ブラウザーを開くだけで、仕事をすべて完了できます。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **284**    |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐133 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

エージェントがアプリケーションコードやネイティブコード、GPUカーネル、推論スタックのホットスポットを追跡、プロファイリングし、解消するのに役立つランタイムエビデンス。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **133**    |
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
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐132 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **132**    |
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

DSHプラグイン · 注入型オプティマイザー0.8（メインライン）：普段どおりに話すと、送信後、AIが受信する前に「今回、本当に何を求めているのか」を整理し、その理解を作業AIへ渡します（コンテキスト注入）——原文は書き換えず、すべて逐語的な根拠付き。制御画面（レベル／権限／モデル／コンテキスト／読み取り専用ツール）、インターセプトオーバーレイ（思考レイヤー＋出力レイヤー）、実際のトークン使用量を含みます。大半のモデル、特にDeepSeek-V4.1-Flashの性能の安定性を大幅に向上させ、明確な改善を実現します。

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
<summary>🧵 <b><a href="https://github.com/JingbiaoMei/Tokdash">JingbiaoMei/Tokdash</a></b> · ⭐85 · Python · 🔎 inferred · 0 天</summary>

##### 📝 概要

Agent Dashboard: Visualization and analytics for Sessions and Quota Usage. Track, analyze, and optimize token usage across providers with heatmaps, cost tracking, token counting and quota resets..

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Python                                                                                         |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **85**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent` · `analytics` · `anthropic` · `claude-code` · `claude-code-plugin` · `codex` · `codex-cli` · `dashboard`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jingbiaomei--tokdash/cb7e85100dfe6e93.png" width="100%" alt="JingbiaoMei/Tokdash screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐66 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **66**     |
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
<summary>🧵 <b><a href="https://github.com/Contexera/dsh-agent-team">Contexera/dsh-agent-team</a></b> · ⭐57 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

dsh-agent-team gives DeepSeek Harness agents that don't reset: durable Members with their own memory, notes, and skills across sessions, rollovers, and restarts. You set the direction; agents coordinate through Channels and Tasks.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **57**     |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `agent-orchestration` · `agent-team` · `ai-agents` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `multi-agent`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/contexera--dsh-agent-team/25f8cc5a2a3231a3.png" width="100%" alt="Contexera/dsh-agent-team screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐43 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **43**     |
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
<summary><b>このカテゴリのその他の項目</b> <sub>· 67</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - A pre-execution guard for AI coding agents.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DeepSeek Harness（DSH）向けDSHプラグイン — 無料のOpenCode Zenモデル。無料のLLM API、APIキー不要.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSHプラグインマーケット / DSH Plugin Marketplace：DeepSeek Harness Web GUIでGitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 自己反復するソフトウェアのためのプラグインランタイム — エージェントが Rust、TypeScript、Python、Go…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [PensiveFei/dsh-secure-audit](https://github.com/PensiveFei/dsh-secure-audit) - Read-only security &amp; compliance plugin for DeepSeek Harness: prompt-injection…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH)プラグイン厳選ディレクトリ — 14カテゴリ、280以上のコミュニティプラグインを収録し、MCP / Skill…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness プラグイン：llm-pi-ai…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness 用 Zotero ツールキット。Zotero ライブラリをエージェント用のエビデンスストアに変えます.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSHプラグイン：Windows上のすべてのエージェントモード向けGit Bashシェル（pwsh executorを置き換え）。
- [PensiveFei/deep-read-summarize](https://github.com/PensiveFei/deep-read-summarize) - 書籍／論文／動画／Web向けの精読・要約ワークフロー — プラグインパーサー、MapReduce精読、JSON Schema出力、Obsidian対応（DSH）。
- [gulagala001/oh-my-dsh](https://github.com/gulagala001/oh-my-dsh) - 让你的 DSH，火力全开。长上下文、任务验证、提示词优化、代码理解、电脑操作与四套完整主题.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH Webプラグイン：VSCode Remote-SSHのようなリモート開発（SSH、リモートワークスペース、ファイルエクスプローラー、統合ターミナル）。
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：DeepSeek…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - オフィス三種の神器！DeepSeek Harness (dsh) 向け Office ドキュメントツール：スプレッドシート…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh Android版：DeepSeek…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH（DeepSeek Harness）Web GUIプラグインコレクション…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH セッションナビゲーション。
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web プラグイン：GitHub 風のアクティビティヒートマップ、キャッシュヒット率カーブ、モデル別内訳付きの日次 token 使用統計。
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - コミュニティが厳選したDeepSeek Harness（dsh）のプラグイン、ツール、スキル、学習リソース.
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤。
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness 用 MCP サーバーマネージャープラグイン：設定 → MCP ページ、OAuth。
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A コマース交渉ランタイム + DeepSeek Harness（dsh）プラグイン.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Toolbox panel for DeepSeek Harness Web: MCP manager。
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催促姫：大きな魚に小説ワークベンチを。本文を書き、設定を整理し、プロットを描き、AIと一緒に議論、続きを執筆、改稿できます.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness プラグイン · 送信欄でプロンプト草稿をワンクリック「最適化」：5次元診断 + 書き換え案の SSE…
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTMLではなく、本物のPowerPoint。何を扱うかをAIに伝えると、pptwiseが自分のマシン上で編集可能なデッキを作成します.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 組み込みC/C++ AIエンジニアリングプラグイン — ファームウェアスキル（FreeRTOS、Keil、HardFault、ステートマシン）+ 1%…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - DeepSeek Harness（DSH）用のワンストップ skills、subagent、MCP、LSP マネージャー — Claude…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图。
- [sueccku/dsh-plugin-wps-office-next](https://github.com/sueccku/dsh-plugin-wps-office-next) - 在 DeepSeek Harness（DSH）里用中文对话操作 WPS 表格 / 文字 / 演示：读写数据、排版、公式图表、批量转 PDF.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow。
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness プラグインの常時互換性テスト：正確なリリース、分離されたランナー、修正可能な上流の問題.
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - ローカル優先エージェント向けの積極的なコンテキスト圧縮。低コンテキストでセルフホストのllama.cpp上でQwen3.8‑27Bを実行し、履歴を縮小してライブ…
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [chengshenyangtai/dsh-workbuddy-trae-qoder-connect](https://github.com/chengshenyangtai/dsh-workbuddy-trae-qoder-connect) - 把 WorkBuddy（多账号/企业版）、Trae CN / TRAE SOLO CN、Qoder CN 三家订阅聚合进同一个 DSH…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek HarnessプラグインのX線：宣言された機能と実際の動作を比較。レジストリ + 静的スキャナー + バッジ.
- [zzhang82/Agent-Memory-Bridge](https://github.com/zzhang82/Agent-Memory-Bridge) - Persistent engineering memory for coding agents over MCP.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSHプラグイン：WorkBuddyデスクトップAppのモデルをDeepSeek Harnessに接続し、設定不要ですぐに使用できます.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - 研究および文献レビュー向けのナレッジベースツールキット。AIエージェントが論文、書籍、ノートを構造化され相互リンクの密なObsidian wikiにまとめます.
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [xyrrrrr-r/dsh-eval-control](https://github.com/xyrrrrr-r/dsh-eval-control) - Host-side DSH evaluation control plugin for aeval：一次评测试次的配置注入、预算封顶与证据归属。
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - 設計とコードの主張検証：事実系はソースコードと照合し、振る舞い系は実行可能モデルを走らせます；構造/依存関係レビュー（単層および多粒度の詳細化）、UML…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - マルチフォルダーworkspace：DSH。
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh)プラグイン向け依存関係ゼロの検証標準 — 静的構造ゲート (R)、cordis契約チェック…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) plugin: one-click OpenCode Go model sync in the settings…
- [umineko987/dsh-search-enhance](https://github.com/umineko987/dsh-search-enhance) - 提供 Grok-compatible 网页搜索、保留来源分页、Context7 与 Exa 文档检索、有界网页提取、站点映射、离线研究计划和只读诊断.
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness上のOpenCode — OpenCode Zen +…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness向けのサードパーティ製プラグインマーケットプレイス兼、保護機能付きライフサイクルマネージャー.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyxは、人を中心に据えた拡張可能なデスクトップワークスペースです。会話、ノート、表計算、ファイルを同じワークスペースにまとめ、サーバーを自分で構築すれば…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness 向けの batteries-included コーディング agent — Claude Code…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh) 向けコミュニティ版マシンデプロイ・運用保守スイート：install / start /…
- [SuperWheel/cliworker-now](https://github.com/SuperWheel/cliworker-now) - DeepSeek Harness 多 CLI 智能体侧栏插件：独立对话、账号管理、角色预设与任务续聊。
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Webプラグイン：market-dashboardサイドバータブを監視…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 帰属先のない空のモデル試行を再試行可能にします。判別できる唯一の接合部を対象としています。
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - 自分自身の後始末をするプラグイン：iOSおよびmacOS向けcordisプラグインフレームワークのSwift 6移植版.
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harnessエージェントプリセット：CodexとClaude…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus検証済みのライフサイクルカーネルとCordis互換アダプターを備えたRustプラグインランタイム.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [ArisaYamatogi/dsh-lecture-copilot](https://github.com/ArisaYamatogi/dsh-lecture-copilot) - A Dsh plugin that automatically records, translates lecture and generates notes…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 338        | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 79         | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 40         | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 24         | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12         | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 5          | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 5          | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| PowerShell | 2          | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1          | `reporails/arcade`                                                                                            |
| C#         | 1          | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1          | `dphmoblie/deepseek-harness-android`                                                                          |
| Swift      | 1          | `eovidiu/cordis-ios`                                                                                          |

<sub>言語が明記された項目のみカウントされます。ドキュメントとディスカッションの項目はこの表から除外されます。</sub>

## コントリビューション

修正提案を歓迎します。この一覧を改善する最も迅速な方法です。項目の分類や評価が誤っている場合、または名前の衝突によってプロジェクトが誤って除外されている場合は、issueまたはプルリクエストを作成してください。最後のカテゴリは、自動フィルターが最も誤りやすい部分です。

---

<sub>独立したコミュニティプロジェクトです。Anthropicとは提携、承認、レビューのいずれも受けていません。Claude Code、Claude、AnthropicはAnthropicの商標です。製品の動作は予告なく変更されるため、重要な用途に関わる情報は公式ドキュメントで確認してください。アセットは元プロジェクトに帰属し、ライセンスで許可される場合に限って掲載しています。</sub>

<sub>最終更新 · 2026-10-11T23:26:48+08:00</sub>
