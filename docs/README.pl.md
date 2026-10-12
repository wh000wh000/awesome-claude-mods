<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Świetne mody Claude">
</p>

<h1 align="center">Świetne mody Claude</h1>

<p align="center"><b>Indeks modów i wtyczek do Claude Code, ocenianych na podstawie dowodów, oraz głębszych zmian w zachowaniu, które wprowadzają.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-585-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <b>Polski</b> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Aktualny indeks** · Ostatnia synchronizacja: `2026-10-13T06:19:35+08:00` (UTC+8)
> · Wpisy: **585** · Dodane w najnowszej aktualizacji: **0** · Języki implementacji: **12**

<sub>Każdy poniższy wpis został automatycznie zebrany, przefiltrowany i ponownie sprawdzony. Żaden z nich nie jest płatną promocją.</sub>

<a id="featured"></a>

## Polecane teraz

<sub>Jeden wpis na kategorię, uszeregowany według oceny dowodów i liczby gwiazdek; ranking jest tworzony ponownie przy każdej aktualizacji. To ranking, a nie rekomendacja — każdy wybór prowadzi do jego pełnej karty poniżej. Preferowane są projekty, które opublikowały zrzut ekranu lub nagranie, aby pasek pozostał wizualny.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9486 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2543 · Python · 👁️ observed</sub>
<sub>Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74439 · TypeScript · 👁️ observed</sub>
<sub>🌊 Oryginalny harness agenta. Wdrażaj inteligentne wieloagentowe roje, koordynuj autonomiczne przepływy pracy i twórz konwersacyjne systemy AI. Oferuje adaptacyjną…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Spis treści

