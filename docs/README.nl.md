<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Geweldige Claude-mods">
</p>

<h1 align="center">Geweldige Claude-mods</h1>

<p align="center"><b>De op basis van bewijs beoordeelde index van Claude Code-mods, plug-ins en het diepere gedrag dat ze veranderen.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-584-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <b>Nederlands</b> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Actieve index** · Laatste synchronisatie: `2026-10-11T19:01:04+08:00` (UTC+8)
> · Items: **584** · Toegevoegd in de nieuwste update: **0** · Implementatietalen: **13**

<sub>Elk item hieronder is automatisch verzameld, gefilterd en opnieuw gecontroleerd. Niets hiervan is betaalde promotie.</sub>

<a id="featured"></a>

## Uitgelicht van dit moment

<sub>Eén item per categorie, gerangschikt op bewijsniveau en sterren, bij elke update opnieuw berekend. Een ranglijst, geen aanbeveling; elke keuze linkt door naar de volledige kaart hieronder. Projecten die een screenshot of opname hebben gepubliceerd krijgen de voorkeur, zodat de balk visueel blijft.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kuangre123--codex-switch/dcd3073c9c57be83.png" width="100%" alt="kuangre123/codex-switch">
<b>🏛️ <a href="https://github.com/kuangre123/codex-switch">kuangre123/codex-switch</a></b>
<sub>⭐70 · Python · 🔎 inferred</sub>
<sub>Codex Switch 是一个 macOS 工具，一键配置 Codex 的自定义 API，同时保留官方 OpenAI 登录。保存后 Codex 的模型选择器里只会出现你选的那个 provider 的模型。也支持 Claude Code 的官方 / 自定义 API 切换。Codex Switch is a lightweight…</sub>
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
<sub>⭐74319 · TypeScript · 👁️ observed</sub>
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
- [Officieel: de eigen repositories en release notes van Anthropic](#officieel-de-eigen-repositories-en-release-notes-van-anthropic) — **11**
- [Mods: gebouwd met de modfunctionaliteit](#mods-gebouwd-met-de-modfunctionaliteit) — **463**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150125 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **150125** |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.295 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

`$.ui.notify` toegevoegd voor mods: geeft een native melding via je eigen meldingsinstelling en zegt welk kanaal deze heeft verzonden Kinderen toegevoegd aan de `Button` van een mod: strings en `Text`, zodat een rij van een lijst met één druk kan worden bediend met een chip of gedimde details erin Een fout opgelost waarbij de hook van een mod een diep geneste toolinvoer afgekapt zonder fout kreeg, zodat een bewaker inhoud kon doorlaten die deze nooit had gezien Aanroepen opgelost die een mod doet tijdens het herladen bij een herstart van een worker voor pluginhooks en die langs de bewakingshook van een andere mod kwamen die een `.catch` heeft; zulke aanroepen worden nu geweigerd Een fout opgelost waarbij hot reload van een mod een opslagactie miste die tijdens `/r

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-09 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.296 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Esc of een onderbreking tijdens een `UserPromptSubmit`-hook of de `prompt.submit`-hook van een mod opgelost: dit beëindigde headless-sessies, wist de getypte prompt of liet de niet-gecontroleerde prompt door. Opgelost: `$.agent.register` slaagde vanuit een hook van een mod die nog actief was nadat de mod opnieuw was geladen of verwijderd; de aanroep wordt nu geweigerd. Opgelost: `$.http.fetch` in mods die een `HEAD`-verzoek weigeren wanneer het antwoord een `Content-Length` bevat die de limiet van 4 MiB voor de body overschrijdt

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic` |
| Evidence | `published by Anthropic itself`                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-10 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/kuangre123/codex-switch">kuangre123/codex-switch</a></b> · ⭐70 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Codex Switch 是一个 macOS 工具，一键配置 Codex 的自定义 API，同时保留官方 OpenAI 登录。保存后 Codex 的模型选择器里只会出现你选的那个 provider 的模型。也支持 Claude Code 的官方 / 自定义 API 切换。Codex Switch is a lightweight helper for configuring multiple coding-agent API routes. For Codex, it keeps Official OpenAI and a custom API provider configured in parallel, registers the custom model in Codex's mod

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `Officieel: de eigen repositories en release notes van Anthropic`                |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **70**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `codex` · `codex-app` · `codex-cli` · `codex-desktop` · `codex-github` · `codex-pet` · `codex-plugin` · `codex-project`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kuangre123--codex-switch/dcd3073c9c57be83.png" width="100%" alt="kuangre123/codex-switch screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/X-C1811/dsh-web-search-plugin">X-C1811/dsh-web-search-plugin</a></b> · ⭐3 · JavaScript · 🔎 inferred · 1 天</summary>

##### 📝 Summary

Geef je DeepSeek Harness-agent meer manieren om op het web te zoeken. Wissel in de instellingen tussen 9 providers, van officiële DeepSeek- en Google-resultaten tot zelf gehoste SearXNG. Probeer Tavily zonder een API-sleutel, of beheer je provid###-sleutels op één plek.

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
| First listed | 2026-10-11 |

🏷 `brave-search` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `exa` · `firecrawl` · `search`

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐483 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **483**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐184 · TypeScript · 👁️ observed · 1 天</summary>

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
| Stars        | **184**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

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
| Stars        | **59**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Verzameling van meer dan 100 mods die je met Claude Code kunt gebruiken.

<sub>🔧 Gebruik in code gevonden: `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`, `docs/COMMUNITY_MODS.md`</sub>

##### 📌 Basic facts

| Field    | Value                                                             |
| -------- | ----------------------------------------------------------------- |
| Category | `Mods: gebouwd met de modfunctionaliteit`                         |
| Evidence | `its own text names a mod API, or it declares the mod capability` |
| Taal     | TypeScript                                                        |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **47**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stars        | **13**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary><b>Meer in deze categorie</b> <sub>· 429</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods en de tools om ze te bouwen: eerst een builderskill, daarna mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - De Claude Code-harness die ik elke dag gebruik, sinds dag één onder deze naam…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Gebruik Claude Mods om het dak van Claude Code te vervangen: wijzig de binary…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Vier Claude Code-mods: Cache Keeper, Recording Mode, Goal Meter en Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Claude Code-mods van Learning Hacker: de werking van de agent begrijpelijk in…
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code-mods die je prompts corrigeren en vertalen voordat Claude ze leest.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Een desktopapp-uiterlijk voor het terminaltranscript van Claude Code, als mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Een zijpaneel voor Claude Code: de subagenten die een sessie uitvoert, wat elk…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Met bronnen onderbouwde Obsidian-kennisbank over Claude Code-mods: hoe ze…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Zijbalkpaneel van Claude Desktop (Code-tabblad): toont alle onafgemaakte en…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code-mods en -vaardigheden van Nekyia Labs, dagelijks gebouwd en…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Vaardigheid die Claude Code-agents leert om Claude Mods…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Gebruiksbalk boven het invoervak van Claude Desktop (Code-tabblad): 5u /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-mods, plug-ins en skills, installeerbaar vanuit één marktplaats.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude-mods (function-hookplug-ins) voor Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - De Baselane-modsgalerij: Claude Code-mods, gecontroleerd en vastgezet.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Een beslissingswachtrij CLI/TUI voor mensen die met conversatieagenten werken.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Een zwevende statuskaart voor Claude Code — model, context, rate limits…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code-mods: screen-guard maskeert namen en geheimen tijdens het delen van…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Ontgrendel de volledige kracht van Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code mod (plugin) die een zijpaneel toevoegt met Activity-, Files…
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
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - Bekijk wat je volgende Claude Code-bericht kost: een live balk boven de prompt…
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
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods voor Claude Code: Clawd, een kleine pixelmascotte die uitbeeldt wat Claude…
- [reporails/arcade](https://github.com/reporails/arcade) - Klassieke desktopgames als Claude Code-mods, gespeeld in een paneel terwijl…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Een samengestelde lijst van Claude Code-mods, installeerbaar als…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Een zeer uitgesproken Claude Code-plugin, ontworpen door een Rustacean die…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code-mods die een agent eerlijk houden — function hooks die de scope…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Mijn verzameling Claude Code-mods, één mod per map.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Een passief-agressieve waterherinnering voor Claude Code.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Vers uit de fabriek. Een Claude Code-mod: vraag om een meme en blijf…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod voor Claude Code: balk voor promptcache, volgende stappen, snelknoppen en…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Een Claude Code-mod die je gebruikslimieten en uitgaven weergeeft in de balk…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Een appstore voor Claude Code-mods binnen Claude Code: gebruik /mods om 2.700…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code-mods: voortgangsbalken voor plannen, een overzicht van wat Claude…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Een pixel-art Naruto-metgezel voor Claude Code: 20 ninja.
- [iamumeransari/claude-show-your-work](https://github.com/iamumeransari/claude-show-your-work) - Claude Code shows images and plays videos right in your terminal: screenshots…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Zes Claude Code-mods: planningslimieten en context boven de prompt, een coach…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Bekijk wat Claude Code op de achtergrond uitvoert: subagents, Codex-taken…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code-mods van MacLeod Labs: streams ontwart het door elkaar lopende werk…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Eerste-dag veldnotities over Claude Code-mods op Windows: een…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods die ik heb gemaakt en persoonlijk gebruik in mijn Claude Code-configuratie.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-mod: live kosten-, context- en planquotameters boven de prompt.
- [pawandeepdhall/claude-mods](https://github.com/pawandeepdhall/claude-mods) - Claude Code mods: always-visible 5-hour &amp; weekly usage limits with reset…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Een Claude Code-mod die fan-out van subagents, prompts met zware context en…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods voor claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Een Claude Code-mod die je globale skills, agents, regels en tools per repo met…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code-plugins (mods): wissel tussen meerdere Claude-accounts, bekijk…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Geteste Claude Code-mods die je met één opdracht installeert: guardrails voor…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods voor Claude Code: plug-ins gebouwd op functiehooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Filmachtige aftiteling voor je codeersessie.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Eigen pluginmarkt voor Claude Code-mods.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Een aantal claude code-mods die ik heb gebouwd.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Een door cliamp aangedreven YouTube-speler in Claude Code (Claude Code-mod).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code-mods: dashboard en autopilot voor agentvloot.
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude Code-mods van vynnlee. Eén map per mod, installeerbaar vanuit één…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Leer een vreemde taal terwijl je met Claude Code werkt.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Thematische antwoorden, diagrammen over de volledige breedte en je context en…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Wanneer een agent Java schrijft, kan code die het Alibaba-voorschrift Java…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Zijbalk met live kosten-, token- en contextgebruik voor Claude Code: een mod…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code-mod: een backlog van de opvolgtaken die Claude in elke sessie…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internetradio in Claude Code: een cliamp-sidebar, minispeler, favorieten…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Herdr-setup + Claude Code-mods voor productontwikkelingswerk.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS-dashboard in notch-stijl voor Claude Code: gebruikslimieten, open…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude is aan het koken. Chat met je squad.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Verzameling van jack.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Een Claude Code-mod: vang pixel-art-Modsters in een idle game terwijl Claude…
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Alles-in-één Claude Code-mod: live HUD, veiligheidsbeveiligingen…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - A space battle above Claude Code.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zie welke bestanden elke Claude Code-agent in zijn context heeft, en hoeveel…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods voor Claude Code: panelen, opdrachten en hooks gebouwd met de plugin…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Houd je hoofd koel. Een thermometer voor je Claude Code-dagen: elk uur krijgt…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Promptcache-, context- en planlimieten in één oogopslag voor Claude Code, in de…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code-mod: een livepaneel met de GitHub PR.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-mods voor de terminal en de desktopapp.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Verzameling Claude Code-mods, elk in een eigen repo: usage-meter…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code-mod: een voortgangspaneel voor taken, subagents, workflowruns, het…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code-mod: een klikbare inhoudsopgave met tijdstempels van de hele…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code-mod: planningslimieten, contextvulling, sessiekosten en tokens per…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-skill + mod die Spaanse woorden toevoegt aan agent-antwoorden.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Een Claude Code-mod die het herstijlt als The Machine uit Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Claude Code-mod: comprimeert op het juiste moment.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code-mod voor verplichte, geverifieerde DAG-workflows van…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-sourcemods voor Claude Code: deelvensters, statusregels, toastmeldingen…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Een Claude Code-mod: één deelvenster per subagent, de bestanden die ze aanraken…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code-mod: sessiestatus, live Spec Kit-voortgang en beheer van…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Het contextvenster als een rij boven de prompt, weergegeven zoals Claude Code…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Een gratis, open-sourceplugin voor Claude Code.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Een Claude-mod die de GitHub pullrequests van de sessie weergeeft in een paneel…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code-mod: genereer geluidseffecten uit tekstprompts met een lokaal…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-vaardigheden: een factchecker voor documentatie, een code-auditor…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code-mod: de regels code van vandaag door Claude — nieuw, bewerkt…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code-mod: klikbare paden in antwoorden — klik op een map om deze in…
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Claude Code mod: picks /effort per prompt with Jev.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-buddyplugin: een ASCII-metgezel boven je prompt die je regels…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code-plugin voor toolzichtbaarheid per agent — verberg en weiger…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code-mods: beveiligingslaag voor Claude Code - geheimen redigeren…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-plugin en -mod: een AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Verzameling geweldige Claude Code-mods | verzameling Claude Code-mods.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: een Claude Code-mod die de antwoorden van Claude en je prompts op…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Geef Claude een pak slaag wanneer het fouten maakt — een…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code-mods: kleine plugins voor livepanelen, kostenbewuste modelroutering…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code-mod &amp; plugin: gebruiksmonitor, tokentracker &amp; statusline.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Een Claude Code-mod die de kleine beslissingen overlaat aan een goedkoop…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Drie gratis Claude Code-mods: .env-waarden verbergen voor toolresultaten, het…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code-mods. touch-map: zie welke bestanden Claude heeft opgesomd…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Een Claude Code-mod die de agentberichten die je nog niet hebt gelezen samenvat…
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mods voor Claude Code: livepanelen, banden en hooks. Een pluginmarktplaats.
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Claude Code-pluginmarktplaats voor 0xnicholasy.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code-mod: voortgangsbalken voor gebruik (context, 5 uur, 7 dagen) en een…
- [akkaradej/hawkeye](https://github.com/akkaradej/hawkeye) - Claude Code mod: status dot, extend prompt cache, context ring, reborn, auto…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code-mods: sessiestatistiekkaarten boven de prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Een geanimeerde braillekat boven de Claude Code-prompt.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code-mod: stuur goedkoop werk via een onderliggend Claude Code naar…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Een pixelkat boven je Claude Code-prompt die een testgesprek met een…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Een Claude Code-mod die een goed moment kiest om te verdichten, zodat het…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods voor Claude Code: tokenmeter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code-pluginmarktplaats van anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code mod: your plan.
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Claude Code-mods om de markt vanuit de terminal te volgen: paneel voor A股/港股/美股…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mods voor Claude Code.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - My private Claude Code mods.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Het LGTM Lines-schip vaart na elke codewijziging voorbij — een Claude Code-mod.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Je Claude-gebruikslimieten als een geanimeerde gezondheidskaart van een…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code-mods voor het S2-team (de ather-marktplaats).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Korte workouts terwijl Claude werkt: een dagelijks doel, streaks, badges en…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Plan-, taak- en agentvoortgang naast de Claude Code-prompt — een Claude Code-mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Een gebruiksoverzicht voor Claude Code: uitgaven per model.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Een Claude Code-mod: live uitsplitsing van het contextvenster boven de prompt.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now Playing-mod voor Claude Code: Apple Music en Spotify boven de prompt, met…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Vijf Claude Code-mods om veel sessies tegelijk uit te voeren: vlootbord…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Claude Code-modpakket uit de Berko-video: Mask, View, Guard, Saving, Chime +…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods voor Claude Code: Cache-klok, Blast Radius, suggesties, werklijst, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Gewoon een uil voor je Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Eénregelige Claude Code-band.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - De originele Doom-engine met Freedoom, speelbaar binnen Claude Code.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Claude Code mod: estimated electricity ⚡ and water 💧 behind each turn and…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Een Claude Code-mod die een doorlopende lijst bijhoudt van de openstaande…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code mods for real Engineers.
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Exclusieve Claude Code-mods voor het d3nim-team.
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code mods: rule-keeper saves your corrections as permanent rules.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Een Tamagotchi die in Claude Code leeft: hij komt uit, eet de code die Claude…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods voor Claude Code, als plug-inmarktplaats.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code-mod: toont de tijd bij elke prompt en elk antwoord in de terminal…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Claude Code-mods geschreven als functiehooks, en de marktplaats die ze…
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code-mods en ontwerpsystemen: crab-crew en het Crab Crew-ontwerpsysteem.
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - Mijn Claude Code-mods, gedeeld als een pluginmarktplaats.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code-mod: nadat een guard een toolaanroep blokkeert, stopt hij herkende…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code-mod: achtergrondtaken in één weergave, met voortgang en ETA.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code-mod: één inbox voor berichten van teamgenoten, benoemde subagents…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code-mod: legt sandboxblokkades uit en zet herhaalde blokkades om in…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favourites for Claude Code: one-click icons for your commands and skills.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hé, gedempt! Weg met de diff, schrap de riff, geen wijzigingen meer, minder…
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - mods voor claude.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code mods: delete-guard (confirm file deletions) and octopus-crew.
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude Code-mod: abonnementsgebruik (5u / 7d) als een balk boven de prompt in…
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Motion-ontworpen mods voor Claude Code: een live, responsieve monitor voor…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Een live radar van je parallelle branches en worktrees boven de prompt: welke…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Embed Alarum.me in your Claude code CLI or Desktop.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Embed Floatee.me in your Claude code CLI or Desktop.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Een Claude Code-mod voor het vastleggen van gedachten tijdens het werk, het…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods en skins voor Claude Code: een live voortgangsbalk voor de taken van…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code-mods (function-hook-plugins): contextband, losse eindjes…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Zeven Claude Code-mods: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+klik om een link te kopiëren op elk codeblok in Claude Code-antwoorden…
- [Gersom/claude-mod-agent-radar](https://github.com/Gersom/claude-mod-agent-radar) - Claude Code-mod: visuele en passieve monitoring van de hoofdagent en diens…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mods voor Claude Code: plugins met hooks, zoals usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code mods (function-hook plugins), installed through one marketplace.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Evangelion-achtige zijbalk voor Claude Code: context, quotum, activiteit, PR.
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code-mods: context-bar-plus (contextbalk, quotum, subagentmodi).
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Statische supply-chain-auditor voor Claude Code Mods — lokaal, offline, alleen…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Duitstalige mods voor Claude Code: context-/cache-aanwijzingen, openstaande…
- [helenkwok/open-links](https://github.com/helenkwok/open-links) - Claude Code-mod: bestandspaden in antwoorden van Claude worden links die het…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Testresultaten in een Claude Code-paneel: fouten, details daarvan en…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-mod: hoe lang elk antwoord duurde, hoe lang Claude nadacht en…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - voor mijn claude-mods.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code-mod: wacht de gebruikslimiet van vijf uur uit en verstuurt…
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Kleine mods voor Claude Code, te beginnen met automatisch doorgaan na de limiet…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Een cockpit boven je Claude Code-prompt. De eend leest de meters af.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Kleine Claude Code-mods: meters voor context- en plangebruik, een…
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
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code-mod: subagents als pixelachtige Claude-mascottes boven de prompt.
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Claude mods voor extra gemak en kwaliteitsverbeteringen.
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code mods (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Twee Claude Code-mods: folio, een bestandsdeelvenster naast de chat, en tint…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Een live taak-HUD voor Claude Code Desktop: een strook boven de prompt terwijl…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Laat je aandacht niet afdwalen terwijl je wacht op het antwoord van Claude Code.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Claude Code-mods voor de projecten van Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Een door de community samengestelde Claude Code Mods-gids: gebruiksscenario.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Een Claude Code-mod die laat zien wat Claude doet in de ondertitel van het…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Een pluizige zwarte kat boven je Claude Code-prompt.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - De Claude Code-mods van Marcel in één pluginmarktplaats (marcel-mods).
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Een Claude Code-mod met verwisselbare toestemmingsprofielen: een veilige basis…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code-mod voor het bijhouden van gerelateerde artefacten en verwijzingen.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community-mods voor Claude Code: bewaking, deelvensters en opdrachten die…
- [MehdiChebbi13/clean-view](https://github.com/MehdiChebbi13/clean-view) - Claude Code mod: hide tool-call noise, show Claude.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Zijpaneel voor Claude Code: bestanden die Claude heeft geschreven…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Een rustig zijpaneel voor Claude Code: wat deze sessie doet, het plan, de…
- [mmedum/nuet](https://github.com/mmedum/nuet) - A dim time above each prompt and each reply in the Claude Code transcript…
- [mmedum/spor](https://github.com/mmedum/spor) - Zet terug wat Claude Code wegvouwt: de bestanden die Claude las, de opdrachten…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code-mod: gebruik van het contextvenster in het promptvoettekstvak.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-mod die de todo-tools weer inschakelt voor modellen die ze…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-mod: één regel per taak in de takenlijst boven de prompt, met de…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Speel Vier op een rij tegen een AI binnen Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code-mod: wanneer een andere code-agent een commit naar je repo maakt…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code-mod voor repo.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Een beveiliging voor SQL in Claude Code: vraagt voordat Claude via een DB CLI…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Eén mod voor Claude Code, Windows en CJK als uitgangspunt: voorbeelden van…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code-mods: miniaturen van afbeeldingen en de statusregel.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - De beste Claude Code-mods, gesorteerd op wat ze voor je doen.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Een Claude Code-mod die risicovolle shellopdrachten.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Twee Claude Mods voor Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code-mods met agenttelemetrie, tijdlijndashboards, mmrun-beoordeling…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Scheld tegen Claude Code en een cartoonhand slaat terug.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code-mods: usage-both toont het gebruik van 5 uur en per week boven de…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live zijpaneel met sessiestatistieken voor het Code-tabblad van de…
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Claude Code mods for the pompeitech interface, themed on the Vesuvius design…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods voor Claude Code: safety-guard blokkeert destructieve opdrachten en…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods voor Claude Code: functie-hookplugins die binnen de sessie worden…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code-mod: live-aandelenkoers, /quote-paneel, prijswaarschuwingen…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code-mod: SSH-host, RAM en gebruikslimieten voor 5 uur/7 dagen in een…
- [RexWei1016/claude-project-progress](https://github.com/RexWei1016/claude-project-progress) - Claude Code mod: project progress pane from GitHub milestones, issues, PRs and…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-mod: push-ups om te doen terwijl Claude werkt. Geen tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - A Claude Code mod that routes tasks to other AI models.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - De modwinkel voor Claude Code: haalt mods op van GitHub, geeft voorbeelden en…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-mod: verandert het plan dat je in planmodus goedkeurt in een live…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Een zorgvuldig geselecteerde lijst van Claude Code-mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenvrije modus: helperagents draaien op Haiku, en grote bestanden en logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Een lofi-soundtrack die de sessie volgt: kalmte, focus, flow, plus signalen…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Leer terwijl Claude codeert: na een beurt die de code heeft gewijzigd…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Een bandopname van elke bewerking die Claude maakt: speel elke wijziging af…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Elke link die je sessie vermeldt, op één regel boven de prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code-functie-hooks minimaal demonstratie: een live token-/kostenpaneel…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Claude Code Mod: 5h-, Wochen- und Fable-Limit als Leiste über dem Prompt.
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: an unofficial Avengers fan mod for Claude Code.
- [shawnbotha/claude-mods](https://github.com/shawnbotha/claude-mods) - Different Claude mods.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Claude Code-mod voor context, groei, quotum, cache, native kosten en…
- [shezis/claude-api-cost-compare](https://github.com/shezis/claude-api-cost-compare) - Claude Code mod: see what your session would cost on the Claude, OpenAI…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code mod: route simple turns and subagents to cheaper models, never…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Een gezellige RPG-HUD-mod voor Claude Code.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commitberichten met één klik voor Claude Code met een dansende pixel-art Malenia.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Personal Claude Code mods.
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugins for Claude Code.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — a Claude Code mod that shows your Claude plan usage.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code-mod: live teamvenster voor elke subagent.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Een Claude Code-mod die de huidige sessie in een paneel toont: elke prompt, het…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Een Claude Code-plugin-marketplace met mods: function-hooks-plugins die banden…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code mods on demand — a skill that reads your conversation and builds…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Claude Mods を管理するrepo.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Customizations for Claude Code.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Claude Code-mod: een balk en een paneel die je subagents volgen, samen met de…
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Claude Code mod that checks the English of your prompt while you write it.
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - A curated catalogue of Claude Code mods, each with a copy-paste prompt that…
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code-mod: 5h/7d-quotum, contextvenster, resterende promptcachetijd en…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code-mod: geanimeerde voortgangsbalk en voltooiingssamenvatting voor…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drie kleine Claude Code-mods: zie wanneer je subagents klaar zijn, zet…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Verkleint grote screenshots voordat Claude ze leest, zodat lange sessies langer…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Zeg &quot;Ik ben de draad kwijt&quot; en Claude legt het vorige antwoord opnieuw uit in…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Toont voorgestelde volgende prompts boven het promptvak.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stel Claude een zijvraag in een venster naast je werk.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace van mods voor Claude Code met installatie in één stap en een…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Aftellingen voor snelheidslimieten en een prognose van het verbruikstempo voor…
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Veiligheidslaag voor Roblox Studio voor Claude Code: RemoteEvent-audit…
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code plugin: your Claude Pro/Max usage limits with a pace forecast…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods voor Claude Code. agent-crew: zie je subagents werken als een live…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Inline and display LaTeX math, plus optional TikZ figures, in Claude.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Een live taakbord voor Claude Code: plan voordat je bouwt, volg elke taak…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod that reports which files Claude changed and why, live subagent…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Altijd zichtbare balk boven de Claude Code-prompt: contextvulling en…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Een zorgvuldig samengestelde verzameling van de beste hulpmiddelen voor de…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Een Claude Code-plugin die toont wat er gebeurt — contextgebruik, actieve…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Mooie, zeer aanpasbare statusregel voor Claude Code CLI met…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle onderdelen van de systeemprompt van Claude Code, 27 ingebouwde…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Meer dan 45 tips om het meeste uit Claude Code te halen, van basis tot…
- [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) - A terminal window manager that knows what your agents are doing.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Mooie vim-stijl-powerline voor Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Bekijk de diff van je codeeragent in een terminalvenster en stuur…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Uitgebreide statusregelplugin voor Claude Code met contextgebruik…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code &amp; Codex lokale token-tracking — statusbalk.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Bouw mods voor Claude Code: haak elk verzoek aan, wijzig elk antwoord, /model…
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness-agent voor langdurige roleplay (DSH-taverneplug-in): import…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Openbare Claude Code-vaardigheden en -mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash-opdrachten en handleidingen voor Claude…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Terminal-statusline voor Claude Code-sessies.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live voetbalstanden, wedstrijden en ranglijsten voor de competitie die je…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Lokaal control plane voor Claude Code op Windows en macOS: wissel met één klik…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill die je codeeragent verandert in een expert in toetsenbordfirmware.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Persoonlijke configuratie van Claude Code, met versiebeheer binnen ~/.claude…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebedstijden, Hijri-datum, adhkar, dagelijkse ayah, sunnah-vasten, Ramadan…
- [LikeACloud7/awesome-frontier-ai-papers](https://github.com/LikeACloud7/awesome-frontier-ai-papers) - Daily tracker for frontier AI lab papers, model cards, system cards, and…
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) - Tavily-powered optional search tool for DeepSeek Harness.
- [livlign/ccbit](https://github.com/livlign/ccbit) - Sessiegevoelige statusregel voor Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness-plug-in voor onderzoeksonderwerpen…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Statusregel met twee regels en truecolor voor Claude Code.
- [William2333ZZ/mywork-deepseekharness](https://github.com/William2333ZZ/mywork-deepseekharness) - MyWork — a personal agent on DeepSeek Harness: AI teammates that each own a…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Pluginbundel voor Claude Code, pi en DeepSeek Harness: HUD voor de statusbalk…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Draagbare Claude Code-toolkit voor .NET DDD/Clean Architecture: strikte…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Draagbare globale configuratie voor Claude Code: aangepaste skills…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-plug-ins die ik elke dag gebruik: skills en mods, opgeschoond zodat…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram in Claude Code: lees chats en kanalen in een paneel en krijg…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, een Tamagotchi-companionmod voor Claude Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marktplaats voor Claude Code-plug-ins en skills om mods voor het spel Hytale…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tokenbeheer voor Claude Code: het topmodel stuurt aan, de uitvoering gaat naar…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live statusregel voor workflowfasen voor Claude Code.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Onofficiële mods voor het tabblad Code van Claude Desktop — usage-pet: een…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository voor Awesome Media-mods van Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Verlaag de tokenuitgaven van Claude Code &amp; Codex: stuur opzoekingen en testruns…
- [zhuravel/magnum](https://github.com/zhuravel/magnum) - Your AI coding agents as a pull-request review team: Claude Code, Codex and…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Eenvoudige en nuttige statuslineconfiguratie voor Claude Code.
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
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agentteams. Onder controle. Strikte werkerslimieten, live…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Aangepaste statusregel voor Claude Code — contextbalk met gebruikspercentage…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Een schone, informatieve statusregel voor Claude Code — toont project…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod: a CRT-style status panel for Claude Code, in the terminal…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code-pluginmarktplaats met baloo: vaardigheden, een agent die…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionele Claude Code-statusregel: sessieduur, kosten in meerdere valuta…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Abonnementsbewuste statusregel voor Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Een uitgebreide terminalstatusregel voor Claude Code — Bun + TypeScript, zonder…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Claude Code-plugin die Mermaid-diagrammen prachtig in het transcript weergeeft…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, vaardigheden en agents voor Claude Code — te beginnen met een…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Aangepaste statusregel voor Claude Code.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Claude Code-plugin: zie altijd je resterende Claude-limiet voor 5 uur…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Echte DeepSeek-API-uitgaven voor Claude Code: herprijst sessietranscripten…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Preview images inside Claude Code: hover a chip under a reply to pop the…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods para Claude Code y Claude Desktop en Windows con WSL: Docker y rendimiento…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code-statusregel met rijen voor het agentenpaneel.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchroniseer de taken van Claude met Fizzy.do voor realtime inzicht voor het…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Toon een gedetailleerde, van kleur voorziene statusbalk voor Claude Code met…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Instellingenmenu, statusregel en configuratie voor Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - home-grown, cage-free claude plugins, skills, mods, and more.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code-omgevingsinstallatieprogramma: skills, statusregel, hooks…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - HUD-style status line for Claude Code — network health, TPS, context, quotas…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude Code-plugins en mods om te begrijpen wat Claude doet: leesbare…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitor de status van Claude Code vanuit je macOS-menubalk met…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Kleurrijke statusbalk met meerdere rijen voor Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code-statusregel voor Windows (PowerShell): gebruiksbalken, afteltimers…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Bearings- en Glossary-mod voor Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Draagbare Claude Code-configuratie: CLAUDE.md, instellingen, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Volg het contextgebruik van Claude Code, sessiekosten en resets van…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Screen reader companion mod for Claude Code (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Een praktische, geverifieerde diepgaande verkenning van Claude Code…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Realtime kostenregistratie en statusregel voor sessiemonitoring voor Claude Code.
- [wmkeza/claude-plugins](https://github.com/wmkeza/claude-plugins) - wmkeza.
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Statusregel met drie regels voor Claude Code: contextdiepte, snelheidslimieten…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - A Claude Code status line: folder, git branch, model, context window usage and…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Proactieve AI-geheugen- en snelheidslimietmonitor…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-hooks, subagents en statuslines: opensourceverzamelingen en -tools…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Een visuele builder voor statusregels van Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code-statusregel die realtime tokengebruik en geschat energieverbruik…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods voor Claude Code: deelvensters, banden en buddies, gebouwd op function…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Geef taken door tussen je Claude Code-sessies.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Dit in een MCP-server om MODS te besturen, de modulaire platformonafhankelijke…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex- en Claude Code-skill voor het vertalen van CK3-mods met een lokale LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods en andere uitbreidingen voor Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code-statusregel: de schoonheid van CCometixLine + de…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: vind wat je Claude Code steeds opnieuw vraagt en maak er een mod…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-barmod voor Claude Code: gebruikslimieten, cachetimer + waarschuwing…

</details>

<a id="dsh-cordis"></a>

## DSH- en Cordis-plug-inecosystemen

DeepSeek Harness en Cordis bereiken dezelfde plek vanuit een andere richting: voor hen is de plug-in het modmechanisme, dus een plug-in daar is het equivalent van een mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74319 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74319**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100481 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **100481** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐84715 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **84715**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81841 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **81841**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35758 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35758**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25487 · Python · 🔎 inferred · 18 天</summary>

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
| Stars        | **25487**  |
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
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8620 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **8620**   |
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
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐7828 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

De meest complete en snelst bijgewerkte Skills-winkel: zorgvuldig geselecteerde originele skillpakketten (voor documentverwerking, contentcreatie, programmeren en ontwikkeling, machine learning, geautomatiseerde workflows en meer), allemaal verpakt en direct klaar voor installatie en gebruik! Ook worden automatisch tienduizenden Skills-projecten op GitHub verzameld en geordend op categorie, bijgewerktatum en aantal Stars. De meest uitgebreide en frequentst bijgewerkte bibliotheek met AI Agent-skills, met zorgvuldig geselecteerde skillpakketten voor documentverwerking, contentcreatie, programmeren, machine learning, geautomatiseerde workflows en vele andere domeinen.

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | Python                                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7828**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

<sub>Asset rechtstreeks gekoppeld vanuit de upstream repository omdat er geen licentie voor herdistributie was opgegeven.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **6133**   |
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
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4466 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **4466**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4280 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **4280**   |
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
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1978 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | TypeScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1978**   |
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
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1801 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Verbind IM-bots met DeepSeek Harness via een QR-code of botreferenties (ondersteuning voor Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord en WhatsApp). Verbind IM-bots met DeepSeek Harness via een QR-code of referenties (9 kanalen).

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1801**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1398 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **1398**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **1169**   |
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
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐365 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **365**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **225**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **133**    |
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
<summary>🧵 <b><a href="https://github.com/mexiaosqwq/dsh-web-mobile">mexiaosqwq/dsh-web-mobile</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH Web UI aangepast voor mobiele apparaten: prettig op smalle schermen, geschikt voor brede schermen

##### 📌 Basic facts

| Field    | Value                                                                            |
| -------- | -------------------------------------------------------------------------------- |
| Category | `DSH- en Cordis-plug-inecosystemen`                                              |
| Evidence | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Taal     | JavaScript                                                                       |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **132**    |
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
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐130 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **130**    |
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
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐58 · HTML · 🔎 inferred · 0 天</summary>

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
| Stars        | **58**     |
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
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐27 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **27**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH 会话导航

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Afbeelding</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>geen media gepubliceerd</sub></td>
</tr></table>

</details>

<details>
<summary><b>Meer in deze categorie</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Een samengestelde lijst met de beste geweldige AI-plugins voor AI-assistenten…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-pluginmarkt / DSH Plugin Marketplace: blader, installeer en update alle…
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - Vervang de statusregel van DSH Web door 1063 memes: typemachine + kleurrijk…
- [arcships/rutis](https://github.com/arcships/rutis) - A plugin runtime for software that iterates on itself — the substrate where…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [1475505/miliastra-beyond-simulator](https://github.com/1475505/miliastra-beyond-simulator) - 千星沙箱模拟器：Lua 驱动的 2D 奇域外置沙箱 ，支持 DeepSeek Harness、Web 和 MCP.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Uitgelichte directory van DeepSeek Harness (DSH)-plugins — meer dan 280…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zotero-toolkit voor DeepSeek harness; maak van je Zotero-bibliotheek een…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH-plugin: Git Bash-shell voor alle agentmodi op Windows.
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - 办公三件套！Office document tools for DeepSeek Harness (dsh): generate, read, and…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Lokale schrijfwerkplek voor Chinese webromanschrijvers (19 tools): verzamel…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh voor Android: integreert DeepSeek Harness, een Ubuntu-runtimeomgeving…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH-webplugin: statistieken over tokengebruik per dag met een…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Door de community samengestelde DeepSeek Harness (dsh)-plug-ins, tools, skills…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - MCP-serverbeheerplugin voor DeepSeek Harness: pagina Instellingen → MCP, OAuth…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness-plugin: 15 engineeringvaardigheden van obra/superpowers…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A-runtime voor commerciële onderhandelingen + DeepSeek Harness-plug-in (dsh).
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - MCP-serverbeheerinterface voor DeepSeek Harness Web — zwevend paneel…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Een echte PowerPoint, geen HTML. Vertel je AI wat er behandeld moet worden en…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 给大肥鱼一个小说工作台：一起写正文、讨论后续情节、整理人物与世界设定，让长篇创作更贴近你的想法.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 插件 · 发送栏一键「优化」提示词草稿：五维诊断 + 改写稿 SSE 流式上屏，可替换 / 复制 /…
- [rezon-aki/dsh-streamfold](https://github.com/rezon-aki/dsh-streamfold) - 流式折叠：一个更好的 DSH 会话窗口——运行中自动展开最新思考小窗，其余过程行折成短摘要；跑完自动折起、穿插正文保留；收起/展开按 3…
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - DeepSeek Harness-plugin: lazy senior-modus en port van de ladder met 7 niveaus…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Login gate for the DeepSeek Harness (dsh) web surface: password or shared-token…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - AI-engineeringplug-in voor embedded C/C++ — firmwarevaardigheden.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Maak van de modellen die op de lokaal ingelogde WorkBuddy-desktopclient staan…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Alles-in-éénbeheerder voor skills, subagents, MCP en LSP voor DeepSeek Harness…
- [xxww0098/dsh-plugin-oauth-subs](https://github.com/xxww0098/dsh-plugin-oauth-subs) - ChatGPT Codex and xAI Grok subscription OAuth for DeepSeek Harness — PKCE /…
- [muyuanjin/dsh-ptc-plus](https://github.com/muyuanjin/dsh-ptc-plus) - A session-bound agent-native REPL for DeepSeek Harness PTC mode.
- [white0dew/awesome-dsh-plugins](https://github.com/white0dew/awesome-dsh-plugins) - Awesome DSH Plugins: a public GitHub directory for DeepSeek Harness plugins…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Altijd actieve compatibiliteitstests voor DeepSeek Harness-plug-ins: exacte…
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - Repair DeepSeek Harness sessions that refuse to load. 修好打不开的 DSH 会话文件.
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - Gratis toolkit zonder gedoe voor DeepSeek Harness (DSH): installatie met één…
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - A curated list of plugins, tools, skins, and extensions for DeepSeek Harness…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness-hostplugin die projectdocumenten en langetermijngeheugen als…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Röntgen voor DeepSeek Harness-plugins: gedeclareerde mogelijkheden versus…
- [Bcy2020/dsh-cc-ecosystem](https://github.com/Bcy2020/dsh-cc-ecosystem) - 让 DeepSeek Harness 用上 Claude Code 全家桶:技能、命令、规则、权限、子代理、hooks—— .claude/ 资产原样加载.
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - 让 DSH 回答变成可操作的界面：计算、图表、表单、模拟与小游戏。独立 DSH 插件 ｜ Interactive answers for DeepSeek…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH-plugin: een IDE-waardig Git-toolvenster als native dsh-better-sidebar-tab…
- [NoneadChina/dsh-nonead-universal-robots](https://github.com/NoneadChina/dsh-nonead-universal-robots) - A plugin enabling DSH to directly control Universal Robots (UR) arms using…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - 设计与代码的声称核验：事实类对照源码，行为类跑可执行模型；含结构/依赖审查（单层与多粒度细化）、UML 审查、基线对比与导出.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Werkruimte met meerdere mappen: laat de agent van DSH (DeepSeek Harness) niet…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plug-in voor technische workflows voor DeepSeek Harness: taakfasen…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Verificat standaard zonder afhankelijkheden voor DeepSeek Harness…
- [Small-tailqwq/dsh-internet-angel-desktop](https://github.com/Small-tailqwq/dsh-internet-angel-desktop) - 一款基于主播女孩重度依赖创建的 适用于 DSH 的 实验性主题皮肤 / Unofficial pixel desktop skin for DSH Web…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode op DeepSeek Harness — DSH-plug-in die OpenCode Zen + Go gratis…
- [xiaoso456/dsh-workflow-lite](https://github.com/xiaoso456/dsh-workflow-lite) - DeepSeek Harness 的软工作流插件：在画布上设计流程，编译成计划提示词，由模型按计划执行；运行状态由模型自己记，没有执行引擎.
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marktplaats voor plug-ins van derden en beheerder van de beveiligde…
- [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) - Query lokale logbestanden met Chinese natuurlijke-taal-tijdsaanduidingen…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx is een mensgerichte, uitbreidbare desktopwerkplek: gesprekken, notities…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Een coding-agent voor DeepSeek Harness met alles inbegrepen — workflows in…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web-invoerplug-in: schakelen tussen verzenden en nieuwe regel, contextmenu…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Biedt de desktopversie van DeepSeek Harness een externe toegangspoort met…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — communitytoolkit voor lokale implementatie en beheer van DeepSeek…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH)-webplugin: markt-dashboard-zijtab voor monitoring — drie…
- [Wenston-dev/awesome-dsh-plugin](https://github.com/Wenston-dev/awesome-dsh-plugin) - Awesome dsh plugin list — automated DeepSeek Harness plugin directory.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness-plug-in: zet de fout bij het instellen van de sandbox-ACL van…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Maakt een niet-toegeschreven lege modelpoging opnieuw uitvoerbaar, voor de ene…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness-agentpreset: Codex en Claude Code als delegatie-subagents, elk…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Een Rust-plug-inruntime met een door Verus geverifieerde levenscycluskernel en…

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

| Taal       | Items | Voorbeelden                                                                                                 |
| ---------- | ----- | ----------------------------------------------------------------------------------------------------------- |
| TypeScript | 379   | `anthropics/claude-code`, `hamzafer/claude-code-mods`, `karanb192/cache-tax`                                |
| JavaScript | 85    | `X-C1811/dsh-web-search-plugin`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`         |
| Python     | 37    | `kuangre123/codex-switch`, `alexgreensh/token-optimizer`, `AgriciDaniel/claude-mods-brain`                  |
| Shell      | 21    | `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`, `andrewbakercloudscale/claude-code-cost-sidebar` |
| HTML       | 10    | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                          |
| Go         | 8     | `cephalofoil/kitt`, `Gaurav-Gosain/tuios`, `kylesnowschwartz/tail-claude-hud`                               |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`           |
| PowerShell | 2     | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                         |
| Swift      | 2     | `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`                                     |
| C          | 1     | `reporails/arcade`                                                                                          |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                     |
| Kotlin     | 1     | `dphmoblie/deepseek-harness-android`                                                                        |
| MDX        | 1     | `jkf87/mod-guide`                                                                                           |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Last updated · 2026-10-11T19:01:04+08:00</sub>
