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
> **Aktualny indeks** · Ostatnia synchronizacja: `2026-10-13T15:03:52+08:00` (UTC+8)
> · Wpisy: **585** · Dodane w najnowszej aktualizacji: **0** · Języki implementacji: **13**

<sub>Każdy poniższy wpis został automatycznie zebrany, przefiltrowany i ponownie sprawdzony. Żaden z nich nie jest płatną promocją.</sub>

<a id="featured"></a>

## Polecane teraz

<sub>Jeden wpis na kategorię, uszeregowany według oceny dowodów i liczby gwiazdek; ranking jest tworzony ponownie przy każdej aktualizacji. To ranking, a nie rekomendacja — każdy wybór prowadzi do jego pełnej karty poniżej. Preferowane są projekty, które opublikowały zrzut ekranu lub nagranie, aby pasek pozostał wizualny.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9490 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2545 · Python · 👁️ observed</sub>
<sub>Znajdź tokeny-duchy. Napraw je. Przetrwaj kompaktowanie. Unikaj pogarszania jakości kontekstu.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74474 · TypeScript · 👁️ observed</sub>
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
- [Oficjalne: własne repozytoria i informacje o wydaniach Anthropic](#oficjalne-własne-repozytoria-i-informacje-o-wydaniach-anthropic) — **16**
- [Mody: stworzone z użyciem możliwości tworzenia modów](#mody-stworzone-z-użyciem-możliwości-tworzenia-modów) — **457**
- [Ekosystemy wtyczek DSH i Cordis](#ekosystemy-wtyczek-dsh-i-cordis) — **101**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150493 · TypeScript · ✅ official · 0 天</summary>

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
| Gwiazdki               | **150493** |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9490 · TypeScript · ✅ official · 3 天</summary>

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
| Gwiazdki               | **9490**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8259 · Python · ✅ official · 3 天</summary>

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
| Gwiazdki               | **8259**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6360 · Python · ✅ official · 243 天</summary>

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
| Gwiazdki               | **6360**   |
| Ostatni push           | 2026-02-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1802 · Shell · ✅ official · 3 天</summary>

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
| Gwiazdki               | **1802**   |
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
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐75 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **75**     |
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
<summary><b>Więcej w tej kategorii</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Dodano `$.ui.notify` dla modów: wyświetla natywne powiadomienie za pomocą…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Naprawiono przypadki, w których klawisz Esc lub przerwanie podczas hooka…
- [songoao25/dsh-chatgpt-sub](https://github.com/songoao25/dsh-chatgpt-sub) - ChatGPT Subscription - a DeepSeek Harness plugin: bind your ChatGPT account via…

</details>

<a id="mods"></a>

## Mody: stworzone z użyciem możliwości tworzenia modów

Każdy wpis tutaj pokazuje dowody użycia możliwości, którą Claude Code zyskał w wersji 2.1.287: rysuje za pośrednictwem `ui.render`, posiada panel, pas lub kartę, odczytuje `$.ui.selection()`, uruchamia współpracowników za pomocą `agent.spawn` albo jasno mówi, że jest modem.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2545 · Python · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Znajdź tokeny-duchy. Napraw je. Przetrwaj kompaktowanie. Unikaj pogarszania jakości kontekstu.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | Python                                                            |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **2545**   |
| Ostatni push           | 2026-10-13 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐543 · JavaScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **543**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐217 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **217**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐164 · TypeScript · 👁️ observed · 8 天</summary>

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
| Gwiazdki               | **164**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐124 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **124**    |
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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐91 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **91**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 4 天</summary>

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
| Gwiazdki               | **79**     |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐77 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **77**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 6 天</summary>

##### 📝 Podsumowanie

Eksperckie skills, agenci, polecenia, reguły, hooki i style wyjścia dla Claude Code — ciągłość sesji + nowoczesne narzędzia CLI do rzeczywistych przepływów pracy programistycznej

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
| Gwiazdki               | **62**     |
| Ostatni push           | 2026-10-07 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐57 · TypeScript · 👁️ observed · 9 天</summary>

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
| Gwiazdki               | **57**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐48 · TypeScript · 👁️ observed · 4 天</summary>

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
| Gwiazdki               | **48**     |
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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐29 · TypeScript · 👁️ observed · 9 天</summary>

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
| Gwiazdki               | **29**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐27 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **27**     |
| Ostatni push           | 2026-10-13 |
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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐18 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **18**     |
| Ostatni push           | 2026-10-13 |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

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
| Gwiazdki               | **13**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 9 天</summary>

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
| Ostatni push           | 2026-10-13 |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 10 天</summary>

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
<summary><b>Więcej w tej kategorii</b> <sub>· 423</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Modyfikacje Claude i narzędzia do ich tworzenia: najpierw umiejętność…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Modyfikacje Claude Code autorstwa Raya Amjada: panele, pasma, strażnicy…
- [petekp/inbox](https://github.com/petekp/inbox) - A Claude Code mod that gathers and intelligently manages outstanding questions…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Środowisko Claude Code, którego używam codziennie, publikowane pod tą nazwą od…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Zmień dach w Claude Mods dla Claude Code: bez modyfikowania pliku binarnego…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cztery modyfikacje Claude Code: Cache Keeper, Recording Mode, Goal Meter i…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Modyfikacje Claude Code od Learning Hacker: przedstaw działanie agenta w…
- [kakha13/claude](https://github.com/kakha13/claude) - Modyfikacje Claude Code, które poprawiają i tłumaczą Twoje prompty, zanim…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Baza wiedzy Obsidian z podanymi źródłami na temat Claude Code mods: jak…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mody i umiejętności Claude Code od Nekyia Labs, tworzone i codziennie używane…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel boczny Claude Desktop (karta Code): wyświetla wszystkie niedokończone i…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Pasek użycia nad polem wejściowym Claude Desktop (karta Code): limit 5h / 7d…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Wygląd aplikacji desktopowej dla transkrypcji terminala Claude Code, jako mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel boczny dla Claude Code: podagenci uruchamiani przez sesję, zadania…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mody Claude Code: menu narzędzi Claude, tryb Zen, motywy terminala, sterowanie…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Umiejętność ucząca agentów Claude Code tworzenia modów Claude.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Społecznościowe mody, wtyczki i umiejętności Claude, instalowalne z jednego…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mody Claude (wtyczki z hakami funkcji) dla Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeria modów Baselane: mody Claude Code, sprawdzone i przypięte.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Kolejka decyzji CLI/TUI dla ludzi pracujących z agentami konwersacyjnymi.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE pane mod: agent board, file tree and HWP/PDF viewer, system…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code rysujący różnice Edit i Write w dwóch kolumnach obok siebie.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mody Claude Code: panel zużycia 像素螃蟹 usage-hud + klikalne linki HTML w…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Pływająca karta statusu dla Claude Code — model, kontekst, limity szybkości…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mody dla Claude Code: wtyczki function-hook dodające aktywne panele i…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Wtyczka Claude Code typu wszystko w jednym.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Test pisania na czas, podczas gdy Claude pracuje. Modyfikacja Code dla Claude.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mody Claude Code: screen-guard ukrywa nazwy i sekrety podczas udostępniania…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mody i skórki dla Claude Code: pasek postępu na żywo dla zadań Claude, czytelny…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Rozszerzenia Claude Code. Odblokuj pełną moc Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod Claude Code (wtyczka), który dodaje panel boczny z kartami Activity, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panele, zabezpieczenia i mody poprawiające wygodę pracy z Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dwa mody Claude Code nad polem promptu: miernik okna kontekstu, limit 5 godzin…
- [Unayung/cc-mods-enil](https://github.com/Unayung/cc-mods-enil) - LINE wewnątrz Claude Code: enil TUI jako mod Claude Code.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Odczytuje pliki markdown nazwane przez Claude Code i renderuje je obok sesji;
- [davekiss/mods](https://github.com/davekiss/mods) - Modyfikacje Claude Code autorstwa Dave Kiss.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code: miniatury wklejonych obrazów nad promptem, w dowolnym terminalu.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Głosowy współpracownik dla Claude Code.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow dla Claude Code: spokojna lista kontrolna nad polem promptu…
- [BatuhanCakmakk/wavy-usage](https://github.com/BatuhanCakmakk/wavy-usage) - Wypełnione płynem pierścienie użycia nad monitem Claude Code: limity 5h/7d…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mody Claude Code: pasek kontekstu, panel agentów, rozmywanie PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mody Claude Code: typing-speed, prędkościomierz pisania na żywo ze statystykami…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fajerwerki dla Claude Code: każde naciśnięcie klawisza, wywołanie narzędzia…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Modyfikacje dla Claude Code: panele, polecenia i hooki zbudowane za pomocą…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Odkrywaj mody, wtyczki i rozszerzenia Claude Code dzięki animowanym…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code: diagramy mermaid rysowane bezpośrednio w transkrypcji.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Małe modyfikacje Claude Code (wtyczki function-hook): session-switcher i inne.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Sklep z aplikacjami dla modyfikacji Claude Code, wewnątrz Claude Code: użyj…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sześć modyfikacji Claude Code: limity planu i kontekst nad promptem, pomocnik…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mody Claude Code: mod-scout (znajduje najczęściej używane mody), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dwa mody Claude Code do jednoczesnego uruchamiania wielu sesji: karta kontekstu…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mody Claude Code na żądanie — umiejętność, która odczytuje Twoją rozmowę i…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: odkrywaj, sprawdzaj, przełączaj i aktualizuj mody Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Najlepsze mody Claude Code: starannie wybrane, sprawdzone i przypięte.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Wtyczka Claude Code: automatyczne kierowanie do modeli Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Modyfikacja Claude Code: panel na żywo z żądaniami PR GitHub, które sesja…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sześć modów dla Claude Code: animowana maskotka Clawd, paski limitu użycia i…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Marketplace modów dla Claude Code: debugger krokowy pętli agenta, podpowiedzi…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Modyfikacje open source dla Claude Code: panele, wiersze stanu, powiadomienia…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Najlepszy kompleksowy pakiet modyfikacji dla Claude Code: limity użycia i HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Odtwarzaj YouTube Shorts w swoim Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Zestaw narzędzi Claude Naren: skills, mody i serwery MCP dla Claude Code.
- [nsodhi-cmu/claude-code-ripple](https://github.com/nsodhi-cmu/claude-code-ripple) - Mod Claude Code, który tworzy grafy wywołań zmian w twoim kodzie.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mody dla Claude Code: Clawd, mała pikselowa maskotka odgrywająca to, co robi…
- [reporails/arcade](https://github.com/reporails/arcade) - Klasyczne gry desktopowe jako mody Claude Code, uruchamiane w panelu podczas…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - modyfikacje kodu dla claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Własny marketplace modyfikacji dla Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Wyselekcjonowana lista modów Claude Code, instalowanych jako marketplace…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Dwa mody Claude Code: cache-keeper i ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mody Claude Code, które pilnują agenta — haki funkcji strzegące zakresu…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Prosto z fabryki. Modyfikacja Claude Code: poproś o mem, nie przerywając pracy.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Modyfikacja Claude Code: pasek pamięci podręcznej promptu, następne kroki…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code rysujący limity użycia i wydatki na pasku nad promptem.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Mod Claude Code do zapisywania myśli w trakcie pracy, porządkowania ich między…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Bieżący status PR GitHub, gotowość do scalania, kontrole, komentarze i alerty…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Hoduj jajko herbaciane, które powoli nabiera smaku podczas pisania code · Hoduj…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Modyfikacje Claude Code autorstwa Hermana (marketplace herman-mods).
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Modyfikacja Claude Code: odpowiadaj punkt po punkcie na Claude, bezpośrednio w…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notatki terenowe z pierwszego dnia o modach Claude Code na Windows: pasek…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Mod Claude Code: status pull request GitHub na żywo.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Małe karty umieszczone pod promptem Claude Code albo zadokowane obok…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: bieżące mierniki kosztu, kontekstu i limitu planu nad…
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 Robimy trochę TECHNO, bejbe 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin i mod Claude Code: AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code, który włącza lub wyłącza globalne umiejętności, agentów…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Przetestowane modyfikacje Claude Code instalowane jednym poleceniem…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Przytulna modyfikacja RPG HUD dla Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Zestaw modyfikacji claude code mojego autorstwa.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modyfikacje Claude Code. touch-map: zobacz jako drzewo i mapę aktywności, które…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Ucz się języka obcego podczas pracy z Claude Code.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Modyfikacja Claude Code, która na bieżąco informuje, które pliki zmienił Claude…
- [0xctx/sysop](https://github.com/0xctx/sysop) - Powiedz Claude, czego chcesz. Otrzymasz wynik zbudowany, przetestowany…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Opiekuje się długą sesją Claude Code, abyś nie musiał tego robić: obserwuje…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - Modyfikacja Claude Code, która utrzymuje ciepłą pamięć podręczną promptu…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Pasek boczny na żywo z kosztami, tokenami i wykorzystaniem kontekstu dla Claude…
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - Modyfikacje Claude Code autorstwa ayagmar: rynek wtyczek.
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Modyfikacje function-hook dla Claude Code: wiersz telemetryczny limitów, panele…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Modyfikacja Claude Code, która prowadzi bieżącą listę otwartych kwestii w…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Modyfikacje Claude Code dla prawdziwych inżynierów.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Podsumowanie sesji terminala Claude Code w karcie Code aplikacji desktopowej…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Mod Claude Code: łap pixel-artowe Modstery w grze bezczynnościowej, podczas gdy…
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Modyfikacja Claude Code: sprawdzaj, z których umiejętności, wtyczek, podagentów…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zobacz, które pliki każdy agent Claude Code ma w swoim kontekście i ile każdego…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Małe mody Claude Code do terminala i aplikacji desktopowej.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Umiejętność + mod Claude CLI, który dodaje hiszpańskie słowa do odpowiedzi…
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Modyfikacja Claude Code — przestań marnować tokeny: /keepwarm.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Twoje zdarzenia Alarum nad promptem Claude Code: co właśnie nadeszło i jedno…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Lista zadań Floatee nad promptem Claude Code: uruchamiaj, prowadź i odhaczaj…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Modyfikacja Claude Code, która stylizuje go na The Machine z Person of Interest.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesji, postęp Spec Kit na żywo i zarządzanie oknem…
- [kevinmedeiros/claude-mods](https://github.com/kevinmedeiros/claude-mods) - Modyfikacje na żywo dla Claude Code: limity planu informujące, jak długo będą…
- [KevinYu1580/jcGearbox](https://github.com/KevinYu1580/jcGearbox) - Modyfikacja Claude Code: wybiera model raz na sesję, a poziom wysiłku przy…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Okno kontekstu jako jeden wiersz nad promptem, narysowane tak, jak Claude Code…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: wykres na żywo pokazujący, co wie Claude Code.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Panel HUD zadań na żywo dla Claude Code Desktop: pasek nad promptem podczas…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Wtyczka Claude Code (mod), która sprawia, że terminalowy interfejs Claude Code…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Nie pozwól, aby twoja uwaga błądziła podczas oczekiwania na odpowiedź Claude…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Czternaście modów Claude Code w jednej wtyczce, każdy z możliwością…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Darmowa, otwartoźródłowa wtyczka dla Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Wyselekcjonowane mody Claude Code, dema oryginalnych twórców, publiczne…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Kolejka promptów dla Claude Code w formie modyfikacji: /after &lt;task&gt; uruchamia…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Modyfikacje Claude Code: starannie wybrane i przetestowane, a każda modyfikacja…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Umiejętności Claude Code: weryfikator faktów w dokumentacji, audytor kodu…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod Claude Code: klikalne ścieżki w odpowiedziach — kliknij folder, aby…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Wtyczka Claude Code buddy: towarzysz ASCII nad promptem, który pamięta Twoje…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Wtyczka Claude Code do widoczności narzędzi per agent — ukrywaj i odmawiaj…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Modyfikacje Claude Code: warstwa bezpieczeństwa dla Claude Code — redagowanie…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Kolekcja świetnych modyfikacji Claude Code | Kolekcja modyfikacji Claude Code.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: nieoficjalny fanowski mod Avengers do Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: modyfikacja Claude Code, która na żądanie odczytuje na głos…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Daj klapsa Claude, gdy coś zepsuje — mod antystresowy dla Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mody Claude Code: małe wtyczki do aktualizowanych paneli, routingu modeli…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code z dowodami. Wtyczka, która planuje, deleguje i potwierdza wykonanie…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Modyfikacja Claude Code: limit 5 h/7 dni, okno kontekstu, czas pozostały do…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod i wtyczka Claude Code: monitor użycia, licznik tokenów i wiersz stanu.
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC (Every Mod Claude Code): wyselekcjonowany, przetestowany zbiór modów Code…
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [adithepmeekhun/self-clear](https://github.com/adithepmeekhun/self-clear) - A Claude Code mod that keeps long agent runs going: at a context size you…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Mody Claude Code autorstwa afterever (marketplace wtyczek).
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [akkaradej/hawkeye](https://github.com/akkaradej/hawkeye) - Mod Claude Code: kropka statusu, rozszerzenie cache promptów, pierścień…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Modyfikacje Claude Code: karty statystyk sesji nad polem promptu.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Animowany kot z alfabetu Braille.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Pikselowy kot nad promptem Claude Code, który wykonuje testowe połączenie z…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code, który wybiera dobry moment na kompakcję, aby utrzymać małe…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modyfikacje Claude dla Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Uniwersalne modyfikacje dla Claude Code: paski, panele, powiadomienia i hooki.
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [AnnihilationWizard/chrome-close](https://github.com/AnnihilationWizard/chrome-close) - Modyfikacja Claude Code umożliwiająca uruchomienie jednego bezgłowego Chrome…
- [aott33/model-router](https://github.com/aott33/model-router) - Modyfikacja Claude Code, która wybiera model dla każdego podagenta przed jego…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Modyfikacja Claude Code: okno kontekstu w jednej spokojnej linii, szarej…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Po każdej zmianie kodu przepływa statek LGTM Lines — modyfikacja Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Limity wykorzystania Claude jako animowana karta zdrowia mieszkańca wioski, z…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mody Claude Code dla zespołu S2 (marketplace ather).
- [astromelon/takgon-mods](https://github.com/astromelon/takgon-mods) - Osobista wtyczka modów Claude Code (takgon-mods).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Krótkie treningi, gdy Claude pracuje: dzienny cel, serie, odznaki i opcjonalne…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Tablica zużycia dla Claude Code: wydatki według modelu.
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Modyfikacje Claude Code: panele, paski i zabezpieczenia działające wewnątrz…
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Modyfikacja Claude Code pokazująca, czym zajmują się podagenci: pasek postępu…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Modyfikacja Claude Code pokazująca, ile czasu zajęła każda tura, w postaci…
- [benelog/claude-mods](https://github.com/benelog/claude-mods) - Modyfikacje dla Claude Code: HUD wiersza stanu i nie tylko.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing dla Claude Code: Apple Music i Spotify nad poleceniem, z…
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - Utrzymywane, audytowane kopie modyfikacji Claude Code (filetree, cache-tax).
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - Karta Performance dla Claude Code pokazuje na żywo przebieg każdego żądania…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mody dla Claude Code: zegar cache, Blast Radius, sugestie, lista zadań, grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Po prostu sowa dla Twojego Claude Code.
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - Osobiste modyfikacje Claude Code.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Modyfikacje Claude Code dla frameworka ai-architect.tools: jedna kwestia na…
- [cerebrai/ironman-mod](https://github.com/cerebrai/ironman-mod) - A claude code mod for humna-AI augmented workflow -- like tony stark.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Oryginalny silnik Doom z Freedoom, grywalny wewnątrz Claude Code.
- [ChristianLemer/claude-mods](https://github.com/ChristianLemer/claude-mods) - Claude Code mods kept in other people.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Panel słownika słów i wtyczka paska stanu Claude Code.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Utrzymuj Claude Code zgodnie z planem: etapy, bramki zatwierdzania i budżet…
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Modyfikacje Claude Code.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Modyfikacje Claude Code przeznaczone wyłącznie dla zespołu d3nim.
- [davidlambl/claude-extensions](https://github.com/davidlambl/claude-extensions) - Claude Code mods, skills and plugins, installable as a plugin marketplace.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi żyjące wewnątrz Claude Code: wykluwa się, zjada kod pisany przez…
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Modyfikacja Claude Code: stan przeglądu PR, zatwierdzenia, kontrole i konflikty…
- [dglasgal/usage-rings](https://github.com/dglasgal/usage-rings) - Modyfikacja Claude Code: pierścienie użycia planu, koszty sesji i modeli według…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - Moja kolekcja modyfikacji claude.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: po zablokowaniu wywołania narzędzia przez guard zatrzymuje…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Ulubione dla Claude Code: ikony jednoklikowe dla poleceń i umiejętności.
- [drnic/claude-mods](https://github.com/drnic/claude-mods)
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - Aktywna tablica falowa planu twojej sesji nad promptem Claude Code.
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instrukcje, umiejętności, rozszerzenia Pi i mody Claude Code dla Pi, Codex i…
- [esinecan/mental-model-mod](https://github.com/esinecan/mental-model-mod) - Claude Code mod: Claude.
- [fbwndrud/tidia](https://github.com/fbwndrud/tidia) - Czyste dyktowanie dla AI: mod Claude Code, który oczyszcza dyktowanie głosowe…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mody do Claude Code (wtyczki function-hook): session-meter i inne.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: jeden mały przycisk, który ukrywa wszystkie modyfikacje…
- [finalpantasy/claude-mod-pack](https://github.com/finalpantasy/claude-mod-pack) - Pakiet modyfikacji Claude: małe modyfikacje Claude Code.
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Modyfikacje zespołu Hospedin dla Claude Code w fazie testów.
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Modyfikacja Claude Code: zamroź sesję i wznów ją później, jak gdyby nic się nie…
- [g761007/hudcade](https://github.com/g761007/hudcade) - Pikselowy HUD dla Claude Code: kontekst, koszt, pamięć podręczna, agenci i…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Kliknięcie Ctrl z klawiszem myszy kopiuje link w każdym bloku kodu w…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - Modyfikacja Claude Code dla aplikacji desktopowej: kliknij odwołanie do pliku w…
- [gugahoi/claude-mods](https://github.com/gugahoi/claude-mods) - Modyfikacje Claude Code: podpowiadanie typu PR GitHub, pasek i panel stanu PR…
- [gyoomun/claude-mods](https://github.com/gyoomun/claude-mods) - Mody Claude Code stworzone przez innych, dostosowane do mojego sposobu pracy…
- [heidiks/agent-kit](https://github.com/heidiks/agent-kit) - Umiejętności, wtyczki i modyfikacje Claude Code.
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Miernik wydatków na żywo dla Claude Code: koszt sesji z podagentami i…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Modyfikacja Claude Code: jak długo trwała każda odpowiedź, jak długo myślał…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Kokpit nad promptem Claude Code. Kaczka odczytuje wskaźniki.
- [Isaacg1000/isaac-mods](https://github.com/Isaacg1000/isaac-mods) - Osiem modyfikacji Claude Code: panel postępu, skórki narzędzi, drzewo plików…
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Mod Claude Code: drzewo plików w pasku bocznym, które pulsuje na plikach…
- [jackmel030/claude-session-notes](https://github.com/jackmel030/claude-session-notes) - Mod Claude Code: przypinane notatki na pasku bocznym dla bieżącej sesji…
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Automatycznie odczytuje rysunki techniczne, a następnie tworzy model w…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Miejsce do przechowywania moich modyfikacji claude.
- [jepperip/claude-session-todo](https://github.com/jepperip/claude-session-todo) - Claude Code mod: a live session todo pane the agent keeps current.
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - Bieżąca tablica podagentów Claude Code wewnątrz VS Code: podagenci każdej…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel użycia kontekstu na pasku bocznym: suma, kategorie, przyrost w każdej…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista plików na pasku bocznym: które pliki utworzono, zmodyfikowano lub…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Futrzasty w stylu 8-bitowym.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel boczny „O co pytałem.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Oś czasu na pasku bocznym: na co przeznaczono czas w tej turze.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Panel wymiany tokenów na pasku bocznym: ile tokenów rozmowa główna wysłała do…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Szczera krótka rozmowa claude code: po każdej odpowiedzi Claude cicho mówi, co…
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Nieoficjalny przewodnik społeczności po modyfikacjach Claude Code.
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Katalog modyfikacji dla Claude Code.
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Modyfikacje Claude Code autorstwa Josepha Ayoub: marketplace wtyczek…
- [K-Mertin/claude-monster-pet](https://github.com/K-Mertin/claude-monster-pet) - A Claude Code mod: raise a pixel-art digital monster that grows from your…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd mieszka w pasku nad twoim promptem Claude Code: odgrywa sesję, pokazuje…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Modyfikacja odczytująca na głos odpowiedzi i powiadomienia Claude Code za…
- [kamalpreet11/claude-mods](https://github.com/kamalpreet11/claude-mods) - Proste i skuteczne mody Claude.
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mody do Claude Code. PixBar: pikselowe stworzenie nad Twoim promptem, które…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod Claude Code: każda sesja Claude Code w jednym pływającym oknie, z…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Małe modyfikacje Claude Code w jednym sklepie z wtyczkami.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Mod Code dla Claude: wybiera model i nakład pracy związane z rozumowaniem…
- [krysmalskipl/claude-code-mods](https://github.com/krysmalskipl/claude-code-mods) - Modyfikacje Claude Code autorstwa krysmalskipl: instaluj tylko te, których…
- [liangRXdev/phi-guard-tw](https://github.com/liangRXdev/phi-guard-tw) - Modyfikacja Claude Code: maskuje tajwański numer dowodu osobistego / zezwolenia…
- [lifeofgurpreet/glanceline](https://github.com/lifeofgurpreet/glanceline) - A Claude Code mod: your session at a glance, with a heads-up before you hit a…
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Tworzony przez społeczność przewodnik po modyfikacjach Claude Code: przypadki…
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Modyfikacja Claude Code: limity twojego planu (sesja 5 h, tydzień) i odnowienie…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Pojedyncze modyfikacje Claude Code z Mod Box, z których każdą można…
- [Lutifya/claude-code-mods](https://github.com/Lutifya/claude-code-mods) - Modyfikacje Claude Code: kolejne kroki (sugerowane prompty + paski użycia) i…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod do Claude Code, który pokazuje, co robi Claude, w podtytule karty iTerm2…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, nieoficjalny fanowski pikselowy towarzysz, który mieszka nad monitem…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Puszysta czarna kotka nad promptem Claude Code.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Małe modyfikacje dla Claude Code: runner-avatar, mały awatar biegnący nad…
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Modyfikacje Claude: licznik tokenów (token-meter).
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Modyfikacja Claude Code: panel na żywo pokazujący, do czego dąży agent…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod Code Claude: panel /sessions do przeglądania i usuwania sesji wraz z ich…
- [melandres8/claude-mods](https://github.com/melandres8/claude-mods) - Modyfikacje Claude Code: relevo.
- [miami1124/pusung-mods](https://github.com/miami1124/pusung-mods) - Claude Code mods by Pu-Sung Chang. Live NBA scores above the prompt, in the…
- [mkiselyow/diff-lens](https://github.com/mkiselyow/diff-lens) - Modyfikacja Claude Code: poproś Claude, aby przeprowadził Cię przez PR, kliknij…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Mod Code dla Claude: Codex (subskrypcja ChatGPT) oraz inne modele nie-Anthropic…
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [MoriHiroshiDesu/hiroshi-claude-mods](https://github.com/MoriHiroshiDesu/hiroshi-claude-mods) - Osobiste modyfikacje Claude Code (interfejs i działanie).
- [mrdainami/trend-radar-mod](https://github.com/mrdainami/trend-radar-mod) - What to make next on YouTube, with proof, plus the thumbnail.
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Mod Code dla Claude: nadaje kartę terminala, w której działa Claude.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code, który ponownie włącza narzędzia todo dla modeli, które je…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Modyfikacja Claude Code, która czeka na bezpieczną pauzę, a następnie…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: jeden wiersz na zadanie nad promptem z bieżącym zadaniem…
- [mugenracerman/clean-view](https://github.com/mugenracerman/clean-view) - Claude Code mod: hides technical output and shows a plain-English progress box…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Graj w Connect Four przeciwko AI wewnątrz Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: gdy inny agent programistyczny wykonuje commit w Twoim…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code dla repozytoriów współdzielonych przez kilku agentów AI…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Modyfikacja Claude Code: jeden przycisk nad promptem dla każdego implementatora…
- [netgfx/claude-swarm-mod](https://github.com/netgfx/claude-swarm-mod) - A Claude Code mod for creating and orchestrating swarms of agents.
- [nozomichi00/claude-code-mods](https://github.com/nozomichi00/claude-code-mods)
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Zabezpieczenie SQL w Claude Code: pyta przed wykonaniem przez Claude poleceń…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Panel notatnika dla Claude Code jako mod.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Jeden mod dla Claude Code, Windows i CJK przede wszystkim: podgląd wklejonych…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mody Code dla Claude: miniatury obrazów i wiersz stanu.
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid: kompleksowy proces przegląd → plan → naprawa, wymuszany przez mody…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Najlepsze mody Claude Code, posortowane według tego, co dla Ciebie robią.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dwa mody Claude dla Claude Code: garde-du-corps.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: mod Code dla Claude. Trwałe worktree z dostępem tylko do odczytu na…
- [phatjam98/claude-mods](https://github.com/phatjam98/claude-mods) - Mody Claude Code autorstwa phatjam98.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Boczny panel statystyk sesji na żywo dla karty Code aplikacji desktopowej…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Moduły dla Claude Code: safety-guard blokuje destrukcyjne polecenia i dostęp do…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Animowany krab Claude w pixel art dla Claude Code: odgrywa nad Twoim promptem…
- [r1305/claude-mods](https://github.com/r1305/claude-mods) - Modyfikacje dla Claude Code: routing modeli z pulpitem zużycia i komunikacją…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod dla Claude Code: pompki do zrobienia podczas pracy Claude. Bez tokenów.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: przewodnik terenowy po modach Code dla Claude, od ELI5 po…
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Otwarty marketplace modyfikacji Claude Code, z umiejętnościami repozytorium do…
- [s-0-a-r/session-meter](https://github.com/s-0-a-r/session-meter) - Modyfikacja Claude Code rejestrująca metryki dla każdej sesji i wyświetlająca…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: zamienia plan zatwierdzony w trybie planu w aktywną listę…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Starannie wybrana lista modyfikacji Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Tryb bez kosztów: agenty pomocnicze działają na Haiku, a duże pliki i logi są…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ścieżka dźwiękowa lofi, która podąża za sesją: spokój, skupienie, przepływ, a…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Ucz się podczas kodowania przez Claude: po turze, która zmieniła kod, nad…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Nagranie każdej zmiany wprowadzanej przez Claude: odtwórz każdą zmianę…
- [ShadowDog007/claude-mods](https://github.com/ShadowDog007/claude-mods)
- [shawnbotha/claude-mods](https://github.com/shawnbotha/claude-mods) - Różne modyfikacje Claude.
- [shawnpetros/claude-receipts](https://github.com/shawnpetros/claude-receipts) - Mod Claude Code: postęp kamieni milowych z uczciwym szacunkiem czasu nauki…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Mody do Claude Code autorstwa Showrin, zwiększające produktywność codziennej…
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Mod Code dla Claude: limity kontekstu i planu z prognozą tempa zużycia oraz…
- [SimplicityGuy/claude-mods](https://github.com/SimplicityGuy/claude-mods) - Modyfikacje Claude Code: marketplace wtyczek, rozpoczynający od hivewatch do…
- [skryvets/claude-status-bar-mod](https://github.com/skryvets/claude-status-bar-mod) - Modyfikacja Claude Code: kolorowe informacje o sesji pod promptem — kontekst…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Mod Code dla Claude, który podtrzymuje działanie sesji bez nadzoru po…
- [Sri-Ln/glitch](https://github.com/Sri-Ln/glitch) - Glitch: a kit of Claude Code mods — themes, a session HUD, budget guard and…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - Zbiór modyfikacji Claude Code: TypeScript hooków funkcji, dostarczanych jako…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Wiadomości commitów jednym kliknięciem dla Claude Code z tańczącą Malenią w…
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Mody dla Claude Code. cache-meter: współczynnik trafień pamięci podręcznej…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — mod Claude Code pokazujący użycie planu Claude.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Nieoficjalne modyfikacje Claude Code autorstwa tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Modyfikacja Claude Code, która wyświetla bieżącą sesję w panelu: każdy prompt…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace pluginów Claude Code z modami: pluginy function-hooks, które rysują…
- [thunini/thinking-flow](https://github.com/thunini/thinking-flow) - A Claude Code mod that draws how Claude reached each answer: your question, a…
- [tomato3017/tomato-claude-mods](https://github.com/tomato3017/tomato-claude-mods) - Claude Code plugin marketplace.
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Słuchaj odpowiedzi Claude Code, gdy aktualnie czytane zdanie jest podświetlane.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Mod Code dla Claude: jeden przycisk pod ostatnią odpowiedzią Claude kopiuje…
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - Tryb CC, który pokazuje, na jakie konto Claude, organizację i plan jesteś…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Modyfikacja Claude Code: animowany pasek postępu i podsumowanie ukończenia dla…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trzy małe mody Claude Code: sprawdzaj, kiedy Twoi podagenci skończą pracę…
- [varunmoka7/disk-sweep](https://github.com/varunmoka7/disk-sweep) - Ostrzega, gdy na komputerze Mac zaczyna brakować miejsca na dysku, a za pomocą…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Powiedz „I.
- [varunmoka7/park](https://github.com/varunmoka7/park) - Zapisz tę sesję Claude Code i napisz notatkę na następną.
- [varunmoka7/read-fence](https://github.com/varunmoka7/read-fence) - Uniemożliwia Claude otwieranie plików jeden po drugim w folderach umiejętności…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Zadaj Claude pytanie poboczne w panelu obok swojej pracy.
- [varunmoka7/skills-az](https://github.com/varunmoka7/skills-az) - Wyświetla listę poleceń slash i umiejętności w kolejności alfabetycznej zaraz…
- [varunmoka7/unattended](https://github.com/varunmoka7/unattended) - Uniemożliwia sesji Claude Code zadawanie pytań, gdy przy klawiaturze nikogo nie…
- [vcdim/claude-code-sciplot](https://github.com/vcdim/claude-code-sciplot) - Mod Claude Code do wykresów naukowych: Python, R, TikZ, MATLAB i Mathematica w…
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Wtyczka Claude Code: odliczanie pamięci podręcznej promptu, współczynnik…
- [wendyyyanto/usage-meter-mod](https://github.com/wendyyyanto/usage-meter-mod) - Mod Claude Code pokazujący limity użycia, kontekst, model i nakład pracy w…
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Claude Code: własny model sesji wybiera model i nakład pracy każdego subagenta.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — gdy kontekst przerasta swoją powłokę, zrzuca ją do folderu i działa…
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Zestaw modyfikacji Claude Code (marketplace wonr-mods).
- [wonwoo/tool-timeline](https://github.com/wonwoo/tool-timeline) - Modyfikacja Claude Code pokazująca, na co zużyto czas w każdej turze: linia pod…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Wtyczka Claude Code: limity użycia Claude Pro/Max wraz z prognozą tempa…
- [xingkaixin/claude-mods](https://github.com/xingkaixin/claude-mods) - Modyfikacje Claude Code.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mody dla Claude Code. agent-crew: obserwuj pracę swoich podagentów jako żywą…
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Mody Claude Code: kapsuła następnego kroku w tradycyjnym chińskim, kopiowanie…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Starannie wybrana kolekcja najlepszych zasobów dla najbardziej niesamowitych…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Wtyczka Claude Code pokazująca, co się dzieje — wykorzystanie kontekstu…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Piękna, wysoce konfigurowalna linia statusu dla Claude Code CLI z obsługą…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Wszystkie części promptu systemowego Claude Code, 27 wbudowanych opisów…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Umiejętność tworzenia filmów AI dla Claude Code i Codex — kinowe filmy…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Ponad 45 wskazówek, jak najlepiej wykorzystać Claude Code — od podstaw po…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generowanie karuzel Xiaohongshu oraz par okładek…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Przeglądaj różnice wygenerowane przez agenta programistycznego w panelu…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Kompleksowa wtyczka paska stanu dla Claude Code z informacjami o wykorzystaniu…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Twórz modyfikacje dla Claude Code: przechwytuj dowolne żądanie, modyfikuj…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Kompleksowy pulpit statusu dla Claude Code — informacje o sesji, paski limitów…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: śledź ślad węglowy swoich sesji Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Estetyczna linia statusu dla Claude Code autorstwa awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Publiczne Skills i modyfikacje Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, modyfikacje, subagenci, hooki, polecenia slash i poradniki dla Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legalne bezpłatne LLM APIs i agenci programistyczni — aktualizowane…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Wyniki na żywo, terminarze i tabele piłki nożnej dla rozgrywek, które…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, który zmienia agenta kodowania w eksperta od firmware.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Pory modlitw, data hidżry, adhkar, codzienny ajat, post sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Osobista konfiguracja Claude Code, wersjonowana w ~/.claude — agenci…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Zestaw wtyczek dla Claude Code, pi i DeepSeek Harness: HUD paska stanu, pasek…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Przenośny zestaw narzędzi Claude Code dla .NET DDD/Clean Architecture: agenci…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Przenośna globalna konfiguracja Claude Code: niestandardowe umiejętności, hooki…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Nieoficjalne mody karty Code w Claude Desktop — usage-pet: pasmo zużycia z…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Wtyczki Claude Code, których używam codziennie: skills i mody uporządkowane…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analizuj użycie tokenów i koszty Claude Code na podstawie lokalnych dzienników…
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Estetyczny i informacyjny wiersz statusu dla Claude Code.
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Konfigurowalny wiersz statusu dla Claude Code z edytorem opartym na…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace wtyczek i umiejętności Claude Code ułatwiających tworzenie modów do…
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Jednowierszowy, oznaczony kolorami statusline dla Claude Code — folder, model…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Wiersz stanu na żywo z fazą przepływu pracy dla Claude Code.
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Mikropulpit na 3 wiersze dla terminala Claude Code — model, zużycie kontekstu…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repozytorium modów Awesome Media dla Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Ogranicz wydatki na Claude Code i tokeny Codex: kieruj wyszukiwania i…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Szybki, konfigurowalny statusline dla Claude Code — pojedynczy statyczny plik…
- [barkleesanders/claude-hud](https://github.com/barkleesanders/claude-hud) - Wyświetlacz przezierny w czasie rzeczywistym dla Claude Code — stan kontekstu…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Wzmocniony, z korekcją kolorów i pozbawiony zależności wiersz stanu dla Claude…
- [ist-j-ichikawa/claude-code-statusline](https://github.com/ist-j-ichikawa/claude-code-statusline) - j-ichikawa.
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Kompaktowy, aktywnie utrzymywany wiersz statusu dla Claude Code — model, nakład…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - przyjazny pasek stanu Claude Code, przy którym można zmienić wszystko — paski…
- [mvrozanti/claude-progressbar](https://github.com/mvrozanti/claude-progressbar) - Paski postępu dla poleceń Bash uruchamianych przez Claude Code, rysowane w jego…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native agent teams. Under control. Hard worker limits, live team visibility…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definiowalne fabryki oprogramowania dla Claude Code na herdr: grafy stacji…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows Pasek stanu PowerShell dla Claude: limity 5-godzinne i tygodniowe z…
- [barnabys-drew/claude-code-statusline](https://github.com/barnabys-drew/claude-code-statusline) - statusLine Claude Code — paski kontekstu i limitu szybkości bezpośrednio z…
- [black-astro/claude-statusline-astro](https://github.com/black-astro/claude-statusline-astro) - Claude Code 상태라인 — 폴더·브랜치·모델·사용량을 한 줄로, 맨 뒤엔 하루 한 번 뽑는 마스코트.
- [Chy-Zaber-Bin-Zahid/claude-code-statusline](https://github.com/Chy-Zaber-Bin-Zahid/claude-code-statusline) - A Claude Code status line with context, 5-hour and weekly usage bars, each in…
- [CosminBd/claude-git-file-tree](https://github.com/CosminBd/claude-git-file-tree) - A git pane for Claude Code: review what Claude changed, read diffs and rendered…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Profesjonalny wiersz stanu Claude Code: czas trwania sesji, koszt w wielu…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod.
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - Rozszerzenie VS Code: postęp zadań Code dla Claude, przewidywany czas…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Podgląd obrazów wewnątrz Claude Code: najedź na znacznik pod odpowiedzią, aby…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Wiersz stanu Code dla Claude: model, paski limitów 5-godzinnego/7-dniowego…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Osobista konfiguracja Claude Code: uprawnienia, pasek stanu, serwery MCP.
- [k-hide10/claude-code-plugins](https://github.com/k-hide10/claude-code-plugins) - Miejsce dystrybucji wtyczek Claude Code (modów, Skill itp.) stworzonych przez…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: przenośna konfiguracja Claude Code — globalne reguły, zestaw…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Wyświetla szczegółowy, oznaczony kolorami pasek stanu dla Claude Code…
- [kpothos/ClaudeKPMods](https://github.com/kpothos/ClaudeKPMods) - Modyfikacje dla Claude Code. sticky-board przypina na ekranie zadania, otwarte…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Dwuwierszowy pasek stanu dla terminalowego agenta programistycznego: katalog…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook linii statusu Claude Code — śledzi użycie tokenów i kontekst między…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Wiersz stanu Code dla Claude z instalatorem dla Linux i Git Bash na Windows.
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Rozbudowany wielowierszowy wiersz stanu dla Claude Code — aktualne limity…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness Nacho dla Claude Code (reguły, tablica, modyfikacje).
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Wielowierszowy wiersz stanu Claude Code: pasek kontekstu, gałąź git, paski…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — wiersz stanu Claude Code dla macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitoruj stan Claude Code z paska menu macOS dzięki wskaźnikom w czasie…
- [pkkid/claude-aitools](https://github.com/pkkid/claude-aitools) - Różne modyfikacje i umiejętności dla mojej konfiguracji Claude Desktop.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Niestandardowy wiersz stanu Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Konfiguracja i mody Code dla Claude, ze wspólnym zestawem komponentów…
- [SatoshiReport/claude-code-cycles](https://github.com/SatoshiReport/claude-code-cycles) - Jak uruchamiamy Claude Code jak zespół inżynieryjny: jedna tablica, chronione…
- [silee-tools/claude-statusline](https://github.com/silee-tools/claude-statusline) - Niezależny od szerokości pionowy HUD statusline dla Claude Code.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [steemandavid/claude-code-statusline](https://github.com/steemandavid/claude-code-statusline) - Custom status line for Claude Code — model, context, and usage stats.
- [Synforger/claude-code-statusline](https://github.com/Synforger/claude-code-statusline) - Statusline dla Claude Code pokazujący na pierwszy rzut oka limity zapytań i…
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - 4-wierszowy wiersz stanu dla Claude Code.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Przenośna konfiguracja Code dla Claude: CLAUDE.md, ustawienia, wiersz stanu…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Uniwersalny wieloprotokołowy StatusLine, samouczący się kontekst i wtyczka…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Śledź użycie kontekstu Claude Code, koszty sesji i resety limitów zapytań…
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - Moje umiejętności, wtyczki i mody Claude Code (marketplace: vladdu).
- [wcampbell-dw/claude-plugins](https://github.com/wcampbell-dw/claude-plugins) - Wtyczki Claude Code: animacje aktywnych subagentów na żywo, pasek statusu Nerd…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Synchronizacja między wieloma maszynami konfiguracji użytkownika Claude Code…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Wiersz stanu Claude Code: folder, gałąź git, model, użycie okna kontekstu i…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detektor degradacji kontekstu 2026 — proaktywny monitor pamięci AI i limitu…
- [ZeroDevi1/claude-usage-bar](https://github.com/ZeroDevi1/claude-usage-bar) - Claude Code / Claude Desktop 用量胶囊状态栏 mod：上下文、5h/7d 限额、费用、窗口卡片与缓存保活.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooki, subagenty i linie stanu Claude Code: kolekcje i narzędzia open source…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Wizualny kreator statusline dla Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code pokazujący bieżące zużycie tokenów i szacowane zużycie…
- [lexfrei/ailine](https://github.com/lexfrei/ailine) - Pasek statusu Claude Code z rzeczywistymi limitami użycia z Anthropic API.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mody dla Claude Code: panele, pasma i towarzysze zbudowani na hakach funkcji.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Przekazuj zadania między sesjami Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - To jest serwer MCP do sterowania MODS, modułowym narzędziem wieloplatformowym…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: znajdź to, o co ponownie i ponownie prosisz Claude Code, i zamień to…
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Biblioteka 3 umiejętności dla Claude Code: session-handoff, session-statusline…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Umiejętność Codex i Claude Code do tłumaczenia modów CK3 za pomocą lokalnego LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mody open source i inne rozszerzenia dla Claude Code.

</details>

<a id="dsh-cordis"></a>

## Ekosystemy wtyczek DSH i Cordis

DeepSeek Harness i Cordis docierają do tego samego miejsca z innego kierunku: dla nich wtyczka jest mechanizmem modów, więc wtyczka w tamtym ekosystemie jest odpowiednikiem moda tutaj.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74474 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **74474**  |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐173746 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **173746** |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100821 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **100821** |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82715 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **82715**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35773 · Go · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **35773**  |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30615 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **30615**  |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25547 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Distilly — przekształcaj sposób, w jaki myślą, w umiejętności wielokrotnego użytku dla dowolnego agenta lub bota. Wcześniej Colleague Skill（原同事 Skill）.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **25547**  |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18556 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **18556**  |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6313 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Rynek wtyczek wewnątrz DeepSeek Harness — przeglądanie, wyszukiwanie, instalacja jednym kliknięciem · Wizualny rynek wtyczek DSH

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6313**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4508 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **4508**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3207 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Odpowiedz mi w HTML — umiejętność agenta, która odpowiada na trudne pytania za pomocą jednostronicowego HTML, który naprawdę da się czytać. Niech AI Agent odpowiada na złożone pytania za pomocą jednej strony HTML.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3207**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3002 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **3002**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2052 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Najlepsza wtyczka DeepSeek Harness do wglądu w kontekst i zarządzania nim, z panelem kontekstu / przeglądarką / paskiem bocznym i poleceniem kontekstu, do statystyk kontekstu, kompozycji, rozbicia, szczegółów ewolucji, zrozumienia, z czego składa się kontekst i jak się rozwija. Kompleksowa wtyczka wizualizacji kontekstu DeepSeek Harness, panel Context oraz przeglądarka i pasek boczny oraz polecenie Context, pozwalające analizować skład kontekstu, ewolucję, kompresję, przycinanie i inne zdarzenia oraz działania.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **2052**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1929 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1929**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1467 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DSH Plugin Radar — radar ekosystemu open source dla wtyczek DeepSeek Harness: ciągłe wyszukiwanie (ponad 21 tys. kandydatów), walidacja środowiska uruchomieniowego k8s (ponad 13 tys. testów), migawki co 15 minut; katalog jest wygenerowanym artefaktem — radar ekosystemu wtyczek DSH open source: ciągłe wyszukiwanie ponad 21 tys. kandydatów, testy środowiska uruchomieniowego k8s na ponad 13 tys. przypadków, migawki co 15 minut; katalog wtyczek jest automatycznie wygenerowanym artefaktem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1467**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1429 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

AI 小说创作软件：把灵感、角色、世界观、大纲、章节写作、审稿和修稿组织成可控流程；提供 Windows/macOS 桌面版，支持本地和在线模型。AI Novel Writing Software: Organizes inspirations, characters, worldbuilding, outlines, chapter drafting, review, and revision into a controllable workflow. Features desktop apps for Windows/macOS, Ollama integration, and a DeepSeek Harness (DSH) plugin preview.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1429**   |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1183 · Go · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1183**   |
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
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Clarklevis1995/dsh-mobile">Clarklevis1995/dsh-mobile</a></b> · ⭐486 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness Mobile 是一个面向 DeepSeek Harness 的原生 iOS 客户端。它通过 dsh-plugin-mobile-gateway 与 Harness 建立 WebSocket 连接，将工作区、会话、实时回复和 Agent 执行轨迹带到 iPhone，同时延续 DeepSeek WebUI 克制、清晰的视觉语言

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Kotlin                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **486**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `android` · `android-app` · `coding-agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-plugin` · `ios`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/clarklevis1995--dsh-mobile/b7ef26df82cda351.png" width="100%" alt="Clarklevis1995/dsh-mobile screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐262 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **262**    |
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
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐205 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Natywna wtyczka DeepSeek Harness (DSH) integrująca TypeSafe Jev lub Decision api takie jak luna jako warstwę decyzyjną System One do wyboru agentów, nadzoru, korekt i zatwierdzeń.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **205**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

面向 DeepSeek Harness 的 Claude Code 风格终端界面，支持 Windows、macOS 与 Linux，兼容透明终端、VS Code 主题和自定义配色。

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
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐185 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wtyczka kopii zapasowej i przywracania DeepSeek Harness (DSH) — eksportuj, importuj, migruj i synchronizuj całą konfigurację DSH, wtyczki, serwery MCP, umiejętności i obszar roboczy. Migracja na inną maszynę jednym kliknięciem.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **185**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐168 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **168**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/franksong2702/dsh-codex-connect">franksong2702/dsh-codex-connect</a></b> · ⭐147 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Use openai-codex models and image generation via ChatGPT OAuth for DeepSeek Harness.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **147**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `chatgpt` · `codex` · `deepseek-harness` · `dsh` · `dsh-plugin` · `gpt-image-2` · `oauth`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/franksong2702--dsh-codex-connect/4cbf6ea0bc489916.jpg" width="100%" alt="franksong2702/dsh-codex-connect screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐142 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **142**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MichengAI/dsh-skills-manager">MichengAI/dsh-skills-manager</a></b> · ⭐142 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DSH Skills Manager — jednolite ładowanie i bezpieczne zarządzanie lokalnymi Agent Skills w DeepSeek Harness · Ładuj i bezpiecznie zarządzaj lokalnymi Agent Skills w DSH

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **142**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/michengai--dsh-skills-manager/da8d2487a70e4bc0.webp" width="100%" alt="MichengAI/dsh-skills-manager screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Duskriver/dsh-opencode-go">Duskriver/dsh-opencode-go</a></b> · ⭐116 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

用于deepseek-harness的opencode-go套餐增强插件。多账号管理、额度UI面板、自动更新模型。An opencode-go subscription enhancement plugin for deepseek-harness — featuring multi-account management, a quota UI panel, and automatic model updates.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **116**    |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/duskriver--dsh-opencode-go/345a83c2d9a3f143.png" width="100%" alt="Duskriver/dsh-opencode-go screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/duskriver--dsh-opencode-go/d75a597695831f54.gif" width="100%" alt="Duskriver/dsh-opencode-go animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐91 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **91**     |
| Ostatni push           | 2026-10-13 |
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
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐89 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Umiejętności i wtyczki You.com do wyszukiwania w sieci, ekstrakcji treści, badań, finansów i odkrywania integracji, pomagające agentom AI budować rozwiązania w oparciu o aktualny kontekst internetowy.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **89**     |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-wsl-workspace-maintainers/dsh-wsl-workspace">dsh-wsl-workspace-maintainers/dsh-wsl-workspace</a></b> · ⭐80 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Obsługa przestrzeni roboczej WSL dla DeepSeek Harness — płynne korzystanie z przestrzeni roboczej WSL, bez potrzeby instalowania kolejnego dsh w WSL; po zainstalowaniu tej wtyczki można bezpośrednio dodać przestrzeń roboczą WSL w GUI. Obsługa przestrzeni roboczej WSL dla DeepSeek Harness — ciesz się płynnym doświadczeniem przestrzeni roboczej WSL bez konieczności instalowania dsh wewnątrz WSL. Po zainstalowaniu tej wtyczki możesz bezpośrednio dodać przestrzeń roboczą WSL z GUI.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **80**     |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-13 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-wsl-workspace-maintainers--dsh-wsl-workspace/252926072330fff2.png" width="100%" alt="dsh-wsl-workspace-maintainers/dsh-wsl-workspace screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐71 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **71**     |
| Ostatni push           | 2026-10-13 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
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
<summary><b>Więcej w tej kategorii</b> <sub>· 67</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Mechanizm ochronny wykonywany przed uruchomieniem dla agentów AI zajmujących…
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Wyselekcjonowana lista najlepszych świetnych wtyczek AI dla asystentów AI, w…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - Sklep, marketplace i centrum wtyczek DeepSeek Harness — ponad 11 000 wtyczek…
- [morluto/jacobian](https://github.com/morluto/jacobian) - Composable mathematics tools for agents.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace: przeglądaj, instaluj i aktualizuj jednym kliknięciem…
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - Ciągle aktualizowane prace badawcze dotyczące grafiki komputerowej, 3DGS i…
- [arcships/rutis](https://github.com/arcships/rutis) - Środowisko uruchomieniowe wtyczek dla oprogramowania, które samo się iteruje…
- [Clarklevis1995/dsh-plugin-mobile-gateway](https://github.com/Clarklevis1995/dsh-plugin-mobile-gateway) - 以websocket为通信方式的dsh网关插件，支持在同一网域内移动端的接入，实现移动端的dsh app.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Aktualny katalog wtyczek DeepSeek Harness — odświeżany co godzinę, codziennie…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Świadome zadań pobieranie kontekstu obszaru roboczego i śledzenie cyklu życia…
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - Wtyczka DeepSeek Harness: deterministyczne profilowanie, czyszczenie i…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Wyselekcjonowany katalog wtyczek DeepSeek Harness (DSH) — ponad 280 wtyczek…
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - Baza wiedzy o tworzeniu wtyczek DeepSeek Harness (dsh): 10-rozdziałowy…
- [songoao25/dsh-bottom-info-bar](https://github.com/songoao25/dsh-bottom-info-bar) - DeepSeek Harness (DSH) plugin: replaces the stats row under the composer with…
- [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) - 【求⭐】🐋DSH Web UI…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Wtyczka DSH: powłoka Git Bash dla wszystkich trybów agentów na Windows…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: wieloplatformowy system agentów do czatów grupowych oparty na…
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - Community GitHub Action for DeepSeek Harness — AI Code Review · CI Diagnosis ·…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Wtyczka WWW DSH: dzienne statystyki użycia tokenów z mapą cieplną aktywności w…
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 插件 · 发送栏一键「优化」提示词草稿：五维诊断 + 改写稿 SSE 流式上屏，可替换 / 复制 /…
- [ArvinQi/dsh-mcp](https://github.com/ArvinQi/dsh-mcp) - DeepSeek Harness 的 MCP 服务器管理插件：可视化界面管理 + 按需热注入，OAuth 鉴权支持，环境变量配置.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Wybrane przez społeczność wtyczki, narzędzia, umiejętności i materiały…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Środowisko uruchomieniowe negocjacji handlowych A2A + wtyczka DeepSeek Harness…
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Panel narzędziowy dla DeepSeek Harness Web: menedżer MCP.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Prawdziwy PowerPoint, nie HTML. Powiedz AI, co ma zawierać prezentacja, a…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - AI debatuje. Kod rozstrzyga. Straty pozostają na stronie.
- [dhicoc/dsh-theme-mineradio](https://github.com/dhicoc/dsh-theme-mineradio) - Kinowy motyw visual-radio ze szkła dla DeepSeek Harness (DSH) Desktop — port…
- [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) - DeepSeek Harness 插件：对话自动沉淀为知识卡，配可检索知识库 + 知识图谱 + 审核中心；SQLite/纯 Markdown…
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - Wtyczka WWW DSH: hierarchiczne drzewo obszaru roboczego na pasku bocznym…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Zamień modele zalogowane w lokalnej aplikacji desktopowej WorkBuddy.
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - Wielowymiarowe ocenianie jakości wtyczek DeepSeek Harness: ocenia repozytorium…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Izolowane testy instalacji i uruchomienia wtyczek DeepSeek Harness: instalują…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Wtyczka doku funkcji DeepSeek Harness: jeden panel do…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Ciągłe testowanie kompatybilności wtyczek DeepSeek Harness: dokładne wydania…
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [jiangnanquan/dsh-ux](https://github.com/jiangnanquan/dsh-ux) - DSH web UI 增强插件 + 无边框 Electron 桌面壳.
- [goodrain/rainskills](https://github.com/goodrain/rainskills) - Rainskills 是一组开源 Agent Skills，让 Codex、Claude Code、Pi Agent、 DeepSeek…
- [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) - DSH Web UI 会话进度插件：输入框停靠区常驻进度条.
- [alone-tree/dsh-skill-mcp-manager](https://github.com/alone-tree/dsh-skill-mcp-manager) - 能力库 (Capability) — one-stop visual management of DSH Skills &amp; MCP: on-demand…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Obszar roboczy z wieloma folderami: pozwala agentowi DSH (DeepSeek Harness)…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Głębokie linki do sesji + pełny eksport sesji (markdown/JSON) + zatwierdzone…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Wtyczka DSH: okno narzędzi Git klasy IDE jako natywna karta dsh-better-sidebar…
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - DSH plugin collection: password auth + trust for dsh web LAN/Tailscale access…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Daj DeepSeek Harness Agent natywne ręce i nogi do obsługi GitHub! Natywnie…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Rodzina wtyczek samodoskonalenia agentów inspirowana Hermesem, stworzona…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Wzorzec weryfikacji wtyczek DeepSeek Harness (dsh) bez zależności — bramki…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Ekosystem wtyczek DeepSeek Harness: 86 wtyczek open source w rodzinie 101…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Wtyczka internetowa DeepSeek Harness (DSH): zakładka paska bocznego…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode w DeepSeek Harness — wtyczka DSH, która zapewnia działanie OpenCode…
- [2861292267/dsh-prompt-forge](https://github.com/2861292267/dsh-prompt-forge) - Ulepszony prompt (Enhance Prompt) WorkBuddy jako wtyczka DeepSeek Harness…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace wtyczek firm trzecich i zabezpieczony menedżer cyklu…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx to zorientowana na człowieka, rozszerzalna desktopowa przestrzeń…
- [cv-superding/dsh-webin](https://github.com/cv-superding/dsh-webin) - Nieoficjalna wtyczka DSH: sterowanie internetowymi interfejsami AI…
- [iluluyu/dsh-ui-outline](https://github.com/iluluyu/dsh-ui-outline) - ChatGPT-style right-edge turn navigation plugin for DeepSeek Harness (dsh) web.
- [lhh010/dsh-input-history](https://github.com/lhh010/dsh-input-history) - DSH Web 输入历史插件：Ctrl+Up / Ctrl+Down 像终端一样召回与切换已发送消息，零核心改动.
- [omdsh-dev/dsh-file-trace](https://github.com/omdsh-dev/dsh-file-trace) - DSH Web UI 文件追踪插件：记录并查看模型读取/写入/编辑的每个文件，带行号内容、终端风逐行 diff（红删绿增蓝改）与 hunk 上下文折叠；支持…
- [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Wtyczka DeepSeek Harness: przekształca błąd aprowizacji ACL piaskownicy Windows…
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Terminy na poziomie wdrożenia dla wywołań narzędzia dsh, które ich nie…
- [fshoocn/cordis-port](https://github.com/fshoocn/cordis-port) - Cordis 核心包的 Python 移植 · 插件化运行时 / 依赖注入 / 事件总线 · Python port of cordis.
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Wtyczka Cordis / DeepSeek Harness — znormalizowane narzędzia GitHub API dla…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [majiayu000/dsh-desk](https://github.com/majiayu000/dsh-desk) - Installable Tauri desktop distribution for DeepSeek Harness with a bundled…
- [elysia395/elysia395](https://github.com/elysia395/elysia395) - elysia395 — Android / Kotlin / DSH plugin developer · 中野三玖推し.

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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

| Język      | Wpisy | Przykładowe projekty                                                                                          |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 376   | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                          |
| JavaScript | 82    | `songoao25/dsh-chatgpt-sub`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`               |
| Python     | 38    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 29    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 14    | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                               |
| Go         | 4     | `mitre/claude-statusline`, `lexfrei/ailine`, `esengine/DeepSeek-Reasonix`                                     |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1     | `Clarklevis1995/dsh-mobile`                                                                                   |
| MDX        | 1     | `jkf87/mod-guide`                                                                                             |
| PowerShell | 1     | `markallisongit/claude-statusline`                                                                            |
| Swift      | 1     | `peaceinitiativemenhadenoil263/claude-status-bar`                                                             |

<sub>Liczone są tylko wpisy, w których określono język. Wpisy dokumentacyjne i dyskusyjne są wyłączone z tej tabeli.</sub>

## Współtworzenie

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Ostatnia aktualizacja · 2026-10-13T15:03:52+08:00</sub>
