<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="精选 Claude Mods">
</p>

<h1 align="center">精选 Claude Mods</h1>

<p align="center"><b>Claude Code mod、插件及其所改变的更深层行为的循证分级索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-594-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <b>简体中文</b> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **实时索引** · 上次同步: `2026-10-16T10:23:36+08:00` (UTC+8)
> · 条目: **594** · 最新更新中新增: **0** · 实现语言: **15**

<sub>以下每个条目均已自动收集、筛选并重新检查。这里没有付费展示内容。</sub>

<a id="featured"></a>

## 当下精选

<sub>每个类别精选一项，按证据等级和星标数排序，并在每次更新时重新计算。这是一个排名，不代表认可；每项精选都会链接到下方的完整卡片。优先选择发布了截图或录屏的项目，以便保持列表的视觉呈现。</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9528 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2571 · Python · 👁️ observed</sub>
<sub>找出幽灵令牌。修复它们。在压缩中存活。避免上下文质量衰减。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐75162 · TypeScript · 👁️ observed</sub>
<sub>🌊 原创 agent harness。部署智能多玩家群体，协调自主工作流，并构建对话式 AI 系统。具备自适应记忆、自学习智能、联邦、向量 RAG 集成，以及原生 Claude Code / Codex / Hermes 和更多集成</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## 目录

