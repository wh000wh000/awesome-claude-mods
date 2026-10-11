<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="超讚的 Claude 模組">
</p>

<h1 align="center">超讚的 Claude 模組</h1>

<p align="center"><b>依證據分級的 Claude Code 模組、外掛，以及它們改變的更深層行為索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-592-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <b>繁體中文</b> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **即時索引** · 上次同步: `2026-10-11T12:27:08+08:00` (UTC+8)
> · 條目: **592** · 最新更新新增項目: **0** · 實作語言: **13**

<sub>以下每個條目都經過自動收集、篩選與再次核查。這裡沒有任何付費置入。</sub>

<a id="featured"></a>

## 當下精選

<sub>每個分類選出一個項目，依證據等級和星標排序，並在每次更新時重新計算。這是排名，不代表背書；每個精選項目都會連結至下方的完整卡片。優先選擇發布了截圖或錄影的專案，讓這個橫列保持視覺化。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9469 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2533 · Python · 👁️ observed</sub>
<sub>尋找幽靈 token。修復它們。在壓縮過程中存活。避免上下文品質衰退。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74299 · TypeScript · 👁️ observed</sub>
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
- [模組：使用模組功能建立](#模組使用模組功能建立) — **470**
- [DSH 與 Cordis 外掛生態系](#dsh-與-cordis-外掛生態系) — **95**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150091 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **150091** |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9469 · TypeScript · ✅ official · 1 天</summary>

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
| Stars        | **9469**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8246 · Python · ✅ official · 1 天</summary>

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
| Stars        | **8246**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6337 · Python · ✅ official · 241 天</summary>

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
| Stars        | **6337**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 1 天</summary>

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
| Stars        | **1798**   |
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
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Cross-session usage & cost observatory for the DeepSeek Harness web profile — trend/heatmap dashboards, per-model peak-hour pricing (CNY/USD), official DeepSeek balance with spend reconciliation.

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `billing` · `cordis` · `cost` · `cost-estimation` · `dashboard` · `deepseek` · `deepseek-harness` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/enc-hanted--dsh-pulse/4a81f8e7c5f01f18.png" width="100%" alt="Enc-hanted/dsh-pulse screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2533 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

尋找幽靈 token。修復它們。在壓縮過程中存活。避免上下文品質衰退。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | Python                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2533**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐474 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **474**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐182 · TypeScript · 👁️ observed · 1 天</summary>

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
| Stars        | **182**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐119 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stars        | **119**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐110 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code 模組：為每個提示選擇推理力度，顯示提示快取和上下文，並可一鍵交接或壓縮

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
| Stars        | **110**    |
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

適用於網頁的代理原生 QA CLI。具確定性，無需撰寫測試，也不需要 LLM。

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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐89 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **89**     |
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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐63 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stars        | **63**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐58 · Shell · 👁️ observed · 4 天</summary>

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
| Stars        | **58**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

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
| Stars        | **46**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>動畫錄影 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">開啟影片</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

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

為 Claude Code 帶來全新體驗：即時駕駛艙窗格、可分享的主題，以及會將 Claude 正在執行的動作演繹出來的像素寵物

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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

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
| Stars        | **8**      |
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
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and cost, work streams, and a markdown reader for .planning. Read-only.

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/6df9cbfbbf321de0.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/3774c05315c85992.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 436</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - 可與 Claude Code 搭配使用的 100 多個 mods 集合.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其建置工具：先是 builder skill，接著是 mods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天執行的 Claude Code harness，自第一天起便以此名稱發布，如今與 ucsandman/Agnostic-AI 使用相同的儲存庫：防護…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 使用 Claude Mods 為 Claude Code 換屋頂：不修改二進位檔，將系統提示與英文提醒替換成你自己的文字（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四個 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 和 Collision Guard。
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code 模組：把代理程式的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - 在 Claude 讀取前修正並翻譯你的提示詞的 Claude Code mods。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的側邊窗格：工作階段執行的子代理程式、各自正在做的事、其權杖，以及只需點擊即可查看的對話.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 來自 Nekyia Labs 的 Claude Code mods 與技能，由生活在持久化家園中的 AI 建置並日常使用。
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Claude Code 的驾驶舱：就在提示词上方显示即时计划列、子智能体列、带重置倒数的使用限制、模型路由与迷你桌宠。CLI 与 Desktop.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 關於 Claude Code 模組、其運作方式、建立方式，以及安裝前檢查方法的附來源 Obsidian 知識庫.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教導 Claude Code agents 建構 Claude Mods（function-hook plugins）的 Skill，附 starter…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 用於 Claude Code 的 Claude Mods（function-hooks plugins）.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社群 Claude mods、插件與技能，可從單一市場安裝。
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane 模組展示館：經過檢查並置頂的 Claude Code 模組.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 供使用對話式代理的人類使用的決策佇列 CLI/TUI。代理張貼問題，人類從單一收件匣回答.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE 面板 mod：代理看板、檔案樹和 HWP/PDF 檢視器、系統狀態、Claude/Codex/Antigravity…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - 適用於 Claude Code 的浮動狀態卡——模型、上下文、速率限制、費用、分支——另附可由任何腳本或 mod 提供資料的進度 API.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code 模組：在你分享螢幕時，screen-guard 會遮蔽名稱與機密；cache-panel 會在提示快取即將失效前提醒你.
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions。解鎖 Claude 的完整威力.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod（外掛），新增含有 Activity、Files、Agents、Context 和 MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - 適用於 Claude Code 的面板、防護措施與生活品質模組：內容、使用量、即時活動、通知、安全規則、提示教練、命令中心.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示框上方的兩個 Claude Code 模組：內容視窗量表、5 小時限制、提示時鐘和工作階段費用。
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - 你的計畫，會自行監看。讓 Claude Code 和任何 MCP 主機即時維護的本機桌面路線圖樹。純 JSON，無雲端.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 讀取 Claude Code 命名的 markdown 檔案，並在工作階段旁呈現；指向任何區塊即可讓 Claude 編輯它。一個 Claude Code 模組.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的語音協作者。與由 ElevenLabs conversational AI 驅動的 3D 狼人討論事情；當你同意後，它會將提示傳送給…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code 模組：typing-speed，具備每次提示統計的即時打字速度計。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code 的煙火：每次按鍵、工具呼叫、提交和通過的測試，都會在提示上方化為盲文煙火升起。Claude Code 模組.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 探索 Claude Code mods、外掛和擴充功能，包含動畫示範、分類清單和直接原始碼連結。由 FindMods.dev 驅動.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code 模組：在逐字稿中內嵌繪製 mermaid 圖表。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code mods（function-hook 外掛程式）：session-switcher 等。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在提示上方顯示貼上的圖片縮圖，適用於任何終端機。
- [joonhyukyim/redpen](https://github.com/joonhyukyim/redpen) - Redpen is a Claude Code mod for reviewing what Claude changed, line by line, in…
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
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code mod that lets Claude log unfinished work to Docs/todos.md, with a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 模組：Clawd，一個迷你的像素吉祥物，會演示 Claude 正在做什麼。
- [reporails/arcade](https://github.com/reporails/arcade) - 作為 Claude Code mods 的經典桌面遊戲，可在 Claude 工作時於窗格中遊玩。由 Reporails 製作.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精選的 Claude Code 模組清單，可作為外掛程式市集安裝：主題、面板、狀態列、肖像.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 讓代理保持可靠的 Claude Code mods——守護範圍、驗證部署，並在提示上方繪製工作階段的 function hooks.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - 我的 Claude Code mods 集合，每個目錄一個 mod。
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - 五個免費的 Claude Code mods：Simple Mode、Usage Tally、Context Handoff、Inbox Alerts 和…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：內容列、代理面板、PDPA 模糊處理。
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - 剛出廠。Claude Code 模組：要求製作迷因，同時繼續工作。草稿會在側邊面板中產生；挑選、混搭、核准並發布到 Slack.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code 模組：提示快取列、後續步驟、快速按鈕和修改重播 — 可從市集安裝。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 一個 Claude Code 模組，在提示上方的列中繪製你的使用量限制和支出.
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - skill-router 模組：Jev 會挑選並載入每個提示所需的技能.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code mod 的應用程式商店，位於 Claude Code 內：輸入 /mods 即可瀏覽、搜尋並安裝 2,700 個 mod，或要求…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（市集 herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code 模組：規劃進度列、記錄 Claude 留在執行中的項目，以及對工具輸出進行權杖遮罩。
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six Claude Code mods: plan limits and context above the prompt, an allowlist…
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
- [AdamCaviness/prompt-marks](https://github.com/AdamCaviness/prompt-marks) - Claude Code mod: marks your prompts in the transcript and jumps between them。
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - 在 Claude Code Desktop 中提供主題化回覆、全寬圖表，以及一眼即可掌握的內容與限制.
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Agent 撰寫 Java 時，違反阿里 Java 規約（p3c）的程式碼無法寫入磁碟.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code 的即時成本、token 與上下文使用量側邊欄：一個在工作階段內顯示每回合成本、快取命中率、消耗速率及 30 天支出的 mod.
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code mod: a backlog of the follow-ups Claude suggests across every…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - 適用於 Claude Code 的 Counter-Strike 1.6 無線電通話——部署時顯示「Fire in the…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internet radio inside Claude Code: a cliamp sidebar, mini player, favorites…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph：用於設計和執行代理圖（軟體工廠）的 Claude Code mod。
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Herdr 設定 + 用於產品開發工作的 Claude Code mods。
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS 的缺口儀表板，適用於 Claude Code：使用量限制、開啟的工作階段、任務進度、提示快取倒數和待辦事項——由五個 Claude Code…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude 正在烹調。和你的 squad 聊天。朋友在線上，就在你的 Claude Code 工作階段旁邊。零 tokens，零洩漏給 Claude.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Claude Code 模組：在 Claude 工作時，於閒置遊戲中捕捉像素藝術 Modsters.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每個 Claude Code agent 在其 context 中有哪些檔案，以及各自的比例.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 保持冷靜。為您的 Claude Code 日子提供的溫度計：根據磁碟上現有的文字記錄，每小時評分 0 到 100，並在您精疲力竭前觸發十分鐘休息的外掛.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 適用於 Terminal 與桌面應用程式的小型 Claude Code mods。
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Collection of Claude Code mods, each in its own repo: usage-meter…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod: a progress pane for tasks, subagents, workflow runs, the goal…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod: a clickable, timestamped table of contents of the whole…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod: plan rate limits, context fill, session cost and per-task…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI skill + mod，可在代理回覆中加入西班牙文單字。
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Claude Mods。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 一個將其重新設計為《疑犯追蹤》中的 The Machine 的 Claude Code mod.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Claude Code 模組：在適當時機壓縮（提交後、測試通過後、提示快取即將過期前），或在 Claude 要求時壓縮。
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Claude Code 的像素藝術 Naruto 夥伴：20 名忍者、60 種忍術，在 Claude 工作時執行。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 的開源 mods：窗格、狀態列、通知、工具防護和斜線指令.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 一個 Claude Code mod：每個子代理一個窗格，顯示其接觸的檔案，以及工作階段的使用量和成本.
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Claude Code mod、外掛、技能、代理、hooks 與 MCP 伺服器的社群目錄。每個項目都連結至其來源.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod：工作階段狀態、即時 Spec Kit 進度與用量視窗治理。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 將內容視窗作為提示上方的一列，採用 Claude Code 繪製自身量表的方式呈現.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - 讓 Claude Code 終端機 UI 看起來像 Claude 桌面應用程式的 Claude Code 外掛程式（模組）：提示氣泡、Markdown…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在背景執行的內容：子代理、Codex 工作、shell、監控器、cron 工作與工作流程.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - A free, open-source plugin for Claude Code.
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - 個人 Claude Code mods：otto-hud，具備內容天氣和提示詞上方帳戶限制資訊的章魚 Otto.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 一個 Claude Mod，在逐字稿旁的面板中顯示工作階段的 GitHub pull requests：將描述引用到提示框中，查看檢查和審查狀態。
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools：用於偵錯 Claude Code 工具呼叫的偵錯器.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文件查證器、程式碼稽核器、錯誤記憶記錄、mod 等.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 好幫手外掛：位於提示詞上方、會記住你的規則並標示 Claude 捷徑的 ASCII 夥伴。
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - 適用於每個代理工具可見性的 Claude Code 插件——依照每個迴圈隱藏並拒絕子代理、技能、MCP 與內建工具。
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods：Claude Code 的安全層 —— 秘密資訊遮蔽、不受信任內容通知、MCP 工具投毒防護、a2a 防火牆、SAST…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Claude Code mods 集合.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin 與 mod：一個 AI-native SDLC。
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - 精彩的 Claude Code 模組合集 | Claude Code 模組合集.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 外掛程式（模組）：在多個 Claude 帳戶之間切換、在狀態橫幅中查看使用量限制，並在終端機面板中管理代理程式、工作樹、檢查點與差異。
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 經過測試、可用單一指令安裝的 Claude Code 模組：YOLO 模式的防護機制、即時成本與內容、面板、寵物等。另附精選的最佳社群模組清單.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一個 Claude Code mod，可依要求用本機開源 Kokoro TTS 聲音朗讀 Claude 的回覆與你的提示.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Spank Claude when it messes up — a stress-relief mod for Claude Code: cartoon…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - 讓你的 Claude Code 用量提升至最多兩倍。這是一個會為每個提示詞與每個子代理程式選擇適當推理努力程度的外掛.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用於即時窗格、成本感知模型路由和安全防護的小型外掛程式。用一個命令從 marketplace 安裝.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 與 plugin：用量監視器、token 追蹤器與狀態列.
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Three free Claude Code mods: hide .env values from tool results, watch a remote…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods。touch-map：以樹狀圖和活動地圖查看 Claude 列出、讀取、編輯或建立了哪些檔案.
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - 一個 Claude Code 模組，以簡明英文摘要你尚未閱讀的代理程式訊息。執行 /catchup、輸入 &#x27;brief me&#x27;，或按下按鈕.
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mods for Claude Code: live panes, bands and hooks. A plugin marketplace.
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [0xnicholasy/claude-mod-collapse-tools](https://github.com/0xnicholasy/claude-mod-collapse-tools) - Claude Code mod: collapses every tool-call row in the transcript to one line;
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Claude Code plugin marketplace for 0xnicholasy。
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code mods + cheap-executor driver：一個 Claude 工作階段擔任主管，MiniMax Code…
- [AdamCaviness/cache-magic](https://github.com/AdamCaviness/cache-magic) - Claude Code mod that offers a flexible alternative to the built-in…
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示上方的動畫盲文貓。
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code 模組：透過子 Claude Code 將低成本工作分派給 GLM/Kimi，將關鍵工作保留在你的訂閱中。移植自 Maggy.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示上方的一隻像素貓，會執行 OmniDimension 語音代理程式測試通話。Claude Code 模組.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一個 Claude Code 模組，會選擇適當時機進行壓縮，以保持上下文視窗較小.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code 的 Claude 模組：token-meter（工作階段權杖、Claude 與本機 LLMs 的比較，搭配 Pac-Man 內容迷宮）。
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider 製作的 Claude Code 外掛程式市集。
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mods for Claude Code。
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - 每次程式碼變更後，LGTM Lines 飛船都會航行經過——一個 Claude Code mod。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 將你的 Claude 使用量限制呈現為動畫村民生命值卡片——一個 Claude Code mod。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 團隊的 Claude Code mods（ather marketplace）。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作時進行短訓練：每日目標、連勝、徽章與可選排行榜。一個 Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code 的用量看板：各模型花費（今日、本週、本月、全部時間）與每週上限預測.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - A Claude Code mod: live context-window breakdown above the prompt.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方顯示 Apple Music 與 Spotify，包含封面圖、控制項與 Up next…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - 五個用於同時執行多個工作階段的 Claude Code mods：fleet board、PR-to-production…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Claude Code mod pack from the Berko video: Mask, View, Guard, Saving, Chime +…
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Claude Code 模組：使用量列、聊天名單、/cube、/handoff、提示清理。
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 模組：快取時鐘、影響範圍、建議、工作清單、烤架。
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code 模組：Suggestion Spotlight 顯示 Claude 的下一個建議提示所指向的內容.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是給你的 Claude Code 的一隻貓頭鷹。
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 單行 Claude Code 頻帶（快取倒數、上下文、限制、下一項任務）加上七個社群模組，以單一外掛安裝，預設保持安靜.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - 原版 Doom 引擎搭配 Freedoom，可在 Claude Code 內遊玩。Mac Apple Silicon alpha.
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - 住在 Claude Code 內的 Tamagotchi：它會孵化、吃掉 Claude 寫的程式碼、留下 bugs，並成長為八種成體之一.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Claude Code 終端機對話中的書籤與 vim 風格標記：醒目顯示一行、標記它，再跳回該處.
- [delexw/codyssey](https://github.com/delexw/codyssey) - 將每個 Claude Code…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code mod：在終端機和桌面應用程式中顯示每個提示和回覆的時間。
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 以函式掛鉤形式撰寫的 Claude Code 模組，以及提供這些模組的市集。dash：工作階段在單一面板中的儀表板.
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code mods 和設計系統：crab-crew 與 Crab Crew 設計系統。
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - My Claude Code mods, shared as a plugin marketplace。
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - divramod 的 Claude Code 程式碼修改：Claude Code 介面的即時面板與調整。
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - 我在每台機器上都使用的 Claude Code 模組：savvy-progress、filetree、skins、blast-radius。
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code mod: after a guard blocks a tool call, it stops recognized detours…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code mod: one inbox for messages from teammates, named subagents and…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code mod: explains sandbox blocks and turns repeated blocks into…
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods。
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - 嘿，靜音了！拋開差異、剪掉即興，不再編輯、少點花費。
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude Code 模組：在 Desktop 應用程式和終端機中，將訂閱用量（5h / 7d）顯示為提示文字上方的橫條。
- [evasuka/work-meter](https://github.com/evasuka/work-meter) - Claude Code mod：在輸入框上方顯示工作進度與帳號額度剩餘。
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - 為 Claude Code 設計的動態模組：即時、響應式監視器，監看模型、努力程度、內容、使用量限制、任務進度、子代理程式與每個工作階段.
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace。
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - 提示詞上方的平行分支和 worktree 即時雷達：哪些可以乾淨合併、哪些有衝突、哪些是堆疊的、哪些仍由 Claude…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - 我的 Claude Code 模組。
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code 的 mods 和 skins：Claude 工作的即時進度列、易讀的深色主題與相配的 Windows Terminal…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Seven Claude Code mods: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - 在 Claude Code 回覆中的每個程式碼區塊上按 Ctrl+點擊即可複製連結。
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - jev 模組：適用於 Claude Code 的 $.jev，來自 TypeSafe Jev 的具型別判斷.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Claude Code mod：顯示 prompt 快取處於暖機或冷卻狀態的面板.
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - 適用於 Claude Code 的模組：hooks 外掛程式，例如 usage-meter。
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code 模組（函式掛鉤外掛程式），透過單一市集安裝.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code 的 Evangelion 風格側邊欄：上下文、配額、活動、PR、硬體、工作階段和 forge 面板。
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - 實用的 claude code mods。
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Claude-Code Plugin (Mod) 可讓你在模型工作時查看其正在做什麼.
- [hamTotk/better-rewind](https://github.com/hamTotk/better-rewind) - Claude Code mod: rewind or summarize from any prompt or AskUserQuestion answer。
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Claude Code 面板中的測試結果：來自 Claude 自身測試執行的失敗、其詳細資訊與執行歷史。
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模組：每個回答花費的時間、Claude 思考的時間，以及 tok/s，顯示在 Claude 桌面應用程式的回覆正下方.
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - 小型 Claude Code mods：內容和計畫使用量儀表、prompt-cache 測量器，以及一個供查看事項的窗格.
- [Jang-seungminn/usage-hud](https://github.com/Jang-seungminn/usage-hud) - Claude Code mod: usage HUD above the prompt with two animated ASCII dogs。
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - 存放我的 claude mods 的地方.
- [jemsley06/reels-while-you-wait](https://github.com/jemsley06/reels-while-you-wait) - Claude Code mod: Instagram Reels in a small Safari window while Claude works。
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
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Claude Code 的 mods 目錄。
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - 可在 Claude Code 工作時於其中遊玩的多人遊戲。
- [juampymdd/claude-code-model-picker](https://github.com/juampymdd/claude-code-model-picker) - Claude Code mod: pick the model and version for the next requests from a band…
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Claude Code mod：你離開時保持提示快取溫熱，並在提示會重新快取大型對話前先詢問.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的帶狀列中：演出 session、顯示正在執行的項目、context 和使用限制，並與你的 CI…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - 一個 Claude Code mod：在提示上方顯示速率限制額度、工作階段 Token 與成本。
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - 使用 VOICEVOX / Irodori-TTS 等朗讀 Claude Code 的回覆與通知的模組。
- [Kareem1809/chat-cigarette](https://github.com/Kareem1809/chat-cigarette) - 🚬 A Claude Code mod: a cigarette burns down with every message — when it。
- [kba977/claude-code-pomodoro](https://github.com/kba977/claude-code-pomodoro) - A pomodoro timer above the Claude Code prompt (Claude Code mod)。
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - 用於讀取並加入你的 Claude Code 工作階段之間對話的 Claude Mod（/crosstalk）。
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code mod: running subagents as pixel Claude mascots above the prompt。
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - 改善便利性／使用體驗的 Claude mods。
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - 用 haiku 壓縮冷掉的 claude code 工作階段——顯示你節省了什麼的一行快取列。
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 兩個 Claude Code mods：folio，聊天旁的檔案窗格；以及 tint，重新設計終端機工作階段並加入狀態列.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 的即時工作任務 HUD：Claude 工作時顯示於提示詞上方的橫條，一鍵即可開啟完整儀表板.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia)。
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 社群策劃的 Claude Code Mods 指南：使用案例、原始示範、相容性證據與安全性備註。English / 中文。非官方.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一個 Claude Code 模組，會在 iTerm2 分頁副標題中顯示 Claude 正在進行的工作，因此只要看一眼分頁列，就能知道哪個工作階段需要你的注意。
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Claude Code 模組：提醒主要工作階段委派工作給子代理程式，並在提示文字上方顯示主要內容與委派內容的權杖數.
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - 我的 claude mod 外掛個人收藏。
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel 的 Claude Code mods，集中於一個外掛市場（marcel-mods）。
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 一個 Claude Code mod，具備可切換的權限設定檔：安全基準、可開關的具名設定檔，其他所有操作仍會詢問.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code 的社群 mods：在 Claude Code 內執行的防護、窗格和指令。Marketplace：modhub。
- [mina-asham/claude-usage-stats](https://github.com/mina-asham/claude-usage-stats) - A Claude Code mod that shows your plan usage。
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code 的安靜側邊面板：此工作階段正在做什麼、它的計畫、代理，以及其他每個工作階段。
- [mmedum/spor](https://github.com/mmedum/spor) - 還原 Claude Code 摺疊的內容：Claude 讀取的檔案、執行的命令，以及每一輪所執行的工作。
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模組：透過在工作階段開始時設定 CLAUDE_CODE_ENABLE_TODO_TOOLS，為省略待辦工具的模型重新啟用它們.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模組：提示上方每個任務清單一行，顯示目前任務、進度列與計數。在終端機與桌面應用程式中外觀相同.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 內與 AI 玩 Connect Four（/connect-four）。
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Claude Code 的像素藝術金絲雀：當 Claude 不再遵循你的指示時，它會死亡，接著自動壓縮並復活。一個 Claude Code 模組.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模組：當另一個程式設計代理提交至你的儲存庫時，Claude 會透過差異與測試進行審查，而不是相信它的報告.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 適用於多個 AI 代理共用儲存庫的 Claude Code 模組：防止秘密值離開 .env、防止推送至公開遠端儲存庫，以及防止 git…
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Claude Code 的賽博霓虹網路廣播窗格——synthwave 旋鈕、目前播放、VU、本機 ffplay。
- [niksavis/handily](https://github.com/niksavis/handily) - 顯示你在任何追蹤器中的工作項目、任務與工作階段的 Claude Code Mod。Mod 只顯示並詢問；從不強制執行.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code 的 SQL 防護欄：在 Claude 透過 DB CLI（函式掛鉤／Mods）執行 DELETE、沒有 WHERE 的…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - 一個適用於 Claude Code、以 Windows 與 CJK 為優先的模組：在任何終端機中提供貼上影像與文字預覽、帶有 CJK…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Claude Code 的提示音：當 Claude 完成、需要你的輸入或遇到錯誤時播放聲音。十種原創音效、自訂檔案、鍵盤選擇器.
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods：影像縮圖與狀態列。
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 最佳的 Claude Code 模組，依它們能為您做的事排序。人工檢查，每個模組一行介紹.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Claude Code mod：在 Claude 桌面應用程式的窗格中查看代理看過的每張圖片與檔案（螢幕截圖、算繪結果、讀取內容）。
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - 一個攔截危險 shell 指令（rm -rf、git reset --hard、強制推送、遷移、全域安裝、curl | sh…）的 Claude Code…
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - 兩個適用於 Claude Code 的 Claude 模組：護欄。
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Claude Code 的 Lazy Panda Panel：不用抬爪也能檢閱文件.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Swear at Claude Code and a cartoon hand slaps back.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code mods: usage-both shows 5-hour and weekly usage above the prompt。
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod: clickable paths in replies — click a folder to open it in…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 桌面應用程式 Code 分頁的即時工作階段統計側邊窗格：上下文、成本、git 變更、回合統計、子代理程式、日誌.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - 適用於我的 Claude Desktop 設定的各種模組與技能。
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code 的模組：safety-guard 會封鎖破壞性指令與秘密檔案存取；notify-router…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods for Claude Code: function-hook plugins that run inside the session…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod：即時股票行情、/quote 面板、價格警示、市場帶，以及模型可呼叫的報價工具。
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod：在提示上方一列顯示 SSH 主機、RAM 與 5h/7d 用量限制。
- [Rinze-Smits/ifc-viewer-claude-mod](https://github.com/Rinze-Smits/ifc-viewer-claude-mod) - IFC Viewer mod for Claude Code。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：在 Claude 工作時做伏地挺身。無 tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커。
- [Rsclub22/claude-mods](https://github.com/Rsclub22/claude-mods)
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - A Claude Code mod that routes tasks to other AI models。
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Claude Code 的模組商店：從 GitHub 擷取模組、預覽模組並提供市集。
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 模組：將你在計畫模式中核准的計畫轉為提示上方的即時核取清單，隨著 Claude 完成每個步驟逐一勾選。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精選的 Claude Code 模組清單。每個項目都已複製，並使用 claude plugin validate 檢查，且標記其可接觸的內容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：輔助代理程式在 Haiku 上執行，大型檔案與日誌則由免費的 Gemini 模型摘要，而不是填滿 Claude 的內容.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 隨工作階段播放的 lo-fi 原聲帶：平靜、專注、流暢，另有通過與失敗測試的提示音。原創音樂.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 撰寫程式時學習：每當一輪操作變更程式碼後，提示上方會出現一個關於該確切變更的問題。依概念評分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 記錄 Claude 所做每次編輯的磁帶：重播每項變更自行輸入的過程、逐步檢視，並將任何檔案倒轉至任何步驟.
- [samaphp/session-links](https://github.com/samaphp/session-links) - 工作階段提及的每個連結，都集中顯示在提示上方的一列中。一個 Claude Code 程式碼修改.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code 函式掛鉤最小示範：提示上方的即時 token／成本面板、可點擊按鈕、獨立繪製的執行緒動畫，全程零 token。
- [shawnbotha/claude-mods](https://github.com/shawnbotha/claude-mods) - Different Claude mods。
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - ShellTime 製作的 Claude Code 模組（function-hook 外掛）。
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Claude Code mod for context, growth, quota, cache, native cost and agent…
- [skryvets/claude-status-bar-mod](https://github.com/skryvets/claude-status-bar-mod) - Claude Code 模組：在提示下方顯示彩色工作階段資訊，包括內容、模型、推理程度及帶有節奏資訊的速率限制列。
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code 的舒適 RPG HUD 修改（測試版，先推出桌面應用程式；計畫支援 CLI）：多職業 Clawd…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [Steady-Matter/spotter-pals](https://github.com/Steady-Matter/spotter-pals) - Spotter: a Claude Code mod with pixel Pals that hatch and grow as your helper…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 為 Claude Code 一鍵產生 commit 訊息，搭配跳舞的像素風 Malenia。
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude Code 模組。
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Personal Claude Code mods。
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code 模組 — marketplace sunkanxx-mods。
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Claude Code 模組：迷你列 HUD。
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Claude Code 的外掛程式。
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Claude Code 的模組：delete-guard（刪除專案資料夾外的檔案時需要核准）。
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Claude Code 模組：就在提示詞上方查看你的 Claude 計畫用量（工作階段與每週限制、重設倒數、內容）；可在終端機與桌面應用程式中運作.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code 模組：每個子代理程式的即時團隊面板（模型、努力程度、步驟、內容、成本、時間）、提示詞上方的工作列，以及 5 小時／每週計畫限制圓環.
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - 一個 Claude Code 模組，會為每種工作選擇模型和推理程度，並顯示這些選擇的成本。
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一個 Claude Code 模組，在窗格中顯示目前工作階段：每個提示詞、Claude 分階段為其完成的工作、每個子代理程式及其答案，以及提示詞的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一個 Claude Code mod 外掛市集：function-hooks 外掛，可在 Claude Code 內繪製 band、窗格和其他 UI.
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code mods on demand — a skill that reads your conversation and builds…
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code 模組：顯示工作階段子代理程式及其狀態的停駐窗格。
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Claude Code mod that writes your Claude usage limits to a file other tools can…
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Claude Code mod：一個追蹤你的子代理程式及其所使用檔案的樂隊與面板。
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Claude Code 模組的精選目錄，每個模組都附有可複製貼上的提示，能為你建置該模組.
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模組：適用於長時間執行任務的動畫進度列與完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 三個小型 Claude Code 模組：查看子代理程式何時完成、在 Claude 完成後佇列訊息，以及讓你最愛的技能保持一鍵可用.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 說出「我迷路了」，Claude 就會再次用日常用語解釋上一則回覆。Claude Code plugin.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作旁的窗格中向 Claude 提出旁支問題。主要對話永遠看不到它。運作方式類似桌面應用程式的 /btw.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Claude Code 模組市集，提供一步安裝及葡萄牙語影片指南。
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Claude Code 的速率限制倒數計時和消耗速率預測。
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - 適用於 Claude Code 的 Roblox Studio 安全層：RemoteEvent 稽核、復原、Team Create 保護，以及重播…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Claude Code 的小型生活品質模組。
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Claude Code 模組：stage-toons，在提示上方以像素藝術 Clawd 卡通顯示工作流程進度列。
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 用於 Claude Code 的 Mods。agent-crew：以即時 pixel crew 觀看你的 subagents 工作，包含…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - A live task board for Claude Code: plan before building, follow every task…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - 持續顯示於 Claude Code 提示文字上方的橫條：桌面與終端機上的內容填入量和速率限制視窗。
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - 個人 Claude Code 模組（外掛程式市集）。
- [zwbao/zebra-mod](https://github.com/zwbao/zebra-mod) - zebra-mod: a Claude Code mod that turns Claude Code into a rare-disease…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 由 Anthropic PBC（无关联关系）这支势不可挡的团队精心打造的顶级资源精选，献给最强大的智能体与无可争议的编码伴侣冠军 Claude Code.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 一款顯示正在發生什麼事的 Claude Code 外掛——內容使用量、作用中的工具、執行中的代理人，以及待辦事項進度。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 高度可自訂的精美 Claude Code CLI 狀態列，支援 powerline、主題等功能.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 系統提示的所有部分、27…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45 多項充分發揮 Claude Code 效用的秘訣，從基礎到進階——包括自訂狀態列指令碼，以及在容器中自行執行的 Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code／Codex 技能 — 產生小紅書輪播圖與微信 21:9+1:1 封面組合.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - 適用於 Claude Code 的精美 vim 風格 powerline。
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 在終端機窗格中檢視 coding agent 的 diff，並將逐行留言傳回 Claude Code、Codex、OpenCode 或 Pi.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 適用於 Claude Code 的完整狀態列外掛程式，提供內容使用量、API 速率限制與成本追蹤。
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code 与 Codex 本地 token 追踪 — 状态列（Codex 业界首创伪 statusline）、GitHub…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - 為 Claude Code 建立修改模組：攔截任何請求、修改任何回應、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - 適用於 Claude Code 的完整狀態列儀表板 — 工作階段資訊、配額列、代理追蹤器、MCP 健康狀態、訊息記錄等.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：追蹤你的 Claude Code 工作階段的碳足跡。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - 由 awesomejun 製作的 Claude Code 美觀狀態列。
- [amirfish1/claude-command-center](https://github.com/amirfish1/claude-command-center) - One local board for Claude Code, Codex, Cursor and 5 more coding agents.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公開的 Claude Code skills 與 mods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - 適用於 Claude Code 的 Skills、mods、subagents、hooks、slash commands 和…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免費 LLM APIs 與程式設計代理 — 每週自動更新並探測驗證兩次。免費方案、免卡試用、免費模型.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - 用於 Claude Code sessions 的終端機 statusline。
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 在你的終端機、Claude Code 和 Cursor CLI statusline，以及 MCP…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Local control plane for Claude Code on Windows and macOS: switch LLM gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 將程式碼代理變成鍵盤韌體專家的 Agent Skill。稽核 ZMK/QMK 鍵位圖、調整 home row mods、讓軌跡球具備圖層感知能力、透過 CI…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - 個人 Claude Code 設定版本，儲存於 ~/.claude — 代理、技能、hooks、設定與狀態列（參考用途，不是入門範本）。
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供禮拜時間、回曆日期、adhkar、每日 ayah、sunnah fasting、Ramadan、Jumu。
- [livlign/ccbit](https://github.com/livlign/ccbit) - 适用于 Claude Code 的会话感知状态列。一个颜文字脸孔会读取逐字稿，并在你的各个会话中叙述状态。一个 Go 二进位档，无 hooks，无常驻程式.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — 用于研究主题、可追溯知识卡片与可重複使用 AI 讨论的 DeepSeek Harness 插件.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Useful statusline for Claude Code that displays model, effort, context, cost…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - 适用于 .NET DDD/Clean Architecture 的可携式 Claude Code 工具包：严格的 TDD…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 適用於 Claude Code、pi 和 DeepSeek Harness 的外掛合集：狀態列 HUD、任務進度條、Tailscale 節點狀態等 · 適用於…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 可攜式的 Claude Code 全域設定：自訂技能、PreToolUse 鉤子與自訂狀態列。可在 Linux、macOS、WSL 上執行.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：整理過的 skills 與 mods，可在任何人的機器上運作.
- [34823/tg-pane](https://github.com/34823/tg-pane) - Claude Code 中的 Telegram：在面板中閱讀聊天與頻道，取得未讀貼文的 AI 摘要。無需 API key，無需機器人.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code 外掛程式與技能市集，用於促進 Hytale 遊戲模組的開發。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code 的權杖治理：由頂級模型負責指揮，執行交給足夠且最便宜的方式。路由核心、由 hook 強制執行的預算上限、遙測、附帶計畫配額的狀態列.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - 適用於 Claude Code 的分割窗格檢視器，運行於 Windows Terminal 和 tmux：以 Markdown…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - 適用於 Claude Code 的即時工作流程階段狀態列（Plan → Exec → Verify → Done），由模型自動更新。
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop Code 分頁的非官方模組——usage-pet：帶有 Clawd 的使用量橫幅，以及動畫像素寵物。淺色與深色、英文與中文.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media 修改版的儲存庫.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - 降低 Claude Code 與 Codex 的 Token 花費：將查詢和測試執行路由至更便宜的模型，將文件轉換為精簡…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Simple and useful status line setup for Claude Code。
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Claude Code 的用量限制警示：macOS 通知、應用程式內警告，以及工作階段（5h）與每週限制的狀態列百分比。
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - 適用於 Linux、WSL、Windows 和 macOS 的可設定 Claude Code 狀態列，包含提示計時、子代理列和終端機設定 UI.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - 適用於 Claude Code 的快速 Rust 狀態列 —— 優先處理負載、快取 git、約 10 毫秒的呈現時間。
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - 具備內容列、token 迷你圖與花費追蹤器的 Claude Code 狀態列。
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - 適用於 Claude Code 的即時用量儀表板——以 Catppuccin 膠囊樣式的側邊窗格顯示內容分解、快取命中、速率限制預測、費用與活動.
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code 的狀態列和權杖列：內容、5 小時及每週用量與節奏標記、活動、git 和成本.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - 在 macOS、Linux 和 Windows 上顯示 Claude Code 的重要狀態詳細資訊，包括模型、內容、限制、git 資訊與工作階段時間.
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - 適用於 Claude Code 的親切、隨心調整的狀態列——真彩色列、約 80 種佈景主題，以及透過單一 JSON 檔案進行的元素個別樣式設定。
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 多列 Claude Code 狀態列：花費、內容百分比、git 和目前使用中的帳戶 —— 具備自動更新的定價和內容視窗.
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - 適用於 claude code、包含實用資訊的狀態列。
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - 用於組織多公司 Claude Code 工作區的入門範本：已清理的 CLAUDE.md 範本、SessionStart…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 原生 agent 團隊。受控。嚴格的工作者限制、即時團隊可見性，以及 Claude Code 的可攜式設定.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code 的自訂狀態列——顯示用量百分比、內容大小、費用與計時器的內容列。
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - A clean, informative status line for Claude Code — shows project, git status…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - 搭載 baloo 的 Claude Code 外掛程式市集：技能、可根據專案決策驗證變更的代理、指南、檢查項目、輸出樣式與狀態列.
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Claude Code 狀態列：內容用量、5h/7d 配額列、重設時間、git 分支。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 專業級 Claude Code 狀態列：工作階段持續時間、使用 ECB 外匯的多幣別費用、每百萬 token 費率、支出上限。MIT、零金鑰、跨平台.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - 具備訂閱感知功能的 Claude Code 狀態列。
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - 一個 Claude Code 外掛程式：在 Mac 上以窗格顯示即時的 Claude Code 和 Codex 工作階段…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code 的豐富終端機狀態列 — Bun + TypeScript，無執行階段相依項.
- [eddywong888/claude-castle-mod](https://github.com/eddywong888/claude-castle-mod) - A Castlevania-style usage HUD mod for Claude Code: context blood meter…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Claude Code plugin，可在 transcript 中精美呈現 Mermaid diagrams：任何終端機中的彩色 Unicode…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - 適用於 Claude Code 的工具、技能與代理程式——首先提供顯示模型、分支、PR、內容大小、提示快取剩餘時間及費用的狀態列.
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Claude Code 全域設定：代理程式、技能、模組、設定。
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Claude Code 外掛：在頁尾右下角隨時查看剩餘的 Claude 5 小時用量限制——不再需要 /usage。
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code 的實際 DeepSeek API 花費：以 DeepSeek…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods para Claude Code y Claude Desktop en Windows con WSL: Docker y rendimiento…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code 狀態列與代理面板列。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 將 Claude 的待辦事項同步至 Fizzy.do，讓團隊即時掌握進度，將任務轉換為持久卡片，以提升協作效率並輕鬆追蹤進度.
- [J-J-E/claude-kanban](https://github.com/J-J-E/claude-kanban) - A markdown kanban board for Claude Code: cards are files, a board pane, and a…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I。
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - 為 Claude Code 顯示詳細且以顏色標示的狀態列，呈現上下文、git 狀態、費用與速率限制.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code 設定選單、狀態列與設定。
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - 在 Windows 上以語音與 Claude Code 對話：使用 codex app-server realtime 的模組與協助工具（ChatGPT 登入）。
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - 自訂 Claude Code 狀態列，包含內容視窗、API 使用量追蹤、git 狀態與工作階段成本。
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - 適用於 Claude Code 的快速 Rust 狀態列（讀取掛鉤 JSON，將指標記錄至 SQLite）。
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - 自製、無籠飼養的 claude 外掛程式、技能、模組及更多內容。
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 環境安裝程式：技能、狀態列、掛鉤、權限，以及可選的 Obsidian-vault MCP 伺服器（--vault_root）.
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - 用於理解 Claude 所做事情的 Claude Code 外掛程式與模組：易讀的回答格式與即時工作階段看板（市集：oshn）。
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - 從你的 macOS 選單列監控 Claude Code 狀態，透過即時指示器顯示作用中任務、待處理權限和經過時間.
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - 適用於 Claude Code 的彩色多列狀態列（配額列、內容與子代理面板）。
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - 用於 Windows (PowerShell) 的 Claude Code 狀態列：使用量列、帶有節奏警告的 5h/7d 重設倒數、自動換行。
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Claude Code plugins。Usage Bars 以三條對齊的長條，同時顯示你的工作階段與每週 rate limits，以及 context…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - 適用於 Claude Code 的 Bearings 和 Glossary mod。
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 自訂 Claude Code statusline（上游：kamranahmedse/claude-statusline）。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code 設定與模組，附有共用元件套件、遊樂場與 Storybook。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 可攜式 Claude Code 設定：CLAUDE.md、settings、statusline、skills。
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - 使用輕量級、無相依性的狀態列儀表板，在你的終端機中追蹤 Claude Code 上下文使用量、工作階段成本和速率限制重設.
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用的模組集合（goal-orchestrator：將 /goal 分解為任務並委派給 SubAgent）。
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code 的即時成本追蹤與工作階段監控狀態列。
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Cordis / DeepSeek Harness 外掛程式——代理程式會在內嵌對話卡片中向人類索取祕密，且始終只會收到具工作階段範圍的不可見…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - 三列式 Claude Code 狀態列：內容深度、跨工作階段速率限制、每個儲存庫的 git 狀態與 worktrees。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - 適用於 Claude Code Agents 的主動式 AI 記憶與速率限制監控器。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks、subagents 和 statuslines：開源集合與工具，按類型分類，並各自附有安全分級。English / 中文.
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Claude Code 狀態列 — Claude/Codex 使用量儀表會在閒置時持續即時更新，顯示內容百分比與進行中的任務。單一安裝指令碼.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - 適用於 Claude Code 狀態列的視覺化建構器。在瀏覽器中設計終端機底部的列，然後貼上一個指令即可安裝.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 顯示即時 token 使用量與預估能源消耗的 Claude Code 狀態列。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 的模組：以函式鉤子為基礎打造的窗格、頻帶與夥伴。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的 Claude Code 工作階段之間傳遞任務。將變更交給負責某個儲存庫的工作階段.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 這是一個用於控制 MODS 的 MCP 伺服器。MODS 是一款適用於跨平台 Fablabs 的模組化工具，包含 CAD/CAM 與機器控制工具.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用於翻譯 CK3 模組的 Codex 與 Claude Code 技能，搭配本機 LLM。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code 的開源模組及其他擴充功能。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你反覆要求 Claude Code 執行的內容，並將其轉換為 mod。另附 8 個範例 mod 和一間虛擬辦公室.

</details>

<a id="dsh-cordis"></a>

## DSH 與 Cordis 外掛生態系

DeepSeek Harness 與 Cordis 從不同方向抵達同一個位置：對它們來說，外掛就是模組機制，因此那裡的外掛就等同於這裡的模組。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74299 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74299**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100435 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **100435** |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81723 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **81723**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐76541 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **76541**  |
| Last push    | 2026-10-11 |
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
| Last push    | 2026-10-11 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30374 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **30374**  |
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
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25474 · Python · 🔎 inferred · 18 天</summary>

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
| Stars        | **25474**  |
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
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9115 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **9115**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8598 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **8598**   |
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
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐7124 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7124**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4270 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **4270**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3144 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **3144**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NanmiCoder/dsh-agent-teams">NanmiCoder/dsh-agent-teams</a></b> · ⭐2012 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 的 Agent Teams 多智能体协作插件，支持多个 AI Agent 组成团队，协同完成复杂任务，实现任务分配、并行执行、成员通信与团队协作。 AgentTeams plugin for DeepSeek Harness

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2012**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agentteams` · `deepseekharness` · `dsh` · `dsh-agent-teams` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nanmicoder--dsh-agent-teams/b3647beca323c018.png" width="100%" alt="NanmiCoder/dsh-agent-teams screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1969 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1969**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1780 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1780**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1394 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

AI 小说创作软件：把灵感、角色、世界观、大纲、章节写作、审稿和修稿组织成可控流程；提供 Windows/macOS 桌面版，支持本地和在线模型。AI Novel Writing Software: Organizes inspirations, characters, worldbuilding, outlines, chapter drafting, review, and revision into a controllable workflow. Features desktop apps for Windows/macOS, Ollama integration, and a DeepSeek Harness (DSH) plugin preview.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1394**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

適用於 Claude Code、Codex、Cursor 及另外 38 個程式設計代理的記憶體，從磁碟上已有的工作階段歷史建立。支援本機搜尋、MCP 和 hooks，無需 LLM，僅需一個 Go 二進位檔。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Go                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1169**   |
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
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐703 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **703**    |
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
<summary>🧵 <b><a href="https://github.com/text2future/flowix">text2future/flowix</a></b> · ⭐453 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **453**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-memory` · `claude-code` · `codex-cli` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `hermes-agent`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/9fc65a8848fe78ee.png" width="100%" alt="text2future/flowix screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/ea3f84c8693d4236.gif" width="100%" alt="text2future/flowix animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Mars-Sea/dsh-commandcode-provider">Mars-Sea/dsh-commandcode-provider</a></b> · ⭐377 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Command Code provider plugin for DeepSeek Harness (dsh). Adds Command Code model access, live model catalog, plan-aware model selection, reasoning effort, image input, web search, and multi-account support.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **377**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `command-code` · `commandcode` · `deepseek-harness` · `dsh` · `dsh-plugin` · `llm` · `llm-provider` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mars-sea--dsh-commandcode-provider/2f2256468a8af0b9.png" width="100%" alt="Mars-Sea/dsh-commandcode-provider screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Your Intelligence, Orchestrated. Every builder. Every team. Every agent. For Everyone.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Go                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **351**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **255**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐250 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **250**    |
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
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Bash, PowerShell 7, and Rust-based tools for dsh on Windows to cut token usage. / 为windows的dsh提供bash、powershell7及rust的高性能tools来减少token消耗

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐128 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **128**    |
| Last push    | 2026-10-11 |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐120 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

執行階段證據，協助代理追蹤、分析並消除應用程式與原生程式碼、GPU 核心和推論堆疊中的熱點。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Python                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **120**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐99 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 外掛——框架升級安全性與外掛閘門：契約預檢、回滾點、失敗時自動回滾、依據證據自動停用；另附多來源外掛市場。非官方。| DSH 外掛：框架升級安全性 + 外掛閘門——升級前契約預檢、回滾點、失敗自動回滾、有確實證據才自動停用；另附多來源外掛市場。非官方社群專案。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **99**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
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
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **74**     |
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
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐73 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

從公網遠端控制 DeepSeek Harness（dsh web）：安裝後即取得專屬加密網址，即使人在外面也能用手機遠端存取，無需位於同一區域網路／WiFi、無需內網穿透，可選擇自行建置服務。從任何地方遠端控制 DeepSeek Harness（dsh web）——加密公開 URL，無需區域網路。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **73**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-web` · `pwa`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://cdn.jsdelivr.net/gh/mrRisega/dsh-remote@main/image/phone-mirror.png" width="100%" alt="mrRisega/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐62 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

基于 Deepseek-Harness 核心底座打造的桌面版 Agent.继承底坐全部能力。并补全 IDE 相关功能。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **62**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Contexera/dsh-agent-team">Contexera/dsh-agent-team</a></b> · ⭐57 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

dsh-agent-team gives DeepSeek Harness agents that don't reset: durable Members with their own memory, notes, and skills across sessions, rollovers, and restarts. You set the direction; agents coordinate through Channels and Tasks.

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **57**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-orchestration` · `agent-team` · `ai-agents` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `multi-agent`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/contexera--dsh-agent-team/25f8cc5a2a3231a3.png" width="100%" alt="Contexera/dsh-agent-team screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 61</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI 程式設計代理的執行前防護器。在工具呼叫執行前，阻擋破壞性的 Git 和檔案系統命令，以及常見的敏感檔案存取嘗試.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - 為包含 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 外掛程式市場 / DSH Plugin Marketplace：在 DeepSeek Harness Web GUI 中一鍵瀏覽、安裝與更新全部…
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - 终末地官网风格的 DSH Web 主题：奶油纸底、墨黑文字、信号黄强调、全直角工业编辑风.
- [arcships/rutis](https://github.com/arcships/rutis) - 用於持續執行程式的外掛執行階段 — Rust core、TypeScript 與 Python 外掛，跨程序與機器.
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - 最佳 Roblox Luau 錯誤檢查器與 API 驗證器 2026 DevForum MCP 工具。
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 持續更新的 DeepSeek Harness 外掛目錄 — 每小時更新，每日進行相容性測試，內建應用程式內外掛商店與腳手架.
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana: DeepSeek Harness as a subagent for HanaAgent。
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - 面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 外掛精選目錄——14 類 280+ 個社群外掛，涵蓋 MCP / Skill / TUI / 多 Agent /…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness 的 Zotero 工具組；將你的 Zotero 書庫轉化為供代理使用的證據庫.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH 外掛：適用於 Windows 上所有代理模式的 Git Bash shell（取代 pwsh executor）。
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：基于 DeepSeek Harness（DSH）的多平台群聊智能体系统｜由 DSH 驱动的多平台群聊智能体系统。
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh安卓版：集成 DeepSeek Harness、Ubuntu 运行环境、插件与文件管理，以及用户授权的 Shizuku 和无障碍自动化.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web plugin: per-day token usage statistics with a GitHub-style activity…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 給中文網文作者的本地寫作工作台。
- [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) - Appearance customization plugin for DeepSeek Harness: theme color palette…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - MCP server manager plugin for DeepSeek Harness: Settings → MCP page, OAuth…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness 插件：15 个 obra/superpowers 工程纪律技能，双语描述，每项技能可独立切换｜DeepSeek…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A commerce negotiation runtime + DeepSeek Harness (dsh) plugin.
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - DeepSeek Harness Web 的 MCP 伺服器管理 UI——浮動面板、JSON 匯入，以及由 profile 支援的持久化儲存.
- [liustack/pptwise](https://github.com/liustack/pptwise) - 真正的 PowerPoint，不是 HTML。告訴 AI 要涵蓋哪些內容，pptwise 就會在你的電腦上建立可編輯的簡報.
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - DeepSeek Harness 插件：DietrichGebert/ponytail 懒人 senior 模式与七阶梯子完美移植，6…
- [godchen520/dsh-web-remote](https://github.com/godchen520/dsh-web-remote) - DSH 手机/外网远程访问插件：免配置公网隧道 + 局域网 HTTPS 直连 + 自定义公网链接/端口 + 微信机器人。
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 將本機 WorkBuddy 桌面端已登入的模型（DeepSeek／GLM／Kimi／MiniMax 等）變成本地的 OpenAI 與 Anthropic…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - One-stop skills, subagent, MCP and LSP manager for DeepSeek Harness (DSH)…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 插件的常時相容性測試：精確版本、隔離 runners，以及可修復的上游問題.
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - Zero-cost, zero-hassle toolkit for DeepSeek Harness (DSH): one-click setup for…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 插件的 X 光：宣告的能力與實際行為。註冊表 + 靜態掃描器 + 徽章.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness 主机插件，将专案文件与长期记忆以纯 Markdown 形式储存在专用的 Obsidian vault 中.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - DSH 的本機優先語音對話。在自己的電腦上執行語音辨識與語音合成，並可選用外部提供者.
- [YunongDai2005/dsh-theone](https://github.com/YunongDai2005/dsh-theone) - One chat for everything, no more hunting for old conversations.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH 外掛：IDE 級 Git 工具視窗，作為原生 dsh-better-sidebar 分頁——分支樹、提交圖、變更、提交詳情、JetBrains…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - 基於 PTC 模式的創造模式：DSH 外掛，結合 Code Mode 工具編排 + 自引用 Cordis 工具與 preset…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多資料夾 workspace：讓 DSH（DeepSeek Harness）的 Agent 不只能讀寫主目錄，還能同時讀寫你新增的其他資料夾.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - DeepSeek Harness 的工程工作流程外掛程式：工作階段、驗證記錄、提交檢查，以及技能和規則管理.
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH 角色扮演外掛：角色卡（系統提示詞注入 + 使用者提示詞改寫）、可分享的單檔案卡包、重現原版 UI 的角色分頁與第一輪選角 chip。
- [openbkn-ai/bkn-dsh](https://github.com/openbkn-ai/bkn-dsh) - OpenBKN。
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) 外掛程式的零相依性驗證標準——靜態結構閘門 (R)、cordis 合約檢查 (K)、沙箱冒煙測試…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness 外掛市場 - 瀏覽、搜尋與安裝 dsh-plugin 主題外掛（dsh 外掛市場：瀏覽／搜尋／安裝外掛）。
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode — 讓 OpenCode Zen + Go 免費方案模型持續運作的 DSH…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness 的第三方外掛市集與受防護生命週期管理器.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人為本且可擴充的桌面工作台：對話、筆記、表格、檔案集中於同一個工作台；自行建立伺服器即可啟用多人即時協作.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 輸入體驗插件：傳送/換行鍵位切換、右鍵選單、面板捲動與尺寸記憶、OpenCode 請求標頭自動注入。
- [heiheiha798/dsh-plugin-subagent-delete](https://github.com/heiheiha798/dsh-plugin-subagent-delete) - DSH plugin: delete_subagent tool + UI - release or permanently remove subagent…
- [momasiku/dsh-pilot](https://github.com/momasiku/dsh-pilot) - Desktop automation for DeepSeek Harness: hands and eyes on the whole Windows…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - 為 DeepSeek Harness 桌面版提供「限網段 + 可選數字密碼」的遠端存取入口。
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Web 外掛：盯盤 market-dashboard 側邊欄分頁——三條附滑入日內圖表的報價列、含產業 alpha…
- [yu381792/superlcm](https://github.com/yu381792/superlcm) - 五种载体，一座本地对话档案馆：原文归档、分层后台摘要、原文查证与跨工具接续。默认原生压缩，Claude Code 与 dsh harness 可选接管.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 外掛程式：將 Windows 沙盒 ACL 設定失敗。
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 讓無法歸屬的空模型嘗試可重新嘗試，適用於唯一能判斷的那個接縫（deepseek-harness 討論串 #8321 與 #9352）.
- [denceee/dsh-everything-claude-code](https://github.com/denceee/dsh-everything-claude-code) - Adapts everything-claude-code to DeepSeek Harness: 11 skills, an ECC agent…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness agent preset: Codex and Claude Code as delegation subagents…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - 具備由 Verus 驗證的生命週期核心與 Cordis 相容性轉接器的 Rust 外掛程式執行階段.
- [mrpulor-gh/nuphus-mcp](https://github.com/mrpulor-gh/nuphus-mcp) - Desktop automation MCP server — computer use for any AI agent: control screen…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin。

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 383  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 79   | `Enc-hanted/dsh-pulse`, `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`                        |
| Python     | 39   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 27   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 14   | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7    | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 6    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2    | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| Swift      | 2    | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1    | `dphmoblie/deepseek-harness-android`                                                                          |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

歡迎提供修正，這是改善此清單最快的方式。如果某個項目被錯誤分類、評等有誤，或某個專案因名稱衝突而被錯誤排除，請建立 issue 或提交 pull request——最後一類是自動篩選最可能出錯的地方。

---

<sub>獨立的社群專案。與 Anthropic 無關聯，也未獲其背書或審查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商標。產品行為可能在未通知的情況下變更；任何關鍵內容都請以官方文件為準。資產仍歸其上游專案所有，僅在授權允許的情況下重製。</sub>

<sub>Last updated · 2026-10-11T12:27:08+08:00</sub>
