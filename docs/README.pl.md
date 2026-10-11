<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Świetne mody Claude">
</p>

<h1 align="center">Świetne mody Claude</h1>

<p align="center"><b>Indeks modów i wtyczek do Claude Code, ocenianych na podstawie dowodów, oraz głębszych zmian w zachowaniu, które wprowadzają.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-595-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <b>Polski</b> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Aktualny indeks** · Ostatnia synchronizacja: `2026-10-12T03:53:55+08:00` (UTC+8)
> · Wpisy: **595** · Dodane w najnowszej aktualizacji: **0** · Języki implementacji: **12**

<sub>Każdy poniższy wpis został automatycznie zebrany, przefiltrowany i ponownie sprawdzony. Żaden z nich nie jest płatną promocją.</sub>

<a id="featured"></a>

## Polecane teraz

<sub>Jeden wpis na kategorię, uszeregowany według oceny dowodów i liczby gwiazdek; ranking jest tworzony ponownie przy każdej aktualizacji. To ranking, a nie rekomendacja — każdy wybór prowadzi do jego pełnej karty poniżej. Preferowane są projekty, które opublikowały zrzut ekranu lub nagranie, aby pasek pozostał wizualny.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9478 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2535 · Python · 👁️ observed</sub>
<sub>Znajdź tokeny-widma. Napraw je. Przetrwaj kompaktowanie. Unikaj pogorszenia jakości kontekstu.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74351 · TypeScript · 👁️ observed</sub>
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
- [Oficjalne: własne repozytoria i informacje o wydaniach Anthropic](#oficjalne-własne-repozytoria-i-informacje-o-wydaniach-anthropic) — **14**
- [Mody: stworzone z użyciem możliwości tworzenia modów](#mody-stworzone-z-użyciem-możliwości-tworzenia-modów) — **464**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150197 · TypeScript · ✅ official · 0 天</summary>

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
| Gwiazdki               | **150197** |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9478 · TypeScript · ✅ official · 2 天</summary>

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
| Gwiazdki               | **9478**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| Gwiazdki               | **8249**   |
| Ostatni push           | 2026-10-09 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6345 · Python · ✅ official · 242 天</summary>

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
| Gwiazdki               | **6345**   |
| Ostatni push           | 2026-02-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| Pierwsze uwzględnienie | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary><b>Więcej w tej kategorii</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Dodano `$.ui.notify` dla modów: wyświetla natywne powiadomienie za pomocą…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Naprawiono przypadki, w których klawisz Esc lub przerwanie podczas hooka…

</details>

<a id="mods"></a>

## Mody: stworzone z użyciem możliwości tworzenia modów

Każdy wpis tutaj pokazuje dowody użycia możliwości, którą Claude Code zyskał w wersji 2.1.287: rysuje za pośrednictwem `ui.render`, posiada panel, pas lub kartę, odczytuje `$.ui.selection()`, uruchamia współpracowników za pomocą `agent.spawn` albo jasno mówi, że jest modem.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2535 · Python · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **2535**   |
| Ostatni push           | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐493 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Społecznościowy katalog publicznych modyfikacji Claude Code (hooków funkcji), skanowanych z GitHub wraz z informacjami, co każda modyfikacja może odczytywać, zapisywać, uruchamiać lub wysyłać przez sieć. Przeglądaj https://mods.aidojo.si/

<sub>🔧 Znaleziono użycie w kodzie: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | JavaScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **493**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐187 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **187**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐137 · TypeScript · 👁️ observed · 7 天</summary>

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
| Gwiazdki               | **137**    |
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
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐80 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Podsumowanie

Claude Code wyświetla obrazy i odtwarza filmy bezpośrednio w terminalu: zrzuty ekranu, nagrania Playwright oraz zsynchronizowane testy QA przed/po. Ghostty i kitty.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                           |
| --------- | ----------------------------------------------------------------- |
| Kategoria | `Mody: stworzone z użyciem możliwości tworzenia modów`            |
| Źródło    | `its own text names a mod API, or it declares the mod capability` |
| Język     | TypeScript                                                        |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **80**     |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐76 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **76**     |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐67 · TypeScript · 👁️ observed · 8 天</summary>

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
| Gwiazdki               | **67**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Podsumowanie

Eksperckie skills, agenci, polecenia, reguły, hooki i style wyjścia dla Claude Code — ciągłość sesji + nowoczesne narzędzia CLI do rzeczywistych przepływów pracy programistycznej

<sub>🔧 Znaleziono użycie w kodzie: `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

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
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 8 天</summary>

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
| Gwiazdki               | **50**     |
| Ostatni push           | 2026-10-03 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Modyfikacje Claude Code: paski postępu planu wyświetlane nad monitem

<sub>🔧 Znaleziono użycie w kodzie: `README.md`</sub>

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
| Pierwsze uwzględnienie | 2026-10-11 |

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
| Ostatni push           | 2026-10-11 |
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
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
| Gwiazdki               | **11**     |
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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

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
| Gwiazdki               | **11**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

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
| Gwiazdki               | **11**     |
| Ostatni push           | 2026-10-05 |
| Pierwsze uwzględnienie | 2026-10-11 |

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

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
| Ostatni push           | 2026-10-08 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
| Gwiazdki               | **7**      |
| Ostatni push           | 2026-10-04 |
| Pierwsze uwzględnienie | 2026-10-11 |

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Podsumowanie

Mody Claude Code: panel zużycia 像素螃蟹 usage-hud + klikalne linki HTML w terminalu i karty kodu HTML do kopiowania jednym kliknięciem html-shelf

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
| Pierwsze uwzględnienie | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
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
<summary><b>Więcej w tej kategorii</b> <sub>· 430</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Modyfikacje Claude i narzędzia do ich tworzenia: najpierw umiejętność…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Środowisko Claude Code, którego używam codziennie, publikowane pod tą nazwą od…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Zmień dach w Claude Mods dla Claude Code: bez modyfikowania pliku binarnego…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cztery modyfikacje Claude Code: Cache Keeper, Recording Mode, Goal Meter i…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Modyfikacje Claude Code od Learning Hacker: przedstaw działanie agenta w…
- [kakha13/claude](https://github.com/kakha13/claude) - Modyfikacje Claude Code, które poprawiają i tłumaczą Twoje prompty, zanim…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mody i umiejętności Claude Code od Nekyia Labs, tworzone i codziennie używane…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Wygląd aplikacji desktopowej dla transkrypcji terminala Claude Code, jako mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel boczny dla Claude Code: podagenci uruchamiani przez sesję, zadania…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Baza wiedzy Obsidian z podanymi źródłami na temat Claude Code mods: jak…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel boczny Claude Desktop (karta Code): wyświetla wszystkie niedokończone i…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Umiejętność ucząca agentów Claude Code tworzenia modów Claude.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Pasek użycia nad polem wejściowym Claude Desktop (karta Code): limit 5h / 7d…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Społecznościowe mody, wtyczki i umiejętności Claude, instalowalne z jednego…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mody Claude (wtyczki z hakami funkcji) dla Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeria modów Baselane: mody Claude Code, sprawdzone i przypięte.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Kolejka decyzji CLI/TUI dla ludzi pracujących z agentami konwersacyjnymi.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Pływająca karta statusu dla Claude Code — model, kontekst, limity szybkości…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mody Claude Code: screen-guard ukrywa nazwy i sekrety podczas udostępniania…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Panel GSD na żywo dla Claude Code: plan działania, drzewo agentów z…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Rozszerzenia Claude Code. Odblokuj pełną moc Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod Claude Code (wtyczka), który dodaje panel boczny z kartami Activity, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panele, zabezpieczenia i mody poprawiające wygodę pracy z Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dwa mody Claude Code nad polem promptu: miernik okna kontekstu, limit 5 godzin…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Wydłuż działanie planu Claude Pro: mody Claude Code zapewniające dokładny HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Odczytuje pliki markdown nazwane przez Claude Code i renderuje je obok sesji;
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Głosowy współpracownik dla Claude Code.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mody Claude Code: typing-speed, prędkościomierz pisania na żywo ze statystykami…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fajerwerki dla Claude Code: każde naciśnięcie klawisza, wywołanie narzędzia…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Odkrywaj mody, wtyczki i rozszerzenia Claude Code dzięki animowanym…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code: diagramy mermaid rysowane bezpośrednio w transkrypcji.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Małe modyfikacje Claude Code (wtyczki function-hook): session-switcher i inne.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code: miniatury wklejonych obrazów nad promptem, w dowolnym terminalu.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mody Claude Code: menu narzędzi Claude, tryb Zen, motywy terminala, sterowanie…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mody Claude Code: mod-scout (znajduje najczęściej używane mody), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dwa mody Claude Code do jednoczesnego uruchamiania wielu sesji: karta kontekstu…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: odkrywaj, sprawdzaj, przełączaj i aktualizuj mody Claude Code.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mody Claude Code: pasek kontekstu, panel agentów, rozmywanie PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Najlepsze mody Claude Code: starannie wybrane, sprawdzone i przypięte.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Wtyczka Claude Code: automatyczne kierowanie do modeli Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sześć modów dla Claude Code: animowana maskotka Clawd, paski limitu użycia i…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Marketplace modów dla Claude Code: debugger krokowy pętli agenta, podpowiedzi…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sześć modyfikacji Claude Code: limity planu i kontekst nad promptem, pomocnik…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Najlepszy kompleksowy pakiet modyfikacji dla Claude Code: limity użycia i HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Odtwarzaj YouTube Shorts w swoim Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Zestaw narzędzi Claude Naren: skills, mody i serwery MCP dla Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code rysujący różnice Edit i Write w dwóch kolumnach obok siebie.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mody dla Claude Code: Clawd, mała pikselowa maskotka odgrywająca to, co robi…
- [reporails/arcade](https://github.com/reporails/arcade) - Klasyczne gry desktopowe jako mody Claude Code, uruchamiane w panelu podczas…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Wyselekcjonowana lista modów Claude Code, instalowanych jako marketplace…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mody Claude Code na żądanie — umiejętność, która odczytuje Twoją rozmowę i…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Bardzo opiniotwórcza wtyczka Claude Code zaprojektowana przez Rustaceana…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mody Claude Code, które pilnują agenta — haki funkcji strzegące zakresu…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Moja kolekcja modyfikacji Claude Code, po jednej modyfikacji w każdym katalogu.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Pasywno-agresywne przypomnienie o piciu wody dla Claude Code.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - The Claude Code mods I use.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Panel macOS notch dla Claude Code: limity użycia, otwarte sesje, postęp zadań…
- [Danovich/turntype](https://github.com/Danovich/turntype) - A typing test for the time while Claude works. A Claude Code mod.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Modyfikacja Claude Code: pasek pamięci podręcznej promptu, następne kroki…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Modyfikacje dla Claude Code: panele, polecenia i hooki zbudowane za pomocą…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Trims huge tool outputs before they fill Claude Code.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code rysujący limity użycia i wydatki na pasku nad promptem.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Modyfikacje Claude Code autorstwa Hermana (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Modyfikacje Claude Code: paski postępu planów, rejestr tego, co Claude…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Zobacz, co Claude Code uruchamia w tle: subagenci, zadania Codex, shelle…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods by MacLeod Labs: streams untangles a session.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notatki terenowe z pierwszego dnia o modach Claude Code na Windows: pasek…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Modyfikacje, które stworzyłem i osobiście używam w swojej konfiguracji Claude…
- [olddonkey/cache-refresher](https://github.com/olddonkey/cache-refresher) - Claude Code mod: shows when the prompt cache expires and what a lapse would…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: bieżące mierniki kosztu, kontekstu i limitu planu nad…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Mod Claude Code, który wstrzymuje rozgałęzianie podagentów, prompty wymagające…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - modyfikacje kodu dla claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code, który włącza lub wyłącza globalne umiejętności, agentów…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Wtyczki (modyfikacje) Claude Code: przełączanie między kilkoma kontami Claude…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Przetestowane modyfikacje Claude Code instalowane jednym poleceniem…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Modyfikacje dla Claude Code: wtyczki zbudowane na hookach funkcji.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Napisy końcowe w stylu filmowym dla sesji programistycznej.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Własny marketplace modyfikacji dla Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Zestaw modyfikacji claude code mojego autorstwa.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modyfikacje Claude Code. touch-map: zobacz jako drzewo i mapę aktywności, które…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Ucz się języka obcego podczas pracy z Claude Code.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Modyfikacje Claude Code do uruchamiania wielu sesji w wielu repozytoriach z…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Podczas pisania przez agenta Java kodu naruszającego standard Java firmy…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Pasek boczny z bieżącym kosztem, liczbą tokenów i użyciem kontekstu dla Claude…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Modyfikacja Claude Code: lista zaległych działań następczych sugerowanych przez…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Goal, tasks and agents above your Claude Code prompt — zero setup.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio internetowe wewnątrz Claude Code: panel boczny cliamp, miniodtwarzacz…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Zabawne i użyteczne modyfikacje Claude Code: pikselowe stworzenie nad promptem…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: modyfikacja Claude Code do projektowania i uruchamiania grafów…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude gotuje. Czatuj ze swoją ekipą. Znajomi online, tuż obok Twojej sesji…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Modyfikacje Claude Code dla prawdziwych inżynierów.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code&#x27;s terminal session recap, in the Claude desktop app&#x27;s Code tab.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Modyfikacja Claude Code all-in-one: HUD na żywo, zabezpieczenia.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Bitwa kosmiczna nad promptem Claude Code podczas jego pracy.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Zobacz, które pliki każdy agent Claude Code ma w swoim kontekście i ile każdego…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Zachowaj zimną krew. Termometr na dni z Claude Code: każda godzina otrzymuje…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Pamięć podręczna promptu, kontekst i limity planu — wszystko na pierwszy rzut…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Małe mody Claude Code do terminala i aplikacji desktopowej.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code mods (plugin marketplace): live sidebar with context, cost and…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Modyfikacja Claude Code: panel postępu zadań, subagentów, przebiegów pracy…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Modyfikacja Claude Code: klikalny, opatrzony znacznikami czasu spis treści…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Modyfikacja Claude Code: limity szybkości planu, zapełnienie kontekstu, koszt…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Umiejętność + mod Claude CLI, który dodaje hiszpańskie słowa do odpowiedzi…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Twoje zdarzenia Alarum nad promptem Claude Code: co właśnie nadeszło i jedno…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Lista zadań Floatee nad promptem Claude Code: uruchamiaj, prowadź i odhaczaj…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Pasek boczny w stylu Evangelion dla Claude Code: kontekst, quota, aktywność…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Modyfikacja Claude Code, która stylizuje go na The Machine z Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod Claude Code do obowiązkowych, zweryfikowanych przepływów…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Modyfikacje open source dla Claude Code: panele, wiersze stanu, powiadomienia…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Modyfikacja Claude Code: osobny panel dla każdego subagenta, plików, których…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesji, postęp Spec Kit na żywo i zarządzanie oknem…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Okno kontekstu jako jeden wiersz nad promptem, narysowane tak, jak Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Panel HUD zadań na żywo dla Claude Code Desktop: pasek nad promptem podczas…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Darmowa, otwartoźródłowa wtyczka dla Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Odkładaj prompty na później i przywracaj je do pola wprowadzania Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Modyfikacja Claude Code wyświetlająca obrazy bezpośrednio w Ghostty i kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Mod Claude, który wyświetla żądania pull GitHub z bieżącej sesji w panelu obok…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Modyfikacja Claude Code: generowanie efektów dźwiękowych z promptów tekstowych…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: a debugger for Claude Code tool calls.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Umiejętności Claude Code: weryfikator faktów w dokumentacji, audytor kodu…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Modyfikacja Claude Code: dzisiejsze wiersze kodu autorstwa Claude — nowe…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Modyfikacja Claude Code: klikalne ścieżki w odpowiedziach — kliknij folder, aby…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Wtyczka Claude Code buddy: towarzysz ASCII nad promptem, który pamięta Twoje…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Modyfikacja Claude Code: routing modeli/wysiłku sterowany przez Jev, kompresja…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Modyfikacje Claude Code: warstwa bezpieczeństwa dla Claude Code — ukrywanie…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - A collection of Claude Code mods.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin i mod Claude Code: AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Kolekcja świetnych modów do Claude Code | 모음집 modów do Claude Code.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Przytulny mod HUD w stylu RPG dla Claude Code.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Modyfikacje Claude Code: panele na żywo i hooki do codziennej pracy.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: modyfikacja Claude Code, która na żądanie odczytuje na głos…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Daj klapsa Claude, gdy coś zepsuje — modyfikacja Claude Code pomagająca…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mody Claude Code: małe wtyczki do aktualizowanych paneli, routingu modeli…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod i wtyczka Claude Code: monitor użycia, licznik tokenów i wiersz stanu.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod Claude Code, który na żywo informuje, które pliki zmienił Claude i…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Modyfikacje Claude Code: karty statystyk sesji nad promptem.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Animowany kot z alfabetu Braille.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Modyfikacja Claude Code: kieruje niedrogą pracę do GLM/Kimi za pośrednictwem…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Pikselowy kot nad promptem Claude Code, który wykonuje testowe połączenie z…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code, który wybiera dobry moment na kompakcję, aby utrzymać małe…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modyfikacje Claude dla Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace wtyczek Claude Code autorstwa anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Uniwersalne modyfikacje dla Claude Code: paski, panele, powiadomienia i hooki.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - My private Claude Code mods.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Statek LGTM Lines przepływa obok po każdej zmianie kodu — moduł Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Limity wykorzystania Claude jako animowana karta zdrowia mieszkańca wioski, z…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Krótkie treningi, gdy Claude pracuje: dzienny cel, serie, odznaki i opcjonalne…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Tablica zużycia dla Claude Code: wydatki według modelu.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Mod Claude Code: podgląd rozbicia okna kontekstu na żywo nad promptem.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing dla Claude Code: Apple Music i Spotify nad poleceniem, z…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mody dla Claude Code: zegar cache, Blast Radius, sugestie, lista zadań, grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Po prostu sowa dla Twojego Claude Code.
- [cesarroger/skill-deck](https://github.com/cesarroger/skill-deck) - A Claude Code mod: keep skills manual-only and switch them on in profiles, per…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Jednowierszowy pasek Claude Code.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Oryginalny silnik Doom z Freedoom, grywalny wewnątrz Claude Code.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Modyfikacja Claude Code, która prowadzi bieżącą listę otwartych kwestii w…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Przejrzyj każdy plik, którego dotyka Claude, jak pull request, bez opuszczania…
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Claude Mods.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code mods: rule-keeper saves your corrections as permanent rules.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi żyjące wewnątrz Claude Code: wykluwa się, zjada kod pisany przez…
- [dbroadhurst/claude-mod-goal](https://github.com/dbroadhurst/claude-mod-goal) - A Goal pane for Claude Code: the overall goal Claude is working toward, why…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - Claude Code Mod to explain commands ran by the agent.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Modyfikacje Claude Code zapisane jako haki funkcji oraz oferujący je…
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - A Claude Code mod: a band above the prompt with Claude news and the breaking or…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: po zablokowaniu wywołania narzędzia przez guard zatrzymuje…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code: zadania działające w tle w jednym widoku, z postępem i…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code: jedna skrzynka odbiorcza na wiadomości od członków zespołu…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code: wyjaśnia blokady piaskownicy i zamienia powtarzające się…
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Claude Code mod: status line with the session.
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Ulubione dla Claude Code: ikony jednym kliknięciem do Twoich poleceń i…
- [Dyarchia/dyarchia](https://github.com/Dyarchia/dyarchia) - Dyarchia: Build and Kanban on every surface.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hej, wyciszyłem to! Precz z diffem, utnij riff, koniec z edycjami i mniejsza…
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods: rewrite-prompt (Ctrl+P rewrites your draft before you send it).
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Mody Code: delete-guard (potwierdzanie usuwania plików) i octopus-crew…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod do Claude Code: użycie subskrypcji (5h / 7d) jako pasek nad polem promptu w…
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods: auto-model-detector routes each prompt to the right model and…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Radar na żywo równoległych gałęzi i drzew roboczych nad promptem: które scalają…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Mody Code (wtyczki function-hook), instalowane za pośrednictwem jednego…
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Modyfikacje Claude Code: context-bar-plus.
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Static supply-chain auditor for Claude Code Mods — local, offline, stdlib-only.
- [hahahahahahahahah6/task-progress-mod](https://github.com/hahahahahahahahah6/task-progress-mod) - Claude Code Mod: live TodoWrite progress bar above the prompt.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Modyfikacja Claude Code: jak długo trwała każda odpowiedź, jak długo myślał…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Mody Code: streamer-mode ukrywa prywatne panele, pasma i wiersz stanu…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Wtyczki function-hook dla Claude Code (modyfikacje).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Modyfikacja Claude Code: przeczekuje pięciogodzinny limit użycia i wysyła za…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Kokpit nad promptem Claude Code. Kaczka odczytuje wskaźniki.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Claude Code mods (function-hook plugins): PR merge follow-through, /clear…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Claude Code mod: live token usage, models and subagents per prompt.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel użycia kontekstu na pasku bocznym: suma, kategorie, przyrost w każdej…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista plików na pasku bocznym: które pliki utworzono, zmodyfikowano lub…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Futrzasty w stylu 8-bitowym.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel boczny „O co pytałem.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Oś czasu na pasku bocznym: na co przeznaczono czas w tej turze.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Panel wymiany tokenów na pasku bocznym: ile tokenów rozmowa główna wysłała do…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Szczera krótka rozmowa claude code: po każdej odpowiedzi Claude cicho mówi, co…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Małe mody dla Claude Code, takie jak nowe polecenia ukośnikowe i panele boczne.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd mieszka w pasku nad twoim promptem Claude Code: odgrywa sesję, pokazuje…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod odczytujący na głos odpowiedzi i powiadomienia z Claude Code za pomocą…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude do odczytywania i dołączania do rozmów między sesjami Claude Code…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mody do Claude Code. PixBar: pikselowe stworzenie nad Twoim promptem, które…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Mody Code (usage-meter, ...).
- [koenrohrer/hearth-band](https://github.com/koenrohrer/hearth-band) - Claude Code mod: a pixel creature per model beside a prompt-cache campfire…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dwie modyfikacje Claude Code: folio, panel plików obok czatu, oraz tint, zmiana…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: wykres na żywo pokazujący, co wie Claude Code.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Nie pozwól, aby twoja uwaga błądziła podczas oczekiwania na odpowiedź Claude…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Modyfikacje Claude Code autorstwa Sanmu — marketplace wtyczek.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Tworzony przez społeczność przewodnik po modyfikacjach Claude Code: przypadki…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod do Claude Code, który pokazuje, co robi Claude, w podtytule karty iTerm2…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Puszysta czarna kotka nad promptem Claude Code.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Modyfikacja Claude Code z przełączanymi profilami uprawnień: bezpieczna baza…
- [Mark-Hickey/claude-nine](https://github.com/Mark-Hickey/claude-nine) - Claude Code mods: Linear + PR watch, cortex mesh toasts, safe repo sync.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Small mods for Claude Code: runner-avatar, a little avatar that runs above your…
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of the agent.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Społecznościowe modyfikacje dla Claude Code: zabezpieczenia, panele i polecenia…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel boczny dla Claude Code: pliki zapisane przez Claude, podziały terminala…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Mod do Claude Code: na podstawie Twojego ostatniego tempa wykorzystania…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Spokojny panel boczny dla Claude Code: co robi ta sesja, jej plan, agenci i…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Przyciemniony czas nad każdym promptem i każdą odpowiedzią w transkrypcji…
- [mmedum/spor](https://github.com/mmedum/spor) - Przywraca to, co Claude Code ukrywa: pliki odczytane przez Claude, uruchomione…
- [mrkshw/cold-cache](https://github.com/mrkshw/cold-cache) - Claude Code mod: warns when a session.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code, który ponownie włącza narzędzia todo dla modeli, które je…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Modyfikacja Claude Code, która czeka na bezpieczną pauzę, a następnie…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: jeden wiersz na zadanie nad promptem z bieżącym zadaniem…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Graj w Connect Four przeciwko AI wewnątrz Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: gdy inny agent programistyczny wykonuje commit w Twoim…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code dla repozytoriów współdzielonych przez kilku agentów AI…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Installe et configure mes mods Claude Code en une commande.
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code mod: flashes the terminal tab while Claude waits on you.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Marketplace modów do Claude Code.
- [netgfx/claude-flow-explainer](https://github.com/netgfx/claude-flow-explainer) - A Claude mod to guide the user step by step on how a flow or code works.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Zabawne, darmowe modyfikacje dla Claude Code, które nigdy nie zużywają tokena.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Zabezpieczenie SQL w Claude Code: pyta przed wykonaniem przez Claude poleceń…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Jeden mod dla Claude Code, Windows i CJK przede wszystkim: podgląd wklejonych…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - Claude Code mods made by the OrbitMap team.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Najlepsze mody Claude Code, posortowane według tego, co dla Ciebie robią.
- [pakornkub/session-insight](https://github.com/pakornkub/session-insight) - Claude Code mod: session usage, skills and agents, with an agent diagram.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dwa mody Claude dla Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Przeklinaj na Claude Code, a rysunkowa dłoń odda cios.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel boczny ze statystykami sesji na żywo dla karty Code aplikacji desktopowej…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Moduły dla Claude Code: safety-guard blokuje destrukcyjne polecenia i dostęp do…
- [ptsnac/claude-session-handoff](https://github.com/ptsnac/claude-session-handoff) - Claude Code mod: session timer and one-click handoff to a fresh context window.
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Modyfikacja Claude Code: aktualny ticker giełdowy, panel /quote, alerty cenowe…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Modyfikacja Claude Code: pasek nad promptem pokazujący wykorzystany kontekst i…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Modyfikacja Claude Code: panel boczny przypinający każdy diagram rysowany przez…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Modyfikacja Claude Code: etap snu, który scala, przepisuje i przycina folder…
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Modyfikacja Claude Code: odrzuca niejasne prompty, zanim zobaczy je Claude, i…
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod: Claude uses your secrets without seeing them.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - A Claude Code mod that keeps secrets out of the session transcript: every key…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Modyfikacja Claude Code: host SSH, pamięć RAM oraz limity użycia 5 h/7 d w…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod dla Claude Code: pompki do zrobienia podczas pracy Claude. Bez tokenów.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - paceline as a Claude Code mod: paces your usage limits in a line above the…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Modyfikacje dla claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: zamienia plan zatwierdzony w trybie planu w aktywną listę…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Starannie wybrana lista modyfikacji Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Tryb bez kosztów: agenty pomocnicze działają na Haiku, a duże pliki i logi są…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ścieżka dźwiękowa lofi, która podąża za sesją: spokój, skupienie, przepływ, a…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Ucz się podczas kodowania przez Claude: po turze, która zmieniła kod, nad…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Nagranie każdej zmiany wprowadzanej przez Claude: odtwórz każdą zmianę…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: nieoficjalny fanowski mod Avengers do Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Modyfikacja Claude Code do wyświetlania nad promptem informacji o kontekście…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Mod Claude Code: kieruj proste tury i subagenty do tańszych modeli, nigdy nie…
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods.
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Claude Code mods, installable as a plugin marketplace: deviation-kernel guards…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - Oryginalny DOOM w panelu Claude Code, bez konieczności instalacji: silnik…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Keep Claude.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Wiadomości commitów jednym kliknięciem dla Claude Code z tańczącą Malenią w…
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — mod Claude Code pokazujący użycie planu Claude.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Małe modyfikacje zmieniające wygląd i dźwięki Claude Code.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Modyfikacja Claude Code, która wyświetla bieżącą sesję w panelu: każdy prompt…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace pluginów Claude Code z modami: pluginy function-hooks, które rysują…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Modyfikacja Claude Code: przepisuje niegotowy prompt w miejscu, wskazując…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Słuchaj odpowiedzi Claude Code, gdy aktualnie czytane zdanie jest podświetlone.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code mod: your context window as Scrooge McDuck.
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code: limit 5h/7d, okno kontekstu, czas pozostały pamięci podręcznej…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Modyfikacja Claude Code: animowany pasek postępu i podsumowanie ukończenia dla…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trzy małe mody Claude Code: sprawdzaj, kiedy Twoi podagenci skończą pracę…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Zmniejsza duże zrzuty ekranu, zanim Claude je odczyta, dzięki czemu długie…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Powiedz „I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Wyświetla sugerowane następne prompty nad polem promptu.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Zadaj Claude pytanie poboczne w panelu obok swojej pracy.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code pings you in Telegram when a task is done or it waits for…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Moje modyfikacje Claude Code.
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - A Claude Code mod: your Godville hero and diary in a sidebar.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Modyfikacje dla Claude Code: pasek limitów użycia (5 godz./tydzień) i panel…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Wtyczka Claude Code: limity użycia Claude Pro/Max wraz z prognozą tempa…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mody dla Claude Code. agent-crew: obserwuj pracę swoich podagentów jako żywą…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Wyświetlanie matematyki LaTeX w tekście i w osobnym widoku, a także…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Tablica zadań na żywo dla Claude Code: planuj przed budowaniem, śledź każde…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Starannie wybrana kolekcja najlepszych zasobów dla najbardziej niesamowitych…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Wtyczka Claude Code pokazująca, co się dzieje — wykorzystanie kontekstu…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Piękna, wysoce konfigurowalna linia statusu dla Claude Code CLI z obsługą…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Wszystkie części promptu systemowego Claude Code, 27 wbudowanych opisów…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI video skill for Claude Code &amp; Codex — cinematic product videos with…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Ponad 45 wskazówek, jak najlepiej wykorzystać Claude Code — od podstaw po…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generuj karuzele Xiaohongshu oraz pary okładek…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Piękny powerline w stylu vim dla Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Przeglądaj różnice wygenerowane przez agenta programistycznego w panelu…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Kompleksowa wtyczka paska stanu dla Claude Code z informacjami o wykorzystaniu…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Twórz modyfikacje dla Claude Code: przechwytuj dowolne żądanie, modyfikuj…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Kompleksowy pulpit statusu dla Claude Code — informacje o sesji, paski limitów…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: śledź ślad węglowy swoich sesji Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Estetyczna linia statusu dla Claude Code autorstwa awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agent do długich sesji odgrywania ról w DeepSeek Harness (wtyczka tawerny DSH)…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Publiczne Skills i modyfikacje Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, modyfikacje, subagenci, hooki, polecenia slash i poradniki dla Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legalne bezpłatne LLM APIs i agenci kodowania — automatycznie aktualizowane…
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - DeepSeek Harness Tavern Plugin - character card roleplay, worldbook management…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Szybki kalkulator kosztów bez zależności oraz konfigurowalny wiersz stanu dla…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Pasek stanu terminala dla sesji Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Wyniki na żywo, terminarze i tabele piłki nożnej dla rozgrywek, które…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Lokalna płaszczyzna sterowania dla Claude Code na Windows i macOS: przełączaj…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, który zmienia agenta kodowania w eksperta od firmware.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Pory modlitw, data hidżry, adhkar, codzienny ajat, post sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Osobista konfiguracja Claude Code, wersjonowana w ~/.claude — agenci…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Pakiet do generowania obrazów i przetwarzania wizualnego dla DeepSeek Harness…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Dwuliniowy statusline truecolor dla Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Pływająca karta przypływów w godzinach szczytu i poza nimi dla DeepSeek…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Zestaw wtyczek dla Claude Code, pi i DeepSeek Harness: HUD paska stanu, pasek…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Przenośny zestaw narzędzi Claude Code dla .NET DDD/Clean Architecture: agenci…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Przenośna globalna konfiguracja Claude Code: niestandardowe umiejętności, hooki…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Wtyczki Claude Code, których używam codziennie: skills i mody uporządkowane…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Nieoficjalne mody karty Code w Claude Desktop — usage-pet: pasmo zużycia z…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace wtyczek i umiejętności Claude Code ułatwiających tworzenie modów do…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Zarządzanie tokenami dla Claude Code: najlepszy model kieruje pracą, a…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Bieżąca statusline fazy przepływu pracy dla Claude Code.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repozytorium modów Awesome Media dla Claude Code.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Prosta i użyteczna konfiguracja statusline dla Claude Code.
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Marketplace de plugins para o Claude Code: mods, skills, agentes, hooks…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Wyświetla wiersz stanu Claude Code z limitami szybkości, bieżącym katalogiem i…
- [eddundead/claude-poker](https://github.com/eddundead/claude-poker) - 8-bit Texas Hold.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Konfigurowalna linia statusu Claude Code dla Linux, WSL, Windows i macOS, z…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Szybki wiersz stanu Rust dla Claude Code — najpierw dane, buforowany git…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Działający pulpit użycia dla Claude Code — podział kontekstu, trafienia pamięci…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Pasek stanu i pasek tokenów dla Claude Code: kontekst, wykorzystanie 5-godzinne…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Wyświetlaj kluczowe informacje o stanie Claude Code, w tym model, kontekst…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Wielowierszowy wiersz stanu Claude Code: wydatki, procent kontekstu, git i…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Pasek stanu z przydatnymi informacjami dla claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Natywne zespoły agentów. Pod kontrolą.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Dodatki Claude Code: kolorowy obserwator kropki statusu karty + dołączony pasek…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definiowalne fabryki oprogramowania dla Claude Code na herdr: grafy stacji…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Wiersz stanu użycia Claude Code dla macOS i Linux, dostępny jako wtyczka…
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code desktop mod: prompt-cache TTL countdown, hit rate and misses.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Niestandardowy statusline dla Claude Code — pasek kontekstu z procentem użycia…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Przejrzysty, informacyjny wiersz stanu dla Claude Code — pokazuje projekt…
- [aubinhaba/claude-code-payment-skills](https://github.com/aubinhaba/claude-code-payment-skills) - Claude Code plugin: code-review skills for payments, consistency, boundaries…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Mod CRT HUD Claude: panel stanu w stylu CRT dla Claude Code, w terminalu i na…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Rynek wtyczek Claude Code z baloo: umiejętności, agent weryfikujący zmiany…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Profesjonalny pasek stanu Claude Code: czas trwania sesji, koszt w wielu…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Uwzględniający subskrypcję wiersz stanu dla Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Rozbudowany terminalowy pasek stanu dla Claude Code — Bun + TypeScript, bez…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Narzędzia, umiejętności i agenci dla Claude Code — na początek pasek statusu…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Niestandardowy statusline Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Rzeczywiste wydatki DeepSeek API dla Claude Code: ponownie wycenia transkrypcje…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Podgląd obrazów wewnątrz Claude Code: najedź na znacznik pod odpowiedzią, aby…
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - My Claude Code setup: mods, skills and plugins.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronizuj zadania do zrobienia Claude z Fizzy.do, aby zapewnić zespołowi…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Śledź stan Claude Code za pomocą kompaktowego pulpitu pokazującego kontekst…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalator środowiska Claude Code: skills, statusline, hooks, permissions oraz…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Wiersz stanu w stylu HUD dla Claude Code — kondycja sieci, TPS, kontekst…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Mały pulpit dla Claude Code: procent kontekstu, odliczanie pamięci podręcznej…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Niestandardowy pasek stanu terminala dla Claude Code: model, katalog, stan git…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Przenośna konfiguracja Claude Code: CLAUDE.md, ustawienia, linia stanu…
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Mod Claude Code desktop (macOS): powiadomienia sesji umożliwiające przejście…
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Pasek stanu śledzenia kosztów w czasie rzeczywistym i monitorowania sesji dla…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Umiejętność Claude Code (VS Code, Windows): podglądy obrazów i przyciski…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Wiersz stanu Claude Code: folder, gałąź git, model, użycie okna kontekstu i…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detektor degradacji kontekstu 2026 — proaktywny monitor pamięci AI i limitu…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooki, subagenty i linie stanu Claude Code: kolekcje i narzędzia open source…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Wizualny kreator statusline dla Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code pokazujący bieżące zużycie tokenów i szacowane zużycie…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mody dla Claude Code: panele, pasma i towarzysze zbudowani na hakach funkcji.
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Claude Code-style UI bundle for the Pi coding agent — tool rendering, spinner…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Przekazuj zadania między sesjami Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - To jest serwer MCP do sterowania MODS, modułowym narzędziem wieloplatformowym…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Umiejętność Codex i Claude Code do tłumaczenia modów CK3 za pomocą lokalnego LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mody open source i inne rozszerzenia dla Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Wiersz stanu Claude Code: wygląd CCometixLine + funkcjonalność HUD Claude.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: znajdź to, o co ponownie i ponownie prosisz Claude Code, i zamień to…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Mod prompt-bar dla Claude Code: limity zużycia, licznik pamięci podręcznej +…

</details>

<a id="dsh-cordis"></a>

## Ekosystemy wtyczek DSH i Cordis

DeepSeek Harness i Cordis docierają do tego samego miejsca z innego kierunku: dla nich wtyczka jest mechanizmem modów, więc wtyczka w tamtym ekosystemie jest odpowiednikiem moda tutaj.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74351 · TypeScript · 👁️ observed · 0 天</summary>

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
| Gwiazdki               | **74351**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100550 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **100550** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐97943 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **97943**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82003 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **82003**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35766 · Go · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **35766**  |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25500 · Python · 🔎 inferred · 19 天</summary>

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
| Gwiazdki               | **25500**  |
| Ostatni push           | 2026-09-22 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18396 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wyselekcjonowana lista wtyczek do DeepSeek Harness (dsh) · wyselekcjonowana lista wtyczek DeepSeek Harness

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **18396**  |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4492 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness（DSH）— mała wielorybica mieszkająca w prawym dolnym rogu interfejsu DSH, która pomaga monitorować saldo konta DeepSeek. Sprężysta i urocza, obsługuje przeciąganie i przyciąganie, odwracanie przy przyciąganiu do lewej krawędzi oraz animację przewijania cyfr. Automatycznie uruchamia się wraz z interfejsem; zaleca się bezpośrednio wywołać instalację dsh

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **4492**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4292 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **4292**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Otwarta baza paska bocznego, obsługująca rejestrację nowych stron paska bocznego przez rozszerzenia firm trzecich. Wbudowane strony renderowania/edycji plików, terminala, czatu bocznego, Git i subagenta ｜ Otwarta baza paska bocznego, obsługuje rejestrowanie nowych stron paska bocznego przez rozszerzenia firm trzecich. Wbudowane renderowanie/edycja plików, terminal, czat boczny, Git i strony subagentów.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **4112**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>animowane nagranie · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

The World's First Virtual Terminal for AI Agents

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3682**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3092 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness Tauri — wersja desktopowa | Instalator ma tylko 8 MB, zero konfiguracji środowiska, wstępnie ustawione wtyczki, Windows / macOS / Linux.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **3092**   |
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
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1995 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1995**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1837 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1837**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1577 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1577**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

<sub>Zasób jest linkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji zezwalającej na redystrybucję.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Oprogramowanie AI do pisania powieści: porządkuje inspiracje, postacie, budowę świata, konspekty, pisanie rozdziałów, recenzowanie i poprawki w kontrolowany przepływ pracy; udostępnia wersje desktopowe dla Windows/macOS oraz obsługuje modele lokalne i online. Oprogramowanie AI do pisania powieści: organizuje inspiracje, postacie, budowę świata, konspekty, tworzenie rozdziałów, recenzowanie i poprawki w kontrolowany przepływ pracy. Oferuje aplikacje desktopowe dla Windows/macOS, integrację z Ollama oraz wersję testową wtyczki DeepSeek Harness (DSH).

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1410**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1172 · Go · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **1172**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1140 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Go                                                                               |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **1140**   |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **705**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **592**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/d-dev0101/open-sea-skin">d-dev0101/open-sea-skin</a></b> · ⭐389 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

🌊 DeepSeek Harness 海洋皮肤与动态主题 | Real-time ocean theme with adjustable waves, sunset & glass opacity. DSH plugin + Chrome/Edge extension; keeps your new-tab homepage.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **389**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `animated-background` · `chrome-extension` · `customization` · `deepseek` · `deepseek-harness` · `deepseek-theme` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/3d9689f0d936d1b0.png" width="100%" alt="d-dev0101/open-sea-skin screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/ccd6ac3920478ffa.gif" width="100%" alt="d-dev0101/open-sea-skin animation"><br><sub>animowane nagranie</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **369**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

ACRYL — Agent Context Relay Yielding Lifecycles. Jeden trwały obszar roboczy, jeden kanoniczny kontekst, dowolny agent programistyczny.

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
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **225**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

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
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cocofhu/anime-find">cocofhu/anime-find</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **176**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `anime` · `anime-search` · `bangumi` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `magnet`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cocofhu--anime-find/4e8000425bf8bf5f.jpg" width="100%" alt="cocofhu/anime-find screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **176**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Delegowanie zadań w czasie dla DeepSeek Harness (dsh): zaplanuj zadania w dogodnej chwili, pozwól im działać bez nadzoru poza godzinami szczytu i wróć po raport. Weryfikacja przez człowieka, komputer stacjonarny i web.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | TypeScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **172**    |
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
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐160 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **160**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐142 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Dowody z wykonania pomagające agentom śledzić i profilować wąskie gardła oraz je usuwać w kodzie aplikacji i natywnym, kernelach GPU oraz stosach inferencji.

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | Python                                                                           |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **142**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **134**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Gwiazdki               | **133**    |
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
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Podsumowanie

Wtyczka DSH · wstrzykiwany optymalizator 0.8 (główna gałąź): mówisz jak zwykle, a po wysłaniu wiadomości i przed jej odebraniem przez AI porządkuje, „czego właściwie potrzeba w tej turze”, po czym przekazuje to rozumienie roboczemu AI (wstrzykiwanie kontekstu) — oryginalne słowa nie są przepisywane, a każda informacja ma dosłowną podstawę. Zawiera interfejs sterowania (poziom/ uprawnienia/model/kontekst/narzędzia tylko do odczytu), nakładkę przechwytującą (warstwa myślenia + warstwa wyników) oraz rzeczywiste zużycie tokenów. Może wyraźnie zwiększyć stabilność działania większości modeli, szczególnie DeepSeek-V4.1-Flash, zapewniając zauważalną poprawę

##### 📌 Podstawowe informacje

| Pole      | Wartość                                                                          |
| --------- | -------------------------------------------------------------------------------- |
| Kategoria | `Ekosystemy wtyczek DSH i Cordis`                                                |
| Źródło    | `declared a mod, plugin or hook, but nothing about the mod surface specifically` |
| Język     | JavaScript                                                                       |

##### 📊 Dane

| Metryka                | Wartość    |
| ---------------------- | ---------- |
| Gwiazdki               | **113**    |
| Ostatni push           | 2026-10-11 |
| Pierwsze uwzględnienie | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Obraz</th><th align="center" width="50%">🎬 Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>nie opublikowano multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b>Więcej w tej kategorii</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Ochrona wykonywana przed uruchomieniem dla agentów AI do kodowania.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Wyselekcjonowana lista najlepszych świetnych wtyczek AI dla asystentów AI, w…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Wtyczka DSH — bezpłatne modele OpenCode Zen dla DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace: przeglądaj, instaluj i aktualizuj jednym kliknięciem…
- [arcships/rutis](https://github.com/arcships/rutis) - Środowisko uruchomieniowe wtyczek dla oprogramowania, które samo się iteruje…
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Desktopowy agent zbudowany na bazie rdzenia Deepseek-Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Aktualny katalog wtyczek DeepSeek Harness — odświeżany co godzinę, codziennie…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Świadome zadań pobieranie kontekstu przestrzeni roboczej i śledzenie cyklu…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Wyselekcjonowany katalog wtyczek DeepSeek Harness (DSH) — ponad 280 wtyczek…
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - 可视化 Agent 编排平台｜基于 DeepSeek Harness，支持 Workflow、Multi-Agent、元编排、MCP 与…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Wtyczka dsh游戏素材大师. Integruje model generowania obrazów seedream i model…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: wieloplatformowy system agentów czatu grupowego oparty na DeepSeek…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Kolekcja wtyczek webowego GUI DSH (DeepSeek Harness) — powiadomienia o…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Wyselekcjonowane przez społeczność wtyczki, narzędzia, umiejętności i materiały…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Wtyczka menedżera serwera MCP dla DeepSeek Harness: strona Ustawienia → MCP…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Środowisko uruchomieniowe negocjacji handlowych A2A + wtyczka DeepSeek Harness…
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Panel narzędzi dla DeepSeek Harness Web: menedżer MCP.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Wtyczka DeepSeek Harness · jedno kliknięcie w pasku wysyłania optymalizuje…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Prawdziwy PowerPoint, nie HTML. Powiedz AI, co ma zawierać prezentacja, a…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Lokalny graf wiedzy o kodzie i środowisko kontekstu dla agentów kodowania, z…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Wtyczka AI do inżynierii wbudowanego C/C++ — umiejętności firmware.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Zamień modele zalogowane w lokalnej aplikacji desktopowej WorkBuddy.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - wtyczka dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Ciągłe testowanie kompatybilności wtyczek DeepSeek Harness: dokładne wydania…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Agresywna kompresja kontekstu dla agentów działających lokalnie.
- [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) - Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Guarded context compaction for DeepSeek Harness (dsh): the LLM proposes…
- [GooDAnDReaDY/dsh-voice](https://github.com/GooDAnDReaDY/dsh-voice) - Voice input for DeepSeek Harness: dictation and voice messages with…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness host plugin that keeps project documents and long-term memory…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) - Native ClineBot / ClinePass provider companion plugin for DeepSeek Harness (DSH).
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Prześwietlenie wtyczek DeepSeek Harness: zadeklarowane możliwości a rzeczywiste…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [GooDAnDReaDY/dsh-lanmode](https://github.com/GooDAnDReaDY/dsh-lanmode) - Mobile gateway and secure local network access for DeepSeek Harness WebUI.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) - Mixture of Agents (MoA) plugin for DeepSeek Harness with /moa slash command…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [chen731215-dev/dsh-muv-table](https://github.com/chen731215-dev/dsh-muv-table) - MUV Variable Table Editor - tavern companion plugin for DeepSeek Harness…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Obszar roboczy z wieloma folderami: pozwala agentowi DSH (DeepSeek Harness)…
- [GooDAnDReaDY/dsh-gitea](https://github.com/GooDAnDReaDY/dsh-gitea) - Gitea/Forgejo toolkit for DeepSeek Harness: issues, PRs, CI, releases…
- [jinhuang712/dsh-survey](https://github.com/jinhuang712/dsh-survey) - Questionnaire-style batch questioning plugin for DeepSeek Harness: 10+…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Wzorzec weryfikacji wtyczek DeepSeek Harness (dsh) bez zależności — bramki…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - Wtyczka DeepSeek Harness (DSH): synchronizacja modeli OpenCode Go jednym…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode w DeepSeek Harness — wtyczka DSH, która zapewnia działanie OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace wtyczek firm trzecich i zabezpieczony menedżer cyklu…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx to oparty na potrzebach ludzi, rozszerzalny pulpit roboczy: rozmowy…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Wyposażony we wszystko agent programistyczny dla DeepSeek Harness — przepływy…
- [GooDAnDReaDY/dsh-tts](https://github.com/GooDAnDReaDY/dsh-tts) - Natural speech synthesis plugin for DeepSeek Harness.
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Nadaj agentowi DeepSeek Harness natywne ręce i nogi do obsługi GitHub! Natywnie…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — społecznościowy zestaw narzędzi do lokalnego wdrażania i…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Permanently delete archived DeepSeek Harness sessions along with their on-disk…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Wtyczka internetowa DeepSeek Harness (DSH): zakładka paska bocznego…
- [tiphareth0/dsh-hardssh](https://github.com/tiphareth0/dsh-hardssh) - Run your work with existing DSH plugins on remote servers, across any number of…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Umożliwia ponowienie próby nieprzypisanej pustej próby modelu — dla tego…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Wtyczki, które sprzątają po sobie: port frameworka wtyczek cordis dla iOS i…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset agenta DeepSeek Harness: Codex i Claude Code jako subagenci delegowani…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Środowisko uruchomieniowe wtyczek Rust z jądrem cyklu życia zweryfikowanym…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Teksty, dyskusje i wideo

Write-ups, discussions and videos about the mod capability.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 382   | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 96    | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 35    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 23    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 15    | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 6     | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 6     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1     | `crafts69guy/claude-statusline.nvim`                                                                          |
| PowerShell | 1     | `GoSlowPoke168/claude-statusline`                                                                             |
| Swift      | 1     | `eovidiu/cordis-ios`                                                                                          |

<sub>Liczone są tylko wpisy, w których określono język. Wpisy dokumentacyjne i dyskusyjne są wyłączone z tej tabeli.</sub>

## Współtworzenie

Corrections are welcome and are the fastest way to improve this list. Open an issue or a pull request if an entry is misfiled, mis-graded, or if a project has been wrongly excluded as a name collision — that last category is where automated filters are most likely to be wrong.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Ostatnia aktualizacja · 2026-10-12T03:53:55+08:00</sub>
