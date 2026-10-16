<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Hervorragende Claude-Mods">
</p>

<h1 align="center">Hervorragende Claude-Mods</h1>

<p align="center"><b>Das evidenzbasiert bewertete Verzeichnis der Claude-Code-Mods und -Plugins sowie des tiefergehenden Verhaltens, das sie verändern.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-597-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <b>Deutsch</b> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Aktuelles Verzeichnis** · Letzte Synchronisierung: `2026-10-16T14:49:31+08:00` (UTC+8)
> · Einträge: **597** · Mit der letzten Aktualisierung hinzugefügt: **0** · Implementierungssprachen: **17**

<sub>Jeder Eintrag unten wurde automatisch erfasst, gefiltert und erneut überprüft. Nichts davon ist bezahlte Platzierung.</sub>

<a id="featured"></a>

## Auswahl des Augenblicks

<sub>Ein Eintrag pro Kategorie, sortiert nach Evidenzgrad und Sternen und bei jeder Aktualisierung neu berechnet. Eine Rangliste, keine Empfehlung; jede Auswahl führt weiter zur vollständigen Karte unten. Projekte, die einen Screenshot oder eine Aufzeichnung veröffentlicht haben, werden bevorzugt, damit die Leiste visuell bleibt.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9528 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2573 · Python · 👁️ observed</sub>
<sub>Finde die Geister-Token. Behebe sie. Überlebe die Komprimierung. Vermeide den Verfall der Kontextqualität.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐75283 · TypeScript · 👁️ observed</sub>
<sub>🌊 Der ursprüngliche Agent-Harness. Setze intelligente Multiplayer-Schwärme ein, koordiniere autonome Workflows und entwickle konversationelle KI-Systeme. Mit…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## Inhalt

