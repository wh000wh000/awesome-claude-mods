<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod straordinarie per Claude">
</p>

<h1 align="center">Mod straordinarie per Claude</h1>

<p align="center"><b>L'indice di mod e plugin per Claude Code, valutati in base alle evidenze, e dei comportamenti più profondi che modificano.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-592-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <b>Italiano</b> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indice aggiornato** · Ultima sincronizzazione: `2026-10-11T12:27:08+08:00` (UTC+8)
> · Voci: **592** · Aggiunte nell'ultimo aggiornamento: **0** · Linguaggi di implementazione: **13**

<sub>Ogni voce qui sotto è stata raccolta, filtrata e verificata nuovamente in automatico. Nessuna voce è un'inserzione a pagamento.</sub>

<a id="featured"></a>

## Selezioni del momento

<sub>Una voce per categoria, classificata in base al livello delle prove e alle stelle, con ricalcolo a ogni aggiornamento. È una classifica, non un'approvazione; ogni selezione rimanda alla relativa scheda completa qui sotto. Sono preferiti i progetti che hanno pubblicato uno screenshot o una registrazione, così la fascia rimane visiva.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9469 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2533 · Python · 👁️ observed</sub>
<sub>Trova i token fantasma. Sistemali. Sopravvivi alla compattazione. Evita il deterioramento della qualità del contesto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74299 · TypeScript · 👁️ observed</sub>
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
- [Mod: realizzate con la funzionalità mod](#mod-realizzate-con-la-funzionalità-mod) — **470**
- [Gli ecosistemi dei plugin DSH e Cordis](#gli-ecosistemi-dei-plugin-dsh-e-cordis) — **95**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150091 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Riepilogo

Claude Code è uno strumento di programmazione agentico che vive nel terminale, comprende la tua base di codice e ti aiuta a programmare più velocemente eseguendo attività di routine, spiegando codice complesso e gestendo i flussi di lavoro git, tutto tramite comandi in linguaggio naturale.

<sub>🔧 Trovato nel codice: `feed.xml`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | TypeScript                                              |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **150091** |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9469 · TypeScript · ✅ official · 1 天</summary>

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
| Stelle                     | **9469**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8246 · Python · ✅ official · 1 天</summary>

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
| Stelle                     | **8246**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6337 · Python · ✅ official · 241 天</summary>

##### 📝 Riepilogo

Un'azione GitHub di revisione della sicurezza basata sull'AI che usa Claude per analizzare le modifiche al codice alla ricerca di vulnerabilità di sicurezza.

##### 📌 Informazioni di base

| Campo      | Valore                                                  |
| ---------- | ------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic` |
| Prova      | `pubblicato direttamente da Anthropic`                  |
| Linguaggio | Python                                                  |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **6337**   |
| Ultimo push                | 2026-02-11 |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 1 天</summary>

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
| Stelle                     | **1798**   |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

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
| Prima comparsa nell'elenco | 2026-10-05 |

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
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Cross-session usage & cost observatory for the DeepSeek Harness web profile — trend/heatmap dashboards, per-model peak-hour pricing (CNY/USD), official DeepSeek balance with spend reconciliation.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic`                                        |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3**      |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `billing` · `cordis` · `cost` · `cost-estimation` · `dashboard` · `deepseek` · `deepseek-harness` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/enc-hanted--dsh-pulse/4a81f8e7c5f01f18.png" width="100%" alt="Enc-hanted/dsh-pulse screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Questo è un launcher per il DeepSeek Harness ufficiale. Non apporta modifiche: avvia semplicemente ciò che sviluppa DeepSeek.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Ufficiali: repository e note di rilascio di Anthropic`                                        |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3**      |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2533 · Python · 👁️ observed · 0 天</summary>

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
| Stelle                     | **2533**   |
| Ultimo push                | 2026-10-10 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐474 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Catalogo della community di mod pubbliche di Claude Code (hook di funzione), analizzate a partire da GitHub con indicazione di ciò che ogni mod può leggere, scrivere, eseguire o inviare tramite la rete. Sfoglia https://mods.aidojo.si/

<sub>🔧 Trovato nel codice: `data/seeds.txt`, `data/duplicates.txt`, `data/repos.txt`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **474**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐182 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: plugin basati su hook che aggiungono righe in tempo reale sopra il prompt, protezioni, pannelli e giochi. Barra del contesto, misuratore di utilizzo, controllo delle revisioni di Codex, anteprima Markdown, riproduzione in corso su Spotify e altro.

<sub>🔧 Trovato nel codice: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **182**    |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐119 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stelle                     | **119**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐110 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Mod per Claude Code: seleziona il livello di ragionamento per ogni prompt, mostra la cache del prompt e il contesto, e consente il passaggio di consegne o la compattazione con un clic

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
| Stelle                     | **110**    |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Un CLI QA nativo per agenti per le pagine web. Deterministico, senza test da scrivere e senza LLM.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | HTML                                                                                |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **104**    |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐89 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Temi per Claude Code: righe degli strumenti con icone, schede con differenze, tabelle e grafici Mermaid, una fascia di utilizzo e quindici temi. /skin li sostituisce al volo.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **89**     |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

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
| Stelle                     | **77**     |
| Ultimo push                | 2026-10-08 |
| Prima comparsa nell'elenco | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **74**     |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Riepilogo

Mod di Claude Code di Darrell Wang — bande sopra il prompt, zero token del modello. Dashboard di Taiwan／USA + altro in arrivo.

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
| Prima comparsa nell'elenco | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐63 · TypeScript · 👁️ observed · 8 天</summary>

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
| Stelle                     | **63**     |
| Ultimo push                | 2026-10-02 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐58 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Riepilogo

Competenze, agenti, comandi, regole, hook e stili di output avanzati per Claude Code — continuità delle sessioni + strumenti moderni CLI per workflow di sviluppo reali

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
| Stelle                     | **58**     |
| Ultimo push                | 2026-10-07 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

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
| Prima comparsa nell'elenco | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

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
| Stelle                     | **27**     |
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
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

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
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Riepilogo

Modifiche di Claude Code: 21 stili e un set completo di funzionalità da attivare quando servono, per il terminale e l'app desktop. · Applica con un clic un nuovo stile a Claude e offre un'intera serie di funzionalità attivabili su richiesta.

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
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Riepilogo

Dieci mod di Claude Code, guide per principianti, prompt per la creazione, demo sicure e un modello per costruire i tuoi mod.

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
| Prima comparsa nell'elenco | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Riepilogo

Mod di Claude Code: usage-band mostra sopra il prompt i tuoi limiti di 5h/7d, la finestra di contesto e il tasso di cache hit

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
| Prima comparsa nell'elenco | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Riepilogo

Mod di Claude Code che rendono più facili da leggere e a cui rispondere le domande di Claude (qa-guide).

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
| Ultimo push                | 2026-10-07 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

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
| Stelle                     | **11**     |
| Ultimo push                | 2026-10-09 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Riepilogo

Dieci mod open source per Claude Code: riquadri in tempo reale, bande, righe di stato e protezioni per le chiamate agli strumenti. Misuratore di combustione, codici di lancio, sessione conclusa, scontro con il boss, animaletto del codice e altro.

<sub>🔧 Trovato nel codice: `swarm/README.md`</sub>

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
| Ultimo push                | 2026-10-03 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Riepilogo

Due mod per Claude Code: bridge Codex per l'uso del computer e sessioni Claude coordinate. Sorgenti, prompt di build, configurazione e test.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **11**     |
| Ultimo push                | 2026-10-05 |
| Prima comparsa nell'elenco | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

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
| Ultimo push                | 2026-10-08 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

KOZMOS — mod visive in tempo reale per Claude Code (CLI + desktop): fasce sopra il prompt, barre laterali, ticker di stato, compagni, protezioni e suoni.

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
| Prima comparsa nell'elenco | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

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
| Stelle                     | **8**      |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Riepilogo

Sei mod di Claude Code in un unico plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) con interruttori per singolo mod, più un rapporto mod-vs-hook.

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
| Prima comparsa nell'elenco | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Riepilogo

Raccolta di mod di Claude Code di 개발동생. Pacchetto taxi: tassametro, navigazione, telecamere per il controllo della velocità, dashcam

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
| Prima comparsa nell'elenco | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Guarda su youtube.com</a> · la riproduzione si apre sul sito ospitante; GitHub non può incorporarla nella pagina</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Riepilogo

Markdown, visualizzato nella casella del prompt di Claude Code mentre digiti. Il codice delimitato diventa una scheda con evidenziazione della sintassi prima ancora che tu chiuda il delimitatore.

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
| Ultimo push                | 2026-10-03 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Riepilogo

Mod Claude Code: pannello utilizzo granchio pixel usage-hud + link HTML cliccabili nel terminale e schede codice con copia in un clic html-shelf

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
| Ultimo push                | 2026-10-08 |
| Prima comparsa nell'elenco | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Mod per Claude Code: plugin con hook di funzione che aggiungono riquadri live e comportamento all'interfaccia del terminale

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | TypeScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **6**      |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Riepilogo

Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and cost, work streams, and a markdown reader for .planning. Read-only.

##### 📌 Informazioni di base

| Campo      | Valore                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Categoria  | `Mod: realizzate con la funzionalità mod`                                           |
| Prova      | `il suo stesso testo nomina una mod API, oppure dichiara la funzionalità delle mod` |
| Linguaggio | JavaScript                                                                          |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **6**      |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/6df9cbfbbf321de0.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/3774c05315c85992.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 436</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Raccolta di oltre 100 mod che puoi usare con Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod di Claude e strumenti per crearle: prima una competenza per la creazione…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - L.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Usa Claude Mods per cambiare il tetto di Claude Code: senza modificare il…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quattro mod di Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mod di Claude Code di Learning Hacker: trasformano il funzionamento dell.
- [kakha13/claude](https://github.com/kakha13/claude) - Mod Claude Code che correggono e traducono i tuoi prompt prima che Claude li…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un riquadro laterale per Claude Code: i subagenti eseguiti da una sessione, ciò…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Pannello della barra laterale di Claude Desktop (scheda Code): elenca tutti i…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mod e competenze di Claude Code di Nekyia Labs, sviluppati e utilizzati ogni…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Una cabina di pilotaggio per Claude Code: barre del piano in tempo reale…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base di conoscenza Obsidian con fonti citate sulle mod di Claude Code: come…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Competenza che insegna agli agenti di Claude Code a creare Mod di Claude…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra di utilizzo sopra la casella di input di Claude Desktop (scheda Code)…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mod di Claude (plugin function-hook) per Claude Code.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin e skill Claude della community, installabili da un unico mercato.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galleria dei mod di Baselane: mod di Claude Code, verificati e fissati.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una coda decisionale CLI/TUI per persone che lavorano con agenti…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod del pannello IDE di Claude Code: pannello degli agenti, albero dei file e…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Scheda di stato flottante per Claude Code — modello, contesto, limiti di…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mod di Claude Code: screen-guard nasconde nomi e segreti durante la…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Estensioni di Claude Code. Sblocca tutto il potenziale di Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) di Claude Code che aggiunge un pannello laterale con schede…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Pannelli, protezioni e mod per migliorare l.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Due mod di Claude Code sopra la casella del prompt: indicatore della finestra…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Il tuo piano, mentre si tiene sotto controllo da solo.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Legge i file markdown a cui Claude Code dà un nome, visualizzati accanto alla…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collaboratore vocale per Claude Code. Parla delle tue idee con un lupo 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mod di Claude Code: typing-speed, un tachimetro della velocità di digitazione…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuochi d.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Scopri mod, plugin ed estensioni di Claude Code con demo animate, elenchi per…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod di Claude Code: diagrammi Mermaid disegnati inline nella trascrizione.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Piccoli mod di Claude Code (plugin con hook di funzione): session-switcher e…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod di Claude Code: miniature delle immagini incollate sopra il prompt, in…
- [joonhyukyim/redpen](https://github.com/joonhyukyim/redpen) - Redpen is a Claude Code mod for reviewing what Claude changed, line by line, in…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mod di Claude Code: mod-scout (trova le mod che useresti di più), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Due mod di Claude Code per eseguire molte sessioni contemporaneamente: una…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Mod Claude Code: controlla nativamente dal TUI il contenuto…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Fai durare più a lungo il piano Pro di Claude: mod di Claude Code per un HUD di…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow per Claude Code: una checklist tranquilla sopra il prompt che mostra…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - I migliori mod per Claude Code: selezionati a mano, convalidati, fissati.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code: routing automatico del modello Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Sei mod per Claude Code: mascotte animata Clawd, barre per limite d.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Un marketplace di mod per Claude Code: un debugger passo-passo per il ciclo…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mod di Claude Code: menu Strumenti di Claude, modalità Zen, temi del terminale…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Il miglior pacchetto di mod tutto-in-uno per Claude Code: limiti di utilizzo e…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Riproduci YouTube Shorts nel tuo Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Toolkit di Naren per Claude: skill, mod e server MCP per Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod di Claude Code che visualizza le differenze di Edit e Write in due colonne…
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code mod that lets Claude log unfinished work to Docs/todos.md, with a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mod per Claude Code: Clawd, una piccola mascotte pixel che mette in scena ciò…
- [reporails/arcade](https://github.com/reporails/arcade) - Giochi desktop classici come mod di Claude Code, giocabili in un pannello…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Un elenco curato di mod di Claude Code, installabili come marketplace di…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mod di Claude Code che mantengono onesto un agente — hook di funzione che…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - La mia raccolta di mod di Claude Code, un mod per directory.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Cinque mod gratuiti di Claude Code: Simple Mode, Usage Tally, Context Handoff…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mod di Claude Code: barra del contesto, pannello degli agenti, sfocatura PDPA.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Appena uscito dalla fabbrica. Una mod di Claude Code: chiedi un meme e continua…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della cache dei prompt, prossimi passi, pulsanti…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Una mod di Claude Code che mostra i limiti di utilizzo e la spesa nella fascia…
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - La modifica skill-router: Jev seleziona e carica le competenze necessarie per…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Un app store per le mod di Claude Code, dentro Claude Code: usa /mods per…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Le mod di Claude Code di Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mod di Claude Code: barre di avanzamento per i piani, un registro di ciò che…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six Claude Code mods: plan limits and context above the prompt, an allowlist…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mod di Claude Code di MacLeod Labs: streams districa il lavoro intrecciato di…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Note sul campo del primo giorno sulle mod di Claude Code su Windows: una barra…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mod che ho realizzato e uso personalmente nella mia configurazione di Claude…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod di Claude Code: misuratori live di costo, contesto e quota del piano sopra…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Una modifica al codice di Claude che trattiene il fan-out dei subagenti, i…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods per claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod per Claude Code che attiva o disattiva le tue competenze, i tuoi agenti…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mod per Claude Code: plugin basati su hook di funzione.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Titoli di coda in stile cinematografico per la tua sessione di programmazione.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un gruppo di mod di claude code realizzate da me.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Un lettore YouTube basato su cliamp all.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Mod di Claude Code: dashboard della flotta di agenti e pilota automatico…
- [vynnlee/mods](https://github.com/vynnlee/mods) - Modifiche di Claude Code realizzate da vynnlee.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Impara una lingua straniera mentre lavori con Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Gestisce una lunga sessione di Claude Code al posto tuo: osserva il riempimento…
- [AdamCaviness/prompt-marks](https://github.com/AdamCaviness/prompt-marks) - Claude Code mod: marks your prompts in the transcript and jumps between them.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Risposte a tema, diagrammi a larghezza completa e contesto e limiti a colpo…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Quando l.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra laterale con costi, token e utilizzo del contesto in tempo reale per…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code mod: a backlog of the follow-ups Claude suggests across every…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Comunicazioni radio di Counter-Strike 1.6 per Claude Code — &quot;Fuoco nel buco&quot;…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internet radio inside Claude Code: a cliamp sidebar, mini player, favorites…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: una mod di Claude Code per progettare ed eseguire grafi di agenti…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Configurazione di Herdr + mod di Claude Code per il lavoro di sviluppo del…
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Dashboard notch di macOS per Claude Code: limiti di utilizzo, sessioni aperte…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude sta cucinando. Chatta con la tua squadra.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Una mod di Claude Code: cattura i Modster in pixel art in un gioco inattivo…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Vedi quali file ogni agente di Claude Code ha nel proprio contesto, e quanto di…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Mantieni la calma. Un termometro per le tue giornate con Claude Code: ogni ora…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Piccole mod di Claude Code per il terminale e l.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Collection of Claude Code mods, each in its own repo: usage-meter…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod: a progress pane for tasks, subagents, workflow runs, the goal…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod: a clickable, timestamped table of contents of the whole…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod: plan rate limits, context fill, session cost and per-task…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI che aggiunge parole spagnole nelle risposte dell.
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Mod di Claude.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Una mod di Claude Code che lo rielabora come The Machine di Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Mod di Claude Code: esegue il compacting al momento giusto.
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Un compagno di Naruto in pixel art per Claude Code: 20 ninja, 60 jutsu…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mod open source per Claude Code: riquadri, righe di stato, notifiche…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Una mod di Claude Code: un riquadro per ogni subagente, i file che modifica e…
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Directory della community di mod, plugin, skill, agenti, hook e server MCP per…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod di Claude Code: stato della sessione, avanzamento live di Spec Kit e…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La finestra di contesto come un.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) di Claude Code che fa apparire l.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Scopri cosa esegue Claude Code in background: sottoagenti, processi Codex…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - A free, open-source plugin for Claude Code.
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - Mod personali di Claude Code: otto-hud, Otto il polpo con meteo del contesto e…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Una Mod di Claude che mostra le richieste pull di GitHub della sessione in un…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: un debugger per le chiamate agli strumenti di Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Competenze di Claude Code: verificatore dei fatti per la documentazione…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin buddy di Claude Code: un compagno ASCII sopra il prompt che ricorda le…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin di Claude Code per la visibilità degli strumenti per agente — nasconde e…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Mod di Claude Code: livello di sicurezza per Claude Code — oscuramento dei…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Una raccolta di mod per Claude Code.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod di Claude Code: un SDLC AI-native.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Raccolta di mod fantastici per Claude Code | Raccolta di mod di 클로드 코드.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugin di Claude Code (mod): passa da un account Claude all.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod di Claude Code testate e installabili con un solo comando: protezioni per…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: una mod di Claude Code che legge ad alta voce, su richiesta, le…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Spank Claude when it messes up — a stress-relief mod for Claude Code: cartoon…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Fai durare fino al doppio il tuo utilizzo di Claude Code.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod di Claude Code: piccoli plugin per riquadri in tempo reale, instradamento…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin di Claude Code: monitoraggio dell.
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Three free Claude Code mods: hide .env values from tool results, watch a remote…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Modifiche al codice di Claude. touch-map: mostra quali file Claude ha elencato…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Un mod di Claude Code che riassume in inglese semplice i messaggi degli agenti…
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mods for Claude Code: live panes, bands and hooks. A plugin marketplace.
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [0xnicholasy/claude-mod-collapse-tools](https://github.com/0xnicholasy/claude-mod-collapse-tools) - Claude Code mod: collapses every tool-call row in the transcript to one line;
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Claude Code plugin marketplace for 0xnicholasy.
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Mod di Claude Code + driver cheap-executor: una sessione Claude come…
- [AdamCaviness/cache-magic](https://github.com/AdamCaviness/cache-magic) - Claude Code mod that offers a flexible alternative to the built-in…
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gatto braille animato sopra il prompt di Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod di Claude Code: indirizza il lavoro economico a GLM/Kimi tramite un Claude…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gatto pixel sopra il prompt di Claude Code che esegue una chiamata di test a…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Una mod di Claude Code che sceglie il momento giusto per compattare e mantenere…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Modifiche di Claude Code per Claude: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace di plugin per Claude Code di anderson-spider.
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mods for Claude Code.
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - La nave LGTM Lines salpa dopo ogni modifica al codice — un mod di Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - I tuoi limiti di utilizzo di Claude come scheda animata della salute di un…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mod di Claude Code per il team S2 (il marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Brevi allenamenti mentre Claude lavora: un obiettivo giornaliero, serie, badge…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un pannello di utilizzo per Claude Code: spesa per modello.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - A Claude Code mod: live context-window breakdown above the prompt.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing per Claude Code: Apple Music e Spotify sopra il prompt, con…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Cinque mod di Claude Code per eseguire molte sessioni contemporaneamente…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Claude Code mod pack from the Berko video: Mask, View, Guard, Saving, Chime +…
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Mod di Claude Code: fascia di utilizzo, elenco chat, /cube, /handoff, pulizia…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod per Claude Code: orologio della cache, Blast Radius, suggerimenti, lista di…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mod di Claude Code: Suggestion Spotlight mostra a cosa si riferisce il prossimo…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un gufo per il tuo Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Fascia di Claude Code su una riga.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Il motore Doom originale con Freedoom, giocabile dentro Claude Code.
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi che vive dentro Claude Code: si schiude, mangia il codice scritto…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Segnalibri e contrassegni in stile Vim nelle conversazioni del terminale di…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Trasforma ogni sessione Claude Code in una piccola avventura: musica generativa…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Mod di Claude Code: mostra l.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mod di Claude Code scritte come hook di funzione e il marketplace che le offre.
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Mod di Claude Code e sistemi di design: crab-crew e il sistema di design Crab…
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - My Claude Code mods, shared as a plugin marketplace.
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - Modifiche al codice di Claude di divramod: riquadri live e personalizzazioni…
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - I mod di Claude Code che uso su ogni macchina: savvy-progress, filetree, skins…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code mod: after a guard blocks a tool call, it stops recognized detours…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code mod: one inbox for messages from teammates, named subagents and…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code mod: explains sandbox blocks and turns repeated blocks into…
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Ehi, silenziato! Elimina il diff, taglia il riff, niente più modifiche e meno…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod di Claude Code: utilizzo dell.
- [evasuka/work-meter](https://github.com/evasuka/work-meter) - Claude Code mod：在輸入框上方顯示工作進度與帳號額度剩餘.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Mod progettati con il motion design per Claude Code: un monitor in tempo reale…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Mercato delle mod di Claude.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar in tempo reale dei tuoi branch paralleli e worktree sopra il prompt…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - Le mie mod di Claude Code.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mod e skin per Claude Code: una barra di avanzamento in tempo reale per le…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Seven Claude Code mods: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+clic per copiare il link su ogni blocco di codice nelle risposte di Claude…
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - Il mod jev: $.jev per Claude Code, giudizi tipizzati da TypeSafe Jev.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Mod di Claude Code: pannello che mostra se la cache dei prompt è calda o fredda.
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mod per Claude Code: plugin di hook, come usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mod di Claude Code (plugin function-hook), installate tramite un unico…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra laterale in stile Evangelion per Claude Code: contesto, quota, attività…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Mod utili per claude code.
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Il plugin (mod) Claude-Code consente di vedere cosa sta facendo il modello…
- [hamTotk/better-rewind](https://github.com/hamTotk/better-rewind) - Claude Code mod: rewind or summarize from any prompt or AskUserQuestion answer.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Risultati dei test in un pannello di Claude Code: errori, dettagli e cronologia…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod di Claude Code: quanto tempo ha richiesto ogni risposta, quanto ha pensato…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Piccole mod di Claude Code: indicatori di contesto e utilizzo del piano…
- [Jang-seungminn/usage-hud](https://github.com/Jang-seungminn/usage-hud) - Claude Code mod: usage HUD above the prompt with two animated ASCII dogs.
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Un luogo dove ospitare le mie mod di claude.
- [jemsley06/reels-while-you-wait](https://github.com/jemsley06/reels-while-you-wait) - Claude Code mod: Instagram Reels in a small Safari window while Claude works.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Pannello laterale dell.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Elenco laterale dei file: quali file sono stati creati, modificati o eliminati…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Mao Mao in stile 8-bit (coniglio nano olandese bianco e nero) corre e salta…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Pannello laterale «Le mie domande»: ogni frase digitata dal proprietario in…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Cronologia laterale: dove è stato impiegato il tempo di questo turno.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Scambio di token nella barra laterale: quanti token la conversazione principale…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Il sincero sacchetto di fagioli di claude code: al termine di ogni turno…
- [jgilb17/claude-mods](https://github.com/jgilb17/claude-mods)
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Checklist del piano con verifica delle evidenze per Claude Code: i piani…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Piccole modifiche per Claude Code, come nuovi comandi slash e riquadri laterali.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catalogo di mod per Claude Code.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Giochi multiplayer da giocare dentro Claude Code mentre lavora.
- [juampymdd/claude-code-model-picker](https://github.com/juampymdd/claude-code-model-picker) - Claude Code mod: pick the model and version for the next requests from a band…
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Mod di Claude Code: mantiene calda la cache del prompt mentre sei lontano e…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive in una fascia sopra il prompt di Claude Code: mette in scena la…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - Un mod di Claude Code che mostra sopra il prompt la disponibilità del limite di…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod per leggere ad alta voce le risposte e le notifiche di Claude Code tramite…
- [Kareem1809/chat-cigarette](https://github.com/Kareem1809/chat-cigarette) - 🚬 A Claude Code mod: a cigarette burns down with every message — when it.
- [kba977/claude-code-pomodoro](https://github.com/kba977/claude-code-pomodoro) - A pomodoro timer above the Claude Code prompt (Claude Code mod).
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod di Claude per leggere e unire le conversazioni tra le tue sessioni di…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code mod: running subagents as pixel Claude mascots above the prompt.
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Mod di Claude per piccole comodità e miglioramenti della qualità d.
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - riduci le sessioni fredde di claude code con haiku — fascia cache su una riga…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Due mod di Claude Code: folio, un riquadro dei file accanto alla chat, e tint…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD delle attività in tempo reale per Claude Code Desktop: una fascia sopra…
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Una guida ai mod di Claude Code curata dalla community: casi d.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Una mod di Claude Code che mostra cosa sta facendo Claude nel sottotitolo della…
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Mod di Claude Code: spinge la sessione principale a delegare agli subagent e…
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - La mia raccolta personale di plugin mod per claude.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Le mod di Claude Code di Marcel in un unico mercato dei plugin (marcel-mods).
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod di Claude Code con profili di autorizzazione commutabili: una base…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mod della community per Claude Code: protezioni, riquadri e comandi eseguiti…
- [mina-asham/claude-usage-stats](https://github.com/mina-asham/claude-usage-stats) - A Claude Code mod that shows your plan usage.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un discreto riquadro laterale per Claude Code: cosa sta facendo questa…
- [mmedum/spor](https://github.com/mmedum/spor) - Ripristina ciò che Claude Code nasconde: i file letti da Claude, i comandi…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod di Claude Code che riattiva gli strumenti todo per i modelli che li…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod di Claude Code: una riga per ogni attività sopra il prompt con l.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Gioca a Connect Four contro un.
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Un canarino in pixel art per Claude Code: muore quando Claude smette di seguire…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Modifica al codice di Claude: quando un altro agente di programmazione esegue…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Modifica al codice di Claude per repository condivisi da diversi agenti IA…
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Un pannello radio Internet cyber-neon per Claude Code: manopola synthwave…
- [niksavis/handily](https://github.com/niksavis/handily) - Mod di Claude Code che mostrano i tuoi elementi di lavoro, le attività e le…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barriera di sicurezza per SQL in Claude Code: chiede conferma prima che…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Una modifica per Claude Code, Windows e CJK prima di tutto: anteprime di…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime per Claude Code: un suono quando Claude termina, richiede il tuo…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mod di Claude Code: miniature delle immagini e riga di stato.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - I migliori mod di Claude Code, ordinati in base a ciò che fanno per te.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Mod di Claude Code: visualizza ogni immagine e file consultato dal tuo agent…
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Una mod di Claude Code che trattiene i comandi shell rischiosi.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Due mod Claude per Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Lazy Panda Panel per Claude Code: esamina i documenti senza alzare una zampa.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Swear at Claude Code and a cartoon hand slaps back.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code mods: usage-both shows 5-hour and weekly usage above the prompt.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod: clickable paths in replies — click a folder to open it in…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Pannello laterale con statistiche della sessione in tempo reale per la scheda…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Varie mod e skill per la mia configurazione di Claude Desktop.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mod per Claude Code: safety-guard blocca i comandi distruttivi e l.
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods for Claude Code: function-hook plugins that run inside the session…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod di Claude Code: ticker azionario in tempo reale, pannello /quote, avvisi…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod di Claude Code: host SSH, RAM e limiti di utilizzo 5h/7d in una riga sopra…
- [Rinze-Smits/ifc-viewer-claude-mod](https://github.com/Rinze-Smits/ifc-viewer-claude-mod) - IFC Viewer mod for Claude Code.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code: flessioni da fare mentre Claude lavora. Nessun token.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [Rsclub22/claude-mods](https://github.com/Rsclub22/claude-mods)
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - A Claude Code mod that routes tasks to other AI models.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Il negozio di mod per Claude Code: acquisisce le mod da GitHub, ne offre…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod di Claude Code: trasforma il piano approvato in modalità piano in una…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una selezione curata di mod di Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modalità senza costi: gli agenti ausiliari funzionano su Haiku e i file e i log…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una colonna sonora lofi che segue la sessione: calma, concentrazione, flusso…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Impara mentre Claude programma: dopo un turno che ha modificato il codice…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una registrazione di ogni modifica effettuata da Claude: riproduci ogni…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Ogni link menzionato dalla tua sessione, in un.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Dimostrazione minima degli hook di funzione di Claude Code: pannello in tempo…
- [shawnbotha/claude-mods](https://github.com/shawnbotha/claude-mods) - Different Claude mods.
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - Mod di Claude Code (plugin con hook sulle funzioni) di ShellTime.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Claude Code mod for context, growth, quota, cache, native cost and agent…
- [skryvets/claude-status-bar-mod](https://github.com/skryvets/claude-status-bar-mod) - Mod di Claude Code: informazioni colorate sulla sessione sotto il prompt…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Un mod HUD RPG accogliente per Claude Code.
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Marketplace personale di mod di Claude Code…
- [Steady-Matter/spotter-pals](https://github.com/Steady-Matter/spotter-pals) - Spotter: a Claude Code mod with pixel Pals that hatch and grow as your helper…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messaggi di commit con un clic per Claude Code con una Malenia in pixel-art che…
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - mod di Claude Code.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Personal Claude Code mods.
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Mod di Claude Code — marketplace sunkanxx-mods.
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Mod di Claude Code: HUD a barra compatta.
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugin per Claude Code.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Mod per Claude Code: delete-guard.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Mod di Claude Code: visualizza l.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Mod di Claude Code: pannello live del team per ogni subagente.
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - Un mod di Claude Code che sceglie il modello e l.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod di Claude Code che mostra la sessione corrente in un pannello: ogni…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace di plugin Claude Code di mod: plugin function-hooks che…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code mods on demand — a skill that reads your conversation and builds…
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Mod di Claude Code: un riquadro agganciato che mostra i sottoagenti della…
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Claude Code mod that writes your Claude usage limits to a file other tools can…
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Mod di Claude Code: una banda e un pannello che tengono traccia dei tuoi…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Un catalogo curato di mod di Claude Code, ciascuno con un prompt da copiare e…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod di Claude Code: fascia di avanzamento animata e riepilogo del completamento…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tre piccoli mod di Claude Code: scopri quando i tuoi sottoagenti termineranno…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Fai a Claude una domanda laterale in un riquadro accanto al tuo lavoro.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace di mod per Claude Code con installazione in un solo passaggio e…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Conti alla rovescia del limite di frequenza e previsione del consumo per Claude…
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Livello di sicurezza di Roblox Studio per Claude Code: audit di RemoteEvent…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Piccoli mod per migliorare l&#x27;esperienza d&#x27;uso di Claude Code.
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Mod di Claude Code: stage-toons, una barra di avanzamento del flusso di lavoro…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod per Claude Code. agent-crew: osserva i tuoi subagenti al lavoro come un…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - A live task board for Claude Code: plan before building, follow every task…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Barra sempre attiva sopra il prompt di Claude Code: riempimento del contesto e…
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - Mod personali di Claude Code (marketplace di plugin).
- [zwbao/zebra-mod](https://github.com/zwbao/zebra-mod) - zebra-mod: a Claude Code mod that turns Claude Code into a rare-disease…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una raccolta curata delle migliori risorse per il più straordinario degli…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin Claude Code che mostra cosa sta succedendo: utilizzo del contesto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Elegante statusline altamente personalizzabile per Claude Code CLI, con…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Tutte le parti del prompt di sistema di Claude Code, 27 descrizioni degli…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Oltre 45 consigli per ottenere il massimo da Claude Code, dalle basi agli…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / competenze Codex — genera caroselli Xiaohongshu e coppie di…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline elegante in stile vim per Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Esamina il diff del tuo agente di coding in un pannello del terminale e invia…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin completo della barra di stato per Claude Code con utilizzo del contesto…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code e tracciamento dei token locali di Codex — barra di stato.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crea mod per Claude Code: aggancia qualsiasi richiesta, modifica qualsiasi…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Dashboard completa della barra di stato per Claude Code — informazioni sulla…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: monitora l.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Una statusline estetica per Claude Code, realizzata da awesomejun.
- [amirfish1/claude-command-center](https://github.com/amirfish1/claude-command-center) - One local board for Claude Code, Codex, Cursor and 5 more coding agents.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Competenze e mod pubblici di Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Competenze, mod, subagenti, hook, comandi slash e guide per Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legali e gratuiti e agenti di coding — aggiornamento automatico…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Statusline del terminale per le sessioni Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Risultati in diretta, calendari e classifiche di calcio per la competizione…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Local control plane for Claude Code on Windows and macOS: switch LLM gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Competenza per agenti che trasforma il tuo agente di programmazione in un…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configurazione personale di Claude Code versionata all.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Orari delle preghiere, data Hijri, adhkar, ayah quotidiana, digiuno sunnah…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Riga di stato consapevole della sessione per Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — plugin DeepSeek Harness per argomenti di ricerca…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Useful statusline for Claude Code that displays model, effort, context, cost…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Toolkit portatile Claude Code per .NET DDD/Clean Architecture: agenti TDD…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Raccolta di plugin per Claude Code, pi e DeepSeek Harness: HUD della barra di…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configurazione globale portabile di Claude Code: skill personalizzate, hook…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin di Claude Code che uso ogni giorno: skill e mod, ripuliti per funzionare…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram dentro Claude Code: leggi chat e canali in un pannello e ricevi…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace per plugin e skill Claude Code per facilitare le mod del gioco…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Governance dei token per Claude Code: il modello principale dirige…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visualizzatore a riquadri divisi per Claude Code in Windows Terminal e tmux: la…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Statusline live delle fasi del flusso di lavoro per Claude Code.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mod non ufficiali per la scheda Code di Claude Desktop — usage-pet: una banda…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository per le mod Awesome Media di Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Riduci la spesa di token di Claude Code e Codex: indirizza ricerche ed…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Simple and useful status line setup for Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Avvisi sui limiti di utilizzo per Claude Code: notifiche macOS, avvisi nell.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Riga di stato configurabile di Claude Code per Linux, WSL, Windows e macOS, con…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Statusline veloce di Rust per Claude Code — payload prima di tutto, git in…
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Statusline di Claude Code con barra del contesto, sparkline dei token e monitor…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Dashboard live dell.
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Una riga di stato e una riga dei token per Claude Code: contesto, utilizzo su 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Mostra i dettagli chiave dello stato di Claude Code, inclusi modello, contesto…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - la statusline amichevole di Claude Code, da modificare in ogni dettaglio…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Riga di stato multilivello di Claude Code: spesa, % del contesto, git e account…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline con informazioni utili per claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Template iniziale per organizzare uno spazio di lavoro Claude Code…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Team di agenti nativi. Sotto controllo.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Riga di stato personalizzata per Claude Code — barra del contesto con…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - A clean, informative status line for Claude Code — shows project, git status…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace di plugin Claude Code con baloo: competenze, un agente che verifica…
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Riga di stato di Claude Code: utilizzo del contesto, barre della quota 5h/7d…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Riga di stato di Claude Code di livello professionale: durata della sessione…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Riga di stato di Claude Code consapevole dell.
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - Un plugin di Claude Code: un riquadro con le sessioni Claude Code e Codex in…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Una ricca riga di stato del terminale per Claude Code — Bun + TypeScript, zero…
- [eddywong888/claude-castle-mod](https://github.com/eddywong888/claude-castle-mod) - A Castlevania-style usage HUD mod for Claude Code: context blood meter…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin di Claude Code che visualizza magnificamente i diagrammi Mermaid nella…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Strumenti, skill e agenti per Claude Code — a partire da una riga di stato che…
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Configurazione globale di Claude Code: agenti, skill, mod, impostazioni.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Plugin di Claude Code: visualizza sempre il limite di utilizzo di Claude di 5…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Spesa reale DeepSeek API per Claude Code: ricalcola il prezzo delle…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods para Claude Code y Claude Desktop en Windows con WSL: Docker y rendimiento…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Riga di stato di Claude Code con righe del pannello degli agenti.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincronizza le attività di Claude con Fizzy.do per una visibilità del team in…
- [J-J-E/claude-kanban](https://github.com/J-J-E/claude-kanban) - A markdown kanban board for Claude Code: cards are files, a board pane, and a…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Visualizza una barra di stato dettagliata e con codifica a colori per Claude…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu delle impostazioni, riga di stato e configurazione di Claude Code.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Parla con Claude Code tramite la voce su Windows: una Mod + helper che usa…
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Riga di stato personalizzata di Claude Code con finestra di contesto…
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - Riga di stato Rust veloce per Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - plugin, skill, mod di claude fatti in casa e senza vincoli, e altro ancora.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Installer dell.
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugin e mod di Claude Code per capire cosa fa Claude: formati di risposta…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitora lo stato di Claude Code dalla barra dei menu macOS con indicatori in…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Barra di stato colorata su più righe per Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Riga di stato di Claude Code per Windows (PowerShell): barre di utilizzo, conto…
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Plugin di Claude Code. Usage Bars mostra i limiti di frequenza della sessione e…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings and Glossary per Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Statusline personalizzata di Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Configurazione e mod di Claude Code, con un kit di componenti condivisi, un…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Config Claude Code portatile: CLAUDE.md, impostazioni, statusline, skill.
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Tieni traccia dell.
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Raccolta di mod per Claude Code.
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Monitoraggio dei costi in tempo reale e riga di stato per il monitoraggio della…
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Plugin Cordis / DeepSeek Harness — l&#x27;agente chiede all&#x27;utente un segreto in una…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Riga di stato di Claude Code su tre righe: profondità del contesto, limiti di…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Rilevatore del deterioramento del contesto 2026 - Monitor proattivo della…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagent e statusline di Claude Code: raccolte e strumenti open-source…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Riga di stato di Claude Code — indicatori di utilizzo Claude/Codex che restano…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Un builder visuale per le statusline di Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline di Claude Code che mostra l.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mod per Claude Code: riquadri, bande e compagni basati su hook di funzione.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passa le attività tra le tue sessioni di Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Questo in un server MCP per controllare MODS, lo strumento modulare…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill di Codex e Claude Code per tradurre mod di CK3 con un LLM locale.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mod open source e altre estensioni per Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: trova ciò che chiedi a Claude Code ancora e ancora e trasformalo in…

</details>

<a id="dsh-cordis"></a>

## Gli ecosistemi dei plugin DSH e Cordis

DeepSeek Harness e Cordis arrivano allo stesso risultato da una direzione diversa: per loro il plugin è il meccanismo delle mod, quindi un plugin lì equivale a una mod qui.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74299 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stelle                     | **74299**  |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100435 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **100435** |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81723 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **81723**  |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐76541 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **76541**  |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **35760**  |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30374 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Una moderna soluzione desktop per l’ecosistema di plugin DeepSeek Harness (DSH). Tutto è un «plugin», anche il desktop stesso è un «plugin».

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **30374**  |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25474 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Riepilogo

Distilly — Distilla il loro modo di pensare in competenze riutilizzabili per qualsiasi agente o bot. Precedentemente Colleague Skill（原同事 Skill）.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | Python                                                                                         |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **25474**  |
| Ultimo push                | 2026-09-22 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9115 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Meta-framework della componibilità spaziotemporale

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **9115**   |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8598 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Ecosistema di aggregazione dei plugin web DeepSeek Harness (DSH) · Tutto è un plugin, distribuito tramite il Creative Workshop · Ecosistema di aggregazione dei plugin web DeepSeek Harness (DSH) · Tutto è un plugin, distribuito tramite il Creative Workshop

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **8598**   |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐7124 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **7124**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4270 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Il plugin TUI ufficialmente più consigliato per DSH: alte prestazioni, basso consumo di risorse, simpatica balena in pixel e interazione fluida con il mouse. Installazione con un solo comando tramite npm. / Il plugin TUI ufficialmente più consigliato per DSH: alte prestazioni, basso consumo di risorse, simpatica balena in pixel, interazione fluida con il mouse e installazione con un solo comando tramite npm

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **4270**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3144 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Versione desktop Tauri di DeepSeek Harness | Installer di soli 8 MB, nessuna configurazione dell’ambiente, plugin preimpostati, Windows / macOS / Linux.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **3144**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NanmiCoder/dsh-agent-teams">NanmiCoder/dsh-agent-teams</a></b> · ⭐2012 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

DeepSeek Harness 的 Agent Teams 多智能体协作插件，支持多个 AI Agent 组成团队，协同完成复杂任务，实现任务分配、并行执行、成员通信与团队协作。 AgentTeams plugin for DeepSeek Harness

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **2012**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agentteams` · `deepseekharness` · `dsh` · `dsh-agent-teams` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nanmicoder--dsh-agent-teams/b3647beca323c018.png" width="100%" alt="NanmiCoder/dsh-agent-teams screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1969 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1969**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1780 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1780**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1394 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

AI 小说创作软件：把灵感、角色、世界观、大纲、章节写作、审稿和修稿组织成可控流程；提供 Windows/macOS 桌面版，支持本地和在线模型。AI Novel Writing Software: Organizes inspirations, characters, worldbuilding, outlines, chapter drafting, review, and revision into a controllable workflow. Features desktop apps for Windows/macOS, Ollama integration, and a DeepSeek Harness (DSH) plugin preview.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **1394**   |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **1169**   |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐703 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Client desktop DeepSeek Harness (dsh) Windows - Node.js + dsh CLI inclusi, avvio con un clic

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **703**    |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/text2future/flowix">text2future/flowix</a></b> · ⭐453 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **453**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent-memory` · `claude-code` · `codex-cli` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `hermes-agent`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/9fc65a8848fe78ee.png" width="100%" alt="text2future/flowix screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/ea3f84c8693d4236.gif" width="100%" alt="text2future/flowix animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Mars-Sea/dsh-commandcode-provider">Mars-Sea/dsh-commandcode-provider</a></b> · ⭐377 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Command Code provider plugin for DeepSeek Harness (dsh). Adds Command Code model access, live model catalog, plan-aware model selection, reasoning effort, image input, web search, and multi-account support.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **377**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `command-code` · `commandcode` · `deepseek-harness` · `dsh` · `dsh-plugin` · `llm` · `llm-provider` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mars-sea--dsh-commandcode-provider/2f2256468a8af0b9.png" width="100%" alt="Mars-Sea/dsh-commandcode-provider screenshot"></td>
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
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **255**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐250 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin DSH (DeepSeek Harness) non ufficiale: usa i modelli web di chat.deepseek.com come provider LLM — acquisizione dell'accesso tramite browser, risoluzione PoW, streaming SSE, chiamate agli strumenti basate su prompt.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **250**    |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **203**    |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Bash, PowerShell 7, and Rust-based tools for dsh on Windows to cut token usage. / 为windows的dsh提供bash、powershell7及rust的高性能tools来减少token消耗

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **203**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin DeepSeek Harness per la migrazione in anteprima delle sessioni tra preset. I passaggi con schema fisso preservano lo stato, l'intento del modello sorgente e le immagini irrisolte; la sessione originale rimane intatta.

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
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐128 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Tema desktop Claude Code per DeepSeek Harness｜ Tema desktop Claude Code creato per la GUI web di DeepSeek Harness

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **128**    |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐120 · Python · 🔎 inferred · 0 天</summary>

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
| Stelle                     | **120**    |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐99 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Plugin DSH - sicurezza degli aggiornamenti del framework e controllo dei plugin: pre-verifica del contratto, punto di ripristino, rollback automatico in caso di errore, disattivazione automatica basata sulle evidenze; include inoltre un marketplace di plugin multi-sorgente. Non ufficiale. | Plugin DSH: sicurezza degli aggiornamenti del framework + controllo dei plugin — pre-verifica del contratto prima dell'aggiornamento, punto di ripristino, rollback automatico in caso di errore e disattivazione automatica solo in presenza di prove certe; include inoltre un marketplace di plugin multi-sorgente. Progetto comunitario non ufficiale.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **99**     |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐85 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

StudyHub: un plugin DeepSeek Harness (DSH) che trasforma il tuo materiale in domande e ripassi dilazionati · plugin di apprendimento DSH che trasforma il tuo materiale in domande e ripassi dilazionati

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **85**     |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

dsh-sieve: plugin di progettazione del contesto e ottimizzazione dei token per DeepSeek Harness (DSH) — filtraggio dell'output degli strumenti, potatura del contesto, divulgazione progressiva delle competenze. Payload più piccolo del 36% nella riproduzione offline. Plugin DSH per la gestione del contesto e il risparmio tramite l'ottimizzazione dei token.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **74**     |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐73 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

Controllo remoto di DeepSeek Harness（dsh web）su Internet: installazione immediata di un indirizzo crittografato dedicato, accesso remoto dal telefono anche fuori casa, senza bisogno della stessa rete locale/WiFi né di perforazione della rete interna; servizio self-hosted opzionale. Controlla DeepSeek Harness (dsh web) da remoto ovunque ti trovi — URL pubblico crittografato, senza LAN richiesta.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | JavaScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **73**     |
| Ultimo push                | 2026-10-10 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-web` · `pwa`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://cdn.jsdelivr.net/gh/mrRisega/dsh-remote@main/image/phone-mirror.png" width="100%" alt="mrRisega/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

<sub>Risorsa collegata direttamente dal repository upstream perché non è stata dichiarata alcuna licenza compatibile con la ridistribuzione.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐62 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

基于 Deepseek-Harness 核心底座打造的桌面版 Agent.继承底坐全部能力。并补全 IDE 相关功能。

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **62**     |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Contexera/dsh-agent-team">Contexera/dsh-agent-team</a></b> · ⭐57 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Riepilogo

dsh-agent-team gives DeepSeek Harness agents that don't reset: durable Members with their own memory, notes, and skills across sessions, rollovers, and restarts. You set the direction; agents coordinate through Channels and Tasks.

##### 📌 Informazioni di base

| Campo      | Valore                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Categoria  | `Gli ecosistemi dei plugin DSH e Cordis`                                                       |
| Prova      | `ha dichiarato una mod, un plugin o un hook, ma nulla di specifico sulla superficie delle mod` |
| Linguaggio | TypeScript                                                                                     |

##### 📊 Dati

| Metrica                    | Valore     |
| -------------------------- | ---------- |
| Stelle                     | **57**     |
| Ultimo push                | 2026-10-11 |
| Prima comparsa nell'elenco | 2026-10-11 |

🏷 `agent-orchestration` · `agent-team` · `ai-agents` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `multi-agent`

---

<table><tr><th align="center" width="50%">🖼 Immagine</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/contexera--dsh-agent-team/25f8cc5a2a3231a3.png" width="100%" alt="Contexera/dsh-agent-team screenshot"></td>
<td align="center" valign="top"><sub>nessun contenuto multimediale pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b>Altro in questa categoria</b> <sub>· 61</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Una protezione pre-esecuzione per gli agenti AI di coding.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Un elenco curato dei migliori plugin AI eccezionali per assistenti AI, inclusi…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH Plugin Marketplace / Mercato dei plugin DSH: sfoglia, installa e aggiorna…
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - 终末地官网风格的 DSH Web 主题：奶油纸底、墨黑文字、信号黄强调、全直角工业编辑风.
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime plugin per programmi che restano in esecuzione — core Rust, plugin…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Miglior Bug Checker Roblox Luau e strumento di verifica API 2026 DevForum MCP.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - La directory in continua evoluzione dei plugin DeepSeek Harness — aggiornata…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana: DeepSeek Harness as a subagent for HanaAgent.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - 面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directory curata di plugin per DeepSeek Harness (DSH) — oltre 280 plugin della…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Toolkit Zotero per DeepSeek harness; trasforma la tua libreria Zotero in un…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH: shell Git Bash per tutte le modalità degli agenti su Windows…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistema di agenti per chat di gruppo multipiattaforma basato su…
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh安卓版：集成 DeepSeek Harness、Ubuntu 运行环境、插件与文件管理，以及用户授权的 Shizuku 和无障碍自动化.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web plugin: per-day token usage statistics with a GitHub-style activity…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Workbench di scrittura locale per autori cinesi di narrativa web.
- [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) - Appearance customization plugin for DeepSeek Harness: theme color palette…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - MCP server manager plugin for DeepSeek Harness: Settings → MCP page, OAuth…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Plugin DeepSeek Harness: 15 competenze di ingegneria obra/superpowers…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A commerce negotiation runtime + DeepSeek Harness (dsh) plugin.
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - Interfaccia di gestione del server MCP per DeepSeek Harness Web — pannello…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vero PowerPoint, non HTML. Dì alla tua IA quali contenuti includere e…
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - Plugin DeepSeek Harness: modalità senior pigra e porting della scala a 7…
- [godchen520/dsh-web-remote](https://github.com/godchen520/dsh-web-remote) - DSH 手机/外网远程访问插件：免配置公网隧道 + 局域网 HTTPS 直连 + 自定义公网链接/端口 + 微信机器人.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Trasforma i modelli già autenticati nel client desktop WorkBuddy locale…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - One-stop skills, subagent, MCP and LSP manager for DeepSeek Harness (DSH)…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Test di compatibilità sempre attivi per i plugin DeepSeek Harness: release…
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - Zero-cost, zero-hassle toolkit for DeepSeek Harness (DSH): one-click setup for…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Raggi X per i plugin DeepSeek Harness: capacità dichiarate rispetto al…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host di DeepSeek Harness che conserva i documenti del progetto e la…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Conversazioni vocali local-first per DSH.
- [YunongDai2005/dsh-theone](https://github.com/YunongDai2005/dsh-theone) - One chat for everything, no more hunting for old conversations.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: una finestra strumenti Git di livello IDE come scheda nativa…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - Modalità creativa basata sulla modalità PTC: plugin DSH, orchestrazione degli…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace con più cartelle: consente all.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plugin per il flusso di lavoro ingegneristico di DeepSeek Harness: fasi delle…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - Plugin di roleplay DSH: schede dei personaggi.
- [openbkn-ai/bkn-dsh](https://github.com/openbkn-ai/bkn-dsh) - OpenBKN.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard di verifica senza dipendenze per i plugin DeepSeek Harness (dsh)…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Mercato dei plugin DeepSeek Harness - sfoglia, cerca e installa i plugin del…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode su DeepSeek Harness — plugin DSH che mantiene operativi OpenCode Zen +…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace di plugin di terze parti e gestore del ciclo di vita…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx è una workstation desktop estensibile e incentrata sulle persone…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Plugin per l.
- [heiheiha798/dsh-plugin-subagent-delete](https://github.com/heiheiha798/dsh-plugin-subagent-delete) - DSH plugin: delete_subagent tool + UI - release or permanently remove subagent…
- [momasiku/dsh-pilot](https://github.com/momasiku/dsh-pilot) - Desktop automation for DeepSeek Harness: hands and eyes on the whole Windows…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Fornisce alla versione desktop di DeepSeek Harness un punto di accesso remoto…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): scheda laterale market-dashboard per il…
- [yu381792/superlcm](https://github.com/yu381792/superlcm) - 五种载体，一座本地对话档案馆：原文归档、分层后台摘要、原文查证与跨工具接续。默认原生压缩，Claude Code 与 dsh harness 可选接管.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin Harness di DeepSeek: trasforma il fallimento del provisioning ACL della…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Rende ripetibile un tentativo vuoto del modello senza attribuzione, per l.
- [denceee/dsh-everything-claude-code](https://github.com/denceee/dsh-everything-claude-code) - Adapts everything-claude-code to DeepSeek Harness: 11 skills, an ECC agent…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness agent preset: Codex and Claude Code as delegation subagents…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime per plugin Rust con un kernel del ciclo di vita verificato da Verus…
- [mrpulor-gh/nuphus-mcp](https://github.com/mrpulor-gh/nuphus-mcp) - Desktop automation MCP server — computer use for any AI agent: control screen…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.

</details>

<a id="writing"></a>

## Testi, discussioni e video

Articoli, discussioni e video sulla funzionalità delle mod.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
| TypeScript | 383  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 79   | `Enc-hanted/dsh-pulse`, `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`                        |
| Python     | 39   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 27   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 14   | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7    | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 6    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2    | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| Swift      | 2    | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1    | `dphmoblie/deepseek-harness-android`                                                                          |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |

<sub>Vengono conteggiate solo le voci che dichiarano una lingua. Le voci di documentazione e discussione sono escluse da questa tabella.</sub>

## Contribuire

Le correzioni sono benvenute e rappresentano il modo più rapido per migliorare questo elenco. Apri una issue o una pull request se una voce è classificata o valutata erroneamente, oppure se un progetto è stato escluso per errore a causa di una collisione di nomi — è proprio in quest'ultima categoria che i filtri automatici hanno più probabilità di sbagliare.

---

<sub>Progetto indipendente della community. Non affiliato a Anthropic, né approvato o revisionato da quest'ultima. Claude Code, Claude e Anthropic sono marchi commerciali di Anthropic. Il comportamento del prodotto può cambiare senza preavviso; verifica qualsiasi informazione essenziale nella documentazione ufficiale. Le risorse restano di proprietà dei rispettivi progetti upstream e vengono riprodotte solo quando una licenza lo consente.</sub>

<sub>Ultimo aggiornamento · 2026-10-11T12:27:08+08:00</sub>
