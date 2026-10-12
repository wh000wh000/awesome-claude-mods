<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="精选 Claude Mods">
</p>

<h1 align="center">精选 Claude Mods</h1>

<p align="center"><b>Claude Code mod、插件及其所改变的更深层行为的循证分级索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-593-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <b>简体中文</b> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **实时索引** · 上次同步: `2026-10-13T04:10:27+08:00` (UTC+8)
> · 条目: **593** · 最新更新中新增: **0** · 实现语言: **12**

<sub>以下每个条目均已自动收集、筛选并重新检查。这里没有付费展示内容。</sub>

<a id="featured"></a>

## 当下精选

<sub>每个类别精选一项，按证据等级和星标数排序，并在每次更新时重新计算。这是一个排名，不代表认可；每项精选都会链接到下方的完整卡片。优先选择发布了截图或录屏的项目，以便保持列表的视觉呈现。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9484 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods">
<b>🧩 <a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b>
<sub>⭐208 · TypeScript · 👁️ observed</sub>
<sub>Claude Code mods：基于钩子构建的插件，可在提示词上方添加实时行、防护、面板和游戏。上下文栏、使用量计、Codex 审查监视器、Markdown 预览、Spotify 正在播放等。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74429 · TypeScript · 👁️ observed</sub>
<sub>🌊 原创 agent harness。部署智能多玩家群体，协调自主工作流，并构建对话式 AI 系统。具备自适应记忆、自学习智能、联邦、向量 RAG 集成，以及原生 Claude Code / Codex / Hermes 和更多集成</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## 目录

