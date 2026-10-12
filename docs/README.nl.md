<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Geweldige Claude-mods">
</p>

<h1 align="center">Geweldige Claude-mods</h1>

<p align="center"><b>De op basis van bewijs beoordeelde index van Claude Code-mods, plug-ins en het diepere gedrag dat ze veranderen.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-596-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <b>Nederlands</b> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Actieve index** · Laatste synchronisatie: `2026-10-12T21:29:43+08:00` (UTC+8)
> · Items: **596** · Toegevoegd in de nieuwste update: **0** · Implementatietalen: **13**

<sub>Elk item hieronder is automatisch verzameld, gefilterd en opnieuw gecontroleerd. Niets hiervan is betaalde promotie.</sub>

<a id="featured"></a>

## Uitgelicht van dit moment

<sub>Eén item per categorie, gerangschikt op bewijsniveau en sterren, bij elke update opnieuw berekend. Een ranglijst, geen aanbeveling; elke keuze linkt door naar de volledige kaart hieronder. Projecten die een screenshot of opname hebben gepubliceerd krijgen de voorkeur, zodat de balk visueel blijft.</sub>

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
<sub>Vind de spooktokens. Los ze op. Overleef compactie. Voorkom kwaliteitsverlies van de context.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74398 · TypeScript · 👁️ observed</sub>
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
- [Officieel: de eigen repositories en release notes van Anthropic](#officieel-de-eigen-repositories-en-release-notes-van-anthropic) — **16**
- [Mods: gebouwd met de modfunctionaliteit](#mods-gebouwd-met-de-modfunctionaliteit) — **482**
- [DSH- en Cordis-plug-inecosystemen](#dsh--en-cordis-plug-inecosystemen) — **86**
- [Schrijven, discussies en video's](#schrijven-discussies-en-videos) — **11**
- [Overige projecten](#overige-projecten) — **1**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150341 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Summary

Claude Code is een agentische coderingstool die in je terminal werkt, je codebase begrijpt en je helpt sneller te coderen door routinetaken uit te voeren, complexe code uit te leggen en git-workflows af te handelen — allemaal via opdrachten in natuurlijke taal.

<sub>🔧 Gebruik in code gevonden: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **150341** |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9482 · TypeScript · ✅ official · 2 天</summary>

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
| Stars        | **9482**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8253 · Python · ✅ official · 2 天</summary>

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
| Stars        | **8253**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242 天</summary>

##### 📝 Summary

Een door AI aangedreven beveiligingscontrole-GitHub-actie die Claude gebruikt om codewijzigingen te analyseren op beveiligingskwetsbaarheden.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6347**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 2 天</summary>

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
| Stars        | **1799**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Officiële Claude Code-mods van See Stack: live contextvenster-HUD, voice-overdeck en terminaltools. Installeer via: npx seestack

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **0**      |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `$.ui.notify` toegevoegd voor mods: geeft een native melding via je eigen…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Esc of een onderbreking tijdens een `UserPromptSubmit`-hook of de…
- [huaweicloud/huaweicloud-devkit](https://github.com/huaweicloud/huaweicloud-devkit) - Official Huawei Cloud plugin for AI agents — skills, MCP tools, safety…

</details>

<a id="mods"></a>

## Mods: gebouwd met de modfunctionaliteit

Elke vermelding hier toont bewijs dat de mogelijkheid voor Claude Code die in 2.1.287 is toegevoegd, wordt gebruikt: de vermelding tekent via `ui.render`, beheert een deelvenster, band of kaart, leest `$.ui.selection()`, start teamgenoten met `agent.spawn`, of zegt duidelijk dat het een mod is.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2541 · Python · 👁️ observed · 0 天</summary>

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
| Stars        | **2541**   |
| Last push    | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐514 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Communitycatalogus van openbare Claude Code-mods (functiehooks), gescand vanuit GitHub, met informatie over wat elke mod kan lezen, schrijven, uitvoeren of via het netwerk kan verzenden. Bekijk https://mods.aidojo.si/

<sub>🔧 Gebruik in code gevonden: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **514**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐200 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code-mods: plugins op basis van hooks die live regels boven de prompt, beveiligingen, panelen en games toevoegen. Contextbalk, gebruiksmeter, Codex-reviewbewaking, Markdown-preview, Spotify Now Playing en meer.

<sub>🔧 Gebruik in code gevonden: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **200**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐152 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stars        | **152**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐135 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **135**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐108 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Skins voor Claude Code: toolrijen met pictogrammen, kaarten met diffs, tabellen en Mermaid-diagrammen, een gebruiksbalk en vijftien thema's. /skin wisselt ze live.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **108**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐81 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **81**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stars        | **79**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐72 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **72**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

##### 📝 Summary

Claude Code-mods door Darrell Wang — banden boven de prompt, zonder modeltokens. Taiwanese／Amerikaanse aandelen-dashboard + meer volgt.

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
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐61 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Summary

Expert-Skills, agents, opdrachten, regels, hooks en uitvoerstijlen voor Claude Code — sessiecontinuïteit + moderne CLI-tools voor realistische ontwikkelworkflows

<sub>🔧 Gebruik in code gevonden: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | Shell                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **61**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

Verzameling van meer dan 100 mods die je met Claude Code kunt gebruiken.

<sub>🔧 Gebruik in code gevonden: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **50**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

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
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stars        | **28**     |
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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Een pixel-Pokémon die boven de prompt in Claude Code leeft

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

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
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐21 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Summary

Build, tests, console en SwiftUI-previews van Xcode binnen Claude Code

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **21**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Claude Code-mods: 21 stijlen en een volledige functieset die je inschakelt wanneer je ze nodig hebt, voor de terminal en de desktopapp. · Geef Claude met één klik een nieuwe stijl en beschik over een volledige set functies die je naar behoefte kunt inschakelen.

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
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

Tien Claude Code-mods, handleidingen voor beginners, prompts voor creatie, veilige demo's en een sjabloon om zelf te bouwen.

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
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code-mod: geplakte afbeeldingen en lange geplakte tekst boven de prompt vooraf bekijken

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **19**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Gebruik Codex, GLM en andere codeeragents als subagents van Claude Code.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **16**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: Clawd acts out what Claude is doing, above the prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **15**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

Twee Claude Code-mods: Codex computer-use-bridge en gecoördineerde Claude-sessies. Broncode, buildprompts, installatie en tests.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **14**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

Claude Code-mods: usage-band toont je limieten voor 5 uur/7 dagen, contextvenster en cache-hitpercentage boven de prompt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **13**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 Summary

Claude Code-mods die de vragen van Claude leesbaarder en makkelijker te beantwoorden maken (qa-guide).

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
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

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
| Stars        | **12**     |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

Tien open-source mods voor Claude Code: live panelen, banden, statusregels en beveiligingen voor toolaanroepen. Verbruiksmeter, launch codes, sessieafsluiting, boss fight, codehuisdier en meer.

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
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
| Stars        | **9**      |
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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Een UI rond je Claude Code- en Codex-terminals die je agents bouwen, zodat het enige model in je hoofd van jou is.

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

KOZMOS — live, visuele mods voor Claude Code (CLI + desktop): banden boven de prompt, zijbalken, een statusTicker, metgezellen, bewakers en geluid.

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
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

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
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Verzameling Claude Code-mods van ontwikkelaarsbroer. Taxipakket: meter, navigatie, flitspalen, dashcam

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
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Bekijken op youtube.com</a> · afspelen wordt geopend op de hostsite; GitHub kan deze niet inline insluiten</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 448</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods en de tools om ze te bouwen: eerst een builderskill, daarna mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - De Claude Code-harness die ik dagelijks gebruik, sinds dag één onder deze naam…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Gebruik Claude Mods om Claude Code een nieuw dak te geven: wijzig de binaire…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Vier Claude Code-mods: Cache Keeper, Recording Mode, Goal Meter en Collision…
- [HolyGrail/claude-mods](https://github.com/HolyGrail/claude-mods)
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code-mods die je prompts verbeteren en vertalen voordat Claude ze leest.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code-mods en -skills van Nekyia Labs, dagelijks gebouwd en gebruikt door…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Met bronnen geciteerde Obsidian-kennisbank over Claude Code-mods: hoe ze…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Een cockpit voor Claude Code: live planbalken, subagentstroken…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Een desktopapp-uiterlijk voor het terminaltranscript van Claude Code, als mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Een zijpaneel voor Claude Code: de subagenten die een sessie uitvoert, wat elk…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Zijbalkpaneel van Claude Desktop (Code-tabblad): toont alle onafgemaakte en…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Gebruiksbalk boven het invoervak van Claude Desktop (Code-tabblad): 5u /…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill die Claude Code-agents leert om Claude Mods (functie-hookplugins) te…
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Een Claude Code-mod waarmee Claude opdrachten kan uitvoeren waarvoor sudo nodig…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-mods, plug-ins en skills, installeerbaar vanuit één marktplaats.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (functie-hookplugins) voor Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - De mods-galerij van Baselane: Claude Code-mods, gecontroleerd en vastgezet.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Een beslissingswachtrij CLI/TUI voor mensen die met conversatieagenten werken.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code-paneelmod: agentenbord, bestandsboom en HWP/PDF-viewer…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Teken diagrammen, LaTeX-wiskunde en afbeeldingen van toolresultaten inline in…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code-mod die Edit- en Write-diffs in twee kolommen naast elkaar weergeeft.
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, tijdens het typen op het promptvak van Claude Code geschilderd.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Claude Code-mods van Ray Amjad: deelvensters, banden, promptbeveiligingen…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code-mods: het gebruikspaneel usage-hud van de pixelkrab + aanklikbare…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Een zwevende statuskaart voor Claude Code — model, context, rate limits…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods voor Claude Code: function-hook-plug-ins die live deelvensters en gedrag…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code-mods: screen-guard maskeert namen en geheimen terwijl je je scherm…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code-extensies. Ontgrendel de volledige kracht van Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod (plugin) die een zijpaneel toevoegt met Activity-, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panelen, vangrails en mods voor gebruiksgemak voor Claude Code: context…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Twee Claude Code-mods boven het promptvak: meter voor het contextvenster…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Laat het Claude Pro-abonnement langer meegaan: Claude Code-mods voor een…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lees de markdown-bestanden die Claude Code benoemt, weergegeven naast de…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code-mod: miniaturen van geplakte afbeeldingen boven de prompt, in elke…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code-mods: menu Claude Tools, Zen-modus, terminalthema.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Spraakcollega voor Claude Code. Bespreek dingen met een 3D-wolf, aangedreven…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code-mods: contextbalk, agentenpaneel, PDPA-vervaging.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code-mods: typing-speed, een live typsnelheidsmeter met statistieken per…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Vuurwerk voor Claude Code: elke toetsaanslag, toolaanroep, commit en geslaagde…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Een typetest voor de tijd dat Claude werkt. Een Claude Code-mod.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods voor Claude Code: deelvensters, opdrachten en hooks, gebouwd met de plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Ontdek Claude Code-mods, plugins en extensies met geanimeerde demo.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code-mod: mermaid-diagrammen inline in het transcript getekend.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods en skins voor Claude Code: een live voortgangsbalk voor de taken van…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Kleine Claude Code-mods (function-hook-plug-ins): session-switcher en meer.
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - Zie wat je volgende Claude Code-bericht kost: een live band boven de prompt met…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Zes Claude Code-mods: planningslimieten en context boven de prompt, een coach…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code-mods: mod-scout (vind de mods die je het vaakst zou gebruiken)…
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Twee Claude Code-mods om veel sessies tegelijk uit te voeren: een contextkaart…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code-mods ontdekken, inspecteren, in- en uitschakelen en…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Beste Claude Code-mods: zorgvuldig geselecteerd, gevalideerd, vastgezet.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code-plug-in: automatische routering van het Claude-model.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Kort grote tooluitvoer in voordat die de context van Claude Code vult.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code-mod: een live deelvenster met de GitHub-PR.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Zes mods voor Claude Code: geanimeerde Clawd-mascotte, balken voor…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Een marktplaats met mods voor Claude Code: een stapsgewijze debugger voor de…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-sourcemods voor Claude Code: deelvensters, statusregels, toastmeldingen…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Het beste alles-in-één modpakket voor Claude Code: gebruikslimieten en…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Speel YouTube Shorts af in je Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods voor Claude Code: Clawd, een kleine pixelmascotte die uitbeeldt wat Claude…
- [reporails/arcade](https://github.com/reporails/arcade) - Klassieke desktopgames als Claude Code-mods, gespeeld in een paneel terwijl…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods voor claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Eigen pluginmarketplace voor Claude Code-mods.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Een samengestelde lijst van Claude Code-mods, installeerbaar als…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code-mods op aanvraag — een vaardigheid die je gesprek leest en de…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Twee Claude Code-mods: cache-keeper en ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Een zeer uitgesproken Claude Code-plugin, ontworpen door een Rustacean die…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code-mods die een agent eerlijk houden — functie-hooks die de scope…
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - De Claude Code-mods die ik gebruik.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS-dashboard in notch-stijl voor Claude Code: gebruikslimieten, open…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude is aan het koken. Chat met je squad.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod voor Claude Code: promptcachebalk, volgende stappen, snelknoppen en…
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Kosten, tokens en plangrenzen van je codeeragents.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Een Claude Code-mod die je gebruikslimieten en uitgaven weergeeft in de balk…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code-mods: voortgangsbalken voor plannen, een overzicht van wat Claude…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Bekijk wat Claude Code op de achtergrond uitvoert: subagents, Codex-taken…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code-mods van MacLeod Labs: streams ontrafelt het verweven werk van een…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Eerste-dag veldnotities over Claude Code-mods op Windows: een…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: een debugger voor Claude Code-toolaanroepen.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code-mod: live status van GitHub pull requests.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Kleine kaarten die onder de Claude Code-prompt staan of in volledig scherm…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-mod: live kosten-, context- en planquotameters boven de prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Een Claude Code-mod die fan-out van subagents, prompts met zware context en…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills voor Claude in vijf pakketten.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We maken wat TECHNO, babyyyy 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-plugin en -mod: een AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Een Claude Code-mod die je globale skills, agents, regels en tools per repo met…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code-plugins (mods): wissel tussen meerdere Claude-accounts, bekijk…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Geteste Claude Code-mods die je met één opdracht installeert: guardrails voor…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods voor Claude Code: plugins gebouwd op function hooks.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Een aantal door mij gebouwde claude code-mods.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code-mods. touch-map: zie welke bestanden Claude heeft opgesomd…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Leer een vreemde taal terwijl je met Claude Code werkt.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Tell Claude what you want. Get it back built, tested, reviewed by another AI…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Beheert een lange Claude Code-sessie zodat jij dat niet hoeft te doen: houdt in…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - A Claude Code mod that keeps your prompt cache warm while you.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Live zijbalk voor kosten-, token- en contextgebruik voor Claude Code: een mod…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Doel, taken en agents boven je Claude Code-prompt — zonder configuratie.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code-mods voor echte Engineers.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Samenvatting van de terminalsessie van Claude Code, op het tabblad Code van de…
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Een verzameling Claude Code-mods van jack.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Een Claude Code-mod: een deelvenster met de taak van de sessie, wat je aandacht…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Een Claude Code-mod: vang pixel-art-Modsters in een idle game terwijl Claude…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zie welke bestanden elke Claude Code-agent in zijn context heeft, en hoeveel…
- [deejay-hub/sf-headless-band](https://github.com/deejay-hub/sf-headless-band) - Een Claude Code-mod voor Salesforce die laat zien welke Orgs verbonden zijn.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Maak van elke Claude Code-sessie een klein avontuur: generatieve muziek die de…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-mods voor de terminal en de desktopapp.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-skill + mod die Spaanse woorden toevoegt aan agent-antwoorden.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Je Alarum-gebeurtenissen boven de prompt van Claude Code: wat er zojuist is…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Je Floatee-backlog boven de prompt van Claude Code: voer je todo.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Een Claude Code-mod voor het vastleggen van gedachten tijdens het werk, ze…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Evangelion-achtige zijbalk voor Claude Code: context, quotum, activiteit, PR.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Een Claude Code-mod die het herstijlt als The Machine uit Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Claude Code-mod: een pixelartteam stelt voor elke taak het juiste model voor…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code-mod voor verplichte, geverifieerde DAG-workflows van…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Een Claude Code-mod: één deelvenster per subagent, de bestanden die ze aanraken…
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Code-mod (CC tint mod): kleur elk venster op basis van de repository…
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - Diverse mods die ik voor claude heb gemaakt en nuttig vind.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code-mod: sessiestatus, live Spec Kit-voortgang en beheer van…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Het contextvenster als een rij boven de prompt, weergegeven zoals Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Een live taak-HUD voor Claude Code Desktop: een strook boven de prompt terwijl…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code-plugin (mod) die de terminalinterface van Claude Code eruit laat…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Laat je aandacht niet afdwalen terwijl je wacht op het antwoord van Claude Code.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Veertien Claude Code-mods in één plugin, elk afzonderlijk in- en…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Een gratis, open-sourceplugin voor Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Geselecteerde Claude Code-mods, demo.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Claude Code-mods voor lange sessies: sitrep kadert de uitkomst en open vragen…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code-mods: samengesteld en getest, waarbij elke mod wordt geleverd met…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code-mods: automatische overdracht en voortgangsbalk.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-vaardigheden: een factchecker voor documentatie, een code-auditor…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Claude Code-mod die ruwe prompts herschrijft naar duidelijke prompts voordat je…
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Een Claude Code-mod die een live casebook bijhoudt van het bewijsmateriaal dat…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - De Claude Code-mods van Pedro La Rosa, in één pluginmarktplaats.
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Claude Code-mod: je gebruikslimieten van 5 uur en 7 dagen als live geanimeerde…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-buddyplugin: een ASCII-metgezel boven je prompt die je regels…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code-plug-in voor zichtbaarheid van tools per agent — subagents, skills…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - LaTeX-weergavemath in de terminal van Claude Code renderen: MathJax inbegrepen…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: een onofficiële Avengers-fanmod voor Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: een Claude Code-mod die de antwoorden van Claude en je prompts op…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Geef Claude een pak slaag als het fouten maakt — een stressverlichtende mod…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code-mods: kleine plugins voor livepanelen, kostenbewuste modelroutering…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code-mod &amp; plugin: gebruiksmonitor, tokentracker &amp; statusline.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Een Claude Code-mod die de kleine beslissingen overlaat aan een goedkoop…
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Vang de afdwaling in het denkproces van je Claude Code-sessie op, direct boven…
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [agukov-dev/token-meter](https://github.com/agukov-dev/token-meter) - Claude Code mod: rate limits, context and spend under the prompt.
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Marktplaats voor Claude Code-mods: agent-board, auto-model, session-collab +…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code-mod: voortgangsbalken voor gebruik (context, 5 uur, 7 dagen) en een…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code-mods: sessiestatistiekkaarten boven de prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Een geanimeerde braillekat boven de Claude Code-prompt.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code-mod: stuur goedkoop werk via een onderliggend Claude Code naar…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Een pixelkat boven je Claude Code-prompt die een testgesprek met een…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Een Claude Code-mod die een goed moment kiest om te verdichten, zodat het…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods voor Claude Code: tokenmeter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Algemene mods voor Claude Code: banden, deelvensters, toasts en hooks.
- [arifamir/nukey](https://github.com/arifamir/nukey) - Nukey the microwave: een Claude Code-mod en plug-inmarktplaats.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Je Claude-gebruikslimieten als een geanimeerde dorpsbewoner-gezondheidskaart…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code-mods voor het S2-team (de ather-marktplaats).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Korte workouts terwijl Claude werkt: een dagelijks doel, streaks, badges en…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Een gebruiksoverzicht voor Claude Code: uitgaven per model.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code-mod die de afteller van de promptcache in de voettekst toont en de…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now Playing-mod voor Claude Code: Apple Music en Spotify boven de prompt, met…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods voor Claude Code: Cache-klok, Blast Radius, suggesties, werklijst, Grill.
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods voor Claude Code: Clean View verbergt toolaanroepen en toont het plan als…
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - Een Claude Code-mod: het overzicht van georkestreerd werk, met uitvoeringen…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code-mods: Suggestion Spotlight toont waar de voorgestelde volgende…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Gewoon een uil voor je Claude Code.
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Mods voor Claude Code die ik heb gemaakt (panelen, opdrachten en hooks).
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - De originele Doom-engine met Freedoom, speelbaar binnen Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Small, readable Claude Code mods from the CorporateChittyChat channel.
- [colorfield/claude-ci-watch](https://github.com/colorfield/claude-ci-watch) - Claude Code mod: Pane and status line for the current branch.
- [colorfield/claude-lagoon-watch](https://github.com/colorfield/claude-lagoon-watch) - Claude Code mod: Pane with the Lagoon project.
- [colorfield/claude-port-guard](https://github.com/colorfield/claude-port-guard) - Claude Code mod: Stops Claude from killing, or running E2E tests against…
- [colorfield/claude-session-line](https://github.com/colorfield/claude-session-line) - Claude Code mod: Status line with context fill, model, effort, git branch or…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Bekijk elk bestand dat Claude aanraakt, zoals een pull request, zonder de…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Keep Claude Code on a plan: stages, approval gates and a file budget enforced…
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Claude Code-mod: een band boven de prompt met het aftellen van de promptcache…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - My personal Claude Code mods, customised for my own setup.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Claude Code-mods exclusief voor het d3nim-team.
- [dankelleher/claude-mod-pin-message](https://github.com/dankelleher/claude-mod-pin-message) - Claude Code-mod: een antwoord boven de prompt vastzetten, inklapbaar tot een…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Elf Claude Code-mods (functie-hookplugins) voor een homelabworkflow met veel…
- [davidcoulson/session-crew](https://github.com/davidcoulson/session-crew) - Een Claude Code-mod die de nevensessies die een desktopsessie start als…
- [daviddecorso/claude-mods](https://github.com/daviddecorso/claude-mods)
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Claude Code mods: an OpenSpec and sub agent board, hand over before compacting…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Een Tamagotchi die in Claude Code leeft: hij komt uit, eet de code die Claude…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bladwijzers en vim-achtige markeringen in Claude Code-terminalgesprekken…
- [DerpcatMusic/claude-context-controls](https://github.com/DerpcatMusic/claude-context-controls) - Claude Code mod: nested context / 5h / weekly rings, compaction threshold and…
- [devsomelife/somelife-claude-mods](https://github.com/devsomelife/somelife-claude-mods)
- [dgsantana/claude-mods](https://github.com/dgsantana/claude-mods) - Claude Code-mods: omp-port.
- [dhiroo-jpg/claude-mods](https://github.com/dhiroo-jpg/claude-mods) - クロードの使用量をチャット画面に表示.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Een Claude Code-mod: een balk boven de prompt met Claude-nieuws en de dringende…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Een Claude Code-mod: een bord met je andere sessies boven de prompt — wie op je…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code-mod: nadat een guard een toolaanroep blokkeert, stopt hij herkende…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code-mod: achtergrondtaken in één weergave, met voortgang en ETA.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code-mod: één inbox voor berichten van teamgenoten, benoemde subagents…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code-mod: legt sandboxblokkades uit en zet herhaalde blokkades om in…
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - A live wave board of your session.
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructies, vaardigheden, Pi-extensies en Claude Code-mods voor Pi, Codex en…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code-mods (functie-hook-plug-ins): session-meter en meer.
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi — a Claude Code mod: a mascot that reads the room above the prompt, with…
- [g761007/hudcade](https://github.com/g761007/hudcade) - Een pixel-art-HUD voor Claude Code: context, kosten, cache, agents en…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Zeven Claude Code-mods: savvy-progress, skins, filetree, cache-tax…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - A Claude Code mod for the desktop app: click a file reference in a reply and it…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Nuttige claude Code-mods.
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Privémarktplaats voor Claude Code-mods.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Duitstalige mods voor Claude Code: context-/cache-aanwijzingen, openstaande…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - De Claude Code-mods van Hector Bailey (pluginmarktplaats: hectorbailey).
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code-mod: drie volgende stappen na elk antwoord, in elke taal, met een…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-mod: hoe lang elk antwoord duurde, hoe lang Claude nadacht en…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude mods marketplace.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Een cockpit boven je Claude Code-prompt. De eend leest de meters af.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Omkeerbare redactie voor Claude Code: privéwaarden worden vervangen door…
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Claude Statusbalk.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Kleine Claude Code-mods: context- en plangebruiksmeters, een prompt-cachemeter…
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Claude Code-mods: contextbalk en de cyberdeck-HUD.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Leest je technische tekeningen automatisch in en modelleert ze vervolgens in…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Een plek voor mijn claude-mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Zijpaneel met contextgebruik: totaal, categorieën, groei per beurt, de grootste…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Zijpaneel met bestandenlijst: welke bestanden tijdens dit gesprek zijn…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Een pluizige 8-bit 毛毛 (zwart-wit Nederlandse hangoor) rent en springt boven het…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Zijpaneel met ‘wat ik heb gevraagd’: elke zin die de gebruiker tijdens dit…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Zijpaneel met tijdlijn: waar de tijd van deze beurt aan is besteed.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Zijpaneel met tokenverkeer: hoeveel tokens het hoofdgesprek elke keer naar…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - De eerlijke bonenpasta van claude code: na elke beurt zegt Claude zachtjes één…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Door bewijs aangestuurde checklist voor Claude Code: goedgekeurde plannen…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI Vereenvoudigd-Chinese vertaling (zelfbeheerde versie) — eigen…
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Onofficiële communitygids voor Claude Code-mods (functiehooks) in 6 talen, met…
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - Twee Claude Code-mods: sessieoverdrachten met antwoorden en het doorsturen van…
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph Ayoub.
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd leeft in een band boven je Claude Code-prompt: speelt de sessie na, toont…
- [kartollikaa/claude-android-emulator](https://github.com/kartollikaa/claude-android-emulator) - Claude Code mod: Android emulator and device screens inside Claude Code.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Een Claude-mod om de gesprekken tussen je Claude Code-sessies te lezen en eraan…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code-mods. PixBar: een pixelwezen boven je prompt dat meebeweegt met je…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code-mod: elke Claude Code-sessie in één zwevend venster, met live…
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - Enkele proof-of-concepts voor claude-code-mods.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Claude Code-mods, gepubliceerd als marktplaats.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: een livegrafiek van wat Claude Code weet.
- [l4ckofsleep/ccdetails](https://github.com/l4ckofsleep/ccdetails) - Claude Code mod: context fill, prompt-cache hit %, rate limits and cost above…
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Ten Claude Code mods: an animated pixel pet, Code Wrapped, lo-fi beats, plus a…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu.
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Een door de community samengestelde Claude Code Mods-gids: gebruiksscenario.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Een Claude Code-mod die laat zien wat Claude doet in de ondertitel van het…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, een onofficiële, door fans gemaakte pixelbegeleider die boven de Claude…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - Hoe vol de context van Claude is, wanneer de cache koud wordt en hoeveel van je…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Een pluizige zwarte kat boven je Claude Code-prompt.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code-mod: beantwoord Claude puntsgewijs, direct in de tekst.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Kleine mods voor Claude Code: runner-avatar, een kleine avatar die boven je…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - Kleine Claude Code-mods van het MateAI-kanaal.
- [matrac/burnline](https://github.com/matrac/burnline) - Claude Code mod: usage limits and task progress in one status line.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code-mod: een livepaneel met wat je AI-codeeragent nastreeft, aanneemt…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code-mod: deelvenster /sessions om sessies met hun gegevens op schijf te…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Zijpaneel voor Claude Code: bestanden die Claude heeft geschreven…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code-mod: voorspelt hoeveel er bij het resetten overblijft van je…
- [Miriam2040/nugget](https://github.com/Miriam2040/nugget) - Select any part of Claude.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Een rustig zijpaneel voor Claude Code: wat deze sessie doet, het plan, de…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Een gedimde tijdsaanduiding boven elke prompt en elk antwoord in het Claude…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Houd de code bij de specificatie: een Claude Code-mod en een GitHub Spec…
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - Claude Code-plugins voor sessies en geheugen: een Memory-paneelmod en een…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-mod die de todo-tools weer inschakelt voor modellen die ze…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code-mod die wacht op een veilige pauze en daarna je sessie overdraagt…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-mod: één regel per taak in de takenlijst boven de prompt, met de…
- [mwmrs/claude-mods](https://github.com/mwmrs/claude-mods)
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Speel Vier op een rij tegen een AI binnen Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code-mod: wanneer een andere code-agent een commit naar je repo maakt…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Claude Code-mod: houdt sessies licht — gebruiksregel, waarschuwing en één…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code-mod voor repo.
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code mod: one button per delegate-skills implementer.
- [ngxuanbminh/pr-watch](https://github.com/ngxuanbminh/pr-watch) - Claude Code mod: watch the GitHub PRs of the repo you.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Activeert de lange Monitor-bewakingen van Claude Code opnieuw wanneer ze…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Een beveiliging voor SQL in Claude Code: vraagt voordat Claude via een DB CLI…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Eén mod voor Claude Code, Windows en CJK als uitgangspunt: voorbeelden van…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - De beste Claude Code-mods, gesorteerd op wat ze voor je doen.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Twee Claude Mods voor Claude Code: garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Tijdstempels voor Claude Code: de tijd bij elk bericht, antwoord en elke…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Wijzigingen bijhouden voor Claude Code: zie precies wat Claude heeft gewijzigd…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Mods voor Claude Code: plugins met functiehooks die in elke repository werken.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Diverse mods en skills voor mijn Claude Desktop-configuratie.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Claude Code-mod: houdt het model, de tokens, tools en tijd van elke subagent…
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Claude Code-mod: elke subagent als een klein stokpoppetje in een zijpaneel, met…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods voor Claude Code: safety-guard blokkeert destructieve opdrachten en…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Een geanimeerde pixelart-Claude-krab voor Claude Code: hij beeldt uit wat…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code-mods, gepubliceerd als één pluginmarketplace.
- [ReDev1L/leanctx-colored](https://github.com/ReDev1L/leanctx-colored) - Claude Code mod: colored lean-ctx output.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-mod: push-ups om te doen terwijl Claude werkt. Geen tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code-mod Koreaanse editie, 6 varianten: aannamen vastleggen, eenvoudige…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - gewoon een lijst met mods die ik gebruik.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Drie dependencyvrije mods voor Claude Code: een responsieve statusregel, een…
- [Ron-Nefyodov/security-poc-mod](https://github.com/Ron-Nefyodov/security-poc-mod) - Uitsluitend een POC-Claude Code-mod voor expliciete, afgebakende lokale…
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - An open-source marketplace for Claude Code mods, with repository skills for…
- [RuahTechSolutions/code-buddy](https://github.com/RuahTechSolutions/code-buddy) - Claude Code-mod: stagingbewaking, impactbereik, bewerkingsreplay en een…
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - Mijn mods voor Claude Code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-mod: verandert het plan dat je in planmodus goedkeurt in een live…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Een zorgvuldig geselecteerde lijst van Claude Code-mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenvrije modus: helperagents draaien op Haiku, en grote bestanden en logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Een lofi-soundtrack die de sessie volgt: kalmte, focus, flow, plus signalen…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Leer terwijl Claude codeert: na een beurt die de code heeft gewijzigd…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Een bandopname van elke bewerking die Claude maakt: speel elke wijziging af…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Claude Code-mods: token-bar, je contextvenster en gebruikslimieten boven de…
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in the conversation…
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Missiecontrole voor Claude Code: live subagentvloot, token- en kostengebruik…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Showrins Claude Code-mods voor een productiever dagelijks werkritme.
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Persoonlijke Claude Code-mods.
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commitberichten met één klik voor Claude Code met een dansende pixel-art Malenia.
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - Een verzameling zelfgemaakte Claude Code-mods (pluginmarketplace).
- [sunwu51/english-assistant](https://github.com/sunwu51/english-assistant) - Claude Code Mods-plug-in voor contextuele Chinees-Engelse vertaling…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Een lokale opslagplaats voor Claude Code-mods.
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Claude Code-mod: zie je Cursor / VS Code-bestand en selectie boven de prompt…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — een Claude Code-mod die je Claude-plangebruik toont.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Een Claude Code-mod die de huidige sessie in een paneel toont: elke prompt, het…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Een Claude Code-plugin-marketplace met mods: function-hooks-plugins die banden…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Claude Code-mods van Toptaab.
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Kleine, leuke en nuttige mods voor Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code-mod: geanimeerde voortgangsbalk en voltooiingssamenvatting voor…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drie kleine Claude Code-mods: zie wanneer je subagents klaar zijn, zet…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Zeg &quot;Ik ben de draad kwijt&quot; en Claude legt het vorige antwoord opnieuw uit in…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stel Claude een zijvraag in een venster naast je werk.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code plugin: prompt-cache countdown, cache hit rate, context weather and…
- [wablevaibhav/claude-mods](https://github.com/wablevaibhav/claude-mods)
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Mijn Claude Code-mods.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Een Claude Code-mod: een markeerstift voor antwoorden, een zijpaneel voor…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter) - Deze Claude Code-mod toont een kaart boven de prompt.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — when context outgrows its shell, shed it into the folder and keep going.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod voor Claude Code: afgeschermde geheimen, taken, controles en CI, dagboek…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code-plug-in: je Claude Pro/Max-gebruikslimieten met een prognose van…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods voor Claude Code. agent-crew: zie je subagents werken als een live…
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - Terminal-zijpaneelmods voor Claude Code — agenttracering, token-aangedreven…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Een live taakbord voor Claude Code: plan voordat je bouwt, volg elke taak…
- [yuu1111/claude-agents-skills](https://github.com/yuu1111/claude-agents-skills) - Claude Code mod that loads Agent Skills from the shared .agents/skills…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Een zorgvuldig samengestelde verzameling van de beste hulpmiddelen voor de…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Een Claude Code-plugin die toont wat er gebeurt — contextgebruik, actieve…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Mooie, zeer aanpasbare statusregel voor Claude Code CLI met…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle onderdelen van de systeemprompt van Claude Code, 27 ingebouwde…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Meer dan 45 tips om het meeste uit Claude Code te halen, van basis tot…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — genereer Xiaohongshu-carrousels en…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Bekijk de diff van je codeeragent in een terminalvenster en stuur…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Uitgebreide statusregelplugin voor Claude Code met contextgebruik…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Bouw mods voor Claude Code: koppel elke aanvraag, wijzig elk antwoord, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Een uitgebreid statuslinedashboard voor Claude Code — sessiegegevens…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: houd de CO₂-voetafdruk van je Claude Code-sessies bij.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Een esthetische statusline voor Claude Code door awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Openbare Claude Code-skills en mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash-opdrachten en handleidingen voor Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legale gratis LLM APIs en codeagents — zichzelf twee keer per week bijgewerkt…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Snelle kostencalculator zonder afhankelijkheden en aanpasbare statusregel voor…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live voetbalstanden, wedstrijden en ranglijsten voor de competitie die je…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill die je codeagent verandert in een expert op het gebied van…
- [Tripstack-Corp/spyc](https://github.com/Tripstack-Corp/spyc) - A Rust TUI file commander where the AI agent in the side pane can query the…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebedstijden, Hijri-datum, adhkar, dagelijkse ayah, sunnah-vasten, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Persoonlijke configuratie van Claude Code, met versiebeheer binnen ~/.claude…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · Onderzoeksgraph — DeepSeek Harness-plug-in voor…
- [chrisnguyen1211/pillrdotlol](https://github.com/chrisnguyen1211/pillrdotlol) - Every coding agent and every API key, in one pill at the edge of your Mac.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Pluginbundel voor Claude Code, pi en DeepSeek Harness: statusbalk-HUD…
- [luucas42/agent-flow](https://github.com/luucas42/agent-flow) - A live workflow panel for Claude Code: the main model, the advisor and every…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Lichtgewicht statusregel voor Claude Code — één Bash-script van ongeveer 170…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-plug-ins die ik elke dag gebruik: skills en mods, opgeschoond zodat…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analyze Claude Code token usage and costs from local conversation logs and…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Onofficiële mods voor het tabblad Code van Claude Desktop — usage-pet: een…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark)-brug, zelf ontwikkeld (geen fork): streamingantwoordkaart…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marktplaats voor Claude Code-plugins en -skills om mods voor de game Hytale te…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tokenbeheer voor Claude Code: het topmodel stuurt aan, de uitvoering gaat naar…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Viewer met gesplitst paneel voor Claude Code in Windows Terminal en tmux: de…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository voor Claude Code Awesome Media-mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Bespaar op Claude Code- en Codex-tokengebruik: stuurt opzoekingen en testruns…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configureerbare Claude Code-statusregel voor Linux, WSL, Windows en macOS, met…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Toon de statusregel van Claude Code met snelheidslimieten, huidige map en…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Een statusregel en tokenregel voor Claude Code: context, gebruik van 5 uur en…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - de vriendelijke statusregel voor Claude Code waarmee je aan alles kunt prutsen…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agentteams. Onder controle. Strikte werkerslimieten, live…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code-add-ons: kleurgecodeerde tabstatus-dotwatcher + ingebouwde…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definieerbare softwarefabrieken voor Claude Code op herdr…
- [0xSerachu/claude-shortcuts](https://github.com/0xSerachu/claude-shortcuts) - Explore and quiz yourself on all Claude Code shortcuts with categorized…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code-statusregel voor macOS en Linux, verpakt als een…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows PowerShell status line for Claude Code: 5-hour and weekly limits with…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code-statusregel in Lua, met een live Neovim-speelplaats.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionele Claude Code-statusregel: sessieduur, kosten in meerdere valuta…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Abonnementsbewuste statusregel voor Claude Code.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Statusregel voor Claude Code in het Spaans: taak, skills, context met…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Kleurrijke statusregel voor Claude Code: planningslimieten, context, kosten en…
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Claude Code-statusregel voor Windows: totaalaantal tokens, kosten tegen…
- [gvart/claude-config](https://github.com/gvart/claude-config) - My Claude Code setup: agent-monitor mod, skills, agents and a one-command…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Statusbalk op één regel voor Claude Code: model, git, context, tokens, kosten…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Voorbeeldafbeeldingen in Claude Code: beweeg de muis over een chip onder een…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Persoonlijke Claude Code-configuratie: machtigingen, statusline, MCP-servers.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code-statusregel met rijen voor het agentenpaneel.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchroniseer de taken van Claude met Fizzy.do voor realtime inzicht voor het…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: draagbare Claude Code-configuratie — globale regels…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Toont een gedetailleerde, kleurgecodeerde statusbalk voor Claude Code met…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Volg de status van Claude Code met een compact dashboard dat context, kosten…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Statusbalk van twee regels voor een terminalcodeeragent: map, git, PR, model…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code-statusline-hook — houdt tokengebruik en context bij over sessies…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, de pixelart-metgezel van Claude Code, en atelier, de vangrail voor…
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Marketplace Claude Code de MSF Supply : mods sélectionnés et figés par commit.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code-omgevingsinstallatieprogramma: skills, statusregel, hooks…
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Rich multi-line status line for Claude Code — live usage limits (5h + weekly)…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Nacho.
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Meerdere regels tellende Claude Code-statusregel: contextbalk, git-branch…
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - Plugins en mods van OrihuelaConde voor Claude Code.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code-statusregel voor macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Bewaak de status van Claude Code vanuit je macOS-menubalk met…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skills en mods voor Claude Code en Cowork — projecttracker, referentiedocument…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code-statusregel voor Windows (PowerShell): gebruiksbalken, aftellingen…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks en een statusregel voor Claude Code, plus een…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Een statusregel van twee regels voor Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Aangepaste statusregel voor Claude Code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Starter-harnas voor Claude Code: hooks, statusregel, lokale modellen…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Draagbare configuratie voor Claude Code (statusregel + installatieprogramma).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Een klein dashboard voor Claude Code: context %, aftellen van de cache, gebruik…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Aangepaste terminalstatusbalk voor Claude Code: model, map, git-status…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Houd het contextgebruik van Claude Code, sessiekosten en resets van…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - modverzameling voor Claude Code.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code-statusregel: de huidige model-ID, de hostnaam, een aanklikbare…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code-vaardigheid (VS Code, Windows): afbeeldingsvoorbeelden en knoppen…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Synchronisatie van Claude Code-configuratie op gebruikersniveau tussen meerdere…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Een Claude Code-statusregel met kleurverlopende voortgangsbalken…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Een Claude Code-statusregel: map, git-branch, model, gebruik van het…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Proactieve AI-geheugen- en snelheidslimietmonitor…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-hooks, subagents en statuslines: opensourceverzamelingen en -tools…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code-statusregel die realtime tokengebruik en geschat energieverbruik…
- [previsioncystolith584/ai-video-downloader](https://github.com/previsioncystolith584/ai-video-downloader) - Download videos from major platforms and automatically add translated…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - Een door Deno aangedreven statusregel voor Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods voor Claude Code: panelen, banden en maatjes gebouwd op functie-hooks.
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Claude Code-achtige UI-bundel voor de Pi-codeeragent — toolweergave…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Geef taken door tussen je Claude Code-sessies.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Dit is een MCP-server om MODS te beheren, de modulaire cross-platformtool voor…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex- en Claude Code-skill voor het vertalen van CK3-mods met een lokale LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source-mods en andere extensies voor Claude Code.
- [alan-oliv/team8](https://github.com/alan-oliv/team8) - A live browser console for Claude Code agent teams — every teammate.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code-statusregel: de schoonheid van CCometixLine + de…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: vind wat je Claude Code steeds opnieuw vraagt en maak er een mod…

</details>

<a id="dsh-cordis"></a>

## DSH- en Cordis-plug-inecosystemen

DeepSeek Harness en Cordis bereiken dezelfde plek vanuit een andere richting: voor hen is de plug-in het modmechanisme, dus een plug-in daar is het equivalent van een mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74398 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74398**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐134601 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **134601** |
| Last push    | 2026-10-12 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100691 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **100691** |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82387 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **82387**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35769**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25517 · Python · 🔎 inferred · 0 天</summary>

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
| Stars        | **25517**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8659 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) Web-plug-inaggregatie-ecosysteem · Alles is een plug-in, verspreid via de Creative Workshop｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8659**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4385 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Officieel sterk aanbevolen TUI-plugin van DSH — hoge prestaties, lage overhead, schattige pixelwalvis, soepele muisinteractie. Installatie met één opdracht via npm. / Officieel door DSH aanbevolen TUI-plugin: hoge prestaties, laag verbruik, schattige pixelwalvis, soepele muisinteractie en installatie met één klik via npm

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4385**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3060 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Tauri-desktopversie | Installer van slechts 8 MB, geen omgevingsconfiguratie nodig, vooraf ingestelde plugins, Windows / macOS / Linux.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3060**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1601 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Een beveiliging vóór uitvoering voor AI-codeagents. Blokkeert destructieve Git- en bestandssysteemopdrachten, plus veelvoorkomende pogingen om toegang te krijgen tot gevoelige bestanden, voordat een toolaanroep wordt uitgevoerd. Ondersteunt Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode en Pi.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1601**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/GanyuanRan/Aegis">GanyuanRan/Aegis</a></b> · ⭐1343 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Make AI coding agents architecture-aware: baseline-first, evidence-verified, drift-checked, and safe across long tasks.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1343**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-skills` · `ai-agents` · `ai-coding` · `architecture-driven-development` · `awsome-coding-plugin` · `baseline-first` · `claude-code` · `codex`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ganyuanran--aegis/4581f8f71af5092d.png" width="100%" alt="GanyuanRan/Aegis screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1179 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **1179**   |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐552 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **552**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/text2future/flowix">text2future/flowix</a></b> · ⭐459 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **459**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-memory` · `claude-code` · `codex-cli` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `hermes-agent`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/9fc65a8848fe78ee.png" width="100%" alt="text2future/flowix screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/ea3f84c8693d4236.gif" width="100%" alt="text2future/flowix animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐374 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Gratis provider voor webzoekopdrachten voor DeepSeek Harness - DuckDuckGo-backend, geen API-sleutel nodig

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **374**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
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
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐230 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness-skin-/achtergrond-/themabundelplugin (dsh-plugin) — 8 Mirage-thema's, accentkleur per gebruiker, Achtergronden 2.0, importeren/exporteren van themabundels en deellinks, favorieten en willekeurige selectie, volledig geïmplementeerd met een native tokensysteem.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **230**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **204**    |
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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐181 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH)-plug-in voor back-ups en herstel — exporteer, importeer, migreer en synchroniseer je volledige DSH-configuratie, plug-ins, MCP-servers, vaardigheden en werkplek. Migratie naar een andere machine met één klik.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **181**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐180 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Runtimebewijs waarmee agents hotspots in applicatie- en native code, GPU-kernels en inferentiestacks kunnen traceren, profileren en wegwerken.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **180**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness-plugin voor previewbare sessiemigratie tussen presets. Overdrachten met een vast schema behouden de status, de intentie van het bronmodel en onopgeloste afbeeldingen; de oorspronkelijke sessie blijft onaangeraakt.

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
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐142 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **142**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Wordt geïnstalleerd met 27 engineering- en productiviteitsvaardigheden uit mattpocock/skills v1.3.1, zonder dat je vaardigheden handmatig hoeft te installeren. Gebouwd met 40 miljard tokens; deze plug-in biedt boven op de oorspronkelijke vaardigheden tien keer meer ontwikkelproductiviteit en helpt beginners sneller met deze vaardighedenbundel aan de slag. Volledige ondersteuning voor GitHub-issues; Markdown is een previewversie; GitLab wordt momenteel niet ondersteund. Bedankt voor je gebruik en steun 💗

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **137**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐121 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness-desktopdierenplugin: een energieke walvismascotte op het dashboard die je gezelschap houdt tijdens het coderen 🐋 Ondersteunt DSH-desktop 0.2.0-rc.2 en oudere Web-versies (desktop pet / mascot, local-first)

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **121**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Aik358/dsh-auto-memory">Aik358/dsh-auto-memory</a></b> · ⭐111 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Proactive associative memory for DSH: system-prompt recall before the model speaks, three-layer auto-consolidation, skill crystallization, and Astra-style context management - handoff ledgers, PLAN whiteboard, water-level sensing. Local-first, model-agnostic, zero deps. 主动联想记忆+Astra 式上下文管理：自动唤回/自动沉淀/技能固化/交接账本与白板跨窗口续命/水位感知。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **111**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `context` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `memory` · `npm` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/ba11cddac1ec16d1.png" width="100%" alt="Aik358/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/a44325f737275ef4.gif" width="100%" alt="Aik358/dsh-auto-memory animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **69**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/leantoken">morluto/leantoken</a></b> · ⭐64 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Code intelligence for agents: find the code that matters and keep your context window and tokens lean.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Rust                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **64**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `ai-coding` · `code-intelligence` · `code-navigation` · `code-retrieval` · `code-search` · `codebase-indexing` · `coding-agents` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--leantoken/38b3e8f4a7b20aea.jpg" width="100%" alt="morluto/leantoken screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cloader/dsh-taskboard">cloader/dsh-taskboard</a></b> · ⭐59 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

deepseekharness 任务看板插件

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **59**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `kanban` · `task-board`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cloader--dsh-taskboard/cfd9efd4514a0b8f.png" width="100%" alt="cloader/dsh-taskboard screenshot"></td>
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
| Last push    | 2026-10-12 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Taakbewuste contextophaling en levenscyclusregistratie van de werkruimte voor AI-coding agents: vind, organiseer en volg continu de meest relevante documenten, code en media voor de huidige taak. Volledig lokaal, geen modelaanroepen, geen netwerk. Taakbewuste contextophaling en levenscyclusregistratie van de werkruimte voor AI-coding agents. Vind, organiseer en volg de werkruimtecontext die het meest relevant is voor de huidige taak — lokaal, deterministisch, zonder modelaanroepen en zonder netwerk.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **54**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

NekroNXT: een multiplatform-groepschatagentsysteem op basis van DeepSeek Harness (DSH)｜Een door DSH aangedreven multiplatform-groepschatagentsysteem

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **35**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness-plug-in: koppel automatisch het contextvenster van een model, toon de bron van de capaciteit, ondersteun bulkconfiguratie via selectievakjes, beheer bestaande vensters en handmatige bewerking.

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
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH-sessienavigatie

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-toolbox-ui">Imzl-zl/dsh-toolbox-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Toolboxpaneel voor DeepSeek Harness Web: MCP-manager (tools en JSON Schema, marktplaats, import, werkruimtekopie) en skillsmanager (bereiken en overschrijven, in-/uitschakelen, automatische modelaanroep, skillhub.cn-marktplaats).

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp` · `skill-manager` · `skills`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-toolbox-ui/bab6fdf6979d2501.png" width="100%" alt="Imzl-zl/dsh-toolbox-ui screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 52</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Een samengestelde lijst met de beste geweldige AI-plugins voor AI-assistenten…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH-plug-in — gratis OpenCode Zen-modellen voor DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-pluginmarkt / DSH Plugin Marketplace: blader, installeer en update alle…
- [arcships/rutis](https://github.com/arcships/rutis) - Een pluginruntime voor software die zichzelf herhaalt — de basis waarop agents…
- [hanelalo/browser-bridge](https://github.com/hanelalo/browser-bridge) - 让你的agent真的像你一样操控你的浏览器窗口.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Uitgelichte directory van DeepSeek Harness (DSH)-plugins — meer dan 280…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH-plugin: Git Bash-shell voor alle agentmodi op Windows.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH-web-GUI-plug-inverzameling (DeepSeek Harness) — taakmeldingen…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Door de community geselecteerde DeepSeek Harness (dsh)-plugins, tools, skills…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - Beheer van updates voor het hoofdprogramma en plugins van DeepSeek Harness…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Een echte PowerPoint, geen HTML. Vertel je AI wat er behandeld moet worden en…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Lokale codekennisgrafiek en contextharness voor codeagents.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Maak van de lokaal ingelogde modellen in de WorkBuddy-desktopapp.
- [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) - DSH 插件：一个设置面板，统一管理 MCP 服务器、技能、场景、记忆、子智能体人格、AGENTS.md…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH-plugin: drie tools voor zoeken binnen de site, zoeken in de volledige…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Altijd actieve compatibiliteitstests voor DeepSeek Harness-plug-ins: exacte…
- [chipweaver/veripower](https://github.com/chipweaver/veripower) - An open-source agent flow from natural language spec through Verilog RTL and…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness-hostplug-in die projectdocumenten en langetermijngeheugen als…
- [PianoPrince/dsh-workspace-mover](https://github.com/PianoPrince/dsh-workspace-mover) - 拖拽真迁移 DSH 会话跨工作区：批量移动、分组合并、挂错归位、回收站、备份恢复 + 对话内 agent 工具；步步备份可回滚，零 token / True…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Röntgen voor DeepSeek Harness-plugins: gedeclareerde mogelijkheden versus…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Werkruimte met meerdere mappen: laat de agent van DSH (DeepSeek Harness) niet…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH-plugin: modellen uit de WorkBuddy-desktopapp aansluiten op DeepSeek…
- [Noob-stupid/dsh-github-login](https://github.com/Noob-stupid/dsh-github-login) - DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Deep links naar sessies + volledige sessie-export (markdown/JSON) +…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH-plug-in: een IDE-achtig Git-toolvenster als native dsh-better-sidebar-tab…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Geef DeepSeek Harness Agent native handen en voeten om GitHub te bedienen!
- [laoduu/DeepSeek-Harness-yizi-themes](https://github.com/laoduu/DeepSeek-Harness-yizi-themes) - 19 hoogwaardige stijlthema.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Verificat standaard zonder afhankelijkheden voor DeepSeek Harness…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness plugin ecosystem: 86 open-source plugins in a 101-repo family…
- [possible055/agentshim](https://github.com/possible055/agentshim) - High-performance, capability-aware repository tools and process execution for…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode op DeepSeek Harness — DSH-plug-in die OpenCode Zen + Go gratis…
- [YeqingTang/dsh-session-flow](https://github.com/YeqingTang/dsh-session-flow) - DSH 会话信息流重设计插件：跨会话档案柜，折叠时间线 / 血缘树 / 检索 / 双模式摘要 / ZIP 导出 / 实时跟踪.
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marktplaats voor plug-ins van derden en beheerder van de beveiligde…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx is een mensgerichte, uitbreidbare desktopwerkplek: gesprekken, notities…
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - DeepSeek Harness op desktop uitvoeren zonder tokenkosten — een gratis…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Een volledig uitgeruste codeeragent voor DeepSeek Harness — workflows in Claude…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH-plugin: toont het saldo van je DeepSeek-account onderaan de linkerzijbalk…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Bots-werkbank: Cordis-plugin die de sdk-bots-orkestratiegateway verbindt…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — communitytoolkit voor lokale implementatie en beheer voor DeepSeek…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH)-webplugin: markt-dashboard-zijtab voor monitoring — drie…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Onafhankelijke plugins en tools van derden voor DeepSeek Harness, onderhouden…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Gebruik gratis modellen van OpenCode Zen in DeepSeek Harness met anonieme…
- [Asukayanamii/learn-cordis4py](https://github.com/Asukayanamii/learn-cordis4py) - Cordis 插件框架的 Python 复刻：上下文与作用域、fiber 生命周期、五种事件分发、服务依赖注入、配置校验、YAML 装载器.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness-plug-in: verandert de fout bij het provisionen van de ACL voor…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Voortgangsbeoordeling voor autonome doelsessies van dsh: stel de lus uit…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - dsh-plug-in: zet een afgebroken lengtestop om in het…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plug-ins die zichzelf opruimen: een Swift 6-port van het…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Een Rust-plug-inruntime met een door Verus geverifieerde levenscycluskernel en…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Arkme-account-, record-, chat- en interwoven-moments-integratie voor DeepSeek…

</details>

<a id="writing"></a>

## Schrijven, discussies en video&#x27;s

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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

<a id="other"></a>

## Overige projecten

Vermeldingen die het modoppervlak aanraken maar zelf geen mods zijn; ze blijven zichtbaar in plaats van verborgen te worden.

<details>
<summary>📦 <b><a href="https://github.com/rajmand/claude_mods">rajmand/claude_mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Overige projecten`                                               |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **0**      |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

</details>

<a id="projects-by-implementation-language"></a>

## Projecten per implementatietaal

The ecosystem is concentrated in Python and TypeScript, but typed clients keep appearing in other languages. This table is generated from the entries themselves.

| Taal       | Items | Voorbeelden                                                                                                   |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 386   | `anthropics/claude-code`, `anthropics/claude-code-action`, `see-stack/claude-code-mods`                       |
| JavaScript | 76    | `huaweicloud/huaweicloud-devkit`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`          |
| Python     | 39    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 10    | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 9     | `persiyanov/herdr-reviewr`, `Tripstack-Corp/spyc`, `cc-friend/ccost`                                          |
| Go         | 5     | `kartollikaa/claude-android-emulator`, `backstabslash/goccc`, `esengine/DeepSeek-Reasonix`                    |
| Swift      | 3     | `chrisnguyen1211/pillrdotlol`, `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`        |
| PowerShell | 2     | `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win`                                   |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1     | `crafts69guy/claude-statusline.nvim`                                                                          |
| MDX        | 1     | `jkf87/mod-guide`                                                                                             |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Last updated · 2026-10-12T21:29:43+08:00</sub>
