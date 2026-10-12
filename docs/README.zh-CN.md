<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="精选 Claude Mods">
</p>

<h1 align="center">精选 Claude Mods</h1>

<p align="center"><b>Claude Code mod、插件及其所改变的更深层行为的循证分级索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-597-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <b>简体中文</b> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **实时索引** · 上次同步: `2026-10-12T17:03:53+08:00` (UTC+8)
> · 条目: **597** · 最新更新中新增: **0** · 实现语言: **15**

<sub>以下每个条目均已自动收集、筛选并重新检查。这里没有付费展示内容。</sub>

<a id="featured"></a>

## 当下精选

<sub>每个类别精选一项，按证据等级和星标数排序，并在每次更新时重新计算。这是一个排名，不代表认可；每项精选都会链接到下方的完整卡片。优先选择发布了截图或录屏的项目，以便保持列表的视觉呈现。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9479 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2540 · Python · 👁️ observed</sub>
<sub>找出幽灵令牌。修复它们。在压缩中存活。避免上下文质量衰减。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74385 · TypeScript · 👁️ observed</sub>
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
- [官方：Anthropic 自有的仓库和发行说明](#官方anthropic-自有的仓库和发行说明) — **18**
- [Mods：使用 mod 能力构建](#mods使用-mod-能力构建) — **474**
- [DSH 和 Cordis 插件生态系统](#dsh-和-cordis-插件生态系统) — **93**
- [文章、讨论与视频](#文章讨论与视频) — **11**
- [其他项目](#其他项目) — **1**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150297 · TypeScript · ✅ official · 0 天</summary>

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
| 星标     | **150297** |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9479 · TypeScript · ✅ official · 2 天</summary>

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
| 星标     | **9479**   |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8252 · Python · ✅ official · 2 天</summary>

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
| 星标     | **8252**   |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242 天</summary>

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
| 星标     | **6347**   |
| 最后推送 | 2026-02-11 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 2 天</summary>

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
| 星标     | **1799**   |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

See Stack 官方 Claude Code mod：实时上下文窗口 HUD、语音叙述面板和终端工具。通过以下方式安装：npx seestack

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明`       |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **0**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/redfox-data/redfox-community-dsh">redfox-data/redfox-community-dsh</a></b> · ⭐7 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

The official bundle plugin package of DSH (DeepSeek Harness) from RedFoxHub（红狐数据）: Over 100 social media data skills (Douyin / Xiaohongshu / Kuaishou / Bilibili / Official Accounts / Video Accounts / Weibo / YouTube / TikTok, etc.), installed in the native DSH skill format with just one click.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `官方：Anthropic 自有的仓库和发行说明`           |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **7**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent-skills` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-skill` · `plugin` · `skills`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/redfox-data--redfox-community-dsh/cb0297dc6c545a28.png" width="100%" alt="redfox-data/redfox-community-dsh screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/fschmutz/claude-usage-panel">fschmutz/claude-usage-panel</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

See your Claude Code plan usage everywhere: GNOME top bar, macOS menu bar, a status line under the Claude Code prompt, and a get_usage MCP tool for Claude Code + Cursor. Session, weekly & per-model (Fable/Opus) limits from the official usage API, with burn-rate forecasts. One-line install, self-updating.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `官方：Anthropic 自有的仓库和发行说明`           |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **6**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `anthropic` · `ccusage` · `claude` · `claude-code` · `cursor` · `developer-tools` · `gnome` · `gnome-extension`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fschmutz--claude-usage-panel/40b54f8d52b03345.png" width="100%" alt="fschmutz/claude-usage-panel screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 为 mods 添加了 `$.ui.notify`：通过你自己的通知设置发出原生通知，并说明发送通知的频道为 mod 的 `Button` 添加了子项：字符串和…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 修复了 `UserPromptSubmit` 钩子或模组的 `prompt.submit` 钩子期间按下 Esc…
- [AlekDob/blockodile-claude-mod](https://github.com/AlekDob/blockodile-claude-mod) - Blockodile official Claude Code mod: an animated croc sidebar that explains…

</details>

<a id="mods"></a>

## Mods：使用 mod 能力构建

此处的每个条目都展示了使用 Claude Code 在 2.1.287 中获得的能力的证据：通过 `ui.render` 进行绘制，拥有窗格、横条或卡片，读取 `$.ui.selection()`，通过 `agent.spawn` 生成协作者，或明确说明自己是 mod。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2540 · Python · 👁️ observed · 0 天</summary>

##### 📝 摘要

找出幽灵令牌。修复它们。在压缩中存活。避免上下文质量衰减。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | Python                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **2540**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐510 · JavaScript · 👁️ observed · 0 天</summary>

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
| 星标     | **510**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐199 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **199**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐149 · TypeScript · 👁️ observed · 7 天</summary>

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
| 星标     | **149**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐120 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **120**    |
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
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 摘要

面向网页的代理原生 QA CLI。确定性执行，无需编写测试，无需 LLM。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | HTML                                         |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **104**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐104 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code 的皮肤：带图标的工具行、差异、表格和 Mermaid 图表卡片、使用量条以及十五种主题。/skin 可实时切换它们。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **104**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐80 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **80**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 3 天</summary>

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
| 星标     | **79**     |
| 最后推送 | 2026-10-08 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SaM-runtime/claude-console">SaM-runtime/claude-console</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

面向 Claude Code 的多项目控制台，作为 Claude Code mod 构建：实时项目面板、触发操作、配额电量；通过 Claude Code 或 Codex 执行。

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
| 首次列入 | 2026-10-12 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sam-runtime--claude-console/7502a46951d79adb.gif" width="100%" alt="SaM-runtime/claude-console screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sam-runtime--claude-console/7502a46951d79adb.gif" width="100%" alt="SaM-runtime/claude-console animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐69 · TypeScript · 👁️ observed · 9 天</summary>

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
| 星标     | **69**     |
| 最后推送 | 2026-10-02 |
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
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

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
| 星标     | **46**     |
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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 9 天</summary>

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
| 星标     | **27**     |
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
| 最后推送 | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **23**     |
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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

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

Claude Code mod: preview pasted images and long pasted text above the prompt

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
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

使用 Codex、GLM 和其他编码代理作为 Claude Code 子代理。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **16**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6 天</summary>

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
| 星标     | **14**     |
| 最后推送 | 2026-10-05 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
| 星标     | **7**      |
| 最后推送 | 2026-10-04 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">观看平台 youtube.com</a> · 播放将在托管网站上打开；GitHub 无法在页面内嵌入</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/natsukium/claude-code-figures-plugin">natsukium/claude-code-figures-plugin</a></b> · ⭐7 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

在 kitty-graphics 终端中内嵌绘制图表、LaTeX 数学公式和工具结果图像——一个 Claude Code 插件

<sub>🔧 在代码中发现使用: `hooks/register.tsx`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **7**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `d2` · `diagrams` · `graphviz` · `kitty-graphics` · `latex`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/natsukium--claude-code-figures-plugin/8b6e1b6a10ace52e.png" width="100%" alt="natsukium/claude-code-figures-plugin screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 440</sub></summary>

- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - 适用于 Claude Code 的专家技能、代理、命令、规则、钩子和输出样式——会话连续性 + 面向真实开发工作流的现代 CLI 工具。
- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - 100 多个可与 Claude Code 配合使用的 mods 集合.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其构建工具：先使用构建器技能，然后使用 mods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天运行的 Claude Code harness，自第一天起就以此名称发布，如今与 ucsandman/Agnostic-AI…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四个 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 和 Collision Guard。
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods：在 Claude 读取提示词前修正并翻译它们。
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 来自 Nekyia Labs 的 Claude Code mods 和技能，由生活在持久化家园中的 AI 每天构建和使用。
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 关于 Claude Code mods 的有来源引用的 Obsidian 知识库：它们的工作方式、构建方法，以及安装前的检查方法.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 为 Claude Code 的终端记录提供桌面应用外观的 mod。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的侧边面板：显示会话运行的子代理、每个子代理正在做什么及其令牌，并可一键查看其对话.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教会 Claude Code 代理构建 Claude Mods（函数钩子插件）的技能，附带入门示例。
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社区 Claude mods、插件和技能，可从一个市场安装。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 适用于 Claude Code 的 Claude Mods（函数钩子插件）.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods 画廊：经过检查并固定的 Claude Code mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 面向与对话代理协作的人类用户的决策队列 CLI/TUI。代理发布问题，人类从一个收件箱中回答.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE 窗格 mod：代理面板、文件树和 HWP/PDF 查看器、系统状态、Claude/Codex/Antigravity…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - 输入时将 Markdown 绘制到 Claude Code 的提示框中。即使你还没闭合围栏，围栏代码也会先变成语法高亮卡片.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf。
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code 的浮动状态卡片——模型、上下文、速率限制、成本、分支——另有一个任何脚本或模组都可以提供进度的 API。
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code 的 Mods：为终端 UI 添加实时窗格和行为的函数钩子插件。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard 在屏幕共享时遮盖姓名和机密信息；cache-panel 会在提示词缓存即将失效前提醒你.
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code 扩展。释放 Claude 的全部力量.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod（插件），添加一个带 Activity、Files、Agents、Context 和 MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code 的面板、防护栏和生活质量 mods：上下文、使用量、实时活动、通知、安全规则、提示词教练、命令中心.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示词框上方的两个 Claude Code mods：上下文窗口计、5 小时限制、提示词时钟和会话成本。
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - 让 Claude Pro 计划持续更久：用于精确使用量 HUD、更短 shell 输出且不重复读取文件的 Claude Code mods.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 读取 Claude Code 命名的 markdown 文件，并将其渲染在会话旁边；指向任意代码块即可让 Claude 编辑它.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在任意终端中将粘贴的图像缩略图显示在提示词上方。
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的语音协作者。与由 ElevenLabs conversational AI 驱动的 3D…
- [ngothanhluc/claude-mermaid-mod](https://github.com/ngothanhluc/claude-mermaid-mod) - Claude Code mod: draws mermaid blocks in Claude。
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed，一款带有每条提示统计信息的实时打字速度计。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - 用于 Claude Code 的烟花：每次按键、工具调用、提交和绿色测试都会在提示上方升起盲文烟花。一个 Claude Code mod.
- [Danovich/turntype](https://github.com/Danovich/turntype) - 在 Claude 工作期间进行的打字测试。一个 Claude Code mod.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 探索Claude Code mods、插件和扩展，浏览动画演示、分类列表和直接源代码链接。由 FindMods.dev 提供支持.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：在记录中内联绘制 mermaid 图表。
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code 的 Mods 和 skins：为 Claude 的任务提供实时进度条、带匹配 Windows Terminal…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code 修改插件（函数钩子插件）：session-switcher 及更多。
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods：Claude Tools 菜单、Zen 模式、终端主题、工作量和模式控制。
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout（查找你最常使用的 mods）、usage-meter、check-ledger、resume-nudge。
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 用于同时运行多个会话的两个Claude Code mods：提示词上方的上下文卡片和聊天旁边的会话窗格.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad。
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：发现、检查、切换和更新Claude Code mods。
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：上下文栏、代理面板、PDPA 模糊处理。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最佳Claude Code Mods：精选、已验证、已置顶。一次 /plugin marketplace 添加，包含 43 个 mods.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 插件：自动进行 Claude 模型路由。为每条提示词、步骤和子代理选择 Haiku、Sonnet 或 Opus…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 的 mods：使用插件函数钩子API构建的窗格、命令和钩子。
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - 在巨大工具输出填满 Claude Code 的上下文之前将其截短。保留错误和摘要，完整文本只需一次 Read 即可查看.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code 的六个 mod：动画 Clawd 吉祥物、用量限制和提示词缓存条、发送前消息检查器、快捷回复、待办队列和成本账本.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code 的 mods 市场：代理循环单步调试器、git 账户提示、工作树状态行等.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 六个 Claude Code…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 的最佳全能模组包：用量限制和上下文 HUD、针对 rm -rf 和 git reset --hard 的带撤销保护、.env…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - 在你的 Claude Code 中播放 YouTube Shorts 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren 的 Claude 工具包：适用于 Claude Code 的技能、模组和 MCP 服务器。通过插件市场一键安装.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code 修改插件，在两列并排布局中绘制 Edit 和 Write 差异。
- [nsodhi-cmu/claude-code-ripple](https://github.com/nsodhi-cmu/claude-code-ripple) - 创建代码变更调用图的 Claude Code mod。
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 的 mods：Clawd，一个会演示Claude正在做什么的小型像素吉祥物。
- [reporails/arcade](https://github.com/reporails/arcade) - 经典桌面游戏作为Claude Code mods，在Claude工作时于窗格中运行。由 Reporails 制作.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精选的 Claude Code 模组列表，可作为插件市场安装：主题、窗格、状态栏、肖像.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 按需生成 Claude Code 模组——一种读取你的对话并构建合适模组的技能：计划进度条、文件窗格、上下文仪表、危险命令防护、测试监视器.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 两个 Claude Code mod：cache-keeper 和 ctx-mod。
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - 由沉迷于 harness engineering 的 Rustacean 设计的、极具主见的 Claude Code 插件。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 让代理保持诚实的Claude Code mods——用于守护范围、验证部署并在提示词上方绘制会话的函数钩子.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - 我使用的 Claude Code mods.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - 用于 Claude Code 的 macOS notch 仪表板：用量限制、打开的会话、任务进度、提示缓存倒计时和待办事项——由五个 Claude Code…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code 的 mod：提示词缓存栏、后续步骤、快捷按钮和更改回放——可从 marketplace 安装。
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - 在一个 Claude Code 面板中查看你的编码代理（Claude Code、Codex、OpenCode、Antigravity）的成本、令牌和计划限制。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 一个 Claude Code mod，会在提示上方的条带中绘制你的使用限制和支出.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（marketplace herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods：计划进度条、记录Claude留下的运行中任务的账本，以及工具输出的令牌屏蔽。
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在后台运行的内容：子代理、Codex 作业、shell、监视器、cron 作业和工作流.
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs 制作的 Claude Code mods：streams 将会话中交错的工作拆分为带颜色编码的 streams。
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - 关于 Windows 上 Claude Code mod 的首日现场笔记：上下文/配额燃料条、泰语 UI mod、Matrix…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools：用于调试 Claude Code 工具调用的调试器.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - 位于 Claude Code 提示下方或全屏时停靠在记录旁的小卡片。每个小组件都是独立模组，可通过斜杠命令切换.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：在提示词上方显示实时成本、上下文和计划配额计量器。图标需要 Nerd Font.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - 一个 Claude Code 模组，在消耗使用量窗口前暂存子代理扩展、大上下文提示和重试循环.
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 面向 Claude 的 28 个 Agent…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - 用于 claude 的 code-mods。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 一个 Claude Code 修改插件，可通过命名配置文件按仓库启用或禁用全局技能、agents、规则和工具.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 插件（模组）：在多个 Claude 账户之间切换，在状态栏中查看使用限制，并在终端窗格中管理代理、工作树、检查点和差异。
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 经过测试、可一键安装的 Claude Code 模组：YOLO 模式防护、实时成本和上下文、窗格、宠物等。另附精选的最佳社区模组列表.
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code 的 mods：基于函数钩子构建的插件。
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca。
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 我制作的一批 claude code mods。
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code 模组。touch-map：以树状图和活动地图查看 Claude 列出、读取、编辑或创建了哪些文件.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - 使用 Claude Code 工作时学习一门外语。
- [20alexl/windvane](https://github.com/20alexl/windvane) - 替你照看漫长的 Claude Code 会话：监视上下文填充情况，起草检查点，在合适的时机压缩，并恢复工作。每个子代理中都有规则，还有项目记忆.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Live cost, token and context usage sidebar for Claude Code: a mod that shows…
- [atharv6f/headway](https://github.com/atharv6f/headway) - 在你的 Claude Code 提示之上显示目标、任务和 agents——无需设置。一个 Claude Code mod.
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude 正在火热进行。与你的小队聊天。朋友在线，就在你的 Claude Code 会话旁边。零 token，零泄露给 Claude.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 面向真正工程师的 Claude Code mods。
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code 的终端会话回顾，位于 Claude desktop app 的 Code 标签页中（一个 Claude Code mod）。
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack 的 Claude Code mods 合集。
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - A Claude Code mod: a pane with the session。
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - 一个 Claude Code mod：在 Claude 工作时，于放置类游戏中捕捉像素艺术 Modsters.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - 全能 Claude Code mod：实时 HUD、安全防护（命令屏蔽、秘密信息遮蔽、支持回滚的回合检查点）、自动 lint/test…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每个 Claude Code 代理在其上下文中有哪些文件，以及每个文件占多少.
- [delexw/codyssey](https://github.com/delexw/codyssey) - 让每个 Claude Code 会话都变成一场小冒险：跟随代理心情变化的生成音乐、每次编辑和命令都会与怪物战斗的像素骑士，以及以游戏风格重新讲述的文字记录.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 用于终端和桌面应用的 Claude Code 小型 mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI 技能 + mod，可在 agent 回复中加入西班牙语单词。
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code 提示词上方的 Alarum 事件：刚刚到达的内容，以及一键将其交给代理.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - 你的 Floatee 待办事项列表显示在 Claude Code 的提示词上方：一键运行、指导并勾选你的 todos.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code 的 Evangelion 风格侧边栏：上下文、配额、活动、PR、硬件、会话和 forge 面板。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 一个将其重新设计为《疑犯追踪》中的 The Machine 的 Claude Code mod.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Claude Code 模组：像素艺术小队为每项任务推荐合适的模型（Haiku、Sonnet、Opus）——EN/PT/ES。
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：用于强制执行并验证子代理 DAG 工作流的 Claude Code mod，带有实时 DAG 窗格。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - 适用于 Claude Code 的开源 mods：面板、状态栏、提示、工具防护和斜杠命令.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 一个 Claude Code 模组：为每个子代理设置一个窗格，显示它们访问的文件，以及会话的用量和费用.
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - 我为 claude 制作的各种实用 mod。
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod：会话状态、实时 Spec Kit 进度和使用窗口治理。
- [KevinYu1580/jev-cc-model-router](https://github.com/KevinYu1580/jev-cc-model-router) - Claude Code mod：每个会话选择一次模型、每回合选择工作量，使用 TypeSafe 的 Jev 判断任务难度.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 上下文窗口作为提示上方的一行，按照 Claude Code 绘制其自身仪表的方式绘制.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 的实时任务 HUD：Claude 工作时显示在提示上方的条带，点击一次即可打开完整仪表板.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code 插件（mod），让 Claude Code 终端界面看起来像 Claude 桌面应用：提示气泡、Markdown 表格、mermaid…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - 一个插件中包含十四个 Claude Code mods，每个都可切换，并提供用于管理、配置和导入 mods 的窗口.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - 一个免费的开源 Claude Code 插件。在你执行 /clear 前，Claude 会写下一份可阅读和编辑的简短交接记录，下一次会话将从中继续.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - 精选的 Claude Code mod、原作者演示、公共代码仓库和安装资源.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Personal Claude Code mods (function-hook plugins): context handoff, repo…
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - 将提示词暂存起来供稍后使用，再将其弹回Claude Code 的输入框。即时完成，不调用模型.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod，在 Ghostty 和 kitty 中内联显示图片。
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 一个 Claude Mod，会在转录记录旁的窗格中显示会话的 GitHub 拉取请求：将描述引用到提示框中，查看检查和评审状态。
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mod：经过精选和测试，每个 mod 都附带构建它时使用的提示词.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code mods：自动交接和进度条。土耳其语，只需几个命令即可安装.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文档事实核查器、代码审计器、错误记忆日志、mod 等.
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Claude Code 模组，在你发送粗略提示之前将其改写得更清晰。只读取你的提示和对话，不读取其他内容.
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - A Claude Code mod that keeps a live casebook of the Evidence rea gives the…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Pedro La Rosa 的 Claude Code mod，汇集于一个插件市场。
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Claude Code mod：将你的 5 小时和 7 天使用限额作为提示词下方实时动画条显示——倒计时、节奏标记、预测、Pac-Man.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code buddy 插件：提示上方的 ASCII 伙伴，会记住你的规则并标记 Claude 的快捷方式。
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code 插件，用于按代理控制工具可见性——在每个循环中隐藏并拒绝子代理、技能、MCP 和内置工具。
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Render LaTeX display math in Claude Code。
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Claude Code mods 集合.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 插件和 mod：一个 AI 原生 SDLC（意图 → 规格 → 计划 → 构建 → 验证 → 评审），带有通过 hook…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code 修改版合集 | Claude Code 修改版合集.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis：为 Claude Code 制作的非官方 Avengers 粉丝 mod.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一个 Claude Code 模组，可按请求朗读 Claude 的回复和你的提示词，使用本地开源 Kokoro TTS 语音.
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用于实时窗格、成本感知模型路由和安全防护的小型插件。只需一条命令即可从市场安装.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 与插件：使用量监视器、令牌跟踪器和状态行.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - 一个 Claude Code mod，将小型决策交给廉价的决策模型：路由、技能、注入筛查、/compact-jev。
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - 就在提示词上方，捕捉 Claude Code 会话思维的偏移.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - afterever 制作的 Claude Code mods（插件市场）。
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Claude Code mod 市场：agent-board、auto-model、session-collab，以及修改版…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods：在提示词上方显示会话统计卡片。
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示词上方的一只会动的盲文猫。
- [aliahmadcse/claude-usage-status](https://github.com/aliahmadcse/claude-usage-status) - Claude Code mod：在状态栏显示模型、工作量、上下文、成本和 5 小时/每周使用限额。
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code mod：通过子 Claude Code 将便宜的工作路由到 GLM/Kimi，把关键工作保留在你的订阅上。从 Maggy 移植.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示符上方的一只像素猫，会运行一次 OmniDimension 语音代理测试通话。Claude Code 修改.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一种 Claude Code mod，会选择合适的时机进行压缩，以保持较小的上下文窗口.
- [Amel-DZRV/claude-code-auto-handoff](https://github.com/Amel-DZRV/claude-code-auto-handoff) - Claude Code mod: context bar with a handoff mark, prompt-cache countdown…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - 用于 Claude Code 的 Claude Mods：token-meter。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - 用于Claude Code 的通用 mods：顶部栏、窗格、toast 和钩子。包括 usage-bar：显示在提示词上方的上下文、成本和计划限制.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 将你的 Claude 使用限制显示为动画村民生命值卡片，并带有每周节奏警告——一个 Claude Code mod。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - 面向 S2 team 的 Claude Code mods（the ather marketplace）。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作时进行短时锻炼：每日目标、连续记录、徽章和可选排行榜。一个 Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code 的用量面板：按模型统计花费（今天、本周、本月、全部时间）和周限制预测。终端 LED 滚动条和桌面应用条 + Details 窗格.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方显示 Apple Music 和 Spotify，带封面图、控制和 Up next 窗格。
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - 用于编排器和工作代理会话的 Claude Code 模组。
- [broening/claude-mods](https://github.com/broening/claude-mods) - 适用于 Claude Code 的模组：缓存时钟、Blast Radius、建议、工作列表、Grill。
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Claude Code 的 mod：Clean View 隐藏工具调用，并将计划显示为检查清单。
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - 一个 Claude Code mod：记录编排式工作，包括运行、通道、子代理、门禁判定和审查结果，并且可以跟随计划文档。
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code mod：Suggestion Spotlight 展示 Claude 建议的下一条提示词所指向的内容.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是给你的 Claude Code 配一只猫头鹰。
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - 我创建的 Claude Code mod（面板、命令和 hooks）。
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - 原版 Doom 引擎，带 Freedoom，可在 Claude Code 内游玩。Mac Apple Silicon alpha.
- [cigarette1991/clawd-pet](https://github.com/cigarette1991/clawd-pet) - Clawd，一个位于提示框上方的 Claude Code mod。
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - 像 pull request 一样审查 Claude 触及的每个文件，无需离开终端。
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 团队专用的 Claude Code mod（usage-meter：蓝色火焰 / Terrier 使用量区间）。
- [dankelleher/pin-message](https://github.com/dankelleher/pin-message) - Claude Code mod: pin a reply above the prompt, collapsible to a one-line summary。
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Eleven Claude Code mods (function-hook plugins) for a many-parallel-sessions…
- [davidcoulson/punch-list](https://github.com/davidcoulson/punch-list) - A Claude Code mod that keeps one to-do list of the things waiting on you…
- [davidcoulson/session-crew](https://github.com/davidcoulson/session-crew) - A Claude Code mod that shows the side sessions a desktop session starts as…
- [daviddecorso/claude-mods](https://github.com/daviddecorso/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - 一个生活在 Claude Code 内的 Tamagotchi：它会孵化、吃掉 Claude 写的代码、留下 bug，并成长为八种成年形态之一.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Claude Code 终端对话中的书签和 vim 风格标记：高亮一行、标记它，然后跳回那里.
- [devsomelife/somelife-claude-mods](https://github.com/devsomelife/somelife-claude-mods)
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - 一个 Claude Code mod：提示词上方的横幅，显示 Claude 新闻以及依赖项的紧急或安全版本发布信息.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code 模组：在 Guard 阻止工具调用后，停止前往同一目标的已识别绕行，并告诉 Claude 询问你。
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code 模组：在一个视图中显示后台任务，从真实输出中读取进度和预计完成时间，并在条带、窗格和 /downrange 中展示，不发起模型请求。
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code 模组：为队友、命名子 Agent 和其他会话的消息提供统一收件箱，并显示未读数量和发送者标签。
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code 模组：解释沙箱拦截原因，并将重复拦截转化为经过审查且可撤销的设置更改。
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [ecombuilder-web/TripleDigit-crab-agents](https://github.com/ecombuilder-web/TripleDigit-crab-agents) - Claude Code mod：右侧 Agents 窗格将每个正在运行和已完成的会话显示为戴帽子的螃蟹，并显示限额倒计时。
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods：rewrite-prompt（Ctrl+P 会在发送前重写你的草稿）。
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - 适用于 Pi、Codex 和 Claude Code 的指令、技能、Pi 扩展和 Claude Code mods。
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods：auto-model-detector 将每个提示词路由到合适的模型和工作量级别。
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods (function-hook plugins): session-meter and more。
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi——一个 Claude Code mod：在提示词上方读取现场氛围的吉祥物，并配有显示计划、限额、git、PR 和模型的实时面板。
- [g761007/hudcade](https://github.com/g761007/hudcade) - A pixel-art HUD for Claude Code: context, cost, cache, agents and rate limits…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - 七个 Claude Code…
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - 包含我的模组的 Claude Code 插件市场。
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - 实用的 claude code 模组。
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Private marketplace of Claude Code mods。
- [hashswingingslasher/model-hint](https://github.com/hashswingingslasher/model-hint) - Claude Code mod: suggests haiku, sonnet or opus for the task you are typing…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - 适用于 Claude Code 的德语 Mods：上下文/缓存提示、带指导的未完成事项、状态行。
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey 的 Claude Code 模组（插件市场：hectorbailey）。
- [hernandezsanti/claude-code-mods](https://github.com/hernandezsanti/claude-code-mods) - Claude Code 模组，强制执行基于工单的提交，保护付费 CI 分钟数，并在打开 PR 时关闭工作树.
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod：每次回答后提供三个后续步骤，支持任意语言，可选本地语音和侧边助手.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模组：每个回答花了多长时间、Claude 思考了多久，以及 tok/s，显示在 Claude 桌面应用中回复的正下方.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods：streamer-mode 在共享屏幕时隐藏私密面板、频段和状态行。
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - 用于我的 claude mods。
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - 位于你的 Claude Code 提示词上方的驾驶舱。鸭子会读取仪表.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: private values are replaced with…
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code 模组：在文件 Claude 刚刚编辑过时发出脉冲的侧边栏文件树。
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Claude 状态栏。
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - 小型 Claude Code mods：上下文和计划使用量仪表、提示词缓存计量器，以及一个显示待查看事项的面板.
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Claude Code 模组：上下文栏和 cyberdeck HUD。
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - 自动读取你的工程图，然后在 SolidWorks 里建模。Reads your engineering drawings…
- [jatinmayekar/claude-task-list](https://github.com/jatinmayekar/claude-task-list) - Claude Code mod: task list above the prompt, managed with /task。
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（a Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（a Claude Code mod）。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（a Claude Code mod）。
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（a Claude Code mod）。
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（a Claude Code mod）。
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - 适用于 Claude Code 的证据门控计划清单：已批准的计划会变成清单，Claude 只有在提供验证证据后才能勾选。
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 简体中文汉化（自管版）——自己的翻译表 + patch 工具 + 升级检查。
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - 非官方社区指南：介绍 6 种语言中的 Claude Code 模组（函数钩子），并提供可搜索的模组目录。
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - 两个 Claude Code 模组：带回复的会话交接，以及将简单轮次路由到更便宜的模型.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的条带中：演绎会话、显示正在运行的内容、上下文和用量限制，并与你的 CI 构建赛跑。非官方粉丝模组.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code の返答や通知を VOICEVOX / Irodori-TTS などで読み上げる mod。
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - 一个 Claude Mod，用于读取并加入你的 Claude Code 会话之间的对话（/crosstalk）。
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods。PixBar：提示词上方的像素生物，会随你的轮次、上下文、五小时窗口和 git 移动.
- [Kiko-42/claude-code-hist](https://github.com/Kiko-42/claude-code-hist) - Claude Code mod: /hist lists your past prompts and jumps the transcript to the…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - 适用于 macOS 的 Claude Code 模组：一个浮动窗口，显示每个 Claude Code…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods。
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - 一些 claude-code-mods 概念验证。
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - 以市场形式发布的 Claude Code 模组。
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 两个 Claude Code 模组：folio，位于聊天旁的文件窗格；以及 tint，为终端会话重新设置样式并添加状态行.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph：一张实时图表，展示 Claude Code 知道些什么.
- [KunalKumarkkr01/prompt-rewriter](https://github.com/KunalKumarkkr01/prompt-rewriter) - Claude Code mod: /rewrite &lt;prompt&gt; picks role + task personas, adds recent web…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - 在等待 Claude Code 的回答时，不要让注意力飘走.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu 的Claude Code mods——一个插件市场（待办事项侧边窗格）。
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - A community-curated Claude Code Mods guide: use cases, original demos…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - 来自 Mod Box 的独立 Claude Code mods，每个都可以单独安装.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一个 Claude Code 修改，在 iTerm2 标签页副标题中显示 Claude 正在做什么，让你一眼查看标签栏就能知道哪个会话需要你的关注。
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy，一个非官方粉丝制作的像素伙伴，住在 Claude Code 提示框上方，并会对 Claude 的操作作出反应.
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - Claude 的上下文已使用多少、缓存何时失效，以及你的 5 小时和每周限额还剩多少——就在 Claude Code 中提示词的正下方。
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Code 提示框上方的一只蓬松黑猫。她会眨眼、呼噜、打盹，也会担心你的上下文。倾注爱意制作，以纪念我的猫 Mango。❤️。
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code 模组：直接在文本中逐点回答 Claude。选择对话中的任意部分，发表评论，然后将所有评论作为一条提示发送.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - 适用于 Claude Code 的小型 mods：runner-avatar，一个在提示词上方运行的小头像。
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - 来自 MateAI 频道的小型 Claude Code 模组。cost-band：提示框上方显示实时列表价成本估算.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code 模组：实时显示你的 AI 编码代理正在追求的目标、所作的假设、计划和决定的面板。确认或标记其假设.
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code 模组：/sessions 窗格，用于浏览和删除会话及其磁盘数据（WSL、Windows、macOS）。
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - 社区制作的 Claude Code 模组：在 Claude Code 内运行的防护程序、窗格和命令。市场：modhub。
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code 的侧边栏：Claude 编写的文件、终端分屏、带 pull 的 git 仓库状态、使用量条、新工单和 TODO 列表——提供 41…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code 模组：根据你近期的使用速率，预测每周限额和 5 小时 Claude 限额在重置时还剩多少。
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code 的安静侧边窗格：此会话正在做什么、它的计划、代理，以及其他每个会话。
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Code 会话记录中每个提示词和每条回复上方的昏暗时间，按你自己的时钟设置显示。
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - 用于会话和记忆的 Claude Code 插件：一个 Memory 窗格模组和一个 session-wrap skill。作为插件市场中的插件安装.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模组：通过在会话开始时设置 CLAUDE_CODE_ENABLE_TODO_TOOLS，为省略待办工具的模型重新启用这些工具.
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 一个 Claude Code 模组：等待安全的暂停时机，然后交接你的会话或将其压缩.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模组：提示词上方每个任务列表任务占一行，显示当前任务、进度条和计数。在终端和桌面应用中外观一致.
- [mwmrs/claude-mods](https://github.com/mwmrs/claude-mods)
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 内与 AI 玩 Connect Four（/connect-four）。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模组：当另一个编码代理向你的仓库提交代码时，Claude 会通过差异和测试进行审查，而不是相信它的报告.
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Claude Code mod: keeps sessions light — usage line, heads-up and one…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 适用于多个 AI 代理共享仓库的 Claude Code 模组：阻止机密值离开 .env、推送到公共远程仓库，以及会清除另一个代理未提交工作的 git 命令.
- [netgfx/claude-flow-explainer](https://github.com/netgfx/claude-flow-explainer) - A Claude mod to guide the user step by step on how a flow or code works。
- [netgfx/claude-html-mod](https://github.com/netgfx/claude-html-mod) - 一个用于在侧面板中显示 html 的 Claude code 模组。
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - 适用于 Claude Code 的有趣免费模组，绝不消耗 token。首先推出：Dungeon Master，一个 D&amp;D DM 屏幕.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Re-arms Claude Code。
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code 中的 SQL 防护栏：通过 DB CLI（函数钩子 / Mods），在 Claude 运行 DELETE、没有 WHERE 的…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - 一个适用于 Claude Code 的模组，以 Windows 和 CJK 为优先：在任何终端中预览粘贴的图片和文本，使用 CJK…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods：图像缩略图和状态行。
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 最优秀的 Claude Code Mods，按它们能为你做什么排序。人工检查，每个一行.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - 适用于 Claude Code 的两个 Claude Mods：garde-du-corps。
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Claude Code 的时间戳：每条消息、回复和工具调用的时间、轮次时长，以及有时间感知能力的 Claude.
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Claude Code 的变更跟踪：准确查看 Claude 对你的 Excel、Word、PDF、Markdown、Confluence、HTML 和 CSV…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - 适用于 Claude Code 的模组：可在任意代码仓库中运行的函数钩子插件。
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - 适用于我的 Claude Desktop 设置的各种模组和技能。
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Claude Code 模组：跟踪每个子 agent 使用的模型、令牌、工具和时间，标记本可使用更便宜模型的运行，并维护按仓库划分且有界的效率日志.
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Claude Code 模组：侧边窗格中每个子 agent 都显示为一个小火柴人，并带有进度和不合常理的评论.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code 模块：safety-guard 会阻止破坏性命令和秘密文件访问；notify-router…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Claude Code 的动画像素艺术 Claude 螃蟹：它会在你的提示词上方演示 Claude 正在做什么.
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods，作为一个插件市场发布。
- [razzamatazm/cache-keeper](https://github.com/razzamatazm/cache-keeper) - Claude Code 模组：先让空闲会话的提示缓存保持温热一次，然后在其冷却前写入交接文档。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 模组：在 Claude 工作时做俯卧撑。无代币.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커。
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - just a list of mods I。
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - 适用于 Claude Code 的三个无依赖模组：响应式状态行、路径保护和密钥保护。纯 Python，故障时放行.
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - 我的 Claude Code 模组。
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：将你在 plan mode 中批准的计划变成提示词上方的实时清单，并在 Claude 完成每一步时勾选。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精心挑选的 Claude Code 模组列表。每个条目都经过克隆，并使用 claude plugin validate 检查，同时标注其可操作的内容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：辅助代理运行在 Haiku 上，大文件和日志由免费的 Gemini 模型进行摘要，而不是填满 Claude 的上下文.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 一段伴随会话的 lofi 原声：平静、专注、心流，以及测试通过和失败时的提示音。原创音乐.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 编码时学习：每当一轮操作修改了代码，提示词上方就会出现一个关于该确切修改的问题。按概念评分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 记录 Claude 所做每次编辑的磁带：重放每次自动输入的修改，逐步查看，并将任何文件倒回到任意步骤.
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Claude Code 模组：token-bar，在提示框上方显示你的上下文窗口和使用限制。
- [shaharz/pr-watch](https://github.com/shaharz/pr-watch) - Claude Code mod: watch PR checks and review comments (Codex included) in a…
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Mission control for Claude Code: live subagent fleet, token/cost usage, effort…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Showrin。
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - 个人 Claude Code mods。
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Claude Code mod: context-window meter per session, with Compact now…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Claude Code 模组（功能钩子）：代理面板、预算条、会话舰队。
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - 防止 Claude 的辅助代理（子代理）耗尽你的使用量。限制同时运行的数量及其使用的模型，并实时查看它们的工作情况.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 用于 Claude Code 的一键 commit messages，带有跳舞的像素艺术 Malenia。
- [Stoneeu/zh-tw-dictation](https://github.com/Stoneeu/zh-tw-dictation) - Claude Code 模组：将提示框中的简体中文（例如语音听写）转换为带台湾措辞的繁体中文（OpenCC s2twp），并进行 Voice Hunter…
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - 亲自制作的 Claude Code 模组合集（插件市场）。
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - 适用于 Claude Code 的可配置状态栏——通过一个配置统一设置 band、原生状态行、窗格和阈值 toast；使用 npx ccstatus 或…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場。
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Claude Code 模组：在提示框上方查看你的 Cursor / VS Code 文件和选区，并让 Claude 知道你正在查看的内容。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter——一个显示你的 Claude 计划使用量（会话和每周限制、重置倒计时、上下文）的 Claude Code mod，位于提示词正上方.
- [texxmexx/claude-usage-bar](https://github.com/texxmexx/claude-usage-bar) - Claude Code-mod: förbrukningsband ovanför textrutan。
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一个用于 Claude Code 的模块，在面板中显示当前会话：每条提示词、Claude 分阶段为其完成的工作、每个子代理及其回答，以及该提示词的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一个 Claude Code plugin marketplace，用于 mods：function-hooks plugins，可在 Claude Code…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code 模组：就地重写粗略提示，列出匹配的技能、待决定事项和最终结果.
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - 在朗读 Claude Code 的回复时高亮当前正在朗读的句子。使用本地语音，支持多种语言.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Toptaab 制作的 Claude Code 模组。
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Claude Code mod that checks the English of your prompt while you write it。
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - 适用于 Claude Code 的小巧、有趣且实用的模组。
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模块：为长时间运行的任务提供动画进度栏和完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 三个小型 Claude Code 模组：查看子代理何时完成、为 Claude 完成后排队发送消息，以及让你喜爱的技能始终只需点击一次即可使用.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 说“I。
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作区旁边的窗格中向 Claude 提出旁支问题。主对话永远不会看到它。功能类似桌面应用中的 /btw.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code 会在任务完成或等待许可时通过 Telegram 提醒你，你可以用手机回复下一个提示词、/status、/last 或 /stop。
- [WarrenLin/claude-typing-practice](https://github.com/WarrenLin/claude-typing-practice) - ⌨️ Claude Code mod：等 AI 回覆時練打字，即時顯示 WPM 與正確率。
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods。
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - 一个 Claude Code 模组：用于回复的荧光笔、用于将查询结果显示为表格的侧面板，以及适用于每个子代理的进度条.
- [wendyyyanto/usage-meter-mod](https://github.com/wendyyyanto/usage-meter-mod) - A Claude Code mod that shows your usage limits, context, model and effort in a…
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter)
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Claude Code 模组：隐藏的秘密、待办事项、检查和 CI、日志、diff、draw.io 及游戏。
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 插件：在提示词正上方显示你的 Claude Pro/Max 使用限制、速度预测、计费周期、以 token 和 $/€…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 适用于 Claude Code 的模组。agent-crew：以实时像素团队的形式查看子代理工作，包括角色、模型、当前工具、进度、代币和时间.
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - 适用于 Claude Code 的终端侧面板模组——agent 跟踪、由令牌驱动的 Tetris、宠物等.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - 一个适用于 Claude Code 的实时任务面板：构建前制定计划，在侧边面板中跟踪每项任务、状态、时间、子代理和检查.
- [youngin-abel-kim/context-gauge](https://github.com/youngin-abel-kim/context-gauge) - 一个 Claude Code 模组：将上下文窗口作为提示框上方的一行仪表显示，并在下方显示细分信息。
- [yu1745/claude-code-image-view](https://github.com/yu1745/claude-code-image-view) - Claude Code mod: show images inline in the terminal。
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 为最出色的智能体精心挑选的顶级资源合集，Claude Code，这款编程伴侣中的公认冠军，来自势不可挡的 Anthropic PBC 团队（无关联）.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 一个显示正在发生什么的 Claude Code 插件——上下文使用情况、活动工具、运行中的代理和待办进度。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 面向 Claude Code CLI 的美观且高度可自定义状态行，支持 powerline、主题等.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 系统提示词的所有部分、27…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ 条技巧，帮助你充分利用 Claude Code，从基础到高级——包括自定义状态行脚本以及在容器中运行自身的 Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - 适用于 Claude Code 的精美 vim 风格 powerline。
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 在终端窗格中审查你的编程代理生成的差异，并将行级评论发送回 Claude Code、Codex、OpenCode 或 Pi。herdr 插件.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 适用于 Claude Code 的综合状态栏插件，包含上下文使用量、API 速率限制和成本跟踪。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - 为 Claude Code 构建 mods：拦截任意请求、修改任意响应、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - 适用于 Claude Code 的综合状态栏仪表板——会话信息、配额条、代理跟踪器、MCP 健康状态、消息历史等.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：跟踪你的 Claude Code 会话的碳足迹。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - 由 awesomejun 制作的 Claude Code 美观状态栏。
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公开的 Claude Code 技能和 mods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code 的技能、mods、子代理、钩子、斜杠命令和指南——可由你的代理安装（参见 INSTALL.md）。
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免费的 LLM APIs 和编程代理——每周自动更新，并经过两次探测验证。免费层级、无需信用卡的试用、免费模型.
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - 用于 Claude Code 的快速、零依赖成本计算器和可自定义 statusline。按模型、日期、项目和分支分解。轻量级，单二进制文件，无需运行时.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - 用于 Claude Code 会话的终端状态栏。
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 在你的终端、你的 Claude Code 和 Cursor CLI 状态行以及 MCP 客户端中，提供你关注的赛事。
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 将你的编程代理变成键盘固件专家的 Agent Skill。审计 ZMK/QMK 键位映射，调整 home row mods，使轨迹球具备层感知能力，使用 CI…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供礼拜时间、回历日期、adhkar、每日经文、圣行斋戒、Ramadan、Jumu。
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - 个人 Claude Code 配置，版本控制于 ~/.claude 中 — agents、skills、hooks、settings 和…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness plugin for research topics…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - 适用于 Claude Code 的双行真彩色状态栏。
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - 适用于 .NET DDD/Clean Architecture 的便携式 Claude Code 工具包：严格的 TDD…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - 轻量级 Claude Code 状态栏——一个约 170 行的 Bash 脚本，零依赖（不需要 jq、Node、Python、守护进程或配置）.
- [yuyongyan29-dev/claude-pet](https://github.com/yuyongyan29-dev/claude-pet) - Clawd, a pixel pet that lives above your Claude Code prompt — a Claude Code…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：技能和 mods，经过整理，可在任何人的机器上运行.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code 插件和技能市场，用于促进对游戏 Hytale 的 mods 开发。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code 的令牌治理：顶级模型负责指挥，执行交给满足要求的最低成本手段。路由内核、由 hook 强制执行的预预算、遥测，以及带计划配额的状态栏.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - 适用于 Windows Terminal 和 tmux 的 Claude Code 分屏查看器：以渲染后的 Markdown 显示会话，包括子代理、实时…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - 用于Claude Code Awesome Media mods 的仓库.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - 降低 Claude Code 和 Codex 的令牌消耗：将查询和测试运行路由到更便宜的模型，把文档转换为紧凑的…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - 适用于 Linux、WSL、Windows 和 macOS 的可配置 Claude Code 状态行，包含提示计时、subagent 行和终端配置 UI.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - 显示 Claude Code statusline，包含速率限制、当前目录和 Git 分支信息，以提升工作区感知.
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code 的状态栏和令牌栏：上下文、5 小时和每周用量及速率标记、活动、git 和成本.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - 显示 Claude Code 的关键状态详情，包括模型、上下文、限制、git 信息和会话时间，适用于 macOS、Linux 和 Windows.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 原生代理团队。尽在掌控。适用于 Claude Code 的严格工作者限制、实时团队可见性和可移植配置.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code 附加组件：标签状态彩色圆点监视器 + 内置 GSD 状态栏。
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr 上可定义的Claude Code 软件工厂：xstate station 图、管理器 mod、rigs、beads 和共享内存。
- [zirkelc/claude-quick-actions](https://github.com/zirkelc/claude-quick-actions) - One-click buttons above the Claude Code prompt for the skills, prompts and…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - 适用于 macOS 和 Linux 的 Claude Code 使用量状态行，打包为 herdr 安装器插件。显示使用百分比、缓存倒计时、上下文和成本.
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - 个人 Claude Code 插件市场（todo-pane）。
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod: a CRT-style status panel for Claude Code, in the terminal…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code 在 Lua 中的状态栏，带有实时 Neovim playground。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 专业级 Claude Code statusline：会话时长、带 ECB FX 的多币种成本、每 MTok 费率、支出上限。MIT、zero-key、跨平台.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - 了解订阅状态的 Claude Code 状态行。
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - 西班牙语 Claude Code 状态栏：任务、skills、带红绿灯指示的上下文、5h/每周使用量和模型。
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - 多彩的 Claude Code 状态栏：计划限额、上下文、成本和 tokens。
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - 适用于 Windows 的 Claude Code 状态栏：token 总量、按 API 费率计算的成本，以及 5h 和 7d 时间窗口的限流重置倒计时.
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Claude Code 的单行状态栏：模型、git、上下文、令牌、成本、运行时间、速率限制。
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - 在 Claude Code 中预览图片：将鼠标悬停在回复下方的标签上即可弹出图片，或使用 /img &lt;path&gt; 在窗格中打开图片.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - 带代理面板行的 Claude Code 状态行。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 将 Claude 的待办事项同步到 Fizzy.do，实现团队实时可见；把任务转换为持久卡片，提升协作并轻松跟踪进度.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Display a detailed, color-coded status bar for Claude Code showing context, git…
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Talk to Claude Code by voice on Windows: a Mod + helper using codex app-server…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - 使用紧凑型仪表板跟踪 Claude Code 状态，显示上下文、成本、时长、Git 分支、速率限制和实时用量。
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code 状态栏钩子——跨会话、压缩操作和 --resume 跟踪 token 使用量与上下文。
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd，Claude Code 的像素艺术伙伴，以及 atelier，Android Code 开发的安全护栏。粉丝制作，非官方.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 环境安装器：技能、状态栏、钩子、权限，以及可选的 Obsidian-vault MCP 服务器（--vault_root）.
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Nacho 的 Claude Code Harness（规则、看板、模组）。
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Multi-line Claude Code status line: context bar, git branch, 9router…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - HUD 风格的 Claude Code 状态栏——网络健康状况、TPS、上下文、配额、成本，全部显示在一行中。
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - OrihuelaConde 为 Claude Code 制作的插件和模组。
- [Paradigm-Study/claude-share](https://github.com/Paradigm-Study/claude-share) - Shared Claude Code sessions: share a session with a link, teammates join from…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline ——适用于 macOS + Linux 的 Claude Code statusline.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitor Claude Code status from your macOS menu bar with real-time indicators…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - 适用于 Claude Code 和 Cowork 的技能与模组——项目跟踪器、参考文档等——打包为可安装的插件市场.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - 适用于 Windows 的 Claude Code 状态行（PowerShell）：使用量条、5 小时/7 天重置倒计时及用量速度警告、自动换行。
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - 适用于 Claude Code 的技能、模组、钩子和状态栏，以及用于在多台计算机之间同步配置的引擎。
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Claude Code 的双行状态栏（git、模型、上下文栏、成本、用量限制），附带可安装它的提示词.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 自定义 Claude Code 状态栏（上游：kamranahmedse/claude-statusline）。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code 配置和模组，带有共享组件套件、playground 和 Storybook。
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Claude Code 的入门 Harness：钩子、状态栏、本地模型、群体调度和工作区模板.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Code 的便携式配置（状态栏 + 安装程序）。
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude Code 的小型仪表板：上下文百分比、缓存倒计时、5 小时和每周用量、一键将 Handoff 转到新聊天，以及在 Claude 忙碌时用于修复…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Claude Code 的自定义终端状态栏：模型、目录、Git 状态、上下文用量和速率限制。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 便携式 Claude Code 配置：CLAUDE.md、settings、状态行、技能。
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Track Claude Code context usage, session costs, and rate limit resets with a…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用の mod 集 (goal-orchestrator: /goal をタスク分解して SubAgent に委譲させる)。
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code 状态栏：当前模型 ID、主机名、可点击的 git 仓库链接，以及项目中运行的 LAN 服务。简洁安静的一行.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code 技能（VS Code、Windows）：在聊天中的文件路径下显示图像预览和打开按钮、可点击的本地链接、上下文环以及自定义编辑器按钮。
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Claude Code 状态栏，带渐变进度条、按颜色分级的会话工作量，以及适配 worktree 的路径。
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Claude Code 状态栏：文件夹、git 分支、模型、上下文窗口使用量和计划使用限额。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026——面向 Claude Code 代理的主动式 AI 记忆与速率限制监控器。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks, subagents and statuslines: open-source collections and…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 显示实时令牌使用量和预计能耗的 Claude Code 状态栏。
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - 由 Deno 驱动的 Claude Code CLI 状态行。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 的 mods：基于函数钩子构建的面板、条带和伙伴。
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - 适用于 Pi 编程 agent 的 Claude Code 风格 UI 捆绑包——工具渲染、加载指示器、状态栏、主题、设置向导。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的Claude Code 会话之间传递任务。将更改交给负责某个仓库的会话.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 这是一个用于控制 MODS 的MCP服务器。MODS 是面向 Fablabs 的模块化跨平台工具，包含 CAD/CAM 和机器控制工具.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用于使用本地LLM翻译 CK3 mods 的Codex和Claude Code 技能。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - 用于Claude Code 的开源 mods 和其他扩展。
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code 状态栏：CCometixLine 美化效果 + Claude HUD 功能。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你反复要求Claude Code 做的事情，并将其变成 mod。此外还包括 8 个示例 mods 和一个虚拟办公室.

</details>

<a id="dsh-cordis"></a>

## DSH 和 Cordis 插件生态系统

DeepSeek Harness 和 Cordis 从不同方向抵达同一目的：对它们而言，插件就是 mod 机制，因此那里的插件相当于这里的 mod。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74385 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **74385**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐125056 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **125056** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100648 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **100648** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82288 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **82288**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35767 · Go · 🔎 inferred · 0 天</summary>

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
| 星标     | **35767**  |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25508 · Python · 🔎 inferred · 0 天</summary>

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
| 星标     | **25508**  |
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
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8651 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **8651**   |
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
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐7881 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **7881**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4544 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **4544**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4323 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **4323**   |
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
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐2954 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Answer me with HTML — an agent skill that answers hard questions with a one-page HTML you can actually read. 让 AI Agent 用一页 HTML 回答复杂问题。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **2954**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1600 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

跨设备的开源Agent工作台

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1600**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/OpenPetsHQ/openpets">OpenPetsHQ/openpets</a></b> · ⭐1281 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Local first, desktop companion platform with animated pets, plugin SDK and coding-agent integrations.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1281**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `ai-agents` · `claude-code` · `coding-agents` · `desktop-companion` · `desktop-pet` · `dsh-plugin` · `electron` · `mcp`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/openpetshq--openpets/cc09d7a603fef14d.png" width="100%" alt="OpenPetsHQ/openpets screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1178 · Go · 🔎 inferred · 0 天</summary>

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
| 星标     | **1178**   |
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
<summary>🧵 <b><a href="https://github.com/ysr666/dsh-vision-router">ysr666/dsh-vision-router</a></b> · ⭐1145 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Eyes for text-only DeepSeek Harness agents: built-in free vision chain (no key) + pixel-level vision tools (Q&A, grounding, crop, pixel diff, colors, OCR, SVG trace, cutout, screenshots). One-command install, no Python, image turns work like ordinary tool-calling turns.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1145**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `multimodal` · `vision`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ysr666--dsh-vision-router/106ad9ed68079834.png" width="100%" alt="ysr666/dsh-vision-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ysr666--dsh-vision-router/d79f0c95491a7bc3.gif" width="100%" alt="ysr666/dsh-vision-router animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1009 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

最全面的 DeepSeek Harness 插件市场——每日更新，信息来源遍布互联网，发布前经过审核。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1009**   |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐552 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **552**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>动画录屏 · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">打开视频</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/1692775560/dsh-Mimir-Academic-research">1692775560/dsh-Mimir-Academic-research</a></b> · ⭐548 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Mimir — 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表、GPU 服务器 SSH 任务编排，管理科研全周期。An open-source research workbench plugin for the whole research cycle.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **548**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `arxiv` · `bibtex` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `experiment-tracking` · `gpu-cluster` · `latex`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/1692775560--dsh-mimir-academic-research/3574bee232095c3c.png" width="100%" alt="1692775560/dsh-Mimir-Academic-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/1692775560--dsh-mimir-academic-research/e05a56815f6c9f53.gif" width="100%" alt="1692775560/dsh-Mimir-Academic-research animation"><br><sub>动画录屏 · <a href="https://raw.githubusercontent.com/1692775560/dsh-Mimir-Academic-research/main/docs/media/mimir-demo.mp4">打开视频</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

📚 一个零依赖、由 git 支持的微型课程库，供 AI Agents 异步分享和搜索经过验证的调试经验。| https://misakanet.org

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **526**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

ACRYL - Agent Context Relay Yielding Lifecycles。一个持久化工作区，一个权威上下文，支持任意编码 Agent。

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
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

原生 DeepSeek Harness (DSH) 插件，将 TypeSafe Jev 或像 luna 这样的 Decision api 集成为用于代理选择、监督、修正和审批的 System One 决策层。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **204**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐180 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness (DSH) 备份与恢复插件——导出、导入、迁移并同步完整的 DSH 配置、插件、MCP 服务器、技能和工作区。一键迁移到另一台机器。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **180**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/sorsama/deepseek-harness-mobile">sorsama/deepseek-harness-mobile</a></b> · ⭐146 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness 的 Android 配套应用 | 在手机上通过局域网进行聊天、管理目标、审批和接收通知。Kotlin + Jetpack Compose。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Kotlin                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **146**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `ai-agents` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sorsama--deepseek-harness-mobile/11352624becb7d93.jpg" width="100%" alt="sorsama/deepseek-harness-mobile screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **137**    |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

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
| 首次列入 | 2026-10-12 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
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
| 首次列入 | 2026-10-12 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/webkubor/dsh-bloom-theme">webkubor/dsh-bloom-theme</a></b> · ⭐59 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness (DSH) 主题插件：Bloom 莫兰迪配色 10 套中国风命名（黛蓝/朱砂/桃夭/天青/竹青/赭石/青金/琥珀/落霞/青莲），OKLCH 调色，明暗双主题，顶栏一键切换，20 组配色实测全部达 WCAG AA

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **59**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `accessibility` · `color-scheme` · `dark-theme` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `morandi`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/webkubor--dsh-bloom-theme/107985cbb7fe6b29.png" width="100%" alt="webkubor/dsh-bloom-theme screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **53**     |
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
<summary>🧵 <b><a href="https://github.com/398894496-arch/KRouter">398894496-arch/KRouter</a></b> · ⭐44 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

你的编码代理会记住你的决策，以及你做过的修改。基于 Obsidian 的纯 Markdown 记忆，由 Claude Code、Codex 和 Cursor 通过 MCP 共享。每个回答都会引用其页面；当知识库中没有答案时，它会如实说明。安装时会导入你过去的会话。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **44**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent-memory` · `ai-agents` · `chinese` · `claude-code` · `claude-code-plugin` · `codex` · `cursor` · `deepseek`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/398894496-arch--krouter/482bdf9e0e0aaa00.gif" width="100%" alt="398894496-arch/KRouter screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/398894496-arch--krouter/482bdf9e0e0aaa00.gif" width="100%" alt="398894496-arch/KRouter animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **44**     |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐36 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **36**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

NekroNXT：基于 DeepSeek Harness（DSH）的多平台群聊智能体系统｜A DSH-powered multi-platform group-chat agent system

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **35**     |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 59</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - 面向 AI 编程代理的执行前防护工具。在工具调用运行前，它会阻止破坏性的 Git 和文件系统命令，以及常见的访问敏感文件的尝试.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - 为包括 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 用于会自我迭代的软件的插件运行时——代理可在其中编写、替换并热加载自己的插件，支持 Rust、TypeScript、Python 和 Go，跨进程和机器运行.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 插件精选目录 — 14 类 280+ 个社区插件，覆盖 MCP / Skill / TUI / 多 Agent…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI 插件集合——任务通知、提供商用量、LAN 代理、MCP 管理器、worktree…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A commerce negotiation runtime + DeepSeek Harness (dsh) plugin.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - DeepSeek Harness Web 的工具箱面板：MCP 管理器。
- [liustack/pptwise](https://github.com/liustack/pptwise) - A real PowerPoint, not HTML. Tell your AI what to cover and pptwise builds an…
- [ppy-web/dsh-plugin-xiaomi-mimo-tts](https://github.com/ppy-web/dsh-plugin-xiaomi-mimo-tts) - 给DSH接入免费的 Xiaomi MiMo TTS API，支持使用预置/自定义/浏览器内置声音朗读正文。
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - 面向编程代理的本地优先代码知识图谱和上下文 harness。MCP + DeepSeek Harness（dsh）插件.
- [MichengAI/dsh-btw](https://github.com/MichengAI/dsh-btw) - DSH 一次性只读旁问插件：基于当前上下文回答，独立气泡，不执行工具 · One-shot read-only side-ask plugin…
- [zhu1090093659/dsh-skins](https://github.com/zhu1090093659/dsh-skins) - Skin center plugin and built-in skins for the DSH Web GUI: skins are pure asset…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Embedded C/C++ AI engineering plugin — firmware skills。
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表。
- [biedongbin/dsh-claude-compat](https://github.com/biedongbin/dsh-claude-compat) - DSH plugin: bridge Claude Code。
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [zhu1090093659/dsh-pet](https://github.com/zhu1090093659/dsh-pet) - Multi-pet companion plugin for the DSH Web GUI: a registry-driven floating pet…
- [islibaodong/dsh-login](https://github.com/islibaodong/dsh-login) - Multi-user login gateway plugin for the DeepSeek Harness Web GUI: login wall…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）。
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow。
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 插件的持续兼容性测试：精确的发布版本、隔离运行器，以及可修复的上游问题.
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - Zero-cost, zero-hassle toolkit for DeepSeek Harness (DSH): one-click setup for…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Guarded context compaction for DeepSeek Harness (dsh): the LLM proposes…
- [FrostLeafKEE/dsh-chat-bridge](https://github.com/FrostLeafKEE/dsh-chat-bridge) - Switch between DeepSeek web chat and workspaces in DeepSeek Harness.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness 主机插件，将项目文档和长期记忆以纯 Markdown 形式保存在专用的 Obsidian vault 中.
- [tafcear/kimi-tide](https://github.com/tafcear/kimi-tide) - 🌊 月汐（kimi-tide）— DSH…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 插件的 X 光检查：声明的能力与实际行为对比。注册表 + 静态扫描器 + 徽章.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）。
- [PeterBon/dsh-hooks](https://github.com/PeterBon/dsh-hooks) - Config-driven lifecycle hooks plugin for DeepSeek Harness。
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [JessenReinhart/dsh-tokenslash](https://github.com/JessenReinhart/dsh-tokenslash)
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [laoduu/DeepSeek-Harness-yizi-themes](https://github.com/laoduu/DeepSeek-Harness-yizi-themes) - 为 DeepSeek Harness（dsh）Web UI 提供的 19 个精品风格主题，完整移植自 YiziMarkdown 的设计语言.
- [openbkn-ai/bkn-dsh](https://github.com/openbkn-ai/bkn-dsh) - OpenBKN。
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Zero-dependency verification standard for DeepSeek Harness (dsh) plugins…
- [SuCriss/dsh-leekbox](https://github.com/SuCriss/dsh-leekbox) - 韭菜盒子 LeekBox — A股看盘助手 · DeepSeek Harness (DSH) web 插件。
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode——让 OpenCode Zen + Go 免费层模型持续工作的 DSH…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — 面向 DeepSeek Harness 的第三方插件市场和受保护的生命周期管理器.
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Run DeepSeek Harness on desktop with zero token costs—a free, open-source GUI…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - 为 DeepSeek Harness 提供开箱即用的编码 Agent — Claude Code 风格的工作流、可选模型、TUI、技能、子…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) - DSH的插件创意市场来啦!～～～欢迎使用&amp;提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [whyself/Amadeus](https://github.com/whyself/Amadeus) - Amadeus: a web workspace for DSH with cloud and web agents, online code…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 插件：将 Windows 沙盒 ACL 配置失败。
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 使一个未归属的空模型尝试可重试，适用于唯一能够判断的那个衔接点（deepseek-harness 讨论 #8321 和 #9352）.
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - dsh 自主目标回合的进度判断：后台作业运行时延后循环，并停止那些回合不再产生工具调用的目标（deepseek-harness 讨论 #7198）.
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - dsh 插件：将截断的长度停止转为 harness 已有的 CONTEXT_WINDOW_EXCEEDED 溢出恢复机制（讨论 #7214）。
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - 能够自我清理的插件：适用于 iOS 和 macOS 的 cordis 插件框架 Swift 6 移植版.
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - 一个 Rust 插件运行时，配备经 Verus 验证的生命周期内核和 Cordis 兼容适配器.

</details>

<a id="writing"></a>

## 文章、讨论与视频

关于模组功能的文章、讨论和视频。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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

<a id="other"></a>

## 其他项目

涉及 mod 接口但本身并非 mod 的条目，保留展示而不隐藏。

<details>
<summary>📦 <b><a href="https://github.com/rajmand/claude_mods">rajmand/claude_mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

上游未发布描述。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `其他项目`                                   |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **0**      |
| 最后推送 | 2026-10-12 |
| 首次列入 | 2026-10-12 |

</details>

<a id="projects-by-implementation-language"></a>

## 按实现语言分类的项目

该生态主要集中在 Python 和 TypeScript，但使用其他语言编写的客户端也在不断出现。本表根据条目自身内容生成。

| 语言       | 条目 | 示例                                                                                                               |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 399  | `anthropics/claude-code`, `anthropics/claude-code-action`, `AlekDob/blockodile-claude-mod`                         |
| JavaScript | 72   | `fschmutz/claude-usage-panel`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                  |
| Python     | 37   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `redfox-data/redfox-community-dsh` |
| Shell      | 28   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`                |
| HTML       | 11   | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                                 |
| Go         | 4    | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `esengine/DeepSeek-Reasonix`                            |
| Rust       | 4    | `persiyanov/herdr-reviewr`, `OpenClawFarm/claude-statusline`, `arcships/rutis`                                     |
| PowerShell | 3    | `GoSlowPoke168/claude-statusline`, `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win`     |
| Swift      | 2    | `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`                                            |
| C          | 1    | `reporails/arcade`                                                                                                 |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                            |
| CSS        | 1    | `zhu1090093659/dsh-skins`                                                                                          |
| Kotlin     | 1    | `sorsama/deepseek-harness-mobile`                                                                                  |
| Lua        | 1    | `crafts69guy/claude-statusline.nvim`                                                                               |
| MDX        | 1    | `jkf87/mod-guide`                                                                                                  |

<sub>仅统计声明了语言的条目。文档和讨论条目不包含在此表中。</sub>

## 参与贡献

欢迎提交更正，这是改进此列表最快的方式。如果某个条目归类错误、等级错误，或者某个项目因名称冲突而被错误排除，请提交 issue 或 pull request——最后这一类是自动筛选最容易出错的地方。

---

<sub>独立社区项目。与 Anthropic 没有关联，也未获其认可或审查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商标。产品行为可能随时变化；对于任何关键依赖，请以官方文档为准进行验证。相关资产仍归其上游项目所有，仅在许可证允许的情况下转载。</sub>

<sub>最后更新 · 2026-10-12T17:03:53+08:00</sub>
