<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Claude Mods">
</p>

<h1 align="center">Awesome Claude Mods</h1>

<p align="center"><b>The evidence-graded index of Claude Code mods, plugins and the deeper behaviour they change.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-593-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><b>English</b> · <a href="docs/README.zh-CN.md">简体中文</a> · <a href="docs/README.zh-TW.md">繁體中文</a> · <a href="docs/README.ja.md">日本語</a> · <a href="docs/README.ko.md">한국어</a> · <a href="docs/README.es.md">Español</a> · <a href="docs/README.fr.md">Français</a> · <a href="docs/README.de.md">Deutsch</a> · <a href="docs/README.pt-BR.md">Português</a> · <a href="docs/README.ru.md">Русский</a> · <a href="docs/README.it.md">Italiano</a> · <a href="docs/README.ar.md">العربية</a> · <a href="docs/README.hi.md">हिन्दी</a> · <a href="docs/README.tr.md">Türkçe</a> · <a href="docs/README.vi.md">Tiếng Việt</a> · <a href="docs/README.th.md">ไทย</a> · <a href="docs/README.id.md">Bahasa Indonesia</a> · <a href="docs/README.pl.md">Polski</a> · <a href="docs/README.nl.md">Nederlands</a> · <a href="docs/README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Live index** · Last sync: `2026-10-13T04:10:27+08:00` (UTC+8)
> · Entries: **593** · Added in the latest update: **0** · Implementation languages: **12**

<sub>Every entry below was collected, filtered and re-checked automatically. Nothing here is a paid placement.</sub>

<a id="featured"></a>

## Picks of the moment

<sub>One entry per category, ranked by evidence grade and stars, recomputed on every update. A ranking, not an endorsement; every pick links through to its full card below. Projects that published a screenshot or a recording are preferred, so the strip stays visual.</sub>

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
<sub>Claude Code mods: plugins built on hooks that add live lines above the prompt, guards, panes and games. Context bar, usage meter, Codex review watch, Markdown…</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74429 · TypeScript · 👁️ observed</sub>
<sub>🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory,…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Contents

