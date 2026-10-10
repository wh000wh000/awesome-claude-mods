<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="超讚的 Claude 模組">
</p>

<h1 align="center">超讚的 Claude 模組</h1>

<p align="center"><b>依證據分級的 Claude Code 模組、外掛，以及它們改變的更深層行為索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-617-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <b>繁體中文</b> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **即時索引** · 上次同步: `2026-10-11T05:58:46+08:00` (UTC+8)
> · 條目: **617** · 最新更新新增項目: **0** · 實作語言: **10**

<sub>以下每個條目都經過自動收集、篩選與再次核查。這裡沒有任何付費置入。</sub>

<a id="featured"></a>

## 當下精選

<sub>每個分類選出一個項目，依證據等級和星標排序，並在每次更新時重新計算。這是排名，不代表背書；每個精選項目都會連結至下方的完整卡片。優先選擇發布了截圖或錄影的專案，讓這個橫列保持視覺化。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9466 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2532 · Python · 👁️ observed</sub>
<sub>Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74280 · TypeScript · 👁️ observed</sub>
<sub>🌊 原始代理人框架。部署智慧型多玩家群集、協調自主工作流程，並建構對話式 AI 系統。具備自適應記憶、自我學習智慧、聯邦、向量 RAG 整合，以及原生支援 Claude Code / Codex / Hermes 和許多其他工具</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## 內容

