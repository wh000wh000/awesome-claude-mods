<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod straordinarie per Claude">
</p>

<h1 align="center">Mod straordinarie per Claude</h1>

<p align="center"><b>L'indice di mod e plugin per Claude Code, valutati in base alle evidenze, e dei comportamenti più profondi che modificano.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-597-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <b>Italiano</b> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indice aggiornato** · Ultima sincronizzazione: `2026-10-16T14:49:31+08:00` (UTC+8)
> · Voci: **597** · Aggiunte nell'ultimo aggiornamento: **0** · Linguaggi di implementazione: **17**

<sub>Ogni voce qui sotto è stata raccolta, filtrata e verificata nuovamente in automatico. Nessuna voce è un'inserzione a pagamento.</sub>

<a id="featured"></a>

## Selezioni del momento

<sub>Una voce per categoria, classificata in base al livello delle prove e alle stelle, con ricalcolo a ogni aggiornamento. È una classifica, non un'approvazione; ogni selezione rimanda alla relativa scheda completa qui sotto. Sono preferiti i progetti che hanno pubblicato uno screenshot o una registrazione, così la fascia rimane visiva.</sub>

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
<sub>Trova i token fantasma. Sistemali. Sopravvivi alla compattazione. Evita il degrado della qualità del contesto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐75283 · TypeScript · 👁️ observed</sub>
<sub>🌊 L&#x27;agent harness originale. Distribuisci sciami intelligenti multi-player, coordina flussi di lavoro autonomi e crea sistemi di AI conversazionale. Include memoria…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## Contenuti

