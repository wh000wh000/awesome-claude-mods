<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Geweldige Claude-mods">
</p>

<h1 align="center">Geweldige Claude-mods</h1>

<p align="center"><b>De op basis van bewijs beoordeelde index van Claude Code-mods, plug-ins en het diepere gedrag dat ze veranderen.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-506-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <b>Nederlands</b> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Actieve index** · Laatste synchronisatie: `2026-10-11T21:12:49+08:00` (UTC+8)
> · Items: **506** · Toegevoegd in de nieuwste update: **0** · Implementatietalen: **12**

<sub>Elk item hieronder is automatisch verzameld, gefilterd en opnieuw gecontroleerd. Niets hiervan is betaalde promotie.</sub>

<a id="featured"></a>

## Uitgelicht van dit moment

<sub>Eén item per categorie, gerangschikt op bewijsniveau en sterren, bij elke update opnieuw berekend. Een ranglijst, geen aanbeveling; elke keuze linkt door naar de volledige kaart hieronder. Projecten die een screenshot of opname hebben gepubliceerd krijgen de voorkeur, zodat de balk visueel blijft.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9473 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2534 · Python · 👁️ observed</sub>
<sub>Vind de spooktokens. Los ze op. Overleef compactie. Voorkom kwaliteitsverlies van de context.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74325 · TypeScript · 👁️ observed</sub>
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
- [Officieel: de eigen repositories en release notes van Anthropic](#officieel-de-eigen-repositories-en-release-notes-van-anthropic) — **15**
- [Mods: gebouwd met de modfunctionaliteit](#mods-gebouwd-met-de-modfunctionaliteit) — **381**
- [DSH- en Cordis-plug-inecosystemen](#dsh--en-cordis-plug-inecosystemen) — **99**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150151 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **150151** |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9473 · TypeScript · ✅ official · 1 天</summary>

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
| Stars        | **9473**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

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
| Stars        | **8248**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

##### 📝 Summary

An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6342**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

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
| Stars        | **1797**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Summary

Supplementary materials for Claude Model Cards

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
| First listed | 2026-10-11 |

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
<summary><b>Meer in deze categorie</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `$.ui.notify` toegevoegd voor mods: geeft een native melding via je eigen…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Esc of een onderbreking tijdens een `UserPromptSubmit`-hook of de…
- [riffkit/skill](https://github.com/riffkit/skill) - Official Riffkit skill — riff a winning TikTok into your own short video from…

</details>

<a id="mods"></a>

## Mods: gebouwd met de modfunctionaliteit

Elke vermelding hier toont bewijs dat de mogelijkheid voor Claude Code die in 2.1.287 is toegevoegd, wordt gebruikt: de vermelding tekent via `ui.render`, beheert een deelvenster, band of kaart, leest `$.ui.selection()`, start teamgenoten met `agent.spawn`, of zegt duidelijk dat het een mod is.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

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
| Stars        | **2534**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐484 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Communitycatalogus van openbare Claude Code-mods (functiehooks), gescand vanuit GitHub, met informatie over wat elke mod kan lezen, schrijven, uitvoeren of via het netwerk kan verzenden. Bekijk https://mods.aidojo.si/

<sub>🔧 Gebruik in code gevonden: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **484**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 7 天</summary>

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
| Stars        | **127**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐93 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **93**     |
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
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stars        | **66**     |
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
<summary>🧩 <b><a href="https://github.com/karanb192/claude-code-mods">karanb192/claude-code-mods</a></b> · ⭐40 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Claude Mods en de tools om ze te bouwen: eerst een builderskill, daarna mods

<sub>🔧 Gebruik in code gevonden: `plugins/mod-builder/skills/mod-builder/references/migrate.md`, `plugins/mod-builder/skills/mod-builder/references/nouns.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **40**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐24 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code toont afbeeldingen en speelt video's rechtstreeks in je terminal af: schermafbeeldingen, Playwright-opnamen en gesynchroniseerde voor-en-na-QA. Ghostty & kitty.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **24**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/9ee7df00aee28636.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/adcbff13953c23f1.gif" width="100%" alt="iamumeransari/claude-show-your-work animation"><br><sub>geanimeerde opname</sub></td>
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
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>geanimeerde opname</sub></td>
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
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Live GSD-dashboard voor Claude Code: roadmap, agentboom met forks, context en kosten, werkstromen en een markdownlezer voor .planning. Alleen-lezen.

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/a31036b15398e820.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>geanimeerde opname</sub></td>
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
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Je plan dat zichzelf in de gaten houdt. Lokale desktop-roadmapboom die Claude Code en elke MCP-host live actueel houdt. Gewoon JSON, geen cloud.

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
| First listed | 2026-10-11 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/leopiney/wolfbud-claude-mod">leopiney/wolfbud-claude-mod</a></b> · ⭐5 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Spraakcollega voor Claude Code. Bespreek dingen met een 3D-wolf, aangedreven door conversatie-AI van ElevenLabs; wanneer je het eens bent, stuurt hij de prompt naar Claude en laat hij van zich horen wanneer Claude klaar is.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **5**      |
| Last push    | 2026-10-08 |
| First listed | 2026-10-10 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/leopiney/wolfbud-claude-mod/main/assets/banner.png" width="100%" alt="leopiney/wolfbud-claude-mod screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HMarzban/claude-mod">HMarzban/claude-mod</a></b> · ⭐4 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Bekijk wat je volgende Claude Code-bericht kost: een live balk boven de prompt met de prompt-cacheaftelling, de prijs voor opnieuw opwarmen, sessiekosten, context en gebruikslimieten voor 5 uur en per week.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4**      |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-ai` · `claude-code` · `claude-code-plugin` · `claude-mod` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dominicrico/jev-router">dominicrico/jev-router</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code-plug-in: automatische routering van het Claude-model. Kiest Haiku, Sonnet of Opus en de redeneerinspanning per prompt, stap en subagent; inspanningslimiet, promptcachebewaking, statusband en benchmarks.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-marketplace` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/e9ab68584ed9c404.jpg" width="100%" alt="dominicrico/jev-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/2a6620c49438b369.gif" width="100%" alt="dominicrico/jev-router animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/FynnXland/fynn-mods">FynnXland/fynn-mods</a></b> · ⭐3 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Zes mods voor Claude Code: geanimeerde Clawd-mascotte, balken voor gebruikslimiet en promptcache, een berichtcontrole vóór verzending, snelle antwoorden, een takenwachtrij en een kostenboek. Terminal en desktopapp, Engels/Duits.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-09 |
| First listed | 2026-10-07 |

🏷 `ai-coding-assistant` · `claude` · `claude-ai` · `claude-code` · `claude-code-marketplace` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mertkayacs/ultramod">mertkayacs/ultramod</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Het beste alles-in-één modpakket voor Claude Code: gebruikslimieten en context-HUD, een beveiliging met undo voor rm -rf en git reset --hard, bescherming van .env en geheimen en een ontvangstbewijs voor elke beurt. Tien mods, één installatie.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/0f9d8b2253819dc8.gif" width="100%" alt="mertkayacs/ultramod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/1537defa7233d7f2.gif" width="100%" alt="mertkayacs/ultramod animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mthli/cc-shorts">mthli/cc-shorts</a></b> · ⭐3 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Speel YouTube Shorts af in je Claude Code 💃

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `claude-mods` · `youtube-shorts`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mthli--cc-shorts/ef652fff732c023d.png" width="100%" alt="mthli/cc-shorts screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/chenyuxiaojin/cyxj-notch">chenyuxiaojin/cyxj-notch</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

macOS-dashboard in notch-stijl voor Claude Code: gebruikslimieten, open sessies, taakvoortgang, prompt-cache-aftelling en to-do's — gevoed door vijf Claude Code-mods (inbegrepen).

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools` · `dynamic-island` · `macos` · `menu-bar`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Christandoh/context-cache">Christandoh/context-cache</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: context usage, session / weekly / Fable limits and prompt-cache temperature above the prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/christandoh--context-cache/3cdd3b2c5a09da7d.png" width="100%" alt="Christandoh/context-cache screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/CodyAMaughan/meme-factory">CodyAMaughan/meme-factory</a></b> · ⭐2 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Vers uit de fabriek. Een Claude Code-mod: vraag om een meme en blijf doorwerken. Concepten worden in een zijpaneel gemaakt; kies, remix, keur goed en plaats ze op Slack.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `fun` · `meme-generator` · `memes` · `slack`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/7417dc8940c4a087.png" width="100%" alt="CodyAMaughan/meme-factory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/8c9d44287267796f.gif" width="100%" alt="CodyAMaughan/meme-factory animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/estruyf/claude-stats-mod">estruyf/claude-stats-mod</a></b> · ⭐2 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Een Claude Code-mod die je gebruikslimieten en uitgaven weergeeft in de balk boven de prompt.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `claude` · `claude-code` · `claude-mod` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/estruyf/claude-stats-mod/main/assets/desktop.png" width="100%" alt="estruyf/claude-stats-mod screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/i-harsha-reddy/naruto-mod">i-harsha-reddy/naruto-mod</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Een pixel-art Naruto-metgezel voor Claude Code: 20 ninja's, 60 jutsu, uitgevoerd terwijl Claude werkt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `naruto` · `pixel-art`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lorenzh/rabe">lorenzh/rabe</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Bekijk wat Claude Code op de achtergrond uitvoert: subagents, Codex-taken, shells, monitors, cron-taken en workflows.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-11 |
| First listed | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/macleodlabs-ai/claudeflow">macleodlabs-ai/claudeflow</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code-mods van MacLeod Labs: streams ontwart het door elkaar lopende werk van een sessie in kleurgecodeerde streams

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/macleodlabs-ai/claudeflow/main/assets/hero.jpg" width="100%" alt="macleodlabs-ai/claudeflow screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/MankhongGarden/claude-code-mods-field-notes">MankhongGarden/claude-code-mods-field-notes</a></b> · ⭐2 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Eerste-dag veldnotities over Claude Code-mods op Windows: een context-/quotabrandstofbalk, een Thaise UI-mod, een Matrix-opstartintro en een veilige updater, plus wat mislukte en waarom (panelen, banden boven de prompt, Thai in Windows Terminal).

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2**      |
| Last push    | 2026-10-09 |
| First listed | 2026-10-07 |

🏷 `anthropic` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mankhonggarden--claude-code-mods-field-notes/832ffcdb7bad9007.png" width="100%" alt="MankhongGarden/claude-code-mods-field-notes screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 347</sub></summary>

- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Een desktopapp-uiterlijk voor het terminaltranscript van Claude Code, als mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Een zijpaneel voor Claude Code: de subagenten die een sessie uitvoert, wat elk…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Zijbalkpaneel van Claude Desktop (Code-tabblad): toont alle onafgemaakte en…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Gebruiksbalk boven het invoervak van Claude Desktop (Code-tabblad): 5u /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-mods, plug-ins en skills, installeerbaar vanuit één marktplaats.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Een beslissingswachtrij CLI/TUI voor mensen die met conversatieagenten werken.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Een zwevende statuskaart voor Claude Code — model, context, rate limits…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lees de markdown-bestanden die Claude Code benoemt, weergegeven naast de…
- [atomashevic/claude-latex-math](https://github.com/atomashevic/claude-latex-math) - Claude Code mod that typesets the LaTeX math in Claude.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Vuurwerk voor Claude Code: elke toetsaanslag, toolaanroep, commit en geslaagde…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Kleine Claude Code-mods (function-hook-plug-ins): session-switcher en meer.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Zes Claude Code-mods: planningslimieten en context boven de prompt, een coach…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code-mod die Edit- en Write-diffs in twee kolommen naast elkaar weergeeft.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Een samengestelde lijst van Claude Code-mods, installeerbaar als…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Een zeer uitgesproken Claude Code-plugin, ontworpen door een Rustacean die…
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Een passief-agressieve waterherinnering voor Claude Code.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-mod: live kosten-, context- en planquotameters boven de prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Een Claude Code-mod die fan-out van subagents, prompts met zware context en…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Een Claude Code-mod die je globale skills, agents, regels en tools per repo met…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code-plugins (mods): wissel tussen meerdere Claude-accounts, bekijk…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Geteste Claude Code-mods die je met één opdracht installeert: guardrails voor…
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Filmachtige aftiteling voor je codeersessie.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Leer een vreemde taal terwijl je met Claude Code werkt.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude Code mods for running many sessions across many repos from one control…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Wanneer een agent Java schrijft, kan code die het Alibaba-voorschrift Java…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Zijbalk met live kosten-, token- en contextgebruik voor Claude Code: een mod…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code-mod: een backlog van de opvolgtaken die Claude in elke sessie…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internetradio in Claude Code: een cliamp-sidebar, minispeler, favorieten…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Fun, useful Claude Code mods: a pixel critter above your prompt, a tools menu…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude is aan het koken. Chat met je squad.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Verzameling van jack.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Een Claude Code-mod: vang pixel-art-Modsters in een idle game terwijl Claude…
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Alles-in-één Claude Code-mod: live HUD, veiligheidsbeveiligingen…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Een ruimtegevecht boven de prompt van Claude Code terwijl het werkt.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zie welke bestanden elke Claude Code-agent in zijn context heeft, en hoeveel…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Houd je hoofd koel. Een thermometer voor je Claude Code-dagen: elk uur krijgt…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Promptcache-, context- en planlimieten in één oogopslag voor Claude Code, in de…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code-mod: een livepaneel met de GitHub PR.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-mods voor de terminal en de desktopapp.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Verzameling Claude Code-mods, elk in een eigen repo: usage-meter…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code-mod: een voortgangspaneel voor taken, subagents, workflowruns, het…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code-mod: een klikbare inhoudsopgave met tijdstempels van de hele…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code-mod: planningslimieten, contextvulling, sessiekosten en tokens per…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-skill + mod die Spaanse woorden toevoegt aan agent-antwoorden.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Integreer Alarum.me in je Claude-code CLI of Desktop.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Evangelion-achtige zijbalk voor Claude Code: context, quotum, activiteit, PR.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Een Claude Code-mod die het herstijlt als The Machine uit Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code-mod voor verplichte, geverifieerde DAG-workflows van…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-sourcemods voor Claude Code: deelvensters, statusregels, toastmeldingen…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code-mod: sessiestatus, live Spec Kit-voortgang en beheer van…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Het contextvenster als een rij boven de prompt, weergegeven zoals Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Een live taak-HUD voor Claude Code Desktop: een strook boven de prompt terwijl…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Een gratis, open-sourceplugin voor Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod that shows images inline in Ghostty and kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Een Claude-mod die de GitHub pullrequests van de sessie weergeeft in een paneel…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-vaardigheden: een factchecker voor documentatie, een code-auditor…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code-mod: de regels code van vandaag door Claude — nieuw, bewerkt…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code-mod: klikbare paden in antwoorden — klik op een map om deze in…
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Claude Code-mod: kiest per prompt /effort met Jev.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-buddyplugin: een ASCII-metgezel boven je prompt die je regels…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code-mods: beveiligingslaag voor Claude Code - geheimen redigeren…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-plugin en -mod: een AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Verzameling geweldige Claude Code-mods | verzameling Claude Code-mods.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Een gezellige RPG-HUD-mod voor Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: een Claude Code-mod die de antwoorden van Claude en je prompts op…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code-mods op aanvraag — een vaardigheid die je gesprek leest en de…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Geef Claude een pak slaag wanneer het fouten maakt — een…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code-mods: kleine plugins voor livepanelen, kostenbewuste modelroutering…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code-mod &amp; plugin: gebruiksmonitor, tokentracker &amp; statusline.
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Drie gratis Claude Code-mods: .env-waarden verbergen voor toolresultaten, het…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code-mods. touch-map: zie welke bestanden Claude heeft opgesomd…
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Claude Code-pluginmarktplaats voor 0xnicholasy.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code-mod: voortgangsbalken voor gebruik (context, 5 uur, 7 dagen) en een…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code-mods: sessiestatistiekkaarten boven de prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Een geanimeerde braillekat boven de Claude Code-prompt.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code-mod: stuur goedkoop werk via een onderliggend Claude Code naar…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Een pixelkat boven je Claude Code-prompt die een testgesprek met een…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Een Claude Code-mod die een goed moment kiest om te verdichten, zodat het…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods voor Claude Code: tokenmeter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code-pluginmarktplaats van anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code-mod: het gebruik van 5 uur en per week van je plan als één regel…
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Claude Code-mods om de markt vanuit de terminal te volgen: paneel voor A股/港股/美股…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mods voor Claude Code.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - Mijn privé-Claude Code-mods.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Het LGTM Lines-schip vaart na elke codewijziging voorbij — een Claude Code-mod.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code-mods voor het S2-team (de ather-marktplaats).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Korte workouts terwijl Claude werkt: een dagelijks doel, streaks, badges en…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Plan-, taak- en agentvoortgang naast de Claude Code-prompt — een Claude Code-mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Een gebruiksoverzicht voor Claude Code: uitgaven per model.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Een Claude Code-mod: live uitsplitsing van het contextvenster boven de prompt.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now Playing-mod voor Claude Code: Apple Music en Spotify boven de prompt, met…
- [bitcars/ctx-bar](https://github.com/bitcars/ctx-bar) - ctx-bar: a Claude Code mod that keeps the context window visible at all times.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods voor Claude Code: Cache-klok, Blast Radius, suggesties, werklijst, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Gewoon een uil voor je Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Eénregelige Claude Code-band.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - De originele Doom-engine met Freedoom, speelbaar binnen Claude Code.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Claude Code-mod: geschat elektriciteitsverbruik ⚡ en waterverbruik 💧 achter…
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Een Claude Code-mod die een doorlopende lijst bijhoudt van de openstaande…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code-mods voor echte Engineers.
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Exclusieve Claude Code-mods voor het d3nim-team.
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code-mods: rule-keeper slaat je correcties op als permanente regels.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Een Tamagotchi die in Claude Code leeft: hij komt uit, eet de code die Claude…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods voor Claude Code, als plug-inmarktplaats.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code-mod: toont de tijd bij elke prompt en elk antwoord in de terminal…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Claude Code-mods geschreven als functiehooks, en de marktplaats die ze…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code-mod: nadat een guard een toolaanroep blokkeert, stopt hij herkende…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code-mod: achtergrondtaken in één weergave, met voortgang en ETA.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code-mod: één inbox voor berichten van teamgenoten, benoemde subagents…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code-mod: legt sandboxblokkades uit en zet herhaalde blokkades om in…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favorieten voor Claude Code: pictogrammen met één klik voor je opdrachten en…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hé, gedempt! Weg met de diff, schrap de riff, geen wijzigingen meer, minder…
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - mods voor claude.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code-mods: delete-guard (bevestiging van bestandsverwijderingen) en…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude Code-mod: abonnementsgebruik (5u / 7d) als een balk boven de prompt in…
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code mod: your background agents as pixel critters, one sprite per model.
- [FeidaWang/edit-replay](https://github.com/FeidaWang/edit-replay) - Edit Replay: step through the file edits Claude made in the last turn, one diff…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod-marktplaats.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Een live radar van je parallelle branches en worktrees boven de prompt: welke…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Een Claude Code-mod voor het vastleggen van gedachten tijdens het werk, het…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods en skins voor Claude Code: een live voortgangsbalk voor de taken van…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code-mods (function-hook-plugins): contextband, losse eindjes…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Zeven Claude Code-mods: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+klik om een link te kopiëren op elk codeblok in Claude Code-antwoorden…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mods voor Claude Code: plugins met hooks, zoals usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code-mods (functie-hook-plug-ins), geïnstalleerd via één marktplaats.
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code-mods: context-bar-plus (contextbalk, quotum, subagentmodi).
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Statische supply-chain-auditor voor Claude Code Mods — lokaal, offline, alleen…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Duitstalige mods voor Claude Code: context-/cache-aanwijzingen, openstaande…
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code mod: capture ideas into an Obsidian vault inbox from any session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-mod: hoe lang elk antwoord duurde, hoe lang Claude nadacht en…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code-mods: streamer-mode verbergt privévensters, banden en de…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - voor mijn claude-mods.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code-mod: wacht de gebruikslimiet van vijf uur uit en verstuurt…
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Kleine mods voor Claude Code, te beginnen met automatisch doorgaan na de limiet…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Een cockpit boven je Claude Code-prompt. De eend leest de meters af.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Kleine Claude Code-mods: meters voor context- en plangebruik, een…
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: a Claude Code mod with a side pane showing where each work item…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Een Claude Code-mod: één deelvenster per subagent, de bestanden die ze aanraken…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Zijpaneel met contextgebruik: totaal, categorieën, groei per beurt, de grootste…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Zijpaneel met bestandenlijst: welke bestanden tijdens dit gesprek zijn…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Een pluizige 8-bit 毛毛 (zwart-wit Nederlandse hangoor) rent en springt boven het…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Zijpaneel met ‘wat ik heb gevraagd’: elke zin die de gebruiker tijdens dit…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Zijpaneel met tijdlijn: waar de tijd van deze beurt aan is besteed.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Zijpaneel met tokenverkeer: hoeveel tokens het hoofdgesprek elke keer naar…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - De eerlijke bonenpasta van claude code: na elke beurt zegt Claude zachtjes één…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Kleine mods voor Claude Code, zoals nieuwe slashopdrachten en zijpanelen.
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Onofficiële communitygids voor Claude Code-mods (functie-hooks) in 6 talen, met…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd leeft in een band boven je Claude Code-prompt: speelt de sessie na, toont…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Een mod die antwoorden en meldingen van Claude Code voorleest met VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Een Claude-mod om de gesprekken tussen je Claude Code-sessies te lezen en eraan…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code-mod: subagents als pixelachtige Claude-mascottes boven de prompt.
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude-mods.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code-mods (gebruiksmeter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Twee Claude Code-mods: folio, een bestandsdeelvenster naast de chat, en tint…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph oh what Claude Code knows.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Laat je aandacht niet afdwalen terwijl je wacht op het antwoord van Claude Code.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Claude Code-mods voor de projecten van Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Een door de community samengestelde Claude Code Mods-gids: gebruiksscenario.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Een Claude Code-mod die laat zien wat Claude doet in de ondertitel van het…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Een pluizige zwarte kat boven je Claude Code-prompt.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Een Claude Code-mod met verwisselbare toestemmingsprofielen: een veilige basis…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community-mods voor Claude Code: bewaking, deelvensters en opdrachten die…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Zijpaneel voor Claude Code: bestanden die Claude heeft geschreven…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Een rustig zijpaneel voor Claude Code: wat deze sessie doet, het plan, de…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Een gedimde tijdsaanduiding boven elke prompt en elk antwoord in het Claude…
- [mmedum/spor](https://github.com/mmedum/spor) - Zet terug wat Claude Code wegvouwt: de bestanden die Claude las, de opdrachten…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code-mod: gebruik van het contextvenster in het promptvoettekstvak.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-mod die de todo-tools weer inschakelt voor modellen die ze…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-mod: één regel per taak in de takenlijst boven de prompt, met de…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Speel Vier op een rij tegen een AI binnen Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code-mod: wanneer een andere code-agent een commit naar je repo maakt…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code-mod voor repo.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods marketplace.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Een beveiliging voor SQL in Claude Code: vraagt voordat Claude via een DB CLI…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Eén mod voor Claude Code, Windows en CJK als uitgangspunt: voorbeelden van…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - De beste Claude Code-mods, gesorteerd op wat ze voor je doen.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Een Claude Code-mod die risicovolle shellopdrachten.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Twee Claude Mods voor Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code-mods met agenttelemetrie, tijdlijndashboards, mmrun-beoordeling…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Scheld tegen Claude Code en een cartoonhand slaat terug.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code-mods: usage-both toont het gebruik van 5 uur en per week boven de…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live zijpaneel met sessiestatistieken voor het Code-tabblad van de…
- [PhilRoli/traintracker-claude](https://github.com/PhilRoli/traintracker-claude) - Claude Code mod: pause sessions before your TrainTracker train arrives.
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Claude Code-mods voor de pompeitech-interface, vormgegeven naar het…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods voor Claude Code: safety-guard blokkeert destructieve opdrachten en…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods voor Claude Code: functie-hookplugins die binnen de sessie worden…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code-mod: live-aandelenkoers, /quote-paneel, prijswaarschuwingen…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code mod: keeps auto-memory up to date in the background after every turn.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code-mod: SSH-host, RAM en gebruikslimieten voor 5 uur/7 dagen in een…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-mod: push-ups om te doen terwijl Claude werkt. Geen tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 Koreaanse edities van Claude Code-mod: aannames vastleggen, eenvoudige taal…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-mod: verandert het plan dat je in planmodus goedkeurt in een live…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Een zorgvuldig geselecteerde lijst van Claude Code-mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenvrije modus: helperagents draaien op Haiku, en grote bestanden en logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Een lofi-soundtrack die de sessie volgt: kalmte, focus, flow, plus signalen…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Leer terwijl Claude codeert: na een beurt die de code heeft gewijzigd…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Een bandopname van elke bewerking die Claude maakt: speel elke wijziging af…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Elke link die je sessie vermeldt, op één regel boven de prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code-functie-hooks minimaal demonstratie: een live token-/kostenpaneel…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Claude Code-mod: 5u-, week- en Fable-limiet als balk boven de prompt.
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in a terminal pane…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Een verzameling plug-ins voor Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: een onofficiële Avengers-fanmod voor Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Claude Code-mod voor context, groei, quotum, cache, native kosten en…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code-mod: stuur eenvoudige beurten en subagents naar goedkopere…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Persoonlijke Claude Code-mods.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - The original DOOM in a Claude Code pane with nothing to install: the engine…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commitberichten met één klik voor Claude Code met een dansende pixel-art Malenia.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Persoonlijke Claude Code-mods.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Een opslagplaats voor mods van Claude Code voor lokaal gebruik.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — een Claude Code-mod die je Claude-plangebruik toont.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Een Claude Code-mod die de huidige sessie in een paneel toont: elke prompt, het…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Een Claude Code-plugin-marketplace met mods: function-hooks-plugins die banden…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Een repo voor het beheren van Claude Mods.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Aanpassingen voor Claude Code.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Enkele Claude-mods.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Claude Code-mod die het Engels van je prompt controleert terwijl je die schrijft.
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Een samengestelde catalogus van Claude Code-mods, elk met een copy-pasteprompt…
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code-mods: een context- en planlimietmeter boven de prompt, en…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code-mod: 5h/7d-quotum, contextvenster, resterende promptcachetijd en…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code-mod: geanimeerde voortgangsbalk en voltooiingssamenvatting voor…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drie kleine Claude Code-mods: zie wanneer je subagents klaar zijn, zet…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Verkleint grote screenshots voordat Claude ze leest, zodat lange sessies langer…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Zeg &quot;Ik ben de draad kwijt&quot; en Claude legt het vorige antwoord opnieuw uit in…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Toont voorgestelde volgende prompts boven het promptvak.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stel Claude een zijvraag in een venster naast je werk.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace van mods voor Claude Code met installatie in één stap en een…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Aftellingen voor snelheidslimieten en een prognose van het verbruikstempo voor…
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code-plug-in: je Claude Pro/Max-gebruikslimieten met een prognose van…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods voor Claude Code. agent-crew: zie je subagents werken als een live…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Inline en weergegeven LaTeX-wiskunde, plus optionele TikZ-figuren, in de…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Een live taakbord voor Claude Code: plan voordat je bouwt, volg elke taak…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code-mod die live rapporteert welke bestanden Claude heeft gewijzigd en…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Een zorgvuldig samengestelde verzameling van de beste hulpmiddelen voor de…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Een Claude Code-plugin die toont wat er gebeurt — contextgebruik, actieve…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Mooie, zeer aanpasbare statusregel voor Claude Code CLI met…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle onderdelen van de systeemprompt van Claude Code, 27 ingebouwde…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Meer dan 45 tips om het meeste uit Claude Code te halen, van basis tot…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Mooie vim-stijl-powerline voor Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Bekijk de diff van je codeeragent in een terminalvenster en stuur…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Uitgebreide statusregelplugin voor Claude Code met contextgebruik…
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness-agent voor langdurige roleplay (DSH-taverneplug-in): import…
- [L-Forster/open-jet](https://github.com/L-Forster/open-jet) - An offline coding agent for local models.
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Fast, zero-dependency cost calculator and customizable statusline for Claude…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Terminal-statusline voor Claude Code-sessies.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live voetbalstanden, wedstrijden en ranglijsten voor de competitie die je…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Lokaal control plane voor Claude Code op Windows en macOS: wissel met één klik…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Persoonlijke configuratie van Claude Code, met versiebeheer binnen ~/.claude…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebedstijden, Hijri-datum, adhkar, dagelijkse ayah, sunnah-vasten, Ramadan…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Sessiegevoelige statusregel voor Claude Code.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Statusregel met twee regels en truecolor voor Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - A floating peak/off-peak tide card for DeepSeek Harness: i18n (en/zh/ru)…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Draagbare Claude Code-toolkit voor .NET DDD/Clean Architecture: strikte…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Draagbare globale configuratie voor Claude Code: aangepaste skills…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-plug-ins die ik elke dag gebruik: skills en mods, opgeschoond zodat…
- [chaybits/ai-session-usage](https://github.com/chaybits/ai-session-usage) - Claude Code and ChatGPT (Codex) subscription limits in one card: a KDE Plasma 6…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tokenbeheer voor Claude Code: het topmodel stuurt aan, de uitvoering gaat naar…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live statusregel voor workflowfasen voor Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Verlaag de tokenuitgaven van Claude Code &amp; Codex: stuur opzoekingen en testruns…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Eenvoudige en nuttige statuslineconfiguratie voor Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Meldingen over gebruikslimieten voor Claude Code: macOS-meldingen…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configureerbare Claude Code-statusregel voor Linux, WSL, Windows en macOS, met…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Snelle Rust-statusregel voor Claude Code — payload eerst, gecachte git…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Een live gebruiksdashboard voor Claude Code — contextverdeling, cachehits…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Een statusregel en tokenregel voor Claude Code: context, gebruik van 5 uur en…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Toon belangrijke statusdetails voor Claude Code, waaronder model, context…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - de vriendelijke statusregel voor Claude Code waarmee je alles kunt aanpassen…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Statusregel met meerdere rijen voor Claude Code: verbruik, context-%, git en…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusregel met nuttige informatie voor claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agentteams. Onder controle. Strikte werkerslimieten, live…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code-add-ons: kleurgecodeerde tabstatus-dotwatcher + ingebouwde…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code-statusregel voor macOS en Linux, verpakt als een…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Aangepaste statusregel voor Claude Code — contextbalk met gebruikspercentage…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Een schone, informatieve statusregel voor Claude Code — toont project…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD-mod: een statuspaneel in CRT-stijl voor Claude Code, in de…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code-pluginmarktplaats met baloo: vaardigheden, een agent die…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionele Claude Code-statusregel: sessieduur, kosten in meerdere valuta…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Abonnementsbewuste statusregel voor Claude Code.
- [dave-net-positive/Claude_Code_PII_Redactor](https://github.com/dave-net-positive/Claude_Code_PII_Redactor) - Mod that detects and redacts PII in Claude Code before it reaches the model.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Een uitgebreide terminalstatusregel voor Claude Code — Bun + TypeScript, zonder…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Claude Code-plugin die Mermaid-diagrammen prachtig in het transcript weergeeft…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, vaardigheden en agents voor Claude Code — te beginnen met een…
- [FunDrivenDev/claude-plugins](https://github.com/FunDrivenDev/claude-plugins) - Public Claude Code plugins: a context-budget status line.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Aangepaste statusregel voor Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Echte DeepSeek-API-uitgaven voor Claude Code: herprijst sessietranscripten…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Voorbeeldafbeeldingen in Claude Code: beweeg de muis over een chip onder een…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods voor Claude Code en Claude Desktop in Windows met WSL: Docker en…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code-statusregel met rijen voor het agentenpaneel.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchroniseer de taken van Claude met Fizzy.do voor realtime inzicht voor het…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Een verzameling Claude Code-vaardigheden, mods en andere add-ons die ik heb…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Instellingenmenu, statusregel en configuratie voor Claude Code.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - zelfgemaakte, kooivrije claude-plug-ins, vaardigheden, mods en meer.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code-omgevingsinstallatieprogramma: skills, statusregel, hooks…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Statusregel in HUD-stijl voor Claude Code — netwerkgezondheid, TPS, context…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude Code-plugins en mods om te begrijpen wat Claude doet: leesbare…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Kleurrijke statusbalk met meerdere rijen voor Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code-statusregel voor Windows (PowerShell): gebruiksbalken, afteltimers…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Bearings- en Glossary-mod voor Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code-configuratie en mods, met een gedeelde componentenkit, een…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - A small dashboard for Claude Code: context %, cache countdown, 5-hour &amp; weekly…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Custom terminal status bar for Claude Code: model, directory, git state…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Draagbare Claude Code-configuratie: CLAUDE.md, instellingen, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code-desktopmod (macOS): sessiemeldingen waarop je kunt klikken om te…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Schermlezerbegeleidermod voor Claude Code (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Een praktische, geverifieerde diepgaande verkenning van Claude Code…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Realtime kostenregistratie en statusregel voor sessiemonitoring voor Claude Code.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Een Claude Code-statusregel: map, git-branch, model, gebruik van het…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Proactieve AI-geheugen- en snelheidslimietmonitor…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-hooks, subagents en statuslines: opensourceverzamelingen en -tools…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Een visuele builder voor statusregels van Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code-statusregel die realtime tokengebruik en geschat energieverbruik…
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code-statusregel: de schoonheid van CCometixLine + de…

</details>

<a id="dsh-cordis"></a>

## DSH- en Cordis-plug-inecosystemen

DeepSeek Harness en Cordis bereiken dezelfde plek vanuit een andere richting: voor hen is de plug-in het modmechanisme, dus een plug-in daar is het equivalent van een mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74325 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74325**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100497 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **100497** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐87809 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **87809**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81879 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **81879**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35759 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35759**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8626 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **8626**   |
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
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6146 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

De pluginmarkt in DeepSeek Harness — bladeren, zoeken, met één klik installeren · DSH 可视化插件市场

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6146**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4478 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness（DSH）— een kleine walvismeisje die rechtsonder in de DSH-interface woont en je DeepSeek-accountsaldo in de gaten houdt. Lekker wiebelig, ondersteunt slepen en vastklikken, omkeren bij vastklikken aan de linkerkant en een scrollende cijferanimatie. Wordt automatisch ingeschakeld wanneer de interface actief is. Je kunt het beste je dsh-installatie meteen inschakelen.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4478**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4285 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **4285**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3153 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3153**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1983 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

De beste DeepSeek Harness-plugin voor inzicht in en beheer van de context, met een contextdashboard, browser, zijbalk en contextopdracht voor contextstatistieken, samenstelling, uitsplitsing, evolutiedetails, inzicht in waaruit de context bestaat en hoe deze evolueert. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1983**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1561 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

跨设备的开源Agent工作台

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1561**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1464 · Python · 🔎 inferred · 0 天</summary>

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
| Stars        | **1464**   |
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
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1401 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Software voor het schrijven van AI-romans: organiseert inspiratie, personages, wereldopbouw, schema's, hoofdstukken schrijven, redactie en revisie in een beheersbare workflow; biedt desktopapps voor Windows/macOS en ondersteunt lokale en online modellen. Software voor het schrijven van AI-romans: organiseert inspiratie, personages, wereldopbouw, schema's, het schrijven van hoofdstukken, redactie en revisie in een beheersbare workflow. Beschikt over desktopapps voor Windows/macOS, Ollama-integratie en een voorbeeldplugin voor DeepSeek Harness (DSH).

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1401**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **1171**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **704**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐283 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **283**    |
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

ACRYL - Agent Context Relay Yielding Lifecycles. Eén persistente werkruimte, één canonieke context, elke coding-agent.

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Tijdverschuivende taakdelegatie voor DeepSeek Harness (dsh): plan taken wanneer het jou uitkomt, ze worden onbemand buiten de piekuren uitgevoerd en je komt terug bij een rapport. Door mensen beoordeeld, desktop + web.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **170**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
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
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Bij installatie worden automatisch de 27 engineering- en productiviteitsskills van mattpocock/skills v1.3.1 meegeleverd; je hoeft skills niet handmatig te installeren. Deze plug-in is gebouwd met 40 miljard tokens en biedt boven op de oorspronkelijke skills 10× meer ontwikkelingsproductiviteit, zodat beginners sneller met deze skillset aan de slag kunnen. Volledige ondersteuning voor GitHub issues; Markdown is een previewversie; GitLab wordt momenteel niet ondersteund. Bedankt voor je gebruik en steun 💗

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **134**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **133**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐131 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **131**    |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐130 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Runtime evidence that helps agents trace, profile, and burn down hotspots in application and native code, GPU kernels, and inference stacks.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **130**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 桌宠插件：元气鲸鱼娘看板娘陪你写代码 🐋 支持 DSH 桌面端 0.2.0-rc.2 与旧版 Web（desktop pet / mascot，local-first）

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **120**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **113**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐65 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Desktopversie van een Agent, gebouwd op de kern van Deepseek-Harness. Behoudt alle mogelijkheden van de basis en vult IDE-gerelateerde functies aan.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **65**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

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
| Stars        | **59**     |
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

Taakbewuste contextretrieval en levenscyclustracking van de werkruimte voor AI-coding-agents: vind, organiseer en volg continu de meest relevante documenten, code en media voor de huidige taak. Volledig lokaal, zonder modelaanroepen en zonder netwerk. Taakbewuste contextretrieval en levenscyclustracking van de werkruimte voor AI-coding-agents. Vind, organiseer en volg de werkruimtecontext die het meest relevant is voor de taak — lokaal, deterministisch, zonder modelaanroepen en zonder netwerk.

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
<summary>🧵 <b><a href="https://github.com/skyf0xx/hedgehog">skyf0xx/hedgehog</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

HEDGEHOG codes Cleaner, Faster and with Fewer Tokens. Hedgehog's AI-driven development builds a task dependency graph from your spec-driven, BMAD-METHOD plan, so Claude Code, Cursor & Gemini CLI stay locked to it. A CLI-enforced state machine for agentic coding. Now builds DeepSeek DSH Plugins. DeepSeek Harness、DSH 插件、AI 编程、BMAD 方法. AI Copywriting

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **44**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `agentic-coding` · `ai-agents` · `ai-assisted-development` · `ai-coding` · `ai-copywriting` · `ai-engineering` · `ai-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/skyf0xx--hedgehog/326d2d3a663269a4.jpg" width="100%" alt="skyf0xx/hedgehog screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐42 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

dsh-plugin voor een meester in gamematerialen. Integreert het seedream-beeldgeneratiemodel en het minimax-videogeneratiemodel en kan allerlei gamematerialen genereren.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **42**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 插件：维护 llm-pi-ai 模型的准确上下文窗口，避免长会话被误判为上下文溢出。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **34**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/6c743bbe3da63616.jpg" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PensiveFei/deep-read-summarize">PensiveFei/deep-read-summarize</a></b> · ⭐31 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Deep reading & summarization workflow for books/papers/videos/web — plugin parsers, MapReduce deep-read, JSON Schema output, Obsidian-ready (DSH)

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **31**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agent` · `content-summarization` · `deepseek` · `dsh-plugin` · `pipeline` · `workflow`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pensivefei--deep-read-summarize/800b10f03f25fe11.png" width="100%" alt="PensiveFei/deep-read-summarize screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Een samengestelde lijst met de beste geweldige AI-plugins voor AI-assistenten…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-pluginmarkt / DSH Plugin Marketplace: blader, installeer en update alle…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [arcships/rutis](https://github.com/arcships/rutis) - Een pluginruntime voor software die zichzelf herhaalt — de basis waarop agents…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Uitgelichte directory van DeepSeek Harness (DSH)-plugins — meer dan 280…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zotero-toolkit voor DeepSeek harness; maak van je Zotero-bibliotheek een…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH-plugin: Git Bash-shell voor alle agentmodi op Windows.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: een multiplatform-groepschatagentsysteem op basis van DeepSeek…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - Kantoortrio! Office-documenttools voor DeepSeek Harness (dsh): spreadsheets…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh voor Android: integreert DeepSeek Harness, een Ubuntu-runtimeomgeving…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH 会话导航.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [weishao2/tizhuang-agent-skills](https://github.com/weishao2/tizhuang-agent-skills) - 2000万+中小学K12真题题库 Skill：免费注册、免费抽题、教材/章节/知识点检索、练习测验与AI智能组卷.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH-webplugin: statistieken over tokengebruik per dag met een…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Door de community samengestelde DeepSeek Harness (dsh)-plug-ins, tools, skills…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - MCP-serverbeheerplugin voor DeepSeek Harness: pagina Instellingen → MCP, OAuth…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness-plugin: 15 engineeringvaardigheden van obra/superpowers…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A-runtime voor commerciële onderhandelingen + DeepSeek Harness-plug-in (dsh).
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - MCP-serverbeheerinterface voor DeepSeek Harness Web — zwevend paneel…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Een echte PowerPoint, geen HTML. Vertel je AI wat er behandeld moet worden en…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催更姬：给大肥鱼一个小说工作台。写正文、理设定、画情节，和 AI 一起讨论、续写与改稿.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 插件 · 发送栏一键「优化」提示词草稿：五维诊断 + 改写稿 SSE 流式上屏，可替换 / 复制 /…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Loginpoort voor het DeepSeek Harness (dsh)-weboppervlak: aanmelden met een…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - AI-engineeringplug-in voor embedded C/C++ — firmwarevaardigheden.
- [Chael-Chael/dsh-reference-anything](https://github.com/Chael-Chael/dsh-reference-anything) - The best DeepSeek Harness plugin for referencing anything — enhanced @ menu for…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Alles-in-éénbeheerder voor skills, subagents, MCP en LSP voor DeepSeek Harness…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Altijd actieve compatibiliteitstests voor DeepSeek Harness-plug-ins: exacte…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive context compaction for local-first agents.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness-hostplugin die projectdocumenten en langetermijngeheugen als…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Röntgen voor DeepSeek Harness-plugins: gedeclareerde mogelijkheden versus…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - A knowledge base toolkit for research and literature review.
- [Mcd0LUO/dsh-guard-repeat-output](https://github.com/Mcd0LUO/dsh-guard-repeat-output) - Host-side degeneration guard for DSH: strips garbage code points, detects…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - 让 DSH 回答变成可操作的界面：计算、图表、表单、模拟与小游戏。独立 DSH 插件 ｜ Interactieve antwoorden voor…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - 设计与代码的声称核验：事实类对照源码，行为类跑可执行模型；含结构/依赖审查（单层与多粒度细化）、UML 审查、基线对比与导出.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Werkruimte met meerdere mappen: laat de agent van DSH (DeepSeek Harness) niet…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plug-in voor technische workflows voor DeepSeek Harness: taakfasen…
- [Kr-ATG/dsh-chat-plus](https://github.com/Kr-ATG/dsh-chat-plus) - DSH 对话体验增强套件（零源码改动，纯插件注入）。Seeker 双栏执行大盘：右栏任务 / 操作面板 / 子智能体 / 产出物四张卡 +…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Verificat standaard zonder afhankelijkheden voor DeepSeek Harness…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode op DeepSeek Harness — DSH-plug-in die OpenCode Zen + Go gratis…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marktplaats voor plug-ins van derden en beheerder van de beveiligde…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx is een mensgerichte, uitbreidbare desktopwerkplek: gesprekken, notities…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Een coding-agent voor DeepSeek Harness met alles inbegrepen — workflows in…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web-invoerplug-in: schakelen tussen verzenden en nieuwe regel, contextmenu…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Biedt de desktopversie van DeepSeek Harness een externe toegangspoort met…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — communitytoolkit voor lokale implementatie en beheer van DeepSeek…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH)-webplugin: markt-dashboard-zijtab voor monitoring — drie…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Maakt een niet-toegeschreven lege modelpoging opnieuw uitvoerbaar, voor de ene…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plug-ins die zichzelf opruimen: een Swift 6-port van het…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness-agentpreset: Codex en Claude Code als delegatie-subagents, elk…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Een Rust-plug-inruntime met een door Verus geverifieerde levenscycluskernel en…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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

| Taal       | Items | Voorbeelden                                                                                                        |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 322   | `anthropics/claude-code`, `anthropics/claude-code-action`, `karanb192/cache-tax`                                   |
| JavaScript | 69    | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `augiefra/claude-mods`                         |
| Python     | 32    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`      |
| Shell      | 19    | `anthropics/claude-agent-sdk-typescript`, `andrewbakercloudscale/claude-code-cost-sidebar`, `Gharib89/claude-mods` |
| HTML       | 12    | `awss1i/assay`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                                       |
| Go         | 6     | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                         |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`                  |
| PowerShell | 2     | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                                |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                            |
| Kotlin     | 1     | `dphmoblie/deepseek-harness-android`                                                                               |
| MDX        | 1     | `jkf87/mod-guide`                                                                                                  |
| Swift      | 1     | `eovidiu/cordis-ios`                                                                                               |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Last updated · 2026-10-11T21:12:49+08:00</sub>
