<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Świetne mody Claude">
</p>

<h1 align="center">Świetne mody Claude</h1>

<p align="center"><b>Indeks modów i wtyczek do Claude Code, ocenianych na podstawie dowodów, oraz głębszych zmian w zachowaniu, które wprowadzają.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-508-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <b>Polski</b> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Aktualny indeks** · Ostatnia synchronizacja: `2026-10-11T14:37:28+08:00` (UTC+8)
> · Wpisy: **508** · Dodane w najnowszej aktualizacji: **0** · Języki implementacji: **11**

<sub>Każdy poniższy wpis został automatycznie zebrany, przefiltrowany i ponownie sprawdzony. Żaden z nich nie jest płatną promocją.</sub>

<a id="featured"></a>

## Polecane teraz

<sub>Jeden wpis na kategorię, uszeregowany według oceny dowodów i liczby gwiazdek; ranking jest tworzony ponownie przy każdej aktualizacji. To ranking, a nie rekomendacja — każdy wybór prowadzi do jego pełnej karty poniżej. Preferowane są projekty, które opublikowały zrzut ekranu lub nagranie, aby pasek pozostał wizualny.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9470 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2534 · Python · 👁️ observed</sub>
<sub>Znajdź tokeny-widma. Napraw je. Przetrwaj kompaktowanie. Unikaj pogorszenia jakości kontekstu.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74307 · TypeScript · 👁️ observed</sub>
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
- [Oficjalne: własne repozytoria i informacje o wydaniach Anthropic](#oficjalne-własne-repozytoria-i-informacje-o-wydaniach-anthropic) — **15**
- [Mody: stworzone z użyciem możliwości tworzenia modów](#mody-stworzone-z-użyciem-możliwości-tworzenia-modów) — **373**
- [Ekosystemy wtyczek DSH i Cordis](#ekosystemy-wtyczek-dsh-i-cordis) — **109**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150102 · TypeScript · ✅ official · 0 天</summary>

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
| Gwiazdki               | **150102** |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9470 · TypeScript · ✅ official · 1 天</summary>

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
| Gwiazdki               | **9470**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8246 · Python · ✅ official · 1 天</summary>

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
| Gwiazdki               | **8246**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6338 · Python · ✅ official · 241 天</summary>

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
| Gwiazdki               | **6338**   |
| Ostatni push           | 2026-02-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 1 天</summary>

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
| Gwiazdki               | **1798**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

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
| Gwiazdki               | **25**     |
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
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Międzysesyjny monitoring użycia i kosztów dla profilu webowego DeepSeek Harness — pulpity trendów/map cieplnych, ceny według modeli i godzin szczytu (CNY/USD), oficjalne saldo DeepSeek z uzgadnianiem wydatków.

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
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `billing` · `cordis` · `cost` · `cost-estimation` · `dashboard` · `deepseek` · `deepseek-harness` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/enc-hanted--dsh-pulse/4a81f8e7c5f01f18.png" width="100%" alt="Enc-hanted/dsh-pulse screenshot"></td>
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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Znajdź tokeny-widma. Napraw je. Przetrwaj kompaktowanie. Unikaj pogorszenia jakości kontekstu.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | Python                                                            |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **2534**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐476 · JavaScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **476**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐183 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code: wtyczki oparte na hookach, które dodają dynamiczne wiersze nad poleceniem, zabezpieczenia, panele i gry. Pasek kontekstu, miernik użycia, monitorowanie przeglądu Codex, podgląd Markdown, aktualnie odtwarzany utwór ze Spotify i nie tylko.

<sub>🔧 Znaleziono użycie w kodzie: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **183**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐121 · TypeScript · 👁️ observed · 6 天</summary>

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
| Gwiazdki               | **121**    |
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
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Natywny dla agentów system QA CLI dla stron internetowych. Deterministyczny, bez konieczności pisania testów, bez LLM.

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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐90 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **90**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **74**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐64 · TypeScript · 👁️ observed · 8 天</summary>

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
| Gwiazdki               | **64**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

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
| Gwiazdki               | **59**     |
| Ostatni push           | 2026-10-07 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Podsumowanie

Kolekcja ponad 100 modów, których możesz używać z Claude Code.

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
| Gwiazdki               | **47**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

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
| Gwiazdki               | **46**     |
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animowane nagranie · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

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
| Gwiazdki               | **27**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **23**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animowane nagranie</sub></td>
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

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
| Gwiazdki               | **20**     |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

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
| Gwiazdki               | **11**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

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
| Gwiazdki               | **8**      |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and cost, work streams, and a markdown reader for .planning. Read-only.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **6**      |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/0972519bbd3cad82.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 339</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Modyfikacje Claude i narzędzia do ich tworzenia: najpierw umiejętność…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Harness Claude Code, którego używam na co dzień, publikowany pod tą nazwą od…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Zmień dach w Claude Code za pomocą Claude Mods: bez modyfikowania pliku…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cztery mody Claude Code: Cache Keeper, Recording Mode, Goal Meter i Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mody Claude Code autorstwa Learning Hacker: przedstawiają działanie agenta w…
- [kakha13/claude](https://github.com/kakha13/claude) - Mody Claude Code, które poprawiają i tłumaczą Twoje prompty, zanim przeczyta je…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel boczny dla Claude Code: podagenci uruchamiani przez sesję, zadania…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Baza wiedzy Obsidian o Claude Code mods, z odwołaniami do źródeł: jak działają…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel boczny Claude Desktop (karta Code): wyświetla wszystkie niedokończone i…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mody i umiejętności Claude Code od Nekyia Labs, tworzone i codziennie używane…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Kokpit dla Claude Code: paski planu na żywo, paski subagentów, limity użycia z…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Umiejętność ucząca agentów Claude Code tworzenia modów Claude.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Pasek użycia nad polem wejściowym Claude Desktop (karta Code): limit 5h / 7d…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mody (wtyczki function-hooks) dla Claude Code.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Społecznościowe mody, wtyczki i umiejętności Claude, instalowalne z jednego…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeria modów Baselane: sprawdzone i przypięte mody Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Kolejka decyzji CLI/TUI dla ludzi pracujących z agentami konwersacyjnymi.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Modyfikacja panelu IDE Claude Code: tablica agentów, drzewo plików i…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Pływająca karta statusu dla Claude Code — model, kontekst, limity szybkości…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Modyfikacje Claude Code: screen-guard maskuje nazwy i sekrety podczas…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Rozszerzenia Claude Code. Odblokuj pełną moc Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod Claude Code (wtyczka), który dodaje panel boczny z kartami Activity, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panele, zabezpieczenia i mody poprawiające komfort pracy w Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dwa mody Claude Code nad polem promptu: miernik okna kontekstu, limit…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Twój plan, który sam się obserwuje. Lokalna drzewiasta mapa drogowa na pulpit…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Odczytuje pliki markdown nazwane przez Claude Code i renderuje je obok sesji;
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Głosowy współpracownik dla Claude Code.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mody Claude Code: typing-speed, aktywny prędkościomierz pisania ze statystykami…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fajerwerki dla Claude Code: każde naciśnięcie klawisza, wywołanie narzędzia…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Odkrywaj mody, wtyczki i rozszerzenia Claude Code z animowanymi demonstracjami…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code: diagramy mermaid rysowane bezpośrednio w transkrypcji.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Małe modyfikacje Claude Code (wtyczki function-hook): session-switcher i inne.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code: miniatury wklejonych obrazów nad promptem, w dowolnym terminalu.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mody Claude Code: mod-scout (znajduje najczęściej używane mody), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dwa mody Claude Code do uruchamiania wielu sesji jednocześnie: karta kontekstu…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Modyfikacja Claude Code: natywne sterowanie zawartością automatycznej kompakcji…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Wydłuż działanie planu Pro Claude: mody Claude Code zapewniające dokładny HUD…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow dla Claude Code: spokojna lista kontrolna nad promptem, pokazująca…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Najlepsze mody kodu Claude: starannie wybrane, zweryfikowane, przypięte.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Wtyczka Claude Code: automatyczne kierowanie do modeli Claude.
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
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Bardzo opiniotwórcza wtyczka Claude Code zaprojektowana przez Rustaceana…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Modyfikacje Claude Code, które pilnują agenta — hooki funkcji chroniące zakres…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Moja kolekcja modyfikacji Claude Code, po jednej modyfikacji w każdym katalogu.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Pięć bezpłatnych modyfikacji Claude Code: Simple Mode, Usage Tally, Context…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Modyfikacje Claude Code: pasek kontekstu, panel agentów, rozmywanie PDPA.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Prosto z fabryki. Mod Claude Code: poproś o mem i pracuj dalej.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod dla Claude Code: pasek pamięci podręcznej promptu, kolejne kroki, szybkie…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code rysujący limity użycia i wydatki na pasku nad promptem.
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - Modyfikacja skill-router: Jev wybiera i ładuje umiejętności potrzebne do…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Sklep z modyfikacjami Claude Code wewnątrz Claude Code: użyj /mods, aby…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Modyfikacje Claude Code autorstwa Hermana (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mody Claude Code: paski postępu planów, rejestr tego, co Claude pozostawił…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six Claude Code mods: plan limits and context above the prompt, an allowlist…
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
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Stylizowane odpowiedzi, diagramy na pełną szerokość oraz kontekst i limity…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Podczas pisania przez agenta Java kodu naruszającego standard Java firmy…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Pasek boczny z bieżącym kosztem, liczbą tokenów i użyciem kontekstu dla Claude…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Modyfikacja Claude Code: lista zaległych działań następczych sugerowanych przez…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Komunikaty radiowe Counter-Strike 1.6 dla Claude Code — „Fire in the hole.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio internetowe wewnątrz Claude Code: panel boczny cliamp, miniodtwarzacz…
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Panel macOS notch dla Claude Code: limity użycia, otwarte sesje, postęp zadań…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude gotuje. Czatuj ze swoją ekipą. Znajomi online, tuż obok Twojej sesji…
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - All-in-one Claude Code mod: a live HUD, safety guards.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zobacz, które pliki każdy agent Claude Code ma w swoim kontekście i ile każdego…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Zachowaj zimną krew. Termometr na dni z Claude Code: każda godzina otrzymuje…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Modyfikacja Claude Code: panel na żywo z żądaniami PR GitHub, które sesja…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Małe mody Claude Code do terminala i aplikacji desktopowej.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod: a progress pane for tasks, subagents, workflow runs, the goal…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod: a clickable, timestamped table of contents of the whole…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod: plan rate limits, context fill, session cost and per-task…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Umiejętność + mod Claude CLI, który dodaje hiszpańskie słowa do odpowiedzi…
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Mody Claude.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Modyfikacja Claude Code, która stylizuje go na The Machine z Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Mod do Claude Code: wykonuje compact w odpowiednim momencie.
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Pikselowy towarzysz Naruto dla Claude Code: 20 ninja, 60 jutsu, wykonywanych…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Modyfikacje open source dla Claude Code: panele, wiersze stanu, powiadomienia…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Modyfikacja Claude Code: osobny panel dla każdego subagenta, plików, których…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesji, postęp Spec Kit na żywo i zarządzanie oknem…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Okno kontekstu jako jeden wiersz nad promptem, narysowane tak, jak Claude Code…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Zobacz, co Claude Code uruchamia w tle: subagenci, zadania Codex, shelle…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Darmowa, otwartoźródłowa wtyczka dla Claude Code.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Mod Claude, który wyświetla żądania pull GitHub z bieżącej sesji w panelu obok…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: debugger wywołań narzędzi Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Umiejętności Claude Code: weryfikator faktów w dokumentacji, audytor kodu…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod: today.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod: clickable paths in replies — click a folder to open it in…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Wtyczka Claude Code buddy: towarzysz ASCII nad promptem, który pamięta Twoje…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Wtyczka Claude Code do widoczności narzędzi per agent — ukrywaj i odrzucaj…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin i mod Claude Code: AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Kolekcja świetnych modów do Claude Code | 모음집 modów do Claude Code.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Wtyczki (modyfikacje) Claude Code: przełączanie między kilkoma kontami Claude…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Przetestowane modyfikacje Claude Code instalowane jednym poleceniem…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: modyfikacja Claude Code, która na żądanie odczytuje na głos…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Spank Claude when it messes up — a stress-relief mod for Claude Code: cartoon…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Wykorzystaj Claude Code nawet dwa razy bardziej.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mody Claude Code: małe wtyczki do aktualizowanych paneli, routingu modeli…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod i wtyczka Claude Code: monitor użycia, licznik tokenów i wiersz stanu.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modyfikacje Claude Code. touch-map: zobacz jako drzewo i mapę aktywności, które…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Modyfikacja Claude Code, która podsumowuje nieprzeczytane wiadomości agentów…
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Marketplace wtyczek Claude Code dla modów 0xnicholasy.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Animowany kot z alfabetu Braille.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Modyfikacja Claude Code: kieruje niedrogą pracę do GLM/Kimi za pośrednictwem…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Pikselowy kot nad promptem Claude Code, który wykonuje testowe połączenie z…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code, który wybiera dobry moment na kompakcję, aby utrzymać małe…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modyfikacje Claude dla Claude Code: token-meter.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Statek LGTM Lines przepływa obok po każdej zmianie kodu — moduł Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Twoje limity użycia Claude jako animowana karta zdrowia wieśniaka — moduł…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mody Claude Code dla zespołu S2 (marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Krótkie treningi, gdy Claude pracuje: dzienny cel, serie, odznaki i opcjonalne…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Tablica zużycia dla Claude Code: wydatki według modelu.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Mod Claude Code: podgląd rozbicia okna kontekstu na żywo nad promptem.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing dla Claude Code: Apple Music i Spotify nad poleceniem, z…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Pięć modów Claude Code do jednoczesnego uruchamiania wielu sesji: tablica…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mody dla Claude Code: zegar cache, Blast Radius, sugestie, lista zadań, grill.
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mody do Claude Code: Suggestion Spotlight pokazuje, czego dotyczy sugerowany…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Po prostu sowa dla Twojego Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Jednowierszowy pasek Claude Code.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Oryginalny silnik Doom z Freedoom, grywalny wewnątrz Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - A Claude Code mod that keeps a running list of the open items in a conversation…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi żyjące wewnątrz Claude Code: wykluwa się, zjada kod pisany przez…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods for Claude Code, as a plugin marketplace.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Modyfikacja Claude Code: pokazuje czas przy każdym prompcie i odpowiedzi w…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Modyfikacje Claude Code zapisane jako haki funkcji oraz oferujący je…
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - Mody Claude Code autorstwa divramod: panele na żywo i ulepszenia interfejsu…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: po zablokowaniu wywołania narzędzia przez guard zatrzymuje…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code: zadania działające w tle w jednym widoku, z postępem i…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code: jedna skrzynka odbiorcza na wiadomości od członków zespołu…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code: wyjaśnia blokady piaskownicy i zamienia powtarzające się…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hej, wyciszyłem to! Precz z diffem, utnij riff, koniec z edycjami i mniejsza…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod do Claude Code: użycie subskrypcji (5h / 7d) jako pasek nad polem promptu w…
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Moduły Claude Code z projektowanymi animacjami: monitor na żywo i responsywny…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Radar na żywo równoległych gałęzi i drzew roboczych nad promptem: które scalają…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Mody Claude Code (wtyczki function-hook): pasmo kontekstu, niedokończone…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Kopiowanie linku przez Ctrl+kliknięcie w każdym bloku kodu w odpowiedziach…
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - Moduł jev: $.jev dla Claude Code, typowane osądy z TypeSafe Jev.
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mody do Claude Code: wtyczki hooków, takie jak usage-meter.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Pasek boczny w stylu Evangelion dla Claude Code: kontekst, quota, aktywność…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Wyniki testów w panelu Claude Code: niepowodzenia, ich szczegóły i historia…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Modyfikacja Claude Code: jak długo trwała każda odpowiedź, jak długo myślał…
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod: waits out the 5-hour usage limit and sends &quot;continue&quot; for you.
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
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd mieszka w pasku nad twoim promptem Claude Code: odgrywa sesję, pokazuje…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod odczytujący na głos odpowiedzi i powiadomienia z Claude Code za pomocą…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude do odczytywania i dołączania do rozmów między sesjami Claude Code…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code mod: running subagents as pixel Claude mascots above the prompt.
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - Ściśnij nieaktywne sesje claude code za pomocą haiku — jednoliniowy pasek…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dwie modyfikacje Claude Code: folio, panel plików obok czatu, oraz tint, zmiana…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Panel HUD zadań na żywo dla Claude Code Desktop: pasek nad promptem podczas…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Tworzony przez społeczność przewodnik po modyfikacjach Claude Code: przypadki…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod do Claude Code, który pokazuje, co robi Claude, w podtytule karty iTerm2…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Puszysta czarna kotka nad promptem Claude Code.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Modyfikacja Claude Code z przełączanymi profilami uprawnień: bezpieczna baza…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Społecznościowe modyfikacje dla Claude Code: zabezpieczenia, panele i polecenia…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Spokojny panel boczny dla Claude Code: co robi ta sesja, jej plan, agenci i…
- [mmedum/spor](https://github.com/mmedum/spor) - Przywraca to, co Claude Code ukrywa: pliki odczytane przez Claude, uruchomione…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code, który ponownie włącza narzędzia todo dla modeli, które je…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: jeden wiersz na zadanie nad promptem z bieżącym zadaniem…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Graj w Connect Four przeciwko AI wewnątrz Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: gdy inny agent programistyczny wykonuje commit w Twoim…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code dla repozytoriów współdzielonych przez kilku agentów AI…
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Panel cyberneonowego radia internetowego dla Claude Code — pokrętło synthwave…
- [niksavis/handily](https://github.com/niksavis/handily) - Mody Claude Code pokazujące elementy pracy, zadania i sesje dla dowolnego…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Zabezpieczenie SQL w Claude Code: pyta przed wykonaniem przez Claude poleceń…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Jeden mod dla Claude Code, Windows i CJK przede wszystkim: podgląd wklejonych…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime dla Claude Code: dźwięk, gdy Claude kończy pracę, potrzebuje Twoich…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Najlepsze mody Claude Code, posortowane według tego, co dla Ciebie robią.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Modyfikacja Claude Code, która przechwytuje ryzykowne polecenia powłoki.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dwa mody Claude dla Claude Code: garde-du-corps.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Panel Lazy Panda dla Claude Code: przeglądaj dokumentację bez kiwnięcia łapą.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Przeklinaj na Claude Code, a rysunkowa dłoń odda cios.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel boczny ze statystykami sesji na żywo dla karty Code aplikacji desktopowej…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Moduły dla Claude Code: safety-guard blokuje destrukcyjne polecenia i dostęp do…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods for Claude Code: function-hook plugins that run inside the session…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Modyfikacja Claude Code: aktualny ticker giełdowy, panel /quote, alerty cenowe…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Modyfikacja Claude Code: host SSH, pamięć RAM oraz limity użycia 5 h/7 d w…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod dla Claude Code: pompki do zrobienia podczas pracy Claude. Bez tokenów.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Sklep z modyfikacjami dla Claude Code: pobiera modyfikacje z GitHub, pokazuje…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: zamienia plan zatwierdzony w trybie planu w aktywną listę…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Starannie wybrana lista modyfikacji Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Tryb bez kosztów: agenty pomocnicze działają na Haiku, a duże pliki i logi są…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ścieżka dźwiękowa lofi, która podąża za sesją: spokój, skupienie, przepływ, a…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Ucz się podczas kodowania przez Claude: po turze, która zmieniła kod, nad…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Nagranie każdej zmiany wprowadzanej przez Claude: odtwórz każdą zmianę…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Każdy link wspomniany w Twojej sesji, w jednym wierszu nad promptem.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Minimalne demo funkcji-hooków Claude Code: panel tokenów/kosztów w czasie…
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Claude Code mod for context, growth, quota, cache, native cost and agent…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Przytulny mod HUD w stylu RPG dla Claude Code.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Wiadomości commitów jednym kliknięciem dla Claude Code z tańczącą Malenią w…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Modyfikacja Claude Code: wyświetla użycie planu Claude.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Modyfikacja Claude Code: panel na żywo dla każdego podagenta.
- [Tejas242/airspace](https://github.com/Tejas242/airspace) - Air traffic control for parallel Claude Code sessions: one writer per file…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Modyfikacja Claude Code, która wyświetla bieżącą sesję w panelu: każdy prompt…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace pluginów Claude Code z modami: pluginy function-hooks, które rysują…
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Mod Claude Code: zadokowany panel pokazujący podagentów sesji i ich stan.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Modyfikacja Claude Code: pasmo i panel śledzące subagentów wraz z używanymi…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code: limit 5h/7d, okno kontekstu, czas pozostały pamięci podręcznej…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Modyfikacja Claude Code: animowany pasek postępu i podsumowanie ukończenia dla…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trzy małe mody Claude Code: sprawdzaj, kiedy Twoi podagenci skończą pracę…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Shrinks big screenshots before Claude reads them, so long sessions last longer…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Powiedz „I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Zadaj Claude pytanie poboczne w panelu obok swojej pracy.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace modów Claude Code z instalacją w jednym kroku i przewodnikiem wideo…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Odliczanie do limitów szybkości i prognoza tempa zużycia dla Claude Code.
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Warstwa bezpieczeństwa Roblox Studio dla Claude Code: audyt RemoteEvent…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mody dla Claude Code. agent-crew: obserwuj pracę swoich podagentów jako żywą…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Tablica zadań na żywo dla Claude Code: planuj przed budowaniem, śledź każde…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Stale widoczny pasek nad promptem Claude Code: zapełnienie kontekstu i okna…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Starannie wybrana kolekcja najlepszych zasobów dla najbardziej niesamowitych…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Wtyczka Claude Code pokazująca, co się dzieje — wykorzystanie kontekstu…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Piękna, wysoce konfigurowalna linia statusu dla Claude Code CLI z obsługą…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Wszystkie części promptu systemowego Claude Code, 27 wbudowanych opisów…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Ponad 45 wskazówek, jak najlepiej wykorzystać Claude Code — od podstaw po…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / umiejętność Codex — generowanie karuzel Xiaohongshu oraz par…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Piękny powerline w stylu vim dla Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Przeglądaj różnice wygenerowane przez agenta programistycznego w panelu…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Kompleksowa wtyczka paska stanu dla Claude Code z informacjami o wykorzystaniu…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code i lokalne śledzenie tokenów Codex — pasek statusu.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Twórz mody do Claude Code: przechwytuj dowolne żądanie, modyfikuj dowolną…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Kompleksowy pulpit paska stanu dla Claude Code — informacje o sesji, paski…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: śledź ślad węglowy swoich sesji Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Estetyczny wiersz statusu dla Claude Code autorstwa awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Publiczne umiejętności i modyfikacje Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mody, podagenci, hooki, polecenia ukośnikowe i przewodniki dla Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legalne bezpłatne LLM APIs i agenci kodowania — automatyczna aktualizacja…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Pasek stanu terminala dla sesji Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Wyniki na żywo, terminarze i tabele piłki nożnej dla rozgrywek, które…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Lokalna płaszczyzna sterowania dla Claude Code na Windows i macOS: przełączaj…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Umiejętność agenta, która zmienia Twojego agenta programistycznego w eksperta…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Osobista konfiguracja Claude Code, wersjonowana w ~/.claude — agenci…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Pory modlitw, data hidżry, adhkar, codzienny ajat, post sunnah, Ramadan…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Pasek statusu świadomy sesji dla Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — wtyczka DeepSeek Harness do tematów badawczych…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Two-line truecolor statusline for Claude Code.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Przenośny zestaw narzędzi Claude Code dla .NET DDD/Clean Architecture: agenci…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Zestaw wtyczek dla Claude Code, pi i DeepSeek Harness: HUD paska stanu, pasek…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Przenośna globalna konfiguracja Claude Code: niestandardowe umiejętności, hooki…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Wtyczki Claude Code, których używam codziennie: skills i mody uporządkowane…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram wewnątrz Claude Code: czytaj czaty i kanały w panelu oraz otrzymuj…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace wtyczek i umiejętności Claude Code ułatwiający modyfikowanie gry…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Zarządzanie tokenami dla Claude Code: najlepszy model kieruje pracą, a…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Przeglądarka z podziałem na panele dla Claude Code w Windows Terminal i tmux…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Bieżąca statusline fazy przepływu pracy dla Claude Code.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Nieoficjalne mody karty Code w Claude Desktop — usage-pet: pas wykorzystania z…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repozytorium modów Awesome Media dla Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Ogranicz wydatki na tokeny Claude Code i Codex: kieruj wyszukiwania i…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Prosta i użyteczna konfiguracja statusline dla Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Alerty o limitach użycia dla Claude Code: powiadomienia macOS, ostrzeżenia w…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Konfigurowalna linia statusu Claude Code dla Linux, WSL, Windows i macOS, z…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Szybki wiersz stanu Rust dla Claude Code — najpierw dane, buforowany git…
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Statusline Claude Code z paskiem kontekstu, wykresem tokenów i śledzeniem…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Działający pulpit użycia dla Claude Code — podział kontekstu, trafienia pamięci…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Pasek stanu i pasek tokenów dla Claude Code: kontekst, wykorzystanie 5-godzinne…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Wyświetlaj kluczowe informacje o stanie Claude Code, w tym model, kontekst…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - przyjazna, konfigurowalna statusline dla Claude Code — paski truecolor, około…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Wielowierszowy wiersz stanu Claude Code: wydatki, procent kontekstu, git i…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Pasek stanu z przydatnymi informacjami dla claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Szablon startowy do organizowania wielofirmowego obszaru roboczego Claude Code…
- [spacegrowth/claude-relay](https://github.com/spacegrowth/claude-relay) - Claude Code plugin: a lead session delegates work packets to executor sessions…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Natywne zespoły agentów. Pod kontrolą.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Niestandardowy statusline dla Claude Code — pasek kontekstu z procentem użycia…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Przejrzysty, informacyjny wiersz stanu dla Claude Code — pokazuje projekt…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Rynek wtyczek Claude Code z baloo: umiejętności, agent weryfikujący zmiany…
- [charlie-818/claude-dispatch](https://github.com/charlie-818/claude-dispatch) - Phone control for a fleet of live Claude Code panes — attach to existing iTerm2…
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Wiersz stanu Claude Code: użycie kontekstu, paski limitów 5h/7d, czasy…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Profesjonalny pasek stanu Claude Code: czas trwania sesji, koszt w wielu…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Uwzględniający subskrypcję wiersz stanu dla Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Rozbudowany terminalowy pasek stanu dla Claude Code — Bun + TypeScript, bez…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Wtyczka Claude Code, która pięknie renderuje diagramy Mermaid w transkrypcie…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Narzędzia, umiejętności i agenci dla Claude Code — na początek pasek statusu…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code 커스텀 상태줄 (모델, effort, 컨텍스트, 캐시, 사용량 한도).
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Wtyczka Claude Code: zawsze wyświetla pozostały limit użycia Claude w ciągu 5…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Rzeczywiste wydatki DeepSeek API dla Claude Code: ponownie wycenia transkrypcje…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Wiersz stanu Claude Code z wierszami panelu agentów.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronizuj zadania do zrobienia Claude z Fizzy.do, aby zapewnić zespołowi…
- [J-J-E/claude-kanban](https://github.com/J-J-E/claude-kanban) - A markdown kanban board for Claude Code: cards are files, a board pane, and a…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Wyświetl szczegółowy, oznaczony kolorami pasek stanu dla Claude Code…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu ustawień, wiersz stanu i konfiguracja Claude Code.
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Niestandardowy wiersz stanu Claude Code z oknem kontekstu, śledzeniem użycia…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalator środowiska Claude Code: skills, statusline, hooks, permissions oraz…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Wtyczki i mody Claude Code pomagające zrozumieć, co robi Claude: czytelne…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitoruj stan Claude Code z menu macOS za pomocą wskaźników w czasie…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Kolorowy wielowierszowy pasek stanu dla Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Wiersz stanu Claude Code dla Windows (PowerShell): paski użycia, odliczanie do…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings and Glossary dla Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Niestandardowy wiersz statusu Claude Code.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Przenośna konfiguracja Claude Code: CLAUDE.md, ustawienia, linia stanu…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Śledź wykorzystanie kontekstu Claude Code, koszty sesji i resety limitów…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Zestaw modów dla Claude Code.
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - A hands-on, verified deep-dive into Claude Code — CLAUDE.md, subagents, skills…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Pasek stanu śledzenia kosztów w czasie rzeczywistym i monitorowania sesji dla…
- [wmkeza/claude-plugins](https://github.com/wmkeza/claude-plugins) - wmkeza.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Wtyczka Cordis / DeepSeek Harness — agent prosi człowieka o sekret w wbudowanej…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Trzywierszowy wiersz stanu Claude Code: głębokość kontekstu, limity szybkości…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detektor degradacji kontekstu 2026 — proaktywny monitor pamięci AI i limitu…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooki, subagenty i linie stanu Claude Code: kolekcje i narzędzia open source…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Wiersz stanu Claude Code — wskaźniki użycia Claude/Codex, które pozostają…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Wizualny kreator statusline dla Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code pokazujący bieżące zużycie tokenów i szacowane zużycie…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mody dla Claude Code: panele, pasma i pomocnicy zbudowane na hookach funkcji.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Przekazuj zadania między sesjami Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Jest to serwer MCP do sterowania MODS, modularnym wieloplatformowym narzędziem…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Umiejętność Codex i Claude Code do tłumaczenia modów CK3 za pomocą lokalnego LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mody open source i inne rozszerzenia dla Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: znajdź czynności, o które ponownie prosisz Claude Code, i…

</details>

<a id="dsh-cordis"></a>

## Ekosystemy wtyczek DSH i Cordis

DeepSeek Harness i Cordis docierają do tego samego miejsca z innego kierunku: dla nich wtyczka jest mechanizmem modów, więc wtyczka w tamtym ekosystemie jest odpowiednikiem moda tutaj.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74307 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **74307**  |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100445 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **100445** |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81766 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **81766**  |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐78887 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **78887**  |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35758 · Go · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **35758**  |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30384 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **30384**  |
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
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25477 · Python · 🔎 inferred · 18 天</summary>

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
| Gwiazdki               | **25477**  |
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
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9115 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **9115**   |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8605 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **8605**   |
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
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐7358 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **7358**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/212e73dc2aecbd46.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4441 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **4441**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4276 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Oficjalnie najbardziej polecana wtyczka TUI dla DSH — wysoka wydajność, niskie zużycie zasobów, uroczy pikselowy wieloryb i płynna obsługa myszy. Instalacja jednym poleceniem przez npm. / Oficjalnie najbardziej polecana wtyczka TUI dla DSH — wysoka wydajność, niskie zużycie zasobów, uroczy pikselowy wieloryb i płynna obsługa myszy, instalacja jednym poleceniem przez npm

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **4276**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3150 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3150**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1970 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1970**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1782 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1782**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1463 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DSH Plugin Radar — otwartoźródłowy radar ekosystemu wtyczek DeepSeek Harness: ciągłe wykrywanie (ponad 21 tys. kandydatów), walidacja środowiska uruchomieniowego k8s (ponad 13 tys. testów), migawki co 15 minut; katalog jest wygenerowanym artefaktem — radar otwartego ekosystemu wtyczek DSH: ciągłe wykrywanie ponad 21 tys. kandydatów, ponad 13 tys. testów na poziomie środowiska uruchomieniowego k8s, migawki co 15 minut; katalog wtyczek jest automatycznie wygenerowanym artefaktem

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1463**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1395 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1395**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1169**   |
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
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐703 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **703**    |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐542 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **542**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>animowane nagranie · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">Otwórz wideo</a></sub></td>
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
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Twoja inteligencja, zorkiestrowana. Każdy twórca. Każdy zespół. Każdy agent. Dla każdego.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Go                                                                               |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **351**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐282 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Po prostu otwórz przeglądarkę — wykonaj całą swoją pracę.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **282**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

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
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Time-shifting task delegation for DeepSeek Harness (dsh): plan tasks at leisure, they run unattended off-peak, come back to a report. Human-adjudicated, desktop + web.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **170**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
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
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐158 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **158**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **132**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **132**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐128 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **128**    |
| Ostatni push           | 2026-10-11 |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐121 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Dowody z działania środowiska wykonawczego pomagające agentom śledzić, profilować i usuwać wąskie gardła w kodzie aplikacji i natywnym, kernelach GPU oraz stosach wnioskowania.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **121**    |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐86 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

StudyHub: wtyczka DeepSeek Harness (DSH), która zamienia własne materiały w pytania i powtórki rozłożone w czasie · Wtyczka edukacyjna DSH zamieniająca własne materiały w pytania i powtórki rozłożone w czasie

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **86**     |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐73 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Zdalne sterowanie DeepSeek Harness (dsh web) przez Internet: po instalacji otrzymujesz własny zaszyfrowany adres, dzięki czemu możesz zdalnie korzystać z telefonu także poza domem, bez konieczności korzystania z tej samej sieci LAN/Wi-Fi i bez przekierowania przez NAT; dostępna jest opcja samodzielnego hostowania usługi. Zdalnie steruj DeepSeek Harness (dsh web) z dowolnego miejsca — zaszyfrowany publiczny URL, bez wymogu LAN.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **73**     |
| Ostatni push           | 2026-10-10 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-web` · `pwa`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://cdn.jsdelivr.net/gh/mrRisega/dsh-remote@main/image/phone-mirror.png" width="100%" alt="mrRisega/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 75</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Strażnik wykonywany przed uruchomieniem dla agentów AI do programowania.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Wyselekcjonowana lista najlepszych świetnych wtyczek AI dla asystentów AI, w…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - Znajdź naprawdę odpowiednią dla siebie wtyczkę DeepSeek Harness w 30 sekund.
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - Wyselekcjonowana lista wtyczek, umiejętności, serwerów MCP, warstw…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace: przeglądaj, instaluj i aktualizuj jednym kliknięciem…
- [beancookie/awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin) - Awesome DeepSeek Harness (DSH) Plugin.
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - 终末地官网风格的 DSH Web 主题：奶油纸底、墨黑文字、信号黄强调、全直角工业编辑风.
- [arcships/rutis](https://github.com/arcships/rutis) - Runtime wtyczek dla programów, które działają nieprzerwanie — rdzeń Rust…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Społeczność agregująca wtyczki DeepSeek Harness — automatyczna synchronizacja…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - 基于 Deepseek-Harness 核心底座打造的桌面版 Agent.继承底坐全部能力。并补全 IDE 相关功能.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Aktualny katalog wtyczek DeepSeek Harness — odświeżany co godzinę, codziennie…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Świadome zadań pobieranie kontekstu przestrzeni roboczej i śledzenie cyklu…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Wyselekcjonowany katalog wtyczek DeepSeek Harness (DSH) — ponad 280 wtyczek…
- [hyzyn/dsh-plugin-kit](https://github.com/hyzyn/dsh-plugin-kit) - Plugin family for the DeepSeek Harness (DSH) Web GUI: a pnpm monorepo with a…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Wtyczka dsh游戏素材大师. Integruje model generowania obrazów seedream i model…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zestaw narzędzi Zotero dla DeepSeek harness;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Wtyczka DSH: powłoka Git Bash dla wszystkich trybów agentów w Windows…
- [FeatherHunter/dsh-prompt](https://github.com/FeatherHunter/dsh-prompt) - DeepSeek Harness 的 Prompt 工具箱：别再复制粘贴——24 条深度模板随手点，/prompt 与智能推荐主动兜底，装好即用、可自定义.
- [Andersen216/dsh-whale-girl-live2d](https://github.com/Andersen216/dsh-whale-girl-live2d) - 🐋 鲸鱼娘桌宠 · Whale Girl Live2D —— DSH（DeepSeek Harness）Web 界面里的 Live2D 桌宠：跟着 agent…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: wieloplatformowy system agentów czatu grupowego oparty na DeepSeek…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — oparta na dowodach ewaluacja i obserwowalność promptów, RAG…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Wtyczka webowa DSH: dzienne statystyki użycia tokenów z mapą aktywności w stylu…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Lokalny warsztat pisarski dla chińskich autorów powieści internetowych.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Wyselekcjonowane przez społeczność wtyczki, narzędzia, umiejętności i materiały…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - MCP server manager plugin for DeepSeek Harness: Settings → MCP page, OAuth…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Wtyczka DeepSeek Harness: 15 umiejętności inżynierskich obra/superpowers…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A commerce negotiation runtime + DeepSeek Harness (dsh) plugin.
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - Interfejs zarządzania serwerem MCP dla DeepSeek Harness Web — pływający panel…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Zweryfikowany rynek wtyczek i autonomiczny rejestr dla DeepSeek Harness.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Prawdziwy PowerPoint, nie HTML. Powiedz AI, co ma zawierać prezentacja, a…
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - Wtyczka DeepSeek Harness: leniwy tryb seniora DietrichGebert/ponytail i port…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Zamień zalogowane modele z lokalnej aplikacji WorkBuddy na kompatybilne z…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - One-stop skills, subagent, MCP and LSP manager for DeepSeek Harness (DSH)…
- [xxww0098/dsh-plugin-oauth-subs](https://github.com/xxww0098/dsh-plugin-oauth-subs) - ChatGPT Codex and xAI Grok subscription OAuth for DeepSeek Harness — PKCE /…
- [muyuanjin/dsh-ptc-plus](https://github.com/muyuanjin/dsh-ptc-plus) - A session-bound agent-native REPL for DeepSeek Harness PTC mode.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Ciągłe testowanie kompatybilności wtyczek DeepSeek Harness: dokładne wydania…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Prześwietlenie wtyczek DeepSeek Harness: zadeklarowane możliwości a rzeczywiste…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Wtyczka hosta DeepSeek Harness, która przechowuje dokumenty projektu i pamięć…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - Rynek wtyczek DSH — instalowanie wtyczek społecznościowych jednym kliknięciem w…
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Inteligencja wtyczek DeepSeek Harness stawiająca agentów na pierwszym miejscu…
- [Cyning12/SpecWave](https://github.com/Cyning12/SpecWave) - SpecWave — multi-host coding CLI + P0 gates/Harness (Cursor/Claude/DSH).
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [Fayelin12/dsh-office](https://github.com/Fayelin12/dsh-office) - Agent-office dashboard for DeepSeek Harness (DSH): workspaces, sessions, token…
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Konwersacje głosowe local-first dla DSH.
- [fan56/dsh-topics-memory](https://github.com/fan56/dsh-topics-memory) - Topic memory for LLM agents — edited, not accumulated: a topic keeps the…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Wtyczka DSH: okno narzędziowe Git klasy IDE jako natywna karta…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - Tryb kreatywny oparty na trybie PTC: wtyczka DSH łączy orkiestrację narzędzi…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - Ranking i katalog wtyczek DeepSeek Harness (DSH)｜Ranking / katalog wtyczek…
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Page capability kit for DeepSeek Harness (dsh): terminal dock, file tree…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Obszar roboczy z wieloma folderami: pozwala agentowi DSH (DeepSeek Harness)…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Wtyczka przepływu pracy inżynierskiej dla DeepSeek Harness: etapy zadań…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - Wtyczka DSH do odgrywania ról: karty postaci.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Przeszukiwalny rejestr wtyczek DeepSeek Harness z wyselekcjonowanymi wpisami i…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Wzorzec weryfikacji wtyczek DeepSeek Harness (dsh) bez zależności — bramki…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode w DeepSeek Harness — wtyczka DSH, która zapewnia działanie OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace wtyczek firm trzecich i zabezpieczony menedżer cyklu…
- [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) - Query local log files with Chinese natural-language time expressions…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx to oparty na potrzebach ludzi, rozszerzalny pulpit roboczy: rozmowy…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Wyposażony we wszystko agent programistyczny dla DeepSeek Harness — przepływy…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Wtyczka poprawiająca obsługę wprowadzania w DSH Web: przełączanie klawiszy…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Zapewnia zdalny dostęp do wersji desktopowej DeepSeek Harness w ograniczonym…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — społecznościowy zestaw narzędzi do lokalnego wdrażania i…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Wtyczka internetowa DeepSeek Harness (DSH): zakładka paska bocznego…
- [yu381792/superlcm](https://github.com/yu381792/superlcm) - 五种载体，一座本地对话档案馆：原文归档、分层后台摘要、原文查证与跨工具接续。默认原生压缩，Claude Code 与 dsh harness 可选接管.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Wtyczka DeepSeek Harness: zamienia niepowodzenie provisioningu ACL sandboxa…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Umożliwia ponowienie próby nieprzypisanej pustej próby modelu — dla tego…
- [denceee/dsh-everything-claude-code](https://github.com/denceee/dsh-everything-claude-code) - Adapts everything-claude-code to DeepSeek Harness: 11 skills, an ECC agent…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset agenta DeepSeek Harness: Codex i Claude Code jako subagenci delegowani…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Środowisko uruchomieniowe wtyczek Rust z jądrem cyklu życia zweryfikowanym…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Sklep z wtyczkami dsh — automatyczne wykrywanie na podstawie tematu GitHub i…

</details>

<a id="writing"></a>

## Teksty, dyskusje i wideo

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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

| Język      | Wpisy | Przykładowe projekty                                                                                          |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 307   | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 82    | `Enc-hanted/dsh-pulse`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                    |
| Python     | 40    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 26    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13    | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 6     | `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`, `bunderlog/claude-plugins`                               |
| Rust       | 4     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `arcships/rutis`                             |
| PowerShell | 2     | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| Swift      | 1     | `peaceinitiativemenhadenoil263/claude-status-bar`                                                             |

<sub>Liczone są tylko wpisy, w których określono język. Wpisy dokumentacyjne i dyskusyjne są wyłączone z tej tabeli.</sub>

## Współtworzenie

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Ostatnia aktualizacja · 2026-10-11T14:37:28+08:00</sub>
