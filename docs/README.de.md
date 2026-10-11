<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Hervorragende Claude-Mods">
</p>

<h1 align="center">Hervorragende Claude-Mods</h1>

<p align="center"><b>Das evidenzbasiert bewertete Verzeichnis der Claude-Code-Mods und -Plugins sowie des tiefergehenden Verhaltens, das sie verändern.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-508-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <b>Deutsch</b> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Aktuelles Verzeichnis** · Letzte Synchronisierung: `2026-10-11T14:37:28+08:00` (UTC+8)
> · Einträge: **508** · Mit der letzten Aktualisierung hinzugefügt: **0** · Implementierungssprachen: **11**

<sub>Jeder Eintrag unten wurde automatisch erfasst, gefiltert und erneut überprüft. Nichts davon ist bezahlte Platzierung.</sub>

<a id="featured"></a>

## Auswahl des Augenblicks

<sub>Ein Eintrag pro Kategorie, sortiert nach Evidenzgrad und Sternen und bei jeder Aktualisierung neu berechnet. Eine Rangliste, keine Empfehlung; jede Auswahl führt weiter zur vollständigen Karte unten. Projekte, die einen Screenshot oder eine Aufzeichnung veröffentlicht haben, werden bevorzugt, damit die Leiste visuell bleibt.</sub>

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
<sub>Finde die Geister-Token. Behebe sie. Überlebe die Komprimierung. Vermeide den Verfall der Kontextqualität.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74307 · TypeScript · 👁️ observed</sub>
<sub>🌊 Der ursprüngliche Agent-Harness. Setze intelligente Multiplayer-Schwärme ein, koordiniere autonome Workflows und entwickle konversationelle KI-Systeme. Mit…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Inhalt