- [Che cos'è una mod per Claude Code](#che-cosè-una-mod-per-claude-code)
- [Come vengono valutate le voci](#come-vengono-valutate-le-voci)
- [Ufficiali: repository e note di rilascio di Anthropic](#ufficiali-repository-e-note-di-rilascio-di-anthropic) — **17**
- [Mod: realizzate con la funzionalità mod](#mod-realizzate-con-la-funzionalità-mod) — **475**
- [Gli ecosistemi dei plugin DSH e Cordis](#gli-ecosistemi-dei-plugin-dsh-e-cordis) — **94**
- [Testi, discussioni e video](#testi-discussioni-e-video) — **11**
- [Progetti per linguaggio di implementazione](#progetti-per-linguaggio-di-implementazione)

## Che cos&#x27;è una mod per Claude Code

Claude Code ha introdotto le **mod** nella versione 2.1.287: estensioni che possono modificare il comportamento più in profondità di quanto potrebbe fare un plugin e disegnare la propria interfaccia.

Una mod può usare un hook di `ui.render` per visualizzare una **riga, una fascia, un riquadro o una scheda** attorno al prompt, leggere il testo selezionato per ultimo con `$.ui.selection()`, creare compagni di squadra con `agent.spawn` e gestire una regione `Client`. Se una mod non riesce a disegnare, fallisce da sola — `ui.fault` impedisce a una mod difettosa di arrestare la sessione.

Questo elenco comprende le mod, la superficie di plugin e hook su cui si basano e gli equivalenti per DSH e Cordis. Deliberatamente **non** comprende l'ecosistema più ampio di Claude Code: un pacchetto di prompt non è una mod.

## Come vengono valutate le voci

La maggior parte degli elenchi di questo settore dichiara semplicemente cosa include. Questo invece indica quanto è stato effettivamente verificato e consente di filtrare di conseguenza. Un livello descrive le prove, non la qualità del progetto — una mod ben realizzata di cui nessuno ha ancora scritto resta comunque `inferred`.

| Valutazione                                                                                    | Significato                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pubblicato direttamente da Anthropic`                                                         | Pubblicato direttamente da Anthropic, oppure letto direttamente dal changelog ufficiale.                                                                                                                                                 |
| `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod`            | Il suo stesso testo nomina una parte della superficie delle mod — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, un riquadro, una fascia o una scheda — quindi l'autore sta descrivendo qualcosa costruito sulla API reale. |
| `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` | Si definisce una mod, un plugin o un hook, ma nel suo testo non nomina nulla di specifico sulla superficie delle mod. Reale, ma non confermato.                                                                                          |
| `corrisponde solo in base al vocabolario`                                                      | Corrisponde solo in base al vocabolario. Incluso per rendere il filtro verificabile, non perché sia ritenuto affidabile.                                                                                                                 |

<a id="official"></a>

## Ufficiali: repository e note di rilascio di Anthropic

Anthropic's own Claude Code repositories, and the releases that defined the mod surface. Read from the source rather than summarised.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151120 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Riepilogo

Claude Code è uno strumento di programmazione agentico che vive nel terminale, comprende la tua base di codice e ti aiuta a programmare più velocemente eseguendo attività di routine, spiegando codice complesso e gestendo i flussi di lavoro git, tutto tramite comandi in linguaggio naturale.

<sub>🔧 Trovato nel codice: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | TypeScript                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **151120** |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9528 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | TypeScript                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **9528**   |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8289 · Python · ✅ official · 0 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | Python                                                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8289**   |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6395 · Python · ✅ official · 246 天</summary>

##### 📝 Riepilogo

Un'azione GitHub di revisione della sicurezza basata sull'IA che utilizza Claude per analizzare le modifiche al codice alla ricerca di vulnerabilità di sicurezza.

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | Python                                                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **6395**   |
| Ultimo push                | 2026-02-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | Shell                                                   |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1813**   |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

##### 📝 Riepilogo

Materiali supplementari per le Model Cards di Claude

##### 📌 Informazioni di base

| Campo     | Valore                                                  |
| --------- | ------------------------------------------------------- |
| Categoria | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova     | `pubblicato direttamente da Anthropic`                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **25**     |
| Ultimo push                | 2025-12-05 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Riepilogo

Aggiunti Claude Mods: ora i plugin possono modificare comportamenti più profondi. Aggiunto You should know, un mod integrato in cui un agente secondario ti copre le spalle e segnala ciò che tu o Claude potreste non notare. Attivalo con `/plugin enable cc-plugin-you-should-know@builtin` (per le sessioni first-party con la telemetria attiva)

##### 📌 Informazioni di base

| Campo     | Valore                                                  |
| --------- | ------------------------------------------------------- |
| Categoria | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova     | `pubblicato direttamente da Anthropic`                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Riepilogo

Aggiunto `$.ui.selection()` per i mod: restituisce il testo selezionato per ultimo in modalità a schermo intero e, quando la selezione si trova all'interno di una riga della trascrizione, quella riga. Risolto un problema per cui il pulsante di un mod eseguiva talvolta l'azione di un altro pulsante quando veniva premuto su una vista disegnata prima del riavvio di Claude Code. Risolto il problema delle sessioni a schermo intero che terminavano con "unrecoverable interface error" quando si apriva la finestra di dialogo delle attività in background mentre un plugin o un mod mostrava righe sopra il prompt. Risolto il problema per cui `claude plugin test` segnalava i mod come disattivati da remoto quando aveva soltanto letto un'impostazione salvata non aggiornata

##### 📌 Informazioni di base

| Campo     | Valore                                                  |
| --------- | ------------------------------------------------------- |
| Categoria | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova     | `pubblicato direttamente da Anthropic`                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Riepilogo

Risolto un problema per cui una regola deny o ask su una parte annidata di un comando shell composto non rimaneva valida durante l'approvazione di un mod installato dall'utente sulle macchine gestite. Risolto il problema dei mod installati che non venivano caricati nella prima sessione dopo un aggiornamento. Aggiunto `agent.spawn` per i compagni di squadra, un unico ID agente tra gli eventi degli hook dei plugin e gli stati idle e waiting in `$.agent.list()`. Risolto il problema delle sessioni che terminavano con "unrecoverable interface error" quando un valore scritto dall'hook `ui.render` di un mod faceva generare un errore a una riga durante il disegno; ora il motore disegna invece la propria riga. Risolto il problema dei contenuti allineati a destra nel pannello o nella banda di un mod che venivano disegnati sotto il simbolo di chiusura o `\[-\]`, wh

##### 📌 Informazioni di base

| Campo     | Valore                                                  |
| --------- | ------------------------------------------------------- |
| Categoria | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova     | `pubblicato direttamente da Anthropic`                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Riepilogo

Aggiunto `serverToolUses` al risultato dell’hook `turn.step` di un mod: lo strumento chiama autonomamente API (il consulente), includendo per ciascuna chiamata id, nome, input, inizio e fine. Aggiunti `ceiling` alla domanda e al verdetto letti dall’hook `tool.check` di un mod, indicando l’approvazione richiesta da un’organizzazione per uno strumento. Aggiunti i tipi `ThemeKey` e `Color` ai tipi degli hook dei plugin, così un editor elenca i colori del tema che il disegno di un mod può nominare. Aggiunto a `claude plugin validate`: ogni hook registrato da un mod in un punto di controllo è elencato con l’indicazione della presenza di un `.catch` (`gatingHooks` in `--json`). Corretto il risultato `turn.step` di un mod

##### 📌 Informazioni di base

| Campo     | Valore                                                  |
| --------- | ------------------------------------------------------- |
| Categoria | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova     | `pubblicato direttamente da Anthropic`                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Riepilogo

Aggiunto `prompt.autocomplete`, un evento a cui una mod si aggancia per aggiungere le proprie righe all'elenco di completamento automatico della casella del prompt Aggiunto il caching del prompt a `$.model.complete` per le mod: `prompt` e `system` prendono blocchi di testo, e `cache: true` su un blocco mette in cache la richiesta fino a esso Aggiunti agenti di workflow all'hook della mod `agent.spawn`, con la loro esecuzione e indice, così una mod può rifiutarli Corretti Write, Edit, NotebookEdit e righe LSP, e singole righe Read, Grep e Glob, nascondendo il motivo per cui una mod ha negato la chiamata: la riga ora mostra il motivo Corretto l'hook `config.set`, `state.set`, `env.set` o `agent.spawn` di una mod che nega dop

##### 📌 Informazioni di base

| Campo     | Valore                                                  |
| --------- | ------------------------------------------------------- |
| Categoria | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova     | `pubblicato direttamente da Anthropic`                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Riepilogo

Aggiunto `isDeferred` a `$.tool.register` per le mod: `false` elenca lo schema dello strumento nel prompt fin dall'inizio invece di tenerlo nascosto dietro la ricerca degli strumenti. Corretto un problema per cui gli hook di una mod sugli eventi `classic.*` venivano ignorati mentre il worker degli hook del plugin si riavviava, lasciando gli hook delle impostazioni a rispondere senza di essi. Corretto il problema per cui `claude plugin test` falliva per le mod che chiamano `$.session.append`; i test possono rileggere le righe aggiunte con il nuovo `mock.session`

##### 📌 Informazioni di base

| Campo     | Valore                                                  |
| --------- | ------------------------------------------------------- |
| Categoria | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova     | `pubblicato direttamente da Anthropic`                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-08 |

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 5</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Aggiunto `$.ui.notify` per le mod: genera una notifica nativa tramite la tua…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Risolto il problema per cui Esc o un.
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod.

</details>

<a id="mods"></a>

## Mod: realizzate con la funzionalità mod

Ogni voce qui mostra prove dell'uso della funzionalità che Claude Code ha acquisito nella versione 2.1.287: esegue il rendering tramite `ui.render`, gestisce un pannello, una fascia o una scheda, legge `$.ui.selection()`, avvia compagni di squadra con `agent.spawn` oppure dichiara esplicitamente di essere una mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2573 · Python · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Trova i token fantasma. Sistemali. Sopravvivi alla compattazione. Evita il degrado della qualità del contesto.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | Python                                                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **2573**   |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐852 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Riepilogo

Custom Claude Code Mods that I need

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **852**    |
| Ultimo push                | 2026-10-14 |
| Prima comparsa nell'elenco | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐604 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Catalogo della community di mod pubbliche di Claude Code (hook di funzione), analizzate a partire da GitHub con indicazione di ciò che ogni mod può leggere, scrivere, eseguire o inviare tramite la rete. Sfoglia https://mods.aidojo.si/

<sub>🔧 Trovato nel codice: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **604**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐259 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Mod per Claude Code: plugin basati su hook che aggiungono righe dinamiche sopra il prompt, protezioni, pannelli e giochi. Barra del contesto, indicatore di utilizzo, monitoraggio delle revisioni di Codex, anteprima Markdown, riproduzione attuale di Spotify e altro.

<sub>🔧 Trovato nel codice: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **259**    |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐218 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **218**    |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐208 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Mods for Claude Code. effortless picks the reasoning effort for every prompt and shows the cache countdown. textless shows art, quotes and chess instead of the wall of text while Claude works.

<sub>🔧 Trovato nel codice: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | HTML                                                                                |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **208**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `ai-tools` · `anthropic` · `chess` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐196 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Riepilogo

Mantieni calda la cache del prompt di Claude Code durante le pause e mostra il costo stimato prima di un invio a freddo.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **196**    |
| Ultimo push                | 2026-10-04 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐154 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Skin per Claude Code: righe degli strumenti con icone, schede per diff, tabelle e grafici Mermaid, una fascia di utilizzo e quindici temi. /skin li cambia al volo.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **154**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐116 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Risposte colorate e personalizzabili di Claude Code: tabelle, codice, diagrammi, grafici e righe degli strumenti in 15 temi, con pulsanti per la copia. Una mod di Claude Code.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **116**    |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐107 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Riepilogo

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 Trovato nel codice: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **107**    |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐94 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Riepilogo

Un mod di Claude Code che porta una dashboard dell'agente in tempo reale nel terminale: contesto e costi, cronologia dell'advisor, ogni controllo delle autorizzazioni, schede dei subagenti e corsie.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **94**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Riepilogo

Una raccolta di mod per claude code

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **80**     |
| Ultimo push                | 2026-10-08 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: barre di avanzamento del piano in tempo reale sopra il prompt

<sub>🔧 Trovato nel codice: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **54**     |
| Ultimo push                | 2026-10-14 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐36 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Una barra con i prompt della tua sessione Claude Code: passa il mouse per leggerli, fai clic per raggiungerli (hook di funzione / Mods)

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **36**     |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Un rinnovamento per Claude Code: un pannello cockpit live, temi condivisibili e un animaletto pixel che mette in scena ciò che sta facendo Claude

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **30**     |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **30**     |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: menu Strumenti Claude, modalità Zen, temi del terminale, controlli dell'intensità e della modalità

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **24**     |
| Ultimo push                | 2026-10-14 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: 21 stili e un set completo di funzionalità da attivare quando servono, per il terminale e l'app desktop. · Applica un nuovo stile a Claude con un clic e offre un set completo di funzionalità attivabili su richiesta.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **22**     |
| Ultimo push                | 2026-10-04 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐20 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: Clawd mette in scena ciò che sta facendo Claude, sopra il prompt

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **20**     |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

##### 📝 Riepilogo

Dieci mod di Claude Code, guide per principianti, prompt per la creazione, demo sicure e un template per crearne uno personalizzato.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **20**     |
| Ultimo push                | 2026-10-02 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 Riepilogo

Due mod di Claude Code: bridge Codex per il controllo del computer e sessioni Claude coordinate. Sorgente, prompt di build, configurazione e test.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **16**     |
| Ultimo push                | 2026-10-05 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/rashedInt32/glass">rashedInt32/glass</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Un aspetto da applicazione desktop per la trascrizione del terminale di Claude Code, come mod

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **15**     |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `markdown` · `syntax-highlighting` · `terminal-ui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/rashedint32--glass/c7b07954a39be0b7.png" width="100%" alt="rashedInt32/glass screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Riepilogo

LINE dentro Claude Code: la TUI enil come mod di Claude Code

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **15**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: usage-band mostra i tuoi limiti di 5h/7d, la finestra di contesto e il tasso di cache hit sopra il prompt

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **14**     |
| Ultimo push                | 2026-10-03 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Riepilogo

Dieci mod open source per Claude Code: pannelli dinamici, bande, statusline e protezioni per le chiamate agli strumenti. Misuratore del consumo, codici di avvio, riepilogo della sessione, boss fight, animaletto del codice e altro.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **14**     |
| Ultimo push                | 2026-10-03 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Riepilogo

Mod di Claude Code che rendono le domande di Claude più facili da leggere e a cui rispondere (qa-guide).

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **12**     |
| Ultimo push                | 2026-10-07 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Claude Code mod: contesto in token, limiti di 5 ore e settimanali rispetto all'orologio, conto alla rovescia della cache dei prompt, costo della sessione e agenti in esecuzione, tutto in una fascia sopra il prompt.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **12**     |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 Riepilogo

KOZMOS — mod live e visivi per Claude Code (CLI + desktop): bande sopra il prompt, barre laterali, ticker di stato, compagni, protezioni e suoni.

<sub>🔧 Trovato nel codice: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **12**     |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐11 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Pixel art animata sopra il prompt di Claude Code che reagisce mentre Claude lavora. Sette scene oppure una tua immagine o GIF. Zero token.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **11**     |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Riepilogo

Fai durare più a lungo il piano Claude Pro: mod di Claude Code per un HUD dei consumi preciso, output della shell più breve e nessuna rilettura ripetuta dei file. I mod spendono zero token.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **10**     |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 30 天</summary>

##### 📝 Riepilogo

Claude Code mods: context window, plan quota burn rate, per-turn cost, and a budget guard that stops the session past a limit

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **9**      |
| Ultimo push                | 2026-09-15 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Un'interfaccia per i tuoi terminali Claude Code e Codex che i tuoi agenti costruiscono, così l'unico modello nella tua testa è il tuo.

<sub>🔧 Trovato nel codice: `CLAUDE.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **9**      |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Riepilogo

Sei mod di Claude Code in un unico plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) con interruttori per ogni mod, più un rapporto mod-vs-hook.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8**      |
| Ultimo push                | 2026-10-04 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Riepilogo

Raccolta di mod di Claude Code di 개발동생. Pacchetto taxi: tassametro, navigatore, telecamere per il controllo della velocità, dashcam

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8**      |
| Ultimo push                | 2026-10-04 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Guarda su youtube.com</a> · la riproduzione si apre sul sito ospitante; GitHub non può incorporarla nella pagina</sub></td>
</tr></table>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 441</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Raccolta di oltre 100 mod utilizzabili con Claude Code.
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Mod di Claude Code di Darrell Wang — bande sopra il prompt, zero token del…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mod di Claude Code di Ray Amjad: riquadri, bande, protezioni del prompt…
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Skills, agenti, comandi, regole, hook e stili di output esperti per Claude Code…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod di Claude e strumenti per crearle: prima una competenza per la creazione…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quattro mod di Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - L.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Usa Claude Mods per mettere un nuovo tetto a Claude Code: senza modificare il…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Build, test, console e anteprime SwiftUI di Xcode dentro Claude Code.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base di conoscenza di Obsidian con fonti citate sui mod di Claude Code: come…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mod di Claude Code di Learning Hacker: rendono il funzionamento dell.
- [kakha13/claude](https://github.com/kakha13/claude) - Mod di Claude Code che correggono e traducono i tuoi prompt prima che Claude li…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mod e skill di Claude Code di Nekyia Labs, creati e utilizzati quotidianamente…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un riquadro laterale per Claude Code: i subagenti eseguiti da una sessione, ciò…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Pannello della barra laterale di Claude Desktop (scheda Code): elenca tutti i…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra di utilizzo sopra la casella di input di Claude Desktop (scheda Code)…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mod di Claude (plugin con hook di funzione) per Claude Code.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Scheda di stato flottante per Claude Code — modello, contesto, limiti di…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill che insegna agli agenti di Claude Code a creare mod Claude.
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una coda decisionale CLI/TUI per persone che lavorano con agenti…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin e skill Claude della community, installabili da un unico mercato.
- [davekiss/mods](https://github.com/davekiss/mods) - Mod di Claude Code di Dave Kiss.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Pannelli, protezioni e mod per migliorare l&#x27;esperienza d&#x27;uso di Claude Code…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mod Claude Code on demand — una skill che legge la tua conversazione e…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galleria di mod di Baselane: mod di Claude Code, verificati e fissati in…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Un test di digitazione per passare il tempo mentre Claude lavora.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Un app store per le mod di Claude Code, dentro Claude Code: /mods per…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sei modifiche di Claude Code: limiti del piano e contesto sopra il prompt…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) di Claude Code che aggiunge un pannello laterale con schede…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod di Claude Code che visualizza le differenze di Edit e Write in due colonne…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mod di Claude Code: pannello dei consumi usage-hud di 像素螃蟹 + link HTML…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mod per Claude Code: plugin con hook di funzione che aggiungono riquadri live e…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mod di Claude Code: screen-guard nasconde nomi e segreti mentre condividi lo…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mod e skin per Claude Code: una barra di avanzamento live per le attività di…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Estensioni di Claude Code. Sblocca tutta la potenza di Claude.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Due mod di Claude Code per eseguire molte sessioni contemporaneamente: una…
- [nsodhi-cmu/claude-code-ripple](https://github.com/nsodhi-cmu/claude-code-ripple) - Claude Code mod that creates graphical traces of your code changes.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Due mod di Claude Code sopra la casella del prompt: indicatore della finestra…
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace delle mie mod per Claude Code.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Legge i file markdown a cui Claude Code dà un nome, visualizzati accanto alla…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow per Claude Code: una checklist essenziale sopra il prompt che mostra…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mod di Claude Code: barra del contesto, pannello degli agenti, sfocatura PDPA.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod di Claude Code: miniature delle immagini incollate sopra il prompt, in…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collaboratore vocale per Claude Code. Parla delle tue idee con un lupo 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mod di Claude Code: typing-speed, un tachimetro della velocità di digitazione…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mod per Claude Code: pannelli, comandi e hook realizzati con il plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Scopri mod, plugin ed estensioni di Claude Code con demo animate, elenchi per…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod di Claude Code: diagrammi Mermaid disegnati direttamente nella trascrizione.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Piccoli mod di Claude Code (plugin con hook di funzione): session-switcher e…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mod di Claude Code: mod-scout (trova i mod che useresti di più), usage-meter…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Toolkit di Naren per Claude: skill, mod e server MCP per Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un insieme di mod per claude code realizzate da me.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: scopri, esamina, attiva/disattiva e aggiorna i mod di Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - I migliori mod di Claude Code: selezionati, convalidati, fissati in alto.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mod di Claude Code per veri ingegneri.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code: routing automatico del modello Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sei mod per Claude Code: mascotte animata Clawd, barre per limite d.
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Alleva un uovo al tè che si insaporisce lentamente mentre scrivi code · Alleva…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mod open source per Claude Code: riquadri, righe di stato, notifiche…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod di Claude Code: rispondi a Claude punto per punto, direttamente sul testo.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mod per Claude Code: Clawd, una piccola mascotte pixelata che mette in scena…
- [reporails/arcade](https://github.com/reporails/arcade) - Giochi desktop classici come mod di Claude Code, giocabili in un riquadro…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods per claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod per Claude Code che attiva o disattiva le tue competenze, i tuoi agenti…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod di Claude Code testate e installabili con un solo comando: protezioni per…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Un elenco curato di mod di Claude Code, installabili come marketplace di…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Due mod di Claude Code: cache-keeper e ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mod di Claude Code che mantengono onesto un agente — hook di funzione che…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Una mod per Claude Code per catturare i pensieri durante il lavoro…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Le mod di Claude Code di Herman (marketplace herman-mods).
- [jrlprost/claude-code-mods](https://github.com/jrlprost/claude-code-mods) - Claude Code mods I build because I need them: context bar, plugin toggler, and…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Mod di Claude Code: seleziona il modello e il livello di ragionamento di ogni…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) di Claude Code che fa apparire l.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Scopri cosa eseguono in background le sessioni di Claude Code: subagent…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Note sul campo del primo giorno sulle mod di Claude Code su Windows: una barra…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod di Claude Code: misuratori live di costo, contesto e quota del piano sopra…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod di Claude Code: un SDLC AI-native.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Sc​​ulaccia Claude quando sbaglia — una mod antistress per Claude Code…
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar and a status line for Claude Code: usage limits, context, model…
- [WQGGSEY/cache-ttl-timer](https://github.com/WQGGSEY/cache-ttl-timer) - Claude Code mod: a prompt-cache TTL countdown in the prompt footer, beside the…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Impara una lingua straniera mentre lavori con Claude Code.
- [Caesarcph/claude-mods](https://github.com/Caesarcph/claude-mods) - Two Claude Code mods: prompt-upgrade and auto-model.
- [CircularBlox/Clarity](https://github.com/CircularBlox/Clarity) - A clearer Claude Code terminal: boxed and organized you/claude conversations…
- [clafronteaccnts/commanddeck](https://github.com/clafronteaccnts/commanddeck) - Claude Code mods: command deck, GitHub issues pane, prompt upgrader, auto model.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Una mod di Claude Code che mantiene un elenco aggiornato degli elementi aperti…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Vedi quali file ogni agente di Claude Code ha nel proprio contesto, e quanto di…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Piccole mod di Claude Code per il terminale e l.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI che aggiunge parole spagnole nelle risposte dell.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Il backlog di Floatee sopra il prompt di Claude Code: esegui, guida e spunta le…
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [gabriel9004/claude-code-mods](https://github.com/gabriel9004/claude-code-mods) - Mods para Claude Code: panel de agentes y tareas con cuota y caché, y banda de…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La finestra di contesto come un.
- [KTCrisis/flux7-mods](https://github.com/KTCrisis/flux7-mods) - Claude Code mods: machine-face avatars that judge tool calls, and live mesh7…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Non lasciare che la tua attenzione divaghi mentre aspetti la risposta di Claude…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Un plugin gratuito e open source per Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [markfulton/safe-keys](https://github.com/markfulton/safe-keys) - Paste an API key into Claude Code. Nothing keeps it.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Competenze di Claude Code: verificatore dei fatti per la documentazione…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin buddy di Claude Code: un compagno ASCII sopra il prompt che ricorda le…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: una mod di Claude Code che legge ad alta voce, su richiesta, le…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [tlq5l/afk-timer](https://github.com/tlq5l/afk-timer) - Claude Code mod: shows how long you.
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod di Claude Code: piccoli plugin per riquadri in tempo reale, instradamento…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin di Claude Code: monitoraggio dell.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Mod di Claude Code: EMCC (Every Mod Claude Code), una raccolta curata e testata…
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [AJMarquez99/prompt-pin](https://github.com/AJMarquez99/prompt-pin) - Pin your latest prompt above the input and browse this session.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alanrsoares/claude-mods](https://github.com/alanrsoares/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gatto braille animato sopra il prompt di Claude Code.
- [almost99/claudecode-mods](https://github.com/almost99/claudecode-mods) - Approved Claude Code Mods.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gatto pixel sopra il prompt di Claude Code che esegue una chiamata di test a…
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Una mod di Claude Code che sceglie il momento giusto per compattare e mantenere…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modifiche di Claude Code per Claude: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mod generiche per Claude Code: bande, pannelli, notifiche e hook.
- [androidZzT/cc-moyu-kit](https://github.com/androidZzT/cc-moyu-kit) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [apiglue/claude-mods](https://github.com/apiglue/claude-mods) - Mods for Claude Code.
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - I tuoi limiti di utilizzo di Claude come scheda animata della salute di un…
- [astromelon/takgon-mods](https://github.com/astromelon/takgon-mods) - 개인 Claude Code mods 플러그인(takgon-mods).
- [astrosteveo/nebula](https://github.com/astrosteveo/nebula) - Claude Code mods and plugins.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Brevi allenamenti mentre Claude lavora: un obiettivo giornaliero, serie, badge…
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [AyeJK/eidola-mod](https://github.com/AyeJK/eidola-mod) - Claude Code mod: a pixel Vessel that reacts to what Claude is doing, plus an…
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods: live panes, bands and guards that run inside Claude Code.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing per Claude Code: Apple Music e Spotify sopra il prompt, con…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [bharath-gp/ai-harness](https://github.com/bharath-gp/ai-harness) - Claude Code plugin marketplace: guardrails and cockpit mod bundles.
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod per Claude Code: orologio della cache, Blast Radius, suggerimenti, lista di…
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un gufo per il tuo Claude Code.
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
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mod di Claude Code (plugin con hook sulle funzioni): session-meter e altro.
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
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod di Claude Code: quanto tempo ha richiesto ogni risposta, quanto ha pensato…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian.
- [ijat/prompt-polish](https://github.com/ijat/prompt-polish) - Claude Code mod that cleans up voice-dictated prompts and teaches the fix.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [jambolo/claude-mods](https://github.com/jambolo/claude-mods) - Mods for Claude Code.
- [jasoncai0/claude-session-hud](https://github.com/jasoncai0/claude-session-hud) - Claude Code mod: rate-limit usage, Codeup MRs and the session.
- [jenkinv/claude-img-viewer](https://github.com/jenkinv/claude-img-viewer) - Show images inside Claude Code.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Pannello laterale dell.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Elenco laterale dei file: quali file sono stati creati, modificati o eliminati…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Mao Mao in stile 8-bit (coniglio nano olandese bianco e nero) corre e salta…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Pannello laterale «Le mie domande»: ogni frase digitata dal proprietario in…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Cronologia laterale: dove è stato impiegato il tempo di questo turno.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Scambio di token nella barra laterale: quanti token la conversazione principale…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Il sincero sacchetto di fagioli di claude code: al termine di ogni turno…
- [jiroamato/claude-mods](https://github.com/jiroamato/claude-mods) - Jiro.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jonirafael/claude-code-mods](https://github.com/jonirafael/claude-code-mods) - Claude Code mods: context-receipt (per-turn context breakdown) and…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [Jsolee/claude-mods](https://github.com/Jsolee/claude-mods) - Mods de Claude Code de Joan Solé: comunitat, el panell dels subagents amb el…
- [jumpei-kurata/claude-mods](https://github.com/jumpei-kurata/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive in una fascia sopra il prompt di Claude Code: mette in scena la…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod che legge ad alta voce le risposte e le notifiche di Claude Code tramite…
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
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Una guida ai mod di Claude Code curata dalla community: casi d.
- [lukeismith/lukes-claudecode-mods](https://github.com/lukeismith/lukes-claudecode-mods) - A collection of claude code mods I built.
- [m-aoki1348125/next-compass](https://github.com/m-aoki1348125/next-compass) - Claude Code mod: four predicted next instructions in four directions, and a…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Una mod di Claude Code che mostra cosa sta facendo Claude nel sottotitolo della…
- [macollins27/owner-rep](https://github.com/macollins27/owner-rep) - A Claude Code mod that watches the coding agent for the person who owns the…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude.
- [Marceux-Croix/Claudeopticon](https://github.com/Marceux-Croix/Claudeopticon) - A process monitoring and ticket system for Claude Code: your todo as a live…
- [marwansaab/Claude-Mods](https://github.com/marwansaab/Claude-Mods)
- [matrix-freed/debrief](https://github.com/matrix-freed/debrief) - Claude Code mod: session-metadata AAR recorder (core + adapters + profiles).
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mod della community per Claude Code: protezioni, pannelli e comandi eseguiti…
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace.
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod di Claude Code che riattiva gli strumenti todo per i modelli che li…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod di Claude Code che attende una pausa sicura, poi trasferisce la sessione o…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod di Claude Code: una riga per ogni attività sopra il prompt con l.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Gioca a Connect Four contro un.
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Modifica al codice di Claude: quando un altro agente di programmazione esegue…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Modifica al codice di Claude per repository condivisi da diversi agenti IA…
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph.
- [oklahaha/deepseek-balance](https://github.com/oklahaha/deepseek-balance) - Claude Code mod: DeepSeek balance gauge, today.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: un mod di Claude Code. Worktree permanenti con un avvio in sola…
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [phatjam98/claude-mods](https://github.com/phatjam98/claude-mods) - Claude Code mods by phatjam98.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Riquadro laterale con statistiche live della sessione per la scheda Code…
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
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code: flessioni da fare mentre Claude lavora. Nessun token.
- [Roberdinho/claude-mods](https://github.com/Roberdinho/claude-mods) - Claude Code mods: prompt-polaroid makes CodeSnap-style Polaroids of your prompts.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: una guida pratica ai mod di Claude Code, dalla spiegazione per…
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod di Claude Code: trasforma il piano approvato in modalità piano in una…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una selezione curata di mod di Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modalità senza costi: gli agenti ausiliari funzionano su Haiku e i file e i log…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una colonna sonora lofi che segue la sessione: calma, concentrazione, flusso…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Impara mentre Claude programma: dopo un turno che ha modificato il codice…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una registrazione di ogni modifica effettuata da Claude: riproduci ogni…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [serafin-meshy/claude-mods](https://github.com/serafin-meshy/claude-mods) - Claude Code mods for Meshy 3D generation: meshy-tray.
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker.
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Marketplace di mod personalizzati per Claude Code (cc-mods), con mod di esempio…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messaggi di commit con un clic per Claude Code con una Malenia in pixel-art che…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod di Claude Code che mostra l.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Mod non ufficiali di Claude Code di tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod di Claude Code che mostra la sessione corrente in un pannello: ogni…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace di plugin Claude Code di mod: plugin function-hooks che…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace.
- [UlongChaS2/learn-trail-mods](https://github.com/UlongChaS2/learn-trail-mods) - Claude Code mod: 설명의 목차를 패널에 띄우고 항목별 설명을 저장해 /recall 로 다시 본다.
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [user0027/claude-mods](https://github.com/user0027/claude-mods)
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod di Claude Code: fascia di avanzamento animata e riepilogo del completamento…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tre piccoli mod di Claude Code: scopri quando i tuoi sottoagenti termineranno…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Fai a Claude una domanda laterale in un riquadro accanto al tuo lavoro.
- [verdantran/my-claude-mods](https://github.com/verdantran/my-claude-mods) - Small mods that change Claude Code.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vmlinuz82/claude-mods](https://github.com/vmlinuz82/claude-mods) - Claude Code mods: a task checklist and a skill/MCP usage band, for the terminal…
- [wildraine/context-gauge](https://github.com/wildraine/context-gauge) - Claude Code mod: context window usage gauge above the prompt.
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wonjangcloud9/wj-mods](https://github.com/wonjangcloud9/wj-mods) - Claude Code mods: cross-session work progress pane, usage band, long-turn…
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Claude Code mod 모음 (wonr-mods 마켓플레이스).
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Claude Code: i tuoi limiti di utilizzo Claude Pro/Max con una…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod per Claude Code. agent-crew: osserva i tuoi subagenti al lavoro come un…
- [ya8282/claude-code-mods](https://github.com/ya8282/claude-code-mods) - Small productivity mods for Claude Code.
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [zhuobichen/zhaowen-claudemod](https://github.com/zhuobichen/zhaowen-claudemod) - 我自用的 Claude Code mod 合集（function hooks）：以 marketplace 形式分发，/plugin install 装.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una raccolta curata delle migliori risorse per il più straordinario degli…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin Claude Code che mostra cosa sta succedendo: utilizzo del contesto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Elegante statusline altamente personalizzabile per Claude Code CLI, con…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Tutte le parti del prompt di sistema di Claude Code, 27 descrizioni degli…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Skill video AI per Claude Code e Codex — video cinematografici di prodotti con…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Oltre 45 consigli per ottenere il massimo da Claude Code, dalle basi agli…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — genera caroselli Xiaohongshu e coppie di…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Esamina il diff del tuo agente di coding in un pannello del terminale e invia…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin completo della barra di stato per Claude Code con utilizzo del contesto…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crea mod per Claude Code: intercetta qualsiasi richiesta, modifica qualsiasi…
- [aqua5230/usage](https://github.com/aqua5230/usage) - macOS menu bar &amp; Windows tray app pinning Claude Code, Codex, Antigravity &amp;…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Una dashboard completa di statusline per Claude Code — informazioni sulla…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: monitora l.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills e mod pubblici per Claude Code.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mod, subagent, hook, comandi slash e guide per Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legali gratuiti e agenti di coding — autoaggiornati, verificati con…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill che trasforma il tuo agente di coding in un esperto di firmware per…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Orari delle preghiere, data Hijri, adhkar, ayah quotidiana, digiuno sunnah…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [romacv/claude-plan-usage-statusline](https://github.com/romacv/claude-plan-usage-statusline) - Claude Code status line showing model, usage limits, git info, and workspace…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Raccolta di plugin per Claude Code, pi e DeepSeek Harness: HUD della barra di…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Toolkit portatile di Claude Code per DDD/Architettura Pulita .NET: agenti TDD…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configurazione globale portabile di Claude Code: competenze personalizzate…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mod non ufficiali per la scheda Code di Claude Desktop — usage-pet: una banda…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin di Claude Code che uso ogni giorno: skill e mod, ripuliti per funzionare…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Statusline personalizzabile per Claude Code con editor drag-and-drop.
- [MindLab-Research/dsh-generative-ui](https://github.com/MindLab-Research/dsh-generative-ui) - Generative UI for DeepSeek Harness — the agent writes TSX and the web UI…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [wide3751/switchboard](https://github.com/wide3751/switchboard) - A Claude Code plugin (mod) that shows every local Claude Code session in one…
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace per plugin e skill di Claude Code per facilitare la creazione di…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visualizzatore a pannelli divisi per Claude Code in Windows Terminal e tmux: la…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository per mod Awesome Media di Claude Code.
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
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline di livello professionale per Claude Code: durata della sessione…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - Plugin Claude Code di divramod, un unico marketplace: skill degli agenti e…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Una riga di stato per Claude Code: contesto, limiti e ritmo della settimana, CI…
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
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Statusline personalizzata di Claude Code.
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Model risk management guardrails for Claude Code: 25 controls in six mod packs…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ StatusLine multiprotocollo universale, autoapprendimento del contesto e…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Rilevatore del deterioramento del contesto 2026 - Monitor proattivo della…
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagent e statusline di Claude Code: raccolte e strumenti open-source…
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mod per Claude Code: riquadri, bande e compagni basati su hook di funzione.
- [ryanclark/statusline](https://github.com/ryanclark/statusline) - Simple status line for Claude Code showing context window/usage limits.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passa le attività tra le tue sessioni di Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: trova ciò che chiedi ripetutamente a Claude Code e trasformalo in un…
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Questo è un server MCP per controllare MODS, lo strumento modulare…
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Libreria di 3 skill per Claude Code: session-handoff, session-statusline e…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill di Codex e Claude Code per tradurre mod di CK3 con un LLM locale.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mod open source e altre estensioni per Claude Code.
- [Grandullon/diariovida-mods](https://github.com/Grandullon/diariovida-mods) - Mods gratis para Claude Code: entiende lo que hace Claude, mejora tus prompts y…
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability.

</details>

<a id="dsh-cordis"></a>

## Gli ecosistemi dei plugin DSH e Cordis

DeepSeek Harness e Cordis arrivano allo stesso risultato da una direzione diversa: per loro il plugin è il meccanismo delle mod, quindi un plugin lì equivale a una mod qui.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250661 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 Trovato nel codice: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                            |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **250661** |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐75283 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

🌊 L'agent harness originale. Distribuisci sciami intelligenti multi-player, coordina flussi di lavoro autonomi e crea sistemi di AI conversazionale. Include memoria adattiva, intelligenza autoapprendente, federazione, integrazione vector RAG e supporto nativo per Claude Code / Codex / Hermes e molti altri integrati

<sub>🔧 Trovato nel codice: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                            |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **75283**  |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4648 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Il plugin TUI ufficialmente più consigliato da DSH: alte prestazioni, basso sovraccarico, simpatica balena pixelata, interazione fluida con il mouse. Installazione con un solo comando tramite npm. / Il plugin TUI ufficialmente più consigliato da DSH: alte prestazioni, basso utilizzo di risorse, simpatica balena pixelata, interazione fluida con il mouse, installazione con un solo comando tramite npm

<sub>🔧 Trovato nel codice: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                            |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **4648**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐723 · Python · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Un elenco curato dei migliori plugin AI eccezionali per assistenti AI, inclusi Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi e altri. https://hol.org/plugins

<sub>🔧 Trovato nel codice: `README.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                            |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | Python                                                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **723**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐277152 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Effettua il reverse engineering di qualsiasi cosa con agenti, dal comportamento delle app fino ai binari nativi.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **277152** |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101415 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **101415** |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84177 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Trasforma qualsiasi idea, piano o base di codice in un bellissimo diagramma interattivo. Una competenza agentica per Claude Code, Codex e altro.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **84177**  |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35813 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Un agente di coding affidabile per attività complesse di ingegneria del software.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Go                                                                                             |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **35813**  |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐31016 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Una moderna soluzione desktop creata per l’ecosistema di plugin DeepSeek Harness (DSH). Tutto è un “plugin”, anche il desktop stesso è un “plugin”.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **31016**  |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25673 · Python · 🔎 inferred · 3 天</summary>

##### 📝 Riepilogo

Distilly — distilla il loro modo di pensare in Skills riutilizzabili per qualsiasi Agent o Bot. In precedenza Colleague Skill（ex Colleague Skill）.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **25673**  |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18927 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **18927**  |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9211 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Meta-framework della componibilità spazio-temporale

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **9211**   |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8806 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness (DSH) Web 插件生态 di aggregazione · Tutto è un plugin, distribuito tramite Creative Workshop｜｜Ecosistema di aggregazione di plugin Web DeepSeek Harness (DSH) · Tutto è un plugin, distribuito tramite Creative Workshop

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8806**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐8132 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8132**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6687 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **6687**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4271 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **4271**   |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3484 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Rispondimi con HTML — una skill per agent che risponde a domande difficili con una pagina HTML di una pagina che puoi davvero leggere. Lascia che AI Agent risponda a problemi complessi con una pagina HTML.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3484**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐2373 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **2373**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2178 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, agent teams, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板、浏览器、侧栏、命令，透视上下文组成、演进、压缩、多 Agent等。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **2178**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐2037 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Collega i bot IM a DeepSeek Harness tramite codice QR o credenziali dei bot (supporta 飞书, 微信, 钉钉, 企业微信, QQ, Slack, Telegram, Discord e WhatsApp). Collega i bot IM a DeepSeek Harness tramite codice QR o credenziali (9 canali).

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **2037**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1473 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1473**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-15 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1206 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Go                                                                                             |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1206**   |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐707 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **707**    |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

📚 Una libreria di micro-lezioni senza dipendenze e basata su git per permettere agli AI Agents di condividere e cercare in modo asincrono esperienze di debugging verificate. | https://misakanet.org

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **526**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Clarklevis1995/dsh-mobile">Clarklevis1995/dsh-mobile</a></b> · ⭐519 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness Mobile 是一个面向 DeepSeek Harness 的原生 iOS 客户端。它通过 dsh-plugin-mobile-gateway 与 Harness 建立 WebSocket 连接，将工作区、会话、实时回复和 Agent 执行轨迹带到 iPhone，同时延续 DeepSeek WebUI 克制、清晰的视觉语言

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Kotlin                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **519**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `android` · `android-app` · `coding-agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-plugin` · `ios`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/clarklevis1995--dsh-mobile/b7ef26df82cda351.png" width="100%" alt="Clarklevis1995/dsh-mobile screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Han-1413141/dsh-cost-meter">Han-1413141/dsh-cost-meter</a></b> · ⭐429 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Cost tracking for DeepSeek Harness: session and model costs, token usage, budgets, provider balances, and coding-plan quotas. Bilingual English/Chinese UI.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **429**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `cost-tracking` · `deepseek` · `deepseek-api` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/han-1413141--dsh-cost-meter/ea3a53e99a515021.png" width="100%" alt="Han-1413141/dsh-cost-meter screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐352 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Your Intelligence, Orchestrated. Any Model, Any Agent, Any One.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Go                                                                                             |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **352**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐274 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **274**    |
| Ultimo push                | 2026-10-15 |
| Prima comparsa nell'elenco | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **256**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin DeepSeek Harness per skin / sfondi / pacchetti tema (dsh-plugin) — 8 set di temi Mirage, colori di accento per utente, sfondi 2.0, importazione/esportazione di pacchetti tema/link di condivisione, preferiti e casuale, implementato con un sistema di token puramente nativo.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **247**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐206 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin nativo DeepSeek Harness (DSH) che integra TypeSafe Jev o un’api decisionale come luna come livello decisionale System One per selezione, supervisione, correzioni e approvazioni degli agenti.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **206**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐199 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **199**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐191 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin di backup e ripristino per DeepSeek Harness (DSH) — esporta, importa, migra e sincronizza la configurazione completa di DSH, i plugin, i server MCP, le competenze e l’area di lavoro. Migrazione con un clic su un altro computer.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **191**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/95eb0411c14b8fcd.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐167 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **167**    |
| Ultimo push                | 2026-10-16 |
| Prima comparsa nell'elenco | 2026-10-16 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 60</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Una protezione pre-esecuzione per agenti di coding AI.
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [sixtysevenlf/dsh-blender-plugin](https://github.com/sixtysevenlf/dsh-blender-plugin) - DSH x Blender direct realtime plugin v2.0 — an AI drives Blender over a direct…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace / Mercato dei plugin DSH: sfoglia, installa e aggiorna…
- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - DeepSeek Harness plugin for previewable cross-preset session migration.
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - Include già all.
- [drewnekota/cetus](https://github.com/drewnekota/cetus) - One macOS app for Claude Code, Codex, and every agent runtime you use…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime per plugin destinato a software che si evolve autonomamente — il…
- [Duskriver/dsh-opencode-go](https://github.com/Duskriver/dsh-opencode-go) - 用于deepseek-harness的opencode-go套餐增强插件。多账号管理、额度UI面板、自动更新模型.
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Agent desktop basato sul nucleo di Deepseek-Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - La directory in continua evoluzione dei plugin DeepSeek Harness — aggiornata…
- [eleckoi/ElecKoi](https://github.com/eleckoi/ElecKoi) - 电子爱PC客户端，由DSH驱动的Agent角色扮演!
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Recupero del contesto dell&#x27;area di lavoro consapevole dell&#x27;attività e…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directory curata di plugin per DeepSeek Harness (DSH) — oltre 280 plugin della…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [duhu2000/dsh-mcp-connector](https://github.com/duhu2000/dsh-mcp-connector) - DeepSeek Harness MCP Connector: connect servers, search tools across active…
- [niiang/dsh-kimino-theme](https://github.com/niiang/dsh-kimino-theme) - Kimi no Na wa (Your Name) theme for DeepSeek Harness Web GUI.
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [FNOSP/fnos-dsh](https://github.com/FNOSP/fnos-dsh) - DeepSeek Harness应用与harness插件 monorepo.
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh per Android: integra DeepSeek Harness, ambiente di esecuzione Ubuntu…
- [UncleK/dsh-think-translate](https://github.com/UncleK/dsh-think-translate) - Thinking-chain UI translation for DeepSeek Harness: 8 target languages, local…
- [geml-spec/geml](https://github.com/geml-spec/geml) - One format, two readers. People and AI agents now co-write the same document.
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion: potenzia dsh-im con i concetti di assistente e casa — mostra…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugin, strumenti, skill e risorse di apprendimento DeepSeek Harness (dsh)…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [LAU-MARS/dsh-cad](https://github.com/LAU-MARS/dsh-cad) - deepseek harness 2D and 3D CAD plugin.
- [realguan/dsh-dock](https://github.com/realguan/dsh-dock) - Centro di controllo desktop multipiattaforma creato appositamente per DeepSeek…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Login gate for the DeepSeek Harness (dsh) web surface: password or shared-token…
- [bloodtmai-cmyk/dsh-ai-hub](https://github.com/bloodtmai-cmyk/dsh-ai-hub) - 面向企业内部 Harness 工作台的轻量控制面.
- [mokuyoaxis/dsh-iris](https://github.com/mokuyoaxis/dsh-iris) - Media generation and visual understanding for DeepSeek Harness, with…
- [bloodtmai-cmyk/dsh-harness-enterprise](https://github.com/bloodtmai-cmyk/dsh-harness-enterprise) - 面向企业内部管控的 DeepSeek Harness 统一智能工作台入口.
- [AIcivilization/dsh-vps-manager](https://github.com/AIcivilization/dsh-vps-manager) - VPS &amp; SSH manager plugin for DeepSeek Harness (DSH): zero-token /vps- commands…
- [BreakFree003/dsh-clinepass-deepseekv4.1](https://github.com/BreakFree003/dsh-clinepass-deepseekv4.1) - Cline Pass for DeepSeek Harness (dsh): one pi-ai provider route pinned to the…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: una finestra degli strumenti Git di livello IDE come scheda nativa…
- [zkforge/dsh-claude-desktop-theme](https://github.com/zkforge/dsh-claude-desktop-theme) - DSH 桌面端 Claude 风格主题插件.
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [lwmxiaobei/dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) - DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制.
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Osserva chiaramente ogni azione osservabile dell.
- [ChaYeWuu/dsh-hyperworkbuddy](https://github.com/ChaYeWuu/dsh-hyperworkbuddy) - 一个 DeepSeek Harness 插件：在 DSH 设置里直接管理 WorkBuddy 多账号，并把模型接进 DSH 与任意 OpenAI 兼容客户端.
- [FeatherHunter/dsh-plugin-update](https://github.com/FeatherHunter/dsh-plugin-update) - 给 DSH 插件加「检查更新 / 安装更新」能力的 npm 包：宿主一段接线 + 面板一个现成组件，查新版、装更新、失败兜底、更新日志与多插件日志一次包掉.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard di verifica senza dipendenze per i plugin DeepSeek Harness (dsh)…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): scheda laterale market-dashboard per il…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode su DeepSeek Harness — plugin DSH che mantiene operativi OpenCode Zen +…
- [27painter/dsh-moli](https://github.com/27painter/dsh-moli) - DSH plugin · Drive the local Moli headless browser from DeepSeek Harness…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace di plugin di terze parti e gestore del ciclo di vita…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx è una workstation desktop estensibile e incentrata sulle persone…
- [DoveLi-Gu/dsh-showcase](https://github.com/DoveLi-Gu/dsh-showcase) - Local, verifiable delivery evidence reports and DSH plugin for coding-agent…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入.
- [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) - DSH的插件创意市场来啦!～～～欢迎使用&amp;提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方…
- [momasiku/dsh-pilot](https://github.com/momasiku/dsh-pilot) - Desktop automation for DeepSeek Harness: hands and eyes on the whole Windows…
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色：换装、白饭、摸头、问候、登录账户余额和本机今日用量预估.
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [ytftu/dsh-session-cost](https://github.com/ytftu/dsh-session-cost) - DSH（DeepSeek Harness）插件：底栏会话消费金额、每条回复本轮金额、右上角开放平台余额/今日用量/峰谷，点击弹出折线图.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin DeepSeek Harness: trasforma il fallimento del provisioning dell.
- [akkefa/deepseek-cordis](https://github.com/akkefa/deepseek-cordis) - Python plugin runtime targeting DeepSeek Harness vendored Cordis semantics.
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…

</details>

<a id="writing"></a>

## Testi, discussioni e video

Articoli, discussioni e video sulla funzionalità delle mod.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 1 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 14 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

##### 📝 Riepilogo

Ciao HN, l'ho creato per me e ho voluto renderlo open source. Il problema: volevo un modo per ricevere promemoria tra un prompt e l'altro, perché spesso trascorro molte ore nel terminale, soprattutto ora che di solito elaboriamo in parallelo così tanti agenti. La prima versione era un rep

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 14 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

##### 📝 Riepilogo

Ho creato questo perché, con gli ultimi modelli di coding, Claude entra in modalità di lavoro intenso con comandi oscuri, al punto che non so più cosa stia facendo. Questa è una modifica (un plugin che usa i nuovi function hook di Claude Code) che traccia una riga sopra il prompt: - il passaggio corrente,

##### 📌 Informazioni di base

| Campo     | Valore                                                                              |
| --------- | ----------------------------------------------------------------------------------- |
| Categoria | `Testi, discussioni e video`                                                        |
| Prova     | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Prima comparsa nell'elenco | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Progetti per linguaggio di implementazione

L'ecosistema è concentrato in Python e TypeScript, ma continuano a comparire client tipizzati in altri linguaggi. Questa tabella viene generata dalle voci stesse.

| Linguaggio | Voci | Esempi                                                                                                        |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 371  | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 82   | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 43   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 14   | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 10   | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 4    | `vulcanshen/ccdrawu`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                         |
| Kotlin     | 2    | `Clarklevis1995/dsh-mobile`, `dphmoblie/deepseek-harness-android`                                             |
| PowerShell | 2    | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| AutoHotkey | 1    | `keithwalsh/claude-code-mods`                                                                                 |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `DimeDataCloud/open-ClaudeOS`                                                                                 |
| Java       | 1    | `bloodtmai-cmyk/dsh-ai-hub`                                                                                   |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |
| Ruby       | 1    | `romacv/claude-plan-usage-statusline`                                                                         |
| Swift      | 1    | `eovidiu/cordis-ios`                                                                                          |
| jq         | 1    | `n0nuser/claude-statusline`                                                                                   |

<sub>Vengono conteggiate solo le voci che dichiarano una lingua. Le voci di documentazione e discussione sono escluse da questa tabella.</sub>

## Contribuire

Le correzioni sono benvenute e rappresentano il modo più rapido per migliorare questo elenco. Apri una issue o una pull request se una voce è classificata o valutata erroneamente, oppure se un progetto è stato escluso per errore a causa di una collisione di nomi — è proprio in quest'ultima categoria che i filtri automatici hanno più probabilità di sbagliare.

---

<sub>Progetto indipendente della community. Non affiliato a Anthropic, né approvato o revisionato da quest'ultima. Claude Code, Claude e Anthropic sono marchi commerciali di Anthropic. Il comportamento del prodotto può cambiare senza preavviso; verifica qualsiasi informazione essenziale nella documentazione ufficiale. Le risorse restano di proprietà dei rispettivi progetti upstream e vengono riprodotte solo quando una licenza lo consente.</sub>

<sub>Ultimo aggiornamento · 2026-10-16T14:49:31+08:00</sub>
