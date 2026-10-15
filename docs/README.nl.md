<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Geweldige Claude-mods">
</p>

<h1 align="center">Geweldige Claude-mods</h1>

<p align="center"><b>De op basis van bewijs beoordeelde index van Claude Code-mods, plug-ins en het diepere gedrag dat ze veranderen.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-612-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <b>Nederlands</b> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Actieve index** · Laatste synchronisatie: `2026-10-16T01:31:05+08:00` (UTC+8)
> · Items: **612** · Toegevoegd in de nieuwste update: **0** · Implementatietalen: **11**

<sub>Elk item hieronder is automatisch verzameld, gefilterd en opnieuw gecontroleerd. Niets hiervan is betaalde promotie.</sub>

<a id="featured"></a>

## Uitgelicht van dit moment

<sub>Eén item per categorie, gerangschikt op bewijsniveau en sterren, bij elke update opnieuw berekend. Een ranglijst, geen aanbeveling; elke keuze linkt door naar de volledige kaart hieronder. Projecten die een screenshot of opname hebben gepubliceerd krijgen de voorkeur, zodat de balk visueel blijft.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9523 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2566 · Python · 👁️ observed</sub>
<sub>Vind de spooktokens. Herstel ze. Overleef compactie. Voorkom kwaliteitsverlies van de context.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74928 · TypeScript · 👁️ observed</sub>
<sub>🌊 De oorspronkelijke agent harness. Implementeer intelligente swarms met meerdere spelers, coördineer autonome workflows en bouw conversationele AI-systemen. Met…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## Inhoud

