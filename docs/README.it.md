<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod straordinarie per Claude">
</p>

<h1 align="center">Mod straordinarie per Claude</h1>

<p align="center"><b>L'indice di mod e plugin per Claude Code, valutati in base alle evidenze, e dei comportamenti più profondi che modificano.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-596-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <b>Italiano</b> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indice aggiornato** · Ultima sincronizzazione: `2026-10-12T21:29:43+08:00` (UTC+8)
> · Voci: **596** · Aggiunte nell'ultimo aggiornamento: **0** · Linguaggi di implementazione: **13**

<sub>Ogni voce qui sotto è stata raccolta, filtrata e verificata nuovamente in automatico. Nessuna voce è un'inserzione a pagamento.</sub>

<a id="featured"></a>

## Selezioni del momento

<sub>Una voce per categoria, classificata in base al livello delle prove e alle stelle, con ricalcolo a ogni aggiornamento. È una classifica, non un'approvazione; ogni selezione rimanda alla relativa scheda completa qui sotto. Sono preferiti i progetti che hanno pubblicato uno screenshot o una registrazione, così la fascia rimane visiva.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9482 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2541 · Python · 👁️ observed</sub>
<sub>Trova i token fantasma. Sistemali. Sopravvivi alla compattazione. Evita il deterioramento della qualità del contesto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74398 · TypeScript · 👁️ observed</sub>
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
- [Ufficiali: repository e note di rilascio di Anthropic](#ufficiali-repository-e-note-di-rilascio-di-anthropic) — **16**
- [Mod: realizzate con la funzionalità mod](#mod-realizzate-con-la-funzionalità-mod) — **482**
- [Gli ecosistemi dei plugin DSH e Cordis](#gli-ecosistemi-dei-plugin-dsh-e-cordis) — **86**
- [Testi, discussioni e video](#testi-discussioni-e-video) — **11**
- [Altri progetti](#altri-progetti) — **1**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150341 · TypeScript · ✅ official · 0 天</summary>

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
| Stelle                     | **150341** |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9482 · TypeScript · ✅ official · 2 天</summary>

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
| Stelle                     | **9482**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8253 · Python · ✅ official · 2 天</summary>

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
| Stelle                     | **8253**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242 天</summary>

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
| Stelle                     | **6347**   |
| Ultimo push                | 2026-02-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 2 天</summary>

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
| Stelle                     | **1799**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Mod Claude Code ufficiali di See Stack: HUD della finestra di contesto in tempo reale, pannello di narrazione vocale e strumenti del terminale. Installa tramite: npx seestack

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic`                             |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **0**      |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Aggiunto `$.ui.notify` per le mod: genera una notifica nativa tramite la tua…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Risolto il problema per cui Esc o un.
- [huaweicloud/huaweicloud-devkit](https://github.com/huaweicloud/huaweicloud-devkit) - Official Huawei Cloud plugin for AI agents — skills, MCP tools, safety…

</details>

<a id="mods"></a>

## Mod: realizzate con la funzionalità mod

Ogni voce qui mostra prove dell'uso della funzionalità che Claude Code ha acquisito nella versione 2.1.287: esegue il rendering tramite `ui.render`, gestisce un pannello, una fascia o una scheda, legge `$.ui.selection()`, avvia compagni di squadra con `agent.spawn` oppure dichiara esplicitamente di essere una mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2541 · Python · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Trova i token fantasma. Sistemali. Sopravvivi alla compattazione. Evita il deterioramento della qualità del contesto.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | Python                                                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **2541**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐514 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **514**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐200 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **200**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐152 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stelle                     | **152**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐135 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Claude Code mostra immagini e riproduce video direttamente nel terminale: screenshot, registrazioni Playwright e controllo QA sincronizzato prima/dopo. Ghostty e kitty.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **135**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐108 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Skin per Claude Code: righe degli strumenti con icone, schede per diff, tabelle e grafici Mermaid, una fascia di utilizzo e quindici temi. /skin le sostituisce al volo.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **108**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐81 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **81**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐72 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **72**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐61 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Riepilogo

Skills, agenti, comandi, regole, hook e stili di output esperti per Claude Code — continuità delle sessioni + strumenti CLI moderni per flussi di sviluppo reali

<sub>🔧 Trovato nel codice: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | Shell                                                                               |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **61**     |
| Ultimo push                | 2026-10-07 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Riepilogo

Raccolta di oltre 100 mod utilizzabili con Claude Code.

<sub>🔧 Trovato nel codice: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **50**     |
| Ultimo push                | 2026-10-03 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stelle                     | **46**     |
| Ultimo push                | 2026-10-08 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stelle                     | **28**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **23**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐21 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stelle                     | **21**     |
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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Modifica di codice Claude: anteprima delle immagini incollate e del testo lungo incollato sopra il prompt

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **19**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Usa Codex, GLM e altri agenti di programmazione come subagenti di Claude Code.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **16**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Claude Code mod: Clawd acts out what Claude is doing, above the prompt

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
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6 天</summary>

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
| Stelle                     | **14**     |
| Ultimo push                | 2026-10-05 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

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
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stelle                     | **12**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stelle                     | **7**      |
| Ultimo push                | 2026-10-04 |
| Prima comparsa nell'elenco | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Guarda su youtube.com</a> · la riproduzione si apre sul sito ospitante; GitHub non può incorporarla nella pagina</sub></td>
</tr></table>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 448</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod di Claude e strumenti per crearle: prima una competenza per la creazione…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - L.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Usa Claude Mods per mettere un nuovo tetto a Claude Code: senza modificare il…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quattro mod di Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [HolyGrail/claude-mods](https://github.com/HolyGrail/claude-mods)
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mod di Claude Code di Learning Hacker: rendono il funzionamento dell.
- [kakha13/claude](https://github.com/kakha13/claude) - Mod di Claude Code che correggono e traducono i tuoi prompt prima che Claude li…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mod e skill di Claude Code di Nekyia Labs, creati e utilizzati quotidianamente…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base di conoscenza di Obsidian con fonti citate sui mod di Claude Code: come…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Una cabina di pilotaggio per Claude Code: barre del piano in tempo reale…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Un aspetto da applicazione desktop per la trascrizione del terminale di Claude…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un riquadro laterale per Claude Code: i subagenti eseguiti da una sessione, ciò…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Pannello della barra laterale di Claude Desktop (scheda Code): elenca tutti i…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra di utilizzo sopra la casella di input di Claude Desktop (scheda Code)…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill che insegna agli agenti di Claude Code a creare mod Claude.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Una mod di Claude Code che consente a Claude di eseguire comandi che richiedono…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin e skill Claude della community, installabili da un unico mercato.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mod di Claude (plugin con hook di funzione) per Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galleria di mod di Baselane: mod di Claude Code, verificati e fissati in…
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una coda decisionale CLI/TUI per persone che lavorano con agenti…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod di pannello IDE Claude Code: bacheca degli agenti, albero dei file e…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Disegna diagrammi, formule LaTeX e immagini dei risultati degli strumenti…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod di Claude Code che visualizza le differenze di Edit e Write in due colonne…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, visualizzato nella casella del prompt di Claude Code mentre digiti.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mod di Claude Code di Ray Amjad: riquadri, bande, protezioni del prompt…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mod di Claude Code: pannello dei consumi usage-hud di 像素螃蟹 + link HTML…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Scheda di stato flottante per Claude Code — modello, contesto, limiti di…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mod per Claude Code: plugin con hook di funzione che aggiungono riquadri live e…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mod di Claude Code: screen-guard nasconde nomi e segreti mentre condividi lo…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Estensioni di Claude Code. Sblocca tutta la potenza di Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) di Claude Code che aggiunge un pannello laterale con schede…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Pannelli, protezioni e mod per migliorare l&#x27;esperienza d&#x27;uso di Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Due mod di Claude Code sopra la casella del prompt: indicatore della finestra…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Fai durare più a lungo il piano Claude Pro: mod di Claude Code per un HUD dei…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Legge i file markdown a cui Claude Code dà un nome, visualizzati accanto alla…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod di Claude Code: miniature delle immagini incollate sopra il prompt, in…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mod di Claude Code: menu Strumenti Claude, modalità Zen, temi del terminale…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collaboratore vocale per Claude Code. Parla delle tue idee con un lupo 3D…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mod di Claude Code: barra del contesto, pannello degli agenti, sfocatura PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mod di Claude Code: typing-speed, un tachimetro della velocità di digitazione…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuochi d.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Un test di digitazione per passare il tempo mentre Claude lavora.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mod per Claude Code: pannelli, comandi e hook realizzati con il plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Scopri mod, plugin ed estensioni di Claude Code con demo animate, elenchi per…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod di Claude Code: diagrammi Mermaid disegnati direttamente nella trascrizione.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mod e skin per Claude Code: una barra di avanzamento live per le attività di…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Piccoli mod di Claude Code (plugin con hook di funzione): session-switcher e…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - Scopri quanto costa il tuo prossimo messaggio di Claude Code: una banda live…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Sei modifiche di Claude Code: limiti del piano e contesto sopra il prompt…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mod di Claude Code: mod-scout (trova i mod che useresti di più), usage-meter…
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Due mod di Claude Code per eseguire molte sessioni contemporaneamente: una…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: scopri, esamina, attiva/disattiva e aggiorna i mod di Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - I migliori mod di Claude Code: selezionati, convalidati, fissati in alto.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code: routing automatico del modello Claude.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Riduce gli enormi output degli strumenti prima che riempiano il contesto di…
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
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mod Claude Code on demand — una skill che legge la tua conversazione e…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Due mod di Claude Code: cache-keeper e ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Un plugin per Claude Code estremamente caratterizzato, progettato da un…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mod di Claude Code che mantengono onesto un agente — hook di funzione che…
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - I mod di Claude Code che uso.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Dashboard notch di macOS per Claude Code: limiti di utilizzo, sessioni aperte…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude sta cucinando. Chatta con la tua squadra.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della cache dei prompt, prossimi passi, pulsanti…
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Costi, token e limiti del piano dei tuoi agenti di programmazione.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Una mod di Claude Code che mostra i limiti di utilizzo e la spesa nella fascia…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Le mod di Claude Code di Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mod di Claude Code: barre di avanzamento per i piani, un registro di ciò che…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Scopri cosa esegue Claude Code in background: sottoagenti, processi Codex…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mod di Claude Code di MacLeod Labs: streams districa il lavoro intercalato di…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Note sul campo del primo giorno sulle mod di Claude Code su Windows: una barra…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: un debugger per le chiamate agli strumenti di Claude Code.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Mod di Claude Code: stato live della pull request GitHub.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Piccole schede che si posizionano sotto il prompt di Claude Code o agganciate…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod di Claude Code: misuratori live di costo, contesto e quota del piano sopra…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Una modifica al codice di Claude che trattiene il fan-out dei subagenti, i…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills per Claude in cinque pacchetti.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 Stiamo creando del TECHNO, tesoro 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod di Claude Code: un SDLC AI-native.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod per Claude Code che attiva o disattiva le tue competenze, i tuoi agenti…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugin di Claude Code (mod): passa da un account Claude all.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod di Claude Code testate e installabili con un solo comando: protezioni per…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mod per Claude Code: plugin basati sui function hook.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un insieme di mod per claude code realizzate da me.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modifiche al codice di Claude. touch-map: mostra quali file Claude ha elencato…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Impara una lingua straniera mentre lavori con Claude Code.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Tell Claude what you want. Get it back built, tested, reviewed by another AI…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Si occupa di una lunga sessione di Claude Code al posto tuo: osserva il…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - A Claude Code mod that keeps your prompt cache warm while you.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra laterale in tempo reale per costi, token e utilizzo del contesto di…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Obiettivo, attività e agenti sopra il prompt di Claude Code — configurazione…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mod di Claude Code per veri ingegneri.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Riepilogo della sessione terminale di Claude Code, nella scheda Code dell.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Raccolta di mod di Claude Code di jack.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Una mod di Claude Code: un riquadro con l.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Un mod di Claude Code: cattura i Modsters in pixel art in un gioco inattivo…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Vedi quali file ogni agente di Claude Code ha nel proprio contesto, e quanto di…
- [deejay-hub/sf-headless-band](https://github.com/deejay-hub/sf-headless-band) - Una mod per Claude Code per Salesforce che mostra quali Orgs sono connesse.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Trasforma ogni sessione di Claude Code in una piccola avventura: musica…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Piccole mod di Claude Code per il terminale e l.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI che aggiunge parole spagnole nelle risposte dell.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - I tuoi eventi Alarum sopra il prompt di Claude Code: cosa è appena arrivato e…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Il backlog di Floatee sopra il prompt di Claude Code: esegui, guida e spunta le…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Una mod per Claude Code per catturare i pensieri durante il lavoro…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra laterale in stile Evangelion per Claude Code: contesto, quota, attività…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Una mod di Claude Code che lo rielabora come The Machine di Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Mod di Claude Code: una squadra in pixel art suggerisce il modello giusto…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod Claude Code per flussi di lavoro DAG obbligatori e verificati…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Una mod di Claude Code: un riquadro per ogni subagente, i file che modifica e…
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Mod per Claude Code (mod CC tint): colora ogni finestra in base al suo…
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - Vari mod che ho creato per claude e che trovo utili.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod di Claude Code: stato della sessione, avanzamento live di Spec Kit e…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La finestra di contesto come un.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD delle attività in tempo reale per Claude Code Desktop: una fascia sopra…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) di Claude Code che fa apparire l.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Non lasciare che la tua attenzione divaghi mentre aspetti la risposta di Claude…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Quattordici mod di Claude Code in un unico plugin, ciascuno attivabile…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Un plugin gratuito e open source per Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Mod di Claude Code selezionati, demo dei creatori originali, repository…
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Mod per Claude Code per sessioni lunghe: sitrep riassume l.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Mod Claude Code: selezionati, testati e ciascuno distribuito con il prompt che…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mod di Claude Code: passaggio automatico e barra di avanzamento.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Competenze di Claude Code: verificatore dei fatti per la documentazione…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod di Claude Code che riscrive i prompt approssimativi rendendoli chiari prima…
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Una mod di Claude Code che mantiene un casebook aggiornato delle prove fornite…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - I mod Claude Code di Pedro La Rosa, in un unico marketplace di plugin.
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Mod Claude Code: i tuoi limiti di utilizzo di 5 ore e 7 giorni come barre…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin buddy di Claude Code: un compagno ASCII sopra il prompt che ricorda le…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin di Claude Code per la visibilità degli strumenti per agente — nasconde e…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Visualizza la matematica LaTeX in modalità display nel terminale di Claude…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: un mod fan non ufficiale di Avengers per Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: una mod di Claude Code che legge ad alta voce, su richiesta, le…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Sculaccia Claude quando combina guai — una mod antistress per Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod di Claude Code: piccoli plugin per riquadri in tempo reale, instradamento…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin di Claude Code: monitoraggio dell.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Un mod di Claude Code che affida le piccole decisioni a un modello decisionale…
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Individua la deriva del ragionamento della tua sessione di Claude Code, proprio…
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [agukov-dev/token-meter](https://github.com/agukov-dev/token-meter) - Claude Code mod: rate limits, context and spend under the prompt.
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Marketplace di mod per Claude Code: agent-board, auto-model, session-collab +…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Mod per Claude Code: barre di avanzamento dell.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Mod di Claude Code: schede delle statistiche della sessione sopra il prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gatto braille animato sopra il prompt di Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod di Claude Code: indirizza il lavoro economico a GLM/Kimi tramite un Claude…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gatto pixel sopra il prompt di Claude Code che esegue una chiamata di test a…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Una mod di Claude Code che sceglie il momento giusto per compattare e mantenere…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modifiche di Claude Code per Claude: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mod generiche per Claude Code: bande, pannelli, notifiche e hook.
- [arifamir/nukey](https://github.com/arifamir/nukey) - Nukey il microonde: marketplace di mod e plugin per Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - I tuoi limiti di utilizzo di Claude come scheda animata della salute di un…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mod di Claude Code per il team S2 (il marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Brevi allenamenti mentre Claude lavora: un obiettivo giornaliero, serie, badge…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un pannello di utilizzo per Claude Code: spesa per modello.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Mod di Claude Code che mostra il conto alla rovescia della cache del prompt nel…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing per Claude Code: Apple Music e Spotify sopra il prompt, con…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod per Claude Code: orologio della cache, Blast Radius, suggerimenti, lista di…
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mod per Claude Code: Clean View nasconde le chiamate agli strumenti e mostra il…
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - Una mod di Claude Code: il registro del lavoro orchestrato, con esecuzioni…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mod di Claude Code: Suggestion Spotlight mostra a cosa si riferisce il prossimo…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un gufo per il tuo Claude Code.
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Mod di Claude Code creati da me (pannelli, comandi e hook).
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Il motore Doom originale con Freedoom, giocabile dentro Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Small, readable Claude Code mods from the CorporateChittyChat channel.
- [colorfield/claude-ci-watch](https://github.com/colorfield/claude-ci-watch) - Claude Code mod: Pane and status line for the current branch.
- [colorfield/claude-lagoon-watch](https://github.com/colorfield/claude-lagoon-watch) - Claude Code mod: Pane with the Lagoon project.
- [colorfield/claude-port-guard](https://github.com/colorfield/claude-port-guard) - Claude Code mod: Stops Claude from killing, or running E2E tests against…
- [colorfield/claude-session-line](https://github.com/colorfield/claude-session-line) - Claude Code mod: Status line with context fill, model, effort, git branch or…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Esamina ogni file modificato da Claude, come una pull request, senza lasciare…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Keep Claude Code on a plan: stages, approval gates and a file budget enforced…
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Mod per Claude Code: una banda sopra il prompt con il conto alla rovescia della…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - My personal Claude Code mods, customised for my own setup.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Mod di Claude Code dedicati al team d3nim.
- [dankelleher/claude-mod-pin-message](https://github.com/dankelleher/claude-mod-pin-message) - Mod di Claude Code: fissa una risposta sopra il prompt, comprimibile in un…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Undici mod di Claude Code (plugin con function hook) per un flusso di lavoro…
- [davidcoulson/session-crew](https://github.com/davidcoulson/session-crew) - Una mod di Claude Code che mostra le sessioni secondarie avviate da una…
- [daviddecorso/claude-mods](https://github.com/daviddecorso/claude-mods)
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Claude Code mods: an OpenSpec and sub agent board, hand over before compacting…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi che vive dentro Claude Code: si schiude, mangia il codice scritto…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Segnalibri e marcatori in stile vim nelle conversazioni del terminale di Claude…
- [DerpcatMusic/claude-context-controls](https://github.com/DerpcatMusic/claude-context-controls) - Claude Code mod: nested context / 5h / weekly rings, compaction threshold and…
- [devsomelife/somelife-claude-mods](https://github.com/devsomelife/somelife-claude-mods)
- [dgsantana/claude-mods](https://github.com/dgsantana/claude-mods) - Mod per Claude Code: omp-port.
- [dhiroo-jpg/claude-mods](https://github.com/dhiroo-jpg/claude-mods) - クロードの使用量をチャット画面に表示.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Un mod di Claude Code: una banda sopra il prompt con le novità di Claude e le…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Una mod per Claude Code: una bacheca delle tue altre sessioni sopra il prompt…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod di Claude Code: dopo che un guard blocca una chiamata a uno strumento…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod di Claude Code: lavori in background in un.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod di Claude Code: un.
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod di Claude Code: spiega i blocchi della sandbox e trasforma i blocchi…
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - A live wave board of your session.
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Istruzioni, competenze, estensioni di Pi e mod di Claude Code per Pi, Codex e…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mod di Claude Code (plugin con hook sulle funzioni): session-meter e altro.
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi — a Claude Code mod: a mascot that reads the room above the prompt, with…
- [g761007/hudcade](https://github.com/g761007/hudcade) - Un HUD in pixel art per Claude Code: contesto, costi, cache, agenti e limiti di…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Sette mod di Claude Code: savvy-progress, skins, filetree, cache-tax…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - A Claude Code mod for the desktop app: click a file reference in a reply and it…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Mod utili per claude code.
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Marketplace privato di mod di Claude Code.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Mod in lingua tedesca per Claude Code: indicazioni su contesto/cache, punti…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Mod di Claude Code di Hector Bailey (marketplace di plugin: hectorbailey).
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Mod di Claude Code: tre passaggi successivi dopo ogni risposta, in qualsiasi…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod di Claude Code: quanto tempo ha richiesto ogni risposta, quanto ha pensato…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude mods marketplace.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Un cockpit sopra il prompt di Claude Code. L.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Redazione reversibile per Claude Code: i valori privati vengono sostituiti con…
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Barra di stato di Claude.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Piccoli mod di Claude Code: indicatori di utilizzo del contesto e del piano, un…
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Mod di Claude Code: barra del contesto e HUD del cyberdeck.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Legge automaticamente i tuoi disegni tecnici, quindi crea il modello in…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Un luogo dove raccogliere le mie mod di claude.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Pannello laterale dell.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Elenco laterale dei file: quali file sono stati creati, modificati o eliminati…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Mao Mao in stile 8-bit (coniglio nano olandese bianco e nero) corre e salta…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Pannello laterale «Le mie domande»: ogni frase digitata dal proprietario in…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Cronologia laterale: dove è stato impiegato il tempo di questo turno.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Scambio di token nella barra laterale: quanti token la conversazione principale…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Il sincero sacchetto di fagioli di claude code: al termine di ogni turno…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Checklist del piano con verifica delle evidenze per Claude Code: i piani…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Localizzazione in cinese semplificato di Claude Code CLI (versione autogestita)…
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Guida non ufficiale della community ai mod di Claude Code (hook delle funzioni)…
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - Due mod di Claude Code: passaggi di consegne tra sessioni con risposte e…
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph Ayoub.
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive in una fascia sopra il prompt di Claude Code: mette in scena la…
- [kartollikaa/claude-android-emulator](https://github.com/kartollikaa/claude-android-emulator) - Claude Code mod: Android emulator and device screens inside Claude Code.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod di Claude per leggere e unire le conversazioni tra le tue sessioni di…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mod di Claude Code. PixBar: una creatura pixelata sopra il tuo prompt che si…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod per Claude Code: ogni sessione di Claude Code in un.
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - Alcune prove di concetto per claude-code-mods.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Mod di Claude Code, pubblicate come marketplace.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: un grafo in tempo reale di ciò che sa Claude Code.
- [l4ckofsleep/ccdetails](https://github.com/l4ckofsleep/ccdetails) - Claude Code mod: context fill, prompt-cache hit %, rate limits and cost above…
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Ten Claude Code mods: an animated pixel pet, Code Wrapped, lo-fi beats, plus a…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Mod di Claude Code di Sanmu — un marketplace di plugin.
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Una guida ai mod di Claude Code curata dalla community: casi d.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Una mod di Claude Code che mostra cosa sta facendo Claude nel sottotitolo della…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, un compagno pixel non ufficiale creato dai fan, che vive sopra il prompt…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - Quanto è pieno il contesto di Claude, quando la sua cache si raffredda e quanto…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Un soffice gatto nero sopra il tuo prompt di Claude Code.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod di Claude Code: rispondi a Claude punto per punto, direttamente sul testo.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Piccoli mod per Claude Code: runner-avatar, un piccolo avatar che corre sopra…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - Piccoli mod di Claude Code dal canale MateAI.
- [matrac/burnline](https://github.com/matrac/burnline) - Claude Code mod: usage limits and task progress in one status line.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod di Claude Code: un pannello live di ciò a cui mira, di ciò che presume…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod di Claude Code: riquadro /sessions per sfogliare ed eliminare le sessioni…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Pannello laterale per Claude Code: file scritti da Claude, terminali…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Mod di Claude Code: proietta quanto resterà dei tuoi limiti settimanali e di 5…
- [Miriam2040/nugget](https://github.com/Miriam2040/nugget) - Select any part of Claude.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un discreto riquadro laterale per Claude Code: cosa sta facendo questa…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Un.
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Mantieni il codice conforme alle specifiche: una mod per Claude Code e…
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - Plugin di Claude Code per sessioni e memoria: un mod del pannello Memory e una…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod di Claude Code che riattiva gli strumenti todo per i modelli che li…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod di Claude Code che attende una pausa sicura, poi trasferisce la sessione o…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod di Claude Code: una riga per ogni attività sopra il prompt con l.
- [mwmrs/claude-mods](https://github.com/mwmrs/claude-mods)
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Gioca a Connect Four contro un.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Modifica al codice di Claude: quando un altro agente di programmazione esegue…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Mod di Claude Code: mantiene leggere le sessioni — riga sull.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Modifica al codice di Claude per repository condivisi da diversi agenti IA…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code mod: one button per delegate-skills implementer.
- [ngxuanbminh/pr-watch](https://github.com/ngxuanbminh/pr-watch) - Claude Code mod: watch the GitHub PRs of the repo you.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Riattiva i monitoraggi lunghi di Monitor di Claude Code quando scadono, senza…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barriera di sicurezza per SQL in Claude Code: chiede conferma prima che…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Una modifica per Claude Code, Windows e CJK prima di tutto: anteprime di…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - I migliori mod di Claude Code, ordinati in base a ciò che fanno per te.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Due mod Claude per Claude Code: garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Timestamp per Claude Code: l.
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Tracciamento delle modifiche per Claude Code: vedi esattamente cosa ha…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Mod per Claude Code: plugin di hook funzionali che funzionano in qualsiasi…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Vari mod e skill per la mia configurazione Claude Desktop.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Mod di Claude Code: tiene traccia del modello, dei token, degli strumenti e del…
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Mod di Claude Code: ogni subagente appare come una piccola persona stilizzata…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mod per Claude Code: safety-guard blocca i comandi distruttivi e l.
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Un granchio Claude animato in pixel art per Claude Code: mette in scena ciò che…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Mod di Claude Code, pubblicati come un unico marketplace di plugin.
- [ReDev1L/leanctx-colored](https://github.com/ReDev1L/leanctx-colored) - Claude Code mod: colored lean-ctx output.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code: flessioni da fare mentre Claude lavora. Nessun token.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 mod di Claude Code in coreano: registro delle supposizioni, linguaggio…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - solo un elenco delle mod che sto usando.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Tre mod prive di dipendenze per Claude Code: una statusline reattiva, un…
- [Ron-Nefyodov/security-poc-mod](https://github.com/Ron-Nefyodov/security-poc-mod) - Mod per Claude Code solo per POC, destinata a dimostrazioni locali di sicurezza…
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - An open-source marketplace for Claude Code mods, with repository skills for…
- [RuahTechSolutions/code-buddy](https://github.com/RuahTechSolutions/code-buddy) - Mod per Claude Code: protezione dello staging, raggio d.
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - I miei mod per Claude Code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod di Claude Code: trasforma il piano approvato in modalità piano in una…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una selezione curata di mod di Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modalità senza costi: gli agenti ausiliari funzionano su Haiku e i file e i log…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una colonna sonora lofi che segue la sessione: calma, concentrazione, flusso…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Impara mentre Claude programma: dopo un turno che ha modificato il codice…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una registrazione di ogni modifica effettuata da Claude: riproduci ogni…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Mod di Claude Code: token-bar, la tua finestra di contesto e i limiti di…
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in the conversation…
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Centro di controllo per Claude Code: flotta di subagenti in tempo reale…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Le mod di Claude Code di Showrin per una produttività quotidiana maggiore.
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Claude Code mods personali.
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messaggi di commit con un clic per Claude Code con una Malenia in pixel-art che…
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - Raccolta di mod di Claude Code creati direttamente (marketplace di plugin).
- [sunwu51/english-assistant](https://github.com/sunwu51/english-assistant) - Plugin Claude Code Mods per la traduzione contestuale cinese-inglese, la…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Repository locale di mod per Claude Code.
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Mod di Claude Code: mostra il tuo file Cursor / VS Code e la selezione sopra il…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod di Claude Code che mostra l.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod di Claude Code che mostra la sessione corrente in un pannello: ogni…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace di plugin Claude Code di mod: plugin function-hooks che…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Mod di Claude Code di Toptaab.
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Mod piccoli, divertenti e utili per Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod di Claude Code: fascia di avanzamento animata e riepilogo del completamento…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tre piccoli mod di Claude Code: scopri quando i tuoi sottoagenti termineranno…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Fai a Claude una domanda laterale in un riquadro accanto al tuo lavoro.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code plugin: prompt-cache countdown, cache hit rate, context weather and…
- [wablevaibhav/claude-mods](https://github.com/wablevaibhav/claude-mods)
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Le mie mod di Claude Code.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Un mod di Claude Code: un evidenziatore per le risposte, un pannello laterale…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter) - Questa mod per Claude Code mostra una scheda sopra il prompt.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — when context outgrows its shell, shed it into the folder and keep going.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod per Claude Code: segreti oscurati, cose da fare, verifiche e CI, diario…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Claude Code: i tuoi limiti di utilizzo Claude Pro/Max con una…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod per Claude Code. agent-crew: osserva i tuoi subagenti al lavoro come un…
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - Mod del pannello laterale del terminale per Claude Code — tracciamento degli…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Una bacheca delle attività live per Claude Code: pianifica prima di costruire…
- [yuu1111/claude-agents-skills](https://github.com/yuu1111/claude-agents-skills) - Claude Code mod that loads Agent Skills from the shared .agents/skills…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una raccolta curata delle migliori risorse per il più straordinario degli…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin Claude Code che mostra cosa sta succedendo: utilizzo del contesto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Elegante statusline altamente personalizzabile per Claude Code CLI, con…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Tutte le parti del prompt di sistema di Claude Code, 27 descrizioni degli…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Oltre 45 consigli per ottenere il massimo da Claude Code, dalle basi agli…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — genera caroselli Xiaohongshu e coppie di…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Esamina il diff del tuo agente di coding in un pannello del terminale e invia…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin completo della barra di stato per Claude Code con utilizzo del contesto…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crea mod per Claude Code: intercetta qualsiasi richiesta, modifica qualsiasi…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Una dashboard completa della statusline per Claude Code — informazioni sulla…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: monitora l.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Una statusline estetica per Claude Code di awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills e mod pubblici per Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mod, subagent, hook, comandi slash e guide per Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legali e gratuiti + agenti di coding — aggiornati automaticamente e…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Calcolatore dei costi rapido e senza dipendenze e statusline personalizzabile…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Risultati in diretta, calendari e classifiche di calcio per la competizione…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill che trasforma il tuo agente di coding in un esperto di firmware per…
- [Tripstack-Corp/spyc](https://github.com/Tripstack-Corp/spyc) - A Rust TUI file commander where the AI agent in the side pane can query the…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Orari delle preghiere, data Hijri, adhkar, ayah quotidiana, digiuno sunnah…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configurazione personale di Claude Code versionata all.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — plugin DeepSeek Harness per argomenti di ricerca…
- [chrisnguyen1211/pillrdotlol](https://github.com/chrisnguyen1211/pillrdotlol) - Every coding agent and every API key, in one pill at the edge of your Mac.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Raccolta di plugin per Claude Code, pi e DeepSeek Harness: HUD della barra di…
- [luucas42/agent-flow](https://github.com/luucas42/agent-flow) - A live workflow panel for Claude Code: the main model, the advisor and every…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Riga di stato leggera per Claude Code — un unico script Bash di circa 170…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin di Claude Code che uso ogni giorno: skill e mod, ripuliti per funzionare…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analyze Claude Code token usage and costs from local conversation logs and…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mod non ufficiali per la scheda Code di Claude Desktop — usage-pet: una banda…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Bridge DSH &lt;-&gt; Feishu (Lark), sviluppato internamente (non è un fork): scheda…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace per plugin e skill di Claude Code per facilitare la creazione di…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Governance dei token per Claude Code: il modello principale dirige…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visualizzatore a pannelli divisi per Claude Code in Windows Terminal e tmux: la…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository per mod Awesome Media di Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Riduci la spesa di Claude Code e dei token Codex: indirizza ricerche e test…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Riga di stato configurabile di Claude Code per Linux, WSL, Windows e macOS, con…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Visualizza la statusline di Claude Code con limiti di frequenza, directory…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Una riga di stato e una riga dei token per Claude Code: contesto, utilizzo su 5…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - la barra di stato amichevole e personalizzabile per Claude Code — barre…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Team di agenti nativi. Sotto controllo.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Componenti aggiuntivi per Claude Code: monitor del punto colorato dello stato…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Fabbriche software definibili per Claude Code su herdr: grafi di stazioni…
- [0xSerachu/claude-shortcuts](https://github.com/0xSerachu/claude-shortcuts) - Explore and quiz yourself on all Claude Code shortcuts with categorized…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Riga di stato dell.
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows PowerShell status line for Claude Code: 5-hour and weekly limits with…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Barra di stato di Claude Code in Lua, con un playground Neovim in tempo reale.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Riga di stato di Claude Code di livello professionale: durata della sessione…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Riga di stato di Claude Code consapevole dell.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Status line per Claude Code in spagnolo: attività, skill, contesto con…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Status line colorata di Claude Code: limiti del piano, contesto, costi e token.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Status line di Claude Code per Windows: totali dei token, costo a tariffa API e…
- [gvart/claude-config](https://github.com/gvart/claude-config) - My Claude Code setup: agent-monitor mod, skills, agents and a one-command…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Barra di stato a riga singola per Claude Code: modello, git, contesto, token…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Anteprima immagini dentro Claude Code: passa il mouse su un chip sotto una…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Configurazione personale di Claude Code: autorizzazioni, statusline, server MCP.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Riga di stato di Claude Code con righe del pannello degli agenti.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincronizza le attività di Claude con Fizzy.do per una visibilità del team in…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: configurazione portatile di Claude Code — regole globali…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Visualizza una barra di stato dettagliata e codificata a colori per Claude…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Monitora lo stato di Claude Code con una dashboard compatta che mostra…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Barra di stato su due righe per un agente di coding da terminale: directory…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook della status line di Claude Code — monitora l.
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, il compagno in pixel art di Claude Code, e atelier, il guardrail per lo…
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Marketplace Claude Code de MSF Supply : mods sélectionnés et figés par commit.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Installer dell.
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Rich multi-line status line for Claude Code — live usage limits (5h + weekly)…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness di Claude Code di Nacho (regole, bacheca, mod).
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Statusline multilinea di Claude Code: barra del contesto, branch git, barre…
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - Plugin e mod di OrihuelaConde per Claude Code.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — statusline di Claude Code per macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitora lo stato di Claude Code dalla barra dei menu di macOS, con indicatori…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skill e mod per Claude Code e Cowork — project-tracker, reference-doc e altro…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Riga di stato di Claude Code per Windows (PowerShell): barre di utilizzo, conti…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skill, mod, hook e una riga di stato per Claude Code, più un motore di…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Una barra di stato su due righe per Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Statusline personalizzata di Claude Code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Harness iniziale per Claude Code: hook, statusline, modelli locali…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configurazione portatile di Claude Code (riga di stato + installatore).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Una piccola dashboard per Claude Code: percentuale di contesto, conto alla…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Barra di stato del terminale personalizzata per Claude Code: modello…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Monitora l.
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Raccolta di mod per Claude Code.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Barra di stato di Claude Code: l.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Skill di Claude Code (VS Code, Windows): anteprime delle immagini e pulsanti di…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Sincronizzazione della configurazione a livello utente di Claude Code su più…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Una statusline di Claude Code con barre di avanzamento sfumate, impegno della…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Una riga di stato di Claude Code: cartella, ramo git, modello, utilizzo della…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Rilevatore del deterioramento del contesto 2026 - Monitor proattivo della…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagent e statusline di Claude Code: raccolte e strumenti open-source…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline di Claude Code che mostra l.
- [previsioncystolith584/ai-video-downloader](https://github.com/previsioncystolith584/ai-video-downloader) - Download videos from major platforms and automatically add translated…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - Una status line basata su Deno per Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mod per Claude Code: riquadri, bande e compagni basati su hook di funzione.
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Pacchetto UI in stile Claude Code per l.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passa le attività tra le tue sessioni di Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Questo è un server MCP per controllare MODS, lo strumento modulare…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill di Codex e Claude Code per tradurre mod di CK3 con un LLM locale.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mod open source e altre estensioni per Claude Code.
- [alan-oliv/team8](https://github.com/alan-oliv/team8) - A live browser console for Claude Code agent teams — every teammate.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Riga di stato di Claude Code: estetica CCometixLine + funzionalità HUD di Claude.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: trova ciò che chiedi ripetutamente a Claude Code e trasformalo in un…

</details>

<a id="dsh-cordis"></a>

## Gli ecosistemi dei plugin DSH e Cordis

DeepSeek Harness e Cordis arrivano allo stesso risultato da una direzione diversa: per loro il plugin è il meccanismo delle mod, quindi un plugin lì equivale a una mod qui.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74398 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **74398**  |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐134601 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **134601** |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100691 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **100691** |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82387 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **82387**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **35769**  |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25517 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Distilly — Distilla il modo in cui pensano in Skills riutilizzabili per qualsiasi Agent o Bot. In precedenza Colleague Skill（原同事 Skill）.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **25517**  |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8659 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Ecosistema di aggregazione dei plugin Web di DeepSeek Harness (DSH) · Tutto è un plugin, distribuito tramite il Laboratorio creativo｜｜Ecosistema di aggregazione dei plugin Web di DeepSeek Harness (DSH) · Tutto è un plugin, distribuito tramite il Laboratorio creativo

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8659**   |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4385 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **4385**   |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3060 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Versione desktop Tauri di DeepSeek Harness | Installer di soli 8mb, configurazione dell'ambiente zero, plugin preimpostati, Windows / macOS / Linux.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3060**   |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1601 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Una protezione pre-esecuzione per gli agenti di coding AI. Blocca i comandi distruttivi di Git e del file system, oltre ai tentativi comuni di accedere a file sensibili, prima dell'esecuzione di una chiamata allo strumento. Supporta Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode e Pi.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1601**   |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/GanyuanRan/Aegis">GanyuanRan/Aegis</a></b> · ⭐1343 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Make AI coding agents architecture-aware: baseline-first, evidence-verified, drift-checked, and safe across long tasks.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1343**   |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `agent-skills` · `ai-agents` · `ai-coding` · `architecture-driven-development` · `awsome-coding-plugin` · `baseline-first` · `claude-code` · `codex`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ganyuanran--aegis/4581f8f71af5092d.png" width="100%" alt="GanyuanRan/Aegis screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1179 · Go · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **1179**   |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐552 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **552**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/text2future/flowix">text2future/flowix</a></b> · ⭐459 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **459**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `agent-memory` · `claude-code` · `codex-cli` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `hermes-agent`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/9fc65a8848fe78ee.png" width="100%" alt="text2future/flowix screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/ea3f84c8693d4236.gif" width="100%" alt="text2future/flowix animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐374 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Provider gratuito di ricerca web per DeepSeek Harness - backend DuckDuckGo, non è necessaria alcuna chiave API.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **374**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Your Intelligence, Orchestrated. Every builder. Every team. Every agent. For Everyone.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Go                                                                                             |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **351**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐230 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin per DeepSeek Harness per cambiare skin / sfondo / pacchetto di temi (dsh-plugin) — 8 temi Mirage, colore d'accento per utente, sfondi 2.0, importazione, esportazione e link di condivisione dei pacchetti di temi, preferiti e casuale, realizzato interamente con un sistema di token nativo.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **230**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin nativo di DeepSeek Harness (DSH) che integra TypeSafe Jev o un'API Decision come luna come livello decisionale System One per la selezione, la supervisione, le correzioni e le approvazioni degli agenti.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **204**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐181 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin di backup e ripristino per DeepSeek Harness (DSH) — esporta, importa, migra e sincronizza la configurazione completa di DSH, i plugin, i server MCP, le skill e il workspace. Migrazione con un clic verso un'altra macchina.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **181**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐180 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Evidenze di runtime che aiutano gli agenti a tracciare, profilare e ridurre i colli di bottiglia nel codice applicativo e nativo, nei kernel GPU e negli stack di inferenza.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **180**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin di DeepSeek Harness per la migrazione tra sessioni con preset diversi e anteprima. I passaggi con schema fisso preservano lo stato, l'intento del modello sorgente e le immagini irrisolte; la sessione originale rimane intatta.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **165**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐142 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **142**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Include già 27 skill di progettazione e produttività di mattpocock/skills v1.3.1, senza bisogno di installarle manualmente. Creato con 40 miliardi di token, questo plugin offre una produttività di sviluppo 10 volte superiore alle skill originali e aiuta anche i principianti a iniziare più rapidamente con questo set di skill. Supporto completo per le issue di GitHub; Markdown è in versione di anteprima; GitLab non è ancora supportato. Grazie per l'uso e il supporto 💗

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **137**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐121 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin per animaletto da scrivania di DeepSeek Harness: una balenottera energica come mascotte che ti accompagna nella scrittura del codice 🐋 Supporta DSH desktop 0.2.0-rc.2 e il vecchio Web (animaletto da scrivania / mascotte, local-first).

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **121**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Aik358/dsh-auto-memory">Aik358/dsh-auto-memory</a></b> · ⭐111 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Proactive associative memory for DSH: system-prompt recall before the model speaks, three-layer auto-consolidation, skill crystallization, and Astra-style context management - handoff ledgers, PLAN whiteboard, water-level sensing. Local-first, model-agnostic, zero deps. 主动联想记忆+Astra 式上下文管理：自动唤回/自动沉淀/技能固化/交接账本与白板跨窗口续命/水位感知。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **111**    |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `context` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `memory` · `npm` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/ba11cddac1ec16d1.png" width="100%" alt="Aik358/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/a44325f737275ef4.gif" width="100%" alt="Aik358/dsh-auto-memory animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **69**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/leantoken">morluto/leantoken</a></b> · ⭐64 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Code intelligence for agents: find the code that matters and keep your context window and tokens lean.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Rust                                                                                           |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **64**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `ai-coding` · `code-intelligence` · `code-navigation` · `code-retrieval` · `code-search` · `codebase-indexing` · `coding-agents` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--leantoken/38b3e8f4a7b20aea.jpg" width="100%" alt="morluto/leantoken screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cloader/dsh-taskboard">cloader/dsh-taskboard</a></b> · ⭐59 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

deepseekharness 任务看板插件

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **59**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `kanban` · `task-board`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cloader--dsh-taskboard/cfd9efd4514a0b8f.png" width="100%" alt="cloader/dsh-taskboard screenshot"></td>
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
| Ultimo push                | 2026-10-12 |
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
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

NekroNXT: sistema di agenti per chat di gruppo multipiattaforma basato su DeepSeek Harness (DSH)｜Un sistema di agenti per chat di gruppo multipiattaforma basato su DSH

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
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-10 |

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

Plugin DeepSeek Harness: abbina automaticamente la finestra di contesto del modello con un clic, mostra l'origine della capacità, supporta la configurazione in blocco tramite selezione, la gestione delle finestre esistenti e la modifica manuale.

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
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Navigazione delle sessioni DSH

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **23**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-toolbox-ui">Imzl-zl/dsh-toolbox-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Pannello Toolbox per DeepSeek Harness Web: gestore di MCP (strumenti e JSON Schema, marketplace, importazione, copia dell'area di lavoro) e gestore delle skills (ambiti e shadowing, attivazione/disattivazione, invocazione automatica del modello, marketplace skillhub.cn).

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **20**     |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent-skills` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp` · `skill-manager` · `skills`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-toolbox-ui/bab6fdf6979d2501.png" width="100%" alt="Imzl-zl/dsh-toolbox-ui screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 52</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Un elenco curato dei migliori plugin AI eccezionali per assistenti AI, inclusi…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin DSH — modelli OpenCode Zen gratuiti per DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace / Mercato dei plugin DSH: sfoglia, installa e aggiorna…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime per plugin destinato a software che si evolve autonomamente — il…
- [hanelalo/browser-bridge](https://github.com/hanelalo/browser-bridge) - 让你的agent真的像你一样操控你的浏览器窗口.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directory curata di plugin per DeepSeek Harness (DSH) — oltre 280 plugin della…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH: shell Git Bash per tutte le modalità agent su Windows.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Raccolta di plugin GUI web per DSH (DeepSeek Harness) — notifiche delle…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugin, strumenti, skill e risorse formative per DeepSeek Harness (dsh)…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - Gestione degli aggiornamenti del programma principale e dei plugin di DeepSeek…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vero PowerPoint, non HTML. Dì alla tua IA quali contenuti includere e…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Grafo locale della conoscenza del codice e harness del contesto per agenti di…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Trasforma i modelli già autenticati nell.
- [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) - DSH 插件：一个设置面板，统一管理 MCP 服务器、技能、场景、记忆、子智能体人格、AGENTS.md…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - Plugin DSH: tre strumenti creati sulla base dell.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - plugin dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Test di compatibilità sempre attivi per i plugin DeepSeek Harness: release…
- [chipweaver/veripower](https://github.com/chipweaver/veripower) - An open-source agent flow from natural language spec through Verilog RTL and…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host di DeepSeek Harness che conserva i documenti del progetto e la…
- [PianoPrince/dsh-workspace-mover](https://github.com/PianoPrince/dsh-workspace-mover) - 拖拽真迁移 DSH 会话跨工作区：批量移动、分组合并、挂错归位、回收站、备份恢复 + 对话内 agent 工具；步步备份可回滚，零 token / True…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Raggi X per i plugin DeepSeek Harness: capacità dichiarate rispetto al…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace con più cartelle: consente all.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - Plugin DSH: collega i modelli dell.
- [Noob-stupid/dsh-github-login](https://github.com/Noob-stupid/dsh-github-login) - DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Deep link alle sessioni + esportazione completa della sessione (markdown/JSON)…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: una finestra degli strumenti Git di livello IDE come scheda nativa…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Dai all.
- [laoduu/DeepSeek-Harness-yizi-themes](https://github.com/laoduu/DeepSeek-Harness-yizi-themes) - 19 temi di stile selezionati per la Web UI di DeepSeek Harness（dsh）, portati…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard di verifica senza dipendenze per i plugin DeepSeek Harness (dsh)…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness plugin ecosystem: 86 open-source plugins in a 101-repo family…
- [possible055/agentshim](https://github.com/possible055/agentshim) - High-performance, capability-aware repository tools and process execution for…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode su DeepSeek Harness — plugin DSH che mantiene operativi OpenCode Zen +…
- [YeqingTang/dsh-session-flow](https://github.com/YeqingTang/dsh-session-flow) - DSH 会话信息流重设计插件：跨会话档案柜，折叠时间线 / 血缘树 / 检索 / 双模式摘要 / ZIP 导出 / 实时跟踪.
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace di plugin di terze parti e gestore del ciclo di vita…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx è uno spazio di lavoro desktop estensibile e incentrato sulle persone…
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Esegui DeepSeek Harness sul desktop senza costi di token: una GUI gratuita e…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Coding agent completo per DeepSeek Harness — workflow in stile Claude Code…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - Plugin DSH: mostra il saldo del tuo account DeepSeek in fondo alla barra…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - Workbench dsh Bots: plugin Cordis che collega il gateway di orchestrazione…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite della comunità per l.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): scheda laterale market-dashboard per il…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Plugin e strumenti indipendenti di terze parti per DeepSeek Harness, mantenuti…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Usa i modelli gratuiti OpenCode Zen in DeepSeek Harness con accesso anonimo o…
- [Asukayanamii/learn-cordis4py](https://github.com/Asukayanamii/learn-cordis4py) - Cordis 插件框架的 Python 复刻：上下文与作用域、fiber 生命周期、五种事件分发、服务依赖注入、配置校验、YAML 装载器.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin DeepSeek Harness: trasforma il fallimento del provisioning dell.
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Valutazione dei progressi per i cicli di obiettivi autonomi di dsh: rimanda il…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - Plugin dsh: trasforma un arresto per lunghezza troncato nel recupero…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugin che ripuliscono dopo sé stessi: un port Swift 6 del framework di plugin…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime per plugin Rust con un kernel del ciclo di vita verificato da Verus…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Integrazione dell.

</details>

<a id="writing"></a>

## Testi, discussioni e video

Articoli, discussioni e video sulla funzionalità delle mod.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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

<a id="other"></a>

## Altri progetti

Voci che interagiscono con la superficie delle mod, ma che non sono mod in sé, mantenute visibili anziché nascoste.

<details>
<summary>📦 <b><a href="https://github.com/rajmand/claude_mods">rajmand/claude_mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Non è stata pubblicata alcuna descrizione upstream.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Altri progetti`                                                                    |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **0**      |
| Ultimo push                | 2026-10-12 |
| Prima comparsa nell'elenco | 2026-10-12 |

</details>

<a id="projects-by-implementation-language"></a>

## Progetti per linguaggio di implementazione

L'ecosistema è concentrato in Python e TypeScript, ma continuano a comparire client tipizzati in altri linguaggi. Questa tabella viene generata dalle voci stesse.

| Linguaggio | Voci | Esempi                                                                                                        |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 386  | `anthropics/claude-code`, `anthropics/claude-code-action`, `see-stack/claude-code-mods`                       |
| JavaScript | 76   | `huaweicloud/huaweicloud-devkit`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`          |
| Python     | 39   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 10   | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 9    | `persiyanov/herdr-reviewr`, `Tripstack-Corp/spyc`, `cc-friend/ccost`                                          |
| Go         | 5    | `kartollikaa/claude-android-emulator`, `backstabslash/goccc`, `esengine/DeepSeek-Reasonix`                    |
| Swift      | 3    | `chrisnguyen1211/pillrdotlol`, `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`        |
| PowerShell | 2    | `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win`                                   |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1    | `crafts69guy/claude-statusline.nvim`                                                                          |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |

<sub>Vengono conteggiate solo le voci che dichiarano una lingua. Le voci di documentazione e discussione sono escluse da questa tabella.</sub>

## Contribuire

Le correzioni sono benvenute e rappresentano il modo più rapido per migliorare questo elenco. Apri una issue o una pull request se una voce è classificata o valutata erroneamente, oppure se un progetto è stato escluso per errore a causa di una collisione di nomi — è proprio in quest'ultima categoria che i filtri automatici hanno più probabilità di sbagliare.

---

<sub>Progetto indipendente della community. Non affiliato a Anthropic, né approvato o revisionato da quest'ultima. Claude Code, Claude e Anthropic sono marchi commerciali di Anthropic. Il comportamento del prodotto può cambiare senza preavviso; verifica qualsiasi informazione essenziale nella documentazione ufficiale. Le risorse restano di proprietà dei rispettivi progetti upstream e vengono riprodotte solo quando una licenza lo consente.</sub>

<sub>Ultimo aggiornamento · 2026-10-12T21:29:43+08:00</sub>
