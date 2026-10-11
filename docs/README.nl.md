<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Geweldige Claude-mods">
</p>

<h1 align="center">Geweldige Claude-mods</h1>

<p align="center"><b>De op basis van bewijs beoordeelde index van Claude Code-mods, plug-ins en het diepere gedrag dat ze veranderen.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-624-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <b>Nederlands</b> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Actieve index** · Laatste synchronisatie: `2026-10-11T10:13:26+08:00` (UTC+8)
> · Items: **624** · Toegevoegd in de nieuwste update: **0** · Implementatietalen: **12**

<sub>Elk item hieronder is automatisch verzameld, gefilterd en opnieuw gecontroleerd. Niets hiervan is betaalde promotie.</sub>

<a id="featured"></a>

## Uitgelicht van dit moment

<sub>Eén item per categorie, gerangschikt op bewijsniveau en sterren, bij elke update opnieuw berekend. Een ranglijst, geen aanbeveling; elke keuze linkt door naar de volledige kaart hieronder. Projecten die een screenshot of opname hebben gepubliceerd krijgen de voorkeur, zodat de balk visueel blijft.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9467 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2533 · Python · 👁️ observed</sub>
<sub>Vind de spooktokens. Los ze op. Overleef compactie. Voorkom kwaliteitsverlies van de context.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74290 · TypeScript · 👁️ observed</sub>
<sub>🌊 De oorspronkelijke agent harness. Implementeer intelligente swarms met meerdere spelers, coördineer autonome workflows en bouw conversationele AI-systemen. Met…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Inhoud