- [What a Claude Code mod is](#what-a-claude-code-mod-is)
- [How entries are graded](#how-entries-are-graded)
- [Official: Anthropic's own repositories and release notes](#official-anthropics-own-repositories-and-release-notes) — **16**
- [Mods: built with the mod capability](#mods-built-with-the-mod-capability) — **467**
- [DSH and Cordis plugin ecosystems](#dsh-and-cordis-plugin-ecosystems) — **99**
- [Writing, discussions and videos](#writing-discussions-and-videos) — **11**
- [Projects by implementation language](#projects-by-implementation-language)

## What a Claude Code mod is

Claude Code gained **mods** in 2.1.287: extensions that may change deeper behaviour than a plugin could, and draw their own interface.

A mod can hook `ui.render` to paint a **row, band, pane or card** around the prompt, read the text you last selected with `$.ui.selection()`, spawn teammates with `agent.spawn`, and own a `Client` region. A mod that fails to draw fails alone — `ui.fault` keeps one broken mod from taking down the session.

This list covers mods, the plugin and hook surface they build on, and the DSH and Cordis equivalents. It deliberately does **not** cover the wider Claude Code ecosystem: a prompt pack is not a mod.

## How entries are graded

Most lists in this space assert inclusion. This one says how much was actually verified, then lets you filter accordingly. A grade describes the evidence, not the quality of the project — a well-built mod nobody has written about yet is still `inferred`.

| Grade                                                                            | What it means                                                                                                                                                                                          |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `published by Anthropic itself`                                                  | Published by Anthropic itself, or read directly from the official changelog.                                                                                                                           |
| `its own text names a mod API, or it declares the mod capability`                | Its own text names part of the mod surface — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, a pane, band or card — so the author is describing something they built against the real API. |
| `declared a mod, plugin or hook, but nothing about the mod surface specifically` | It calls itself a mod, plugin or hook, but nothing in its text names the mod surface specifically. Real, but unconfirmed.                                                                              |
| `matched on vocabulary alone`                                                    | Matched on vocabulary alone. Included so the filter is auditable, not because it is believed.                                                                                                          |

<a id="official"></a>

## Official: Anthropic&#x27;s own repositories and release notes

Anthropic's own Claude Code repositories, and the releases that defined the mod surface. Read from the source rather than summarised.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150402 · TypeScript · ✅ official · 1d</summary>

##### 📝 Summary

Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

<sub>🔧 Found used in code: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |
| Language | TypeScript                                                      |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **150402** |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9484 · TypeScript · ✅ official · 3d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |
| Language | TypeScript                                                      |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9484**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8255 · Python · ✅ official · 3d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |
| Language | Python                                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8255**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6351 · Python · ✅ official · 243d</summary>

##### 📝 Summary

An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |
| Language | Python                                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6351**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1800 · Shell · ✅ official · 3d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |
| Language | Shell                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1800**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311d</summary>

##### 📝 Summary

Supplementary materials for Claude Model Cards

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |

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

Added Claude Mods: plugins may now modify deeper behavior Added You should know, a built-in mod where a side agent watches your back and flags things you or Claude might miss. Turn it on with `/plugin enable cc-plugin-you-should-know@builtin` (for first-party sessions with telemetry on)

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Added `$.ui.selection()` for mods: returns the text you last selected in fullscreen mode and, when the selection lies within one transcript row, that row Fixed a mod's button sometimes running a different button's action when pressed on a view drawn before Claude Code restarted Fixed fullscreen sessions exiting with "unrecoverable interface error" when opening the background tasks dialog while a plugin or mod showed rows above the prompt Fixed `claude plugin test` reporting mods as turned off remotely when it had only read an out-of-date saved setting

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Fixed a deny or ask rule on a nested part of a compound shell command not holding over a user-installed mod's approval on managed machines Fixed installed mods not loading in the first session after an upgrade Added `agent.spawn` for teammates, one agent id across plugin hook events, and idle and waiting states in `$.agent.list()` Fixed sessions ending with "unrecoverable interface error" when a value a mod's `ui.render` hook wrote made a row throw while drawn; the engine now draws its own row instead Fixed right-aligned content in a mod's pane or band drawing under the close mark or `\[-\]`, wh

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Added `serverToolUses` to the result of a mod's `turn.step` hook: the tool calls the API ran itself (the advisor), each with its id, name, input, start and end Added `ceiling` to the question and verdict a mod's `tool.check` hook reads, naming the approval an organization requires for a tool Added `ThemeKey` and `Color` types to the plugin hooks typings, so an editor lists the theme colors a mod's drawing can name Added to `claude plugin validate`: each hook a mod registers at a gating site is listed with whether it has a `.catch` (`gatingHooks` under `--json`) Fixed a mod's `turn.step` result

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Added `prompt.autocomplete`, an event a mod hooks to add its own rows to the prompt box's autocomplete list Added prompt caching to `$.model.complete` for mods: `prompt` and `system` take blocks of text, and `cache: true` on a block caches the request up to it Added workflow agents to the `agent.spawn` mod hook, with their run and index, so a mod can refuse them Fixed Write, Edit, NotebookEdit and LSP rows, and single Read, Grep and Glob rows, hiding why a mod denied the call: the row now shows the reason Fixed a mod's `config.set`, `state.set`, `env.set` or `agent.spawn` hook that denies afte

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Added `isDeferred` to `$.tool.register` for mods: `false` lists the tool's schema in the prompt from the start instead of behind tool search Fixed a mod's hooks on `classic.*` events being skipped while the plugin hooks worker restarts, which left settings hooks to answer without them Fixed `claude plugin test` failing for mods that call `$.session.append`; tests can read the appended rows back with the new `mock.session`

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes` |
| Evidence | `published by Anthropic itself`                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

MCP management console for the official DeepSeek Harness MCP client: /mcp command with health diagnostics and pipeline trial calls, a Settings MCP tab with server CRUD (approval-gated writes, automatic backups) and a tool trial console over the official tool pipeline (Apache-2.0, dsh-plugin).

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes`                  |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-ticktick">PerryLink/dsh-ticktick</a></b> · ⭐4 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

TickTick (Dida365) task bridge for DeepSeek Harness: Session-header task panel (list filter, undone/completed views, search, drag reorder), 11 curated agent tools, settings card, over the official TickTick MCP endpoint.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes`                  |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4**      |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dida365` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/aa581021cb97f4dd.png" width="100%" alt="PerryLink/dsh-ticktick screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/44088595da097cb2.gif" width="100%" alt="PerryLink/dsh-ticktick animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary><b>More in this category</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.ui.notify` for mods: raises a native notification through your own…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Fixed Esc or an interrupt during a `UserPromptSubmit` hook or a mod.

</details>

<a id="mods"></a>

## Mods: built with the mod capability

Every entry here shows evidence of using the capability Claude Code gained in 2.1.287: it draws through `ui.render`, owns a pane, band or card, reads `$.ui.selection()`, spawns teammates with `agent.spawn`, or says plainly that it is a mod.

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐527 · JavaScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Community catalogue of public Claude Code mods (function hooks), scanned from GitHub with what each mod can read, write, run or send over the network. Browse https://mods.aidojo.si/

<sub>🔧 Found used in code: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **527**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐208 · TypeScript · 👁️ observed · 1d</summary>

##### 📝 Summary

Claude Code mods: plugins built on hooks that add live lines above the prompt, guards, panes and games. Context bar, usage meter, Codex review watch, Markdown preview, Spotify now playing and more.

<sub>🔧 Found used in code: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **208**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐159 · TypeScript · 👁️ observed · 8d</summary>

##### 📝 Summary

Keep Claude Code’s prompt cache warm during breaks and show the estimated cost before a cold send.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **159**    |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>animated recording · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Open video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐146 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Claude Code shows images and plays videos right in your terminal: screenshots, Playwright recordings, and synced before/after QA. Ghostty & kitty.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **146**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐117 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Skins for Claude Code: tool rows with icons, diff, table and Mermaid chart cards, a usage band and fifteen themes. /skin swaps them live.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **117**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>no media published</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐88 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Colorful, themeable Claude Code replies: tables, code, diagrams, charts and tool rows in 15 themes, with copy buttons. A Claude Code mod.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **88**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 4d</summary>

##### 📝 Summary

A collection of claude code mods

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **78**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐74 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

A Claude Code mod that puts a live agent dashboard in your terminal: context and cost, advisor timeline, every permission check, subagent cards and swimlanes.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6d</summary>

##### 📝 Summary

Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens. 台股／美股看板 + more to come.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | HTML                                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **65**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 5d</summary>

##### 📝 Summary

Expert skills, agents, commands, rules, hooks & output styles for Claude Code — session continuity + modern CLI tooling for real-world dev workflows

<sub>🔧 Found used in code: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | Shell                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **62**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐55 · TypeScript · 👁️ observed · 9d</summary>

##### 📝 Summary

Collection of 100+ mods you can use with Claude Code.

<sub>🔧 Found used in code: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **55**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 4d</summary>

##### 📝 Summary

Claude Code mods: live plan progress bars above the prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **47**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animated recording · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Open video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9d</summary>

##### 📝 Summary

Watch Claude Code fabricate a little cartoon as you work.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **32**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9d</summary>

##### 📝 Summary

A rail of your Claude Code session's prompts: hover to read, click to jump (function hooks / Mods)

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **28**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0d</summary>

##### 📝 Summary

A pixel Pokémon that lives above the prompt in Claude Code

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>animated recording</sub></td>
</tr></table>

<sub>Asset hot-linked from the upstream repository because no redistribution-friendly licence was declared.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐24 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

A glow-up for Claude Code: a live cockpit pane, shareable themes, and a pixel pet that acts out what Claude is doing

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **24**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10d</summary>

##### 📝 Summary

Xcode's build, tests, console and SwiftUI previews inside Claude Code

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8d</summary>

##### 📝 Summary

Claude Code mods: 21 styles and a full set of features you turn on when you need them, for the terminal and the desktop app. · 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10d</summary>

##### 📝 Summary

Ten Claude Code mods, beginner guides, creation prompts, safe demos, and a build-your-own template.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

<sub>Asset hot-linked from the upstream repository because no redistribution-friendly licence was declared.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Claude Code mod: preview pasted images and long pasted text above the prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **19**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐17 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Claude Code mod: Clawd acts out what Claude is doing, above the prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **17**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐15 · JavaScript · 👁️ observed · 7d</summary>

##### 📝 Summary

Two Claude Code mods: Codex computer-use bridge and coordinated Claude sessions. Source, build prompts, setup and tests.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **15**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9d</summary>

##### 📝 Summary

Claude Code mods: usage-band shows your 5h/7d limits, context window and cache hit rate above the prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **13**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5d</summary>

##### 📝 Summary

Claude Code mods that make Claude's questions easier to read and answer (qa-guide).

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **12**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>animated recording · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Open video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1d</summary>

##### 📝 Summary

Claude Code mod: context in tokens, 5-hour and weekly limits vs. the clock, prompt cache countdown, session cost and running agents, in one band above the prompt.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **12**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9d</summary>

##### 📝 Summary

Ten open-source mods for Claude Code: live panes, bands, status lines and tool-call guards. Burn meter, launch codes, session wrapped, boss fight, code pet and more.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **12**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8d</summary>

##### 📝 Summary

Animated pixel art above your Claude Code prompt that reacts while Claude works. Seven scenes, or your own image or GIF. Zero tokens.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **10**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27d</summary>

##### 📝 Summary

Session trackers for Claude Code built as mods: context window, plan quota burn rate, per-turn cost

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-09-15 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>animated recording</sub></td>
</tr></table>

<sub>Asset hot-linked from the upstream repository because no redistribution-friendly licence was declared.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0d</summary>

##### 📝 Summary

A UI around your Claude Code and Codex terminals that your agents build, so the only model in your head is yours.

<sub>🔧 Found used in code: `CLAUDE.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2d</summary>

##### 📝 Summary

KOZMOS — live, visual mods for Claude Code (CLI + desktop): bands above the prompt, sidebars, status ticker, companions, guards and sound.

<sub>🔧 Found used in code: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8d</summary>

##### 📝 Summary

Six Claude Code mods in one plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) with per-mod switches, plus a mods-vs-hooks report.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8d</summary>

##### 📝 Summary

개발동생의 Claude Code mods 모음. 택시 팩: 미터기, 내비, 과속 단속 카메라, 블랙박스

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Watch on youtube.com</a> · playback opens on the host site; GitHub cannot embed it inline</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐8 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Your plan, watching itself. Local desktop roadmap tree that Claude Code and any MCP host keep up to date live. Plain JSON, no cloud.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

<sub>Asset hot-linked from the upstream repository because no redistribution-friendly licence was declared.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐8 · TypeScript · 👁️ observed · 3d</summary>

##### 📝 Summary

Make the Claude Pro plan last longer: Claude Code mods for an exact usage HUD, shorter shell output and no repeat file reads. The mods spend zero tokens.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary><b>More in this category</b> <sub>· 433</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods and the tools to build them: a builder skill, then mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - The Claude Code harness I run every day, published under this name since day…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Four Claude Code mods: Cache Keeper, Recording Mode, Goal Meter, and Collision…
- [HolyGrail/claude-mods](https://github.com/HolyGrail/claude-mods)
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods that fix and translate your prompts before Claude reads them.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods and skills from Nekyia Labs, built and used daily by AIs…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Source-cited Obsidian knowledge base about Claude Code mods: how they work, how…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - A desktop-app look for Claude Code.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - A side pane for Claude Code: the subagents a session runs, what each is doing…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop（Code 分頁）側欄面板：列出你所有 Claude Code session 中未完成與進行中的待辦，依專案分組.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop（Code 分頁）輸入框上方的用量條：5h / 7d 額度、token 用量、花費.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill that teaches Claude Code agents to build Claude Mods.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: Claude Tools menu, Zen mode, terminal themes, effort and mode…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community Claude mods, plugins &amp; skills, installable from one marketplace.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (function-hooks plugins) for Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - The Baselane mods gallery: Claude Code mods, checked and pinned.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - A decision queue CLI/TUI for humans working with conversational agents.
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code mod that draws Edit and Write diffs in two side-by-side columns.
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, painted onto Claude Code.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - A floating status card for Claude Code — model, context, rate limits, cost…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods for Claude Code: function-hook plugins that add live panes and behaviour…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard masks names and secrets while you screen-share;
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Unlock the full power of Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod (plugin) that adds a side pane with Activity, Files, Agents…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, guardrails and quality-of-life mods for Claude Code: context, usage…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Two Claude Code mods above the prompt box: context-window meter, 5-hour limit…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Read the markdown files Claude Code names, rendered beside the session, and…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude.
- [Danovich/turntype](https://github.com/Danovich/turntype) - A typing test for the time while Claude works. A Claude Code mod.
- [gixxy22/hide-diffs](https://github.com/gixxy22/hide-diffs) - Claude Code mod: one-line summaries instead of full diffs, ctrl+q to toggle.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: pasted image thumbnails above the prompt, in any terminal.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Voice coworker for Claude Code. Talk things through with a 3D wolf powered by…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow for Claude Code: a calm checklist above the prompt showing the plan…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, a live typing speedometer with per-prompt stats.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fireworks for Claude Code: every keystroke, tool call, commit and green test…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Discover Claude Code mods, plugins and extensions with animated demos, category…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod: mermaid diagrams drawn inline in the transcript.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Small Claude Code mods (function-hook plugins): session-switcher and more.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six Claude Code mods: plan limits and context above the prompt, an allowlist…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout.
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Two Claude Code mods for running many sessions at once: a context card above…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code mods on demand — a skill that reads your conversation and builds…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: discover, inspect, toggle and update Claude Code mods.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Best Claude Code Mods: hand-picked, validated, pinned.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code plugin: automatic Claude model routing.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Six mods for Claude Code: animated Clawd mascot, usage-limit and prompt-cache…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - An app store for Claude Code mods, inside Claude Code: /mods to browse, search…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - A marketplace of mods for Claude Code: a step debugger for the agent loop, git…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-source mods for Claude Code: panes, status lines, toasts, tool guards and…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - The best all-in-one mod pack for Claude Code: usage limits and context HUD, a…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Play YouTube Shorts in your Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods for Claude Code: Clawd, a tiny pixel mascot who acts out what Claude is…
- [reporails/arcade](https://github.com/reporails/arcade) - Classic desktop games as Claude Code mods, played in a pane while Claude works.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods for claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - A curated list of Claude Code mods, installable as a plugin marketplace…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Two Claude Code mods: cache-keeper and ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code mods that keep an agent honest — function hooks that guard scope…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della prompt cache, prossimi passi, bottoni rapidi e…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - A Claude Code mod that draws your usage limits and spend in the band above the…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Live GitHub PR status, merge readiness, checks, comments and alerts inside…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods: progress bars for plans, a ledger of what Claude left…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - See what Claude Code runs in the background: subagents, Codex jobs, shells…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Day-one field notes on Claude Code mods on Windows: a context/quota fuel bar, a…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: a debugger for Claude Code tool calls.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code mod: live GitHub pull request status.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod: live cost, context &amp; plan-quota meters above the prompt.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin and mod: an AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - A Claude Code mod that turns your global skills, agents, rules and tools on or…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Tested, one-command-install Claude Code mods: guardrails for YOLO mode, live…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - A bunch of claude code mods built by me.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods. touch-map: see which files Claude listed, read, edited or…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Pick up a foreign language while you work with Claude Code.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod that reports which files Claude changed and why, live subagent…
- [0xctx/sysop](https://github.com/0xctx/sysop) - Tell Claude what you want. Get it back built, tested, reviewed by another AI…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Babysits a long Claude Code session so you don.
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - A Claude Code mod that keeps your prompt cache warm while you.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Live cost, token and context usage sidebar for Claude Code: a mod that shows…
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - ayagmar.
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Function-hook mods for Claude Code: a limits telemetry row, multi-select…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code mods for real Engineers.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code&#x27;s terminal session recap, in the Claude desktop app&#x27;s Code tab.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - A Claude Code mod: a pane with the session.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [davekiss/mods](https://github.com/davekiss/mods) - Claude Code mods by Dave Kiss.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - See which files each Claude Code agent has in its context, and how much of each.
- [deejay-hub/sf-headless-band](https://github.com/deejay-hub/sf-headless-band) - A Claude Code mod for Salesforce showing which Orgs are connected.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Small Claude Code mods for the terminal and the desktop app.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI skill + mod that adds Spanish words into agent replies.
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Claude Code mod that saves you prompt-cache re-writes: /keepwarm keeps the…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Your Alarum events above Claude Code.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - A Claude Code mod for capturing thoughts mid-work, triaging them across…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - A Claude Code mod that restyles it as The Machine from Person of Interest.
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Code mod (CC tint mod): color each window by its repository, ring the…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: session status, live Spec Kit progress and usage-window…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - The context window as one row above the prompt, drawn the way Claude Code draws…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - A live task HUD for Claude Code Desktop: a strip above the prompt while Claude…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code plugin (mod) that makes the Claude Code terminal UI look like the…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Don&#x27;t let your attention wander off while waiting for Claude Code&#x27;s answer.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - A free, open-source plugin for Claude Code.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: answer Claude point by point, right on the text.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Claude Code mods for long sessions: sitrep boxes each reply.
- [midudev/better-claude](https://github.com/midudev/better-claude) - A prompt queue for Claude Code, as a mod: /after &lt;task&gt; runs it after the…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated, tested, and every mod ships with the prompt that…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills: a docs fact-checker, a code auditor, a bug-memory log, a…
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - A Claude Code mod that keeps a live casebook of the Evidence rea gives the…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code buddy plugin: an ASCII companion above your prompt that remembers…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods: security layer for Claude Code - secret redaction…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Render LaTeX display math in Claude Code.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods collection | 클로드 코드 모드 모음집.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: an unofficial Avengers fan mod for Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: a Claude Code mod that reads Claude.
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Spank Claude when it messes up — a stress-relief mod for Claude Code: cartoon…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods: small plugins for live panes, cost-aware model routing, and…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, with receipts. A plugin that plans, delegates and proves work is…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod &amp; plugin: usage monitor, token tracker &amp; statusline.
- [yyosifov/prompt-mods](https://github.com/yyosifov/prompt-mods) - Small, finished Claude Code mods for the prompt box.
- [08hida28-bot/usage-meter](https://github.com/08hida28-bot/usage-meter) - Claude Code mod: always-on usage display (context, rate limits, cost).
- [0xgigilau/claude-usage-meters](https://github.com/0xgigilau/claude-usage-meters) - Claude Code mod: progress bars for context, session/week/month usage and…
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Catch the drift of your Claude Code session.
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods: session stat cards above the prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - An animated braille cat above the Claude Code prompt.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - A pixel cat above your Claude Code prompt that runs an OmniDimension voice…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - A Claude Code mod that picks a good moment to compact to keep the context…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods for Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - General-purpose mods for Claude Code: bands, panes, toasts and hooks.
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - A Claude Code mod that picks the model for each subagent before it starts, and…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Short workouts while Claude works: a daily goal, streaks, badges and optional…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - A usage board for Claude Code: spend per model (today, week, month, all time)…
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods: live panes, bands and guards that run inside Claude Code.
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - A Claude Code mod that shows what your subagents are up to: a progress bar…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - A Claude Code mod that shows how long each turn took, in a small stopwatch chip…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now Playing mod for Claude Code: Apple Music and Spotify above the prompt, with…
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - Maintained, audited copies of Claude Code mods (filetree, cache-tax).
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods fuer Claude Code: Cache-Uhr, Blast Radius, Vorschlaege, Arbeitsliste, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Just a owl for your Claude Code.
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - 個人 Claude Code mods.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - The original Doom engine with Freedoom, playable inside Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Small, readable Claude Code mods from the CorporateChittyChat channel.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Keep Claude Code on a plan: stages, approval gates and a file budget enforced…
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Claude Code mods.
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Claude Code mod: a band above the prompt with the prompt-cache countdown, cache…
- [curran-gehring/claude-dot](https://github.com/curran-gehring/claude-dot) - A Claude Code mod that brings OpenAI.
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - My personal Claude Code mods, customised for my own setup.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀 전용 Claude Code mods (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Claude Code mod: see which skills, plugins, subagents and MCP tools your…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Eleven Claude Code mods (function-hook plugins) for a many-parallel-sessions…
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Claude Code mods: an OpenSpec and sub agent board, hand over before compacting…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - A Tamagotchi that lives inside Claude Code: it hatches, eats the code Claude…
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Claude Code mod: PR review state, approvals, checks and conflicts above the…
- [denys-nabatov/claude-usage-bar](https://github.com/denys-nabatov/claude-usage-bar) - Claude Code mod: 5-hour and weekly limit usage board above the prompt, with…
- [DerpcatMusic/claude-context-controls](https://github.com/DerpcatMusic/claude-context-controls) - Claude Code mod: nested context / 5h / weekly rings, compaction threshold and…
- [dgsantana/claude-mods](https://github.com/dgsantana/claude-mods) - Claude Code mods: omp-port.
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - A Claude Code mod: a board of your other sessions above the prompt — who waits…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code mod: after a guard blocks a tool call, it stops recognized detours…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code mod: one inbox for messages from teammates, named subagents and…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code mod: explains sandbox blocks and turns repeated blocks into…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favourites for Claude Code: one-click icons for your commands and skills.
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - A live wave board of your session.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [esinecan/mental-model-mod](https://github.com/esinecan/mental-model-mod) - Claude Code mod: Claude.
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Claude Code Mod for background test progress: JUnit, Karma, pytest and unittest.
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods (function-hook plugins): session-meter and more.
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [fran343/claude-mods](https://github.com/fran343/claude-mods)
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Claude Code mod: freeze a session and resume it later as if nothing happened.
- [g761007/hudcade](https://github.com/g761007/hudcade) - A pixel-art HUD for Claude Code: context, cost, cache, agents and rate limits…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+click copy link on every code block in Claude Code replies.
- [GeekyVenkatTuring/portfolio-ticker](https://github.com/GeekyVenkatTuring/portfolio-ticker) - Claude Code mod: portfolio value and P&amp;L above the prompt, plus /portfolio.
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - A Claude Code mod for the desktop app: click a file reference in a reply and it…
- [h3h/blocks-only](https://github.com/h3h/blocks-only) - Claude Code mod: coding turns end in a validated report of typed blocks, drawn…
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Private marketplace of Claude Code mods.
- [haruki-cl/claude-code-mods](https://github.com/haruki-cl/claude-code-mods) - Claude Code mods: token-weather (context usage and memory pane), run-cat.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code mod: how long each answer took, how long Claude thought, and tok/s…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude mods marketplace.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - A cockpit above your Claude Code prompt. The duck reads the gauges.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - 自动读取你的工程图，然后在 SolidWorks 里建模。Reads your engineering drawings…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - A live board of Claude Code subagents inside VS Code: every conversation.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（a Claude Code mod）.
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（a Claude Code mod）.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（a Claude Code mod）.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（a Claude Code mod）.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（a Claude Code mod）.
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Evidence-gated plan checklist for Claude Code: approved plans become a…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 简体中文汉化（自管版）——自己的翻译表 + patch 工具 + 升级检查.
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph Ayoub.
- [jrojasdeveloper/naruto-buddy](https://github.com/jrojasdeveloper/naruto-buddy) - Claude Code mod: animated pixel-art Naruto above the prompt.
- [jrpferreira2002-jpg/clawd-vibe](https://github.com/jrpferreira2002-jpg/clawd-vibe) - Claude Code mod: Clawd above the prompt, clawd has moods.
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd lives in a band above your Claude Code prompt: acts out the session…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code の返答や通知を VOICEVOX / Irodori-TTS などで読み上げる mod.
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code mod: every Claude Code session in one floating window, with live…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Small Claude Code mods in one plugin marketplace.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code mod: picks the model and reasoning effort of every subagent.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph on what Claude Code knows.
- [kyuskoj/claude-mods](https://github.com/kyuskoj/claude-mods)
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Ten Claude Code mods: an animated pixel pet, Code Wrapped, lo-fi beats, plus a…
- [Loup0007A/claude-mods](https://github.com/Loup0007A/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - A community-curated Claude Code Mods guide: use cases, original demos…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - A Claude Code mod that shows what Claude is doing in the iTerm2 tab subtitle…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Small mods for Claude Code: runner-avatar, a little avatar that runs above your…
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Mods Claude : compteur de tokens (token-meter).
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of what your AI coding agent is aiming for…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code mod: /sessions pane to browse and delete sessions with their…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Side pane for Claude Code: files Claude wrote, terminal splits, git repo status…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Claude Code mod: Codex (ChatGPT subscription) and other non-Anthropic models as…
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Claude Code mod: names the terminal tab Claude runs in.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code mod that switches the todo tools back on for models that leave them…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod that waits for a safe pause, then hands your session over or…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code mod: one line per task list above the prompt with the current task…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Play Connect Four against an AI inside Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code mod: when another coding agent commits to your repo, Claude notices…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Claude Code mod: keeps sessions light — usage line, heads-up and one…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code mod for repos shared by several AI agents: stops secret values…
- [NaokiIshimura/claude-code-mod-prompt-templates](https://github.com/NaokiIshimura/claude-code-mod-prompt-templates) - A Claude Code mod that inserts prompt templates from number-key buttons above…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code mod: one button per delegate-skills implementer.
- [NicoSKOOL/seo-mods](https://github.com/NicoSKOOL/seo-mods) - Claude Code mods for SEO: live DataWise rankings above the prompt, and a guard…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Re-arms Claude Code.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - A guard rail for SQL in Claude Code: asks before Claude runs DELETE, UPDATE…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - A notepad pane for Claude Code, as a mod.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - One mod for Claude Code, Windows and CJK first: pasted-image and text previews…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid: the comb review → plan → fix pipeline, enforced by Claude Code mods.
- [omarnaman/claude-mods](https://github.com/omarnaman/claude-mods)
- [Orfila-antoine/claude-mods](https://github.com/Orfila-antoine/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - The best Claude Code Mods, sorted by what they do for you.
- [pakornkub/session-insight](https://github.com/pakornkub/session-insight) - Claude Code mod: session usage, skills and agents, with an agent diagram.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Deux Claude Mods pour Claude Code : garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Timestamps for Claude Code: the time on every message, reply and tool call…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Track changes for Claude Code: see exactly what Claude changed in your Excel…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: a Claude Code mod. Perm worktrees with a read-only head start, crew…
- [PhilRoli/claude-mods](https://github.com/PhilRoli/claude-mods) - Claude Code mod: pause sessions before your TrainTracker train arrives.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods for Claude Code: function-hook plugins that run inside the session…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod: press-ups to do while Claude works. No tokens.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: a field guide to Claude Code mods, from ELI5 to policy engineering…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - just a list of mods I.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Three dependency-free mods for Claude Code: a responsive statusline, a…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods for claude code.
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - An open-source marketplace for Claude Code mods, with repository skills for…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod: turns the plan you approve in plan mode into a live checklist…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - A hand-picked list of Claude Code mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Cost-free mode: helper agents run on Haiku, and big files and logs are…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - A lofi soundtrack that follows the session: calm, focus, flow, plus cues for…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Learn while Claude codes: after a turn that changed code, one question about…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - A tape of every edit Claude makes: replay each change typing itself in, step…
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - A Claude Code mod: a project dashboard and isometric city map of tasks, agents…
- [serhiichuk/claude-shake](https://github.com/serhiichuk/claude-shake) - Claude Code mod: shrink long sessions by replacing old tool results with…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board and other Claude Code mods by André Servaes.
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Mission control for Claude Code: live subagent fleet, token/cost usage, effort…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Showrin.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Claude Code mod: context and plan limits with burn-rate projection, plus a…
- [skryvets/claude-status-bar-mod](https://github.com/skryvets/claude-status-bar-mod) - Claude Code mod: coloured session info under the prompt - context, model…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Claude Code mod that keeps unattended sessions going through usage limits, API…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - One-click commit messages for Claude Code with a dancing pixel-art Malenia.
- [sunwu51/english-assistant](https://github.com/sunwu51/english-assistant) - Claude Code Mods plugin for contextual Chinese-English translation, spelling…
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Mods for Claude Code. cache-meter: prompt-cache hit rate, context fill and…
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Claude Code mod: see your Cursor / VS Code file and selection above the prompt…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — a Claude Code mod that shows your Claude plan usage.
- [tanmen/claude-usage-bars](https://github.com/tanmen/claude-usage-bars) - Unofficial Claude Code mod: Claude Code Desktop の入力欄の上に context・5h・7d の使用率をバーで出す.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code mod: live crew panel for every subagent.
- [thangnguyen-69/claude-mods](https://github.com/thangnguyen-69/claude-mods) - Claude Code plugin marketplace: Plannotator reviews on the tailnet, and more to…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - A Claude Code mod that shows the current session in a pane: each prompt, the…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - A Claude Code plugin marketplace of mods: function-hooks plugins that draw…
- [tiger3645/claude-tts](https://github.com/tiger3645/claude-tts) - Claude Code mod: read Claude.
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Claude Code mod that writes your Claude usage limits to a file other tools can…
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Claude Code mod: one button under Claude.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Claude Code mods by Toptaab.
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - CC mode which shows which Claude account, organization and plan you are signed…
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code mod: animated progress band and completion summary for long-running…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Three small Claude Code mods: see when your subagents will finish, queue…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Say &quot;I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Ask Claude a side question in a pane next to your work.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code plugin: prompt-cache countdown, cache hit rate, context weather and…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods.
- [webfront/claude-mods](https://github.com/webfront/claude-mods) - Special mods for claude code and code in claude app.
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Claude Code mod: the session&#x27;s own model picks each subagent&#x27;s model and effort.
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter) - This Claude Code mod shows a card above the prompt.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — when context outgrows its shell, shed it into the folder and keep going.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod per Claude Code: segreti oscurati, cose da fare, verifiche e CI, diario…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code plugin: your Claude Pro/Max usage limits with a pace forecast…
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC (Every Mod Claude Code): a curated, tested collection of Claude Code mods.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods for Claude Code. agent-crew: watch your subagents work as a live pixel…
- [zhitongLIU/claude-code-mods](https://github.com/zhitongLIU/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - A hand-picked collection of the finest of resources for the most awesome of…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - A Claude Code plugin that shows what.
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Beautiful highly customizable statusline for Claude Code CLI with powerline…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - All parts of Claude Code.
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI video skill for Claude Code &amp; Codex — cinematic product videos with…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ tips for getting the most out of Claude Code, from basics to advanced…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Review your coding agent.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Comprehensive status line plugin for Claude Code with context usage, API rate…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Build mods for Claude Code: Hook any request, modify any response, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - A comprehensive statusline dashboard for Claude Code — session info, quota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: track the carbon footprint of your Claude Code sessions.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - An aesthetic statusline for Claude Code by awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Public Claude Code skills and mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash commands and guides for Claude Code…
- [sageox/ox](https://github.com/sageox/ox) - The hivemind for AI coding agents — persistent team context recorded once and…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legal free LLM APIs &amp; coding agents — self-updating, probe-verified twice a…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live football(soccer) scores, fixtures and standings for the competition you…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill that turns your coding agent into a keyboard firmware expert.
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) - Voice-first session loop for DeepSeek Harness: a composer microphone button…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Prayer times, Hijri date, adhkar, daily ayah, sunnah fasting, Ramadan, Jumu.
- [PerryLink/dsh-mask](https://github.com/PerryLink/dsh-mask) - PII masking middleware for DeepSeek Harness: anonymize names, phones, emails…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Personal Claude Code configuration versioned inside ~/.claude — agents, skills…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness plugin for research topics…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - Multi-agent orchestration layer for DeepSeek Harness (omd)…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Lightweight Claude Code status line — one ~170-line Bash script, zero…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Portable Claude Code global configuration: custom skills, PreToolUse hooks, and…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code plugins I use every day: skills and mods, cleaned up so they work…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analyze Claude Code token usage and costs from local conversation logs and…
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Beautiful, informative status line for Claude Code.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - A visual board for your Claude Code agents: see sessions, subagents and…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - A customizable status line for Claude Code with a drag-and-drop editor.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace for Claude Code Plugins and Skills to facilitate mods of the game…
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Single-line, color-coded statusline for Claude Code — folder, model, context…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Split-pane viewer for Claude Code in Windows Terminal and tmux: the session as…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - A 3-line micro-dashboard for the Claude Code terminal — model, context burn…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository for Claude Code Awesome Media mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Cut Claude Code &amp; Codex token spend: routes lookups and test runs to cheaper…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - A fast, configurable status line for Claude Code — single static Go binary.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Compact, actively-maintained status line for Claude Code — model, effort, token…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - the friendly, fiddle-with-everything status line for Claude Code — truecolor…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agent teams. Under control. Hard worker limits, live team visibility…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows PowerShell status line for Claude Code: 5-hour and weekly limits with…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Statusline para Claude Code en español: tarea, skills, contexto con semáforo…
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - VS Code extension: Claude Code task progress, ETA and rate-limit quota via…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Claude Code status line for Windows: token totals, API-rate cost, and…
- [gvart/claude-config](https://github.com/gvart/claude-config) - My Claude Code setup: agent-monitor mod, skills, agents and a one-command…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Single-line status bar for Claude Code: model, git, context, tokens, cost…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Preview images inside Claude Code: hover a chip under a reply to pop the…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Claude Code status line: model, 5h/7d quota bars, monthly spend bar, cwd.
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Personal Claude Code configuration: permissions, statusline, MCP servers.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code status line with agent panel rows.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Display a detailed, color-coded status bar for Claude Code showing context, git…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Two-line status bar for a terminal coding agent: directory, git, PR, model…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code statusline hook — tracks token usage and context across sessions…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Claude Code statusline with installer for Linux and Git Bash on Windows.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - home-grown, cage-free claude plugins, skills, mods, and more.
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Marketplace Claude Code de MSF Supply : mods sélectionnés et figés par commit.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Rich multi-line status line for Claude Code — live usage limits (5h + weekly)…
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Multi-line Claude Code status line: context bar, git branch, 9router…
- [Paradigm-Study/claude-share](https://github.com/Paradigm-Study/claude-share) - Shared Claude Code sessions: share a session with a link, teammates join from…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitor Claude Code status from your macOS menu bar with real-time indicators…
- [pkkid/claude-aitools](https://github.com/pkkid/claude-aitools) - Various mods and skills for my Claude Desktop setup.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skills and mods for Claude Code and Cowork — project-tracker, reference-doc…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code status line for Windows (PowerShell): usage bars, 5h/7d reset…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Custom Claude Code statusline (upstream: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Model risk management guardrails for Claude Code: 25 controls in six mod packs…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Starter harness for Claude Code: hooks, statusline, local models, swarm…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Claude Code 用の 4 行ステータスライン（context / rate limit / cost / git / worktree）.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Portable Claude Code config: CLAUDE.md, settings, statusline, skills.
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Universal Multi-Protocol StatusLine, Context Self-Learning &amp; Dinotty Plugin…
- [tylergraydev/cc-mods](https://github.com/tylergraydev/cc-mods) - Mods for Claude Code: side panes, status lines, toasts and tool-call guards as…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Track Claude Code context usage, session costs, and rate limit resets with a…
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - My Claude Code skills, plugins and mods (marketplace: vladdu).
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - 多机同步 Claude Code 用户级配置（settings.json + statusline），GitHub / Gitee 双源.
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - A Claude Code status line: folder, git branch, model, context window usage and…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Proactive AI Memory &amp; Rate-Limit Monitor for Claude…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks, subagents and statuslines: open-source collections and…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code statusline showing real-time token usage and estimated energy…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - A Deno-powered status line for Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods for Claude Code: panes, bands and buddies built on function hooks.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pass tasks between your Claude Code sessions.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - This in a MCP server to control MODS, the modular cross platforms tool for…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex and Claude Code skill for translating CK3 mods with a local LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods and other extensions for Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: find what you ask Claude Code again and again, and turn it into a…

</details>

<a id="dsh-cordis"></a>

## DSH and Cordis plugin ecosystems

DeepSeek Harness and Cordis reach the same place from a different direction: for them the plugin is the mod mechanism, so a plugin there is the equivalent of a mod here.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74429 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

<sub>🔧 Found used in code: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74429**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐149050 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Reverse engineer anything with agents, from app behavior down to native binaries.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **149050** |
| Last push    | 2026-10-12 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100741 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **100741** |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82506 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **82506**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0d</summary>

##### 📝 Summary

A reliable coding agent for complex software engineering tasks.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Go                                                                               |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **35769**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25532 · Python · 🔎 inferred · 0d</summary>

##### 📝 Summary

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25532**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18512 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **18512**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8666 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8666**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6273 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6273**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4459 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DSH's officially top-recommended TUI plugin — high performance, low overhead, cute pixel whale, smooth mouse interaction. One-command install via npm. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4459**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3680 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

The World's First Virtual Terminal for AI Agents

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3680**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3418 · Python · 🔎 inferred · 0d</summary>

##### 📝 Summary

本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3418**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3033 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3033**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1911 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1911**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1422 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

AI 小说创作软件：把灵感、角色、世界观、大纲、章节写作、审稿和修稿组织成可控流程；提供 Windows/macOS 桌面版，支持本地和在线模型。AI Novel Writing Software: Organizes inspirations, characters, worldbuilding, outlines, chapter drafting, review, and revision into a controllable workflow. Features desktop apps for Windows/macOS, Ollama integration, and a DeepSeek Harness (DSH) plugin preview.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1422**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1181 · Go · 🔎 inferred · 0d</summary>

##### 📝 Summary

Memory for Claude Code, Codex, Cursor and 38 more coding agents, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Go                                                                               |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1181**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐261 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **261**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **255**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-research-report">PerryLink/dsh-research-report</a></b> · ⭐214 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Verifiable research-report engine for DeepSeek Harness: content-addressed evidence ledger (claim-snapshot binding, tamper-evident) plus versioned sealed reports with per-claim verification verdicts and a manifest-sealed directory.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **214**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `audit` · `citation-verification` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/2a270ca82dba24d3.png" width="100%" alt="PerryLink/dsh-research-report screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/dafefe1b3e0cd96e.gif" width="100%" alt="PerryLink/dsh-research-report animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

面向 DeepSeek Harness 的 Claude Code 风格终端界面，支持 Windows、macOS 与 Linux，兼容透明终端、VS Code 主题和自定义配色。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **197**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐194 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **194**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **165**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐144 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **144**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animated recording</sub></td>
</tr></table>

<sub>Asset hot-linked from the upstream repository because no redistribution-friendly licence was declared.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-memento">PerryLink/dsh-memento</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Bounded, layered, approval-gated, auditable cross-session memory for DeepSeek Harness: a ctx.memory capability seam with a zero-dependency SQLite provider, a memory tool, and frozen snapshot injection. Maintenance status: FROZEN since 2026-10-05.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **141**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `agent-memory` · `ai-agent` · `ai-agents` · `approval` · `audit` · `cordis` · `deepseek-harness` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/f63bd5eb5a8052b8.png" width="100%" alt="PerryLink/dsh-memento screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/0ce3328d348abdce.gif" width="100%" alt="PerryLink/dsh-memento animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐140 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **140**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xcisxc29/dsh-wechat">xcisxc29/dsh-wechat</a></b> · ⭐137 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

WeChat channel for DeepSeek Harness

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **137**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `automation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `remote-control` · `wechat` · `wechat-bot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xcisxc29--dsh-wechat/689ef8e1483bcfd7.png" width="100%" alt="xcisxc29/dsh-wechat screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-permission-rules">PerryLink/dsh-permission-rules</a></b> · ⭐122 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Claude Code-style declarative permission rules for DeepSeek Harness: ordered allow/deny/ask rules with tool-name, argument (glob/regex), and workspace-path matching on the tools/pre-execute waterfall, session-log audit, and HMR reload.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **122**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `ai-safety` · `allow-deny-ask` · `approval` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/d950618f5f9cf382.png" width="100%" alt="PerryLink/dsh-permission-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/25c9ccd2f2133850.gif" width="100%" alt="PerryLink/dsh-permission-rules animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **90**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

<sub>Asset hot-linked from the upstream repository because no redistribution-friendly licence was declared.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

基于 Deepseek-Harness 核心底座打造的桌面版 Agent.继承底坐全部能力。并补全 IDE 相关功能。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **69**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and validate the DeepSeek-Harness community plugin marketplace.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **69**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-fund-research">PerryLink/dsh-fund-research</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Deterministic research reports for Chinese public mutual funds, as a DeepSeek Harness plugin: one fund code in, a versioned Markdown report out, with performance decomposition, holdings penetration, style attribution and explicit data-gap declarations. Metrics are computed in code, not by the model.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **68**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `finance` · `fund-research`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/9a258f42b5375ed7.png" width="100%" alt="PerryLink/dsh-fund-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/c127c0b5eda50892.gif" width="100%" alt="PerryLink/dsh-fund-research animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐60 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **60**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0d</summary>

##### 📝 Summary

The living DeepSeek Harness plugin directory — refreshed hourly, compat-tested daily, with an in-app plugin store and scaffolder. DSH 插件活目录：每小时刷新，每日兼容实测，内置插件商店与脚手架。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | HTML                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **59**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体。纯本地、零模型调用、零网络。  Task-aware workspace context retrieval and lifecycle tracking for AI coding agents. Find, organize, and track the workspace context most relevant to the task at hand — locally, deterministically, zero model calls, zero network.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **54**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary><b>More in this category</b> <sub>· 65</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - A pre-execution guard for AI coding agents.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - A curated list of the best awesome AI plugins for AI assistants including…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub…
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - 图形学与3DGS、空间智能持续更新论文；AI Agent Skills for 3D Gaussian Splatting, NeRF &amp; Computer…
- [arcships/rutis](https://github.com/arcships/rutis) - A plugin runtime for software that iterates on itself — the substrate where…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana: DeepSeek Harness as a subagent for HanaAgent.
- [GDWhisper/dsh-web-startup-auth](https://github.com/GDWhisper/dsh-web-startup-auth) - DSH（DeepSeek Harness）远程 Web 启动 + 用户名/密码认证插件.
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - DeepSeek Harness plugin: deterministic data profiling, cleaning, and…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 插件精选目录 — 14 类 280+ 个社区插件，覆盖 MCP / Skill / TUI / 多 Agent…
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - DeepSeek Harness (dsh) plugin development knowledge base: the 10-chapter…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：基于 DeepSeek Harness（DSH）的多平台群聊智能体系统｜A DSH-powered multi-platform…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin: Git Bash shell for all agent modes on Windows.
- [YRN-playmaker/dsh-wallpaper_share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - 一键同步壁纸引擎各类动态场景壁纸的插件，设置应用启动项。A &quot;wallpaper engine&quot; synchronization plugin mounted…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web plugin: per-day token usage statistics with a GitHub-style activity…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站.
- [liustack/pptwise](https://github.com/liustack/pptwise) - A real PowerPoint, not HTML. Tell your AI what to cover and pptwise builds an…
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - Cross-device DeepSeek Harness session sync: a dedicated git mirror with…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - DSH web plugin: a hierarchical workspace tree for the sidebar — titles…
- [ddtcorex/govard](https://github.com/ddtcorex/govard) - Go-based local development orchestrator for Magento, Laravel, Symfony, Next.js…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) - Vendor parameter translation and deterministic JSON repair for DeepSeek…
- [PerryLink/dsh-observe](https://github.com/PerryLink/dsh-observe) - OpenTelemetry and Langfuse observability exporter for DeepSeek Harness…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - A bilingual, continuously maintained directory of plugins for DeepSeek Harness…
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - Multi-dimensional quality scoring for DeepSeek Harness plugins: scores a repo…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · DeepSeek Harness 功能坞插件：一张面板统一注册/开关所有小功能——用量记账（自定义单价·分时价）、模型设置与余额、19…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Always-on compatibility testing for DeepSeek Harness plugins: exact releases…
- [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) - Native ClineBot / ClinePass provider companion plugin for DeepSeek Harness (DSH).
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness host plugin that keeps project documents and long-term memory…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray for DeepSeek Harness plugins: declared capabilities vs actual behavior.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Podman-backed execution for DeepSeek Harness (dsh).
- [kelemiao/dsh-animation-optimization](https://github.com/kelemiao/dsh-animation-optimization) - DSH 动画优化：输出流式动画与 Claude Code 风格外观插件.
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - Local-first voice conversations for DSH.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC 模式基础上的创造模式:DSH 插件,合成 Code Mode 工具编排 + 自引用 Cordis 工具与 preset 创作指导,物化为…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Page capability kit for DeepSeek Harness (dsh): terminal dock, file tree…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Zero-dependency verification standard for DeepSeek Harness (dsh) plugins…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness plugin ecosystem: 86 open-source plugins in a 101-repo family…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode on DeepSeek Harness — DSH plugin that keeps OpenCode Zen + Go…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — third-party plugin marketplace and guarded lifecycle manager for…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人为本的可拓展桌面工作台：对话、笔记、表格、文件在同一工作台；自建服务端即可开启多人实时协作.
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Run DeepSeek Harness on desktop with zero token costs—a free, open-source GUI…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Bots workbench: Cordis plugin bridging the sdk-bots orchestration gateway…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Hermes-inspired agent self-evolution plugin family, purpose-built for DeepSeek…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Independent third-party plugins and tools for DeepSeek Harness, maintained by…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Use OpenCode Zen free models in DeepSeek Harness with anonymous access or an…
- [yangzhe1991/dsh-web-enhance](https://github.com/yangzhe1991/dsh-web-enhance) - DSH Web UI 增强插件:思维链默认展开、官方 API 会话价格统计、文件用系统程序打开、跑完提醒 | DSH (DeepSeek Harness)…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness plugin: turns the Windows sandbox ACL provisioning failure…
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Deployment-level deadlines for dsh tool calls that declare none: mounted on the…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - A Rust plugin runtime with a Verus-verified lifecycle kernel and Cordis…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Cordis / DeepSeek Harness plugin — normalized GitHub API tools for AI agents…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Writing, discussions and videos

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9d</summary>

##### 📝 Summary

Hi HN, I built this for myself and wanted to open-source it. The problem: I wanted a way to get reminders in-between prompts as I often spend long hours in the terminal, especially now that we&#x27;re usually parallel-processing so many agents. The first version was a simple rep

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10d</summary>

##### 📝 Summary

I built this because with latest coding models, Claude goes into deep-work mode with obscure commands so that I never know anymore what it&#x27;s up to. This is a mod (a plugin using Claude Code&#x27;s new function hooks) that draws one line above the prompt: - the current step,

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Writing, discussions and videos`                                 |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Projects by implementation language

The ecosystem is concentrated in Python and TypeScript, but typed clients keep appearing in other languages. This table is generated from the entries themselves.

| Language   | Entries | Examples                                                                                                         |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| TypeScript | 384     | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                             |
| JavaScript | 79      | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                   |
| Python     | 39      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `AgriciDaniel/claude-mods-brain` |
| Shell      | 28      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`              |
| HTML       | 14      | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                        |
| Go         | 5       | `sageox/ox`, `mitre/claude-statusline`, `esengine/DeepSeek-Reasonix`                                             |
| Rust       | 5       | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                                  |
| PowerShell | 3       | `Gabriel-Dalton/claude-statusline-tokens`, `markallisongit/claude-statusline`, `rainyfei/claude-statusline-win`  |
| C          | 2       | `reporails/arcade`, `tylergraydev/cc-mods`                                                                       |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                          |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                             |
| Swift      | 1       | `peaceinitiativemenhadenoil263/claude-status-bar`                                                                |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Last updated · 2026-10-13T04:10:27+08:00</sub>