- [什么是 Claude Code mod](#什么是-claude-code-mod)
- [条目的分级方式](#条目的分级方式)
- [官方：Anthropic 自有的仓库和发行说明](#官方anthropic-自有的仓库和发行说明) — **19**
- [Mods：使用 mod 能力构建](#mods使用-mod-能力构建) — **480**
- [DSH 和 Cordis 插件生态系统](#dsh-和-cordis-插件生态系统) — **87**
- [文章、讨论与视频](#文章讨论与视频) — **8**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151080 · TypeScript · ✅ official · 0 天</summary>

##### 📝 摘要

Claude Code 是一个存在于你的终端中的代理式编码工具，能够理解你的代码库，并通过执行常规任务、解释复杂代码以及处理 git 工作流来帮助你更快地编码——这一切都通过自然语言命令完成。

<sub>🔧 在代码中发现使用: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 基本信息

| 字段 | 值                                     |
| ---- | -------------------------------------- |
| 类别 | `官方：Anthropic 自有的仓库和发行说明` |
| 依据 | `由 Anthropic 自行发布`                |
| 语言 | TypeScript                             |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **151080** |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9528 · TypeScript · ✅ official · 0 天</summary>

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
| 星标     | **9528**   |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8288 · Python · ✅ official · 0 天</summary>

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
| 星标     | **8288**   |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6393 · Python · ✅ official · 246 天</summary>

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
| 星标     | **6393**   |
| 最后推送 | 2026-02-11 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

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
| 星标     | **1813**   |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>此类别中的更多内容</b> <sub>· 7</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 为 mods 添加了 `$.ui.notify`：通过你自己的通知设置发出原生通知，并说明发送通知的频道为 mod 的 `Button` 添加了子项：字符串和…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 修复了 `UserPromptSubmit` 钩子或模组的 `prompt.submit` 钩子期间按下 Esc…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod。
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod。
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - A curated directory of source-verified DeepSeek Harness (DSH) plugins, tools…
- [songoao25/dsh-chatgpt-sub](https://github.com/songoao25/dsh-chatgpt-sub) - ChatGPT Subscription - a DeepSeek Harness plugin: bind your ChatGPT account via…

</details>

<a id="mods"></a>

## Mods：使用 mod 能力构建

此处的每个条目都展示了使用 Claude Code 在 2.1.287 中获得的能力的证据：通过 `ui.render` 进行绘制，拥有窗格、横条或卡片，读取 `$.ui.selection()`，通过 `agent.spawn` 生成协作者，或明确说明自己是 mod。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2571 · Python · 👁️ observed · 0 天</summary>

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
| 星标     | **2571**   |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐833 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 摘要

Custom Claude Code Mods that I need

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **833**    |
| 最后推送 | 2026-10-14 |
| 首次列入 | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐601 · JavaScript · 👁️ observed · 0 天</summary>

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
| 星标     | **601**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐257 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **257**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐215 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **215**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐206 · HTML · 👁️ observed · 0 天</summary>

##### 📝 摘要

Mods for Claude Code. effortless picks the reasoning effort for every prompt and shows the cache countdown. textless shows art, quotes and chess instead of the wall of text while Claude works.

<sub>🔧 在代码中发现使用: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | HTML                                         |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **206**    |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `ai-tools` · `anthropic` · `chess` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐194 · TypeScript · 👁️ observed · 11 天</summary>

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
| 星标     | **194**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐152 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code 的皮肤：带图标的工具行、差异、表格和 Mermaid 图表卡片、使用量条带及十五种主题。/skin 可实时切换。

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **152**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐116 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **116**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐105 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 在代码中发现使用: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **105**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐94 · TypeScript · 👁️ observed · 3 天</summary>

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
| 星标     | **94**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

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
| 星标     | **80**     |
| 最后推送 | 2026-10-08 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/REMvisual/claude-handoff">REMvisual/claude-handoff</a></b> · ⭐64 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code session handoffs — now a Claude Code mod: /compact-handoff swaps the conversation for a validated handoff and keeps going. Skills + chain-linked sessions.

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **64**     |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-16 |

🏷 `agentic-ai` · `ai-coding-agent` · `anthropic` · `anthropic-claude` · `claude-code` · `claude-code-skills` · `claude-skills` · `compaction`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/remvisual--claude-handoff/7da5cfcffe4d5280.png" width="100%" alt="REMvisual/claude-handoff screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 摘要

Claude Code mods：在提示词上方显示实时计划进度条

<sub>🔧 在代码中发现使用: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **54**     |
| 最后推送 | 2026-10-14 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>动画录屏 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">打开视频</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐36 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **36**     |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **30**     |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 摘要

Claude Code mods：Claude Tools 菜单、Zen 模式、终端主题、工作量和模式控制

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
| 最后推送 | 2026-10-14 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

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
| 星标     | **22**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

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
| 星标     | **16**     |
| 最后推送 | 2026-10-05 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 摘要

Claude Code 中的 LINE：作为 Claude Code mod 的 enil TUI

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **15**     |
| 最后推送 | 2026-10-13 |
| 首次列入 | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| 星标     | **14**     |
| 最后推送 | 2026-10-03 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| 星标     | **14**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 2 天</summary>

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
| 最后推送 | 2026-10-13 |
| 首次列入 | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

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
| 星标     | **12**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐11 · TypeScript · 👁️ observed · 12 天</summary>

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
| 星标     | **11**     |
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
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
| 星标     | **10**     |
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 30 天</summary>

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
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 摘要

Claude Code 的面板、防护栏和生活质量 mods：上下文、使用量、实时活动、通知、安全规则、提示词教练、命令中心。

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
| 最后推送 | 2026-10-06 |
| 首次列入 | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/timoncool/givememod">timoncool/givememod</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

按需生成 Claude Code 模组——一种读取你的对话并构建合适模组的技能：计划进度条、文件窗格、上下文仪表、危险命令防护、测试监视器。11 个经过测试的模板、29 个构建模块，以及一个包含 3,057 个公开模组的地图。终端和桌面端。

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
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-11 |

🏷 `agent-skills` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-skill`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/timoncool--givememod/6fb8ba0c74031f7f.png" width="100%" alt="timoncool/givememod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/timoncool--givememod/5f58df5c7bdd37f9.gif" width="100%" alt="timoncool/givememod animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 446</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - 100 多个可与 Claude Code 配合使用的 mods 集合.
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad 的 Claude Code mods：窗格、条带、提示词保护、密钥处理和记忆工具。一个市场，每个 mod 独立安装.
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - 适用于 Claude Code 的专家技能、代理、命令、规则、钩子和输出样式——会话连续性 + 面向真实开发工作流的现代 CLI 工具。
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其构建工具：先使用构建器技能，然后使用 mods。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四个 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 和 Collision Guard。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天运行的 Claude Code harness，自第一天起就以此名称发布，如今与 ucsandman/Agnostic-AI…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）。
- [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) - A measured tool-call firewall for AI agents: allow, ask or deny before the…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - 在 Claude Code 中使用 Xcode 的构建、测试、控制台和 SwiftUI 预览。
- [BrianHuang813/clawd-actor](https://github.com/BrianHuang813/clawd-actor) - Claude Code mod：Clawd 在提示词上方演示 Claude 正在做什么。
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 关于 Claude Code mods 的有来源引用的 Obsidian 知识库：它们的工作方式、构建方法，以及安装前的检查方法.
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods：在 Claude 读取提示词前修正并翻译它们。
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 来自 Nekyia Labs 的 Claude Code mods 和技能，由生活在持久化家园中的 AI 每天构建和使用。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的侧边面板：显示会话运行的子代理、每个子代理正在做什么及其令牌，并可一键查看其对话.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 适用于 Claude Code 的 Claude Mods（函数钩子插件）.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code 的浮动状态卡片——模型、上下文、速率限制、成本、分支——另有一个任何脚本或模组都可以提供进度的 API。
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教会 Claude Code 代理构建 Claude Mods（函数钩子插件）的技能，附带入门示例。
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code。
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 面向与对话代理协作的人类用户的决策队列 CLI/TUI。代理发布问题，人类从一个收件箱中回答.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社区 Claude mods、插件和技能，可从一个市场安装。
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss 制作的 Claude Code 模组。
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods 画廊：经过检查并固定的 Claude Code mods.
- [Danovich/turntype](https://github.com/Danovich/turntype) - 在 Claude 工作期间进行的打字测试。一个 Claude Code mod.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code mods 的 app store，位于 Claude Code 内：/mods 可浏览、搜索并安装 2,700 个 mods，或让…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 六个 Claude Code…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod（插件），添加一个带 Activity、Files、Agents、Context 和 MCP…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code 修改插件，在两列并排布局中绘制 Edit 和 Write 差异。
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf。
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code 的 Mods：为终端 UI 添加实时窗格和行为的函数钩子插件。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard 在屏幕共享时遮盖姓名和机密信息；cache-panel 会在提示词缓存即将失效前提醒你.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code 的 Mods 和 skins：为 Claude 的任务提供实时进度条、带匹配 Windows Terminal…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code 扩展。释放 Claude 的全部力量.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示词框上方的两个 Claude Code mods：上下文窗口计、5 小时限制、提示词时钟和会话成本。
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca。
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 读取 Claude Code 命名的 markdown 文件，并将其渲染在会话旁边；指向任意代码块即可让 Claude 编辑它.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code 的 GlanceFlow：提示词上方的简洁清单，展示计划、进度以及何时需要 Claude。人人都能使用的简洁视图，面向工程师的详细信息.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：上下文栏、代理面板、PDPA 模糊处理。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在任意终端中将粘贴的图像缩略图显示在提示词上方。
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的语音协作者。与由 ElevenLabs conversational AI 驱动的 3D…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 用于同时运行多个会话的两个Claude Code mods：提示词上方的上下文卡片和聊天旁边的会话窗格.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed，一款带有每条提示统计信息的实时打字速度计。
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 的 mods：使用插件函数钩子API构建的窗格、命令和钩子。
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 探索Claude Code mods、插件和扩展，浏览动画演示、分类列表和直接源代码链接。由 FindMods.dev 提供支持.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：在记录中内联绘制 mermaid 图表。
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code 修改插件（函数钩子插件）：session-switcher 及更多。
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout（查找你最常使用的 mods）、usage-meter、check-ledger、resume-nudge。
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren 的 Claude 工具包：适用于 Claude Code 的技能、模组和 MCP 服务器。通过插件市场一键安装.
- [nuromirzak/nibbl](https://github.com/nuromirzak/nibbl) - A tiny pixel pet that nibbles your bugs. Lives above your Claude Code prompt.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 我制作的一批 claude code mods。
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：发现、检查、切换和更新Claude Code mods。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最佳Claude Code Mods：精选、已验证、已置顶。一次 /plugin marketplace 添加，包含 43 个 mods.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 面向真正工程师的 Claude Code mods。
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 插件：自动进行 Claude 模型路由。为每条提示词、步骤和子代理选择 Haiku、Sonnet 或 Opus…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code 的六个 mod：动画 Clawd 吉祥物、用量限制和提示词缓存条、发送前消息检查器、快捷回复、待办队列和成本账本.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - 适用于 Claude Code 的开源 mods：面板、状态栏、提示、工具防护和斜杠命令.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code 模组：直接在文本上逐点回答 Claude。选择对话中的任意部分，对其发表评论，并将所有评论作为一个提示词发送.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス。
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 的 mods：Clawd，一个会演示Claude正在做什么的小型像素吉祥物。
- [reporails/arcade](https://github.com/reporails/arcade) - 经典桌面游戏作为Claude Code mods，在Claude工作时于窗格中运行。由 Reporails 制作.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - 用于 claude 的 code-mods。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 一个 Claude Code 修改插件，可通过命名配置文件按仓库启用或禁用全局技能、agents、规则和工具.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 经过测试、可一键安装的 Claude Code 模组：YOLO 模式防护、实时成本和上下文、窗格、宠物等。另附精选的最佳社区模组列表.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code。
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精选的 Claude Code 模组列表，可作为插件市场安装：主题、窗格、状态栏、肖像.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 两个 Claude Code mod：cache-keeper 和 ctx-mod。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 让代理保持诚实的Claude Code mods——用于守护范围、验证部署并在提示词上方绘制会话的函数钩子.
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin。
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory。
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification。
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 用于在工作中途记录想法、跨项目和机器整理想法，并将其转换为提示词的 Claude Code mod。
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - 寫 code 時養一顆慢慢入味的茶葉蛋 · Raise a tea egg that slowly marinates while you code。
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（marketplace herman-mods）。
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code 模组：为每个子智能体选择模型和推理强度。
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code 插件（mod），让 Claude Code 终端界面看起来像 Claude 桌面应用：提示气泡、Markdown 表格、mermaid…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在后台运行的内容：子代理、Codex 作业、shell、监视器、cron 作业和工作流.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - 关于 Windows 上 Claude Code mod 的首日现场笔记：上下文/配额燃料条、泰语 UI mod、Matrix…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better。
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：在提示词上方显示实时成本、上下文和计划配额计量器。图标需要 Nerd Font.
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs。
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈。
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band。
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 插件和 mod：一个 AI 原生 SDLC（意图 → 规格 → 计划 → 构建 → 验证 → 评审），带有通过 hook…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Claude 搞砸时就揍它 — 一个适用于 Claude Code 的减压修改模块：卡通屁股、8 个拍打动作、9 个屁股、标记、连击和音效.
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar for Claude Code: usage limits, context, model, cost, git and session…
- [WQGGSEY/cache-ttl-timer](https://github.com/WQGGSEY/cache-ttl-timer) - Claude Code mod: a prompt-cache TTL countdown in the prompt footer, beside the…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - 使用 Claude Code 工作时学习一门外语。
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - 用于 Claude Code 的实时成本、token 和上下文用量侧边栏：一个在会话内显示每轮成本、缓存命中率、消耗速率和 30 天支出的 mod.
- [Br4inergy/claude-hands-off](https://github.com/Br4inergy/claude-hands-off) - Your AI agent can&#x27;t push to a repo, deploy a project or drop a table that isn&#x27;t…
- [Caesarcph/claude-mods](https://github.com/Caesarcph/claude-mods) - Two Claude Code mods: prompt-upgrade and auto-model。
- [CircularBlox/Clarity](https://github.com/CircularBlox/Clarity) - A clearer Claude Code terminal: boxed and organized you/claude conversations…
- [clafronteaccnts/commanddeck](https://github.com/clafronteaccnts/commanddeck) - Claude Code mods: command deck, GitHub issues pane, prompt upgrader, auto model。
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 一个 Claude Code mod：持续列出对话中的未完成事项，并在提示词上方的条带中显示.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每个 Claude Code 代理在其上下文中有哪些文件，以及每个文件占多少.
- [daydeda/daymods](https://github.com/daydeda/daymods) - Small, independent mods for Claude Code: install only the ones you want.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 用于终端和桌面应用的 Claude Code 小型 mods。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI 技能 + mod，可在 agent 回复中加入西班牙语单词。
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - 你的 Floatee 待办事项列表显示在 Claude Code 的提示词上方：一键运行、指导并勾选你的 todos.
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [HoyngM/claude-mods](https://github.com/HoyngM/claude-mods) - Mods for Claude Code。
- [iuliandita/mods](https://github.com/iuliandita/mods) - Claude Code mods you can install one at a time.
- [joaquinsalinas06/crabbus](https://github.com/joaquinsalinas06/crabbus) - See what every Claude Code subagent is really doing — two-way messaging, tokens…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 上下文窗口作为提示上方的一行，按照 Claude Code 绘制其自身仪表的方式绘制.
- [KTCrisis/flux7-mods](https://github.com/KTCrisis/flux7-mods) - Claude Code mods: machine-face avatars that judge tool calls, and live mesh7…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - 在等待 Claude Code 的回答时，不要让注意力飘走.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - 一个免费的开源 Claude Code 插件。在你执行 /clear 前，Claude 会写下一份可阅读和编辑的简短交接记录，下一次会话将从中继续.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session。
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [nonputtipong/claude-code-prompt-enhancer](https://github.com/nonputtipong/claude-code-prompt-enhancer) - ✻ A Claude Code mod that rewrites your rough draft into a clear, project-aware…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文档事实核查器、代码审计器、错误记忆日志、mod 等.
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code buddy 插件：提示上方的 ASCII 伙伴，会记住你的规则并标记 Claude 的快捷方式。
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work。
- [Steady-Matter/spotter-pals](https://github.com/Steady-Matter/spotter-pals) - Spotter: a Claude Code mod with pixel Pals that hatch and grow as your helper…
- [swicken/tiller](https://github.com/swicken/tiller) - Local daemon + Claude Code mods for spawning, messaging and controlling agent…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一个 Claude Code 模组，可按请求朗读 Claude 的回复和你的提示词，使用本地开源 Kokoro TTS 语音.
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop。
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用于实时窗格、成本感知模型路由和安全防护的小型插件。只需一条命令即可从市场安装.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 与插件：使用量监视器、令牌跟踪器和状态行.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude Code mods：EMCC（Every Mod Claude Code），为 Claude Code 精选并测试的 mods 集合。
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [1upcreative/ooze-o-meter](https://github.com/1upcreative/ooze-o-meter) - A bubbling ooze canister and lab log that fill live while rsync moves files to…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace)。
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [aiob3/claude-grounds-demo](https://github.com/aiob3/claude-grounds-demo) - Demo for claude-grounds (Claude Code mods): a median() bug with text sort and a…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [alanrsoares/claude-mods](https://github.com/alanrsoares/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示词上方的一只会动的盲文猫。
- [almost99/claudecode-mods](https://github.com/almost99/claudecode-mods) - Approved Claude Code Mods。
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示符上方的一只像素猫，会运行一次 OmniDimension 语音代理测试通话。Claude Code 修改.
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一种 Claude Code mod，会选择合适的时机进行压缩，以保持较小的上下文窗口.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - 用于 Claude Code 的 Claude Mods：token-meter。
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - 用于Claude Code 的通用 mods：顶部栏、窗格、toast 和钩子。包括 usage-bar：显示在提示词上方的上下文、成本和计划限制.
- [AnnihilationWizard/secret-guard](https://github.com/AnnihilationWizard/secret-guard) - A Claude Code mod that adds a gitleaks pre-commit hook to each Git project you…
- [apiglue/claude-mods](https://github.com/apiglue/claude-mods) - Mods for Claude Code。
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 将你的 Claude 使用限制显示为动画村民生命值卡片，并带有每周节奏警告——一个 Claude Code mod。
- [astrosteveo/nebula](https://github.com/astrosteveo/nebula) - Claude Code mods and plugins。
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作时进行短时锻炼：每日目标、连续记录、徽章和可选排行榜。一个 Claude Code mod.
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [bardaxx/spec-flow](https://github.com/bardaxx/spec-flow) - Claude Code mod: a side pane that follows a spec from idea to merge。
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods: live panes, bands and guards that run inside Claude Code。
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方显示 Apple Music 和 Spotify，带封面图、控制和 Up next 窗格。
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [broening/claude-mods](https://github.com/broening/claude-mods) - 适用于 Claude Code 的模组：缓存时钟、Blast Radius、建议、工作列表、Grill。
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是给你的 Claude Code 配一只猫头鹰。
- [CladiusIV/claude-mods](https://github.com/CladiusIV/claude-mods) - A Claude Code plugin marketplace of mods: changes to Claude Code。
- [danial112233/claude-skill-navigator](https://github.com/danial112233/claude-skill-navigator) - Claude Code mod: picks the installed skill that fits each request and tells…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [davidpravst/claude-mods](https://github.com/davidpravst/claude-mods) - Moji modi za Claude Code。
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [diegocamara89/claude-mods](https://github.com/diegocamara89/claude-mods) - Mods do Claude Code (function hooks): Sonnet por padrão para subagentes…
- [dj-thank/claude-x-timeline](https://github.com/dj-thank/claude-x-timeline) - X (Twitter) in Claude Code — a live, clickable timeline mod — and a template…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - My collection of claude mods.
- [DzmitryShut/once](https://github.com/DzmitryShut/once) - Claude Code mod: run one prompt on another model or effort.
- [ecombuilder-web/TripleDigit-file-links](https://github.com/ecombuilder-web/TripleDigit-file-links) - Claude Code mod: a Files pane beside the chat listing every file created or…
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [Elmanuel1/claude-mods](https://github.com/Elmanuel1/claude-mods) - Claude Code mods: docs-watch。
- [evertonalves-ai/mod-forge](https://github.com/evertonalves-ai/mod-forge) - Claude Code skill that builds, debugs, audits and packages Claude Code mods…
- [fabiobosioit/claude-mods](https://github.com/fabiobosioit/claude-mods)
- [fbwndrud/tidia](https://github.com/fbwndrud/tidia) - Tidy dictation for AI: a Claude Code mod that cleans up voice dictation before…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods（function-hook 插件）：session-meter 及更多。
- [flaviorg/crew](https://github.com/flaviorg/crew) - Claude Code mod: a live panel of the subagents Claude delegates to — model…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code。
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace。
- [Fox1304/FT_Claude_PromptUpgrader](https://github.com/Fox1304/FT_Claude_PromptUpgrader) - Claude Code mod: upgrades unclear prompts with a short question panel and picks…
- [FranciscoDeLaPuente/claude-mods](https://github.com/FranciscoDeLaPuente/claude-mods) - Claude Code mods and cross-platform installers (Windows, Linux, macOS, WSL)。
- [geonhos/claude-code-mod](https://github.com/geonhos/claude-code-mod)
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [heidiks/agent-kit](https://github.com/heidiks/agent-kit) - Skills, plugins and Claude Code mods. Install only what you need.
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Claude Code 的实时支出计量器：显示包含子代理和工作流的会话成本，停靠在右侧。
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-effort-switch](https://github.com/HuliLulu46/cc-effort-switch)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模组：每个回答花了多长时间、Claude 思考了多久，以及 tok/s，显示在 Claude 桌面应用中回复的正下方.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [iamshadmantaqi/claude-usage-band](https://github.com/iamshadmantaqi/claude-usage-band) - Claude Code mod: one bar above the prompt with context against your…
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian。
- [ikstewa/workstreams](https://github.com/ikstewa/workstreams) - Experimental claude code mod for managing work。
- [ilya-paskhover/claude-code-mods](https://github.com/ilya-paskhover/claude-code-mods) - Claude Code mods: turn-pulse (last-turn summary band) and notes。
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jenkinv/claude-img-viewer](https://github.com/jenkinv/claude-img-viewer) - Show images inside Claude Code。
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（a Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（a Claude Code mod）。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（a Claude Code mod）。
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（a Claude Code mod）。
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（a Claude Code mod）。
- [jeyu5m123/prompt-upgrade](https://github.com/jeyu5m123/prompt-upgrade) - Claude Code mod: the /better command upgrades a rough prompt before it is sent.
- [jiroamato/claude-mods](https://github.com/jiroamato/claude-mods) - Jiro。
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jrlprost/claude-code-mods](https://github.com/jrlprost/claude-code-mods) - Claude Code mods I build because I need them: context bar, plugin toggler, and…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [Jsolee/claude-mods](https://github.com/Jsolee/claude-mods) - Mods de Claude Code de Joan Solé: comunitat, el panell dels subagents amb el…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的条带中：演绎会话、显示正在运行的内容、上下文和用量限制，并与你的 CI 构建赛跑。非官方粉丝模组.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code の返答や通知を VOICEVOX / Irodori-TTS などで読み上げる mod。
- [katipally/modz](https://github.com/katipally/modz) - Claude Code mods: install with /plugin install &lt;mod&gt; --marketplace…
- [keithwalsh/claude-code-mods](https://github.com/keithwalsh/claude-code-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high。
- [levy-n/claude-code-mods](https://github.com/levy-n/claude-code-mods) - Claude Code mods for long sessions: context-handoff。
- [lifeofgurpreet/g-line](https://github.com/lifeofgurpreet/g-line) - A Claude Code mod: your session at a glance, with a heads-up before you hit a…
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [LouiSvon/claude-code-mods](https://github.com/LouiSvon/claude-code-mods) - Deux mods pour l&#x27;app Claude Code : barre des tâches des agents et ligne d&#x27;état.
- [lperezmo/cache-caffeine](https://github.com/lperezmo/cache-caffeine) - Claude Code mod: keeps the prompt cache warm while you step away, and wakes…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - A community-curated Claude Code Mods guide: use cases, original demos…
- [lukeismith/lukes-claudecode-mods](https://github.com/lukeismith/lukes-claudecode-mods) - A collection of claude code mods I built。
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一个 Claude Code 修改，在 iTerm2 标签页副标题中显示 Claude 正在做什么，让你一眼查看标签栏就能知道哪个会话需要你的关注。
- [MadCrow69/claude-mods](https://github.com/MadCrow69/claude-mods) - Mods para o Claude Code (chat-cost)。
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude。
- [Marceux-Croix/Claudeopticon](https://github.com/Marceux-Croix/Claudeopticon) - A ticket system for Claude Code: your todo as a live ticket board you can hand…
- [matrix-freed/debrief](https://github.com/matrix-freed/debrief) - Claude Code mod: session-metadata AAR recorder (core + adapters + profiles)。
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code 的社区 mods：在 Claude Code 内运行的防护、窗格和命令。市场：modhub。
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace。
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhnhattonthat/claude-finish-notify](https://github.com/minhnhattonthat/claude-finish-notify) - Claude Code mod: popup with Focus-terminal button when Claude finishes (Windows)。
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you。
- [mreedr/gh-linear-parse-mod](https://github.com/mreedr/gh-linear-parse-mod) - Claude Code mod: GitHub PR and Linear links band above the prompt。
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模组：通过在会话开始时设置 CLAUDE_CODE_ENABLE_TODO_TOOLS，为省略待办工具的模型重新启用这些工具.
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 一个 Claude Code 模组：等待安全的暂停时机，然后交接你的会话或将其压缩.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模组：提示词上方每个任务列表任务占一行，显示当前任务、进度条和计数。在终端和桌面应用中外观一致.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 内与 AI 玩 Connect Four（/connect-four）。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模组：当另一个编码代理向你的仓库提交代码时，Claude 会通过差异和测试进行审查，而不是相信它的报告.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 适用于多个 AI 代理共享仓库的 Claude Code 模组：阻止机密值离开 .env、推送到公共远程仓库，以及会清除另一个代理未提交工作的 git 命令.
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph。
- [patle1/claude-mods](https://github.com/patle1/claude-mods) - My Claude Code mods, skill and agents, with an installer for cloud sessions。
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack：一个 Claude Code 模组。在一个面板和状态栏中提供永久工作树、只读起步环境、团队控制盘和上下文库.
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [petrovyuri/claude-code-mods](https://github.com/petrovyuri/claude-code-mods)
- [phatjam98/claude-mods](https://github.com/phatjam98/claude-mods) - Claude Code mods by phatjam98。
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 桌面应用 Code 选项卡的实时会话统计侧边栏：上下文、成本、git 变更、回合统计、子代理、日志.
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [piollosmash-dotcom/claude-mods](https://github.com/piollosmash-dotcom/claude-mods)
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pupuchan1/dopa-ide](https://github.com/pupuchan1/dopa-ide) - Claude Code mod: a dopamine band above the prompt, fireworks and a fanfare when…
- [PurpleDotStudio/claude-mods](https://github.com/PurpleDotStudio/claude-mods) - Claude Code mods: a side panel for what the session needs from you。
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code。
- [r1305/claude-mods](https://github.com/r1305/claude-mods) - Mods para Claude Code: enrutado de modelos con dashboard de consumo y…
- [rakavanagh/savvy-status](https://github.com/rakavanagh/savvy-status) - Claude Code mod: watch your subagents work as a crew of crabs, with live file…
- [ramonfabrega/mods](https://github.com/ramonfabrega/mods) - Claude Code mods: hooks modules that change the interface.
- [RemyLespagnol/sharp-compact](https://github.com/RemyLespagnol/sharp-compact) - Claude Code mod: before every compaction, the session writes its own handoff…
- [RichardJSun/claude-code-mods](https://github.com/RichardJSun/claude-code-mods) - Claude Code mods, published as a plugin marketplace。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 模组：在 Claude 工作时做俯卧撑。无代币.
- [Roberdinho/claude-mods](https://github.com/Roberdinho/claude-mods) - Claude Code mods: prompt-polaroid makes CodeSnap-style Polaroids of your prompts。
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain：Claude Code 模组实地指南，从 ELI5 到策略工程，包含现场测试和引导式教程。
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：将你在 plan mode 中批准的计划变成提示词上方的实时清单，并在 Claude 完成每一步时勾选。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精心挑选的 Claude Code 模组列表。每个条目都经过克隆，并使用 claude plugin validate 检查，同时标注其可操作的内容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：辅助代理运行在 Haiku 上，大文件和日志由免费的 Gemini 模型进行摘要，而不是填满 Claude 的上下文.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 一段伴随会话的 lofi 原声：平静、专注、心流，以及测试通过和失败时的提示音。原创音乐.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 编码时学习：每当一轮操作修改了代码，提示词上方就会出现一个关于该确切修改的问题。按概念评分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 记录 Claude 所做每次编辑的磁带：重放每次自动输入的修改，逐步查看，并将任何文件倒回到任意步骤.
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them。
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - A Claude Code mod: a project dashboard and isometric city map of tasks, agents…
- [serafin-meshy/claude-mods](https://github.com/serafin-meshy/claude-mods) - Claude Code mods for Meshy 3D generation: meshy-tray。
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [shhac/claude-mods](https://github.com/shhac/claude-mods) - Mods for Claude Code。
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker。
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - 自定义 Claude Code mods 市场（cc-mods），包含 vendored Anthropic 示例 mods。
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 用于 Claude Code 的一键 commit messages，带有跳舞的像素艺术 Malenia。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter——一个显示你的 Claude 计划使用量（会话和每周限制、重置倒计时、上下文）的 Claude Code mod，位于提示词正上方.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - tanmen 制作的非官方 Claude Code mods（marketplace：tanmen）。
- [tg-bomze/editable-diff](https://github.com/tg-bomze/editable-diff) - Claude Code mod: editable diff panel for Claude。
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一个用于 Claude Code 的模块，在面板中显示当前会话：每条提示词、Claude 分阶段为其完成的工作、每个子代理及其回答，以及该提示词的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一个 Claude Code plugin marketplace，用于 mods：function-hooks plugins，可在 Claude Code…
- [toml0006/claude-session-stats](https://github.com/toml0006/claude-session-stats) - Claude Code mod: live pane of your session。
- [Tyru5/claude-callout-colors](https://github.com/Tyru5/claude-callout-colors) - Claude Code mod: color decision/summary sections in replies。
- [UlongChaS2/learn-trail-mods](https://github.com/UlongChaS2/learn-trail-mods) - Claude Code mod: 설명의 목차를 패널에 띄우고 항목별 설명을 저장해 /recall 로 다시 본다。
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模块：为长时间运行的任务提供动画进度栏和完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 三个小型 Claude Code 模组：查看子代理何时完成、为 Claude 完成后排队发送消息，以及让你喜爱的技能始终只需点击一次即可使用.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 说“I。
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作区旁边的窗格中向 Claude 提出旁支问题。主对话永远不会看到它。功能类似桌面应用中的 /btw.
- [verdantran/my-claude-mods](https://github.com/verdantran/my-claude-mods) - Small mods that change Claude Code。
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [warstellar/claude-mods](https://github.com/warstellar/claude-mods) - Small mods for the Claude Code desktop app。
- [wildraine/context-gauge](https://github.com/wildraine/context-gauge) - Claude Code mod: context window usage gauge above the prompt。
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac。
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Claude Code mod 모음 (wonr-mods 마켓플레이스)。
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 插件：在提示词正上方显示你的 Claude Pro/Max 使用限制、速度预测、计费周期、以 token 和 $/€…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 适用于 Claude Code 的模组。agent-crew：以实时像素团队的形式查看子代理工作，包括角色、模型、当前工具、进度、代币和时间.
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
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
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公开的 Claude Code 技能和 mods。
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun。
- [amirfish1/claude-command-center](https://github.com/amirfish1/claude-command-center) - One local board for Claude Code, Codex, Cursor and 5 more coding agents.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code 的技能、mods、子代理、钩子、斜杠命令和指南——可由你的代理安装（参见 INSTALL.md）。
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免费的 LLM APIs 和编程代理——自动更新，每周通过探测验证两次。免费层级、无需银行卡的试用、免费模型.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 在你的终端、你的 Claude Code 和 Cursor CLI 状态行以及 MCP 客户端中，提供你关注的赛事。
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 将你的编程代理变成键盘固件专家的 Agent Skill。审计 ZMK/QMK 键位映射，调整 home row mods，使轨迹球具备层感知能力，使用 CI…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供礼拜时间、回历日期、adhkar、每日经文、圣行斋戒、Ramadan、Jumu。
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - 适用于 .NET DDD/Clean Architecture 的便携式 Claude Code 工具包：严格的 TDD…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 便携式 Claude Code 全局配置：自定义技能、PreToolUse hooks 和自定义状态行。可在 Linux、macOS、WSL 上运行.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：技能和 mods，经过整理，可在任何人的机器上运行.
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - 带拖放编辑器的可自定义 Claude Code 状态行。
- [MindLab-Research/dsh-generative-ui](https://github.com/MindLab-Research/dsh-generative-ui) - Generative UI for DeepSeek Harness — the agent writes TSX and the web UI…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - 面向你的 Claude Code agents 的可视化看板：将 sessions、subagents 和 background agents…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code 插件和技能市场，用于促进对游戏 Hytale 的 mods 开发。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - 适用于 Claude Code 的分屏查看器，可在 Windows Terminal 和 tmux 中使用：以渲染后的 Markdown…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - 用于Claude Code Awesome Media mods 的仓库.
- [dayfinggg/anthropic-claude-code-agent-skills](https://github.com/dayfinggg/anthropic-claude-code-agent-skills) - 18 engineering skills, 14 specialist agents, the Brief output style, two mods…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [michalschroeder/claude-statusline](https://github.com/michalschroeder/claude-statusline) - My Claude Code statusline + supporting hooks。
- [RaggioS/claude-code-statusline](https://github.com/RaggioS/claude-code-statusline) - Single-file POSIX statusline for Claude Code: dir, git branch, model, context…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - 适用于 Claude Code 的增强型彩色分级、零依赖状态栏.
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [faleiro-thiago/claude-skills-mods](https://github.com/faleiro-thiago/claude-skills-mods) - Facilitadores pessoais para Claude Code, versionados por item。
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens。
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [pkkid/claude-aitools](https://github.com/pkkid/claude-aitools) - Various mods and skills for my Claude Desktop setup。
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン。
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline。
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [31c0c3/claude-statusline](https://github.com/31c0c3/claude-statusline) - One-line Claude Code status line in bash and jq: context, cache, limits, cost。
- [afarrell/claude-meter](https://github.com/afarrell/claude-meter) - Minimal Claude Code statusline — context bar, 5h bar, and 7-day rolling…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games。
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code plugin marketplace with baloo: skills, an agent that verifies…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 专业级 Claude Code 状态栏：会话时长、结合 ECB 外汇汇率的多币种成本、每 MTok 费率和支出上限。MIT，零密钥、跨平台.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod 的 Claude Code 插件，一个 marketplace：用于 Claude Code 的 agent skills 和实时面板.
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - 用于 Claude Code 的状态栏：上下文、限额和本周进度、代码库的 CI、部署和 PR，以及你的机器。
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust。
- [federbenjamin/claude-statusline](https://github.com/federbenjamin/claude-statusline) - A two-line Claude Code status line showing branch, PR, model, context, cost…
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [hawkymisc/claude-plugins](https://github.com/hawkymisc/claude-plugins) - Hawkie。
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [jamesyoung-dev/claude-cache-countdown](https://github.com/jamesyoung-dev/claude-cache-countdown) - Keeps claude_statusline_plus。
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jdmalter/claude-code-statusline](https://github.com/jdmalter/claude-code-statusline) - A muted three-line status line for Claude Code, in bash for Git Bash on Windows。
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [kouui/magic-claude-code-plugin](https://github.com/kouui/magic-claude-code-plugin) - awesome claude code plugin marketplace: skills, mods, ...
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Talk to Claude Code by voice on Windows: a Mod + helper using codex app-server…
- [LiamMorganDev/claude-setup](https://github.com/LiamMorganDev/claude-setup) - My complete Claude Code setup: mods, skills, commands, hooks and CLAUDE.md…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [Monte9/claude-memory-mods](https://github.com/Monte9/claude-memory-mods) - Curate Claude Code&#x27;s own memory files: a pane to view every project&#x27;s memory…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status。
- [n0nuser/claude-statusline](https://github.com/n0nuser/claude-statusline) - 3-line status bar for Claude Code — model, context usage, cost, git status, and…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 自定义 Claude Code 状态栏（上游：kamranahmedse/claude-statusline）。
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Model risk management guardrails for Claude Code: 25 controls in six mod packs…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company。
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ 适用于 Claude Code 的通用多协议 StatusLine、上下文自学习和 Dinotty 插件。
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Vudaperep/Visual-cc-mod-creator](https://github.com/Vudaperep/Visual-cc-mod-creator) - A visual builder for Claude Code panes: pick widgets, see a live terminal…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026——面向 Claude Code 代理的主动式 AI 记忆与速率限制监控器。
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks, subagents and statuslines: open-source collections and…
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 的 mods：基于函数钩子构建的面板、条带和伙伴。
- [ryanclark/statusline](https://github.com/ryanclark/statusline) - Simple status line for Claude Code showing context window/usage limits。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的Claude Code 会话之间传递任务。将更改交给负责某个仓库的会话.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你反复要求Claude Code 做的事情，并将其变成 mod。此外还包括 8 个示例 mods 和一个虚拟办公室.
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 这是一个用于控制 MODS 的MCP服务器。MODS 是面向 Fablabs 的模块化跨平台工具，包含 CAD/CAM 和机器控制工具.
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - 适用于 Claude Code 的 3 个技能库：session-handoff、session-statusline 和…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用于使用本地LLM翻译 CK3 mods 的Codex和Claude Code 技能。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - 用于Claude Code 的开源 mods 和其他扩展。
- [Grandullon/diariovida-mods](https://github.com/Grandullon/diariovida-mods) - Mods gratis para Claude Code: entiende lo que hace Claude, mejora tus prompts y…
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability。
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## DSH 和 Cordis 插件生态系统

DeepSeek Harness 和 Cordis 从不同方向抵达同一目的：对它们而言，插件就是 mod 机制，因此那里的插件相当于这里的 mod。

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250498 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 在代码中发现使用: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `DSH 和 Cordis 插件生态系统`                 |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **250498** |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐75162 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **75162**  |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4639 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

DSH's officially top-recommended TUI plugin — high performance, low overhead, cute pixel whale, smooth mouse interaction. One-command install via npm. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

<sub>🔧 在代码中发现使用: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `DSH 和 Cordis 插件生态系统`                 |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | TypeScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **4639**   |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐716 · Python · 👁️ observed · 0 天</summary>

##### 📝 摘要

为包括 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My Pi、Grok、OpenCodek DSH、Kimi 等在内的 AI 助手精选的优秀 AI 插件列表。https://hol.org/plugins

<sub>🔧 在代码中发现使用: `README.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `DSH 和 Cordis 插件生态系统`                 |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | Python                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **716**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐272286 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **272286** |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101373 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **101373** |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84082 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **84082**  |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35812 · Go · 🔎 inferred · 0 天</summary>

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
| 星标     | **35812**  |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30974 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **30974**  |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25669 · Python · 🔎 inferred · 2 天</summary>

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
| 星标     | **25669**  |
| 最后推送 | 2026-10-13 |
| 首次列入 | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9208 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

时空可组合性元框架

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **9208**   |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8798 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **8798**   |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4272 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **4272**   |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3463 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **3463**   |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3032 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **3032**   |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-15 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1569 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **1569**   |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PC2005-cloud/dsh-pet">PC2005-cloud/dsh-pet</a></b> · ⭐1521 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DSH 桌面宠物：一行命令装好即用的透明动画小桌宠，支持多开、大小位置随心配置；还内置 DIY 素材链，能用 AI 视频自造专属宠物

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1521**   |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `deepseek-harness` · `desktop-pet` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pc2005-cloud--dsh-pet/2b101f3bcf23988f.png" width="100%" alt="PC2005-cloud/dsh-pet screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pc2005-cloud--dsh-pet/9f4b7093fcbfacf4.gif" width="100%" alt="PC2005-cloud/dsh-pet animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1473 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1473**   |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-15 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1205 · Go · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Go                                               |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1205**   |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐706 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **706**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Mars-Sea/dsh-commandcode-provider">Mars-Sea/dsh-commandcode-provider</a></b> · ⭐393 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Command Code provider plugin for DeepSeek Harness (dsh). Adds Command Code model access, live model catalog, plan-aware model selection, reasoning effort, image input, web search, and multi-account support.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **393**    |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `command-code` · `commandcode` · `deepseek-harness` · `dsh` · `dsh-plugin` · `llm` · `llm-provider` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mars-sea--dsh-commandcode-provider/2f2256468a8af0b9.png" width="100%" alt="Mars-Sea/dsh-commandcode-provider screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐301 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Just open your browser — get all your work done.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **301**    |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐274 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **274**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **256**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐191 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness (DSH) 备份与恢复插件 — 导出、导入、迁移和同步完整的 DSH 配置、插件、MCP 服务器、技能和工作区。一键迁移到另一台机器。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **191**    |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/95eb0411c14b8fcd.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐164 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **164**    |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-15 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐163 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **163**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-15 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **120**    |
| 最后推送 | 2026-10-15 |
| 首次列入 | 2026-10-15 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐101 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DSH plugin - framework upgrade safety & plugin gating: contract pre-check, rollback point, auto-rollback on failure, evidence-based auto-disable; plus a multi-source plugin market. Unofficial. | DSH 插件：框架升级安全 + 插件门控——升级前契约预检、回滚点、失败自动回滚、有确证证据才自动禁用；另带多源插件市场。非官方社区项目。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **101**    |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Clarklevis1995/dsh-plugin-mobile-gateway">Clarklevis1995/dsh-plugin-mobile-gateway</a></b> · ⭐78 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

以websocket为通信方式的dsh网关插件，支持在同一网域内移动端的接入，实现移动端的dsh app

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **78**     |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/clarklevis1995--dsh-plugin-mobile-gateway/b7ef26df82cda351.png" width="100%" alt="Clarklevis1995/dsh-plugin-mobile-gateway screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐77 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **77**     |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐70 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **70**     |
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐60 · HTML · 🔎 inferred · 0 天</summary>

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
| 星标     | **60**     |
| 最后推送 | 2026-10-16 |
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
| 最后推送 | 2026-10-16 |
| 首次列入 | 2026-10-16 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 53</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI 编程代理的执行前防护工具。在工具调用运行前，它会阻止破坏性的 Git 和文件系统命令，以及常见的访问敏感文件的尝试.
- [Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) - Curated DeepSeek Harness (DSH) plugins, extensions, tools, skills, clients…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 用于会自我迭代的软件的插件运行时——代理可在其中编写、替换并热加载自己的插件，支持 Rust、TypeScript、Python 和 Go，跨进程和机器运行.
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool。
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 插件精选目录 — 14 类 280+ 个社区插件，覆盖 MCP / Skill / TUI / 多 Agent…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH 插件：在 Windows 上为所有代理模式提供 Git Bash shell（替代 pwsh 执行器）。
- [FNOSP/fnos-dsh](https://github.com/FNOSP/fnos-dsh) - DeepSeek Harness应用与harness插件 monorepo。
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站。
- [pearjelly/deep-blend](https://github.com/pearjelly/deep-blend) - Create and refine Blender product scenes in DSH: editable recipes, model…
- [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution plugin for DeepSeek Harness: versioned, auditable…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [Lenonss/DSH_VsCodeMode](https://github.com/Lenonss/DSH_VsCodeMode) - VSCode-style coding for DeepSeek Harness: Monaco editor (tabs/QuickOpen), agent…
- [zhu1090093659/dsh-skins](https://github.com/zhu1090093659/dsh-skins) - Skin center plugin and built-in skins for the DSH Web GUI: skins are pure asset…
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [zhu1090093659/dsh-pet](https://github.com/zhu1090093659/dsh-pet) - Multi-pet companion plugin for the DSH Web GUI: a registry-driven floating pet…
- [a903067276-rgb/dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions) - Clickable file paths in DSH replies: Codex-style inline open, 📂 reveal in file…
- [baosfeng/my-dsh-plugins](https://github.com/baosfeng/my-dsh-plugins) - DSH（DeepSeek Harness）插件与技能集合仓库：插件独立版本、GitHub Release 发布（插件与技能清单见仓库 README）。
- [earthwalker17/MiniDSH](https://github.com/earthwalker17/MiniDSH) - Minimal surface, complete architecture: a small, local-first coding-agent…
- [yuezengwu/dsh-explain](https://github.com/yuezengwu/dsh-explain) - Private, local-first continuous learning for DeepSeek Harness: capture, review…
- [bloodtmai-cmyk/dsh-ai-hub](https://github.com/bloodtmai-cmyk/dsh-ai-hub) - 面向企业内部 Harness 工作台的轻量控制面。
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 插件的 X 射线：声明的能力与实际行为。注册表 + 静态扫描器 + 徽章.
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) - J-Space Cognition Suite SV1 原生 DeepSeek Harness 智能体预设与独立 Cordis…
- [Mars-Sea/dsh-deeppilot](https://github.com/Mars-Sea/dsh-deeppilot) - Native iPhone companion plugin for DeepSeek Harness — sessions, approvals…
- [yu502950715yang/dsh-use-wallpaper](https://github.com/yu502950715yang/dsh-use-wallpaper) - 把 Wallpaper Engine 动态壁纸搬进 DeepSeek Harness 的 Web GUI：浏览器内实时渲染 scene 壁纸。
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - 看清 AI 编码智能体的每一次可观察行动。 · Trace your agents, down to every tool and MCP.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Zero-dependency verification standard for DeepSeek Harness (dsh) plugins…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness 插件生态：一个由 101 个仓库组成的系列中的 86 个开源插件，其中 100 个由 PerryLink…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode——让 OpenCode Zen + Go 免费层模型持续工作的 DSH…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — 面向 DeepSeek Harness 的第三方插件市场和受保护的生命周期管理器.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人为本的可拓展桌面工作台：对话、笔记、表格、文件在同一工作台；自建服务端即可开启多人实时协作.
- [DoveLi-Gu/dsh-showcase](https://github.com/DoveLi-Gu/dsh-showcase) - Local, verifiable delivery evidence reports and DSH plugin for coding-agent…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入。
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色插件：三套服装、任务表情、三口白饭、摸头鼓脸、铁盆帽与手写问候.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成。
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 插件：将 Windows 沙盒 ACL 配置失败。
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [zhang-guo-wen/dsh-claude-compat](https://github.com/zhang-guo-wen/dsh-claude-compat) - deepseek harness 插件，兼容claude的skill、rules加载规则，mcp配置。
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [q253595422/dsh-imagegen-video](https://github.com/q253595422/dsh-imagegen-video) - DeepSeek Harness plugin: image + video generation studio with an infinite…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步。

</details>

<a id="writing"></a>

## 文章、讨论与视频

关于模组功能的文章、讨论和视频。

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 0 天</summary>

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
| 首次列入 | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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

| 语言       | 条目 | 示例                                                                                                          |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 382  | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 70   | `songoao25/dsh-chatgpt-sub`, `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`                        |
| Python     | 42   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 32   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 16   | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 9    | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 3    | `vulcanshen/ccdrawu`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                         |
| PowerShell | 2    | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| AutoHotkey | 1    | `keithwalsh/claude-code-mods`                                                                                 |
| C          | 1    | `reporails/arcade`                                                                                            |
| CSS        | 1    | `zhu1090093659/dsh-skins`                                                                                     |
| Java       | 1    | `bloodtmai-cmyk/dsh-ai-hub`                                                                                   |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |
| Swift      | 1    | `eovidiu/cordis-ios`                                                                                          |
| jq         | 1    | `n0nuser/claude-statusline`                                                                                   |

<sub>仅统计声明了语言的条目。文档和讨论条目不包含在此表中。</sub>

## 参与贡献

欢迎提交更正，这是改进此列表最快的方式。如果某个条目归类错误、等级错误，或者某个项目因名称冲突而被错误排除，请提交 issue 或 pull request——最后这一类是自动筛选最容易出错的地方。

---

<sub>独立社区项目。与 Anthropic 没有关联，也未获其认可或审查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商标。产品行为可能随时变化；对于任何关键依赖，请以官方文档为准进行验证。相关资产仍归其上游项目所有，仅在许可证允许的情况下转载。</sub>

<sub>最后更新 · 2026-10-16T10:23:36+08:00</sub>