- [Was ein Claude-Code-Mod ist](#was-ein-claude-code-mod-ist)
- [Wie Einträge bewertet werden](#wie-einträge-bewertet-werden)
- [Offiziell: Eigene Repositories und Release Notes von Anthropic](#offiziell-eigene-repositories-und-release-notes-von-anthropic) — **17**
- [Mods: mit der Mod-Funktion erstellt](#mods-mit-der-mod-funktion-erstellt) — **475**
- [DSH- und Cordis-Plugin-Ökosysteme](#dsh--und-cordis-plugin-ökosysteme) — **94**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151120 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Zusammenfassung

Claude Code ist ein agentisches Programmierwerkzeug, das in deinem Terminal ausgeführt wird, deine Codebasis versteht und dich durch die Ausführung routinemäßiger Aufgaben, die Erklärung komplexen Codes und die Verwaltung von Git-Workflows schneller programmieren lässt – alles über Befehle in natürlicher Sprache.

<sub>🔧 Im Code gefunden: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                             |
| --------- | ---------------------------------------------------------------- |
| Kategorie | `Offiziell: Eigene Repositories und Release Notes von Anthropic` |
| Beleg     | `von Anthropic selbst veröffentlicht`                            |
| Sprache   | TypeScript                                                       |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **151120** |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9528 · TypeScript · ✅ official · 0 天</summary>

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
| Sterne            | **9528**   |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8289 · Python · ✅ official · 0 天</summary>

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
| Sterne            | **8289**   |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6395 · Python · ✅ official · 246 天</summary>

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
| Sterne            | **6395**   |
| Letzter Push      | 2026-02-11 |
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

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
| Sterne            | **1813**   |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>Mehr in dieser Kategorie</b> <sub>· 5</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `$.ui.notify` für Mods hinzugefügt: sendet über deine eigene…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Behoben: Esc oder ein Interrupt während eines `UserPromptSubmit`-Hooks oder des…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod.

</details>

<a id="mods"></a>

## Mods: mit der Mod-Funktion erstellt

Jeder Eintrag hier belegt die Verwendung der Funktion, die Claude Code in 2.1.287 erhalten hat: Er zeichnet über `ui.render`, besitzt ein Pane, Band oder eine Karte, liest `$.ui.selection()`, startet mit `agent.spawn` Teammitglieder oder bezeichnet sich ausdrücklich als Mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2573 · Python · 👁️ observed · 0 天</summary>

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
| Sterne            | **2573**   |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐852 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

Custom Claude Code Mods that I need

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **852**    |
| Letzter Push      | 2026-10-14 |
| Erstmals gelistet | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐604 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Community-Katalog öffentlicher Claude Code-Mods (Funktions-Hooks), aus GitHub gescannt, einschließlich der Informationen, was jeder Mod lesen, schreiben, ausführen oder über das Netzwerk senden kann. https://mods.aidojo.si/ durchsuchen

<sub>🔧 Im Code gefunden: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **604**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐259 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Claude-Code-Mods: Plugins auf Hook-Basis, die Live-Zeilen über der Eingabeaufforderung, Schutzfunktionen, Bereiche und Spiele hinzufügen. Kontextleiste, Nutzungsanzeige, Codex-Review-Überwachung, Markdown-Vorschau, aktuell abgespielter Spotify-Titel und mehr.

<sub>🔧 Im Code gefunden: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **259**    |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐218 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **218**    |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐208 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Mods for Claude Code. effortless picks the reasoning effort for every prompt and shows the cache countdown. textless shows art, quotes and chess instead of the wall of text while Claude works.

<sub>🔧 Im Code gefunden: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | HTML                                                                      |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **208**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `ai-tools` · `anthropic` · `chess` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐196 · TypeScript · 👁️ observed · 11 天</summary>

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
| Sterne            | **196**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐154 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **154**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐116 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **116**    |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐107 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 Im Code gefunden: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **107**    |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐94 · TypeScript · 👁️ observed · 3 天</summary>

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
| Sterne            | **94**     |
| Letzter Push      | 2026-10-12 |
| Erstmals gelistet | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Zusammenfassung

Eine Sammlung von claude code-Mods

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **80**     |
| Letzter Push      | 2026-10-08 |
| Erstmals gelistet | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

Claude-Code-Mods: Live-Fortschrittsbalken für Pläne über der Eingabeaufforderung

<sub>🔧 Im Code gefunden: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **54**     |
| Letzter Push      | 2026-10-14 |
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐36 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **36**     |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **30**     |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **30**     |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Zusammenfassung

Claude Code-Mods: Claude-Tools-Menü, Zen-Modus, Terminal-Themes, Steuerungen für Aufwand und Modus

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **24**     |
| Letzter Push      | 2026-10-14 |
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Zusammenfassung

Claude-Code-Mods: 21 Stile und ein vollständiger Funktionsumfang, den du bei Bedarf für das Terminal und die Desktop-App aktivierst. · Verleihe Claude mit einem Klick einen neuen Stil und erhalte einen vollständigen Satz bedarfsgesteuert aktivierbarer Funktionen.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **22**     |
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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐20 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Claude-Code-Mod: Clawd stellt über dem Prompt dar, was Claude tut

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
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

##### 📝 Zusammenfassung

Zehn Claude-Code-Mods, Einsteigeranleitungen, Erstellungs-Prompts, sichere Demos und eine Vorlage zum eigenen Erstellen.

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 Zusammenfassung

Zwei Claude-Code-Mods: Codex-Computer-Use-Bridge und koordinierte Claude-Sitzungen. Quellcode, Build-Prompts, Einrichtung und Tests.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | JavaScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **16**     |
| Letzter Push      | 2026-10-05 |
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/rashedInt32/glass">rashedInt32/glass</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Desktop-App-Optik für das Terminal-Transkript von Claude Code, als Mod

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **15**     |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `markdown` · `syntax-highlighting` · `terminal-ui`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/rashedint32--glass/c7b07954a39be0b7.png" width="100%" alt="rashedInt32/glass screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Zusammenfassung

LINE innerhalb von Claude Code: die enil-TUI als Claude Code-Mod

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **15**     |
| Letzter Push      | 2026-10-13 |
| Erstmals gelistet | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Sterne            | **14**     |
| Letzter Push      | 2026-10-03 |
| Erstmals gelistet | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Zusammenfassung

Zehn Open-Source-Mods für Claude Code: Live-Bereiche, Bänder, Statuszeilen und Schutzfunktionen für Tool-Aufrufe. Verbrauchsanzeige, Startcodes, Sitzungsabschluss, Bosskampf, Code-Haustier und mehr.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `Mods: mit der Mod-Funktion erstellt`                                     |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **14**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Zusammenfassung

Claude-Code-Mods, die die Fragen von Claude leichter lesbar und beantwortbar machen (qa-guide).

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **12**     |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 Zusammenfassung

KOZMOS — visuelle Live-Mods für Claude Code (CLI + Desktop): Leisten über der Eingabeaufforderung, Seitenleisten, Status-Ticker, Begleiter, Wächter und Sound.

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
| Sterne            | **12**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐11 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **11**     |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Zusammenfassung

Lass den Claude-Pro-Tarif länger reichen: Claude Code-Mods für eine genaue Nutzungsanzeige, kürzere Shell-Ausgabe und keine wiederholten Dateilesevorgänge. Die Mods verbrauchen null Tokens.

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
| Letzter Push      | 2026-10-09 |
| Erstmals gelistet | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 30 天</summary>

##### 📝 Zusammenfassung

Claude Code mods: context window, plan quota burn rate, per-turn cost, and a budget guard that stops the session past a limit

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Eine Benutzeroberfläche für deine Claude Code- und Codex-Terminals, die deine Agenten erstellen, damit das einzige Modell in deinem Kopf deines ist.

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
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Zusammenfassung

Sechs Claude Code-Mods in einem Plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) mit Schaltern pro Mod sowie ein Mods-vs.-Hooks-Bericht.

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Zusammenfassung

Sammlung von Claude Code-Mods von 개발동생. Taxi-Paket: Taxameter, Navigation, Geschwindigkeitsüberwachungskameras, Dashcam

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
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Ansehen auf youtube.com</a> · Die Wiedergabe wird auf der Host-Website geöffnet; GitHub kann sie nicht inline einbetten</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mehr in dieser Kategorie</b> <sub>· 441</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Sammlung von über 100 Mods, die du mit Claude Code verwenden kannst.
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Claude-Code-Mods von Darrell Wang — Bänder über der Eingabeaufforderung, ohne…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Claude-Code-Mods von Ray Amjad: Bereiche, Bänder, Eingabeaufforderungswächter…
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Experten-Skills, Agenten, Befehle, Regeln, Hooks und Ausgabestile für Claude…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods und die Werkzeuge zu ihrer Erstellung: zuerst ein Builder-Skill…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Vier Claude-Code-Mods: Cache Keeper, Recording Mode, Goal Meter und Collision…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Das Claude-Code-Harness, das ich täglich ausführe, seit dem ersten Tag unter…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Gib Claude Code mit Claude Mods ein neues Dach: Ändere ohne Anpassung der…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Xcodes Build, Tests, Konsole und SwiftUI-Vorschauen innerhalb von Claude Code.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Quellenbelegte Obsidian-Wissensdatenbank über Claude Code-Mods: wie sie…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hackers Claude-Code-Mods: Mache die Arbeitsweise des Agenten…
- [kakha13/claude](https://github.com/kakha13/claude) - Claude-Code-Mods, die deine Prompts korrigieren und übersetzen, bevor Claude…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code-Mods und Skills von Nekyia Labs, täglich erstellt und genutzt von…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Ein Seitenbereich für Claude Code: die Subagenten, die eine Sitzung ausführt…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop-Seitenleistenbereich (Code-Tab): listet alle unerledigten und…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Nutzungsleiste über dem Eingabefeld von Claude Desktop (Code-Tab)…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (Function-Hook-Plugins) für Claude Code.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Eine schwebende Statuskarte für Claude Code – Modell, Kontext, Ratenlimits…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill, der Claude Code-Agenten beibringt, Claude Mods (Function-Hook-Plugins)…
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Eine Entscheidungswarteschlange CLI/TUI für Menschen, die mit…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Community-Claude-Mods, -Plugins und -Skills, über einen einzigen Marktplatz…
- [davekiss/mods](https://github.com/davekiss/mods) - Claude-Code-Mods von Dave Kiss.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, Schutzvorrichtungen und Komfort-Mods für Claude Code: Kontext, Nutzung…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code-Mods auf Abruf – ein Skill, der deine Unterhaltung liest und den…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Die Baselane-Mods-Galerie: Claude Code-Mods, geprüft und angeheftet.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Ein Tipp-Test für die Zeit, während Claude arbeitet. Eine Claude Code-Mod.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Ein App-Store für Claude-Code-Mods in Claude Code: Mit /mods 2.700 Mods…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sechs Claude-Code-Mods: Planlimits und Kontext über dem Prompt, ein Coach für…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Claude Code-Mod (Plugin), das einen Seitenbereich mit den Tabs Activity, Files…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Claude-Code-Mod, der Edit- und Write-Diffs in zwei nebeneinanderliegenden…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code-Mods: das Nutzungspanel usage-hud 像素螃蟹 + im Terminal anklickbare…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods für Claude Code: Function-Hook-Plugins, die Live-Bereiche und Verhalten…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code-Mods: screen-guard maskiert Namen und Geheimnisse beim Teilen des…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods und Skins für Claude Code: eine Live-Fortschrittsleiste für die Aufgaben…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code-Erweiterungen. Schalte die volle Leistung von Claude frei.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Zwei Claude Code-Mods zum gleichzeitigen Ausführen vieler Sitzungen: eine…
- [nsodhi-cmu/claude-code-ripple](https://github.com/nsodhi-cmu/claude-code-ripple) - Claude Code mod that creates graphical traces of your code changes.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Zwei Claude Code-Mods über dem Eingabefeld: Kontextfenster-Anzeige…
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Eigener Claude Code-Mod-Plugin-Marktplatz.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lies die Markdown-Dateien, die Claude Code benennt, neben der Sitzung…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow für Claude Code: eine ruhige Checkliste über dem Prompt, die Plan…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code-Mods: Kontextleiste, Agentenpanel, PDPA-Unschärfe.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code-Mod: Miniaturansichten eingefügter Bilder über der…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Sprach-Coworker für Claude Code. Besprich Dinge mit einem 3D-Wolf, der von…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code-Mods: typing-speed, ein Live-Tippgeschwindigkeitsmesser mit…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods für Claude Code: Bereiche, Befehle und Hooks, erstellt mit dem Plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Entdecke Claude Code-Mods, Plugins und Erweiterungen mit animierten Demos…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code-Mod: Mermaid-Diagramme direkt im Transkript gezeichnet.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Kleine Claude Code-Mods (Function-Hook-Plugins): session-switcher und mehr.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code-Mods: mod-scout.
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Narens Claude-Toolkit: Skills, Mods und MCP-Server für Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Eine Reihe von claude code-Mods, die ich erstellt habe.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code-Mods entdecken, prüfen, umschalten und aktualisieren.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Beste Claude Code-Mods: handverlesen, validiert, angeheftet.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude-Code-Mods für echte Engineers.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude-Code-Plugin: automatisches Routing des Claude-Modells.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sechs Mods für Claude Code: animiertes Clawd-Maskottchen, Nutzungsbegrenzungs…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Beim Coden ein Tee-Ei aufziehen, das langsam durchzieht · Ziehe beim Coden ein…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-Source-Mods für Claude Code: Bereiche, Statuszeilen, Toasts, Tool-Wächter…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code-Mod: Claude Punkt für Punkt beantworten, direkt im Text.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods für Claude Code: Clawd, ein winziges Pixel-Maskottchen, das darstellt, was…
- [reporails/arcade](https://github.com/reporails/arcade) - Klassische Desktopspiele als Claude Code-Mods, die in einem Bereich gespielt…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - Code-Mods für claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Ein Claude-Code-Mod, der deine globalen Skills, Agents, Regeln und Tools pro…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Getestete Claude Code-Mods mit Installation per einem Befehl…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Eine kuratierte Liste von Claude Code-Mods, installierbar als…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Zwei Claude Code-Mods: cache-keeper und ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code-Mods, die einen Agenten auf Kurs halten — Function Hooks, die den…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Ein Claude Code-Mod zum Festhalten von Gedanken während der Arbeit, zum…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Hermans Claude Code Mods (Marktplatz herman-mods).
- [jrlprost/claude-code-mods](https://github.com/jrlprost/claude-code-mods) - Claude Code mods I build because I need them: context bar, plugin toggler, and…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code-Mod: wählt das Modell und den Denkaufwand jedes Subagents aus.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code-Plugin (Mod), das die Claude-Code-Terminaloberfläche wie die…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Sieh, was Claude Code im Hintergrund ausführt: Subagents, Codex-Jobs, Shells…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Feldnotizen vom ersten Tag zu Claude Code-Mods auf Windows: eine…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code-Mod: Live-Kosten-, Kontext- und Plan-Kontingentanzeigen über dem…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code-Plugin und -Mod: ein AI-nativer SDLC.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Verpasse Claude einen Klaps, wenn es Mist baut — ein Stressabbau-Mod für…
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar and a status line for Claude Code: usage limits, context, model…
- [WQGGSEY/cache-ttl-timer](https://github.com/WQGGSEY/cache-ttl-timer) - Claude Code mod: a prompt-cache TTL countdown in the prompt footer, beside the…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Lerne eine Fremdsprache, während du mit Claude Code arbeitest.
- [Caesarcph/claude-mods](https://github.com/Caesarcph/claude-mods) - Two Claude Code mods: prompt-upgrade and auto-model.
- [CircularBlox/Clarity](https://github.com/CircularBlox/Clarity) - A clearer Claude Code terminal: boxed and organized you/claude conversations…
- [clafronteaccnts/commanddeck](https://github.com/clafronteaccnts/commanddeck) - Claude Code mods: command deck, GitHub issues pane, prompt upgrader, auto model.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Ein Claude Code Mod, das eine fortlaufende Liste der offenen Punkte in einer…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Sieh, welche Dateien jeder Claude Code-Agent in seinem Kontext hat und wie viel…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Kleine Claude Code-Mods für das Terminal und die Desktop-App.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Claude CLI-Skill + Mod, der spanische Wörter in Agentenantworten einfügt.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Dein Floatee-Backlog über dem Prompt von Claude Code: Todos mit einem Klick…
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [gabriel9004/claude-code-mods](https://github.com/gabriel9004/claude-code-mods) - Mods para Claude Code: panel de agentes y tareas con cuota y caché, y banda de…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Das Kontextfenster als eine Zeile über der Eingabeaufforderung, dargestellt so…
- [KTCrisis/flux7-mods](https://github.com/KTCrisis/flux7-mods) - Claude Code mods: machine-face avatars that judge tool calls, and live mesh7…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Lass deine Aufmerksamkeit nicht abschweifen, während du auf die Antwort von…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Ein kostenloses, quelloffenes Plugin für Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [markfulton/safe-keys](https://github.com/markfulton/safe-keys) - Paste an API key into Claude Code. Nothing keeps it.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code-Skills: ein Faktenprüfer für Dokumentation, ein Code-Auditor, ein…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code-Buddy-Plugin: ein ASCII-Begleiter über deiner Eingabeaufforderung…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: ein Claude Code-Mod, der Claudes Antworten und deine Prompts auf…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [tlq5l/afk-timer](https://github.com/tlq5l/afk-timer) - Claude Code mod: shows how long you.
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude-Code-Mods: kleine Plugins für Live-Bereiche, kostenbewusstes…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude-Code-Mod und -Plugin: Nutzungsmonitor, Token-Tracker und Statuszeile.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude-Code-Mods: EMCC (Every Mod Claude Code), eine kuratierte, getestete…
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [AJMarquez99/prompt-pin](https://github.com/AJMarquez99/prompt-pin) - Pin your latest prompt above the input and browse this session.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alanrsoares/claude-mods](https://github.com/alanrsoares/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Eine animierte Braille-Katze über der Claude Code-Eingabeaufforderung.
- [almost99/claudecode-mods](https://github.com/almost99/claudecode-mods) - Approved Claude Code Mods.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Eine Pixelkatze über deinem Claude-Code-Prompt, die einen Testanruf mit einem…
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Ein Claude Code-Mod, der einen geeigneten Zeitpunkt für die Komprimierung…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude-Mods für Claude Code: Token-Anzeige.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Allgemeine Mods für Claude Code: Bänder, Bereiche, Toasts und Hooks.
- [androidZzT/cc-moyu-kit](https://github.com/androidZzT/cc-moyu-kit) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [apiglue/claude-mods](https://github.com/apiglue/claude-mods) - Mods for Claude Code.
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Deine Claude-Nutzungslimits als animierte Dorfbewohner-Gesundheitskarte mit…
- [astromelon/takgon-mods](https://github.com/astromelon/takgon-mods) - 개인 Claude Code mods 플러그인(takgon-mods).
- [astrosteveo/nebula](https://github.com/astrosteveo/nebula) - Claude Code mods and plugins.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Kurze Workouts, während Claude arbeitet: ein Tagesziel, Streaks, Badges und…
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [AyeJK/eidola-mod](https://github.com/AyeJK/eidola-mod) - Claude Code mod: a pixel Vessel that reacts to what Claude is doing, plus an…
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods: live panes, bands and guards that run inside Claude Code.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Now-Playing-Mod für Claude Code: Apple Music und Spotify über der Eingabe, mit…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [bharath-gp/ai-harness](https://github.com/bharath-gp/ai-harness) - Claude Code plugin marketplace: guardrails and cockpit mod bundles.
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods für Claude Code: Cache-Uhr, Blast Radius, Vorschläge, Arbeitsliste, Grill.
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Nur eine Eule für deinen Claude Code.
- [CladiusIV/claude-mods](https://github.com/CladiusIV/claude-mods) - A Claude Code plugin marketplace of mods: changes to Claude Code.
- [coil398/claude-session-brief](https://github.com/coil398/claude-session-brief) - Claude Code mod: session summary band, subagent and hook activity above the…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [davidpravst/claude-mods](https://github.com/davidpravst/claude-mods) - Moji modi za Claude Code.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [dblanken-yale/cache-buster](https://github.com/dblanken-yale/cache-buster) - Claude Code mod: prompt-cache age band with a Compact button.
- [diegocamara89/claude-mods](https://github.com/diegocamara89/claude-mods) - Mods do Claude Code (function hooks): Sonnet por padrão para subagentes…
- [DimeDataCloud/open-ClaudeOS](https://github.com/DimeDataCloud/open-ClaudeOS) - Claude mods interactive operating system.
- [ecombuilder-web/TripleDigit-file-links](https://github.com/ecombuilder-web/TripleDigit-file-links) - Claude Code mod: a Files pane beside the chat listing every file created or…
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [Elmanuel1/claude-mods](https://github.com/Elmanuel1/claude-mods) - Claude Code mods: docs-watch.
- [evertonalves-ai/mod-forge](https://github.com/evertonalves-ai/mod-forge) - Claude Code skill that builds, debugs, audits and packages Claude Code mods…
- [fabiobosioit/claude-mods](https://github.com/fabiobosioit/claude-mods)
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude-Code-Mods (Function-Hook-Plugins): session-meter und mehr.
- [flaviorg/crew](https://github.com/flaviorg/crew) - Claude Code mod: a live panel of the subagents Claude delegates to — model…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [geonhos/claude-code-mod](https://github.com/geonhos/claude-code-mod)
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [gyoomun/claude-mods](https://github.com/gyoomun/claude-mods) - 다른 사람이 만든 Claude Code 모드를 내 작업 방식에 맞게 고친 것 (coach-on-call, next-steps-multi).
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [heidiks/agent-kit](https://github.com/heidiks/agent-kit) - Skills, plugins and Claude Code mods. Install only what you need.
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HikiJun97/claude-mods](https://github.com/HikiJun97/claude-mods) - Personal Claude Code mods.
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-effort-switch](https://github.com/HuliLulu46/cc-effort-switch)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code-Mod: wie lange jede Antwort dauerte, wie lange Claude nachdachte…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian.
- [ijat/prompt-polish](https://github.com/ijat/prompt-polish) - Claude Code mod that cleans up voice-dictated prompts and teaches the fix.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [jambolo/claude-mods](https://github.com/jambolo/claude-mods) - Mods for Claude Code.
- [jasoncai0/claude-session-hud](https://github.com/jasoncai0/claude-session-hud) - Claude Code mod: rate-limit usage, Codeup MRs and the session.
- [jenkinv/claude-img-viewer](https://github.com/jenkinv/claude-img-viewer) - Show images inside Claude Code.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Kontextnutzungsbereich in der Seitenleiste: Gesamtmenge, Kategorien, Wachstum…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Dateiliste in der Seitenleiste: Welche Dateien in dieser Unterhaltung neu…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 im 8-Bit-Stil (schwarz-weißes holländisches Hängeohrkaninchen) läuft und…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - „Meine Fragen“ in der Seitenleiste: Jede Nachricht, die der Benutzer in dieser…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Zeitachse in der Seitenleiste: Wofür die Zeit in dieser Runde aufgewendet wurde…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Token-Verkehr in der Seitenleiste: Wie viele Token die Hauptunterhaltung bei…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Die ehrliche Bohnenpaste von claude code: Nach jeder abgeschlossenen Runde sagt…
- [jiroamato/claude-mods](https://github.com/jiroamato/claude-mods) - Jiro.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jonirafael/claude-code-mods](https://github.com/jonirafael/claude-code-mods) - Claude Code mods: context-receipt (per-turn context breakdown) and…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [Jsolee/claude-mods](https://github.com/Jsolee/claude-mods) - Mods de Claude Code de Joan Solé: comunitat, el panell dels subagents amb el…
- [jumpei-kurata/claude-mods](https://github.com/jumpei-kurata/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd lebt in einem Band über deinem Claude Code-Prompt: stellt die Sitzung…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod, der Antworten und Benachrichtigungen von Claude Code mit VOICEVOX /…
- [kargarisaac/claude-fleet](https://github.com/kargarisaac/claude-fleet) - Claude Code mod: a docked pane showing every subagent as a tree with model…
- [katipally/modz](https://github.com/katipally/modz) - Claude Code mods: install with /plugin install &lt;mod&gt; --marketplace…
- [keithwalsh/claude-code-mods](https://github.com/keithwalsh/claude-code-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [Krishna30396/Pixel-Progress](https://github.com/Krishna30396/Pixel-Progress) - A pixel progress bar with time left for Claude Code: tasks done, percent and…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high.
- [levy-n/claude-code-mods](https://github.com/levy-n/claude-code-mods) - Claude Code mods for long sessions: context-handoff.
- [lifeofgurpreet/g-line](https://github.com/lifeofgurpreet/g-line) - A Claude Code mod: your session at a glance, with a heads-up before you hit a…
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [lperezmo/cache-caffeine](https://github.com/lperezmo/cache-caffeine) - Claude Code mod: keeps the prompt cache warm while you step away, and wakes…
- [lperezmo/session-relaunch](https://github.com/lperezmo/session-relaunch) - Claude Code mod: /relaunch reopens the current session in a new terminal tab so…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Ein von der Community kuratierter Leitfaden zu Claude Code-Mods…
- [lukeismith/lukes-claudecode-mods](https://github.com/lukeismith/lukes-claudecode-mods) - A collection of claude code mods I built.
- [m-aoki1348125/next-compass](https://github.com/m-aoki1348125/next-compass) - Claude Code mod: four predicted next instructions in four directions, and a…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Ein Claude-Code-Mod, der anzeigt, was Claude im Untertitel des iTerm2-Tabs tut…
- [macollins27/owner-rep](https://github.com/macollins27/owner-rep) - A Claude Code mod that watches the coding agent for the person who owns the…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude.
- [Marceux-Croix/Claudeopticon](https://github.com/Marceux-Croix/Claudeopticon) - A process monitoring and ticket system for Claude Code: your todo as a live…
- [marwansaab/Claude-Mods](https://github.com/marwansaab/Claude-Mods)
- [matrix-freed/debrief](https://github.com/matrix-freed/debrief) - Claude Code mod: session-metadata AAR recorder (core + adapters + profiles).
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community-Mods für Claude Code: Guards, Bereiche und Befehle, die innerhalb von…
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace.
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Claude Code-Mod, der die Todo-Tools für Modelle wieder aktiviert, die sie…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code-Mod, der auf eine sichere Pause wartet und dann deine Sitzung…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code-Mod: eine Zeile pro Aufgabe der Aufgabenliste über dem Prompt mit…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Spiele Vier gewinnt gegen eine AI innerhalb von Claude Code (/connect-four).
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude-Code-Mod: Wenn ein anderer Coding-Agent Änderungen in dein Repository…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude-Code-Mod für Repositories, die von mehreren KI-Agenten gemeinsam genutzt…
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph.
- [oklahaha/deepseek-balance](https://github.com/oklahaha/deepseek-balance) - Claude Code mod: DeepSeek balance gauge, today.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: ein Claude Code-Mod. Dauerhafte Worktrees mit schreibgeschütztem…
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [phatjam98/claude-mods](https://github.com/phatjam98/claude-mods) - Claude Code mods by phatjam98.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live-Seitenbereich mit Sitzungsstatistiken für den Code-Tab der…
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [piollosmash-dotcom/claude-mods](https://github.com/piollosmash-dotcom/claude-mods)
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pupuchan1/dopa-ide](https://github.com/pupuchan1/dopa-ide) - Claude Code mod: a dopamine band above the prompt, fireworks and a fanfare when…
- [PurpleDotStudio/claude-mods](https://github.com/PurpleDotStudio/claude-mods) - Claude Code mods: a side panel for what the session needs from you.
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [r1305/claude-mods](https://github.com/r1305/claude-mods) - Mods para Claude Code: enrutado de modelos con dashboard de consumo y…
- [rakavanagh/savvy-status](https://github.com/rakavanagh/savvy-status) - Claude Code mod: watch your subagents work as a crew of crabs, with live file…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [reedchan7/claude-mods-pulse](https://github.com/reedchan7/claude-mods-pulse) - Pulse: live TTFT, tok/s, prompt-cache hit rate and usage left in Claude Code.
- [retogo/claude-media-view](https://github.com/retogo/claude-media-view) - A Claude Code mod that shows images and GIFs inline in the terminal — and lets…
- [revilo-digital/second-opinion](https://github.com/revilo-digital/second-opinion) - Claude Code mod: ask OpenAI, Gemini or Grok for a second opinion on Claude.
- [RichardJSun/claude-code-mods](https://github.com/RichardJSun/claude-code-mods) - Claude Code mods, published as a plugin marketplace.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code-Mod: Liegestütze, die man machen kann, während Claude arbeitet.
- [Roberdinho/claude-mods](https://github.com/Roberdinho/claude-mods) - Claude Code mods: prompt-polaroid makes CodeSnap-style Polaroids of your prompts.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: ein Praxisleitfaden zu Claude Code-Mods, von ELI5 bis Policy…
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code-Mod: verwandelt den im Planmodus genehmigten Plan in eine…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Eine handverlesene Liste von Claude Code-Mods.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Kostenloser Modus: Hilfsagenten laufen auf Haiku, und große Dateien und Logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Ein Lofi-Soundtrack, der der Sitzung folgt: Ruhe, Fokus, Flow sowie Hinweise…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Lerne, während Claude programmiert: Nach einem Durchlauf, der den Code geändert…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Ein Band mit jeder Änderung, die Claude vornimmt: Spiele jede Änderung ab…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [serafin-meshy/claude-mods](https://github.com/serafin-meshy/claude-mods) - Claude Code mods for Meshy 3D generation: meshy-tray.
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker.
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Marketplace für benutzerdefinierte Claude Code-Mods (cc-mods), mit gebündelten…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Ein-Klick-Commit-Nachrichten für Claude Code mit einer tanzenden…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — ein Claude Code-Mod, der die Nutzung deines Claude-Plans anzeigt…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Inoffizielle Claude-Code-Mods von tanmen (Marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Ein Claude-Code-Mod, der die aktuelle Sitzung in einem Bereich anzeigt: jede…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Ein Claude Code-Plugin-Marketplace für Mods: function-hooks-Plugins, die…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace.
- [UlongChaS2/learn-trail-mods](https://github.com/UlongChaS2/learn-trail-mods) - Claude Code mod: 설명의 목차를 패널에 띄우고 항목별 설명을 저장해 /recall 로 다시 본다.
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [user0027/claude-mods](https://github.com/user0027/claude-mods)
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude-Code-Mod: animierte Fortschrittsleiste und Abschlusszusammenfassung für…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Drei kleine Claude Code-Mods: Sieh, wann deine Subagents fertig werden, stelle…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Sag „I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Stelle Claude eine Nebenfrage in einem Bereich neben deiner Arbeit.
- [verdantran/my-claude-mods](https://github.com/verdantran/my-claude-mods) - Small mods that change Claude Code.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vmlinuz82/claude-mods](https://github.com/vmlinuz82/claude-mods) - Claude Code mods: a task checklist and a skill/MCP usage band, for the terminal…
- [wildraine/context-gauge](https://github.com/wildraine/context-gauge) - Claude Code mod: context window usage gauge above the prompt.
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wonjangcloud9/wj-mods](https://github.com/wonjangcloud9/wj-mods) - Claude Code mods: cross-session work progress pane, usage band, long-turn…
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Claude Code mod 모음 (wonr-mods 마켓플레이스).
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code-Plugin: deine Claude-Pro/Max-Nutzungslimits mit einer…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods für Claude Code. agent-crew: Beobachte deine Subagenten bei der Arbeit als…
- [ya8282/claude-code-mods](https://github.com/ya8282/claude-code-mods) - Small productivity mods for Claude Code.
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [zhuobichen/zhaowen-claudemod](https://github.com/zhuobichen/zhaowen-claudemod) - 我自用的 Claude Code mod 合集（function hooks）：以 marketplace 形式分发，/plugin install 装.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Eine handverlesene Sammlung der besten Ressourcen für die großartigsten…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Ein Claude-Code-Plugin, das anzeigt, was gerade geschieht – Kontextnutzung…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Wunderschöne, hochgradig anpassbare Statuszeile für Claude Code CLI mit…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Alle Teile des System-Prompts von Claude Code, 27 integrierte…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - KI-Videofähigkeit für Claude Code &amp; Codex — filmische Produktvideos mit…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Mehr als 45 Tipps, um Claude Code optimal zu nutzen, von den Grundlagen bis zu…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex Skill — Xiaohongshu-Karussells und WeChat-Coverpaare im…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Überprüfe den Diff deines Coding-Agents in einem Terminalbereich und sende…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Umfassendes Statuszeilen-Plugin für Claude Code mit Kontextnutzung…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Erstelle Mods für Claude Code: Fange jede Anfrage ab, ändere jede Antwort…
- [aqua5230/usage](https://github.com/aqua5230/usage) - macOS menu bar &amp; Windows tray app pinning Claude Code, Codex, Antigravity &amp;…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Ein umfassendes Statuszeilen-Dashboard für Claude Code — Sitzungsinformationen…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Verfolge den CO₂-Fußabdruck deiner Claude-Code-Sitzungen.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Öffentliche Claude-Code-Skills und -Mods.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, Mods, Subagenten, Hooks, Slash-Befehle und Anleitungen für Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Rechtlich kostenlose LLM-APIs- und Coding-Agenten — selbstaktualisierend…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Ein Agent Skill, der deinen Coding-Agenten in einen Experten für…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Gebetszeiten, Hijri-Datum, Adhkar, täglicher Ayah, freiwilliges Fasten…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [romacv/claude-plan-usage-statusline](https://github.com/romacv/claude-plan-usage-statusline) - Claude Code status line showing model, usage limits, git info, and workspace…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Plugin-Sammlung für Claude Code, pi und DeepSeek Harness: Statusleisten-HUD…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Portables Claude-Code-Toolkit für .NET DDD/Clean Architecture: strikte…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Portable globale Konfiguration für Claude Code: benutzerdefinierte Skills…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Inoffizielle Mods für den Code-Tab von Claude Desktop — usage-pet: eine…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Claude Code-Plugins, die ich täglich verwende: Skills und Mods, aufgeräumt…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Eine anpassbare Statuszeile für Claude Code mit Drag-and-drop-Editor.
- [MindLab-Research/dsh-generative-ui](https://github.com/MindLab-Research/dsh-generative-ui) - Generative UI for DeepSeek Harness — the agent writes TSX and the web UI…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [wide3751/switchboard](https://github.com/wide3751/switchboard) - A Claude Code plugin (mod) that shows every local Claude Code session in one…
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marktplatz für Claude Code-Plugins und Skills zur Erstellung von Mods für das…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Ansicht mit geteiltem Bereich für Claude Code in Windows Terminal und tmux: die…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository für Claude Code Awesome Media-Mods.
- [dayfinggg/anthropic-claude-code-agent-skills](https://github.com/dayfinggg/anthropic-claude-code-agent-skills) - 18 engineering skills, 14 specialist agents, the Brief output style, two mods…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [michalschroeder/claude-statusline](https://github.com/michalschroeder/claude-statusline) - My Claude Code statusline + supporting hooks.
- [OFurtun/claude-custom-statusline](https://github.com/OFurtun/claude-custom-statusline) - Furtun.
- [RaggioS/claude-code-statusline](https://github.com/RaggioS/claude-code-statusline) - Single-file POSIX statusline for Claude Code: dir, git branch, model, context…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [faleiro-thiago/claude-skills-mods](https://github.com/faleiro-thiago/claude-skills-mods) - Facilitadores pessoais para Claude Code, versionados por item.
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [31c0c3/claude-statusline](https://github.com/31c0c3/claude-statusline) - One-line Claude Code status line in bash and jq: context, cache, limits, cost.
- [afarrell/claude-meter](https://github.com/afarrell/claude-meter) - Minimal Claude Code statusline — context bar, 5h bar, and 7-day rolling…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games.
- [alexmagnum2d0/anki-claude-mode](https://github.com/alexmagnum2d0/anki-claude-mode) - Anki pane for Claude Code: decks, review and cards Claude adds, through…
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - Personal Claude Code plugin marketplace (todo-pane).
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professionelle Claude Code-Statuszeile: Sitzungsdauer, Kosten in mehreren…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramods Claude-Code-Plugins, ein Marketplace: Agent-Skills und Live-Bereiche…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Eine Statuszeile für Claude Code: Kontext, Limits und das Tempo der Woche, die…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Two-row status line for Claude Code: context, rate limits with pace markers…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust.
- [federbenjamin/claude-statusline](https://github.com/federbenjamin/claude-statusline) - A two-line Claude Code status line showing branch, PR, model, context, cost…
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Talk to Claude Code by voice on Windows: a Mod + helper using codex app-server…
- [LiamMorganDev/claude-setup](https://github.com/LiamMorganDev/claude-setup) - My complete Claude Code setup: mods, skills, commands, hooks and CLAUDE.md…
- [luck7x/claude-cache-keepalive](https://github.com/luck7x/claude-cache-keepalive) - Keep Claude Code&#x27;s prompt cache warm while you&#x27;re away — cheap…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [Monte9/claude-memory-mods](https://github.com/Monte9/claude-memory-mods) - Curate Claude Code&#x27;s own memory files: a pane to view every project&#x27;s memory…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [n0nuser/claude-statusline](https://github.com/n0nuser/claude-statusline) - 3-line status bar for Claude Code — model, context usage, cost, git status, and…
- [nhooey/claude-code-usage-statusline](https://github.com/nhooey/claude-code-usage-statusline) - A Claude Code status line and per-turn cost readout in one program: token…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [Recokioshi/claude-kit](https://github.com/Recokioshi/claude-kit) - a set of useful skills and mods for claude code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Benutzerdefinierte Claude Code-Statuszeile.
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Model risk management guardrails for Claude Code: 25 controls in six mod packs…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Universelle Multi-Protokoll-StatusLine, selbstlernender Kontext und…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Kontextverfall-Detektor 2026 – Proaktiver KI-Speicher- und Ratenlimit-Monitor…
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code-Hooks, Subagents und Statuszeilen: Open-Source-Sammlungen und Tools…
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods für Claude Code: Bereiche, Leisten und Begleiter auf Basis von Function…
- [ryanclark/statusline](https://github.com/ryanclark/statusline) - Simple status line for Claude Code showing context window/usage limits.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Übergib Aufgaben zwischen deinen Claude Code-Sitzungen.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Finde heraus, wonach du Claude Code immer wieder fragst, und…
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Dies ist ein MCP-Server zur Steuerung von MODS, dem modularen…
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Bibliothek mit 3 Skills für Claude Code: session-handoff, session-statusline…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex- und Claude-Code-Skill zum Übersetzen von CK3-Mods mit einem lokalen LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-Source-Mods und weitere Erweiterungen für Claude Code.
- [Grandullon/diariovida-mods](https://github.com/Grandullon/diariovida-mods) - Mods gratis para Claude Code: entiende lo que hace Claude, mejora tus prompts y…
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability.

</details>

<a id="dsh-cordis"></a>

## DSH- und Cordis-Plugin-Ökosysteme

DeepSeek Harness und Cordis erreichen dasselbe Ziel aus einer anderen Richtung: Für sie ist das Plugin der Mod-Mechanismus, daher entspricht ein Plugin dort einer Mod hier.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250661 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 Im Code gefunden: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                       |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **250661** |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐75283 · TypeScript · 👁️ observed · 0 天</summary>

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
| Sterne            | **75283**  |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4648 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

DSHs offiziell am meisten empfohlene TUI-Plugin — hohe Leistung, geringer Ressourcenverbrauch, niedlicher Pixelwal und reibungslose Mausinteraktion. Installation mit einem npm-Befehl. / DSHs offiziell am meisten empfohlenes TUI-Plugin, hohe Leistung, geringer Ressourcenverbrauch, niedlicher Pixelwal, reibungslose Mausinteraktion, Installation mit einem npm-Befehl

<sub>🔧 Im Code gefunden: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                       |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | TypeScript                                                                |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **4648**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐723 · Python · 👁️ observed · 0 天</summary>

##### 📝 Zusammenfassung

Eine kuratierte Liste der besten großartigen KI-Plugins für KI-Assistenten, darunter Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi und weitere. https://hol.org/plugins

<sub>🔧 Im Code gefunden: `README.md`</sub>

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                      |
| --------- | ------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                       |
| Beleg     | `der eigene Text nennt einen Mod API oder erklärt die Mod-Funktionalität` |
| Sprache   | Python                                                                    |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **723**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐277152 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **277152** |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101415 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **101415** |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84177 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **84177**  |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35813 · Go · 🔎 inferred · 0 天</summary>

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
| Sterne            | **35813**  |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐31016 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Eine moderne Desktop-Lösung für das DeepSeek Harness (DSH)-Plugin-Ökosystem. Alles ist ein „Plugin“, auch der Desktop selbst ist ein „Plugin“.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **31016**  |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25673 · Python · 🔎 inferred · 3 天</summary>

##### 📝 Zusammenfassung

Distilly — Dis­tilliere, wie sie denken, in wiederverwendbare Skills für jeden Agenten oder Bot. Früher Colleague Skill（原同事 Skill）.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **25673**  |
| Letzter Push      | 2026-10-13 |
| Erstmals gelistet | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18927 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **18927**  |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9211 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **9211**   |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8806 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness (DSH) Web-Plugin-Aggregationsökosystem · Alles ist ein Plugin, verteilt über die Kreativwerkstatt｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Alles ist ein Plugin, verteilt über die Kreativwerkstatt

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **8806**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐8132 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Python                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **8132**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6687 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **6687**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4271 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **4271**   |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3484 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Antworte mir mit HTML — eine Agentenfähigkeit, die schwierige Fragen mit einer einseitigen HTML-Seite beantwortet, die du tatsächlich lesen kannst. Lass den KI-Agenten komplexe Fragen mit einer einseitigen HTML-Seite beantworten.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **3484**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐2373 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Sterne            | **2373**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2178 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, agent teams, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板、浏览器、侧栏、命令，透视上下文组成、演进、压缩、多 Agent等。

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **2178**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐2037 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

IM-Bots über QR-Code oder Bot-Zugangsdaten mit DeepSeek Harness verbinden (unterstützt 飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord und WhatsApp). IM-Bots über QR-Code oder Zugangsdaten mit DeepSeek Harness verbinden (9 Kanäle).

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **2037**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1473 · Python · 🔎 inferred · 0 天</summary>

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
| Sterne            | **1473**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-15 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1206 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Go                                                                                             |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **1206**   |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐707 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **707**    |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

📚 Eine git-gestützte Micro-Lesson-Bibliothek ohne Abhängigkeiten, in der KI-Agenten asynchron verifizierte Debugging-Erfahrungen teilen und durchsuchen können. | https://misakanet.org

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
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Clarklevis1995/dsh-mobile">Clarklevis1995/dsh-mobile</a></b> · ⭐519 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness Mobile 是一个面向 DeepSeek Harness 的原生 iOS 客户端。它通过 dsh-plugin-mobile-gateway 与 Harness 建立 WebSocket 连接，将工作区、会话、实时回复和 Agent 执行轨迹带到 iPhone，同时延续 DeepSeek WebUI 克制、清晰的视觉语言

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Kotlin                                                                                         |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **519**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `android` · `android-app` · `coding-agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-plugin` · `ios`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/clarklevis1995--dsh-mobile/b7ef26df82cda351.png" width="100%" alt="Clarklevis1995/dsh-mobile screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Han-1413141/dsh-cost-meter">Han-1413141/dsh-cost-meter</a></b> · ⭐429 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Cost tracking for DeepSeek Harness: session and model costs, token usage, budgets, provider balances, and coding-plan quotas. Bilingual English/Chinese UI.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **429**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `cost-tracking` · `deepseek` · `deepseek-api` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/han-1413141--dsh-cost-meter/ea3a53e99a515021.png" width="100%" alt="Han-1413141/dsh-cost-meter screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐352 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Your Intelligence, Orchestrated. Any Model, Any Agent, Any One.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | Go                                                                                             |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **352**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐274 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **274**    |
| Letzter Push      | 2026-10-15 |
| Erstmals gelistet | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **256**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness-Skin-/Wallpaper-/Theme-Paket-Plugin (dsh-plugin) — 8 Mirage-Themes, benutzerbezogene Akzentfarbe, Wallpaper 2.0, Import/Export von Theme-Paketen und Freigabelinks, Favoriten und Zufallsauswahl, vollständig mit einem nativen Token-System umgesetzt.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **247**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐206 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Natives DeepSeek Harness (DSH)-Plugin, das TypeSafe Jev oder eine Decision API wie luna als System One-Entscheidungsebene für Agentenauswahl, Überwachung, Korrekturen und Genehmigungen integriert.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **206**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐199 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | JavaScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **199**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐191 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

DeepSeek Harness (DSH) Backup- und Wiederherstellungs-Plugin – exportiere, importiere, migriere und synchronisiere deine vollständige DSH-Konfiguration, Plugins, MCP-Server, Skills und deinen Arbeitsbereich. Migration auf einen anderen Rechner mit einem Klick.

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **191**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/95eb0411c14b8fcd.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐167 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Zusammenfassung

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Grundlegende Fakten

| Feld      | Wert                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| Kategorie | `DSH- und Cordis-Plugin-Ökosysteme`                                                            |
| Beleg     | `nennt einen Mod, ein Plugin oder einen Hook, aber nichts speziell über die Mod-Schnittstelle` |
| Sprache   | TypeScript                                                                                     |

##### 📊 Daten

| Messwert          | Wert       |
| ----------------- | ---------- |
| Sterne            | **167**    |
| Letzter Push      | 2026-10-16 |
| Erstmals gelistet | 2026-10-16 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Bild</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Das Asset wird per Hotlink aus dem Upstream-Repository eingebunden, da keine lizenzfreundliche Weiterverwendungslizenz angegeben wurde.</sub>

</details>

<details>
<summary><b>Mehr in dieser Kategorie</b> <sub>· 60</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Eine Schutzvorrichtung vor der Ausführung für AI-Coding-Agenten.
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [sixtysevenlf/dsh-blender-plugin](https://github.com/sixtysevenlf/dsh-blender-plugin) - DSH x Blender direct realtime plugin v2.0 — an AI drives Blender over a direct…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH-Plugin-Marktplatz / DSH Plugin Marketplace: Im DeepSeek Harness Web GUI mit…
- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - DeepSeek Harness plugin for previewable cross-preset session migration.
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - Enthält nach der Installation direkt 27 Engineering- und Produktivitätsskills…
- [drewnekota/cetus](https://github.com/drewnekota/cetus) - One macOS app for Claude Code, Codex, and every agent runtime you use…
- [arcships/rutis](https://github.com/arcships/rutis) - Eine Plugin-Laufzeitumgebung für Software, die sich selbst weiterentwickelt…
- [Duskriver/dsh-opencode-go](https://github.com/Duskriver/dsh-opencode-go) - 用于deepseek-harness的opencode-go套餐增强插件。多账号管理、额度UI面板、自动更新模型.
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Desktop-Agent auf Basis des Deepseek-Harness-Kerns.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Das lebendige DeepSeek Harness-Plugin-Verzeichnis — stündlich aktualisiert…
- [eleckoi/ElecKoi](https://github.com/eleckoi/ElecKoi) - 电子爱PC客户端，由DSH驱动的Agent角色扮演!
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Aufgabenbewusste Arbeitsbereichskontextsuche und Lebenszyklusverfolgung für…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Ausgewähltes Verzeichnis für DeepSeek Harness-(DSH)-Plugins — über 280…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [duhu2000/dsh-mcp-connector](https://github.com/duhu2000/dsh-mcp-connector) - DeepSeek Harness MCP Connector: connect servers, search tools across active…
- [niiang/dsh-kimino-theme](https://github.com/niiang/dsh-kimino-theme) - Kimi no Na wa (Your Name) theme for DeepSeek Harness Web GUI.
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [FNOSP/fnos-dsh](https://github.com/FNOSP/fnos-dsh) - DeepSeek Harness应用与harness插件 monorepo.
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh-Android-Version: integriert DeepSeek Harness, eine Ubuntu-Laufzeitumgebung…
- [UncleK/dsh-think-translate](https://github.com/UncleK/dsh-think-translate) - Thinking-chain UI translation for DeepSeek Harness: 8 target languages, local…
- [geml-spec/geml](https://github.com/geml-spec/geml) - One format, two readers. People and AI agents now co-write the same document.
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion: Erweitert dsh-im mit dem Konzept von Assistenz und Zuhause –…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Von der Community kuratierte DeepSeek Harness (dsh)-Plugins, Tools, Skills und…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [LAU-MARS/dsh-cad](https://github.com/LAU-MARS/dsh-cad) - deepseek harness 2D and 3D CAD plugin.
- [realguan/dsh-dock](https://github.com/realguan/dsh-dock) - Plattformübergreifendes Desktop-Kontrollzentrum speziell für DeepSeek Harness…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Login gate for the DeepSeek Harness (dsh) web surface: password or shared-token…
- [bloodtmai-cmyk/dsh-ai-hub](https://github.com/bloodtmai-cmyk/dsh-ai-hub) - 面向企业内部 Harness 工作台的轻量控制面.
- [mokuyoaxis/dsh-iris](https://github.com/mokuyoaxis/dsh-iris) - Media generation and visual understanding for DeepSeek Harness, with…
- [bloodtmai-cmyk/dsh-harness-enterprise](https://github.com/bloodtmai-cmyk/dsh-harness-enterprise) - 面向企业内部管控的 DeepSeek Harness 统一智能工作台入口.
- [AIcivilization/dsh-vps-manager](https://github.com/AIcivilization/dsh-vps-manager) - VPS &amp; SSH manager plugin for DeepSeek Harness (DSH): zero-token /vps- commands…
- [BreakFree003/dsh-clinepass-deepseekv4.1](https://github.com/BreakFree003/dsh-clinepass-deepseekv4.1) - Cline Pass for DeepSeek Harness (dsh): one pi-ai provider route pinned to the…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH-Plugin: ein Git-Toolfenster in IDE-Qualität als nativer…
- [zkforge/dsh-claude-desktop-theme](https://github.com/zkforge/dsh-claude-desktop-theme) - DSH 桌面端 Claude 风格主题插件.
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [lwmxiaobei/dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) - DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制.
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Jede beobachtbare Aktion des KI-Coding-Agenten sichtbar machen.
- [ChaYeWuu/dsh-hyperworkbuddy](https://github.com/ChaYeWuu/dsh-hyperworkbuddy) - 一个 DeepSeek Harness 插件：在 DSH 设置里直接管理 WorkBuddy 多账号，并把模型接进 DSH 与任意 OpenAI 兼容客户端.
- [FeatherHunter/dsh-plugin-update](https://github.com/FeatherHunter/dsh-plugin-update) - 给 DSH 插件加「检查更新 / 安装更新」能力的 npm 包：宿主一段接线 + 面板一个现成组件，查新版、装更新、失败兜底、更新日志与多插件日志一次包掉.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Verifizierungsstandard ohne Abhängigkeiten für DeepSeek-Harness-(dsh-)Plugins –…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) Web-Plugin: Market-Dashboard-Seitenleiste zur…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode auf DeepSeek Harness — DSH-Plugin, das OpenCode Zen + Go-Modelle der…
- [27painter/dsh-moli](https://github.com/27painter/dsh-moli) - DSH plugin · Drive the local Moli headless browser from DeepSeek Harness…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — Marktplatz für Plugins von Drittanbietern und geschützter…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx ist eine menschenzentrierte, erweiterbare Desktop-Workstation…
- [DoveLi-Gu/dsh-showcase](https://github.com/DoveLi-Gu/dsh-showcase) - Local, verifiable delivery evidence reports and DSH plugin for coding-agent…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入.
- [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) - DSH的插件创意市场来啦!～～～欢迎使用&amp;提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方…
- [momasiku/dsh-pilot](https://github.com/momasiku/dsh-pilot) - Desktop automation for DeepSeek Harness: hands and eyes on the whole Windows…
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色：换装、白饭、摸头、问候、登录账户余额和本机今日用量预估.
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [ytftu/dsh-session-cost](https://github.com/ytftu/dsh-session-cost) - DSH（DeepSeek Harness）插件：底栏会话消费金额、每条回复本轮金额、右上角开放平台余额/今日用量/峰谷，点击弹出折线图.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness-Plugin: Wandelt den Fehler bei der ACL-Bereitstellung der…
- [akkefa/deepseek-cordis](https://github.com/akkefa/deepseek-cordis) - Python plugin runtime targeting DeepSeek Harness vendored Cordis semantics.
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…

</details>

<a id="writing"></a>

## Texte, Diskussionen und Videos

Artikel, Diskussionen und Videos über die Mod-Funktionalität.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 1 天</summary>

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
| Erstmals gelistet | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 14 天</summary>

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
| Erstmals gelistet | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
| Erstmals gelistet | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| Erstmals gelistet | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 14 天</summary>

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
| Erstmals gelistet | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| TypeScript | 371      | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 82       | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 43       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 14       | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 10       | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 4        | `vulcanshen/ccdrawu`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                         |
| Kotlin     | 2        | `Clarklevis1995/dsh-mobile`, `dphmoblie/deepseek-harness-android`                                             |
| PowerShell | 2        | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| AutoHotkey | 1        | `keithwalsh/claude-code-mods`                                                                                 |
| C          | 1        | `reporails/arcade`                                                                                            |
| C#         | 1        | `DimeDataCloud/open-ClaudeOS`                                                                                 |
| Java       | 1        | `bloodtmai-cmyk/dsh-ai-hub`                                                                                   |
| MDX        | 1        | `jkf87/mod-guide`                                                                                             |
| Ruby       | 1        | `romacv/claude-plan-usage-statusline`                                                                         |
| Swift      | 1        | `eovidiu/cordis-ios`                                                                                          |
| jq         | 1        | `n0nuser/claude-statusline`                                                                                   |

<sub>Es werden nur Einträge gezählt, die eine Sprache angeben. Dokumentations- und Diskussionseinträge sind von dieser Tabelle ausgeschlossen.</sub>

## Mitwirken

Korrekturen sind willkommen und der schnellste Weg, diese Liste zu verbessern. Erstelle ein Issue oder einen Pull Request, wenn ein Eintrag falsch einsortiert oder falsch eingestuft wurde oder ein Projekt aufgrund einer Namenskollision zu Unrecht ausgeschlossen wurde — in dieser letzten Kategorie sind automatisierte Filter am wahrscheinlichsten fehlerhaft.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Zuletzt aktualisiert · 2026-10-16T14:49:31+08:00</sub>
