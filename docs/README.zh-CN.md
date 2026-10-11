<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="精选 Claude Mods">
</p>

<h1 align="center">精选 Claude Mods</h1>

<p align="center"><b>Claude Code mod、插件及其所改变的更深层行为的循证分级索引。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-591-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <b>简体中文</b> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **实时索引** · 上次同步: `2026-10-12T06:04:10+08:00` (UTC+8)
> · 条目: **591** · 最新更新中新增: **0** · 实现语言: **12**

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
<sub>⭐2535 · Python · 👁️ observed</sub>
<sub>找出幽灵令牌。修复它们。在压缩中存活。避免上下文质量衰减。</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74358 · TypeScript · 👁️ observed</sub>
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
- [官方：Anthropic 自有的仓库和发行说明](#官方anthropic-自有的仓库和发行说明) — **14**
- [Mods：使用 mod 能力构建](#mods使用-mod-能力构建) — **460**
- [DSH 和 Cordis 插件生态系统](#dsh-和-cordis-插件生态系统) — **106**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150215 · TypeScript · ✅ official · 0 天</summary>

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
| 星标     | **150215** |
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| 星标     | **8249**   |
| 最后推送 | 2026-10-09 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6346 · Python · ✅ official · 242 天</summary>

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
| 星标     | **6346**   |
| 最后推送 | 2026-02-11 |
| 首次列入 | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| 星标     | **1798**   |
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
<summary><b>此类别中的更多内容</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 为 mods 添加了 `$.ui.notify`：通过你自己的通知设置发出原生通知，并说明发送通知的频道为 mod 的 `Button` 添加了子项：字符串和…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 修复了 `UserPromptSubmit` 钩子或模组的 `prompt.submit` 钩子期间按下 Esc…

</details>

<a id="mods"></a>

## Mods：使用 mod 能力构建

此处的每个条目都展示了使用 Claude Code 在 2.1.287 中获得的能力的证据：通过 `ui.render` 进行绘制，拥有窗格、横条或卡片，读取 `$.ui.selection()`，通过 `agent.spawn` 生成协作者，或明确说明自己是 mod。

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2535 · Python · 👁️ observed · 0 天</summary>

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
| 星标     | **2535**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐497 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

公共 Claude Code 模组的社区目录，从 GitHub 扫描而来，并注明每个模组可以读取、写入、运行或通过网络发送的内容。浏览 https://mods.aidojo.si/

<sub>🔧 在代码中发现使用: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | JavaScript                                   |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **497**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐188 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **188**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐142 · TypeScript · 👁️ observed · 7 天</summary>

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
| 星标     | **142**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐99 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **99**     |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐91 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **91**     |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐78 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **78**     |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐67 · TypeScript · 👁️ observed · 9 天</summary>

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
| 星标     | **67**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 摘要

适用于 Claude Code 的专家技能、代理、命令、规则、钩子和输出样式——会话连续性 + 面向真实开发工作流的现代 CLI 工具

<sub>🔧 在代码中发现使用: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 基本信息

| 字段 | 值                                           |
| ---- | -------------------------------------------- |
| 类别 | `Mods：使用 mod 能力构建`                    |
| 依据 | `其自身文本提到模组 API，或声明支持模组功能` |
| 语言 | Shell                                        |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **59**     |
| 最后推送 | 2026-10-07 |
| 首次列入 | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

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
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
| 最后推送 | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Use Codex, GLM, and other coding agents as Claude Code subagents.

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
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
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
<summary>🧩 <b><a href="https://github.com/paulbkim-dev/claude-code-cache-warmer">paulbkim-dev/claude-code-cache-warmer</a></b> · ⭐13 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 摘要

Claude Code mod that keeps the prompt cache warm and shows each refresh's cost and saving

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
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `claude-code` · `claude-code-plugin` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
| 星标     | **11**     |
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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| 星标     | **11**     |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

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
| 星标     | **11**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

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
| 星标     | **11**     |
| 最后推送 | 2026-10-05 |
| 首次列入 | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 3 天</summary>

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
| 最后推送 | 2026-10-08 |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 摘要

输入时将 Markdown 绘制到 Claude Code 的提示框中。即使你还没闭合围栏，围栏代码也会先变成语法高亮卡片。

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
| 最后推送 | 2026-10-03 |
| 首次列入 | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 426</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - 100 多个可与 Claude Code 配合使用的 mods 集合.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 及其构建工具：先使用构建器技能，然后使用 mods。
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 我每天运行的 Claude Code harness，自第一天起就以此名称发布，如今与 ucsandman/Agnostic-AI…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）。
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 四个 Claude Code mods：Cache Keeper、Recording Mode、Goal Meter 和 Collision Guard。
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西。
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods：在 Claude 读取提示词前修正并翻译它们。
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 来自 Nekyia Labs 的 Claude Code mods 和技能，由生活在持久化家园中的 AI 每天构建和使用。
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 为 Claude Code 的终端记录提供桌面应用外观的 mod。
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code 的侧边面板：显示会话运行的子代理、每个子代理正在做什么及其令牌，并可一键查看其对话.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - 关于 Claude Code mods 的有来源引用的 Obsidian 知识库：它们的工作方式、构建方法，以及安装前的检查方法.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - 教会 Claude Code 代理构建 Claude Mods（函数钩子插件）的技能，附带入门示例。
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 社区 Claude mods、插件和技能，可从一个市场安装。
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - 适用于 Claude Code 的 Claude Mods（函数钩子插件）.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods 画廊：经过检查并固定的 Claude Code mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 面向与对话代理协作的人类用户的决策队列 CLI/TUI。代理发布问题，人类从一个收件箱中回答.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf。
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code 的浮动状态卡片——模型、上下文、速率限制、成本、分支——另有一个任何脚本或模组都可以提供进度的 API。
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code 的 Mods：为终端 UI 添加实时窗格和行为的函数钩子插件。
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods：screen-guard 在屏幕共享时遮盖姓名和机密信息；cache-panel 会在提示词缓存即将失效前提醒你.
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - 适用于 Claude Code 的实时 GSD 仪表板：路线图、带分支的代理树、上下文和成本、工作流，以及用于 .planning 的 markdown…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code 扩展。释放 Claude 的全部力量.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod（插件），添加一个带 Activity、Files、Agents、Context 和 MCP…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code 的面板、防护栏和生活质量 mods：上下文、使用量、实时活动、通知、安全规则、提示词教练、命令中心.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 提示词框上方的两个 Claude Code mods：上下文窗口计、5 小时限制、提示词时钟和会话成本。
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - 让 Claude Pro 计划持续更久：用于精确使用量 HUD、更短 shell 输出且不重复读取文件的 Claude Code mods.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - 读取 Claude Code 命名的 markdown 文件，并将其渲染在会话旁边；指向任意代码块即可让 Claude 编辑它.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code 的语音协作者。与由 ElevenLabs conversational AI 驱动的 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods：typing-speed，一款带有每条提示统计信息的实时打字速度计。
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - 用于 Claude Code 的烟花：每次按键、工具调用、提交和绿色测试都会在提示上方升起盲文烟花。一个 Claude Code mod.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 探索Claude Code mods、插件和扩展，浏览动画演示、分类列表和直接源代码链接。由 FindMods.dev 提供支持.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod：在记录中内联绘制 mermaid 图表。
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code 的 Mods 和 skins：为 Claude 的任务提供实时进度条、带匹配 Windows Terminal…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 小型 Claude Code 修改插件（函数钩子插件）：session-switcher 及更多。
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod：在任意终端中将粘贴的图像缩略图显示在提示词上方。
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods：Claude Tools 菜单、Zen 模式、终端主题、工作量和模式控制。
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods：mod-scout（查找你最常使用的 mods）、usage-meter、check-ledger、resume-nudge。
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 用于同时运行多个会话的两个Claude Code mods：提示词上方的上下文卡片和聊天旁边的会话窗格.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr：发现、检查、切换和更新Claude Code mods。
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods：上下文栏、代理面板、PDPA 模糊处理。
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 最佳Claude Code Mods：精选、已验证、已置顶。一次 /plugin marketplace 添加，包含 43 个 mods.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 插件：自动进行 Claude 模型路由。为每条提示词、步骤和子代理选择 Haiku、Sonnet 或 Opus…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code 的六个 mod：动画 Clawd 吉祥物、用量限制和提示词缓存条、发送前消息检查器、快捷回复、待办队列和成本账本.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code 的 mods 市场：代理循环单步调试器、git 账户提示、工作树状态行等.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 六个 Claude Code…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code 的最佳全能模组包：用量限制和上下文 HUD、针对 rm -rf 和 git reset --hard 的带撤销保护、.env…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - 在你的 Claude Code 中播放 YouTube Shorts 💃。
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren 的 Claude 工具包：适用于 Claude Code 的技能、模组和 MCP 服务器。通过插件市场一键安装.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code 修改插件，在两列并排布局中绘制 Edit 和 Write 差异。
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code mod that lets Claude log unfinished work to Docs/todos.md, with a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code 的 mods：Clawd，一个会演示Claude正在做什么的小型像素吉祥物。
- [reporails/arcade](https://github.com/reporails/arcade) - 经典桌面游戏作为Claude Code mods，在Claude工作时于窗格中运行。由 Reporails 制作.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 精选的 Claude Code 模组列表，可作为插件市场安装：主题、窗格、状态栏、肖像.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 按需生成 Claude Code 模组——一种读取你的对话并构建合适模组的技能：计划进度条、文件窗格、上下文仪表、危险命令防护、测试监视器.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - 由沉迷于 harness engineering 的 Rustacean 设计的、极具主见的 Claude Code 插件。
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 让代理保持诚实的Claude Code mods——用于守护范围、验证部署并在提示词上方绘制会话的函数钩子.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - 我收集的Claude Code mods，每个目录一个 mod。
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 适用于 Claude Code 的被动攻击式饮水提醒。零令牌，最大限度的评判.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - 我使用的 Claude Code mods.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph：用于设计和运行代理图的Claude Code mod（软件工厂）。
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - 用于 Claude Code 的 macOS notch 仪表板：用量限制、打开的会话、任务进度、提示缓存倒计时和待办事项——由五个 Claude Code…
- [Danovich/turntype](https://github.com/Danovich/turntype) - 在 Claude 工作期间进行的打字测试。一个 Claude Code mod.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code 的 mod：提示词缓存栏、后续步骤、快捷按钮和更改回放——可从 marketplace 安装。
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code 的 mods：使用插件函数钩子API构建的窗格、命令和钩子。
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - 在巨大工具输出填满 Claude Code 的上下文之前将其截短。保留错误和摘要，完整文本只需一次 Read 即可查看.
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - 在 Claude Code 中一目了然地查看提示词缓存、上下文和计划限制，显示在提示词页脚和提示词上方。
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Cost, tokens and plan limits of your coding agents。
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 一个 Claude Code mod，会在提示上方的条带中绘制你的使用限制和支出.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman 的 Claude Code mods（marketplace herman-mods）。
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods：计划进度条、记录Claude留下的运行中任务的账本，以及工具输出的令牌屏蔽。
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - 查看 Claude Code 在后台运行的内容：子代理、Codex 作业、shell、监视器、cron 作业和工作流.
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs 制作的 Claude Code mods：streams 将会话中交错的工作拆分为带颜色编码的 streams。
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - 关于 Windows 上 Claude Code mod 的首日现场笔记：上下文/配额燃料条、泰语 UI mod、Matrix…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - 我制作并亲自用于我的Claude Code 设置的 mods。
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools：用于调试 Claude Code 工具调用的调试器.
- [olddonkey/cache-refresher](https://github.com/olddonkey/cache-refresher) - Claude Code mod：显示提示缓存何时过期以及过期会造成的代价，并可通过 keep-alive ping 保持缓存温热。
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod：在提示词上方显示实时成本、上下文和计划配额计量器。图标需要 Nerd Font.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - 一个 Claude Code 模组，在消耗使用量窗口前暂存子代理扩展、大上下文提示和重试循环.
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 面向 Claude 的 28 个 Agent…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - 用于 claude 的 code-mods。
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 一个 Claude Code 修改插件，可通过命名配置文件按仓库启用或禁用全局技能、agents、规则和工具.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 插件（模组）：在多个 Claude 账户之间切换，在状态栏中查看使用限制，并在终端窗格中管理代理、工作树、检查点和差异。
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 经过测试、可一键安装的 Claude Code 模组：YOLO 模式防护、实时成本和上下文、窗格、宠物等。另附精选的最佳社区模组列表.
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code 的 mods：基于函数钩子构建的插件。
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - 为你的编码会话提供电影风格的演职员表。一款原生 Claude Mod，不调用模型，也不进行遥测.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca。
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 我制作的一批 claude code mods。
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code 模组。touch-map：以树状图和活动地图查看 Claude 列出、读取、编辑或创建了哪些文件.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - 使用 Claude Code 工作时学习一门外语。
- [20alexl/windvane](https://github.com/20alexl/windvane) - Babysits a long Claude Code session so you don。
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude Code mods，用于从一个控制塔跨多个 repos 运行多个会话。
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - 适用于 Claude Code 的实时成本、令牌和上下文用量侧边栏：在会话中显示每轮成本、缓存命中率、消耗速率和 30 天支出.
- [atharv6f/headway](https://github.com/atharv6f/headway) - 在你的 Claude Code 提示之上显示目标、任务和 agents——无需设置。一个 Claude Code mod.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code 内的网络电台：cliamp 侧栏、迷你播放器、收藏、发现、专注模式，以及用于 Claude 的电台工具。
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - 有趣且实用的 Claude Code mods：提示词上方的像素小生物、带 Agent Dock 的工具菜单、项目框和状态栏。另附 10 分钟构建你自己的指南.
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude 正在火热进行。与你的小队聊天。朋友在线，就在你的 Claude Code 会话旁边。零 token，零泄露给 Claude.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 面向真正工程师的 Claude Code mods。
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code 的终端会话回顾，位于 Claude desktop app 的 Code 标签页中（一个 Claude Code mod）。
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code 的提示词上方的一场太空战，在它工作时进行.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 查看每个 Claude Code 代理在其上下文中有哪些文件，以及每个文件占多少.
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Claude Code mod：显示会话内存、CPU 和运行时间的状态行。
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 保持头脑冷静。为你的 Claude Code 日子准备的温度计：根据磁盘上已有的 transcript，每小时从 0 到 100…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 用于终端和桌面应用的 Claude Code 小型 mods。
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code mods（插件市场）：带有上下文、成本和使用量仪表的实时侧边栏。
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod：用于任务、子代理、工作流运行、目标和工具调用的进度窗格，带有进度条、时间戳和剩余时间估算。
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod：在提示词上方以彩色进度条显示计划速率限制、上下文填充量、会话成本和每项任务的令牌数。
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI 技能 + mod，可在 agent 回复中加入西班牙语单词。
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code 提示词上方的 Alarum 事件：刚刚到达的内容，以及一键将其交给代理.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - 你的 Floatee 待办事项列表显示在 Claude Code 的提示词上方：一键运行、指导并勾选你的 todos.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code 的 Evangelion 风格侧边栏：上下文、配额、活动、PR、硬件、会话和 forge 面板。
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 一个将其重新设计为《疑犯追踪》中的 The Machine 的 Claude Code mod.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：Claude Code 修改版，用于强制执行经验证的子智能体 DAG 工作流，并提供实时 DAG 窗格。
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - 适用于 Claude Code 的开源 mods：面板、状态栏、提示、工具防护和斜杠命令.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 一个 Claude Code 模组：为每个子代理设置一个窗格，显示它们访问的文件，以及会话的用量和费用.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod：会话状态、实时 Spec Kit 进度和使用窗口治理。
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 上下文窗口作为提示上方的一行，按照 Claude Code 绘制其自身仪表的方式绘制.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop 的实时任务 HUD：Claude 工作时显示在提示上方的条带，点击一次即可打开完整仪表板.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - 一个免费的开源 Claude Code 插件。在你执行 /clear 前，Claude 会写下一份可阅读和编辑的简短交接记录，下一次会话将从中继续.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - 将提示词暂存起来供稍后使用，再将其弹回Claude Code 的输入框。即时完成，不调用模型.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod，在 Ghostty 和 kitty 中内联显示图片。
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 一个 Claude Mod，会在转录记录旁的窗格中显示会话的 GitHub 拉取请求：将描述引用到提示框中，查看检查和评审状态。
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code mods：自动交接和进度条。土耳其语，只需几个命令即可安装.
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod：使用本地 Stable Audio 模型（sa3.cpp）根据文本提示词生成音效。无需API，无需Python.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills：文档事实核查器、代码审计器、错误记忆日志、mod 等.
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Claude Code mod that rewrites rough prompts into clear ones before you send…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod：按 Claude 统计今天所有会话中的代码行数——新增、编辑、删除——悬停时按项目排名。
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod：回复中的路径可点击——点击文件夹即可在 Finder 中打开，点击文件名即可打开文件。
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code buddy 插件：提示上方的 ASCII 伙伴，会记住你的规则并标记 Claude 的快捷方式。
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod：由 Jev 引导的模型/effort 路由、逐字上下文压缩和输出裁剪，以实现更便宜的长会话。
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods：Claude Code 的安全层——秘密信息脱敏、不受信任内容通知、MCP 工具投毒防护、a2a 防火墙、SAST…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Claude Code mods 集合.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 插件和 mod：一个 AI 原生 SDLC（意图 → 规格 → 计划 → 构建 → 验证 → 评审），带有通过 hook…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code 修改版合集 | Claude Code 修改版合集.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods：用于日常工作的实时面板和钩子。
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks：一个 Claude Code 模组，可按请求朗读 Claude 的回复和你的提示词，使用本地开源 Kokoro TTS 语音.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Claude 搞砸时就打它——适用于 Claude Code 的减压 mod：卡通屁股、8 个巴掌、9 个屁股、标记、连击和音效.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods：用于实时窗格、成本感知模型路由和安全防护的小型插件。只需一条命令即可从市场安装.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod 与插件：使用量监视器、令牌跟踪器和状态行.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - 一个 Claude Code mod，将小型决策交给廉价的决策模型：路由、技能、注入筛查、/compact-jev。
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod：实时报告 Claude 修改了哪些文件及原因、子代理状态和剩余计划限制。
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - afterever 制作的 Claude Code mods（插件市场）。
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod：根据 TypeSafe Jev 的评判，将每个子代理路由到最便宜的 Claude 模型。
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods：在提示词上方显示会话统计卡片。
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 提示词上方的一只会动的盲文猫。
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code mod：通过子 Claude Code 将便宜的工作路由到 GLM/Kimi，把关键工作保留在你的订阅上。从 Maggy 移植.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code 提示符上方的一只像素猫，会运行一次 OmniDimension 语音代理测试通话。Claude Code 修改.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 一种 Claude Code mod，会选择合适的时机进行压缩，以保持较小的上下文窗口.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - 用于 Claude Code 的 Claude Mods：token-meter。
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider 的 Claude Code 插件市场。
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - 用于Claude Code 的通用 mods：顶部栏、窗格、toast 和钩子。包括 usage-bar：显示在提示词上方的上下文、成本和计划限制.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - 我的私人 Claude Code mods。
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 将你的 Claude 使用限制显示为动画村民生命值卡片，并带有每周节奏警告——一个 Claude Code mod。
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - 面向 S2 team 的 Claude Code mods（the ather marketplace）。
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - 一个 Claude Code mod，让 Claude 使用通俗英语写作，并标记其惯常的写作习惯.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - 在 Claude 工作时进行短时锻炼：每日目标、连续记录、徽章和可选排行榜。一个 Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code 的用量面板：按模型统计花费（今天、本周、本月、全部时间）和周限制预测。终端 LED 滚动条和桌面应用条 + Details 窗格.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - 一个 Claude Code 模组：在提示词上方实时显示上下文窗口细分。极简权限：不访问网络、文件、进程或模型调用.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code 的 Now Playing mod：在提示上方显示 Apple Music 和 Spotify，带封面图、控制和 Up next 窗格。
- [broening/claude-mods](https://github.com/broening/claude-mods) - 适用于 Claude Code 的模组：缓存时钟、Blast Radius、建议、工作列表、Grill。
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 只是给你的 Claude Code 配一只猫头鹰。
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 单行 Claude Code 条带（缓存倒计时、上下文、限制、下一项任务），外加七个社区模组，作为一个插件安装，默认保持安静.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - 原版 Doom 引擎，带 Freedoom，可在 Claude Code 内游玩。Mac Apple Silicon alpha.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 单词词典面板和状态栏插件。
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 一个 Claude Code mod，持续记录对话中的待处理事项，并将其显示在提示词上方的横条中.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - 像 pull request 一样审查 Claude 触及的每个文件，无需离开终端。
- [CTeitzel/cache-band](https://github.com/CTeitzel/cache-band) - Claude Code mod: a band above the prompt with the prompt-cache countdown, cache…
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Claude Mods。
- [danielmertens/Claude-mods](https://github.com/danielmertens/Claude-mods) - Collection of personal Claude mods.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - 一个生活在 Claude Code 内的 Tamagotchi：它会孵化、吃掉 Claude 写的代码、留下 bug，并成长为八种成年形态之一.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [dbroadhurst/claude-mod-goal](https://github.com/dbroadhurst/claude-mod-goal) - 一个用于 Claude Code 的目标面板：整体目标 Claude 正在努力实现什么、为什么，以及进展到什么程度。
- [delexw/codyssey](https://github.com/delexw/codyssey) - Turn every Claude Code session into a little adventure: generative music that…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - 用于解释代理运行的命令的 Claude Code Mod。
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 以函数钩子编写的 Claude Code mods，以及提供它们的市场。dash：单个窗格中的会话仪表板.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - 一个 Claude Code mod：提示词上方的横幅，显示 Claude 新闻以及依赖项的紧急或安全版本发布信息.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code 模组：在 Guard 阻止工具调用后，停止前往同一目标的已识别绕行，并告诉 Claude 询问你。
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code 模组：在一个视图中显示后台任务，从真实输出中读取进度和预计完成时间，并在条带、窗格和 /downrange 中展示，不发起模型请求。
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code 模组：为队友、命名子 Agent 和其他会话的消息提供统一收件箱，并显示未读数量和发送者标签。
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code 模组：解释沙箱拦截原因，并将重复拦截转化为经过审查且可撤销的设置更改。
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code 收藏夹：用于命令和技能的一键图标。
- [Dyarchia/dyarchia](https://github.com/Dyarchia/dyarchia) - Dyarchia：在每个界面上构建和使用 Kanban。桌面端、Web、CLI、TUI、Claude Code mod 和 MCP 共享一个本地状态.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - 嘿，已静音！抛开差异，删掉重复，不再编辑，少花积分。
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods：rewrite-prompt（Ctrl+P 会在发送前重写你的草稿）。
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - 适用于 Pi、Codex 和 Claude Code 的指令、技能、Pi 扩展和 Claude Code mods。
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code mods：delete-guard（确认文件删除）和 octopus-crew（当前模型、顾问模型和子代理模型的像素吉祥物）。
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude Code 修改：在 Desktop 应用和终端中，以提示符上方的条形显示订阅用量（5h / 7d）。
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods：auto-model-detector 将每个提示词路由到合适的模型和工作量级别。
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - 提示上方的并行分支和工作树实时雷达：哪些可以干净合并，哪些存在冲突，哪些是堆叠的，哪些仍在由 Claude 会话处理，以及落地它们的顺序.
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods（function-hook 插件）：上下文横幅、未完成事项、检查点监控、审查关卡、代理开销.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code 修改（函数钩子插件），通过一个市场安装.
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Claude Code plugin marketplace with my mods。
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - 适用于 Claude Code 的德语 Mods：上下文/缓存提示、带指导的未完成事项、状态行。
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey。
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Claude Code mod: a pixel-art squad suggests the right model。
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod：每次回答后提供三个后续步骤，支持任意语言，可选本地语音和侧边助手.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 模组：每个回答花了多长时间、Claude 思考了多久，以及 tok/s，显示在 Claude 桌面应用中回复的正下方.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods：streamer-mode 在共享屏幕时隐藏私密面板、频段和状态行。
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - 用于我的 claude mods。
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code 函数钩子插件（mods）。
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod：等待 5 小时使用限制结束，并替你发送 &quot;continue&quot;。
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - 位于你的 Claude Code 提示词上方的驾驶舱。鸭子会读取仪表.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Claude Code mods（function-hook 插件）：PR 合并后续处理、/clear 交接、后台任务横幅、审查账本、轻量级 TTS。
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - 小型 Claude Code mods：上下文和计划使用量仪表、提示词缓存计量器，以及一个显示待查看事项的面板.
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Claude Code mod：实时显示每个提示词的 token 使用量、模型和子代理。
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（a Claude Code mod）。
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（a Claude Code mod）。
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（a Claude Code mod）。
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（a Claude Code mod）。
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（a Claude Code mod）。
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - 适用于 Claude Code 的小型模组，例如新的斜杠命令和侧边面板.
- [juro-mont/claude-ev-charging](https://github.com/juro-mont/claude-ev-charging) - An EV-charging progress bar and session panel for Claude Code helper agents。
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd 住在你的 Claude Code 提示上方的条带中：演绎会话、显示正在运行的内容、上下文和用量限制，并与你的 CI 构建赛跑。非官方粉丝模组.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code の返答や通知を VOICEVOX / Irodori-TTS などで読み上げる mod。
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - 一个 Claude Mod，用于读取并加入你的 Claude Code 会话之间的对话（/crosstalk）。
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods。PixBar：提示词上方的像素生物，会随你的轮次、上下文、五小时窗口和 git 移动.
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods。
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code mods（usage-meter 等）。
- [koenrohrer/hearth-band](https://github.com/koenrohrer/hearth-band) - Claude Code mod：每个模型旁边都有一个像素生物，位于提示词上方的提示词缓存篝火旁。
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 两个 Claude Code 模组：folio，位于聊天旁的文件窗格；以及 tint，为终端会话重新设置样式并添加状态行.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph：一张实时图表，展示 Claude Code 知道些什么.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - 在等待 Claude Code 的回答时，不要让注意力飘走.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu 的Claude Code mods——一个插件市场（待办事项侧边窗格）。
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - 适用于 Angel（Vremia）项目的 Claude Code Mods。
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - A community-curated Claude Code Mods guide: use cases, original demos…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - 来自 Mod Box 的独立 Claude Code mods，每个都可以单独安装.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - 一个插件中包含十四个 Claude Code mods，每个都可切换，并提供用于管理、配置和导入 mods 的窗口.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - 一个 Claude Code 修改，在 iTerm2 标签页副标题中显示 Claude 正在做什么，让你一眼查看标签栏就能知道哪个会话需要你的关注。
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: answer Claude point by point, right on the text.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 一个 Claude Code 模组，具有可切换的权限配置：安全基线、可开启和关闭的命名配置，其他所有操作仍会询问.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - 适用于 Claude Code 的小型 mods：runner-avatar，一个在提示词上方运行的小头像。
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - 用于跟踪相关工件和引用的 Claude Code mod。
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of what your AI coding agent is aiming for…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - 社区制作的 Claude Code 模组：在 Claude Code 内运行的防护程序、窗格和命令。市场：modhub。
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code 的侧边面板：Claude 编写的文件、终端分栏、带拉取功能的 git 仓库状态、使用量条和新工单——提供 41 种复古配色方案。
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code 的安静侧边窗格：此会话正在做什么、它的计划、代理，以及其他每个会话。
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Code 会话记录中每个提示词和每条回复上方的昏暗时间，按你自己的时钟设置显示。
- [mmedum/spor](https://github.com/mmedum/spor) - 恢复 Claude Code 收起的内容：Claude 读取的文件、运行的命令，以及每一轮执行的操作。
- [mrkshw/cold-cache](https://github.com/mrkshw/cold-cache) - Claude Code mod：当会话的提示词缓存变冷时发出警告，并提供由 Haiku 编写的交接或压缩选项，以替代昂贵的无缓存重新读取.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code 模组：通过在会话开始时设置 CLAUDE_CODE_ENABLE_TODO_TOOLS，为省略待办工具的模型重新启用这些工具.
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 一个 Claude Code 模组：等待安全的暂停时机，然后交接你的会话或将其压缩.
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code 模组：提示词上方每个任务列表任务占一行，显示当前任务、进度条和计数。在终端和桌面应用中外观一致.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - 在 Claude Code 内与 AI 玩 Connect Four（/connect-four）。
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code 模组：当另一个编码代理向你的仓库提交代码时，Claude 会通过差异和测试进行审查，而不是相信它的报告.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 适用于多个 AI 代理共享仓库的 Claude Code 模组：阻止机密值离开 .env、推送到公共远程仓库，以及会清除另一个代理未提交工作的 git 命令.
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - 用一条命令安装并配置我的 Claude Code mods（macOS、Linux、Windows）。
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code mod：当 Claude 等待你的回应时闪烁终端标签页。
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods 市场。
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - 适用于 Claude Code 的有趣免费模组，绝不消耗 token。首先推出：Dungeon Master，一个 D&amp;D DM 屏幕.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code 中的 SQL 防护栏：通过 DB CLI（函数钩子 / Mods），在 Claude 运行 DELETE、没有 WHERE 的…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - 一个适用于 Claude Code 的模组，以 Windows 和 CJK 为优先：在任何终端中预览粘贴的图片和文本，使用 CJK…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods：图像缩略图和状态行。
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - 由 OrbitMap 团队制作的 Claude Code mods。
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 最优秀的 Claude Code Mods，按它们能为你做什么排序。人工检查，每个一行.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - 适用于 Claude Code 的两个 Claude Mods：garde-du-corps。
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 桌面应用 Code 标签页的实时会话统计侧边窗格：上下文、成本、git 更改、回合统计、子代理、日志.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Various mods and skills for my Claude Desktop setup。
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code 模块：safety-guard 会阻止破坏性命令和秘密文件访问；notify-router…
- [ptsnac/claude-session-handoff](https://github.com/ptsnac/claude-session-handoff) - Claude Code mod：会话计时器，以及一键交接到新的上下文窗口。
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code 模组：实时股票行情、/quote 窗格、价格提醒、市场区间，以及模型可调用的报价工具。
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods，作为一个插件市场发布。
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code 模组：提示词上方显示已使用的上下文，并倒计时提示词缓存何时失效。
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code 模组：一个侧边窗格，固定 Claude 绘制的每张图表，并持续维护工作地图。
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code 模组：一个梦境处理流程，合并、重写并清理 Claude 的记忆文件夹，同时支持备份和撤销。
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code 模组：在 Claude 看到模糊提示词之前将其拦截，并建议使用项目自身的术语。
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod：Claude 使用你的机密信息，但无法看到它们.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - 一个让机密信息不出现在会话记录中的 Claude Code mod：每个密钥都会变成 Claude 仍可使用的占位符。
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code 模组：在提示词上方一行显示 SSH 主机、RAM 和 5h/7d 使用限制。
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 模组：在 Claude 工作时做俯卧撑。无代币.
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - paceline 作为 Claude Code mod：在提示词上方用一行显示你的使用限额进度。
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - 适用于 claude code 的模组。
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod：将你在 plan mode 中批准的计划变成提示词上方的实时清单，并在 Claude 完成每一步时勾选。
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 精心挑选的 Claude Code 模组列表。每个条目都经过克隆，并使用 claude plugin validate 检查，同时标注其可操作的内容.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 零成本模式：辅助代理运行在 Haiku 上，大文件和日志由免费的 Gemini 模型进行摘要，而不是填满 Claude 的上下文.
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 一段伴随会话的 lofi 原声：平静、专注、心流，以及测试通过和失败时的提示音。原创音乐.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - 在 Claude 编码时学习：每当一轮操作修改了代码，提示词上方就会出现一个关于该确切修改的问题。按概念评分.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - 记录 Claude 所做每次编辑的磁带：重放每次自动输入的修改，逐步查看，并将任何文件倒回到任意步骤.
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Claude 的插件集合.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis：为 Claude Code 制作的非官方 Avengers 粉丝 mod.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - 用于在提示词上方显示上下文、增长、配额、缓存、原生成本和代理活动，并提供会话详情的 Claude Code mod.
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - 个人 Claude Code mods。
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Claude Code mods，可作为插件市场安装：deviation-kernel 防止设计中被拒绝的假设，cache-meter…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - 无需安装的 Claude Code 面板中的原版 DOOM：引擎在 Mod 内运行，共享软件篇章和 Freedoom 随插件附带。
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Mody Claude Code (function hooks): panel agentów, pasek budżetu, flota sesji。
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - 防止 Claude 的辅助代理（子代理）耗尽你的使用量。限制同时运行的数量及其使用的模型，并实时查看它们的工作情况.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 用于 Claude Code 的一键 commit messages，带有跳舞的像素艺术 Malenia。
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods——marketplace sunkanxx-mods。
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter——一个显示你的 Claude 计划使用量（会话和每周限制、重置倒计时、上下文）的 Claude Code mod，位于提示词正上方.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - 改变 Claude Code 外观和声音的小型模组.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 一个用于 Claude Code 的模块，在面板中显示当前会话：每条提示词、Claude 分阶段为其完成的工作、每个子代理及其回答，以及该提示词的成本.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - 一个 Claude Code plugin marketplace，用于 mods：function-hooks plugins，可在 Claude Code…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - 在朗读 Claude Code 的回复时高亮当前正在朗读的句子。使用本地语音，支持多种语言.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods。
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code mod: your context window as Scrooge McDuck。
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code 模组：在提示符上方一行显示 5h/7d 配额、上下文窗口、提示缓存剩余时间和会话成本，悬停时显示每个子代理的成本。
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 模块：为长时间运行的任务提供动画进度栏和完成摘要。
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 三个小型 Claude Code 模组：查看子代理何时完成、为 Claude 完成后排队发送消息，以及让你喜爱的技能始终只需点击一次即可使用.
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - 在 Claude 读取大尺寸截图前将其缩小，使长会话持续更久，并告知 Claude 缩放比例，以便点击仍能落在正确位置.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - 说“I。
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - 在提示词框上方显示建议的下一条提示词。输入 /auto，可在 10 秒倒计时后让它替你发送第一条建议。默认关闭.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 在工作区旁边的窗格中向 Claude 提出旁支问题。主对话永远不会看到它。功能类似桌面应用中的 /btw.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code pings you in Telegram when a task is done or it waits for…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - 我的 Claude Code 模组。
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - A Claude Code mod: a highlighter pen for replies, a side panel for query…
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - A Claude Code mod: your Godville hero and diary in a sidebar.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - 适用于 Claude Code 的模组：使用限额栏（5 小时/每周）以及任务/待办事项面板.
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 插件：在提示词正上方显示你的 Claude Pro/Max 使用限制、速度预测、计费周期、以 token 和 $/€…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - 适用于 Claude Code 的模组。agent-crew：以实时像素团队的形式查看子代理工作，包括角色、模型、当前工具、进度、代币和时间.
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - 在 Claude 桌面 Code 标签页中，于 Claude 的回复内嵌并显示 LaTeX 数学公式，以及可选的 TikZ 图形.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - 一个适用于 Claude Code 的实时任务面板：构建前制定计划，在侧边面板中跟踪每项任务、状态、时间、子代理和检查.
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 为最出色的智能体精心挑选的顶级资源合集，Claude Code，这款编程伴侣中的公认冠军，来自势不可挡的 Anthropic PBC 团队（无关联）.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 一个显示正在发生什么的 Claude Code 插件——上下文使用情况、活动工具、运行中的代理和待办进度。
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 面向 Claude Code CLI 的美观且高度可自定义状态行，支持 powerline、主题等.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 系统提示词的所有部分、27…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ 条技巧，帮助你充分利用 Claude Code，从基础到高级——包括自定义状态行脚本以及在容器中运行自身的 Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - 适用于 Claude Code 的精美 vim 风格 powerline。
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 在终端窗格中审查你的编程代理生成的差异，并将行级评论发送回 Claude Code、Codex、OpenCode 或 Pi。herdr 插件.
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - herdr 的浏览器和手机客户端：为每个 agent pane 提供聊天和实时终端，并支持通过 SSH 连接远程 PC、接收 Web 推送提醒。
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 适用于 Claude Code 的综合状态栏插件，包含上下文使用量、API 速率限制和成本跟踪。
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - 为 Claude Code 构建 mods：拦截任意请求、修改任意响应、/model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - 适用于 Claude Code 的综合状态栏仪表板——会话信息、配额条、代理跟踪器、MCP 健康状态、消息历史等.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon：跟踪你的 Claude Code 会话的碳足迹。
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - 由 awesomejun 制作的 Claude Code 美观状态栏。
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 公开的 Claude Code 技能和 mods。
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code 的技能、mods、子代理、钩子、斜杠命令和指南——可由你的代理安装（参见 INSTALL.md）。
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 合法免费的 LLM APIs 和编程代理——每周自动更新，并经过两次探测验证。免费层级、无需信用卡的试用、免费模型.
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - DeepSeek Harness Tavern…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - 用于 Claude Code 的快速、零依赖成本计算器和可自定义 statusline。按模型、日期、项目和分支分解。轻量级，单二进制文件，无需运行时.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - 用于 Claude Code 会话的终端状态栏。
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 在你的终端、你的 Claude Code 和 Cursor CLI 状态行以及 MCP 客户端中，提供你关注的赛事。
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - 用于 Claude Code（运行于 Windows 和 macOS）的本地控制平面：在固定端点后方一键切换 LLM 网关，提供 SSE…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 将你的编程代理变成键盘固件专家的 Agent Skill。审计 ZMK/QMK 键位映射，调整 home row mods，使轨迹球具备层感知能力，使用 CI…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - 在 Claude Code 中提供礼拜时间、回历日期、adhkar、每日经文、圣行斋戒、Ramadan、Jumu。
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - 个人 Claude Code 配置，版本控制于 ~/.claude 中 — agents、skills、hooks、settings 和…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - 适用于 Claude Code 的双行真彩色状态栏。
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - 用于 DeepSeek Harness 的浮动高峰/低峰潮汐卡：i18n（en/zh/ru）、本地时间窗口、会话成本.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - 适用于 .NET DDD/Clean Architecture 的便携式 Claude Code 工具包：严格的 TDD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 便携式 Claude Code 全局配置：自定义技能、PreToolUse 钩子和自定义状态栏。运行于 Linux、macOS、WSL.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 我每天使用的 Claude Code 插件：技能和 mods，经过整理，可在任何人的机器上运行.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Claude Code 插件和技能市场，用于促进对游戏 Hytale 的 mods 开发。
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code 的令牌治理：顶级模型负责指挥，执行交给满足要求的最低成本手段。路由内核、由 hook 强制执行的预预算、遥测，以及带计划配额的状态栏.
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - 适用于 Claude Code 的实时工作流阶段状态栏（Plan → Exec → Verify → Done），由模型自动更新。
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - 用于Claude Code Awesome Media mods 的仓库.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code 的简单实用状态栏配置。
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Claude Code 的插件市场：mods、skills、agents、hooks、输出样式和主题，可逐一安装.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - 显示 Claude Code statusline，包含速率限制、当前目录和 Git 分支信息，以提升工作区感知.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - 适用于 Linux、WSL、Windows 和 macOS 的可配置 Claude Code 状态行，包含提示计时、subagent 行和终端配置 UI.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - 适用于 Claude Code 的快速 Rust 状态栏——负载优先、缓存 git、约 10ms 渲染。
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - 适用于 Claude Code 的实时用量仪表板——在 Catppuccin 胶囊式侧边面板中显示上下文细分、缓存命中、速率限制预测、成本和活动.
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code 的状态栏和令牌栏：上下文、5 小时和每周用量及速率标记、活动、git 和成本.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - 显示 Claude Code 的关键状态详情，包括模型、上下文、限制、git 信息和会话时间，适用于 macOS、Linux 和 Windows.
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 多行 Claude Code 状态栏：花费、上下文百分比、git 和活动账户——价格和上下文窗口自动更新.
- [QingqiShi/claude](https://github.com/QingqiShi/claude) - Personal ~/.claude for Claude Code: settings, global CLAUDE.md, hooks, status…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - 包含 claude code 实用信息的状态栏。
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 原生代理团队。尽在掌控。适用于 Claude Code 的严格工作者限制、实时团队可见性和可移植配置.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code 附加组件：标签状态彩色圆点监视器 + 内置 GSD 状态栏。
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr 上可定义的Claude Code 软件工厂：xstate station 图、管理器 mod、rigs、beads 和共享内存。
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - 适用于 macOS 和 Linux 的 Claude Code 使用量状态行，打包为 herdr 安装器插件。显示使用百分比、缓存倒计时、上下文和成本.
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code desktop mod: prompt-cache TTL countdown, hit rate and misses。
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - 适用于 Claude Code 的自定义状态行——显示用量百分比、上下文大小、成本和计时器的上下文栏。
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - 适用于 Claude Code 的简洁信息状态栏——显示项目、git 状态、模型、会话时间、上下文用量和速率限制.
- [aubinhaba/claude-code-payment-skills](https://github.com/aubinhaba/claude-code-payment-skills) - Claude Code plugin: code-review skills for payments, consistency, boundaries…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - 带有 baloo 的 Claude Code 插件市场：技能、一个根据项目决策、指南、检查项、输出样式和状态栏验证更改的代理.
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground。
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 专业级 Claude Code statusline：会话时长、带 ECB FX 的多币种成本、每 MTok 费率、支出上限。MIT、zero-key、跨平台.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - 了解订阅状态的 Claude Code 状态行。
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - A Claude Code plugin: a pane of the live Claude Code and Codex sessions on your…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code 的丰富终端状态栏——Bun + TypeScript，零运行时依赖.
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins。
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - 适用于 Claude Code 的工具、技能和代理——从显示模型、分支、PR、上下文大小、提示词缓存剩余时间和成本的状态行开始.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code 自定义状态栏（模型、effort、上下文、缓存、使用量限额）。
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code 的真实 DeepSeek API 支出：按照 DeepSeek…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - 在 Claude Code 中预览图片：将鼠标悬停在回复下方的标签上即可弹出图片，或使用 /img &lt;path&gt; 在窗格中打开图片.
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - My Claude Code setup: mods, skills and plugins。
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 将 Claude 的待办事项同步到 Fizzy.do，实现团队实时可见；把任务转换为持久卡片，提升协作并轻松跟踪进度.
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I。
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - 使用紧凑型仪表板跟踪 Claude Code 状态，显示上下文、成本、时长、Git 分支、速率限制和实时用量。
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 环境安装器：技能、状态栏、钩子、权限，以及可选的 Obsidian-vault MCP 服务器（--vault_root）.
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status。
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - HUD 风格的 Claude Code 状态栏——网络健康状况、TPS、上下文、配额、成本，全部显示在一行中。
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skills and mods for Claude Code and Cowork — project-tracker, reference-doc…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code。
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Code 的便携式配置（状态栏 + 安装程序）。
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude Code 的小型仪表板：上下文百分比、缓存倒计时、5 小时和每周用量、一键将 Handoff 转到新聊天，以及在 Claude 忙碌时用于修复…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Claude Code 的自定义终端状态栏：模型、目录、Git 状态、上下文用量和速率限制。
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 便携式 Claude Code 配置：CLAUDE.md、settings、状态行、技能。
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code 的实时成本跟踪和会话监控状态栏。
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code 技能（VS Code、Windows）：在聊天中的文件路径下显示图像预览和打开按钮、可点击的本地链接、上下文环以及自定义编辑器按钮。
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Claude Code 状态栏：文件夹、git 分支、模型、上下文窗口使用量和计划使用限额。
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026——面向 Claude Code 代理的主动式 AI 记忆与速率限制监控器。
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks, subagents and statuslines: open-source collections and…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code 状态栏的可视化构建器。在浏览器中设计终端底部的栏，然后粘贴一条命令即可安装.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 显示实时令牌使用量和预计能耗的 Claude Code 状态栏。
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code 的 mods：基于函数钩子构建的面板、条带和伙伴。
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - 适用于 Pi 编程 agent 的 Claude Code 风格 UI 捆绑包——工具渲染、加载指示器、状态栏、主题、设置向导。
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - 在你的Claude Code 会话之间传递任务。将更改交给负责某个仓库的会话.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - 这是一个用于控制 MODS 的MCP服务器。MODS 是面向 Fablabs 的模块化跨平台工具，包含 CAD/CAM 和机器控制工具.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 用于使用本地LLM翻译 CK3 mods 的Codex和Claude Code 技能。
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - 用于Claude Code 的开源 mods 和其他扩展。
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code 状态栏：CCometixLine 美化效果 + Claude HUD 功能。
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker：找出你反复要求Claude Code 做的事情，并将其变成 mod。此外还包括 8 个示例 mods 和一个虚拟办公室.
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Claude Code 的 prompt-bar mod：使用限制、缓存计时器和提醒、模型/工作量选择器、侧边窗格。

</details>

<a id="dsh-cordis"></a>

## DSH 和 Cordis 插件生态系统

DeepSeek Harness 和 Cordis 从不同方向抵达同一目的：对它们而言，插件就是 mod 机制，因此那里的插件相当于这里的 mod。

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74358 · TypeScript · 👁️ observed · 0 天</summary>

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
| 星标     | **74358**  |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐100891 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **100891** |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100557 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **100557** |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82028 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **82028**  |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35768 · Go · 🔎 inferred · 0 天</summary>

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
| 星标     | **35768**  |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25499 · Python · 🔎 inferred · 19 天</summary>

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
| 星标     | **25499**  |
| 最后推送 | 2026-09-22 |
| 首次列入 | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4493 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **4493**   |
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
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

全球首个面向 AI Agents 的虚拟终端

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **3682**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3093 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **3093**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1995 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1995**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1841 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **1841**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1591 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

面向 AI 编程代理的执行前防护工具。在工具调用运行前，它会阻止破坏性的 Git 和文件系统命令，以及常见的访问敏感文件的尝试。支持 Amp Code、Antigravity CLI、Claude Code、Codex、Cursor、DeepSeek Harness、Devin CLI、GitHub Copilot CLI、Grok Build、Hermes Agent、Kimi Code、OpenClaw、OpenCode 和 Pi。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **1591**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1578 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **1578**   |
| 最后推送 | 2026-10-11 |
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
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **1410**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1173 · Go · 🔎 inferred · 0 天</summary>

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
| 星标     | **1173**   |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness (dsh) Windows 桌面客户端——捆绑 Node.js + dsh CLI，一键启动

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **705**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness 桌面应用：用于 DSH Sessions、项目、文件、网页研究、插件和 Office artifacts 的本地 AI 桌面工作区。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **592**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

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
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness 的免费网页搜索提供商——DuckDuckGo 后端，无需 API 密钥

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **369**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **225**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/cocofhu/anime-find">cocofhu/anime-find</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **176**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `anime` · `anime-search` · `bangumi` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `magnet`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cocofhu--anime-find/4e8000425bf8bf5f.jpg" width="100%" alt="cocofhu/anime-find screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **176**    |
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
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

适用于 DeepSeek Harness (dsh) 的延时任务委派：从容规划任务，在非高峰时段无人值守运行，回来查看报告。人工裁决，支持桌面端和网页端。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | TypeScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **172**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

适用于可预览跨预设会话迁移的 DeepSeek Harness 插件。固定模式的交接会保留状态、源模型意图和未解决的图像；原始会话保持不变。

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
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>动画录屏</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐160 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **160**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐143 · Python · 🔎 inferred · 0 天</summary>

##### 📝 摘要

运行时证据，帮助 agents 在应用程序和原生代码、GPU kernels 以及推理栈中跟踪、分析并消除热点。

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | Python                                           |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **143**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐135 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **135**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 基本信息

| 字段 | 值                                               |
| ---- | ------------------------------------------------ |
| 类别 | `DSH 和 Cordis 插件生态系统`                     |
| 依据 | `声明支持模组、插件或钩子，但未具体说明模组接口` |
| 语言 | JavaScript                                       |

##### 📊 数据

| 指标     | 值         |
| -------- | ---------- |
| 星标     | **133**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **133**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>动画录屏</sub></td>
</tr></table>

<sub>由于未声明适合再分发的许可证，该资源通过上游代码仓库的外链引用。</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **113**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐100 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 星标     | **100**    |
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 摘要

StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into questions and spaced review · 把自己的资料变成题目与间隔复习的 DSH 学习插件

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
| 最后推送 | 2026-10-11 |
| 首次列入 | 2026-10-12 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 图片</th><th align="center" width="50%">🎬 视频</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>未发布媒体</sub></td>
</tr></table>

</details>

<details>
<summary><b>此类别中的更多内容</b> <sub>· 72</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - 为包括 Claude Code、OpenAI Codex / ChatGPT、Gemini、Antigravity、Pi / Oh My…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 用于会自我迭代的软件的插件运行时——代理可在其中编写、替换并热加载自己的插件，支持 Rust、TypeScript、Python 和 Go，跨进程和机器运行.
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool。
- [ZASENJC/dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) - 自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - 基于 Deepseek-Harness 核心底座打造的桌面版 Agent.继承底坐全部能力。并补全 IDE 相关功能.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - The living DeepSeek Harness plugin directory — refreshed hourly, compat-tested…
- [1475505/miliastra-beyond-simulator](https://github.com/1475505/miliastra-beyond-simulator) - 千星沙箱模拟器：Lua 驱动的 2D 奇域外置沙箱 ，支持 DeepSeek Harness、Web 和 MCP。
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - 面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体.
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent 是面向 AI 编程 agents 的开源 FDE Harness——进入时，将你的业务判断写入文件。
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 插件精选目录 — 14 类 280+ 个社区插件，覆盖 MCP / Skill / TUI / 多 Agent…
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - 可视化 Agent 编排平台｜基于 DeepSeek Harness，支持 Workflow、Multi-Agent、元编排、MCP 与…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：基于 DeepSeek Harness（DSH）的多平台群聊智能体系统｜A DSH-powered multi-platform…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI 插件集合——任务通知、提供商用量、LAN 代理、MCP 管理器、worktree…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站。
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - 适用于 DeepSeek Harness 的 MCP 服务器管理插件：设置 → MCP 页面，支持 OAuth。
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A commerce negotiation runtime + DeepSeek Harness (dsh) plugin.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - DeepSeek Harness Web 的工具箱面板：MCP 管理器。
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 插件 · 发送栏一键「优化」提示词草稿：五维诊断 + 改写稿 SSE 流式上屏，可替换 / 复制 /…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - 经过验证的 DeepSeek Harness 插件市场和自治注册表。
- [liustack/pptwise](https://github.com/liustack/pptwise) - A real PowerPoint, not HTML. Tell your AI what to cover and pptwise builds an…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - 面向编程代理的本地优先代码知识图谱和上下文 harness。MCP + DeepSeek Harness（dsh）插件.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - 经过垃圾信息过滤的 DeepSeek Harness (dsh) 插件、捆绑包和技能开放数据注册表.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Embedded C/C++ AI engineering plugin — firmware skills。
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow。
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 插件的持续兼容性测试：精确的发布版本、隔离运行器，以及可修复的上游问题.
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive context compaction for local-first agents.
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Guarded context compaction for DeepSeek Harness (dsh): the LLM proposes…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web 和桌面版本，集成 Plugins、Skills 和 Interfaces.
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness 主机插件，将项目文档和长期记忆以纯 Markdown 形式保存在专用的 Obsidian vault 中.
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - 精心整理、以证据为依据的 DeepSeek Harness (DSH) 插件目录：经过验证的可加载扩展、技能，以及考虑权限的安装指南.
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 插件的 X 光检查：声明的能力与实际行为对比。注册表 + 静态扫描器 + 徽章.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）。
- [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) - DeepSeek Harness 的 Mixture of Agents (MoA) 插件，支持 /moa 斜杠命令、文件工作区和 Live Canvas 集成。
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - 可搜索的 DeepSeek Harness 插件注册表，提供精心整理的条目和经 manifest 验证的 GitHub 发现功能.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Zero-dependency verification standard for DeepSeek Harness (dsh) plugins…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) 插件：在设置面板中一键同步 OpenCode Go模型——获取所有服务器模型，探测可用性和视觉能力，并写回…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness 上的 OpenCode——让 OpenCode Zen + Go 免费层模型持续工作的 DSH…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — 面向 DeepSeek Harness 的第三方插件市场和受保护的生命周期管理器.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人为本的可拓展桌面工作台：对话、笔记、表格、文件在同一工作台；自建服务端即可开启多人实时协作.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - 为 DeepSeek Harness 提供开箱即用的编码 Agent — Claude Code 风格的工作流、可选模型、TUI、技能、子…
- [GooDAnDReaDY/dsh-live-canvas](https://github.com/GooDAnDReaDY/dsh-live-canvas) - Interactive Visual Frontend Studio, Retool-Style CRUD Engine, Time-Travel…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - 永久删除已归档的 DeepSeek Harness 会话，以及其磁盘上的历史记录和日志目录.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [tiphareth0/dsh-hardssh](https://github.com/tiphareth0/dsh-hardssh) - 在远程服务器上使用现有 DSH 插件运行工作，可跨任意数量的机器。
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 使一个未归属的空模型尝试可重试，适用于唯一能够判断的那个衔接点（deepseek-harness 讨论 #8321 和 #9352）.
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - 能够自我清理的插件：适用于 iOS 和 macOS 的 cordis 插件框架 Swift 6 移植版.
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness 代理预设：将 Codex 和 Claude Code 作为委派子代理，每个子代理均提供只读和完全访问权限级别.
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - 一个 Rust 插件运行时，配备经 Verus 验证的生命周期内核和 Cordis 兼容适配器.
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity 仪表板：tok/s、DSH 风格的缓存命中率、五小时和每周配额。默认使用英语，可切换中文，Windows 安装可逆.
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider)。
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步。

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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

<a id="projects-by-implementation-language"></a>

## 按实现语言分类的项目

该生态主要集中在 Python 和 TypeScript，但使用其他语言编写的客户端也在不断出现。本表根据条目自身内容生成。

| 语言       | 条目 | 示例                                                                                                          |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 377  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 90   | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 38   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 25   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 17   | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Rust       | 6    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| Go         | 5    | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| PowerShell | 2    | `GoSlowPoke168/claude-statusline`, `YangShen-SWE/dsh-plugin-simple-pet`                                       |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1    | `crafts69guy/claude-statusline.nvim`                                                                          |
| Swift      | 1    | `eovidiu/cordis-ios`                                                                                          |

<sub>仅统计声明了语言的条目。文档和讨论条目不包含在此表中。</sub>

## 参与贡献

欢迎提交更正，这是改进此列表最快的方式。如果某个条目归类错误、等级错误，或者某个项目因名称冲突而被错误排除，请提交 issue 或 pull request——最后这一类是自动筛选最容易出错的地方。

---

<sub>独立社区项目。与 Anthropic 没有关联，也未获其认可或审查。Claude Code、Claude 和 Anthropic 是 Anthropic 的商标。产品行为可能随时变化；对于任何关键依赖，请以官方文档为准进行验证。相关资产仍归其上游项目所有，仅在许可证允许的情况下转载。</sub>

<sub>最后更新 · 2026-10-12T06:04:10+08:00</sub>
