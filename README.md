<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Claude Mods">
</p>

<h1 align="center">Awesome Claude Mods</h1>

<p align="center"><b>The evidence-graded index of Claude Code mods, plugins and the deeper behaviour they change.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-596-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><b>English</b> · <a href="docs/README.zh-CN.md">简体中文</a> · <a href="docs/README.zh-TW.md">繁體中文</a> · <a href="docs/README.ja.md">日本語</a> · <a href="docs/README.ko.md">한국어</a> · <a href="docs/README.es.md">Español</a> · <a href="docs/README.fr.md">Français</a> · <a href="docs/README.de.md">Deutsch</a> · <a href="docs/README.pt-BR.md">Português</a> · <a href="docs/README.ru.md">Русский</a> · <a href="docs/README.it.md">Italiano</a> · <a href="docs/README.ar.md">العربية</a> · <a href="docs/README.hi.md">हिन्दी</a> · <a href="docs/README.tr.md">Türkçe</a> · <a href="docs/README.vi.md">Tiếng Việt</a> · <a href="docs/README.th.md">ไทย</a> · <a href="docs/README.id.md">Bahasa Indonesia</a> · <a href="docs/README.pl.md">Polski</a> · <a href="docs/README.nl.md">Nederlands</a> · <a href="docs/README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Live index** · Last sync: `2026-10-12T21:29:43+08:00` (UTC+8)
> · Entries: **596** · Added in the latest update: **0** · Implementation languages: **13**

<sub>Every entry below was collected, filtered and re-checked automatically. Nothing here is a paid placement.</sub>

<a id="featured"></a>

## Picks of the moment