- [Wat een Claude Code-mod is](#wat-een-claude-code-mod-is)
- [Hoe items worden beoordeeld](#hoe-items-worden-beoordeeld)
- [Officieel: de eigen repositories en release notes van Anthropic](#officieel-de-eigen-repositories-en-release-notes-van-anthropic) — **16**
- [Mods: gebouwd met de modfunctionaliteit](#mods-gebouwd-met-de-modfunctionaliteit) — **479**
- [DSH- en Cordis-plug-inecosystemen](#dsh--en-cordis-plug-inecosystemen) — **109**
- [Schrijven, discussies en video's](#schrijven-discussies-en-videos) — **8**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151028 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Summary

Claude Code is een agentische coderingstool die in je terminal werkt, je codebase begrijpt en je helpt sneller te coderen door routinetaken uit te voeren, complexe code uit te leggen en git-workflows af te handelen — allemaal via opdrachten in natuurlijke taal.

<sub>🔧 Gebruik in code gevonden: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **151028** |
| Last push    | 2026-10-14 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9523 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **9523**   |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8284 · Python · ✅ official · 0 天</summary>

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
| Stars        | **8284**   |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6390 · Python · ✅ official · 245 天</summary>

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
| Stars        | **6390**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1812 · Shell · ✅ official · 0 天</summary>

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
| Stars        | **1812**   |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>Meer in deze categorie</b> <sub>· 4</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `$.ui.notify` toegevoegd voor mods: geeft een native melding via je eigen…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Esc of een onderbreking tijdens een `UserPromptSubmit`-hook of de…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.

</details>

<a id="mods"></a>

## Mods: gebouwd met de modfunctionaliteit

Elke vermelding hier toont bewijs dat de mogelijkheid voor Claude Code die in 2.1.287 is toegevoegd, wordt gebruikt: de vermelding tekent via `ui.render`, beheert een deelvenster, band of kaart, leest `$.ui.selection()`, start teamgenoten met `agent.spawn`, of zegt duidelijk dat het een mod is.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2566 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

Vind de spooktokens. Herstel ze. Overleef compactie. Voorkom kwaliteitsverlies van de context.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2566**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐822 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Custom Claude Code Mods that I need

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **822**    |
| Last push    | 2026-10-14 |
| First listed | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐590 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **590**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐254 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **254**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐211 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **211**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐204 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

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
| Stars        | **204**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐192 · TypeScript · 👁️ observed · 11 天</summary>

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
| Stars        | **192**    |
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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐115 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **115**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐98 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 Gebruik in code gevonden: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **98**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐91 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stars        | **91**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stars        | **80**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐68 · TypeScript · 👁️ observed · 12 天</summary>

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
| Stars        | **68**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code-mods: live voortgangsbalken voor het plan boven de prompt

<sub>🔧 Gebruik in code gevonden: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | JavaScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **54**     |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐33 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **33**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐29 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **29**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code-mods: menu Claude Tools, Zen-modus, terminalthema's, inspannings- en modusbediening

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
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

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
| Stars        | **22**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 12 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

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
| Stars        | **16**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

LINE in Claude Code: de enil TUI als een Claude Code-mod

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
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Stars        | **14**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Stars        | **14**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 2 天</summary>

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
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 5 天</summary>

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
| Stars        | **11**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 Summary

Laat het Claude Pro-abonnement langer meegaan: Claude Code-mods voor een nauwkeurig gebruikspaneel, kortere shell-uitvoer en geen herhaalde bestandslezingen. De mods gebruiken nul tokens.

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
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 29 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 1 天</summary>

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
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
| Stars        | **8**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Bekijken op youtube.com</a> · afspelen wordt geopend op de hostsite; GitHub kan deze niet inline insluiten</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Panelen, vangrails en mods voor gebruiksgemak voor Claude Code: context, gebruik, live activiteit, meldingen, veiligheidsregels, promptcoach, commandocentrum.

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
| Last push    | 2026-10-06 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Danovich/turntype">Danovich/turntype</a></b> · ⭐7 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Summary

Een typetest voor de tijd dat Claude werkt. Een Claude Code-mod.

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `claude-mods` · `typing` · `typing-game` · `typing-practice` · `typing-test`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/mod-store">hellosverre/mod-store</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Een appstore voor Claude Code-mods, binnen Claude Code: /mods om 2.700 mods te bekijken, zoeken en installeren, of vraag Claude er een te vinden

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
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `mods`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--mod-store/8bcf88eb3b07c96f.gif" width="100%" alt="hellosverre/mod-store screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--mod-store/8bcf88eb3b07c96f.gif" width="100%" alt="hellosverre/mod-store animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 445</sub></summary>

- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Claude Code-mods door Darrell Wang — banden boven de prompt, zonder…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Claude Code-mods van Ray Amjad: deelvensters, banden, promptbeveiligingen…
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Expert-Skills, agents, opdrachten, regels, hooks en uitvoerstijlen voor Claude…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods en de tools om ze te bouwen: eerst een builderskill, daarna mods.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Vier Claude Code-mods: Cache Keeper, Recording Mode, Goal Meter en Collision…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - De Claude Code-harness die ik dagelijks gebruik, sinds dag één onder deze naam…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Gebruik Claude Mods om Claude Code een nieuw dak te geven: wijzig de binaire…
- [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) - A measured tool-call firewall for AI agents: allow, ask or deny before the…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Build, tests, console en SwiftUI-previews van Xcode binnen Claude Code.
- [BrianHuang813/clawd-actor](https://github.com/BrianHuang813/clawd-actor) - Claude Code-mod: Clawd beeldt boven de prompt uit wat Claude doet.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Met bronnen geciteerde Obsidian-kennisbank over Claude Code-mods: hoe ze…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code-mods die je prompts verbeteren en vertalen voordat Claude ze leest.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code-mods en -skills van Nekyia Labs, dagelijks gebouwd en gebruikt door…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Een zijpaneel voor Claude Code: de subagenten die een sessie uitvoert, wat elk…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Zijbalkpaneel van Claude Desktop (Code-tabblad): toont alle onafgemaakte en…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Gebruiksbalk boven het invoervak van Claude Desktop (Code-tabblad): 5u /…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (functie-hookplugins) voor Claude Code.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Een zwevende statuskaart voor Claude Code — model, context, rate limits…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill die Claude Code-agents leert om Claude Mods (functie-hookplugins) te…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-mods, plug-ins en skills, installeerbaar vanuit één marktplaats.
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [davekiss/mods](https://github.com/davekiss/mods) - Claude Code-mods van Dave Kiss.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Een beslissingswachtrij CLI/TUI voor mensen die met conversatieagenten werken.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - De mods-galerij van Baselane: Claude Code-mods, gecontroleerd en vastgezet.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Zes Claude Code-mods: planningslimieten en context boven de prompt, een coach…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod (plugin) die een zijpaneel toevoegt met Activity-, Files…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude Code-mod die Edit- en Write-diffs in twee kolommen naast elkaar weergeeft.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code-mods: het gebruikspaneel usage-hud van de pixelkrab + aanklikbare…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code-mods op aanvraag — een vaardigheid die je gesprek leest en de…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods voor Claude Code: function-hook-plug-ins die live deelvensters en gedrag…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code-mods: screen-guard maskeert namen en geheimen terwijl je je scherm…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods en skins voor Claude Code: een live voortgangsbalk voor de taken van…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code-extensies. Ontgrendel de volledige kracht van Claude.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Twee Claude Code-mods boven het promptvak: meter voor het contextvenster…
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Eigen pluginmarketplace voor Claude Code-mods.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lees de markdown-bestanden die Claude Code benoemt, weergegeven naast de…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow voor Claude Code: een rustige checklist boven de prompt die het…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code-mods: contextbalk, agentenpaneel, PDPA-vervaging.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code-mod: miniaturen van geplakte afbeeldingen boven de prompt, in elke…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Spraakcollega voor Claude Code. Bespreek dingen met een 3D-wolf, aangedreven…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Twee Claude Code-mods om veel sessies tegelijk uit te voeren: een contextkaart…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code-mods: typing-speed, een live typsnelheidsmeter met statistieken per…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods voor Claude Code: deelvensters, opdrachten en hooks, gebouwd met de plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Ontdek Claude Code-mods, plugins en extensies met geanimeerde demo.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code-mod: mermaid-diagrammen inline in het transcript getekend.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Kleine Claude Code-mods (function-hook-plug-ins): session-switcher en meer.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code-mods: mod-scout (vind de mods die je het vaakst zou gebruiken)…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [nuromirzak/nibbl](https://github.com/nuromirzak/nibbl) - A tiny pixel pet that nibbles your bugs. Lives above your Claude Code prompt.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Een aantal door mij gebouwde claude code-mods.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code-mods ontdekken, inspecteren, in- en uitschakelen en…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Beste Claude Code-mods: zorgvuldig geselecteerd, gevalideerd, vastgezet.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code-mods voor echte Engineers.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code-plug-in: automatische routering van het Claude-model.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Zes mods voor Claude Code: geanimeerde Clawd-mascotte, balken voor…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-sourcemods voor Claude Code: deelvensters, statusregels, toastmeldingen…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code-mod: beantwoord Claude puntsgewijs, rechtstreeks in de tekst.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods voor Claude Code: Clawd, een kleine pixelmascotte die uitbeeldt wat Claude…
- [reporails/arcade](https://github.com/reporails/arcade) - Klassieke desktopgames als Claude Code-mods, gespeeld in een paneel terwijl…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods voor claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Een Claude Code-mod die je globale skills, agents, regels en tools per repo met…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Geteste Claude Code-mods die je met één opdracht installeert: guardrails voor…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Een samengestelde lijst van Claude Code-mods, installeerbaar als…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Twee Claude Code-mods: cache-keeper en ctx-mod.
- [xsyetopz/claudetto](https://github.com/xsyetopz/claudetto) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code-mods die een agent eerlijk houden — functie-hooks die de scope…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Een Claude Code-mod voor het vastleggen van gedachten tijdens het werk, ze…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Kweek een thee-ei dat langzaam intrekt terwijl je code schrijft · Kweek een…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code-plugin (mod) die de terminalinterface van Claude Code eruit laat…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Bekijk wat Claude Code op de achtergrond uitvoert: subagents, Codex-taken…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Eerste-dag veldnotities over Claude Code-mods op Windows: een…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-mod: live kosten-, context- en planquotameters boven de prompt.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-plugin en -mod: een AI-native SDLC.
- [tiger42/claude-mods](https://github.com/tiger42/claude-mods) - My personal Claude mods.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Geef Claude een pak slaag wanneer het fouten maakt — een…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, met bewijsstukken. Een plug-in die werk plant, delegeert en…
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar for Claude Code: usage limits, context, model, cost, git and session…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Leer een vreemde taal terwijl je met Claude Code werkt.
- [AmiTu1020/mods-context-auto-handoff-public](https://github.com/AmiTu1020/mods-context-auto-handoff-public) - Claude Code mod：context 快滿時自動寫交接卡、開新對話接手（可設定項目與檢查，交接中鎖工具）.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Live zijbalk voor kosten-, token- en contextgebruik voor Claude Code: een mod…
- [Azertyuiop442/deepshrink](https://github.com/Azertyuiop442/deepshrink) - Proven-freshness context store for coding agents - mtime-verified reuse, TF-IDF…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [cga-management/claude-decisions](https://github.com/cga-management/claude-decisions) - Claude Code mod: a Decisions pane that tracks the open decisions Claude raises…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Een Claude Code-mod die een doorlopende lijst bijhoudt van de openstaande…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Houd Claude Code op koers: fasen, goedkeuringspoorten en een bestandsbudget dat…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zie welke bestanden elke Claude Code-agent in zijn context heeft, en hoeveel…
- [daydeda/daymods](https://github.com/daydeda/daymods) - Small, independent mods for Claude Code: install only the ones you want.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-mods voor de terminal en de desktopapp.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-skill + mod die Spaanse woorden toevoegt aan agent-antwoorden.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Je Alarum-gebeurtenissen boven de prompt van Claude Code: wat er zojuist is…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Je Floatee-backlog boven de prompt van Claude Code: voer je todo.
- [HoyngM/claude-mods](https://github.com/HoyngM/claude-mods) - Mods for Claude Code.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code-mod voor verplichte, geverifieerde DAG-workflows van…
- [iuliandita/mods](https://github.com/iuliandita/mods) - Claude Code mods you can install one at a time.
- [joaquinsalinas06/crabbus](https://github.com/joaquinsalinas06/crabbus) - See what every Claude Code subagent is really doing — two-way messaging, tokens…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Het contextvenster als een rij boven de prompt, weergegeven zoals Claude Code…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code-mod: kiest het model en de redeneerinspanning van elke subagent.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Laat je aandacht niet afdwalen terwijl je wacht op het antwoord van Claude Code.
- [LudovicLaloux/agent-crew](https://github.com/LudovicLaloux/agent-crew) - Claude Code mod: see your parallel agents as costumed pixel-art Clawds, in a…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Een gratis, open-sourceplugin voor Claude Code.
- [marulimo/claude-code-mods](https://github.com/marulimo/claude-code-mods) - Claude Code の Mod 6本（Codex/Devin への依頼、AI 使用率、X 投稿、AI の振り分け、ハッシュタグの流し見、待ち時間の雑談）.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nonputtipong/claude-code-prompt-enhancer](https://github.com/nonputtipong/claude-code-prompt-enhancer) - ✻ A Claude Code mod that rewrites your rough draft into a clear, project-aware…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-vaardigheden: een factchecker voor documentatie, een code-auditor…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [restante/claudio-tts](https://github.com/restante/claudio-tts) - Make Claude Code talk back 🔊 Local text-to-speech for Claude Code replies…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-buddyplugin: een ASCII-metgezel boven je prompt die je regels…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [swicken/tiller](https://github.com/swicken/tiller) - Local daemon + Claude Code mods for spawning, messaging and controlling agent…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: een Claude Code-mod die de antwoorden van Claude en je prompts op…
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code-mods: kleine plugins voor livepanelen, kostenbewuste modelroutering…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code-mod &amp; plugin: gebruiksmonitor, tokentracker &amp; statusline.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [wonjoonSeol-WS/claude-side-insights](https://github.com/wonjoonSeol-WS/claude-side-insights) - Side panel for Claude Code (a mod): checks every question got answered, walks…
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude Code-mods: EMCC (Every Mod Claude Code), een samengestelde, geteste…
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mods for Claude Code: live panes, bands and hooks. A plugin marketplace.
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [0x5421/plan-progress](https://github.com/0x5421/plan-progress) - A fork of zycck/claude-mods plan-progress: live progress bars for Claude Code…
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [aiob3/claude-grounds-demo](https://github.com/aiob3/claude-grounds-demo) - Demo for claude-grounds (Claude Code mods): a median() bug with text sort and a…
- [akirachangtw/claude-mods](https://github.com/akirachangtw/claude-mods) - Claude-mods.
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Een geanimeerde braillekat boven de Claude Code-prompt.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Een pixelkat boven je Claude Code-prompt die een testgesprek met een…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Een Claude Code-mod die een goed moment kiest om te verdichten, zodat het…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods voor Claude Code: tokenmeter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code mod: your plan.
- [andras-gyarmati/claude-task-progress](https://github.com/andras-gyarmati/claude-task-progress) - Claude Code mod: progress bars above the prompt for long tasks, background…
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Algemene mods voor Claude Code: banden, deelvensters, toasts en hooks.
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt.
- [arcnessai/arcdr](https://github.com/arcnessai/arcdr) - herdr mobile &amp; web client that shows what your Claude Code mods report — answer…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Je Claude-gebruikslimieten als een geanimeerde dorpsbewoner-gezondheidskaart…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Korte workouts terwijl Claude werkt: een dagelijks doel, streaks, badges en…
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [bahaospanov/skills](https://github.com/bahaospanov/skills) - De Claude Code-mods van Bakhtiyar Ospanov: plug-ins gebouwd op functiehooks.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now Playing-mod voor Claude Code: Apple Music en Spotify boven de prompt, met…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [Br4inergy/claude-hands-off](https://github.com/Br4inergy/claude-hands-off) - Your AI agent can&#x27;t push to a repo, deploy a project or drop a table that isn&#x27;t…
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [Br4inergy/claude-loadout](https://github.com/Br4inergy/claude-loadout) - Loadout, the mod manager for Claude Code: audits every mod and every update…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods voor Claude Code: Cache-klok, Blast Radius, suggesties, werklijst, Grill.
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Gewoon een uil voor je Claude Code.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Claude Code mods for the ai-architect.tools harness: one concern per mod, state…
- [chinayuren2022-2025/claude-english-coach](https://github.com/chinayuren2022-2025/claude-english-coach) - Claude Code mod: practise English by working with Claude in English only…
- [CiroVilmer/jev-agent-router](https://github.com/CiroVilmer/jev-agent-router) - Claude Code mod that picks the model and effort of every subagent from its task…
- [CoderDayton/vii-mods](https://github.com/CoderDayton/vii-mods) - Claude Code mods for memory, safety and workflow.
- [creamcitycyber/usage-meter](https://github.com/creamcitycyber/usage-meter) - Claude Code mod for monitoring usage.
- [Crinitys/copy-list](https://github.com/Crinitys/copy-list) - Claude Code mod: a pane of paths and //Next: lines with copy buttons.
- [danhere/session-usage](https://github.com/danhere/session-usage) - Claude Code mod: context window usage above the prompt, split by category.
- [danieldeusing/capi-cc-mod](https://github.com/danieldeusing/capi-cc-mod) - Capi: a Claude Code mod that teaches you a language above the prompt, one…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - My collection of claude mods.
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dtakamiya/claude-code-mods](https://github.com/dtakamiya/claude-code-mods) - Claude Code Mods marketplace.
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [eduojeda/claude-last-answer](https://github.com/eduojeda/claude-last-answer) - Claude Code mod: re-read the agent.
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - claude용 mods.
- [ezekohon/context-meter](https://github.com/ezekohon/context-meter) - Claude Code mod: live context window and token usage under the prompt.
- [FabianFTR/claude-mods](https://github.com/FabianFTR/claude-mods)
- [fabiopbarbieri/agents-progress](https://github.com/fabiopbarbieri/agents-progress) - Claude Code mod: progress bar above the prompt and a live panel of subagents.
- [flaviorg/claude-mods](https://github.com/flaviorg/claude-mods) - Hub marketplace for my original Claude Code mods: tripwire, canopy, crew…
- [flaviorg/crew](https://github.com/flaviorg/crew) - Claude Code mod: a live panel of the subagents Claude delegates to — model…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [gwarf/claude-plugins](https://github.com/gwarf/claude-plugins) - Claude Code mods by Baptiste Grenier: a plugin marketplace.
- [h1048576/claude-mods](https://github.com/h1048576/claude-mods) - Claude Code mods - show-mode plugin.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Een live uitgavenmeter voor Claude Code: de kosten van de sessie met subagents…
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-effort-switch](https://github.com/HuliLulu46/cc-effort-switch)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-mod: hoe lang elk antwoord duurde, hoe lang Claude nadacht en…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian.
- [ilya-paskhover/claude-code-mods](https://github.com/ilya-paskhover/claude-code-mods) - Claude Code mods: turn-pulse (last-turn summary band) and notes.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jepperip/claude-session-todo](https://github.com/jepperip/claude-session-todo) - Claude Code mod: a live session todo pane the agent keeps current.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Zijpaneel met contextgebruik: totaal, categorieën, groei per beurt, de grootste…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Zijpaneel met bestandenlijst: welke bestanden tijdens dit gesprek zijn…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Een pluizige 8-bit 毛毛 (zwart-wit Nederlandse hangoor) rent en springt boven het…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Zijpaneel met ‘wat ik heb gevraagd’: elke zin die de gebruiker tijdens dit…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Zijpaneel met tijdlijn: waar de tijd van deze beurt aan is besteed.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Zijpaneel met tokenverkeer: hoeveel tokens het hoofdgesprek elke keer naar…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - De eerlijke bonenpasta van claude code: na elke beurt zegt Claude zachtjes één…
- [jjayakumar-gif/compass-claude-mods](https://github.com/jjayakumar-gif/compass-claude-mods)
- [joaopasbento/claude-mods](https://github.com/joaopasbento/claude-mods) - Claude Code mods: token-weather, a live forecast of the context window above…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd leeft in een band boven je Claude Code-prompt: speelt de sessie na, toont…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Een mod die antwoorden en meldingen van Claude Code voorleest met VOICEVOX /…
- [kakwok/claude-mods](https://github.com/kakwok/claude-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [kinetikoy/claude-mod-issue](https://github.com/kinetikoy/claude-mod-issue) - A Claude Mod for showing an Issue panel inside Claude Code (WIP).
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Niceties/quality of life improvement Claude mods.
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high.
- [Lerma4/claude-code-mods](https://github.com/Lerma4/claude-code-mods) - A collection of mods for Claude Code.
- [levy-n/claude-code-mods](https://github.com/levy-n/claude-code-mods) - Claude Code mods for long sessions: context-handoff.
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Een door de community samengestelde Claude Code Mods-gids: gebruiksscenario.
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Claude Code mod: guards the 1-hour prompt cache of idle sessions — countdown…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Een Claude Code-mod die laat zien wat Claude doet in de ondertitel van het…
- [macollins27/owner-rep](https://github.com/macollins27/owner-rep) - A Claude Code mod that watches the coding agent for the person who owns the…
- [MagnusPladsen/claude-mods](https://github.com/MagnusPladsen/claude-mods) - Personal global Claude Code mods.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Communitymods voor Claude Code: beveiligingen, panelen en opdrachten die binnen…
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace.
- [migmorales22/claude-stock-ticker](https://github.com/migmorales22/claude-stock-ticker) - A Claude Code mod: /stock AAPL keeps one stock.
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [mori-tt/claude-mods-demo](https://github.com/mori-tt/claude-mods-demo)
- [mreedr/gh-linear-parse-mod](https://github.com/mreedr/gh-linear-parse-mod) - Claude Code mod: GitHub PR and Linear links band above the prompt.
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code mod: context window usage in the prompt footer mode slot.
- [mtmtian/cc-mods](https://github.com/mtmtian/cc-mods) - Claude Code mods (function-hook plugins) forked from other authors, kept in one…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-mod die de todo-tools weer inschakelt voor modellen die ze…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code-mod die wacht op een veilige pauze en daarna je sessie overdraagt…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-mod: één regel per taak in de takenlijst boven de prompt, met de…
- [mukuro696-dev/guard-and-band-for-claude-code](https://github.com/mukuro696-dev/guard-and-band-for-claude-code) - Small self-made Claude Code mods: guard-a.
- [mvacoimbra/claude-mods-hub](https://github.com/mvacoimbra/claude-mods-hub) - One /mods pane for every installed Claude Code mod.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Speel Vier op een rij tegen een AI binnen Claude Code (/connect-four).
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code-mod: wanneer een andere code-agent een commit naar je repo maakt…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code-mod voor repo.
- [nasmarr/claude-mods](https://github.com/nasmarr/claude-mods) - A small catalog of Claude Code mods.
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [NathapolDev/al-status-line](https://github.com/NathapolDev/al-status-line) - AL Status for Claude Code mods.
- [necobit/claude-lupin-title](https://github.com/necobit/claude-lupin-title) - A Claude Code mod: typewriter clacks, a full-screen title card and excuses with…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph.
- [niksavis/handily](https://github.com/niksavis/handily) - Claude Code-mods die je werkitems, taken en sessies tonen, voor elke tracker.
- [nxhung1610/claude-odometer](https://github.com/nxhung1610/claude-odometer) - Claude Code mod that shows your 5-hour and 7-day usage limits right under the…
- [oscar-guggiana-neto-neocol/claude-mods](https://github.com/oscar-guggiana-neto-neocol/claude-mods)
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Twee Claude Mods voor Claude Code: garde-du-corps.
- [patle1/claude-mods](https://github.com/patle1/claude-mods) - My Claude Code mods, skill and agents, with an installer for cloud sessions.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: een Claude Code-mod. Permanente worktrees met een alleen-lezen…
- [pekala/linear-review-link](https://github.com/pekala/linear-review-link) - Claude Code mod: the current branch.
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live zijpaneel met sessiestatistieken voor het Code-tabblad van de…
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [poska-lab/cc-work-buddy](https://github.com/poska-lab/cc-work-buddy) - Unofficial Claude Code mod: a little Claude above your prompt that shows what…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pstahel/token-weather-claude-code-mod](https://github.com/pstahel/token-weather-claude-code-mod) - A live dashboard of your context window and prompt cache above the Claude Code…
- [pupuchan1/dopa-ide](https://github.com/pupuchan1/dopa-ide) - Claude Code mod: a dopamine band above the prompt, fireworks and a fanfare when…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [ramonfabrega/mods](https://github.com/ramonfabrega/mods) - Claude Code mods: hooks modules that change the interface.
- [reedchan7/claude-mods-pulse](https://github.com/reedchan7/claude-mods-pulse) - Pulse: live TTFT, tok/s, prompt-cache hit rate and usage left in Claude Code.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-mod: push-ups om te doen terwijl Claude werkt. Geen tokens.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: een praktijkgids voor Claude Code-mods, van ELI5 tot…
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-mod: verandert het plan dat je in planmodus goedkeurt in een live…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Een zorgvuldig geselecteerde lijst van Claude Code-mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenvrije modus: helperagents draaien op Haiku, en grote bestanden en logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Een lofi-soundtrack die de sessie volgt: kalmte, focus, flow, plus signalen…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Leer terwijl Claude codeert: na een beurt die de code heeft gewijzigd…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Een bandopname van elke bewerking die Claude maakt: speel elke wijziging af…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [schudarin/chudarin-context-mod](https://github.com/schudarin/chudarin-context-mod) - A Claude Code mod: a side panel that shows what fills your context, how much of…
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [ShadowDog007/claude-mods](https://github.com/ShadowDog007/claude-mods)
- [shhac/claude-mods](https://github.com/shhac/claude-mods) - Mods for Claude Code.
- [shichang4fun/claude-mods](https://github.com/shichang4fun/claude-mods) - Personal Claude Code mods, published as a plugin marketplace.
- [sijunnoh/claude-usage-status](https://github.com/sijunnoh/claude-usage-status) - Claude Code mod that shows 5-hour/7-day usage limits, time until reset…
- [sinozu/claude-code-mods](https://github.com/sinozu/claude-code-mods)
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker.
- [skaterino/claude-mods](https://github.com/skaterino/claude-mods) - Claude-Code-Mods: Verbrauchs-Statuszeile mit Auto-Neustart (verbrauch) und…
- [sngymgt/claude-mods](https://github.com/sngymgt/claude-mods)
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commitberichten met één klik voor Claude Code met een dansende pixel-art Malenia.
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — een Claude Code-mod die je Claude-plangebruik toont.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Onofficiële Claude Code-mods van tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Een Claude Code-mod die de huidige sessie in een paneel toont: elke prompt, het…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Een Claude Code-plugin-marketplace met mods: function-hooks-plugins die banden…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace.
- [tinkybeatz/tinky-claude-mods](https://github.com/tinkybeatz/tinky-claude-mods) - Claude Code mods: interface and behaviour plugins built on function hooks.
- [toml0006/claude-session-stats](https://github.com/toml0006/claude-session-stats) - Claude Code mod: live pane of your session.
- [Ty-Stev/ty-mods](https://github.com/Ty-Stev/ty-mods) - Ty.
- [tyastonotaufiq/claude-mods](https://github.com/tyastonotaufiq/claude-mods)
- [utsavsingh899/claude-obsidian-bridge](https://github.com/utsavsingh899/claude-obsidian-bridge) - A Claude Code mod: one Obsidian note for each Claude session, with replies from…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code-mod: geanimeerde voortgangsbalk en voltooiingssamenvatting voor…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drie kleine Claude Code-mods: zie wanneer je subagents klaar zijn, zet…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Zeg &quot;Ik ben de draad kwijt&quot; en Claude legt het vorige antwoord opnieuw uit in…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stel Claude een zijvraag in een venster naast je werk.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vlle/job-hunt-cc](https://github.com/vlle/job-hunt-cc) - A Claude Code mod that lets you find job and tailor your resume(s).
- [warstellar/claude-mods](https://github.com/warstellar/claude-mods) - Small mods for the Claude Code desktop app.
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wsouto/claude-status-bar-mod](https://github.com/wsouto/claude-status-bar-mod) - Claude Code mod: model, effort, folder, git state, pull request and a stacked…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code-plug-in: je Claude Pro/Max-gebruikslimieten met een prognose van…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods voor Claude Code. agent-crew: zie je subagents werken als een live…
- [yishu-ziyu/plain-steps](https://github.com/yishu-ziyu/plain-steps) - Claude Code mod：替你读完每一步的命令和输出，只留下判断要用的一行.
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zcharef/session-topic](https://github.com/zcharef/session-topic) - Claude Code mod that names each session after what it is about, and shows the…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [Ztubben/claude-code-mods](https://github.com/Ztubben/claude-code-mods) - Mods and other artifacts for Claude Code.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Een zorgvuldig samengestelde verzameling van de beste hulpmiddelen voor de…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Een Claude Code-plugin die toont wat er gebeurt — contextgebruik, actieve…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Mooie, zeer aanpasbare statusregel voor Claude Code CLI met…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle onderdelen van de systeemprompt van Claude Code, 27 ingebouwde…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI-videovaardigheid voor Claude Code &amp; Codex — filmische productvideo.
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Meer dan 45 tips om het meeste uit Claude Code te halen, van basis tot…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — genereer Xiaohongshu-carrousels en…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Bekijk de diff van je codeeragent in een terminalvenster en stuur…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Uitgebreide statusregelplugin voor Claude Code met contextgebruik…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Bouw mods voor Claude Code: koppel elke aanvraag, wijzig elk antwoord, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Een uitgebreid statuslinedashboard voor Claude Code — sessie-informatie…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: houd de CO₂-voetafdruk van je Claude Code-sessies bij.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Openbare Claude Code-skills en mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash-opdrachten en handleidingen voor Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legale gratis LLM APIs en codeeragents — zichzelf twee keer per week…
- [sageox/ox](https://github.com/sageox/ox) - The hivemind for AI coding agents — persistent team context recorded once and…
- [congmnguyen/claude-code-wsl2-setup](https://github.com/congmnguyen/claude-code-wsl2-setup) - Guides and scripts for Claude Code on WSL2: screenshot paste, Windows…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live voetbalstanden, wedstrijden en ranglijsten voor de competitie die je…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill die je codeagent verandert in een expert op het gebied van…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebedstijden, Hijri-datum, adhkar, dagelijkse ayah, sunnah-vasten, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Persoonlijke configuratie van Claude Code, met versiebeheer binnen ~/.claude…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Pluginbundel voor Claude Code, pi en DeepSeek Harness: statusbalk-HUD…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Draagbare Claude Code-toolkit voor .NET DDD/Clean Architecture: strikte…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Draagbare globale configuratie voor Claude Code: aangepaste skills…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Onofficiële mods voor het tabblad Code van Claude Desktop — usage-pet: een…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-plug-ins die ik elke dag gebruik: skills en mods, opgeschoond zodat…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Een aanpasbare statusregel voor Claude Code met een editor met slepen en…
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Een visueel bord voor je Claude Code-agents: bekijk sessies, subagents en…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marktplaats voor Claude Code-plugins en -skills om mods voor de game Hytale te…
- [GerardoFC8/claude-subagent-statusline](https://github.com/GerardoFC8/claude-subagent-statusline) - Real-time sub-agent delegation tracking in your Claude Code statusline.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Viewer met gesplitst scherm voor Claude Code in Windows Terminal en tmux: de…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository voor Claude Code Awesome Media-mods.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [wpfleger96/claude-code-status-line](https://github.com/wpfleger96/claude-code-status-line) - Real-time status bar for Claude Code showing model, context usage, session…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [ahwenu/claude-cafe-mods](https://github.com/ahwenu/claude-cafe-mods) - ☕ Claude Code の Mod 集。cafe-files: 喫茶店風のファイルペイン（/files）.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Een versterkte, kleurgegradeerde statusregel zonder afhankelijkheden voor…
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agentteams. Onder controle. Strikte limieten voor het aantal werkers…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [31c0c3/claude-statusline](https://github.com/31c0c3/claude-statusline) - One-line Claude Code status line in bash and jq: context, cache, limits, cost.
- [aaltw/claude-code-statusline](https://github.com/aaltw/claude-code-statusline) - Catppuccin Mocha powerline statusline for Claude Code — model, tokens, context…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games.
- [alvsheeesh/claude-toolbox](https://github.com/alvsheeesh/claude-toolbox) - Portable Claude Code toolbox: my mods (dock, Clean View, Burn Meter…) as a…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code plugin marketplace with baloo: skills, an agent that verifies…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionele statusregel voor Claude Code: sessieduur, kosten in meerdere…
- [dentaco/claude-starter](https://github.com/dentaco/claude-starter) - Alex Znamenskiy.
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Een statusregel voor Claude Code: context, limieten en het tempo van deze week…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust.
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [hawkymisc/claude-plugins](https://github.com/hawkymisc/claude-plugins) - Hawkie.
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Voorbeeldafbeeldingen in Claude Code: beweeg de muis over een chip onder een…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [jamesyoung-dev/claude-cache-countdown](https://github.com/jamesyoung-dev/claude-cache-countdown) - Keeps claude_statusline_plus.
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jdmalter/claude-code-statusline](https://github.com/jdmalter/claude-code-statusline) - A muted three-line status line for Claude Code, in bash for Git Bash on Windows.
- [JesseWebDotCom/claude-overview](https://github.com/JesseWebDotCom/claude-overview) - A live Claude Code side pane: Claude and Codex usage limits, context breakdown…
- [kouui/magic-claude-code-plugin](https://github.com/kouui/magic-claude-code-plugin) - awesome claude code plugin marketplace: skills, mods, ...
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code-statusline-hook — houdt tokengebruik en context bij over sessies…
- [mderiano/claude-cockpit](https://github.com/mderiano/claude-cockpit) - Cockpit for Claude Code: a live, colorful pane showing commands &amp; output, file…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [milan44i/claude-setup](https://github.com/milan44i/claude-setup) - An installable Claude Code setup: self-healing TypeScript hook…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [mr-pmillz/claude-code-pmillz-statusline](https://github.com/mr-pmillz/claude-code-pmillz-statusline) - a status line variant for claude code that shows useful info.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Aangepaste statusregel voor Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Universele Multi-Protocol StatusLine, Context Self-Learning &amp; Dinotty Plugin…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Proactieve AI-geheugen- en snelheidslimietmonitor…
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-hooks, subagents en statuslines: opensourceverzamelingen en -tools…
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods voor Claude Code: panelen, banden en maatjes gebouwd op functie-hooks.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Geef taken door tussen je Claude Code-sessies.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: vind wat je Claude Code steeds opnieuw vraagt en maak er een mod…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Dit is een MCP-server om MODS te beheren, de modulaire cross-platformtool voor…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex- en Claude Code-skill voor het vertalen van CK3-mods met een lokale LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source-mods en andere extensies voor Claude Code.
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability.
- [Isllanrx/status_cli](https://github.com/Isllanrx/status_cli) - Status line in Rust for Claude Code, Codex CLI and Antigravity CLI: usage…

</details>

<a id="dsh-cordis"></a>

## DSH- en Cordis-plug-inecosystemen

DeepSeek Harness en Cordis bereiken dezelfde plek vanuit een andere richting: voor hen is de plug-in het modmechanisme, dus een plug-in daar is het equivalent van een mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250344 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 Gebruik in code gevonden: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                               |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **250344** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74928 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74928**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4634 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Officieel sterk aanbevolen TUI-plugin van DSH — hoge prestaties, lage overhead, schattige pixelwalvis, soepele muisinteractie. Installatie met één opdracht via npm. / Officieel door DSH aanbevolen TUI-plugin: hoge prestaties, laag verbruik, schattige pixelwalvis, soepele muisinteractie en installatie met één klik via npm

<sub>🔧 Gebruik in code gevonden: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                               |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4634**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐695 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

Een samengestelde lijst met de beste geweldige AI-plugins voor AI-assistenten, waaronder Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi en meer. https://hol.org/plugins

<sub>🔧 Gebruik in code gevonden: `README.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                               |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | Python                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **695**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐264520 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **264520** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101316 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **101316** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐83980 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **83980**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35804 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35804**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30949 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Een moderne desktopoplossing voor het plugin-ecosysteem van DeepSeek Harness (DSH). Alles is een «plugin», en de desktop zelf is ook een «plugin».

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30949**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25656 · Python · 🔎 inferred · 2 天</summary>

##### 📝 Summary

Distilly — Leid af hoe zij denken tot herbruikbare Skills voor elke Agent of Bot. Voorheen Colleague Skill（原同事 Skill）.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25656**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18884 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **18884**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9204 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **9204**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8792 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **8792**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6647 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6647**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/loopx-project/loopx">loopx-project/loopx</a></b> · ⭐6317 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

A control plane with a durable state kernel for long-horizon agents and teams. Keep work moving and improving across sessions, with less human attention.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6317**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-16 |

🏷 `agent-control-plane` · `agent-harness` · `ai-agents` · `claude-code` · `codex` · `dsh-plugin` · `local-first` · `long-horizon-agents`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/8582e0735bb2d9e1.webp" width="100%" alt="loopx-project/loopx screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/34519ef8d110de64.gif" width="100%" alt="loopx-project/loopx animation"><br><sub>geanimeerde opname · <a href="https://raw.githubusercontent.com/loopx-project/loopx/main/docs/assets/personal-workspace/loopx-dashboard-launch.mp4">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4193 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, side chat, Git, and sub-agent pages.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4193**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>geanimeerde opname · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Video openen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3442 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Beantwoord me met HTML — een agentvaardigheid die moeilijke vragen beantwoordt met een HTML-pagina van één pagina die je daadwerkelijk kunt lezen. Laat AI Agent complexe vragen beantwoorden met één HTML-pagina.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3442**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/edison7009/EchoBird">edison7009/EchoBird</a></b> · ⭐3305 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Manage ChatGPT, Codex CLI, and Claude Code accounts and track quota in one place. Use multi-model smart routing with priority and automatic failover. Install AI tools and deploy local LLMs in one click.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Rust                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3305**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `dsh-plugins` · `kimi-code` · `openclaw` · `opencode`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/edison7009--echobird/0d743c36df1b336d.png" width="100%" alt="edison7009/EchoBird screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3015 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **3015**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1563 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

AI 小说创作软件：把灵感、角色、世界观、大纲、章节写作、审稿和修稿组织成可控流程；提供 Windows/macOS 桌面版，支持本地和在线模型。AI Novel Writing Software: Organizes inspirations, characters, worldbuilding, outlines, chapter drafting, review, and revision into a controllable workflow. Features desktop apps for Windows/macOS, Ollama integration, and a DeepSeek Harness (DSH) plugin preview.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1563**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-16 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1473 · Python · 🔎 inferred · 0 天</summary>

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
| Stars        | **1473**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1204 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Go                                                                               |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1204**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐205 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Native DeepSeek Harness (DSH)-plugin die TypeSafe Jev of een Decision-api zoals luna integreert als een System One-beslaglaag voor agentselectie, toezicht, correcties en goedkeuringen.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **205**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐164 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **164**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐128 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness-desktopdierplug-in: de energieke walvismascotte vergezelt je bij het coderen 🐋 Ondersteunt DSH-desktopversie 0.2.0-rc.2 en oudere Web-versies (desktop pet / mascot, local-first)

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **128**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐98 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **98**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐77 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **77**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐60 · HTML · 🔎 inferred · 0 天</summary>

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
| Stars        | **60**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/unStone/dsh-xray">unStone/dsh-xray</a></b> · ⭐7 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

X-ray voor DeepSeek Harness-plug-ins: gedeclareerde mogelijkheden tegenover daadwerkelijk gedrag. Register + statische scanner + badges.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agent-security` · `ai-agents` · `ai-security` · `capability-analysis` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unstone--dsh-xray/35167f8867e8b79d.png" width="100%" alt="unStone/dsh-xray screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ItQianChen/dsh-github-flow">ItQianChen/dsh-github-flow</a></b> · ⭐5 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Geef DeepSeek Harness Agent native handen en voeten om GitHub te bedienen! Hergebruik veilig de gh CLI-referenties, met ondersteuning voor automatisch aanmaken en beoordelen van PR's, diagnose en reparatie van mislukte CI, driedimensionale Issues-taken en een SWR-cockpit met panoramische weergave die in 0 ms opent.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **5**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `gh-cli` · `github-cli`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/itqianchen--dsh-github-flow/e6f0174132cf93c1.png" width="100%" alt="ItQianChen/dsh-github-flow screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-plugin-doctor">PerryLink/dsh-plugin-doctor</a></b> · ⭐4 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Verificat standaard zonder afhankelijkheden voor DeepSeek Harness (dsh)-plug-ins — poorten voor statische structuur (R), cordis-contractcontroles (K), sandbox-smoketest (D) en controles van ecosysteemvermeldingen (CC). Verificat standaard zonder afhankelijkheden voor DSH-plug-ins: poorten voor statische structuur, cordis-contractscans, headless sandbox-smoketests en verificatie van ecosysteemvermeldingen.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `ai-agent` · `ai-agents` · `cli` · `cordis` · `deepseek-harness` · `developer-tools` · `doctor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-doctor/f2d1164a0731d7a5.png" width="100%" alt="PerryLink/dsh-plugin-doctor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-doctor/f697a1f89119c87d.gif" width="100%" alt="PerryLink/dsh-plugin-doctor animation"><br><sub>geanimeerde opname</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AI-Scarlett/DSH-Store">AI-Scarlett/DSH-Store</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH STORE — marktplaats voor plug-ins van derden en beheerder van de beveiligde levenscyclus voor DeepSeek Harness.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `plugin-manager` · `plugin-marketplace`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ai-scarlett--dsh-store/b9170b12b3cf26b9.jpg" width="100%" alt="AI-Scarlett/DSH-Store screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Atelyx/Atelyx">Atelyx/Atelyx</a></b> · ⭐3 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Atelyx is een mensgerichte, uitbreidbare desktopwerkplek: gesprekken, notities, tabellen en bestanden in dezelfde werkplek; met een zelf beheerde server kun je realtime samenwerking voor meerdere personen inschakelen. De applicatie zelf is een uiterst dunne kern; functies zoals gesprekken, notities, tabellen, canvas, zoeken en agenda worden geleverd door plug-ins die met de applicatie worden verspreid. Ze kunnen worden uitgeschakeld of door plug-ins van derden worden vervangen — het doel is nieuwe paradigma's voor samenwerking en werk in het AI-tijdperk te verkennen.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Rust                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `atelyx-plugin` · `collaboration` · `cordis` · `knowledge-base` · `local-first` · `markdown` · `pkm` · `plugin-platform`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Atelyx/Atelyx/main/atelyx-app/assets/icons/icon.png" width="100%" alt="Atelyx/Atelyx screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 76</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Een beveiliging vóór uitvoering voor AI-codeeragents.
- [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) - GenUI for DeepSeek Harness: interactive UI components rendered inline in…
- [Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet) - 📚 Een micro-lessenbibliotheek zonder afhankelijkheden, ondersteund door git…
- [DDDMUC/dsh-free-search](https://github.com/DDDMUC/dsh-free-search) - Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key…
- [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) - Cost tracking for DeepSeek Harness: session and model costs, token usage…
- [cv-superding/dsh-deepseek-web-login](https://github.com/cv-superding/dsh-deepseek-web-login) - Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as…
- [yexi-by/dsh-unrestricted](https://github.com/yexi-by/dsh-unrestricted) - DeepSeek Harness 提示词破限插件：通过系统提示词解除模型回答限制，深度适配 Web 与桌面端多模式及工具调用.
- [acryldev/acryl](https://github.com/acryldev/acryl) - ACRYL - Agent Context Relay Yielding Lifecycles.
- [dshplugin/dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) - DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 10000+ 人工精选社区插件，每日更新、完全免费.
- [wenbin-wb/dsh-bridge](https://github.com/wenbin-wb/dsh-bridge) - 🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 /…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-pluginmarkt / DSH Plugin Marketplace: blader, installeer en update alle…
- [MichengAI/dsh-skills-manager](https://github.com/MichengAI/dsh-skills-manager) - DSH Skills Manager — 在 DeepSeek Harness 中统一加载并安全管理本机 Agent Skills · Load and…
- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - DeepSeek Harness plugin for previewable cross-preset session migration.
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - Bij installatie krijg je 27 engineering- en productiviteitsskills uit…
- [arcships/rutis](https://github.com/arcships/rutis) - Een pluginruntime voor software die zichzelf herhaalt — de basis waarop agents…
- [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) - Remote-work assistant for DeepSeek Harness (DSH): connect SSH.
- [SiriLee/dsh-rewind](https://github.com/SiriLee/dsh-rewind) - DSH 插件：便捷无感的同窗口内对话回退，从不新建分支；自带轻量工作区备份，可一并还原文件（Claude Code /rewind 语义）.
- [Microqian2th/dsh-codex-effort-slider](https://github.com/Microqian2th/dsh-codex-effort-slider) - Codex 风格的推理等级滑条（DeepSeek Harness 插件）：可拖动连续滑条 + 高档位渐变星尘特效.
- [WestFox-AwA/dsh-prompt-optimizer](https://github.com/WestFox-AwA/dsh-prompt-optimizer) - DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把&quot;这一轮到底要什么&quot;理清楚，再把这份理解交给工作 AI(上下文注入)…
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) - DSH plugin - framework upgrade safety &amp; plugin gating: contract pre-check…
- [eleckoi/ElecKoi](https://github.com/eleckoi/ElecKoi) - 电子爱PC客户端，由DSH驱动的Agent角色扮演!
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Uitgelichte directory van DeepSeek Harness (DSH)-plugins — meer dan 280…
- [hkkz9522/dsh-session-manager](https://github.com/hkkz9522/dsh-session-manager) - DeepSeek Harness session and workspace manager —— Workspaces: archive and…
- [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) - 【求⭐】🐋DSH Web UI…
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [Lxiayu/DshCockpit](https://github.com/Lxiayu/DshCockpit) - Desktop cockpit for DeepSeek Harness (dsh): token usage &amp; cost tracking, budget…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH-plugin: Git Bash-shell voor alle agentmodi op Windows.
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh voor Android: geïntegreerd met DeepSeek Harness, Ubuntu-runtimeomgeving…
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 给中文网文作者的本地写作工作台.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Door de community samengestelde DeepSeek Harness (dsh)-plugins, tools, skills…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A-runtime voor commerciële onderhandelingen + DeepSeek Harness (dsh)-plugin.
- [pearjelly/deep-blend](https://github.com/pearjelly/deep-blend) - Create and refine Blender product scenes in DSH: editable recipes, model…
- [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution plugin for DeepSeek Harness: versioned, auditable…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [lemoncat7/dsh-knowledge](https://github.com/lemoncat7/dsh-knowledge) - Installable DeepSeek Harness knowledge base plugin.
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [earthwalker17/MiniDSH](https://github.com/earthwalker17/MiniDSH) - Minimal surface, complete architecture: a small, local-first coding-agent…
- [evoelsewhere/evoflux](https://github.com/evoelsewhere/evoflux) - Evoflux is an open-source, local-first workspace where AI agents build…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - DeepSeek Harness 的多智能体编排层 —— 42 skills / 33 角色卡 / 55 MCP 工具 / graph DAG 运行时 /…
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) - DSH Web UI 会话进度插件：输入框停靠区常驻进度条.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [omdsh-dev/dsh-minigames](https://github.com/omdsh-dev/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - Local-first voice conversations for DSH.
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) - J-Space Cognition Suite SV1 原生 DeepSeek Harness 智能体预设与独立 Cordis…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Zie elke observeerbare actie van AI-codeeragents.
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Page capability kit for DeepSeek Harness (dsh): terminal dock, file tree…
- [kolawong/fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh) - Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness-pluginecosysteem: 86 opensourceplugins in een familie van 101…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH)-webplugin: markt-dashboard-zijtab voor monitoring — drie…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode op DeepSeek Harness — DSH-plug-in die OpenCode Zen + Go gratis…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入.
- [higekibaka/dsh-vertex-argon](https://github.com/higekibaka/dsh-vertex-argon) - Vertex Argon — Google Vertex AI &amp; Gemini API dual-route Gemini 4 Argon plugin…
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色插件：三套服装、任务表情、三口白饭、摸头鼓脸、铁盆帽与手写问候.
- [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [viyiviyi/dsh-tree-task-flow](https://github.com/viyiviyi/dsh-tree-task-flow) - 树形任务流 · DeepSeek Harness 插件：把多步任务组织成目标→任务→子任务三级树，节点完成时由 AI…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Use OpenCode Zen free models in DeepSeek Harness with anonymous access or an…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness-plug-in: verandert de fout bij het provisionen van de ACL voor…
- [zhang-guo-wen/dsh-claude-compat](https://github.com/zhang-guo-wen/dsh-claude-compat) - deepseek harness 插件，兼容claude的skill、rules加载规则，mcp配置.
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [q253595422/dsh-imagegen-video](https://github.com/q253595422/dsh-imagegen-video) - DeepSeek Harness plugin: image + video generation studio with an infinite…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…

</details>

<a id="writing"></a>

## Schrijven, discussies en video&#x27;s

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 0 天</summary>

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
| First listed | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 13 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| TypeScript | 390   | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 92    | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 42    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 29    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12    | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 9     | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 5     | `vulcanshen/ccdrawu`, `sageox/ox`, `aaltw/claude-code-statusline`                                             |
| PowerShell | 2     | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| C          | 1     | `reporails/arcade`                                                                                            |
| Kotlin     | 1     | `dphmoblie/deepseek-harness-android`                                                                          |
| Swift      | 1     | `necobit/claude-lupin-title`                                                                                  |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Last updated · 2026-10-16T01:31:05+08:00</sub>
