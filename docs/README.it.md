<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod straordinarie per Claude">
</p>

<h1 align="center">Mod straordinarie per Claude</h1>

<p align="center"><b>L'indice di mod e plugin per Claude Code, valutati in base alle evidenze, e dei comportamenti più profondi che modificano.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-494-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <b>Italiano</b> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indice aggiornato** · Ultima sincronizzazione: `2026-10-13T19:28:29+08:00` (UTC+8)
> · Voci: **494** · Aggiunte nell'ultimo aggiornamento: **0** · Linguaggi di implementazione: **13**

<sub>Ogni voce qui sotto è stata raccolta, filtrata e verificata nuovamente in automatico. Nessuna voce è un'inserzione a pagamento.</sub>

<a id="featured"></a>

## Selezioni del momento

<sub>Una voce per categoria, classificata in base al livello delle prove e alle stelle, con ricalcolo a ogni aggiornamento. È una classifica, non un'approvazione; ogni selezione rimanda alla relativa scheda completa qui sotto. Sono preferiti i progetti che hanno pubblicato uno screenshot o una registrazione, così la fascia rimane visiva.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9493 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2548 · Python · 👁️ observed</sub>
<sub>Trova i token fantasma. Sistemali. Sopravvivi alla compattazione. Evita il degrado della qualità del contesto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74489 · TypeScript · 👁️ observed</sub>
<sub>🌊 L&#x27;agent harness originale. Distribuisci sciami intelligenti multi-player, coordina flussi di lavoro autonomi e crea sistemi di AI conversazionale. Include memoria…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Contenuti

