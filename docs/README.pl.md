<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Świetne mody Claude">
</p>

<h1 align="center">Świetne mody Claude</h1>

<p align="center"><b>Indeks modów i wtyczek do Claude Code, ocenianych na podstawie dowodów, oraz głębszych zmian w zachowaniu, które wprowadzają.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-599-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <b>Polski</b> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Aktualny indeks** · Ostatnia synchronizacja: `2026-10-10T23:31:01+08:00` (UTC+8)
> · Wpisy: **599** · Dodane w najnowszej aktualizacji: **0** · Języki implementacji: **12**

<sub>Każdy poniższy wpis został automatycznie zebrany, przefiltrowany i ponownie sprawdzony. Żaden z nich nie jest płatną promocją.</sub>

<a id="featured"></a>

## Polecane teraz

<sub>Jeden wpis na kategorię, uszeregowany według oceny dowodów i liczby gwiazdek; ranking jest tworzony ponownie przy każdej aktualizacji. To ranking, a nie rekomendacja — każdy wybór prowadzi do jego pełnej karty poniżej. Preferowane są projekty, które opublikowały zrzut ekranu lub nagranie, aby pasek pozostał wizualny.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9463 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods">
<b>🧩 <a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b>
<sub>⭐178 · TypeScript · 👁️ observed</sub>
<sub>Modyfikacje Claude Code: wtyczki oparte na hookach, które dodają dynamiczne wiersze nad poleceniem, zabezpieczenia, panele i gry. Pasek kontekstu, miernik użycia,…</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74252 · TypeScript · 👁️ observed</sub>
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
- [Mody: stworzone z użyciem możliwości tworzenia modów](#mody-stworzone-z-użyciem-możliwości-tworzenia-modów) — **467**
- [Ekosystemy wtyczek DSH i Cordis](#ekosystemy-wtyczek-dsh-i-cordis) — **104**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150006 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Podsumowanie

Claude Code to agentyczne narzędzie programistyczne działające w terminalu, które rozumie bazę kodu i pomaga programować szybciej, wykonując rutynowe zadania, wyjaśniając złożony kod i obsługując przepływy pracy git — wszystko za pomocą poleceń w języku naturalnym.

<sub>🔧 Znaleziono użycie w kodzie: `feed.xml`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |
| Język     | TypeScript                                                         |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **150006** |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9463 · TypeScript · ✅ official · 0 天</summary>

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
| Gwiazdki               | **9463**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8243 · Python · ✅ official · 0 天</summary>

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
| Gwiazdki               | **8243**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6331 · Python · ✅ official · 240 天</summary>

##### 📝 Podsumowanie

Zasilana przez AI akcja GitHub do przeglądu bezpieczeństwa, wykorzystująca Claude do analizy zmian w kodzie pod kątem luk w zabezpieczeniach.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |
| Język     | Python                                                             |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6331**   |
| Ostatni push           | 2026-02-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 0 天</summary>

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
| Gwiazdki               | **1797**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐24 · ✅ official · 308 天</summary>

##### 📝 Podsumowanie

Materiały uzupełniające do Claude Model Cards

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `published by Anthropic itself`                                    |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **24**     |
| Ostatni push           | 2025-12-05 |
| Pierwsze uwzględnienie | 2026-10-05 |

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Oficjalne moduły Claude Code od See Stack: interaktywny pasek kontekstu, odtwarzacz głosu i narzędzia terminala.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                            |
| --------- | ------------------------------------------------------------------ |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic` |
| Źródło    | `its own text names a mod API, or it declares the mod capability`  |
| Język     | TypeScript                                                         |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **0**      |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/6cbb21cab871f393.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/6cbb21cab871f393.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Konsola zarządzania MCP dla oficjalnego klienta DeepSeek Harness MCP: polecenie /mcp z diagnostyką stanu i wywołaniami testowymi potoku, karta Settings MCP z operacjami CRUD serwerów (zapisy wymagające zatwierdzenia, automatyczne kopie zapasowe) oraz konsola testowania narzędzi w oficjalnym potoku narzędzi (Apache-2.0, dsh-plugin).

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
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

this is a launcher for the official DeepSeek Harness. no modifications it just launches what DeepSeek develops.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Oficjalne: własne repozytoria i informacje o wydaniach Anthropic`               |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3**      |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐460 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Społecznościowy katalog publicznych modyfikacji Claude Code (hooków funkcji), skanowanych z GitHub wraz z informacjami, co każda modyfikacja może odczytywać, zapisywać, uruchamiać lub wysyłać przez sieć. Przeglądaj https://mods.aidojo.si/

<sub>🔧 Znaleziono użycie w kodzie: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `contributing.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **460**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐178 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code: wtyczki oparte na hookach, które dodają dynamiczne wiersze nad poleceniem, zabezpieczenia, panele i gry. Pasek kontekstu, miernik użycia, monitorowanie przeglądu Codex, podgląd Markdown, aktualnie odtwarzany utwór ze Spotify i nie tylko.

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
| Gwiazdki               | **178**    |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Deterministyczne narzędzie QA sterowane przez przeglądarkę do stron internetowych. Bez pisania testów, bez LLM.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | HTML                                                              |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **104**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐104 · TypeScript · 👁️ observed · 6 天</summary>

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
| Gwiazdki               | **104**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐79 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Skórki dla Claude Code: wiersze narzędzi z ikonami, kartami różnic, tabel i wykresów Mermaid, pasmo użycia oraz piętnaście motywów. /skin przełącza je na żywo.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **79**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Kolekcja modów claude code

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **77**     |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 4 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code autorstwa Darrell Wang — paski nad promptem, zero tokenów modelu. Tablica tajwańskich i amerykańskich akcji + kolejne funkcje w przygotowaniu.

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
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐58 · TypeScript · 👁️ observed · 7 天</summary>

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
| Gwiazdki               | **58**     |
| Ostatni push           | 2026-10-02 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐57 · Shell · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Eksperckie umiejętności, agenci, polecenia, reguły, hooki i style wyjściowe dla Claude Code — ciągłość sesji + nowoczesne narzędzia CLI do rzeczywistych przepływów pracy programistycznej

<sub>🔧 Znaleziono użycie w kodzie: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | Shell                                                             |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **57**     |
| Ostatni push           | 2026-10-07 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐44 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Kolekcja ponad 100 modów, których możesz używać z Claude Code.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **44**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐44 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Mody Claude Code: paski postępu planu na żywo nad promptem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **44**     |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animowane nagranie · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/claude-code-mods">karanb192/claude-code-mods</a></b> · ⭐40 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude i narzędzia do ich tworzenia: najpierw umiejętność konstruktora, potem modyfikacje

<sub>🔧 Znaleziono użycie w kodzie: `plugins/mod-builder/skills/mod-builder/references/migrate.md`, `plugins/mod-builder/skills/mod-builder/references/nouns.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **40**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐26 · TypeScript · 👁️ observed · 7 天</summary>

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
| Gwiazdki               | **26**     |
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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

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
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

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
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐19 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Dziesięć modów Claude Code, poradniki dla początkujących, prompty do tworzenia, bezpieczne demonstracje i szablon do samodzielnego budowania.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **19**     |
| Ostatni push           | 2026-10-02 |
| Pierwsze uwzględnienie | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Mody Claude Code: usage-band pokazuje limity 5h/7d, okno kontekstu i współczynnik trafień pamięci podręcznej nad promptem

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
| Pierwsze uwzględnienie | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Mody Claude Code ułatwiające czytanie i odpowiadanie na pytania Claude (qa-guide).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **11**     |
| Ostatni push           | 2026-10-07 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>animowane nagranie · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

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
| Gwiazdki               | **11**     |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Podsumowanie

Dwa mody Claude Code: most Codex do obsługi komputera oraz skoordynowane sesje Claude. Kod źródłowy, prompty budowania, konfiguracja i testy.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **11**     |
| Ostatni push           | 2026-10-05 |
| Pierwsze uwzględnienie | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Dziesięć modów open source dla Claude Code: panele na żywo, pasma, wiersze stanu i zabezpieczenia wywołań narzędzi. Miernik spalania, kody startowe, podsumowanie sesji, walka z bossem, zwierzak kodu i wiele więcej.

<sub>🔧 Znaleziono użycie w kodzie: `swarm/README.md`</sub>

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
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Interfejs wokół terminali Claude Code i Codex, który budują Twoi agenci, dzięki czemu jedynym modelem w Twojej głowie pozostaje Twój własny.

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
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

KOZMOS — bieżące, wizualne mody dla Claude Code (CLI + aplikacja desktopowa): pasy nad znakiem zachęty, paski boczne, przewijany wskaźnik stanu, towarzysze, zabezpieczenia i dźwięk.

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
| Pierwsze uwzględnienie | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Podsumowanie

Sześć modyfikacji Claude Code w jednej wtyczce (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) z przełącznikami dla każdej modyfikacji oraz raportem modyfikacji względem hooków.

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
| Pierwsze uwzględnienie | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Podsumowanie

Zestaw modów Claude Code autorstwa 개발동생. Pakiet taksówkowy: taksometr, nawigacja, fotoradar, wideorejestrator

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **7**      |
| Ostatni push           | 2026-10-04 |
| Pierwsze uwzględnienie | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Obejrzyj w serwisie youtube.com</a> · odtwarzanie otwiera się w witrynie źródłowej; GitHub nie może osadzić go bezpośrednio</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Markdown rysowany w polu promptu Claude Code podczas pisania. Ogrodzony kod staje się kartą z podświetlaniem składni, zanim jeszcze zamkniesz ogrodzenie.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **7**      |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Podsumowanie

Mody Claude Code: 像素螃蟹用量面板 usage-hud + klikalne linki HTML w terminalu i karty kodu z kopiowaniem jednym kliknięciem html-shelf

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **7**      |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Mody dla Claude Code: wtyczki function-hook dodające aktywne panele i zachowanie do interfejsu terminala

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6**      |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 24 天</summary>

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
| Gwiazdki               | **6**      |
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
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Mod Claude Code (wtyczka), który dodaje panel boczny z kartami Activity, Files, Agents, Context i MCP, wiersz statusu nad promptem, odświeżony czat, diagramy Mermaid w terminalu, tabele oraz panele kodu i diff. Kolory są zgodne zarówno z /color, jak i /theme (dark, light i inne).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6**      |
| Ostatni push           | 2026-10-06 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Panele, zabezpieczenia i mody poprawiające komfort pracy w Claude Code: kontekst, użycie, aktywność na żywo, powiadomienia, reguły bezpieczeństwa, trener promptów i centrum poleceń.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6**      |
| Ostatni push           | 2026-10-06 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/leopiney/wolfbud-claude-mod">leopiney/wolfbud-claude-mod</a></b> · ⭐5 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Głosowy współpracownik dla Claude Code. Porozmawiaj o rozwiązaniu z trójwymiarowym wilkiem napędzanym konwersacyjną AI ElevenLabs; gdy się zgodzisz, wyśle prompt do Claude i odezwie się, gdy Claude zakończy pracę.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **5**      |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/leopiney/wolfbud-claude-mod/main/assets/banner.png" width="100%" alt="leopiney/wolfbud-claude-mod screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 433</sub></summary>

- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Harness Claude Code, którego używam na co dzień, publikowany pod tą nazwą od…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Zmień dach w Claude Code za pomocą Claude Mods: bez modyfikowania pliku…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cztery mody Claude Code: Cache Keeper, Recording Mode, Goal Meter i Collision…
- [kakha13/claude](https://github.com/kakha13/claude) - Mody Claude Code, które poprawiają i tłumaczą Twoje prompty, zanim przeczyta je…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mody Claude Code autorstwa Learning Hacker: przedstawiają działanie agenta w…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel boczny dla Claude Code: podagenci uruchamiani przez sesję, zadania…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Baza wiedzy Obsidian o Claude Code mods, z odwołaniami do źródeł: jak działają…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Umiejętność ucząca agentów Claude Code tworzenia modów Claude.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel boczny Claude Desktop (karta Code): wyświetla wszystkie niedokończone i…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mody i umiejętności Claude Code od Nekyia Labs, tworzone i codziennie używane…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Kokpit dla Claude Code: paski planu na żywo, paski subagentów, limity użycia z…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mody (wtyczki function-hooks) dla Claude Code.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Pasek użycia nad polem wejściowym Claude Desktop (karta Code): limit 5h / 7d…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Społecznościowe mody, wtyczki i umiejętności Claude, instalowalne z jednego…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeria modów Baselane: sprawdzone i przypięte mody Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Kolejka decyzji CLI/TUI dla ludzi pracujących z agentami konwersacyjnymi.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Modyfikacja panelu IDE Claude Code: tablica agentów, drzewo plików i…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Pływająca karta statusu dla Claude Code — model, kontekst, limity szybkości…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Modyfikacje Claude Code: screen-guard maskuje nazwy i sekrety podczas…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Rozszerzenia Claude Code. Odblokuj pełną moc Claude.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Odczytuje pliki markdown nazwane przez Claude Code i renderuje je obok sesji;
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dwa mody Claude Code nad polem promptu: miernik okna kontekstu, limit…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mody Claude Code: typing-speed, aktywny prędkościomierz pisania ze statystykami…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Odkrywaj mody, wtyczki i rozszerzenia Claude Code z animowanymi demonstracjami…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code: diagramy mermaid rysowane bezpośrednio w transkrypcji.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Małe modyfikacje Claude Code (wtyczki function-hook): session-switcher i inne.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code: miniatury wklejonych obrazów nad promptem, w dowolnym terminalu.
- [joonhyukyim/redpen](https://github.com/joonhyukyim/redpen) - Redpen is a Claude Code mod for reviewing what Claude changed, line by line, in…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mody Claude Code: mod-scout (znajduje najczęściej używane mody), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dwa mody Claude Code do uruchamiania wielu sesji jednocześnie: karta kontekstu…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Claude Code mod: control autocompaction content from the TUI natively.
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Wydłuż działanie planu Pro Claude: mody Claude Code zapewniające dokładny HUD…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fajerwerki dla Claude Code: każde naciśnięcie klawisza, wywołanie narzędzia…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Najlepsze mody kodu Claude: starannie wybrane, zweryfikowane, przypięte.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Wtyczka Claude Code: automatyczne kierowanie do modeli Claude.
- [drkokorev/cockpit-for-claude](https://github.com/drkokorev/cockpit-for-claude) - Bieżący panel instrumentów dla Claude Code: kontekst, limity częstotliwości…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sześć modów dla Claude Code: animowana maskotka Clawd, paski limitu użycia i…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Marketplace modyfikacji dla Claude Code: debugger krokowy pętli agenta…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mody Claude Code: menu Tools Claude, tryb Zen, motywy terminala, sterowanie…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Najlepszy kompleksowy pakiet modyfikacji dla Claude Code: limity użycia i HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Odtwarzaj YouTube Shorts w swoim Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Zestaw narzędzi Claude Naren: skills, mody i serwery MCP dla Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code rysujący różnice Edit i Write w dwóch kolumnach obok siebie.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mody dla Claude Code: Clawd, mała pikselowa maskotka pokazująca, co robi Claude.
- [reporails/arcade](https://github.com/reporails/arcade) - Klasyczne gry desktopowe jako modyfikacje Claude Code, uruchamiane w panelu…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Wyselekcjonowana lista modów Claude Code, instalowanych jako marketplace…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Modyfikacje Claude Code, które pilnują agenta — hooki funkcji chroniące zakres…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Moja kolekcja modyfikacji Claude Code, po jednej modyfikacji w każdym katalogu.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Pięć bezpłatnych modyfikacji Claude Code: Simple Mode, Usage Tally, Context…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow dla Claude Code: spokojna lista kontrolna nad promptem, pokazująca…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: wykrywanie, sprawdzanie, przełączanie i aktualizowanie modów Claude Code.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Prosto z fabryki. Mod Claude Code: poproś o mem i pracuj dalej.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod dla Claude Code: pasek pamięci podręcznej promptu, kolejne kroki, szybkie…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code rysujący limity użycia i wydatki na pasku nad promptem.
- [griches/installguard](https://github.com/griches/installguard) - Mod Claude Code: sprawdza każdy nowy pakiet, zanim Claude go zainstaluje, i…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - An app store for Claude Code mods, inside Claude Code: /mods to browse, search…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Modyfikacje Claude Code autorstwa Hermana (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mody Claude Code: paski postępu planów, rejestr tego, co Claude pozostawił…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Mody Claude Code do codziennego UX: limity planu, kontekst i działania agenta.
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mody Claude Code od MacLeod Labs: streams rozplątuje przeplatającą się pracę…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notatki terenowe z pierwszego dnia o modach Claude Code na Windows: pasek…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Modyfikacje, które stworzyłem i osobiście używam w mojej konfiguracji Claude…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: bieżące mierniki kosztu, kontekstu i limitu planu nad…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Mod Claude Code, który wstrzymuje rozgałęzianie podagentów, prompty wymagające…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods dla claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code, który włącza lub wyłącza globalne umiejętności, agentów…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mody dla Claude Code: wtyczki zbudowane na hookach funkcji.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Napisy końcowe w stylu filmowym dla sesji programistycznej.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Zestaw modyfikacji claude code stworzonych przeze mnie.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Odtwarzacz YouTube oparty na cliamp wewnątrz Claude Code (mod Claude Code).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Mody Claude Code: panel agent-fleet i autopilot (marketplace local-mods).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Modyfikacje Claude Code autorstwa vynnlee.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Ucz się języka obcego podczas pracy z Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Opiekuje się długą sesją Claude Code, abyś nie musiał tego robić: obserwuje…
- [Akash001uts/claude-mods](https://github.com/Akash001uts/claude-mods) - Modyfikacje Claude Code: pasek okna kontekstu i automatyczne przekazywanie…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Podczas pisania przez agenta Java kodu naruszającego standard Java firmy…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Live cost, token and context usage sidebar for Claude Code: a mod that shows…
- [arviaja/token-watch](https://github.com/arviaja/token-watch) - Mod Claude Code: pokazuje użycie tokenów, limity planu i temperaturę pamięci…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Komunikaty radiowe Counter-Strike 1.6 dla Claude Code — „Fire in the hole.
- [burnrate-ai/burnrate](https://github.com/burnrate-ai/burnrate) - Zobacz i spowolnij tempo, w jakim Claude Code zużywa limity Claude.ai…
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Panel macOS notch dla Claude Code: limity użycia, otwarte sesje, postęp zadań…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude gotuje. Czatuj ze swoją ekipą. Znajomi online, tuż obok Twojej sesji…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Moduł Claude Code: łap pixel-artowe Modsters w grze bezczynnościowej, podczas…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Bitwa kosmiczna nad poleceniem Claude Code podczas jego pracy.
- [davidbalzan/status-band](https://github.com/davidbalzan/status-band) - Modyfikacje Claude Code autorstwa David Balzan: status-band, pasek statusu nad…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zobacz, które pliki każdy agent Claude Code ma w swoim kontekście i ile każdego…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Zachowaj zimną krew. Termometr na dni z Claude Code: każda godzina otrzymuje…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Skraca ogromne wyniki narzędzi, zanim zapełnią kontekst Claude Code.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Małe mody Claude Code do terminala i aplikacji desktopowej.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Umiejętność + mod Claude CLI, który dodaje hiszpańskie słowa do odpowiedzi…
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Mody Claude.
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - Modyfikacja skill-router: Jev wybiera i ładuje umiejętności potrzebne do…
- [gregdotca/claude-mods](https://github.com/gregdotca/claude-mods) - Mody Claude Code autorstwa Greg Chetcuti.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code mod do obowiązkowych, zweryfikowanych przepływów…
- [Jianyuuuuu/claude-code-feishu-mod](https://github.com/Jianyuuuuu/claude-code-feishu-mod) - Rozmawiaj z Claude Code z Feishu/Lark — moduł Claude Code korzystający z…
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Mod Claude Code (mod CC tint): koloruje każde okno według jego repozytorium…
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - A community directory of Claude Code mods, plugins, skills, agents, hooks and…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesji, postęp Spec Kit na żywo i zarządzanie oknem…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Okno kontekstu jako jeden wiersz nad promptem, narysowane tak, jak Claude Code…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Wtyczka (mod) do Claude Code, która sprawia, że terminalowy interfejs…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Zobacz, co Claude Code uruchamia w tle: subagenci, zadania Codex, shelle…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Wyczyść czat, zachowaj pracę. Wtyczka Claude Code + mod relay: Claude zapisuje…
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Wyselekcjonowane mody do Claude Code, oryginalne prezentacje twórców, publiczne…
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Osobiste mody Claude Code (wtyczki function-hook): przekazanie kontekstu…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Mod Claude, który wyświetla żądania pull GitHub z bieżącej sesji w panelu obok…
- [nevermemo/token-watch](https://github.com/nevermemo/token-watch) - Planuj użycie i okno kontekstu jako cienkie paski nad promptem Claude Code.
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: debugger wywołań narzędzi Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Umiejętności Claude Code: weryfikator faktów w dokumentacji, audytor kodu…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod Claude Code, który przed wysłaniem przekształca nieprecyzyjne prompty w…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Wtyczka Claude Code buddy: towarzysz ASCII nad promptem, który pamięta Twoje…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Wtyczka Claude Code do widoczności narzędzi per agent — ukrywaj i odrzucaj…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Modyfikacja Claude Code: routing modeli/wysiłku sterowany przez Jev…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Kolekcja modów Claude Code.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin i mod Claude Code: AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Kolekcja świetnych modów do Claude Code | 모음집 modów do Claude Code.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Wtyczki (modyfikacje) Claude Code: przełączanie między kilkoma kontami Claude…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Przetestowane modyfikacje Claude Code instalowane jednym poleceniem…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Moduły Claude Code: panele na żywo i hooki do codziennej pracy.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: modyfikacja Claude Code, która na żądanie odczytuje na głos…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mody Claude Code: małe wtyczki do aktualizowanych paneli, routingu modeli…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod i wtyczka Claude Code: monitor użycia, licznik tokenów i wiersz stanu.
- [Verinoda-Labs/verinoda-symbiosis](https://github.com/Verinoda-Labs/verinoda-symbiosis) - Verinoda + Claude Code razem: Verinoda z verinoda-live, modułem Claude Code…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Trzy darmowe moduły Claude Code: ukrywanie wartości .env w wynikach narzędzi…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modyfikacje Claude Code. touch-map: zobacz jako drzewo i mapę aktywności, które…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Modyfikacja Claude Code, która podsumowuje nieprzeczytane wiadomości agentów…
- [0xBADC0FFEE/claude-code-mods](https://github.com/0xBADC0FFEE/claude-code-mods) - Moduły dla Claude Code zbudowane na hookach funkcji: marketplace wtyczek.
- [abdurrahimagca/claude-statusbar](https://github.com/abdurrahimagca/claude-statusbar) - Claude Code mod: a compact status row with context, rate limit, cache…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Animowany kot z alfabetu Braille.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Stylizowane odpowiedzi, diagramy na pełną szerokość oraz kontekst i limity…
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Modyfikacja Claude Code: kieruje niedrogą pracę do GLM/Kimi za pośrednictwem…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Pikselowy kot nad promptem Claude Code, który wykonuje testowe połączenie z…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code, który wybiera dobry moment na kompakcję, aby utrzymać małe…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modyfikacje Claude dla Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Rynek wtyczek Claude Code autorstwa anderson-spider.
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Mody do Claude Code do obserwowania rynku z terminala: panel A股/港股/美股 z…
- [AnnihilationWizard/chrome-close](https://github.com/AnnihilationWizard/chrome-close) - A Claude Code mod that allows one headless Chrome at a time and flags the…
- [AnnihilationWizard/quiet-diffs](https://github.com/AnnihilationWizard/quiet-diffs) - A Claude Code mod that shows file edits as one-line summaries instead of full…
- [aott33/model-router](https://github.com/aott33/model-router) - Modyfikacja Claude Code, która wybiera model dla każdego subagenta przed jego…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Modyfikacja Claude Code: Twoje okno kontekstu w jednej spokojnej linii, szarej…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Statek LGTM Lines przepływa obok po każdej zmianie kodu — moduł Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Twoje limity użycia Claude jako animowana karta zdrowia wieśniaka — moduł…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mody Claude Code dla zespołu S2 (marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Krótkie treningi, gdy Claude pracuje: dzienny cel, serie, odznaki i opcjonalne…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Tablica zużycia dla Claude Code: wydatki według modelu.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing dla Claude Code: Apple Music i Spotify nad poleceniem, z…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Pięć modów Claude Code do jednoczesnego uruchamiania wielu sesji: tablica…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Moduły Claude Code dla sesji orkiestratora i workerów.
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Moduły Claude Code: pasek użycia, lista rozmówców, /cube, /handoff, czyszczenie…
- [bilal-psd/skills](https://github.com/bilal-psd/skills) - Moje mody i umiejętności do Claude Code jako marketplace wtyczek.
- [Blind3y3Design/agents-panel](https://github.com/Blind3y3Design/agents-panel) - Modyfikacja Claude Code: panel na żywo ze wszystkimi subagentami, zawierający…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mody dla Claude Code: zegar cache, Blast Radius, sugestie, lista zadań, grill.
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mody do Claude Code: Suggestion Spotlight pokazuje, czego dotyczy sugerowany…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Po prostu sowa dla Twojego Claude Code.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Mody Claude Code dla środowiska ai-architect.tools: jeden zakres…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Jednowierszowy pasek Claude Code.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Oryginalny silnik Doom z Freedoom, grywalny wewnątrz Claude Code.
- [cmorss/claude-mods](https://github.com/cmorss/claude-mods) - Claude Code mods for git worktrees: /terminal and /worktree-files open a…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code mods for real Engineers.
- [CookPiu/token-almanac](https://github.com/CookPiu/token-almanac) - Mod do Claude Code: mierniki limitu użycia, odliczanie do resetu, statystyki…
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Moduły Claude Code przeznaczone wyłącznie dla zespołu d3nim.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi żyjące wewnątrz Claude Code: wykluwa się, zjada kod pisany przez…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Zakładki i znaczniki w stylu vim wewnątrz rozmów terminala Claude Code…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Zmień każdą sesję Claude Code w małą przygodę: muzyka generatywna podążająca za…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Modyfikacje Claude Code zapisane jako haki funkcji oraz oferujący je…
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - Mody Claude Code autorstwa divramod: panele na żywo i ulepszenia interfejsu…
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - Moduły Claude Code, których używam na każdej maszynie: savvy-progress…
- [dtakamiya/claude-code-mods](https://github.com/dtakamiya/claude-code-mods) - Marketplace modów do Claude Code.
- [EgonLeitner/claude-code-mods](https://github.com/EgonLeitner/claude-code-mods) - Marketplace egonleitner: modyfikacje Claude Code autorstwa Egona Leitnera.
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Pamięć podręczna promptów, kontekst i limity planu dla Claude Code — rzut oka w…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hey, Muted it! Ditch the diff cut the riff, no more edits less of credits.
- [elkinaguas/claude-mods](https://github.com/elkinaguas/claude-mods)
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude Code mod: subscription usage (5h / 7d) as a band above the prompt in the…
- [EvoMap/evolver-claude-code-mods](https://github.com/EvoMap/evolver-claude-code-mods) - Evolver dla Claude Code oparty na hookach funkcji (Mods): przywoływanie…
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Moduły Claude Code z projektowanymi animacjami: monitor na żywo i responsywny…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - My Claude Code mods.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - A Claude Code mod for capturing thoughts mid-work, triaging them across…
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - Moduł jev: $.jev dla Claude Code, typowane osądy z TypeSafe Jev.
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mody do Claude Code: wtyczki hooków, takie jak usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code mods (function-hook plugins), installed through one marketplace.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Pasek boczny w stylu Evangelion dla Claude Code: kontekst, quota, aktywność…
- [griches/buildpane](https://github.com/griches/buildpane) - Mod Claude Code: diagnostyka build, test i lint w panelu na żywo dla każdego…
- [griches/simpane](https://github.com/griches/simpane) - Mod Claude Code: iOS Simulator obok twojej sesji, z narzędziami pozwalającymi…
- [hamTotk/better-rewind](https://github.com/hamTotk/better-rewind) - Claude Code mod: rewind or summarize from any prompt or AskUserQuestion answer.
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Wyniki testów w panelu Claude Code: niepowodzenia, ich szczegóły i historia…
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Claude Code mod: compacts at the right moment.
- [hfknight/claude-mod-said](https://github.com/hfknight/claude-mod-said) - Modyfikacja Claude Code: /said otwiera panel boczny wysłanych przez ciebie…
- [hmcdaniel03/claude-mods](https://github.com/hmcdaniel03/claude-mods) - Mody do Claude Code autorstwa Huntera: marketplace wtyczek (hunters-mods).
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Modyfikacja Claude Code: jak długo trwała każda odpowiedź, jak długo myślał…
- [IanYHChu/claude-mods-games](https://github.com/IanYHChu/claude-mods-games) - Gry zbudowane na modułach Claude, rozgrywane nad promptem Claude Code.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Modyfikacja Claude Code: przeczekuje 5-godzinny limit użycia i wysyła za Ciebie…
- [icedevil2001/session-sidebar](https://github.com/icedevil2001/session-sidebar) - Modyfikacja Claude Code: odnośniki, rzeczy, które warto wiedzieć, i zadania do…
- [iddhi-sulakshana/claude-mods](https://github.com/iddhi-sulakshana/claude-mods) - Moduły dla Claude Code: przyciski kolejnych kroków, komunikacja między sesjami…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Moduł Claude Code: boczny panel drzewa plików, który pulsuje przy plikach…
- [jagp/xray-mod](https://github.com/jagp/xray-mod) - ⋐∿⋑ Stare deeply into your contexts: a live Claude Code mod showing what fills…
- [JanSuthacheeva/claude-code-mods](https://github.com/JanSuthacheeva/claude-code-mods) - Mody do Claude Code, których używam na co dzień.
- [jeppenpeppen/claude-mods](https://github.com/jeppenpeppen/claude-mods) - Jespers egna moddar för Claude Code.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel użycia kontekstu na pasku bocznym: suma, kategorie, przyrost w każdej…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista plików na pasku bocznym: które pliki utworzono, zmodyfikowano lub…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Futrzasty w stylu 8-bitowym.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel boczny „O co pytałem.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Oś czasu na pasku bocznym: na co przeznaczono czas w tej turze.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Panel wymiany tokenów na pasku bocznym: ile tokenów rozmowa główna wysłała do…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Szczera krótka rozmowa claude code: po każdej odpowiedzi Claude cicho mówi, co…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Lista kontrolna planu dla Claude Code z weryfikacją dowodów: zatwierdzone plany…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Małe mody dla Claude Code, takie jak nowe polecenia ukośnikowe i panele boczne.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Gry wieloosobowe do grania wewnątrz Claude Code, gdy pracuje.
- [juampymdd/claude-code-model-picker](https://github.com/juampymdd/claude-code-model-picker) - Claude Code mod: pick the model and version for the next requests from a band…
- [juniormartinxo/jm-claude-mods](https://github.com/juniormartinxo/jm-claude-mods)
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Modyfikacja Claude Code: utrzymuje ciepłą pamięć podręczną promptu podczas…
- [K-Mertin/claude-monster-pet](https://github.com/K-Mertin/claude-monster-pet) - A Claude Code mod: raise a pixel-art digital monster that grows from your…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd mieszka w pasku nad twoim promptem Claude Code: odgrywa sesję, pokazuje…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - Modyfikacja Claude Code pokazująca limit wykorzystania, tokeny sesji i koszt…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod odczytujący na głos odpowiedzi i powiadomienia z Claude Code za pomocą…
- [katipally/modz](https://github.com/katipally/modz) - Modyfikacje Claude Code: instalacja za pomocą /plugin install &lt;mod&gt;…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude do odczytywania i dołączania do rozmów między sesjami Claude Code…
- [kikostefanov-lab/claude-code-mods](https://github.com/kikostefanov-lab/claude-code-mods) - Claude Code mods: a Whiteboard pane where Claude draws Mermaid/UML diagrams…
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - Ściśnij nieaktywne sesje claude code za pomocą haiku — jednoliniowy pasek…
- [kk5190/claude-code-mods](https://github.com/kk5190/claude-code-mods) - Moduły dla Claude Code: miernik kontekstu i panele serwera deweloperskiego.
- [krishna-goutham-tls/folio](https://github.com/krishna-goutham-tls/folio) - Modyfikacja Claude Code: odczytuj pliki projektu w panelu obok czatu.
- [KytioisaCat/playpen](https://github.com/KytioisaCat/playpen) - Who needs attention? Your other Claude Code sessions as cards above the prompt…
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Tworzony przez społeczność przewodnik po modyfikacjach Claude Code: przypadki…
- [lucaslenglet/session-namer](https://github.com/lucaslenglet/session-namer) - Moduł Claude Code: sugerowane przez AI nazwy sesji zgodne z Twoją konwencją…
- [lucasram20/claude-mods](https://github.com/lucasram20/claude-mods)
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - A Claude Code mod that shows what Claude is doing in the iTerm2 tab subtitle…
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Claude Code mod: nudges the main session to delegate to subagents and shows…
- [m-tababi/session-handoff](https://github.com/m-tababi/session-handoff) - Claude Code mod: session handoffs on demand — write, resume, and restart into a…
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Modyfikacja Claude Code z przełączanymi profilami uprawnień: bezpieczna baza…
- [MiCat-S/context-hud](https://github.com/MiCat-S/context-hud) - Claude Code mod: one-line usage HUD above the prompt.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel boczny dla Claude Code: pliki, które Claude napisał, podziały terminala…
- [mlt-5/manager](https://github.com/mlt-5/manager) - Moduł Claude Code: miernik kontekstu oraz kompaktowe przyciski / commit &amp; push…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Spokojny panel boczny dla Claude Code: co robi ta sesja, jej plan, agenci i…
- [mmedum/spor](https://github.com/mmedum/spor) - Puts back what Claude Code folds away: the files Claude read, the commands it…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Trzymaj kod zgodny ze specyfikacją: moduł Claude Code i rozszerzenie GitHub…
- [moonteek/claude-mods](https://github.com/moonteek/claude-mods) - Claude Mody Code: pasek pamięci i aktualizowana na żywo lista kontrolna zadań…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Mody Code: automatyczne przekazywanie i pasek postępu.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code, który ponownie włącza narzędzia todo dla modeli, które je…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: jeden wiersz na zadanie nad promptem z bieżącym zadaniem…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Graj w Connect Four przeciwko AI wewnątrz Claude Code (/connect-four).
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Kanarek w pikselowej oprawie dla Claude Code: umiera, gdy Claude przestaje…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: gdy inny agent programistyczny wykonuje commit w Twoim…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code dla repozytoriów współdzielonych przez kilku agentów AI…
- [natsume-777/claude-mods](https://github.com/natsume-777/claude-mods) - Marketplace modułów Claude Code (wtyczek opartych na hookach funkcji)…
- [nevermemo/token-watch-vscode](https://github.com/nevermemo/token-watch-vscode) - Użycie planu Claude Code i okno kontekstu na pasku statusu VS Code.
- [New-Retr0/claude-dock](https://github.com/New-Retr0/claude-dock) - Modyfikacje Claude Code: session-dock i agent-model-badge.
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Panel cyberneonowego radia internetowego dla Claude Code — pokrętło synthwave…
- [niksavis/handily](https://github.com/niksavis/handily) - Mody Claude Code pokazujące elementy pracy, zadania i sesje dla dowolnego…
- [NMenzel/claude-integrity-mod](https://github.com/NMenzel/claude-integrity-mod) - Claude Integrity: rozróżnia implementację od weryfikacji w Claude Code.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Ponownie uzbraja długie obserwacje Monitor w Claude Code po ich wygaśnięciu…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Zabezpieczenie SQL w Claude Code: pyta przed wykonaniem przez Claude poleceń…
- [OctopiAI/claude-code-statusline](https://github.com/OctopiAI/claude-code-statusline) - A lightweight Claude Code Mod.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Jeden mod dla Claude Code, Windows i CJK przede wszystkim: podgląd wklejonych…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime dla Claude Code: dźwięk, gdy Claude kończy pracę, potrzebuje Twoich…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Modyfikacje Claude Code: miniatury obrazów i wiersz stanu.
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Najlepsze mody Claude Code, posortowane według tego, co dla Ciebie robią.
- [Oualid0/claude-mods](https://github.com/Oualid0/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Modyfikacja Claude Code: zobacz każdy obraz i plik, na który patrzył Twój agent…
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dwa mody Claude dla Claude Code: garde-du-corps.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Panel Lazy Panda dla Claude Code: przeglądaj dokumentację bez kiwnięcia łapą.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel boczny ze statystykami sesji na żywo dla karty Code aplikacji desktopowej…
- [Pigula1984/workbench](https://github.com/Pigula1984/workbench) - Moduły Claude Code: pasek stanu nad promptem.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Various mods and skills for my Claude Desktop setup.
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Moduły Claude Code dla interfejsu pompeitech, utrzymane w stylistyce systemu…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Moduły dla Claude Code: safety-guard blokuje destrukcyjne polecenia i dostęp do…
- [ptpmediabr/ideas-shelf](https://github.com/ptpmediabr/ideas-shelf) - Półka pomysłów dla projektu: zapisuj pomysły na tablicy i oznaczaj je jako…
- [ptpmediabr/mods-manager](https://github.com/ptpmediabr/mods-manager) - Panel do wyświetlania, włączania, wyłączania, instalowania i grupowania modów…
- [ptpmediabr/side-chat](https://github.com/ptpmediabr/side-chat) - Panel bocznego czatu wewnątrz sesji, który odpowiada na pytania lub wykonuje…
- [ptpmediabr/usage-weather](https://github.com/ptpmediabr/usage-weather) - Jedna spokojna linia nad poleceniem: kontekst, wykorzystanie w okresie 5 godzin…
- [qarge/claude-mods](https://github.com/qarge/claude-mods)
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Modyfikacja Claude Code: aktualny ticker giełdowy, panel /quote, alerty cenowe…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Moduły Claude Code opublikowane jako jeden marketplace wtyczek.
- [raoofaltaher/claude-code-mods](https://github.com/raoofaltaher/claude-code-mods) - Moduły Claude Code: account-bars.
- [redjackfred/claude-code-mods](https://github.com/redjackfred/claude-code-mods) - Mody Claude Code: pomodoro w pikselowej oprawie, paski postępu podagentów…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Modyfikacja Claude Code: host SSH, pamięć RAM oraz limity użycia 5 h/7 d w…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod dla Claude Code: pompki do zrobienia podczas pracy Claude. Bez tokenów.
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - po prostu lista modułów, których używam.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Sklep z modyfikacjami dla Claude Code: pobiera modyfikacje z GitHub, pokazuje…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: zamienia plan zatwierdzony w trybie planu w aktywną listę…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Starannie wybrana lista modyfikacji Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Tryb bez kosztów: agenty pomocnicze działają na Haiku, a duże pliki i logi są…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ścieżka dźwiękowa lofi, która podąża za sesją: spokój, skupienie, przepływ, a…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Ucz się podczas kodowania przez Claude: po turze, która zmieniła kod, nad…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Nagranie każdej zmiany wprowadzanej przez Claude: odtwórz każdą zmianę…
- [samaphp/prompt-stash](https://github.com/samaphp/prompt-stash) - Schowek na myśli, które przychodzą Ci do głowy podczas pracy Claude Code.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Każdy link wspomniany w Twojej sesji, w jednym wierszu nad promptem.
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Moduły Claude Code: token-bar, okno kontekstu i limity użycia nad promptem.
- [Savo2610/claude-mods](https://github.com/Savo2610/claude-mods) - Moje moduły Claude-Code: telegram-draht (Telegram jako łącze z telefonem) i…
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Minimalne demo funkcji-hooków Claude Code: panel tokenów/kosztów w czasie…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board i inne modyfikacje Claude Code autorstwa André Servaes.
- [ShadowDog007/claude-mods](https://github.com/ShadowDog007/claude-mods)
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - Mody Claude Code (wtyczki function-hook) autorstwa ShellTime.
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Mody Claude Code autorstwa Showrin, zapewniające bardziej produktywną codzienną…
- [shumatsumonobu/claude-mods-bench](https://github.com/shumatsumonobu/claude-mods-bench) - Cztery modyfikacje Claude Code instalowane za pomocą /plugin: zatwierdzaj…
- [simplybychris/claude-code-mods](https://github.com/simplybychris/claude-code-mods) - Mody do Claude Code: tryb nagrywania, pasek pamięci podręcznej, Snake i panel…
- [SocialChamp/socialchamp-claude-mods](https://github.com/SocialChamp/socialchamp-claude-mods) - Modyfikacje Social Champ dla Claude Code: panel kalendarza oparty na konektorze…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Przytulny mod HUD w stylu RPG dla Claude Code.
- [sstani-bgv/claude-blast-radius](https://github.com/sstani-bgv/claude-blast-radius) - Modyfikacja Claude Code: pyta w Claude przed wysłaniem wiadomości Telegram.
- [sstani-bgv/claude-crew](https://github.com/sstani-bgv/claude-crew) - Modyfikacja Claude Code: panel boczny z animowanym krabem pikselowym dla…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Osobisty marketplace modyfikacji Claude Code…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Wiadomości commitów jednym kliknięciem dla Claude Code z tańczącą Malenią w…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Modyfikacja Claude Code: wyświetla użycie planu Claude.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Modyfikacja Claude Code: panel na żywo dla każdego podagenta.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Modyfikacja Claude Code, która wyświetla bieżącą sesję w panelu: każdy prompt…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace pluginów Claude Code z modami: pluginy function-hooks, które rysują…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Wykorzystaj Claude Code nawet dwa razy bardziej.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Mody Claude Code autorstwa Toptaab.
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Repozytorium do zarządzania modami Claude.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Modyfikacja Claude Code: pasmo i panel śledzące subagentów wraz z używanymi…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Modyfikacja Claude Code: animowany pasek postępu i podsumowanie ukończenia dla…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Powiedz „I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Zadaj Claude pytanie poboczne w panelu obok swojej pracy.
- [VdustR/vp-cc-mods](https://github.com/VdustR/vp-cc-mods) - Wszystkie mody Claude Code autorstwa VdustR: marketplace wtyczek z modami i…
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Roblox Studio safety layer for Claude Code: RemoteEvent audit, undo, Team…
- [VizzleTF/claude-skills](https://github.com/VizzleTF/claude-skills) - Marketplace wtyczek Claude Code: tidemark.
- [WorldOccupier/claude-mods](https://github.com/WorldOccupier/claude-mods)
- [wszaq/claude-mods](https://github.com/wszaq/claude-mods) - Małe wtyczki Claude Code zapewniające bezpieczniejsze i bardziej przejrzyste…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mody dla Claude Code. agent-crew: obserwuj pracę swoich podagentów jako żywą…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Claude Code mods: 繁中下一步膠囊、區塊複製、貼圖縮圖.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [zhuzhu0710/claude-mods](https://github.com/zhuzhu0710/claude-mods)
- [ziedgithub/claude-code-mods](https://github.com/ziedgithub/claude-code-mods)
- [Zinzan48/claude-mods](https://github.com/Zinzan48/claude-mods) - Modyfikacje Claude Code: context-budget.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Starannie wybrana kolekcja najlepszych zasobów dla najbardziej niesamowitych…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Wtyczka Claude Code pokazująca, co się dzieje — wykorzystanie kontekstu…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Piękna, wysoce konfigurowalna linia statusu dla Claude Code CLI z obsługą…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Wszystkie części promptu systemowego Claude Code, 27 wbudowanych opisów…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Ponad 45 wskazówek, jak najlepiej wykorzystać Claude Code — od podstaw po…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / umiejętność Codex — generowanie karuzel Xiaohongshu oraz par…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Przeglądaj różnice wygenerowane przez agenta programistycznego w panelu…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Kompleksowa wtyczka paska stanu dla Claude Code z informacjami o wykorzystaniu…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code i lokalne śledzenie tokenów Codex — pasek statusu.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Twórz mody do Claude Code: przechwytuj dowolne żądanie, modyfikuj dowolną…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Kompleksowy pulpit paska stanu dla Claude Code — informacje o sesji, paski…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: śledź ślad węglowy swoich sesji Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Estetyczny wiersz statusu dla Claude Code autorstwa awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Publiczne umiejętności i modyfikacje Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mody, podagenci, hooki, polecenia ukośnikowe i przewodniki dla Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legalne bezpłatne LLM APIs i agenci kodowania — automatyczna aktualizacja…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Pasek stanu terminala dla sesji Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Wyniki na żywo, terminarze i tabele piłki nożnej dla rozgrywek, które…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Umiejętność agenta, która zmienia Twojego agenta programistycznego w eksperta…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Osobista konfiguracja Claude Code, wersjonowana w ~/.claude — agenci…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Pory modlitw, data hidżry, adhkar, codzienny ajat, post sunnah, Ramadan…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Pasek statusu świadomy sesji dla Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — wtyczka DeepSeek Harness do tematów badawczych…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Przenośny zestaw narzędzi Claude Code dla .NET DDD/Clean Architecture: agenci…
- [saadnvd1/agent-os](https://github.com/saadnvd1/agent-os) - Mobile-first web UI for managing AI coding sessions.
- [essedev/relay](https://github.com/essedev/relay) - Native macOS terminal for running many coding agents in parallel.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Zestaw wtyczek dla Claude Code, pi i DeepSeek Harness: HUD paska stanu, pasek…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Przenośna globalna konfiguracja Claude Code: niestandardowe umiejętności, hooki…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Wtyczki Claude Code, których używam codziennie: skills i mody uporządkowane…
- [vtmocanu/cc-statusline](https://github.com/vtmocanu/cc-statusline) - Dwuwierszowa linia statusu ANSI dla Claude Code: kontekst git + k8s, paski…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram inside Claude Code: read chats and channels in a pane, get AI…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Most DSH &lt;-&gt; Feishu (Lark), opracowany samodzielnie (nie fork): karta…
- [Dakaric/claude-code-statusline](https://github.com/Dakaric/claude-code-statusline) - Gotowy do użycia wiersz stanu dla Claude Code: pasek okna kontekstu, TTL…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace wtyczek i umiejętności Claude Code ułatwiający modyfikowanie gry…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Zarządzanie tokenami dla Claude Code: najlepszy model kieruje pracą, a…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Przeglądarka z podziałem na panele dla Claude Code w Windows Terminal i tmux…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Nieoficjalne mody karty Code w Claude Desktop — usage-pet: pas wykorzystania z…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repozytorium modów Awesome Media dla Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Ogranicz wydatki na tokeny Claude Code i Codex: kieruj wyszukiwania i…
- [sergiomorapardo/claude-statusline](https://github.com/sergiomorapardo/claude-statusline) - Linia stanu w stylu Powerlevel10k dla Claude Code: paski wykorzystania, stan…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Alerty o limitach użycia dla Claude Code: powiadomienia macOS, ostrzeżenia w…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Konfigurowalna linia statusu Claude Code dla Linux, WSL, Windows i macOS, z…
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Statusline Claude Code z paskiem kontekstu, wykresem tokenów i śledzeniem…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Wyświetlaj kluczowe informacje o stanie Claude Code, w tym model, kontekst…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - przyjazna, konfigurowalna statusline dla Claude Code — paski truecolor, około…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline with usefull information for claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Szablon startowy do organizowania wielofirmowego obszaru roboczego Claude Code…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Natywne zespoły agentów. Pod kontrolą.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Custom statusline for Claude Code — context bar with usage percentage, context…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Rynek wtyczek Claude Code z baloo: umiejętności, agent weryfikujący zmiany…
- [chrisns/claude-image-cli-mod](https://github.com/chrisns/claude-image-cli-mod) - See the images that commands print (imgcat, iTerm2 inline images) in your…
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Wiersz stanu Claude Code: użycie kontekstu, paski limitów 5h/7d, czasy…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Profesjonalny pasek stanu Claude Code: czas trwania sesji, koszt w wielu…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Uwzględniający subskrypcję wiersz stanu dla Claude Code.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - Wtyczki Claude Code autorstwa divramod, jeden marketplace: umiejętności agentów…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Dwuwierszowy pasek stanu dla Claude Code: kontekst, limity szybkości z…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Wtyczka Claude Code, która pięknie renderuje diagramy Mermaid w transkrypcie…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, skills, and agents for Claude Code — starting with a status line showing…
- [GeorgeDong32/pi-claude-code-tui](https://github.com/GeorgeDong32/pi-claude-code-tui) - TUI w stylu Claude Code dla pi: wiersze narzędzi CC, wiersz statusu, wiersze…
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Wtyczka Claude Code: zawsze wyświetla pozostały limit użycia Claude w ciągu 5…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Rzeczywiste wydatki DeepSeek API dla Claude Code: ponownie wycenia transkrypcje…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Wiersz stanu Claude Code z wierszami panelu agentów.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronizuj zadania do zrobienia Claude z Fizzy.do, aby zapewnić zespołowi…
- [izzatum/claude-code-cockpit](https://github.com/izzatum/claude-code-cockpit) - Wtyczka wiersza statusu Claude Code (cockpit): procent kontekstu, koszt sesji i…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - A live usage dashboard for Claude Code — context breakdown, cache hits…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Wyświetl szczegółowy, oznaczony kolorami pasek stanu dla Claude Code…
- [KitchenSink4AI/claude-code-statusline](https://github.com/KitchenSink4AI/claude-code-statusline) - Wskaźnik kontekstu dla Claude Code: rzeczywiste tempo zużycia, pozostałe tury…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu ustawień, wiersz stanu i konfiguracja Claude Code.
- [lakofsth/claude-code-experience-kit](https://github.com/lakofsth/claude-code-experience-kit) - Dostosowania na poziomie harnessu dla Claude Code: zapewnij agentowi bieżący…
- [Larg0Winch/claude-label](https://github.com/Larg0Winch/claude-label) - Edytowalna etykieta dla każdego okna na pasku stanu Claude Code.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Talk to Claude Code by voice on Windows: a Mod + helper using codex app-server…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook wiersza stanu Claude Code — śledzi użycie tokenów i kontekst między…
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Niestandardowy wiersz stanu Claude Code z oknem kontekstu, śledzeniem użycia…
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - Szybka linia stanu Rust dla Claude Code.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalator środowiska Claude Code: skills, statusline, hooks, permissions oraz…
- [ngz-fernando/claude-code-limites](https://github.com/ngz-fernando/claude-code-limites) - limites: modyfikacja Claude Code, która pokazuje zużyty kontekst, okna planu i…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Wtyczki i mody Claude Code pomagające zrozumieć, co robi Claude: czytelne…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitoruj stan Claude Code z menu macOS za pomocą wskaźników w czasie…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Kolorowy wielowierszowy pasek stanu dla Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Wiersz stanu Claude Code dla Windows (PowerShell): paski użycia, odliczanie do…
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Wtyczki Claude Code. Usage Bars pokazuje limity szybkości dla sesji i tygodnia…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings and Glossary dla Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Niestandardowy wiersz statusu Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Konfiguracja i mody Claude Code, ze współdzielonym zestawem komponentów…
- [Sect0R/claude-code-statusline](https://github.com/Sect0R/claude-code-statusline) - Claude Code StatusLine: monitor tokenów i kosztów.
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Mały pulpit dla Claude Code: procent wykorzystania kontekstu, odliczanie…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Przenośna konfiguracja Claude Code: CLAUDE.md, ustawienia, linia stanu…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Śledź wykorzystanie kontekstu Claude Code, koszty sesji i resety limitów…
- [vus955-gif/claude-code-token-heatmap](https://github.com/vus955-gif/claude-code-token-heatmap) - A /tokens pane for Claude Code: tokens used per day as a heatmap, each API…
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Wtyczka Cordis / DeepSeek Harness — agent prosi człowieka o sekret w wbudowanej…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Trzywierszowy wiersz stanu Claude Code: głębokość kontekstu, limity szybkości…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detektor degradacji kontekstu 2026 — proaktywny monitor pamięci AI i limitu…
- [zerofaultlabs/claude-statusline](https://github.com/zerofaultlabs/claude-statusline) - Linia stanu Claude Code: wykorzystanie kontekstu, limity zapytań, koszt i…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooki, subagenty i linie stanu Claude Code: kolekcje i narzędzia open source…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Wiersz stanu Claude Code — wskaźniki użycia Claude/Codex, które pozostają…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - Wiersz stanu obsługiwany przez Deno dla Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mody dla Claude Code: panele, pasma i pomocnicy zbudowane na hookach funkcji.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Przekazuj zadania między sesjami Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Jest to serwer MCP do sterowania MODS, modularnym wieloplatformowym narzędziem…
- [pedrotspinola/lps-statusline](https://github.com/pedrotspinola/lps-statusline) - Niestandardowy wiersz stanu Claude Code: model + poziom wysiłku, natywny limit…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Umiejętność Codex i Claude Code do tłumaczenia modów CK3 za pomocą lokalnego LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mody open source i inne rozszerzenia dla Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: znajdź czynności, o które ponownie prosisz Claude Code, i…
- [Niedvin/ClauDiscombobulating](https://github.com/Niedvin/ClauDiscombobulating) - Modyfikacja prompt-bar dla Claude Code: limity użycia, licznik pamięci…

</details>

<a id="dsh-cordis"></a>

## Ekosystemy wtyczek DSH i Cordis

DeepSeek Harness i Cordis docierają do tego samego miejsca z innego kierunku: dla nich wtyczka jest mechanizmem modów, więc wtyczka w tamtym ekosystemie jest odpowiednikiem moda tutaj.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74252 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **74252**  |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100357 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **100357** |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81556 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **81556**  |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐64291 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **64291**  |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35752 · Go · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **35752**  |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30351 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Nowoczesne rozwiązanie desktopowe stworzone dla ekosystemu wtyczek DeepSeek Harness (DSH). Wszystko jest „wtyczką”, a sam pulpit również jest „wtyczką”.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **30351**  |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25465 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Podsumowanie

Distilly — Wyodrębniaj sposób ich myślenia do postaci wielokrotnego użytku umiejętności dla dowolnego agenta lub bota. Dawniej Colleague Skill（原同事 Skill）.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **25465**  |
| Ostatni push           | 2026-09-22 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9110 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Meta-framework kompozycyjności czasoprzestrzennej

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **9110**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8593 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Ekosystem agregacji wtyczek webowych DeepSeek Harness (DSH) · Wszystko jest wtyczką, dystrybuowaną przez Warsztat Kreatywny ｜｜ Ekosystem agregacji wtyczek webowych DeepSeek Harness (DSH) · Wszystko jest wtyczką, dystrybuowaną przez Warsztat Kreatywny

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **8593**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐6642 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6642**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4262 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DSH's officially top-recommended TUI plugin — high performance, low overhead, cute pixel whale, smooth mouse interaction. One-command install via npm. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **4262**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3158 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Desktopowa wersja DeepSeek Harness Tauri | Instalator o rozmiarze zaledwie 8 MB, bez konfiguracji środowiska, wstępnie ustawione wtyczki, Windows / macOS / Linux.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3158**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1542 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

跨设备的开源Agent工作台

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1542**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1165 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Pamięć dla Claude Code, Codex, Cursor i 35 innych agentów programistycznych, tworzona na podstawie historii sesji znajdującej się już na dysku. Lokalne wyszukiwanie, MCP i hooki, bez LLM, jeden plik binarny Go.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Go                                                                               |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1165**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐701 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Klient desktopowy DeepSeek Harness (dsh) Windows — zawiera Node.js + dsh CLI, uruchamianie jednym kliknięciem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **701**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
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
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/text2future/flowix">text2future/flowix</a></b> · ⭐452 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Notatki dla ciebie, pamięć dla twoich agentów. / Wbudowany agent Deepseek harness / Do pracy biurowej, pisania i programowania

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **452**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent-memory` · `claude-code` · `codex-cli` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `hermes-agent`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/9fc65a8848fe78ee.png" width="100%" alt="text2future/flowix screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/ea3f84c8693d4236.gif" width="100%" alt="text2future/flowix animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/d-dev0101/open-sea-skin">d-dev0101/open-sea-skin</a></b> · ⭐388 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

🌊 Oceaniczna skórka i dynamiczny motyw DeepSeek Harness | Motyw oceanu w czasie rzeczywistym z regulowanymi falami, zachodem słońca i przezroczystością szkła. Wtyczka DSH + rozszerzenie Chrome/Edge; zachowuje twoją stronę główną nowej karty.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **388**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `animated-background` · `chrome-extension` · `customization` · `deepseek` · `deepseek-harness` · `deepseek-theme` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/3d9689f0d936d1b0.png" width="100%" alt="d-dev0101/open-sea-skin screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/ccd6ac3920478ffa.gif" width="100%" alt="d-dev0101/open-sea-skin animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Mars-Sea/dsh-commandcode-provider">Mars-Sea/dsh-commandcode-provider</a></b> · ⭐377 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Command Code provider plugin for DeepSeek Harness (dsh). Adds Command Code model access, live model catalog, plan-aware model selection, reasoning effort, image input, web search, and multi-account support.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **377**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `command-code` · `commandcode` · `deepseek-harness` · `dsh` · `dsh-plugin` · `llm` · `llm-provider` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mars-sea--dsh-commandcode-provider/2f2256468a8af0b9.png" width="100%" alt="Mars-Sea/dsh-commandcode-provider screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐281 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Just open your browser — get all your work done.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **281**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Nieoficjalny plugin DSH (DeepSeek Harness): używaj modeli webowych chat.deepseek.com jako dostawcy LLM — przechwytywanie logowania w przeglądarce, rozwiązywanie PoW, strumieniowanie SSE, wywołania narzędzi oparte na promptach.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **247**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐219 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **219**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Natywna wtyczka DeepSeek Harness (DSH) integrująca TypeSafe Jev lub Decision api, takie jak luna, jako warstwę decyzyjną System One do wyboru agentów, nadzoru, korekt i zatwierdzeń.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **203**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dshplugin/dsh-plugin-hub">dshplugin/dsh-plugin-hub</a></b> · ⭐193 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 10000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、搜索、安装各类 AI 插件。

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **193**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent` · `ai` · `cli` · `community-plugins` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `dsh-plugin-org`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dshplugin--dsh-plugin-hub/7dd84080ee0003e9.png" width="100%" alt="dshplugin/dsh-plugin-hub screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wtyczka DeepSeek Harness do migracji sesji między presetami z możliwością podglądu. Przekazania o stałym schemacie zachowują stan, intencję modelu źródłowego i nierozwiązane obrazy; oryginalna sesja pozostaje nienaruszona.

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
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐156 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **156**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/sorsama/deepseek-harness-mobile">sorsama/deepseek-harness-mobile</a></b> · ⭐137 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Android companion dla DeepSeek Harness | czat, cele, zatwierdzenia i powiadomienia z telefonu przez sieć LAN. Kotlin + Jetpack Compose.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Kotlin                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **137**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sorsama--deepseek-harness-mobile/11352624becb7d93.jpg" width="100%" alt="sorsama/deepseek-harness-mobile screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐129 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Po instalacji otrzymujesz 27 umiejętności inżynieryjnych i zwiększających produktywność z mattpocock/skills v1.3.1, bez potrzeby ręcznej instalacji umiejętności. 40 miliardów tokenów posłużyło do stworzenia tej wtyczki; w porównaniu z pierwotnymi umiejętnościami zapewnia ona 10-krotny wzrost wydajności programowania, a także pomaga początkującym szybciej rozpocząć pracę z tym zestawem umiejętności. Pełne wsparcie dla GitHub issue; Markdown jest w wersji podglądowej; GitLab nie jest obecnie obsługiwany. Dziękujemy za korzystanie i wsparcie 💗

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **129**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐126 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Motyw desktopowy Claude Code dla DeepSeek Harness｜ Motyw desktopowy Claude Code stworzony dla internetowego GUI DeepSeek Harness

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **126**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐119 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wtyczka pupila na pulpit DeepSeek Harness: pełna energii wielorybia dziewczyna jako asystentka towarzyszy ci podczas programowania 🐋 Obsługuje wersję desktopową DSH 0.2.0-rc.2 i starszą wersję Web (desktop pet / mascot, local-first)

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **119**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐87 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Umiejętności i wtyczki You.com do wyszukiwania w sieci, ekstrakcji treści, badań, finansów i wykrywania integracji, pomagające agentom AI tworzyć rozwiązania z wykorzystaniem aktualnego kontekstu internetowego.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **87**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐84 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into questions and spaced review · 把自己的资料变成题目与间隔复习的 DSH 学习插件

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **84**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Soren-ABT/dsh-knowledge">Soren-ABT/dsh-knowledge</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Knowledge base & RAG plugin for DeepSeek Harness (DSH): chunking, local embeddings, hybrid search, management panel

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **72**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `knowledge-based-systems` · `rag`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/soren-abt--dsh-knowledge/40cc300fdf79ee94.png" width="100%" alt="Soren-ABT/dsh-knowledge screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐70 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

dsh-sieve: wtyczka do inżynierii kontekstu i optymalizacji tokenów dla DeepSeek Harness (DSH) — filtrowanie wyników narzędzi, przycinanie kontekstu, progresywne ujawnianie umiejętności. O 36% mniejszy ładunek w odtwarzaniu offline. Wtyczka do zarządzania kontekstem DSH i optymalizacji tokenów w celu oszczędzania.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **70**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 70</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Strażnik wykonywany przed uruchomieniem dla agentów AI do programowania.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Wyselekcjonowana lista najlepszych świetnych wtyczek AI dla asystentów AI, w…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace: przeglądaj, instaluj i aktualizuj jednym kliknięciem…
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - 终末地官网风格的 DSH Web 主题：奶油纸底、墨黑文字、信号黄强调、全直角工业编辑风.
- [arcships/rutis](https://github.com/arcships/rutis) - Runtime wtyczek dla programów, które działają nieprzerwanie — rdzeń Rust…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [ZASENJC/dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) - 自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and…
- [Clarklevis1995/dsh-plugin-mobile-gateway](https://github.com/Clarklevis1995/dsh-plugin-mobile-gateway) - 以websocket为通信方式的dsh网关插件，支持在同一网域内移动端的接入，实现移动端的dsh app.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Aktualny katalog wtyczek DeepSeek Harness — odświeżany co godzinę, codziennie…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana: DeepSeek Harness as a subagent for HanaAgent.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Wyselekcjonowany katalog wtyczek DeepSeek Harness (DSH) — ponad 280 wtyczek…
- [hyzyn/dsh-plugin-kit](https://github.com/hyzyn/dsh-plugin-kit) - Plugin family for the DeepSeek Harness (DSH) Web GUI: a pnpm monorepo with a…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Wtyczka DeepSeek Harness: utrzymuje dokładne okno kontekstu modelu llm-pi-ai…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zotero toolkit for DeepSeek harness; Turn your Zotero library into an evidence…
- [Andersen216/dsh-whale-girl-live2d](https://github.com/Andersen216/dsh-whale-girl-live2d) - 🐋 鲸鱼娘桌宠 · Whale Girl Live2D —— DSH（DeepSeek Harness）Web 界面里的 Live2D 桌宠：跟着 agent…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: wieloplatformowy system agentów czatu grupowego oparty na DeepSeek…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Nawigacja po sesjach DSH.
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - Community GitHub Action for DeepSeek Harness — AI Code Review · CI Diagnosis ·…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Ewaluacja promptów, RAG, umiejętności, agentów i przepływów pracy oparta…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Wyselekcjonowane przez społeczność wtyczki, narzędzia, umiejętności i materiały…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 给中文网文作者的本地写作工作台.
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Wtyczka DeepSeek Harness: 15 umiejętności inżynierskich obra/superpowers…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Środowisko uruchomieniowe negocjacji handlowych A2A + wtyczka DeepSeek Harness…
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - MCP server management UI for DeepSeek Harness Web — floating panel, JSON…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Prawdziwy PowerPoint, nie HTML. Powiedz AI, co ma zawierać prezentacja, a…
- [Player-MINEPIG/dsh-tavern](https://github.com/Player-MINEPIG/dsh-tavern) - 以 DSH 原生会话与执行机制为权威的酒馆兼容插件，提供前后端 API，支持自由组合酒馆能力与 DSH 原生功能.
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - Wtyczka DeepSeek Harness: leniwy tryb seniora DietrichGebert/ponytail i port…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 给大肥鱼一个小说工作台：一起写正文、讨论后续情节、整理人物与世界设定，让长篇创作更贴近你的想法.
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - Wtyczka webowa DSH: hierarchiczne drzewo obszaru roboczego na pasku bocznym…
- [zhu1090093659/dsh-skins](https://github.com/zhu1090093659/dsh-skins) - Skin center plugin and built-in skins for the DSH Web GUI: skins are pure asset…
- [godchen520/dsh-web-remote](https://github.com/godchen520/dsh-web-remote) - DSH 手机/外网远程访问插件：免配置公网隧道 + 局域网 HTTPS 直连 + 自定义公网链接/端口 + 微信机器人.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Kompleksowy menedżer umiejętności, subagentów, MCP i LSP dla DeepSeek Harness…
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - Wielowymiarowa ocena jakości wtyczek DeepSeek Harness: ocenia repozytorium lub…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Izolowane testy instalacji i uruchomienia wtyczek DeepSeek Harness: instalują…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Wtyczka dokująca funkcji DeepSeek Harness: jeden panel do…
- [evoelsewhere/evoflux](https://github.com/evoelsewhere/evoflux) - Evoflux is an open-source, local-first workspace where AI agents build…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Ciągłe testowanie kompatybilności wtyczek DeepSeek Harness: dokładne wydania…
- [zhu1090093659/dsh-pet](https://github.com/zhu1090093659/dsh-pet) - Multi-pet companion plugin for the DSH Web GUI: a registry-driven floating pet…
- [Liaoyuanxinghuo/DSH-Plugin-Manager](https://github.com/Liaoyuanxinghuo/DSH-Plugin-Manager)
- [losebird/dsh-plugin-market](https://github.com/losebird/dsh-plugin-market) - DeepSeek Harness plugins market｜DSH 插件市场.
- [Tlyer233/dsh-vscode-review](https://github.com/Tlyer233/dsh-vscode-review) - deepseek harness review插件, 可以让你在vscode中直观看到dsh的&quot;增删改&quot;操作, 支持逐行ac或rj.
- [XHR666/dsh-mpkg-wallpaper](https://github.com/XHR666/dsh-mpkg-wallpaper) - Wtyczka DSH: używa plików .mpkg / katalogów Warsztatu Steam Wallpaper Engine…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeekBot: otwartoźródłowa alternatywa dla GrokBot, zbudowana na DeepSeek…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Prześwietlenie wtyczek DeepSeek Harness: zadeklarowane możliwości a rzeczywiste…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Wtyczka hosta DeepSeek Harness, która przechowuje dokumenty projektu i pamięć…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Wtyczka DSH: okno narzędziowe Git klasy IDE jako natywna karta…
- [Mars-Sea/dsh-deeppilot](https://github.com/Mars-Sea/dsh-deeppilot) - Native iPhone companion plugin for DeepSeek Harness — sessions, approvals…
- [adithyanraj03/dsh-graft-plugin](https://github.com/adithyanraj03/dsh-graft-plugin) - A DeepSeek Harness plugin that puts graft — a prebuilt graph of every symbol…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - Weryfikacja twierdzeń dotyczących projektu i kodu: fakty porównywane z kodem…
- [ddtcorex/maestro-skills](https://github.com/ddtcorex/maestro-skills) - Uniwersalne centrum umiejętności rozwoju agentów AI i wtyczka Cordis dla…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Wtyczka przepływu pracy inżynierskiej dla DeepSeek Harness: etapy zadań…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Wzorzec weryfikacji wtyczek DeepSeek Harness (dsh) bez zależności — bramki…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode w DeepSeek Harness — wtyczka DSH, która zapewnia działanie OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace wtyczek firm trzecich i zabezpieczony menedżer cyklu…
- [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) - Query local log files with Chinese natural-language time expressions…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx to oparty na potrzebach ludzi, rozszerzalny pulpit roboczy: rozmowy…
- [beihzb/dsh-notebook](https://github.com/beihzb/dsh-notebook) - Natywny notatnik w stylu Jupyter dla DeepSeek Harness: rzeczywisty sidecar…
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - demon dsh: rejestruje serwer internetowy DeepSeek Harness (dsh web) jako…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Bogato wyposażony agent kodujący dla DeepSeek Harness — przepływy pracy w stylu…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Wtyczka poprawiająca obsługę wprowadzania w DSH Web: przełączanie klawiszy…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Rodzina wtyczek samodoskonalenia agentów inspirowana Hermes, zaprojektowana…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - 为 DeepSeek Harness 桌面版提供「限网段 + 可选数字密码」的远程访问入口.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Wtyczka DeepSeek Harness: zamienia niepowodzenie provisioningu ACL sandboxa…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Umożliwia ponowienie próby nieprzypisanej pustej próby modelu — dla tego…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Środowisko uruchomieniowe wtyczek Rust z jądrem cyklu życia zweryfikowanym…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Teksty, dyskusje i wideo

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 0 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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

| Język      | Wpisy | Przykładowe projekty                                                                                             |
| ---------- | ----- | ---------------------------------------------------------------------------------------------------------------- |
| TypeScript | 385   | `anthropics/claude-code`, `anthropics/claude-code-action`, `see-stack/claude-code-mods`                          |
| JavaScript | 86    | `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                     |
| Python     | 41    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `AgriciDaniel/claude-mods-brain` |
| Shell      | 31    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`              |
| HTML       | 10    | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                               |
| Go         | 5     | `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`, `bunderlog/claude-plugins`                                  |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `melderan/claude-statusline-rust`, `arcships/rutis`                                  |
| Swift      | 3     | `bhargava-gumpula/claude-mods`, `essedev/relay`, `peaceinitiativemenhadenoil263/claude-status-bar`               |
| C          | 1     | `reporails/arcade`                                                                                               |
| CSS        | 1     | `zhu1090093659/dsh-skins`                                                                                        |
| Kotlin     | 1     | `sorsama/deepseek-harness-mobile`                                                                                |
| PowerShell | 1     | `rainyfei/claude-statusline-win`                                                                                 |

<sub>Liczone są tylko wpisy, w których określono język. Wpisy dokumentacyjne i dyskusyjne są wyłączone z tej tabeli.</sub>

## Współtworzenie

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Ostatnia aktualizacja · 2026-10-10T23:31:01+08:00</sub>