- [Czym jest mod do Claude Code](#czym-jest-mod-do-claude-code)
- [Jak oceniane są wpisy](#jak-oceniane-są-wpisy)
- [Oficjalne: własne repozytoria i informacje o wydaniach Anthropic](#oficjalne-własne-repozytoria-i-informacje-o-wydaniach-anthropic) — **17**
- [Mody: stworzone z użyciem możliwości tworzenia modów](#mody-stworzone-z-użyciem-możliwości-tworzenia-modów) — **451**
- [Ekosystemy wtyczek DSH i Cordis](#ekosystemy-wtyczek-dsh-i-cordis) — **106**
- [Teksty, dyskusje i wideo](#teksty-dyskusje-i-wideo) — **11**
- [Projekty według języka implementacji](#projekty-według-języka-implementacji)

## Czym jest mod do Claude Code

Claude Code gained **mods** in 2.1.287: extensions that may change deeper behaviour than a plugin could, and draw their own interface.

A mod can hook `ui.render` to paint a **row, band, pane or card** around the prompt, read the text you last selected with `$.ui.selection()`, spawn teammates with `agent.spawn`, and own a `Client` region. A mod that fails to draw fails alone — `ui.fault` keeps one broken mod from taking down the session.

This list covers mods, the plugin and hook surface they build on, and the DSH and Cordis equivalents. It deliberately does **not** cover the wider Claude Code ecosystem: a prompt pack is not a mod.

## Jak oceniane są wpisy

Most lists in this space assert inclusion. This one says how much was actually verified, then lets you filter accordingly. A grade describes the evidence, not the quality of the project — a well-built mod nobody has written about yet is still `inferred`.

| Ocena                                                                            | Znaczenie                                                                                                                                                                                              |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `published by Anthropic itself`                                                  | Published by Anthropic itself, or read directly from the official changelog.                                                                                                                           |
| `its own text names a mod API, or it declares the mod capability`                | Its own text names part of the mod surface — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, a pane, band or card — so the author is describing something they built against the real API. |
| `declared a mod, plugin or hook, but nothing about the mod surface specifically` | It calls itself a mod, plugin or hook, but nothing in its text names the mod surface specifically. Real, but unconfirmed.                                                                              |
| `matched on vocabulary alone`                                                    | Matched on vocabulary alone. Included so the filter is auditable, not because it is believed.                                                                                                          |

<a id="official"></a>

## Oficjalne: własne repozytoria i informacje o wydaniach Anthropic

Anthropic's own Claude Code repositories, and the releases that defined the mod surface. Read from the source rather than summarised.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150420 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Podsumowanie

Claude Code to agentyczne narzędzie programistyczne działające w terminalu, które rozumie bazę kodu i pomaga programować szybciej, wykonując rutynowe zadania, wyjaśniając złożony kod i obsługując przepływy pracy git — wszystko za pomocą poleceń w języku naturalnym.

<sub>🔧 Znaleziono użycie w kodzie: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |
| Język     | TypeScript                                                         |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **150420** |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9486 · TypeScript · ✅ official · 3 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |
| Język     | TypeScript                                                         |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **9486**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8255 · Python · ✅ official · 3 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |
| Język     | Python                                                             |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **8255**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6354 · Python · ✅ official · 243 天</summary>

##### 📝 Podsumowanie

Oparte na AI działanie GitHub do przeglądu bezpieczeństwa, wykorzystujące Claude do analizowania zmian w kodzie pod kątem luk w zabezpieczeniach.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |
| Język     | Python                                                             |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6354**   |
| Ostatni push           | 2026-02-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1800 · Shell · ✅ official · 3 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |
| Język     | Shell                                                              |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1800**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

##### 📝 Podsumowanie

Materiały uzupełniające do kart modeli Claude

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **25**     |
| Ostatni push           | 2025-12-05 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Podsumowanie

Dodano mody Claude: wtyczki mogą teraz modyfikować głębsze zachowanie. Dodano You should know, wbudowany mod, w którym agent pomocniczy obserwuje sytuację i sygnalizuje rzeczy, które Ty lub Claude możecie przeoczyć. Włącz go za pomocą `/plugin enable cc-plugin-you-should-know@builtin` (dla sesji first-party z włączoną telemetrią)

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Podsumowanie

Dodano `$.ui.selection()` dla modów: zwraca ostatnio zaznaczony tekst w trybie pełnoekranowym, a gdy zaznaczenie znajduje się w jednym wierszu transkryptu, zwraca ten wiersz. Naprawiono błąd, przez który przycisk moda czasami uruchamiał działanie innego przycisku po naciśnięciu w widoku narysowanym przed ponownym uruchomieniem Claude Code. Naprawiono kończenie sesji pełnoekranowych z komunikatem „unrecoverable interface error” przy otwieraniu okna zadań w tle, gdy wtyczka lub mod wyświetlały wiersze nad poleceniem. Naprawiono zgłaszanie przez `claude plugin test` modów jako zdalnie wyłączonych, gdy odczytano jedynie nieaktualne zapisane ustawienie

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Podsumowanie

Naprawiono błąd, przez który reguła deny lub ask dotycząca zagnieżdżonej części złożonego polecenia powłoki nie obejmowała zatwierdzania moda zainstalowanego przez użytkownika na zarządzanych komputerach. Naprawiono nieładowanie zainstalowanych modów w pierwszej sesji po aktualizacji. Dodano `agent.spawn` dla członków zespołu, jeden identyfikator agenta we wszystkich zdarzeniach hooków wtyczek oraz stany bezczynności i oczekiwania w `$.agent.list()`. Naprawiono kończenie sesji z komunikatem „unrecoverable interface error”, gdy wartość zapisana przez hook `ui.render` moda powodowała błąd wiersza podczas rysowania; silnik rysuje teraz własny wiersz. Naprawiono wyrównaną do prawej zawartość w panelu lub pasie moda, która była rysowana pod znacznikiem zamknięcia lub `\[-\]`, wh

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Podsumowanie

Dodano `serverToolUses` do wyniku hooka `turn.step` modyfikacji: narzędzie wywołuje API uruchomione samodzielnie (doradcę), każde z jego identyfikatorem, nazwą, danymi wejściowymi, czasem rozpoczęcia i zakończenia. Dodano `ceiling` do pytania i werdyktu odczytywanych przez hook `tool.check` modyfikacji, określając nazwę zgody wymaganej przez organizację na użycie narzędzia. Dodano typy `ThemeKey` i `Color` do typów hooków wtyczek, aby edytor wyświetlał kolory motywu, które może nazwać rysunek modyfikacji. Dodano do `claude plugin validate`: każdy hook rejestrowany przez modyfikację w miejscu kontroli jest wymieniony wraz z informacją, czy ma `.catch` (`gatingHooks` w ramach `--json`). Naprawiono wynik `turn.step` modyfikacji

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Podsumowanie

Dodano `prompt.autocomplete`, zdarzenie, do którego mod podpina się, aby dodać własne wiersze do listy autouzupełniania pola promptu Dodano buforowanie promptów do `$.model.complete` dla modów: `prompt` i `system` przyjmują bloki tekstu, a `cache: true` na bloku buforuje żądanie do niego Dodano agentów przepływu pracy do haka moda `agent.spawn`, z ich uruchomieniem i indeksem, aby mod mógł ich odrzucić Naprawiono wiersze Write, Edit, NotebookEdit i LSP oraz pojedyncze wiersze Read, Grep i Glob, ukrywające, dlaczego mod odmówił wywołania: wiersz teraz pokazuje powód Naprawiono hak `config.set`, `state.set`, `env.set` lub `agent.spawn` moda, który odmawia po

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Podsumowanie

Dodano `isDeferred` do `$.tool.register` dla modów: `false` od początku wyświetla schemat narzędzia w prompcie zamiast ukrywać go za wyszukiwaniem narzędzi Naprawiono pomijanie hooków modu przez `classic.*` zdarzenia podczas ponownego uruchamiania workera hooków wtyczki, przez co hooki ustawień musiały odpowiadać bez nich Naprawiono niepowodzenie `claude plugin test` w przypadku modów wywołujących `$.session.append`; testy mogą odczytywać z powrotem dołączone wiersze za pomocą nowego `mock.session`

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Konsola zarządzania MCP dla oficjalnego klienta DeepSeek Harness MCP: polecenie /mcp z diagnostyką stanu i testowymi wywołaniami potoku, karta Ustawienia MCP z CRUD serwerów (zapisy wymagające zatwierdzenia, automatyczne kopie zapasowe) oraz konsola testowania narzędzi w oficjalnym potoku narzędzi (Apache-2.0, dsh-plugin).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic`               |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **74**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/fschmutz/claude-usage-panel">fschmutz/claude-usage-panel</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

See your Claude Code plan usage everywhere: GNOME top bar, macOS menu bar, a status line under the Claude Code prompt, and a get_usage MCP tool for Claude Code + Cursor. Session, weekly & per-model (Fable/Opus) limits from the official usage API, with burn-rate forecasts. One-line install, self-updating.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic`               |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6**      |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `anthropic` · `ccusage` · `claude` · `claude-code` · `cursor` · `developer-tools` · `gnome` · `gnome-extension`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fschmutz--claude-usage-panel/40b54f8d52b03345.png" width="100%" alt="fschmutz/claude-usage-panel screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-ticktick">PerryLink/dsh-ticktick</a></b> · ⭐4 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Most zadań TickTick (Dida365) dla DeepSeek Harness: panel zadań w nagłówku sesji (filtrowanie listy, widoki niewykonanych/ukończonych, wyszukiwanie, zmiana kolejności metodą przeciągnij i upuść), 11 wyselekcjonowanych narzędzi agentów, karta ustawień, przez oficjalny punkt końcowy TickTick MCP.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic`               |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **4**      |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dida365` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/aa581021cb97f4dd.png" width="100%" alt="PerryLink/dsh-ticktick screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/44088595da097cb2.gif" width="100%" alt="PerryLink/dsh-ticktick animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Dodano `$.ui.notify` dla modów: wyświetla natywne powiadomienie za pomocą…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Naprawiono przypadki, w których klawisz Esc lub przerwanie podczas hooka…

</details>

<a id="mods"></a>

## Mody: stworzone z użyciem możliwości tworzenia modów

Każdy wpis tutaj pokazuje dowody użycia możliwości, którą Claude Code zyskał w wersji 2.1.287: rysuje za pośrednictwem `ui.render`, posiada panel, pas lub kartę, odczytuje `$.ui.selection()`, uruchamia współpracowników za pomocą `agent.spawn` albo jasno mówi, że jest modem.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2543 · Python · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | Python                                                            |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **2543**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐530 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Społecznościowy katalog publicznych modyfikacji Claude Code (hooków funkcji), skanowanych z GitHub wraz z informacjami, co każda modyfikacja może odczytywać, zapisywać, uruchamiać lub wysyłać przez sieć. Przeglądaj https://mods.aidojo.si/

<sub>🔧 Znaleziono użycie w kodzie: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **530**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐210 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code: wtyczki oparte na hookach, które dodają nad monitem dynamiczne wiersze, zabezpieczenia, panele i gry. Pasek kontekstu, miernik użycia, monitor recenzji Codex, podgląd Markdown, aktualnie odtwarzany utwór Spotify i więcej.

<sub>🔧 Znaleziono użycie w kodzie: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **210**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐161 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Podsumowanie

Podtrzymuj ciepło pamięci podręcznej promptu Claude Code podczas przerw i pokazuj szacowany koszt przed wysłaniem po wychłodzeniu pamięci.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **161**    |
| Ostatni push           | 2026-10-04 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>animowane nagranie · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐117 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Skórki dla Claude Code: wiersze narzędzi z ikonami, karty różnic, tabel i wykresów Mermaid, pasek użycia oraz piętnaście motywów. /skin przełącza je na żywo.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **117**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Kolorowe, konfigurowalne odpowiedzi Claude Code: tabele, kod, diagramy, wykresy i wiersze narzędzi w 15 motywach, z przyciskami kopiowania. Modyfikacja Claude Code.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **88**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Podsumowanie

Zbiór modyfikacji claude code

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **78**     |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Mod Claude Code, który umieszcza w terminalu pulpit agenta na żywo: kontekst i koszt, oś czasu doradcy, każdą kontrolę uprawnień, karty podagentów i tory.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **75**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code autorstwa Darrell Wang — pasma nad monitem, zero tokenów modelu. Pulpit akcji tajwańskich／amerykańskich + kolejne funkcje w przygotowaniu.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | HTML                                                              |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **65**     |
| Ostatni push           | 2026-10-05 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Podsumowanie

Eksperckie skills, agenci, polecenia, reguły, hooki i style wyjścia dla Claude Code — ciągłość sesji + nowoczesne narzędzia CLI do rzeczywistych przepływów pracy programistycznej

<sub>🔧 Znaleziono użycie w kodzie: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | Shell                                                             |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **62**     |
| Ostatni push           | 2026-10-07 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐55 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Podsumowanie

Kolekcja ponad 100 modyfikacji, których możesz używać z Claude Code.

<sub>🔧 Znaleziono użycie w kodzie: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **55**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code: paski postępu planu wyświetlane nad monitem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **47**     |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animowane nagranie · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Podsumowanie

Obserwuj, jak Claude Code tworzy małą kreskówkę podczas Twojej pracy.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **32**     |
| Ostatni push           | 2026-10-02 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Podsumowanie

Pasek promptów z sesji Claude Code: najedź, aby przeczytać, kliknij, aby przejść (function hooks / Mods)

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **28**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐26 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Ulepszenie dla Claude Code: panel kokpitu na żywo, motywy możliwe do udostępniania oraz pikselowy zwierzak pokazujący, co robi Claude

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **26**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Pikselowy Pokémon żyjący nad monitem w Claude Code

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **25**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Podsumowanie

Kompilowanie, testy, konsola i podglądy SwiftUI z Xcode wewnątrz Claude Code

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **20**     |
| Ostatni push           | 2026-10-02 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code: 21 stylów i pełny zestaw funkcji włączanych wtedy, gdy ich potrzebujesz, dla terminala i aplikacji desktopowej. · Jednym kliknięciem nadaj Claude nowy styl i korzystaj z pełnego zestawu funkcji włączanych na żądanie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **20**     |
| Ostatni push           | 2026-10-04 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 Podsumowanie

Dziesięć modyfikacji Claude Code, poradniki dla początkujących, prompty do tworzenia, bezpieczne demonstracje i szablon do samodzielnego zbudowania.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **20**     |
| Ostatni push           | 2026-10-02 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Modyfikacja Claude Code: podgląd wklejonych obrazów i długiego wklejonego tekstu nad promptem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **19**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐17 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Modyfikacja Claude Code: Clawd odgrywa to, co robi Claude, nad promptem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **17**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Dwie modyfikacje Claude Code: most Codex computer-use i skoordynowane sesje Claude. Źródła, prompty budowania, konfiguracja i testy.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **16**     |
| Ostatni push           | 2026-10-05 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code: usage-band pokazuje limity 5h/7d, okno kontekstu i współczynnik trafień pamięci podręcznej nad monitem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **13**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code, które ułatwiają czytanie i odpowiadanie na pytania Claude (qa-guide).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **12**     |
| Ostatni push           | 2026-10-07 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>animowane nagranie · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Claude Code mod: kontekst w tokenach, limity 5-godzinne i tygodniowe względem zegara, odliczanie pamięci podręcznej promptu, koszt sesji i działające agenty — wszystko w jednym pasku nad promptem.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **12**     |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Podsumowanie

Dziesięć modyfikacji open source dla Claude Code: dynamiczne panele, pasma, linie statusu i zabezpieczenia wywołań narzędzi. Miernik zużycia, kody uruchamiania, podsumowanie sesji, walka z bossem, zwierzak kodowy i więcej.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **12**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Podsumowanie

Animowana pikselowa grafika nad promptem Claude Code, która reaguje podczas pracy Claude. Siedem scen lub własny obraz albo GIF. Zero tokenów.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **10**     |
| Ostatni push           | 2026-10-04 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

##### 📝 Podsumowanie

Śledzenie sesji dla Claude Code zbudowane jako mody: okno kontekstu, tempo zużycia limitu planu, koszt na turę

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **9**      |
| Ostatni push           | 2026-09-15 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Interfejs wokół terminali Claude Code i Codex, które budują Twoi agenci, dzięki czemu jedynym modelem w Twojej głowie jest Twój własny.

<sub>🔧 Znaleziono użycie w kodzie: `CLAUDE.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **9**      |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Podsumowanie

KOZMOS — wizualne mody działające na żywo dla Claude Code (CLI + komputer): pasma nad polem promptu, panele boczne, pasek stanu, towarzysze, strażnicy i dźwięk.

<sub>🔧 Znaleziono użycie w kodzie: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **9**      |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Wydłuż działanie planu Claude Pro: mody Claude Code zapewniające dokładny HUD zużycia, krótsze wyjście powłoki i brak ponownego odczytu plików. Mody zużywają zero tokenów.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **9**      |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Podsumowanie

Sześć modów Claude Code w jednej wtyczce (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) z przełącznikami dla poszczególnych modów oraz raportem mods-vs-hooks.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **8**      |
| Ostatni push           | 2026-10-04 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Podsumowanie

Kolekcja modów Claude Code autorstwa 개발동생. Pakiet taxi: taksometr, nawigacja, kamery kontroli prędkości, wideorejestrator

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **8**      |
| Ostatni push           | 2026-10-04 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Obejrzyj w serwisie youtube.com</a> · odtwarzanie otwiera się w witrynie źródłowej; GitHub nie może osadzić go bezpośrednio</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Twój plan, obserwujący sam siebie. Lokalny komputerowy plan rozwoju w formie drzewa, który Claude Code i każdy host MCP na bieżąco aktualizują. Zwykły JSON, bez chmury.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **8**      |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 417</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Modyfikacje Claude i narzędzia do ich tworzenia: najpierw umiejętność…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Środowisko Claude Code, którego używam codziennie, publikowane pod tą nazwą od…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Modyfikacje Claude Code autorstwa Raya Amjada: panele, pasma, strażnicy…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Zmień dach w Claude Mods dla Claude Code: bez modyfikowania pliku binarnego…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cztery modyfikacje Claude Code: Cache Keeper, Recording Mode, Goal Meter i…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Modyfikacje Claude Code od Learning Hacker: przedstaw działanie agenta w…
- [kakha13/claude](https://github.com/kakha13/claude) - Modyfikacje Claude Code, które poprawiają i tłumaczą Twoje prompty, zanim…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Baza wiedzy Obsidian z podanymi źródłami na temat Claude Code mods: jak…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mody i umiejętności Claude Code od Nekyia Labs, tworzone i codziennie używane…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Kokpit dla Claude Code: paski planu na żywo, paski subagentów, limity użycia z…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Wygląd aplikacji desktopowej dla transkrypcji terminala Claude Code, jako mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel boczny dla Claude Code: podagenci uruchamiani przez sesję, zadania…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mody Claude Code: menu narzędzi Claude, tryb Zen, motywy terminala, sterowanie…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel boczny Claude Desktop (karta Code): wyświetla wszystkie niedokończone i…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Pasek użycia nad polem wejściowym Claude Desktop (karta Code): limit 5h / 7d…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Umiejętność ucząca agentów Claude Code tworzenia modów Claude.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Społecznościowe mody, wtyczki i umiejętności Claude, instalowalne z jednego…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mody Claude (wtyczki z hakami funkcji) dla Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeria modów Baselane: mody Claude Code, sprawdzone i przypięte.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Kolejka decyzji CLI/TUI dla ludzi pracujących z agentami konwersacyjnymi.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code rysujący różnice Edit i Write w dwóch kolumnach obok siebie.
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown rysowany w polu promptu Claude Code podczas pisania.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mody Claude Code: panel zużycia 像素螃蟹 usage-hud + klikalne linki HTML w…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Pływająca karta statusu dla Claude Code — model, kontekst, limity szybkości…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mody dla Claude Code: wtyczki function-hook dodające aktywne panele i…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mody Claude Code: screen-guard ukrywa nazwy i sekrety podczas udostępniania…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mody i skórki dla Claude Code: pasek postępu na żywo dla zadań Claude, czytelny…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Rozszerzenia Claude Code. Odblokuj pełną moc Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod Claude Code (wtyczka), który dodaje panel boczny z kartami Activity, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panele, zabezpieczenia i mody poprawiające wygodę pracy z Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dwa mody Claude Code nad polem promptu: miernik okna kontekstu, limit 5 godzin…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Odczytuje pliki markdown nazwane przez Claude Code i renderuje je obok sesji;
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude gotuje. Czatuj ze swoją ekipą. Znajomi online, tuż obok Twojej sesji…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Test pisania na czas, podczas gdy Claude pracuje. Modyfikacja Code dla Claude.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code: miniatury wklejonych obrazów nad promptem, w dowolnym terminalu.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Głosowy współpracownik dla Claude Code.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow dla Claude Code: spokojna lista kontrolna nad polem promptu…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mody Claude Code: pasek kontekstu, panel agentów, rozmywanie PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mody Claude Code: typing-speed, prędkościomierz pisania na żywo ze statystykami…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fajerwerki dla Claude Code: każde naciśnięcie klawisza, wywołanie narzędzia…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Modyfikacje dla Claude Code: panele, polecenia i hooki zbudowane za pomocą…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Odkrywaj mody, wtyczki i rozszerzenia Claude Code dzięki animowanym…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code: diagramy mermaid rysowane bezpośrednio w transkrypcji.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Małe modyfikacje Claude Code (wtyczki function-hook): session-switcher i inne.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sześć modyfikacji Claude Code: limity planu i kontekst nad promptem, pomocnik…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mody Claude Code: mod-scout (znajduje najczęściej używane mody), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dwa mody Claude Code do jednoczesnego uruchamiania wielu sesji: karta kontekstu…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mody Claude Code na żądanie — umiejętność, która odczytuje Twoją rozmowę i…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: odkrywaj, sprawdzaj, przełączaj i aktualizuj mody Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Najlepsze mody Claude Code: starannie wybrane, sprawdzone i przypięte.
- [davekiss/mods](https://github.com/davekiss/mods) - Modyfikacje Claude Code autorstwa Dave Kiss.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Wtyczka Claude Code: automatyczne kierowanie do modeli Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Modyfikacja Claude Code: panel na żywo z żądaniami PR GitHub, które sesja…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sześć modów dla Claude Code: animowana maskotka Clawd, paski limitu użycia i…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Sklep z aplikacjami dla modyfikacji Claude Code, wewnątrz Claude Code: użyj…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Marketplace modów dla Claude Code: debugger krokowy pętli agenta, podpowiedzi…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Modyfikacje open source dla Claude Code: panele, wiersze stanu, powiadomienia…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Najlepszy kompleksowy pakiet modyfikacji dla Claude Code: limity użycia i HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Odtwarzaj YouTube Shorts w swoim Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Zestaw narzędzi Claude Naren: skills, mody i serwery MCP dla Claude Code.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mody dla Claude Code: Clawd, mała pikselowa maskotka odgrywająca to, co robi…
- [reporails/arcade](https://github.com/reporails/arcade) - Klasyczne gry desktopowe jako mody Claude Code, uruchamiane w panelu podczas…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - modyfikacje kodu dla claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Własny marketplace modyfikacji dla Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Wyselekcjonowana lista modów Claude Code, instalowanych jako marketplace…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Dwa mody Claude Code: cache-keeper i ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Bardzo opiniotwórcza wtyczka Claude Code zaprojektowana przez Rustaceana…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mody Claude Code, które pilnują agenta — haki funkcji strzegące zakresu…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Fresh from the factory. A Claude Code mod: ask for a meme, keep working.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Modyfikacja Claude Code: pasek pamięci podręcznej promptu, następne kroki…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code rysujący limity użycia i wydatki na pasku nad promptem.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Mod Claude Code do zapisywania myśli w trakcie pracy, porządkowania ich między…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Bieżący status PR GitHub, gotowość do scalania, kontrole, komentarze i alerty…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Modyfikacje Claude Code autorstwa Hermana (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Modyfikacje Claude Code: paski postępu planów, rejestr tego, co Claude…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notatki terenowe z pierwszego dnia o modach Claude Code na Windows: pasek…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: debugger dla wywołań narzędzi Code dla Claude.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Mod Claude Code: status pull request GitHub na żywo.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Małe karty umieszczone pod promptem Claude Code albo zadokowane obok…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: bieżące mierniki kosztu, kontekstu i limitu planu nad…
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 Robimy trochę TECHNO, bejbe 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin i mod Claude Code: AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code, który włącza lub wyłącza globalne umiejętności, agentów…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Przetestowane modyfikacje Claude Code instalowane jednym poleceniem…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Przytulna modyfikacja RPG HUD dla Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Zestaw modyfikacji claude code mojego autorstwa.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Modyfikacje Claude Code: panel floty agentów i autopilot.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modyfikacje Claude Code. touch-map: zobacz jako drzewo i mapę aktywności, które…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Ucz się języka obcego podczas pracy z Claude Code.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Modyfikacja Claude Code, która na bieżąco informuje, które pliki zmienił Claude…
- [0xctx/sysop](https://github.com/0xctx/sysop) - Powiedz Claude, czego chcesz. Otrzymasz wynik zbudowany, przetestowany…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Opiekuje się długą sesją Claude Code, abyś nie musiał tego robić: obserwuje…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - Modyfikacja Claude Code, która utrzymuje ciepłą pamięć podręczną promptu…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Pasek boczny na żywo z kosztami, tokenami i wykorzystaniem kontekstu dla Claude…
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - Modyfikacje Claude Code autorstwa ayagmar: rynek wtyczek.
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Modyfikacje function-hook dla Claude Code: wiersz telemetryczny limitów, panele…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Modyfikacje Claude Code dla prawdziwych inżynierów.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Podsumowanie sesji terminala Claude Code w karcie Code aplikacji desktopowej…
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Modyfikacja Claude Code: panel z zadaniem sesji, informacjami o tym, co wymaga…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Mod Claude Code: łap pixel-artowe Modstery w grze bezczynnościowej, podczas gdy…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zobacz, które pliki każdy agent Claude Code ma w swoim kontekście i ile każdego…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Małe mody Claude Code do terminala i aplikacji desktopowej.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Umiejętność + mod Claude CLI, który dodaje hiszpańskie słowa do odpowiedzi…
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Modyfikacja Claude Code, która oszczędza ponownego zapisywania pamięci…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Twoje zdarzenia Alarum nad promptem Claude Code: co właśnie nadeszło i jedno…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Lista zadań Floatee nad promptem Claude Code: uruchamiaj, prowadź i odhaczaj…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Modyfikacja Claude Code, która stylizuje go na The Machine z Person of Interest.
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Mod Claude Code (mod CC tint): koloruj każde okno według jego repozytorium…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesji, postęp Spec Kit na żywo i zarządzanie oknem…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Okno kontekstu jako jeden wiersz nad promptem, narysowane tak, jak Claude Code…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: wykres na żywo pokazujący, co wie Claude Code.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Panel HUD zadań na żywo dla Claude Code Desktop: pasek nad promptem podczas…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Wtyczka Claude Code (mod), która sprawia, że terminalowy interfejs Claude Code…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Nie pozwól, aby twoja uwaga błądziła podczas oczekiwania na odpowiedź Claude…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Czternaście modów Claude Code w jednej wtyczce, każdy z możliwością…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Darmowa, otwartoźródłowa wtyczka dla Claude Code.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: answer Claude point by point, right on the text.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Mody Claude Code do długich sesji: sitrep podsumowuje wynik każdej odpowiedzi i…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Kolejka promptów dla Claude Code w formie modyfikacji: /after &lt;task&gt; uruchamia…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Modyfikacje Claude Code: starannie wybrane i przetestowane, a każda modyfikacja…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Umiejętności Claude Code: weryfikator faktów w dokumentacji, audytor kodu…
- [Orfila-antoine/claude-mods](https://github.com/Orfila-antoine/claude-mods)
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Modyfikacja Claude Code, która prowadzi na żywo księgę dowodów przekazywanych…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Wtyczka Claude Code buddy: towarzysz ASCII nad promptem, który pamięta Twoje…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Wtyczka Claude Code do widoczności narzędzi per agent — ukrywaj i odmawiaj…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Modyfikacje Claude Code: warstwa bezpieczeństwa dla Claude Code — redagowanie…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Renderowanie matematyki LaTeX w trybie display w terminalu Claude Code…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Kolekcja świetnych modyfikacji Claude Code | Kolekcja modyfikacji Claude Code.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: nieoficjalny fanowski mod Avengers do Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: modyfikacja Claude Code, która na żądanie odczytuje na głos…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Daj klapsa Claude, gdy coś zepsuje — mod antystresowy dla Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mody Claude Code: małe wtyczki do aktualizowanych paneli, routingu modeli…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code z dowodami. Wtyczka, która planuje, deleguje i potwierdza wykonanie…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod i wtyczka Claude Code: monitor użycia, licznik tokenów i wiersz stanu.
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC (Every Mod Claude Code): wyselekcjonowany, przetestowany zbiór modów Code…
- [yyosifov/prompt-mods](https://github.com/yyosifov/prompt-mods) - Małe, ukończone modyfikacje Claude Code dla pola promptu.
- [0xgigilau/claude-usage-meters](https://github.com/0xgigilau/claude-usage-meters) - Modyfikacja Claude Code: paski postępu dla kontekstu, użycia w…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Marketplace modyfikacji Claude Code (my-claude-mods): pasek statusu, panele…
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Modyfikacje Claude Code: karty statystyk sesji nad polem promptu.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Animowany kot z alfabetu Braille.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Pikselowy kot nad promptem Claude Code, który wykonuje testowe połączenie z…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code, który wybiera dobry moment na kompakcję, aby utrzymać małe…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modyfikacje Claude dla Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Uniwersalne modyfikacje dla Claude Code: paski, panele, powiadomienia i hooki.
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - Modyfikacja Claude Code, która wybiera model dla każdego podagenta przed jego…
- [arthurseredaa/herdr-pane-peek](https://github.com/arthurseredaa/herdr-pane-peek) - Claude Code mod for herdr: search panes across all workspaces and insert the…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Limity wykorzystania Claude jako animowana karta zdrowia mieszkańca wioski, z…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mody Claude Code dla zespołu S2 (marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Krótkie treningi, gdy Claude pracuje: dzienny cel, serie, odznaki i opcjonalne…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Tablica zużycia dla Claude Code: wydatki według modelu.
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Modyfikacje Claude Code: panele, paski i zabezpieczenia działające wewnątrz…
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Modyfikacja Claude Code pokazująca, czym zajmują się podagenci: pasek postępu…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Modyfikacja Claude Code pokazująca, ile czasu zajęła każda tura, w postaci…
- [benelog/claude-mods](https://github.com/benelog/claude-mods) - Mods for Claude Code: a status-line HUD and more.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing dla Claude Code: Apple Music i Spotify nad poleceniem, z…
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - Utrzymywane, audytowane kopie modyfikacji Claude Code (filetree, cache-tax).
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - The Performance tab for Claude Code turns: a live waterfall of every model…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mody dla Claude Code: zegar cache, Blast Radius, sugestie, lista zadań, grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Po prostu sowa dla Twojego Claude Code.
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - Osobiste modyfikacje Claude Code.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Oryginalny silnik Doom z Freedoom, grywalny wewnątrz Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Małe, czytelne modyfikacje Claude Code z kanału CorporateChittyChat.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Utrzymuj Claude Code zgodnie z planem: etapy, bramki zatwierdzania i budżet…
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Modyfikacje Claude Code.
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Mod Claude Code: pasek nad promptem z odliczaniem pamięci podręcznej promptu…
- [curran-gehring/claude-dot](https://github.com/curran-gehring/claude-dot) - Modyfikacja Claude Code przenosząca kropki OpenAI do Claude: zawsze włączony…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - Moje osobiste modyfikacje Claude Code, dostosowane do mojej konfiguracji…
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Mody Claude Code przeznaczone wyłącznie dla zespołu d3nim.
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Modyfikacja Claude Code: sprawdzaj, z których umiejętności, wtyczek, podagentów…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Jedenaście modyfikacji Claude Code (wtyczek function-hook) do domowego…
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Modyfikacje Claude Code: tablica OpenSpec i podagentów, przekazanie przed…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi żyjące wewnątrz Claude Code: wykluwa się, zjada kod pisany przez…
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Modyfikacja Claude Code: stan przeglądu PR, zatwierdzenia, kontrole i konflikty…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Mod Claude Code: tablica pozostałych sesji nad promptem — kto na ciebie czeka…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - My collection of claude mods.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: po zablokowaniu wywołania narzędzia przez guard zatrzymuje…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code: zadania działające w tle w jednym widoku, z postępem i…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code: jedna skrzynka odbiorcza na wiadomości od członków zespołu…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code: wyjaśnia blokady piaskownicy i zamienia powtarzające się…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Ulubione dla Claude Code: ikony jednoklikowe dla poleceń i umiejętności.
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - Aktywna tablica falowa planu twojej sesji nad promptem Claude Code.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instrukcje, umiejętności, rozszerzenia Pi i mody Claude Code dla Pi, Codex i…
- [esinecan/mental-model-mod](https://github.com/esinecan/mental-model-mod) - Modyfikacja Claude Code: roboczy model Erena autorstwa Claude, przedstawiony…
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Modyfikacja Claude Code do śledzenia postępu testów w tle: JUnit, Karma, pytest…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mody do Claude Code (wtyczki function-hook): session-meter i inne.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: one tiny button that hides every Claude Code mod above your…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Modyfikacje zespołu Hospedin dla Claude Code w fazie testów.
- [fran343/claude-mods](https://github.com/fran343/claude-mods)
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Modyfikacja Claude Code: zamroź sesję i wznów ją później, jak gdyby nic się nie…
- [g761007/hudcade](https://github.com/g761007/hudcade) - Pikselowy HUD dla Claude Code: kontekst, koszt, pamięć podręczna, agenci i…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Kliknięcie Ctrl z klawiszem myszy kopiuje link w każdym bloku kodu w…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - Modyfikacja Claude Code dla aplikacji desktopowej: kliknij odwołanie do pliku w…
- [h3h/blocks-only](https://github.com/h3h/blocks-only) - Modyfikacja Claude Code: tury programowania kończą się zweryfikowanym raportem…
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Prywatny marketplace modów do Claude Code.
- [haruki-cl/claude-code-mods](https://github.com/haruki-cl/claude-code-mods) - Modyfikacje Claude Code: token-weather (panel użycia kontekstu i pamięci)…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Niemieckojęzyczne mody dla Claude Code: informacje o kontekście/cache, otwarte…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - A live spend meter for Claude Code: the session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Modyfikacja Claude Code: jak długo trwała każda odpowiedź, jak długo myślał…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - marketplace modyfikacji claude.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Kokpit nad promptem Claude Code. Kaczka odczytuje wskaźniki.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Automatycznie odczytuje rysunki techniczne, a następnie tworzy model w…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - Bieżąca tablica podagentów Claude Code wewnątrz VS Code: podagenci każdej…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel użycia kontekstu na pasku bocznym: suma, kategorie, przyrost w każdej…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista plików na pasku bocznym: które pliki utworzono, zmodyfikowano lub…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Futrzasty w stylu 8-bitowym.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel boczny „O co pytałem.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Oś czasu na pasku bocznym: na co przeznaczono czas w tej turze.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Panel wymiany tokenów na pasku bocznym: ile tokenów rozmowa główna wysłała do…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Szczera krótka rozmowa claude code: po każdej odpowiedzi Claude cicho mówi, co…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Lista kontrolna planu dla Claude Code z bramkowaniem dowodami: zatwierdzone…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code.
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Modyfikacje Claude Code autorstwa Josepha Ayoub: marketplace wtyczek…
- [jrojasdeveloper/naruto-buddy](https://github.com/jrojasdeveloper/naruto-buddy) - Modyfikacja Claude Code: animowany Naruto w pixel arcie nad promptem.
- [jrpferreira2002-jpg/clawd-vibe](https://github.com/jrpferreira2002-jpg/clawd-vibe) - Modyfikacja Claude Code: Clawd nad polem promptu, clawd ma nastroje.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd mieszka w pasku nad twoim promptem Claude Code: odgrywa sesję, pokazuje…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Modyfikacja odczytująca na głos odpowiedzi i powiadomienia Claude Code za…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mody do Claude Code. PixBar: pikselowe stworzenie nad Twoim promptem, które…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod Claude Code: każda sesja Claude Code w jednym pływającym oknie, z…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Małe modyfikacje Claude Code w jednym sklepie z wtyczkami.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Mod Code dla Claude: wybiera model i nakład pracy związane z rozumowaniem…
- [kyuskoj/claude-mods](https://github.com/kyuskoj/claude-mods)
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Te mody Claude Code: animowany pikselowy zwierzak, Code Wrapped, bity lo-fi, a…
- [Loup0007A/claude-mods](https://github.com/Loup0007A/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Tworzony przez społeczność przewodnik po modyfikacjach Claude Code: przypadki…
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Mod de Claude Code: los límites de tu plan (sesión 5h, semana) y la renovación…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Pojedyncze modyfikacje Claude Code z Mod Box, z których każdą można…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod do Claude Code, który pokazuje, co robi Claude, w podtytule karty iTerm2…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Puszysta czarna kotka nad promptem Claude Code.
- [malitov/effort-per-model](https://github.com/malitov/effort-per-model) - Claude Code mod: remembers the effort level per model and restores it on switch.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Mody Code Marcela dla Claude na jednym rynku wtyczek (marcel-mods).
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Małe modyfikacje dla Claude Code: runner-avatar, mały awatar biegnący nad…
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Modyfikacje Claude: licznik tokenów (token-meter).
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Modyfikacja Claude Code: panel na żywo pokazujący, do czego dąży agent…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod Code Claude: panel /sessions do przeglądania i usuwania sesji wraz z ich…
- [melandres8/claude-mods](https://github.com/melandres8/claude-mods) - Claude Code mods: relevo (planner/builder relay between two sessions) and…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel boczny dla Claude Code: pliki napisane przez Claude, podziały terminala…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Mod Code dla Claude: Codex (subskrypcja ChatGPT) oraz inne modele nie-Anthropic…
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [MoriHiroshiDesu/hiroshi-claude-mods](https://github.com/MoriHiroshiDesu/hiroshi-claude-mods) - Mods pessoais do Claude Code (interface e comportamento).
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Mod Code dla Claude: nadaje kartę terminala, w której działa Claude.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code, który ponownie włącza narzędzia todo dla modeli, które je…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Modyfikacja Claude Code, która czeka na bezpieczną pauzę, a następnie…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: jeden wiersz na zadanie nad promptem z bieżącym zadaniem…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Graj w Connect Four przeciwko AI wewnątrz Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: gdy inny agent programistyczny wykonuje commit w Twoim…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Mod do Claude Code: utrzymuje sesje w lekkiej formie — wiersz użycia…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code dla repozytoriów współdzielonych przez kilku agentów AI…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Modyfikacja Claude Code: jeden przycisk nad promptem dla każdego implementatora…
- [NicoSKOOL/seo-mods](https://github.com/NicoSKOOL/seo-mods) - Mody Code dla Claude do SEO: aktualne rankingi DataWise nad promptem oraz…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Ponownie uzbraja długie obserwacje Monitor w Claude Code po ich wygaśnięciu…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Zabezpieczenie SQL w Claude Code: pyta przed wykonaniem przez Claude poleceń…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Panel notatnika dla Claude Code jako mod.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Jeden mod dla Claude Code, Windows i CJK przede wszystkim: podgląd wklejonych…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mody Code dla Claude: miniatury obrazów i wiersz stanu.
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid: kompleksowy proces przegląd → plan → naprawa, wymuszany przez mody…
- [omarnaman/claude-mods](https://github.com/omarnaman/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Najlepsze mody Claude Code, posortowane według tego, co dla Ciebie robią.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dwa mody Claude dla Claude Code: garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Znaczniki czasu dla Claude Code: czas przy każdej wiadomości, odpowiedzi i…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: mod Code dla Claude. Trwałe worktree z dostępem tylko do odczytu na…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live session-stats side pane for the Claude desktop app.
- [PhilRoli/claude-mods](https://github.com/PhilRoli/claude-mods) - Mod Code dla Claude: wstrzymuje sesje, zanim przyjedzie Twój pociąg TrainTracker.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Moduły dla Claude Code: safety-guard blokuje destrukcyjne polecenia i dostęp do…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Animowany krab Claude w pixel art dla Claude Code: odgrywa nad Twoim promptem…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mody dla Claude Code: wtyczki function-hook działające wewnątrz sesji…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod dla Claude Code: pompki do zrobienia podczas pracy Claude. Bez tokenów.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: przewodnik terenowy po modach Code dla Claude, od ELI5 po…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - po prostu lista modów, których używam.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Trzy pozbawione zależności mody dla Claude Code: responsywny wiersz stanu…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mody dla claude code.
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Otwarty marketplace modyfikacji Claude Code, z umiejętnościami repozytorium do…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: zamienia plan zatwierdzony w trybie planu w aktywną listę…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Starannie wybrana lista modyfikacji Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Tryb bez kosztów: agenty pomocnicze działają na Haiku, a duże pliki i logi są…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ścieżka dźwiękowa lofi, która podąża za sesją: spokój, skupienie, przepływ, a…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Ucz się podczas kodowania przez Claude: po turze, która zmieniła kod, nad…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Nagranie każdej zmiany wprowadzanej przez Claude: odtwórz każdą zmianę…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - Mod Code dla Claude: pulpit projektu i izometryczna mapa miasta zadań, agentów…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board i inne mody Code dla Claude autorstwa André Servaes.
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Centrum dowodzenia dla Claude Code: na żywo flota subagentów, użycie tokenów i…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Mody do Claude Code autorstwa Showrin, zwiększające produktywność codziennej…
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Mod Code dla Claude: limity kontekstu i planu z prognozą tempa zużycia oraz…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Mod Code dla Claude, który podtrzymuje działanie sesji bez nadzoru po…
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Claude Code mod: context-window meter per session, with Compact now…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - Zbiór modyfikacji Claude Code: TypeScript hooków funkcji, dostarczanych jako…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Wiadomości commitów jednym kliknięciem dla Claude Code z tańczącą Malenią w…
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Mody dla Claude Code. cache-meter: współczynnik trafień pamięci podręcznej…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — mod Claude Code pokazujący użycie planu Claude.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Unofficial Claude Code mods by tanmen (marketplace: tanmen).
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Mod Code dla Claude: aktualny panel zespołu dla każdego podagenta.
- [thangnguyen-69/claude-mods](https://github.com/thangnguyen-69/claude-mods) - Rynek wtyczek Code dla Claude: recenzje Plannotator w tailnecie i kolejne…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Modyfikacja Claude Code, która wyświetla bieżącą sesję w panelu: każdy prompt…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace pluginów Claude Code z modami: pluginy function-hooks, które rysują…
- [tiger3645/claude-tts](https://github.com/tiger3645/claude-tts) - Claude Code: modyfikacja odczytująca na głos odpowiedzi Claude.
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Mod Code dla Claude: jeden przycisk pod ostatnią odpowiedzią Claude kopiuje…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Mody Claude Code od Toptaab.
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - Tryb CC, który pokazuje, na jakie konto Claude, organizację i plan jesteś…
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Kilka modów Claude.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Modyfikacja Claude Code: animowany pasek postępu i podsumowanie ukończenia dla…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trzy małe mody Claude Code: sprawdzaj, kiedy Twoi podagenci skończą pracę…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Powiedz „I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Zadaj Claude pytanie poboczne w panelu obok swojej pracy.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Wtyczka Claude Code: odliczanie pamięci podręcznej promptu, współczynnik…
- [webfront/claude-mods](https://github.com/webfront/claude-mods) - Specjalne mody dla claude code i kodu w aplikacji claude.
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Claude Code: własny model sesji wybiera model i nakład pracy każdego subagenta.
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Niewielkie modyfikacje ułatwiające pracę z Claude Code.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — gdy kontekst przerasta swoją powłokę, zrzuca ją do folderu i działa…
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod dla Claude Code: ukryte sekrety, zadania do wykonania, kontrole i CI…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Wtyczka Claude Code: limity użycia Claude Pro/Max wraz z prognozą tempa…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mody dla Claude Code. agent-crew: obserwuj pracę swoich podagentów jako żywą…
- [zhitongLIU/claude-code-mods](https://github.com/zhitongLIU/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Starannie wybrana kolekcja najlepszych zasobów dla najbardziej niesamowitych…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Wtyczka Claude Code pokazująca, co się dzieje — wykorzystanie kontekstu…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Piękna, wysoce konfigurowalna linia statusu dla Claude Code CLI z obsługą…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Wszystkie części promptu systemowego Claude Code, 27 wbudowanych opisów…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Umiejętność tworzenia filmów AI dla Claude Code i Codex — kinowe filmy…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Ponad 45 wskazówek, jak najlepiej wykorzystać Claude Code — od podstaw po…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generuj karuzele Xiaohongshu oraz pary okładek…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Przeglądaj różnice wygenerowane przez agenta programistycznego w panelu…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Kompleksowa wtyczka paska stanu dla Claude Code z informacjami o wykorzystaniu…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Twórz modyfikacje dla Claude Code: przechwytuj dowolne żądanie, modyfikuj…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Kompleksowy pulpit statusu dla Claude Code — informacje o sesji, paski limitów…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: śledź ślad węglowy swoich sesji Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Estetyczna linia statusu dla Claude Code autorstwa awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agent DeepSeek Harness do długich sesji roleplay (wtyczka tawerny DSH): import…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Publiczne Skills i modyfikacje Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, modyfikacje, subagenci, hooki, polecenia slash i poradniki dla Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legalne bezpłatne LLM APIs i agenci kodowania — automatycznie aktualizowane…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Wyniki na żywo, terminarze i tabele piłki nożnej dla rozgrywek, które…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, który zmienia agenta kodowania w eksperta od firmware.
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) - Sesja DeepSeek Harness oparta przede wszystkim na głosie: przycisk mikrofonu…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Pory modlitw, data hidżry, adhkar, codzienny ajat, post sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Osobista konfiguracja Claude Code, wersjonowana w ~/.claude — agenci…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — wtyczka DeepSeek Harness do tematów badawczych…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - Warstwa orkiestracji wielu agentów dla DeepSeek Harness (omd) — tryby…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Zestaw wtyczek dla Claude Code, pi i DeepSeek Harness: HUD paska stanu, pasek…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Portable Claude Code toolkit for .NET DDD/Clean Architecture: strict TDD…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Lekki wiersz stanu Claude Code — jeden skrypt Bash o długości około 170…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Przenośna globalna konfiguracja Claude Code: niestandardowe umiejętności, hooki…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Nieoficjalne mody karty Code w Claude Desktop — usage-pet: pasmo zużycia z…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Wtyczki Claude Code, których używam codziennie: skills i mody uporządkowane…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analizuj użycie tokenów i koszty Claude Code na podstawie lokalnych dzienników…
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Estetyczny i informacyjny wiersz statusu dla Claude Code.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Wizualna tablica dla agentów Claude Code: wyświetlaj sesje, podagentów i…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Konfigurowalny wiersz statusu dla Claude Code z edytorem opartym na…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace wtyczek i umiejętności Claude Code ułatwiających tworzenie modów do…
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Jednowierszowy, oznaczony kolorami statusline dla Claude Code — folder, model…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Zarządzanie tokenami dla Claude Code: najlepszy model kieruje pracą, a…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Przeglądarka z podzielonym panelem dla Claude Code w Windows Terminal i tmux…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Mikropulpit na 3 wiersze dla terminala Claude Code — model, zużycie kontekstu…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repozytorium modów Awesome Media dla Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Ogranicz wydatki na Claude Code i tokeny Codex: kieruj wyszukiwania i…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Szybki, konfigurowalny statusline dla Claude Code — pojedynczy statyczny plik…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Wyświetla wiersz stanu Claude Code z limitami szybkości, bieżącym katalogiem i…
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Kompaktowy, aktywnie utrzymywany wiersz statusu dla Claude Code — model, nakład…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - przyjazny pasek stanu Claude Code, przy którym można zmienić wszystko — paski…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definiowalne fabryki oprogramowania dla Claude Code na herdr: grafy stacji…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows Pasek stanu PowerShell dla Claude: limity 5-godzinne i tygodniowe z…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Wiersz stanu Claude Code w Lua wraz z działającym na żywo playgroundem Neovim.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod.
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - Rozszerzenie VS Code: postęp zadań Code dla Claude, przewidywany czas…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mody dla Claude Code: aktualne panele, wskaźniki i więcej, instalowane jako…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Kolorowa linia statusu Claude Code: limity planu, kontekst, koszt i tokeny.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Linia statusu Claude Code dla Windows: sumy tokenów, koszt według stawki API i…
- [gvart/claude-config](https://github.com/gvart/claude-config) - Moja konfiguracja Claude Code: modyfikacja agent-monitor, umiejętności, agenci…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Jednowierszowy pasek stanu dla Claude Code: model, git, kontekst, tokeny…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Podgląd obrazów wewnątrz Claude Code: najedź na znacznik pod odpowiedzią, aby…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Wiersz stanu Code dla Claude: model, paski limitów 5-godzinnego/7-dniowego…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Osobista konfiguracja Claude Code: uprawnienia, pasek stanu, serwery MCP.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Wiersz stanu Claude Code z wierszami panelu agentów.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: przenośna konfiguracja Claude Code — globalne reguły, zestaw…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Wyświetla szczegółowy, oznaczony kolorami pasek stanu dla Claude Code…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Śledź stan Claude Code za pomocą kompaktowego pulpitu pokazującego kontekst…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Dwuwierszowy pasek stanu dla terminalowego agenta programistycznego: katalog…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook linii statusu Claude Code — śledzi użycie tokenów i kontekst między…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Wiersz stanu Code dla Claude z instalatorem dla Linux i Git Bash na Windows.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - własne, wolne od klatek wtyczki, umiejętności, mody i nie tylko dla claude.
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Marketplace Claude Code od MSF Supply: modyfikacje wybrane i przypięte do…
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Rozbudowany wielowierszowy wiersz stanu dla Claude Code — aktualne limity…
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Wielowierszowy wiersz stanu Claude Code: pasek kontekstu, gałąź git, paski…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — wiersz stanu Claude Code dla macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitoruj stan Claude Code z paska menu macOS dzięki wskaźnikom w czasie…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Umiejętności i modyfikacje dla Claude Code i Cowork — project-tracker…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Wiersz stanu Claude Code dla Windows (PowerShell): paski użycia, odliczanie…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Niestandardowy wiersz stanu Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Konfiguracja i mody Code dla Claude, ze wspólnym zestawem komponentów…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Mechanizmy kontroli ryzyka modeli dla Code dla Claude: 25 kontroli w sześciu…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Szkielet startowy dla Claude Code: hooki, statusline, modele lokalne…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - 4-wierszowy wiersz stanu dla Claude Code.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Przenośna konfiguracja Code dla Claude: CLAUDE.md, ustawienia, wiersz stanu…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Uniwersalny wieloprotokołowy StatusLine, samouczący się kontekst i wtyczka…
- [tylergraydev/cc-mods](https://github.com/tylergraydev/cc-mods) - Mody dla Claude Code: panele boczne, wiersze stanu, powiadomienia i…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Śledź użycie kontekstu Claude Code, koszty sesji i resety limitów zapytań…
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - Moje umiejętności, wtyczki i mody Claude Code (marketplace: vladdu).
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Synchronizacja między wieloma maszynami konfiguracji użytkownika Claude Code…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Statusline Claude Code z gradientowymi paskami postępu, wysiłkiem sesji…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Wiersz stanu Claude Code: folder, gałąź git, model, użycie okna kontekstu i…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detektor degradacji kontekstu 2026 — proaktywny monitor pamięci AI i limitu…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooki, subagenty i linie stanu Claude Code: kolekcje i narzędzia open source…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code pokazujący bieżące zużycie tokenów i szacowane zużycie…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mody dla Claude Code: panele, pasma i towarzysze zbudowani na hakach funkcji.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Przekazuj zadania między sesjami Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - To jest serwer MCP do sterowania MODS, modułowym narzędziem wieloplatformowym…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Umiejętność Codex i Claude Code do tłumaczenia modów CK3 za pomocą lokalnego LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mody open source i inne rozszerzenia dla Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: znajdź to, o co ponownie i ponownie prosisz Claude Code, i zamień to…

</details>

<a id="dsh-cordis"></a>

## Ekosystemy wtyczek DSH i Cordis

DeepSeek Harness i Cordis docierają do tego samego miejsca z innego kierunku: dla nich wtyczka jest mechanizmem modów, więc wtyczka w tamtym ekosystemie jest odpowiednikiem moda tutaj.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74439 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

🌊 Oryginalny harness agenta. Wdrażaj inteligentne wieloagentowe roje, koordynuj autonomiczne przepływy pracy i twórz konwersacyjne systemy AI. Oferuje adaptacyjną pamięć, samouczącą się inteligencję, federację, integrację wektorową RAG oraz natywną obsługę Claude Code / Codex / Hermes i wielu innych zintegrowanych narzędzi.

<sub>🔧 Znaleziono użycie w kodzie: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                 |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **74439**  |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐153127 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Inżynieria wsteczna wszystkiego za pomocą agentów — od działania aplikacji po natywne pliki binarne.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **153127** |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100748 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

🎨 Najlepsza wtyczka do projektowania DeepSeek Harness. Alternatywa open source dla Claude Design. 🖥️ Aplikacja desktopowa z podejściem local-first. 🖼️ Twój agent programistyczny staje się silnikiem projektowym: prototypy, strony docelowe, pulpity nawigacyjne, slajdy, obrazy i wideo — rzeczywiste pliki, eksport HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode i ponad 20 CLI przez BYOK.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **100748** |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82525 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Przekształć dowolny pomysł, plan lub bazę kodu w piękny interaktywny diagram. Umiejętność agenta dla Claude Code, Codex i innych.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **82525**  |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Niezawodny agent programistyczny do złożonych zadań inżynierii oprogramowania.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Go                                                                               |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **35769**  |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25532 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Distilly — przekształcaj sposób, w jaki myślą, w wielokrotnego użytku Skills dla dowolnego Agenta lub Bota. Wcześniej Colleague Skill（原同事 Skill）.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **25532**  |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18516 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wyselekcjonowana lista wtyczek dla DeepSeek Harness (dsh) · Wyselekcjonowana lista wtyczek DeepSeek Harness

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **18516**  |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8667 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Ekosystem agregacji wtyczek DeepSeek Harness (DSH) Web · Wszystko jest wtyczką, dystrybuowaną przez Creative Workshop ｜｜Ekosystem agregacji wtyczek DeepSeek Harness (DSH) Web · Wszystko jest wtyczką, dystrybuowaną przez Creative Workshop

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **8667**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6275 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Rynek wtyczek wewnątrz DeepSeek Harness — przeglądaj, wyszukuj i instaluj jednym kliknięciem · Wizualny rynek wtyczek DSH

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6275**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4461 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Oficjalnie najbardziej polecany plugin TUI dla DSH — wysoka wydajność, niski narzut, uroczy pikselowy wieloryb, płynna obsługa myszy. Instalacja jednym poleceniem przez npm. / Oficjalnie najbardziej polecany plugin TUI dla DSH: wysoka wydajność, niski narzut, uroczy pikselowy wieloryb, płynna obsługa myszy, instalacja jednym poleceniem przez npm

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **4461**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3680 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Pierwszy na świecie wirtualny terminal dla agentów AI

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3680**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3034 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness Tauri wersja desktopowa | Instalator tylko 8mb, zerowa konfiguracja środowiska, gotowe wtyczki, Windows / macOS / Linux.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3034**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1911 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Podłącz boty IM do DeepSeek Harness za pomocą kodu QR lub danych uwierzytelniających (9 kanałów).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1911**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1423 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Oprogramowanie AI do tworzenia powieści: organizuje inspiracje, postacie, budowanie świata, konspekty, pisanie rozdziałów, recenzowanie i poprawianie w kontrolowany przepływ pracy; oferuje wersje desktopowe dla Windows/macOS oraz obsługuje modele lokalne i online. Oprogramowanie AI do pisania powieści: organizuje inspiracje, postacie, budowanie świata, konspekty, tworzenie rozdziałów, recenzowanie i poprawianie w kontrolowany przepływ pracy. Oferuje aplikacje desktopowe dla Windows/macOS, integrację z Ollama oraz wersję demonstracyjną wtyczki DeepSeek Harness (DSH).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1423**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1182 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Pamięć dla Claude Code, Codex, Cursor i 38 innych agentów programistycznych, zbudowana na podstawie historii sesji znajdującej się już na Twoim dysku. Lokalne wyszukiwanie, MCP i hooki, bez LLM, jeden binarny plik Go.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Go                                                                               |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1182**   |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wecode-ai/Wegent">wecode-ai/Wegent</a></b> · ⭐870 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Plan, build, and deliver with an open-source, self-hostable AI workspace for coding, collaboration, and automation.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **870**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent` · `ai` · `chatbot` · `claude-code` · `codex` · `dsh-plugin` · `wework`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wecode-ai--wegent/991765bc5aba6a3c.png" width="100%" alt="wecode-ai/Wegent screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **593**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **526**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐261 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Nieoficjalna wtyczka DSH (DeepSeek Harness): używaj modeli internetowych chat.deepseek.com jako dostawcy LLM — przechwytywanie logowania w przeglądarce, rozwiązywanie PoW, strumieniowanie SSE, wywołania narzędzi oparte na promptach.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **261**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

ACRYL - Agent Context Relay Yielding Lifecycles. Jeden trwały obszar roboczy, jeden kanoniczny kontekst, dowolny agent programistyczny.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **255**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-research-report">PerryLink/dsh-research-report</a></b> · ⭐214 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Weryfikowalny silnik raportów badawczych dla DeepSeek Harness: księga dowodów adresowanych treścią (powiązanie twierdzenie–migawka, wykrywanie manipulacji) oraz wersjonowane, zapieczętowane raporty z werdyktami weryfikacji dla poszczególnych twierdzeń i katalogiem zapieczętowanym manifestem.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **214**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `audit` · `citation-verification` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/2a270ca82dba24d3.png" width="100%" alt="PerryLink/dsh-research-report screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/dafefe1b3e0cd96e.gif" width="100%" alt="PerryLink/dsh-research-report animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Interfejs terminala w stylu Claude Code dla DeepSeek Harness, obsługujący Windows, macOS i Linux, kompatybilny z przezroczystym terminalem, motywami VS Code oraz niestandardowymi kolorami.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **197**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐194 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

🚀 Wtyczka zdalnego dostępu wielokanałowego i ochrony bezpieczeństwa DeepSeek Harness | Bezpośrednie połączenie przez kod QR w sieci lokalnej, tunel Cloudflare / własny tunel publiczny, pełny cykl rozmów z botami WeChat / QQ / Feishu / Telegram | Wbudowane uwierzytelnianie bezpieczeństwa dostępu we wszystkich protokołach, ochrona przed manipulacją w tle oraz system odzyskiwania po awariach

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **194**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wtyczka DeepSeek Harness do możliwej do podglądu migracji sesji między presetami. Przekazania o stałym schemacie zachowują stan, intencję modelu źródłowego i nierozwiązane obrazy; oryginalna sesja pozostaje nietknięta.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **165**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐144 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Motyw pulpitu Claude Code dla DeepSeek Harness｜ Motyw pulpitu Claude Code stworzony dla internetowego GUI DeepSeek Harness

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **144**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-memento">PerryLink/dsh-memento</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Ograniczona, warstwowa, zatwierdzana i audytowalna pamięć między sesjami dla DeepSeek Harness: warstwa możliwości ctx.memory z pozbawionym zależności dostawcą SQLite, narzędziem pamięci i wstrzykiwaniem zamrożonych migawek. Status utrzymania: FROZEN od 2026-10-05.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **141**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-memory` · `ai-agent` · `ai-agents` · `approval` · `audit` · `cordis` · `deepseek-harness` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/f63bd5eb5a8052b8.png" width="100%" alt="PerryLink/dsh-memento screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/0ce3328d348abdce.gif" width="100%" alt="PerryLink/dsh-memento animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐140 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Po instalacji otrzymujesz 27 umiejętności z zakresu inżynierii i produktywności z mattpocock/skills v1.3.1 — bez konieczności ręcznej instalacji. 40 miliardów tokenów posłużyło do stworzenia tej wtyczki, która zapewnia 10-krotnie większą produktywność niż oryginalne umiejętności i pomaga początkującym szybciej rozpocząć pracę z tym zestawem. Pełne wsparcie dla GitHub issue; Markdown jest w wersji podglądowej; GitLab nie jest obecnie obsługiwany. Dziękujemy za korzystanie i wsparcie 💗

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **140**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-permission-rules">PerryLink/dsh-permission-rules</a></b> · ⭐122 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Deklaratywne reguły uprawnień w stylu Claude Code dla DeepSeek Harness: uporządkowane reguły zezwalania/odrzucania/pytania z dopasowaniem nazwy narzędzia, argumentu (glob/regex) i ścieżki obszaru roboczego w potoku tools/pre-execute, audytem dziennika sesji i przeładowaniem HMR.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **122**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `ai-safety` · `allow-deny-ask` · `approval` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/d950618f5f9cf382.png" width="100%" alt="PerryLink/dsh-permission-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/25c9ccd2f2133850.gif" width="100%" alt="PerryLink/dsh-permission-rules animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AskTheWay/dsh-auto-memory">AskTheWay/dsh-auto-memory</a></b> · ⭐106 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Claude Code-style auto-memory plugin for DeepSeek Harness (dsh): typed memory files + MEMORY.md index auto-injected into the system prompt. File-only, no external services.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **106**    |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-harness` · `agent-memory` · `ai-agent` · `ai-tools` · `auto-memory` · `claude-code` · `coding-agent` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/asktheway--dsh-auto-memory/1ff60db2b929f245.png" width="100%" alt="AskTheWay/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wtyczka DeepSeek Harness (DSH): ✨ ulepszanie promptów jednym kliknięciem + 💬 rozpoznawanie mowy (automatyczne zatrzymanie po zakończeniu mówienia · podwójny silnik chmurowy/lokalny) · dodatkowo 🔁 ponowne uruchamianie usługi jednym kliknięciem w razie awarii

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **90**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Desktopowy agent zbudowany na bazie rdzenia Deepseek-Harness. Dziedziczy wszystkie możliwości podstawy i uzupełnia funkcje związane z IDE.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **69**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Rynek wtyczek społeczności DeepSeek-Harness, który automatycznie je kategoryzuje, gromadzi i weryfikuje. Automatycznie kategoryzuje, gromadzi i weryfikuje rynek wtyczek społeczności DeepSeek-Harness.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **69**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-fund-research">PerryLink/dsh-fund-research</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Deterministyczne raporty badawcze dotyczące chińskich publicznych funduszy inwestycyjnych, jako wtyczka DeepSeek Harness: na wejściu jeden kod funduszu, na wyjściu wersjonowany raport Markdown z dekompozycją wyników, penetracją portfela, atrybucją stylu i wyraźnymi deklaracjami braków danych. Metryki są obliczane w kodzie, a nie przez model.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **68**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `finance` · `fund-research`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/9a258f42b5375ed7.png" width="100%" alt="PerryLink/dsh-fund-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/c127c0b5eda50892.gif" width="100%" alt="PerryLink/dsh-fund-research animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐60 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wtyczka z motywami Catppuccin dla DeepSeek Harness Web GUI: błyskawiczne przełączanie między czterema motywami — Latte / Frappé / Macchiato / Mocha — oraz wbudowany, opcjonalny efekt szklanego interfejsu (Glassmorphism)

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **60**     |
| Ostatni push           | 2026-10-12 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Ochrona wykonywana przed uruchomieniem dla agentów AI do kodowania.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Wyselekcjonowana lista najlepszych świetnych wtyczek AI dla asystentów AI, w…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace: przeglądaj, instaluj i aktualizuj jednym kliknięciem…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、211个世界与上万素材、开局随心定制、世界自行运转、零漂移存档.
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - Ciągle aktualizowane artykuły naukowe z grafiki komputerowej, 3DGS i…
- [arcships/rutis](https://github.com/arcships/rutis) - Środowisko uruchomieniowe wtyczek dla oprogramowania, które samo się iteruje…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Społecznościowy agregator wtyczek DeepSeek Harness — automatyczna…
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Aktualny katalog wtyczek DeepSeek Harness — odświeżany co godzinę, codziennie…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana: DeepSeek Harness jako podagent dla HanaAgent.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Świadome zadań pobieranie kontekstu obszaru roboczego i śledzenie cyklu życia…
- [GDWhisper/dsh-web-startup-auth](https://github.com/GDWhisper/dsh-web-startup-auth) - Wtyczka zdalnego uruchamiania Web dla DSH (DeepSeek Harness) + uwierzytelnianie…
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - Wtyczka DeepSeek Harness: deterministyczne profilowanie, czyszczenie i…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent to otwarty FDE Harness dla agentów programistycznych AI — przy wejściu…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Otwarta alternatywa dla GrokBot zbudowana na DeepSeek Harness.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Wyselekcjonowany katalog wtyczek DeepSeek Harness (DSH) — ponad 280 wtyczek…
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - Baza wiedzy o tworzeniu wtyczek DeepSeek Harness (dsh): 10-rozdziałowy…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: wieloplatformowy system agentów do czatów grupowych oparty na…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Wtyczka DSH: powłoka Git Bash dla wszystkich trybów agentów na Windows…
- [YRN-playmaker/dsh-wallpaper_share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - Wtyczka do synchronizacji różnego rodzaju dynamicznych tapet z silnika tapet…
- [AskTheWay/dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor) - ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Kolekcja wtyczek webowego GUI DSH (DeepSeek Harness) — powiadomienia o…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Wtyczka WWW DSH: dzienne statystyki użycia tokenów z mapą cieplną aktywności w…
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - Przejrzysty ranking i rekomendacje ekosystemu wtyczek DSH: codzienne…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Prawdziwy PowerPoint, nie HTML. Powiedz AI, co ma zawierać prezentacja, a…
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - Synchronizacja sesji DeepSeek Harness między urządzeniami: dedykowany mirror…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Lokalny graf wiedzy o kodzie i środowisko kontekstu dla agentów kodowania, z…
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - Wtyczka WWW DSH: hierarchiczne drzewo obszaru roboczego na pasku bocznym…
- [ddtcorex/govard](https://github.com/ddtcorex/govard) - Orkiestrator lokalnego programowania oparty na Go dla Magento, Laravel…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Zamień modele zalogowane w lokalnej aplikacji desktopowej WorkBuddy.
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) - Tłumaczenie parametrów dostawców i deterministyczna naprawa JSON dla DeepSeek…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - Dwujęzyczny, stale utrzymywany katalog wtyczek do DeepSeek Harness (DSH).
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - Wielowymiarowe ocenianie jakości wtyczek DeepSeek Harness: ocenia repozytorium…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Izolowane testy instalacji i uruchomienia wtyczek DeepSeek Harness: instalują…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Wtyczka doku funkcji DeepSeek Harness: jeden panel do…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Ciągłe testowanie kompatybilności wtyczek DeepSeek Harness: dokładne wydania…
- [liang-today/dsh-liangxiang](https://github.com/liang-today/dsh-liangxiang) - 众香成势，梁子显相。DeepSeek Harness 的 WebUI 插件，欢迎一起打梁.
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Wtyczka hosta DeepSeek Harness, która przechowuje dokumenty projektowe i pamięć…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - Wyselekcjonowany katalog wtyczek DeepSeek Harness (DSH), oparty na dowodach…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Prześwietlenie wtyczek DeepSeek Harness: zadeklarowane możliwości a rzeczywiste…
- [ayingQAQ/dsh-web-launcher](https://github.com/ayingQAQ/dsh-web-launcher) - Windows 上的 DeepSeek Harness Web 一键启动器｜One-click launcher with background…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Obszar roboczy z wieloma folderami: pozwala agentowi DSH (DeepSeek Harness)…
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Wykonywanie DeepSeek Harness (dsh) z użyciem Podman.
- [kelemiao/dsh-animation-optimization](https://github.com/kelemiao/dsh-animation-optimization) - Optymalizacja animacji DSH: wtyczka wyglądu animacji strumieniowych i w stylu…
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - Rozmowy głosowe local-first dla DSH. Uruchamiaj rozpoznawanie i syntezę mowy na…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Wtyczka DSH: okno narzędzi Git klasy IDE jako natywna karta dsh-better-sidebar…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - Tryb kreatywny oparty na trybie PTC: wtyczka DSH łącząca orkiestrację narzędzi…
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Pakiet funkcji strony dla DeepSeek Harness (dsh): dok terminala, drzewo plików…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Daj DeepSeek Harness Agent natywne ręce i nogi do obsługi GitHub! Natywnie…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Wzorzec weryfikacji wtyczek DeepSeek Harness (dsh) bez zależności — bramki…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Ekosystem wtyczek DeepSeek Harness: 86 wtyczek open source w rodzinie 101…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Rynek wtyczek DeepSeek Harness — przeglądaj, wyszukuj i instaluj wtyczki z…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode w DeepSeek Harness — wtyczka DSH, która zapewnia działanie OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace wtyczek firm trzecich i zabezpieczony menedżer cyklu…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx to zorientowana na człowieka, rozszerzalna desktopowa przestrzeń…
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Uruchamiaj DeepSeek Harness na komputerze bez kosztów tokenów — darmowy…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Bots workbench: wtyczka Cordis łącząca bramę orkiestracji sdk-bots z web…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Rodzina wtyczek samodoskonalenia agentów inspirowana Hermesem, stworzona…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — społecznościowy zestaw do lokalnego wdrażania i utrzymania dla…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Wtyczka internetowa DeepSeek Harness (DSH): zakładka paska bocznego…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Niezależne wtyczki i narzędzia stron trzecich dla DeepSeek Harness, utrzymywane…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Używaj darmowych modeli OpenCode Zen w DeepSeek Harness z dostępem anonimowym…
- [yangzhe1991/dsh-web-enhance](https://github.com/yangzhe1991/dsh-web-enhance) - Rozszerzona wtyczka DSH Web UI: domyślne rozwijanie łańcucha myślenia…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Wtyczka DeepSeek Harness: przekształca błąd aprowizacji ACL piaskownicy Windows…
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Terminy na poziomie wdrożenia dla wywołań narzędzia dsh, które ich nie…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Środowisko uruchomieniowe wtyczek Rust z jądrem cyklu życia zweryfikowanym…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Wtyczka Cordis / DeepSeek Harness — znormalizowane narzędzia GitHub API dla…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Wbudowany pulpit Antigravity: tok/s, współczynnik trafień pamięci podręcznej w…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Arkme account, records, chat and interwoven-moments integration for DeepSeek…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Sklep z wtyczkami dsh — automatyczne wykrywanie i synchronizacja co godzinę na…

</details>

<a id="writing"></a>

## Teksty, dyskusje i wideo

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Podsumowanie

Cześć HN, stworzyłem to na własny użytek i chciałem udostępnić jako open source. Problem polegał na tym, że potrzebowałem sposobu na otrzymywanie przypomnień między promptami, ponieważ często spędzam długie godziny w terminalu, zwłaszcza teraz, gdy zwykle przetwarzamy równolegle tak wiele agentów. Pierwsza wersja była prostym rep

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

##### 📝 Podsumowanie

Nie opublikowano opisu w upstreamie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

##### 📝 Podsumowanie

Zbudowałem to, ponieważ przy najnowszych modelach kodujących Claude przechodzi w tryb głębokiej pracy z niejasnymi poleceniami, przez co nie wiem już, co robi. To modyfikacja (wtyczka wykorzystująca nowe haki funkcji Claude Code), która rysuje jedną linię nad promptem: — bieżący krok,

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Teksty, dyskusje i wideo`                                        |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Pierwsze uwzględnienie | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Projekty według języka implementacji

The ecosystem is concentrated in Python and TypeScript, but typed clients keep appearing in other languages. This table is generated from the entries themselves.

| Język      | Wpisy | Przykładowe projekty                                                                                            |
| ---------- | ----- | --------------------------------------------------------------------------------------------------------------- |
| TypeScript | 378   | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                            |
| JavaScript | 78    | `fschmutz/claude-usage-panel`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`               |
| Python     | 40    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`   |
| Shell      | 26    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`             |
| HTML       | 15    | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                       |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                                 |
| Go         | 4     | `mitre/claude-statusline`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                      |
| PowerShell | 3     | `Gabriel-Dalton/claude-statusline-tokens`, `markallisongit/claude-statusline`, `rainyfei/claude-statusline-win` |
| C          | 2     | `reporails/arcade`, `tylergraydev/cc-mods`                                                                      |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                         |
| Lua        | 1     | `crafts69guy/claude-statusline.nvim`                                                                            |
| Swift      | 1     | `peaceinitiativemenhadenoil263/claude-status-bar`                                                               |

<sub>Liczone są tylko wpisy, w których określono język. Wpisy dokumentacyjne i dyskusyjne są wyłączone z tej tabeli.</sub>

## Współtworzenie

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Ostatnia aktualizacja · 2026-10-13T06:19:35+08:00</sub>