- [Che cos'è una mod per Claude Code](#che-cosè-una-mod-per-claude-code)
- [Come vengono valutate le voci](#come-vengono-valutate-le-voci)
- [Ufficiali: repository e note di rilascio di Anthropic](#ufficiali-repository-e-note-di-rilascio-di-anthropic) — **14**
- [Mod: realizzate con la funzionalità mod](#mod-realizzate-con-la-funzionalità-mod) — **371**
- [Gli ecosistemi dei plugin DSH e Cordis](#gli-ecosistemi-dei-plugin-dsh-e-cordis) — **98**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150543 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Riepilogo

Claude Code è uno strumento di programmazione agentico che vive nel terminale, comprende la tua base di codice e ti aiuta a programmare più velocemente eseguendo attività di routine, spiegando codice complesso e gestendo i flussi di lavoro git, tutto tramite comandi in linguaggio naturale.

<sub>🔧 Trovato nel codice: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | TypeScript                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **150543** |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9493 · TypeScript · ✅ official · 3 天</summary>

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
| Stelle                     | **9493**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8261 · Python · ✅ official · 3 天</summary>

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
| Stelle                     | **8261**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6361 · Python · ✅ official · 243 天</summary>

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
| Stelle                     | **6361**   |
| Ultimo push                | 2026-02-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1804 · Shell · ✅ official · 3 天</summary>

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
| Stelle                     | **1804**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

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
<summary><b>Altro in questa categoria</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Aggiunto `$.ui.notify` per le mod: genera una notifica nativa tramite la tua…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Risolto il problema per cui Esc o un.

</details>

<a id="mods"></a>

## Mod: realizzate con la funzionalità mod

Ogni voce qui mostra prove dell'uso della funzionalità che Claude Code ha acquisito nella versione 2.1.287: esegue il rendering tramite `ui.render`, gestisce un pannello, una fascia o una scheda, legge `$.ui.selection()`, avvia compagni di squadra con `agent.spawn` oppure dichiara esplicitamente di essere una mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2548 · Python · 👁️ observed · 0 天</summary>

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
| Stelle                     | **2548**   |
| Ultimo push                | 2026-10-13 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐548 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **548**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐339 · Python · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

macOS menu bar & Windows tray app pinning Claude Code, Codex, Antigravity & Grok CLI quota, burn rate, and cost to your screen. Local-first, no LLM API calls. HTML reports, 14 themes.

<sub>🔧 Trovato nel codice: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | Python                                                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **339**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐221 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **221**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐166 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stelle                     | **166**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐164 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Claude Code mostra immagini e riproduce video direttamente nel terminale: screenshot, registrazioni Playwright e QA sincronizzato prima/dopo. Ghostty e kitty.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **164**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐128 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **128**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **96**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 4 天</summary>

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
| Stelle                     | **79**     |
| Ultimo push                | 2026-10-08 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐77 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **77**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

##### 📝 Riepilogo

Mod di Claude Code di Darrell Wang — bande sopra il prompt, zero token del modello. Dashboard per azioni taiwanesi／azioni statunitensi + altro in arrivo.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | HTML                                                                                |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **65**     |
| Ultimo push                | 2026-10-05 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 6 天</summary>

##### 📝 Riepilogo

Skills, agenti, comandi, regole, hook e stili di output esperti per Claude Code — continuità delle sessioni + strumenti CLI moderni per flussi di sviluppo reali

<sub>🔧 Trovato nel codice: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | Shell                                                                               |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **62**     |
| Ultimo push                | 2026-10-07 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐49 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: barre di avanzamento del piano in tempo reale sopra il prompt

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **49**     |
| Ultimo push                | 2026-10-08 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arjun0014/project-sentinel">Arjun0014/project-sentinel</a></b> · ⭐47 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Centro di controllo per le esecuzioni prolungate di Claude Code: contesto e avanzamento dell'esecuzione a colpo d'occhio, passaggi di consegne Autopilot, protezioni e una vista delle attività rilassata, nel terminale e in Claude Desktop.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **47**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-agents-automation` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arjun0014--project-sentinel/cd63c979e03573e7.png" width="100%" alt="Arjun0014/project-sentinel screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Riepilogo

Guarda Claude Code inventare un piccolo cartone animato mentre lavori.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **32**     |
| Ultimo push                | 2026-10-02 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐29 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stelle                     | **29**     |
| Ultimo push                | 2026-10-03 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐28 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **28**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Un Pokémon pixelato che vive sopra il prompt in Claude Code

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **25**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Riepilogo

Build, test, console e anteprime SwiftUI di Xcode dentro Claude Code

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
| Ultimo push                | 2026-10-02 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stelle                     | **20**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐18 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **18**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stelle                     | **13**     |
| Ultimo push                | 2026-10-03 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stelle                     | **13**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 6 天</summary>

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
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stelle                     | **10**     |
| Ultimo push                | 2026-10-04 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

##### 📝 Riepilogo

Tracker di sessione per Claude Code realizzati come mod: finestra di contesto, consumo della quota del piano, costo per turno

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
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stelle                     | **9**      |
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
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **9**      |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stelle                     | **9**      |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary><b>Altro in questa categoria</b> <sub>· 337</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Raccolta di oltre 100 mod utilizzabili con Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod di Claude e strumenti per crearle: prima una competenza per la creazione…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mod di Claude Code di Ray Amjad: riquadri, bande, protezioni del prompt…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - L.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Usa Claude Mods per mettere un nuovo tetto a Claude Code: senza modificare il…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quattro mod di Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mod di Claude Code di Learning Hacker: rendono il funzionamento dell.
- [kakha13/claude](https://github.com/kakha13/claude) - Mod di Claude Code che correggono e traducono i tuoi prompt prima che Claude li…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base di conoscenza di Obsidian con fonti citate sui mod di Claude Code: come…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mod e skill di Claude Code di Nekyia Labs, creati e utilizzati quotidianamente…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Un aspetto da applicazione desktop per la trascrizione del terminale di Claude…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mod di Claude Code: menu Strumenti Claude, modalità Zen, temi del terminale…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Pannello della barra laterale di Claude Desktop (scheda Code): elenca tutti i…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra di utilizzo sopra la casella di input di Claude Desktop (scheda Code)…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un riquadro laterale per Claude Code: i subagenti eseguiti da una sessione, ciò…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill che insegna agli agenti di Claude Code a creare mod Claude.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin e skill Claude della community, installabili da un unico mercato.
- [davekiss/mods](https://github.com/davekiss/mods) - Mod di Claude Code di Dave Kiss.
- [devbrother2024/devbrothers-mods](https://github.com/devbrother2024/devbrothers-mods) - Raccolta di mod di Claude Code di 개발동생.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mod di Claude (plugin con hook di funzione) per Claude Code.
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Il tuo piano, mentre osserva se stesso.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galleria di mod di Baselane: mod di Claude Code, verificati e fissati in…
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una coda decisionale CLI/TUI per persone che lavorano con agenti…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod del pannello IDE di Claude Code: board dell.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod di Claude Code che visualizza le differenze di Edit e Write in due colonne…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, visualizzato nella casella del prompt di Claude Code mentre digiti.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mod di Claude Code: pannello dei consumi usage-hud di 像素螃蟹 + link HTML…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Scheda di stato flottante per Claude Code — modello, contesto, limiti di…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mod per Claude Code: plugin con hook di funzione che aggiungono riquadri live e…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Il plugin all-in-one per Claude Code. Parla con la tua squadra, condividi…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Un test di digitazione per passare il tempo mentre Claude lavora.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mod di Claude Code: screen-guard nasconde nomi e segreti mentre condividi lo…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mod e skin per Claude Code: una barra di avanzamento live per le attività di…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Estensioni di Claude Code. Sblocca tutta la potenza di Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) di Claude Code che aggiunge un pannello laterale con schede…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Pannelli, protezioni e mod per migliorare l&#x27;esperienza d&#x27;uso di Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Due mod di Claude Code sopra la casella del prompt: indicatore della finestra…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Legge i file markdown a cui Claude Code dà un nome, visualizzati accanto alla…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod di Claude Code: miniature delle immagini incollate sopra il prompt, in…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collaboratore vocale per Claude Code. Parla delle tue idee con un lupo 3D…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow per Claude Code: una checklist essenziale sopra il prompt che mostra…
- [BatuhanCakmakk/wavy-usage](https://github.com/BatuhanCakmakk/wavy-usage) - Anelli di utilizzo riempiti di liquido sopra il prompt di Claude Code: limiti…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mod di Claude Code: barra del contesto, pannello degli agenti, sfocatura PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mod di Claude Code: typing-speed, un tachimetro della velocità di digitazione…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuochi d.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mod per Claude Code: pannelli, comandi e hook realizzati con il plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Scopri mod, plugin ed estensioni di Claude Code con demo animate, elenchi per…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod di Claude Code: diagrammi Mermaid disegnati direttamente nella trascrizione.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Piccoli mod di Claude Code (plugin con hook di funzione): session-switcher e…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Un app store per le mod di Claude Code, dentro Claude Code: /mods per…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sei modifiche di Claude Code: limiti del piano e contesto sopra il prompt…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mod di Claude Code: mod-scout (trova i mod che useresti di più), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Due mod di Claude Code per eseguire molte sessioni contemporaneamente: una…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mod Claude Code on demand — una skill che legge la tua conversazione e…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: scopri, esamina, attiva/disattiva e aggiorna i mod di Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - I migliori mod di Claude Code: selezionati, convalidati, fissati in alto.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code: routing automatico del modello Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Mod di Claude Code: un riquadro in tempo reale delle PR di GitHub che una…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sei mod per Claude Code: mascotte animata Clawd, barre per limite d.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Un marketplace di mod per Claude Code: un debugger passo-passo per il ciclo…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mod open source per Claude Code: riquadri, righe di stato, notifiche…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Il miglior pacchetto di mod tutto-in-uno per Claude Code: limiti di utilizzo e…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Riproduci YouTube Shorts nel tuo Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Toolkit di Naren per Claude: skill, mod e server MCP per Claude Code.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mod per Claude Code: Clawd, una piccola mascotte pixelata che mette in scena…
- [reporails/arcade](https://github.com/reporails/arcade) - Giochi desktop classici come mod di Claude Code, giocabili in un riquadro…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods per claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace delle mie mod per Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Un elenco curato di mod di Claude Code, installabili come marketplace di…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Due mod di Claude Code: cache-keeper e ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mod di Claude Code che mantengono onesto un agente — hook di funzione che…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Appena uscito dalla fabbrica. Una mod di Claude Code: chiedi un meme e continua…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della cache dei prompt, prossimi passi, pulsanti…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Una mod di Claude Code che mostra i limiti di utilizzo e la spesa nella fascia…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Una mod per Claude Code per catturare i pensieri durante il lavoro…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Stato PR di GitHub in tempo reale, disponibilità al merge, controlli, commenti…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Alleva un uovo al tè che si insaporisce lentamente mentre scrivi code · Alleva…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Le mod di Claude Code di Herman (marketplace herman-mods).
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Scopri cosa eseguono in background le sessioni di Claude Code: subagent…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod di Claude Code: rispondi a Claude punto per punto, direttamente sul testo.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Note sul campo del primo giorno sulle mod di Claude Code su Windows: una barra…
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Mod di Claude Code: stato live della pull request GitHub.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod di Claude Code: misuratori live di costo, contesto e quota del piano sopra…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod di Claude Code: un SDLC AI-native.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod per Claude Code che attiva o disattiva le tue competenze, i tuoi agenti…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod di Claude Code testate e installabili con un solo comando: protezioni per…
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un insieme di mod per claude code realizzate da me.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modifiche al codice di Claude. touch-map: mostra quali file Claude ha elencato…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Impara una lingua straniera mentre lavori con Claude Code.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Di&#x27; a Claude cosa vuoi. Ricevilo costruito, testato, revisionato da un&#x27;altra IA…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Si occupa di una lunga sessione di Claude Code al posto tuo: osserva il…
- [Akeuuh/claude-mods](https://github.com/Akeuuh/claude-mods) - Claude Code plugin marketplace: mods built on function hooks.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra laterale in tempo reale per costi, token e utilizzo del contesto di…
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Mod basate su function hook per Claude Code: riga di telemetria dei limiti…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Una mod di Claude Code che mantiene un elenco aggiornato degli elementi aperti…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mod di Claude Code per veri ingegneri.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Riepilogo della sessione terminale di Claude Code, nella scheda Code dell.
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Mod di Claude Code: visualizza quali competenze, plugin, sottoagenti e…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Vedi quali file ogni agente di Claude Code ha nel proprio contesto, e quanto di…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Piccole mod di Claude Code per il terminale e l.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI che aggiunge parole spagnole nelle risposte dell.
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Mod di Claude Code – smetti di sprecare token: /keepwarm.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - I tuoi eventi Alarum sopra il prompt di Claude Code: cosa è appena arrivato e…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Il backlog di Floatee sopra il prompt di Claude Code: esegui, guida e spunta le…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Una mod di Claude Code che lo rielabora come The Machine di Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod di Claude Code per flussi di lavoro DAG obbligatori e…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod di Claude Code: stato della sessione, avanzamento live di Spec Kit e…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La finestra di contesto come un.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Mod di Claude Code: seleziona il modello e il livello di ragionamento di ogni…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: un grafo in tempo reale di ciò che Claude Code sa.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD delle attività in tempo reale per Claude Code Desktop: una fascia sopra…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) di Claude Code che fa apparire l.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Non lasciare che la tua attenzione divaghi mentre aspetti la risposta di Claude…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Un plugin gratuito e open source per Claude Code.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Una coda di prompt per Claude Code, come mod: /after &lt;task&gt; esegue l.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Mod Claude Code: selezionati, testati e ciascuno distribuito con il prompt che…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Competenze di Claude Code: verificatore dei fatti per la documentazione…
- [partalemre/MODZ](https://github.com/partalemre/MODZ) - 17 plugin di Claude Code in un unico pannello.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod per Claude Code: percorsi cliccabili nelle risposte — fai clic su una…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin buddy di Claude Code: un compagno ASCII sopra il prompt che ricorda le…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Raccolta di mod eccezionali per Claude Code | Raccolta di mod per Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: una mod di Claude Code che legge ad alta voce, su richiesta, le…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Spank Claude when it messes up — a stress-relief mod for Claude Code: cartoon…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod di Claude Code: piccoli plugin per riquadri in tempo reale, instradamento…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, con prove. Un plugin che pianifica, delega e dimostra che il…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod di Claude Code: quota 5h/7d, finestra di contesto, tempo residuo della…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin di Claude Code: monitoraggio dell.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Mod di Claude Code: EMCC (Every Mod Claude Code), una raccolta curata e testata…
- [adithepmeekhun/self-clear](https://github.com/adithepmeekhun/self-clear) - Una mod per Claude Code che mantiene in esecuzione le lunghe sessioni degli…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gatto braille animato sopra il prompt di Claude Code.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gatto pixel sopra il prompt di Claude Code che esegue una chiamata di test a…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Una mod di Claude Code che sceglie il momento giusto per compattare e mantenere…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modifiche di Claude Code per Claude: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mod generiche per Claude Code: bande, pannelli, notifiche e hook.
- [aott33/model-router](https://github.com/aott33/model-router) - Una mod di Claude Code che seleziona il modello per ogni subagente prima…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Una mod di Claude Code: la finestra di contesto in un.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - La nave delle righe LGTM salpa dopo ogni modifica al codice — una mod di Claude…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - I tuoi limiti di utilizzo di Claude come scheda animata della salute di un…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mod di Claude Code per il team S2 (il marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Brevi allenamenti mentre Claude lavora: un obiettivo giornaliero, serie, badge…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un pannello di utilizzo per Claude Code: spesa per modello.
- [bahaospanov/skills](https://github.com/bahaospanov/skills) - I mod di Claude Code di Bakhtiyar Ospanov: plugin basati su hook di funzione.
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Una mod di Claude Code che mostra le attività dei subagenti: una barra di…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Una mod di Claude Code che mostra quanto è durata ogni interazione, in un…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing per Claude Code: Apple Music e Spotify sopra il prompt, con…
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - La scheda Prestazioni per Claude Code mostra un waterfall live di ogni…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod per Claude Code: orologio della cache, Blast Radius, suggerimenti, lista di…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un gufo per il tuo Claude Code.
- [cerebrai/ironman-mod](https://github.com/cerebrai/ironman-mod) - Una mod claude code per un flusso di lavoro umano-AI aumentato -- come tony…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Mantieni Claude Code su un piano: fasi, passaggi di approvazione e budget dei…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi che vive dentro Claude Code: si schiude, mangia il codice scritto…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Preferiti per Claude Code: icone con un clic per i tuoi comandi e le tue…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mod di Claude Code (plugin con hook sulle funzioni): session-meter e altro.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Nascondi-mod di Claude: un piccolo pulsante che nasconde tutte le mod di Claude…
- [finalpantasy/claude-mod-pack](https://github.com/finalpantasy/claude-mod-pack) - Pacchetto di mod Claude: piccole mod di Claude Code.
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Mod di Claude Code: congela una sessione e riprendila più tardi come se non…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+clic sul link di copia in ogni blocco di codice nelle risposte di Claude…
- [guojunjie0614-cyber/workhorse](https://github.com/guojunjie0614-cyber/workhorse) - Claude Code mod: hand coding, review and ops jobs to Codex as background…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Un indicatore live della spesa per Claude Code: il costo della sessione con…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod di Claude Code: quanto tempo ha richiesto ogni risposta, quanto ha pensato…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Un cockpit sopra il prompt di Claude Code. L.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Legge automaticamente i tuoi disegni tecnici, quindi crea il modello in…
- [jBeyondstars/ultracode-models](https://github.com/jBeyondstars/ultracode-models) - Claude Code mod: pick the model and effort every subagent runs on, Ultracode…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - Una bacheca in tempo reale dei sottoagenti di Claude Code dentro VS Code: i…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Pannello laterale dell.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Elenco laterale dei file: quali file sono stati creati, modificati o eliminati…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Mao Mao in stile 8-bit (coniglio nano olandese bianco e nero) corre e salta…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Pannello laterale «Le mie domande»: ogni frase digitata dal proprietario in…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Cronologia laterale: dove è stato impiegato il tempo di questo turno.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Scambio di token nella barra laterale: quanti token la conversazione principale…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Il sincero sacchetto di fagioli di claude code: al termine di ogni turno…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 汉化（自管版）——propria tabella di traduzione + strumento di patch +…
- [jidhra/claude-mods](https://github.com/jidhra/claude-mods) - Jidhra.
- [kadaliao/claude-mods](https://github.com/kadaliao/claude-mods) - Mod di Claude Code: plugin con hook di funzione che modificano l.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive in una fascia sopra il prompt di Claude Code: mette in scena la…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod che legge ad alta voce le risposte e le notifiche di Claude Code tramite…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mod di Claude Code. PixBar: una creatura pixelata sopra il tuo prompt che si…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod per Claude Code: ogni sessione di Claude Code in un.
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Piccole mod di Claude Code in un unico marketplace di plugin.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Una guida ai mod di Claude Code curata dalla community: casi d.
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Mod di Claude Code: i limiti del tuo piano (sessione di 5h, settimana) e il…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Una mod di Claude Code che mostra cosa sta facendo Claude nel sottotitolo della…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, un compagno pixel non ufficiale creato dai fan che vive sopra il prompt…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Un soffice gatto nero sopra il tuo prompt di Claude Code.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Piccoli mod per Claude Code: runner-avatar, un piccolo avatar che corre sopra…
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod di Claude Code: un pannello live di ciò a cui mira, di ciò che presume…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod di Claude Code: riquadro /sessions per sfogliare ed eliminare le sessioni…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mod della community per Claude Code: protezioni, pannelli e comandi eseguiti…
- [mkiselyow/diff-lens](https://github.com/mkiselyow/diff-lens) - Mod di Claude Code: chiedi a Claude di guidarti attraverso una PR, fai clic su…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Mod di Claude Code: Codex (abbonamento ChatGPT) e altri modelli non-Anthropic…
- [MohamedHamed001/claude-mods](https://github.com/MohamedHamed001/claude-mods) - Claude Code plugins: delegation.
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Mod di Claude Code: assegna un nome alla scheda del terminale in cui viene…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod di Claude Code che riattiva gli strumenti todo per i modelli che li…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod di Claude Code che attende una pausa sicura, poi trasferisce la sessione o…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod di Claude Code: una riga per ogni attività sopra il prompt con l.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Gioca a Connect Four contro un.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Modifica al codice di Claude: quando un altro agente di programmazione esegue…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Modifica al codice di Claude per repository condivisi da diversi agenti IA…
- [niksavis/handily](https://github.com/niksavis/handily) - Claude Code mods that show your work items, tasks and sessions, for any…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barriera di sicurezza per SQL in Claude Code: chiede conferma prima che…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Un pannello blocco note per Claude Code, come mod.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Una modifica per Claude Code, Windows e CJK prima di tutto: anteprime di…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - I migliori mod di Claude Code, ordinati in base a ciò che fanno per te.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Due mod Claude per Claude Code: garde-du-corps.
- [partalemre/transceiver](https://github.com/partalemre/transceiver) - Plugin di Claude Code (beta): chat del team all.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: un mod di Claude Code. Worktree permanenti con un avvio in sola…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Riquadro laterale con statistiche live della sessione per la scheda Code…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code: flessioni da fare mentre Claude lavora. Nessun token.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: una guida pratica ai mod di Claude Code, dalla spiegazione per…
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Un marketplace open source per i mod di Claude Code, con competenze del…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod di Claude Code: trasforma il piano approvato in modalità piano in una…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una selezione curata di mod di Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modalità senza costi: gli agenti ausiliari funzionano su Haiku e i file e i log…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una colonna sonora lofi che segue la sessione: calma, concentrazione, flusso…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Impara mentre Claude programma: dopo un turno che ha modificato il codice…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una registrazione di ogni modifica effettuata da Claude: riproduci ogni…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Le mod di Claude Code di Showrin per una produttività quotidiana maggiore.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Mod di Claude Code: limiti di contesto e piano con proiezione del tasso di…
- [sohi2212/claude-agent-radar](https://github.com/sohi2212/claude-agent-radar) - Mod di Claude Code: radar in tempo reale degli agenti in background + canvas di…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Mod di Claude Code che mantiene attive le sessioni non presidiate oltre i…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Marketplace di mod personalizzati per Claude Code (cc-mods), con mod di esempio…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messaggi di commit con un clic per Claude Code con una Malenia in pixel-art che…
- [SummerRiversound/review-inbox](https://github.com/SummerRiversound/review-inbox) - Mod di Claude Code: PR in attesa della tua revisione, ciascuna riassunta in…
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Mod per Claude Code. cache-meter: percentuale di riscontri positivi della cache…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod di Claude Code che mostra l.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Mod non ufficiali di Claude Code di tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod di Claude Code che mostra la sessione corrente in un pannello: ogni…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace di plugin Claude Code di mod: plugin function-hooks che…
- [thunini/thinking-flow](https://github.com/thunini/thinking-flow) - Una mod per Claude Code che mostra come Claude è arrivato a ogni risposta: la…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Ascolta le risposte di Claude Code mentre la frase letta viene evidenziata.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Mod di Claude Code: un pulsante sotto l.
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - Modalità CC che mostra a quale account, organizzazione e piano Claude hai…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod di Claude Code: fascia di avanzamento animata e riepilogo del completamento…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tre piccoli mod di Claude Code: scopri quando i tuoi sottoagenti termineranno…
- [varunmoka7/disk-sweep](https://github.com/varunmoka7/disk-sweep) - Avvisa quando il Mac ha poco spazio su disco e, con /disk, elenca i residui…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di.
- [varunmoka7/park](https://github.com/varunmoka7/park) - Salva questa sessione di Claude Code e scrivi una nota per la successiva.
- [varunmoka7/read-fence](https://github.com/varunmoka7/read-fence) - Impedisce a Claude di aprire i file delle cartelle di skill, regole e plugin…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Fai a Claude una domanda laterale in un riquadro accanto al tuo lavoro.
- [varunmoka7/skills-az](https://github.com/varunmoka7/skills-az) - Mostra un elenco dei tuoi comandi slash e delle skill in ordine alfabetico non…
- [varunmoka7/unattended](https://github.com/varunmoka7/unattended) - Impedisce a una sessione di Claude Code di farti domande quando non c.
- [vcdim/claude-code-sciplot](https://github.com/vcdim/claude-code-sciplot) - Una mod di Claude Code per i grafici scientifici: Python, R, TikZ, MATLAB e…
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Plugin per Claude Code: conto alla rovescia della cache dei prompt, percentuale…
- [wonwoo/tool-timeline](https://github.com/wonwoo/tool-timeline) - Una mod di Claude Code che mostra dove è finito il tempo di ogni turno: una…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Claude Code: i tuoi limiti di utilizzo Claude Pro/Max con una…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod per Claude Code. agent-crew: osserva i tuoi subagenti al lavoro come un…
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
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Una dashboard completa di statusline per Claude Code — informazioni sulla…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: monitora l.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Una statusline estetica per Claude Code di awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills e mod pubblici per Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mod, subagent, hook, comandi slash e guide per Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legali gratuiti e agenti di coding — autoaggiornati, verificati con…
- [aiedwardyi/claude-usage-monitor](https://github.com/aiedwardyi/claude-usage-monitor) - Plugin statusline di Claude Code per quote di 5 ore/7 giorni, utilizzo del…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Risultati in diretta, calendari e classifiche di calcio per la competizione…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill che trasforma il tuo agente di coding in un esperto di firmware per…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Orari delle preghiere, data Hijri, adhkar, ayah quotidiana, digiuno sunnah…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configurazione personale di Claude Code versionata all.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Raccolta di plugin per Claude Code, pi e DeepSeek Harness: HUD della barra di…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Toolkit portatile di Claude Code per DDD/Architettura Pulita .NET: agenti TDD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configurazione globale portabile di Claude Code: competenze personalizzate…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mod non ufficiali per la scheda Code di Claude Desktop — usage-pet: una banda…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin di Claude Code che uso ogni giorno: skill e mod, ripuliti per funzionare…
- [vtmocanu/cc-statusline](https://github.com/vtmocanu/cc-statusline) - Statusline ANSI su due righe per Claude Code: contesto git + k8s, barre dei…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analizza l.
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Statusline elegante e informativa per Claude Code.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Una bacheca visuale per i tuoi agent Claude Code: visualizza sessioni, subagent…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Statusline personalizzabile per Claude Code con editor drag-and-drop.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace per plugin e skill di Claude Code per facilitare la creazione di…
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Statusline a riga singola e codificata a colori per Claude Code — cartella…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visualizzatore a pannelli divisi per Claude Code in Windows Terminal e tmux: la…
- [ian-exnodes/statusbar](https://github.com/ian-exnodes/statusbar) - Claude Code plugin: a live two-row status line under the prompt with model…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Riga di stato live della fase del workflow per Claude Code.
- [mvrozanti/claude-progressbar](https://github.com/mvrozanti/claude-progressbar) - Barre di avanzamento per i comandi Bash eseguiti da Claude Code, disegnate…
- [naturalmoods/herdr-telegram-notify](https://github.com/naturalmoods/herdr-telegram-notify) - Messages you on Telegram when an agent finishes or needs input, with its last…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Un micro-dashboard a 3 righe per il terminale Claude Code — modello, consumo…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository per mod Awesome Media di Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Riduci la spesa di Claude Code e dei token Codex: indirizza ricerche e test…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Una statusline veloce e configurabile per Claude Code — singolo binario statico…
- [barkleesanders/claude-hud](https://github.com/barkleesanders/claude-hud) - Display heads-up in tempo reale per Claude Code — salute del contesto, attività…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Una statusline amplificata e con colori graduati, senza dipendenze, per Claude…
- [ist-j-ichikawa/claude-code-statusline](https://github.com/ist-j-ichikawa/claude-code-statusline) - Statusline personalizzata di j-ichikawa per Claude Code CLI.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Display key status details for Claude Code including model, context, limits…
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Statusline compatta e mantenuta attivamente per Claude Code — modello, impegno…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Team di agenti nativi. Sotto controllo.
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Riga di stato PowerShell di Windows Code per Claude Code: limiti di 5 ore e…
- [barnabys-drew/claude-code-statusline](https://github.com/barnabys-drew/claude-code-statusline) - statusLine di Claude Code — barre del contesto e dei limiti di frequenza…
- [black-astro/claude-statusline-astro](https://github.com/black-astro/claude-statusline-astro) - Statusline di Claude Code — cartella, ramo, modello e utilizzo su una sola…
- [Chy-Zaber-Bin-Zahid/claude-code-statusline](https://github.com/Chy-Zaber-Bin-Zahid/claude-code-statusline) - Una status line di Claude Code con barre per il contesto e l.
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Riga di stato di Claude Code in Lua, con un playground Neovim in tempo reale.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline di livello professionale per Claude Code: durata della sessione…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - Plugin Claude Code di divramod, un unico marketplace: skill degli agenti e…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Una riga di stato per Claude Code: contesto, limiti e ritmo della settimana, CI…
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - Estensione di VS Code: avanzamento dell.
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Anteprima immagini dentro Claude Code: passa il mouse su un chip sotto una…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Riga di stato di Claude Code: modello, barre della quota 5h/7d, barra della…
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sync Claude.
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Visualizza una barra di stato dettagliata e codificata a colori per Claude…
- [KitchenSink4AI/claude-code-statusline](https://github.com/KitchenSink4AI/claude-code-statusline) - L.
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Barra di stato su due righe per un agente di coding da terminale: directory…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook della status line di Claude Code — monitora l.
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Statusline di Claude Code con installer per Linux e Git Bash su Windows.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — statusline di Claude Code per macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitora lo stato di Claude Code dalla barra dei menu di macOS, con indicatori…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Statusline personalizzata di Claude Code.
- [sgarcia-dev/claude-agent-watch](https://github.com/sgarcia-dev/claude-agent-watch) - Live pane and status line for the Codex, OpenCode, Antigravity, Hermes and…
- [silee-tools/claude-statusline](https://github.com/silee-tools/claude-statusline) - HUD statusline verticale a pila indipendente dalla larghezza per Claude Code.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configurazione portatile di Claude Code (riga di stato + installatore).
- [steemandavid/claude-code-statusline](https://github.com/steemandavid/claude-code-statusline) - Status line personalizzata per Claude Code — modello, contesto e statistiche di…
- [Synforger/claude-code-statusline](https://github.com/Synforger/claude-code-statusline) - Statusline per Claude Code che mostra a colpo d.
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Riga di stato di Claude Code di 4 righe.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configurazione portatile di Claude Code: CLAUDE.md, impostazioni, statusline…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ StatusLine multiprotocollo universale, autoapprendimento del contesto e…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Monitora l.
- [wcampbell-dw/claude-plugins](https://github.com/wcampbell-dw/claude-plugins) - Plugin di Claude Code: spinner in tempo reale per i subagenti, status line Nerd…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Sincronizzazione della configurazione a livello utente di Claude Code su più…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Rilevatore del deterioramento del contesto 2026 - Monitor proattivo della…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagent e statusline di Claude Code: raccolte e strumenti open-source…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Un builder visuale per le statusline di Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline di Claude Code che mostra l.
- [lexfrei/ailine](https://github.com/lexfrei/ailine) - Statusline di Claude Code con limiti d.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mod per Claude Code: riquadri, bande e compagni basati su hook di funzione.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passa le attività tra le tue sessioni di Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Questo è un server MCP per controllare MODS, lo strumento modulare…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: trova ciò che chiedi ripetutamente a Claude Code e trasformalo in un…
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Libreria di 3 skill per Claude Code: session-handoff, session-statusline e…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill di Codex e Claude Code per tradurre mod di CK3 con un LLM locale.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mod open source e altre estensioni per Claude Code.

</details>

<a id="dsh-cordis"></a>

## Gli ecosistemi dei plugin DSH e Cordis

DeepSeek Harness e Cordis arrivano allo stesso risultato da una direzione diversa: per loro il plugin è il meccanismo delle mod, quindi un plugin lì equivale a una mod qui.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74489 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **74489**  |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐184903 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **184903** |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100875 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

🎨 Il miglior plugin di progettazione per DeepSeek Harness. L'alternativa open source a Claude Design. 🖥️ App desktop locale. 🖼️ Il tuo agente di programmazione diventa il motore di progettazione: prototipi, landing page, dashboard, presentazioni, immagini e video — file reali, esportazione HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode e oltre 20 CLI tramite BYOK.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **100875** |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82831 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **82831**  |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35774 · Go · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **35774**  |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30656 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **30656**  |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25562 · Python · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **25562**  |
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
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9157 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **9157**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8691 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8691**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4532 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Il plugin TUI ufficialmente più consigliato da DSH: alte prestazioni, basso sovraccarico, simpatica balena pixelata, interazione fluida con il mouse. Installazione con un solo comando tramite npm. / Il plugin TUI ufficialmente più consigliato da DSH: alte prestazioni, basso utilizzo di risorse, simpatica balena pixelata, interazione fluida con il mouse, installazione con un solo comando tramite npm

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **4532**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3684 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Il primo terminale virtuale al mondo per AI Agent

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3684**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3422 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3422**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3251 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Answer me with HTML — an agent skill that answers hard questions with a one-page HTML you can actually read. 让 AI Agent 用一页 HTML 回答复杂问题。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3251**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2064 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Il miglior plugin DeepSeek Harness per analisi e gestione del contesto, con dashboard / browser / sidebar del contesto e comando contestuale, per statistiche del contesto, composizione, scomposizione, dettagli sull’evoluzione, comprensione di com’è fatto il contesto e di come evolve. Plugin all-in-one di visualizzazione del contesto per DeepSeek Harness, con pannello Context, browser e barra laterale, e comando Context, per analizzare composizione, evoluzione, compressione, pruning e altri eventi e azioni del contesto.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **2064**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1942 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **1942**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1640 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Postazione di lavoro Agent open source multipiattaforma

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1640**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1185 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Memoria per Claude Code, Codex, Cursor e altri 38 agenti di coding, costruita a partire dalla cronologia delle sessioni già presente sul disco. Ricerca locale, MCP e hook, nessun LLM, un solo binario Go.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Go                                                                                             |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1185**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1011 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Il marketplace di plugin DeepSeek Harness più completo — aggiornato quotidianamente, con fonti provenienti da Internet e revisionato prima della pubblicazione.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1011**   |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

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
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/shengsheng90/DSH-taskboard">shengsheng90/DSH-taskboard</a></b> · ⭐334 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin Taskboard locale nativo per DeepSeek Harness. Progetti supportati da SQLite, assegnazione e revisione da parte degli Agent e Web UI nativa — senza iframe e senza un secondo runtime di chat.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **334**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `task-management` · `taskboard`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/shengsheng90--dsh-taskboard/641e63303f0eed9c.png" width="100%" alt="shengsheng90/DSH-taskboard screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐231 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **231**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐205 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **205**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐186 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **186**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐143 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Include già all'installazione 27 competenze di ingegneria e produttività di mattpocock/skills v1.3.1, senza dover installare manualmente le competenze. Questo plugin è stato creato con 40 miliardi di token e offre un'efficienza di sviluppo 10 volte superiore rispetto alle competenze originali, aiutando anche i principianti a imparare più rapidamente a usare questo kit di competenze. Supporto completo per le issue di GitHub; Markdown è in versione di anteprima; GitLab non è ancora supportato. Grazie per il tuo utilizzo e supporto 💗

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **143**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐124 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness 桌宠插件：元气鲸鱼娘看板娘陪你写代码 🐋 支持 DSH 桌面端 0.2.0-rc.2 与旧版 Web（desktop pet / mascot，local-first）

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **124**    |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐89 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Skill e plugin You.com per ricerca web, estrazione di contenuti, ricerca, finanza e scoperta di integrazioni, che aiutano gli agenti AI a costruire con contesto web aggiornato.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **89**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/JingbiaoMei/Tokdash">JingbiaoMei/Tokdash</a></b> · ⭐85 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Agent Dashboard: Visualization and analytics for Sessions and Quota Usage. Track, analyze, and optimize token usage across providers with heatmaps, cost tracking, token counting and quota resets..

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **85**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent` · `analytics` · `anthropic` · `claude-code` · `claude-code-plugin` · `codex` · `codex-cli` · `dashboard`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jingbiaomei--tokdash/cb7e85100dfe6e93.png" width="100%" alt="JingbiaoMei/Tokdash screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-wsl-workspace-maintainers/dsh-wsl-workspace">dsh-wsl-workspace-maintainers/dsh-wsl-workspace</a></b> · ⭐80 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

WSL workspace support for DeepSeek Harness——无缝的 WSL 工作区使用体验，无需在 WSL 之中再安装一个dsh，安装该插件后在 GUI 里直接添加 WSL 工作区即可。WSL workspace support for DeepSeek Harness — Enjoy a seamless WSL workspace experience without needing to install dsh inside WSL. Once this plugin is installed, you can directly add a WSL workspace right from the GUI.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **80**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-wsl-workspace-maintainers--dsh-wsl-workspace/252926072330fff2.png" width="100%" alt="dsh-wsl-workspace-maintainers/dsh-wsl-workspace screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Agent desktop basato sul nucleo di Deepseek-Harness. Eredita tutte le funzionalità del nucleo e completa le funzioni relative all'IDE.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **72**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

La directory in continua evoluzione dei plugin DeepSeek Harness — aggiornata ogni ora, testata quotidianamente per la compatibilità, con negozio di plugin e scaffolder integrati. Directory attiva dei plugin DSH: aggiornata ogni ora, testata quotidianamente per la compatibilità, con negozio di plugin e scaffolder integrati.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | HTML                                                                                           |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **59**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Recupero del contesto dell'area di lavoro consapevole dell'attività e tracciamento del ciclo di vita per AI coding agent: trova, organizza e monitora continuamente i documenti, il codice e i contenuti multimediali più rilevanti per l'attività corrente. Interamente locale, zero chiamate ai modelli, zero rete. Recupero del contesto dell'area di lavoro consapevole dell'attività e tracciamento del ciclo di vita per AI coding agent. Trova, organizza e monitora il contesto dell'area di lavoro più rilevante per l'attività in corso — localmente, in modo deterministico, con zero chiamate ai modelli e zero rete.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **54**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-plugin-guide">PerryLink/dsh-plugin-guide</a></b> · ⭐50 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Knowledge base sullo sviluppo di plugin DeepSeek Harness (dsh): guida allo sviluppo in 10 capitoli, playbook di rilascio, problemi upstream non risolti verificati sul codice sorgente e dati misurati sull'ecosistema — installabile come bundle DSH.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **50**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `ai-agents` · `checker` · `cli` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/d665a08f58e38532.png" width="100%" alt="PerryLink/dsh-plugin-guide screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/3aee78fb7bcfc697.gif" width="100%" alt="PerryLink/dsh-plugin-guide animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

NekroNXT: sistema di agenti per chat di gruppo multipiattaforma basato su DeepSeek Harness (DSH) | Sistema di agenti per chat di gruppo multipiattaforma basato su DSH

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **35**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **34**     |
| Ultimo push                | 2026-10-13 |
| Prima comparsa nell'elenco | 2026-10-13 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 64</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Una protezione pre-esecuzione per agenti di coding AI.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Un elenco curato dei migliori plugin AI eccezionali per assistenti AI, inclusi…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace / Mercato dei plugin DSH: sfoglia, installa e aggiorna…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、211个世界与上万素材、开局随心定制、世界自行运转、零漂移存档.
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - Paper aggiornati continuamente su grafica, 3DGS e intelligenza spaziale;
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime per plugin destinato a software che si evolve autonomamente — il…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directory curata di plugin per DeepSeek Harness (DSH) — oltre 280 plugin della…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH: shell Git Bash per tutte le modalità agent su Windows.
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh per Android: integra DeepSeek Harness, ambiente di esecuzione Ubuntu…
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion: potenzia dsh-im con i concetti di assistente e casa — mostra…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH 会话导航.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin Web DSH: statistiche giornaliere sull.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin DeepSeek Harness · “Ottimizzazione” con un clic della bozza del prompt…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugin, strumenti, skill e risorse di apprendimento DeepSeek Harness (dsh)…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime di negoziazione commerciale A2A + plugin DeepSeek Harness (dsh).
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vero PowerPoint, non HTML. Dì alla tua IA quali contenuti includere e…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - AI argues. Code settles. The losses stay on the page.
- [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) - Read-time project memory plugin for DeepSeek Harness (dsh).
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - Plugin Web DSH: albero gerarchico del workspace per la barra laterale — i…
- [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) - Plugin DeepSeek Harness: le conversazioni vengono automaticamente condensate in…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [realguan/dsh-dock](https://github.com/realguan/dsh-dock) - 专为 DeepSeek Harness (DSH) 打造的跨平台桌面控制中心：多工作台管理、3,400+ 社区插件市场、会话自愈、凭据与系统诊断.
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Test di compatibilità sempre attivi per i plugin DeepSeek Harness: release…
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - Repair DeepSeek Harness sessions that refuse to load. 修好打不开的 DSH 会话文件.
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - A curated list of plugins, tools, skins, and extensions for DeepSeek Harness…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [jiangnanquan/dsh-ux](https://github.com/jiangnanquan/dsh-ux) - Plugin di potenziamento DSH web UI + shell desktop Electron senza bordi.
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [EdwinZDZ/dsh-api-balance-ring](https://github.com/EdwinZDZ/dsh-api-balance-ring) - Anello del saldo DeepSeek API in tempo reale per il composer di DeepSeek…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray for DeepSeek Harness plugins: declared capabilities vs actual behavior.
- [alone-tree/dsh-skill-mcp-manager](https://github.com/alone-tree/dsh-skill-mcp-manager) - Libreria di capacità (Capability) — gestione visuale one-stop di DSH Skills e…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace con più cartelle: consente all.
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - The bilingual, source-backed registry and installer for the DeepSeek Harness…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: una finestra degli strumenti Git di livello IDE come scheda nativa…
- [mjylfz/dsh-skill-mover](https://github.com/mjylfz/dsh-skill-mover) - 把其他 Agent 的技能一键搬进 DeepSeek Harness：支持 14 个平台 + 共享层识别、同名技能合并、不重复搬运、可回滚.
- [xiaoso456/dsh-workflow-lite](https://github.com/xiaoso456/dsh-workflow-lite) - DeepSeek Harness 的软工作流插件：在画布上设计流程，编译成计划提示词，由模型按计划执行；运行状态由模型自己记，没有执行引擎.
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Osserva chiaramente ogni azione osservabile dell.
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - Il plugin DeepSeek Harness Personalization Settings serve a configurare il…
- [cv-superding/dsh-webin](https://github.com/cv-superding/dsh-webin) - Plugin DSH non ufficiale: controlla web UI AI (DeepSeek/Qwen/...) in un browser…
- [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) - 第三方适配插件：把上游 REA（逆向一切，github.com/morluto/rea）的 MCP 服务注册进 DeepSeek Harness，得到…
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - Raccolta di plugin DSH: autenticazione con password + trust per accesso…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Dai all.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard di verifica senza dipendenze per i plugin DeepSeek Harness (dsh)…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Ecosistema di plugin DeepSeek Harness: 86 plugin open source in una famiglia di…
- [SuCriss/dsh-leekbox](https://github.com/SuCriss/dsh-leekbox) - 韭菜盒子 LeekBox — A股看盘助手 · DeepSeek Harness (DSH) web 插件.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): scheda laterale market-dashboard per il…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode su DeepSeek Harness — plugin DSH che mantiene operativi OpenCode Zen +…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace di plugin di terze parti e gestore del ciclo di vita…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx è una workstation desktop estensibile e incentrata sulle persone…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Un agent di codifica completo per DeepSeek Harness — flussi di lavoro in stile…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [iluluyu/dsh-ui-outline](https://github.com/iluluyu/dsh-ui-outline) - ChatGPT-style right-edge turn navigation plugin for DeepSeek Harness (dsh) web.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite della comunità per l.
- [Wenston-dev/awesome-dsh-plugin](https://github.com/Wenston-dev/awesome-dsh-plugin) - Awesome dsh plugin list — automated DeepSeek Harness plugin directory.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin DeepSeek Harness: trasforma il fallimento del provisioning dell.
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Scadenze a livello di deployment per le chiamate allo strumento dsh che non ne…
- [fshoocn/cordis-port](https://github.com/fshoocn/cordis-port) - Port di Python del pacchetto principale Cordis · runtime modulare / dependency…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Plugin Cordis / DeepSeek Harness — strumenti GitHub API normalizzati per agenti…
- [majiayu000/dsh-desk](https://github.com/majiayu000/dsh-desk) - Distribuzione desktop Tauri installabile per DeepSeek Harness con runtime…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [LittleCar30/dsh-deepseek-web](https://github.com/LittleCar30/dsh-deepseek-web) - Standalone dsh desktop plugin for driving DeepSeek Web through a dedicated real…

</details>

<a id="writing"></a>

## Testi, discussioni e video

Articoli, discussioni e video sulla funzionalità delle mod.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
| Prima comparsa nell'elenco | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
| TypeScript | 296  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 72   | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 45   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 25   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13   | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 6    | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                               |
| Go         | 4    | `mitre/claude-statusline`, `lexfrei/ailine`, `esengine/DeepSeek-Reasonix`                                     |
| PowerShell | 2    | `markallisongit/claude-statusline`, `czcdr/dsh-plugin-rea`                                                    |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1    | `dphmoblie/deepseek-harness-android`                                                                          |
| Lua        | 1    | `crafts69guy/claude-statusline.nvim`                                                                          |
| Swift      | 1    | `peaceinitiativemenhadenoil263/claude-status-bar`                                                             |

<sub>Vengono conteggiate solo le voci che dichiarano una lingua. Le voci di documentazione e discussione sono escluse da questa tabella.</sub>

## Contribuire

Le correzioni sono benvenute e rappresentano il modo più rapido per migliorare questo elenco. Apri una issue o una pull request se una voce è classificata o valutata erroneamente, oppure se un progetto è stato escluso per errore a causa di una collisione di nomi — è proprio in quest'ultima categoria che i filtri automatici hanno più probabilità di sbagliare.

---

<sub>Progetto indipendente della community. Non affiliato a Anthropic, né approvato o revisionato da quest'ultima. Claude Code, Claude e Anthropic sono marchi commerciali di Anthropic. Il comportamento del prodotto può cambiare senza preavviso; verifica qualsiasi informazione essenziale nella documentazione ufficiale. Le risorse restano di proprietà dei rispettivi progetti upstream e vengono riprodotte solo quando una licenza lo consente.</sub>

<sub>Ultimo aggiornamento · 2026-10-13T19:28:29+08:00</sub>