- [Was ein Claude-Code-Mod ist](#was-ein-claude-code-mod-ist)
- [Wie Einträge bewertet werden](#wie-einträge-bewertet-werden)
- [Offiziell: Eigene Repositories und Release Notes von Anthropic](#offiziell-eigene-repositories-und-release-notes-von-anthropic) — **15**
- [Mods: mit der Mod-Funktion erstellt](#mods-mit-der-mod-funktion-erstellt) — **373**
- [DSH- und Cordis-Plugin-Ökosysteme](#dsh--und-cordis-plugin-ökosysteme) — **109**
- [Texte, Diskussionen und Videos](#texte-diskussionen-und-videos) — **11**
- [Projekte nach Implementierungssprache](#projekte-nach-implementierungssprache)

## Was ein Claude-Code-Mod ist

Claude Code erhielt in Version 2.1.287 **Mods**: Erweiterungen, die tiefer in das Verhalten eingreifen können als ein Plugin und ihre eigene Benutzeroberfläche zeichnen.

Ein Mod kann sich in `ui.render` einklinken, um eine **Zeile, Leiste, einen Bereich oder eine Karte** rund um die Eingabeaufforderung zu zeichnen, den zuletzt mit `$.ui.selection()` ausgewählten Text lesen, mit `agent.spawn` Teammitglieder starten und einen `Client`-Bereich verwalten. Wenn ein Mod beim Zeichnen scheitert, fällt nur er selbst aus — `ui.fault` verhindert, dass ein defekter Mod die Sitzung beendet.

Diese Liste umfasst Mods, die Plugin- und Hook-Schnittstelle, auf der sie aufbauen, sowie die Entsprechungen in DSH und Cordis. Das weitere Claude Code-Ökosystem wird bewusst **nicht** abgedeckt: Ein Prompt-Paket ist kein Mod.

## Wie Einträge bewertet werden

Die meisten Listen in diesem Bereich behaupten lediglich, was dazugehört. Diese hier zeigt, wie viel tatsächlich überprüft wurde, und ermöglicht anschließend eine entsprechende Filterung. Eine Einstufung beschreibt die Belege, nicht die Qualität des Projekts — ein gut entwickelter Mod, über den bisher niemand geschrieben hat, ist weiterhin `inferred`.

| Bewertung                                                                                      | Bedeutung                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `von Anthropic selbst veröffentlicht`                                                          | Von Anthropic selbst veröffentlicht oder direkt aus dem offiziellen Changelog übernommen.                                                                                                                                               |
| `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität`                      | Der eigene Text nennt einen Teil der Mod-Schnittstelle — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, einen Bereich, eine Leiste oder eine Karte — und beschreibt damit etwas, das gegen die echte API entwickelt wurde. |
| `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` | Bezeichnet sich selbst als Mod, Plugin oder Hook, aber nichts im Text nennt die Mod-Schnittstelle ausdrücklich. Echt, aber unbestätigt.                                                                                                 |
| `allein aufgrund des Vokabulars gefunden`                                                      | Allein aufgrund des Vokabulars gefunden. Aufgenommen, damit der Filter überprüfbar ist, nicht weil der Eintrag als zutreffend gilt.                                                                                                     |

<a id="official"></a>

## Offiziell: Eigene Repositories und Release Notes von Anthropic

Eigene Claude-Code-Repositories von Anthropic sowie die Releases, die die Mod-Oberfläche definiert haben. Aus der Quelle gelesen statt zusammengefasst.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150102 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Zusammenfassung

Claude Code ist ein agentisches Programmierwerkzeug, das in deinem Terminal ausgeführt wird, deine Codebasis versteht und dich durch die Ausführung routinemäßiger Aufgaben, die Erklärung komplexen Codes und die Verwaltung von Git-Workflows schneller programmieren lässt – alles über Befehle in natürlicher Sprache.

<sub>🔧 Im Code gefunden: `feed.xml`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | TypeScript                                                       |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **150102** |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9470 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | TypeScript                                                       |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **9470**   |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8246 · Python · ✅ official · 1 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | Python                                                           |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **8246**   |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6338 · Python · ✅ official · 241 天</summary>

##### 📝 Zusammenfassung

Eine KI-gestützte Sicherheitsprüfungs-GitHub-Action, die Claude verwendet, um Codeänderungen auf Sicherheitslücken zu analysieren.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | Python                                                           |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **6338**   |
| Letzter Push      | 2026-02-11 |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 1 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | Shell                                                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **1798**   |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Zusammenfassung

Zusatzmaterialien für Claude Model Cards

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **25**     |
| Letzter Push      | 2025-12-05 |
| Erstmals gelistet | 2026-10-05 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Zusammenfassung

Claude Mods hinzugefügt: Plugins können nun tieferes Verhalten verändern. „You should know“ hinzugefügt, ein integriertes Mod, bei dem ein Seitenagent dir den Rücken freihält und auf Dinge hinweist, die du oder Claude übersehen könnten. Mit `/plugin enable cc-plugin-you-should-know@builtin` aktivieren (für First-Party-Sitzungen mit aktivierter Telemetrie)

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Zusammenfassung

`$.ui.selection()` für Mods hinzugefügt: Gibt den zuletzt im Vollbildmodus ausgewählten Text zurück und, wenn die Auswahl innerhalb einer Transkriptzeile liegt, diese Zeile. Behoben: Die Schaltfläche eines Mods führte beim Drücken in einer Ansicht, die vor dem Neustart von Claude Code gezeichnet wurde, manchmal die Aktion einer anderen Schaltfläche aus. Behoben: Vollbildsitzungen wurden beim Öffnen des Dialogs für Hintergrundaufgaben mit „unrecoverable interface error“ beendet, wenn ein Plugin oder Mod Zeilen über der Eingabe anzeigte. Behoben: `claude plugin test` meldete Mods aus der Ferne als deaktiviert, obwohl lediglich eine veraltete gespeicherte Einstellung gelesen worden war

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Zusammenfassung

Behoben: Eine Verweigerungs- oder Abfrageregel für einen verschachtelten Teil eines zusammengesetzten Shell-Befehls blieb auf verwalteten Rechnern nicht über die Genehmigung eines benutzerinstallierten Mods hinweg bestehen. Behoben: Installierte Mods wurden in der ersten Sitzung nach einem Upgrade nicht geladen. `agent.spawn` für Teammitglieder hinzugefügt, eine Agenten-ID über Plugin-Hook-Ereignisse hinweg sowie in den Zuständen „idle“ und „waiting“ in `$.agent.list()`. Behoben: Sitzungen wurden mit „unrecoverable interface error“ beendet, wenn ein Wert, den der `ui.render`-Hook eines Mods schrieb, beim Zeichnen einen Fehler in einer Zeile verursachte; die Engine zeichnet nun stattdessen ihre eigene Zeile. Behoben: Rechtsbündiger Inhalt im Bereich oder Band eines Mods wurde unter dem Schließen-Symbol oder `\[-\]` gezeichnet, wh

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Zusammenfassung

`serverToolUses` zum Ergebnis des Hooks `turn.step` eines Mods hinzugefügt: Das Tool ruft API selbst auf (den Advisor), jeweils mit ID, Name, Eingabe, Start und Ende. `ceiling` zur Frage und zum Urteil hinzugefügt, die der Hook `tool.check` eines Mods liest, wobei die Genehmigung benannt wird, die eine Organisation für ein Tool verlangt. Die Typen `ThemeKey` und `Color` zu den Plugin-Hook-Typdefinitionen hinzugefügt, damit ein Editor die Theme-Farben auflistet, die die Darstellung eines Mods benennen kann. Zu `claude plugin validate` hinzugefügt: Jeder Hook, den ein Mod an einer Prüfstelle registriert, wird mit der Information aufgelistet, ob er über ein `.catch` verfügt (`gatingHooks` unter `--json`). Das Ergebnis `turn.step` eines Mods korrigiert.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Zusammenfassung

`prompt.autocomplete` hinzugefügt, ein Ereignis, an das sich ein Mod hängt, um der Autovervollständigungsliste der Prompt-Box eigene Zeilen hinzuzufügen. Prompt-Caching zu `$.model.complete` für Mods hinzugefügt: `prompt` und `system` nehmen Textblöcke entgegen, und `cache: true` auf einem Block cached die Anfrage bis dorthin. Workflow-Agenten zum `agent.spawn`-Mod-Hook hinzugefügt, mit ihrem Lauf und Index, damit ein Mod sie ablehnen kann. Write-, Edit-, NotebookEdit- und LSP-Zeilen sowie einzelne Read-, Grep- und Glob-Zeilen korrigiert, die verbergen, warum ein Mod den Aufruf verweigert hat: Die Zeile zeigt nun den Grund. Einen `config.set`-, `state.set`-, `env.set`- oder `agent.spawn`-Hook eines Mods korrigiert, der ablehnt, nachde

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Zusammenfassung

`isDeferred` zu `$.tool.register` für Mods hinzugefügt: `false` listet das Schema des Tools von Anfang an im Prompt statt hinter der Tool-Suche auf. Einen Mod-Hook für `classic.*`-Ereignisse korrigiert, der übersprungen wurde, während der Plugin-Hooks-Worker neu gestartet wurde, wodurch Settings-Hooks ohne ihn antworten mussten. `claude plugin test` behoben, das bei Mods fehlschlug, die `$.session.append` aufrufen; Tests können die angehängten Zeilen mit dem neuen `mock.session` wieder einlesen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Sitzungsübergreifendes Nutzungs- & Kosten-Observatorium für das DeepSeek Harness Web-Profil — Trend-/Heatmap-Dashboards, Peak-Hour-Preise pro Modell (CNY/USD), offizielles DeepSeek-Guthaben mit Ausgabenabgleich.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic`                               |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **3**      |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `billing` · `cordis` · `cost` · `cost-estimation` · `dashboard` · `deepseek` · `deepseek-harness` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/enc-hanted--dsh-pulse/4a81f8e7c5f01f18.png" width="100%" alt="Enc-hanted/dsh-pulse screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mehr in dieser Kategorie</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `$.ui.notify` für Mods hinzugefügt: sendet über deine eigene…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Behoben: Esc oder ein Interrupt während eines `UserPromptSubmit`-Hooks oder des…

</details>

<a id="mods"></a>

## Mods: mit der Mod-Funktion erstellt

Jeder Eintrag hier belegt die Verwendung der Funktion, die Claude Code in 2.1.287 erhalten hat: Er zeichnet über `ui.render`, besitzt ein Pane, Band oder eine Karte, liest `$.ui.selection()`, startet mit `agent.spawn` Teammitglieder oder bezeichnet sich ausdrücklich als Mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Finde die Geister-Token. Behebe sie. Überlebe die Komprimierung. Vermeide den Verfall der Kontextqualität.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | Python                                                                    |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **2534**   |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐476 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Community-Katalog öffentlicher Claude Code-Mods (Funktions-Hooks), aus GitHub gescannt, einschließlich der Informationen, was jeder Mod lesen, schreiben, ausführen oder über das Netzwerk senden kann. https://mods.aidojo.si/ durchsuchen

<sub>🔧 Im Code gefunden: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `contributing.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **476**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐183 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mods: Plugins auf Basis von Hooks, die Live-Zeilen über dem Prompt, Guards, Panes und Spiele hinzufügen. Kontextleiste, Nutzungsanzeige, Codex Review Watch, Markdown-Vorschau, Spotify Now Playing und mehr.

<sub>🔧 Im Code gefunden: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **183**    |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐121 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Zusammenfassung

Halte den Prompt-Cache von Claude Code während Pausen warm und zeige die geschätzten Kosten vor dem Senden nach einem Kaltstart an.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **121**    |
| Letzter Push      | 2026-10-04 |
| Erstmals gelistet | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Ein agentenorientiertes QA-CLI für Webseiten. Deterministisch, keine Tests zu schreiben, kein LLM.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | HTML                                                                      |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **104**    |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐90 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Skins für Claude Code: Werkzeugzeilen mit Icons, Diff-, Tabellen- und Mermaid-Diagrammkarten, ein Nutzungsband und fünfzehn Themes. /skin wechselt sie live.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **90**     |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

Eine Sammlung von Claude-Code-Mods

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **77**     |
| Letzter Push      | 2026-10-08 |
| Erstmals gelistet | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Farbenfrohe, anpassbare Claude Code-Antworten: Tabellen, Code, Diagramme, Grafiken und Tool-Zeilen in 15 Themes mit Kopierschaltflächen. Ein Claude Code-Mod.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **74**     |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mods von Darrell Wang – Bänder über dem Prompt, null Modell-Tokens. Börsenübersichten für Taiwan／USA + weitere geplant.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | HTML                                                                      |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **65**     |
| Letzter Push      | 2026-10-05 |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐64 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Ein Claude Code-Mod, der ein Live-Agent-Dashboard in dein Terminal bringt: Kontext und Kosten, Berater-Zeitachse, jede Berechtigungsprüfung, Subagent-Karten und Swimlanes.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **64**     |
| Letzter Push      | 2026-10-02 |
| Erstmals gelistet | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Zusammenfassung

Experten-Skills, Agenten, Befehle, Regeln, Hooks und Output Styles für Claude Code – Sitzungskontinuität plus moderne CLI-Werkzeuge für praxisnahe Entwicklungsworkflows

<sub>🔧 Im Code gefunden: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | Shell                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **59**     |
| Letzter Push      | 2026-10-07 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Sammlung von mehr als 100 Mods, die du mit Claude Code verwenden kannst.

<sub>🔧 Im Code gefunden: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **47**     |
| Letzter Push      | 2026-10-03 |
| Erstmals gelistet | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mods: Live-Fortschrittsbalken für Pläne oberhalb des Prompts

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **46**     |
| Letzter Push      | 2026-10-08 |
| Erstmals gelistet | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Sieh zu, wie Claude Code während deiner Arbeit einen kleinen Cartoon erstellt.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **32**     |
| Letzter Push      | 2026-10-02 |
| Erstmals gelistet | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Eine Leiste mit den Prompts deiner Claude Code-Sitzung: Zum Lesen darüberfahren, zum Springen anklicken (Funktions-Hooks / Mods)

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **27**     |
| Letzter Push      | 2026-10-03 |
| Erstmals gelistet | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Eine Aufwertung für Claude Code: ein Live-Cockpit-Bereich, teilbare Themes und ein Pixel-Haustier, das darstellt, was Claude gerade tut

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **23**     |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Xcodes Build, Tests, Konsole und SwiftUI-Previews innerhalb von Claude Code

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **20**     |
| Letzter Push      | 2026-10-02 |
| Erstmals gelistet | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mods: 21 Stile und ein vollständiger Funktionsumfang, den du bei Bedarf für Terminal und Desktop-App aktivierst. · Verpasse Claude mit einem Klick einen neuen Stil und erhalte einen vollständigen Satz bedarfsgesteuert aktivierbarer Funktionen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **20**     |
| Letzter Push      | 2026-10-04 |
| Erstmals gelistet | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Zehn Claude-Code-Mods, Anleitungen für Anfänger, Erstellungs-Prompts, sichere Demos und eine Vorlage zum Erstellen eigener Mods.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **20**     |
| Letzter Push      | 2026-10-02 |
| Erstmals gelistet | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Claude-Code-Mods: usage-band zeigt deine 5-Stunden-/7-Tage-Limits, das Kontextfenster und die Cache-Trefferrate über der Eingabeaufforderung an

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **12**     |
| Letzter Push      | 2026-10-03 |
| Erstmals gelistet | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mods, die die Fragen von Claude leichter lesbar und beantwortbar machen (qa-guide).

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **11**     |
| Letzter Push      | 2026-10-07 |
| Erstmals gelistet | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mod: Kontext in Tokens, 5-Stunden- und Wochenlimits im Vergleich zur Uhrzeit, Countdown für den Prompt-Cache, Sitzungskosten und laufende Agenten – alles in einer Leiste über dem Prompt.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **11**     |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Zehn Open-Source-Mods für Claude Code: Live-Bereiche, Bänder, Statuszeilen und Schutzvorrichtungen für Tool-Aufrufe. Burn Meter, Launch Codes, Session Wrapped, Boss Fight, Code Pet und mehr.

<sub>🔧 Im Code gefunden: `swarm/README.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **11**     |
| Letzter Push      | 2026-10-03 |
| Erstmals gelistet | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Zusammenfassung

Zwei Claude-Code-Mods: Codex-Computer-Use-Bridge und koordinierte Claude-Sitzungen. Quelltext, Build-Prompts, Einrichtung und Tests.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **11**     |
| Letzter Push      | 2026-10-05 |
| Erstmals gelistet | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Animierte Pixelgrafik über deiner Claude-Code-Eingabeaufforderung, die reagiert, während Claude arbeitet. Sieben Szenen oder dein eigenes Bild bzw. GIF. Keine Tokens.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **10**     |
| Letzter Push      | 2026-10-04 |
| Erstmals gelistet | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

Eine Benutzeroberfläche für deine Claude-Code- und Codex-Terminals, die deine Agenten erstellen, sodass das einzige Modell in deinem Kopf deines ist.

<sub>🔧 Im Code gefunden: `CLAUDE.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **9**      |
| Letzter Push      | 2026-10-08 |
| Erstmals gelistet | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

KOZMOS – Live-Visual-Mods für Claude Code (CLI + Desktop): Leisten über der Eingabeaufforderung, Seitenleisten, Status-Ticker, Begleiter, Schutzfunktionen und Sound.

<sub>🔧 Im Code gefunden: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **9**      |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

##### 📝 Zusammenfassung

Als Mods entwickelte Sitzungs-Tracker für Claude Code: Kontextfenster, Verbrauchsrate des Plan-Kontingents und Kosten pro Durchlauf

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **8**      |
| Letzter Push      | 2026-09-15 |
| Erstmals gelistet | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Sechs Claude Code-Mods in einem Plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) mit Schaltern pro Mod, plus ein Mods-vs-Hooks-Bericht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **8**      |
| Letzter Push      | 2026-10-04 |
| Erstmals gelistet | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Zusammenfassung

Sammlung von Claude Code-Mods von 개발동생. Taxi-Paket: Taxameter, Navigation, Geschwindigkeitsüberwachungskamera, Dashcam

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **7**      |
| Letzter Push      | 2026-10-04 |
| Erstmals gelistet | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Ansehen auf youtube.com</a> · Die Wiedergabe wird auf der Host-Website geöffnet; GitHub kann sie nicht inline einbetten</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Markdown, das während der Eingabe in das Prompt-Feld von Claude Code gezeichnet wird. Abgetrennter Code wird als Karte mit Syntaxhervorhebung dargestellt, noch bevor du den Fence schließt.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **7**      |
| Letzter Push      | 2026-10-03 |
| Erstmals gelistet | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mods: 像素螃蟹用量面板 usage-hud + im Terminal anklickbare HTML-Links und Codekarten mit Ein-Klick-Kopieren html-shelf

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **7**      |
| Letzter Push      | 2026-10-08 |
| Erstmals gelistet | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Mods für Claude Code: Function-Hook-Plugins, die Live-Bereiche und Verhalten zur Terminal-Oberfläche hinzufügen

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **6**      |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Live-GSD-Dashboard für Claude Code: Roadmap, Agentenbaum mit Verzweigungen, Kontext und Kosten, Arbeitsströme sowie ein Markdown-Reader für .planning. Nur lesbar.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **6**      |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/0972519bbd3cad82.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mehr in dieser Kategorie</b> <sub>· 339</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods und die Werkzeuge zu ihrer Erstellung: zuerst ein Builder-Skill…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Das Claude Code-Harness, das ich täglich ausführe, seit dem ersten Tag unter…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Gib Claude Code mit Claude Mods ein neues Dach: Ändere die Binärdatei nicht…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Vier Claude-Code-Mods: Cache Keeper, Recording Mode, Goal Meter und Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Claude-Code-Mods von Learning Hacker: Die Arbeitsweise des Agenten verständlich…
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code-Mods, die deine Prompts korrigieren und übersetzen, bevor Claude…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Ein Seitenbereich für Claude Code: die Subagenten, die eine Sitzung ausführt…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Mit Quellen belegte Obsidian-Wissensdatenbank über Claude-Code-Mods: wie sie…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop-Seitenleistenbereich (Code-Tab): listet alle unerledigten und…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code-Mods und Skills von Nekyia Labs, erstellt und täglich genutzt von…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Ein Cockpit für Claude Code: Live-Planbalken, Subagenten-Leisten…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Fähigkeit, die Claude-Code-Agenten beibringt, Claude-Mods…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Nutzungsleiste über dem Eingabefeld von Claude Desktop (Code-Tab)…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (Function-Hooks-Plugins) für Claude Code.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-Mods, -Plugins und -Skills, über einen einzigen Marktplatz…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Die Baselane-Mods-Galerie: überprüfte und angeheftete Claude Code-Mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Eine Entscheidungswarteschlange CLI/TUI für Menschen, die mit…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE-Pane-Mod: Agenten-Board, Dateibaum und HWP/PDF-Viewer…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Eine schwebende Statuskarte für Claude Code – Modell, Kontext, Ratenlimits…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude-Code-Mods: screen-guard maskiert Namen und Geheimnisse während der…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude-Code-Erweiterungen. Erschließe die volle Leistungsfähigkeit von Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code-Mod (Plugin), das einen Seitenbereich mit den Tabs Activity, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Bereiche, Leitplanken und Komfort-Mods für Claude Code: Kontext, Nutzung…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Zwei Claude Code-Mods über dem Eingabefeld: Kontextfensteranzeige…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Dein Plan, der sich selbst überwacht. Lokaler Desktop-Roadmap-Baum, den Claude…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lies die Markdown-Dateien, die Claude Code benennt, neben der Sitzung…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Sprach-Coworker für Claude Code. Besprich Dinge mit einem 3D-Wolf, der von…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude-Code-Mods: typing-speed, ein Live-Tachometer für die Tippgeschwindigkeit…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Feuerwerk für Claude Code: Jeder Tastendruck, jeder Tool-Aufruf, jeder Commit…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Entdecken Sie Claude Code-Mods, Plugins und Erweiterungen mit animierten Demos…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code-Mod: Mermaid-Diagramme inline im Transkript gezeichnet.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Kleine Claude Code-Mods (Function-Hook-Plugins): session-switcher und mehr.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code-Mod: eingefügte Bild-Thumbnails über dem Prompt, in jedem Terminal.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude-Code-Mods: mod-scout.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Zwei Claude-Code-Mods zum gleichzeitigen Ausführen vieler Sitzungen: eine…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Claude-Code-Mod: Inhalt der automatischen Kompaktierung nativ über die TUI…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Lass den Claude Pro-Tarif länger laufen: Claude Code-Mods für ein genaues…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow für Claude Code: eine ruhige Checkliste über dem Prompt, die Plan…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Beste Claude-Code-Mods: handverlesen, validiert, angeheftet.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude-Code-Plugin: automatisches Routing des Claude-Modells.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sechs Mods für Claude Code: animiertes Clawd-Maskottchen, Nutzungsbegrenzungs…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Ein Marktplatz für Mods für Claude Code: ein Step-Debugger für die…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude-Code-Mods: Claude-Tools-Menü, Zen-Modus, Terminaldesigns, Steuerungen…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Das beste All-in-one-Mod-Paket für Claude Code: Nutzungsgrenzen und…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Spiele YouTube Shorts in deinem Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Narens Claude-Toolkit: Skills, Mods und MCP-Server für Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude-Code-Mod, der Edit- und Write-Diffs in zwei nebeneinanderliegenden…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods für Claude Code: Clawd, ein winziges Pixel-Maskottchen, das darstellt, was…
- [reporails/arcade](https://github.com/reporails/arcade) - Klassische Desktopspiele als Claude Code-Mods, die in einem Bereich gespielt…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Eine kuratierte Liste von Claude Code-Mods, installierbar als…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Ein sehr meinungsstarkes Claude Code Plugin, entworfen von einem Rustacean, der…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code-Mods, die einen Agenten auf Kurs halten — Function-Hooks, die den…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Meine Sammlung von Claude Code-Mods, ein Mod pro Verzeichnis.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Fünf kostenlose Claude Code-Mods: Simple Mode, Usage Tally, Context Handoff…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code-Mods: Kontextleiste, Agenten-Panel, PDPA-Unschärfe.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Frisch aus der Fabrik. Ein Claude Code-Mod: Bitte um ein Meme und arbeite…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod für Claude Code: Prompt-Cache-Leiste, nächste Schritte…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Ein Claude Code-Mod, der deine Nutzungslimits und Ausgaben in der Leiste über…
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - Der skill-router-Mod: Jev wählt die für jeden Prompt benötigten Skills aus und…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Ein App Store für Claude Code-Mods, innerhalb von Claude Code: /mods zum…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Hermans Claude Code Mods (Marktplatz herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code-Mods: Fortschrittsbalken für Pläne, ein Protokoll dessen, was…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sechs Claude-Code-Mods: Planlimits und Kontext über dem Prompt, ein Coach für…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Feldnotizen vom ersten Tag zu Claude Code-Mods auf Windows: eine…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods, die ich erstellt habe und persönlich in meiner Claude Code-Umgebung…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-Mod: Live-Kosten-, Kontext- und Plan-Kontingentanzeigen über dem…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Ein Claude-Code-Mod, der Subagenten-Verteilung, Prompts mit umfangreichem…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods für claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Ein Claude-Code-Mod, der deine globalen Skills, Agents, Regeln und Tools pro…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods für Claude Code: Plugins auf Basis von Funktions-Hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Filmähnlicher Abspann für deine Coding-Sitzung.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Eine Reihe von claude code-Mods, die ich erstellt habe.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Ein auf cliamp basierender YouTube-Player innerhalb von Claude Code.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code-Mods: Agentenflotten-Dashboard und Autopilot (local-mods-Marktplatz).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude-Code-Mods von vynnlee. Ein Ordner pro Mod, aus einem Marktplatz…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Lerne eine Fremdsprache, während du mit Claude Code arbeitest.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Thematisierte Antworten, Diagramme über die volle Breite sowie Kontext und…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Wenn ein Agent Java schreibt, können Codezeilen, die gegen Alibabas Java-Regeln…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Seitenleiste für Live-Kosten, Token- und Kontextnutzung in Claude Code: ein…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code Mod: ein Backlog der Follow-ups, die Claude über alle Sessions…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Counter-Strike-1.6-Funksprüche für Claude Code – „Fire in the hole“ beim…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internetradio in Claude Code: eine cliamp-Seitenleiste, Mini-Player, Favoriten…
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS-Notch-Dashboard für Claude Code: Nutzungslimits, offene Sitzungen…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude kocht. Chatten Sie mit Ihrem Squad.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - All-in-one Claude Code mod: a live HUD, safety guards.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Sieh, welche Dateien jeder Claude Code-Agent in seinem Kontext hat und wie viel…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Behalte einen kühlen Kopf. Ein Thermometer für deine Claude-Code-Tage: Jede…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code Mod: ein Live-Bereich der GitHub PRs, die eine Session öffnet oder…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-Mods für das Terminal und die Desktop-App.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude-Code-Mod: Ein Fortschrittsbereich für Aufgaben, Subagenten…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude-Code-Mod: Ein anklickbares, mit Zeitstempeln versehenes…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude-Code-Mod: Planratenlimits, Kontextauslastung, Sitzungskosten und Tokens…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-Skill + Mod, der spanische Wörter in Agentenantworten einfügt.
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Claude Mods.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Ein Claude Code-Mod, das es als The Machine aus Person of Interest neu…
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Claude-Code-Mod: führt zum richtigen Zeitpunkt eine Komprimierung durch.
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Ein Pixel-Art-Naruto-Begleiter für Claude Code: 20 Ninja, 60 Jutsu, ausgeführt…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-Source-Mods für Claude Code: Bereiche, Statuszeilen, Toasts, Tool-Wächter…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Ein Claude Code-Mod: ein Bereich für jeden Subagenten, die von ihm berührten…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code-Mod: Sitzungsstatus, Live-Spec Kit-Fortschritt und…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Das Kontextfenster als eine Zeile über der Eingabeaufforderung, dargestellt so…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Sieh, was Claude Code im Hintergrund ausführt: Subagenten, Codex-Jobs, Shells…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Ein kostenloses, quelloffenes Plugin für Claude Code.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Ein Claude-Mod, der die GitHub Pull Requests der Sitzung in einem Bereich neben…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: ein Debugger für Claude-Code-Werkzeugaufrufe.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-Skills: ein Faktenprüfer für Dokumentation, ein Code-Auditor, ein…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod: today.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude-Code-Mod: Anklickbare Pfade in Antworten – auf einen Ordner klicken, um…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-Buddy-Plugin: ein ASCII-Begleiter über deiner Eingabeaufforderung…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code-Plugin für die Sichtbarkeit von Tools pro Agent — Subagenten…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-Plugin und -Mod: ein AI-nativer SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Sammlung großartiger Claude Code-Mods | Sammlung von Claude-Code-Mods.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code-Plugins (Mods): Wechsle zwischen mehreren Claude-Konten, beobachte…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Getestete Claude Code-Mods mit Installation per einem Befehl…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: ein Claude Code-Mod, der Claudes Antworten und deine Prompts auf…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Versohle Claude, wenn es Mist baut – ein Stressabbau-Mod für Claude Code…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Mit deinem Claude-Code-Verbrauch bis zu doppelt so weit kommen.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude-Code-Mods: kleine Plugins für Live-Bereiche, kostenbewusstes…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude-Code-Mod und -Plugin: Nutzungsmonitor, Token-Tracker und Statuszeile.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude-Code-Mods. touch-map: Sieh als Baum und Aktivitätskarte, welche Dateien…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Ein Claude-Code-Mod, der ungelesene Agentennachrichten in einfachem Englisch…
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Claude-Code-Plugin-Marktplatz für die Mods von 0xnicholasy.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Eine animierte Braille-Katze über der Claude Code-Eingabeaufforderung.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude-Code-Mod: Leitet kostengünstige Aufgaben über einen untergeordneten…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Eine Pixelkatze über deinem Claude-Code-Prompt, die einen Testanruf mit einem…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Ein Claude Code-Mod, der einen geeigneten Zeitpunkt für die Komprimierung…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude-Mods für Claude Code: Token-Anzeige.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Das LGTM-Lines-Schiff segelt nach jeder Codeänderung vorbei — ein…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Deine Claude-Nutzungslimits als animierte Dorfbewohner-Gesundheitskarte — ein…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code-Mods für das S2-Team (der ather-Marktplatz).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Kurze Workouts, während Claude arbeitet: ein Tagesziel, Streaks, Badges und…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Ein Nutzungs-Dashboard für Claude Code: Ausgaben pro Modell.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Ein Claude-Code-Mod: Live-Aufschlüsselung des Kontextfensters über dem Prompt.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now-Playing-Mod für Claude Code: Apple Music und Spotify über der Eingabe, mit…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Fünf Claude Code-Mods zum gleichzeitigen Ausführen vieler Sitzungen…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods für Claude Code: Cache-Uhr, Blast Radius, Vorschläge, Arbeitsliste, Grill.
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code-Mods: Suggestion Spotlight zeigt, worauf sich der nächste…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Nur eine Eule für deinen Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Einzeiliges Claude Code-Band.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Die originale Doom-Engine mit Freedoom, spielbar innerhalb von Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - A Claude Code mod that keeps a running list of the open items in a conversation…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Ein Tamagotchi, das in Claude Code lebt: Es schlüpft, frisst den Code, den…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods for Claude Code, as a plugin marketplace.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code-Mod: zeigt die Zeit jedes Prompts und jeder Antwort im Terminal und…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Claude-Code-Mods, als Funktions-Hooks geschrieben, und der Marktplatz, der sie…
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - divramods Claude-Code-Mods: Live-Bereiche und Anpassungen für die…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude-Code-Mod: Nachdem ein Guard einen Tool-Aufruf blockiert hat, stoppt er…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude-Code-Mod: Hintergrundaufträge in einer Ansicht, mit aus der…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude-Code-Mod: ein Posteingang für Nachrichten von Teammitgliedern, benannten…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude-Code-Mod: Erklärt Sandbox-Blockierungen und wandelt wiederholte…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hey, stummgeschaltet! Schluss mit Diff, kürzt den Riff, keine weiteren…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude-Code-Mod: Abonnementnutzung.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Bewegungsdesign-Mods für Claude Code: ein Live-Monitor mit reaktionsfähiger…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Ein Live-Radar deiner parallelen Branches und Worktrees über dem Prompt: welche…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude-Code-Mods (Function-Hook-Plugins): Kontextband, offene Punkte…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Strg+Klick zum Kopieren des Links in jedem Codeblock in Claude Code-Antworten…
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - Der jev-Mod: $.jev für Claude Code, typisierte Beurteilungen von TypeSafe Jev.
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mods für Claude Code: Hook-Plugins wie usage-meter.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Evangelion-Seitenleiste für Claude Code: Kontext, Kontingent, Aktivität, PRs…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Testergebnisse in einem Claude Code-Bereich: Fehler, ihre Details und…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-Mod: wie lange jede Antwort dauerte, wie lange Claude nachdachte…
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod: waits out the 5-hour usage limit and sends &quot;continue&quot; for you.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Kontextnutzungsbereich in der Seitenleiste: Gesamtmenge, Kategorien, Wachstum…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Dateiliste in der Seitenleiste: Welche Dateien in dieser Unterhaltung neu…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 im 8-Bit-Stil (schwarz-weißes holländisches Hängeohrkaninchen) läuft und…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - „Meine Fragen“ in der Seitenleiste: Jede Nachricht, die der Benutzer in dieser…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Zeitachse in der Seitenleiste: Wofür die Zeit in dieser Runde aufgewendet wurde…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Token-Verkehr in der Seitenleiste: Wie viele Token die Hauptunterhaltung bei…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Die ehrliche Bohnenpaste von claude code: Nach jeder abgeschlossenen Runde sagt…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Evidenzbasierte Plan-Checkliste für Claude Code: Genehmigte Pläne werden zu…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Kleine Mods für Claude Code, etwa neue Slash-Befehle und Seitenbereiche.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Multiplayer-Spiele, die man in Claude Code spielen kann, während es arbeitet.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd lebt in einem Band über deinem Claude Code-Prompt: stellt die Sitzung…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Ein Mod, der Antworten und Benachrichtigungen von Claude Code mit VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Ein Claude-Mod zum Lesen und Zusammenführen der Unterhaltungen zwischen deinen…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude-Code-Mod: Laufende Subagenten als Pixel-Claude-Maskottchen über dem…
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - Kalte Claude-Code-Sitzungen mit Haiku zusammenstauchen — eine einzeilige…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Zwei Claude Code-Mods: folio, ein Dateibereich neben dem Chat, und tint, eine…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Ein Live-Aufgaben-HUD für Claude Code Desktop: eine Leiste über dem Prompt…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Ein von der Community kuratierter Leitfaden zu Claude Code-Mods…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Ein Claude-Code-Mod, der anzeigt, was Claude im Untertitel des iTerm2-Tabs tut…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Eine flauschige schwarze Katze über deinem Claude-Code-Prompt.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Ein Claude-Code-Mod mit umschaltbaren Berechtigungsprofilen: eine sichere…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community-Mods für Claude Code: Wächter, Bereiche und Befehle, die innerhalb…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Ein ruhiger Seitenbereich für Claude Code: was diese Sitzung tut, ihr Plan…
- [mmedum/spor](https://github.com/mmedum/spor) - Stellt wieder her, was Claude Code ausblendet: die von Claude gelesenen…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-Mod, der die Todo-Tools für Modelle wieder aktiviert, die sie…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-Mod: eine Zeile pro Aufgabe der Aufgabenliste über dem Prompt mit…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Spiele Vier gewinnt gegen eine AI innerhalb von Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude-Code-Mod: Wenn ein anderer Coding-Agent Änderungen in dein Repository…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude-Code-Mod für Repositories, die von mehreren KI-Agenten gemeinsam genutzt…
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Ein Cyber-Neon-Internetradio-Bereich für Claude Code – Synthwave-Wahlrad…
- [niksavis/handily](https://github.com/niksavis/handily) - Claude Code-Mods, die deine Arbeitselemente, Aufgaben und Sitzungen für jeden…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Eine Schutzschranke für SQL in Claude Code: Fragt nach, bevor Claude DELETE…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Ein Mod für Claude Code, Windows und CJK zuerst: Vorschauen eingefügter Bilder…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime für Claude Code: ein Ton, wenn Claude fertig ist, deine Eingabe benötigt…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Die besten Claude Code-Mods, sortiert danach, was sie für Sie tun.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Ein Claude Code-Mod, das riskante Shell-Befehle.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Zwei Claude-Mods für Claude Code: garde-du-corps.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Lazy Panda Panel für Claude Code: Dokumente prüfen, ohne eine Pfote zu heben.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Beschimpfe Claude Code, und eine Cartoon-Hand schlägt zurück.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live-Sitzungsstatistiken-Seitenbereich für den Code-Tab der Claude Desktop-App…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods für Claude Code: safety-guard blockiert destruktive Befehle und den…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods für Claude Code: Function-Hook-Plugins, die innerhalb der Sitzung…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code-Mod: Live-Aktienticker, /quote-Bereich, Preisalarme, Marktband und…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code-Mod: SSH-Host, RAM und 5h/7d-Nutzungslimits in einer Zeile über dem…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-Mod: Liegestütze, die man machen kann, während Claude arbeitet.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Der Mod-Shop für Claude Code: durchsucht GitHub nach Mods, zeigt Vorschauen und…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-Mod: verwandelt den im Planmodus genehmigten Plan in eine…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Eine handverlesene Liste von Claude Code-Mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenloser Modus: Hilfsagenten laufen auf Haiku, und große Dateien und Logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ein Lofi-Soundtrack, der der Sitzung folgt: Ruhe, Fokus, Flow sowie Hinweise…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Lerne, während Claude programmiert: Nach einem Durchlauf, der den Code geändert…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Ein Band mit jeder Änderung, die Claude vornimmt: Spiele jede Änderung ab…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Jeder Link, den deine Sitzung erwähnt, in einer Zeile über der…
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code Function Hooks – minimale Demo: ein Live-Token-/Kostenpanel über…
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Claude-Code-Mod für Kontext, Wachstum, Quota, Cache, native Kosten und…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Ein gemütlicher RPG-HUD-Mod für Claude Code.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Ein-Klick-Commit-Nachrichten für Claude Code mit einer tanzenden…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Claude-Code-Mod: Sieh deine Claude-Tarifnutzung.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude-Code-Mod: Live-Crew-Bereich für jeden Subagent.
- [Tejas242/airspace](https://github.com/Tejas242/airspace) - Air traffic control for parallel Claude Code sessions: one writer per file…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Ein Claude-Code-Mod, der die aktuelle Sitzung in einem Bereich anzeigt: jede…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Ein Claude Code-Plugin-Marketplace für Mods: function-hooks-Plugins, die…
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code-Mod: ein angedockter Bereich, der die Subagents der Sitzung und…
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Claude Code-Mod: eine Leiste und ein Panel, die deine Subagenten verfolgen…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude-Code-Mod: 5h/7d-Kontingent, Kontextfenster, verbleibende…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude-Code-Mod: animierte Fortschrittsleiste und Abschlusszusammenfassung für…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drei kleine Claude Code-Mods: Sieh, wann deine Subagents fertig werden, stelle…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Shrinks big screenshots before Claude reads them, so long sessions last longer…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Sag „I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stelle Claude eine Nebenfrage in einem Bereich neben deiner Arbeit.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace für Claude Code-Mods mit Ein-Schritt-Installation und…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Countdowns für Ratenbegrenzungen und eine Prognose der Verbrauchsrate für…
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Sicherheitsebene für Roblox Studio und Claude Code: RemoteEvent-Prüfung…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods für Claude Code. agent-crew: Beobachte deine Subagenten bei der Arbeit als…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Ein Live-Aufgabenboard für Claude Code: vor dem Erstellen planen, jede Aufgabe…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Immer aktives Band über der Claude Code-Eingabeaufforderung: Kontextfüllstand…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Eine handverlesene Sammlung der besten Ressourcen für die großartigsten…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Ein Claude-Code-Plugin, das anzeigt, was gerade geschieht – Kontextnutzung…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Wunderschöne, hochgradig anpassbare Statuszeile für Claude Code CLI mit…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle Teile des System-Prompts von Claude Code, 27 integrierte…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Mehr als 45 Tipps, um Claude Code optimal zu nutzen, von den Grundlagen bis zu…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — erstellt Xiaohongshu-Karussells und…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Schöne Powerline im Vim-Stil für Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Überprüfe den Diff deines Coding-Agents in einem Terminalbereich und sende…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Umfassendes Statuszeilen-Plugin für Claude Code mit Kontextnutzung…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code &amp; Codex lokales Token-Tracking – Statusleiste.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Erstelle Mods für Claude Code: Hänge dich an jede Anfrage, ändere jede Antwort…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Umfassendes Statuszeilen-Dashboard für Claude Code — Sitzungsinformationen…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Verfolge den CO₂-Fußabdruck deiner Claude Code-Sitzungen.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Eine ästhetische Statuszeile für Claude Code von awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Öffentliche Claude Code-Skills und Mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, Mods, Subagents, Hooks, Slash-Befehle und Anleitungen für Claude Code –…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Rechtlich kostenlose LLM APIs &amp; Coding-Agents — zweimal wöchentlich…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Terminal-Statuszeile für Claude-Code-Sitzungen.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live-Fußballergebnisse, Spielpläne und Tabellen für den Wettbewerb, dem du…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Lokale Steuerungsebene für Claude Code auf Windows und macOS: LLM Gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, der deinen Coding-Agenten in einen Experten für Tastatur-Firmware…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Persönliche Claude Code-Konfiguration, versioniert innerhalb von ~/.claude…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebetszeiten, Hijri-Datum, Adhkar, täglicher Ayah, freiwilliges Fasten…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Sitzungsbewusste Statuszeile für Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek-Harness-Plugin für Forschungsthemen…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Two-line truecolor statusline for Claude Code.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Portables Claude Code-Toolkit für .NET DDD/Clean Architecture: strikte…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Plugin-Sammlung für Claude Code, pi und DeepSeek Harness: Statusleisten-HUD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Portable globale Konfiguration für Claude Code: benutzerdefinierte Fähigkeiten…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-Plugins, die ich täglich verwende: Skills und Mods, aufgeräumt…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram in Claude Code: Chats und Kanäle in einem Fensterbereich lesen und…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marktplatz für Claude-Code-Plugins und -Fähigkeiten, um Mods für das Spiel…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token-Verwaltung für Claude Code: Das Topmodell gibt die Richtung vor, die…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Geteilter-Fensterbereich-Viewer für Claude Code in Windows Terminal und tmux…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live-Statuszeile für Workflow-Phasen in Claude Code.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Inoffizielle Mods für den Code-Tab von Claude Desktop — usage-pet: ein…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository für Claude Code Awesome Media-Mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Senke die Tokenkosten von Claude Code &amp; Codex: Leitet Abfragen und Testläufe an…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Einfache und nützliche Statusline-Einrichtung für Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Nutzungslimit-Warnungen für Claude Code: macOS-Benachrichtigungen…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Konfigurierbare Claude Code-Statusleiste für Linux, WSL, Windows und macOS, mit…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Schnelle Rust-Statuszeile für Claude Code — Payload zuerst, gecachtes Git…
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Claude-Code-Statuszeile mit Kontextleiste, Token-Sparkline und Kosten-Tracker.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Ein Live-Nutzungsdashboard für Claude Code — Kontextaufschlüsselung…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Eine Status- und Tokenzeile für Claude Code: Kontext, 5-Stunden- und…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Wichtige Statusdetails für Claude Code anzeigen, darunter Modell, Kontext…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - die freundliche, an allem herumspielende Statuszeile für Claude Code…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Mehrzeilige Claude Code-Statuszeile: Ausgaben, Kontext-%, Git und aktiver…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statuszeile mit nützlichen Informationen für claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Startvorlage zum Organisieren eines Claude-Code-Arbeitsbereichs für mehrere…
- [spacegrowth/claude-relay](https://github.com/spacegrowth/claude-relay) - Claude Code plugin: a lead session delegates work packets to executor sessions…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native Agententeams. Unter Kontrolle. Strikte Arbeiterlimits, Live-Sichtbarkeit…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Benutzerdefinierte Statusline für Claude Code — Kontextleiste mit…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Eine übersichtliche, informative Statuszeile für Claude Code — zeigt Projekt…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code-Plugin-Marktplatz mit baloo: Fähigkeiten, ein Agent, der Änderungen…
- [charlie-818/claude-dispatch](https://github.com/charlie-818/claude-dispatch) - Phone control for a fleet of live Claude Code panes — attach to existing iTerm2…
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Claude Code-Statuszeile: Kontextnutzung, 5h-/7d-Kontingentbalken…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionelle Claude-Code-Statuszeile: Sitzungsdauer, Kosten in mehreren…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Abonnementbewusste Statuszeile für Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Eine umfangreiche Terminal-Statuszeile für Claude Code — Bun + TypeScript…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Claude Code-Plugin, das Mermaid-Diagramme im Transkript ansprechend darstellt…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, Skills und Agenten für Claude Code — beginnend mit einer Statuszeile…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code 커스텀 상태줄 (모델, effort, 컨텍스트, 캐시, 사용량 한도).
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Claude Code-Plugin: Sieh dein verbleibendes Claude-5-Stunden-Nutzungslimit…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Echte DeepSeek API-Ausgaben für Claude Code: bepreist Sitzungs-Transkripte neu…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code-Statuszeile mit Agentenpanel-Zeilen.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronisiere Claude.
- [J-J-E/claude-kanban](https://github.com/J-J-E/claude-kanban) - Ein Markdown-Kanban-Board für Claude Code: Karten sind Dateien, ein…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Zeigt eine detaillierte, farbcodierte Statusleiste für Claude Code mit Kontext…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code-Einstellungsmenü, Statusline und Konfiguration.
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Benutzerdefinierte Claude Code-Statuszeile mit Kontextfenster…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code-Umgebungsinstaller: Skills, Statuszeile, Hooks, Berechtigungen und…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude Code-Plugins und -Mods, um zu verstehen, was Claude tut: übersichtliche…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Überwache den Status von Claude Code über deine macOS-Menüleiste mit…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Farbenfrohe mehrzeilige Statusleiste für Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code-Statuszeile für Windows (PowerShell): Nutzungsleisten…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Bearings- und Glossary-Mod für Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Benutzerdefinierte Claude Code-Statuszeile.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Portierbare Claude-Code-Konfiguration: CLAUDE.md, Einstellungen, Statuszeile…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Verfolge die Kontextnutzung von Claude Code, Sitzungskosten und Zurücksetzungen…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code-Mod-Sammlung.
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - A hands-on, verified deep-dive into Claude Code — CLAUDE.md, subagents, skills…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Statuszeile zur Echtzeit-Kostenverfolgung und Sitzungsüberwachung für Claude…
- [wmkeza/claude-plugins](https://github.com/wmkeza/claude-plugins) - wmkeza.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Cordis / DeepSeek Harness-Plugin — der Agent bittet den Menschen in einer…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Dreizeilige Claude Code-Statuszeile: Kontexttiefe, sitzungsübergreifende…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Kontextverfall-Detektor 2026 – Proaktiver KI-Speicher- und Ratenlimit-Monitor…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-Hooks, Subagents und Statuszeilen: Open-Source-Sammlungen und Tools…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Claude Code-Statuszeile — Live bleibende Claude/Codex-Nutzungsanzeigen während…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Ein visueller Builder für Claude-Code-Statuszeilen.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude-Code-Statuszeile mit Echtzeit-Tokenverbrauch und geschätztem…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods für Claude Code: Bereiche, Bänder und Begleiter auf Basis von…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Übergebe Aufgaben zwischen deinen Claude Code-Sitzungen.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Dies in einem MCP-Server zur Steuerung von MODS, dem modularen…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex- und Claude-Code-Fähigkeit zum Übersetzen von CK3-Mods mit einem lokalen…
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-Source-Mods und weitere Erweiterungen für Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Finde heraus, was du Claude Code immer wieder fragst, und verwandle…

</details>

<a id="dsh-cordis"></a>

## DSH- und Cordis-Plugin-Ökosysteme

DeepSeek Harness und Cordis erreichen dasselbe Ziel aus einer anderen Richtung: Für sie ist das Plugin der Mod-Mechanismus, daher entspricht ein Plugin dort einer Mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74307 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

🌊 Der ursprüngliche Agent-Harness. Setze intelligente Multiplayer-Schwärme ein, koordiniere autonome Workflows und entwickle konversationelle KI-Systeme. Mit adaptivem Gedächtnis, selbstlernender Intelligenz, Föderation, Vektor-RAG-Integration und nativer Integration von Claude Code / Codex / Hermes und vielen weiteren.

<sub>🔧 Im Code gefunden: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                       |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **74307**  |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100445 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

🎨 Bestes DeepSeek Harness Design-Plugin. Die Open-Source-Alternative zu Claude Design. 🖥️ Desktop-App mit Local-First-Ansatz. 🖼️ Dein Coding-Agent wird zur Design-Engine: Prototypen, Landingpages, Dashboards, Folien, Bilder und Videos – echte Dateien, Export als HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode und mehr als 20 CLIs über BYOK.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **100445** |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81766 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Verwandle jede Idee, jeden Plan oder jede Codebasis in ein ansprechendes interaktives Diagramm. Eine Agent-Skill für Claude Code, Codex und weitere.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **81766**  |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐78887 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Mit Agents alles zurückentwickeln, vom App-Verhalten bis hin zu nativen Binärdateien.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **78887**  |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35758 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Ein zuverlässiger Coding-Agent für komplexe Softwareentwicklungsaufgaben.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Go                                                                                             |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **35758**  |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30384 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Moderne Desktop-Lösung für das DeepSeek Harness (DSH)-Plugin-Ökosystem. Alles ist ein „Plugin“, auch der Desktop selbst ist ein „Plugin“.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **30384**  |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25477 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Zusammenfassung

Distilly – Extrahiere, wie sie denken, in wiederverwendbare Skills für jeden Agenten oder Bot. Früher Colleague Skill（原同事 Skill）.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **25477**  |
| Letzter Push      | 2026-09-22 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9115 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Meta-Framework für raumzeitliche Komponierbarkeit

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **9115**   |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8605 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness (DSH) Web-Plugin-Aggregationsökosystem · Alles ist ein Plugin, verteilt über die Creative Workshop｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **8605**   |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐7358 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **7358**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/212e73dc2aecbd46.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4441 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **4441**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4276 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Offiziell meistempfohlenes TUI-Plugin von DSH – hohe Leistung, geringer Overhead, niedlicher Pixel-Wal, reibungslose Mausinteraktion. Installation mit einem Befehl über npm. / Offiziell meistempfohlenes TUI-Plugin von DSH: hohe Leistung, geringe Auslastung, niedlicher Pixel-Wal, reibungslose Mausinteraktion, Installation mit einem Befehl über npm

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **4276**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3150 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness Tauri-Desktopversion | Nur 8 MB großer Installer, keine Einrichtung der Umgebung, voreingestellte Plugins, Windows / macOS / Linux.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **3150**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1970 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Das beste DeepSeek-Harness-Plugin für Einblick und Verwaltung des Kontexts, mit Kontext-Dashboard, -Browser, -Seitenleiste und Kontextbefehl für Kontextstatistiken, Zusammensetzung, Aufschlüsselung und Details zur Entwicklung, um zu verstehen, wie der Kontext aufgebaut ist und wie er sich entwickelt. All-in-one-Plugin zur Visualisierung des DeepSeek-Harness-Kontexts mit Kontextpanel, Browser, Seitenleiste und Kontextbefehl zur Übersicht über Zusammensetzung, Entwicklung, Komprimierung, Beschneidung und weitere Ereignisse und Aktionen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **1970**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1782 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

IM-Bots über QR-Code oder Bot-Zugangsdaten mit DeepSeek Harness verbinden (unterstützt Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord und WhatsApp). IM-Bots über QR-Code oder Zugangsdaten mit DeepSeek Harness verbinden (9 Kanäle).

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **1782**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1463 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **1463**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1395 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

KI-Software zum Schreiben von Romanen: Organisiert Ideen, Figuren, Worldbuilding, Entwürfe, Kapitelentwürfe, Begutachtung und Überarbeitung in einem kontrollierbaren Workflow. Bietet Desktop-Apps für Windows/macOS, unterstützt lokale und Online-Modelle. KI-Software zum Schreiben von Romanen: Organisiert Ideen, Figuren, Worldbuilding, Entwürfe, Kapitelentwürfe, Begutachtung und Überarbeitung in einem kontrollierbaren Workflow. Bietet Desktop-Apps für Windows/macOS, Ollama-Integration und eine Vorschau des DeepSeek-Harness-(DSH-)Plugins.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **1395**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Speicher für Claude Code, Codex, Cursor und 38 weitere Coding-Agenten, erstellt aus dem bereits auf deiner Festplatte vorhandenen Sitzungsverlauf. Lokale Suche, MCP und Hooks, kein LLM, eine Go-Binärdatei.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Go                                                                                             |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **1169**   |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐703 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness (dsh) Windows Desktop-Client – gebündelt mit Node.js + dsh CLI, Start mit einem Klick

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **703**    |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐542 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **542**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **526**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Deine Intelligenz, orchestriert. Jeder Builder. Jedes Team. Jeder Agent. Für alle.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Go                                                                                             |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **351**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐282 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Just open your browser — get all your work done.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **282**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

ACRYL - Agent Context Relay Yielding Lifecycles. Ein persistenter Arbeitsbereich, ein kanonischer Kontext, jeder Coding-Agent.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **255**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Native DeepSeek Harness (DSH)-Plugin-Integration von TypeSafe Jev oder einer Decision-API wie luna als System One-Entscheidungsebene für Agentenauswahl, Überwachung, Korrekturen und Genehmigungen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **203**    |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Time-shifting task delegation for DeepSeek Harness (dsh): plan tasks at leisure, they run unattended off-peak, come back to a report. Human-adjudicated, desktop + web.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **170**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness-Plugin für die Vorschau einer sitzungsübergreifenden Migration zwischen Presets. Übergaben mit festem Schema bewahren Zustand, Absicht des Ursprungsmodells und ungelöste Bilder; die ursprüngliche Sitzung bleibt unverändert.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **165**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐158 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **158**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **132**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **132**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐128 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Claude Code-Desktop-Theme für DeepSeek Harness｜ Claude Code-Desktop-Theme für die Web-GUI von DeepSeek Harness

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **128**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐121 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Laufzeitnachweise, die Agenten dabei helfen, Hotspots in Anwendungs- und nativem Code, GPU-Kerneln und Inferenz-Stacks nachzuverfolgen, zu profilieren und zu beseitigen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **121**    |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐86 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

StudyHub: ein DeepSeek Harness (DSH)-Plugin, das deine eigenen Materialien in Fragen und verteilte Wiederholungen umwandelt · DSH-Lern-Plugin, das eigene Materialien in Fragen und verteilte Wiederholungen umwandelt

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **86**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐73 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness（dsh web）aus der Ferne über das öffentliche Internet steuern: Nach der Installation erhältst du eine eigene verschlüsselte Adresse und kannst auch unterwegs per Smartphone remote darauf zugreifen – ohne dasselbe LAN/WLAN und ohne Portweiterleitung; optional mit selbst gehostetem Dienst. Remote-Steuerung von DeepSeek Harness (dsh web) von überall – verschlüsselte öffentliche URL, kein LAN erforderlich.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **73**     |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-web` · `pwa`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://cdn.jsdelivr.net/gh/mrRisega/dsh-remote@main/image/phone-mirror.png" width="100%" alt="mrRisega/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary><b>Mehr in dieser Kategorie</b> <sub>· 75</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Eine Schutzmaßnahme vor der Ausführung für AI-Coding-Agenten.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Eine kuratierte Liste der besten großartigen KI-Plugins für KI-Assistenten…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-Plugin-Marktplatz / DSH Plugin Marketplace: Im DeepSeek Harness Web GUI mit…
- [beancookie/awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin) - Awesome DeepSeek Harness (DSH) Plugin.
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - DSH-Web-Theme im Stil der offiziellen Website von 终末地: cremefarbener…
- [arcships/rutis](https://github.com/arcships/rutis) - Eine Plugin-Runtime für Programme, die weiterlaufen — Rust-Kern, TypeScript…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Desktop-Agent auf Basis des Deepseek-Harness-Kerns.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Das lebendige DeepSeek Harness-Plugin-Verzeichnis — stündlich aktualisiert…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Aufgabenbewusster Abruf von Arbeitsbereichskontext und Lifecycle-Tracking für…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Ausgewähltes Verzeichnis für DeepSeek Harness-(DSH)-Plugins — über 280…
- [hyzyn/dsh-plugin-kit](https://github.com/hyzyn/dsh-plugin-kit) - Plugin family for the DeepSeek Harness (DSH) Web GUI: a pnpm monorepo with a…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh Spiel-Asset-Meister-Plugin. Bindet das seedream Bildgenerierungsmodell und…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zotero-Toolkit für DeepSeek harness; verwandle deine Zotero-Bibliothek in einen…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH-Plugin: Git-Bash-Shell für alle Agentenmodi auf Windows.
- [FeatherHunter/dsh-prompt](https://github.com/FeatherHunter/dsh-prompt) - DeepSeek Harness 的 Prompt 工具箱：别再复制粘贴——24 条深度模板随手点，/prompt 与智能推荐主动兜底，装好即用、可自定义.
- [Andersen216/dsh-whale-girl-live2d](https://github.com/Andersen216/dsh-whale-girl-live2d) - 🐋 鲸鱼娘桌宠 · Whale Girl Live2D —— DSH（DeepSeek Harness）Web 界面里的 Live2D 桌宠：跟着 agent…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: plattformübergreifendes Gruppenchat-Agentensystem auf Basis von…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidenzgestützte Evaluation und Observability für Prompts, RAG, Skills…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH Web-Plugin: tägliche Token-Nutzungsstatistiken mit einer GitHub-artigen…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Lokale Schreibumgebung für chinesische Webroman-Autoren (19 Werkzeuge): Vor dem…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - MCP-Serververwaltungs-Plugin für DeepSeek Harness: Seite Einstellungen → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness-Plugin: 15 obra/superpowers Engineering-Skills, zweisprachige…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A-Laufzeitumgebung für Handelsverhandlungen + DeepSeek-Harness-(dsh-)Plugin.
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - MCP-Serververwaltungsoberfläche für DeepSeek Harness Web – schwebendes Panel…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Ein echtes PowerPoint, kein HTML. Sag deiner KI, was abgedeckt werden soll, und…
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - DeepSeek Harness-Plugin: Lazy-Senior-Modus und Portierung der siebenstufigen…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Macht die auf dem lokalen WorkBuddy-Desktop angemeldeten Modelle.
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - All-in-one-Verwaltung für Skills, Subagenten, MCP und LSP für DeepSeek Harness…
- [xxww0098/dsh-plugin-oauth-subs](https://github.com/xxww0098/dsh-plugin-oauth-subs) - ChatGPT Codex and xAI Grok subscription OAuth for DeepSeek Harness — PKCE /…
- [muyuanjin/dsh-ptc-plus](https://github.com/muyuanjin/dsh-ptc-plus) - A session-bound agent-native REPL for DeepSeek Harness PTC mode.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Permanente Kompatibilitätstests für DeepSeek Harness-Plugins: exakte Releases…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Röntgenblick für DeepSeek Harness-Plugins: deklarierte Fähigkeiten im Vergleich…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness-Host-Plugin, das Projektdokumente und Langzeitgedächtnis als…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [Cyning12/SpecWave](https://github.com/Cyning12/SpecWave) - SpecWave — multi-host coding CLI + P0 gates/Harness (Cursor/Claude/DSH).
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [Fayelin12/dsh-office](https://github.com/Fayelin12/dsh-office) - Agent-office dashboard for DeepSeek Harness (DSH): workspaces, sessions, token…
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Local-first-Sprachgespräche für DSH. Spracherkennung und Sprachsynthese auf…
- [fan56/dsh-topics-memory](https://github.com/fan56/dsh-topics-memory) - Topic memory for LLM agents — edited, not accumulated: a topic keeps the…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH-Plugin: ein Git-Toolfenster auf IDE-Niveau als nativer…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - Kreativmodus auf Grundlage des PTC-Modus: DSH-Plugin, das die…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Page capability kit for DeepSeek Harness (dsh): terminal dock, file tree…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Arbeitsbereich mit mehreren Ordnern: Ermöglicht dem DSH-Agenten.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Engineering-Workflow-Plugin für DeepSeek Harness: Aufgabenphasen…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH-Plugin für Rollenspiele: Charakterkarten.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Verifizierungsstandard ohne Abhängigkeiten für DeepSeek-Harness-(dsh-)Plugins –…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode auf DeepSeek Harness — DSH-Plugin, das OpenCode Zen + Go-Modelle der…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — Marktplatz für Plugins von Drittanbietern und geschützter…
- [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) - Query local log files with Chinese natural-language time expressions…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx ist eine menschenorientierte, erweiterbare Desktop-Arbeitsumgebung…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Ein Coding-Agent mit allem Drum und Dran für DeepSeek Harness — Claude…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH-Web-Eingabe-Plugin: Umschalten zwischen Senden und Zeilenumbruch…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Bietet der Desktopversion von DeepSeek Harness einen Fernzugang mit „begrenztem…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — Community-Versionsmaschinen-Deployment- und Betriebssuite für…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) Web-Plugin: Market-Dashboard-Seitenleiste zur…
- [yu381792/superlcm](https://github.com/yu381792/superlcm) - Fünf Träger, ein lokives Dialogarchiv: Archivierung des Originals…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness-Plugin: verwandelt den Fehler bei der Bereitstellung der…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Macht einen nicht zugeordneten leeren Modellversuch erneut versuchbar, für die…
- [denceee/dsh-everything-claude-code](https://github.com/denceee/dsh-everything-claude-code) - Passt everything-claude-code an DeepSeek Harness an: 11 Skills, ein…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek-Harness-Agent-Voreinstellung: Codex und Claude Code als…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Eine Rust-Plugin-Laufzeitumgebung mit einem durch Verus verifizierten…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Texte, Diskussionen und Videos

Artikel, Diskussionen und Videos über die Mod-Funktionalität.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Hallo HN, ich habe das für mich selbst entwickelt und wollte es als Open Source veröffentlichen. Das Problem: Ich wollte eine Möglichkeit, zwischen Prompts Erinnerungen zu erhalten, da ich oft lange Zeit im Terminal verbringe, besonders jetzt, da wir normalerweise so viele Agenten parallel verarbeiten. Die erste Version war ein einfacher Rep

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Zusammenfassung

Es wurde keine Beschreibung vom Upstream veröffentlicht.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Ich habe dies entwickelt, weil Claude bei den neuesten Coding-Modellen in einen Tiefenarbeitsmodus mit obskuren Befehlen wechselt, sodass ich nicht mehr weiß, was gerade passiert. Dies ist ein Mod (ein Plugin, das die neuen Function Hooks von Claude Code verwendet), der eine Zeile über dem Prompt anzeigt: – den aktuellen Schritt,

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Texte, Diskussionen und Videos`                                          |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Erstmals gelistet | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Projekte nach Implementierungssprache

Das Ökosystem konzentriert sich auf Python und TypeScript, aber typisierte Clients tauchen weiterhin in anderen Sprachen auf. Diese Tabelle wird aus den Einträgen selbst generiert.

| Sprache    | Einträge | Beispiele                                                                                                     |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 307      | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 82       | `Enc-hanted/dsh-pulse`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                    |
| Python     | 40       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 26       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13       | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 6        | `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`, `bunderlog/claude-plugins`                               |
| Rust       | 4        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `arcships/rutis`                             |
| PowerShell | 2        | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1        | `reporails/arcade`                                                                                            |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                       |
| Swift      | 1        | `peaceinitiativemenhadenoil263/claude-status-bar`                                                             |

<sub>Es werden nur Einträge gezählt, die eine Sprache angeben. Dokumentations- und Diskussionseinträge sind von dieser Tabelle ausgeschlossen.</sub>

## Mitwirken

Korrekturen sind willkommen und der schnellste Weg, diese Liste zu verbessern. Erstelle ein Issue oder einen Pull Request, wenn ein Eintrag falsch einsortiert oder falsch eingestuft wurde oder ein Projekt aufgrund einer Namenskollision zu Unrecht ausgeschlossen wurde — in dieser letzten Kategorie sind automatisierte Filter am wahrscheinlichsten fehlerhaft.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Zuletzt aktualisiert · 2026-10-11T14:37:28+08:00</sub>
