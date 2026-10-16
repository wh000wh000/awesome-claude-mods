<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="超讚的 Claude 模組">
</p>

<h1 align="center">超讚的 Claude 模組</h1>

<p align="center"><b>依證據分級的 Claude Code 模組、外掛，以及它們改變的更深層行為索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-587-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <b>繁體中文</b> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **即時索引** · 上次同步: `2026-10-16T19:18:13+08:00` (UTC+8)
> · 條目: **587** · 最新更新新增項目: **0** · 實作語言: **14**

<sub>以下每個條目都經過自動收集、篩選與再次核查。這裡沒有任何付費置入。</sub>

<a id="featured"></a>

## 當下精選

<sub>每個分類選出一個項目，依證據等級和星標排序，並在每次更新時重新計算。這是排名，不代表背書；每個精選項目都會連結至下方的完整卡片。優先選擇發布了截圖或錄影的專案，讓這個橫列保持視覺化。</sub>

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
<sub>找出幽靈 token。修復它們。在壓縮中存活。避免上下文品質衰退。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐75403 · TypeScript · 👁️ observed</sub>
<sub>🌊 原始代理人框架。部署智慧型多玩家群集、協調自主工作流程，並建構對話式 AI 系統。具備自適應記憶、自我學習智慧、聯邦、向量 RAG 整合，以及原生支援 Claude Code / Codex / Hermes 和許多其他工具</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐16 · 👁️ observed</sub>
</td>
</tr>
</table>

## 內容

