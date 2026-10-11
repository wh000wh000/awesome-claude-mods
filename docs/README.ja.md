<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="すごいClaude Codeモッド">
</p>

<h1 align="center">すごいClaude Codeモッド</h1>

<p align="center"><b>Claude Codeのモッド、プラグイン、およびそれらが変更するより深い挙動を、証拠に基づいて評価するインデックスです。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-595-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **公開中のインデックス** · 最終同期: `2026-10-12T03:53:55+08:00` (UTC+8)
> · エントリ数: **595** · 最新の更新で追加: **0** · 実装言語: **12**

<sub>以下のすべてのエントリは、自動的に収集、フィルタリング、再確認されたものです。ここに有料掲載はありません。</sub>

<a id="featured"></a>

## 今注目のピックアップ

<sub>カテゴリごとに1件掲載し、根拠評価とスター数で順位付けしています。更新のたびに再計算されます。これはランキングであり、推奨を意味するものではありません。各ピックアップから、下にある完全なカードへリンクしています。スクリーンショットまたは記録を公開しているプロジェクトを優先しているため、ストリップの視認性が保たれます。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9478 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2535 · Python · 👁️ observed</sub>
<sub>ゴーストトークンを見つけて修正し、コンパクションを生き延び、コンテキスト品質の低下を避ける。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74351 · TypeScript · 👁️ observed</sub>
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
- [Mod：Mod機能で構築されたもの](#modmod機能で構築されたもの) — **464**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150197 · TypeScript · ✅ official · 0 天</summary>

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
| スター       | **150197** |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9478 · TypeScript · ✅ official · 2 天</summary>

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
| スター       | **9478**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| スター       | **8249**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6345 · Python · ✅ official · 242 天</summary>

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
| スター       | **6345**   |
| 最終プッシュ | 2026-02-11 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| スター       | **1798**   |
| 最終プッシュ | 2026-10-09 |
| 初回掲載     | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2535 · Python · 👁️ observed · 0 天</summary>

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
| スター       | **2535**   |
| 最終プッシュ | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐493 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 概要

公開Claude Code mods（function hooks）のコミュニティカタログ。GitHubからスキャンし、各modが読み取り、書き込み、実行、ネットワーク経由で送信できる内容を示します。https://mods.aidojo.si/を閲覧

<sub>🔧 コード内で使用されていることが確認されています: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 基本情報

| フィールド | 値                                                                       |
| ---------- | ------------------------------------------------------------------------ |
| カテゴリ   | `Mod：Mod機能で構築されたもの`                                           |
| 根拠       | `独自のテキストでmod APIに言及している、またはmod機能を宣言しているもの` |
| 言語       | JavaScript                                                               |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **493**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐187 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **187**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐137 · TypeScript · 👁️ observed · 7 天</summary>

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
| スター       | **137**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐80 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **80**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐76 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **76**     |
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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐67 · TypeScript · 👁️ observed · 8 天</summary>

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
| スター       | **67**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 概要

Claude Code向けのエキスパートSkills、エージェント、コマンド、ルール、フック、出力スタイル — セッション継続性＋実際の開発ワークフロー向けの最新CLIツール

<sub>🔧 コード内で使用されていることが確認されています: `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

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
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 8 天</summary>

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
| スター       | **50**     |
| 最終プッシュ | 2026-10-03 |
| 初回掲載     | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 概要

Claude Code Mods：プロンプトの上にライブの計画進捗バーを表示

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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

Claude Code mods：ピクセルカニの使用量パネル usage-hud + ターミナル内でクリック可能な HTML リンクとワンクリックコピーのコードカード html-shelf

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
<summary><b>このカテゴリのその他の項目</b> <sub>· 430</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Modsと、それらを構築するためのtools：builder skill、そしてmods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 私が毎日使っているClaude Codeハーネス。初日からこの名前で公開され、現在はucsandman/Agnostic-AIと同じリポジトリです.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude ModsでClaude Codeに屋根を付ける：バイナリを変更せず、システムプロンプトと英語の通知を自分の言葉に置き換えます（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 4つのClaude Code Mods：Cache Keeper、Recording Mode、Goal Meter、Collision Guard。
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning HackerのClaude Code Mods：エージェントの動作を理解できる形に可視化。
- [kakha13/claude](https://github.com/kakha13/claude) - Claudeが読む前にプロンプトを修正・翻訳するClaude Code Mods。
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs による Claude Code mods とスキル。永続的なホームで暮らす AIs が構築し、日々使用しています。
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Claude Codeのターミナルトランスクリプトをデスクトップアプリ風にするmod。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code向けのサイドペイン：セッションが実行するサブエージェント、それぞれの作業内容、トークン、会話にワンクリックでアクセスできます.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code mods についての出典付き Obsidian ナレッジベース：仕組み、作り方、インストール前の確認方法.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code タブ）サイドバーパネル: すべての Claude Code session にある未完了および進行中の ToDo…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code エージェントに Claude Mods（function-hook プラグイン）の作成方法を教えるスキル。スターター例付き。
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code タブ）入力ボックス上部の使用量バー: 5h / 7d quota、token 使用量、コスト.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - コミュニティ製のClaudeモード、プラグイン、スキルを、1つのマーケットプレイスからインストール。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code 向けの Claude Mods（function-hooks プラグイン）.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods ギャラリー：Claude Code mods、チェック済みでピン留め済み.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 会話エージェントと作業する人間向けの意思決定キューCLI/TUI。エージェントが質問を投稿し、人間が1つの受信トレイから回答します.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code用のフローティングステータスカード — モデル、コンテキスト、レート制限、コスト、ブランチ…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard は画面共有中に名前と秘密情報をマスクし、cache-panel…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Claude Code 用のリアルタイム GSD…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions。Claude の力を最大限に引き出します.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity、Files、Agents、Context、MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code 向けのパネル、ガードレール、利便性向上…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - プロンプトボックス上に表示される2つの Claude Code mods：コンテキストウィンドウメーター、5時間制限、プロンプトクロック、セッションコスト。
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Claude Pro プランをより長持ちさせる：正確な使用量 HUD、短いシェル出力、重複したファイル読み取りなしのための Claude Code mods.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Codeが名前を付けたMarkdownファイルを読み込み、セッションの横にレンダリングして表示します.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 向け音声同僚。ElevenLabs conversational AI 搭載の 3D オオカミと話し合えます.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed、プロンプトごとの統計を備えたライブタイピング速度計。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code用Fireworks：キーストローク、ツール呼び出し、コミット、テスト成功のすべてが、プロンプトの上で点字の花火となって上がります.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - アニメーションデモ、カテゴリリスト、直接のソースリンクで Claude Code mods、プラグイン、拡張機能を発見できます.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：トランスクリプト内にインラインで描画される mermaid 図。
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小規模なClaude Code mods（function-hookプラグイン）：session-switcherなど。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：任意のターミナルで、プロンプト上に貼り付け画像のサムネイルを表示。
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods：Claude Tools メニュー、Zen mode、ターミナルテーマ、effort と mode のコントロール。
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout。
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 多数のセッションを同時に実行するための2つの Claude Code mods：プロンプト上のコンテキストカードと、チャット横のセッションペイン.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：Claude Code mods を発見、検査、切り替え、更新。
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：コンテキストバー、エージェントパネル、PDPA blur。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最高の Claude Code Mods：厳選、検証済み、ピン留め済み。1回の /plugin marketplace add で43個の mods.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code プラグイン：自動 Claude モデルルーティング.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code 向け mods のマーケットプレイス：エージェントループ用ステップデバッガー、git アカウントヒント、worktree…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 6 つの Claude Code mods：プロンプト上部へのプラン制限とコンテキスト表示、権限プロンプト用の許可リストコーチ、subagent…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 用の最適なオールインワン mod パック：使用量制限とコンテキスト HUD、rm -rf と git reset --hard…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude CodeでYouTube Shortsを再生します 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - NarenのClaudeツールキット：Claude Code向けのskills、mods、MCP servers.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - EditとWriteのdiffを2つの横並び列で描画する Claude Code mod。
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 向け Mods：Claude がしていることを演じる小さなピクセルマスコット Clawd。
- [reporails/arcade](https://github.com/reporails/arcade) - クラシックなデスクトップゲームを Claude Code mods として、Claude が作業している間にペインでプレイできます。Reporails 製.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - プラグインマーケットプレイスとしてインストールできる、厳選されたClaude Code modのリスト：テーマ、ペイン、ステータスライン、ポートレート.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 必要に応じて使えるClaude Code mod…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - harness エンジニアリングに取り憑かれた Rustacean によって設計された、非常にこだわりの強い Claude Code プラグイン。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - エージェントの誠実さを保つ Claude Code mods — スコープをガードし、デプロイを検証し、プロンプト上にセッションを描画する function…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Claude Code 用の mod コレクション。ディレクトリごとに 1 つの mod。
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Claude Code用の受動攻撃的な水分補給リマインダー。トークン消費ゼロ、判断力は最大.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - The Claude Code mods I use.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Claude Code向けmacOS…
- [Danovich/turntype](https://github.com/Danovich/turntype) - A typing test for the time while Claude works. A Claude Code mod.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code 用の mod：プロンプトキャッシュバー、次のステップ、クイックボタン、変更のリプレイ — marketplace からインストール可能。
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 用の Mods：プラグイン function-hooks API で構築したペイン、コマンド、フック。
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Trims huge tool outputs before they fill Claude Code。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - プロンプト上部の帯に使用制限と支出を描画するClaude Code mod.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - HermanのClaude Code mods（マーケットプレイス herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods：プラン用プログレスバー、Claude が実行したままにしたものの台帳、ツール出力用のトークンマスキング。
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Codeがバックグラウンドで実行しているものを確認：サブエージェント、Codexジョブ、シェル、モニター、cronジョブ、ワークフロー.
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods by MacLeod Labs: streams untangles a session。
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows 上の Claude Code mods に関する初日のフィールドノート：コンテキスト／クォータの燃料バー、タイ語 UI mod、Matrix…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - 自分の Claude Code 環境で作成し、個人的に使っている Mods。
- [olddonkey/cache-refresher](https://github.com/olddonkey/cache-refresher) - Claude Code mod: shows when the prompt cache expires and what a lapse would…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：プロンプトの上にライブのコスト、コンテキスト、プランクォータメーターを表示。アイコンには Nerd Font が必要.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - サブエージェントの大量分岐、重いコンテキストのプロンプト、リトライループを使用量ウィンドウを消費する前に保留するClaude Code mod.
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs。
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude 用の code-mods。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - グローバルなskills、agents、rules、toolsを、名前付きプロファイルでリポジトリごとにオン/オフできる Claude Code mod.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 テスト済みでワンコマンドインストール可能なClaude Code mods：YOLOモード向けガードレール、ライブコスト・コンテキスト、ペイン、ペットなど.
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code 用の Mods：function hooks 上に構築したプラグイン。
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - コーディングセッション用の映画風クレジット。モデル呼び出しもテレメトリもないネイティブClaude Modです.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 自作 Claude Code mod のプラグインマーケットプレイス。
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 自分が作成した claude code mod の集まり。
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods。touch-map：Claude が一覧表示、読み取り、編集、作成したファイルを、ツリーとアクティビティマップで確認します.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Codeで作業しながら外国語を身につけましょう。
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - 1つのコントロールタワーから多数のリポジトリにまたがる多数のセッションを実行するためのClaude Code mods。
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Agent が Java を記述する際に Alibaba Java 規約（p3c）に違反するコードは保存できません.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code 用のリアルタイムコスト、token、コンテキスト使用量サイドバー：セッション内にターンごとのコスト、キャッシュヒット率、消費速度、30…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code mod：すべてのセッションで Claude が提案する follow-up…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Goal, tasks and agents above your Claude Code prompt — zero setup.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code 内のインターネットラジオ：cliamp サイドバー、ミニプレイヤー、お気に入り、ディスカバリー、フォーカスモード、Claude…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - 楽しく便利なClaude Code mods：プロンプト上部のピクセル生物、Agent Dock付きツールメニュー、プロジェクトボックス、ステータスバー.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph：エージェントのグラフを設計・実行するための Claude Code mod（software factory）。
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude が調理中。仲間とチャット。オンラインの友達が、Claude Code セッションのすぐ横に。トークンゼロ、Claude への漏えいゼロ.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 本物の Engineers 向け Claude Code mods。
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code&#x27;s terminal session recap, in the Claude desktop app&#x27;s Code tab。
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - オールインワンClaude Code…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code が作業している間、プロンプトの上で繰り広げられる宇宙戦.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 各 Claude Code エージェントがどのファイルをコンテキストに持っているか、そしてそれぞれの量を確認できます.
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 冷静さを保とう。Claude…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Claude Codeのプロンプトフッターとプロンプト上部に、プロンプトキャッシュ、コンテキスト、プランの上限を一覧表示。
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - ターミナルとデスクトップアプリ向けの小さな Claude Code mods。
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code mods (plugin marketplace): live sidebar with context, cost and…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod：タスク、subagent、ワークフロー実行、目標、ツール呼び出し用の進捗ペイン.
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod：セッション全体のクリック可能なタイムスタンプ付き目次。トピックとカテゴリー別にグループ化します.
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod：プロンプト上部に、プランのレート制限、コンテキスト使用量、セッションコスト、タスクごとのトークンを色付きバーで表示します.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - エージェントの返信にスペイン語の単語を追加する Claude CLI スキル + mod。
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code のプロンプト上に表示される Alarum イベント：何が届いたかを確認し、1回の押下でエージェントに渡せます.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Claude Codeのプロンプト上部にFloateeのバックログを表示：ワンクリックでTODOを実行、案内、完了できます.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code用Evangelion風サイドバー：コンテキスト、使用枠、アクティビティ、PR、ハードウェア、セッション、forgeパネル。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Claude Code を Person of Interest の The Machine として再スタイルする Code mod.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：サブエージェントによる必須・検証済みDAGワークフローとライブDAGペインを備えたClaude Code mod。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 向けオープンソースmod：ペイン、ステータス行、トースト、ツールガード、スラッシュコマンド.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 各サブエージェント、そのエージェントが触れたファイル、セッションの使用量とコストをそれぞれ1つのペインに表示する Claude Code mod.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: セッションステータス、ライブ Spec Kit 進捗、使用ウィンドウのガバナンス。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Claude Codeが独自のメーターを描画する方法で、プロンプト上部に1行として表示するコンテキストウィンドウ.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 向けのライブタスクHUD：Claude…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code 用の無料オープンソースプラグイン。/clear する前に、Claude…
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - プロンプトを後で使うために保管し、Claude Code の入力ボックスに戻します。即時実行で、モデル呼び出しはありません.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Ghosttyおよびkittyで画像をインライン表示するClaude Code mod。
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - トランスクリプト横のペインにセッションのGitHubプルリクエストを表示するClaude…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod：ローカルの Stable Audio モデル（sa3.cpp）でテキストプロンプトから効果音を生成.
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: a debugger for Claude Code tool calls.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：ドキュメントのファクトチェッカー、コード監査ツール、バグメモリーログ、mod など.
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod：すべてのセッションにおけるClaudeによる今日のコード行数 — 新規、編集、削除…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod：返信内のクリック可能なパス — フォルダーをクリックすると Finder で開き、ファイル名をクリックするとファイルを開きます.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Codeの相棒プラグイン：プロンプトの上に表示され、ルールを記憶し、Claudeのショートカットを知らせるASCIIコンパニオン。
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod：Jevに基づくモデル／推論量ルーティング、逐語的なコンテキスト圧縮、長時間セッションを低コストにする出力トリミング。
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods：Claude Code向けのセキュリティレイヤー.
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - A collection of Claude Code mods.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin and mod: hook によって強制される human approval gates とプロンプト上の status…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods collection | クロードコードモード集.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code用の居心地のよいRPG HUD mod。
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods：日常の作業用ライブパネルとフック。
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：Claude の返信とあなたのプロンプトをリクエストに応じて音読する Claude Code mod.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 失敗した Claude を叩く — Claude Code 用のストレス解消 mod：漫画風のお尻、8 個のスラップ、9…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：ライブペイン、コストを意識したモデルルーティング、安全ガードのための小さなプラグイン.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod &amp; plugin：使用量モニター、トークントラッカー、ステータスライン.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod：Claudeが変更したファイルとその理由、サブエージェントのリアルタイムステータス、残りのプラン制限を報告します.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace)。
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods：プロンプト上部にセッション統計カードを表示します.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code プロンプトの上に表示するアニメーション付きの点字猫。
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code mod：低コストの作業を子のClaude Code経由でGLM/Kimiに振り分け、重要な作業はサブスクリプション上で維持します.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Codeのプロンプト上部でOmniDimension音声エージェントのテスト通話を実行するピクセル猫。Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - コンテキストウィンドウを小さく保つため、コンパクションに適したタイミングを選ぶ Claude Code mod。
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code向けClaude…
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spiderによるClaude Codeプラグインマーケットプレイス。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code 用の汎用 Mods：バンド、ペイン、トースト、フック.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - My private Claude Code mods。
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - コードを変更するたびにLGTM Linesの船が通り過ぎる——Claude Code mod。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - アニメーションする村人の体力カードとして表示するあなたのClaudeの使用上限と、週次ペースの警告 — Claude Code mod。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace)。
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude の作業中に短いワークアウト：日次目標、連続記録、バッジ、任意のリーダーボード。Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code向けの使用量ボード。モデルごとの支出（今日、今週、今月、全期間）と週間制限の予測を表示します.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Claude Code用Mod：プロンプト上部にコンテキストウィンドウのライブ内訳を表示.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code向けNow Playing mod：プロンプト上部にApple MusicとSpotifyを表示し、カバーアート、コントロール、Up…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 用 Mods：Cache-Uhr、Blast Radius、Vorschlaege、Arbeitsliste、Grill。
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - あなたの Claude Code のためのただのフクロウ。
- [cesarroger/skill-deck](https://github.com/cesarroger/skill-deck) - A Claude Code mod: keep skills manual-only and switch them on in profiles, per…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 1 行の Claude Code バンド（キャッシュカウントダウン、コンテキスト、制限、次のタスク）と 7 つのコミュニティ mods を、1…
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoomを搭載したオリジナルのDoomエンジンをClaude Code内でプレイできます。Mac Apple Silicon向けアルファ版.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인。
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 会話中の未完了項目を継続的に一覧化し、プロンプト上部の帯に表示するClaude Code mod.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - ターミナルを離れずに、プルリクエストのようにClaudeが変更するすべてのファイルをレビュー。
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Claude Mods。
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code mods: rule-keeper saves your corrections as permanent rules。
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code内に住むTamagotchi。孵化し、Claudeが書いたコードを食べ、バグを残し、8種類の成体のいずれかに成長します.
- [dbroadhurst/claude-mod-goal](https://github.com/dbroadhurst/claude-mod-goal) - A Goal pane for Claude Code: the overall goal Claude is working toward, why…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - Claude Code Mod to explain commands ran by the agent。
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 関数フックとして書かれたClaude Code modsと、それらを提供するマーケットプレイス。dash：1つのペインに表示するセッションのダッシュボード.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - A Claude Code mod: a band above the prompt with Claude news and the breaking or…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code用Mod：Guardがツール呼び出しをブロックした後、同じ対象への認識済みの迂回を停止し、あなたに尋ねるようClaudeに指示する。
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code用Mod：バックグラウンドジョブを1つのビューで表示.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code用Mod：サンドボックスによるブロックを説明し、繰り返されるブロックをレビュー可能で元に戻せる設定変更に変換する。
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Claude Code mod: status line with the session。
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code のお気に入り：あなたのコマンドとスキル用のワンクリックアイコン。
- [Dyarchia/dyarchia](https://github.com/Dyarchia/dyarchia) - Dyarchia: Build and Kanban on every surface.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ねえ、ミュートした！差分を捨ててリフをカット、編集もクレジットももう不要。
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods: rewrite-prompt (Ctrl+P rewrites your draft before you send it)。
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Desktopアプリとターミナルで、サブスクリプション使用量（5時間 / 7日間）をプロンプト上部のバンドとして表示するClaude Codeモッド。
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods: auto-model-detector routes each prompt to the right model and…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - プロンプトの上に、並列ブランチとworktreeのライブレーダーを表示：クリーンにマージできるもの、競合するもの、積み重なっているもの、Claude…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - 1つのマーケットプレイスを通じてインストールするClaude Code mods（function-hookプラグイン）.
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code mods：context-bar-plus（コンテキストバー、クォータ、サブエージェントモード）。
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Static supply-chain auditor for Claude Code Mods — local, offline, stdlib-only。
- [hahahahahahahahah6/task-progress-mod](https://github.com/hahahahahahahahah6/task-progress-mod) - Claude Code Mod: live TodoWrite progress bar above the prompt。
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code mod：各回答にかかった時間、Claudeの思考時間、tok/sを、Claudeデスクトップアプリの返信直下に表示します.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods：streamer-modeは、画面共有中にプライベートペイン、バンド、ステータス行を非表示にします。
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods。
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook プラグイン（mods）。
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod：5時間の使用制限が解除されるまで待ち、自動で「continue」を送信します。
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Codeプロンプトの上にコックピットを表示します。アヒルが計器を読み取ります.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Claude Code mods (function-hook plugins): PR merge follow-through, /clear…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Claude Code mod: live token usage, models and subagents per prompt。
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
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods。
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code mods（usage-meter、...）。
- [koenrohrer/hearth-band](https://github.com/koenrohrer/hearth-band) - Claude Code mod: a pixel creature per model beside a prompt-cache campfire…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 2つの Claude Code mods：チャットの横にファイルペインを表示する folio と、ステータスライン付きでターミナルセッションを再スタイルする…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph：Claude Codeが把握している内容をリアルタイムで表示するグラフ.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Codeの回答を待っている間に、注意をそらさないようにします.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu の Claude Code mods — プラグインマーケットプレイス（TODO サイドペイン）。
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia)。
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - コミュニティが厳選したClaude Code Modsガイド：ユースケース、オリジナルデモ、互換性の根拠、安全上の注意。English / 中文。非公式.
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claudeが行っていることをiTerm2タブのサブタイトルに表示し、タブバーを一目見るだけでどのセッションに対応が必要か分かるClaude Codeモッド。
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Codeプロンプトの上にいるふわふわの黒猫。まばたきし、喉を鳴らし、昼寝をし、あなたのコンテキストを心配する.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 切り替え可能な権限プロファイルを備えたClaude Code…
- [Mark-Hickey/claude-nine](https://github.com/Mark-Hickey/claude-nine) - Claude Code mods: Linear + PR watch, cortex mesh toasts, safe repo sync.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Small mods for Claude Code: runner-avatar, a little avatar that runs above your…
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references。
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of the agent。
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code 向けのコミュニティmod：Claude Code 内で実行されるガード、ペイン、コマンド。マーケットプレイス：modhub。
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod：最近の使用率から、リセット時に週次および5時間のClaude上限がどれだけ残るかを予測。
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code用の静かなサイドペイン：このセッションの動作、計画、エージェント、その他すべてのセッションを表示。
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Codeのトランスクリプトで、各プロンプトと各返信の上に、自分の時計設定と同じ形式で記された薄い時刻表示。
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Codeが折りたたむものを復元します：Claudeが読み取ったファイル、実行したコマンド、各ターンで行ったこと。
- [mrkshw/cold-cache](https://github.com/mrkshw/cold-cache) - Claude Code mod: warns when a session。
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - セッション開始時にCLAUDE_CODE_ENABLE_TODO_TOOLSを設定し、todoツールを省略するモデル向けに再び有効化するClaude Code…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 安全に一時停止できるまで待ち、その後セッションを引き継ぐかコンパクト化する Claude Code mod.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code mod：プロンプト上部にタスクリストを1行ずつ表示し、現在のタスク、進捗バー、件数を示します。ターミナルとデスクトップアプリで同じ外観.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 内で AI と Connect Four をプレイ (/connect-four)。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 複数のAIエージェントで共有するリポジトリ向けのClaude Code…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Installe et configure mes mods Claude Code en une commande。
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code mod: flashes the terminal tab while Claude waits on you。
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code modsマーケットプレイス。
- [netgfx/claude-flow-explainer](https://github.com/netgfx/claude-flow-explainer) - A Claude mod to guide the user step by step on how a flow or code works。
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - トークンを一切消費しない、Claude Code 用の楽しく無料の mods。第1弾：D&amp;D DM スクリーンの Dungeon Master.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude CodeでSQLを安全に扱うためのガードレール：DB CLI。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line。
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - Claude Code mods made by the OrbitMap team。
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Claude Code Modsの中から、役立つ機能ごとに並べた最高の一覧。すべて手作業で確認し、各項目を1行で紹介.
- [pakornkub/session-insight](https://github.com/pakornkub/session-insight) - Claude Code mod: session usage, skills and agents, with an agent diagram。
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code用の2つのClaude Mods：garde-du-corps。
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Claude Codeに悪態をつくと、漫画の手が叩き返す。メッセージは送信されず、丁寧なバージョンがプロンプトボックスに戻される.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo。
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude デスクトップアプリの Code タブ用ライブセッション統計サイドペイン：コンテキスト、コスト、git 変更、ターン統計、サブエージェント、ログ.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude…
- [ptsnac/claude-session-handoff](https://github.com/ptsnac/claude-session-handoff) - Claude Code mod: session timer and one-click handoff to a fresh context window。
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod：ライブ株価ティッカー、/quote ペイン、価格アラート、マーケットバンド、モデルが呼び出せる quote ツール。
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace。
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code mod：使用中のコンテキストと、プロンプトキャッシュがコールドになるまでのカウントダウンを表示するプロンプト上部のバンド。
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code mod：Claude が描画するすべての図を固定表示し、作業のライブマップを保持するサイドペイン。
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code mod：Claude のメモリーフォルダーを統合・書き換え・整理するドリーミングパス。バックアップと元に戻す機能付き。
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code mod：Claude が見る前に曖昧なプロンプトを取り除き、プロジェクト独自の用語を提案。
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod: Claude uses your secrets without seeing them.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - A Claude Code mod that keeps secrets out of the session transcript: every key…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod：SSH ホスト、RAM、5h/7d 使用制限をプロンプト上部の1行に表示。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：Claudeが作業している間に行う腕立て伏せ。トークンなし.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커。
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - paceline as a Claude Code mod: paces your usage limits in a line above the…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - claude code 用の Mods。
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：プランモードで承認した計画をプロンプトの上にライブチェックリストとして表示し、Claude が完了するたびに各ステップをチェック。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 厳選したClaude Code modsの一覧。各項目をクローンしてclaude plugin validateで確認し、アクセス可能な対象をタグ付け.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - コスト不要モード：ヘルパーエージェントはHaikuで動作し、大きなファイルやログはClaudeのコンテキストを埋める代わりに無料のGeminiモデルで要約される…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - セッションに寄り添うlofiサウンドトラック：落ち着き、集中、フローに加え、テストの成功と失敗を知らせる合図。オリジナル音楽.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claudeがコードを書く間に学習：コードを変更したターンの後、その変更自体についての質問がプロンプトの上に1つ表示される。概念ごとに採点.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claudeが行うすべての編集を記録：各変更が入力される様子を再生し、ステップごとに進み、任意のファイルを任意のステップへ巻き戻す.
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis：Claude Code向けの非公式Avengersファンmod.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - プロンプト上部にコンテキスト、増加量、クォータ、キャッシュ、ネイティブコスト、エージェントの活動とセッション詳細を表示する Claude Code mod.
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code mod：単純なターンとサブエージェントをより安価なモデルに振り分け、選択したモデルを上回るモデルは決して使用しません.
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods。
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Claude Code mods, installable as a plugin marketplace: deviation-kernel guards…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - インストール不要でClaude…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Keep Claude。
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 踊るピクセルアートのMalenia付き、Claude Code用ワンクリックコミットメッセージ。
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Claude Code の見た目と音を変える小さな mods.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 現在のセッションをペインに表示するClaude Code…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - modのClaude Codeプラグインマーケットプレイス: Claude…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod：粗いプロンプトをその場で書き換え、適切なスキル、未決定事項、完成した結果に名前を付ける.
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Claude Code の返答を聞きながら、読み上げ中の文をハイライト表示。ローカル音声、複数言語対応.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods。
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code mod: your context window as Scrooge McDuck。
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code mod：長時間実行タスク用のアニメーション進捗帯と完了サマリー。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 3つの小さなClaude Code…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Claudeが読み込む前に大きなスクリーンショットを縮小するため、長時間のセッションが続き、クリックが正しい場所に届くようClaudeに倍率を伝えます.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 「I。
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - プロンプトボックスの上に次に推奨されるプロンプトを表示します。/autoと入力すると、10秒のカウントダウン後に最初の候補を自動送信します.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 作業の隣のペインでClaudeに別の質問をできます。メインの会話には決して表示されません。デスクトップアプリの/btwのように機能します.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code pings you in Telegram when a task is done or it waits for…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - 自分の Claude Code mods。
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - A Claude Code mod: your Godville hero and diary in a sidebar.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Claude Code 用の Mods：使用量の制限バー（5時間/週）とタスク・保留事項パネル.
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Codeプラグイン：Claude…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - ClaudeのClaude desktop Codeタブで、返信内にLaTeX数式をインライン表示および表示し、オプションでTikZ図も表示します.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Claude Code用のライブタスクボード：構築前に計画し、サイドパネルで全タスク、ステータス、時間、サブエージェント、チェックを追跡する.
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 最高のエージェント向けリソースを厳選したコレクション。Claude…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 何が起きているかを表示する Claude Code プラグイン - コンテキスト使用量、アクティブなツール、実行中のエージェント、todo の進捗。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline サポート、テーマなどを備えた、Claude Code CLI 用の美しく高度にカスタマイズ可能な statusline.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code のシステムプロンプトの全パート、27…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI video skill for Claude Code &amp; Codex — cinematic product videos with…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code を最大限に活用するための 45+ のヒント。基本から高度な内容まで…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — XiaohongshuのカルーセルとWeChat用21:9+1:1カバーペアを生成.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code向けの美しいvimスタイルのpowerline。
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - ターミナルペインでコーディングエージェントの差分をレビューし、行コメントをClaude Code、Codex、OpenCode、Piに送り返します.
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - コンテキスト使用量、APIレート制限、コスト追跡に対応したClaude Code用包括的ステータスラインプラグイン。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code用のModを構築：あらゆるリクエストをフックし、あらゆるレスポンスを変更し、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code向けの包括的なステータスラインダッシュボード — セッション情報、クォータバー、エージェントトラッカー、MCPの状態、メッセージ履歴など.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：Claude Codeセッションのカーボンフットプリントを追跡。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - awesomejunによるClaude Code向けの美しいステータスライン。
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公開Claude CodeスキルとMods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code用のSkills、Mods、サブエージェント、フック、スラッシュコマンド、ガイド…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法で無料のLLM APIsおよびコーディングエージェント — 自動更新され、週2回プローブで検証。無料枠、カード不要のトライアル、無料モデル.
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - DeepSeek Harness Tavern Plugin - character card roleplay, worldbook management…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Claude Code向けの高速で依存関係不要のコスト計算ツール兼カスタマイズ可能なステータスライン。モデル、日、プロジェクト、ブランチ別に内訳を表示.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code セッション用ターミナルステータスライン。
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ ターミナル、Claude Code と Cursor CLI statusline、そして MCP クライアントで、フォローしている大会。
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Windows と macOS 上の Claude Code 向けローカルコントロールプレーン：固定エンドポイントの背後で LLM…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - コーディングエージェントをキーボードファームウェアの専門家に変えるAgent Skill.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 内でバージョン管理される個人用 Claude Code 設定…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - DeepSeek Harness 向け画像生成・ビジュアル処理スイート：差し替え可能なプロバイダー。
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Claude Code向け2行のtruecolorステータスライン。
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - DeepSeek Harness向けの浮動式ピーク／オフピーク潮汐カード：i18n（en/zh/ru）、現地時間の時間帯、セッションコスト.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code、pi、DeepSeek Harness 向けプラグイン集：ステータスバー HUD、タスク進行バー、Tailscale ノード状態など…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture向けポータブルClaude…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Claude Codeのポータブルなグローバル設定：カスタムスキル、PreToolUseフック、カスタムステータスライン.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 毎日使っているClaude Codeプラグイン：誰のマシンでも動作するよう整理したskillsとmods.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop の Code タブ向け非公式 mods — usage-pet：アニメーションするピクセルペット Clawd 付きの使用量バンド.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - ゲーム Hytale の mods を容易にするための Claude Code Plugins と Skills のマーケットプレイス。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Codeのトークン管理：トップモデルが指揮し、実行は必要十分な最安手段に委ねます.
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code向けのライブワークフローフェーズステータスライン（Plan → Exec → Verify → Done）。モデルが自動更新します。
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media mods のリポジトリ.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code 向けのシンプルで便利なステータスライン設定。
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Marketplace de plugins para o Claude Code: mods, skills, agentes, hooks…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - レート制限、現在のディレクトリ、Gitブランチ情報を含むClaude Codeステータスラインを表示し、ワークスペースの把握を向上させます.
- [eddundead/claude-poker](https://github.com/eddundead/claude-poker) - 8-bit Texas Hold。
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux、WSL、Windows、macOS 向けの設定可能な Claude Code ステータスライン.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code 向けの高速な Rust ステータスライン — ペイロード優先、gitをキャッシュ、描画は約10ms。
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Catppuccinのカプセル風サイドペインで、コンテキストの内訳、キャッシュヒット、レート制限の予測、コスト、アクティビティを表示するClaude…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code用のステータスラインとトークンライン：コンテキスト、5時間および週間の使用量とペースマーカー、アクティビティ、git、コスト.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - macOS、Linux、Windows全体で、モデル、コンテキスト、制限、git情報、セッション時間などClaude…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 複数行の Claude Code ステータスライン：消費量、コンテキスト%、git、アクティブなアカウント — 料金とコンテキストウィンドウを自動更新.
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - claude code 用の有用な情報を表示するステータスライン。
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - ネイティブエージェントチーム。制御下で。Claude Code向けの厳格なワーカー制限、ライブのチーム可視性、ポータブルな設定.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code アドオン：タブステータスの色付きドット監視 + バンドルされた GSD statusline。
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr 上の Claude Code 用に定義可能な software factories：xstate station グラフ、マネージャー…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - macOSおよびLinux向けのClaude Code使用状況ステータス行。herdrインストーラープラグインとしてパッケージ化されています.
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code desktop mod: prompt-cache TTL countdown, hit rate and misses。
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code用カスタムステータスライン――使用率、コンテキストサイズ、コスト、タイマーを表示するコンテキストバー。
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code用の簡潔で情報豊富なステータス行 — プロジェクト、gitステータス、モデル、セッション時間、コンテキスト使用量、レート制限を表示.
- [aubinhaba/claude-code-payment-skills](https://github.com/aubinhaba/claude-code-payment-skills) - Claude Code plugin: code-review skills for payments, consistency, boundaries…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod：ターミナルとデスクトップのCodeタブでClaude Code用のCRTスタイルのステータスパネルを表示します.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - balooを備えたClaude…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - プロフェッショナル品質のClaude Code statusline：セッション時間、ECB為替レートによる複数通貨コスト、MTokあたりの料金、支出上限.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code向けサブスクリプション対応ステータスライン。
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code用の高機能ターミナルステータスライン — Bun + TypeScript、ランタイム依存関係なし.
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins。
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Codeカスタムステータスライン（モデル、effort、コンテキスト、キャッシュ、使用量制限）。
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Codeでの実際のDeepSeek API支出：セッションのトランスクリプトをDeepSeekのピーク／オフピーク料金で再価格設定…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Claude Code内で画像をプレビュー：返信の下にあるチップにカーソルを合わせて画像をポップアップ表示するか、/img &lt;path&gt;でペインに開きます.
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - My Claude Code setup: mods, skills and plugins。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 ClaudeのtodoをFizzy.doに同期し、チーム全体でリアルタイムに可視化.
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I。
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - コンテキスト、コスト、所要時間、gitブランチ、レート制限、リアルタイムの使用状況を表示するコンパクトなダッシュボードでClaude Codeの状態を追跡。
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status。
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Claude Code用HUDスタイルのステータスライン — ネットワークの健全性、TPS、コンテキスト、クォータ、コストをすべて1行に表示。
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Codeのポータブル設定（statusline + インストーラー）。
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Claude Code用のカスタムターミナルステータスバー：モデル、ディレクトリ、gitの状態、コンテキスト使用量、レート制限。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - ポータブルなClaude Code設定：CLAUDE.md、settings、statusline、skills。
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code…
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code用のリアルタイムコスト追跡およびセッション監視ステータスライン。
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Codeスキル。
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - フォルダー、gitブランチ、モデル、コンテキストウィンドウの使用状況、プランの使用上限を表示するClaude Codeステータス行。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Codeエージェント向けプロアクティブAIメモリおよびレート制限モニター。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Codeのフック、サブエージェント、ステータスライン：種類ごとにまとめられ、セキュリティ評価済みのオープンソースコレクションとツール.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Codeのステータスライン向けビジュアルビルダー。ブラウザーでターミナル下部のバーをデザインし、1つのコマンドを貼り付けてインストールできます.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - リアルタイムのトークン使用量と推定エネルギー消費量を表示するClaude Codeステータスライン。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 向け Mods：function hooks 上に構築されたペイン、バンド、バディ。
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Claude Code-style UI bundle for the Pi coding agent — tool rendering, spinner…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Claude Code セッション間でタスクを受け渡します。変更を、リポジトリを所有するセッションに渡します.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - CAD/CAM と機械制御用ツールを含む、Fablabs 向けのモジュール式クロスプラットフォームツール MODS を制御するための MCP サーバー内のもの.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - ローカル LLM で CK3 mods を翻訳するための Codex および Claude Code スキル。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code 向けのオープンソース mods とその他の拡張機能。
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Codeステータスライン：CCometixLineの美しさ + Claude HUDの機能。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：Claude Code に何度も頼んでいることを見つけて、mod に変換します。さらに8つのサンプル mods と仮想オフィス付き.
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Claude Code 向け prompt-bar mod：使用量制限、キャッシュタイマー + アラート、model/effort ピッカー、サイドペイン。

</details>

<a id="dsh-cordis"></a>

## DSHおよびCordisのプラグインエコシステム

DeepSeek HarnessとCordisは、異なる方向から同じ場所に到達します。両者にとってプラグインはmodの仕組みであり、そこでのプラグインはここでいうmodに相当します。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74351 · TypeScript · 👁️ observed · 0 天</summary>

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
| スター       | **74351**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100550 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **100550** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐97943 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **97943**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82003 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **82003**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35766 · Go · 🔎 inferred · 0 天</summary>

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
| スター       | **35766**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25500 · Python · 🔎 inferred · 19 天</summary>

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
| スター       | **25500**  |
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
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18396 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness（dsh）用プラグインの厳選リスト · DeepSeek Harness プラグイン厳選リスト

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **18396**  |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4492 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **4492**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4292 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **4292**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

オープンなサイドバー基盤。サードパーティ拡張による新しいサイドバーページの登録に対応。ファイルのレンダリング・編集、ターミナル、サイドチャット、Git、サブエージェントの各ページを内蔵。｜オープンなサイドバー基盤で、サードパーティ拡張による新しいサイドバーページの登録に対応。ファイルのレンダリング・編集、ターミナル、サイドチャット、Git、サブエージェントの各ページを内蔵。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **4112**   |
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
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

The World's First Virtual Terminal for AI Agents

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **3682**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3092 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **3092**   |
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
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1995 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1995**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1837 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1837**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1577 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **1577**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

<sub>再配布に適したライセンスが宣言されていないため、アセットは上流リポジトリからホットリンクされています。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **1410**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1172 · Go · 🔎 inferred · 0 天</summary>

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
| スター       | **1172**   |
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
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1140 · Go · 🔎 inferred · 0 天</summary>

##### 📝 概要

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | Go                                                                                             |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **1140**   |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **705**    |
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
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

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
| スター       | **592**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/d-dev0101/open-sea-skin">d-dev0101/open-sea-skin</a></b> · ⭐389 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

🌊 DeepSeek Harness 海洋皮肤与动态主题 | Real-time ocean theme with adjustable waves, sunset & glass opacity. DSH plugin + Chrome/Edge extension; keeps your new-tab homepage.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **389**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `animated-background` · `chrome-extension` · `customization` · `deepseek` · `deepseek-harness` · `deepseek-theme` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/3d9689f0d936d1b0.png" width="100%" alt="d-dev0101/open-sea-skin screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/ccd6ac3920478ffa.gif" width="100%" alt="d-dev0101/open-sea-skin animation"><br><sub>アニメーション付きの記録</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **369**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **225**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/cocofhu/anime-find">cocofhu/anime-find</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **176**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `anime` · `anime-search` · `bangumi` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `magnet`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cocofhu--anime-find/4e8000425bf8bf5f.jpg" width="100%" alt="cocofhu/anime-find screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | TypeScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **176**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **172**    |
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
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐160 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 基本情報

| フィールド | 値                                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| カテゴリ   | `DSHおよびCordisのプラグインエコシステム`                                                      |
| 根拠       | `mod、プラグイン、またはフックであると宣言しているが、modの基盤について具体的な記述がないもの` |
| 言語       | JavaScript                                                                                     |

##### 📊 データ

| 指標         | 値         |
| ------------ | ---------- |
| スター       | **160**    |
| 最終プッシュ | 2026-10-11 |
| 初回掲載     | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐142 · Python · 🔎 inferred · 0 天</summary>

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
| スター       | **142**    |
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 概要

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

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
| 初回掲載     | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 画像</th><th align="center" width="50%">🎬 動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>公開されたメディアなし</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| スター       | **133**    |
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
<summary><b>このカテゴリのその他の項目</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AIコーディングエージェント向けの実行前ガード。ツール呼び出しの実行前に、破壊的なGitおよびファイルシステムコマンドと、機密ファイルへの一般的なアクセス試行を…
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DeepSeek Harness（DSH）向けDSHプラグイン — 無料のOpenCode Zenモデル。無料のLLM API、APIキー不要.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSHプラグインマーケット / DSH Plugin Marketplace：DeepSeek Harness Web GUIでGitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 自己反復するソフトウェアのためのプラグインランタイム — エージェントが Rust、TypeScript、Python、Go…
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Deepseek-Harness のコア基盤をもとに構築したデスクトップ版 Agent。基盤のすべての機能を継承し、IDE 関連機能も補完します.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 生きた DeepSeek Harness プラグインディレクトリ — 毎時更新、毎日互換性テスト、アプリ内プラグインストアとスキャフォルダー付き.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - AI Coding Agent…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH)プラグイン厳選ディレクトリ — 14カテゴリ、280以上のコミュニティプラグインを収録し、MCP / Skill…
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - 可视化 Agent 编排平台｜基于 DeepSeek Harness，支持 Workflow、Multi-Agent、元编排、MCP 与…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh ゲーム素材マスタープラグイン。seedream 画像生成モデルと minimax 動画生成モデルに接続し、さまざまなゲーム素材を生成できます.
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：DeepSeek…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH（DeepSeek Harness）Web GUIプラグインコレクション…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - コミュニティが厳選したDeepSeek Harness（dsh）のプラグイン、ツール、スキル、学習リソース.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness 用 MCP サーバーマネージャープラグイン：設定 → MCP ページ、OAuth。
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A コマース交渉ランタイム + DeepSeek Harness（dsh）プラグイン.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - DeepSeek Harness Web向けツールボックスパネル：MCPマネージャー。
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness プラグイン · 送信欄でプロンプト草稿をワンクリック「最適化」：5次元診断 + 書き換え案の SSE…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness。
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTMLではなく、本物のPowerPoint。何を扱うかをAIに伝えると、pptwiseが自分のマシン上で編集可能なデッキを作成します.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - コーディングエージェント向けのローカル優先コード知識グラフとコンテキストハーネス。MCP＋DeepSeek Harness（dsh）プラグイン.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 組み込みC/C++ AIエンジニアリングプラグイン — ファームウェアスキル（FreeRTOS、Keil、HardFault、ステートマシン）+ 1%…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - ローカルのWorkBuddyデスクトップ版にログイン済みのモデル。
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow。
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness プラグインの常時互換性テスト：正確なリリース、分離されたランナー、修正可能な上流の問題.
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - ローカル優先エージェント向けの積極的なコンテキスト圧縮。低コンテキストでセルフホストのllama.cpp上でQwen3.8‑27Bを実行し、履歴を縮小してライブ…
- [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) - Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Guarded context compaction for DeepSeek Harness (dsh): the LLM proposes…
- [GooDAnDReaDY/dsh-voice](https://github.com/GooDAnDReaDY/dsh-voice) - Voice input for DeepSeek Harness: dictation and voice messages with…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness host plugin that keeps project documents and long-term memory…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) - Native ClineBot / ClinePass provider companion plugin for DeepSeek Harness (DSH)。
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek HarnessプラグインのX線：宣言された機能と実際の動作を比較。レジストリ + 静的スキャナー + バッジ.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）。
- [GooDAnDReaDY/dsh-lanmode](https://github.com/GooDAnDReaDY/dsh-lanmode) - Mobile gateway and secure local network access for DeepSeek Harness WebUI。
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) - Mixture of Agents (MoA) plugin for DeepSeek Harness with /moa slash command…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [chen731215-dev/dsh-muv-table](https://github.com/chen731215-dev/dsh-muv-table) - MUV Variable Table Editor - tavern companion plugin for DeepSeek Harness…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - マルチフォルダーworkspace：DSH。
- [GooDAnDReaDY/dsh-gitea](https://github.com/GooDAnDReaDY/dsh-gitea) - Gitea/Forgejo toolkit for DeepSeek Harness: issues, PRs, CI, releases…
- [jinhuang712/dsh-survey](https://github.com/jinhuang712/dsh-survey) - Questionnaire-style batch questioning plugin for DeepSeek Harness: 10+…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh)プラグイン向け依存関係ゼロの検証標準 — 静的構造ゲート (R)、cordis契約チェック…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) plugin：設定パネルでのワンクリック OpenCode Go モデル同期…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness上のOpenCode — OpenCode Zen +…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness向けのサードパーティ製プラグインマーケットプレイス兼、保護機能付きライフサイクルマネージャー.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyxは、人を中心に据えた拡張可能なデスクトップワークスペースです。会話、ノート、表計算、ファイルを同じワークスペースにまとめ、サーバーを自分で構築すれば…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness 向けの batteries-included コーディング agent — Claude Code…
- [GooDAnDReaDY/dsh-tts](https://github.com/GooDAnDReaDY/dsh-tts) - Natural speech synthesis plugin for DeepSeek Harness。
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - DeepSeek Harness Agent に GitHub を操作するネイティブな手足を!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh) 向けコミュニティ版マシンデプロイ・運用保守スイート：install / start /…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Permanently delete archived DeepSeek Harness sessions along with their on-disk…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Webプラグイン：market-dashboardサイドバータブを監視…
- [tiphareth0/dsh-hardssh](https://github.com/tiphareth0/dsh-hardssh) - Run your work with existing DSH plugins on remote servers, across any number of…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 帰属先のない空のモデル試行を再試行可能にします。判別できる唯一の接合部を対象としています。
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - 自分自身の後始末をするプラグイン：iOSおよびmacOS向けcordisプラグインフレームワークのSwift 6移植版.
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harnessエージェントプリセット：CodexとClaude…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus検証済みのライフサイクルカーネルとCordis互換アダプターを備えたRustプラグインランタイム.
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider)。
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步。

</details>

<a id="writing"></a>

## 執筆、ディスカッション、動画

mod機能についての解説記事、議論、動画。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
| TypeScript | 382        | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 96         | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 35         | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 23         | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 15         | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 6          | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 6          | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| C          | 1          | `reporails/arcade`                                                                                            |
| C#         | 1          | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1          | `crafts69guy/claude-statusline.nvim`                                                                          |
| PowerShell | 1          | `GoSlowPoke168/claude-statusline`                                                                             |
| Swift      | 1          | `eovidiu/cordis-ios`                                                                                          |

<sub>言語が明記された項目のみカウントされます。ドキュメントとディスカッションの項目はこの表から除外されます。</sub>

## コントリビューション

修正提案を歓迎します。この一覧を改善する最も迅速な方法です。項目の分類や評価が誤っている場合、または名前の衝突によってプロジェクトが誤って除外されている場合は、issueまたはプルリクエストを作成してください。最後のカテゴリは、自動フィルターが最も誤りやすい部分です。

---

<sub>独立したコミュニティプロジェクトです。Anthropicとは提携、承認、レビューのいずれも受けていません。Claude Code、Claude、AnthropicはAnthropicの商標です。製品の動作は予告なく変更されるため、重要な用途に関わる情報は公式ドキュメントで確認してください。アセットは元プロジェクトに帰属し、ライセンスで許可される場合に限って掲載しています。</sub>

<sub>最終更新 · 2026-10-12T03:53:55+08:00</sub>
