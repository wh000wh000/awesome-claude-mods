<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="超讚的 Claude 模組">
</p>

<h1 align="center">超讚的 Claude 模組</h1>

<p align="center"><b>依證據分級的 Claude Code 模組、外掛，以及它們改變的更深層行為索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-494-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <b>繁體中文</b> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **即時索引** · 上次同步: `2026-10-13T21:42:20+08:00` (UTC+8)
> · 條目: **494** · 最新更新新增項目: **0** · 實作語言: **13**

<sub>以下每個條目都經過自動收集、篩選與再次核查。這裡沒有任何付費置入。</sub>

<a id="featured"></a>

## 當下精選

<sub>每個分類選出一個項目，依證據等級和星標排序，並在每次更新時重新計算。這是排名，不代表背書；每個精選項目都會連結至下方的完整卡片。優先選擇發布了截圖或錄影的專案，讓這個橫列保持視覺化。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9493 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2548 · Python · 👁️ observed</sub>
<sub>找出幽靈 token。修復它們。在壓縮中存活。避免上下文品質衰退。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74489 · TypeScript · 👁️ observed</sub>
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
- [官方：Anthropic 自有的程式碼儲存庫與版本發行說明](#官方anthropic-自有的程式碼儲存庫與版本發行說明) — **14**
- [模組：使用模組功能建立](#模組使用模組功能建立) — **371**
- [DSH 與 Cordis 外掛生態系](#dsh-與-cordis-外掛生態系) — **98**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150543 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **150543** |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9493 · TypeScript · ✅ official · 3 天</summary>

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
| Stars        | **9493**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8261 · Python · ✅ official · 3 天</summary>

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
| Stars        | **8261**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6361 · Python · ✅ official · 243 天</summary>

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
| Stars        | **6361**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1804 · Shell · ✅ official · 3 天</summary>

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
| Stars        | **1804**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

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
<summary><b>此分類中的更多項目</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 為 mods 新增了 `$.ui.notify`：透過你自己的通知設定發出原生通知，並說明是哪個 channel 傳送了它 為 mod 的 `Button`…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 修復在 `UserPromptSubmit` 掛鉤或模組的 `prompt.submit` 掛鉤期間按下 Esc…

</details>

<a id="mods"></a>

## 模組：使用模組功能建立

此處的每個項目都展現了使用 Claude Code 在 2.1.287 中取得的功能的證據：它透過 `ui.render` 繪製內容、擁有窗格、區段或卡片、讀取 `$.ui.selection()`、使用 `agent.spawn` 產生隊友，或明確表示自己是模組。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2548 · Python · 👁️ observed · 0 天</summary>

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
| Stars        | **2548**   |
| Last push    | 2026-10-13 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐548 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **548**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐339 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

macOS 選單列與 Windows 系統匣應用程式釘選 Claude Code、Codex、Antigravity 與 Grok 的 CLI 配額、消耗速率和費用到你的螢幕上。本地優先，不進行 LLM API 呼叫。HTML 報告，14 種主題。

<sub>🔧 在程式碼中找到使用處: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | Python                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **339**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐221 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **221**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐166 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stars        | **166**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐164 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code 直接在終端機中顯示圖片並播放影片：螢幕截圖、Playwright 錄製內容，以及同步的前後 QA。Ghostty & kitty。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **164**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐128 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **128**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **96**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 4 天</summary>

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
| Stars        | **79**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐77 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **77**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

##### 📝 Summary

Darrell Wang 製作的 Claude Code mods — 提示上方的資訊列，不消耗模型 Token。台股／美股看板 + 更多功能即將推出。

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
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 6 天</summary>

##### 📝 Summary

Claude Code 的專家 skills、agents、commands、rules、hooks 與 output styles — 工作階段延續性 + 現代化 CLI 工具，適用於真實世界的開發工作流程

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
| Stars        | **62**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐49 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Summary

Claude Code mods：在提示上方顯示即時計畫進度列

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **49**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>動畫錄影 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">開啟影片</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arjun0014/project-sentinel">Arjun0014/project-sentinel</a></b> · ⭐47 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

長時間 Claude Code 執行的任務控制中心：一眼掌握上下文與執行進度、Autopilot 交接、防護措施與平靜的活動檢視，支援終端機與 Claude Desktop。

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | TypeScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **47**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-agents-automation` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arjun0014--project-sentinel/cd63c979e03573e7.png" width="100%" alt="Arjun0014/project-sentinel screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐29 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stars        | **29**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐28 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **28**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

生活在 Claude Code 提示上方的像素 Pokémon

##### 📌 Basic facts

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Category | `模組：使用模組功能建立`                     |
| Evidence | `其自身文字提到模組 API，或宣告具備模組功能` |
| 語言     | JavaScript                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>動畫錄影</sub></td>
</tr></table>

<sub>由於未宣告允許重新散布的授權條款，資產以熱連結方式載入自上游儲存庫。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 11 天</summary>

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
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stars        | **20**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐18 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **18**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stars        | **13**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stars        | **13**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 6 天</summary>

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
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

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
| Stars        | **9**      |
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
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stars        | **9**      |
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
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **9**      |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stars        | **9**      |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

一個 plugin 中包含六個 Claude Code mods（Token Weather、Cache Keeper、Wait What、Prompt Queue、Snake、Blast Radius），可個別切換，另附 mods 與 hooks 的比較報告。

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
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 337</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - 可與 Claude Code 搭配使用的 100 多個 mods 集合.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其建置工具：先是 builder skill，接著是 mods。
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad 的 Claude Code 模組：窗格、區帶、提示防護、機密處理與記憶工具。單一市場，每個模組可獨立安裝.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天執行的 Claude Code harness，自第一天起就以此名稱發布，現在與 ucsandman/Agnostic-AI 使用相同的儲存庫：防護…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 為 Claude Code 換屋頂：不修改二進位檔，將系統提示與英文提醒換成你自己的文字（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四個 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 與 Collision Guard。
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods，在 Claude 讀取提示前修正並翻譯你的提示。
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 附有來源引註的 Obsidian 知識庫，介紹 Claude Code mods：它們如何運作、如何建立，以及安裝前如何檢查.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 來自 Nekyia Labs 的 Claude Code mods 與 skills，由住在持久家園中的 AI 每日建立並使用。
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 將 Claude Code 的終端機文字記錄呈現為桌面應用程式外觀的 mod。
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods：Claude Tools menu、Zen mode、terminal themes、effort 與 mode…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的側邊窗格：工作階段執行的子代理程式、各自正在做的事、其權杖，以及只需點擊即可查看的對話.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教導 Claude Code agents 建立 Claude Mods（function-hook plugins）的 Skill，附有入門範例。
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社群 Claude mods、插件與技能，可從單一市場安裝。
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss 的 Claude Code 模組。
- [devbrother2024/devbrothers-mods](https://github.com/devbrother2024/devbrothers-mods) - 개발동생 的 Claude Code mods 集合。計程車套件：計價器、導航、超速取締攝影機、行車記錄器。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 適用於 Claude Code 的 Claude Mods（function-hooks plugins）.
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - 你的計畫，正在自我監看。讓 Claude Code 和任何 MCP 主機即時維持同步的本機桌面路線圖樹。純 JSON，無雲端.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods gallery：已檢查並置頂的 Claude Code mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 供使用對話式代理的人類使用的決策佇列 CLI/TUI。代理張貼問題，人類從單一收件匣回答.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE 面板 mod：Agent 看板、檔案樹與 HWP／PDF 檢視器、系統狀態、Claude／Codex／Antigravity…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code mod，可在兩個並排欄中繪製 Edit 和 Write 差異。
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown，在您輸入時直接繪製到 Claude Code 的提示框中。圍欄程式碼甚至在您關閉圍欄之前，就會變成語法高亮卡片.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods：像素螃蟹用量面板 usage-hud + 終端機中可點擊的 HTML 連結與一鍵複製程式碼卡片 html-shelf。
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - 適用於 Claude Code 的浮動狀態卡——模型、上下文、速率限制、費用、分支——另附可由任何腳本或 mod 提供資料的進度 API.
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code 的模組：為終端機 UI 新增即時窗格與行為的函式鉤子外掛程式。
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - 全方位的 Claude Code 插件。與你的團隊聊天、分享程式碼，並在工作階段旁保持即時房間（使用量、git、天氣、lo-fi 等）.
- [Danovich/turntype](https://github.com/Danovich/turntype) - 在 Claude 工作時進行的打字測試。Claude Code 模組.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard 在你分享螢幕時遮蔽名稱與 secrets；cache-panel 在 prompt cache…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code 的 Mods 與外觀：為 Claude 的任務提供即時進度列、易讀的深色主題與相配的 Windows Terminal…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions。解鎖 Claude 的完整威力.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod（外掛），新增含有 Activity、Files、Agents、Context 和 MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - 適用於 Claude Code 的面板、護欄與生活品質 mods：context、usage、即時活動、通知、安全規則、prompt…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示框上方的兩個 Claude Code mods：context-window meter、5 小時限制、prompt clocks 與工作階段成本。
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 讀取 Claude Code 命名的 markdown 檔案，並在工作階段旁呈現；指向任何區塊即可讓 Claude 編輯它。一個 Claude Code 模組.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在任何 terminal 中，將貼上的圖片縮圖顯示於 prompt 上方。
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的語音協作者。與由 ElevenLabs conversational AI 驅動的 3D 狼人討論事情；當你同意後，它會將提示傳送給…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code 的 GlanceFlow：提示詞上方的簡潔檢查清單，顯示計畫、進度，以及何時需要 Claude.
- [BatuhanCakmakk/wavy-usage](https://github.com/BatuhanCakmakk/wavy-usage) - Claude Code 提示詞上方的液體填充式使用量環：5 小時／7 天限制、內容脈絡、快取 TTL、高強度模式下的戰鬥機，以及顯示近期回合與費用的面板.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：context bar、agents panel、PDPA blur。
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed，即時打字速度計，附每次 prompt 的統計資料。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code 的煙火：每次按鍵、工具呼叫、提交和通過的測試，都會在提示上方化為盲文煙火升起。Claude Code 模組.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 的 Mods：使用外掛 function-hooks API 建立的窗格、指令與 hooks。
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 透過動畫示範、分類清單與直接來源連結，探索 Claude Code mods、plugins 與 extensions。由 FindMods.dev 提供支援.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：在 transcript 中內嵌繪製 mermaid 圖表。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code mods（function-hook 外掛程式）：session-switcher 等。
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code 模組的應用程式商店，就在 Claude Code 中：使用 /mods 瀏覽、搜尋與安裝 2,700 個模組，或要求 Claude…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 六個 Claude Code mods：在提示上方顯示計畫限制與上下文、用於權限提示的允許清單教練、subagent…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout（找出你最常使用的 mods）、usage-meter、check-ledger、resume-nudge。
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 適用於同時執行多個工作階段的兩個 Claude Code mods：prompt 上方的 context card 與聊天旁邊的 sessions pane.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 按需建立 Claude Code 模組——讀取你的對話並建立適合你的模組：計畫進度列、檔案窗格、內容量表、危險指令防護、測試監視器.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：探索、檢查、切換與更新 Claude Code mods。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最佳 Claude Code Mods：精選、驗證並置頂。一次 /plugin marketplace add，43 個 mods.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 插件：自動 Claude model routing.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code 模組：即時顯示工作階段開啟或推送到的 GitHub PR——CI、審查、衝突、合併——所有工作階段共用一個輪詢器.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code 的六個 mods：動態 Clawd 吉祥物、用量限制與提示快取列、傳送前訊息檢查器、快速回覆、待辦佇列和成本帳本.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code 的 mods marketplace：agent loop 的逐步除錯器、git 帳號提示、worktree 狀態列，以及更多功能.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code 的開源 mods：窗格、狀態列、通知、工具防護和斜線指令.
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 的最佳全能 mod pack：使用限制與上下文 HUD、針對 rm -rf 和 git reset --hard…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - 在您的 Claude Code 中播放 YouTube Shorts 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren 的 Claude 工具組：適用於 Claude Code 的 skills、mods 與 MCP servers。可透過外掛市場使用單一指令安裝.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - 適用於 Claude Code 的 Mods：Clawd，一個會演示 Claude 正在做什麼的小型像素吉祥物。
- [reporails/arcade](https://github.com/reporails/arcade) - 經典桌面遊戲化身為 Claude Code mods，在 Claude 工作時於面板中遊玩。由 Reporails 製作.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude 的 code-mods。
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 我自己的 Claude Code mod 外掛市場。
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精選的 Claude Code 模組清單，可作為外掛程式市集安裝：主題、面板、狀態列、肖像.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 兩個 Claude Code mods：cache-keeper 和 ctx-mod。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 讓 agent 保持誠實的 Claude Code mods——守護範圍、驗證部署，並在 prompt 上方繪製工作階段的 function hooks.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - 剛出廠的新鮮貨。Claude Code 模組：要求產生迷因，同時繼續工作。草稿在側邊面板中生成；挑選、混搭、核准並發佈至 Slack.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - 每個 Claude Code 的 mod：提示快取列、後續步驟、快速按鈕與變更重播——可從 marketplace 安裝。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 一個 Claude Code 模組，在提示上方的列中繪製你的使用量限制和支出.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 用於在工作中途擷取想法、跨專案與機器整理想法，並將其轉換成提示的 Claude Code 模組。
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - 在 Claude Code 內即時查看 GitHub PR 狀態、合併準備度、檢查、留言與警示。
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - 寫 code 時養一顆慢慢入味的茶葉蛋 · 在你寫 code 時養一顆慢慢醃入味的茶葉蛋。
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（市集 herman-mods）。
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在背景執行的內容：subagents、Codex jobs、shells、monitors、cron jobs 與…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code 模組：直接在文字上逐點回答 Claude。選取對話中的任意部分，加入評論，並將所有評論作為一個提示詞傳送.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - 關於 Windows 上 Claude Code mods 的第一天現場筆記：context/配額燃料條、Thai UI mod、Matrix…
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code mod：在橫幅與窗格中即時顯示 GitHub pull request 狀態（檢查、審查、討論串、合併佇列），並提供已確認的合併操作.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：在提示詞上方顯示即時成本、context 與方案配額儀表。圖示需要 Nerd Font.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin 與 mod：一個 AI-native SDLC。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 一個 Claude Code mod，可用具名 profiles 針對每個 repo 開啟或關閉你的全域 skills、agents、rules 和…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 經過測試、可用單一指令安裝的 Claude Code 模組：YOLO 模式的防護機制、即時成本與內容、面板、寵物等。另附精選的最佳社群模組清單.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 一批由我建立的 claude code mods。
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods。touch-map：以樹狀圖和活動地圖查看 Claude 列出、讀取、編輯或建立了哪些檔案.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - 使用 Claude Code 工作時學習外語。
- [0xctx/sysop](https://github.com/0xctx/sysop) - 告訴 Claude 你想要什麼。取得由另一個 AI 建構、測試、審查並合併的成果.
- [20alexl/windvane](https://github.com/20alexl/windvane) - 替你照看漫長的 Claude Code 工作階段：監視上下文填充情況、起草檢查點、在適當時機壓縮，然後恢復工作。每個子代理都有規則，也有專案記憶.
- [Akeuuh/claude-mods](https://github.com/Akeuuh/claude-mods) - Claude Code 外掛市集：以函式掛鉤建立的 mods。
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code 的即時成本、Token 與上下文用量側欄：一個在工作階段內顯示每回合成本、快取命中率、消耗速率與 30 天支出的模組.
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Claude Code 的函式 hook 模組：限制遙測列、多選問題與下一步面板，以及每次提交後更新 README.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Claude Code Mod：持續列出對話中的未完成項目，並在提示詞上方的橫帶中顯示.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 為真正的 Engineers 打造的 Claude Code 模組。
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code 的終端機工作階段摘要，位於 Claude 桌面應用程式的 Code 分頁中（Claude Code 模組）。
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Claude Code 模組：查看你的對話正在使用哪些技能、插件、子代理與 MCP 工具。
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每個 Claude Code agent 在其 context 中有哪些檔案，以及各自的比例.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 適用於 Terminal 與桌面應用程式的小型 Claude Code mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI skill + mod，可在代理回覆中加入西班牙文單字。
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Claude Code Mod – 別再浪費權杖：/keepwarm。
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - 位於 Claude Code 提示之上的 Alarum 事件：剛剛收到的內容，以及一鍵交給代理程式.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - 你的 Floatee 待辦清單位於 Claude Code 的 prompt 上方：一鍵執行、引導並勾選你的 todos.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 一個將其重新設計為《疑犯追蹤》中的 The Machine 的 Claude Code mod.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：Claude Code mod，用於強制且已驗證的 subagents DAG workflows，並提供即時 DAG 窗格。
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod：工作階段狀態、即時 Spec Kit 進度與用量視窗治理。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 將內容視窗作為提示上方的一列，採用 Claude Code 繪製自身量表的方式呈現.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code 模組：挑選每個子代理程式的模型與推理投入程度。
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph：顯示 Claude Code 所知內容的即時圖表.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 的即時工作任務 HUD：Claude 工作時顯示於提示詞上方的橫條，一鍵即可開啟完整儀表板.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code plugin (mod)，讓 Claude Code 終端機 UI 看起來像 Claude 桌面應用程式：提示泡泡、Markdown…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - 等待 Claude Code 回覆時，不要讓你的注意力飄走.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - 適用於 Claude Code 的免費開源外掛。在你執行 /clear 前，Claude 會寫下一份可供閱讀與編輯的簡短交接內容，下一個工作階段會從中繼續.
- [midudev/better-claude](https://github.com/midudev/better-claude) - 適用於 Claude Code 的提示佇列模組：/after &lt;task&gt; 會在目前任務完成後執行該任務，不介入引導.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods：經過精選與測試，且每個 mod 都附有建立它時使用的提示.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文件查證器、程式碼稽核器、錯誤記憶記錄、mod 等.
- [partalemre/MODZ](https://github.com/partalemre/MODZ) - 一個面板中的 17 個 Claude Code plugins。即時查看 Claude 的每一步：agents、files、plans、tests 與…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod：回覆中的可點擊 paths — 點擊資料夾可在 Finder 中開啟，點擊檔名可開啟檔案。
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 好幫手外掛：位於提示詞上方、會記住你的規則並標示 Claude 捷徑的 ASCII 夥伴。
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - 精彩的 Claude Code 模組集合 | Claude Code 模組合集.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一個 Claude Code mod，可依要求用本機開源 Kokoro TTS 聲音朗讀 Claude 的回覆與你的提示.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 當 Claude 搞砸時揍它 — Claude Code 的紓壓 mod：卡通屁股、8 個拍打器、9 個屁股、標記、連擊、音效.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用於即時窗格、成本感知模型路由和安全防護的小型外掛程式。用一個命令從 marketplace 安裝.
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code，附帶憑據。一個會規劃、委派並證明工作已完成的插件.
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code 模組：在提示上方單行顯示 5h/7d 配額、上下文視窗、提示快取剩餘時間與工作階段成本，將每個子代理程式的成本顯示於滑鼠懸停時。
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 與 plugin：用量監視器、token 追蹤器與狀態列.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude Code mods：EMCC (Every Mod Claude Code)，一套為 Claude Code 精選且經測試的 mods 集合。
- [adithepmeekhun/self-clear](https://github.com/adithepmeekhun/self-clear) - 讓長時間 agent runs 持續進行的 Claude Code mod：在你選擇的 context size 下，Claude 會寫入…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示上方的動畫盲文貓。
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示上方的一隻像素貓，會執行 OmniDimension 語音代理程式測試通話。Claude Code 模組.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一個 Claude Code 模組，會選擇適當時機進行壓縮，以保持上下文視窗較小.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code 的 Claude 模組：token-meter（工作階段權杖、Claude 與本機 LLMs 的比較，搭配 Pac-Man 內容迷宮）。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code 的通用 mods：bands、窗格、toasts 與 hooks。包含 usage-bar：在提示上方顯示內容、成本與計畫限制.
- [aott33/model-router](https://github.com/aott33/model-router) - 一款 Claude Code 模組，可在每個子 Agent 啟動前為其選擇模型，並顯示每個模型的成本.
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Claude Code Mod：在一行安靜的文字中顯示你的內容脈絡視窗，只有重要時才變色.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - 每次程式碼變更後，LGTM Lines 船隻都會揚帆駛過 — Claude Code Mod。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 將您的 Claude 使用量限制製作成動畫村民生命值卡片，並附上每週進度警告 — 一個 Claude Code 模組。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 團隊的 Claude Code 模組（ather 商城）。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作時進行短訓練：每日目標、連勝、徽章與可選排行榜。一個 Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code 的用量看板：各模型花費（今日、本週、本月、全部時間）與每週上限預測.
- [bahaospanov/skills](https://github.com/bahaospanov/skills) - Bakhtiyar Ospanov 的 Claude Code mods：基於 function hooks 建置的 plugins。
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - 一款 Claude Code 模組，顯示子 Agent 正在處理的工作：提示詞上方的進度列與即時 Agent 面板。savvy-progress 的分支.
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - 一款 Claude Code 模組，在 Claude 的回覆下方以小型碼表標籤顯示每個回合耗時.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方顯示 Apple Music 與 Spotify，包含封面圖、控制項與 Up next…
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - Claude Code 的 Performance 分頁會顯示：每個模型請求與工具呼叫的即時瀑布圖、送往核准的部分，以及能追回時間的修正方案.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code 模組：快取時鐘、影響範圍、建議、工作清單、烤架。
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是給你的 Claude Code 的一隻貓頭鷹。
- [cerebrai/ironman-mod](https://github.com/cerebrai/ironman-mod) - 用於 human-AI 增強工作流程的 claude code mod -- 就像 tony stark。
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - 讓 Claude Code 按計畫執行：透過 hooks 強制執行階段、核准關卡與檔案預算，另有七個附加模組（代理、token、交接、警示、PR、密鑰）.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - 住在 Claude Code 內的 Tamagotchi：它會孵化、吃掉 Claude 寫的程式碼、留下 bugs，並成長為八種成體之一.
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code 的最愛：一鍵存取指令和技能的圖示。
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code 模組（函式掛鉤外掛）：session-meter 及其他模組。
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider：一個小按鈕，可隱藏提示上方的每個 Claude Code 模組，也能將它們恢復.
- [finalpantasy/claude-mod-pack](https://github.com/finalpantasy/claude-mod-pack) - Claude Mod Pack：小型 Claude Code Mods。包含使用量限制狀態帶與 /mods 切換面板、可隱藏所有 Mod…
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Claude Code 模組：凍結工作階段，稍後像什麼都沒發生過一樣恢復。
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - 在 Claude Code 回覆的每個程式碼區塊上按住 Ctrl 並點擊即可複製連結。
- [guojunjie0614-cyber/workhorse](https://github.com/guojunjie0614-cyber/workhorse) - Claude Code mod：將編碼、審查與營運工作交給 Codex，作為背景子 Agent 執行。
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Claude Code 的即時花費計量器：顯示工作階段與子代理程式及工作流程的成本，停駐於右側。
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模組：每個回答花費的時間、Claude 思考的時間，以及 tok/s，顯示在 Claude 桌面應用程式的回覆正下方.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - 位於你的 Claude Code 提示輸入框上方的駕駛艙。這隻鴨子會讀取儀表.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - 自動讀取你的工程圖，然後在 SolidWorks 裡建模。讀取你的工程圖（DWG/DXF/PDF/影像），並在 SolidWorks 中建立零件模型.
- [jBeyondstars/ultracode-models](https://github.com/jBeyondstars/ultracode-models) - Claude Code mod：選擇每個子 Agent 執行時使用的模型與運算強度，包括 Ultracode 工作流程 Agent.
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - VS Code 內的 Claude Code 子代理即時看板：每個對話的子代理及其任務詳細資訊、訂閱使用量與內容填充情況.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼。/ctx 開或關（Claude Code 模組）。
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（Claude Code 模組）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（Claude Code 模組）。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（Claude Code 模組）。
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（Claude Code 模組）。
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（Claude Code 模組）。
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 繁體中文漢化（自管版）——自己的翻譯表 + patch 工具 + 升級檢查。
- [jidhra/claude-mods](https://github.com/jidhra/claude-mods) - Jidhra 的 Claude Code mods 集於一個外掛市集。
- [kadaliao/claude-mods](https://github.com/kadaliao/claude-mods) - Claude Code mods：改變 Claude Code 自身介面與行為的 function-hook plugins。
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的帶狀列中：演出 session、顯示正在執行的項目、context 和使用限制，並與你的 CI…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - 使用 VOICEVOX／Irodori-TTS 等朗讀 Claude Code 的回覆與通知 mod。
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code 模組。PixBar：位於提示上方的像素生物，會隨著您的回合、內容、五小時視窗與 git 移動.
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code 模組：將每個 Claude Code 工作階段集中在一個浮動視窗中，提供各工作階段目前處理內容及需要你介入之處的即時摘要.
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - 在一個外掛市集中提供小型 Claude Code 模組。model-guard：依規則選擇每個子 Agent 執行所使用的模型。非官方.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 社群策劃的 Claude Code Mods 指南：使用案例、原始示範、相容性證據與安全性備註。English / 中文。非官方.
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Claude Code 模組：在提示下方顯示方案限制（5 小時工作階段、每週）與續訂時間，並估算何時耗盡。不使用 token.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一個 Claude Code 模組，會在 iTerm2 分頁副標題中顯示 Claude 正在進行的工作，因此只要看一眼分頁列，就能知道哪個工作階段需要你的注意。
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy，一個非官方粉絲製作的像素夥伴，生活在 Claude Code 提示詞上方，並會對 Claude 的操作做出反應.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - 位於你的 Claude Code 提示上方的一隻蓬鬆黑貓。她會眨眼、呼嚕、打盹，並擔心你的內容量。用愛製作，以紀念我的貓 Mango。❤️。
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Claude Code 的小型模組：runner-avatar，在提示上方執行的小頭像。
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code 模組：即時面板，顯示你的 AI 程式設計代理正在瞄準、假設、規劃和決策的內容。確認或標記其假設.
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code mod：/sessions 面板，用於瀏覽和刪除工作階段及其磁碟上的資料（WSL、Windows、macOS）。
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code 的社群 mods：在 Claude Code 內執行的 guards、窗格與指令。Marketplace：modhub。
- [mkiselyow/diff-lens](https://github.com/mkiselyow/diff-lens) - Claude Code Mod：請 Claude 引導你完成 PR，點擊其回覆中的任一檔案連結，即可查看該檔案相對於基礎分支的變更，並捲動至對應行.
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Claude Code 模組：Codex（ChatGPT 訂閱）及其他非 Anthropic 模型作為工作階段與子代理程式模型，無代理伺服器。
- [MohamedHamed001/claude-mods](https://github.com/MohamedHamed001/claude-mods) - Claude Code 外掛：委派。
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Claude Code 模組：命名 Claude…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模組：透過在工作階段開始時設定 CLAUDE_CODE_ENABLE_TODO_TOOLS，為省略待辦工具的模型重新啟用它們.
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod，等待安全的暫停時機，接著交接你的工作階段或將其壓縮.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模組：提示上方每個任務清單一行，顯示目前任務、進度列與計數。在終端機與桌面應用程式中外觀相同.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 內與 AI 玩 Connect Four（/connect-four）。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模組：當另一個程式設計代理提交至你的儲存庫時，Claude 會透過差異與測試進行審查，而不是相信它的報告.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 適用於多個 AI 代理共用儲存庫的 Claude Code 模組：防止秘密值離開 .env、防止推送至公開遠端儲存庫，以及防止 git…
- [niksavis/handily](https://github.com/niksavis/handily) - Claude Code mods，顯示你的工作項目、任務與工作階段，適用於任何追蹤器。Mods 只顯示並詢問；永遠不會強制執行.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code 的 SQL 防護欄：在 Claude 透過 DB CLI（函式掛鉤／Mods）執行 DELETE、沒有 WHERE 的…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - 一個適用於 Claude Code 的記事本窗格，作為模組。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - 一個適用於 Claude Code、以 Windows 與 CJK 為優先的模組：在任何終端機中提供貼上影像與文字預覽、帶有 CJK…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 最佳的 Claude Code 模組，依它們能為您做的事排序。人工檢查，每個模組一行介紹.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - 兩個適用於 Claude Code 的 Claude 模組：護欄。
- [partalemre/transceiver](https://github.com/partalemre/transceiver) - Claude Code plugin（beta）：Claude Code 內的團隊聊天.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack：一個 Claude Code 模組。在同一個窗格與狀態列中，提供具唯讀起始狀態的永久 worktree、團隊控制項與內容庫.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 桌面應用程式 Code 分頁的即時工作階段統計側邊窗格：上下文、成本、git 變更、回合統計、子代理程式、記錄.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod：在 Claude 工作時做伏地挺身。無 tokens.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain：Claude Code 模組的實務指南，從 ELI5 到政策工程，附實地測試與引導式教學。
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - 一個開放原始碼的 Claude Code 修改市集，具備用於貢獻內容的儲存庫 skills 與一致的美術作品.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 模組：將你在計畫模式中核准的計畫轉為提示上方的即時核取清單，隨著 Claude 完成每個步驟逐一勾選。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精選的 Claude Code 模組清單。每個項目都已複製，並使用 claude plugin validate 檢查，且標記其可接觸的內容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：輔助代理程式在 Haiku 上執行，大型檔案與日誌則由免費的 Gemini 模型摘要，而不是填滿 Claude 的內容.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 隨工作階段播放的 lo-fi 原聲帶：平靜、專注、流暢，另有通過與失敗測試的提示音。原創音樂.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 撰寫程式時學習：每當一輪操作變更程式碼後，提示上方會出現一個關於該確切變更的問題。依概念評分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 記錄 Claude 所做每次編輯的磁帶：重播每項變更自行輸入的過程、逐步檢視，並將任何檔案倒轉至任何步驟.
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Showrin 的 Claude Code 模組，讓每日忙碌工作更有效率.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Claude Code 模組：內容與計畫上限及消耗率預測，另有來自純文字檔案或自訂命令的截止期限雷達，顯示於程式碼旁的窗格中。
- [sohi2212/claude-agent-radar](https://github.com/sohi2212/claude-agent-radar) - Claude Code mod：背景代理程式的即時雷達 + n8n 風格的計畫畫布，支援巢狀子代理程式計畫。
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Claude Code 模組，讓無人看管的工作階段持續通過用量上限、API 錯誤與內容已滿的狀態。
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - 自訂 Claude Code mods marketplace（cc-mods），附帶 vendored Anthropic sample mods。
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 為 Claude Code 一鍵產生 commit 訊息，搭配跳舞的像素風 Malenia。
- [SummerRiversound/review-inbox](https://github.com/SummerRiversound/review-inbox) - Claude Code mod：等待你審查的 PR，每個都以白話摘要，另加上你自己的 PR 與 issues。
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Claude Code 的模組。cache-meter：提示快取命中率、內容填充與自動壓縮控制。usage-limits：5 小時與每週上限.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — 一個 Claude Code 模組，會在提示正上方顯示您的 Claude 計畫用量（工作階段與每週限額、重設倒數、上下文）.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - tanmen 製作的非官方 Claude Code 模組（市集：tanmen）。
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一個 Claude Code 模組，在窗格中顯示目前工作階段：每個提示詞、Claude 分階段為其完成的工作、每個子代理程式及其答案，以及提示詞的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一個 Claude Code mod 外掛市集：function-hooks 外掛，可在 Claude Code 內繪製 band、窗格和其他 UI.
- [thunini/thinking-flow](https://github.com/thunini/thinking-flow) - 一個 Claude Code mod，繪製出 Claude 如何得到每個答案：你的問題、幾個白話步驟，以及答案.
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - 在朗讀句子時反白顯示，同時聆聽 Claude Code 的回覆。本機語音，支援多種語言.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Claude Code 模組：Claude 最後回覆下方的一個按鈕，可複製你上次訊息後的所有回覆，包含其可見的思考內容與你對其問題的回答。不包含工具輸出.
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - CC 模式，會在提示尾端顯示你登入的 Claude 帳戶、組織與方案，以及你的用量上限。
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模組：適用於長時間執行任務的動畫進度列與完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 三個小型 Claude Code 模組：查看子代理程式何時完成、在 Claude 完成後佇列訊息，以及讓你最愛的技能保持一鍵可用.
- [varunmoka7/disk-sweep](https://github.com/varunmoka7/disk-sweep) - 當你的 Mac 磁碟空間不足時發出警告，並透過 /disk 列出可勾選刪除的舊 Claude Code 殘留檔案.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 說出「我迷路了」，Claude 就會再次用日常用語解釋上一則回覆。Claude Code plugin.
- [varunmoka7/park](https://github.com/varunmoka7/park) - 儲存這個 Claude Code 工作階段，並為下一個工作階段寫下備註。如果你使用 herdr，/park 也會要求其他代理程式分頁儲存，並可關閉它們.
- [varunmoka7/read-fence](https://github.com/varunmoka7/read-fence) - 當你開啟 fence 時，阻止 Claude 逐一開啟你的 skill、rule 與 plugin 資料夾中的檔案。Skills 仍會正常執行.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作旁的窗格中向 Claude 提出旁支問題。主要對話永遠看不到它。運作方式類似桌面應用程式的 /btw.
- [varunmoka7/skills-az](https://github.com/varunmoka7/skills-az) - 當你在提示詞中輸入 / 時，立即以 A 到 Z 的順序顯示 slash commands 與 skills 清單，並在你持續輸入時縮小結果範圍.
- [varunmoka7/unattended](https://github.com/varunmoka7/unattended) - 阻止 Claude Code 工作階段在鍵盤前無人時向你提問。輸入 /unattended，或使用 CLAUDE_UNATTENDED=1 啟動.
- [vcdim/claude-code-sciplot](https://github.com/vcdim/claude-code-sciplot) - 一個用於科學繪圖的 Claude Code mod：在側邊窗格中使用 Python、R、TikZ、MATLAB 與 Mathematica，並搭配即時互動式…
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code 外掛：在 prompt 下方的 permission-mode 行中顯示 prompt-cache…
- [wonwoo/tool-timeline](https://github.com/wonwoo/tool-timeline) - 一個 Claude Code mod，顯示每一輪時間花費在哪裡：每輪下方都有一列，可展開為模型請求與工具呼叫的時間軸.
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 外掛：在提示詞正上方顯示你的 Claude Pro/Max 使用量限制、使用速率預測、計費週期、以 token 和 $/€…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 用於 Claude Code 的 Mods。agent-crew：以即時 pixel crew 觀看你的 subagents 工作，包含…
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
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code 的完整狀態列儀表板 — 工作階段資訊、配額條、Agent 追蹤器、MCP 健康狀態、訊息歷史記錄等.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：追蹤你的 Claude Code 工作階段的碳足跡。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - 由 awesomejun 製作的 Claude Code 美觀狀態列。
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公開的 Claude Code skills 與 mods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code 的 Skills、mods、子代理、hooks、斜線命令與指南 — 可由你的代理安裝（請參閱 INSTALL.md）。
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免費的 LLM APIs 與程式設計 Agent — 每週自動更新並探測驗證兩次。免費方案、免卡試用、免費模型.
- [aiedwardyi/claude-usage-monitor](https://github.com/aiedwardyi/claude-usage-monitor) - Claude Code 狀態列插件，在終端機中顯示 5 小時／7 天配額、上下文使用量、Token 及重設倒數.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 在你的終端機、Claude Code 和 Cursor CLI statusline，以及 MCP…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 將你的程式設計代理變成鍵盤韌體專家的 Agent Skill。稽核 ZMK/QMK keymaps、調整 home row mods、讓 trackballs…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供禮拜時間、回曆日期、adhkar、每日 ayah、sunnah fasting、Ramadan、Jumu。
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - 個人 Claude Code 設定版本，儲存於 ~/.claude — 代理、技能、hooks、設定與狀態列（參考用途，不是入門範本）。
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 適用於 Claude Code、pi 與 DeepSeek Harness 的插件合集：狀態列 HUD、任務進度條、Tailscale 節點狀態等 · 適用於…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - 適用於 .NET DDD/Clean Architecture 的可攜式 Claude Code 工具組：嚴格的 TDD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 可攜式 Claude Code 全域設定：自訂技能、PreToolUse hooks，以及自訂狀態列。可在 Linux、macOS、WSL 上執行.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - 適用於 Claude Desktop Code 分頁的非官方 mods — usage-pet：帶有 Clawd 動畫像素寵物的 usage band.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：整理過的 skills 與 mods，可在任何人的機器上運作.
- [vtmocanu/cc-statusline](https://github.com/vtmocanu/cc-statusline) - Claude Code 的雙行 ANSI 狀態列：git + k8s context、rate-limit 長條、服務健康狀態、AI session 主題。
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - 從本機對話記錄與狀態列資料分析 Claude Code 的 token 使用量與成本。
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - 美觀且資訊豐富的 Claude Code 狀態列。零相依性、跨平台。pip install claude-status。
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - 你的 Claude Code 代理視覺化看板：將工作階段、子代理與背景代理顯示為卡片，並繪製箭頭讓它們彼此交談.
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - 可自訂的 Claude Code 狀態列，配備拖放編輯器。
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code Plugins 與 Skills 的 marketplace，用於促進 Hytale 的遊戲 mods。
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Claude Code 的單行彩色狀態列——資料夾、模型、內容使用量與速率限制。
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Windows Terminal 與 tmux 中 Claude Code 的分割窗格檢視器：將 session 以渲染後的 Markdown 呈現，包含…
- [ian-exnodes/statusbar](https://github.com/ian-exnodes/statusbar) - Claude Code 外掛：提示詞下方的即時雙列狀態列，顯示模型、git、上下文填充量、5h/7d 配額、token、費用與工作階段時間。
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code 的即時工作流程階段狀態列（Plan → Exec → Verify → Done），由模型自行更新。
- [mvrozanti/claude-progressbar](https://github.com/mvrozanti/claude-progressbar) - 在狀態列中繪製 Claude Code 執行的 Bash 命令進度條：從輸出解析、根據過往執行結果估算，預設使用盲文.
- [naturalmoods/herdr-telegram-notify](https://github.com/naturalmoods/herdr-telegram-notify) - 當 Agent 完成工作或需要輸入時，在 Telegram 上通知你，並附上其最後訊息、變更、持續時間與費用.
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Claude Code 終端機的 3 行微型儀表板——模型、內容消耗、速率限制進度與倒數計時，以及完整 git 狀態。Node、零相依套件、MIT.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media mods 的 Repository.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - 降低 Claude Code 和 Codex 的 token 消耗：将查询和测试运行路由到更便宜的模型，把文档转换为紧凑的…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - 快速且可設定的 Claude Code 狀態列——單一靜態 Go 二進位檔。
- [barkleesanders/claude-hud](https://github.com/barkleesanders/claude-hud) - Claude Code 的即時抬頭顯示器 — context health、tool activity、agent tracking、rate…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - 適用於 Claude Code 的增強型色彩分級、零相依性狀態列.
- [ist-j-ichikawa/claude-code-statusline](https://github.com/ist-j-ichikawa/claude-code-statusline) - j-ichikawa 為 Claude Code CLI 製作的自訂 statusline。
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - 在 macOS、Linux 與 Windows 中顯示 Claude Code 的關鍵狀態詳細資訊，包括模型、上下文、限制、git 資訊與工作階段時間.
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - 精簡且積極維護的 Claude Code 狀態列 — 在一行中顯示模型、工作量、token 使用量、速率限制和重設時間.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 原生 agent teams。盡在掌控。Claude Code 的嚴格 worker limits、即時 team visibility 與可攜式…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - 適用於 Claude Code 的 Windows PowerShell 狀態列：5 小時與每週限制及重設倒數計時、context 視窗列，以及色彩門檻.
- [barnabys-drew/claude-code-statusline](https://github.com/barnabys-drew/claude-code-statusline) - Claude Code statusLine——直接來自 hook payload 的 context 與 rate-limit bars，另可透過…
- [black-astro/claude-statusline-astro](https://github.com/black-astro/claude-statusline-astro) - Claude Code 狀態列——用一行顯示資料夾、分支、模型與使用量，最後是每天抽出一次的吉祥物。Windows、macOS、Linux 通用.
- [Chy-Zaber-Bin-Zahid/claude-code-statusline](https://github.com/Chy-Zaber-Bin-Zahid/claude-code-statusline) - 一個 Claude Code 狀態列，包含 context、5 小時與每週使用量 bars，各自採用不同形狀，方便你區分它們.
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude 在 Lua 中的 Code 狀態列，附帶即時 Neovim 操場。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 專業級 Claude Code 狀態列：工作階段時長、搭配 ECB 外匯的多幣別費用、每百萬權杖費率、支出上限。MIT、零金鑰、跨平台.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod 的 Claude Code 外掛程式，單一市集：適用於 Claude Code 的 agent skills 與即時窗格.
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Claude Code 的狀態列：內容、限制與本週進度、儲存庫的 CI、部署與 PR，以及你的機器。
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - VS Code 擴充功能：透過本機 IPC socket 的 statusLine 顯示 Claude Code 任務進度、預計抵達時間與速率限制配額。
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - 在 Claude Code 內預覽圖片：將游標移至回覆下方的標籤即可彈出圖片，或使用 /img &lt;path&gt; 在窗格中開啟圖片.
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Claude Code 狀態列：模型、5 小時／7 天配額列、每月支出列、cwd。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 將 Claude 的待辦事項同步至 Fizzy.do，讓團隊即時掌握進度，將任務轉為持久卡片，以提升協作效率並輕鬆追蹤進度.
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - 為 Claude Code 顯示詳細且具色彩編碼的狀態列，呈現內容、git 狀態、成本與速率限制.
- [KitchenSink4AI/claude-code-statusline](https://github.com/KitchenSink4AI/claude-code-statusline) - Claude Code 的內容量表：實際消耗速率、剩餘回合、速率限制，以及在撞上上限前而非之後升級的警示.
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - 適用於終端機程式碼代理的兩行狀態列：目錄、git、PR、模型、內容與 5h/7d 配額。不使用網路，不需要憑證.
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code statusline hook — 跨 sessions、compacts 與 --resume 追蹤 token usage 和…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Claude Code 狀態列，附帶適用於 Linux 與 Windows 上 Git Bash 的安裝程式。
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — macOS + Linux 的 Claude Code 狀態列.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - 從你的 macOS 選單列監控 Claude Code 狀態，以即時指示器顯示使用中的工作、待處理權限與經過時間.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 自訂 Claude Code 狀態列（上游：kamranahmedse/claude-statusline）。
- [sgarcia-dev/claude-agent-watch](https://github.com/sgarcia-dev/claude-agent-watch) - Codex、OpenCode、Antigravity、Hermes 與 Claude 子 Agent 的即時窗格與狀態列，這些子 Agent 由 Claude…
- [silee-tools/claude-statusline](https://github.com/silee-tools/claude-statusline) - 與寬度無關的 Claude Code 垂直堆疊狀態列 HUD。
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Code 的可攜式設定（狀態列 + 安裝程式）。
- [steemandavid/claude-code-statusline](https://github.com/steemandavid/claude-code-statusline) - Claude Code 的自訂狀態列——模型、內容與用量統計。
- [Synforger/claude-code-statusline](https://github.com/Synforger/claude-code-statusline) - Claude Code 的狀態列，一眼顯示速率限制與內容用量——單一基於 jq 的 shell 指令碼。
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Claude Code 的 4 行狀態列（context／rate limit／cost／git／worktree）。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 可攜式 Claude Code 設定：CLAUDE.md、settings、statusline、skills。
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Claude Code 的通用多協定 StatusLine、內容自我學習與 Dinotty 外掛。
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - 使用輕量且不依賴相依套件的終端機狀態列儀表板，追蹤 Claude Code 的內容使用量、工作階段成本與速率限制重設.
- [wcampbell-dw/claude-plugins](https://github.com/wcampbell-dw/claude-plugins) - Claude Code 外掛程式：即時子代理程式載入動畫、Nerd Font 狀態列，以及帳戶切換。
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - 多機同步 Claude Code 使用者層級設定（settings.json + statusline），GitHub / Gitee 雙源。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - 適用於 Claude Code Agents 的主動式 AI 記憶與速率限制監控器。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks、subagents 和 statuslines：開源集合與工具，按類型分類，並各自附有安全分級。English / 中文.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code 狀態列的視覺化建置器。在瀏覽器中設計終端機底部的列，然後貼上一個指令即可安裝.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 顯示即時 token 使用量與預估能源消耗的 Claude Code 狀態列。
- [lexfrei/ailine](https://github.com/lexfrei/ailine) - 具備來自 Anthropic API 真實使用限制的 Claude Code 狀態列。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - 適用於 Claude Code 的 Mods：基於 function hooks 建立的 panes、bands 與 buddies。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的 Claude Code 工作階段之間傳遞任務。將變更交給擁有某個 repo 的工作階段.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 這是在 MCP server 中控制 MODS 的工具；MODS 是適用於 Fablabs 的模組化跨平台工具，包含 CAD/CAM 與機器控制工具.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你一次又一次要求 Claude Code 執行的操作，並將其轉換為 mod。另附 8 個範例 mods 與虛擬辦公室.
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Claude Code 的 3 個 skills 函式庫：session-handoff、session-statusline 與 memory-audit…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用於翻譯 CK3 mods 的 Codex 與 Claude Code skill，搭配本機 LLM。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - 適用於 Claude Code 的開源 mods 與其他 extensions。

</details>

<a id="dsh-cordis"></a>

## DSH 與 Cordis 外掛生態系

DeepSeek Harness 與 Cordis 從不同方向抵達同一個位置：對它們來說，外掛就是模組機制，因此那裡的外掛就等同於這裡的模組。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74489 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74489**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐184903 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **184903** |
| Last push    | 2026-10-13 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100875 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **100875** |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82831 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **82831**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35774 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35774**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30656 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **30656**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25562 · Python · 🔎 inferred · 0 天</summary>

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
| Stars        | **25562**  |
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
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9157 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **9157**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8691 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **8691**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4532 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 官方首推的 TUI 插件——高性能、低占用、可爱的像素鲸鱼、流畅的鼠标交互。通过 npm 一键安装。/ DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4532**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3684 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

全球首個面向 AI Agents 的虛擬終端機

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3684**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3422 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

本地優先、開源的自我進化跨平台 AI 內容發現 Agent：先理解你，再主動從 B站、小紅書、抖音、YouTube、X、知乎、Reddit、微博等平台與開放 Web 尋找內容。（支援 deepseek harness 外掛） | 本地優先的開源跨平台 AI 內容發現 Agent：理解你之後，主動在 Bilibili、小紅書、抖音、YouTube、X、知乎、Reddit、微博與開放網路上尋找內容。（支援 deepseek harness 外掛）

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Python                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3422**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2064 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

最優秀的 DeepSeek Harness 上下文洞察與管理插件，提供上下文儀表板／瀏覽器／側邊欄與上下文命令，用於上下文統計、組成、拆解、演進詳情，理解上下文由何構成以及如何演進。一站式 DeepSeek Harness 上下文視覺化插件，Context 面板及瀏覽器和側邊欄與 Context 命令，透視上下文組成、演進、壓縮、剪枝等事件與動作。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2064**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1942 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

透過掃碼或機器人憑證把 IM 機器人接入 DeepSeek Harness（支援飛書、微信、釘釘、企業微信、QQ、Slack、Telegram、Discord 和 WhatsApp）。透過 QR code 或憑證將 IM 機器人連接到 DeepSeek Harness（9 個渠道）。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1942**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1185 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **1185**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/shengsheng90/DSH-taskboard">shengsheng90/DSH-taskboard</a></b> · ⭐334 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 的原生本地 Taskboard 插件。由 SQLite 驅動的專案、Agent 認領／審核，以及原生 Web UI — 無 iframe，無第二個聊天執行環境。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **334**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `task-management` · `taskboard`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/shengsheng90--dsh-taskboard/641e63303f0eed9c.png" width="100%" alt="shengsheng90/DSH-taskboard screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐231 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 換膚／桌布／主題包外掛 (dsh-plugin) — 8 套 Mirage 主題、每位使用者的強調色、桌布 2.0、主題包匯入匯出／分享連結、收藏與隨機選擇，完全以原生 token 系統實現。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **231**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐205 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **205**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐186 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **186**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐124 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **124**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐89 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

You.com 的技能與插件，適用於網頁搜尋、內容擷取、研究、金融與整合探索，協助 AI Agent 使用最新的網頁上下文進行建構。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **89**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-wsl-workspace-maintainers/dsh-wsl-workspace">dsh-wsl-workspace-maintainers/dsh-wsl-workspace</a></b> · ⭐80 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 的 WSL 工作區支援——無縫的 WSL 工作區使用體驗，不需要在 WSL 中再安裝一個 dsh。安裝此外掛後，在 GUI 中直接新增 WSL 工作區即可。DeepSeek Harness 的 WSL 工作區支援 — 享受無縫的 WSL 工作區體驗，不必在 WSL 內安裝 dsh。安裝此外掛後，即可直接從 GUI 新增 WSL 工作區。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **80**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-wsl-workspace-maintainers--dsh-wsl-workspace/252926072330fff2.png" width="100%" alt="dsh-wsl-workspace-maintainers/dsh-wsl-workspace screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

基於 Deepseek-Harness 核心底座打造的桌面版 Agent。繼承底座的全部能力，並補全 IDE 相關功能。

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
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

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
| Stars        | **59**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

面向 AI Coding Agent 的任務感知工作區上下文檢索與生命週期追蹤：按目前任務找到、組織並持續追蹤最相關的文件、程式碼與媒體。純本地、零模型呼叫、零網路。任務感知的工作區上下文檢索與生命週期追蹤工具，面向 AI coding agents。尋找、組織並追蹤與目前任務最相關的工作區上下文——在本地以確定性方式運作，零模型呼叫、零網路。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **54**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-plugin-guide">PerryLink/dsh-plugin-guide</a></b> · ⭐50 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (dsh) 插件開發知識庫：10 章開發指南、發布手冊、經來源驗證的未修復上游問題，以及實測生態系資料 — 可作為 DSH bundle 安裝。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **50**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `ai-agents` · `checker` · `cli` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/d665a08f58e38532.png" width="100%" alt="PerryLink/dsh-plugin-guide screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/3aee78fb7bcfc697.gif" width="100%" alt="PerryLink/dsh-plugin-guide animation"><br><sub>動畫錄影</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 外掛：一鍵匹配模型上下文視窗，顯示容量來源，支援勾選批次設定、既有視窗管理與手動編輯。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **34**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 工作階段導覽

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HaoyueQin/dsh-usage-statistics-panel">HaoyueQin/dsh-usage-statistics-panel</a></b> · ⭐23 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH web 插件：每日 token 使用量統計，包含 GitHub 風格活動熱圖、快取命中率曲線與各 model 分解

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | TypeScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `cordis` · `data-visualization` · `deepseek-harness` · `dsh-plugin` · `llm` · `plugin` · `react` · `settings-panel`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/haoyueqin--dsh-usage-statistics-panel/e57757e1005cbc5b.png" width="100%" alt="HaoyueQin/dsh-usage-statistics-panel screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/pptwise">liustack/pptwise</a></b> · ⭐21 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **21**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agent-skill` · `agent-skills` · `ai-agent` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deck-generation`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--pptwise/e6f193d6fc2ea355.png" width="100%" alt="liustack/pptwise screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KannaKuron/dsh-better-workspace">KannaKuron/dsh-better-workspace</a></b> · ⭐18 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH web 插件：側邊欄的階層式工作區樹 — 標題中包含 / 會分組成虛擬資料夾；add-workspace 流程新增父群組彈出視窗

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
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `sidebar` · `tree` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kannakuron--dsh-better-workspace/83cddff440dfe49a.png" width="100%" alt="KannaKuron/dsh-better-workspace screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vecnode/vncode">vecnode/vncode</a></b> · ⭐8 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

vncode 🤖 Agent-Human IDE ⌨️ Web 與 Desktop 版本，整合 Plugins、Skills 與 Interfaces。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-skills` · `deepseek-ai` · `deepseek-api` · `deepseek-chat` · `deepseek-harness` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vecnode--vncode/73837d3e9e3dc179.png" width="100%" alt="vecnode/vncode screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/unStone/dsh-xray">unStone/dsh-xray</a></b> · ⭐7 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 外掛的 X-ray：宣告的能力與實際行為。登錄庫 + 靜態掃描器 + 徽章。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | Python                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-security` · `ai-agents` · `ai-security` · `capability-analysis` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unstone--dsh-xray/35167f8867e8b79d.png" width="100%" alt="unStone/dsh-xray screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/alone-tree/dsh-skill-mcp-manager">alone-tree/dsh-skill-mcp-manager</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

能力庫 (Capability) — DSH Skills 與 MCP 的一站式視覺化管理：隨需 MCP 載入、會話內熱重載，以及可在外掛程式中檢視 SKILL/MCP 描述。

##### 📌 Basic facts

| Field    | Value                                               |
| -------- | --------------------------------------------------- |
| Category | `DSH 與 Cordis 外掛生態系`                          |
| Evidence | `宣告為模組、外掛程式或 hook，但未具體提及模組介面` |
| 語言     | JavaScript                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp` · `skill`

---

<table><tr><th align="center" width="50%">🖼 圖片</th><th align="center" width="50%">🎬 影片</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/alone-tree--dsh-skill-mcp-manager/bc0fce1b6eabef09.png" width="100%" alt="alone-tree/dsh-skill-mcp-manager screenshot"></td>
<td align="center" valign="top"><sub>尚未發布媒體</sub></td>
</tr></table>

</details>

<details>
<summary><b>此分類中的更多項目</b> <sub>· 64</sub></summary>

- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) - 用 HTML 回答我——一項能以一頁你真正讀得懂的 HTML 回答棘手問題的 Agent 技能。讓 AI Agent 用一頁 HTML 回答複雜問題.
- [anywhere-labs/Agents-Anywhere](https://github.com/anywhere-labs/Agents-Anywhere) - 跨裝置的開源 Agent 工作台。
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI 程式設計 Agent 的執行前防護工具。在工具呼叫執行前，阻止破壞性的 Git 和檔案系統命令，以及常見的敏感檔案存取嘗試.
- [LivXue/dsh-plugin-shop](https://github.com/LivXue/dsh-plugin-shop) - 最全面的 DeepSeek Harness 插件市場 — 每日更新，來源遍及網際網路，發布前經過審核.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - 為包含 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet) - 📚 一個零相依、由 git 支援的微課程函式庫，讓 AI Agent 非同步分享與搜尋經驗證的除錯經驗。 | https://misakanet.org。
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH 外掛 — DeepSeek Harness (DSH) 的免費 OpenCode Zen 模型。免費 LLM API，不需要 API 金鑰.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 外掛程式市場 / DSH Plugin Marketplace：在 DeepSeek Harness Web GUI 中一鍵瀏覽、安裝與更新全部…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 內建破甲 18+ 互動敘事：有真人感的 NPC（自主決策／拒絕迎合）、211 個世界與上萬份素材、開局隨心自訂、世界自行運轉、零漂移存檔.
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - 圖形學與 3DGS、空間智慧持續更新論文；適用於 3D Gaussian Splatting、NeRF 與 Computer Graphics…
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - 安裝即內建mattpocock/skills v1.3.1的27個工程與效率技能，無需手動安裝技能.
- [arcships/rutis](https://github.com/arcships/rutis) - 一個供會自我迭代的軟體使用的外掛執行環境 — 代理程式可在 Rust、TypeScript、Python 與 Go…
- [JingbiaoMei/Tokdash](https://github.com/JingbiaoMei/Tokdash) - Agent 儀表板：Sessions 與 Quota Usage 的視覺化與分析.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 外掛精選目錄——14 類 280+ 個社群外掛，涵蓋 MCP / Skill / TUI / 多 Agent /…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin：適用於 Windows 所有代理程式模式的 Git Bash shell（取代 pwsh executor）。
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：基於 DeepSeek Harness（DSH）的多平台群組聊天 Agent 系統｜由 DSH 驅動的多平台群組聊天 Agent 系統。
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh 安卓版：整合 DeepSeek Harness、Ubuntu 執行環境、插件與檔案管理，以及使用者授權的 Shizuku 和無障礙自動化.
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion：以助理和家的概念增強 dsh-im——哪個工作區有助理管理、是否在線一目了然，搬家拖一下就行.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 插件 · 傳送列一鍵「最佳化」提示詞草稿：五維診斷 + 改寫稿 SSE…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - 社群策展的 DeepSeek Harness (dsh) 插件、工具、技能與學習資源。可搜尋的雙語目錄 | DeepSeek 插件、工具與技能精選。
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A 商務談判執行環境 + DeepSeek Harness (dsh) 插件.
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - AI 爭辯。程式碼裁決。損失留在頁面上。一個由 Agent 操作的真實 HK + US 券商帳戶；Agent…
- [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) - DeepSeek Harness (dsh) 的讀取時專案記憶體外掛。
- [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) - DeepSeek Harness 插件：將對話自動沉澱為知識卡，搭配可搜尋知識庫 + 知識圖譜 + 審核中心；SQLite／純 Markdown…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - 經垃圾訊息過濾、以開放資料為基礎的 DeepSeek Harness (dsh) 外掛、套件組合與技能登錄庫.
- [realguan/dsh-dock](https://github.com/realguan/dsh-dock) - 專為 DeepSeek Harness (DSH) 打造的跨平台桌面控制中心：多工作台管理、3,400+ 社群外掛市集、工作階段自我修復、憑據與系統診斷.
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 外掛：基於知乎開放平台官方 API 建立的站內搜尋、全網索引搜尋與直接回答三項工具。搜尋不產生幻覺，引用有出處。（原生嵌入「設定-外掛-外掛設定」）。
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 插件的常時相容性測試：精確版本、隔離 runners，以及可修復的上游問題.
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - 修復拒絕載入的 DeepSeek Harness 工作階段。修好打不開的 DSH 工作階段檔案.
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - DeepSeek Harness (DSH) 的精選外掛、工具、換膚與擴充功能清單.
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 外掛：Web GUI 中的 IDE 風格 Git 面板——分支／提交歷史總覽、變更提交與…
- [jiangnanquan/dsh-ux](https://github.com/jiangnanquan/dsh-ux) - DSH Web UI 增強插件 + 無邊框 Electron 桌面外殼。
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 外掛：將 WorkBuddy 桌面 App 中的模型接入 DeepSeek Harness，零設定即可使用。（原生嵌入「設定-外掛-外掛設定」）。
- [EdwinZDZ/dsh-api-balance-ring](https://github.com/EdwinZDZ/dsh-api-balance-ring) - DeepSeek Harness 編輯器的即時 DeepSeek API…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多資料夾 workspace：讓 DSH（DeepSeek Harness）的 Agent 不只能讀寫主目錄，還能同時讀寫你新增的其他資料夾.
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - DeepSeek Harness 外掛生態的雙語、具來源支援的登錄庫與安裝程式.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH 外掛：IDE 等級的 Git 工具視窗，作為原生 dsh-better-sidebar 分頁 — 分支樹、提交圖、變更、提交詳細資訊與…
- [mjylfz/dsh-skill-mover](https://github.com/mjylfz/dsh-skill-mover) - 將其他 Agent 的技能一鍵搬進 DeepSeek Harness：支援 14 個平台 + 共用層識別、同名技能合併、不重複搬運、可回復.
- [xiaoso456/dsh-workflow-lite](https://github.com/xiaoso456/dsh-workflow-lite) - DeepSeek Harness 的軟工作流程外掛：在畫布上設計流程，編譯成計畫提示詞，由模型依計畫執行；執行狀態由模型自行記錄，沒有執行引擎。
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - 看清 AI 編碼代理的每一次可觀察行動。 · 追蹤你的代理，深入到每個工具與 MCP.
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - DeepSeek Harness Personalization Settings 外掛程式用於設定 Agent 的暱稱、回應風格、語氣與自訂命令.
- [cv-superding/dsh-webin](https://github.com/cv-superding/dsh-webin) - 非官方 DSH 外掛程式：透過 DSH 自己的 Chromium webview guest，在真實瀏覽器中驅動 AI web UI…
- [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) - 第三方適配外掛：將上游 REA（逆向一切，github.com/morluto/rea）的 MCP 服務註冊到 DeepSeek Harness，取得…
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - DSH 外掛程式集合：用於 dsh web LAN/Tailscale 存取的密碼驗證 + 信任 (dsh-web-auth) 等.
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 讓 DeepSeek Harness Agent 擁有操作 GitHub 的原生手腳!
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) 外掛程式的零相依性驗證標準——靜態結構閘門 (R)、cordis 合約檢查 (K)、沙箱冒煙測試…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness 外掛生態系：101 個儲存庫組成的家族中有 86 個開源外掛，其中 100 個由 PerryLink…
- [SuCriss/dsh-leekbox](https://github.com/SuCriss/dsh-leekbox) - 韭菜盒子 LeekBox — A股看盤助手 · DeepSeek Harness (DSH) Web 外掛。
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness（DSH）Web 外掛：盯盤 market-dashboard 側邊欄分頁——三條附滑入日內圖表的報價列、含產業 alpha…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode — 讓 OpenCode Zen + Go 免費方案模型持續運作的 DSH…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness 的第三方外掛市集與受防護生命週期管理器.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人為本且可擴充的桌面工作台：對話、筆記、試算表、檔案位於同一工作台；自建伺服器即可啟用多人即時協作.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness 的全配 coding agent — Claude Code…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH 外掛：在左側邊欄底部顯示你的 DeepSeek 帳戶餘額（原生 UI）。
- [iluluyu/dsh-ui-outline](https://github.com/iluluyu/dsh-ui-outline) - DeepSeek Harness (dsh) Web 的 ChatGPT 風格右側邊緣回合導覽外掛。
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh)…
- [Wenston-dev/awesome-dsh-plugin](https://github.com/Wenston-dev/awesome-dsh-plugin) - Awesome dsh 外掛清單 — 自動化 DeepSeek Harness 外掛目錄.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness plugin：將 Windows sandbox ACL 佈建失敗。
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - 針對未宣告截止期限的 dsh 工具呼叫設定部署層級的截止期限：它掛載於 tools/execute 瀑布流上，將無聲卡住的工具呼叫轉換為模型可見的…
- [fshoocn/cordis-port](https://github.com/fshoocn/cordis-port) - Cordis 核心套件的 Python 移植 · 外掛程式化執行階段 / 依賴注入 / 事件匯流排 · Python port of…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Cordis / DeepSeek Harness 外掛——供 AI 代理程式使用的標準化 GitHub API 工具。
- [majiayu000/dsh-desk](https://github.com/majiayu000/dsh-desk) - 可安裝的 Tauri 桌面版 DeepSeek Harness，內建執行環境、可信賴的插件審核及每日相容性檢查.
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin。
- [LittleCar30/dsh-deepseek-web](https://github.com/LittleCar30/dsh-deepseek-web) - 用專用的真實瀏覽器操作 DeepSeek Web 的獨立 dsh 桌面外掛。

</details>

<a id="writing"></a>

## 文章、討論與影片

關於模組功能的文章、討論與影片。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
| TypeScript | 296  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 72   | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 45   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 25   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13   | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 6    | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                               |
| Go         | 4    | `mitre/claude-statusline`, `lexfrei/ailine`, `esengine/DeepSeek-Reasonix`                                     |
| PowerShell | 2    | `markallisongit/claude-statusline`, `czcdr/dsh-plugin-rea`                                                    |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1    | `dphmoblie/deepseek-harness-android`                                                                          |
| Lua        | 1    | `crafts69guy/claude-statusline.nvim`                                                                          |
| Swift      | 1    | `peaceinitiativemenhadenoil263/claude-status-bar`                                                             |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

歡迎提供修正，這是改善此清單最快的方式。如果某個項目被錯誤分類、評等有誤，或某個專案因名稱衝突而被錯誤排除，請建立 issue 或提交 pull request——最後一類是自動篩選最可能出錯的地方。

---

<sub>獨立的社群專案。與 Anthropic 無關聯，也未獲其背書或審查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商標。產品行為可能在未通知的情況下變更；任何關鍵內容都請以官方文件為準。資產仍歸其上游專案所有，僅在授權允許的情況下重製。</sub>

<sub>Last updated · 2026-10-13T21:42:20+08:00</sub>