- [Wat een Claude Code-mod is](#wat-een-claude-code-mod-is)
- [Hoe items worden beoordeeld](#hoe-items-worden-beoordeeld)
- [Officieel: de eigen repositories en release notes van Anthropic](#officieel-de-eigen-repositories-en-release-notes-van-anthropic) — **18**
- [Mods: gebouwd met de modfunctionaliteit](#mods-gebouwd-met-de-modfunctionaliteit) — **484**
- [DSH- en Cordis-plug-inecosystemen](#dsh--en-cordis-plug-inecosystemen) — **111**
- [Schrijven, discussies en video's](#schrijven-discussies-en-videos) — **11**
- [Projecten per implementatietaal](#projecten-per-implementatietaal)

## Wat een Claude Code-mod is

Claude Code gained **mods** in 2.1.287: extensions that may change deeper behaviour than a plugin could, and draw their own interface.

A mod can hook `ui.render` to paint a **row, band, pane or card** around the prompt, read the text you last selected with `$.ui.selection()`, spawn teammates with `agent.spawn`, and own a `Client` region. A mod that fails to draw fails alone — `ui.fault` keeps one broken mod from taking down the session.

This list covers mods, the plugin and hook surface they build on, and the DSH and Cordis equivalents. It deliberately does **not** cover the wider Claude Code ecosystem: a prompt pack is not a mod.

## Hoe items worden beoordeeld

Most lists in this space assert inclusion. This one says how much was actually verified, then lets you filter accordingly. A grade describes the evidence, not the quality of the project — a well-built mod nobody has written about yet is still `inferred`.

| Beoordeling                                                                      | Wat het betekent                                                                                                                                                                                       |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `published by Anthropic itself`                                                  | Published by Anthropic itself, or read directly from the official changelog.                                                                                                                           |
| `its own text names a mod API, or it declares the mod capability`                | Its own text names part of the mod surface — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, a pane, band or card — so the author is describing something they built against the real API. |
| `declared a mod, plugin or hook, but nothing about the mod surface specifically` | It calls itself a mod, plugin or hook, but nothing in its text names the mod surface specifically. Real, but unconfirmed.                                                                              |
| `matched on vocabulary alone`                                                    | Matched on vocabulary alone. Included so the filter is auditable, not because it is believed.                                                                                                          |

<a id="official"></a>

## Officieel: de eigen repositories en release notes van Anthropic

De eigen Claude-coderepositories van Anthropic en de releases die het modoppervlak hebben bepaald. Lees ze rechtstreeks uit de bron in plaats van uit een samenvatting.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150075 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Summary

Claude Code is een agentische coderingstool die in je terminal werkt, je codebase begrijpt en je helpt sneller te coderen door routinetaken uit te voeren, complexe code uit te leggen en git-workflows af te handelen — allemaal via opdrachten in natuurlijke taal.

<sub>🔧 Gebruik in code gevonden: `feed.xml`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **150075** |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9467 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9467**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8245 · Python · ✅ official · 1 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8245**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6336 · Python · ✅ official · 241 天</summary>

##### 📝 Summary

Een door AI aangedreven beveiligingsreview-GitHub Action die Claude gebruikt om codewijzigingen te analyseren op beveiligingskwetsbaarheden.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6336**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 1 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | Shell                                                             |

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

Aanvullend materiaal voor Claude Model Cards

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

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

Claude Mods toegevoegd: plugins kunnen nu dieper gedrag wijzigen. You should know toegevoegd, een ingebouwde mod waarin een zij-agent over je waakt en dingen markeert die jij of Claude mogelijk missen. Schakel deze in met `/plugin enable cc-plugin-you-should-know@builtin` (voor first-party-sessies met telemetrie ingeschakeld)

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

`$.ui.selection()` toegevoegd voor mods: retourneert de tekst die je het laatst in de volledig-schermmodus hebt geselecteerd en, wanneer de selectie binnen één transcriptregel valt, die regel. Een mod gerepareerd waarvan de knop soms de actie van een andere knop uitvoerde wanneer deze werd ingedrukt in een weergave die was getekend voordat Claude Code opnieuw was gestart. Volledig-scherms sessies gerepareerd die werden beëindigd met "unrecoverable interface error" bij het openen van het dialoogvenster voor achtergrondtaken terwijl een plugin of mod regels boven de prompt toonde. `claude plugin test` gerepareerd, dat mods op afstand als uitgeschakeld rapporteerde wanneer het alleen een verouderde opgeslagen instelling had gelezen

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Een deny- of ask-regel op een genest onderdeel van een samengestelde shellopdracht gerepareerd die niet bleef gelden boven de goedkeuring van een door de gebruiker geïnstalleerde mod op beheerde machines. Geïnstalleerde mods gerepareerd die niet in de eerste sessie na een upgrade werden geladen. `agent.spawn` toegevoegd voor teamgenoten, één agent-ID voor alle plugin-hookgebeurtenissen en inactieve en wachtende statussen in `$.agent.list()`. Sessies gerepareerd die eindigden met "unrecoverable interface error" wanneer een waarde die de `ui.render`-hook van een mod had geschreven, ervoor zorgde dat een rij een fout gaf tijdens het tekenen; de engine tekent nu zijn eigen rij. Rechts uitgelijnde inhoud in het paneel of de band van een mod gerepareerd die onder het sluitmarkeringsteken of `\[-\]` werd getekend, wh

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

`serverToolUses` toegevoegd aan het resultaat van de `turn.step`-hook van een mod: de toolaanroepen die API zelf uitvoerde (de adviseur), elk met id, naam, invoer, start en einde. `ceiling` toegevoegd aan de vraag en het oordeel die de `tool.check`-hook van een mod leest, waarbij de goedkeuring wordt benoemd die een organisatie voor een tool vereist. De typen `ThemeKey` en `Color` toegevoegd aan de typeringen van de plug-inhooks, zodat een editor de themakleuren opsomt die de tekening van een mod kan benoemen. Toegevoegd aan `claude plugin validate`: elke hook die een mod op een gating-site registreert, wordt vermeld met de vraag of deze een `.catch` heeft (`gatingHooks` onder `--json`). Het resultaat van een mod opgelost: `turn.step`

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

`prompt.autocomplete` toegevoegd, een event waaraan een mod haakt om eigen rijen toe te voegen aan de autocomplete-lijst van het promptvak Prompt-caching toegevoegd aan `$.model.complete` voor mods: `prompt` en `system` nemen tekstblokken, en `cache: true` op een blok cachet het verzoek tot daar Workflow-agents toegevoegd aan de `agent.spawn` mod-hook, met hun run en index, zodat een mod ze kan weigeren Write-, Edit-, NotebookEdit- en LSP-rijen gerepareerd, en enkele Read-, Grep- en Glob-rijen, waarbij verborgen werd waarom een mod de aanroep weigerde: de rij toont nu de reden Een `config.set`-, `state.set`-, `env.set`- of `agent.spawn`-hook van een mod gerepareerd die weigert na

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

`isDeferred` toegevoegd aan `$.tool.register` voor mods: `false` vermeldt het schema van de tool vanaf het begin in de prompt in plaats van achter tool search Een mod-hakenprobleem opgelost waarbij hooks op `classic.*`-gebeurtenissen werden overgeslagen terwijl de plugin-hooks-worker opnieuw startte, waardoor instellingenhooks zonder deze informatie moesten antwoorden Opgelost dat `claude plugin test` mislukte voor mods die `$.session.append` aanroepen; tests kunnen de toegevoegde rijen teruglezen met de nieuwe `mock.session`

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

MCP beheerconsole voor de officiële DeepSeek Harness MCP client: /mcp-command met healthdiagnostics en pipeline-proefaanroepen, een Settings MCP tabblad met server-CRUD (writes afgeschermd met goedkeuring, automatische back-ups) en een tool-proefconsole via de officiële toolpipeline (Apache-2.0, dsh-plugin).

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic`                |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Cross-session usage & cost observatory for the DeepSeek Harness web profile — trend/heatmap dashboards, per-model peak-hour pricing (CNY/USD), official DeepSeek balance with spend reconciliation.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic`                |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `billing` · `cordis` · `cost` · `cost-estimation` · `dashboard` · `deepseek` · `deepseek-harness` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/enc-hanted--dsh-pulse/4a81f8e7c5f01f18.png" width="100%" alt="Enc-hanted/dsh-pulse screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Dit is een launcher voor de officiële DeepSeek Harness. Geen aanpassingen; hij start alleen wat DeepSeek ontwikkelt.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic`                |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `$.ui.notify` toegevoegd voor mods: geeft een native melding via je eigen…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Esc of een onderbreking tijdens een `UserPromptSubmit`-hook of de…
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - A curated directory of source-verified DeepSeek Harness (DSH) plugins, tools…

</details>

<a id="mods"></a>

## Mods: gebouwd met de modfunctionaliteit

Elke vermelding hier toont bewijs dat de mogelijkheid voor Claude Code die in 2.1.287 is toegevoegd, wordt gebruikt: de vermelding tekent via `ui.render`, beheert een deelvenster, band of kaart, leest `$.ui.selection()`, start teamgenoten met `agent.spawn`, of zegt duidelijk dat het een mod is.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2533 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

Vind de spooktokens. Los ze op. Overleef compactie. Voorkom kwaliteitsverlies van de context.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2533**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐470 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Communitycatalogus van openbare Claude Code-mods (functiehooks), gescand vanuit GitHub, met informatie over wat elke mod kan lezen, schrijven, uitvoeren of via het netwerk kan verzenden. Bekijk https://mods.aidojo.si/

<sub>🔧 Gebruik in code gevonden: `data/seeds.txt`, `data/duplicates.txt`, `data/repos.txt`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **470**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐182 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code-mods: plugins die op hooks zijn gebaseerd en live regels boven de prompt, bewaking, panelen en games toevoegen. Contextbalk, gebruiksmeter, Codex reviewbewaking, Markdown-preview, wat er nu op Spotify speelt en meer.

<sub>🔧 Gebruik in code gevonden: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **182**    |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐117 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

Houd de promptcache van Claude Code tijdens pauzes warm en toon de geschatte kosten vóór een koude verzending.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **117**    |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐109 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code-mod: kiest de redeneerinspanning voor elke prompt, toont de promptcache en context en draagt met één klik over of comprimeert

<sub>🔧 Gebruik in code gevonden: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | HTML                                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **109**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Een agent-native QA CLI voor webpagina's. Deterministisch, geen tests om te schrijven, geen LLM.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | HTML                                                              |

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

Skins voor Claude Code: gereedschapsrijen met pictogrammen, diff-, tabel- en Mermaid-diagramkaarten, een gebruiksbalk en vijftien thema's. /skin wisselt ze direct.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **88**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Een verzameling claude code-mods

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

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

Kleurrijke, aanpasbare antwoorden van Claude Code: tabellen, code, diagrammen, grafieken en toolrijen in 15 thema's, met knoppen om te kopiëren. Een Claude Code-mod.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Summary

Claude Code-mods van Darrell Wang — banden boven de prompt, nul modeltokens. 台股／美股看板 + er volgt meer.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | HTML                                                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **65**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐62 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Een Claude Code-mod die een live agentdashboard in je terminal plaatst: context en kosten, tijdlijn van de adviseur, elke machtigingscontrole, subagentkaarten en swimlanes.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **62**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐57 · Shell · 👁️ observed · 3 天</summary>

##### 📝 Summary

Expert-skills, agents, opdrachten, regels, hooks en outputstijlen voor Claude Code — sessiecontinuïteit + moderne CLI-tooling voor realistische ontwikkelworkflows

<sub>🔧 Gebruik in code gevonden: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | Shell                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **57**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Claude Code-mods: live voortgangsbalken voor het plan boven de prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **46**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Kijk hoe Claude Code tijdens je werk een kleine cartoon maakt.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **32**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Een rail met de prompts van je Claude Code-sessie: beweeg erover om te lezen, klik om te springen (functie-hooks / Mods)

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **27**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Een upgrade voor Claude Code: een live cockpitpaneel, deelbare thema's en een pixelhuisdier dat uitbeeldt wat Claude aan het doen is

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Xcode's build, tests, console en SwiftUI-previews binnen Claude Code

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

Claude Code-mods: 21 stijlen en een volledige set functies die je naar behoefte inschakelt, voor de terminal en de desktopapp. · Geef Claude met één klik een nieuwe stijl en beschik over een volledige set functies die je naar behoefte kunt inschakelen.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Tien Claude Code-mods, beginnersgidsen, creatieprompts, veilige demo's en een sjabloon om zelf te bouwen.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Claude Code-mods: usage-band toont je 5h/7d-limieten, contextvenster en cache-hitpercentage boven de prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **12**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

Claude Code-mods die de vragen van Claude gemakkelijker leesbaar en beantwoordbaar maken (qa-guide).

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code-mod: context in tokens, limieten van 5 uur en per week versus de klok, aftelling van de promptcache, sessiekosten en actieve agents, in één balk boven de prompt.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-09 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Tien open-source mods voor Claude Code: livepanelen, banden, statusregels en beveiliging voor toolaanroepen. Burn meter, launch codes, session wrapped, boss fight, code pet en meer.

<sub>🔧 Gebruik in code gevonden: `swarm/README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Summary

Twee Claude Code-mods: Codex-bridge voor computergebruik en gecoördineerde Claude-sessies. Broncode, buildprompts, installatie en tests.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Geanimeerde pixelkunst boven je Claude Code-prompt die reageert terwijl Claude werkt. Zeven scènes, of je eigen afbeelding of GIF. Geen tokens.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **10**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Een interface rond je Claude Code- en Codex-terminals die door je agents wordt gebouwd, zodat het enige model in je hoofd van jou is.

<sub>🔧 Gebruik in code gevonden: `CLAUDE.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-08 |
| First listed | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

KOZMOS — live, visuele mods voor Claude Code (CLI + desktop): balken boven de prompt, zijbalken, statusregel, metgezellen, beveiligingen en geluid.

<sub>🔧 Gebruik in code gevonden: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

##### 📝 Summary

Sessietrackers voor Claude Code, gebouwd als mods: contextvenster, verbruikssnelheid van het planningsquotum en kosten per beurt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-09-15 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

Zes Claude Code-mods in één plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) met schakelaars per mod, plus een rapport over mods versus hooks.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

Verzameling Claude Code-mods van ontwikkelaarsbroertje. Taxipakket: taxameter, navigatie, flitspalen, dashcam

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Bekijken op youtube.com</a> · afspelen wordt geopend op de hostsite; GitHub kan deze niet inline insluiten</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Markdown, tijdens het typen op het promptvak van Claude Code geschilderd. Omheinde code wordt al vóór je het hek sluit een kaart met syntaxmarkering.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-03 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Claude Code-mods: 像素螃蟹用量面板 usage-hud + HTML-links die in de terminal klikbaar zijn en codekaarten voor kopiëren met één klik html-shelf

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-08 |
| First listed | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Mods voor Claude Code: function-hook-plug-ins die live deelvensters en gedrag aan de terminalinterface toevoegen

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Summary

Claude Code mod (plugin) die een zijpaneel toevoegt met Activity-, Files-, Agents-, Context- en MCP-tabs, een statusregel boven de prompt, een opnieuw gestylede chat, Mermaid-diagrammen in de terminal, tabellen, en code- en diffpanelen. Kleuren volgen zowel /color als het /theme (dark, light en andere).

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-06 |
| First listed | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 450</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Verzameling van meer dan 100 mods die je met Claude Code kunt gebruiken.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods en de tools om ze te bouwen: eerst een builderskill, daarna mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - De Claude Code-harness die ik elke dag gebruik, sinds dag één onder deze naam…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Gebruik Claude Mods om het dak van Claude Code te vervangen: wijzig de binary…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Vier Claude Code-mods: Cache Keeper, Recording Mode, Goal Meter en Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Claude Code-mods van Learning Hacker: de werking van de agent begrijpelijk in…
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code-mods die je prompts corrigeren en vertalen voordat Claude ze leest.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Een zijpaneel voor Claude Code: de subagenten die een sessie uitvoert, wat elk…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Een cockpit voor Claude Code: live planbalken, subagentstroken…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Met bronnen onderbouwde Obsidian-kennisbank over Claude Code-mods: hoe ze…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Vaardigheid die Claude Code-agents leert om Claude Mods…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Zijbalkpaneel van Claude Desktop (Code-tabblad): toont alle onafgemaakte en…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code-mods en -vaardigheden van Nekyia Labs, dagelijks gebouwd en…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude-mods (function-hookplug-ins) voor Claude Code.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Gebruiksbalk boven het invoervak van Claude Desktop (Code-tabblad): 5u /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-mods, plug-ins en skills, installeerbaar vanuit één marktplaats.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - De Baselane-modsgalerij: Claude Code-mods, gecontroleerd en vastgezet.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Een beslissingswachtrij CLI/TUI voor mensen die met conversatieagenten werken.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE-paneelmod: agentenbord, bestandsboom en HWP/PDF-viewer…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Een zwevende statuskaart voor Claude Code — model, context, rate limits…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code-mods: screen-guard maskeert namen en geheimen tijdens het delen van…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Ontgrendel de volledige kracht van Claude.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Deelvensters, vangrails en mods voor meer gebruiksgemak in Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Twee Claude Code-mods boven het promptvak: een meter voor het contextvenster…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Je plan dat zichzelf in de gaten houdt.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lees de markdown-bestanden die Claude Code benoemt, weergegeven naast de…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Spraakcollega voor Claude Code. Bespreek dingen met een 3D-wolf, aangedreven…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code-mods: typing-speed, een live snelheidsmeter voor typen met…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Vuurwerk voor Claude Code: elke toetsaanslag, toolaanroep, commit en geslaagde…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Ontdek Claude Code-mods, plugins en extensies met geanimeerde demo.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code-mod: mermaid-diagrammen inline in het transcript getekend.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Kleine Claude Code-mods (function-hook-plug-ins): session-switcher en meer.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code-mod: geplakte afbeeldingsminiaturen boven de prompt, in elke…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - Zie wat je volgende Claude Code-bericht kost: een live balk boven de prompt met…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code-mods: mod-scout (vind de mods die je het vaakst zou gebruiken)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Twee Claude Code-mods om veel sessies tegelijk uit te voeren: een contextkaart…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Claude Code-mod: beheer de inhoud van automatische contextcompressie native…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Laat het Claude Pro-abonnement langer meegaan: Claude Code-mods voor een exacte…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow voor Claude Code: een rustige checklist boven de prompt die het…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Beste Claude Code-mods: met de hand geselecteerd, gevalideerd, vastgezet.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code-plug-in: automatische routering van het Claude-model.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Zes mods voor Claude Code: geanimeerde Clawd-mascotte, balken voor…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Een marktplaats met mods voor Claude Code: een stapsgewijze debugger voor de…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code-mods: menu Claude Tools, Zen-modus, terminalthema.
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Het beste alles-in-één modpakket voor Claude Code: gebruikslimieten en…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Speel YouTube Shorts af in je Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code-mod die Edit- en Write-diffs in twee kolommen naast elkaar weergeeft.
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code mod that lets Claude log unfinished work to Docs/todos.md, with a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods voor Claude Code: Clawd, een kleine pixelmascotte die uitbeeldt wat Claude…
- [reporails/arcade](https://github.com/reporails/arcade) - Klassieke desktopgames als Claude Code-mods, gespeeld in een paneel terwijl…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Een samengestelde lijst van Claude Code-mods, installeerbaar als…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code-mods die een agent eerlijk houden — function hooks die de scope…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Mijn verzameling Claude Code-mods, één mod per map.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Vijf gratis Claude Code-mods: Simple Mode, Usage Tally, Context Handoff, Inbox…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code-mods: contextbalk, agentenpaneel, PDPA-vervaging.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Vers uit de fabriek. Een Claude Code-mod: vraag om een meme en blijf…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod voor Claude Code: balk voor promptcache, volgende stappen, snelknoppen en…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Een Claude Code-mod die je gebruikslimieten en uitgaven weergeeft in de balk…
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - De skill-router-mod: Jev kiest en laadt de vaardigheden die elke prompt nodig…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Een appstore voor Claude Code-mods binnen Claude Code: gebruik /mods om 2.700…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code-mods: voortgangsbalken voor plannen, een overzicht van wat Claude…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Claude Code-mods voor dagelijks UX-gebruik: planlimieten, context en wat de…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code-mods door MacLeod Labs: streams ontwart het door elkaar lopende…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Eerste-dag veldnotities over Claude Code-mods op Windows: een…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods die ik heb gemaakt en persoonlijk gebruik in mijn Claude Code-configuratie.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-mod: live kosten-, context- en planquotameters boven de prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Een Claude Code-mod die fan-out van subagents, prompts met zware context en…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods voor claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Een Claude Code-mod die je globale skills, agents, regels en tools per repo met…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods voor Claude Code: plug-ins gebouwd op functiehooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Filmachtige aftiteling voor je codeersessie.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Een aantal claude code-mods die ik heb gebouwd.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Een door cliamp aangedreven YouTube-speler in Claude Code (Claude Code-mod).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code-mods: dashboard en autopilot voor agentvloot.
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude Code-mods van vynnlee. Eén map per mod, installeerbaar vanuit één…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Leer een vreemde taal terwijl je met Claude Code werkt.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Past een lange Claude Code-sessie op zodat jij dat niet hoeft te doen: houdt in…
- [akerskuuug/claude-mods](https://github.com/akerskuuug/claude-mods) - Claude Code-mod: gebruik, limieten, branch en model rond de prompt.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Thematische antwoorden, diagrammen over de volledige breedte en je context en…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Wanneer een agent Java schrijft, kan code die het Alibaba-voorschrift Java…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Zijbalk met live kosten-, token- en contextgebruik voor Claude Code: een mod…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code mod: a backlog of the follow-ups Claude suggests across every…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Counter-Strike 1.6-radiomeldingen voor Claude Code - &#x27;Fire in the hole&#x27; bij…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internet radio inside Claude Code: a cliamp sidebar, mini player, favorites…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: een Claude Code-mod voor het ontwerpen en uitvoeren van grafieken…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Herdr-configuratie + Claude Code-mods voor productontwikkeling.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS-dashboard in notch-stijl voor Claude Code: gebruikslimieten, open…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude is aan het koken. Chat met je squad.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Een Claude Code-mod: vang pixelart-Modsters in een inactief spel terwijl Claude…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Een ruimtegevecht boven de prompt van Claude Code terwijl het werkt.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zie welke bestanden elke Claude Code-agent in zijn context heeft, en hoeveel…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Houd je hoofd koel. Een thermometer voor je Claude Code-dagen: elk uur krijgt…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-mods voor de terminal en de desktopapp.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-skill + mod die Spaanse woorden toevoegt aan agent-antwoorden.
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Claude Mods.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Een Claude Code-mod die het herstijlt als The Machine uit Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Claude Code-mod: comprimeert op het juiste moment.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code-mod voor verplichte, geverifieerde DAG-workflows van…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Een pixel-art Naruto-metgezel voor Claude Code: 20 ninja.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-sourcemods voor Claude Code: deelvensters, statusregels, toastmeldingen…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Een Claude Code-mod: één deelvenster per subagent, de bestanden die ze aanraken…
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Een communitydirectory van Claude Code-mods, plug-ins, skills, agents, hooks en…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code-mod: sessiestatus, live Spec Kit-voortgang en beheer van…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Het contextvenster als een rij boven de prompt, weergegeven zoals Claude Code…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code-plugin (mod) die de terminalinterface van Claude Code eruit laat…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Bekijk wat Claude Code op de achtergrond uitvoert: subagents, Codex-taken…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - A free, open-source plugin for Claude Code.
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - Persoonlijke Claude Code-mods: otto-hud, Otto de octopus met…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Een Claude-mod die de GitHub pullrequests van de sessie weergeeft in een paneel…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: een debugger voor toolaanroepen van Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-vaardigheden: een factchecker voor documentatie, een code-auditor…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-buddyplugin: een ASCII-metgezel boven je prompt die je regels…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code-plugin voor toolzichtbaarheid per agent — verberg en weiger…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code-mod: door Jev aangestuurde model-/effortroutering…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code-mods: beveiligingslaag voor Claude Code — redactie van geheimen…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Een verzameling Claude Code-mods.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-plugin en -mod: een AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Verzameling geweldige Claude Code-mods | verzameling Claude Code-mods.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code-plugins (mods): wissel tussen meerdere Claude-accounts, bekijk…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Geteste Claude Code-mods die je met één opdracht installeert: guardrails voor…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: een Claude Code-mod die de antwoorden van Claude en je prompts op…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Laat je Claude Code-gebruik tot twee keer zo lang meegaan.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code-mods: kleine plugins voor livepanelen, kostenbewuste modelroutering…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code-mod &amp; plugin: gebruiksmonitor, tokentracker &amp; statusline.
- [Verinoda-Labs/verinoda-symbiosis](https://github.com/Verinoda-Labs/verinoda-symbiosis) - Verinoda + Claude Code, samen: Verinoda met verinoda-live, een Claude Code-mod…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Een Claude Code-mod die de kleine beslissingen overlaat aan een goedkoop…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Three free Claude Code mods: hide .env values from tool results, watch a remote…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code-mods. touch-map: zie welke bestanden Claude heeft opgesomd…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Een Claude Code-mod die de agentberichten die je nog niet hebt gelezen samenvat…
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mods for Claude Code: live panes, bands and hooks. A plugin marketplace.
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [0xnicholasy/claude-mod-collapse-tools](https://github.com/0xnicholasy/claude-mod-collapse-tools) - Claude Code mod: collapses every tool-call row in the transcript to one line;
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Claude Code plugin marketplace for 0xnicholasy.
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code-mods + cheap-executor-driver: één Claude-sessie als lead, MiniMax…
- [AdamCaviness/cache-magic](https://github.com/AdamCaviness/cache-magic) - Claude Code mod that auto writes a handoff before a large session.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code-mods van afterever (plug-inmarkt).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Een geanimeerde braillekat boven de Claude Code-prompt.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code-mod: stuur goedkoop werk via een onderliggend Claude Code naar…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Een pixelkat boven je Claude Code-prompt die een testgesprek met een…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Een Claude Code-mod die een goed moment kiest om te verdichten, zodat het…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods voor Claude Code: tokenmeter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code-pluginmarktplaats van anderson-spider.
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mods for Claude Code.
- [ankits3a/cache-keeper](https://github.com/ankits3a/cache-keeper) - Claude Code-mod: prompt-cacheband, keep-warm, handoff-beoordelingsproef.
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Het LGTM Lines-schip vaart na elke codewijziging voorbij — een Claude Code-mod.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Je Claude-gebruikslimieten als een geanimeerde gezondheidskaart van een…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code-mods voor het S2-team (de ather-marktplaats).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - Een Claude Code-mod die Claude gewoon Engels laat schrijven en de gebruikelijke…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Korte workouts terwijl Claude werkt: een dagelijks doel, streaks, badges en…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Een gebruiksoverzicht voor Claude Code: uitgaven per model.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - A Claude Code mod: live context-window breakdown above the prompt.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code-mod die het aftellen van de promptcache in de voettekst toont en de…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now Playing-mod voor Claude Code: Apple Music en Spotify boven de prompt, met…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Vijf Claude Code-mods om veel sessies tegelijk uit te voeren: vlootbord…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Claude Code mod pack from the Berko video: Mask, View, Guard, Saving, Chime +…
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Claude Code-mods: gebruiksbalk, chatroster, /cube, /handoff, promptopschoning.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods voor Claude Code: Cache-klok, Blast Radius, suggesties, werklijst, Grill.
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code-mods: Suggestion Spotlight laat zien waar de voorgestelde volgende…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Gewoon een uil voor je Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Eénregelige Claude Code-band.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - De originele Doom-engine met Freedoom, speelbaar binnen Claude Code.
- [cmorss/claude-mods](https://github.com/cmorss/claude-mods) - Claude Code-mods voor git-worktrees: /terminal en /worktree-files openen een…
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Een Tamagotchi die in Claude Code leeft: hij komt uit, eet de code die Claude…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bladwijzers en vim-achtige markeringen in Claude Code-terminalgesprekken…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code-mod: SwiftUI-previews weergegeven door Xcode, getoond in een…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Maak van elke Claude Code-sessie een klein avontuur: generatieve muziek die de…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code-mod: toont de tijd bij elke prompt en elk antwoord in de terminal…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Claude Code-mods geschreven als functiehooks, en de marktplaats die ze…
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code-mods en ontwerpsystemen: crab-crew en het Crab Crew-ontwerpsysteem.
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - My Claude Code mods, shared as a plugin marketplace.
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - divramod.
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - De Claude Code-mods die ik op elke machine gebruik: savvy-progress, filetree…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code mod: after a guard blocks a tool call, it stops recognized detours…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code mod: one inbox for messages from teammates, named subagents and…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code mod: explains sandbox blocks and turns repeated blocks into…
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hé, gedempt! Weg met de diff, schrap de riff, geen wijzigingen meer, minder…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude Code-mod: abonnementsgebruik (5u / 7d) als een balk boven de prompt in…
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Motion-ontworpen mods voor Claude Code: een live, responsieve monitor voor…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod-marktplaats.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Een live radar van je parallelle branches en worktrees boven de prompt: welke…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - Mijn Claude Code-mods.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods en skins voor Claude Code: een live voortgangsbalk voor de taken van…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Seven Claude Code mods: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+klik om een link te kopiëren op elk codeblok in Claude Code-antwoorden…
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - De jev-mod: $.jev voor Claude Code, getypeerde oordelen van TypeSafe Jev.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Claude Code-mod: paneel dat toont of de promptcache warm of koud is.
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mods voor Claude Code: plugins met hooks, zoals usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code-mods (functie-hookplugins), geïnstalleerd via één marketplace.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Evangelion-achtige zijbalk voor Claude Code: context, quotum, activiteit, PR.
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Nuttige claude code-mods.
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Met de Claude-Code-plug-in (mod) kun je zien wat het model doet terwijl het…
- [hamTotk/better-rewind](https://github.com/hamTotk/better-rewind) - Claude Code mod: rewind or summarize from any prompt or AskUserQuestion answer.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Testresultaten in een Claude Code-paneel: fouten, details daarvan en…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-mod: hoe lang elk antwoord duurde, hoe lang Claude nadacht en…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Kleine Claude Code-mods: meters voor context- en planverbruik, een…
- [Jang-seungminn/usage-hud](https://github.com/Jang-seungminn/usage-hud) - Claude Code mod: usage HUD above the prompt with two animated ASCII dogs.
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Een plek om mijn claude-mods te huisvesten.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Zijpaneel met contextgebruik: totaal, categorieën, groei per beurt, de grootste…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Zijpaneel met bestandenlijst: welke bestanden tijdens dit gesprek zijn…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Een pluizige 8-bit 毛毛 (zwart-wit Nederlandse hangoor) rent en springt boven het…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Zijpaneel met ‘wat ik heb gevraagd’: elke zin die de gebruiker tijdens dit…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Zijpaneel met tijdlijn: waar de tijd van deze beurt aan is besteed.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Zijpaneel met tokenverkeer: hoeveel tokens het hoofdgesprek elke keer naar…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - De eerlijke bonenpasta van claude code: na elke beurt zegt Claude zachtjes één…
- [jgilb17/claude-mods](https://github.com/jgilb17/claude-mods)
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Bewijsafhankelijke planchecklist voor Claude Code: goedgekeurde plannen worden…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Kleine mods voor Claude Code, zoals nieuwe slashopdrachten en zijpanelen.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catalogus van mods voor Claude Code.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Multiplayergames om binnen Claude Code te spelen terwijl het werkt.
- [juliomyitbrain/claude-code-git-graph](https://github.com/juliomyitbrain/claude-code-git-graph) - Claude Code-mod: een deelvenster dat de commitgrafiek van de repository tekent…
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Claude Code-mod: houdt de promptcache warm terwijl je weg bent en vraagt…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd leeft in een band boven je Claude Code-prompt: speelt de sessie na, toont…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - Een Claude Code-mod die de rate-limit-ruimte, sessietokens en kosten boven de…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Een mod die antwoorden en meldingen van Claude Code voorleest met VOICEVOX /…
- [Kareem1809/chat-cigarette](https://github.com/Kareem1809/chat-cigarette) - 🚬 A Claude Code mod: a cigarette burns down with every message — when it.
- [KashifManzer/clear-caption](https://github.com/KashifManzer/clear-caption) - A Claude Code mod that adds plain-language captions and state markers to tool…
- [kba977/claude-code-pomodoro](https://github.com/kba977/claude-code-pomodoro) - A pomodoro timer above the Claude Code prompt (Claude Code mod).
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Een Claude-mod om de gesprekken tussen je Claude Code-sessies te lezen en eraan…
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Claude mods voor extra.
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - vermoeide claude code-sessies met haiku comprimeren — cachebalk van één regel…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Twee Claude Code-mods: folio, een bestandsdeelvenster naast de chat, en tint…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Een live taak-HUD voor Claude Code Desktop: een strook boven de prompt terwijl…
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [loucimj/turn-chime](https://github.com/loucimj/turn-chime) - Claude Code mod: chime after 40s turns, spoken announcement after 5-minute turns.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Een door de community samengestelde Claude Code Mods-gids: gebruiksscenario.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Een Claude Code-mod die laat zien wat Claude doet in de ondertitel van het…
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Claude Code-mod: spoort de hoofdsessie aan om te delegeren aan subagents en…
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - Mijn persoonlijke verzameling claude-modplug-ins.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - De Claude Code-mods van Marcel in één plug-inmarkt (marcel-mods).
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Een Claude Code-mod met verwisselbare toestemmingsprofielen: een veilige basis…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community-mods voor Claude Code: bewaking, deelvensters en opdrachten die…
- [mina-asham/claude-usage-stats](https://github.com/mina-asham/claude-usage-stats) - A Claude Code mod that shows your plan usage.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Een rustig zijpaneel voor Claude Code: wat deze sessie doet, het plan, de…
- [mmedum/spor](https://github.com/mmedum/spor) - Zet terug wat Claude Code wegvouwt: de bestanden die Claude las, de opdrachten…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-mod die de todo-tools weer inschakelt voor modellen die ze…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-mod: één regel per taak in de takenlijst boven de prompt, met de…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Speel Vier op een rij tegen een AI binnen Claude Code (/connect-four).
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Een pixel-artkanarie voor Claude Code: hij sterft wanneer Claude je instructies…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code-mod: wanneer een andere code-agent een commit naar je repo maakt…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code-mod voor repo.
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Een cyber-neon-internetradiopaneel voor Claude Code - synthwave-draaiknop, nu…
- [niksavis/handily](https://github.com/niksavis/handily) - Claude Code-mods die je werkitems, taken en sessies tonen, voor elke tracker.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Een beveiliging voor SQL in Claude Code: vraagt voordat Claude via een DB CLI…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Eén mod voor Claude Code, Windows en CJK als uitgangspunt: voorbeelden van…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime voor Claude Code: een geluid wanneer Claude klaar is, je invoer nodig…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code-mods: miniaturen van afbeeldingen en de statusregel.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - De beste Claude Code-mods, gesorteerd op wat ze voor je doen.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Claude Code-mod: bekijk elke afbeelding en elk bestand waar je agent naar heeft…
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Een Claude Code-mod die risicovolle shellopdrachten.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Twee Claude Mods voor Claude Code: garde-du-corps.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Lazy Panda Panel voor Claude Code: bekijk documenten zonder een poot uit te…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Swear at Claude Code and a cartoon hand slaps back.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code mods: usage-both shows 5-hour and weekly usage above the prompt.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live zijpaneel met sessiestatistieken voor het Code-tabblad van de…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Diverse mods en vaardigheden voor mijn Claude Desktop-configuratie.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods voor Claude Code: safety-guard blokkeert destructieve opdrachten en…
- [prompteafacil-hub/mods-claude-code](https://github.com/prompteafacil-hub/mods-claude-code) - Mods voor Claude Code van de prompteafacil-community.
- [ptpmediabr/ideas-shelf](https://github.com/ptpmediabr/ideas-shelf) - Plank met ideeën per project: noteer ideeën op een bord en markeer ze als…
- [ptpmediabr/mods-manager](https://github.com/ptpmediabr/mods-manager) - Dashboard om je mods en plugins te bekijken, in en uit te schakelen, te…
- [ptpmediabr/side-chat](https://github.com/ptpmediabr/side-chat) - Een zijchatvenster binnen de sessie dat vragen beantwoordt of verzoeken…
- [ptpmediabr/usage-weather](https://github.com/ptpmediabr/usage-weather) - Eén rustige regel boven de prompt: context, gebruik over 5 uur en per week, of…
- [qarge/claude-mods](https://github.com/qarge/claude-mods)
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code-mod: live-aandelenkoers, /quote-paneel, prijswaarschuwingen…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code-mod: SSH-host, RAM en gebruikslimieten voor 5 uur/7 dagen in een…
- [Rinze-Smits/ifc-viewer-claude-mod](https://github.com/Rinze-Smits/ifc-viewer-claude-mod) - IFC Viewer mod for Claude Code.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-mod: push-ups om te doen terwijl Claude werkt. Geen tokens.
- [Rsclub22/claude-mods](https://github.com/Rsclub22/claude-mods)
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - A Claude Code mod that routes tasks to other AI models.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - De modwinkel voor Claude Code: haalt mods op van GitHub, geeft voorbeelden en…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-mod: verandert het plan dat je in planmodus goedkeurt in een live…
- [sadhirr1/claude-mods](https://github.com/sadhirr1/claude-mods) - Gewoon een repo met verschillende claude-mods.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Een zorgvuldig geselecteerde lijst van Claude Code-mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenvrije modus: helperagents draaien op Haiku, en grote bestanden en logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Een lofi-soundtrack die de sessie volgt: kalmte, focus, flow, plus signalen…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Leer terwijl Claude codeert: na een beurt die de code heeft gewijzigd…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Een bandopname van elke bewerking die Claude maakt: speel elke wijziging af…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Elke link die je sessie vermeldt, op één regel boven de prompt.
- [SanjayPG/claude-code-usage-tracker](https://github.com/SanjayPG/claude-code-usage-tracker) - Claude Code-mod: live voortgangsbalken voor het gebruiksquotum boven je prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code-functie-hooks minimaal demonstratie: een live token-/kostenpaneel…
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - Claude Code-mods (plugins met functiehooks) door ShellTime.
- [siller/supermod](https://github.com/siller/supermod) - Claude Code-mod: voortgang van Superpowers, contextvenster en agents boven de…
- [skryvets/claude-status-bar-mod](https://github.com/skryvets/claude-status-bar-mod) - Claude Code-mod: gekleurde sessie-informatie onder de prompt — context…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Een gezellige RPG-HUD-mod voor Claude Code.
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Persoonlijke Claude Code-modmarketplace: clean-view, where-am-i, next-steps…
- [Steady-Matter/spotter-pals](https://github.com/Steady-Matter/spotter-pals) - Spotter: a Claude Code mod with pixel Pals that hatch and grow as your helper…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commitberichten met één klik voor Claude Code met een dansende pixel-art Malenia.
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude-codemods.
- [stylusnexus/claude-mods](https://github.com/stylusnexus/claude-mods)
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Personal Claude Code mods.
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code-mods — marketplace sunkanxx-mods.
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Claude Code-mods: mini-bar-HUD.
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugins voor Claude Code.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Mods voor Claude Code: delete-guard.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Claude Code-mod: bekijk het gebruik van je Claude-plan.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code-mod: live teamvenster voor elke subagent.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - Een Claude Code-mod die voor elk soort werk het model en de inspanning kiest en…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Een Claude Code-mod die de huidige sessie in een paneel toont: elke prompt, het…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Een Claude Code-plugin-marketplace met mods: function-hooks-plugins die banden…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code mods on demand — a skill that reads your conversation and builds…
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code-mod: een vastgezet paneel met de subagents van de sessie en hun…
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Claude Code mod that writes your Claude usage limits to a file other tools can…
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Claude Code-mod: een balk en een paneel die je subagents volgen, samen met de…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Een samengestelde catalogus van Claude Code-mods, elk met een prompt die je…
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code-mods van Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code-mod: geanimeerde voortgangsbalk en voltooiingssamenvatting voor…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drie kleine Claude Code-mods: zie wanneer je subagents klaar zijn, zet…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Zeg &quot;Ik ben de draad kwijt&quot; en Claude legt het vorige antwoord opnieuw uit in…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stel Claude een zijvraag in een venster naast je werk.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace van mods voor Claude Code met installatie in één stap en een…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Aftellingen voor snelheidslimieten en een prognose van het verbruikstempo voor…
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Veiligheidslaag voor Roblox Studio voor Claude Code: RemoteEvent-audit…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Kleine kwaliteitsverbeterende mods voor Claude Code.
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Claude Code-mods: stage-toons, een voortgangsbalk voor de workflow boven de…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods voor Claude Code. agent-crew: zie je subagents werken als een live…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - A live task board for Claude Code: plan before building, follow every task…
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Claude Code-mods: capsule voor de volgende stap in 繁中, blokken kopiëren…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Altijd zichtbare balk boven de Claude Code-prompt: contextvulling en…
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - Persoonlijke Claude Code-mods (pluginmarketplace).
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Een zorgvuldig samengestelde verzameling van de beste hulpmiddelen voor de…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Een Claude Code-plugin die toont wat er gebeurt — contextgebruik, actieve…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Mooie, zeer aanpasbare statusregel voor Claude Code CLI met…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle onderdelen van de systeemprompt van Claude Code, 27 ingebouwde…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Meer dan 45 tips om het meeste uit Claude Code te halen, van basis tot…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — genereer Xiaohongshu-carrousels en…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Mooie vim-stijl-powerline voor Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Bekijk de diff van je codeeragent in een terminalvenster en stuur…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Uitgebreide statusregelplugin voor Claude Code met contextgebruik…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code &amp; Codex lokale token-tracking — statusbalk.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Bouw mods voor Claude Code: haak elk verzoek aan, wijzig elk antwoord, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Een uitgebreid statuslijndashboard voor Claude Code — sessie-informatie…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: volg de ecologische voetafdruk van je Claude Code-sessies.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Een esthetische statusregel voor Claude Code van awesomejun.
- [amirfish1/claude-command-center](https://github.com/amirfish1/claude-command-center) - One local board for Claude Code, Codex, Cursor and 5 more coding agents.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Openbare Claude Code-vaardigheden en -mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash-opdrachten en handleidingen voor Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legale gratis LLM APIs en codeeragents — zichzelf twee keer per week…
- [398894496-arch/DSH-KRouter](https://github.com/398894496-arch/DSH-KRouter) - Second brain for coding agents. Seal the day, distill into Obsidian, merge…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Terminal-statusline voor Claude Code-sessies.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live voetbalstanden, wedstrijden en ranglijsten voor de competitie die je…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Local control plane for Claude Code on Windows and macOS: switch LLM gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill die je codeeragent verandert in een expert in toetsenbordfirmware.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Persoonlijke configuratie van Claude Code, met versiebeheer binnen ~/.claude…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebedstijden, Hijri-datum, adhkar, dagelijkse ayah, sunnah-vasten, Ramadan…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Sessiegevoelige statusregel voor Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness-plug-in voor onderzoeksonderwerpen…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Draagbare Claude Code-toolkit voor .NET DDD/Clean Architecture: strikte…
- [saadnvd1/agent-os](https://github.com/saadnvd1/agent-os) - Mobile-first web UI for managing AI coding sessions.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Pluginbundel voor Claude Code, pi en DeepSeek Harness: HUD voor de statusbalk…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Draagbare globale configuratie voor Claude Code: aangepaste skills…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-plug-ins die ik elke dag gebruik: skills en mods, opgeschoond zodat…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram in Claude Code: lees chats en kanalen in een paneel en krijg…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark)-bridge, zelf ontwikkeld (geen fork)…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marktplaats voor Claude Code-plug-ins en skills om mods voor het spel Hytale…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tokenbeheer voor Claude Code: het topmodel stuurt aan, de uitvoering gaat naar…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Viewer met gesplitst venster voor Claude Code in Windows Terminal en tmux: de…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live statusregel voor workflowfasen voor Claude Code.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Onofficiële mods voor het tabblad Code van Claude Desktop — usage-pet: een…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository voor Awesome Media-mods van Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Verlaag de tokenuitgaven van Claude Code &amp; Codex: stuur opzoekingen en testruns…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Simple and useful status line setup for Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Meldingen over gebruikslimieten voor Claude Code: macOS-meldingen…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configureerbare Claude Code-statusregel voor Linux, WSL, Windows en macOS, met…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Snelle Rust-statusregel voor Claude Code — payload eerst, gecachte git…
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Claude Code-statusregel met contextbalk, token-sparkline en kostentracker.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Een live gebruiksdashboard voor Claude Code — contextverdeling, cachehits…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Een statusregel en tokenregel voor Claude Code: context, gebruik van 5 uur en…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Toon belangrijke statusdetails voor Claude Code, waaronder model, context…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - de vriendelijke statusregel voor Claude Code waarmee je alles kunt aanpassen…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Statusregel met meerdere rijen voor Claude Code: verbruik, context-%, git en…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusregel met nuttige informatie voor claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Startertemplate voor het organiseren van een Claude Code-werkruimte voor…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agentteams. Onder controle. Strikte werkerslimieten, live…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definieerbare softwarefabrieken voor Claude Code op herdr…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Aangepaste statusregel voor Claude Code — contextbalk met gebruikspercentage…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - A clean, informative status line for Claude Code — shows project, git status…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code-pluginmarktplaats met baloo: vaardigheden, een agent die…
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Claude Code-statusregel: contextgebruik, quotumbalken voor 5 uur/7 dagen…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionele Claude Code-statusregel: sessieduur, kosten in meerdere valuta…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Abonnementsbewuste statusregel voor Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Een uitgebreide terminalstatusregel voor Claude Code — Bun + TypeScript, zonder…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Statusregel met twee rijen voor Claude Code: context, snelheidslimieten met…
- [eddywong888/claude-castle-mod](https://github.com/eddywong888/claude-castle-mod) - A Castlevania-style usage HUD mod for Claude Code: context blood meter…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Claude Code-plugin die Mermaid-diagrammen prachtig in het transcript weergeeft…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, vaardigheden en agents voor Claude Code — te beginnen met een…
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Globale configuratie voor Claude Code: agents, skills, mods, instellingen.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Claude Code-plugin: zie altijd je resterende Claude-limiet voor 5 uur…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Echte DeepSeek-API-uitgaven voor Claude Code: herprijst sessietranscripten…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods para Claude Code y Claude Desktop en Windows con WSL: Docker y rendimiento…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code-statusregel met rijen voor het agentenpaneel.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchroniseer de taken van Claude met Fizzy.do voor realtime inzicht voor het…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Toon een gedetailleerde, van kleur voorziene statusbalk voor Claude Code met…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Instellingenmenu, statusregel en configuratie voor Claude Code.
- [Larg0Winch/claude-label](https://github.com/Larg0Winch/claude-label) - Bewerkbaar label per venster in de statusregel van Claude Code.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Praat met Claude Code via je stem op Windows: een Mod + helper die codex…
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Aangepaste Claude Code-statusregel met contextvenster, tracking van…
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - Snelle Rust-statusregel voor Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - zelfgemaakte, kooivrije claude-plugins, skills, mods en meer.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code-omgevingsinstallatieprogramma: skills, statusregel, hooks…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude Code-plugins en mods om te begrijpen wat Claude doet: leesbare…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitor de status van Claude Code vanuit je macOS-menubalk met…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Kleurrijke statusbalk met meerdere rijen voor Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code-statusregel voor Windows (PowerShell): gebruiksbalken, afteltimers…
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Claude Code-plug-ins. Usage Bars toont je sessie- en wekelijkse…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Bearings- en Glossary-mod voor Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Aangepaste Claude Code-statusregel (upstream: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code-configuratie en mods, met een gedeelde componentenkit, een…
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Een klein dashboard voor Claude Code: contextpercentage, cache-afteltimer…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Draagbare Claude Code-configuratie: CLAUDE.md, instellingen, statusline, skills.
- [tichara1/ai.claude-status-panel](https://github.com/tichara1/ai.claude-status-panel) - Mod voor Claude Code: paneel boven de prompt met context, limieten, kosten…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Volg het contextgebruik van Claude Code, sessiekosten en resets van…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Mod-verzameling voor Claude Code.
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Realtime kostenregistratie en statusregel voor sessiemonitoring voor Claude Code.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Cordis / DeepSeek Harness-plug-in — de agent vraagt de mens om een geheim in…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Statusregel met drie regels voor Claude Code: contextdiepte, snelheidslimieten…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Proactieve AI-geheugen- en snelheidslimietmonitor…
- [zerofaultlabs/claude-statusline](https://github.com/zerofaultlabs/claude-statusline) - Een Claude Code-statusregel: contextgebruik, snelheidslimieten, kosten en…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-hooks, subagents en statuslines: opensourceverzamelingen en -tools…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Claude Code-statusregel — live blijvende Claude/Codex-gebruikmeters terwijl je…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Een visuele builder voor statusregels van Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code-statusregel die realtime tokengebruik en geschat energieverbruik…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods voor Claude Code: deelvensters, banden en buddies, gebouwd op function…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Geef taken door tussen je Claude Code-sessies.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Dit in een MCP-server om MODS te besturen, de modulaire platformonafhankelijke…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex- en Claude Code-skill voor het vertalen van CK3-mods met een lokale LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods en andere uitbreidingen voor Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: vind wat je Claude Code steeds opnieuw vraagt en maak er een mod…

</details>

<a id="dsh-cordis"></a>

## DSH- en Cordis-plug-inecosystemen

DeepSeek Harness en Cordis bereiken dezelfde plek vanuit een andere richting: voor hen is de plug-in het modmechanisme, dus een plug-in daar is het equivalent van een mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74290 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

🌊 De oorspronkelijke agent harness. Implementeer intelligente swarms met meerdere spelers, coördineer autonome workflows en bouw conversationele AI-systemen. Met adaptief geheugen, zelflerende intelligentie, federatie, vectorintegratie van RAG en native Claude Code / Codex / Hermes en vele andere geïntegreerde systemen

<sub>🔧 Gebruik in code gevonden: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                               |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74290**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100412 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

🎨 Beste DeepSeek Harness Design Plugin. Het open-source alternatief voor Claude Design. 🖥️ Desktopapplicatie met lokale prioriteit. 🖼️ Je coding-agent wordt de designengine: prototypes, landingspagina's, dashboards, dia's, afbeeldingen en video — echte bestanden, export naar HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode en meer dan 20 CLI's via BYOK.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **100412** |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81684 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Zet elk idee, plan of codebase om in een prachtig interactief diagram. Een agentvaardigheid voor Claude Code, Codex en meer.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **81684**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐73982 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Reverse-engineer alles met agents, van appgedrag tot native binaries.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **73982**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35761 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Een betrouwbare codeeragent voor complexe software-engineeringtaken.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Go                                                                               |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **35761**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30367 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Een moderne desktopoplossing voor het DeepSeek Harness (DSH)-plug-in-ecosysteem. Alles is een «plug-in», en de desktop zelf is ook een «plug-in».

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30367**  |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25472 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Summary

Distilly — destilleer hoe zij denken tot herbruikbare Skills voor elke Agent of Bot. Voorheen Colleague Skill（原同事 Skill）.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25472**  |
| Last push    | 2026-09-22 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9113 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Meta-framework voor spatiotemporele composabiliteit

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9113**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8596 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) Web-pluginaggregatie-ecosysteem · Alles is een plugin, verspreid via de Creative Workshop｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8596**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4268 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH's officieel meest aanbevolen TUI-plug-in — hoge prestaties, laag verbruik, schattige pixelwalvis en vloeiende muisinteractie. Installatie met één opdracht via npm. / DSH's officieel aanbevolen TUI-plug-in: hoge prestaties, laag verbruik, schattige pixelwalvis, vloeiende muisinteractie en installatie met één klik via npm

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4268**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The World's First Virtual Terminal for AI Agents

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3682**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3409 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3409**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1462 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1462**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1168 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Geheugen voor Claude Code, Codex, Cursor en 38 andere codeeragents, opgebouwd uit de sessiegeschiedenis die al op je schijf staat. Lokale zoekfunctie, MCP en hooks, geen LLM, één Go-binary.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Go                                                                               |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1168**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1009 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

De meest uitgebreide DeepSeek Harness-pluginmarkt — dagelijks vernieuwd, afkomstig van het internet en vóór publicatie beoordeeld.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1009**   |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐702 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (dsh) Windows-desktopclient - Node.js + dsh CLI gebundeld, starten met één klik

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **702**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Your Intelligence, Orchestrated. Every builder. Every team. Every agent. For Everyone.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Go                                                                               |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **351**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐282 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Just open your browser — get all your work done.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **282**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **255**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐248 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Officiële DSH (DeepSeek Harness)-plugin: gebruik webmodellen van chat.deepseek.com als LLM-provider — vastleggen van browserlogin, PoW-oplossing, SSE-streaming en op prompting gebaseerde toolaanroepen.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **248**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-trading">zhu1090093659/dsh-trading</a></b> · ⭐238 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Agent-native trading terminal built on DeepSeek Harness. Crypto, US, CN and HK in one three-column GUI, 19+ hot-swappable connectors, dry-run by default with human approval on every live order. BYOK, no data redistribution.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **238**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-native` · `ai-agent` · `cryptocurrency` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `trading-terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhu1090093659/dsh-trading/main/docs/banners/banner-en.jpg" width="100%" alt="zhu1090093659/dsh-trading screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Native DeepSeek Harness (DSH)-plugin die TypeSafe Jev of Decision api zoals luna integreert als System One-beslissingslaag voor agentselectie, supervisie, correcties en goedkeuringen.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **203**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness-plugin voor previewbare sessiemigratie tussen presets. Overdrachten met een vast schema behouden de status, de intentie van het bronmodel en onopgeloste afbeeldingen; de oorspronkelijke sessie blijft onaangeroerd.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **165**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/2BingLing/dsh-market">2BingLing/dsh-market</a></b> · ⭐138 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 插件市场 · 持续收录 6000+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 6000+ plugins, Chinese search, 5-dim scoring, one-click install.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **138**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `deepseek-harness` · `deepseek-harness-plugin` · `deepseek-harness-plugins` · `dsh` · `dsh-bundle` · `dsh-market` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/banner.webp" width="100%" alt="2BingLing/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mexiaosqwq/dsh-web-mobile">mexiaosqwq/dsh-web-mobile</a></b> · ⭐130 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH Web UI 移动端适配：窄屏好用，宽屏适用

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **130**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-ui` · `plugin` · `responsive` · `web-ui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mexiaosqwq--dsh-web-mobile/0edd0e3313404adf.jpg" width="100%" alt="mexiaosqwq/dsh-web-mobile screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐127 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Claude Code-desktopthema voor DeepSeek Harness｜ Claude Code-desktopthema ontworpen voor de web-GUI van DeepSeek Harness

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **127**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐119 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Runtime-bewijs waarmee agents hotspots in applicatie- en native code, GPU-kernels en inferentiestacks kunnen traceren, profileren en wegwerken.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **119**    |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dickpy/dsh-imagegen">dickpy/dsh-imagegen</a></b> · ⭐103 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH (DeepSeek Harness) Web GUI AI image generation plugin: text-to-image & image-to-image via OpenAI-compatible endpoints (gpt-image-2), with shared cross-device history.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **103**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dickpy--dsh-imagegen/5859c3cebcc07298.png" width="100%" alt="dickpy/dsh-imagegen screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐85 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

StudyHub: een DeepSeek Harness-plug-in (DSH) die je eigen materiaal omzet in vragen en gespreide herhaling · DSH-studieplug-in die je eigen materiaal omzet in vragen en gespreide herhaling

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **85**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐75 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness（dsh web）op afstand bedienen via het openbare internet: na installatie krijg je een exclusief versleuteld adres en kun je ook buitenshuis vanaf je telefoon op afstand toegang krijgen, zonder hetzelfde LAN/WiFi en zonder NAT-traversal; zelf hosten is optioneel. DeepSeek Harness (dsh web) overal op afstand bedienen — versleutelde openbare URL, geen LAN vereist.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **75**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-web` · `pwa`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://cdn.jsdelivr.net/gh/mrRisega/dsh-remote@main/image/phone-mirror.png" width="100%" alt="mrRisega/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐73 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

dsh-sieve: contextengineering- en tokenoptimalisatieplugin voor DeepSeek Harness (DSH) — filtering van tooluitvoer, context­snoeiing, progressieve bekendmaking van vaardigheden. 36% kleinere payload bij offline afspelen. DSH-plugin voor contextbeheer en tokenoptimalisatie.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **73**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Marktplaats die communityplug-ins van DeepSeek-Harness automatisch classificeert, selecteert en valideert. Classificeert, selecteert en valideert automatisch de communityplug-insmarktplaats van DeepSeek-Harness.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **69**     |
| Last push    | 2026-10-10 |
| First listed | 2026-10-10 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐57 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Summary

De voortdurend bijgewerkte DeepSeek Harness-plugincatalogus — elk uur vernieuwd, dagelijks op compatibiliteit getest, met een ingebouwde pluginstore en scaffolder. DSH-plugincatalogus: elk uur vernieuwd, dagelijks op compatibiliteit getest, met ingebouwde pluginstore en scaffolder.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | HTML                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **57**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体。纯本地、零模型调用、零网络。  Task-aware workspace context retrieval and lifecycle tracking for AI coding agents. Find, organize, and track the workspace context most relevant to the task at hand — locally, deterministically, zero model calls, zero network.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **53**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 77</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Een guard vóór uitvoering voor AI-codeeragents.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Een samengestelde lijst met de beste geweldige AI-plugins voor AI-assistenten…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - Vind in 30 seconden de DeepSeek Harness-plugin die echt bij je past.
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-pluginmarkt / DSH Plugin Marketplace: blader, installeer en update alle…
- [arcships/rutis](https://github.com/arcships/rutis) - Een plugin-runtime voor programma.
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Community voor DeepSeek Harness-plug-ins — automatische synchronisatie van…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Beste Roblox Luau-bugchecker en API-verifier 2026 DevForum MCP-tool.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Uitgelichte directory van DeepSeek Harness (DSH)-plugins — meer dan 280…
- [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) - 【求⭐】🐋DSH Web UI…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zotero-toolkit voor DeepSeek harness; maak van je Zotero-bibliotheek een…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH-plugin: Git Bash-shell voor alle agentmodi op Windows.
- [jingyi0605/Codingns4DSH](https://github.com/jingyi0605/Codingns4DSH) - 把外部 Agent CLI、持久终端、工作区调试和远程访问，装进 DSH 原生界面.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: een multiplatform-groepschatagentsysteem op basis van DeepSeek…
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web plugin: per-day token usage statistics with a GitHub-style activity…
- [JustGenius-s/DSH-Desktop](https://github.com/JustGenius-s/DSH-Desktop) - DSH-Desktop.
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Lokale schrijfwerkplek voor Chinese webromanschrijvers (19 tools): verzamel…
- [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) - Appearance customization plugin for DeepSeek Harness: theme color palette…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - Transparante ranglijst en aanbevelingen voor het DSH-plug-inecosysteem…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Door de community samengestelde DeepSeek Harness (dsh)-plug-ins, tools…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness-plugin: 15 engineeringvaardigheden van obra/superpowers…
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - MCP-serverbeheerinterface voor DeepSeek Harness Web — zwevend paneel…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Geverifieerde pluginmarkt en autonoom register voor DeepSeek Harness.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Een echte PowerPoint, geen HTML. Vertel je AI wat er behandeld moet worden en…
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - DeepSeek Harness-plugin: lazy senior-modus en port van de ladder met 7 niveaus…
- [daha1216/dsh-plugin-collection](https://github.com/daha1216/dsh-plugin-collection) - DeepSeek Harness（DSH）第三方插件精选目录：一键安装，条目均指向插件作者原仓库.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spamgefilterd register met open gegevens van DeepSeek Harness (dsh)-plugins…
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [godchen520/dsh-web-remote](https://github.com/godchen520/dsh-web-remote) - DSH 手机/外网远程访问插件：免配置公网隧道 + 局域网 HTTPS 直连 + 自定义公网链接/端口 + 微信机器人.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Maak van de modellen die op de lokaal ingelogde WorkBuddy-desktopclient staan…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Geïsoleerde install-and-smoke-testdrivers voor DeepSeek Harness-plug-ins…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Altijd actieve compatibiliteitstests voor DeepSeek Harness-plug-ins: exacte…
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeekBot: het open-sourcealternatief voor GrokBot, gebouwd op DeepSeek…
- [klarkxy/dsh-plugins](https://github.com/klarkxy/dsh-plugins) - Small, independently installable plugins for DeepSeek Harness.
- [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) - DSH Web UI 会话进度插件：输入框停靠区常驻进度条.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Röntgen voor DeepSeek Harness-plugins: gedeclareerde mogelijkheden versus…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness-hostplugin die projectdocumenten en langetermijngeheugen als…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH-pluginmarkt — installeer community-plugins met één klik binnen de DeepSeek…
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first pluginintelligentie voor DeepSeek Harness: bestaande plugins…
- [omdsh-dev/dsh-minigames](https://github.com/omdsh-dev/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Voicegesprekken voor DSH, lokaal als uitgangspunt.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH-plugin: een IDE-waardig Git-toolvenster als native dsh-better-sidebar-tab…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - Creatieve modus op basis van de PTC-modus: DSH-plugin, combineert de…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH)-pluginranglijst en -directory｜DeepSeek…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Werkruimte met meerdere mappen: laat de agent van DSH (DeepSeek Harness) niet…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plug-in voor technische workflows voor DeepSeek Harness: taakfasen…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH-plugin voor rollenspellen: personagekaarten.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Doorzoekbaar DeepSeek Harness-pluginregister met geselecteerde vermeldingen en…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Verificat standaard zonder afhankelijkheden voor DeepSeek Harness…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness-plug-inmarkt - blader door, zoek en installeer plug-ins uit…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode op DeepSeek Harness — DSH-plug-in die OpenCode Zen + Go gratis…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marktplaats voor plug-ins van derden en beheerder van de beveiligde…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx is een mensgerichte, uitbreidbare desktopwerkplek: gesprekken, notities…
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh-daemon: registreert de DeepSeek Harness-webserver (dsh web) als een…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web-invoerplug-in: schakelen tussen verzenden en nieuwe regel, contextmenu…
- [HarcoChen/dsh-intellij-integration](https://github.com/HarcoChen/dsh-intellij-integration) - DeepSeek Harness (DSH) for JetBrains IDEs — AI coding with native diffs, tool…
- [InterPSS-Project/ipss-agent](https://github.com/InterPSS-Project/ipss-agent) - InterPSS Agentic Power System Simulation Agent for AC load flow, DC-based…
- [lhh010/dsh-input-history](https://github.com/lhh010/dsh-input-history) - DSH Web 输入历史插件：Ctrl+Up / Ctrl+Down 像终端一样召回与切换已发送消息，零核心改动.
- [momasiku/dsh-pilot](https://github.com/momasiku/dsh-pilot) - Desktop automation for DeepSeek Harness: hands and eyes on the whole Windows…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Biedt de desktopversie van DeepSeek Harness een externe toegangspoort met…
- [omdsh-dev/dsh-file-trace](https://github.com/omdsh-dev/dsh-file-trace) - DSH Web UI 文件追踪插件：记录并查看模型读取/写入/编辑的每个文件，带行号内容、终端风逐行 diff（红删绿增蓝改）与 hunk 上下文折叠；支持…
- [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH)-webplugin: markt-dashboard-zijtab voor monitoring — drie…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness-plug-in: zet de fout bij het instellen van de sandbox-ACL van…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Maakt een niet-toegeschreven lege modelpoging opnieuw uitvoerbaar, voor de ene…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness agent preset: Codex and Claude Code as delegation subagents…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Een Rust-plug-inruntime met een door Verus geverifieerde levenscycluskernel en…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH-pluginaggregator: aggregatie en zoeken van alle DeepSeek Harness-plugins op…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh-plug-inmarkt - automatische ontdekking en elk uur synchroniseren op basis…

</details>

<a id="writing"></a>

## Schrijven, discussies en video&#x27;s

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Summary

Hoi HN, ik heb dit voor mezelf gebouwd en wilde het opensourcen. Het probleem: ik wilde een manier om tussen prompts door herinneringen te krijgen, omdat ik vaak lange uren in de terminal doorbreng, vooral nu we meestal zoveel agents parallel verwerken. De eerste versie was een eenvoudige her

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

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

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Summary

Ik heb dit gebouwd omdat Claude bij de nieuwste codeermodellen in een modus voor diep werk terechtkomt met obscure opdrachten, waardoor ik niet meer weet wat het aan het doen is. Dit is een mod (een plugin die de nieuwe functie-hooks van Claude Code gebruikt) die één regel boven de prompt tekent: - de huidige stap,

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Schrijven, discussies en video&#x27;s`                           |
| Evidence | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Projecten per implementatietaal

The ecosystem is concentrated in Python and TypeScript, but typed clients keep appearing in other languages. This table is generated from the entries themselves.

| Taal       | Items | Voorbeelden                                                                                                   |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 402   | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                          |
| JavaScript | 85    | `Enc-hanted/dsh-pulse`, `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`                        |
| Python     | 45    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 29    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 16    | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7     | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2     | `rainyfei/claude-statusline-win`, `daha1216/dsh-plugin-collection`                                            |
| Swift      | 2     | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| MDX        | 1     | `jkf87/mod-guide`                                                                                             |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Last updated · 2026-10-11T10:13:26+08:00</sub>