- [什麼是 Claude Code 模組](#什麼是-claude-code-模組)
- [條目分級方式](#條目分級方式)
- [官方：Anthropic 自有的程式碼儲存庫與版本發行說明](#官方anthropic-自有的程式碼儲存庫與版本發行說明) — **16**
- [模組：使用模組功能建立](#模組使用模組功能建立) — **493**
- [DSH 與 Cordis 外掛生態系](#dsh-與-cordis-外掛生態系) — **97**
- [文章、討論與影片](#文章討論與影片) — **11**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150059 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Summary

Claude Code 是一款駐留在終端機中的代理式編碼工具，能理解您的程式碼庫，並透過執行例行工作、解釋複雜程式碼及處理 git 工作流程，協助您更快速地編寫程式碼——全部透過自然語言指令完成。

<sub>🔧 在程式碼中找到使用處: `feed.xml`</sub>

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |
| 語言     | TypeScript                                         |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **150059** |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9466 · TypeScript · ✅ official · 1 天</summary>

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
| Stars        | **9466**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8244 · Python · ✅ official · 1 天</summary>

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
| Stars        | **8244**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6335 · Python · ✅ official · 241 天</summary>

##### 📝 Summary

使用 Claude 分析程式碼變更以尋找安全漏洞的 AI 驅動安全性審查 GitHub Action。

##### 📌 Basic facts

| Field    | Value                                              |
| -------- | -------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明` |
| Evidence | `由 Anthropic 本身發布`                            |
| 語言     | Python                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6335**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 1 天</summary>

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
| Stars        | **1799**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

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
| First listed | 2026-10-05 |

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
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

官方 DeepSeek Harness MCP client 的 MCP 管理主控台：具備健康診斷與 pipeline trial calls 的 /mcp 命令、含 server CRUD（需核准閘控寫入、自動備份）的 Settings MCP 分頁，以及透過官方 tool pipeline 的工具試用主控台（Apache-2.0, dsh-plugin）。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明`  |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

這是官方 DeepSeek Harness 的啟動器。不進行任何修改，只會啟動 DeepSeek 開發的內容。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `官方：Anthropic 自有的程式碼儲存庫與版本發行說明`  |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 為 mods 新增了 `$.ui.notify`：透過你自己的通知設定發出原生通知，並說明是哪個 channel 傳送了它 為 mod 的 `Button`…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 修復在 `UserPromptSubmit` 掛鉤或模組的 `prompt.submit` 掛鉤期間按下 Esc…

</details>

<a id="mods"></a>

## 模組：使用模組功能建立

此處的每個項目都展現了使用 Claude Code 在 2.1.287 中取得的功能的證據：它透過 `ui.render` 繪製內容、擁有窗格、區段或卡片、讀取 `$.ui.selection()`、使用 `agent.spawn` 產生隊友，或明確表示自己是模組。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2532 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | Python                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2532**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>動畫錄影</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐467 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

公開 Claude Code 模組（函式 Hooks）的社群目錄，從 GitHub 掃描，並列出每個模組可以讀取、寫入、執行或透過網路傳送的內容。瀏覽 https://mods.aidojo.si/

<sub>🔧 在程式碼中找到使用處: `data/seeds.txt`, `data/duplicates.txt`, `data/repos.txt`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **467**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐181 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code mods：基於 hooks 建立的外掛，可在提示上方即時加入行、守衛、面板與遊戲。Context bar、使用量計量器、Codex review watch、Markdown 預覽、Spotify 正在播放等。

<sub>🔧 在程式碼中找到使用處: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **181**    |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐115 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stars        | **115**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐106 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

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
| Stars        | **106**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

An agent-native QA CLI for web pages. Deterministic, no tests to write, no LLM.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | HTML                                         |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **104**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code 的外觀：帶有圖示的工具列、diff、表格與 Mermaid 圖表卡片、用量帶及十五種主題。/skin 可即時切換它們。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **88**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

claude code 模組集合

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **77**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Colorful, themeable Claude Code replies: tables, code, diagrams, charts and tool rows in 15 themes, with copy buttons. A Claude Code mod.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Summary

Darrell Wang 製作的 Claude Code mods — 提示詞上方的頻段，不佔用模型 token。台股／美股看板 + 更多內容即將推出。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | HTML                                         |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **65**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐59 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stars        | **59**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐57 · Shell · 👁️ observed · 3 天</summary>

##### 📝 Summary

適用於 Claude Code 的專家技能、代理程式、指令、規則、hooks 與輸出樣式 — 工作階段延續性 + 現代 CLI 工具，適用於真實世界的開發工作流程

<sub>🔧 在程式碼中找到使用處: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | Shell                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **57**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐45 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Claude Code 模組：提示上方的即時計畫進度列

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **45**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>動畫錄影 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">開啟影片</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

觀看 Claude Code 在你工作時生成一個小卡通。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **32**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

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
| Stars        | **27**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **23**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

在 Claude Code 中使用 Xcode 的建置、測試、主控台與 SwiftUI 預覽

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
| Last push    | 2026-10-02 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

Claude Code 模组：21 种风格，以及一整套可在需要时开启的功能，适用于终端机与桌面应用程式。· 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

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
| Last push    | 2026-10-04 |
| First listed | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

十個 Claude Code mods、初學者指南、creation prompts、安全 demos，以及 build-your-own template。

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
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Claude Code mods：usage-band 在 prompt 上方顯示你的 5h/7d 限制、context window 和 cache hit rate

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
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

讓 Claude 的問題更容易閱讀與回答的 Claude Code mods（qa-guide）。

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
| Last push    | 2026-10-07 |
| First listed | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>動畫錄影 · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">開啟影片</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

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
| Stars        | **11**     |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Claude Code 的十個開源模組：即時窗格、橫幅、狀態列與工具呼叫防護。燃燒計、發射代碼、工作階段結束、頭目戰、程式碼寵物及更多功能。

<sub>🔧 在程式碼中找到使用處: `swarm/README.md`</sub>

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
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Summary

兩個 Claude Code 模組：Codex computer-use 橋接器和協調的 Claude 工作階段。原始碼、建置提示、設定與測試。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stars        | **10**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

圍繞你的 Claude Code 和 Codex terminals 的 UI，由你的 agents 建構，所以你腦中唯一的 model 就是你自己的。

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
| Last push    | 2026-10-08 |
| First listed | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

KOZMOS——適用於 Claude Code 的即時視覺化模組（CLI + 桌面）：提示上方的頻帶、側邊欄、狀態跑馬燈、夥伴、守衛和音效。

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
| Stars        | **9**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

一個外掛中的六個 Claude Code mods（Token Weather、Cache Keeper、Wait What、Prompt Queue、Snake、Blast Radius），具備各 mod 的開關，另附 mods 與 hooks 的報告。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 25 天</summary>

##### 📝 Summary

以模組形式建立的 Claude Code 工作階段追蹤器：內容視窗、計畫配額消耗率、每回合成本

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-09-15 |
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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

개발동생 的 Claude Code mods 集合。計程車套件：計費表、導航、超速取締攝影機、行車記錄器

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">觀看平台 youtube.com</a> · 播放會在主機網站上開啟；GitHub 無法將其嵌入頁面內</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Markdown，在您輸入時直接繪製到 Claude Code 的提示框中。圍欄程式碼甚至在您關閉圍欄之前，就會變成語法高亮卡片。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-03 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Claude Code mod：像素螃蟹用量面板 usage-hud + 終端裡可點的 HTML 連結和一鍵複製程式碼卡片 html-shelf

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-08 |
| First listed | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code 的模組：為終端機 UI 新增即時窗格與行為的函式鉤子外掛程式

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Summary

Claude Code mod（外掛），新增含有 Activity、Files、Agents、Context 和 MCP 分頁的側邊窗格、提示上方的狀態列、重新設計樣式的聊天、終端機中的 Mermaid 圖表、表格，以及程式碼與 diff 面板。色彩同時遵循 /color 和 /theme（dark、light 和其他）。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-06 |
| First listed | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 459</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - 可與 Claude Code 搭配使用的 100 多個 mods 集合.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其建置工具：先是 builder skill，接著是 mods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天執行的 Claude Code harness，自第一天起便以此名稱發布，如今與 ucsandman/Agnostic-AI 使用相同的儲存庫：防護…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 使用 Claude Mods 為 Claude Code 換屋頂：不修改二進位檔，將系統提示與英文提醒替換成你自己的文字（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四個 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 和 Collision Guard。
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code 模組：把代理程式的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - 在 Claude 讀取前修正並翻譯你的提示詞的 Claude Code mods。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的側邊窗格：工作階段執行的子代理程式、各自正在做的事、其權杖，以及只需點擊即可查看的對話.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Claude Code 的驾驶舱：就在提示词上方显示即时计划列、子智能体列、带重置倒数的使用限制、模型路由与迷你桌宠。CLI 与 Desktop.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 關於 Claude Code 模組、其運作方式、建立方式，以及安裝前檢查方法的附來源 Obsidian 知識庫.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教導 Claude Code agents 建構 Claude Mods（function-hook plugins）的 Skill，附 starter…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 來自 Nekyia Labs 的 Claude Code mods 與技能，由生活在持久化家園中的 AI 建置並日常使用。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 用於 Claude Code 的 Claude Mods（function-hooks plugins）.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社群 Claude mods、插件與技能，可從單一市場安裝。
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane 模組展示館：經過檢查並置頂的 Claude Code 模組.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 供使用對話式代理的人類使用的決策佇列 CLI/TUI。代理張貼問題，人類從單一收件匣回答.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE 面板 mod：代理看板、檔案樹和 HWP/PDF 檢視器、系統狀態、Claude/Codex/Antigravity…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - 適用於 Claude Code 的浮動狀態卡——模型、上下文、速率限制、費用、分支——另附可由任何腳本或 mod 提供資料的進度 API.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code 模組：在你分享螢幕時，screen-guard 會遮蔽名稱與機密；cache-panel 會在提示快取即將失效前提醒你.
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions。解鎖 Claude 的完整威力.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - 適用於 Claude Code 的面板、防護措施與生活品質模組：內容、使用量、即時活動、通知、安全規則、提示教練、命令中心.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示框上方的兩個 Claude Code 模組：內容視窗量表、5 小時限制、提示時鐘和工作階段費用。
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Your plan, watching itself. Local desktop roadmap tree that Claude Code and any…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 讀取 Claude Code 命名的 markdown 檔案，並在工作階段旁呈現；指向任何區塊即可讓 Claude 編輯它。一個 Claude Code 模組.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的語音協作者。與由 ElevenLabs conversational AI 驅動的 3D 狼人討論事情；當你同意後，它會將提示傳送給…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code 模組：typing-speed，具備每次提示統計的即時打字速度計。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code 的煙火：每次按鍵、工具呼叫、提交和通過的測試，都會在提示上方化為盲文煙火升起。Claude Code 模組.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 探索 Claude Code mods、外掛和擴充功能，包含動畫示範、分類清單和直接原始碼連結。由 FindMods.dev 驅動.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code 模組：在逐字稿中內嵌繪製 mermaid 圖表。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code mods（function-hook 外掛程式）：session-switcher 等。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在提示上方顯示貼上的圖片縮圖，適用於任何終端機。
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code 模組：mod-scout（尋找您最常使用的模組）、usage-meter、check-ledger、resume-nudge。
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 用於同時執行多個工作階段的兩個 Claude Code 模組：提示上方的內容卡片，以及聊天旁的工作階段窗格.
- [scodge-24/workface](https://github.com/scodge-24/workface) - Claude Code mod：直接從 TUI 原生控制自動壓縮內容.
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - 讓 Claude Pro 方案持續更久：Claude Code 模組，提供精確的使用量 HUD、更短的 shell 輸出，以及不重複讀取檔案.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow for Claude Code：在 prompt 上方顯示計畫、進度以及 Claude 何時需要你的平靜 checklist.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最佳 Claude Code Mods：精選、已驗證、已釘選。一次 /plugin marketplace add，43 個 mods.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 插件：自動 Claude model routing.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code 的六個 mods：動態 Clawd 吉祥物、用量限制與提示快取列、傳送前訊息檢查器、快速回覆、待辦佇列和成本帳本.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code mods 市集：代理迴圈的逐步除錯器、Git 帳戶提示、工作樹狀態列等.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods：Claude 工具選單、Zen 模式、終端機主題、工作量與模式控制項。
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 的最佳全能 mod pack：使用限制與上下文 HUD、針對 rm -rf 和 git reset --hard…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - 在您的 Claude Code 中播放 YouTube Shorts 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren 的 Claude 工具組：適用於 Claude Code 的 skills、mods 與 MCP servers。可透過外掛市場使用單一指令安裝.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code mod，可在兩個並排欄中繪製 Edit 和 Write 差異。
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 模組：Clawd，一個迷你的像素吉祥物，會演示 Claude 正在做什麼。
- [reporails/arcade](https://github.com/reporails/arcade) - 作為 Claude Code mods 的經典桌面遊戲，可在 Claude 工作時於窗格中遊玩。由 Reporails 製作.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精選的 Claude Code 模組清單，可作為外掛程式市集安裝：主題、面板、狀態列、肖像.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 讓代理保持可靠的 Claude Code mods——守護範圍、驗證部署，並在提示上方繪製工作階段的 function hooks.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - 我的 Claude Code mods 集合，每個目錄一個 mod。
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - 五個免費的 Claude Code mods：Simple Mode、Usage Tally、Context Handoff、Inbox Alerts 和…
- [arviaja/token-watch](https://github.com/arviaja/token-watch) - Claude Code mod：顯示此 Mac 上工作階段的 token 使用量、計畫限制和快取溫度。
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur。
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - 剛出廠。Claude Code 模組：要求製作迷因，同時繼續工作。草稿會在側邊面板中產生；挑選、混搭、核准並發布到 Slack.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code 模組：提示快取列、後續步驟、快速按鈕和修改重播 — 可從市集安裝。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 一個 Claude Code 模組，在提示上方的列中繪製你的使用量限制和支出.
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - skill-router 模組：Jev 會挑選並載入每個提示所需的技能.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code mod 的應用程式商店，位於 Claude Code 內：輸入 /mods 即可瀏覽、搜尋並安裝 2,700 個 mod，或要求…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（市集 herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code 模組：規劃進度列、記錄 Claude 留在執行中的項目，以及對工具輸出進行權杖遮罩。
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 日常 UX 用的 Claude Code mods：plan limits、context，以及 agent 正在做什麼。
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs 的 Claude Code mods：streams 將一個 session 中交錯的工作拆解為色彩編碼的 streams。
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - 關於 Windows 上 Claude Code mods 的第一天現場筆記：context/配額燃料條、Thai UI mod、Matrix…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - 我製作並親自用於 Claude Code 設定的模組。
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：在提示詞上方顯示即時成本、context 與方案配額儀表。圖示需要 Nerd Font.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - 一個 Claude Code 模組，會在子代理大量分流、需要大量內容脈絡的提示詞與重試迴圈消耗你的使用量視窗前先暫存它們.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude 的 code-mods。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 一個 Claude Code mod，可用具名 profiles 針對每個 repo 開啟或關閉你的全域 skills、agents、rules 和…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code 的模組：基於函式掛鉤建立的外掛。
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - 電影風格的編碼工作階段片尾字幕。原生 Claude Mod，不會呼叫模型，也不會進行遙測.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 我打造的一批 claude code 模組。
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Claude Code 內由 cliamp 驅動的 YouTube 播放器（Claude Code 模組）。
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods：agent-fleet dashboard 與 autopilot（local-mods marketplace）。
- [vynnlee/mods](https://github.com/vynnlee/mods) - vynnlee 製作的 Claude Code 模組。每個模組一個資料夾，可從單一市場安裝.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - 使用 Claude Code 工作時學習外語。
- [20alexl/windvane](https://github.com/20alexl/windvane) - 替你照看漫長的 Claude Code 工作階段：監看內容填滿、草擬檢查點、在適當時機壓縮，並恢復工作。每個子代理程式都有規則，也有專案記憶.
- [akerskuuug/claude-mods](https://github.com/akerskuuug/claude-mods) - Claude Code mod: usage, limits, branch and model around the prompt。
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - 在 Claude Code Desktop 中提供主題化回覆、全寬圖表，以及一眼即可掌握的內容與限制.
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Agent 撰寫 Java 時，違反阿里 Java 規約（p3c）的程式碼無法寫入磁碟.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code 的即時成本、token 與上下文使用量側邊欄：一個在工作階段內顯示每回合成本、快取命中率、消耗速率及 30 天支出的 mod.
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - 適用於 Claude Code 的 Counter-Strike 1.6 無線電通話——部署時顯示「Fire in the…
- [burnrate-ai/burnrate](https://github.com/burnrate-ai/burnrate) - 查看並放慢 Claude Code 消耗你的 Claude.ai 限制的速度 — 一個 Claude Code mod：即時限制帶、快取看門狗、限制煞車。
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Herdr setup + Claude Code mods for product dev work。
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS 的缺口儀表板，適用於 Claude Code：使用量限制、開啟的工作階段、任務進度、提示快取倒數和待辦事項——由五個 Claude Code…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude 正在烹調。和你的 squad 聊天。朋友在線上，就在你的 Claude Code 工作階段旁邊。零 tokens，零洩漏給 Claude.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Claude Code 模組：在 Claude 工作時，於閒置遊戲中捕捉像素藝術 Modsters.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - 在 Claude Code 工作期間，其提示上方的一場太空戰鬥.
- [davidbalzan/status-band](https://github.com/davidbalzan/status-band) - David Balzan 製作的 Claude Code 模組：status-band，位於提示上方的狀態列。
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每個 Claude Code agent 在其 context 中有哪些檔案，以及各自的比例.
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 保持冷靜。為您的 Claude Code 日子提供的溫度計：根據磁碟上現有的文字記錄，每小時評分 0 到 100，並在您精疲力竭前觸發十分鐘休息的外掛.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - 在 Claude Code 的內容填滿前截短龐大的工具輸出。保留錯誤和摘要，完整文字只需讀取一次即可查看.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 適用於 Terminal 與桌面應用程式的小型 Claude Code mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI skill + mod，可在代理回覆中加入西班牙文單字。
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Claude Mods。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - A Claude Code mod that restyles it as The Machine from Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Claude Code 模組：在適當時機壓縮（提交後、測試通過後、提示快取即將過期前），或在 Claude 要求時壓縮。
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：Claude Code 模組，用於強制執行並驗證子代理程式的 DAG 工作流程，附帶即時 DAG 面板。
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - A pixel-art Naruto companion for Claude Code: 20 ninja, 60 jutsu, performed…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-source mods for Claude Code: panes, status lines, toasts, tool guards and…
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Claude Code mod、外掛、技能、代理、hooks 與 MCP 伺服器的社群目錄。每個項目都連結至其來源.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod：工作階段狀態、即時 Spec Kit 進度與用量視窗治理。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 將內容視窗作為提示上方的一列，採用 Claude Code 繪製自身量表的方式呈現.
- [koslowskyj/tdd-mod](https://github.com/koslowskyj/tdd-mod) - Experimental Claude Code mod that enforces test-driven development: on coding…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - 讓 Claude Code 終端機 UI 看起來像 Claude 桌面應用程式的 Claude Code 外掛程式（模組）：提示氣泡、Markdown…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在背景執行的內容：子代理、Codex 工作、shell、監控器、cron 工作與工作流程.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - 清除聊天，保留工作。Claude Code plugin + relay mod：Claude 會儲存一段簡短交接、清除內容，並自行在新的 context…
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - Personal Claude Code mods: otto-hud, Otto the octopus with context weather and…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 一個 Claude Mod，在逐字稿旁的面板中顯示工作階段的 GitHub pull requests：將描述引用到提示框中，查看檢查和審查狀態。
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools：用於偵錯 Claude Code 工具呼叫的偵錯器.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文件查證器、程式碼稽核器、錯誤記憶記錄、mod 等.
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Claude Code mod，會在你傳送粗略提示前將其改寫成清楚的提示。讀取你的提示和對話，除此之外不讀取任何內容.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 好幫手外掛：位於提示詞上方、會記住你的規則並標示 Claude 捷徑的 ASCII 夥伴。
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - 適用於每個代理工具可見性的 Claude Code 插件——依照每個迴圈隱藏並拒絕子代理、技能、MCP 與內建工具。
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod：由 Jev 引導的模型／工作量路由、逐字保留的內容壓縮，以及輸出截短，讓長時間工作階段更省成本。
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods: security layer for Claude Code - secret redaction…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Claude Code mods 集合.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin 與 mod：一個 AI-native SDLC。
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - 精彩的 Claude Code 模組合集 | Claude Code 模組合集.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 外掛程式（模組）：在多個 Claude 帳戶之間切換、在狀態橫幅中查看使用量限制，並在終端機面板中管理代理程式、工作樹、檢查點與差異。
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 經過測試、可用單一指令安裝的 Claude Code 模組：YOLO 模式的防護機制、即時成本與內容、面板、寵物等。另附精選的最佳社群模組清單.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code 模組：適用於日常工作的即時面板與 hooks。
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一個 Claude Code mod，可依要求用本機開源 Kokoro TTS 聲音朗讀 Claude 的回覆與你的提示.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用於即時窗格、成本感知模型路由和安全防護的小型外掛程式。用一個命令從 marketplace 安裝.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 與 plugin：用量監視器、token 追蹤器與狀態列.
- [Verinoda-Labs/verinoda-symbiosis](https://github.com/Verinoda-Labs/verinoda-symbiosis) - Verinoda + Claude Code，攜手合作：Verinoda 搭配 verinoda-live，這是一個 Claude Code…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods。touch-map：以樹狀圖和活動地圖查看 Claude 列出、讀取、編輯或建立了哪些檔案.
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - 一個 Claude Code 模組，以簡明英文摘要你尚未閱讀的代理程式訊息。執行 /catchup、輸入 &#x27;brief me&#x27;，或按下按鈕.
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code mods + cheap-executor driver: one Claude session as lead, MiniMax…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace)。
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示上方的動畫盲文貓。
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code 模組：透過子 Claude Code 將低成本工作分派給 GLM/Kimi，將關鍵工作保留在你的訂閱中。移植自 Maggy.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示上方的一隻像素貓，會執行 OmniDimension 語音代理程式測試通話。Claude Code 模組.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一個 Claude Code 模組，會選擇適當時機進行壓縮，以保持上下文視窗較小.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code 的 Claude 模組：token-meter（工作階段權杖、Claude 與本機 LLMs 的比較，搭配 Pac-Man 內容迷宮）。
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider 製作的 Claude Code 外掛程式市集。
- [ankits3a/cache-keeper](https://github.com/ankits3a/cache-keeper) - Claude Code mod: prompt-cache band, keep-warm, handoff judge trial。
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - 一個 Claude Code 模組，會在每個子代理程式啟動前為其選擇模型，並顯示每個模型的成本.
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - 一個 Claude Code mod：用一行安靜顯示你的上下文視窗，在重要之前保持灰色.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - 每次程式碼變更後，LGTM Lines 飛船都會航行經過——一個 Claude Code mod。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 將你的 Claude 使用量限制呈現為動畫村民生命值卡片——一個 Claude Code mod。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 團隊的 Claude Code mods（ather marketplace）。
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作時進行短訓練：每日目標、連勝、徽章與可選排行榜。一個 Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code 的用量看板：各模型花費（今日、本週、本月、全部時間）與每週上限預測.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方顯示 Apple Music 與 Spotify，包含封面圖、控制項與 Up next…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - 五個用於同時執行多個工作階段的 Claude Code mods：fleet board、PR-to-production…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - 適用於協調器與工作執行緒工作階段的 Claude Code 模組。
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Claude Code 模組：使用量列、聊天名單、/cube、/handoff、提示清理。
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 模組：快取時鐘、影響範圍、建議、工作清單、烤架。
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code 模組：Suggestion Spotlight 顯示 Claude 的下一個建議提示所指向的內容.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是給你的 Claude Code 的一隻貓頭鷹。
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - 適用於 ai-architect.tools harness 的 Claude Code 模組：每個模組專注一項關注點，透過相依性共享狀態。
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 單行 Claude Code 頻帶（快取倒數、上下文、限制、下一項任務）加上七個社群模組，以單一外掛安裝，預設保持安靜.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - 原版 Doom 引擎搭配 Freedoom，可在 Claude Code 內遊玩。Mac Apple Silicon alpha.
- [cmorss/claude-mods](https://github.com/cmorss/claude-mods) - 用於 git worktree 的 Claude Code 模組：/terminal 和 /worktree-files 會在對話運作的 worktree…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 給真正工程師的 Claude Code 模組。
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 團隊專用的 Claude Code 模組（usage-meter：藍色火焰／梗犬使用量列）。
- [David-AP-TON618/claude-explain](https://github.com/David-AP-TON618/claude-explain) - Claude Code mod: /explain re-renders an answer as controlled language (STE), a…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - 住在 Claude Code 內的 Tamagotchi：它會孵化、吃掉 Claude 寫的程式碼、留下 bugs，並成長為八種成體之一.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Claude Code 終端機對話中的書籤與 vim 風格標記：醒目顯示一行、標記它，再跳回該處.
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane。
- [delexw/codyssey](https://github.com/delexw/codyssey) - 將每個 Claude Code…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code mod: shows the time on each prompt and reply in the terminal and…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 以函式掛鉤形式撰寫的 Claude Code 模組，以及提供這些模組的市集。dash：工作階段在單一面板中的儀表板.
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code mods and design systems: crab-crew and the Crab Crew design system。
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - divramod 的 Claude Code 程式碼修改：Claude Code 介面的即時面板與調整。
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - 我在每台機器上都使用的 Claude Code 模組：savvy-progress、filetree、skins、blast-radius。
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods。
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - 嘿，靜音了！拋開差異、剪掉即興，不再編輯、少點花費。
- [elkinaguas/claude-mods](https://github.com/elkinaguas/claude-mods)
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude Code 模組：在 Desktop 應用程式和終端機中，將訂閱用量（5h / 7d）顯示為提示文字上方的橫條。
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Claude Code Mod for background test progress: JUnit, Karma, pytest and unittest.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - 為 Claude Code 設計的動態模組：即時、響應式監視器，監看模型、努力程度、內容、使用量限制、任務進度、子代理程式與每個工作階段.
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace。
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - A live radar of your parallel branches and worktrees above the prompt: which…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - 我的 Claude Code 模組。
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude。
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+click copy link on every code block in Claude Code replies。
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - jev 模組：適用於 Claude Code 的 $.jev，來自 TypeSafe Jev 的具型別判斷.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Mod de Claude Code: panel que muestra si el caché de prompts está caliente o…
- [Gersom/claude-mod-usage-meter](https://github.com/Gersom/claude-mod-usage-meter) - Mod de Claude Code: recuadro con el % de contexto y de los límites de 5 horas y…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - 適用於 Claude Code 的模組：hooks 外掛程式，例如 usage-meter。
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code 模組（函式掛鉤外掛程式），透過單一市集安裝.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code 的 Evangelion 風格側邊欄：上下文、配額、活動、PR、硬體、工作階段和 forge 面板。
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Useful claude code mods。
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Claude-Code Plugin (Mod) lets you see what the model is doing while it works.
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Claude Code 面板中的測試結果：來自 Claude 自身測試執行的失敗、其詳細資訊與執行歷史。
- [hfknight/claude-mod-said](https://github.com/hfknight/claude-mod-said) - 一個 Claude Code 模組：/said 以時間軸形式開啟你所傳送訊息的側邊面板；按一下即可跳回該訊息。
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模組：每個回答花費的時間、Claude 思考的時間，以及 tok/s，顯示在 Claude 桌面應用程式的回覆正下方.
- [icedevil2001/session-sidebar](https://github.com/icedevil2001/session-sidebar) - Claude Code mod：在右側邊欄顯示工作階段的連結、須知事項與待辦項目。
- [iddhi-sulakshana/claude-mods](https://github.com/iddhi-sulakshana/claude-mods) - Claude Code 的模組：下一步按鈕、跨工作階段訊息傳遞，以及每回合模型路由。
- [jagp/xray-mod](https://github.com/jagp/xray-mod) - ⋐∿⋑ 深入凝視你的內容：即時 Claude Code 模組，逐次呼叫、逐輪顯示填入內容視窗的項目.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - A Claude Code mod: one pane for every subagent, the files they touch, and your…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼。/ctx 開或關（Claude Code 模組）。
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（Claude Code 模組）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（Claude Code 模組）。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（Claude Code 模組）。
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（Claude Code 模組）。
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（Claude Code 模組）。
- [jgilb17/claude-mods](https://github.com/jgilb17/claude-mods)
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Claude Code 的證據閘門計畫檢查清單：核准的計畫會成為檢查清單，Claude 只有在具備驗證證據時才能勾選。
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Claude Code 的小型修改，例如新的斜線命令與側邊面板.
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code。
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - 可在 Claude Code 工作時於其中遊玩的多人遊戲。
- [juliomyitbrain/claude-code-git-graph](https://github.com/juliomyitbrain/claude-code-git-graph) - Claude Code mod: a pane that draws the repository。
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Claude Code mod：你離開時保持提示快取溫熱，並在提示會重新快取大型對話前先詢問.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的帶狀列中：演出 session、顯示正在執行的項目、context 和使用限制，並與你的 CI…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - 一個 Claude Code mod：在提示上方顯示速率限制額度、工作階段 Token 與成本。
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - 使用 VOICEVOX / Irodori-TTS 等朗讀 Claude Code 的回覆與通知的模組。
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - 用於讀取並加入你的 Claude Code 工作階段之間對話的 Claude Mod（/crosstalk）。
- [kikostefanov-lab/claude-code-mods](https://github.com/kikostefanov-lab/claude-code-mods) - Claude Code 模組：白板窗格，讓 Claude 繪製 Mermaid/UML 圖表，並在本機呈現。
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Niceties/quality of life improvement Claude mods。
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - 用 haiku 壓縮冷掉的 claude code 工作階段——顯示你節省了什麼的一行快取列。
- [kk5190/claude-code-mods](https://github.com/kk5190/claude-code-mods) - Claude Code 的模組：內容量計與開發伺服器窗格。
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - A live task HUD for Claude Code Desktop: a strip above the prompt while Claude…
- [KytioisaCat/playpen](https://github.com/KytioisaCat/playpen) - 誰需要關注？你的其他 Claude Code 工作階段會以提示文字上方的卡片顯示——一個 Claude Code 模組。
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 社群策劃的 Claude Code Mods 指南：使用案例、原始示範、相容性證據與安全性備註。English / 中文。非官方.
- [lucasram20/claude-mods](https://github.com/lucasram20/claude-mods)
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一個 Claude Code 模組，會在 iTerm2 分頁副標題中顯示 Claude 正在進行的工作，因此只要看一眼分頁列，就能知道哪個工作階段需要你的注意。
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Claude Code 模組：提醒主要工作階段委派工作給子代理程式，並在提示文字上方顯示主要內容與委派內容的權杖數.
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - My personal collection of claude mod plugins。
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel。
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 一個 Claude Code mod，具備可切換的權限設定檔：安全基準、可開關的具名設定檔，其他所有操作仍會詢問.
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references。
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community mods for Claude Code: guards, panes, and commands that run inside…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code 的側邊面板：Claude 編寫的檔案、終端機分割畫面、具有 pull 功能的 git 儲存庫狀態、使用量列與新工單——提供 41…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mikejhill/claude-usage-status](https://github.com/mikejhill/claude-usage-status) - Claude Code mod: always-on band showing 5h/weekly limits, context fill, and…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code 的安靜側邊面板：此工作階段正在做什麼、它的計畫、代理，以及其他每個工作階段。
- [mmedum/spor](https://github.com/mmedum/spor) - 還原 Claude Code 摺疊的內容：Claude 讀取的檔案、執行的命令，以及每一輪所執行的工作。
- [moonteek/claude-mods](https://github.com/moonteek/claude-mods) - Claude Code 模組：提示詞上方的記憶體列與即時任務檢查清單.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code 模組：自動交接與進度列。土耳其文，只需幾個指令即可安裝.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模組：透過在工作階段開始時設定 CLAUDE_CODE_ENABLE_TODO_TOOLS，為省略待辦工具的模型重新啟用它們.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模組：提示上方每個任務清單一行，顯示目前任務、進度列與計數。在終端機與桌面應用程式中外觀相同.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 內與 AI 玩 Connect Four（/connect-four）。
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Claude Code 的像素藝術金絲雀：當 Claude 不再遵循你的指示時，它會死亡，接著自動壓縮並復活。一個 Claude Code 模組.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模組：當另一個程式設計代理提交至你的儲存庫時，Claude 會透過差異與測試進行審查，而不是相信它的報告.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 適用於多個 AI 代理共用儲存庫的 Claude Code 模組：防止秘密值離開 .env、防止推送至公開遠端儲存庫，以及防止 git…
- [narley/sessions-sidebar](https://github.com/narley/sessions-sidebar) - Claude Code mod: a sidebar listing every Claude Code session, for Warp。
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Claude Code 的賽博霓虹網路廣播窗格——synthwave 旋鈕、目前播放、VU、本機 ffplay。
- [niksavis/handily](https://github.com/niksavis/handily) - 顯示你在任何追蹤器中的工作項目、任務與工作階段的 Claude Code Mod。Mod 只顯示並詢問；從不強制執行.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - 在 Claude Code 的長時間 Monitor 監看過期時重新啟用，不喚醒 Claude，也不消耗一次回合。
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code 的 SQL 防護欄：在 Claude 透過 DB CLI（函式掛鉤／Mods）執行 DELETE、沒有 WHERE 的…
- [OctopiAI/claude-code-statusline](https://github.com/OctopiAI/claude-code-statusline) - 輕量級的 Claude Code 模組。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - 一個適用於 Claude Code、以 Windows 與 CJK 為優先的模組：在任何終端機中提供貼上影像與文字預覽、帶有 CJK…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Claude Code 的提示音：當 Claude 完成、需要你的輸入或遇到錯誤時播放聲音。十種原創音效、自訂檔案、鍵盤選擇器.
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods：影像縮圖與狀態列。
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 最佳的 Claude Code 模組，依它們能為您做的事排序。人工檢查，每個模組一行介紹.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Claude Code mod：在 Claude 桌面應用程式的窗格中查看代理看過的每張圖片與檔案（螢幕截圖、算繪結果、讀取內容）。
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - A Claude Code mod that holds risky shell commands。
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - 兩個適用於 Claude Code 的 Claude 模組：護欄。
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Claude Code 的 Lazy Panda Panel：不用抬爪也能檢閱文件.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 桌面應用程式 Code 分頁的即時工作階段統計側邊窗格：上下文、成本、git 變更、回合統計、子代理程式、日誌.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - 適用於我的 Claude Desktop 設定的各種模組與技能。
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code 的模組：safety-guard 會封鎖破壞性指令與秘密檔案存取；notify-router…
- [prompteafacil-hub/mods-claude-code](https://github.com/prompteafacil-hub/mods-claude-code) - Mods de Claude Code de la comunidad prompteafacil。
- [ptpmediabr/ideas-shelf](https://github.com/ptpmediabr/ideas-shelf) - 依專案整理的點子架：在面板中記下點子並標記為已完成；內容會儲存在專案根目錄的 IDEAS.md.
- [ptpmediabr/mods-manager](https://github.com/ptpmediabr/mods-manager) - 用於檢視、啟用、停用、安裝 mods 與 plugins，以及將它們分組為設定檔的面板.
- [ptpmediabr/side-chat](https://github.com/ptpmediabr/side-chat) - 工作階段內的側邊聊天窗格，可在你選擇的模型上回答問題或執行要求.
- [ptpmediabr/usage-weather](https://github.com/ptpmediabr/usage-weather) - 提示上方的一行簡潔資訊：內容、5 小時與每週使用量、提示快取是否溫熱，以及「清除並繼續」按鈕.
- [qarge/claude-mods](https://github.com/qarge/claude-mods)
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod：即時股票行情、/quote 面板、價格警示、市場帶，以及模型可呼叫的報價工具。
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - 以單一外掛市集發布的 Claude Code 模組。
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod：在提示上方一列顯示 SSH 主機、RAM 與 5h/7d 用量限制。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：在 Claude 工作時做伏地挺身。無 tokens.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Claude Code 的模組商店：從 GitHub 擷取模組、預覽模組並提供市集。
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 模組：將你在計畫模式中核准的計畫轉為提示上方的即時核取清單，隨著 Claude 完成每個步驟逐一勾選。
- [sadhirr1/claude-mods](https://github.com/sadhirr1/claude-mods) - Just a repo with different claude mods。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精選的 Claude Code 模組清單。每個項目都已複製，並使用 claude plugin validate 檢查，且標記其可接觸的內容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：輔助代理程式在 Haiku 上執行，大型檔案與日誌則由免費的 Gemini 模型摘要，而不是填滿 Claude 的內容.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 隨工作階段播放的 lo-fi 原聲帶：平靜、專注、流暢，另有通過與失敗測試的提示音。原創音樂.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 撰寫程式時學習：每當一輪操作變更程式碼後，提示上方會出現一個關於該確切變更的問題。依概念評分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 記錄 Claude 所做每次編輯的磁帶：重播每項變更自行輸入的過程、逐步檢視，並將任何檔案倒轉至任何步驟.
- [samaphp/session-links](https://github.com/samaphp/session-links) - 工作階段提及的每個連結，都集中顯示在提示上方的一列中。一個 Claude Code 程式碼修改.
- [SanjayPG/claude-code-usage-tracker](https://github.com/SanjayPG/claude-code-usage-tracker) - Claude Code mod: live usage-quota progress bars above your prompt.
- [SanjayPG/claude-quota-band.](https://github.com/SanjayPG/claude-quota-band.) - Claude Code mod: live usage-quota progress bars above your prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code 函式掛鉤最小示範：提示上方的即時 token／成本面板、可點擊按鈕、獨立繪製的執行緒動畫，全程零 token。
- [servaes/cockpit](https://github.com/servaes/cockpit) - André Servaes 的 Cockpit Board 和其他 Claude Code 模組。
- [shaheershoaib/agent-warehouse](https://github.com/shaheershoaib/agent-warehouse) - agent-warehouse: a Claude Code mod by Shaheer Shoaib.
- [shaheershoaib/usage-meter](https://github.com/shaheershoaib/usage-meter) - usage-meter: a Claude Code mod by Shaheer Shoaib.
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - ShellTime 製作的 Claude Code 模組（function-hook 外掛）。
- [siller/supermod](https://github.com/siller/supermod) - Claude Code mod: Superpowers progress, context window and agents above the…
- [simplybychris/claude-code-mods](https://github.com/simplybychris/claude-code-mods) - Claude Code 的模組：Rec Mode、Cache Bar、Snake 與代理程式面板。
- [skryvets/claude-code-session-mod](https://github.com/skryvets/claude-code-session-mod) - Claude Code mod: coloured session info under the prompt - context, model…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code 的舒適 RPG HUD 修改（測試版，先推出桌面應用程式；計畫支援 CLI）：多職業 Clawd…
- [sstani-bgv/claude-crew](https://github.com/sstani-bgv/claude-crew) - Claude Code 模組：供子代理程式使用的像素螃蟹側邊欄。
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 為 Claude Code 一鍵產生 commit 訊息，搭配跳舞的像素風 Malenia。
- [StevenGFX/claude-gh-actions](https://github.com/StevenGFX/claude-gh-actions) - Claude Code mod: GitHub Actions runs in a /ci pane, the status line and toasts。
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude code mods。
- [stylusnexus/claude-mods](https://github.com/stylusnexus/claude-mods)
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods。
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Claude Code mods: mini-bar HUD。
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugins for Claude Code。
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Mods for Claude Code: delete-guard。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Claude Code 模組：就在提示詞上方查看你的 Claude 計畫用量（工作階段與每週限制、重設倒數、內容）；可在終端機與桌面應用程式中運作.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code 模組：每個子代理程式的即時團隊面板（模型、努力程度、步驟、內容、成本、時間）、提示詞上方的工作列，以及 5 小時／每週計畫限制圓環.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一個 Claude Code 模組，在窗格中顯示目前工作階段：每個提示詞、Claude 分階段為其完成的工作、每個子代理程式及其答案，以及提示詞的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一個 Claude Code mod 外掛市集：function-hooks 外掛，可在 Claude Code 內繪製 band、窗格和其他 UI.
- [thickiran/claude-coaster-tycoon](https://github.com/thickiran/claude-coaster-tycoon) - 🎢 Claude builds you a RollerCoaster Tycoon-style theme park while it works.
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code mod: a docked pane showing the session。
- [tjanuki/claude-mod-context-meter](https://github.com/tjanuki/claude-mod-context-meter) - Claude Code mod: context-window fill in the status line and a hand-off reminder…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - 讓你的 Claude Code 用量提升至最多兩倍。這是一個會為每個提示詞與每個子代理程式選擇適當推理努力程度的外掛.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Toptaab 製作的 Claude Code 模組。
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Claude Code mod：一個追蹤你的子代理程式及其所使用檔案的樂隊與面板。
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - A curated catalogue of Claude Code mods, each with a copy-paste prompt that…
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模組：適用於長時間執行任務的動畫進度列與完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Three small Claude Code mods: see when your subagents will finish, queue…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 說出「我迷路了」，Claude 就會再次用日常用語解釋上一則回覆。Claude Code plugin.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作旁的窗格中向 Claude 提出旁支問題。主要對話永遠看不到它。運作方式類似桌面應用程式的 /btw.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace de mods do Claude Code com instalação em um passo e guia em vídeo…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Rate-limit countdowns and a burn-rate forecast for Claude Code。
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - 適用於 Claude Code 的 Roblox Studio 安全層：RemoteEvent 稽核、復原、Team Create 保護，以及重播…
- [was865/usage-band](https://github.com/was865/usage-band) - Claude Code mod: context window, prompt cache hit rate and countdown, rate…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code。
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Claude Code mods: stage-toons, a workflow progress bar above the prompt with…
- [wolves/usage-line](https://github.com/wolves/usage-line) - Claude Code mod: usage, model, effort and advisor readout above the prompt。
- [wszaq/claude-mods](https://github.com/wszaq/claude-mods) - 用於更安全、更清晰本機工作流程的小型 Claude Code 外掛.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 用於 Claude Code 的 Mods。agent-crew：以即時 pixel crew 觀看你的 subagents 工作，包含…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Claude Code 模組：繁中下一步膠囊、區塊複製、貼圖縮圖。
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - 持續顯示於 Claude Code 提示文字上方的橫條：桌面與終端機上的內容填入量和速率限制視窗。
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - Personal Claude Code mods (plugin marketplace)。
- [zhuzhu0710/claude-mods](https://github.com/zhuzhu0710/claude-mods)
- [ziedgithub/claude-code-mods](https://github.com/ziedgithub/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 由 Anthropic PBC（无关联关系）这支势不可挡的团队精心打造的顶级资源精选，献给最强大的智能体与无可争议的编码伴侣冠军 Claude Code.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 一款顯示正在發生什麼事的 Claude Code 外掛——內容使用量、作用中的工具、執行中的代理人，以及待辦事項進度。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 高度可自訂的精美 Claude Code CLI 狀態列，支援 powerline、主題等功能.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 系統提示的所有部分、27…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45 多項充分發揮 Claude Code 效用的秘訣，從基礎到進階——包括自訂狀態列指令碼，以及在容器中自行執行的 Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code／Codex 技能 — 產生小紅書輪播圖與微信 21:9+1:1 封面組合.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Beautiful vim-style powerline for Claude Code。
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 在終端機窗格中檢視 coding agent 的 diff，並將逐行留言傳回 Claude Code、Codex、OpenCode 或 Pi.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 適用於 Claude Code 的完整狀態列外掛程式，提供內容使用量、API 速率限制與成本追蹤。
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code 与 Codex 本地 token 追踪 — 状态列（Codex 业界首创伪 statusline）、GitHub…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - 為 Claude Code 建立修改模組：攔截任何請求、修改任何回應、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - 適用於 Claude Code 的完整狀態列儀表板 — 工作階段資訊、配額列、代理追蹤器、MCP 健康狀態、訊息記錄等.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：追蹤你的 Claude Code 工作階段的碳足跡。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - 由 awesomejun 製作的 Claude Code 美觀狀態列。
- [fatihaydost/brand-identity-skill](https://github.com/fatihaydost/brand-identity-skill) - A Claude Code skill that designs a brand identity as one system: logo…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公開的 Claude Code skills 與 mods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - 適用於 Claude Code 的 Skills、mods、subagents、hooks、slash commands 和…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免費 LLM APIs 與程式設計代理 — 每週自動更新並探測驗證兩次。免費方案、免卡試用、免費模型.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - 用於 Claude Code sessions 的終端機 statusline。
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 在你的終端機、Claude Code 和 Cursor CLI statusline，以及 MCP…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 將程式碼代理變成鍵盤韌體專家的 Agent Skill。稽核 ZMK/QMK 鍵位圖、調整 home row mods、讓軌跡球具備圖層感知能力、透過 CI…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - 個人 Claude Code 設定版本，儲存於 ~/.claude — 代理、技能、hooks、設定與狀態列（參考用途，不是入門範本）。
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供禮拜時間、回曆日期、adhkar、每日 ayah、sunnah fasting、Ramadan、Jumu。
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) - Tavily-powered optional search tool for DeepSeek Harness。
- [livlign/ccbit](https://github.com/livlign/ccbit) - 适用于 Claude Code 的会话感知状态列。一个颜文字脸孔会读取逐字稿，并在你的各个会话中叙述状态。一个 Go 二进位档，无 hooks，无常驻程式.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — 用于研究主题、可追溯知识卡片与可重複使用 AI 讨论的 DeepSeek Harness 插件.
- [igdigitallab/cardloop](https://github.com/igdigitallab/cardloop) - Your AI dev team on your own server, steered from your phone.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - 适用于 .NET DDD/Clean Architecture 的可携式 Claude Code 工具包：严格的 TDD…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 適用於 Claude Code、pi 和 DeepSeek Harness 的外掛合集：狀態列 HUD、任務進度條、Tailscale 節點狀態等 · 適用於…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 可攜式的 Claude Code 全域設定：自訂技能、PreToolUse 鉤子與自訂狀態列。可在 Linux、macOS、WSL 上執行.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：整理過的 skills 與 mods，可在任何人的機器上運作.
- [34823/tg-pane](https://github.com/34823/tg-pane) - Claude Code 中的 Telegram：在面板中閱讀聊天與頻道，取得未讀貼文的 AI 摘要。無需 API key，無需機器人.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge，自行开发（非 fork）：串流回复卡／单一实例中的多个机器人。
- [Dakaric/claude-code-statusline](https://github.com/Dakaric/claude-code-statusline) - Claude Code 的即插即用狀態列：上下文視窗列、提示快取 TTL、具節奏控制的 5 小時與每週速率限制、一鍵切換帳號.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code 外掛程式與技能市集，用於促進 Hytale 遊戲模組的開發。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code 的權杖治理：由頂級模型負責指揮，執行交給足夠且最便宜的方式。路由核心、由 hook 強制執行的預算上限、遙測、附帶計畫配額的狀態列.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - 適用於 Claude Code 的分割窗格檢視器，運行於 Windows Terminal 和 tmux：以 Markdown…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop Code 分頁的非官方模組——usage-pet：帶有 Clawd 的使用量橫幅，以及動畫像素寵物。淺色與深色、英文與中文.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media 修改版的儲存庫.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - 降低 Claude Code 與 Codex 的 Token 花費：將查詢和測試執行路由至更便宜的模型，將文件轉換為精簡…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Claude Code 的用量限制警示：macOS 通知、應用程式內警告，以及工作階段（5h）與每週限制的狀態列百分比。
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - 適用於 Linux、WSL、Windows 和 macOS 的可設定 Claude Code 狀態列，包含提示計時、子代理列和終端機設定 UI.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Fast Rust statusline for Claude Code — payload-first, cached git, ~10ms renders。
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - 具備內容列、token 迷你圖與花費追蹤器的 Claude Code 狀態列。
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - 適用於 Claude Code 的即時用量儀表板——以 Catppuccin 膠囊樣式的側邊窗格顯示內容分解、快取命中、速率限制預測、費用與活動.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - 在 macOS、Linux 和 Windows 上顯示 Claude Code 的重要狀態詳細資訊，包括模型、內容、限制、git 資訊與工作階段時間.
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - 適用於 Claude Code 的親切、隨心調整的狀態列——真彩色列、約 80 種佈景主題，以及透過單一 JSON 檔案進行的元素個別樣式設定。
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Multi-row Claude Code status line: spend, context %, git, and active account…
- [QingqiShi/claude](https://github.com/QingqiShi/claude) - Personal ~/.claude for Claude Code: settings, global CLAUDE.md, hooks, status…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - 適用於 claude code、包含實用資訊的狀態列。
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - 用於組織多公司 Claude Code 工作區的入門範本：已清理的 CLAUDE.md 範本、SessionStart…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 原生 agent 團隊。受控。嚴格的工作者限制、即時團隊可見性，以及 Claude Code 的可攜式設定.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code 的自訂狀態列——顯示用量百分比、內容大小、費用與計時器的內容列。
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - 搭載 baloo 的 Claude Code 外掛程式市集：技能、可根據專案決策驗證變更的代理、指南、檢查項目、輸出樣式與狀態列.
- [chrisns/claude-image-cli-mod](https://github.com/chrisns/claude-image-cli-mod) - 在你的 Claude Code 記錄中查看命令列印的圖片（imgcat、iTerm2 內嵌圖片）.
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Claude Code 狀態列：內容用量、5h/7d 配額列、重設時間、git 分支。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 專業級 Claude Code 狀態列：工作階段持續時間、使用 ECB 外匯的多幣別費用、每百萬 token 費率、支出上限。MIT、零金鑰、跨平台.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - 具備訂閱感知功能的 Claude Code 狀態列。
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - A Claude Code plugin: a pane of the live Claude Code and Codex sessions on your…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - A rich terminal statusline for Claude Code — Bun + TypeScript, zero runtime…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Claude Code 的雙列狀態列：上下文、帶有節奏標記的速率限制、成本與快取。
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Claude Code plugin，可在 transcript 中精美呈現 Mermaid diagrams：任何終端機中的彩色 Unicode…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - 適用於 Claude Code 的工具、技能與代理程式——首先提供顯示模型、分支、PR、內容大小、提示快取剩餘時間及費用的狀態列.
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Claude Code global config: agents, skills, mods, settings。
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Claude Code 外掛：在頁尾右下角隨時查看剩餘的 Claude 5 小時用量限制——不再需要 /usage。
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code 的實際 DeepSeek API 花費：以 DeepSeek…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code 狀態列與代理面板列。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 將 Claude 的待辦事項同步至 Fizzy.do，讓團隊即時掌握進度，將任務轉換為持久卡片，以提升協作效率並輕鬆追蹤進度.
- [izzatum/claude-code-cockpit](https://github.com/izzatum/claude-code-cockpit) - Claude Code status line plugin（cockpit）：context %、session cost 與 rate…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - A status line and token line for Claude Code: context, 5-hour and weekly usage…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - 為 Claude Code 顯示詳細且以顏色標示的狀態列，呈現上下文、git 狀態、費用與速率限制.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code 設定選單、狀態列與設定。
- [Larg0Winch/claude-label](https://github.com/Larg0Winch/claude-label) - Claude Code 狀態列中每個視窗可編輯的標籤。由 Pacto（pacto.global）提供.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - 在 Windows 上以語音與 Claude Code 對話：使用 codex app-server realtime 的模組與協助工具（ChatGPT 登入）。
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code 狀態列掛鉤——跨工作階段追蹤權杖用量與上下文，壓縮並使用 --resume。
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - 自訂 Claude Code 狀態列，包含內容視窗、API 使用量追蹤、git 狀態與工作階段成本。
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - 適用於 Claude Code 的快速 Rust 狀態列（讀取掛鉤 JSON，將指標記錄至 SQLite）。
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - home-grown, cage-free claude plugins, skills, mods, and more。
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 環境安裝程式：技能、狀態列、掛鉤、權限，以及可選的 Obsidian-vault MCP 伺服器（--vault_root）.
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - 用於理解 Claude 所做事情的 Claude Code 外掛程式與模組：易讀的回答格式與即時工作階段看板（市集：oshn）。
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - 從你的 macOS 選單列監控 Claude Code 狀態，透過即時指示器顯示作用中任務、待處理權限和經過時間.
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - 適用於 Claude Code 的彩色多列狀態列（配額列、內容與子代理面板）。
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - 用於 Windows (PowerShell) 的 Claude Code 狀態列：使用量列、帶有節奏警告的 5h/7d 重設倒數、自動換行。
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Claude Code plugins。Usage Bars 以三條對齊的長條，同時顯示你的工作階段與每週 rate limits，以及 context…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - 適用於 Claude Code 的 Bearings 和 Glossary mod。
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 自訂 Claude Code statusline（上游：kamranahmedse/claude-statusline）。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code 設定與模組，附有共用元件套件、遊樂場與 Storybook。
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude Code 的小型儀表板：上下文百分比、快取倒數計時、5 小時與每週使用量、一鍵 Handoff 至新的聊天，以及在 Claude…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 可攜式 Claude Code 設定：CLAUDE.md、settings、statusline、skills。
- [thurtado1993/claude-cabina](https://github.com/thurtado1993/claude-cabina) - Cabina: a live session dashboard for the Claude Code Desktop side panel。
- [tichara1/ai.claude-status-panel](https://github.com/tichara1/ai.claude-status-panel) - Mod pro Claude Code: panel nad promptem s kontextem, limity, cenou, stavem…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - 使用輕量級、無相依性的狀態列儀表板，在你的終端機中追蹤 Claude Code 上下文使用量、工作階段成本和速率限制重設.
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用の mod 集 (goal-orchestrator: /goal をタスク分解して SubAgent に委譲させる)。
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Real-time cost tracking and session monitoring statusline for Claude Code。
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Cordis / DeepSeek Harness 外掛程式——代理程式會在內嵌對話卡片中向人類索取祕密，且始終只會收到具工作階段範圍的不可見…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - 三列式 Claude Code 狀態列：內容深度、跨工作階段速率限制、每個儲存庫的 git 狀態與 worktrees。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - 適用於 Claude Code Agents 的主動式 AI 記憶與速率限制監控器。
- [zerofaultlabs/claude-statusline](https://github.com/zerofaultlabs/claude-statusline) - 一個 Claude Code 狀態列：一眼查看上下文使用量、速率限制、成本和快取命中。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks、subagents 和 statuslines：開源集合與工具，按類型分類，並各自附有安全分級。English / 中文.
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Claude Code 狀態列 — Claude/Codex 使用量儀表會在閒置時持續即時更新，顯示內容百分比與進行中的任務。單一安裝指令碼.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code statusline showing real-time token usage and estimated energy…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 的模組：以函式鉤子為基礎打造的窗格、頻帶與夥伴。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的 Claude Code 工作階段之間傳遞任務。將變更交給負責某個儲存庫的工作階段.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 這是一個用於控制 MODS 的 MCP 伺服器。MODS 是一款適用於跨平台 Fablabs 的模組化工具，包含 CAD/CAM 與機器控制工具.
- [pedrotspinola/lps-statusline](https://github.com/pedrotspinola/lps-statusline) - 自訂 Claude Code 狀態列：模型 + 努力程度、原生使用額度、git 資訊、上下文視窗、Gruvbox 主題。
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用於翻譯 CK3 模組的 Codex 與 Claude Code 技能，搭配本機 LLM。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code 的開源模組及其他擴充功能。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你反覆要求 Claude Code 執行的內容，並將其轉換為 mod。另附 8 個範例 mod 和一間虛擬辦公室.

</details>

<a id="dsh-cordis"></a>

## DSH 與 Cordis 外掛生態系

DeepSeek Harness 與 Cordis 從不同方向抵達同一個位置：對它們來說，外掛就是模組機制，因此那裡的外掛就等同於這裡的模組。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74280 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74280**  |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100394 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

🎨 最佳 DeepSeek Harness 設計外掛。開源的 Claude Design 替代方案。🖥️ 本機優先的桌面應用程式。🖼️ 您的編碼代理人成為設計引擎：原型、登陸頁面、儀表板、投影片、圖片與影片——真實檔案，支援 HTML/PDF/PPTX/MP4 匯出。🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode，以及透過 BYOK 支援的 20 多個 CLI。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **100394** |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81639 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **81639**  |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐70094 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **70094**  |
| Last push    | 2026-10-10 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35760**  |
| Last push    | 2026-10-10 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30358 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30358**  |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25470 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Summary

Distilly——將他們的思考方式提煉成適用於任何代理人或機器人的可重複使用技能。前身為 Colleague Skill（原同事 Skill）。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Python                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25470**  |
| Last push    | 2026-09-22 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9112 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **9112**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8594 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) Web 外掛聚合生態 · 萬物皆外掛，透過創意工坊分發｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8594**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4266 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 官方首推的 TUI 外掛——高效能、低負載、可愛像素鯨魚、流暢滑鼠互動。透過 npm 一鍵安裝。／DSH 官方首推的 TUI 外掛，高效能低佔用，可愛像素鯨魚，流暢滑鼠互動，npm 一鍵安裝

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4266**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3162 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Tauri 桌面版｜仅 8mb 安装程式，无需设定环境，预设插件，Windows / macOS / Linux。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3162**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1583 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

AI 程式設計代理的執行前防護器。在工具呼叫執行前，阻擋破壞性的 Git 和檔案系統命令，以及常見的敏感檔案存取嘗試。支援 Amp Code、Antigravity CLI、Claude Code、Codex、Cursor、DeepSeek Harness、Devin CLI、GitHub Copilot CLI、Grok Build、Hermes Agent、Kimi Code、OpenClaw、OpenCode 和 Pi。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1583**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1167 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Memory for Claude Code, Codex, Cursor and 38 more coding agents, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Go                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1167**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1139 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Go                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1139**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1007 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The most comprehensive DeepSeek Harness plugin market — refreshed daily, sourced across the Internet, reviewed before publishing.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1007**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐702 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (dsh) Windows 桌面客户端－内建 Node.js + dsh CLI，一键启动

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **702**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **593**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

非官方 DSH（DeepSeek Harness）外掛：將 chat.deepseek.com 網頁模型作為 LLM provider 使用——瀏覽器登入擷取、PoW 求解、SSE 串流、基於提示的工具呼叫。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **247**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

原生 DeepSeek Harness (DSH) 插件，整合 TypeSafe Jev 或類似 luna 的 Decision api，作為代理選擇、監督、修正與核准的 System One 決策層。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **203**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 插件，用于可预览的跨预设会话迁移。固定架构的交接可保留状态、来源模型意图及未解析的图片；原始会话保持不变。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **165**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐130 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

安裝即自帶 mattpocock/skills v1.3.1 的 27 個工程與效率技能，無需手動安裝技能。400 億 token 打造本插件，在原始技能之上提供 10 倍的開發效率，也能幫助新手更快上手該技能套件。全力支援 GitHub issue；Markdown 為預覽版；GitLab 暫不支援。感謝您的使用和支援💗

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
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐127 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 的 Claude Code 桌面主題｜為 DeepSeek Harness 網頁 GUI 打造的 Claude Code 桌面主題

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **127**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>動畫錄影</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐87 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

You.com 用於 web search、content extraction、research、finance 與 integration discovery 的技能與插件，協助 AI agents 以最新 web context 進行建構。

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
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐85 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

StudyHub：一個 DeepSeek Harness (DSH) 外掛，將你自己的資料轉換成題目與間隔複習 · 將自己的資料變成題目與間隔複習的 DSH 學習外掛

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **85**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

dsh-sieve：DeepSeek Harness (DSH) 的上下文工程与 token 最佳化插件 — 工具输出筛选、上下文剪枝、渐进式技能揭露。离线重播的载荷缩小 36%。DSH 上下文管理与 token 最佳化节省插件。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **72**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

自動分類、收錄和驗證 DeepSeek-Harness 社群外掛的市場。自動分類、整理並驗證 DeepSeek-Harness 社群外掛市場。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **69**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐57 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Summary

持續更新的 DeepSeek Harness 外掛目錄 — 每小時更新，每日進行相容性測試，內建應用程式內外掛商店與腳手架。DSH 外掛活目錄：每小時更新，每日進行相容性實測，內建外掛商店與腳手架。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | HTML                                                |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **57**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐27 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

NekroNXT：基于 DeepSeek Harness（DSH）的多平台群聊智能体系统｜由 DSH 驱动的多平台群聊智能体系统

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **27**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zp-home/dsh-recommend">zp-home/dsh-recommend</a></b> · ⭐22 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 外掛生態透明排行與推薦：每日自動抓取 dsh-plugin 主題 + 公開評分模型 + 排行／推薦外掛與靜態站

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **22**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `deepseek-harness` · `dsh-plugin` · `plugin` · `rankings` · `recommendations`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zp-home--dsh-recommend/fbc10141cf0df5b3.png" width="100%" alt="zp-home/dsh-recommend screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-superpower">Wenaixi/dsh-superpower</a></b> · ⭐21 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 插件：15 个 obra/superpowers 工程纪律技能，双语描述，每项技能可独立切换｜DeepSeek Harness 插件：15 个 obra/superpowers 工程纪律技能，技能描述中英双语自由切换，每一个技能本身自由开关

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **21**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `brainstorming` · `chinese` · `code-review` · `cordis` · `debugging` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-superpower/72fd369dacf071c0.png" width="100%" alt="Wenaixi/dsh-superpower screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-mcp-manager-ui">Imzl-zl/dsh-mcp-manager-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Web 的 MCP 伺服器管理 UI——浮動面板、JSON 匯入，以及由 profile 支援的持久化儲存。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-mcp-manager-ui/344d069db6cf421d.png" width="100%" alt="Imzl-zl/dsh-mcp-manager-ui screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/pptwise">liustack/pptwise</a></b> · ⭐19 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

真正的 PowerPoint，不是 HTML。告訴 AI 要涵蓋哪些內容，pptwise 就會在你的電腦上建立可編輯的簡報。Agent skill + DSH plugin，不需帳戶，也不需要 API key 即可轉譯。| 真正的 PPT，不是 HTML。跟 AI 說要講什麼，pptwise 在你自己電腦上做出一份能改的 PPT。Agent skill + DSH 插件，不用註冊，渲染不用 API key。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **19**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `agent-skill` · `agent-skills` · `ai-agent` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deck-generation`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--pptwise/e6f193d6fc2ea355.png" width="100%" alt="liustack/pptwise screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-ponytail">Wenaixi/dsh-ponytail</a></b> · ⭐18 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 插件：DietrichGebert/ponytail 懒人 senior 模式与七阶梯子完美移植，6 个技能描述双语自由切换，各个技能自由开关，零 tool 注册，全场景零缓存破坏

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **18**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-skills` · `ai-agents` · `claude-code` · `code-review` · `cordis` · `cursor` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-ponytail/ffd031e53f39269a.png" width="100%" alt="Wenaixi/dsh-ponytail screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KannaKuron/dsh-better-workspace">KannaKuron/dsh-better-workspace</a></b> · ⭐17 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 网页插件：侧边栏的阶层式工作区树状结构 — 标题中包含 / 的项目会归入虚拟资料夹；新增工作区流程加入父群组弹出视窗

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **17**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `sidebar` · `tree` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kannakuron--dsh-better-workspace/83cddff440dfe49a.png" width="100%" alt="KannaKuron/dsh-better-workspace screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 63</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - 為包含 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 外掛程式市場 / DSH Plugin Marketplace：在 DeepSeek Harness Web GUI 中一鍵瀏覽、安裝與更新全部…
- [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) - Remote-work assistant for DeepSeek Harness (DSH): connect SSH。
- [morluto/flameox](https://github.com/morluto/flameox) - Runtime evidence that helps agents trace, profile, and burn down hotspots in…
- [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) - DSH plugin - framework upgrade safety &amp; plugin gating: contract pre-check…
- [arcships/rutis](https://github.com/arcships/rutis) - 用於持續執行程式的外掛執行階段 — Rust core、TypeScript 與 Python 外掛，跨程序與機器.
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 外掛聚合社群 — 自動同步 dsh-plugin 生態系 · 精選目錄 · 每 4 小時自動維護 |…
- [mrRisega/dsh-remote](https://github.com/mrRisega/dsh-remote) - 公网远程控制 DeepSeek Harness。
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool。
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 外掛精選目錄——14 類 280+ 個社群外掛，涵蓋 MCP / Skill / TUI / 多 Agent /…
- [Cerbur/clutch-dsh](https://github.com/Cerbur/clutch-dsh) - Open-source DSH plugins for DeepSeek Harness：Git Worktree session…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin: Git Bash shell for all agent modes on Windows。
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness 的 Zotero 工具組；將你的 Zotero 書庫轉化為供代理使用的證據庫.
- [maxwell-feng/dsh-tinyfish-search](https://github.com/maxwell-feng/dsh-tinyfish-search) - TinyFish-backed web search provider for DeepSeek Harness (ctx.web) — 将内置…
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - DeepSeek Harness 的社群 GitHub 動作 — AI 程式碼審查 · CI 診斷 · 自動修復 · Issue → PR。
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 給中文網文作者的本地寫作工作台。
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - 社群精选的 DeepSeek Harness (dsh) 插件、工具、技能与学习资源。可搜寻的双语目录｜DeepSeek 插件、工具与技能精选。
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness。
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [miuzel/dsh-graph](https://github.com/miuzel/dsh-graph) - 把工作组织成目标看板的 DeepSeek Harness (dsh) 插件：目标 / 判据 / 上下文卡片 / 执行 attempt…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 將本機 WorkBuddy 桌面端已登入的模型（DeepSeek／GLM／Kimi／MiniMax 等）變成本地的 OpenAI 與 Anthropic…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - DeepSeek Harness plugins 的隔離安裝與冒煙測試驅動：將 repo 或 npm package 安裝到一次性的 DSH_HOME…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · DeepSeek Harness 功能坞插件：一张面板统一注册／开关所有小功能——用量记账（自订单价·分时价）、模型设定与余额、19…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 插件的常時相容性測試：精確版本、隔離 runners，以及可修復的上游問題.
- [gezi-wen/sage-mem](https://github.com/gezi-wen/sage-mem) - File-based cross-session memory for DeepSeek Harness (DSH) — every memory is a…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeekBot：开源的 GrokBot 替代品，基于 DeepSeek Harness (DSH) 构建.
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - The bilingual, source-backed registry and installer for the DeepSeek Harness…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 插件的 X 光：宣告的能力與實際行為。註冊表 + 靜態掃描器 + 徽章.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness 主机插件，将专案文件与长期记忆以纯 Markdown 形式储存在专用的 Obsidian vault 中.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）。
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Podman-backed execution for DeepSeek Harness (dsh)。
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Local-first voice conversations for DSH.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH 外掛：IDE 級 Git 工具視窗，作為原生 dsh-better-sidebar 分頁——分支樹、提交圖、變更、提交詳情、JetBrains…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC 模式基础上的创造模式:DSH 插件,合成 Code Mode 工具编排 + 自引用 Cordis 工具与 preset 创作指导,物化为…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - DeepSeek Harness 的工程工作流程外掛程式：工作階段、驗證記錄、提交檢查，以及技能和規則管理.
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH 角色扮演插件：角色卡（系统提示词注入 + 用户提示词改写）、可分享的单文件卡包、复刻原版 UI 的角色页签与首轮选角 chip。
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) 外掛程式的零相依性驗證標準——靜態結構閘門 (R)、cordis 合約檢查 (K)、沙箱冒煙測試…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness 外掛市場 - 瀏覽、搜尋與安裝 dsh-plugin 主題外掛（dsh 外掛市場：瀏覽／搜尋／安裝外掛）。
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode — 讓 OpenCode Zen + Go 免費方案模型持續運作的 DSH…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness 的第三方外掛市集與受防護生命週期管理器.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人為本且可擴充的桌面工作台：對話、筆記、表格、檔案集中於同一個工作台；自行建立伺服器即可啟用多人即時協作.
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh daemon：將 DeepSeek Harness 網頁伺服器。
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 輸入體驗插件：傳送/換行鍵位切換、右鍵選單、面板捲動與尺寸記憶、OpenCode 請求標頭自動注入。
- [grloper/dsh-claude-oauth](https://github.com/grloper/dsh-claude-oauth) - Claude Pro/Max OAuth model provider for DeepSeek Harness with Google/Gmail…
- [iasiv5/dsh-skip-browser-auth](https://github.com/iasiv5/dsh-skip-browser-auth) - DSH 插件：（Web Profile 专用）自动跳过 BrowserAuth，访问 Web 地址即可直接使用，无需每次复制启动 URL 中的随机 Token…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - 為 DeepSeek Harness 桌面版提供「限網段 + 可選數字密碼」的遠端存取入口。
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 外掛程式：將 Windows 沙盒 ACL 設定失敗。
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 讓無法歸屬的空模型嘗試可重新嘗試，適用於唯一能判斷的那個接縫（deepseek-harness 討論串 #8321 與 #9352）.
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - 具備由 Verus 驗證的生命週期核心與 Cordis 相容性轉接器的 Rust 外掛程式執行階段.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 外掛商城 - 基於 GitHub topic:dsh-plugin 自動發現與每小時定時同步。

</details>

<a id="writing"></a>

## 文章、討論與影片

關於模組功能的文章、討論與影片。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
| First listed | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
| TypeScript | 396  | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                          |
| JavaScript | 87   | `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                  |
| Python     | 43   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 16   | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7    | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2    | `rainyfei/claude-statusline-win`, `YangShen-SWE/dsh-plugin-simple-pet`                                        |
| Swift      | 2    | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1    | `reporails/arcade`                                                                                            |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

歡迎提供修正，這是改善此清單最快的方式。如果某個項目被錯誤分類、評等有誤，或某個專案因名稱衝突而被錯誤排除，請建立 issue 或提交 pull request——最後一類是自動篩選最可能出錯的地方。

---

<sub>獨立的社群專案。與 Anthropic 無關聯，也未獲其背書或審查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商標。產品行為可能在未通知的情況下變更；任何關鍵內容都請以官方文件為準。資產仍歸其上游專案所有，僅在授權允許的情況下重製。</sub>

<sub>Last updated · 2026-10-11T05:58:46+08:00</sub>
