<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Excellents mods Claude">
</p>

<h1 align="center">Excellents mods Claude</h1>

<p align="center"><b>L’index de Claude Code regroupant les mods et plugins évalués selon les preuves, ainsi que les comportements sous-jacents qu’ils modifient.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-585-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <b>Français</b> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Index en ligne** · Dernière synchronisation: `2026-10-13T06:19:35+08:00` (UTC+8)
> · Entrées: **585** · Ajoutées lors de la dernière mise à jour: **0** · Langages d’implémentation: **12**

<sub>Chaque entrée ci-dessous a été collectée, filtrée et revérifiée automatiquement. Aucun contenu présenté ici n’est sponsorisé.</sub>

<a id="featured"></a>

## Sélections du moment

<sub>Une entrée par catégorie, classée selon le niveau de preuve et le nombre d’étoiles, puis recalculée à chaque mise à jour. Il s’agit d’un classement, pas d’une recommandation ; chaque sélection renvoie à sa fiche complète ci-dessous. Les projets ayant publié une capture d’écran ou un enregistrement sont privilégiés, afin que le bandeau reste visuel.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9486 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2543 · Python · 👁️ observed</sub>
<sub>Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74439 · TypeScript · 👁️ observed</sub>
<sub>🌊 L&#x27;agent harness original. Déployez des essaims intelligents multi-joueurs, coordonnez des workflows autonomes et créez des systèmes d&#x27;IA conversationnelle.…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Contenu

