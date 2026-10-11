<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Hervorragende Claude-Mods">
</p>

<h1 align="center">Hervorragende Claude-Mods</h1>

<p align="center"><b>Das evidenzbasiert bewertete Verzeichnis der Claude-Code-Mods und -Plugins sowie des tiefergehenden Verhaltens, das sie verändern.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-534-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <b>Deutsch</b> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Aktuelles Verzeichnis** · Letzte Synchronisierung: `2026-10-11T23:26:48+08:00` (UTC+8)
> · Einträge: **534** · Mit der letzten Aktualisierung hinzugefügt: **0** · Implementierungssprachen: **12**

<sub>Jeder Eintrag unten wurde automatisch erfasst, gefiltert und erneut überprüft. Nichts davon ist bezahlte Platzierung.</sub>

<a id="featured"></a>

## Auswahl des Augenblicks

<sub>Ein Eintrag pro Kategorie, sortiert nach Evidenzgrad und Sternen und bei jeder Aktualisierung neu berechnet. Eine Rangliste, keine Empfehlung; jede Auswahl führt weiter zur vollständigen Karte unten. Projekte, die einen Screenshot oder eine Aufzeichnung veröffentlicht haben, werden bevorzugt, damit die Leiste visuell bleibt.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9474 · TypeScript · ✅ official</sub>
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
<sub>⭐74336 · TypeScript · 👁️ observed</sub>
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
- [Offiziell: Eigene Repositories und Release Notes von Anthropic](#offiziell-eigene-repositories-und-release-notes-von-anthropic) — **14**
- [Mods: mit der Mod-Funktion erstellt](#mods-mit-der-mod-funktion-erstellt) — **408**
- [DSH- und Cordis-Plugin-Ökosysteme](#dsh--und-cordis-plugin-ökosysteme) — **101**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150172 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Zusammenfassung

Claude Code ist ein agentisches Programmierwerkzeug, das in deinem Terminal ausgeführt wird, deine Codebasis versteht und dich durch die Ausführung routinemäßiger Aufgaben, die Erklärung komplexen Codes und die Verwaltung von Git-Workflows schneller programmieren lässt – alles über Befehle in natürlicher Sprache.

<sub>🔧 Im Code gefunden: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | TypeScript                                                       |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **150172** |
| Letzter Push      | 2026-10-10 |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9474 · TypeScript · ✅ official · 1 天</summary>

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
| Sterne            | **9474**   |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

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
| Sterne            | **8248**   |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

##### 📝 Zusammenfassung

Eine KI-gestützte Sicherheitsüberprüfungsaktion GitHub, die Claude verwendet, um Codeänderungen auf Sicherheitslücken zu analysieren.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | Python                                                           |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **6342**   |
| Letzter Push      | 2026-02-11 |
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

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
| Sterne            | **1797**   |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-11 |

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
| Erstmals gelistet | 2026-10-11 |

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐486 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Community-Katalog öffentlicher Claude Code-Mods (Funktions-Hooks), aus GitHub gescannt, einschließlich der Informationen, was jeder Mod lesen, schreiben, ausführen oder über das Netzwerk senden kann. https://mods.aidojo.si/ durchsuchen

<sub>🔧 Im Code gefunden: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **486**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐338 · Python · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

macOS menu bar & Windows tray app pinning Claude Code, Codex, Antigravity & Grok CLI quota, burn rate, and cost to your screen. Local-first, no LLM API calls. HTML reports, 14 themes.

<sub>🔧 Im Code gefunden: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | Python                                                                    |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **338**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐186 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

Claude Code mods: plugins built on hooks that add live lines above the prompt, guards, panes and games. Context bar, usage meter, Codex review watch, Markdown preview, Spotify now playing and more.

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
| Sterne            | **186**    |
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐132 · TypeScript · 👁️ observed · 7 天</summary>

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
| Sterne            | **132**    |
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
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **96**     |
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

A collection of claude code mods

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
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **75**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

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
| Sterne            | **66**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Zusammenfassung

Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens. 台股／美股看板 + more to come.

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
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Zusammenfassung

Expert skills, agents, commands, rules, hooks & output styles for Claude Code — session continuity + modern CLI tooling for real-world dev workflows

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
| Erstmals gelistet | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

Claude Code mods: live plan progress bars above the prompt

<sub>🔧 Im Code gefunden: `README.md`</sub>

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
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐44 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Claude Code zeigt Bilder an und spielt Videos direkt in deinem Terminal ab: Screenshots, Playwright-Aufzeichnungen und synchronisierte Vorher-/Nachher-QA. Ghostty & kitty.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **44**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

A pixel Pokémon that lives above the prompt in Claude Code

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **25**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

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
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Zusammenfassung

Xcode's build, tests, console and SwiftUI previews inside Claude Code

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
| Erstmals gelistet | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Claude Code mods: 21 styles and a full set of features you turn on when you need them, for the terminal and the desktop app. · 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

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
| Erstmals gelistet | 2026-10-11 |

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

Ten Claude Code mods, beginner guides, creation prompts, safe demos, and a build-your-own template.

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
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Claude Code mods: usage-band shows your 5h/7d limits, context window and cache hit rate above the prompt

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **13**     |
| Letzter Push      | 2026-10-03 |
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Zusammenfassung

Claude Code mods that make Claude's questions easier to read and answer (qa-guide).

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
| Erstmals gelistet | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Ten open-source mods for Claude Code: live panes, bands, status lines and tool-call guards. Burn meter, launch codes, session wrapped, boss fight, code pet and more.

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
| Erstmals gelistet | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Zusammenfassung

Two Claude Code mods: Codex computer-use bridge and coordinated Claude sessions. Source, build prompts, setup and tests.

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
| Erstmals gelistet | 2026-10-11 |

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

A UI around your Claude Code and Codex terminals that your agents build, so the only model in your head is yours.

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
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

KOZMOS — live, visual mods for Claude Code (CLI + desktop): bands above the prompt, sidebars, status ticker, companions, guards and sound.

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
| Erstmals gelistet | 2026-10-11 |

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

Six Claude Code mods in one plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) with per-mod switches, plus a mods-vs-hooks report.

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
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

개발동생의 Claude Code mods 모음. 택시 팩: 미터기, 내비, 과속 단속 카메라, 블랙박스

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
| Erstmals gelistet | 2026-10-11 |

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Zusammenfassung

Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf

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
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mehr in dieser Kategorie</b> <sub>· 374</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Collection of 100+ mods you can use with Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods und die Werkzeuge zu ihrer Erstellung: zuerst ein Builder-Skill…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - The Claude Code harness I run every day, published under this name since day…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Four Claude Code mods: Cache Keeper, Recording Mode, Goal Meter, and Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods that fix and translate your prompts before Claude reads them.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Desktop-App-Optik für das Terminal-Transkript von Claude Code, als Mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Ein Seitenbereich für Claude Code: die Subagenten, die eine Sitzung ausführt…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Source-cited Obsidian knowledge base about Claude Code mods: how they work, how…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop-Seitenleistenbereich (Code-Tab): listet alle unerledigten und…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods and skills from Nekyia Labs, built and used daily by AIs…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill that teaches Claude Code agents to build Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Nutzungsleiste über dem Eingabefeld von Claude Desktop (Code-Tab)…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-Mods, -Plugins und -Skills, über einen einzigen Marktplatz…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (function-hooks plugins) for Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - The Baselane mods gallery: Claude Code mods, checked and pinned.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Eine Entscheidungswarteschlange CLI/TUI für Menschen, die mit…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Eine schwebende Statuskarte für Claude Code – Modell, Kontext, Ratenlimits…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods für Claude Code: Function-Hook-Plugins, die Live-Bereiche und Verhalten…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard masks names and secrets while you screen-share;
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live-GSD-Dashboard für Claude Code: Roadmap, Agentenbaum mit Verzweigungen…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Unlock the full power of Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code-Mod (Plugin), das einen Seitenbereich mit den Tabs Activity, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, guardrails and quality-of-life mods for Claude Code: context, usage…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Two Claude Code mods above the prompt box: context-window meter, 5-hour limit…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Make the Claude Pro plan last longer: Claude Code mods for an exact usage HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lies die Markdown-Dateien, die Claude Code benennt, neben der Sitzung…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Sprach-Coworker für Claude Code. Besprich Dinge mit einem 3D-Wolf, der von…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, a live typing speedometer with per-prompt stats.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Feuerwerk für Claude Code: Jeder Tastendruck, jeder Tool-Aufruf, jeder Commit…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Discover Claude Code mods, plugins and extensions with animated demos, category…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod: mermaid diagrams drawn inline in the transcript.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Kleine Claude Code-Mods (Function-Hook-Plugins): session-switcher und mehr.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: pasted image thumbnails above the prompt, in any terminal.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: Claude Tools menu, Zen mode, terminal themes, effort and mode…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Two Claude Code mods for running many sessions at once: a context card above…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: discover, inspect, toggle and update Claude Code mods.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Best Claude Code Mods: hand-picked, validated, pinned.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude-Code-Plugin: automatisches Routing des Claude-Modells.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sechs Mods für Claude Code: animiertes Clawd-Maskottchen, Nutzungsbegrenzungs…
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Ein Claude-Code-Mod, mit dem Claude Befehle ausführen kann, die sudo benötigen…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - A marketplace of mods for Claude Code: a step debugger for the agent loop, git…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sechs Claude-Code-Mods: Planlimits und Kontext über dem Prompt, ein Coach für…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Das beste All-in-one-Mod-Paket für Claude Code: Nutzungsgrenzen und…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Spiele YouTube Shorts in deinem Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Narens Claude-Toolkit: Skills, Mods und MCP-Server für Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude-Code-Mod, der Edit- und Write-Diffs in zwei nebeneinanderliegenden…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods for Claude Code: Clawd, a tiny pixel mascot who acts out what Claude is…
- [reporails/arcade](https://github.com/reporails/arcade) - Classic desktop games as Claude Code mods, played in a pane while Claude works.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Eine kuratierte Liste von Claude Code-Mods, installierbar als…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Ein sehr meinungsstarkes Claude Code Plugin, entworfen von einem Rustacean, der…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code mods that keep an agent honest — function hooks that guard scope…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Eine passiv-aggressive Wassererinnerung für Claude Code.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - macOS-Notch-Dashboard für Claude Code: Nutzungslimits, offene Sitzungen…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della prompt cache, prossimi passi, bottoni rapidi e…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code Mod: ein Live-Bereich der GitHub PRs, die eine Session öffnet oder…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Ein Claude Code-Mod, der deine Nutzungslimits und Ausgaben in der Leiste über…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Hermans Claude Code Mods (Marktplatz herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods: progress bars for plans, a ledger of what Claude left…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Ein Pixel-Art-Naruto-Begleiter für Claude Code: 20 Ninja, 60 Jutsu, ausgeführt…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Sieh, was Claude Code im Hintergrund ausführt: Subagenten, Codex-Jobs, Shells…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Feldnotizen vom ersten Tag zu Claude Code-Mods auf Windows: eine…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-Mod: Live-Kosten-, Kontext- und Plan-Kontingentanzeigen über dem…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Ein Claude-Code-Mod, der Subagenten-Verteilung, Prompts mit umfangreichem…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods for claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Ein Claude-Code-Mod, der deine globalen Skills, Agents, Regeln und Tools pro…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code-Plugins (Mods): Wechsle zwischen mehreren Claude-Konten, beobachte…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Getestete Claude Code-Mods mit Installation per einem Befehl…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods for Claude Code: plugins built on function hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Filmähnlicher Abspann für deine Coding-Sitzung.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - A bunch of claude code mods built by me.
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code-Mods auf Abruf – ein Skill, der deine Unterhaltung liest und den…
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - A cliamp-backed YouTube player inside Claude Code (Claude Code mod).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude Code mods by vynnlee. One folder per mod, installable from one…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Lerne eine Fremdsprache, während du mit Claude Code arbeitest.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude-Code-Mods zum Ausführen vieler Sitzungen über viele Repositories hinweg…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Wenn ein Agent Java schreibt, können Codezeilen, die gegen Alibabas Java-Regeln…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Seitenleiste für Live-Kosten, Token- und Kontextnutzung in Claude Code: ein…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code Mod: ein Backlog der Follow-ups, die Claude über alle Sessions…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internetradio in Claude Code: eine cliamp-Seitenleiste, Mini-Player, Favoriten…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Unterhaltsame, nützliche Claude-Code-Mods: ein Pixelwesen über deinem Prompt…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude kocht. Chatten Sie mit Ihrem Squad.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - All-in-one-Claude-Code-Mod: Live-HUD, Sicherheitsvorkehrungen.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Eine Weltraumschlacht über dem Prompt von Claude Code, während dieser arbeitet.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Sieh, welche Dateien jeder Claude Code-Agent in seinem Kontext hat und wie viel…
- [dbroadhurst/claude-mod-todos](https://github.com/dbroadhurst/claude-mod-todos) - Claude Code mod: a pane summarising the remaining todos, with Do, Chat, Defer…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Behalte einen kühlen Kopf. Ein Thermometer für deine Claude-Code-Tage: Jede…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Prompt-Cache-, Kontext- und Plan-Limits für Claude Code auf einen Blick, in der…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-Mods für das Terminal und die Desktop-App.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude-Code-Mod: Ein Fortschrittsbereich für Aufgaben, Subagenten…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude-Code-Mod: Ein anklickbares, mit Zeitstempeln versehenes…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude-Code-Mod: Planratenlimits, Kontextauslastung, Sitzungskosten und Tokens…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-Skill + Mod, der spanische Wörter in Agentenantworten einfügt.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Your Alarum events above Claude Code.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Dein Floatee-Backlog über dem Prompt von Claude Code: Todos mit einem Klick…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Evangelion-Seitenleiste für Claude Code: Kontext, Kontingent, Aktivität, PRs…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Ein Claude Code-Mod, das es als The Machine aus Person of Interest neu…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code-Mod für obligatorische, verifizierte DAG-Workflows…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-Source-Mods für Claude Code: Bereiche, Statuszeilen, Toasts, Tool-Wächter…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code-Mod: Sitzungsstatus, Live-Spec Kit-Fortschritt und…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Das Kontextfenster als eine Zeile über der Eingabeaufforderung, dargestellt so…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Ein Live-Aufgaben-HUD für Claude Code Desktop: eine Leiste über dem Prompt…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Ein kostenloses, quelloffenes Plugin für Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Stash prompts for later and pop them back into Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude-Code-Mod, der Bilder inline in Ghostty und kitty anzeigt.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Ein Claude-Mod, der die GitHub Pull Requests der Sitzung in einem Bereich neben…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod: generate sound effects from text prompts with a local Stable…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-Skills: ein Faktenprüfer für Dokumentation, ein Code-Auditor, ein…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude-Code-Mod: die heutigen Codezeilen von Claude – neue, bearbeitete und…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude-Code-Mod: Anklickbare Pfade in Antworten – auf einen Ordner klicken, um…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-Buddy-Plugin: ein ASCII-Begleiter über deiner Eingabeaufforderung…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude-Code-Mod: Jev-gestützte Modell-/Aufwandsweiterleitung, wortgetreue…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code-Mods: Sicherheitsschicht für Claude Code – Geheimnis-Schwärzung…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-Plugin und -Mod: ein AI-nativer SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Sammlung großartiger Claude Code-Mods | Sammlung von Claude-Code-Mods.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Ein gemütlicher RPG-HUD-Mod für Claude Code.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: ein Claude Code-Mod, der Claudes Antworten und deine Prompts auf…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Versohle Claude, wenn es Mist baut – ein Stressabbau-Mod für Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude-Code-Mods: kleine Plugins für Live-Bereiche, kostenbewusstes…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude-Code-Mod und -Plugin: Nutzungsmonitor, Token-Tracker und Statuszeile.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude-Code-Mods. touch-map: Sieh als Baum und Aktivitätskarte, welche Dateien…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code-Mod, der live meldet, welche Dateien Claude geändert hat und warum…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code-Mods: Sitzungsstatistikkarten über dem Prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Eine animierte Braille-Katze über der Claude Code-Eingabeaufforderung.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude-Code-Mod: Leitet kostengünstige Aufgaben über einen untergeordneten…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Eine Pixelkatze über deinem Claude-Code-Prompt, die einen Testanruf mit einem…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Ein Claude Code-Mod, der einen geeigneten Zeitpunkt für die Komprimierung…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude-Mods für Claude Code: Token-Anzeige.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code-Plugin-Marktplatz von anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - General-purpose mods for Claude Code: bands, panes, toasts and hooks.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Das LGTM-Lines-Schiff segelt nach jeder Codeänderung vorbei — ein…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Deine Claude-Nutzungslimits als animierte Dorfbewohner-Gesundheitskarte mit…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Kurze Workouts, während Claude arbeitet: ein Tagesziel, Streaks, Badges und…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Plan-, Aufgaben- und Agentenfortschritt neben dem Claude Code-Prompt – ein…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Ein Nutzungs-Dashboard für Claude Code: Ausgaben pro Modell.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Ein Claude-Code-Mod: Live-Aufschlüsselung des Kontextfensters über dem Prompt.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude-Code-Mod, der den Countdown des Prompt-Caches in der Fußzeile anzeigt…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now-Playing-Mod für Claude Code: Apple Music und Spotify über der Eingabe, mit…
- [benlrice/logpane](https://github.com/benlrice/logpane) - Claude Code mod: a pane that tails the files your Bash calls write to.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods für Claude Code: Cache-Uhr, Blast Radius, Vorschläge, Arbeitsliste, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Nur eine Eule für deinen Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Einzeiliges Claude Code-Band.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Die originale Doom-Engine mit Freedoom, spielbar innerhalb von Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Ein Claude-Code-Mod, der eine laufende Liste der offenen Punkte eines Gesprächs…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Überprüfe jede Datei, die Claude anfasst, wie bei einem Pull Request, ohne das…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude-Code-Mods für echte Engineers.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Ein Tamagotchi, das in Claude Code lebt: Es schlüpft, frisst den Code, den…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Claude-Code-Mods, als Funktions-Hooks geschrieben, und der Marktplatz, der sie…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude-Code-Mod: Nachdem ein Guard einen Tool-Aufruf blockiert hat, stoppt er…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude-Code-Mod: Hintergrundaufträge in einer Ansicht, mit aus der…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude-Code-Mod: ein Posteingang für Nachrichten von Teammitgliedern, benannten…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude-Code-Mod: Erklärt Sandbox-Blockierungen und wandelt wiederholte…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoriten für Claude Code: Ein-Klick-Symbole für deine Befehle und Skills.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hey, stummgeschaltet! Schluss mit Diff, kürzt den Riff, keine weiteren…
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code-Mods: delete-guard (Löschen von Dateien bestätigen) und…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Claude-Code-Mod: Abonnementnutzung.
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude-Code-Mod: deine Hintergrundagenten als Pixel-Kreaturen, ein Sprite pro…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Ein Live-Radar deiner parallelen Branches und Worktrees über dem Prompt: welche…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Ein Claude Code-Mod zum Erfassen von Gedanken während der Arbeit, ihrer…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Strg+Klick zum Kopieren des Links in jedem Codeblock in Claude Code-Antworten…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code-Mods (Function-Hook-Plugins), installiert über einen einzigen…
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code-Mods: context-bar-plus (Kontextleiste, Kontingent, Subagent-Modi).
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude-Code-Mod: Erfasse Ideen aus jeder Sitzung in einem…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-Mod: wie lange jede Antwort dauerte, wie lange Claude nachdachte…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code-Mods: Der Streamer-Modus blendet private Bereiche, Bänder und die…
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook plugins (mods).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude-Code-Mod: wartet das Fünf-Stunden-Nutzungslimit ab und sendet für Sie…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Ein Cockpit über deinem Claude Code-Prompt. Die Ente liest die Anzeigen ab.
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code mod: sidebar file tree that pulses on files Claude just edited.
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: ein Claude-Code-Mod mit einem Seitenbereich, der zeigt, an…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Ein Claude Code-Mod: ein Bereich für jeden Subagenten, die von ihm berührten…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Kontextnutzungsbereich in der Seitenleiste: Gesamtmenge, Kategorien, Wachstum…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Dateiliste in der Seitenleiste: Welche Dateien in dieser Unterhaltung neu…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 im 8-Bit-Stil (schwarz-weißes holländisches Hängeohrkaninchen) läuft und…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - „Meine Fragen“ in der Seitenleiste: Jede Nachricht, die der Benutzer in dieser…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Zeitachse in der Seitenleiste: Wofür die Zeit in dieser Runde aufgewendet wurde…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Token-Verkehr in der Seitenleiste: Wie viele Token die Hauptunterhaltung bei…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Die ehrliche Bohnenpaste von claude code: Nach jeder abgeschlossenen Runde sagt…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Kleine Mods für Claude Code, etwa neue Slash-Befehle und Seitenbereiche.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd lebt in einem Band über deinem Claude Code-Prompt: stellt die Sitzung…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Ein Mod, der Antworten und Benachrichtigungen von Claude Code mit VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Ein Claude-Mod zum Lesen und Zusammenführen der Unterhaltungen zwischen deinen…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude-Code-Mods. PixBar: eine Pixel-Kreatur über deinem Prompt, die sich mit…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude-Code-Mod: Laufende Subagenten als Pixel-Claude-Maskottchen über dem…
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code-Mods (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Zwei Claude Code-Mods: folio, ein Dateibereich neben dem Chat, und tint, eine…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: ein Live-Graph darüber, was Claude Code weiß.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Lass deine Aufmerksamkeit nicht abschweifen, während du auf die Antwort von…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Ein von der Community kuratierter Leitfaden zu Claude Code-Mods…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Ein Claude-Code-Mod, der anzeigt, was Claude im Untertitel des iTerm2-Tabs tut…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Eine flauschige schwarze Katze über deinem Claude-Code-Prompt.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Ein Claude-Code-Mod mit umschaltbaren Berechtigungsprofilen: eine sichere…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community-Mods für Claude Code: Wächter, Bereiche und Befehle, die innerhalb…
- [merrickxxx/grill-pane](https://github.com/merrickxxx/grill-pane) - Claude Code mod: grilling interviews with clickable answers in a side pane.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Seitenbereich für Claude Code: von Claude geschriebene Dateien…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude-Code-Mod: Prognose dessen, was von deinen wöchentlichen und 5-stündigen…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Ein ruhiger Seitenbereich für Claude Code: was diese Sitzung tut, ihr Plan…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Eine gedämpfte Zeitangabe über jedem Prompt und jeder Antwort im Claude…
- [mmedum/spor](https://github.com/mmedum/spor) - Stellt wieder her, was Claude Code ausblendet: die von Claude gelesenen…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code-Mod: Nutzung des Kontextfensters im Modus-Steckplatz der…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-Mod, der die Todo-Tools für Modelle wieder aktiviert, die sie…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod that waits for a safe pause, then hands your session over or…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-Mod: eine Zeile pro Aufgabe der Aufgabenliste über dem Prompt mit…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Spiele Vier gewinnt gegen eine AI innerhalb von Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude-Code-Mod: Wenn ein anderer Coding-Agent Änderungen in dein Repository…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude-Code-Mod für Repositories, die von mehreren KI-Agenten gemeinsam genutzt…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Marktplatz für Claude-Code-Mods.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Fun, free mods for Claude Code that never spend a token.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Eine Schutzschranke für SQL in Claude Code: Fragt nach, bevor Claude DELETE…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Ein Mod für Claude Code, Windows und CJK zuerst: Vorschauen eingefügter Bilder…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Die besten Claude Code-Mods, sortiert danach, was sie für Sie tun.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Zwei Claude-Mods für Claude Code: garde-du-corps.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Beschimpfe Claude Code, und eine Cartoon-Hand schlägt zurück.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live-Sitzungsstatistiken-Seitenbereich für den Code-Tab der Claude Desktop-App…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods für Claude Code: safety-guard blockiert destruktive Befehle und den…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code-Mod: Live-Aktienticker, /quote-Bereich, Preisalarme, Marktband und…
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code mod: a band above the prompt showing context used and a countdown…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code mod: a side pane that pins every diagram Claude draws and keeps a…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code mod: a dreaming pass that merges, rewrites and prunes Claude.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude-Code-Mod: hält den Auto-Memory im Hintergrund nach jedem Durchlauf…
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code mod: drops vague prompts before Claude sees them, and suggests the…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code-Mod: SSH-Host, RAM und 5h/7d-Nutzungslimits in einer Zeile über dem…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-Mod: Liegestütze, die man machen kann, während Claude arbeitet.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods for claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-Mod: verwandelt den im Planmodus genehmigten Plan in eine…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Eine handverlesene Liste von Claude Code-Mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenloser Modus: Hilfsagenten laufen auf Haiku, und große Dateien und Logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ein Lofi-Soundtrack, der der Sitzung folgt: Ruhe, Fokus, Flow sowie Hinweise…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Lerne, während Claude programmiert: Nach einem Durchlauf, der den Code geändert…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Ein Band mit jeder Änderung, die Claude vornimmt: Spiele jede Änderung ab…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - Ein Mod für claude code, der den Wechsel zwischen Konten ermöglicht.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Jeder Link, den deine Sitzung erwähnt, in einer Zeile über der…
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code Function Hooks – minimale Demo: ein Live-Token-/Kostenpanel über…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: ein inoffizieller Avengers-Fan-Mod für Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Claude-Code-Mod für Kontext, Wachstum, Quota, Cache, native Kosten und…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code-Mod: Leitet einfache Turns und Subagenten an günstigere Modelle…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - Das originale DOOM in einem Claude-Code-Bereich, ohne dass etwas installiert…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Ein-Klick-Commit-Nachrichten für Claude Code mit einer tanzenden…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — ein Claude Code-Mod, der die Nutzung deines Claude-Plans anzeigt…
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - Ein Claude-Code-Mod, der für jede Art von Arbeit das Modell und den Aufwand…
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Small mods that change how Claude Code looks and sounds.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Ein Claude-Code-Mod, der die aktuelle Sitzung in einem Bereich anzeigt: jede…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Ein Claude Code-Plugin-Marketplace für Mods: function-hooks-Plugins, die…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod: rewrites a rough prompt in place, naming fitting skills, open…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Anpassungen für Claude Code.
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude-Code-Mod: 5h/7d-Kontingent, Kontextfenster, verbleibende…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude-Code-Mod: animierte Fortschrittsleiste und Abschlusszusammenfassung für…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drei kleine Claude Code-Mods: Sieh, wann deine Subagents fertig werden, stelle…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Verkleinert große Screenshots, bevor Claude sie liest, damit lange Sitzungen…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Sag „I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Zeigt vorgeschlagene nächste Prompts über dem Prompt-Feld an.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stelle Claude eine Nebenfrage in einem Bereich neben deiner Arbeit.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace für Claude Code-Mods mit Ein-Schritt-Installation und…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Countdowns für Ratenbegrenzungen und eine Prognose der Verbrauchsrate für…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods para o Claude Code: faixa de limites de uso (5h/semanal) e painel de…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code-Plugin: deine Claude-Pro/Max-Nutzungslimits mit einer…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods für Claude Code. agent-crew: Beobachte deine Subagenten bei der Arbeit als…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Inline- und angezeigte LaTeX-Mathematik sowie optionale TikZ-Abbildungen in den…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Ein Live-Aufgabenboard für Claude Code: vor dem Erstellen planen, jede Aufgabe…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Eine handverlesene Sammlung der besten Ressourcen für die großartigsten…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Ein Claude-Code-Plugin, das anzeigt, was gerade geschieht – Kontextnutzung…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Wunderschöne, hochgradig anpassbare Statuszeile für Claude Code CLI mit…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle Teile des System-Prompts von Claude Code, 27 integrierte…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Mehr als 45 Tipps, um Claude Code optimal zu nutzen, von den Grundlagen bis zu…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Schöne Powerline im Vim-Stil für Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Überprüfe den Diff deines Coding-Agents in einem Terminalbereich und sende…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Umfassendes Statuszeilen-Plugin für Claude Code mit Kontextnutzung…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Build mods for Claude Code: Hook any request, modify any response, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - A comprehensive statusline dashboard for Claude Code — session info, quota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: track the carbon footprint of your Claude Code sessions.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - An aesthetic statusline for Claude Code by awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness Langform-Rollenspiel-Agent（DSH-Tavernen-Plugin）: Import von…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Public Claude Code skills and mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash commands and guides for Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legal free LLM APIs &amp; coding agents — self-updating, probe-verified twice a…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Schneller, abhängigkeitenfreier Kostenrechner und anpassbare Statuszeile für…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Terminal-Statuszeile für Claude-Code-Sitzungen.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live-Fußballergebnisse, Spielpläne und Tabellen für den Wettbewerb, dem du…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Lokale Steuerungsebene für Claude Code auf Windows und macOS: LLM Gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill that turns your coding agent into a keyboard firmware expert.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Persönliche Claude Code-Konfiguration, versioniert innerhalb von ~/.claude…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebetszeiten, Hijri-Datum, Adhkar, täglicher Ayah, freiwilliges Fasten…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Image generation &amp; visual processing suite for DeepSeek Harness: pluggable…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Zweizeilige Truecolor-Statuszeile für Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Eine schwebende Gezeitenkarte für Spitzen- und Nebenzeiten in DeepSeek Harness…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Portables Claude Code-Toolkit für .NET DDD/Clean Architecture: strikte…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Portable globale Konfiguration für Claude Code: benutzerdefinierte Fähigkeiten…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-Plugins, die ich täglich verwende: Skills und Mods, aufgeräumt…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, a Tamagotchi companion mod for Claude Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace for Claude Code Plugins and Skills to facilitate mods of the game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token-Verwaltung für Claude Code: Das Topmodell gibt die Richtung vor, die…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live-Statuszeile für Workflow-Phasen in Claude Code.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository for Claude Code Awesome Media mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Senke die Tokenkosten von Claude Code &amp; Codex: Leitet Abfragen und Testläufe an…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Einfache und nützliche Statusline-Einrichtung für Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Nutzungslimit-Warnungen für Claude Code: macOS-Benachrichtigungen…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Zeigt die Statuszeile von Claude Code mit Ratenlimits, aktuellem Verzeichnis…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Konfigurierbare Claude Code-Statusleiste für Linux, WSL, Windows und macOS, mit…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Schnelle Rust-Statuszeile für Claude Code — Payload zuerst, gecachtes Git…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Ein Live-Nutzungsdashboard für Claude Code — Kontextaufschlüsselung…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Eine Status- und Tokenzeile für Claude Code: Kontext, 5-Stunden- und…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Wichtige Statusdetails für Claude Code anzeigen, darunter Modell, Kontext…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Mehrzeilige Claude Code-Statuszeile: Ausgaben, Kontext-%, Git und aktiver…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statuszeile mit nützlichen Informationen für claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Native Agententeams. Unter Kontrolle. Strikte Arbeiterlimits, Live-Sichtbarkeit…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code-Add-ons: farbiger Punktwächter für den Tab-Status plus gebündelte…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code-Statuszeile für macOS und Linux, verpackt als…
- [alexleveled/claude-read-aloud](https://github.com/alexleveled/claude-read-aloud) - Hear Claude Code.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Benutzerdefinierte Statusline für Claude Code — Kontextleiste mit…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Eine übersichtliche, informative Statuszeile für Claude Code — zeigt Projekt…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT-HUD-Mod: ein Statuspanel im CRT-Stil für Claude Code, im Terminal…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code-Plugin-Marktplatz mit baloo: Fähigkeiten, ein Agent, der Änderungen…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionelle Claude-Code-Statuszeile: Sitzungsdauer, Kosten in mehreren…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Abonnementbewusste Statuszeile für Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Eine umfangreiche Terminal-Statuszeile für Claude Code — Bun + TypeScript…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Claude Code-Plugin, das Mermaid-Diagramme im Transkript ansprechend darstellt…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, Skills und Agenten für Claude Code — beginnend mit einer Statuszeile…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Benutzerdefinierte Statuszeile für Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Echte DeepSeek API-Ausgaben für Claude Code: bepreist Sitzungs-Transkripte neu…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Vorschaubilder innerhalb von Claude Code anzeigen: Bewege den Mauszeiger über…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code-Statuszeile mit Agentenpanel-Zeilen.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronisiere Claude.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code-Einstellungsmenü, Statusline und Konfiguration.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Verfolge den Status von Claude Code mit einem kompakten Dashboard, das Kontext…
- [msetsma/claude-style](https://github.com/msetsma/claude-style) - Claude Code style mod: prompt bubbles, tool-call cards and rails, framed bands…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code-Umgebungsinstaller: Skills, Statuszeile, Hooks, Berechtigungen und…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - HUD-artige Statuszeile für Claude Code – Netzwerkzustand, TPS, Kontext…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude Code-Plugins und -Mods, um zu verstehen, was Claude tut: übersichtliche…
- [pbhwheeler/claude-config](https://github.com/pbhwheeler/claude-config) - Portable Claude Code config: settings.json, hooks, status line, and a bootstrap…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Farbenfrohe mehrzeilige Statusleiste für Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code-Statuszeile für Windows (PowerShell): Nutzungsleisten…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Tragbare Konfiguration für Claude Code (Statuszeile + Installationsprogramm).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Ein kleines Dashboard für Claude Code: Kontext %, Cache-Countdown, 5-Stunden…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Benutzerdefinierte Terminal-Statusleiste für Claude Code: Modell, Verzeichnis…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Portierbare Claude-Code-Konfiguration: CLAUDE.md, Einstellungen, Statuszeile…
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code-Desktop-(macOS)-Mod: Sitzungsbenachrichtigungen zum direkten…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Screenreader-Begleitmod für Claude Code (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Ein praxisnaher, verifizierter Deep Dive in Claude Code — CLAUDE.md, Subagents…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Statuszeile zur Echtzeit-Kostenverfolgung und Sitzungsüberwachung für Claude…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude-Code-Skill (VS Code, Windows): Bildvorschauen und Schaltflächen zum…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Eine Claude Code-Statuszeile: Ordner, Git-Branch, Modell, Nutzung des…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Kontextverfall-Detektor 2026 – Proaktiver KI-Speicher- und Ratenlimit-Monitor…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-Hooks, Subagents und Statuszeilen: Open-Source-Sammlungen und Tools…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Ein visueller Builder für Claude-Code-Statuszeilen.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude-Code-Statuszeile mit Echtzeit-Tokenverbrauch und geschätztem…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods for Claude Code: panes, bands and buddies built on function hooks.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pass tasks between your Claude Code sessions.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - This in a MCP server to control MODS, the modular cross platforms tool for…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex and Claude Code skill for translating CK3 mods with a local LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods and other extensions for Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code-Statuszeile: Ästhetik von CCometixLine + HUD-Funktionalität von…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: find what you ask Claude Code again and again, and turn it into a…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## DSH- und Cordis-Plugin-Ökosysteme

DeepSeek Harness und Cordis erreichen dasselbe Ziel aus einer anderen Richtung: Für sie ist das Plugin der Mod-Mechanismus, daher entspricht ein Plugin dort einer Mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74336 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **74336**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100521 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **100521** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐91711 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **91711**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81929 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **81929**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| Sterne            | **35760**  |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25495 · Python · 🔎 inferred · 19 天</summary>

##### 📝 Zusammenfassung

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **25495**  |
| Letzter Push      | 2026-09-22 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18380 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **18380**  |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8629 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **8629**   |
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
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐8510 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **8510**   |
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
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6159 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Der Plugin-Markt in DeepSeek Harness — durchsuchen, suchen, mit einem Klick installieren · DSH 可视化插件市场

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **6159**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4486 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness（DSH）Eine kleine Wal-Maid, die in der unteren rechten Ecke der DSH-Oberfläche lebt und Ihnen hilft, das Guthaben Ihres DeepSeek-Kontos im Blick zu behalten. Niedlich und federnd, mit Drag-and-Drop-Andocken, Umkehrung beim Andocken an der linken Seite und animiertem Zahlenlauf. Wird automatisch mit der Oberfläche aktiviert. Es wird empfohlen, sie direkt mit Ihrer dsh-Installation zu holen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **4486**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4286 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **4286**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4107 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, side chat, Git, and sub-agent pages.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **4107**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>animierte Aufzeichnung · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3119 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness Tauri-Desktopversion | Nur 8 MB Installationsprogramm, keine Einrichtung der Umgebung, vorinstallierte Plugins, Windows / macOS / Linux.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **3119**   |
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
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1406 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **1406**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

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
| Sterne            | **1171**   |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **704**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
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
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐334 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **334**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐284 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Einfach den Browser öffnen — erledige deine gesamte Arbeit.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **284**    |
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
| Letzter Push      | 2026-10-11 |
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

Zeitversetzte Aufgabendelegation für DeepSeek Harness (dsh): Planen Sie Aufgaben in Ruhe, lassen Sie sie unbeaufsichtigt außerhalb der Spitzenzeiten ausführen und kehren Sie zu einem Bericht zurück. Von Menschen beurteilt, Desktop + Web.

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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐133 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Laufzeitnachweise, die Agents dabei unterstützen, Hotspots in Anwendungs- und nativem Code, GPU-Kernels und Inferenz-Stacks nachzuverfolgen, zu profilieren und zu beseitigen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **133**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐132 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **132**    |
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
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness 桌宠插件：元气鲸鱼娘看板娘陪你写代码 🐋 支持 DSH 桌面端 0.2.0-rc.2 与旧版 Web（desktop pet / mascot，local-first）

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **120**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DSH-Plugin · injektionsbasierter Optimierer 0.8 (Hauptzweig): Du sprichst wie gewohnt, und nach dem Absenden und vor dem Empfang durch die AI klärt es, was „diese Runde eigentlich benötigt“, und übergibt dieses Verständnis an die Arbeits-AI (Kontextinjektion) — der Originaltext wird nicht umgeschrieben, jede Aussage wird wörtlich belegt. Enthält eine Steuerungsoberfläche (Stufe/Berechtigungen/Modell/Kontext/Lesewerkzeuge), eine Abfang-Overlay (Denkebene + Ausgabebene) sowie den tatsächlichen Token-Verbrauch. Kann die Leistungsstabilität der meisten Modelle deutlich verbessern, insbesondere von DeepSeek-V4.1-Flash, und zu einer spürbaren Verbesserung führen

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **113**    |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/JingbiaoMei/Tokdash">JingbiaoMei/Tokdash</a></b> · ⭐85 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Agent Dashboard: Visualization and analytics for Sessions and Quota Usage. Track, analyze, and optimize token usage across providers with heatmaps, cost tracking, token counting and quota resets..

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **85**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent` · `analytics` · `anthropic` · `claude-code` · `claude-code-plugin` · `codex` · `codex-cli` · `dashboard`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jingbiaomei--tokdash/cb7e85100dfe6e93.png" width="100%" alt="JingbiaoMei/Tokdash screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐66 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Desktop-Agent auf Basis des Deepseek-Harness-Kerns. Übernimmt alle Fähigkeiten der Basis und ergänzt IDE-bezogene Funktionen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **66**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Das lebendige DeepSeek Harness-Plugin-Verzeichnis — stündlich aktualisiert, täglich auf Kompatibilität getestet, mit In-App-Plugin-Store und Scaffolder. Lebendiges DSH-Plugin-Verzeichnis: stündliche Aktualisierung, tägliche reale Kompatibilitätstests, integrierter Plugin-Store und Scaffolder.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | HTML                                                                                           |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **59**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Contexera/dsh-agent-team">Contexera/dsh-agent-team</a></b> · ⭐57 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

dsh-agent-team gives DeepSeek Harness agents that don't reset: durable Members with their own memory, notes, and skills across sessions, rollovers, and restarts. You set the direction; agents coordinate through Channels and Tasks.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **57**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent-orchestration` · `agent-team` · `ai-agents` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `multi-agent`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/contexera--dsh-agent-team/25f8cc5a2a3231a3.png" width="100%" alt="Contexera/dsh-agent-team screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Aufgabenbewusster Abruf von Arbeitsbereichskontext und Lifecycle-Tracking für AI Coding Agents: Findet, organisiert und verfolgt fortlaufend die für die aktuelle Aufgabe relevantesten Dokumente, Codes und Medien. Rein lokal, null Modellaufrufe, null Netzwerk. Aufgabenbewusster Arbeitsbereichskontext-Abruf und Lifecycle-Tracking für AI Coding Agents. Finde, organisiere und verfolge den für die aktuelle Aufgabe relevantesten Arbeitsbereichskontext — lokal, deterministisch, null Modellaufrufe, null Netzwerk.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **53**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐43 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

dsh Spiel-Asset-Meister-Plugin. Bindet das seedream Bildgenerierungsmodell und das minimax Videogenerierungsmodell ein und kann verschiedene Spiel-Assets generieren.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **43**     |
| Letzter Push      | 2026-10-11 |
| Erstmals gelistet | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mehr in dieser Kategorie</b> <sub>· 67</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - A pre-execution guard for AI coding agents.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Eine kuratierte Liste der besten großartigen KI-Plugins für KI-Assistenten…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH-Plugin — kostenlose OpenCode-Zen-Modelle für DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-Plugin-Marktplatz / DSH Plugin Marketplace: Im DeepSeek Harness Web GUI mit…
- [arcships/rutis](https://github.com/arcships/rutis) - Eine Plugin-Laufzeitumgebung für Software, die sich selbst weiterentwickelt…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [PensiveFei/dsh-secure-audit](https://github.com/PensiveFei/dsh-secure-audit) - Read-only security &amp; compliance plugin for DeepSeek Harness: prompt-injection…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Ausgewähltes Verzeichnis für DeepSeek Harness-(DSH)-Plugins — über 280…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 插件：维护 llm-pi-ai 模型的准确上下文窗口，避免长会话被误判为上下文溢出.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zotero-Toolkit für DeepSeek harness; verwandle deine Zotero-Bibliothek in einen…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH-Plugin: Git-Bash-Shell für alle Agentenmodi auf Windows.
- [PensiveFei/deep-read-summarize](https://github.com/PensiveFei/deep-read-summarize) - Workflow zum intensiven Lesen und Zusammenfassen von Büchern…
- [gulagala001/oh-my-dsh](https://github.com/gulagala001/oh-my-dsh) - 让你的 DSH，火力全开。长上下文、任务验证、提示词优化、代码理解、电脑操作与四套完整主题.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH-Web-Plugin: Remote-Entwicklung ähnlich wie VSCode Remote-SSH.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: plattformübergreifendes Gruppenchat-Agentensystem auf Basis von…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - Das Büro-Dreierpack! Office-Dokumentwerkzeuge für DeepSeek Harness (dsh)…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh für Android: integriert DeepSeek Harness, eine Ubuntu-Laufzeitumgebung…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH-Web-GUI-Plugin-Sammlung (DeepSeek Harness) — Aufgabenbenachrichtigungen…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH 会话导航.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH Web-Plugin: tägliche Token-Nutzungsstatistiken mit einer GitHub-artigen…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Von der Community kuratierte DeepSeek-Harness-(dsh-)Plugins, Tools, Skills und…
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - MCP-Serververwaltungs-Plugin für DeepSeek Harness: Seite Einstellungen → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness-Plugin: 15 obra/superpowers Engineering-Skills, zweisprachige…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A-Laufzeitumgebung für Handelsverhandlungen + DeepSeek-Harness-(dsh-)Plugin.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Toolbox panel for DeepSeek Harness Web: MCP manager.
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - Chuigengji: Eine Roman-Arbeitsumgebung für Da Feiyu.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 插件 · 发送栏一键「优化」提示词草稿：五维诊断 + 改写稿 SSE 流式上屏，可替换 / 复制 /…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Ein echtes PowerPoint, kein HTML. Sag deiner KI, was abgedeckt werden soll, und…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Eingebettetes C/C++-AI-Engineering-Plugin — Firmware-Skills.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - All-in-one-Verwaltung für Skills, Subagenten, MCP und LSP für DeepSeek Harness…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [sueccku/dsh-plugin-wps-office-next](https://github.com/sueccku/dsh-plugin-wps-office-next) - 在 DeepSeek Harness（DSH）里用中文对话操作 WPS 表格 / 文字 / 演示：读写数据、排版、公式图表、批量转 PDF.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Permanente Kompatibilitätstests für DeepSeek Harness-Plugins: exakte Releases…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive Kontextkomprimierung für Local-First-Agents.
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [chengshenyangtai/dsh-workbuddy-trae-qoder-connect](https://github.com/chengshenyangtai/dsh-workbuddy-trae-qoder-connect) - 把 WorkBuddy（多账号/企业版）、Trae CN / TRAE SOLO CN、Qoder CN 三家订阅聚合进同一个 DSH…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Röntgenblick für DeepSeek Harness-Plugins: deklarierte Fähigkeiten im Vergleich…
- [zzhang82/Agent-Memory-Bridge](https://github.com/zzhang82/Agent-Memory-Bridge) - Persistent engineering memory for coding agents over MCP.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH-Plugin: Die Modelle der WorkBuddy-Desktop-App mit DeepSeek Harness…
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - Ein Wissensdatenbank-Toolkit für Recherche und Literaturübersicht.
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [xyrrrrr-r/dsh-eval-control](https://github.com/xyrrrrr-r/dsh-eval-control) - Host-side DSH evaluation control plugin for aeval：一次评测试次的配置注入、预算封顶与证据归属.
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - 设计与代码的声称核验：事实类对照源码，行为类跑可执行模型；含结构/依赖审查（单层与多粒度细化）、UML 审查、基线对比与导出.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Arbeitsbereich mit mehreren Ordnern: Ermöglicht dem DSH-Agenten.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Verifizierungsstandard ohne Abhängigkeiten für DeepSeek-Harness-(dsh-)Plugins –…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) plugin: one-click OpenCode Go model sync in the settings…
- [umineko987/dsh-search-enhance](https://github.com/umineko987/dsh-search-enhance) - 提供 Grok-compatible 网页搜索、保留来源分页、Context7 与 Exa 文档检索、有界网页提取、站点映射、离线研究计划和只读诊断.
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode auf DeepSeek Harness — DSH-Plugin, das OpenCode Zen + Go-Modelle der…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — Marktplatz für Plugins von Drittanbietern und geschützter…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx ist eine menschenorientierte, erweiterbare Desktop-Arbeitsumgebung…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Ein Coding-Agent mit allem Drum und Dran für DeepSeek Harness — Claude…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — Community-Versionsmaschinen-Deployment- und Betriebssuite für…
- [SuperWheel/cliworker-now](https://github.com/SuperWheel/cliworker-now) - DeepSeek Harness 多 CLI 智能体侧栏插件：独立对话、账号管理、角色预设与任务续聊.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) Web-Plugin: Market-Dashboard-Seitenleiste zur…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Macht einen nicht zugeordneten leeren Modellversuch erneut versuchbar, für die…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins, die selbst aufräumen: eine Swift-6-Portierung des…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek-Harness-Agent-Voreinstellung: Codex und Claude Code als…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Eine Rust-Plugin-Laufzeitumgebung mit einem durch Verus verifizierten…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [ArisaYamatogi/dsh-lecture-copilot](https://github.com/ArisaYamatogi/dsh-lecture-copilot) - A Dsh plugin that automatically records, translates lecture and generates notes…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 338      | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 79       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 40       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 24       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12       | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 5        | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 5        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| PowerShell | 2        | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1        | `reporails/arcade`                                                                                            |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1        | `dphmoblie/deepseek-harness-android`                                                                          |
| Swift      | 1        | `eovidiu/cordis-ios`                                                                                          |

<sub>Es werden nur Einträge gezählt, die eine Sprache angeben. Dokumentations- und Diskussionseinträge sind von dieser Tabelle ausgeschlossen.</sub>

## Mitwirken

Korrekturen sind willkommen und der schnellste Weg, diese Liste zu verbessern. Erstelle ein Issue oder einen Pull Request, wenn ein Eintrag falsch einsortiert oder falsch eingestuft wurde oder ein Projekt aufgrund einer Namenskollision zu Unrecht ausgeschlossen wurde — in dieser letzten Kategorie sind automatisierte Filter am wahrscheinlichsten fehlerhaft.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Zuletzt aktualisiert · 2026-10-11T23:26:48+08:00</sub>