<sub>One entry per category, ranked by evidence grade and stars, recomputed on every update. A ranking, not an endorsement; every pick links through to its full card below. Projects that published a screenshot or a recording are preferred, so the strip stays visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9482 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2541 · Python · 👁️ observed</sub>
<sub>Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74398 · TypeScript · 👁️ observed</sub>
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
- [Mods: built with the mod capability](#mods-built-with-the-mod-capability) — **482**
- [DSH and Cordis plugin ecosystems](#dsh-and-cordis-plugin-ecosystems) — **86**
- [Writing, discussions and videos](#writing-discussions-and-videos) — **11**
- [Other projects](#other-projects) — **1**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150341 · TypeScript · ✅ official · 0d</summary>

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
| Stars        | **150341** |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9482 · TypeScript · ✅ official · 2d</summary>

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
| Stars        | **9482**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8253 · Python · ✅ official · 2d</summary>

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
| Stars        | **8253**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242d</summary>

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
| Stars        | **6347**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 2d</summary>

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
| Stars        | **1799**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310d</summary>

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Official Claude Code mods by See Stack: live context window HUD, voice narration deck, and terminal tools. Install via: npx seestack

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Official: Anthropic&#x27;s own repositories and release notes`   |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **0**      |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary><b>More in this category</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.ui.notify` for mods: raises a native notification through your own…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Fixed Esc or an interrupt during a `UserPromptSubmit` hook or a mod.
- [huaweicloud/huaweicloud-devkit](https://github.com/huaweicloud/huaweicloud-devkit) - Official Huawei Cloud plugin for AI agents — skills, MCP tools, safety…

</details>

<a id="mods"></a>

## Mods: built with the mod capability

Every entry here shows evidence of using the capability Claude Code gained in 2.1.287: it draws through `ui.render`, owns a pane, band or card, reads `$.ui.selection()`, spawns teammates with `agent.spawn`, or says plainly that it is a mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2541 · Python · 👁️ observed · 0d</summary>

##### 📝 Summary

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2541**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>animated recording</sub></td>
</tr></table>

<sub>Asset hot-linked from the upstream repository because no redistribution-friendly licence was declared.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐514 · JavaScript · 👁️ observed · 0d</summary>

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
| Stars        | **514**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐200 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **200**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐152 · TypeScript · 👁️ observed · 8d</summary>

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
| Stars        | **152**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐135 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **135**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐108 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **108**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>no media published</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐81 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **81**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 3d</summary>

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
| Stars        | **79**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐72 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **72**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐61 · Shell · 👁️ observed · 5d</summary>

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
| Stars        | **61**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 9d</summary>

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
| Stars        | **50**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3d</summary>

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
| Stars        | **46**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **23**     |
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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐21 · TypeScript · 👁️ observed · 10d</summary>

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
| Stars        | **21**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9d</summary>

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
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

Use Codex, GLM, and other coding agents as Claude Code subagents.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: built with the mod capability`                             |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **16**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐15 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **15**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6d</summary>

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
| Stars        | **14**     |
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26d</summary>

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
| Last push    | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 8d</summary>

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
| Stars        | **7**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Watch on youtube.com</a> · playback opens on the host site; GitHub cannot embed it inline</sub></td>
</tr></table>

</details>

<details>
<summary><b>More in this category</b> <sub>· 448</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods and the tools to build them: a builder skill, then mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - The Claude Code harness I run every day, published under this name since day…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）.
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
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community Claude mods, plugins &amp; skills, installable from one marketplace.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (function-hooks plugins) for Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - The Baselane mods gallery: Claude Code mods, checked and pinned.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - A decision queue CLI/TUI for humans working with conversational agents.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE pane mod: agent board, file tree and HWP/PDF viewer, system…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code mod that draws Edit and Write diffs in two side-by-side columns.
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, painted onto Claude Code.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - A floating status card for Claude Code — model, context, rate limits, cost…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods for Claude Code: function-hook plugins that add live panes and behaviour…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard masks names and secrets while you screen-share;
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Unlock the full power of Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod (plugin) that adds a side pane with Activity, Files, Agents…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, guardrails and quality-of-life mods for Claude Code: context, usage…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Two Claude Code mods above the prompt box: context-window meter, 5-hour limit…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Make the Claude Pro plan last longer: Claude Code mods for an exact usage HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Read the markdown files Claude Code names, rendered beside the session, and…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: pasted image thumbnails above the prompt, in any terminal.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: Claude Tools menu, Zen mode, terminal themes, effort and mode…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Voice coworker for Claude Code. Talk things through with a 3D wolf powered by…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, a live typing speedometer with per-prompt stats.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fireworks for Claude Code: every keystroke, tool call, commit and green test…
- [Danovich/turntype](https://github.com/Danovich/turntype) - A typing test for the time while Claude works. A Claude Code mod.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Discover Claude Code mods, plugins and extensions with animated demos, category…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod: mermaid diagrams drawn inline in the transcript.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Small Claude Code mods (function-hook plugins): session-switcher and more.
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six Claude Code mods: plan limits and context above the prompt, an allowlist…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout.
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Two Claude Code mods for running many sessions at once: a context card above…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: discover, inspect, toggle and update Claude Code mods.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Best Claude Code Mods: hand-picked, validated, pinned.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code plugin: automatic Claude model routing.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Trims huge tool outputs before they fill Claude Code.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Six mods for Claude Code: animated Clawd mascot, usage-limit and prompt-cache…
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
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code mods on demand — a skill that reads your conversation and builds…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Two Claude Code mods: cache-keeper and ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code mods that keep an agent honest — function hooks that guard scope…
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - The Claude Code mods I use.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS notch dashboard for Claude Code: usage limits, open sessions, task…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della prompt cache, prossimi passi, bottoni rapidi e…
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Cost, tokens and plan limits of your coding agents.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - A Claude Code mod that draws your usage limits and spend in the band above the…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods: progress bars for plans, a ledger of what Claude left…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - See what Claude Code runs in the background: subagents, Codex jobs, shells…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods by MacLeod Labs: streams untangles a session.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Day-one field notes on Claude Code mods on Windows: a context/quota fuel bar, a…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: a debugger for Claude Code tool calls.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code mod: live GitHub pull request status.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code mod: live cost, context &amp; plan-quota meters above the prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - A Claude Code mod that holds subagent fan-out, heavy-context prompts and retry…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin and mod: an AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - A Claude Code mod that turns your global skills, agents, rules and tools on or…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code plugins (mods): switch between several Claude accounts, watch usage…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Tested, one-command-install Claude Code mods: guardrails for YOLO mode, live…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods for Claude Code: plugins built on function hooks.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - A bunch of claude code mods built by me.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods. touch-map: see which files Claude listed, read, edited or…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Pick up a foreign language while you work with Claude Code.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Tell Claude what you want. Get it back built, tested, reviewed by another AI…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Babysits a long Claude Code session so you don.
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - A Claude Code mod that keeps your prompt cache warm while you.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Live cost, token and context usage sidebar for Claude Code: a mod that shows…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Goal, tasks and agents above your Claude Code prompt — zero setup.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code mods for real Engineers.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code&#x27;s terminal session recap, in the Claude desktop app&#x27;s Code tab.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack 的 Claude Code mods 合集.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - A Claude Code mod: a pane with the session.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - See which files each Claude Code agent has in its context, and how much of each.
- [deejay-hub/sf-headless-band](https://github.com/deejay-hub/sf-headless-band) - A Claude Code mod for Salesforce showing which Orgs are connected.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Turn every Claude Code session into a little adventure: generative music that…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Small Claude Code mods for the terminal and the desktop app.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI skill + mod that adds Spanish words into agent replies.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Your Alarum events above Claude Code.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - A Claude Code mod for capturing thoughts mid-work, triaging them across…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra lateral estilo Evangelion para Claude Code: contexto, cuota, actividad…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - A Claude Code mod that restyles it as The Machine from Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Claude Code mod: a pixel-art squad suggests the right model.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code mod for mandatory, verified DAG workflows of…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - A Claude Code mod: one pane for every subagent, the files they touch, and your…
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Code mod (CC tint mod): color each window by its repository, ring the…
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - Various mods I have made for claude that I find helpful.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: session status, live Spec Kit progress and usage-window…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - The context window as one row above the prompt, drawn the way Claude Code draws…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - A live task HUD for Claude Code Desktop: a strip above the prompt while Claude…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code plugin (mod) that makes the Claude Code terminal UI look like the…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Don&#x27;t let your attention wander off while waiting for Claude Code&#x27;s answer.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - A free, open-source plugin for Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Claude Code mods for long sessions: sitrep boxes each reply.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated, tested, and every mod ships with the prompt that…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code skills: a docs fact-checker, a code auditor, a bug-memory log, a…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Claude Code mod that rewrites rough prompts into clear ones before you send…
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - A Claude Code mod that keeps a live casebook of the Evidence rea gives the…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Pedro La Rosa.
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Claude Code mod: your 5-hour and 7-day usage limits as live, animated bars…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code buddy plugin: an ASCII companion above your prompt that remembers…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Render LaTeX display math in Claude Code.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: an unofficial Avengers fan mod for Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: a Claude Code mod that reads Claude.
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Spank Claude when it messes up — a stress-relief mod for Claude Code: cartoon…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code mods: small plugins for live panes, cost-aware model routing, and…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code mod &amp; plugin: usage monitor, token tracker &amp; statusline.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Catch the drift of your Claude Code session.
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [agukov-dev/token-meter](https://github.com/agukov-dev/token-meter) - Claude Code mod: rate limits, context and spend under the prompt.
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Claude Code mods marketplace: agent-board, auto-model, session-collab +…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods: session stat cards above the prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - An animated braille cat above the Claude Code prompt.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code mod: route cheap work to GLM/Kimi through a child Claude Code, keep…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - A pixel cat above your Claude Code prompt that runs an OmniDimension voice…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - A Claude Code mod that picks a good moment to compact to keep the context…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods for Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - General-purpose mods for Claude Code: bands, panes, toasts and hooks.
- [arifamir/nukey](https://github.com/arifamir/nukey) - Nukey the microwave: a Claude Code mod and plugin marketplace.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Short workouts while Claude works: a daily goal, streaks, badges and optional…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - A usage board for Claude Code: spend per model (today, week, month, all time)…
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now Playing mod for Claude Code: Apple Music and Spotify above the prompt, with…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods fuer Claude Code: Cache-Uhr, Blast Radius, Vorschlaege, Arbeitsliste, Grill.
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - A Claude Code mod: the record of orchestrated work, with runs, lanes…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code mods: Suggestion Spotlight shows what Claude.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Just a owl for your Claude Code.
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Mods do Claude Code criados por mim (painéis, comandos e hooks).
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - The original Doom engine with Freedoom, playable inside Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Small, readable Claude Code mods from the CorporateChittyChat channel.
- [colorfield/claude-ci-watch](https://github.com/colorfield/claude-ci-watch) - Claude Code mod: Pane and status line for the current branch.
- [colorfield/claude-lagoon-watch](https://github.com/colorfield/claude-lagoon-watch) - Claude Code mod: Pane with the Lagoon project.
- [colorfield/claude-port-guard](https://github.com/colorfield/claude-port-guard) - Claude Code mod: Stops Claude from killing, or running E2E tests against…
- [colorfield/claude-session-line](https://github.com/colorfield/claude-session-line) - Claude Code mod: Status line with context fill, model, effort, git branch or…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Keep Claude Code on a plan: stages, approval gates and a file budget enforced…
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Claude Code mod: a band above the prompt with the prompt-cache countdown, cache…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - My personal Claude Code mods, customised for my own setup.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀 전용 Claude Code mods (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [dankelleher/claude-mod-pin-message](https://github.com/dankelleher/claude-mod-pin-message) - Claude Code mod: pin a reply above the prompt, collapsible to a one-line summary.
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Eleven Claude Code mods (function-hook plugins) for a many-parallel-sessions…
- [davidcoulson/session-crew](https://github.com/davidcoulson/session-crew) - A Claude Code mod that shows the side sessions a desktop session starts as…
- [daviddecorso/claude-mods](https://github.com/daviddecorso/claude-mods)
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Claude Code mods: an OpenSpec and sub agent board, hand over before compacting…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - A Tamagotchi that lives inside Claude Code: it hatches, eats the code Claude…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [DerpcatMusic/claude-context-controls](https://github.com/DerpcatMusic/claude-context-controls) - Claude Code mod: nested context / 5h / weekly rings, compaction threshold and…
- [devsomelife/somelife-claude-mods](https://github.com/devsomelife/somelife-claude-mods)
- [dgsantana/claude-mods](https://github.com/dgsantana/claude-mods) - Claude Code mods: omp-port.
- [dhiroo-jpg/claude-mods](https://github.com/dhiroo-jpg/claude-mods) - クロードの使用量をチャット画面に表示.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - A Claude Code mod: a band above the prompt with Claude news and the breaking or…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - A Claude Code mod: a board of your other sessions above the prompt — who waits…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code mod: after a guard blocks a tool call, it stops recognized detours…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code mod: one inbox for messages from teammates, named subagents and…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code mod: explains sandbox blocks and turns repeated blocks into…
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - A live wave board of your session.
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods (function-hook plugins): session-meter and more.
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi — a Claude Code mod: a mascot that reads the room above the prompt, with…
- [g761007/hudcade](https://github.com/g761007/hudcade) - A pixel-art HUD for Claude Code: context, cost, cache, agents and rate limits…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Seven Claude Code mods: savvy-progress, skins, filetree, cache-tax…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - A Claude Code mod for the desktop app: click a file reference in a reply and it…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Useful claude code mods.
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Private marketplace of Claude Code mods.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey.
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code mod: how long each answer took, how long Claude thought, and tok/s…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude mods marketplace.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - A cockpit above your Claude Code prompt. The duck reads the gauges.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: private values are replaced with…
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Claude Status Bar.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Claude Code mods: context bar and the cyberdeck HUD.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - 自动读取你的工程图，然后在 SolidWorks 里建模。Reads your engineering drawings…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 側邊欄的 context 用量面板：總量、分類、每輪成長、最佔地方的前幾名、快取、Claude 現在在做什麼.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 側邊欄的檔案清單：這次對話新建、修改、刪掉了哪些檔案，各改了幾行。/files 開或關（a Claude Code mod）.
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 8-bit 風格的毛毛（黑白荷蘭垂耳兔）在輸入框上方跑跑跳跳：等待時攤平、工作時跑、用工具時跳（a Claude Code mod）.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 側邊欄的「我問過的」：主人這次對話打過的每一句話，點一下看全文、複製、放回輸入框。/prompts 開或關（a Claude Code mod）.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 側邊欄的時間軸：這一輪的時間花在哪（等模型、想、寫、跑指令、網路、讀寫檔案、等幫手）。/timeline 開或關（a Claude Code mod）.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 側邊欄的 token 往來：主對話每次送給 Anthropic 多少 token、等多久、收到多少，最上面是合計.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code 的誠實豆沙包：每一輪答完，Claude 小聲說一句心裡話（a Claude Code mod）.
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Evidence-gated plan checklist for Claude Code: approved plans become a…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 简体中文汉化（自管版）——自己的翻译表 + patch 工具 + 升级检查.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - Two Claude Code mods: session handoffs with replies, and routing simple turns…
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph Ayoub.
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd lives in a band above your Claude Code prompt: acts out the session…
- [kartollikaa/claude-android-emulator](https://github.com/kartollikaa/claude-android-emulator) - Claude Code mod: Android emulator and device screens inside Claude Code.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - A Claude Mod to read and join the conversations between your Claude Code…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code mod: every Claude Code session in one floating window, with live…
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - Some proof of concepts for claude-code-mods.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Claude Code mods, published as a marketplace.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph oh what Claude Code knows.
- [l4ckofsleep/ccdetails](https://github.com/l4ckofsleep/ccdetails) - Claude Code mod: context fill, prompt-cache hit %, rate limits and cost above…
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Ten Claude Code mods: an animated pixel pet, Code Wrapped, lo-fi beats, plus a…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu.
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - A community-curated Claude Code Mods guide: use cases, original demos…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - A Claude Code mod that shows what Claude is doing in the iTerm2 tab subtitle…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, an unofficial fan-made pixel companion that lives above the Claude Code…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: answer Claude point by point, right on the text.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Small mods for Claude Code: runner-avatar, a little avatar that runs above your…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - Small Claude Code mods from the MateAI channel.
- [matrac/burnline](https://github.com/matrac/burnline) - Claude Code mod: usage limits and task progress in one status line.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of what your AI coding agent is aiming for…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code mod: /sessions pane to browse and delete sessions with their…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Side pane for Claude Code: files Claude wrote, terminal splits, git repo status…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [Miriam2040/nugget](https://github.com/Miriam2040/nugget) - Select any part of Claude.
- [mmedum/glimt](https://github.com/mmedum/glimt) - A quiet side pane for Claude Code: what this session is doing, its plan, its…
- [mmedum/nuet](https://github.com/mmedum/nuet) - A dim time above each prompt and each reply in the Claude Code transcript…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - Claude Code plugins for sessions and memory: a Memory pane mod and a…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code mod that switches the todo tools back on for models that leave them…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod that waits for a safe pause, then hands your session over or…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code mod: one line per task list above the prompt with the current task…
- [mwmrs/claude-mods](https://github.com/mwmrs/claude-mods)
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Play Connect Four against an AI inside Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code mod: when another coding agent commits to your repo, Claude notices…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Claude Code mod: keeps sessions light — usage line, heads-up and one…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code mod for repos shared by several AI agents: stops secret values…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code mod: one button per delegate-skills implementer.
- [ngxuanbminh/pr-watch](https://github.com/ngxuanbminh/pr-watch) - Claude Code mod: watch the GitHub PRs of the repo you.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Re-arms Claude Code.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - A guard rail for SQL in Claude Code: asks before Claude runs DELETE, UPDATE…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - One mod for Claude Code, Windows and CJK first: pasted-image and text previews…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - The best Claude Code Mods, sorted by what they do for you.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Deux Claude Mods pour Claude Code : garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Timestamps for Claude Code: the time on every message, reply and tool call…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Track changes for Claude Code: see exactly what Claude changed in your Excel…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Mods for Claude Code: plugins of function hooks that work in any repository.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Various mods and skills for my Claude Desktop setup.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Claude Code mod: tracks every subagent.
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Claude Code mod: every subagent as a little stick person in a side pane, with…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ReDev1L/leanctx-colored](https://github.com/ReDev1L/leanctx-colored) - Claude Code mod: colored lean-ctx output.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod: press-ups to do while Claude works. No tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - just a list of mods I.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Three dependency-free mods for Claude Code: a responsive statusline, a…
- [Ron-Nefyodov/security-poc-mod](https://github.com/Ron-Nefyodov/security-poc-mod) - POC-only Claude Code mod for explicit, scoped local security demonstrations.
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - An open-source marketplace for Claude Code mods, with repository skills for…
- [RuahTechSolutions/code-buddy](https://github.com/RuahTechSolutions/code-buddy) - Claude Code mod: staging guard, blast radius, edit replay and an agents panel…
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - My mods for Claude Code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code mod: turns the plan you approve in plan mode into a live checklist…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - A hand-picked list of Claude Code mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Cost-free mode: helper agents run on Haiku, and big files and logs are…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - A lofi soundtrack that follows the session: calm, focus, flow, plus cues for…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Learn while Claude codes: after a turn that changed code, one question about…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - A tape of every edit Claude makes: replay each change typing itself in, step…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Claude Code mods: token-bar, your context window and usage limits above the…
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in the conversation…
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Mission control for Claude Code: live subagent fleet, token/cost usage, effort…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Showrin.
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods.
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - One-click commit messages for Claude Code with a dancing pixel-art Malenia.
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - 직접 만든 Claude Code mod 모음 (플러그인 마켓플레이스).
- [sunwu51/english-assistant](https://github.com/sunwu51/english-assistant) - Claude Code Mods plugin for contextual Chinese-English translation, spelling…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場.
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Claude Code mod: see your Cursor / VS Code file and selection above the prompt…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — a Claude Code mod that shows your Claude plan usage.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - A Claude Code mod that shows the current session in a pane: each prompt, the…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - A Claude Code plugin marketplace of mods: function-hooks plugins that draw…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Claude Code mods by Toptaab.
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Small, fun and useful mods for Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code mod: animated progress band and completion summary for long-running…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Three small Claude Code mods: see when your subagents will finish, queue…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Say &quot;I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Ask Claude a side question in a pane next to your work.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code plugin: prompt-cache countdown, cache hit rate, context weather and…
- [wablevaibhav/claude-mods](https://github.com/wablevaibhav/claude-mods)
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - A Claude Code mod: a highlighter pen for replies, a side panel for query…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter) - This Claude Code mod shows a card above the prompt.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — when context outgrows its shell, shed it into the folder and keep going.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod per Claude Code: segreti oscurati, cose da fare, verifiche e CI, diario…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code plugin: your Claude Pro/Max usage limits with a pace forecast…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods for Claude Code. agent-crew: watch your subagents work as a live pixel…
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - Terminal side-panel mods for Claude Code — agent tracing, token-powered Tetris…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - A live task board for Claude Code: plan before building, follow every task…
- [yuu1111/claude-agents-skills](https://github.com/yuu1111/claude-agents-skills) - Claude Code mod that loads Agent Skills from the shared .agents/skills…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - A hand-picked collection of the finest of resources for the most awesome of…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - A Claude Code plugin that shows what.
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Beautiful highly customizable statusline for Claude Code CLI with powerline…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - All parts of Claude Code.
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ tips for getting the most out of Claude Code, from basics to advanced…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Review your coding agent.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Comprehensive status line plugin for Claude Code with context usage, API rate…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Build mods for Claude Code: Hook any request, modify any response, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - A comprehensive statusline dashboard for Claude Code — session info, quota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: track the carbon footprint of your Claude Code sessions.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - An aesthetic statusline for Claude Code by awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Public Claude Code skills and mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash commands and guides for Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legal free LLM APIs &amp; coding agents — self-updating, probe-verified twice a…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Fast, zero-dependency cost calculator and customizable statusline for Claude…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live football(soccer) scores, fixtures and standings for the competition you…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill that turns your coding agent into a keyboard firmware expert.
- [Tripstack-Corp/spyc](https://github.com/Tripstack-Corp/spyc) - A Rust TUI file commander where the AI agent in the side pane can query the…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Prayer times, Hijri date, adhkar, daily ayah, sunnah fasting, Ramadan, Jumu.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Personal Claude Code configuration versioned inside ~/.claude — agents, skills…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness plugin for research topics…
- [chrisnguyen1211/pillrdotlol](https://github.com/chrisnguyen1211/pillrdotlol) - Every coding agent and every API key, in one pill at the edge of your Mac.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [luucas42/agent-flow](https://github.com/luucas42/agent-flow) - A live workflow panel for Claude Code: the main model, the advisor and every…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Lightweight Claude Code status line — one ~170-line Bash script, zero…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code plugins I use every day: skills and mods, cleaned up so they work…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analyze Claude Code token usage and costs from local conversation logs and…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace for Claude Code Plugins and Skills to facilitate mods of the game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Split-pane viewer for Claude Code in Windows Terminal and tmux: the session as…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository for Claude Code Awesome Media mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Cut Claude Code &amp; Codex token spend: routes lookups and test runs to cheaper…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - A status line and token line for Claude Code: context, 5-hour and weekly usage…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - the friendly, fiddle-with-everything status line for Claude Code — truecolor…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agent teams. Under control. Hard worker limits, live team visibility…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [0xSerachu/claude-shortcuts](https://github.com/0xSerachu/claude-shortcuts) - Explore and quiz yourself on all Claude Code shortcuts with categorized…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows PowerShell status line for Claude Code: 5-hour and weekly limits with…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professional-grade Claude Code statusline: session duration, multi-currency…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Subscription-aware status line for Claude Code.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Statusline para Claude Code en español: tarea, skills, contexto con semáforo…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Claude Code status line for Windows: token totals, API-rate cost, and…
- [gvart/claude-config](https://github.com/gvart/claude-config) - My Claude Code setup: agent-monitor mod, skills, agents and a one-command…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Single-line status bar for Claude Code: model, git, context, tokens, cost…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Preview images inside Claude Code: hover a chip under a reply to pop the…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Personal Claude Code configuration: permissions, statusline, MCP servers.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code status line with agent panel rows.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sync Claude.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Display a detailed, color-coded status bar for Claude Code showing context, git…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Two-line status bar for a terminal coding agent: directory, git, PR, model…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code statusline hook — tracks token usage and context across sessions…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Marketplace Claude Code de MSF Supply : mods sélectionnés et figés par commit.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Rich multi-line status line for Claude Code — live usage limits (5h + weekly)…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness de Claude Code de Nacho (reglas, tablero, mods).
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Multi-line Claude Code status line: context bar, git branch, 9router…
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - OrihuelaConde.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitor Claude Code status from your macOS menu bar with real-time indicators…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skills and mods for Claude Code and Cowork — project-tracker, reference-doc…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code status line for Windows (PowerShell): usage bars, 5h/7d reset…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Custom Claude Code statusline (upstream: kamranahmedse/claude-statusline).
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Starter harness for Claude Code: hooks, statusline, local models, swarm…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - A small dashboard for Claude Code: context %, cache countdown, 5-hour &amp; weekly…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Custom terminal status bar for Claude Code: model, directory, git state…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Track Claude Code context usage, session costs, and rate limit resets with a…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用の mod 集 (goal-orchestrator: /goal をタスク分解して SubAgent に委譲させる).
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - 多机同步 Claude Code 用户级配置（settings.json + statusline），GitHub / Gitee 双源.
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - A Claude Code status line: folder, git branch, model, context window usage and…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Proactive AI Memory &amp; Rate-Limit Monitor for Claude…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code hooks, subagents and statuslines: open-source collections and…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code statusline showing real-time token usage and estimated energy…
- [previsioncystolith584/ai-video-downloader](https://github.com/previsioncystolith584/ai-video-downloader) - Download videos from major platforms and automatically add translated…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - A Deno-powered status line for Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods for Claude Code: panes, bands and buddies built on function hooks.
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Claude Code-style UI bundle for the Pi coding agent — tool rendering, spinner…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pass tasks between your Claude Code sessions.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - This in a MCP server to control MODS, the modular cross platforms tool for…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex and Claude Code skill for translating CK3 mods with a local LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods and other extensions for Claude Code.
- [alan-oliv/team8](https://github.com/alan-oliv/team8) - A live browser console for Claude Code agent teams — every teammate.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code statusline: CCometixLine beauty + Claude HUD functionality.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: find what you ask Claude Code again and again, and turn it into a…

</details>

<a id="dsh-cordis"></a>

## DSH and Cordis plugin ecosystems

DeepSeek Harness and Cordis reach the same place from a different direction: for them the plugin is the mod mechanism, so a plugin there is the equivalent of a mod here.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74398 · TypeScript · 👁️ observed · 0d</summary>

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
| Stars        | **74398**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐134601 · TypeScript · 🔎 inferred · 0d</summary>

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
| Stars        | **134601** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100691 · TypeScript · 🔎 inferred · 0d</summary>

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
| Stars        | **100691** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82387 · JavaScript · 🔎 inferred · 0d</summary>

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
| Stars        | **82387**  |
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
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25517 · Python · 🔎 inferred · 0d</summary>

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
| Stars        | **25517**  |
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
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8659 · TypeScript · 🔎 inferred · 0d</summary>

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
| Stars        | **8659**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4385 · TypeScript · 🔎 inferred · 0d</summary>

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
| Stars        | **4385**   |
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
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3060 · TypeScript · 🔎 inferred · 0d</summary>

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
| Stars        | **3060**   |
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
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1601 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

A pre-execution guard for AI coding agents. It blocks destructive Git and file system commands, plus common attempts to access sensitive files, before a tool call runs. Supports Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode, and Pi.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1601**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/GanyuanRan/Aegis">GanyuanRan/Aegis</a></b> · ⭐1343 · Python · 🔎 inferred · 0d</summary>

##### 📝 Summary

Make AI coding agents architecture-aware: baseline-first, evidence-verified, drift-checked, and safe across long tasks.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1343**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-skills` · `ai-agents` · `ai-coding` · `architecture-driven-development` · `awsome-coding-plugin` · `baseline-first` · `claude-code` · `codex`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ganyuanran--aegis/4581f8f71af5092d.png" width="100%" alt="GanyuanRan/Aegis screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1179 · Go · 🔎 inferred · 0d</summary>

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
| Stars        | **1179**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐552 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **552**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>animated recording · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">Open video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/text2future/flowix">text2future/flowix</a></b> · ⭐459 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **459**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-memory` · `claude-code` · `codex-cli` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `hermes-agent`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/9fc65a8848fe78ee.png" width="100%" alt="text2future/flowix screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/ea3f84c8693d4236.gif" width="100%" alt="text2future/flowix animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐374 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **374**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0d</summary>

##### 📝 Summary

Your Intelligence, Orchestrated. Every builder. Every team. Every agent. For Everyone.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Go                                                                               |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **351**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>animated recording</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐230 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **230**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Native DeepSeek Harness (DSH) plugin integrating TypeSafe Jev or Decision api like luna as a System One decision layer for agent selection, supervision, corrections, and approvals.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **204**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐181 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **181**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐180 · Python · 🔎 inferred · 0d</summary>

##### 📝 Summary

Runtime evidence that helps agents trace, profile, and burn down hotspots in application and native code, GPU kernels, and inference stacks.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **180**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐142 · TypeScript · 🔎 inferred · 0d</summary>

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
| Stars        | **142**    |
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0d</summary>

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
| Stars        | **137**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐121 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness 桌宠插件：元气鲸鱼娘看板娘陪你写代码 🐋 支持 DSH 桌面端 0.2.0-rc.2 与旧版 Web（desktop pet / mascot，local-first）

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **121**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Aik358/dsh-auto-memory">Aik358/dsh-auto-memory</a></b> · ⭐111 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Proactive associative memory for DSH: system-prompt recall before the model speaks, three-layer auto-consolidation, skill crystallization, and Astra-style context management - handoff ledgers, PLAN whiteboard, water-level sensing. Local-first, model-agnostic, zero deps. 主动联想记忆+Astra 式上下文管理：自动唤回/自动沉淀/技能固化/交接账本与白板跨窗口续命/水位感知。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **111**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `context` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `memory` · `npm` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/ba11cddac1ec16d1.png" width="100%" alt="Aik358/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/a44325f737275ef4.gif" width="100%" alt="Aik358/dsh-auto-memory animation"><br><sub>animated recording</sub></td>
</tr></table>

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
<summary>🧵 <b><a href="https://github.com/morluto/leantoken">morluto/leantoken</a></b> · ⭐64 · Rust · 🔎 inferred · 0d</summary>

##### 📝 Summary

Code intelligence for agents: find the code that matters and keep your context window and tokens lean.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | Rust                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **64**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `ai-coding` · `code-intelligence` · `code-navigation` · `code-retrieval` · `code-search` · `codebase-indexing` · `coding-agents` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--leantoken/38b3e8f4a7b20aea.jpg" width="100%" alt="morluto/leantoken screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cloader/dsh-taskboard">cloader/dsh-taskboard</a></b> · ⭐59 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

deepseekharness 任务看板插件

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **59**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `kanban` · `task-board`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cloader--dsh-taskboard/cfd9efd4514a0b8f.png" width="100%" alt="cloader/dsh-taskboard screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

NekroNXT：基于 DeepSeek Harness（DSH）的多平台群聊智能体系统｜A DSH-powered multi-platform group-chat agent system

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **35**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **34**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

DSH 会话导航

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-toolbox-ui">Imzl-zl/dsh-toolbox-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0d</summary>

##### 📝 Summary

Toolbox panel for DeepSeek Harness Web: MCP manager (tools & JSON Schema, market, import, workspace copy) and skills manager (scopes & shadowing, enable/disable, model auto-invocation, skillhub.cn market).

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH and Cordis plugin ecosystems`                                               |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Language | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp` · `skill-manager` · `skills`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-toolbox-ui/bab6fdf6979d2501.png" width="100%" alt="Imzl-zl/dsh-toolbox-ui screenshot"></td>
<td align="center" valign="top"><sub>no media published</sub></td>
</tr></table>

</details>

<details>
<summary><b>More in this category</b> <sub>· 52</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - A curated list of the best awesome AI plugins for AI assistants including…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - A plugin runtime for software that iterates on itself — the substrate where…
- [hanelalo/browser-bridge](https://github.com/hanelalo/browser-bridge) - 让你的agent真的像你一样操控你的浏览器窗口.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 插件精选目录 — 14 类 280+ 个社区插件，覆盖 MCP / Skill / TUI / 多 Agent…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin: Git Bash shell for all agent modes on Windows.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver…
- [liustack/pptwise](https://github.com/liustack/pptwise) - A real PowerPoint, not HTML. Tell your AI what to cover and pptwise builds an…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) - DSH 插件：一个设置面板，统一管理 MCP 服务器、技能、场景、记忆、子智能体人格、AGENTS.md…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Always-on compatibility testing for DeepSeek Harness plugins: exact releases…
- [chipweaver/veripower](https://github.com/chipweaver/veripower) - An open-source agent flow from natural language spec through Verilog RTL and…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness host plugin that keeps project documents and long-term memory…
- [PianoPrince/dsh-workspace-mover](https://github.com/PianoPrince/dsh-workspace-mover) - 拖拽真迁移 DSH 会话跨工作区：批量移动、分组合并、挂错归位、回收站、备份恢复 + 对话内 agent 工具；步步备份可回滚，零 token / True…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray for DeepSeek Harness plugins: declared capabilities vs actual behavior.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [Noob-stupid/dsh-github-login](https://github.com/Noob-stupid/dsh-github-login) - DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [laoduu/DeepSeek-Harness-yizi-themes](https://github.com/laoduu/DeepSeek-Harness-yizi-themes) - 为 DeepSeek Harness（dsh）Web UI 提供的 19 个精品风格主题，完整移植自 YiziMarkdown 的设计语言.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Zero-dependency verification standard for DeepSeek Harness (dsh) plugins…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness plugin ecosystem: 86 open-source plugins in a 101-repo family…
- [possible055/agentshim](https://github.com/possible055/agentshim) - High-performance, capability-aware repository tools and process execution for…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode on DeepSeek Harness — DSH plugin that keeps OpenCode Zen + Go…
- [YeqingTang/dsh-session-flow](https://github.com/YeqingTang/dsh-session-flow) - DSH 会话信息流重设计插件：跨会话档案柜，折叠时间线 / 血缘树 / 检索 / 双模式摘要 / ZIP 导出 / 实时跟踪.
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — third-party plugin marketplace and guarded lifecycle manager for…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人为本的可拓展桌面工作台：对话、笔记、表格、文件在同一工作台；自建服务端即可开启多人实时协作.
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Run DeepSeek Harness on desktop with zero token costs—a free, open-source GUI…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Bots workbench: Cordis plugin bridging the sdk-bots orchestration gateway…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Independent third-party plugins and tools for DeepSeek Harness, maintained by…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Use OpenCode Zen free models in DeepSeek Harness with anonymous access or an…
- [Asukayanamii/learn-cordis4py](https://github.com/Asukayanamii/learn-cordis4py) - Cordis 插件框架的 Python 复刻：上下文与作用域、fiber 生命周期、五种事件分发、服务依赖注入、配置校验、YAML 装载器.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness plugin: turns the Windows sandbox ACL provisioning failure…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - dsh plugin: turn a truncated length stop into the CONTEXT_WINDOW_EXCEEDED…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - A Rust plugin runtime with a Verus-verified lifecycle kernel and Cordis…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Arkme account, records, chat and interwoven-moments integration for DeepSeek…

</details>

<a id="writing"></a>

## Writing, discussions and videos

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10d</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10d</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10d</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8d</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2d</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9d</summary>

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

<a id="other"></a>

## Other projects

Entries that touch the mod surface but are not themselves mods, kept visible rather than hidden.

<details>
<summary>📦 <b><a href="https://github.com/rajmand/claude_mods">rajmand/claude_mods</a></b> · TypeScript · 👁️ observed · 0d</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Other projects`                                                  |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Language | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **0**      |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

</details>

<a id="projects-by-implementation-language"></a>

## Projects by implementation language

The ecosystem is concentrated in Python and TypeScript, but typed clients keep appearing in other languages. This table is generated from the entries themselves.

| Language   | Entries | Examples                                                                                                      |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 386     | `anthropics/claude-code`, `anthropics/claude-code-action`, `see-stack/claude-code-mods`                       |
| JavaScript | 76      | `huaweicloud/huaweicloud-devkit`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`          |
| Python     | 39      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 10      | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 9       | `persiyanov/herdr-reviewr`, `Tripstack-Corp/spyc`, `cc-friend/ccost`                                          |
| Go         | 5       | `kartollikaa/claude-android-emulator`, `backstabslash/goccc`, `esengine/DeepSeek-Reasonix`                    |
| Swift      | 3       | `chrisnguyen1211/pillrdotlol`, `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`        |
| PowerShell | 2       | `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win`                                   |
| C          | 1       | `reporails/arcade`                                                                                            |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                          |
| MDX        | 1       | `jkf87/mod-guide`                                                                                             |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Last updated · 2026-10-12T21:29:43+08:00</sub>