- [Ce qu’est un mod Claude Code](#ce-quest-un-mod-claude-code)
- [Comment les entrées sont évaluées](#comment-les-entrées-sont-évaluées)
- [Officiel : les propres dépôts et notes de version de Anthropic](#officiel--les-propres-dépôts-et-notes-de-version-de-anthropic) — **17**
- [Mods : conçus avec la capacité de mod](#mods--conçus-avec-la-capacité-de-mod) — **451**
- [Écosystèmes de plugins DSH et Cordis](#écosystèmes-de-plugins-dsh-et-cordis) — **106**
- [Articles, discussions et vidéos](#articles-discussions-et-vidéos) — **11**
- [Projets par langage d’implémentation](#projets-par-langage-dimplémentation)

## Ce qu’est un mod Claude Code

Claude Code a intégré les **mods** en 2.1.287 : des extensions susceptibles de modifier le comportement plus en profondeur qu’un plugin, et qui dessinent leur propre interface.

Un mod peut s’accrocher à `ui.render` pour afficher une **ligne, une bande, un panneau ou une carte** autour de l’invite, lire le texte que vous avez sélectionné en dernier avec `$.ui.selection()`, créer des coéquipiers avec `agent.spawn` et gérer une région `Client`. Un mod qui échoue à s’afficher échoue seul — `ui.fault` empêche un mod défaillant de faire tomber la session.

Cette liste couvre les mods, l’interface des plugins et des hooks sur laquelle ils s’appuient, ainsi que les équivalents DSH et Cordis. Elle ne couvre délibérément **pas** l’écosystème plus large de Claude Code : un pack d’invites n’est pas un mod.

## Comment les entrées sont évaluées

La plupart des listes dans ce domaine affirment qu’un élément en fait partie. Celle-ci indique ce qui a réellement été vérifié, puis vous permet de filtrer en conséquence. Un niveau décrit les éléments probants, et non la qualité du projet — un mod bien conçu dont personne n’a encore parlé reste `inferred`.

| Évaluation                                                                               | Signification                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `publié par Anthropic lui-même`                                                          | Publié par Anthropic lui-même, ou lu directement dans le changelog officiel.                                                                                                                                                                                |
| `son propre texte mentionne un mod API, ou déclare la prise en charge des mods`          | Son propre texte mentionne une partie de l’interface des mods — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, un panneau, une bande ou une carte — : l’auteur décrit donc quelque chose qu’il a conçu pour fonctionner avec le véritable API. |
| `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` | Se présente comme un mod, un plugin ou un hook, mais rien dans son texte ne mentionne spécifiquement l’interface des mods. Réel, mais non confirmé.                                                                                                         |
| `correspondance fondée uniquement sur le vocabulaire`                                    | Correspondance fondée uniquement sur le vocabulaire. Incluse pour que le filtre soit vérifiable, et non parce qu’elle est considérée comme fiable.                                                                                                          |

<a id="official"></a>

## Officiel : les propres dépôts et notes de version de Anthropic

Les dépôts Code personnels de Anthropic pour Claude, ainsi que les versions qui ont défini la surface des mods. À consulter dans la source plutôt que dans un résumé.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150420 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Résumé

Claude Code est un outil de programmation agentique qui s'exécute dans votre terminal, comprend votre base de code et vous aide à coder plus rapidement en exécutant les tâches routinières, en expliquant le code complexe et en gérant les workflows git, le tout au moyen de commandes en langage naturel.

<sub>🔧 Utilisé dans le code: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |
| Langage   | TypeScript                                                       |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **150420** |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9486 · TypeScript · ✅ official · 3 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |
| Langage   | TypeScript                                                       |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **9486**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8255 · Python · ✅ official · 3 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |
| Langage   | Python                                                           |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8255**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6354 · Python · ✅ official · 243 天</summary>

##### 📝 Résumé

Une GitHub Action d’examen de sécurité alimentée par l’IA, utilisant Claude pour analyser les modifications du code à la recherche de vulnérabilités de sécurité.

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |
| Langage   | Python                                                           |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **6354**   |
| Dernière mise à jour du dépôt | 2026-02-11 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1800 · Shell · ✅ official · 3 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |
| Langage   | Shell                                                            |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1800**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

##### 📝 Résumé

Documents complémentaires pour les fiches des modèles Claude

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **25**     |
| Dernière mise à jour du dépôt | 2025-12-05 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Résumé

Ajout de Claude Mods : les plugins peuvent désormais modifier un comportement plus profond. Ajout de You should know, un mod intégré où un agent secondaire surveille vos arrières et signale les éléments que vous ou Claude pourriez manquer. Activez-le avec `/plugin enable cc-plugin-you-should-know@builtin` (pour les sessions first-party avec la télémétrie activée)

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Résumé

Ajout de `$.ui.selection()` pour les mods : renvoie le dernier texte sélectionné en mode plein écran et, lorsque la sélection se trouve dans une seule ligne de transcription, cette ligne. Correction du bouton d’un mod qui exécutait parfois l’action d’un autre bouton lorsqu’il était pressé sur une vue dessinée avant le redémarrage de Claude Code. Correction des sessions plein écran qui se terminaient avec « unrecoverable interface error » lors de l’ouverture de la boîte de dialogue des tâches en arrière-plan alors qu’un plugin ou un mod affichait des lignes au-dessus de l’invite. Correction de `claude plugin test` qui signalait les mods comme désactivés à distance alors qu’il avait seulement lu un paramètre enregistré obsolète

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Résumé

Correction d’une règle deny ou ask sur une partie imbriquée d’une commande shell composée qui ne persistait pas au-delà de l’approbation d’un mod installé par l’utilisateur sur des machines gérées. Correction des mods installés qui ne se chargeaient pas lors de la première session après une mise à niveau. Ajout de `agent.spawn` pour les coéquipiers, d’un identifiant d’agent unique pour les événements de hook de plugin ainsi que pour les états inactif et en attente dans `$.agent.list()`. Correction des sessions qui se terminaient avec « unrecoverable interface error » lorsqu’une valeur écrite par le hook `ui.render` d’un mod provoquait une erreur lors du dessin d’une ligne ; le moteur dessine désormais sa propre ligne à la place. Correction du contenu aligné à droite dans le panneau ou la bande d’un mod qui était dessiné sous la marque de fermeture ou `\[-\]`, wh

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Résumé

Ajout de `serverToolUses` au résultat du hook `turn.step` d’un mod : l’outil appelle lui-même API (le conseiller), avec son identifiant, son nom, son entrée, son début et sa fin. Ajout de `ceiling` à la question et au verdict lus par le hook `tool.check` d’un mod, en nommant l’approbation requise par l’organisation pour un outil. Ajout des types `ThemeKey` et `Color` aux types des hooks de plugins, afin qu’un éditeur répertorie les couleurs de thème qu’un dessin de mod peut nommer. Ajout à `claude plugin validate` : chaque hook enregistré par un mod sur un site de contrôle est répertorié avec l’indication qu’il possède un `.catch` (`gatingHooks` sous `--json`). Correction du résultat `turn.step` d’un mod.

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Résumé

Ajout de `prompt.autocomplete`, un événement auquel un mod s’accroche pour ajouter ses propres lignes à la liste de saisie automatique de la boîte d’invite Ajout de la mise en cache des invites à `$.model.complete` pour les mods : `prompt` et `system` prennent des blocs de texte, et `cache: true` sur un bloc met en cache la requête jusqu’à celui-ci Ajout d’agents de workflow au hook de mod `agent.spawn`, avec leur exécution et leur index, afin qu’un mod puisse les refuser Correction des lignes Write, Edit, NotebookEdit et LSP, ainsi que des lignes uniques Read, Grep et Glob, qui masquaient pourquoi un mod avait refusé l’appel : la ligne affiche désormais la raison Correction du hook `config.set`, `state.set`, `env.set` ou `agent.spawn` d’un mod qui refuse aprè

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Résumé

Ajout de `isDeferred` à `$.tool.register` pour les mods : `false` liste dès le début le schéma de l'outil dans le prompt au lieu de le laisser derrière la recherche d'outils. Correction des hooks d'un mod sur les événements `classic.*`, qui étaient ignorés pendant le redémarrage du worker des hooks du plugin, laissant les hooks de réglages répondre sans eux. Correction de l'échec de `claude plugin test` pour les mods qui appellent `$.session.append` ; les tests peuvent relire les lignes ajoutées avec le nouveau `mock.session`

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Console de gestion MCP pour le client officiel DeepSeek Harness MCP : commande /mcp avec diagnostics de santé et appels d’essai de pipeline, un onglet Paramètres MCP avec CRUD de serveurs (écritures soumises à approbation, sauvegardes automatiques) et une console d’essai d’outils via le pipeline d’outils officiel (Apache-2.0, dsh-plugin).

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic`                         |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **74**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/fschmutz/claude-usage-panel">fschmutz/claude-usage-panel</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

See your Claude Code plan usage everywhere: GNOME top bar, macOS menu bar, a status line under the Claude Code prompt, and a get_usage MCP tool for Claude Code + Cursor. Session, weekly & per-model (Fable/Opus) limits from the official usage API, with burn-rate forecasts. One-line install, self-updating.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic`                         |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **6**      |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `anthropic` · `ccusage` · `claude` · `claude-code` · `cursor` · `developer-tools` · `gnome` · `gnome-extension`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fschmutz--claude-usage-panel/40b54f8d52b03345.png" width="100%" alt="fschmutz/claude-usage-panel screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-ticktick">PerryLink/dsh-ticktick</a></b> · ⭐4 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Pont de tâches TickTick (Dida365) pour DeepSeek Harness : panneau de tâches dans l’en-tête de session (filtre de liste, vues des tâches non terminées/terminées, recherche, réorganisation par glisser-déposer), 11 outils d’agent sélectionnés, carte de paramètres, via l’endpoint officiel TickTick MCP.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic`                         |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4**      |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dida365` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/aa581021cb97f4dd.png" width="100%" alt="PerryLink/dsh-ticktick screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/44088595da097cb2.gif" width="100%" alt="PerryLink/dsh-ticktick animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Ajout de `$.ui.notify` pour les mods : déclenche une notification native via…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Correction d.

</details>

<a id="mods"></a>

## Mods : conçus avec la capacité de mod

Every entry here shows evidence of using the capability Claude Code gained in 2.1.287: it draws through `ui.render`, owns a pane, band or card, reads `$.ui.selection()`, spawns teammates with `agent.spawn`, or says plainly that it is a mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2543 · Python · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | Python                                                                          |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **2543**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐530 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Catalogue communautaire de mods publics Claude Code (hooks de fonctions), analysés depuis GitHub avec indication de ce que chaque mod peut lire, écrire, exécuter ou envoyer sur le réseau. Parcourir https://mods.aidojo.si/

<sub>🔧 Utilisé dans le code: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **530**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐210 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Résumé

Mods Claude Code : plugins reposant sur des hooks qui ajoutent des lignes en temps réel au-dessus de l'invite, des protections, des volets et des jeux. Barre de contexte, compteur d'utilisation, surveillance des révisions Codex, aperçu Markdown, lecture en cours sur Spotify et plus encore.

<sub>🔧 Utilisé dans le code: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **210**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐161 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Maintenez le cache de prompts de Claude Code à chaud pendant les pauses et affichez le coût estimé avant un envoi à froid.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **161**    |
| Dernière mise à jour du dépôt | 2026-10-04 |
| Première apparition           | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>enregistrement animé · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐117 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Skins pour Claude Code : lignes d’outils avec icônes, cartes de différences, de tableaux et de graphiques Mermaid, bandeau d’utilisation et quinze thèmes. /skin les remplace instantanément.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **117**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Réponses Claude Code colorées et personnalisables : tableaux, code, diagrammes, graphiques et lignes d’outils dans 15 thèmes, avec boutons de copie. Un mod Claude Code.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **88**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Résumé

Une collection de mods pour claude code

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **78**     |
| Dernière mise à jour du dépôt | 2026-10-08 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Un mod Claude Code qui affiche un tableau de bord d'agent en direct dans votre terminal : contexte et coût, chronologie du conseiller, chaque vérification d'autorisation, cartes de sous-agents et couloirs.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **75**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

##### 📝 Résumé

Mods Claude Code par Darrell Wang — bandes au-dessus de l'invite, sans tokens de modèle. Tableau des actions taïwanaises／américaines + d'autres à venir.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | HTML                                                                            |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **65**     |
| Dernière mise à jour du dépôt | 2026-10-05 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Résumé

Skills, agents, commandes, règles, hooks et styles de sortie experts pour Claude Code — continuité des sessions et outils CLI modernes pour les flux de développement réels

<sub>🔧 Utilisé dans le code: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | Shell                                                                           |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **62**     |
| Dernière mise à jour du dépôt | 2026-10-07 |
| Première apparition           | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐55 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Résumé

Collection de plus de 100 mods utilisables avec Claude Code.

<sub>🔧 Utilisé dans le code: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **55**     |
| Dernière mise à jour du dépôt | 2026-10-03 |
| Première apparition           | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Résumé

Mods Claude Code : barres de progression du plan en direct au-dessus de l'invite

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **47**     |
| Dernière mise à jour du dépôt | 2026-10-08 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>enregistrement animé · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Résumé

Regardez Claude Code fabriquer un petit dessin animé pendant que vous travaillez.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **32**     |
| Dernière mise à jour du dépôt | 2026-10-02 |
| Première apparition           | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Résumé

Une barre latérale des prompts de votre session Claude Code : survolez pour lire, cliquez pour accéder (hooks de fonctions / Mods)

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **28**     |
| Dernière mise à jour du dépôt | 2026-10-03 |
| Première apparition           | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐26 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Une nouvelle jeunesse pour Claude Code : un panneau de cockpit en direct, des thèmes partageables et un animal de compagnie pixelisé qui met en scène ce que fait Claude

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **26**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Un Pokémon en pixels qui vit au-dessus de l'invite dans Claude Code

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **25**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Résumé

Compilation, tests, console et aperçus SwiftUI de Xcode dans Claude Code

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **20**     |
| Dernière mise à jour du dépôt | 2026-10-02 |
| Première apparition           | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Mods Claude Code : 21 styles et un ensemble complet de fonctionnalités à activer selon vos besoins, pour le terminal et l'application de bureau. · Appliquez un nouveau style à Claude en un clic et profitez d'un ensemble complet de fonctionnalités activables à la demande.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **20**     |
| Dernière mise à jour du dépôt | 2026-10-04 |
| Première apparition           | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 Résumé

Dix mods Claude Code, guides pour débutants, prompts de création, démonstrations sûres et modèle pour créer le vôtre.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **20**     |
| Dernière mise à jour du dépôt | 2026-10-02 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Modification de code Claude : prévisualise les images et les longs textes collés au-dessus de l’invite

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **19**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐17 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Mod Claude Code : Clawd reproduit ce que fait Claude, au-dessus de l’invite

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **17**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Résumé

Deux mods Claude Code : pont d'utilisation de l'ordinateur Codex et sessions Claude coordonnées. Code source, prompts de compilation, configuration et tests.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **16**     |
| Dernière mise à jour du dépôt | 2026-10-05 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Résumé

Mods Claude Code : usage-band affiche vos limites de 5 h/7 j, la fenêtre de contexte et le taux de réussite du cache au-dessus de l'invite

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **13**     |
| Dernière mise à jour du dépôt | 2026-10-03 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 Résumé

Mods Claude Code qui rendent les questions de Claude plus faciles à lire et auxquelles il est plus facile de répondre (qa-guide).

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **12**     |
| Dernière mise à jour du dépôt | 2026-10-07 |
| Première apparition           | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>enregistrement animé · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Résumé

Mod pour Claude Code : contexte en tokens, limites de 5 heures et hebdomadaires par rapport à l’horloge, compte à rebours du cache de prompt, coût de la session et agents en cours, le tout dans une barre au-dessus du prompt.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **12**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Résumé

Dix mods open source pour Claude Code : volets en direct, bandes, lignes d'état et protections des appels d'outils. Compteur de consommation, codes de lancement, session terminée, combat de boss, animal de code et plus encore.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **12**     |
| Dernière mise à jour du dépôt | 2026-10-03 |
| Première apparition           | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Pixel art animé au-dessus de votre prompt Claude Code, qui réagit pendant que Claude travaille. Sept scènes, ou votre propre image ou GIF. Zéro token.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **10**     |
| Dernière mise à jour du dépôt | 2026-10-04 |
| Première apparition           | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

##### 📝 Résumé

Suivi de sessions pour Claude Code, sous forme de mods : fenêtre de contexte, taux de consommation du quota de plan, coût par tour

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **9**      |
| Dernière mise à jour du dépôt | 2026-09-15 |
| Première apparition           | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Une interface autour de vos terminaux Claude Code et Codex, que vos agents construisent, afin que le seul modèle dans votre tête soit le vôtre.

<sub>🔧 Utilisé dans le code: `CLAUDE.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **9**      |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Résumé

KOZMOS — mods visuels en direct pour Claude Code (CLI + bureau) : bandes au-dessus de l’invite, barres latérales, ticker d’état, compagnons, gardiens et son.

<sub>🔧 Utilisé dans le code: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **9**      |
| Dernière mise à jour du dépôt | 2026-10-10 |
| Première apparition           | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Résumé

Faites durer plus longtemps le forfait Claude Pro : des mods Claude Code pour un HUD d’utilisation précis, une sortie shell plus courte et l’absence de relecture des fichiers. Les mods ne consomment aucun token.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **9**      |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Six mods Claude Code dans un seul plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) avec des interrupteurs par mod, ainsi qu’un rapport mods-vs-hooks.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8**      |
| Dernière mise à jour du dépôt | 2026-10-04 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Collection de mods Claude Code de 개발동생. Pack taxi : compteur, navigation, caméra de contrôle de vitesse, caméra embarquée

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8**      |
| Dernière mise à jour du dépôt | 2026-10-04 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Regarder sur youtube.com</a> · la lecture s’ouvre sur le site hôte ; GitHub ne peut pas l’intégrer directement</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Votre plan, qui se regarde lui-même. Arbre de feuille de route local pour ordinateur de bureau que Claude Code et tout hôte MCP maintiennent à jour en direct. Simple JSON, sans cloud.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8**      |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 417</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods Claude et outils pour les créer : un skill de construction, puis des mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Le harness Claude Code que j.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mods Claude Code de Ray Amjad : volets, bandes, protections d.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Donnez un nouveau toit à Claude Code avec Claude Mods : sans modifier le…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quatre mods Claude Code : Cache Keeper, Recording Mode, Goal Meter et Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods Claude Code de Learning Hacker : rendre le fonctionnement de l.
- [kakha13/claude](https://github.com/kakha13/claude) - Mods Claude Code qui corrigent et traduisent vos prompts avant que Claude ne…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de connaissances Obsidian citant ses sources sur les mods de Claude Code…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods et skills Claude Code de Nekyia Labs, créés et utilisés quotidiennement…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Un cockpit pour Claude Code : barres de plan en direct, bandes de sous-agents…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Une apparence d.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un volet latéral pour Claude Code : les sous-agents exécutés par une session…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods Claude Code : menu Tools de Claude, mode Zen, thèmes de terminal…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panneau latéral Claude Desktop (onglet Code) : répertorie les tâches inachevées…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barre d.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill qui apprend aux agents Claude Code à créer des mods Claude.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins et skills communautaires pour Claude, installables depuis une…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods Claude (plugins à hooks de fonction) pour Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galerie de mods Baselane : mods Claude Code, vérifiés et épinglés.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Une file de décisions CLI/TUI pour les humains travaillant avec des agents…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod pour Claude Code qui affiche les diffs Edit et Write dans deux colonnes…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, peint dans la boîte de prompt de Claude Code pendant la saisie.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods Claude Code : panneau d.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Carte d.
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods pour Claude Code : plugins de hooks de fonctions qui ajoutent des panneaux…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods Claude Code : screen-guard masque les noms et les secrets pendant le…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods et skins pour Claude Code : barre de progression en direct pour les tâches…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensions Claude Code. Débloquez toute la puissance de Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) pour Claude Code qui ajoute un panneau latéral avec les onglets…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panneaux, garde-fous et mods améliorant le confort d.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Deux mods Claude Code au-dessus de la zone d.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lit les fichiers markdown nommés par Claude Code, affichés à côté de la…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude cuisine. Discutez avec votre équipe.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Un test de frappe pour patienter pendant que Claude travaille.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code : miniatures des images collées au-dessus de l.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collègue vocal pour Claude Code. Discutez avec un loup en 3D propulsé par l.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow pour Claude Code : une liste de contrôle claire au-dessus de…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods Claude Code : barre de contexte, panneau des agents, floutage PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods Claude Code : typing-speed, un compteur de vitesse de frappe en direct…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Feux d.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods pour Claude Code : volets, commandes et hooks créés avec le plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Découvrez les mods, plugins et extensions Claude Code grâce à des démos…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code : diagrammes Mermaid dessinés directement dans la transcription.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Petits mods Claude Code (plugins à hooks de fonction) : session-switcher et…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six mods Claude Code : limites de plan et contexte au-dessus du prompt, coach…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods Claude Code : mod-scout (trouver les mods que vous utiliseriez le plus)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Deux mods Claude Code pour exécuter de nombreuses sessions simultanément : une…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods Code Claude à la demande — une compétence qui lit votre conversation et…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr : découvrir, inspecter, activer ou désactiver et mettre à jour les mods…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Meilleurs mods Claude Code : sélectionnés, validés et épinglés.
- [davekiss/mods](https://github.com/davekiss/mods) - Mods Claude Code de Dave Kiss.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code : routage automatique des modèles Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Modification de code Claude : volet en direct des PR GitHub qu.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Six mods pour Claude Code : mascotte Clawd animée, barres de limite…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Une boutique d.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Une marketplace de mods pour Claude Code : un débogueur pas à pas pour la…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods open source pour Claude Code : panneaux, lignes d.
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Le meilleur pack de mods tout-en-un pour Claude Code : limites d.
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Lisez des YouTube Shorts dans votre Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Boîte à outils Claude de Naren : skills, mods et serveurs MCP pour Claude Code.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods pour Claude Code : Clawd, une minuscule mascotte pixelisée qui met en…
- [reporails/arcade](https://github.com/reporails/arcade) - Jeux de bureau classiques sous forme de mods Claude Code, auxquels on joue dans…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods pour claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace de mes propres mods pour Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Une liste organisée de mods de Claude Code, installables comme une marketplace…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Deux mods Claude Code : cache-keeper et ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code très affirmé, conçu par un Rustacean passionné d.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods Claude Code qui gardent un agent honnête — des hooks de fonction qui…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Fresh from the factory. A Claude Code mod: ask for a meme, keep working.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod pour Claude Code : barre de cache d.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code qui affiche vos limites d.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Un mod pour Claude Code permettant de noter ses réflexions en cours de travail…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - État en direct des PR GitHub, préparation à la fusion, vérifications…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods pour Claude Code : barres de progression pour les plans, registre de ce…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notes de terrain du premier jour sur les mods Claude Code sur Windows : une…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools : un débogueur pour les appels d.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Mod Claude Code : état en direct des pull requests GitHub.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - De petites cartes qui se placent sous l.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod pour Claude Code : compteurs en direct du coût, du contexte et du quota de…
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 Nous fabriquons du TECHNO, bébéééé 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin et mod de Claude Code : un SDLC natif de l.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod Claude Code qui active ou désactive vos compétences, agents, règles et…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de Claude Code testés et installables en une commande : garde-fous pour…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Un mod d.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un ensemble de mods claude code créés par mes soins.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Mods Claude Code : tableau de bord et pilote automatique pour flotte d.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods Claude Code. touch-map : voyez quels fichiers Claude a listés, lus…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Apprenez une langue étrangère tout en travaillant avec Claude Code.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod Claude Code qui indique en direct quels fichiers Claude a modifiés et…
- [0xctx/sysop](https://github.com/0xctx/sysop) - Dites à Claude ce que vous voulez. Récupérez-le construit, testé, révisé par…
- [20alexl/windvane](https://github.com/20alexl/windvane) - S.
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - Un mod Claude Code qui maintient votre cache d.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barre latérale en direct des coûts, tokens et de l.
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - Mods Claude Code de ayagmar : un marché de plugins.
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Mods à crochets de fonctions pour Claude Code : une ligne de télémétrie des…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods Claude Code pour de vrais ingénieurs.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Récapitulatif de session du terminal de Claude Code, dans l.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Un mod Claude Code : un volet présentant la tâche de la session, ce qui…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Un mod Claude Code : attrapez des Modsters en pixel art dans un jeu…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Voyez quels fichiers chaque agent de Claude Code a dans son contexte, et quelle…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Petits mods Claude Code pour le terminal et l.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI qui ajoute des mots espagnols aux réponses des agents.
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Mod Claude Code qui vous évite de réécrire le cache des invites : /keepwarm…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Vos événements Alarum au-dessus de l.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Votre liste de tâches Floatee au-dessus du prompt de Claude Code : exécutez…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code qui le transforme en The Machine de Person of Interest.
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Mod Claude Code (mod CC tint) : colorer chaque fenêtre selon son dépôt…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code : état de la session, progression Spec Kit en direct et…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La fenêtre de contexte sous forme d.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph : un graphique en direct de ce que Claude Code sait.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tâches en direct pour Claude Code Desktop : une barre au-dessus de…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin Claude Code (mod) qui donne à l.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Ne laissez pas votre attention vagabonder pendant que vous attendez la réponse…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Quatorze mods Claude Code dans un seul plugin, chacun activable séparément…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuit et open source pour Claude Code.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod Claude Code : répondez à Claude point par point, directement sur le texte.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Mods Claude Code pour les longues sessions : sitrep encadre le résultat et les…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Une file d.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Modifications Claude Code : sélectionnées et testées, chaque modification étant…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Compétences de Claude Code : vérificateur de faits pour la documentation…
- [Orfila-antoine/claude-mods](https://github.com/Orfila-antoine/claude-mods)
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Un mod Claude Code qui conserve un dossier de preuves en direct des éléments…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compagnon de Claude Code : un compagnon ASCII au-dessus de votre invite…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin Claude Code pour la visibilité des outils par agent — masquer et refuser…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Mods Claude Code : couche de sécurité pour Claude Code — masquage des secrets…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Rend les formules mathématiques LaTeX en mode affichage dans le terminal de…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Collection de mods géniaux pour Claude Code | Collection de mods pour Claude…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis : un mod de fans non officiel des Avengers pour Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks : un mod de Claude Code qui lit à voix haute, à la demande, les…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Frappez Claude quand il fait une erreur — un mod défouloir pour Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code : petits plugins pour les panneaux en direct, le routage…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, avec justificatifs. Un plugin qui planifie, délègue et prouve que…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod et plugin Claude Code : moniteur d.
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC (Every Mod Claude Code) : une collection organisée et testée de mods Code…
- [yyosifov/prompt-mods](https://github.com/yyosifov/prompt-mods) - De petits mods Claude Code aboutis pour la boîte d.
- [0xgigilau/claude-usage-meters](https://github.com/0xgigilau/claude-usage-meters) - Mod Claude Code : barres de progression pour le contexte, l.
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Place de marché de mods Claude Code (my-claude-mods) : bandeau d.
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Mods Claude Code : cartes de statistiques de session au-dessus de l.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un chat animé en braille au-dessus de l.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un chat pixel au-dessus de votre prompt Claude Code qui exécute un appel de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code qui choisit le bon moment pour compacter afin de garder…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods de Claude pour Claude Code : compteur de tokens.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods polyvalents pour Claude Code : bandes, volets, notifications et hooks.
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - Un mod Claude Code qui sélectionne le modèle de chaque sous-agent avant son…
- [arthurseredaa/herdr-pane-peek](https://github.com/arthurseredaa/herdr-pane-peek) - Claude Code mod for herdr: search panes across all workspaces and insert the…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Vos limites d.
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mods Claude Code pour l.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - De courtes séances d.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un tableau d.
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Mods Claude Code : panneaux, bandeaux et protections en direct qui s.
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Un mod Claude Code qui montre ce que font vos sous-agents : une barre de…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Un mod Claude Code qui indique la durée de chaque tour dans une petite pastille…
- [benelog/claude-mods](https://github.com/benelog/claude-mods) - Mods for Claude Code: a status-line HUD and more.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing pour Claude Code : Apple Music et Spotify au-dessus de…
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - Copies maintenues et auditées de mods Claude Code (filetree, cache-tax).
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - The Performance tab for Claude Code turns: a live waterfall of every model…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods pour Claude Code : horloge du cache, rayon d.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Simplement un hibou pour votre Claude Code.
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - Mods Claude Code personnels.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Le moteur Doom original avec Freedoom, jouable dans Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Petits mods Claude Code lisibles issus du canal CorporateChittyChat.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Maintenez Claude Code sur un plan : étapes, barrières d.
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Mods Claude Code.
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Mod Claude Code : une barre au-dessus du prompt avec le compte à rebours du…
- [curran-gehring/claude-dot](https://github.com/curran-gehring/claude-dot) - Un mod Claude Code qui apporte les points de OpenAI à Claude : un assistant…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - Mes mods Claude Code personnels, personnalisés pour ma propre configuration…
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Mods Claude Code réservés à l.
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Mod Claude Code : voyez quels skills, plugins, sous-agents et outils MCP votre…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Onze mods Claude Code (plugins de hooks de fonctions) pour un flux de travail…
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Mods Claude Code : tableau OpenSpec et sous-agent, transfert avant la…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi qui vit dans Claude Code : il éclot, mange le code écrit par…
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Mod Claude Code : état de la revue de PR, approbations, vérifications et…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Un mod Claude Code : un tableau de vos autres sessions au-dessus du prompt…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - My collection of claude mods.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code : après qu&#x27;un guard bloque un appel d&#x27;outil, il arrête les…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code : tâches en arrière-plan dans une seule vue, avec progression…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code : une seule boîte de réception pour les messages des…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code : explique les blocages du sandbox et transforme les blocages…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoris pour Claude Code : icônes en un clic pour vos commandes et compétences.
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - Un tableau de vagues en direct présentant le plan de votre session au-dessus de…
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, compétences, extensions Pi et mods Claude Code pour Pi, Codex et…
- [esinecan/mental-model-mod](https://github.com/esinecan/mental-model-mod) - Mod Claude Code : modèle de travail d.
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Mod Claude Code pour la progression des tests en arrière-plan : JUnit, Karma…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mods Code de Claude (plugins de hooks de fonctions) : session-meter et autres.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: one tiny button that hides every Claude Code mod above your…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods en test de l.
- [fran343/claude-mods](https://github.com/fran343/claude-mods)
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Mod Claude Code : figez une session et reprenez-la plus tard comme si rien ne…
- [g761007/hudcade](https://github.com/g761007/hudcade) - Un HUD en pixel art pour Claude Code : contexte, coût, cache, agents et limites…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+clic pour copier le lien sur chaque bloc de code dans les réponses de…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - Un mod Claude Code pour l.
- [h3h/blocks-only](https://github.com/h3h/blocks-only) - Mod Claude Code : les tours de programmation se terminent par un rapport validé…
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Marché privé de mods Code de Claude.
- [haruki-cl/claude-code-mods](https://github.com/haruki-cl/claude-code-mods) - Mods Claude Code : token-weather (utilisation du contexte et volet de mémoire)…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Mods en allemand pour Claude Code : indications de contexte/cache, points en…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - A live spend meter for Claude Code: the session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de code Claude : durée de chaque réponse, durée de réflexion de Claude et…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - marketplace de mods claude.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Un cockpit au-dessus de votre prompt Claude Code. Le canard lit les jauges.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Lit automatiquement vos plans d.
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - Tableau en direct des sous-agents de Claude Code dans VS Code : les sous-agents…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panneau latéral d.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Liste des fichiers dans la barre latérale : fichiers créés, modifiés ou…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Un lapin hollandais nain bélier 8-bit (noir et blanc) court et bondit au-dessus…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - La barre latérale « ce que j.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Chronologie dans la barre latérale : où le temps de ce tour a été dépensé…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Échanges de tokens dans la barre latérale : combien de tokens la conversation…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Le petit mot honnête de claude code : après chaque tour, Claude murmure une…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Liste de contrôle de planification soumise à des preuves pour Claude Code : les…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code.
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Mods Claude Code de Joseph Ayoub : une marketplace de plugins (joseph-mods).
- [jrojasdeveloper/naruto-buddy](https://github.com/jrojasdeveloper/naruto-buddy) - Mod Claude Code : Naruto en pixel art animé au-dessus de l.
- [jrpferreira2002-jpg/clawd-vibe](https://github.com/jrpferreira2002-jpg/clawd-vibe) - Mod Claude Code : Clawd au-dessus de l.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vit dans un bandeau au-dessus de votre prompt Claude Code : il met en…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod qui lit les réponses et notifications de Claude Code à voix haute avec…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods pour Claude Code. PixBar : une créature pixelisée au-dessus de votre…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod Claude Code : chaque session Claude Code dans une fenêtre flottante, avec…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Petits mods Claude Code réunis dans un marché de plugins.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Mod Code Claude : choisit le modèle et l.
- [kyuskoj/claude-mods](https://github.com/kyuskoj/claude-mods)
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Dix mods Claude Code : un animal pixelisé animé, Code Wrapped, des rythmes…
- [Loup0007A/claude-mods](https://github.com/Loup0007A/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guide des mods de code Claude sélectionnés par la communauté : cas…
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Mod de Claude Code: los límites de tu plan (sesión 5h, semana) y la renovación…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Mods Claude Code individuels issus de la Mod Box, chacun installable séparément.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de code Claude qui affiche ce que fait Claude dans le sous-titre de…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Un chat noir duveteux au-dessus de votre invite Code Claude.
- [malitov/effort-per-model](https://github.com/malitov/effort-per-model) - Claude Code mod: remembers the effort level per model and restores it on switch.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Les mods Code Claude de Marcel dans une seule marketplace de plugins…
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Petits mods pour Claude Code : runner-avatar, un petit avatar qui court…
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Mods Claude : compteur de tokens (token-meter).
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod de Claude Code : panneau en direct présentant les objectifs, hypothèses…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod Claude Code : volet /sessions pour parcourir et supprimer les sessions…
- [melandres8/claude-mods](https://github.com/melandres8/claude-mods) - Claude Code mods: relevo (planner/builder relay between two sessions) and…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panneau latéral pour Claude Code : fichiers écrits par Claude, divisions du…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Mod Code Claude : Codex (abonnement ChatGPT) et autres modèles non-Anthropic…
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [MoriHiroshiDesu/hiroshi-claude-mods](https://github.com/MoriHiroshiDesu/hiroshi-claude-mods) - Mods pessoais do Claude Code (interface e comportamento).
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Mod Code Claude : nomme l.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de code Claude qui réactive les outils todo pour les modèles qui les…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod Claude Code qui attend une pause sûre, puis transmet votre session ou la…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de code Claude : une ligne par tâche au-dessus du prompt avec la tâche…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jouez au Puissance 4 contre une IA dans Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de code Claude : lorsqu.
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Mod Code de Claude : garde les sessions légères — ligne d.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code mod pour les dépôts partagés par plusieurs agents IA : empêche les…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code mod : un bouton par implémenteur de delegate-skills.
- [NicoSKOOL/seo-mods](https://github.com/NicoSKOOL/seo-mods) - Mods Code Claude pour le SEO : classements DataWise en direct au-dessus du…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Réarme les surveillances longues de Monitor de Claude Code lorsqu.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Un garde-fou pour le SQL dans Claude Code : demande confirmation avant que…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Un volet de bloc-notes pour Code Claude, sous forme de mod.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un seul mod pour Claude Code, Windows et le CJK en priorité : aperçus d.
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mods Code Claude : vignettes d.
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid : le pipeline de revue en peigne → plan → correction, imposé par les…
- [omarnaman/claude-mods](https://github.com/omarnaman/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Les meilleurs Mods de Claude Code, classés selon ce qu.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Deux Mods Claude pour Claude Code : garde-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Horodatages pour Claude Code : l.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack : un mod Code Claude. Worktrees permanents avec un départ en lecture…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live session-stats side pane for the Claude desktop app.
- [PhilRoli/claude-mods](https://github.com/PhilRoli/claude-mods) - Mod Code Claude : mettez les sessions en pause avant l.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods pour Claude Code : safety-guard bloque les commandes destructrices et…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Un crabe Claude en pixel art animé pour Claude Code : il met en scène ce que…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods pour Code Claude : plugins function-hook qui s.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code : des pompes à faire pendant que Claude travaille. Aucun token.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain : un guide de terrain des mods Code Claude, de ELI5 à l.
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - simplement une liste des mods que j.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Trois mods sans dépendances pour Claude Code : une ligne d.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods pour claude code.
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Une marketplace open source pour les mods Claude Code, avec des skills de dépôt…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code : transforme le plan que vous approuvez en mode plan en une…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Une liste soigneusement sélectionnée de mods Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode sans coût : les agents auxiliaires fonctionnent sur Haiku, et les gros…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Une bande-son lofi qui suit la session : calme, concentration, fluidité, ainsi…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Apprenez pendant que Claude code : après un tour ayant modifié le code, une…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Un enregistrement de chaque modification effectuée par Claude : rejouez chaque…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - Un mod Code Claude : un tableau de bord de projet et une carte isométrique…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board et autres mods Code Claude par André Servaes.
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Centre de contrôle pour Claude Code : flotte d.
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Les mods Code de Claude de Showrin pour une activité quotidienne plus…
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Mod Code Claude : limites de contexte et de plan avec projection du rythme de…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Mod Code Claude qui maintient les sessions sans surveillance malgré les limites…
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Claude Code mod: context-window meter per session, with Compact now…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - Une collection de mods Claude Code : hooks de fonctions TypeScript, distribués…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messages de commit en un clic pour Claude Code avec une Malenia en pixel art…
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Mods pour Code Claude. cache-meter : taux de réussite du prompt-cache…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de code Claude qui affiche l.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Unofficial Claude Code mods by tanmen (marketplace: tanmen).
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Mod Code Claude : panneau d.
- [thangnguyen-69/claude-mods](https://github.com/thangnguyen-69/claude-mods) - Marketplace de plugins Code Claude : revues Plannotator sur le tailnet, et plus…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod Claude Code qui affiche la session actuelle dans un panneau : chaque…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins Claude Code de mods : des plugins function-hooks qui…
- [tiger3645/claude-tts](https://github.com/tiger3645/claude-tts) - Mod de Claude Code : lire à voix haute les réponses de Claude.
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Mod Code Claude : un bouton sous la dernière réponse de Claude copie toutes les…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Mods Code de Claude par Toptaab.
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - Mode CC qui affiche, dans le pied de prompt, le compte, l.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Quelques mods Claude.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code : barre de progression animée et résumé de complétion pour les…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trois petits mods Claude Code : voyez quand vos sous-agents auront terminé…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Dites « I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Posez à Claude une question annexe dans un panneau à côté de votre travail.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code plugin : compte à rebours du cache de prompt, taux d.
- [webfront/claude-mods](https://github.com/webfront/claude-mods) - Mods spéciaux pour claude code et code dans claude app.
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Mod de Claude Code : le modèle de la session choisit lui-même le modèle et…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Petits mods d.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — lorsque le contexte dépasse les limites de son enveloppe, le déposer…
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod pour Code Claude : secrets masqués, tâches à faire, vérifications et CI…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Code Claude : vos limites d.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods pour Code Claude. agent-crew : surveillez le travail de vos sous-agents…
- [zhitongLIU/claude-code-mods](https://github.com/zhitongLIU/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Une collection soigneusement sélectionnée des meilleures ressources pour les…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin Claude Code qui montre ce qui se passe - utilisation du contexte…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Ligne d.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Toutes les parties du prompt système de Claude Code, les 27 descriptions…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Compétence vidéo IA pour Claude Code &amp; Codex — vidéos produit cinématiques avec…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Plus de 45 conseils pour tirer le meilleur parti de Claude Code, des bases aux…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — générez des carrousels Xiaohongshu et des paires…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Examinez le diff de votre agent de programmation dans un panneau de terminal et…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de ligne d.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Créez des mods pour Claude Code : interceptez toute requête, modifiez toute…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Tableau de bord complet de ligne d.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon : suivez l.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Une ligne d.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agent de jeu de rôle long format DeepSeek Harness (plugin taverne DSH)…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills et mods publics pour Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, sous-agents, hooks, commandes slash et guides pour Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs légaux gratuits et agents de codage — mise à jour automatique…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Scores, calendriers et classements de football en direct pour les…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill qui transforme votre agent de codage en expert des firmwares de…
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) - Boucle de session orientée voix pour DeepSeek Harness : un bouton de microphone…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horaires de prière, date hégirienne, adhkar, ayah quotidienne, jeûne sunnah…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuration personnelle Claude Code versionnée dans ~/.claude — agents…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — plugin DeepSeek Harness pour les sujets de recherche…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - Couche d.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Collection de plugins pour Claude Code, pi et DeepSeek Harness : HUD de barre…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Portable Claude Code toolkit for .NET DDD/Clean Architecture: strict TDD…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Ligne d.
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuration globale portable de Claude Code : compétences personnalisées…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods non officiels pour l.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins Claude Code que j.
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analysez l.
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Ligne d.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Un tableau visuel pour vos agents Claude Code : voyez les sessions, les…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Ligne d.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins et de skills Claude Code pour faciliter la création de…
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Ligne d.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gouvernance des tokens pour Claude Code : le meilleur modèle dirige…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visionneuse à panneaux divisés pour Claude Code dans Windows Terminal et tmux…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Micro-tableau de bord de 3 lignes pour le terminal Claude Code — modèle…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Dépôt de mods Awesome Media pour Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Réduisez les dépenses de Claude Code et de tokens Codex : achemine les…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Une ligne d.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Affichez la barre d.
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Ligne d.
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - la ligne d.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Usines logicielles définissables pour Claude Code sur herdr : graphes de…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Ligne d.
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Ligne d.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod.
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - Extension VS Code : progression des tâches Code Claude, ETA et quota de limite…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods pour Code Claude : volets en direct, jauges et plus encore, installables…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Ligne d.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Ligne d.
- [gvart/claude-config](https://github.com/gvart/claude-config) - Ma configuration Claude Code : mod agent-monitor, skills, agents et programme…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Barre d.
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Prévisualisez les images dans Claude Code : survolez une pastille sous une…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Ligne d.
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Configuration personnelle de Claude Code : permissions, statusline, serveurs MCP.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Ligne d&#x27;état Code de Claude avec des lignes de panneau d&#x27;agents.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS : configuration Claude Code portable — règles globales…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Affiche une barre d.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Suivez l.
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Barre d.
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook de ligne d.
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - statusline Code Claude avec installateur pour Linux et Git Bash sur Windows.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - plugins, compétences, mods claude et plus encore, faits maison et sans cage.
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Marketplace Claude Code de MSF Supply : mods sélectionnés et figés par commit.
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Ligne d.
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Ligne d.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — ligne d.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Surveillez l.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Compétences et mods pour Claude Code et Cowork — suivi de projet, document de…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Ligne d&#x27;état Code de Claude pour Windows (PowerShell) : barres d&#x27;utilisation…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Ligne d.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Config et mods Code Claude, avec un kit de composants partagé, un terrain de…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Garde-fous de gestion des risques de modèle pour Code Claude : 25 contrôles…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Structure de démarrage pour Claude Code : hooks, ligne d.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuration portable de Claude Code.
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Ligne d.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Config Code Claude portable : CLAUDE.md, settings, statusline, skills.
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ StatusLine multi-protocole universelle, auto-apprentissage du contexte et…
- [tylergraydev/cc-mods](https://github.com/tylergraydev/cc-mods) - Mods pour Code Claude : volets latéraux, lignes d.
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Suivez l.
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - Mes compétences, plugins et mods Claude Code (marketplace : vladdu).
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Synchronisation multi-machine de la configuration utilisateur de Claude Code…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Une ligne d.
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Une ligne d.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Détecteur de dégradation du contexte 2026 - Mémoire proactive d.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, sous-agents et lignes d.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Barre d.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods pour Claude Code : volets, bandes et compagnons fondés sur des hooks de…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Transférez des tâches entre vos sessions Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Ceci dans un serveur MCP pour contrôler MODS, l.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill Codex et Claude Code pour traduire les mods CK3 avec un LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods open source et autres extensions pour Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker : retrouvez ce que vous demandez encore et encore à Claude Code et…

</details>

<a id="dsh-cordis"></a>

## Écosystèmes de plugins DSH et Cordis

DeepSeek Harness et Cordis atteignent le même objectif par une autre voie : chez eux, le plugin est le mécanisme de mods ; un plugin y équivaut donc à un mod ici.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74439 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

🌊 L'agent harness original. Déployez des essaims intelligents multi-joueurs, coordonnez des workflows autonomes et créez des systèmes d'IA conversationnelle. Fonctionnalités : mémoire adaptative, intelligence à auto-apprentissage, fédération, intégration vectorielle RAG et prise en charge native de Claude Code / Codex / Hermes et de nombreux autres systèmes intégrés

<sub>🔧 Utilisé dans le code: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                          |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **74439**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐153127 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Faites de la rétro-ingénierie sur n’importe quoi avec des agents, du comportement des applications jusqu’aux binaires natifs.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **153127** |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100748 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

🎨 Meilleur plugin de conception pour DeepSeek Harness. L’alternative open source à Claude Design. 🖥️ Application de bureau privilégiant le local. 🖼️ Votre agent de programmation devient le moteur de conception : prototypes, pages d’atterrissage, tableaux de bord, diapositives, images et vidéos — fichiers réels, export HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode et plus de 20 CLI via BYOK.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **100748** |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82525 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Transformez n'importe quelle idée, plan ou base de code en un magnifique diagramme interactif. Une compétence d'agent pour Claude Code, Codex et plus encore.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **82525**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Un agent de programmation fiable pour les tâches complexes d’ingénierie logicielle.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Go                                                                                       |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **35769**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25532 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Distilly — Distillez leur manière de penser en Skills réutilisables pour tout Agent ou Bot. Anciennement Colleague Skill（原同事 Skill）.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **25532**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18516 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Une liste organisée de plugins pour DeepSeek Harness (dsh) · Liste精选 de plugins DeepSeek Harness

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **18516**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8667 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Écosystème d’agrégation de plugins Web DeepSeek Harness (DSH) · Tout est un plugin, distribué via l’atelier créatif ｜｜Écosystème d’agrégation de plugins Web DeepSeek Harness (DSH) · Tout est un plugin, distribué via l’atelier créatif

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8667**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6275 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Le marché de plugins dans DeepSeek Harness — parcourir, rechercher, installer en un clic · Marché visuel de plugins DSH

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **6275**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4461 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Le plugin TUI officiellement le plus recommandé par DSH — hautes performances, faible surcharge, adorable baleine pixelisée et interaction fluide à la souris. Installation en une commande via npm. / Plugin TUI officiellement recommandé en priorité par DSH, hautes performances et faible consommation, adorable baleine pixelisée, interaction fluide à la souris, installation en une commande via npm

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4461**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3680 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Le premier terminal virtuel au monde pour agents IA

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **3680**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3034 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Version de bureau Tauri de DeepSeek Harness | Installateur de seulement 8 Mo, aucune configuration d’environnement, plugins prédéfinis, Windows / macOS / Linux.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **3034**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1911 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Connectez des bots IM à DeepSeek Harness via un code QR ou des identifiants de bot (prise en charge de Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord et WhatsApp). Connectez des bots IM à DeepSeek Harness via un code QR ou des identifiants (9 canaux).

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1911**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1423 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Logiciel d’écriture de romans avec IA : organise les inspirations, les personnages, la construction de l’univers, les synopsis, la rédaction des chapitres, la relecture et la révision en un flux de travail contrôlable ; fournit des versions de bureau pour Windows/macOS, avec prise en charge des modèles locaux et en ligne. Logiciel d’écriture de romans avec IA : organise les inspirations, les personnages, la construction de l’univers, les synopsis, la rédaction des chapitres, la relecture et la révision en un flux de travail contrôlable. Fournit des applications de bureau pour Windows/macOS, une intégration d’Ollama et un aperçu du plugin DeepSeek Harness (DSH).

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1423**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1182 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Mémoire pour Claude Code, Codex, Cursor et 38 autres agents de codage, créée à partir de l’historique des sessions déjà présent sur votre disque. Recherche locale, MCP et hooks, sans LLM, un seul binaire Go.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Go                                                                                       |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1182**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wecode-ai/Wegent">wecode-ai/Wegent</a></b> · ⭐870 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plan, build, and deliver with an open-source, self-hostable AI workspace for coding, collaboration, and automation.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **870**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agent` · `ai` · `chatbot` · `claude-code` · `codex` · `dsh-plugin` · `wework`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wecode-ai--wegent/991765bc5aba6a3c.png" width="100%" alt="wecode-ai/Wegent screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **593**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **526**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐261 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin DSH (DeepSeek Harness) non officiel : utiliser les modèles web chat.deepseek.com comme fournisseur LLM - capture de connexion navigateur, résolution PoW, streaming SSE, appels d’outils basés sur le prompting.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **261**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

ACRYL - Agent Context Relay Yielding Lifecycles. Un espace de travail persistant, un contexte canonique, n’importe quel agent de codage.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **255**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-research-report">PerryLink/dsh-research-report</a></b> · ⭐214 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Moteur de rapports de recherche vérifiables pour DeepSeek Harness : registre de preuves adressé par le contenu (liaison affirmation-instantané, inviolable) plus rapports scellés versionnés avec verdicts de vérification par affirmation et un répertoire scellé par manifeste.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **214**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `audit` · `citation-verification` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/2a270ca82dba24d3.png" width="100%" alt="PerryLink/dsh-research-report screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/dafefe1b3e0cd96e.gif" width="100%" alt="PerryLink/dsh-research-report animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Interface de terminal de style Claude Code pour DeepSeek Harness, prenant en charge Windows, macOS et Linux, compatible avec les terminaux transparents, les thèmes VS Code et les couleurs personnalisées.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **197**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐194 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

🚀 Plugin d’accès distant multicanal et de protection de sécurité pour DeepSeek Harness | Connexion directe par scan QR sur le réseau local, tunnel public Cloudflare / autohébergé, conversations sur tout le cycle de vie via bots WeChat / QQ / Feishu / Telegram | Authentification de sécurité intégrée pour l’accès tous protocoles, protection anti-altération en arrière-plan et système de survie après sinistre

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **194**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin DeepSeek Harness pour la migration de sessions inter-préréglages avec prévisualisation. Les transferts à schéma fixe préservent l’état, l’intention du modèle source et les images non résolues ; la session d’origine reste intacte.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **165**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐144 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Thème de bureau Claude Code pour DeepSeek Harness｜Thème de bureau Claude Code conçu pour l’interface web GUI de DeepSeek Harness

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **144**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-memento">PerryLink/dsh-memento</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Mémoire intersessions bornée, en couches, soumise à approbation et auditable pour DeepSeek Harness : une jointure de capacité ctx.memory avec un fournisseur SQLite sans dépendance, un outil de mémoire et une injection d’instantané figé. Statut de maintenance : FIGÉ depuis le 2026-10-05.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **141**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agent-memory` · `ai-agent` · `ai-agents` · `approval` · `audit` · `cordis` · `deepseek-harness` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/f63bd5eb5a8052b8.png" width="100%" alt="PerryLink/dsh-memento screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/0ce3328d348abdce.gif" width="100%" alt="PerryLink/dsh-memento animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐140 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

L’installation inclut 27 compétences d’ingénierie et de productivité de mattpocock/skills v1.3.1, sans qu’il soit nécessaire d’installer manuellement les compétences. Ce plugin, conçu avec 40 milliards de tokens, offre une efficacité de développement multipliée par 10 par rapport aux compétences d’origine et aide également les débutants à prendre plus rapidement en main cette suite de compétences. Prise en charge complète des issues GitHub ; Markdown est en version d’aperçu ; GitLab n’est pas encore pris en charge. Merci pour votre utilisation et votre soutien💗

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **140**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-permission-rules">PerryLink/dsh-permission-rules</a></b> · ⭐122 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Règles d’autorisation déclaratives de style Claude Code pour DeepSeek Harness : règles allow/deny/ask ordonnées avec correspondance par nom d’outil, argument (glob/regex) et chemin d’espace de travail dans la cascade tools/pre-execute, audit du journal de session et rechargement HMR.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **122**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `ai-safety` · `allow-deny-ask` · `approval` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/d950618f5f9cf382.png" width="100%" alt="PerryLink/dsh-permission-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/25c9ccd2f2133850.gif" width="100%" alt="PerryLink/dsh-permission-rules animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AskTheWay/dsh-auto-memory">AskTheWay/dsh-auto-memory</a></b> · ⭐106 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Claude Code-style auto-memory plugin for DeepSeek Harness (dsh): typed memory files + MEMORY.md index auto-injected into the system prompt. File-only, no external services.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **106**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agent-harness` · `agent-memory` · `ai-agent` · `ai-tools` · `auto-memory` · `claude-code` · `coding-agent` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/asktheway--dsh-auto-memory/1ff60db2b929f245.png" width="100%" alt="AskTheWay/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin DeepSeek Harness (DSH) : ✨ amélioration des prompts en un clic + 💬 reconnaissance vocale (arrêt automatique après la parole · double moteur cloud/local) · avec 🔁 redémarrage du service en un clic en cas d’anomalie

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **90**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Agent version bureau construit sur le socle central Deepseek-Harness. Hérite de toutes les capacités du socle. Et complète les fonctionnalités liées à l’IDE.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **69**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Marché qui classe, répertorie et vérifie automatiquement les plugins de la communauté DeepSeek-Harness. Classe, sélectionne et vérifie automatiquement les plugins du marché de la communauté DeepSeek-Harness.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **69**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-fund-research">PerryLink/dsh-fund-research</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Rapports de recherche déterministes pour les fonds communs publics chinois, sous forme de plugin DeepSeek Harness : un code de fonds en entrée, un rapport Markdown versionné en sortie, avec décomposition de performance, pénétration des positions, attribution de style et déclarations explicites de lacunes de données. Les métriques sont calculées dans le code, pas par le modèle.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **68**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `finance` · `fund-research`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/9a258f42b5375ed7.png" width="100%" alt="PerryLink/dsh-fund-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/c127c0b5eda50892.gif" width="100%" alt="PerryLink/dsh-fund-research animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐60 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin de thème Catppuccin pour l’interface Web de DeepSeek Harness : basculez en un clic entre les quatre thèmes Latte / Frappé / Macchiato / Mocha, avec un effet de verre (Glassmorphism) intégré et activable.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **60**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-13 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Protection avant exécution pour les agents de codage IA.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Une liste sélectionnée des meilleurs plugins IA remarquables pour les…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Marché de plugins DSH / DSH Plugin Marketplace : parcourez, installez et mettez…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、211个世界与上万素材、开局随心定制、世界自行运转、零漂移存档.
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - Articles mis à jour en continu sur le graphisme, 3DGS et l.
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins pour des logiciels qui itèrent sur eux-mêmes — le…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Communauté de plugins DeepSeek Harness — synchronisation automatique de…
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Le répertoire vivant des plugins DeepSeek Harness — actualisé toutes les…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana : DeepSeek Harness comme sous-agent pour HanaAgent.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Recherche de contexte d.
- [GDWhisper/dsh-web-startup-auth](https://github.com/GDWhisper/dsh-web-startup-auth) - Plugin de lancement Web distant + authentification par nom d.
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - Plugin DeepSeek Harness : profilage, nettoyage et vérification déterministes…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent est un FDE Harness open source pour agents de codage IA — à l.
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Alternative open source à GrokBot construite sur DeepSeek Harness.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Répertoire sélectionné de plugins DeepSeek Harness (DSH) — plus de 280 plugins…
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - Base de connaissances de développement de plugins DeepSeek Harness (dsh) : le…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT : système d.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH : shell Git Bash pour tous les modes d.
- [YRN-playmaker/dsh-wallpaper_share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - Plugin de synchronisation en un clic de divers fonds d.
- [AskTheWay/dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor) - ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Collection de plugins d.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin web DSH : statistiques d.
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - Classement et recommandations transparents de l.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vrai PowerPoint, pas du HTML. Indiquez à votre IA les sujets à couvrir et…
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - Synchronisation interappareils des sessions DeepSeek Harness : un miroir git…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Graphe de connaissances du code et harness de contexte local d.
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - Plugin web DSH : une arborescence hiérarchique d.
- [ddtcorex/govard](https://github.com/ddtcorex/govard) - Orchestrateur de développement local basé sur Go pour Magento, Laravel…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Transformez les modèles déjà connectés sur l.
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) - Traduction des paramètres de fournisseurs et réparation déterministe de JSON…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - Répertoire bilingue, maintenu en continu, de plugins pour DeepSeek Harness…
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - Notation qualité multidimensionnelle pour plugins DeepSeek Harness : note un…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Essais isolés d.
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Plugin dock de fonctionnalités DeepSeek Harness : un panneau unique…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Tests de compatibilité permanents pour les plugins DeepSeek Harness : versions…
- [liang-today/dsh-liangxiang](https://github.com/liang-today/dsh-liangxiang) - 众香成势，梁子显相。DeepSeek Harness 的 WebUI 插件，欢迎一起打梁.
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin hôte DeepSeek Harness qui conserve les documents du projet et la mémoire…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - Répertoire sélectionné et fondé sur des éléments probants de plugins DeepSeek…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayons X pour les plugins DeepSeek Harness : capacités déclarées comparées au…
- [ayingQAQ/dsh-web-launcher](https://github.com/ayingQAQ/dsh-web-launcher) - Windows 上的 DeepSeek Harness Web 一键启动器｜One-click launcher with background…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espace de travail multi-dossiers : permet à l.
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Exécution prise en charge par Podman pour DeepSeek Harness (dsh).
- [kelemiao/dsh-animation-optimization](https://github.com/kelemiao/dsh-animation-optimization) - Optimisation des animations DSH : plugin d.
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - Conversations vocales local-first pour DSH.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH : fenêtre d.
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - Mode créatif basé sur le mode PTC : plugin DSH, orchestration d.
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Kit de fonctionnalités de page pour DeepSeek Harness (dsh) : dock de terminal…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Donnez à l.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard de vérification sans dépendances pour les plugins DeepSeek Harness…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Écosystème de plugins DeepSeek Harness : 86 plugins open source dans une…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Marché de plugins DeepSeek Harness - parcourez, recherchez et installez les…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode sur DeepSeek Harness — plugin DSH qui permet à OpenCode Zen + Go…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins tiers et gestionnaire de cycle de vie…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx est un espace de travail de bureau extensible et centré sur l.
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Exécutez DeepSeek Harness sur ordinateur sans aucun coût en tokens — une…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - Espace de travail dsh Bots : plugin Cordis reliant la passerelle…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Famille de plugins d.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite communautaire de déploiement et d.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web DeepSeek Harness (DSH) : onglet latéral market-dashboard de suivi du…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Plugins et outils tiers indépendants pour DeepSeek Harness, maintenus par…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Utilisez les modèles gratuits d.
- [yangzhe1991/dsh-web-enhance](https://github.com/yangzhe1991/dsh-web-enhance) - Plugin d.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin DeepSeek Harness : transforme l.
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Échéances au niveau du déploiement pour les appels d.
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins Rust avec un noyau de cycle de vie vérifié par Verus et…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Plugin Cordis / DeepSeek Harness — outils GitHub API normalisés pour agents IA…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Tableau de bord Antigravity en ligne : tok/s, taux de succès du cache de style…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Arkme account, records, chat and interwoven-moments integration for DeepSeek…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Marché des plugins dsh - découverte automatique et synchronisation horaire à…

</details>

<a id="writing"></a>

## Articles, discussions et vidéos

Articles, discussions et vidéos consacrés aux fonctionnalités des mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Résumé

Bonjour HN, j’ai créé ceci pour moi-même et je voulais le publier en open source. Le problème : je voulais un moyen de recevoir des rappels entre les prompts, car je passe souvent de longues heures dans le terminal, surtout maintenant que nous traitons généralement autant d’agents en parallèle. La première version était un simple rep

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

##### 📝 Résumé

Aucune description en amont n’a été publiée.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

##### 📝 Résumé

J’ai créé ceci parce qu’avec les derniers modèles de codage, Claude passe en mode travail approfondi avec des commandes obscures, si bien que je ne sais plus ce qu’il fait. Il s’agit d’un mod (un plugin utilisant les nouveaux hooks de fonctions de Claude Code) qui trace une ligne au-dessus de l’invite : - l’étape actuelle,

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Articles, discussions et vidéos`                                               |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |

##### 📊 Données

| Indicateur          | Valeur     |
| ------------------- | ---------- |
| Première apparition | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Projets par langage d’implémentation

L’écosystème est concentré en Python et TypeScript, mais des clients typés apparaissent régulièrement dans d’autres langages. Ce tableau est généré à partir des entrées elles-mêmes.

| Langage    | Entrées | Exemples                                                                                                        |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| TypeScript | 378     | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                            |
| JavaScript | 78      | `fschmutz/claude-usage-panel`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`               |
| Python     | 40      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`   |
| Shell      | 26      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`             |
| HTML       | 15      | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                       |
| Rust       | 5       | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                                 |
| Go         | 4       | `mitre/claude-statusline`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                      |
| PowerShell | 3       | `Gabriel-Dalton/claude-statusline-tokens`, `markallisongit/claude-statusline`, `rainyfei/claude-statusline-win` |
| C          | 2       | `reporails/arcade`, `tylergraydev/cc-mods`                                                                      |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                         |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                            |
| Swift      | 1       | `peaceinitiativemenhadenoil263/claude-status-bar`                                                               |

<sub>Seules les entrées qui déclarent un langage sont comptabilisées. Les entrées de documentation et de discussion sont exclues de ce tableau.</sub>

## Contribuer

Les corrections sont les bienvenues et constituent le moyen le plus rapide d’améliorer cette liste. Ouvrez une issue ou une pull request si une entrée est mal classée, mal évaluée, ou si un projet a été exclu à tort en raison d’une homonymie — c’est la catégorie dans laquelle les filtres automatisés risquent le plus de se tromper.

---

<sub>Projet communautaire indépendant. Non affilié à Anthropic, qui ne l’a ni approuvé ni évalué. Claude Code, Claude et Anthropic sont des marques commerciales de Anthropic. Le comportement des produits peut changer sans préavis ; vérifiez tout élément critique dans la documentation officielle. Les ressources restent la propriété de leurs projets d’origine et ne sont reproduites que lorsque la licence l’autorise.</sub>

<sub>Dernière mise à jour · 2026-10-13T06:19:35+08:00</sub>