- [什麼是 Claude Code 模組](#什麼是-claude-code-模組)
- [條目分級方式](#條目分級方式)
- [官方：Anthropic 自有的程式碼儲存庫與版本發行說明](#官方anthropic-自有的程式碼儲存庫與版本發行說明) — **18**
- [模組：使用模組功能建立](#模組使用模組功能建立) — **466**
- [DSH 與 Cordis 外掛生態系](#dsh-與-cordis-外掛生態系) — **93**
- [文章、討論與影片](#文章討論與影片) — **10**
- [按實作語言分類的專案](#按實作語言分類的專案)

## 什麼是 Claude Code 模組

Claude Code 在 2.1.287 版加入了 **模組**：這類擴充功能能比外掛程式改變更深層的行為，並繪製自己的介面。

模組可以掛接 `ui.render`，在提示旁繪製 **列、區帶、窗格或卡片**；使用 `$.ui.selection()` 讀取你最後選取的文字；使用 `agent.spawn` 產生隊友；並擁有一個 `Client` 區域。無法繪製的模組只會自行失效——`ui.fault` 能避免單一故障模組拖垮工作階段。

此清單涵蓋模組、其所建立的外掛程式與 hook 介面，以及 DSH 和 Cordis 的對應功能。清單刻意**不**涵蓋更廣泛的 Claude Code 生態系：提示套件不是模組。

## 條目分級方式

這個領域的大多數清單只宣稱某項目應被納入。本清單會說明實際驗證到的程度，然後讓你據此篩選。等級描述的是證據，而不是專案品質——一個尚未有人撰文介紹、但製作精良的模組，仍然只是 `inferred`。

| 評級                                                | 代表意義                                                                                                                                                |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `由 Anthropic 本身發布`                             | 由 Anthropic 本身發布，或直接從官方變更日誌讀取。                                                                                                       |
| `其自身文字提到模組 API，或宣告具備模組功能`        | 其自身文字提到模組介面的一部分——`ui.render`、`ui.fault`、`agent.spawn`、`$.ui.selection()`、窗格、區帶或卡片——因此作者描述的是建構在實際 API 上的內容。 |
| `宣告為模組、外掛程式或 hook，但未具體提及模組介面` | 它自稱為模組、外掛程式或 hook，但其文字沒有具體提及模組介面。確實存在，但尚未確認。                                                                     |
| `僅因詞彙相符`                                      | 僅因詞彙相符。納入是為了讓篩選結果可稽核，而不是因為我們相信它。                                                                                        |

<a id="official"></a>

## 官方：Anthropic 自有的程式碼儲存庫與版本發行說明

Anthropic 自有的 Claude Code 程式碼儲存庫，以及定義模組介面的版本發行內容。直接閱讀來源，而非摘要整理。

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151169 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Summary

Claude Code 是一款駐留在終端機中的代理式編碼工具，能理解您的程式碼庫，並透過執行例行工作、解釋複雜程式碼及處理 git 工作流程，協助您更快速地編寫程式碼——全部透過自然語言指令完成。

<sub>🔧 在程式碼中找到使用處: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |
| 語言     | TypeScript                                         |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **151169** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9530 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |
| 語言     | TypeScript                                         |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9530**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8290 · Python · ✅ official · 0 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |
| 語言     | Python                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8290**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6397 · Python · ✅ official · 246 天</summary>

##### 📝 Summary

一個由 AI 驅動的安全審查 GitHub Action，使用 Claude 分析程式碼變更中的安全漏洞。

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |
| 語言     | Python                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6397**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |
| 語言     | Shell                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1813**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

##### 📝 Summary

Claude Model Cards 的補充材料

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25**     |
| Last push    | 2025-12-05 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

新增 Claude Mods：外掛現在可以修改更深層的行為 新增 You should know，一個內建模組，由側邊代理程式替你留意，並標示你或 Claude 可能錯過的事項。使用 `/plugin enable cc-plugin-you-should-know@builtin` 開啟（適用於已啟用遙測的第一方工作階段）

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

為 mods 新增 `$.ui.selection()`：在全螢幕模式中返回你最後選取的文字；當選取內容位於單一轉錄列內時，則返回該列。修正了在 Claude Code 重新啟動前繪製的檢視中按下 mod 按鈕時，該按鈕有時會執行另一個按鈕動作的問題。修正了當插件或 mod 在提示詞上方顯示列時，開啟背景任務對話方塊會使全螢幕工作階段因「無法復原的介面錯誤」退出的問題。修正了 `claude plugin test` 將 mods 回報為遠端停用，但實際上只是讀取了過時儲存設定的問題

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

修正了複合 shell 指令的巢狀部分中的 deny 或 ask 規則，在受管理機器上無法持續套用於使用者安裝的 mod 核准狀態的問題。修正了升級後第一個工作階段未載入已安裝 mods 的問題。為隊友新增 `agent.spawn`，在插件 hook 事件中使用一個代理程式 id，並在 `$.agent.list()` 中新增閒置與等待狀態。修正了 mod 的 `ui.render` hook 寫入某個值、導致列在繪製時拋出錯誤而使工作階段因「無法復原的介面錯誤」結束的問題；引擎現在會改為繪製自己的列。修正了 mod 面板或列中的右對齊內容繪製在關閉標記或 `\[-\]` 下方的問題，

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

在 mod 的 `turn.step` hook 結果中加入 `serverToolUses`：該工具會自行執行 API（顧問），每次執行都包含其 id、名稱、輸入、開始與結束時間。在 mod 的 `tool.check` hook 讀取的問題與判定中加入 `ceiling`，並命名組織要求工具取得的核准。在外掛 hooks 型別定義中加入 `ThemeKey` 與 `Color` 型別，讓編輯器列出 mod 繪圖可命名的主題色彩。加入至 `claude plugin validate`：mod 在閘門位置註冊的每個 hook 都會列出其是否具有 `.catch`（`--json` 下的 `gatingHooks`）。修正 mod 的 `turn.step` 結果

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

已新增 `prompt.autocomplete`，這是一個事件，mod 可掛接它以將自己的列加入提示框的自動完成清單 已為 mods 在 `$.model.complete` 中新增提示詞快取：`prompt` 與 `system` 接受文字區塊，而區塊上的 `cache: true` 會快取到該處為止的請求 已將工作流程代理加入 `agent.spawn` mod hook，包含其 run 與 index，讓 mod 可以拒絕它們 已修正 Write、Edit、NotebookEdit 與 LSP 列，以及單一 Read、Grep 與 Glob 列，隱藏 mod 拒絕呼叫的原因：該列現在會顯示原因 已修正 mod 的 `config.set`、`state.set`、`env.set` 或 `agent.spawn` hook 拒絕 afte

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

為模組將 `isDeferred` 加入 `$.tool.register`：`false` 從一開始就在提示中列出工具的結構描述，而不是藏在工具搜尋後方 修正模組在 `classic.*` 事件上的 hook，因外掛程式 hook worker 重啟而遭跳過，導致設定 hook 在沒有這些 hook 的情況下回應 修正呼叫 `$.session.append` 的模組執行 `claude plugin test` 失敗；測試可透過新的 `mock.session` 讀回附加的列

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-08 |

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 6</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 為 mods 新增了 `$.ui.notify`：透過你自己的通知設定發出原生通知，並說明是哪個 channel 傳送了它 為 mod 的 `Button`…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 修復在 `UserPromptSubmit` 掛鉤或模組的 `prompt.submit` 掛鉤期間按下 Esc…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod。
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod。
- [riffkit/skill](https://github.com/riffkit/skill) - Official Riffkit skill — riff a winning TikTok into your own short video from…

</details>

<a id="mods"></a>

## 模組：使用模組功能建立

此處的每個項目都展現了使用 Claude Code 在 2.1.287 中取得的功能的證據：它透過 `ui.render` 繪製內容、擁有窗格、區段或卡片、讀取 `$.ui.selection()`、使用 `agent.spawn` 產生隊友，或明確表示自己是模組。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2573 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

找出幽靈 token。修復它們。在壓縮中存活。避免上下文品質衰退。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | Python                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2573**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>動畫錄影</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐875 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Custom Claude Code Mods that I need

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **875**    |
| Last push    | 2026-10-14 |
| First listed | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐606 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

公開 Claude Code 模組（函式 Hooks）的社群目錄，從 GitHub 掃描，並列出每個模組可以讀取、寫入、執行或透過網路傳送的內容。瀏覽 https://mods.aidojo.si/

<sub>🔧 在程式碼中找到使用處: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **606**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐261 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mods：基於 hooks 建立的插件，可在提示上方加入即時列、防護、面板與遊戲。內容列、使用量計、Codex review watch、Markdown 預覽、Spotify 正在播放等。

<sub>🔧 在程式碼中找到使用處: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **261**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐218 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **218**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐208 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Mods for Claude Code. effortless picks the reasoning effort for every prompt and shows the cache countdown. textless shows art, quotes and chess instead of the wall of text while Claude works.

<sub>🔧 在程式碼中找到使用處: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | HTML                                         |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **208**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-tools` · `anthropic` · `chess` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐197 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Summary

在休息期間保持 Claude Code 的提示詞快取溫熱，並在冷啟動傳送前顯示預估成本。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **197**    |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>動畫錄影 · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">開啟影片</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐153 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code 的外觀：帶有圖示、差異、表格和 Mermaid 圖表卡片的工具列、使用量區帶，以及十五種主題。/skin 可即時切換。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **153**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐116 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

色彩繽紛、可佈景主題化的 Claude Code 回覆：表格、程式碼、圖表、圖形和工具列，提供 15 種主題及複製按鈕。一個 Claude Code 模組。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **116**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐108 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 在程式碼中找到使用處: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **108**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐95 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

一個 Claude Code 模組，將即時代理程式儀表板放入終端機：內容脈絡與費用、顧問時間軸、每次權限檢查、子代理程式卡片與泳道。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **95**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

claude code mods 的集合

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **80**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code mods：在提示上方顯示即時計畫進度列

<sub>🔧 在程式碼中找到使用處: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **54**     |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>動畫錄影 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">開啟影片</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐36 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

你的 Claude Code 工作階段提示列：懸停即可閱讀，點擊即可跳轉（函式 hooks / Mods）

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **36**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

A glow-up for Claude Code: a live cockpit pane, shareable themes, and a pixel pet that acts out what Claude is doing

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code mods：Claude Tools menu、Zen mode、terminal themes、effort 與 mode controls

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **24**     |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Summary

Claude Code mods：21 種樣式與一整套可在需要時啟用的功能，適用於終端機與桌面應用程式。· 一鍵為 Claude 換上新風格，並提供一整套按需開啟的功能。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **22**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐20 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code 模組：Clawd 在提示詞上方演示 Claude 正在做的事

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

##### 📝 Summary

十個 Claude Code mods、新手指南、建立提示、安全示範，以及一個自建模板。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 Summary

兩個 Claude Code mods：Codex computer-use bridge 與協同 Claude 工作階段。原始碼、建置提示、設定與測試。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **16**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐15 · TypeScript · 👁️ observed · 13 天</summary>

##### 📝 Summary

Claude Code 的十個開源 mods：即時面板、資訊列、狀態列與工具呼叫防護。Burn meter、launch codes、session wrapped、boss fight、code pet 等。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **15**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/rashedInt32/glass">rashedInt32/glass</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

A desktop-app look for Claude Code's terminal transcript, as a mod

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **15**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `markdown` · `syntax-highlighting` · `terminal-ui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/rashedint32--glass/87a4efdbb6ca206e.png" width="100%" alt="rashedInt32/glass screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Claude Code 裡的 LINE：作為 Claude Code mod 的 enil TUI

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **15**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 13 天</summary>

##### 📝 Summary

Claude Code mods：usage-band 在提示上方顯示你的 5h／7d 限額、上下文視窗與快取命中率

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **14**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

Claude Code mods，讓 Claude 的問題更容易閱讀與回答（qa-guide）。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **12**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>動畫錄影 · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">開啟影片</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code 模組：在提示詞上方的單一列中顯示 token 中的上下文、5 小時與每週限額相對於時鐘的狀態、提示詞快取倒數、工作階段費用與執行中的代理程式。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **12**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

KOZMOS — 適用於 Claude Code（CLI + desktop）的即時視覺 mods：提示上方的頻帶、側邊欄、狀態 ticker、companions、guards 與音效。

<sub>🔧 在程式碼中找到使用處: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **12**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐11 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

位於你的 Claude Code prompt 上方的動畫 pixel art，會在 Claude 工作時做出反應。七個場景，或你自己的 image 或 GIF。零 tokens。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

讓 Claude Pro 方案維持更久：Claude Code mods 提供精確的 usage HUD、更短的 shell 輸出，且不重複讀取檔案。這些 mods 完全不消耗 tokens。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **10**     |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mods that keep context use, plan quota and per-turn cost on screen, plus a guard that stops a session once it goes over budget.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

圍繞你的 Claude Code 與 Codex terminals 建立的 UI，由你的 agents 建構，因此你腦中唯一的模型就是你的模型。

<sub>🔧 在程式碼中找到使用處: `CLAUDE.md`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-16 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/michalstrnadel/AgentBar">michalstrnadel/AgentBar</a></b> · ⭐9 · Swift · 👁️ observed · 0 天</summary>

##### 📝 Summary

Approve Claude Code permission prompts right from your menu bar — no terminal switching — plus live status for every AI coding agent (Claude, Codex, Copilot, Antigravity).

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | Swift                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-agents` · `anthropic` · `appkit` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `codex`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/michalstrnadel--agentbar/65a4bda4005552e7.gif" width="100%" alt="michalstrnadel/AgentBar screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

適用於 Claude Code 的面板、護欄與生活品質 mods：context、usage、即時活動、通知、安全規則、prompt coach、command hub。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-06 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 432</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - 可與 Claude Code 搭配使用的 100 多個 mods 集合.
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Darrell Wang 製作的 Claude Code mods — 提示上方的資訊列，不消耗模型 Token。台股／美股看板 + 更多功能即將推出.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad 的 Claude Code 模組：窗格、區帶、提示防護、機密處理與記憶工具。單一市場，每個模組可獨立安裝.
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Claude Code 的專家 skills、agents、commands、rules、hooks 與 output styles — 工作階段延續性 +…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其建置工具：先是 builder skill，接著是 mods。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四個 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 與 Collision Guard。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天執行的 Claude Code harness，自第一天起就以此名稱發布，現在與 ucsandman/Agnostic-AI 使用相同的儲存庫：防護…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 為 Claude Code 換屋頂：不修改二進位檔，將系統提示與英文提醒換成你自己的文字（2.1.287+）。
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - 在 Claude Code 中使用 Xcode 的建置、測試、主控台與 SwiftUI 預覽。
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 附有來源引註的 Obsidian 知識庫，介紹 Claude Code mods：它們如何運作、如何建立，以及安裝前如何檢查.
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods，在 Claude 讀取提示前修正並翻譯你的提示。
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 來自 Nekyia Labs 的 Claude Code mods 與 skills，由住在持久家園中的 AI 每日建立並使用。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的側邊窗格：工作階段執行的子代理程式、各自正在做的事、其權杖，以及只需點擊即可查看的對話.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 適用於 Claude Code 的 Claude Mods（function-hooks plugins）.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - 適用於 Claude Code 的浮動狀態卡——模型、上下文、速率限制、費用、分支——另附可由任何腳本或 mod 提供資料的進度 API.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教導 Claude Code agents 建立 Claude Mods（function-hook plugins）的 Skill，附有入門範例。
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code。
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 供使用對話式代理的人類使用的決策佇列 CLI/TUI。代理張貼問題，人類從單一收件匣回答.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社群 Claude mods、插件與技能，可從單一市場安裝。
- [az9713/claude-mod-pack](https://github.com/az9713/claude-mod-pack) - 一個 plugin 中包含六個 Claude Code mods。
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss 的 Claude Code 模組。
- [devbrother2024/devbrothers-mods](https://github.com/devbrother2024/devbrothers-mods) - 개발동생 的 Claude Code mods 集合。計程車套件：計價器、導航、超速取締攝影機、行車記錄器。
- [timoncool/givememod](https://github.com/timoncool/givememod) - 按需建立 Claude Code 模組——讀取你的對話並建立適合你的模組：計畫進度列、檔案窗格、內容量表、危險指令防護、測試監視器.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods gallery：已檢查並置頂的 Claude Code mods.
- [Danovich/turntype](https://github.com/Danovich/turntype) - 在 Claude 工作時進行的打字測試。Claude Code 模組.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code 模組的應用程式商店，就在 Claude Code 中：使用 /mods 瀏覽、搜尋與安裝 2,700 個模組，或要求 Claude…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 六個 Claude Code mods：在提示上方顯示計畫限制與上下文、用於權限提示的允許清單教練、subagent…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod（外掛），新增含有 Activity、Files、Agents、Context 和 MCP…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code mod，可在兩個並排欄中繪製 Edit 和 Write 差異。
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods：像素螃蟹用量面板 usage-hud + 終端機中可點擊的 HTML 連結與一鍵複製程式碼卡片 html-shelf。
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code 的模組：為終端機 UI 新增即時窗格與行為的函式鉤子外掛程式。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard 在你分享螢幕時遮蔽名稱與 secrets；cache-panel 在 prompt cache…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code 的 Mods 與外觀：為 Claude 的任務提供即時進度列、易讀的深色主題與相配的 Windows Terminal…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions。解鎖 Claude 的完整威力.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 適用於同時執行多個工作階段的兩個 Claude Code mods：prompt 上方的 context card 與聊天旁邊的 sessions pane.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示框上方的兩個 Claude Code mods：context-window meter、5 小時限制、prompt clocks 與工作階段成本。
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 我自己的 Claude Code mod 外掛市場。
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 讀取 Claude Code 命名的 markdown 檔案，並在工作階段旁呈現；指向任何區塊即可讓 Claude 編輯它。一個 Claude Code 模組.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code 的 GlanceFlow：提示詞上方的簡潔檢查清單，顯示計畫、進度，以及何時需要 Claude.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：context bar、agents panel、PDPA blur。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在任何 terminal 中，將貼上的圖片縮圖顯示於 prompt 上方。
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的語音協作者。與由 ElevenLabs conversational AI 驅動的 3D 狼人討論事情；當你同意後，它會將提示傳送給…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed，即時打字速度計，附每次 prompt 的統計資料。
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 的 Mods：使用外掛 function-hooks API 建立的窗格、指令與 hooks。
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 透過動畫示範、分類清單與直接來源連結，探索 Claude Code mods、plugins 與 extensions。由 FindMods.dev 提供支援.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：在 transcript 中內嵌繪製 mermaid 圖表。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code mods（function-hook 外掛程式）：session-switcher 等。
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout（找出你最常使用的 mods）、usage-meter、check-ledger、resume-nudge。
- [LudovicLaloux/agent-crew](https://github.com/LudovicLaloux/agent-crew) - Claude Code mod: see your parallel agents as costumed pixel-art Clawds, in a…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren 的 Claude 工具組：適用於 Claude Code 的 skills、mods 與 MCP servers。可透過外掛市場使用單一指令安裝.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 一批由我建立的 claude code mods。
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：探索、檢查、切換與更新 Claude Code mods。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最佳 Claude Code Mods：精選、驗證並置頂。一次 /plugin marketplace add，43 個 mods.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 為真正的 Engineers 打造的 Claude Code 模組。
- [Coolkidlab-Yin/agent-mobile-control](https://github.com/Coolkidlab-Yin/agent-mobile-control) - Drive your local Claude Code and Codex sessions from your phone, as chat rooms.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 插件：自動 Claude model routing.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code 的六個 mods：動態 Clawd 吉祥物、用量限制與提示快取列、傳送前訊息檢查器、快速回覆、待辦佇列和成本帳本.
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - 寫 code 時養一顆慢慢入味的茶葉蛋 · 在你寫 code 時養一顆慢慢醃入味的茶葉蛋。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 的開源 mods：窗格、狀態列、通知、工具防護和斜線指令.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code 模組：直接在文字上逐點回答 Claude。選取對話中的任意部分，加入評論，並將所有評論作為一個提示詞傳送.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス。
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - 適用於 Claude Code 的 Mods：Clawd，一個會演示 Claude 正在做什麼的小型像素吉祥物。
- [reporails/arcade](https://github.com/reporails/arcade) - 經典桌面遊戲化身為 Claude Code mods，在 Claude 工作時於面板中遊玩。由 Reporails 製作.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude 的 code-mods。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 一個 Claude Code mod，可用具名 profiles 針對每個 repo 開啟或關閉你的全域 skills、agents、rules 和…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 經過測試、可用單一指令安裝的 Claude Code 模組：YOLO 模式的防護機制、即時成本與內容、面板、寵物等。另附精選的最佳社群模組清單.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code。
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精選的 Claude Code 模組清單，可作為外掛程式市集安裝：主題、面板、狀態列、肖像.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 兩個 Claude Code mods：cache-keeper 和 ctx-mod。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 讓 agent 保持誠實的 Claude Code mods——守護範圍、驗證部署，並在 prompt 上方繪製工作階段的 function hooks.
- [yocloud-code/claude-vault](https://github.com/yocloud-code/claude-vault) - Claude Code mod: use database, server and cluster credentials without Claude…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin。
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory。
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification。
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 用於在工作中途擷取想法、跨專案與機器整理想法，並將其轉換成提示的 Claude Code 模組。
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（市集 herman-mods）。
- [jrlprost/claude-code-mods](https://github.com/jrlprost/claude-code-mods) - Claude Code mods I build because I need them: context bar, plugin toggler, and…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code 模組：挑選每個子代理程式的模型與推理投入程度。
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code plugin (mod)，讓 Claude Code 終端機 UI 看起來像 Claude 桌面應用程式：提示泡泡、Markdown…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在背景執行的內容：subagents、Codex jobs、shells、monitors、cron jobs 與…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - 關於 Windows 上 Claude Code mods 的第一天現場筆記：context/配額燃料條、Thai UI mod、Matrix…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup。
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better。
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：在提示詞上方顯示即時成本、context 與方案配額儀表。圖示需要 Nerd Font.
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs。
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈。
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band。
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin 與 mod：一個 AI-native SDLC。
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 當 Claude 搞砸時揍它 — Claude Code 的紓壓 mod：卡通屁股、8 個拍打器、9 個屁股、標記、連擊、音效.
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar and a status line for Claude Code: usage limits, context, model…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - 使用 Claude Code 工作時學習外語。
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code 的即時成本、Token 與上下文用量側欄：一個在工作階段內顯示每回合成本、快取命中率、消耗速率與 30 天支出的模組.
- [CircularBlox/Clarity](https://github.com/CircularBlox/Clarity) - A clearer Claude Code terminal: boxed and organized you/claude conversations…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Claude Code Mod：持續列出對話中的未完成項目，並在提示詞上方的橫帶中顯示.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每個 Claude Code agent 在其 context 中有哪些檔案，以及各自的比例.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 適用於 Terminal 與桌面應用程式的小型 Claude Code mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI skill + mod，可在代理回覆中加入西班牙文單字。
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - 你的 Floatee 待辦清單位於 Claude Code 的 prompt 上方：一鍵執行、引導並勾選你的 todos.
- [fredrikbonde/claude-context-bar](https://github.com/fredrikbonde/claude-context-bar) - Claude Code mod: context window as a stacked bar above the prompt。
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [gabriel9004/claude-code-mods](https://github.com/gabriel9004/claude-code-mods) - Mods para Claude Code: panel de agentes y tareas con cuota y caché, y banda de…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 將內容視窗作為提示上方的一列，採用 Claude Code 繪製自身量表的方式呈現.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - 等待 Claude Code 回覆時，不要讓你的注意力飄走.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - 適用於 Claude Code 的免費開源外掛。在你執行 /clear 前，Claude 會寫下一份可供閱讀與編輯的簡短交接內容，下一個工作階段會從中繼續.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [markfulton/safe-keys](https://github.com/markfulton/safe-keys) - Paste an API key into Claude Code. Nothing keeps it.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session。
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文件查證器、程式碼稽核器、錯誤記憶記錄、mod 等.
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [reeny404/mod-hud](https://github.com/reeny404/mod-hud) - Claude Code mod: see which session is waiting on you at a glance, and hatch a…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一個 Claude Code mod，可依要求用本機開源 Kokoro TTS 聲音朗讀 Claude 的回覆與你的提示.
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop。
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用於即時窗格、成本感知模型路由和安全防護的小型外掛程式。用一個命令從 marketplace 安裝.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 與 plugin：用量監視器、token 追蹤器與狀態列.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude Code mods：EMCC (Every Mod Claude Code)，一套為 Claude Code 精選且經測試的 mods 集合。
- [XyndoX/repograph](https://github.com/XyndoX/repograph) - Obsidian-style repo graph pane for Claude Code: files, dependencies and changes…
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [Abdoul-sudo/prompt-enhancer](https://github.com/Abdoul-sudo/prompt-enhancer) - Claude Code mod: rewrites vague prompts using the active project。
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace)。
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [AJMarquez99/prompt-pin](https://github.com/AJMarquez99/prompt-pin) - Pin your latest prompt above the input and browse this session。
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alanrsoares/claude-mods](https://github.com/alanrsoares/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示上方的動畫盲文貓。
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示上方的一隻像素貓，會執行 OmniDimension 語音代理程式測試通話。Claude Code 模組.
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一個 Claude Code 模組，會選擇適當時機進行壓縮，以保持上下文視窗較小.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code 的 Claude 模組：token-meter（工作階段權杖、Claude 與本機 LLMs 的比較，搭配 Pac-Man 內容迷宮）。
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code 的通用 mods：bands、窗格、toasts 與 hooks。包含 usage-bar：在提示上方顯示內容、成本與計畫限制.
- [androidZzT/cc-moyu-kit](https://github.com/androidZzT/cc-moyu-kit) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [AnnihilationWizard/secret-guard](https://github.com/AnnihilationWizard/secret-guard) - A Claude Code mod that adds a gitleaks pre-commit hook to each Git project you…
- [apiglue/claude-mods](https://github.com/apiglue/claude-mods) - Mods for Claude Code。
- [arjunkambj/claude-mods](https://github.com/arjunkambj/claude-mods) - Arjun。
- [Arkboi-GG/claude-mods](https://github.com/Arkboi-GG/claude-mods) - A small collection of Claude Code mods。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 將您的 Claude 使用量限制製作成動畫村民生命值卡片，並附上每週進度警告 — 一個 Claude Code 模組。
- [astromelon/takgon-mods](https://github.com/astromelon/takgon-mods) - 개인 Claude Code mods 플러그인(takgon-mods)。
- [astrosteveo/nebula](https://github.com/astrosteveo/nebula) - Claude Code mods and plugins。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作時進行短訓練：每日目標、連勝、徽章與可選排行榜。一個 Claude Code mod.
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [AydinHassan/claude-mods](https://github.com/AydinHassan/claude-mods) - Claude Code mods。
- [bardaxx/modsbook](https://github.com/bardaxx/modsbook) - A book of Claude Code mods: side panes, bands, status lines and hooks, each one…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方顯示 Apple Music 與 Spotify，包含封面圖、控制項與 Up next…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [blackironj/claude-mods](https://github.com/blackironj/claude-mods)
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 模組：快取時鐘、影響範圍、建議、工作清單、烤架。
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是給你的 Claude Code 的一隻貓頭鷹。
- [chinayuren2022-2025/claude-english-coach](https://github.com/chinayuren2022-2025/claude-english-coach) - Claude Code mod: practise English by working with Claude in English only…
- [coil398/claude-session-brief](https://github.com/coil398/claude-session-brief) - Claude Code mod: session summary band, subagent and hook activity above the…
- [comdoly-life/claude-session-dashboard](https://github.com/comdoly-life/claude-session-dashboard) - Claude Code mod: live dashboard of subagents, agent teams and workflows with…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [davidyerm/claude-mods](https://github.com/davidyerm/claude-mods) - Mods for Claude Code。
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [diegocamara89/claude-mods](https://github.com/diegocamara89/claude-mods) - Mods do Claude Code (function hooks): Sonnet por padrão para subagentes…
- [DimeDataCloud/open-ClaudeOS](https://github.com/DimeDataCloud/open-ClaudeOS) - Claude mods interactive operating system。
- [Djdhmf/clawd-office](https://github.com/Djdhmf/clawd-office) - A Claude Code mod: a living 8-bit office of Claude crabs in a side panel that…
- [Djdhmf/prompt-enhancer](https://github.com/Djdhmf/prompt-enhancer) - A Claude Code mod: a pixel-art librarian crab above your prompt that rewrites…
- [drprockz/claude-mods](https://github.com/drprockz/claude-mods) - Private Claude Code mods (marketplace: drprockz-mods)。
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [Elmanuel1/claude-mods](https://github.com/Elmanuel1/claude-mods) - Claude Code mods: docs-watch。
- [EslamHanafy/delegate-watch](https://github.com/EslamHanafy/delegate-watch) - Live Claude Code pane that shows what your delegated coding agents。
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods (function-hook plugins): session-meter and more。
- [FunJim/claude-code-add-to-chat](https://github.com/FunJim/claude-code-add-to-chat) - Codex-style Add to chat for Claude Code: annotate any part of a reply, send all…
- [gnehiur/claude-code-volc-tts](https://github.com/gnehiur/claude-code-volc-tts) - Claude Code mod：用火山引擎豆包语音流式朗读 Claude 的最终回复（暂停/继续/倍速/缓存）。
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [grvermeulen/claude-mods](https://github.com/grvermeulen/claude-mods) - Claude Code mods: tweaked copies of community mods。
- [gwarf/claude-plugins](https://github.com/gwarf/claude-plugins) - Claude Code mods by gwarf: a plugin marketplace。
- [gyoomun/claude-mods](https://github.com/gyoomun/claude-mods) - 다른 사람이 만든 Claude Code 모드를 내 작업 방식에 맞게 고친 것 (coach-on-call, next-steps-multi)。
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [heidiks/agent-kit](https://github.com/heidiks/agent-kit) - Skills, plugins and Claude Code mods. Install only what you need.
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HikiJun97/claude-mods](https://github.com/HikiJun97/claude-mods) - Personal Claude Code mods。
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模組：每個回答花費的時間、Claude 思考的時間，以及 tok/s，顯示在 Claude 桌面應用程式的回覆正下方.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods。
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian。
- [Ilja-Garbuz/claude-code-mods](https://github.com/Ilja-Garbuz/claude-code-mods) - Claude Code terminal mods: session side panel, opencode-style prompt panels…
- [IntelliNorge/auto-model](https://github.com/IntelliNorge/auto-model) - Claude Code mod: picks the cheapest model that fits each prompt。
- [intent-driven-dev/claude-mods](https://github.com/intent-driven-dev/claude-mods) - Claude Code mods: live panes and hooks for everyday workflows。
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [jambolo/claude-mods](https://github.com/jambolo/claude-mods) - Mods for Claude Code。
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼。/ctx 開或關（Claude Code 模組）。
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（Claude Code 模組）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（Claude Code 模組）。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（Claude Code 模組）。
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（Claude Code 模組）。
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（Claude Code 模組）。
- [jiroamato/claude-mods](https://github.com/jiroamato/claude-mods) - Jiro。
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jonirafael/claude-code-mods](https://github.com/jonirafael/claude-code-mods) - Claude Code mods: context-receipt (per-turn context breakdown) and…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [jumpei-kurata/claude-mods](https://github.com/jumpei-kurata/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的帶狀列中：演出 session、顯示正在執行的項目、context 和使用限制，並與你的 CI…
- [kaisudo0520/cc-dashboard](https://github.com/kaisudo0520/cc-dashboard) - Live mission-control pane for Claude Code: Fable and Codex usage, branch review…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - 使用 VOICEVOX／Irodori-TTS 等朗讀 Claude Code 的回覆與通知 mod。
- [kargarisaac/subagents-tree](https://github.com/kargarisaac/subagents-tree) - Claude Code mod: a docked pane showing every subagent as a tree with model…
- [katipally/modz](https://github.com/katipally/modz) - Claude Code mods: install with /plugin install &lt;mod&gt; --marketplace…
- [keithwalsh/claude-code-mods](https://github.com/keithwalsh/claude-code-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [koenvdheide/cys](https://github.com/koenvdheide/cys) - A Claude Code mod that tracks the temporary files Claude creates and asks it to…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [Krishna30396/Pixel-Progress](https://github.com/Krishna30396/Pixel-Progress) - A pixel progress bar with time left for Claude Code: tasks done, percent and…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high。
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Claude Code mod: guards the 1-hour prompt cache of idle sessions — countdown…
- [m-aoki1348125/next-compass](https://github.com/m-aoki1348125/next-compass) - Claude Code mod: four predicted next instructions in four directions, and a…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一個 Claude Code 模組，會在 iTerm2 分頁副標題中顯示 Claude 正在進行的工作，因此只要看一眼分頁列，就能知道哪個工作階段需要你的注意。
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude。
- [Marceux-Croix/Claudeopticon](https://github.com/Marceux-Croix/Claudeopticon) - A process monitoring and ticket system for Claude Code: your todo as a live…
- [marwansaab/Claude-Mods](https://github.com/marwansaab/Claude-Mods)
- [mashiro-no-rabo/blaze-mod](https://github.com/mashiro-no-rabo/blaze-mod) - Claude Code mod for tracking plans+tickets (jj only, atm)。
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community mods for Claude Code: guards, panes, and commands that run inside…
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace。
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模組：透過在工作階段開始時設定 CLAUDE_CODE_ENABLE_TODO_TOOLS，為省略待辦工具的模型重新啟用它們.
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod，等待安全的暫停時機，接著交接你的工作階段或將其壓縮.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模組：提示上方每個任務清單一行，顯示目前任務、進度列與計數。在終端機與桌面應用程式中外觀相同.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 內與 AI 玩 Connect Four（/connect-four）。
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模組：當另一個程式設計代理提交至你的儲存庫時，Claude 會透過差異與測試進行審查，而不是相信它的報告.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 適用於多個 AI 代理共用儲存庫的 Claude Code 模組：防止秘密值離開 .env、防止推送至公開遠端儲存庫，以及防止 git…
- [narley/sessions-sidebar](https://github.com/narley/sessions-sidebar) - Claude Code mod: a sidebar listing every Claude Code session, for Warp。
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - One mod for Claude Code, Windows and CJK first: pasted-image and text previews…
- [osinelnikov/activity-dashboard](https://github.com/osinelnikov/activity-dashboard) - Claude Code mod: live activity pane with time, tokens, agents, cost and PDF…
- [pappusinghadip/pappu-claude-mods](https://github.com/pappusinghadip/pappu-claude-mods)
- [parab-aditya/cache-keeper](https://github.com/parab-aditya/cache-keeper) - Keeps Claude Code&#x27;s prompt cache warm while you&#x27;re away, with a band above the…
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack：一個 Claude Code 模組。在同一個窗格與狀態列中，提供具唯讀起始狀態的永久 worktree、團隊控制項與內容庫.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 桌面應用程式 Code 分頁的即時工作階段統計側邊窗格：上下文、成本、git 變更、回合統計、子代理程式、記錄.
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
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：在 Claude 工作時做伏地挺身。無 tokens.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain：Claude Code 模組的實務指南，從 ELI5 到政策工程，附實地測試與引導式教學。
- [roboza/kanbot](https://github.com/roboza/kanbot) - A global kanban board in Claude Code that hands queued cards to background…
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 模組：將你在計畫模式中核准的計畫轉為提示上方的即時核取清單，隨著 Claude 完成每個步驟逐一勾選。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精選的 Claude Code 模組清單。每個項目都已複製，並使用 claude plugin validate 檢查，且標記其可接觸的內容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：輔助代理程式在 Haiku 上執行，大型檔案與日誌則由免費的 Gemini 模型摘要，而不是填滿 Claude 的內容.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 隨工作階段播放的 lo-fi 原聲帶：平靜、專注、流暢，另有通過與失敗測試的提示音。原創音樂.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 撰寫程式時學習：每當一輪操作變更程式碼後，提示上方會出現一個關於該確切變更的問題。依概念評分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 記錄 Claude 所做每次編輯的磁帶：重播每項變更自行輸入的過程、逐步檢視，並將任何檔案倒轉至任何步驟.
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them。
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - A Claude Code mod: a project dashboard and isometric city map of tasks, agents…
- [schudarin/chudarin-context-mod](https://github.com/schudarin/chudarin-context-mod) - A Claude Code mod: a side panel that shows what fills your context, how much of…
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker。
- [sr-gene/gene-claude-mods](https://github.com/sr-gene/gene-claude-mods)
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Custom Claude Code mods marketplace (cc-mods), with vendored Anthropic sample…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 為 Claude Code 一鍵產生 commit 訊息，搭配跳舞的像素風 Malenia。
- [taketonomy/privacy-guard](https://github.com/taketonomy/privacy-guard) - Claude Code Mod: blocks git commit/push that adds personal names or Slack tokens。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — 一個 Claude Code 模組，會在提示正上方顯示您的 Claude 計畫用量（工作階段與每週限額、重設倒數、上下文）.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - tanmen 製作的非官方 Claude Code 模組（市集：tanmen）。
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一個 Claude Code 模組，在窗格中顯示目前工作階段：每個提示詞、Claude 分階段為其完成的工作、每個子代理程式及其答案，以及提示詞的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一個 Claude Code mod 外掛市集：function-hooks 外掛，可在 Claude Code 內繪製 band、窗格和其他 UI.
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace。
- [timoranjes/agent-arcade](https://github.com/timoranjes/agent-arcade) - Playful live view of Claude and its subagents: animated dashboard, stats band…
- [tinkybeatz/tinky-claude-mods](https://github.com/tinkybeatz/tinky-claude-mods) - Claude Code mods: interface and behaviour plugins built on function hooks。
- [tyler4400/tyler-claude-mods](https://github.com/tyler4400/tyler-claude-mods) - Claude Code plugins: status-card (会话状态卡片) &amp; session-title (智能自动标题) — Live…
- [UlongChaS2/learn-trail-mods](https://github.com/UlongChaS2/learn-trail-mods) - Claude Code mod: 설명의 목차를 패널에 띄우고 항목별 설명을 저장해 /recall 로 다시 본다。
- [user0027/claude-mods](https://github.com/user0027/claude-mods)
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模組：適用於長時間執行任務的動畫進度列與完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 三個小型 Claude Code 模組：查看子代理程式何時完成、在 Claude 完成後佇列訊息，以及讓你最愛的技能保持一鍵可用.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 說出「我迷路了」，Claude 就會再次用日常用語解釋上一則回覆。Claude Code plugin.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作旁的窗格中向 Claude 提出旁支問題。主要對話永遠看不到它。運作方式類似桌面應用程式的 /btw.
- [Vatroslav/cc-mod-ferro](https://github.com/Vatroslav/cc-mod-ferro) - Claude Code mod: a pixel-art Norwich Terrier runs across a meadow above the…
- [vdvoorder/filemap](https://github.com/vdvoorder/filemap) - A Claude Code mod that draws a git repository as a treemap in a side pane and…
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vmlinuz82/claude-mods](https://github.com/vmlinuz82/claude-mods) - Claude Code mods: a task checklist and a skill/MCP usage band, for the terminal…
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac。
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wonjangcloud9/wj-mods](https://github.com/wonjangcloud9/wj-mods) - Claude Code mods: cross-session work progress pane, usage band, long-turn…
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Claude Code mod 모음 (wonr-mods 마켓플레이스)。
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 外掛：在提示詞正上方顯示你的 Claude Pro/Max 使用量限制、使用速率預測、計費週期、以 token 和 $/€…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 用於 Claude Code 的 Mods。agent-crew：以即時 pixel crew 觀看你的 subagents 工作，包含…
- [XyndoX/agentdeck](https://github.com/XyndoX/agentdeck) - A live AI-agent dashboard in a Claude Code pane: agent flow, tool activity…
- [ya8282/claude-code-mods](https://github.com/ya8282/claude-code-mods) - Small productivity mods for Claude Code。
- [Yumbang/scopus-for-dobby](https://github.com/Yumbang/scopus-for-dobby) - Stateful CLI for searching, collecting, and managing academic papers from the…
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 由 Anthropic PBC（无关联关系）这支势不可挡的团队精心打造的顶级资源精选，献给最强大的智能体与无可争议的编码伴侣冠军 Claude Code.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 一款顯示正在發生什麼事的 Claude Code 外掛——內容使用量、作用中的工具、執行中的代理人，以及待辦事項進度。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 高度可自訂的精美 Claude Code CLI 狀態列，支援 powerline、主題等功能.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 系統提示的所有部分、27…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Claude Code 與 Codex 的 AI 影片技能 — 使用 Remotion 製作電影感產品影片：152 張鏡頭配方卡、209…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45 多項充分發揮 Claude Code 效用的秘訣，從基礎到進階——包括自訂狀態列指令碼，以及在容器中自行執行的 Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — 產生小紅書輪播圖與微信 21:9+1:1 封面組合.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 在終端機窗格中檢視 coding agent 的 diff，並將逐行留言傳回 Claude Code、Codex、OpenCode 或 Pi.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 適用於 Claude Code 的完整狀態列外掛程式，提供內容使用量、API 速率限制與成本追蹤。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - 為 Claude Code 建立 mods：攔截任何請求、修改任何回應、/model…
- [aqua5230/usage](https://github.com/aqua5230/usage) - macOS menu bar &amp; Windows tray app pinning Claude Code, Codex, Antigravity &amp;…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code 的完整狀態列儀表板 — 工作階段資訊、配額條、Agent 追蹤器、MCP 健康狀態、訊息歷史記錄等.
- [tmck-code/yet-another-statusline](https://github.com/tmck-code/yet-another-statusline) - A statusline for Claude Code inspired by terminal monitor programs。
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：追蹤你的 Claude Code 工作階段的碳足跡。
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公開的 Claude Code skills 與 mods。
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun。
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code 的 Skills、mods、子代理、hooks、斜線命令與指南 — 可由你的代理安裝（請參閱 INSTALL.md）。
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免費的 LLM APIs 與程式設計 Agent — 每週自動更新並探測驗證兩次。免費方案、免卡試用、免費模型.
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 將你的程式設計代理變成鍵盤韌體專家的 Agent Skill。稽核 ZMK/QMK keymaps、調整 home row mods、讓 trackballs…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供禮拜時間、回曆日期、adhkar、每日 ayah、sunnah fasting、Ramadan、Jumu。
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [WaterTian/cc-hud](https://github.com/WaterTian/cc-hud) - Compact Claude Code statusline — zero-dependency, crash-free on Windows。
- [romacv/claude-plan-usage-statusline](https://github.com/romacv/claude-plan-usage-statusline) - Claude Code status line showing model, usage limits, git info, and workspace…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 適用於 Claude Code、pi 與 DeepSeek Harness 的插件合集：狀態列 HUD、任務進度條、Tailscale 節點狀態等 · 適用於…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - 適用於 .NET DDD/Clean Architecture 的可攜式 Claude Code 工具組：嚴格的 TDD…
- [3xDevOps/aether](https://github.com/3xDevOps/aether) - Self-hosted multiplayer cloud runtime for coding agents.
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 可攜式 Claude Code 全域設定：自訂技能、PreToolUse hooks，以及自訂狀態列。可在 Linux、macOS、WSL 上執行.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - 適用於 Claude Desktop Code 分頁的非官方 mods — usage-pet：帶有 Clawd 動畫像素寵物的 usage band.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：整理過的 skills 與 mods，可在任何人的機器上運作.
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - 可自訂的 Claude Code 狀態列，配備拖放編輯器。
- [MindLab-Research/dsh-generative-ui](https://github.com/MindLab-Research/dsh-generative-ui) - Generative UI for DeepSeek Harness — the agent writes TSX and the web UI…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [wide3751/switchboard](https://github.com/wide3751/switchboard) - A Claude Code plugin (mod) that shows every local Claude Code session in one…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code Plugins 與 Skills 的 marketplace，用於促進 Hytale 的遊戲 mods。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Windows Terminal 與 tmux 中 Claude Code 的分割窗格檢視器：將 session 以渲染後的 Markdown 呈現，包含…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media mods 的 Repository.
- [dayfinggg/anthropic-claude-code-agent-skills](https://github.com/dayfinggg/anthropic-claude-code-agent-skills) - 18 engineering skills, 14 specialist agents, the Brief output style, two mods…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [michalschroeder/claude-statusline](https://github.com/michalschroeder/claude-statusline) - My Claude Code statusline + supporting hooks。
- [OFurtun/claude-custom-statusline](https://github.com/OFurtun/claude-custom-statusline) - Furtun。
- [RaggioS/claude-code-statusline](https://github.com/RaggioS/claude-code-statusline) - Single-file POSIX statusline for Claude Code: dir, git branch, model, context…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン。
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline。
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [afarrell/claude-meter](https://github.com/afarrell/claude-meter) - Minimal Claude Code statusline — context bar, 5h bar, and 7-day rolling…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 專業級 Claude Code 狀態列：工作階段時長、搭配 ECB 外匯的多幣別費用、每百萬權杖費率、支出上限。MIT、零金鑰、跨平台.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod。
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Two-row status line for Claude Code: context, rate limits with pace markers…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust。
- [federbenjamin/claude-statusline](https://github.com/federbenjamin/claude-statusline) - A two-line Claude Code status line showing branch, PR, model, context, cost…
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [hey-yvan/claude-quota-bar](https://github.com/hey-yvan/claude-quota-bar) - Fast Rust statusline for Claude Code — battery-bar 5h/7d quota, ctx, cache age…
- [hopetonp/claude-voice-mod](https://github.com/hopetonp/claude-voice-mod) - Two-way natural voice conversations for Claude Code on macOS and Windows。
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [itamartz/ClaudeCode-Mods](https://github.com/itamartz/ClaudeCode-Mods) - A Claude Code plugin marketplace of personal mods: hooks, panes and commands…
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [LemonYangZW/cc-mods](https://github.com/LemonYangZW/cc-mods) - Practical, low-distraction mods for Claude Code。
- [LiamMorganDev/claude-setup](https://github.com/LiamMorganDev/claude-setup) - My complete Claude Code setup: mods, skills, commands, hooks and CLAUDE.md…
- [luck7x/claude-cache-keepalive](https://github.com/luck7x/claude-cache-keepalive) - Keep Claude Code&#x27;s prompt cache warm while you&#x27;re away — cheap…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [Monte9/claude-memory-mods](https://github.com/Monte9/claude-memory-mods) - Curate Claude Code&#x27;s own memory files: a pane to view every project&#x27;s memory…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [n0nuser/claude-statusline](https://github.com/n0nuser/claude-statusline) - 3-line status bar for Claude Code — model, context usage, cost, git status, and…
- [Nader-mech/claude-statusline](https://github.com/Nader-mech/claude-statusline) - Claude Code status line showing 5-hour and weekly subscription usage, with…
- [nhooey/claude-code-usage-statusline](https://github.com/nhooey/claude-code-usage-statusline) - A Claude Code status line and per-turn cost readout in one program: token…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [Recokioshi/claude-kit](https://github.com/Recokioshi/claude-kit) - a set of useful skills and mods for claude code。
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 自訂 Claude Code 狀態列（上游：kamranahmedse/claude-statusline）。
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [saeed1507100/claude-context-meter](https://github.com/saeed1507100/claude-context-meter) - Claude Code plugin: live context-window meter with hoverable breakdown, detail…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company。
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - 適用於 Claude Code Agents 的主動式 AI 記憶與速率限制監控器。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks、subagents 和 statuslines：開源集合與工具，按類型分類，並各自附有安全分級。English / 中文.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - 適用於 Claude Code 的 Mods：基於 function hooks 建立的 panes、bands 與 buddies。
- [ryanclark/statusline](https://github.com/ryanclark/statusline) - Simple status line for Claude Code showing context window/usage limits。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的 Claude Code 工作階段之間傳遞任務。將變更交給擁有某個 repo 的工作階段.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你一次又一次要求 Claude Code 執行的操作，並將其轉換為 mod。另附 8 個範例 mods 與虛擬辦公室.
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 這是在 MCP server 中控制 MODS 的工具；MODS 是適用於 Fablabs 的模組化跨平台工具，包含 CAD/CAM 與機器控制工具.
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Biblioteca de 3 skills para Claude Code: session-handoff, session-statusline e…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用於翻譯 CK3 mods 的 Codex 與 Claude Code skill，搭配本機 LLM。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - 適用於 Claude Code 的開源 mods 與其他 extensions。
- [Grandullon/diariovida-mods](https://github.com/Grandullon/diariovida-mods) - Mods gratis para Claude Code: entiende lo que hace Claude, mejora tus prompts y…
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability。

</details>

<a id="dsh-cordis"></a>

## DSH 與 Cordis 外掛生態系

DeepSeek Harness 與 Cordis 從不同方向抵達同一個位置：對它們來說，外掛就是模組機制，因此那裡的外掛就等同於這裡的模組。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐75403 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

🌊 原始代理人框架。部署智慧型多玩家群集、協調自主工作流程，並建構對話式 AI 系統。具備自適應記憶、自我學習智慧、聯邦、向量 RAG 整合，以及原生支援 Claude Code / Codex / Hermes 和許多其他工具

<sub>🔧 在程式碼中找到使用處: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                   |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **75403**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4658 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

DSH 官方首推的 TUI 插件——高性能、低占用、可爱的像素鲸鱼、流畅的鼠标交互。通过 npm 一键安装。/ DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

<sub>🔧 在程式碼中找到使用處: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                   |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4658**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐731 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

為包含 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My Pi、Grok、OpenCodek DSH、Kimi 等在內的 AI 助理精選最佳優質 AI 外掛程式清單。https://hol.org/plugins

<sub>🔧 在程式碼中找到使用處: `README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                   |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | Python                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **731**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐282066 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

使用代理程式逆向工程任何事物，從應用程式行為到原生二進位檔。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **282066** |
| Last push    | 2026-10-16 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101444 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **101444** |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84279 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

將任何想法、計畫或程式碼庫轉換成精美的互動式圖表。適用於 Claude Code、Codex 及更多工具的代理人技能。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **84279**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/80b6efa0c1ca677d.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35818 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

適用於複雜軟體工程任務的可靠程式設計代理。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Go                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **35818**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐31046 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

為 DeepSeek Harness (DSH) 插件生態打造的現代化桌面端解決方案。萬物皆「插件」，桌面本身也是「插件」。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **31046**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25678 · Python · 🔎 inferred · 3 天</summary>

##### 📝 Summary

Distilly — 將他們的思考方式提煉成適用於任何 Agent 或 Bot 的可重複使用 Skills。前身為 Colleague Skill（原同事 Skill）。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Python                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25678**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9210 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

時空可組合性的元框架

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9210**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8815 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) Web 外掛聚合生態 · 萬物皆外掛，透過創意工坊分發｜｜DeepSeek Harness (DSH) Web 外掛聚合生態 · 一切皆為外掛，透過創意工坊分發

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8815**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4280 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4280**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐2455 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2455**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/T-Auto.png?size=160" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2186 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, agent teams, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板、浏览器、侧栏、命令，透视上下文组成、演进、压缩、多 Agent等。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2186**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1474 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Python                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1474**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1215 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Go                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1215**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐710 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **710**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

📚 一個零相依、由 git 支援的微課程函式庫，讓 AI Agent 非同步分享與搜尋經驗證的除錯經驗。 | https://misakanet.org

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Python                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **526**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐277 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **277**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **256**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐206 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

原生 DeepSeek Harness (DSH) 插件，整合 TypeSafe Jev 或如 luna 的 Decision api，作為 Agent 選擇、監督、修正與核准的 System One 決策層。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **206**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐199 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **199**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐192 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) 備份與還原外掛 — 匯出、匯入、遷移並同步完整的 DSH 設定、外掛、MCP 伺服器、技能與工作區。只需一鍵即可遷移至另一台機器。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **192**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/95eb0411c14b8fcd.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐181 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **181**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/2c813d2312e069f3.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐171 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **171**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>動畫錄影</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐163 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **163**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-15 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐154 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

安裝即內建mattpocock/skills v1.3.1的27個工程與效率技能，無需手動安裝技能。以400億token打造本外掛，在原始技能之上提供10倍的開發效率，也能幫助新手更快上手這套技能。全力支援GitHub issue；Markdown為預覽版；GitLab暫不支援。感謝您的使用和支援💗

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **154**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/yannicksong0106/dsh-550c-boot">yannicksong0106/dsh-550c-boot</a></b> · ⭐152 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

550C 开机动画 for DeepSeek Harness — 首帧由宿主半边注入，DSH 的 Loading 卡片不露脸；桌面原生标题栏按钮收编成终端配色 | 550C boot splash plugin for DSH

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **152**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `boot-splash` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `loading-animation` · `splash-screen` · `web-ui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/yannicksong0106--dsh-550c-boot/8d4b5595a9704213.png" width="100%" alt="yannicksong0106/dsh-550c-boot screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐130 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 桌寵外掛：元氣鯨魚娘看板娘陪你寫程式 🐋 支援 DSH 桌面端 0.2.0-rc.2 與舊版 Web（desktop pet / mascot，local-first）

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **130**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/amlyczz/dsh-agy-link">amlyczz/dsh-agy-link</a></b> · ⭐114 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Google Antigravity (agy CLI) models for DeepSeek Harness — streaming chat, thinking, tool activity, usage, in-GUI Google OAuth login

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **114**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `antigravity` · `dsh` · `dsh-plugin` · `gemini`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amlyczz--dsh-agy-link/bad2c8c0993107d5.png" width="100%" alt="amlyczz/dsh-agy-link screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **112**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐102 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH plugin - framework upgrade safety & plugin gating: contract pre-check, rollback point, auto-rollback on failure, evidence-based auto-disable; plus a multi-source plugin market. Unofficial. | DSH 插件：框架升级安全 + 插件门控——升级前契约预检、回滚点、失败自动回滚、有确证证据才自动禁用；另带多源插件市场。非官方社区项目。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **102**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐93 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **93**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PKUfudawei/dsh-capability-menu">PKUfudawei/dsh-capability-menu</a></b> · ⭐87 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

一个面向 DeepSeek Harness 的统一能力管理插件，为 Tools/Skills 提供常驻、按需、禁用三档暴露策略，以减少上下文占用并支持运行时动态发现与执行。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **87**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `cordis` · `deepseek-harness` · `dsh-plugin` · `mcp` · `skills`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pkufudawei--dsh-capability-menu/beebe8dc6377a667.png" width="100%" alt="PKUfudawei/dsh-capability-menu screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 59</sub></summary>

- [strukto-ai/mirage](https://github.com/strukto-ai/mirage) - The World。
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI 程式設計 Agent 的執行前防護工具。在工具呼叫執行前，阻止破壞性的 Git 和檔案系統命令，以及常見的敏感檔案存取嘗試.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 外掛程式市場 / DSH Plugin Marketplace：在 DeepSeek Harness Web GUI 中一鍵瀏覽、安裝與更新全部…
- [arcships/rutis](https://github.com/arcships/rutis) - 一個供會自我迭代的軟體使用的外掛執行環境 — 代理程式可在 Rust、TypeScript、Python 與 Go…
- [morluto/leantoken](https://github.com/morluto/leantoken) - Code intelligence for agents: find the code that matters and keep your context…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - 基於 Deepseek-Harness 核心底座打造的桌面版 Agent。繼承底座的全部能力，並補全 IDE 相關功能.
- [cloader/dsh-taskboard](https://github.com/cloader/dsh-taskboard) - deepseekharness 任务看板插件。
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 持續更新的 DeepSeek Harness 外掛目錄 — 每小時更新，每日進行相容性測試，內建應用程式內外掛商店與腳手架.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - 面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 外掛精選目錄——14 類 280+ 個社群外掛，涵蓋 MCP / Skill / TUI / 多 Agent /…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [cosyncing/cosyncing](https://github.com/cosyncing/cosyncing) - Synchronize and Orchestrate agents from CLI to GUI, across desktop to phone.
- [skyf0xx/hedgehog](https://github.com/skyf0xx/hedgehog) - HEDGEHOG codes Cleaner, Faster and with Fewer Tokens.
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：基於 DeepSeek Harness（DSH）的多平台群組聊天 Agent 系統｜由 DSH 驅動的多平台群組聊天 Agent 系統。
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 外掛：一鍵匹配模型上下文視窗，顯示容量來源，支援勾選批次設定、既有視窗管理與手動編輯.
- [pigeon189/zcode-fox-widget](https://github.com/pigeon189/zcode-fox-widget) - 同仓两条产品线：main = ZCode狐娘小挂件。
- [Dalizi2026/dsh-factory-provider](https://github.com/Dalizi2026/dsh-factory-provider) - 把 Factory (Droid) 订阅额度接入 DeepSeek Harness (DSH) 的原生 LLM provider 插件 · Factory…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH 工作階段導覽。
- [liustack/pptwise](https://github.com/liustack/pptwise) - A real PowerPoint, not HTML. Tell your AI what to cover and pptwise builds an…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - 社群策展的 DeepSeek Harness (dsh) 插件、工具、技能與學習資源。可搜尋的雙語目錄 | DeepSeek 插件、工具與技能精選。
- [ppy-web/dsh-plugin-xiaomi-mimo-tts](https://github.com/ppy-web/dsh-plugin-xiaomi-mimo-tts) - 给DSH接入免费的 Xiaomi MiMo TTS API，支持使用预置/自定义/浏览器内置声音朗读正文。
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [jiesou/dsh-opencode-zen-free-provider](https://github.com/jiesou/dsh-opencode-zen-free-provider) - OpenCode Zen 免费模型接入 DeepSeek Harness。1M 上下文，同步全部元数据。
- [muyuanjin/dsh-ptc-plus](https://github.com/muyuanjin/dsh-ptc-plus) - A session-bound agent-native REPL for DeepSeek Harness PTC mode.
- [cv-superding/dsh-webin](https://github.com/cv-superding/dsh-webin) - Unofficial DSH plugin: drive AI web UIs (DeepSeek/Qwen/...) in a REAL browser…
- [morlay/dsh-plugin](https://github.com/morlay/dsh-plugin) - dsh plugins。
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [maple110011/dsh-obsidian-math](https://github.com/maple110011/dsh-obsidian-math) - 面向数学笔记的 DeepSeek Harness 助手，驻留在 Obsidian 右侧栏.
- [mytianyi0712/dsh-tui-plugin-OhMyPi](https://github.com/mytianyi0712/dsh-tui-plugin-OhMyPi) - 一个dsh的终端样式插件，灵感来自Oh My Pi。
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 外掛的 X-ray：宣告的能力與實際行為。登錄庫 + 靜態掃描器 + 徽章.
- [hxy91819/dsh-auth](https://github.com/hxy91819/dsh-auth) - Caddy-fronted administrator authentication for DeepSeek Harness: Argon2id…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode — 讓 OpenCode Zen + Go 免費方案模型持續運作的 DSH…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - 看清 AI 編碼代理的每一次可觀察行動。 · 追蹤你的代理，深入到每個工具與 MCP.
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh daemon: register the DeepSeek Harness web server (dsh web) as an…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [FeatherHunter/dsh-plugin-update](https://github.com/FeatherHunter/dsh-plugin-update) - 给 DSH 插件加「检查更新 / 安装更新」能力的 npm 包：宿主一段接线 + 面板一个现成组件，查新版、装更新、失败兜底、更新日志与多插件日志一次包掉。
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - DSH plugin collection: password auth + trust for dsh web LAN/Tailscale access…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) 外掛程式的零相依性驗證標準——靜態結構閘門 (R)、cordis 合約檢查 (K)、沙箱冒煙測試…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Web 外掛：盯盤 market-dashboard 側邊欄分頁——三條附滑入日內圖表的報價列、含產業 alpha…
- [zhangx413/dsh-pbr-material](https://github.com/zhangx413/dsh-pbr-material) - DeepSeek Harness plugin: a photo of a surface becomes a complete tileable PBR…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness 的第三方外掛市集與受防護生命週期管理器.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人為本且可擴充的桌面工作台：對話、筆記、試算表、檔案位於同一工作台；自建伺服器即可啟用多人即時協作.
- [DoveLi-Gu/dsh-showcase](https://github.com/DoveLi-Gu/dsh-showcase) - Local, verifiable delivery evidence reports and DSH plugin for coding-agent…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入。
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - 为 DeepSeek Harness 桌面版提供「限网段 + 可选数字密码」的远程访问入口。
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色：换装、白饭、摸头、问候、登录账户余额和本机今日用量预估.
- [wangxing-git/dsh-autogate](https://github.com/wangxing-git/dsh-autogate) - DeepSeek Harness 自动审批插件：在 workspace-write 沙箱之上叠加确定性规则 + LLM…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成。
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness plugin：將 Windows sandbox ACL 佈建失敗。
- [akkefa/deepseek-cordis](https://github.com/akkefa/deepseek-cordis) - Python plugin runtime targeting DeepSeek Harness vendored Cordis semantics。
- [YYZ-YingSe/cordis-x](https://github.com/YYZ-YingSe/cordis-x) - An embeddable Rust plugin runtime with dependency-aware lifecycles and Rust…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [Yesyugao/dsh-claude-harness](https://github.com/Yesyugao/dsh-claude-harness) - Claude branding for the DeepSeek Harness desktop app in one plugin: the Claude…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…

</details>

<a id="writing"></a>

## 文章、討論與影片

關於模組功能的文章、討論與影片。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐16 · 👁️ observed · 1 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

##### 📝 Summary

嗨，HN，我為自己打造了這個工具，並想將它開源。問題是：我經常長時間待在終端機中，尤其是現在我們通常會並行處理這麼多代理程式，因此我想要一種能在提示之間取得提醒的方法。第一個版本是一個簡單的 rep

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 8 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 14 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

##### 📝 Summary

我建立這個是因為在最新的程式設計模型中，Claude 會使用晦澀的命令進入深度工作模式，讓我再也不知道它在做什麼。這是一個模組（使用 Claude Code 新功能掛鉤的外掛），會在提示詞上方繪製一行：- 目前步驟，

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `文章、討論與影片`                           |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## 按實作語言分類的專案

這個生態系主要集中在 Python 和 TypeScript，但支援型別的用戶端仍持續以其他語言出現。本表格是從各項目本身產生的。

| 語言       | 條目 | 範例                                                                                                          |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 375  | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 77   | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 38   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 14   | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 12   | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 4    | `vulcanshen/ccdrawu`, `3xDevOps/aether`, `esengine/DeepSeek-Reasonix`                                         |
| Swift      | 2    | `michalstrnadel/AgentBar`, `eovidiu/cordis-ios`                                                               |
| AutoHotkey | 1    | `keithwalsh/claude-code-mods`                                                                                 |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `DimeDataCloud/open-ClaudeOS`                                                                                 |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |
| Ruby       | 1    | `romacv/claude-plan-usage-statusline`                                                                         |
| jq         | 1    | `n0nuser/claude-statusline`                                                                                   |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

歡迎提供修正，這是改善此清單最快的方式。如果某個項目被錯誤分類、評等有誤，或某個專案因名稱衝突而被錯誤排除，請建立 issue 或提交 pull request——最後一類是自動篩選最可能出錯的地方。

---

<sub>獨立的社群專案。與 Anthropic 無關聯，也未獲其背書或審查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商標。產品行為可能在未通知的情況下變更；任何關鍵內容都請以官方文件為準。資產仍歸其上游專案所有，僅在授權允許的情況下重製。</sub>

<sub>Last updated · 2026-10-16T19:18:13+08:00</sub>