- [什么是 Claude Code mod](#什么是-claude-code-mod)
- [条目的分级方式](#条目的分级方式)
- [官方：Anthropic 自有的仓库和发行说明](#官方anthropic-自有的仓库和发行说明) — **16**
- [Mods：使用 mod 能力构建](#mods使用-mod-能力构建) — **467**
- [DSH 和 Cordis 插件生态系统](#dsh-和-cordis-插件生态系统) — **99**
- [文章、讨论与视频](#文章讨论与视频) — **11**
- [按实现语言分类的项目](#按实现语言分类的项目)

## 什么是 Claude Code mod

Claude Code 在 2.1.287 中获得了**模组**：它们能够改变比插件更深层的行为，并绘制自己的界面。

模组可以挂接到 `ui.render`，在提示周围绘制**行、带区、窗格或卡片**；通过 `$.ui.selection()` 读取你最近选择的文本；通过 `agent.spawn` 派生队友；并拥有一个 `Client` 区域。无法绘制的模组只会自行失败——`ui.fault` 会阻止一个故障模组拖垮整个会话。

此列表涵盖模组、它们所构建于其上的插件与钩子接口，以及 DSH 和 Cordis 中的对应功能。列表特意**不**涵盖更广泛的 Claude Code 生态：提示词包不是模组。

## 条目的分级方式

这个领域的大多数列表只会声称某项内容应被收录。本列表会说明实际核验到的程度，然后让你据此筛选。等级描述的是证据，而不是项目质量——一个尚未有人撰文介绍但构建良好的模组，仍然只是 `inferred`。

| 等级                                             | 含义                                                                                                                                                    |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `由 Anthropic 自行发布`                          | 由 Anthropic 自行发布，或直接读取自官方更新日志。                                                                                                       |
| `其自身文本提到模组 API，或声明支持模组功能`     | 其自身文本提到模组接口的一部分——`ui.render`、`ui.fault`、`agent.spawn`、`$.ui.selection()`、窗格、带区或卡片——因此作者描述的是基于真实 API 构建的内容。 |
| `声明支持模组、插件或钩子，但未具体说明模组接口` | 它自称是模组、插件或钩子，但文本中没有具体提到模组接口。确实存在，但尚未确认。                                                                          |
| `仅凭词汇匹配`                                   | 仅凭词汇匹配。收录它是为了让筛选过程可审计，而不是因为认为它可信。                                                                                      |

<a id="official"></a>

## 官方：Anthropic 自有的仓库和发行说明

Anthropic 自有的 Claude Code 代码仓库，以及定义 mod 接口的各个版本发布。直接阅读源内容，而不是摘要。

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150402 · TypeScript · ✅ official · 1 天</summary>

##### 📝 摘要

Claude Code 是一个存在于你的终端中的代理式编码工具，能够理解你的代码库，并通过执行常规任务、解释复杂代码以及处理 git 工作流来帮助你更快地编码——这一切都通过自然语言命令完成。

<sub>🔧 在代码中发现使用: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |
| 语言 | TypeScript                             |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **150402** |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9484 · TypeScript · ✅ official · 3 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |
| 语言 | TypeScript                             |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **9484**   |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8255 · Python · ✅ official · 3 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |
| 语言 | Python                                 |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **8255**   |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6351 · Python · ✅ official · 243 天</summary>

##### 📝 摘要

一个由 AI 驱动的安全审查 GitHub Action，使用 Claude 分析代码变更中的安全漏洞。

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |
| 语言 | Python                                 |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **6351**   |
| 最后推送 | 2026-02-11 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1800 · Shell · ✅ official · 3 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |
| 语言 | Shell                                  |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1800**   |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

##### 📝 摘要

Claude Model Cards 的补充材料

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **25**     |
| 最后推送 | 2025-12-05 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 摘要

新增 Claude Mods：插件现在可以修改更深层的行为。新增 You should know，这是一个内置 mod，由侧边代理为你留意并标记你或 Claude 可能忽略的事项。使用 `/plugin enable cc-plugin-you-should-know@builtin` 启用（适用于已开启遥测的第一方会话）

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 摘要

为 mods 新增 `$.ui.selection()`：全屏模式下返回你上次选择的文本；当选择内容位于单个转录行内时，还会返回该行。修复某个 mod 的按钮在之前绘制的视图上按下时，有时会执行另一个按钮的操作，而 Claude Code 已重启。修复插件或 mod 在提示词上方显示行时，打开后台任务对话框会导致全屏会话以“unrecoverable interface error”退出。修复 `claude plugin test` 在远程关闭 mods 时报告 mods 已关闭，而实际情况只是读取了过时的保存设置

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 摘要

修复了复合 shell 命令嵌套部分中的 deny 或 ask 规则在受管机器上无法继续适用于用户安装的 mod 批准的问题 修复了升级后已安装 mod 未在首次会话中加载的问题 为队友添加了 `agent.spawn`，在插件钩子事件中使用一个代理 id，并在 `$.agent.list()` 中添加了空闲和等待状态 修复了当某个 mod 的 `ui.render` 钩子写入的值导致某行在绘制时抛出错误而使会话以“unrecoverable interface error”结束的问题；引擎现在会改为绘制自己的行 修复了 mod 窗格或条带中的右对齐内容绘制在关闭标记或 `\[-\]` 下方的问题，wh

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 摘要

向 mod 的 `turn.step` hook 的结果添加了 `serverToolUses`：工具调用了 API 自身运行的内容（advisor），每个都带有其 id、名称、输入、开始和结束 向 mod 的 `tool.check` hook 读取的问题和裁定添加了 `ceiling`，命名组织对工具所需的批准 向插件 hook 类型添加了 `ThemeKey` 和 `Color` 类型，因此编辑器会列出 mod 绘制可命名的主题颜色 添加到 `claude plugin validate`：mod 在 gating site 注册的每个 hook 都会列出是否具有 `.catch`（`--json` 下的 `gatingHooks`） 修复了 mod 的 `turn.step` 结果

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 摘要

添加了 `prompt.autocomplete`，这是一个事件，mod 可挂钩它以向提示框的自动完成列表添加自己的行；为 mod 向 `$.model.complete` 添加了提示词缓存：`prompt` 和 `system` 接收文本块，而块上的 `cache: true` 会缓存到该处为止的请求；向 `agent.spawn` mod 挂钩添加了工作流 agent，包含其运行和索引，因此 mod 可以拒绝它们；修复了 Write、Edit、NotebookEdit 和 LSP 行，以及单个 Read、Grep 和 Glob 行，隐藏 mod 拒绝调用的原因：该行现在显示原因；修复了拒绝 afte 的 mod 的 `config.set`、`state.set`、`env.set` 或 `agent.spawn` 挂钩

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 摘要

已将 `isDeferred` 添加到用于 mod 的 `$.tool.register`：`false` 从一开始就在提示词中列出工具的 schema，而不是隐藏在工具搜索后面 修复了插件 hooks worker 重启期间跳过 mod 在 `classic.*` 事件上的 hooks 的问题，这导致设置 hooks 在没有这些 hooks 的情况下进行响应 修复了调用 `$.session.append` 的 mod 中 `claude plugin test` 失败的问题；测试现在可以使用新的 `mock.session` 读回追加的行

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

官方 DeepSeek Harness MCP 客户端的 MCP 管理控制台：带健康诊断和流水线试调用的 /mcp 命令、带服务器 CRUD（需批准写入、自动备份）的 Settings MCP 标签页，以及基于官方工具流水线的工具试用控制台（Apache-2.0, dsh-plugin）。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `官方：Anthropic 自有的仓库和发行说明`           |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **74**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-ticktick">PerryLink/dsh-ticktick</a></b> · ⭐4 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向 DeepSeek Harness 的 TickTick (Dida365) 任务桥：Session-header 任务面板（列表过滤、未完成/已完成视图、搜索、拖拽重排）、11 个精选 agent 工具、settings 卡片，基于官方 TickTick MCP endpoint。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `官方：Anthropic 自有的仓库和发行说明`           |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **4**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dida365` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/aa581021cb97f4dd.png" width="100%" alt="PerryLink/dsh-ticktick screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/44088595da097cb2.gif" width="100%" alt="PerryLink/dsh-ticktick animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 为 mods 添加了 `$.ui.notify`：通过你自己的通知设置发出原生通知，并说明发送通知的频道为 mod 的 `Button` 添加了子项：字符串和…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 修复了 `UserPromptSubmit` 钩子或模组的 `prompt.submit` 钩子期间按下 Esc…

</details>

<a id="mods"></a>

## Mods：使用 mod 能力构建

此处的每个条目都展示了使用 Claude Code 在 2.1.287 中获得的能力的证据：通过 `ui.render` 进行绘制，拥有窗格、横条或卡片，读取 `$.ui.selection()`，通过 `agent.spawn` 生成协作者，或明确说明自己是 mod。

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐527 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

公共 Claude Code 模组的社区目录，从 GitHub 扫描而来，并注明每个模组可以读取、写入、运行或通过网络发送的内容。浏览 https://mods.aidojo.si/

<sub>🔧 在代码中发现使用: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **527**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐208 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 摘要

Claude Code mods：基于钩子构建的插件，可在提示词上方添加实时行、防护、面板和游戏。上下文栏、使用量计、Codex 审查监视器、Markdown 预览、Spotify 正在播放等。

<sub>🔧 在代码中发现使用: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **208**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐159 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 摘要

在休息期间保持 Claude Code 的提示缓存处于温热状态，并在冷发送前显示预计成本。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **159**    |
| 最后推送 | 2026-10-04 |
| 首次列入 | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>动画录屏 · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">打开视频</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐146 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code 可直接在终端中显示图片和播放视频：屏幕截图、Playwright 录制，以及同步的前后 QA。支持 Ghostty 和 kitty。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **146**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐117 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Skins for Claude Code: tool rows with icons, diff, table and Mermaid chart cards, a usage band and fifteen themes. /skin swaps them live.

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **117**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

色彩丰富、可主题化的 Claude Code 回复：表格、代码、图表、图形和工具行，提供 15 种主题及复制按钮。一个 Claude Code mod。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **88**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 摘要

claude code mods 集合

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **78**     |
| 最后推送 | 2026-10-08 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

一款 Claude Code 模组，在终端中显示实时代理仪表板：上下文和费用、顾问时间线、每次权限检查、子代理卡片和泳道。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **74**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

##### 📝 摘要

Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens. 台股／美股看板 + more to come.

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | HTML                                         |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **65**     |
| 最后推送 | 2026-10-05 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 5 天</summary>

##### 📝 摘要

适用于 Claude Code 的专家技能、代理、命令、规则、钩子和输出样式——会话连续性 + 面向真实开发工作流的现代 CLI 工具

<sub>🔧 在代码中发现使用: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | Shell                                        |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **62**     |
| 最后推送 | 2026-10-07 |
| 首次列入 | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐55 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 摘要

100 多个可与 Claude Code 配合使用的 mods 集合。

<sub>🔧 在代码中发现使用: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **55**     |
| 最后推送 | 2026-10-03 |
| 首次列入 | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 摘要

Claude Code mods：在提示词上方显示实时计划进度条

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **47**     |
| 最后推送 | 2026-10-08 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>动画录屏 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">打开视频</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 摘要

观看 Claude Code 在你工作时生成一幅小卡通。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **32**     |
| 最后推送 | 2026-10-02 |
| 首次列入 | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 摘要

Claude Code 会话提示词的侧栏：悬停阅读，点击跳转（函数钩子 / Mods）

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **28**     |
| 最后推送 | 2026-10-03 |
| 首次列入 | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

生活在 Claude Code 提示词上方的像素风 Pokémon

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **25**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐24 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

让 Claude Code 焕然一新：实时驾驶舱面板、可分享主题，以及一个会演示 Claude 正在做什么的像素宠物

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **24**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 摘要

在 Claude Code 中使用 Xcode 的构建、测试、控制台和 SwiftUI 预览

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **20**     |
| 最后推送 | 2026-10-02 |
| 首次列入 | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 摘要

Claude Code mods: 21 styles and a full set of features you turn on when you need them, for the terminal and the desktop app. · 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **20**     |
| 最后推送 | 2026-10-04 |
| 首次列入 | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 摘要

十个 Claude Code mods、入门指南、创建提示词、安全演示以及一个自建模板。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **20**     |
| 最后推送 | 2026-10-02 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code mod：在提示词上方预览粘贴的图像和长篇粘贴文本

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **19**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐17 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code mod：Clawd 在提示词上方演示 Claude 正在做什么

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **17**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐15 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 摘要

两个 Claude Code mods：Codex computer-use 桥接器和协调的 Claude 会话。源代码、构建提示词、设置和测试。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **15**     |
| 最后推送 | 2026-10-05 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 摘要

Claude Code mods：usage-band 在提示词上方显示你的 5h/7d 限制、上下文窗口和缓存命中率

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **13**     |
| 最后推送 | 2026-10-03 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 摘要

Claude Code mods：让 Claude 的问题更易于阅读和回答（qa-guide）。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **12**     |
| 最后推送 | 2026-10-07 |
| 首次列入 | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>动画录屏 · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">打开视频</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 摘要

Claude Code mod：在提示上方的一条栏中显示以 token 计的上下文、5 小时和每周限制与时钟对比、提示缓存倒计时、会话成本和正在运行的智能体。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **12**     |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 摘要

适用于 Claude Code 的十个开源 mods：实时面板、条带、状态行和工具调用防护。消耗计、启动代码、会话回顾、Boss 战、代码宠物等。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **12**     |
| 最后推送 | 2026-10-03 |
| 首次列入 | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 摘要

在你的 Claude Code 提示词上方显示动态像素画，并在 Claude 工作时做出反应。七个场景，也可以使用你自己的图像或 GIF。零令牌。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **10**     |
| 最后推送 | 2026-10-04 |
| 首次列入 | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

##### 📝 摘要

以 mods 形式构建的 Claude Code 会话追踪器：上下文窗口、计划配额消耗率、每轮成本

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **9**      |
| 最后推送 | 2026-09-15 |
| 首次列入 | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

围绕你的 Claude Code 和 Codex 终端构建的 UI，由你的代理打造，因此你脑海中的唯一模型就是你自己的模型。

<sub>🔧 在代码中发现使用: `CLAUDE.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **9**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 摘要

KOZMOS ——适用于 Claude Code 的实时可视化 mods（CLI + 桌面端）：提示词上方的条带、侧边栏、状态滚动条、伙伴、防护和声音。

<sub>🔧 在代码中发现使用: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **9**      |
| 最后推送 | 2026-10-10 |
| 首次列入 | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 摘要

一个插件中包含六个 Claude Code mods（Token Weather、Cache Keeper、Wait What、Prompt Queue、Snake、Blast Radius），支持逐个 mod 切换，另附 mods 与 hooks 对比报告。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **8**      |
| 最后推送 | 2026-10-04 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 摘要

개발동생 的 Claude Code mods 集合。出租车套件：计价器、导航、测速摄像头、行车记录仪

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **8**      |
| 最后推送 | 2026-10-04 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">观看平台 youtube.com</a> · 播放将在托管网站上打开；GitHub 无法在页面内嵌入</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

你的计划，正在自我观察。本地桌面路线图树，Claude Code 和任何 MCP host 都会实时保持更新。纯 JSON，无云。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **8**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐8 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 摘要

让 Claude Pro 计划持续更久：用于精确使用量 HUD、更短 shell 输出且不重复读取文件的 Claude Code mods。这些 mods 消耗零令牌。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **8**      |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 433</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其构建工具：先使用构建器技能，然后使用 mods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天运行的 Claude Code harness，自第一天起就以此名称发布，如今与 ucsandman/Agnostic-AI…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）。
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad 的 Claude Code mods：窗格、条带、提示词保护、密钥处理和记忆工具。一个市场，每个 mod 独立安装.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四个 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 和 Collision Guard。
- [HolyGrail/claude-mods](https://github.com/HolyGrail/claude-mods)
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods：在 Claude 读取提示词前修正并翻译它们。
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 来自 Nekyia Labs 的 Claude Code mods 和技能，由生活在持久化家园中的 AI 每天构建和使用。
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 关于 Claude Code mods 的有来源引用的 Obsidian 知识库：它们的工作方式、构建方法，以及安装前的检查方法.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Claude Code 的驾驶舱：实时计划条、子代理条、带重置倒计时的用量限制、模型路由和一个小宠物，都位于提示词上方。CLI 和 Desktop.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 为 Claude Code 的终端记录提供桌面应用外观的 mod。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的侧边面板：显示会话运行的子代理、每个子代理正在做什么及其令牌，并可一键查看其对话.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教会 Claude Code 代理构建 Claude Mods（函数钩子插件）的技能，附带入门示例。
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods：Claude Tools 菜单、Zen 模式、终端主题、工作量和模式控制。
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社区 Claude mods、插件和技能，可从一个市场安装。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 适用于 Claude Code 的 Claude Mods（函数钩子插件）.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods 画廊：经过检查并固定的 Claude Code mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 面向与对话代理协作的人类用户的决策队列 CLI/TUI。代理发布问题，人类从一个收件箱中回答.
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - 在 kitty-graphics 终端中内嵌绘制图表、LaTeX 数学公式和工具结果图像——一个 Claude Code 插件。
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code 修改插件，在两列并排布局中绘制 Edit 和 Write 差异。
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - 输入时将 Markdown 绘制到 Claude Code 的提示框中。即使你还没闭合围栏，围栏代码也会先变成语法高亮卡片.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf。
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code 的浮动状态卡片——模型、上下文、速率限制、成本、分支——另有一个任何脚本或模组都可以提供进度的 API。
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code 的 Mods：为终端 UI 添加实时窗格和行为的函数钩子插件。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard 在屏幕共享时遮盖姓名和机密信息；cache-panel 会在提示词缓存即将失效前提醒你.
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code 扩展。释放 Claude 的全部力量.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod（插件），添加一个带 Activity、Files、Agents、Context 和 MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code 的面板、防护栏和生活质量 mods：上下文、使用量、实时活动、通知、安全规则、提示词教练、命令中心.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示词框上方的两个 Claude Code mods：上下文窗口计、5 小时限制、提示词时钟和会话成本。
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 读取 Claude Code 命名的 markdown 文件，并将其渲染在会话旁边；指向任意代码块即可让 Claude 编辑它.
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude 正在火热进行。与你的小队聊天。朋友在线，就在你的 Claude Code 会话旁边。零 token，零泄露给 Claude.
- [Danovich/turntype](https://github.com/Danovich/turntype) - 在 Claude 工作期间进行的打字测试。一个 Claude Code mod.
- [gixxy22/hide-diffs](https://github.com/gixxy22/hide-diffs) - Claude Code mod：用单行摘要替代完整 diffs，ctrl+q 切换。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在任意终端中将粘贴的图像缩略图显示在提示词上方。
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的语音协作者。与由 ElevenLabs conversational AI 驱动的 3D…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow for Claude Code: a calm checklist above the prompt showing the plan…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：上下文栏、代理面板、PDPA 模糊处理。
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed，一款带有每条提示统计信息的实时打字速度计。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - 用于 Claude Code 的烟花：每次按键、工具调用、提交和绿色测试都会在提示上方升起盲文烟花。一个 Claude Code mod.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 的 mods：使用插件函数钩子API构建的窗格、命令和钩子。
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 探索Claude Code mods、插件和扩展，浏览动画演示、分类列表和直接源代码链接。由 FindMods.dev 提供支持.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：在记录中内联绘制 mermaid 图表。
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code 的 Mods 和 skins：为 Claude 的任务提供实时进度条、带匹配 Windows Terminal…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code 修改插件（函数钩子插件）：session-switcher 及更多。
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 六个 Claude Code…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout（查找你最常使用的 mods）、usage-meter、check-ledger、resume-nudge。
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 用于同时运行多个会话的两个Claude Code mods：提示词上方的上下文卡片和聊天旁边的会话窗格.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 按需生成 Claude Code 模组——一种读取你的对话并构建合适模组的技能：计划进度条、文件窗格、上下文仪表、危险命令防护、测试监视器.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：发现、检查、切换和更新Claude Code mods。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最佳Claude Code Mods：精选、已验证、已置顶。一次 /plugin marketplace 添加，包含 43 个 mods.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 插件：自动进行 Claude 模型路由。为每条提示词、步骤和子代理选择 Haiku、Sonnet 或 Opus…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod：会话打开或推送到的 GitHub PR 的实时窗格——CI、评审、冲突、合并——所有会话共享一个轮询器.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code 的六个 mod：动画 Clawd 吉祥物、用量限制和提示词缓存条、发送前消息检查器、快捷回复、待办队列和成本账本.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code mods 的 app store，位于 Claude Code 内：/mods 可浏览、搜索并安装 2,700 个 mods，或让…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code 的 mods 市场：代理循环单步调试器、git 账户提示、工作树状态行等.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - 适用于 Claude Code 的开源 mods：面板、状态栏、提示、工具防护和斜杠命令.
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 的最佳全能模组包：用量限制和上下文 HUD、针对 rm -rf 和 git reset --hard 的带撤销保护、.env…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - 在你的 Claude Code 中播放 YouTube Shorts 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren 的 Claude 工具包：适用于 Claude Code 的技能、模组和 MCP 服务器。通过插件市场一键安装.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 的 mods：Clawd，一个会演示Claude正在做什么的小型像素吉祥物。
- [reporails/arcade](https://github.com/reporails/arcade) - 经典桌面游戏作为Claude Code mods，在Claude工作时于窗格中运行。由 Reporails 制作.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - 用于 claude 的 code-mods。
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca。
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精选的 Claude Code 模组列表，可作为插件市场安装：主题、窗格、状态栏、肖像.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 两个 Claude Code mod：cache-keeper 和 ctx-mod。
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - 由沉迷于 harness engineering 的 Rustacean 设计的、极具主见的 Claude Code 插件。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 让代理保持诚实的Claude Code mods——用于守护范围、验证部署并在提示词上方绘制会话的函数钩子.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code 的 mod：提示词缓存栏、后续步骤、快捷按钮和更改回放——可从 marketplace 安装。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 一个 Claude Code mod，会在提示上方的条带中绘制你的使用限制和支出.
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - 在 Claude Code 中实时查看 GitHub PR 状态、合并就绪情况、检查、评论和提醒。
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（marketplace herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods：计划进度条、记录Claude留下的运行中任务的账本，以及工具输出的令牌屏蔽。
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在后台运行的内容：子代理、Codex 作业、shell、监视器、cron 作业和工作流.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - 关于 Windows 上 Claude Code mod 的首日现场笔记：上下文/配额燃料条、泰语 UI mod、Matrix…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools：用于调试 Claude Code 工具调用的调试器.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code mod：在信息条和窗格中实时显示 GitHub 拉取请求状态（检查、审查、讨论串、合并队列），并提供已确认的合并操作.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - 位于 Claude Code 提示下方或全屏时停靠在记录旁的小卡片。每个小组件都是独立模组，可通过斜杠命令切换.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：在提示词上方显示实时成本、上下文和计划配额计量器。图标需要 Nerd Font.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 我们正在制造一些 TECHNO 宝贝 😈。
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 插件和 mod：一个 AI 原生 SDLC（意图 → 规格 → 计划 → 构建 → 验证 → 评审），带有通过 hook…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 一个 Claude Code 修改插件，可通过命名配置文件按仓库启用或禁用全局技能、agents、规则和工具.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 经过测试、可一键安装的 Claude Code 模组：YOLO 模式防护、实时成本和上下文、窗格、宠物等。另附精选的最佳社区模组列表.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code 的舒适 RPG HUD mod（测试版，优先支持桌面应用；计划支持 CLI）：多职业 Clawd…
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 我制作的一批 claude code mods。
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods：代理群组仪表板和自动驾驶（local-mods marketplace）。
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code 模组。touch-map：以树状图和活动地图查看 Claude 列出、读取、编辑或创建了哪些文件.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - 使用 Claude Code 工作时学习一门外语。
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code 模组，实时报告 Claude 修改了哪些文件及原因、子智能体状态，以及剩余的计划限制。
- [0xctx/sysop](https://github.com/0xctx/sysop) - 告诉 Claude 你想要什么。获得构建、测试、经另一 AI 审查并合并后的结果.
- [20alexl/windvane](https://github.com/20alexl/windvane) - 替你照看漫长的 Claude Code 会话：监视上下文填充情况，起草检查点，在合适的时机压缩，并恢复工作。每个子代理中都有规则，还有项目记忆.
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - 一个 Claude Code mod，让你的提示词缓存在人离开时保持温热.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - 用于 Claude Code 的实时成本、token 和上下文用量侧边栏：一个在会话内显示每轮成本、缓存命中率、消耗速率和 30 天支出的 mod.
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - ayagmar。
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Claude Code 的函数钩子模组：限制遥测行、多选问题和后续步骤面板，以及每次提交后的 README 更新.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 面向真正工程师的 Claude Code mods。
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code&#x27;s terminal session recap, in the Claude desktop app&#x27;s Code tab。
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - 一个 Claude Code mod：包含会话任务、需要你处理的事项、你的上一条提示词和已保存解释的窗格。
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - 一个 Claude Code mod：在 Claude 工作时，于放置类游戏中捕捉像素艺术 Modsters.
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss 制作的 Claude Code 模组。
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每个 Claude Code 代理在其上下文中有哪些文件，以及每个文件占多少.
- [deejay-hub/sf-headless-band](https://github.com/deejay-hub/sf-headless-band) - 用于 Salesforce 的 Claude Code mod，显示哪些 Org 已连接。
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 用于终端和桌面应用的 Claude Code 小型 mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI 技能 + mod，可在 agent 回复中加入西班牙语单词。
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Claude Code 模组，帮你避免重写提示缓存：/keepwarm 让缓存持续到休息结束，提示上方的实时倒计时显示缓存何时过期，/tokens…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code 提示词上方的 Alarum 事件：刚刚到达的内容，以及一键将其交给代理.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - 你的 Floatee 待办事项列表显示在 Claude Code 的提示词上方：一键运行、指导并勾选你的 todos.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 用于在工作中途记录想法、跨项目和机器整理想法，并将其转换为提示词的 Claude Code mod。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 一个将其重新设计为《疑犯追踪》中的 The Machine 的 Claude Code mod.
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Code mod（CC tint mod）：根据代码库为每个窗口着色，为当前窗口加环，给线程编号，并为整个 Claude 桌面应用着色.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod：会话状态、实时 Spec Kit 进度和使用窗口治理。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 上下文窗口作为提示上方的一行，按照 Claude Code 绘制其自身仪表的方式绘制.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 的实时任务 HUD：Claude 工作时显示在提示上方的条带，点击一次即可打开完整仪表板.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code 插件（mod），让 Claude Code 终端界面看起来像 Claude 桌面应用：提示气泡、Markdown 表格、mermaid…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - 在等待 Claude Code 的回答时，不要让注意力飘走.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - 一个插件中包含十四个 Claude Code mods，每个都可切换，并提供用于管理、配置和导入 mods 的窗口.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - 一个免费的开源 Claude Code 插件。在你执行 /clear 前，Claude 会写下一份可阅读和编辑的简短交接记录，下一次会话将从中继续.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: answer Claude point by point, right on the text.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - 适用于长时间会话的 Claude Code mods：sitrep 为每条回复记录结果和待解决问题；ctx-relay 跟踪上下文，并在上下文填满前进行交接.
- [midudev/better-claude](https://github.com/midudev/better-claude) - 一个以模组形式提供的 Claude Code 提示队列：/after &lt;task&gt; 会在当前任务完成后运行该任务，不进行干预.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mod：经过精选和测试，每个 mod 都附带构建它时使用的提示词.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文档事实核查器、代码审计器、错误记忆日志、mod 等.
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - 一个 Claude Code mod，会维护代理获得的 Evidence rea 的实时案例簿：Ghidra 冷启动、必须引用真实 evidence_id…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code buddy 插件：提示上方的 ASCII 伙伴，会记住你的规则并标记 Claude 的快捷方式。
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code 插件，用于按代理控制工具可见性——在每个循环中隐藏并拒绝子代理、技能、MCP 和内置工具。
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods: security layer for Claude Code - secret redaction…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - 在 Claude Code 的终端中渲染 LaTeX 展示数学公式：内置 MathJax，无需安装任何内容。
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - 优秀的 Claude Code 模组合集 | 클로드 코드 모드 모음집。通过状态行、主题、提醒等功能自定义 Claude Code ·…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis：为 Claude Code 制作的非官方 Avengers 粉丝 mod.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一个 Claude Code 模组，可按请求朗读 Claude 的回复和你的提示词，使用本地开源 Kokoro TTS 语音.
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Claude 搞砸时就拍它——适用于 Claude Code 的减压 mod：卡通屁股、8 个拍打器、9 个屁股、标记、连击、声音.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用于实时窗格、成本感知模型路由和安全防护的小型插件。只需一条命令即可从市场安装.
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - 带凭证的 Claude Code。一个负责规划、委派并证明工作已完成的插件.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 与插件：使用量监视器、令牌跟踪器和状态行.
- [yyosifov/prompt-mods](https://github.com/yyosifov/prompt-mods) - 面向提示框的小型、完成度高的 Claude Code 模组。
- [08hida28-bot/usage-meter](https://github.com/08hida28-bot/usage-meter) - Claude Code 模组：始终显示使用情况（上下文、速率限制、成本）。
- [0xgigilau/claude-usage-meters](https://github.com/0xgigilau/claude-usage-meters) - Claude Code mod: progress bars for context, session/week/month usage and…
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - 就在提示词上方，捕捉 Claude Code 会话思维的偏移.
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code 模组市场（my-claude-mods）：状态栏、面板、防护和工具。
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod：用量进度条（上下文、5 小时、7 天）和提示词上方的紧凑按钮。
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods: session stat cards above the prompt。
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示词上方的一只会动的盲文猫。
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示符上方的一只像素猫，会运行一次 OmniDimension 语音代理测试通话。Claude Code 修改.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一种 Claude Code mod，会选择合适的时机进行压缩，以保持较小的上下文窗口.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - 用于 Claude Code 的 Claude Mods：token-meter。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - 用于Claude Code 的通用 mods：顶部栏、窗格、toast 和钩子。包括 usage-bar：显示在提示词上方的上下文、成本和计划限制.
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - A Claude Code mod that picks the model for each subagent before it starts, and…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 将你的 Claude 使用限制显示为动画村民生命值卡片，并带有每周节奏警告——一个 Claude Code mod。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - 面向 S2 team 的 Claude Code mods（the ather marketplace）。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作时进行短时锻炼：每日目标、连续记录、徽章和可选排行榜。一个 Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code 的用量面板：按模型统计花费（今天、本周、本月、全部时间）和周限制预测。终端 LED 滚动条和桌面应用条 + Details 窗格.
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods: live panes, bands and guards that run inside Claude Code。
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - A Claude Code mod that shows what your subagents are up to: a progress bar…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - A Claude Code mod that shows how long each turn took, in a small stopwatch chip…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方显示 Apple Music 和 Spotify，带封面图、控制和 Up next 窗格。
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - 经过维护和审计的 Claude Code 模组副本（filetree、cache-tax）。仅限所有者，提交已签名.
- [broening/claude-mods](https://github.com/broening/claude-mods) - 适用于 Claude Code 的模组：缓存时钟、Blast Radius、建议、工作列表、Grill。
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是给你的 Claude Code 配一只猫头鹰。
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - 個人 Claude Code mods。
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - 原版 Doom 引擎，带 Freedoom，可在 Claude Code 内游玩。Mac Apple Silicon alpha.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - 来自 CorporateChittyChat 频道的小型、易读 Claude Code mods.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - 让 Claude Code 按计划执行：通过 hooks 强制实施阶段、审批关卡和文件预算，另有七个附加 mod（代理、令牌、交接、提醒、PR、密钥）.
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Claude Code mods。
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Claude Code mod：提示词上方的信息条显示提示词缓存倒计时、缓存填充量、命中率、上下文填充量、自动压缩阈值以及 Compact 按钮.
- [curran-gehring/claude-dot](https://github.com/curran-gehring/claude-dot) - A Claude Code mod that brings OpenAI。
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - 我个人的 Claude Code mods，针对我自己的设置定制（macOS、Chrome、gruvbox）。
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 团队专用的 Claude Code mod（usage-meter：蓝色火焰 / Terrier 使用量区间）。
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Claude Code 模组：查看对话正在使用哪些技能、插件、子智能体和 MCP 工具。
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - 用于多并行会话 homelab 工作流的十一种 Claude Code mods（function-hook 插件）。
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Claude Code mods：OpenSpec 和子代理看板、压缩前交接、保持提示词缓存温热，以及针对危险 shell 命令的飞行前检查。
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - 一个生活在 Claude Code 内的 Tamagotchi：它会孵化、吃掉 Claude 写的代码、留下 bug，并成长为八种成年形态之一.
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Claude Code 模组：在提示框上方显示 PR 审查状态、批准、检查和冲突。
- [denys-nabatov/claude-usage-bar](https://github.com/denys-nabatov/claude-usage-bar) - Claude Code mod: 5-hour and weekly limit usage board above the prompt, with…
- [DerpcatMusic/claude-context-controls](https://github.com/DerpcatMusic/claude-context-controls) - Claude Code mod：提示词上方显示嵌套上下文 / 5h / 每周环、压缩阈值和子代理模型锁定。
- [dgsantana/claude-mods](https://github.com/dgsantana/claude-mods) - Claude Code mods：omp-port（TTSR、分层规则、AGENTS.md、APPEND_SYSTEM、advisor）+ nerd 状态栏。
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Claude Code mod：提示词上方显示其他会话的面板——谁在等你、谁仍在工作，以及正在做什么.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code 模组：在 Guard 阻止工具调用后，停止前往同一目标的已识别绕行，并告诉 Claude 询问你。
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code 模组：在一个视图中显示后台任务，从真实输出中读取进度和预计完成时间，并在条带、窗格和 /downrange 中展示，不发起模型请求。
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code 模组：为队友、命名子 Agent 和其他会话的消息提供统一收件箱，并显示未读数量和发送者标签。
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code 模组：解释沙箱拦截原因，并将重复拦截转化为经过审查且可撤销的设置更改。
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favourites for Claude Code: one-click icons for your commands and skills。
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - Claude Code 提示词上方的会话计划实时波浪看板。一个 Claude Code mod.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - 适用于 Pi、Codex 和 Claude Code 的指令、技能、Pi 扩展和 Claude Code mods。
- [esinecan/mental-model-mod](https://github.com/esinecan/mental-model-mod) - Claude Code mod: Claude。
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - 用于后台测试进度的 Claude Code 模组：JUnit、Karma、pytest 和 unittest.
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods（function-hook 插件）：session-meter 及更多。
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Hospedin 团队为 Claude Code 测试中的 mods。
- [fran343/claude-mods](https://github.com/fran343/claude-mods)
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Claude Code 模组：冻结会话，稍后恢复，就像什么都没发生过一样。
- [g761007/hudcade](https://github.com/g761007/hudcade) - 用于 Claude Code 的像素艺术 HUD：上下文、成本、缓存、代理和速率限制一目了然，Claude 思考时显示小型 8-bit 场景，并提供…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - 在 Claude Code 回复中的每个代码块上使用 Ctrl+单击复制链接。
- [GeekyVenkatTuring/portfolio-ticker](https://github.com/GeekyVenkatTuring/portfolio-ticker) - Claude Code mod: portfolio value and P&amp;L above the prompt, plus /portfolio。
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - 适用于桌面应用的 Claude Code mod：点击回复中的文件引用，即可在 VS Code 中打开对应行。支持 Remote-SSH.
- [h3h/blocks-only](https://github.com/h3h/blocks-only) - Claude Code mod: coding turns end in a validated report of typed blocks, drawn…
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Claude Code mods 的私有市场。
- [haruki-cl/claude-code-mods](https://github.com/haruki-cl/claude-code-mods) - Claude Code 模组：token-weather（上下文使用情况和记忆面板）、run-cat（Claude 思考时显示一只正在奔跑的猫）。
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - 适用于 Claude Code 的德语 Mods：上下文/缓存提示、带指导的未完成事项、状态行。
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey 的 Claude Code 模组（插件市场：hectorbailey）。
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模组：每个回答花了多长时间、Claude 思考了多久，以及 tok/s，显示在 Claude 桌面应用中回复的正下方.
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude mods marketplace。
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - 位于你的 Claude Code 提示词上方的驾驶舱。鸭子会读取仪表.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - 自动读取你的工程图，然后在 SolidWorks 里建模。Reads your engineering drawings…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - VS Code 中的 Claude Code 子智能体实时看板：每个对话的子智能体及其任务详情、订阅使用情况和上下文占用.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（a Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（a Claude Code mod）。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（a Claude Code mod）。
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（a Claude Code mod）。
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（a Claude Code mod）。
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - 适用于 Claude Code 的证据门控计划清单：已批准的计划会变成清单，Claude 只有在提供验证证据后才能勾选。
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 简体中文汉化（自管版）——自己的翻译表 + patch 工具 + 升级检查。
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph Ayoub 的 Claude Code mods：一个插件市场（joseph-mods）。
- [jrojasdeveloper/naruto-buddy](https://github.com/jrojasdeveloper/naruto-buddy) - Claude Code 模组：提示框上方的动画像素艺术 Naruto。
- [jrpferreira2002-jpg/clawd-vibe](https://github.com/jrpferreira2002-jpg/clawd-vibe) - Claude Code mod: Clawd above the prompt, clawd has moods。
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的条带中：演绎会话、显示正在运行的内容、上下文和用量限制，并与你的 CI 构建赛跑。非官方粉丝模组.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code の返答や通知を VOICEVOX / Irodori-TTS などで読み上げる mod。
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods。PixBar：提示词上方的像素生物，会随你的轮次、上下文、五小时窗口和 git 移动.
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code mod：在一个浮动窗口中显示每个 Claude Code 会话，并实时摘要各会话正在做什么以及哪些会话需要你处理.
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Small Claude Code mods in one plugin marketplace.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code 模组：为每个子智能体选择模型和推理强度。
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph on what Claude Code knows.
- [kyuskoj/claude-mods](https://github.com/kyuskoj/claude-mods)
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - 十个 Claude Code mods：动画像素宠物、Code Wrapped、lo-fi 节拍，以及安全网、变更窗格、/standup 日志等.
- [Loup0007A/claude-mods](https://github.com/Loup0007A/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - A community-curated Claude Code Mods guide: use cases, original demos…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一个 Claude Code 修改，在 iTerm2 标签页副标题中显示 Claude 正在做什么，让你一眼查看标签栏就能知道哪个会话需要你的关注。
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Code 提示框上方的一只蓬松黑猫。她会眨眼、呼噜、打盹，也会担心你的上下文。倾注爱意制作，以纪念我的猫 Mango。❤️。
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel 的 Claude Code 模组，汇集于一个插件市场（marcel-mods）。
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - 适用于 Claude Code 的小型 mods：runner-avatar，一个在提示词上方运行的小头像。
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Mods Claude : compteur de tokens (token-meter)。
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code 模组：实时显示你的 AI 编码代理正在追求的目标、所作的假设、计划和决定的面板。确认或标记其假设.
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code 模组：/sessions 窗格，用于浏览和删除会话及其磁盘数据（WSL、Windows、macOS）。
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code 的侧边栏：Claude 编写的文件、终端分屏、带 pull 的 git 仓库状态、使用量条、新工单和 TODO 列表——提供 41…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Claude Code 模组：将 Codex（ChatGPT 订阅）及其他非 Anthropic 模型用作会话和子智能体模型，无需代理。
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Claude Code 模组：显示 Claude…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模组：通过在会话开始时设置 CLAUDE_CODE_ENABLE_TODO_TOOLS，为省略待办工具的模型重新启用这些工具.
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 一个 Claude Code 模组：等待安全的暂停时机，然后交接你的会话或将其压缩.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模组：提示词上方每个任务列表任务占一行，显示当前任务、进度条和计数。在终端和桌面应用中外观一致.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 内与 AI 玩 Connect Four（/connect-four）。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模组：当另一个编码代理向你的仓库提交代码时，Claude 会通过差异和测试进行审查，而不是相信它的报告.
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Claude Code mod：保持会话轻量——用量行、提醒和一次压缩，不完整读取巨大文件，截断长 shell 输出。
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 适用于多个 AI 代理共享仓库的 Claude Code 模组：阻止机密值离开 .env、推送到公共远程仓库，以及会清除另一个代理未提交工作的 git 命令.
- [NaokiIshimura/claude-code-mod-prompt-templates](https://github.com/NaokiIshimura/claude-code-mod-prompt-templates) - 一个 Claude Code 模组，可通过提示框上方的数字键按钮插入提示模板。
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code mod：提示词上方为每个 delegate-skills…
- [NicoSKOOL/seo-mods](https://github.com/NicoSKOOL/seo-mods) - 用于 SEO 的 Claude Code 模组：提示框上方实时显示 DataWise 排名，并防止关键词蚕食。
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - 在 Claude Code 的长时间 Monitor 监视过期时重新启用它们，不唤醒 Claude，也不消耗一个轮次。
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code 中的 SQL 防护栏：通过 DB CLI（函数钩子 / Mods），在 Claude 运行 DELETE、没有 WHERE 的…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - 一个以模组形式提供的 Claude Code 记事本面板。
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - 一个适用于 Claude Code 的模组，以 Windows 和 CJK 为优先：在任何终端中预览粘贴的图片和文本，使用 CJK…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code 模组：图片缩略图和状态行。
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid：由 Claude Code 模组强制执行的组合审查 → 规划 → 修复流水线。
- [omarnaman/claude-mods](https://github.com/omarnaman/claude-mods)
- [Orfila-antoine/claude-mods](https://github.com/Orfila-antoine/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 最优秀的 Claude Code Mods，按它们能为你做什么排序。人工检查，每个一行.
- [pakornkub/session-insight](https://github.com/pakornkub/session-insight) - Claude Code 模组：会话使用情况、技能和智能体，以及智能体图表。
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - 适用于 Claude Code 的两个 Claude Mods：garde-du-corps。
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Claude Code 的时间戳：每条消息、回复和工具调用的时间、轮次时长，以及有时间感知能力的 Claude.
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Claude Code 的变更跟踪：准确查看 Claude 对你的 Excel、Word、PDF、Markdown、Confluence、HTML 和 CSV…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack：一个 Claude Code 模组。在一个面板和状态栏中提供永久工作树、只读起步环境、团队控制盘和上下文库.
- [PhilRoli/claude-mods](https://github.com/PhilRoli/claude-mods) - Claude Code 模组：在 TrainTracker 列车抵达前暂停会话。
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code 模块：safety-guard 会阻止破坏性命令和秘密文件访问；notify-router…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Claude Code 的动画像素艺术 Claude 螃蟹：它会在你的提示词上方演示 Claude 正在做什么.
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Claude Code 模组：在会话内运行的函数钩子插件（english-coach、toolbar）。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 模组：在 Claude 工作时做俯卧撑。无代币.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain：Claude Code 模组实地指南，从 ELI5 到策略工程，包含现场测试和引导式教程。
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - 只是我正在使用的 mods 列表。
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - 适用于 Claude Code 的三个无依赖模组：响应式状态行、路径保护和密钥保护。纯 Python，故障时放行.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - claude code 的模组。
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - 一个用于 Claude Code mods 的开源市场，提供用于贡献的仓库 skills 和一致的 artwork.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：将你在 plan mode 中批准的计划变成提示词上方的实时清单，并在 Claude 完成每一步时勾选。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精心挑选的 Claude Code 模组列表。每个条目都经过克隆，并使用 claude plugin validate 检查，同时标注其可操作的内容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：辅助代理运行在 Haiku 上，大文件和日志由免费的 Gemini 模型进行摘要，而不是填满 Claude 的上下文.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 一段伴随会话的 lofi 原声：平静、专注、心流，以及测试通过和失败时的提示音。原创音乐.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 编码时学习：每当一轮操作修改了代码，提示词上方就会出现一个关于该确切修改的问题。按概念评分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 记录 Claude 所做每次编辑的磁带：重放每次自动输入的修改，逐步查看，并将任何文件倒回到任意步骤.
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - 一个 Claude Code 模组：项目仪表盘，以及显示任务、智能体和资源的等距城市地图。
- [serhiichuk/claude-shake](https://github.com/serhiichuk/claude-shake) - Claude Code 模组：在压缩期间用已保存文件占位符替换旧的工具结果，缩短长会话。
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board 及 André Servaes 制作的其他 Claude Code 模组。
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Claude Code 的任务控制中心：实时 subagent 队列、token/成本用量、effort 切换和完成通知.
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Showrin 的 Claude Code mods，让日常工作更高效.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Claude Code 模组：在代码旁的面板中显示上下文和计划限制、消耗速率预测，以及来自普通文件或自定义命令的截止日期雷达。
- [skryvets/claude-status-bar-mod](https://github.com/skryvets/claude-status-bar-mod) - Claude Code 模组：提示框下方的彩色会话信息——上下文、模型、工作强度和速率限制进度条。
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Claude Code mod that keeps unattended sessions going through usage limits, API…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - Claude Code mods 集合：以插件市场形式提供的 TypeScript 个函数 hooks。
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 用于 Claude Code 的一键 commit messages，带有跳舞的像素艺术 Malenia。
- [sunwu51/english-assistant](https://github.com/sunwu51/english-assistant) - Claude Code Mods 插件：提供上下文相关的中英翻译、拼写纠正和双语回复。
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Mods for Claude Code. cache-meter: prompt-cache hit rate, context fill and…
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Claude Code 模组：在提示框上方查看你的 Cursor / VS Code 文件和选区，并让 Claude 知道你正在查看的内容。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter——一个显示你的 Claude 计划使用量（会话和每周限制、重置倒计时、上下文）的 Claude Code mod，位于提示词正上方.
- [tanmen/claude-usage-bars](https://github.com/tanmen/claude-usage-bars) - Unofficial Claude Code mod: Claude Code Desktop の入力欄の上に context・5h・7d の使用率をバーで出す。
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code mod: live crew panel for every subagent。
- [thangnguyen-69/claude-mods](https://github.com/thangnguyen-69/claude-mods) - Claude Code plugin marketplace: Plannotator reviews on the tailnet, and more to…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一个用于 Claude Code 的模块，在面板中显示当前会话：每条提示词、Claude 分阶段为其完成的工作、每个子代理及其回答，以及该提示词的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一个 Claude Code plugin marketplace，用于 mods：function-hooks plugins，可在 Claude Code…
- [tiger3645/claude-tts](https://github.com/tiger3645/claude-tts) - Claude Code mod: read Claude。
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Claude Code mod that writes your Claude usage limits to a file other tools can…
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Claude Code mod: one button under Claude。
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Toptaab 制作的 Claude Code 模组。
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - CC mode which shows which Claude account, organization and plan you are signed…
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods。
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模块：为长时间运行的任务提供动画进度栏和完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 三个小型 Claude Code 模组：查看子代理何时完成、为 Claude 完成后排队发送消息，以及让你喜爱的技能始终只需点击一次即可使用.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 说“I。
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作区旁边的窗格中向 Claude 提出旁支问题。主对话永远不会看到它。功能类似桌面应用中的 /btw.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code 插件：在提示词下方权限模式行中显示提示词缓存倒计时、缓存命中率、上下文天气和每周限制（不是状态栏）。
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - 我的 Claude Code 模组。
- [webfront/claude-mods](https://github.com/webfront/claude-mods) - Special mods for claude code and code in claude app。
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Claude Code mod: the session&#x27;s own model picks each subagent&#x27;s model and effort。
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - 为 Claude Code 提供的小型生活质量改进模组。
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter) - 此 Claude Code mod 会在提示词上方显示一张卡片。卡片按类型显示上下文窗口中的令牌.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — when context outgrows its shell, shed it into the folder and keep going.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Claude Code 模组：隐藏的秘密、待办事项、检查和 CI、日志、diff、draw.io 及游戏。
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 插件：在提示词正上方显示你的 Claude Pro/Max 使用限制、速度预测、计费周期、以 token 和 $/€…
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC (Every Mod Claude Code): a curated, tested collection of Claude Code mods。
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 适用于 Claude Code 的模组。agent-crew：以实时像素团队的形式查看子代理工作，包括角色、模型、当前工具、进度、代币和时间.
- [zhitongLIU/claude-code-mods](https://github.com/zhitongLIU/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 为最出色的智能体精心挑选的顶级资源合集，Claude Code，这款编程伴侣中的公认冠军，来自势不可挡的 Anthropic PBC 团队（无关联）.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 一个显示正在发生什么的 Claude Code 插件——上下文使用情况、活动工具、运行中的代理和待办进度。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 面向 Claude Code CLI 的美观且高度可自定义状态行，支持 powerline、主题等.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 系统提示词的所有部分、27…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - 面向 Claude Code 和 Codex 的 AI 视频技能 — 使用 Remotion 制作电影感产品视频：152 张镜头配方卡、209…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ 条技巧，帮助你充分利用 Claude Code，从基础到高级——包括自定义状态行脚本以及在容器中运行自身的 Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 在终端窗格中审查你的编程代理生成的差异，并将行级评论发送回 Claude Code、Codex、OpenCode 或 Pi。herdr 插件.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 适用于 Claude Code 的综合状态栏插件，包含上下文使用量、API 速率限制和成本跟踪。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - 为 Claude Code 构建 mods：拦截任意请求、修改任意响应、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - 适用于 Claude Code 的综合状态栏仪表板——会话信息、配额条、代理跟踪器、MCP 健康状态、消息历史等.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：跟踪你的 Claude Code 会话的碳足迹。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - 由 awesomejun 制作的 Claude Code 美观状态栏。
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公开的 Claude Code 技能和 mods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code 的技能、mods、子代理、钩子、斜杠命令和指南——可由你的代理安装（参见 INSTALL.md）。
- [sageox/ox](https://github.com/sageox/ox) - The hivemind for AI coding agents — persistent team context recorded once and…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免费的 LLM APIs 和编程代理——每周自动更新，并经过两次探测验证。免费层级、无需信用卡的试用、免费模型.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 在你的终端、你的 Claude Code 和 Cursor CLI 状态行以及 MCP 客户端中，提供你关注的赛事。
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 将你的编程代理变成键盘固件专家的 Agent Skill。审计 ZMK/QMK 键位映射，调整 home row mods，使轨迹球具备层感知能力，使用 CI…
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) - 面向 DeepSeek Harness 的语音优先会话循环：composer 麦克风按钮，带浏览器/本地语音转文本。
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供礼拜时间、回历日期、adhkar、每日经文、圣行斋戒、Ramadan、Jumu。
- [PerryLink/dsh-mask](https://github.com/PerryLink/dsh-mask) - 面向 DeepSeek Harness 的 PII masking…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - 个人 Claude Code 配置，版本控制于 ~/.claude 中 — agents、skills、hooks、settings 和…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness plugin for research topics…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - 面向 DeepSeek Harness (omd) 的多 agent 编排层 — autopilot/ralph/team 模式、19 张角色卡、40…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - 轻量级 Claude Code 状态栏——一个约 170 行的 Bash 脚本，零依赖（不需要 jq、Node、Python、守护进程或配置）.
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Portable Claude Code global configuration: custom skills, PreToolUse hooks, and…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：技能和 mods，经过整理，可在任何人的机器上运行.
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - 从本地对话日志和状态栏数据分析 Claude Code 的令牌使用量和成本。
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Beautiful, informative status line for Claude Code.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - 面向你的 Claude Code agents 的可视化看板：将 sessions、subagents 和 background agents…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - A customizable status line for Claude Code with a drag-and-drop editor。
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code 插件和技能市场，用于促进对游戏 Hytale 的 mods 开发。
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - 面向 Claude Code 的单行、颜色编码 statusline — 文件夹、模型、上下文用量和速率限制。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code 的令牌治理：顶级模型负责指挥，执行交给满足要求的最低成本手段。路由内核、由 hook 强制执行的预预算、遥测，以及带计划配额的状态栏.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - 适用于 Windows Terminal 和 tmux 的 Claude Code 分屏查看器：以渲染后的 Markdown 显示会话，包括子代理、实时…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Claude Code 终端的三行微型仪表盘——模型、上下文消耗、速率限制进度与倒计时，以及完整的 git 状态。Node，零依赖，MIT.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - 用于Claude Code Awesome Media mods 的仓库.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - 降低 Claude Code 和 Codex 的令牌消耗：将查询和测试运行路由到更便宜的模型，把文档转换为紧凑的…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - 适用于 Claude Code 的快速、可配置状态行——单个静态 Go 二进制文件。
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - 显示 Claude Code statusline，包含速率限制、当前目录和 Git 分支信息，以提升工作区感知.
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Compact, actively-maintained status line for Claude Code — model, effort, token…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - 适用于 Claude Code 的友好、可随意调整一切的状态栏——真彩色信息条、约 80 种主题，以及通过一个 JSON 文件对各元素进行样式设置。
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 原生代理团队。尽在掌控。适用于 Claude Code 的严格工作者限制、实时团队可见性和可移植配置.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr 上可定义的Claude Code 软件工厂：xstate station 图、管理器 mod、rigs、beads 和共享内存。
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - 适用于 Claude Code 的 Windows PowerShell 状态行：显示 5 小时和每周限额及重置倒计时、上下文窗口栏和颜色阈值。无依赖.
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code 在 Lua 中的状态栏，带有实时 Neovim playground。
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - 西班牙语 Claude Code 状态栏：任务、skills、带红绿灯指示的上下文、5h/每周使用量和模型。
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - VS Code extension: Claude Code task progress, ETA and rate-limit quota via…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins。
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - 多彩的 Claude Code 状态栏：计划限额、上下文、成本和 tokens。
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - 适用于 Windows 的 Claude Code 状态栏：token 总量、按 API 费率计算的成本，以及 5h 和 7d 时间窗口的限流重置倒计时.
- [gvart/claude-config](https://github.com/gvart/claude-config) - 我的 Claude Code 设置：agent-monitor 模组、技能、代理和一键安装程序。
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Claude Code 的单行状态栏：模型、git、上下文、令牌、成本、运行时间、速率限制。
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - 在 Claude Code 中预览图片：将鼠标悬停在回复下方的标签上即可弹出图片，或使用 /img &lt;path&gt; 在窗格中打开图片.
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Claude Code status line: model, 5h/7d quota bars, monthly spend bar, cwd。
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - 个人 Claude Code 配置：权限、statusline、MCP 服务器。
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - 带代理面板行的 Claude Code 状态行。
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS：可移植的 Claude Code 设置——全局规则、插件集、每个项目的记忆、状态栏和启动器，通过一个脚本安装.
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - 为 Claude Code 显示详细的彩色编码状态栏，展示上下文、git 状态、费用和速率限制.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - 使用紧凑型仪表板跟踪 Claude Code 状态，显示上下文、成本、时长、Git 分支、速率限制和实时用量。
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - 面向终端编码代理的两行状态栏：目录、git、PR、模型、上下文以及 5h/7d 配额。无需网络，无需凭据.
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code 状态栏钩子——跨会话、压缩操作和 --resume 跟踪 token 使用量与上下文。
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Claude Code statusline with installer for Linux and Git Bash on Windows。
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - home-grown, cage-free claude plugins, skills, mods, and more。
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - MSF Supply 的 Marketplace Claude Code：按 commit 精选并固定的模组。
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 环境安装器：技能、状态栏、钩子、权限，以及可选的 Obsidian-vault MCP 服务器（--vault_root）.
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status。
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - 适用于 Claude Code 的丰富多行状态行——实时使用限额（5 小时 + 每周）、上下文窗口使用情况、模型/cwd/git、真彩色条.
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - 多行 Claude Code 状态栏：上下文条、git 分支、每个账户的 9router 配额条、CPU/RAM、Spotify。
- [Paradigm-Study/claude-share](https://github.com/Paradigm-Study/claude-share) - Shared Claude Code sessions: share a session with a link, teammates join from…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline ——适用于 macOS + Linux 的 Claude Code statusline.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - 从 macOS 菜单栏监控 Claude Code 状态，实时显示活动任务、待处理权限和已用时间.
- [pkkid/claude-aitools](https://github.com/pkkid/claude-aitools) - 适用于我的 Claude Desktop 设置的各种模组和技能。
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - 适用于 Claude Code 和 Cowork 的技能与模组——项目跟踪器、参考文档等——打包为可安装的插件市场.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - 适用于 Windows 的 Claude Code 状态行（PowerShell）：使用量条、5 小时/7 天重置倒计时及用量速度警告、自动换行。
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - 适用于 Claude Code 的技能、模组、钩子和状态栏，以及用于在多台计算机之间同步配置的引擎。
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 自定义 Claude Code 状态栏（上游：kamranahmedse/claude-statusline）。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Model risk management guardrails for Claude Code: 25 controls in six mod packs…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Claude Code 的入门 Harness：钩子、状态栏、本地模型、群体调度和工作区模板.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Code 的便携式配置（状态栏 + 安装程序）。
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Claude Code 用の 4 行ステータスライン（context / rate limit / cost / git / worktree）。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Portable Claude Code config: CLAUDE.md, settings, statusline, skills。
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Universal Multi-Protocol StatusLine, Context Self-Learning &amp; Dinotty Plugin…
- [tylergraydev/cc-mods](https://github.com/tylergraydev/cc-mods) - Mods for Claude Code: side panes, status lines, toasts and tool-call guards as…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - 使用轻量、无依赖的终端状态栏仪表板，跟踪 Claude Code 上下文使用量、会话费用和速率限制重置.
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - My Claude Code skills, plugins and mods (marketplace: vladdu)。
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code 技能（VS Code、Windows）：在聊天中的文件路径下显示图像预览和打开按钮、可点击的本地链接、上下文环以及自定义编辑器按钮。
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - 多机同步 Claude Code 用户级配置（settings.json + statusline），GitHub / Gitee 双源。
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Claude Code 状态栏，带渐变进度条、按颜色分级的会话工作量，以及适配 worktree 的路径。
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Claude Code 状态栏：文件夹、git 分支、模型、上下文窗口使用量和计划使用限额。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026——面向 Claude Code 代理的主动式 AI 记忆与速率限制监控器。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks, subagents and statuslines: open-source collections and…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 显示实时令牌使用量和预计能耗的 Claude Code 状态栏。
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - 由 Deno 驱动的 Claude Code CLI 状态行。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 的 mods：基于函数钩子构建的面板、条带和伙伴。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的Claude Code 会话之间传递任务。将更改交给负责某个仓库的会话.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 这是一个用于控制 MODS 的MCP服务器。MODS 是面向 Fablabs 的模块化跨平台工具，包含 CAD/CAM 和机器控制工具.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用于使用本地LLM翻译 CK3 mods 的Codex和Claude Code 技能。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - 用于Claude Code 的开源 mods 和其他扩展。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你反复要求Claude Code 做的事情，并将其变成 mod。此外还包括 8 个示例 mods 和一个虚拟办公室.

</details>

<a id="dsh-cordis"></a>

## DSH 和 Cordis 插件生态系统

DeepSeek Harness 和 Cordis 从不同方向抵达同一目的：对它们而言，插件就是 mod 机制，因此那里的插件相当于这里的 mod。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74429 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

🌊 原创 agent harness。部署智能多玩家群体，协调自主工作流，并构建对话式 AI 系统。具备自适应记忆、自学习智能、联邦、向量 RAG 集成，以及原生 Claude Code / Codex / Hermes 和更多集成

<sub>🔧 在代码中发现使用: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `DSH 和 Cordis 插件生态系统`                 |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **74429**  |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐149050 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

使用代理从应用行为到原生二进制文件，逆向工程任何内容。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **149050** |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100741 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

🎨 最佳 DeepSeek Harness 设计插件。开源的 Claude Design 替代方案。🖥️ 本地优先的桌面应用。🖼️ 你的编码代理变成设计引擎：原型、落地页、仪表板、幻灯片、图像和视频——真实文件，支持 HTML/PDF/PPTX/MP4 导出。🤖 通过 BYOK 支持 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode 及 20+ CLI。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **100741** |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82506 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

将任何想法、计划或代码库转化为美观的交互式图表。适用于 Claude Code、Codex 等的代理技能。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **82506**  |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

##### 📝 摘要

一个用于复杂软件工程任务的可靠编码代理。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Go                                               |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **35769**  |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25532 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **25532**  |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18512 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **18512**  |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8666 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **8666**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6273 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **6273**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4459 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DSH's officially top-recommended TUI plugin — high performance, low overhead, cute pixel whale, smooth mouse interaction. One-command install via npm. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **4459**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3680 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

世界首个面向 AI Agents 的虚拟终端

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **3680**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3418 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **3418**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3033 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **3033**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1911 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1911**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1422 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

AI 小说创作软件：把灵感、角色、世界观、大纲、章节写作、审稿和修稿组织成可控流程；提供 Windows/macOS 桌面版，支持本地和在线模型。AI Novel Writing Software: Organizes inspirations, characters, worldbuilding, outlines, chapter drafting, review, and revision into a controllable workflow. Features desktop apps for Windows/macOS, Ollama integration, and a DeepSeek Harness (DSH) plugin preview.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1422**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1181 · Go · 🔎 inferred · 0 天</summary>

##### 📝 摘要

适用于 Claude Code、Codex、Cursor 以及另外 38 个编码代理的记忆，基于已存储在磁盘上的会话历史构建。本地搜索、MCP 和钩子，无需 LLM，仅需一个 Go 二进制文件。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Go                                               |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1181**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐261 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

非官方 DSH (DeepSeek Harness) 插件：将 chat.deepseek.com 网页模型用作 LLM provider - 浏览器登录捕获、PoW 求解、SSE 流式传输、基于提示的工具调用。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **261**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

ACRYL - Agent Context Relay Yielding Lifecycles。一个持久工作区、一个规范上下文、任意 coding agent。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **255**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-research-report">PerryLink/dsh-research-report</a></b> · ⭐214 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向 DeepSeek Harness 的可验证研究报告引擎：内容寻址证据账本（声明-快照绑定、防篡改），加上带有逐声明验证结论的版本化密封报告和 manifest 密封目录。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **214**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `audit` · `citation-verification` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/2a270ca82dba24d3.png" width="100%" alt="PerryLink/dsh-research-report screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/dafefe1b3e0cd96e.gif" width="100%" alt="PerryLink/dsh-research-report animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向 DeepSeek Harness 的 Claude Code 风格终端界面，支持 Windows、macOS 与 Linux，兼容透明终端、VS Code 主题和自定义配色。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **197**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐194 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **194**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness 的可预览跨预设会话迁移插件。固定架构的交接会保留状态、源模型意图和未解决的图像；原始会话保持不变。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **165**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐144 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **144**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-memento">PerryLink/dsh-memento</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向 DeepSeek Harness 的有界、分层、需批准、可审计的跨会话记忆：一个 ctx.memory 能力接缝，带有零依赖 SQLite provider、一个记忆工具，以及冻结快照注入。维护状态：自 2026-10-05 起 FROZEN。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **141**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `agent-memory` · `ai-agent` · `ai-agents` · `approval` · `audit` · `cordis` · `deepseek-harness` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/f63bd5eb5a8052b8.png" width="100%" alt="PerryLink/dsh-memento screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/0ce3328d348abdce.gif" width="100%" alt="PerryLink/dsh-memento animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐140 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **140**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xcisxc29/dsh-wechat">xcisxc29/dsh-wechat</a></b> · ⭐137 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness 的 WeChat 频道

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **137**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agent` · `automation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `remote-control` · `wechat` · `wechat-bot`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xcisxc29--dsh-wechat/689ef8e1483bcfd7.png" width="100%" alt="xcisxc29/dsh-wechat screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-permission-rules">PerryLink/dsh-permission-rules</a></b> · ⭐122 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向 DeepSeek Harness 的 Claude Code 风格声明式权限规则：有序的 allow/deny/ask 规则，在 tools/pre-execute 瀑布流上匹配工具名、参数（glob/regex）和工作区路径，session-log 审计，以及 HMR 重载。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **122**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `ai-safety` · `allow-deny-ask` · `approval` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/d950618f5f9cf382.png" width="100%" alt="PerryLink/dsh-permission-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/25c9ccd2f2133850.gif" width="100%" alt="PerryLink/dsh-permission-rules animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **90**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

基于 Deepseek-Harness 核心底座打造的桌面版 Agent.继承底坐全部能力。并补全 IDE 相关功能。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **69**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and validate the DeepSeek-Harness community plugin marketplace.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **69**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-fund-research">PerryLink/dsh-fund-research</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向中国公募基金的确定性研究报告，作为 DeepSeek Harness 插件：输入一个基金代码，输出一份版本化 Markdown 报告，包含业绩分解、持仓穿透、风格归因和明确的数据缺口声明。指标由代码计算，而不是由模型计算。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **68**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `finance` · `fund-research`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/9a258f42b5375ed7.png" width="100%" alt="PerryLink/dsh-fund-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/c127c0b5eda50892.gif" width="100%" alt="PerryLink/dsh-fund-research animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐60 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **60**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-13 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 摘要

The living DeepSeek Harness plugin directory — refreshed hourly, compat-tested daily, with an in-app plugin store and scaffolder. DSH 插件活目录：每小时刷新，每日兼容实测，内置插件商店与脚手架。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | HTML                                             |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **59**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体。纯本地、零模型调用、零网络。  Task-aware workspace context retrieval and lifecycle tracking for AI coding agents. Find, organize, and track the workspace context most relevant to the task at hand — locally, deterministically, zero model calls, zero network.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **54**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 65</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - 面向 AI 编程代理的执行前防护工具。在工具调用运行前，它会阻止破坏性的 Git 和文件系统命令，以及常见的访问敏感文件的尝试.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - 为包括 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub…
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - 图形学与3DGS、空间智能持续更新论文；AI Agent Skills for 3D Gaussian Splatting, NeRF &amp; Computer…
- [arcships/rutis](https://github.com/arcships/rutis) - 用于会自我迭代的软件的插件运行时——代理可在其中编写、替换并热加载自己的插件，支持 Rust、TypeScript、Python 和 Go，跨进程和机器运行.
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana：将 DeepSeek Harness 作为 HanaAgent 的 subagent。
- [GDWhisper/dsh-web-startup-auth](https://github.com/GDWhisper/dsh-web-startup-auth) - DSH（DeepSeek Harness）远程 Web 启动 + 用户名/密码认证插件.
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - DeepSeek Harness 插件：确定性数据画像、清洗和验证 (dsh-data-quality)。
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent 是一个面向 AI coding agents 的开源 FDE Harness…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 插件精选目录 — 14 类 280+ 个社区插件，覆盖 MCP / Skill / TUI / 多 Agent…
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - DeepSeek Harness (dsh) 插件开发知识库：10 章开发指南、发布手册、经源码验证的未修复上游问题，以及实测生态数据 — 可作为 DSH…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：基于 DeepSeek Harness（DSH）的多平台群聊智能体系统｜A DSH-powered multi-platform…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH 插件：在 Windows 上为所有代理模式提供 Git Bash shell（替代 pwsh 执行器）。
- [YRN-playmaker/dsh-wallpaper_share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - 一键同步壁纸引擎各类动态场景壁纸的插件，设置应用启动项。A &quot;wallpaper engine&quot; synchronization plugin mounted…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI 插件集合——任务通知、提供商用量、LAN 代理、MCP 管理器、worktree…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web 插件：按日 token 用量统计，带有 GitHub 风格活动热力图、缓存命中率曲线和按模型拆分。
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站。
- [liustack/pptwise](https://github.com/liustack/pptwise) - A real PowerPoint, not HTML. Tell your AI what to cover and pptwise builds an…
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - 跨设备 DeepSeek Harness 会话同步：专用 git mirror，采用仅追加的 keep-both 冲突解决。
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - 面向编程代理的本地优先代码知识图谱和上下文 harness。MCP + DeepSeek Harness（dsh）插件.
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - DSH web 插件：侧边栏的分层工作区树 — 标题中包含 / 会分组到虚拟文件夹；add-workspace 流程获得父组弹窗。
- [ddtcorex/govard](https://github.com/ddtcorex/govard) - 基于 Go 的 Magento、Laravel、Symfony、Next.js、WordPress 等本地开发编排器.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) - 面向 DeepSeek Harness 的供应商参数翻译和确定性 JSON 修复：/translate 在 11 个供应商之间映射…
- [PerryLink/dsh-observe](https://github.com/PerryLink/dsh-observe) - 面向 DeepSeek Harness 的 OpenTelemetry 和 Langfuse 可观测性导出器：turn/step/tool/LLM…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - A bilingual, continuously maintained directory of plugins for DeepSeek Harness…
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - 面向 DeepSeek Harness 插件的多维质量评分：从安装成功。
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - 面向 DeepSeek Harness 插件的隔离安装与冒烟测试试运行：将 repo 或 npm package 安装到一次性 DSH_HOME…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · DeepSeek Harness 功能坞插件：一张面板统一注册/开关所有小功能——用量记账（自定义单价·分时价）、模型设置与余额、19…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 插件的持续兼容性测试：精确的发布版本、隔离运行器，以及可修复的上游问题.
- [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) - 面向 DeepSeek Harness (DSH) 的原生 ClineBot / ClinePass provider companion 插件。
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness 主机插件，将项目文档和长期记忆以纯 Markdown 形式保存在专用的 Obsidian vault 中.
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 插件的 X 光检查：声明的能力与实际行为对比。注册表 + 静态扫描器 + 徽章.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Podman-backed execution for DeepSeek Harness (dsh)。
- [kelemiao/dsh-animation-optimization](https://github.com/kelemiao/dsh-animation-optimization) - DSH 动画优化：输出流式动画与 Claude Code 风格外观插件。
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - 面向 DSH 的本地优先语音对话。在你自己的机器上运行语音识别和语音合成，可选外部 providers.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC 模式基础上的创造模式:DSH 插件,合成 Code Mode 工具编排 + 自引用 Cordis 工具与 preset 创作指导,物化为…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Page capability kit for DeepSeek Harness (dsh): terminal dock, file tree…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Zero-dependency verification standard for DeepSeek Harness (dsh) plugins…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness 插件生态：一个由 101 个仓库组成的系列中的 86 个开源插件，其中 100 个由 PerryLink…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode——让 OpenCode Zen + Go 免费层模型持续工作的 DSH…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — 面向 DeepSeek Harness 的第三方插件市场和受保护的生命周期管理器.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人为本的可拓展桌面工作台：对话、笔记、表格、文件在同一工作台；自建服务端即可开启多人实时协作.
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Run DeepSeek Harness on desktop with zero token costs—a free, open-source GUI…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Bots 工作台：将 Cordis 插件桥接到 dsh 网页 shell 的 sdk-bots 编排网关（聊天、群组、MCP、每个代理的工作区隔离环境）。
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - 受 Hermes 启发的智能体自进化插件系列，专为 DeepSeek Harness 打造。
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - 由 Wanbinyu 维护的 DeepSeek Harness 独立第三方插件和工具。
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - 在 DeepSeek Harness 中使用 OpenCode Zen 免费模型，支持匿名访问或可选的 API 密钥。
- [yangzhe1991/dsh-web-enhance](https://github.com/yangzhe1991/dsh-web-enhance) - DSH Web UI 增强插件:思维链默认展开、官方 API 会话价格统计、文件用系统程序打开、跑完提醒 | DSH (DeepSeek Harness)…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 插件：将 Windows 沙盒 ACL 配置失败。
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Deployment-level deadlines for dsh tool calls that declare none: mounted on the…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - 一个 Rust 插件运行时，配备经 Verus 验证的生命周期内核和 Cordis 兼容适配器.
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Cordis / DeepSeek Harness plugin — normalized GitHub API tools for AI agents…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - 内联 Antigravity 仪表板：tok/s、DSH 风格缓存命中率、五小时和每周配额。默认英文，可切换中文，可逆 Windows 安装.
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步。

</details>

<a id="writing"></a>

## 文章、讨论与视频

关于模组功能的文章、讨论和视频。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 摘要

嗨 HN，我为自己构建了这个，并想将其开源。问题是：我想要一种在提示之间获得提醒的方式，因为我经常在终端里待很长时间，尤其是现在我们通常并行处理如此多的代理。第一个版本是一个简单的 rep

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

##### 📝 摘要

我构建它是因为面对最新的编码模型时，Claude 会使用晦涩的命令进入深度工作模式，让我再也不知道它在做什么。这是一个模组（使用 Claude Code 新函数钩子的插件），会在提示符上方绘制一行：- 当前步骤，

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `文章、讨论与视频`                           |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 首次列入 | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## 按实现语言分类的项目

该生态主要集中在 Python 和 TypeScript，但使用其他语言编写的客户端也在不断出现。本表根据条目自身内容生成。

| 语言       | 条目 | 示例                                                                                                             |
| ---------- | ---- | ---------------------------------------------------------------------------------------------------------------- |
| TypeScript | 384  | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                             |
| JavaScript | 79   | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                   |
| Python     | 39   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `AgriciDaniel/claude-mods-brain` |
| Shell      | 28   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`              |
| HTML       | 14   | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                        |
| Go         | 5    | `sageox/ox`, `mitre/claude-statusline`, `esengine/DeepSeek-Reasonix`                                             |
| Rust       | 5    | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                                  |
| PowerShell | 3    | `Gabriel-Dalton/claude-statusline-tokens`, `markallisongit/claude-statusline`, `rainyfei/claude-statusline-win`  |
| C          | 2    | `reporails/arcade`, `tylergraydev/cc-mods`                                                                       |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                          |
| Lua        | 1    | `crafts69guy/claude-statusline.nvim`                                                                             |
| Swift      | 1    | `peaceinitiativemenhadenoil263/claude-status-bar`                                                                |

<sub>仅统计声明了语言的条目。文档和讨论条目不包含在此表中。</sub>

## 参与贡献

欢迎提交更正，这是改进此列表最快的方式。如果某个条目归类错误、等级错误，或者某个项目因名称冲突而被错误排除，请提交 issue 或 pull request——最后这一类是自动筛选最容易出错的地方。

---

<sub>独立社区项目。与 Anthropic 没有关联，也未获其认可或审查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商标。产品行为可能随时变化；对于任何关键依赖，请以官方文档为准进行验证。相关资产仍归其上游项目所有，仅在许可证允许的情况下转载。</sub>

<sub>最后更新 · 2026-10-13T04:10:27+08:00</sub>
