<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Excellents mods Claude">
</p>

<h1 align="center">Excellents mods Claude</h1>

<p align="center"><b>L’index de Claude Code regroupant les mods et plugins évalués selon les preuves, ainsi que les comportements sous-jacents qu’ils modifient.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-607-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <b>Français</b> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Index en ligne** · Dernière synchronisation: `2026-10-16T17:05:57+08:00` (UTC+8)
> · Entrées: **607** · Ajoutées lors de la dernière mise à jour: **0** · Langages d’implémentation: **17**

<sub>Chaque entrée ci-dessous a été collectée, filtrée et revérifiée automatiquement. Aucun contenu présenté ici n’est sponsorisé.</sub>

<a id="featured"></a>

## Sélections du moment

<sub>Une entrée par catégorie, classée selon le niveau de preuve et le nombre d’étoiles, puis recalculée à chaque mise à jour. Il s’agit d’un classement, pas d’une recommandation ; chaque sélection renvoie à sa fiche complète ci-dessous. Les projets ayant publié une capture d’écran ou un enregistrement sont privilégiés, afin que le bandeau reste visuel.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9530 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2573 · Python · 👁️ observed</sub>
<sub>Trouvez les jetons fantômes. Corrigez-les. Survivez à la compaction. Évitez la dégradation de la qualité du contexte.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐75341 · TypeScript · 👁️ observed</sub>
<sub>🌊 L&#x27;agent harness original. Déployez des essaims intelligents multi-joueurs, coordonnez des workflows autonomes et créez des systèmes d&#x27;IA conversationnelle.…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐16 · 👁️ observed</sub>
</td>
</tr>
</table>

## Contenu

- [Ce qu’est un mod Claude Code](#ce-quest-un-mod-claude-code)
- [Comment les entrées sont évaluées](#comment-les-entrées-sont-évaluées)
- [Officiel : les propres dépôts et notes de version de Anthropic](#officiel--les-propres-dépôts-et-notes-de-version-de-anthropic) — **17**
- [Mods : conçus avec la capacité de mod](#mods--conçus-avec-la-capacité-de-mod) — **475**
- [Écosystèmes de plugins DSH et Cordis](#écosystèmes-de-plugins-dsh-et-cordis) — **105**
- [Articles, discussions et vidéos](#articles-discussions-et-vidéos) — **10**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151143 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Résumé

Claude Code est un outil de programmation agentique qui s'exécute dans votre terminal, comprend votre base de code et vous aide à coder plus rapidement en exécutant les tâches routinières, en expliquant le code complexe et en gérant les workflows git, le tout au moyen de commandes en langage naturel.

<sub>🔧 Utilisé dans le code: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                           |
| --------- | ---------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic` |
| Source    | `publié par Anthropic lui-même`                                  |
| Langage   | TypeScript                                                       |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **151143** |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9530 · TypeScript · ✅ official · 0 天</summary>

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
| Étoiles                       | **9530**   |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8290 · Python · ✅ official · 0 天</summary>

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
| Étoiles                       | **8290**   |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6398 · Python · ✅ official · 246 天</summary>

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
| Étoiles                       | **6398**   |
| Dernière mise à jour du dépôt | 2026-02-11 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

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
| Étoiles                       | **1813**   |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>Plus dans cette catégorie</b> <sub>· 5</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Ajout de `$.ui.notify` pour les mods : déclenche une notification native via…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Correction d.
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod.

</details>

<a id="mods"></a>

## Mods : conçus avec la capacité de mod

Every entry here shows evidence of using the capability Claude Code gained in 2.1.287: it draws through `ui.render`, owns a pane, band or card, reads `$.ui.selection()`, spawns teammates with `agent.spawn`, or says plainly that it is a mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2573 · Python · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Trouvez les jetons fantômes. Corrigez-les. Survivez à la compaction. Évitez la dégradation de la qualité du contexte.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | Python                                                                          |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **2573**   |
| Dernière mise à jour du dépôt | 2026-10-15 |
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
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐863 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Résumé

Custom Claude Code Mods that I need

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **863**    |
| Dernière mise à jour du dépôt | 2026-10-14 |
| Première apparition           | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐606 · JavaScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **606**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐260 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **260**    |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐218 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **218**    |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐208 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Mods for Claude Code. effortless picks the reasoning effort for every prompt and shows the cache countdown. textless shows art, quotes and chess instead of the wall of text while Claude works.

<sub>🔧 Utilisé dans le code: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | HTML                                                                            |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **208**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `ai-tools` · `anthropic` · `chess` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐196 · TypeScript · 👁️ observed · 11 天</summary>

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
| Étoiles                       | **196**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐154 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **154**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐115 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **115**    |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐108 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Résumé

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 Utilisé dans le code: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **108**    |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐95 · TypeScript · 👁️ observed · 3 天</summary>

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
| Étoiles                       | **95**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

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
| Étoiles                       | **80**     |
| Dernière mise à jour du dépôt | 2026-10-08 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Résumé

Mods Claude Code : barres de progression du plan en direct au-dessus de l'invite

<sub>🔧 Utilisé dans le code: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **54**     |
| Dernière mise à jour du dépôt | 2026-10-14 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>enregistrement animé · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐36 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **36**     |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **30**     |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **30**     |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Résumé

Mods Claude Code : menu Tools de Claude, mode Zen, thèmes de terminal, contrôles d’effort et de mode

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **24**     |
| Dernière mise à jour du dépôt | 2026-10-14 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 12 天</summary>

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
| Étoiles                       | **22**     |
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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐20 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **20**     |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐15 · TypeScript · 👁️ observed · 13 天</summary>

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
| Étoiles                       | **15**     |
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
<summary>🧩 <b><a href="https://github.com/rashedInt32/glass">rashedInt32/glass</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Une apparence d’application de bureau pour le transcript du terminal de Claude Code, sous forme de mod

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **15**     |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `markdown` · `syntax-highlighting` · `terminal-ui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/rashedint32--glass/c7b07954a39be0b7.png" width="100%" alt="rashedInt32/glass screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Résumé

LINE à l’intérieur de Claude Code : le TUI enil en tant que mod de Claude Code

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **15**     |
| Dernière mise à jour du dépôt | 2026-10-13 |
| Première apparition           | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Étoiles                       | **14**     |
| Dernière mise à jour du dépôt | 2026-10-03 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

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
| Étoiles                       | **12**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐11 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **11**     |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
| Étoiles                       | **10**     |
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Claude Code mods that keep context use, plan quota and per-turn cost on screen, plus a guard that stops a session once it goes over budget.

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
| Dernière mise à jour du dépôt | 2026-10-16 |
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
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 12 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary><b>Plus dans cette catégorie</b> <sub>· 441</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Collection de plus de 100 mods utilisables avec Claude Code.
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Mods Claude Code par Darrell Wang — bandes au-dessus de l.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mods Claude Code de Ray Amjad : volets, bandes, protections d.
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Skills, agents, commandes, règles, hooks et styles de sortie experts pour…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods Claude et outils pour les créer : un skill de construction, puis des mods.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quatre mods Claude Code : Cache Keeper, Recording Mode, Goal Meter et Collision…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Le harness Claude Code que j.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Donnez un nouveau toit à Claude Code avec Claude Mods : sans modifier le…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Compilation, tests, console et aperçus SwiftUI de Xcode dans Claude Code.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de connaissances Obsidian citant ses sources sur les mods de Claude Code…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods Claude Code de Learning Hacker : rendre le fonctionnement de l.
- [kakha13/claude](https://github.com/kakha13/claude) - Mods Claude Code qui corrigent et traduisent vos prompts avant que Claude ne…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panneau latéral Claude Desktop (onglet Code) : répertorie les tâches inachevées…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barre d.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods et skills Claude Code de Nekyia Labs, créés et utilisés quotidiennement…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un volet latéral pour Claude Code : les sous-agents exécutés par une session…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods Claude (plugins à hooks de fonction) pour Claude Code.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Carte d.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill qui apprend aux agents Claude Code à créer des mods Claude.
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Une file de décisions CLI/TUI pour les humains travaillant avec des agents…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins et skills communautaires pour Claude, installables depuis une…
- [davekiss/mods](https://github.com/davekiss/mods) - Mods Claude Code de Dave Kiss.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panneaux, garde-fous et mods améliorant le confort d.
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods Code Claude à la demande — une compétence qui lit votre conversation et…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galerie de mods Baselane : mods Claude Code, vérifiés et épinglés.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Un test de frappe pour patienter pendant que Claude travaille.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Une boutique d.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six mods Claude Code : limites de plan et contexte au-dessus du prompt, coach…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) pour Claude Code qui ajoute un panneau latéral avec les onglets…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod pour Claude Code qui affiche les diffs Edit et Write dans deux colonnes…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods Claude Code : panneau d.
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods pour Claude Code : plugins de hooks de fonctions qui ajoutent des panneaux…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods Claude Code : screen-guard masque les noms et les secrets pendant le…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods et skins pour Claude Code : barre de progression en direct pour les tâches…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensions Claude Code. Débloquez toute la puissance de Claude.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Deux mods Claude Code pour exécuter de nombreuses sessions simultanément : une…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Deux mods Claude Code au-dessus de la zone d.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace de mes propres mods pour Claude Code.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lit les fichiers markdown nommés par Claude Code, affichés à côté de la…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow pour Claude Code : une liste de contrôle claire au-dessus de…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods Claude Code : barre de contexte, panneau des agents, floutage PDPA.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code : miniatures des images collées au-dessus de l.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collègue vocal pour Claude Code. Discutez avec un loup en 3D propulsé par l.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods Claude Code : typing-speed, un compteur de vitesse de frappe en direct…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods pour Claude Code : volets, commandes et hooks créés avec le plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Découvrez les mods, plugins et extensions Claude Code grâce à des démos…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code : diagrammes Mermaid dessinés directement dans la transcription.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Petits mods Claude Code (plugins à hooks de fonction) : session-switcher et…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods Claude Code : mod-scout (trouver les mods que vous utiliseriez le plus)…
- [LudovicLaloux/agent-crew](https://github.com/LudovicLaloux/agent-crew) - Claude Code mod: see your parallel agents as costumed pixel-art Clawds, in a…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Boîte à outils Claude de Naren : skills, mods et serveurs MCP pour Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un ensemble de mods claude code créés par mes soins.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr : découvrir, inspecter, activer ou désactiver et mettre à jour les mods…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Meilleurs mods Claude Code : sélectionnés, validés et épinglés.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods Claude Code pour de vrais ingénieurs.
- [Coolkidlab-Yin/agent-mobile-control](https://github.com/Coolkidlab-Yin/agent-mobile-control) - Drive your local Claude Code and Codex sessions from your phone, as chat rooms.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code : routage automatique des modèles Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Six mods pour Claude Code : mascotte Clawd animée, barres de limite…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Élevez un œuf de thé qui marine lentement pendant que vous codez · Élevez un…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods open source pour Claude Code : panneaux, lignes d.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod Claude Code : répondez à Claude point par point, directement sur le texte.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods pour Claude Code : Clawd, une minuscule mascotte pixelisée qui met en…
- [reporails/arcade](https://github.com/reporails/arcade) - Jeux de bureau classiques sous forme de mods Claude Code, auxquels on joue dans…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods pour claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod Claude Code qui active ou désactive vos compétences, agents, règles et…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de Claude Code testés et installables en une commande : garde-fous pour…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Une liste organisée de mods de Claude Code, installables comme une marketplace…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Deux mods Claude Code : cache-keeper et ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods Claude Code qui gardent un agent honnête — des hooks de fonction qui…
- [yocloud-code/claude-vault](https://github.com/yocloud-code/claude-vault) - Claude Code mod: use database, server and cluster credentials without Claude…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Un mod pour Claude Code permettant de noter ses réflexions en cours de travail…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods Claude Code de Herman (marketplace herman-mods).
- [jrlprost/claude-code-mods](https://github.com/jrlprost/claude-code-mods) - Claude Code mods I build because I need them: context bar, plugin toggler, and…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Mod Code Claude : choisit le modèle et l.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin Claude Code (mod) qui donne à l.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Voyez ce que Claude Code exécute en arrière-plan : sous-agents, tâches Codex…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notes de terrain du premier jour sur les mods Claude Code sur Windows : une…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod pour Claude Code : compteurs en direct du coût, du contexte et du quota de…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin et mod de Claude Code : un SDLC natif de l.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Frappez Claude quand il se trompe — un mod de soulagement du stress pour…
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar and a status line for Claude Code: usage limits, context, model…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Apprenez une langue étrangère tout en travaillant avec Claude Code.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barre latérale en direct des coûts, tokens et de l.
- [CircularBlox/Clarity](https://github.com/CircularBlox/Clarity) - A clearer Claude Code terminal: boxed and organized you/claude conversations…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Un mod Claude Code qui conserve une liste évolutive des éléments ouverts d.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Voyez quels fichiers chaque agent de Claude Code a dans son contexte, et quelle…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Petits mods Claude Code pour le terminal et l.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI qui ajoute des mots espagnols aux réponses des agents.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Votre liste de tâches Floatee au-dessus du prompt de Claude Code : exécutez…
- [fredrikbonde/claude-context-bar](https://github.com/fredrikbonde/claude-context-bar) - Claude Code mod: context window as a stacked bar above the prompt.
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [gabriel9004/claude-code-mods](https://github.com/gabriel9004/claude-code-mods) - Mods para Claude Code: panel de agentes y tareas con cuota y caché, y banda de…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La fenêtre de contexte sous forme d.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Ne laissez pas votre attention vagabonder pendant que vous attendez la réponse…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuit et open source pour Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [markfulton/safe-keys](https://github.com/markfulton/safe-keys) - Paste an API key into Claude Code. Nothing keeps it.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Compétences de Claude Code : vérificateur de faits pour la documentation…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [reeny404/mod-hud](https://github.com/reeny404/mod-hud) - Claude Code mod: see which session is waiting on you at a glance, and hatch a…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks : un mod de Claude Code qui lit à voix haute, à la demande, les…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [tlq5l/afk-timer](https://github.com/tlq5l/afk-timer) - Claude Code mod: shows how long you.
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code : petits plugins pour les panneaux en direct, le routage…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod et plugin Claude Code : moniteur d.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Mods Claude Code : EMCC (Every Mod Claude Code), une collection sélectionnée et…
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [Abdoul-sudo/prompt-enhancer](https://github.com/Abdoul-sudo/prompt-enhancer) - Claude Code mod: rewrites vague prompts using the active project.
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [AJMarquez99/prompt-pin](https://github.com/AJMarquez99/prompt-pin) - Pin your latest prompt above the input and browse this session.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alanrsoares/claude-mods](https://github.com/alanrsoares/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un chat animé en braille au-dessus de l.
- [almost99/claudecode-mods](https://github.com/almost99/claudecode-mods) - Approved Claude Code Mods.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un chat pixel au-dessus de votre prompt Claude Code qui exécute un appel de…
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code qui choisit le bon moment pour compacter afin de garder…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods de Claude pour Claude Code : compteur de tokens.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods polyvalents pour Claude Code : bandes, volets, notifications et hooks.
- [androidZzT/cc-moyu-kit](https://github.com/androidZzT/cc-moyu-kit) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [AnnihilationWizard/secret-guard](https://github.com/AnnihilationWizard/secret-guard) - A Claude Code mod that adds a gitleaks pre-commit hook to each Git project you…
- [apiglue/claude-mods](https://github.com/apiglue/claude-mods) - Mods for Claude Code.
- [arjunkambj/claude-mods](https://github.com/arjunkambj/claude-mods) - Arjun.
- [Arkboi-GG/claude-mods](https://github.com/Arkboi-GG/claude-mods) - A small collection of Claude Code mods.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Vos limites d.
- [astromelon/takgon-mods](https://github.com/astromelon/takgon-mods) - 개인 Claude Code mods 플러그인(takgon-mods).
- [astrosteveo/nebula](https://github.com/astrosteveo/nebula) - Claude Code mods and plugins.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - De courtes séances d.
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [bardaxx/modsbook](https://github.com/bardaxx/modsbook) - A book of Claude Code mods: side panes, bands, status lines and hooks, each one…
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code mods: live panes, bands and guards that run inside Claude Code.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing pour Claude Code : Apple Music et Spotify au-dessus de…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [bharath-gp/ai-harness](https://github.com/bharath-gp/ai-harness) - Claude Code plugin marketplace: guardrails and cockpit mod bundles.
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods pour Claude Code : horloge du cache, rayon d.
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Simplement un hibou pour votre Claude Code.
- [chinayuren2022-2025/claude-english-coach](https://github.com/chinayuren2022-2025/claude-english-coach) - Claude Code mod: practise English by working with Claude in English only…
- [CladiusIV/claude-mods](https://github.com/CladiusIV/claude-mods) - A Claude Code plugin marketplace of mods: changes to Claude Code.
- [coil398/claude-session-brief](https://github.com/coil398/claude-session-brief) - Claude Code mod: session summary band, subagent and hook activity above the…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [davidyerm/claude-mods](https://github.com/davidyerm/claude-mods) - Mods for Claude Code.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [diegocamara89/claude-mods](https://github.com/diegocamara89/claude-mods) - Mods do Claude Code (function hooks): Sonnet por padrão para subagentes…
- [DimeDataCloud/open-ClaudeOS](https://github.com/DimeDataCloud/open-ClaudeOS) - Claude mods interactive operating system.
- [Djdhmf/clawd-office](https://github.com/Djdhmf/clawd-office) - A Claude Code mod: a living 8-bit office of Claude crabs in a side panel that…
- [Djdhmf/prompt-enhancer](https://github.com/Djdhmf/prompt-enhancer) - A Claude Code mod: a pixel-art librarian crab above your prompt that rewrites…
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [Elmanuel1/claude-mods](https://github.com/Elmanuel1/claude-mods) - Claude Code mods: docs-watch.
- [EslamHanafy/delegate-watch](https://github.com/EslamHanafy/delegate-watch) - Live Claude Code pane that shows what your delegated coding agents.
- [evertonalves-ai/mod-forge](https://github.com/evertonalves-ai/mod-forge) - Claude Code skill that builds, debugs, audits and packages Claude Code mods…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mods Code de Claude (plugins de hooks de fonctions) : session-meter et autres.
- [FunJim/claude-code-add-to-chat](https://github.com/FunJim/claude-code-add-to-chat) - Codex-style Add to chat for Claude Code: annotate any part of a reply, send all…
- [gnehiur/claude-code-volc-tts](https://github.com/gnehiur/claude-code-volc-tts) - Claude Code mod：用火山引擎豆包语音流式朗读 Claude 的最终回复（暂停/继续/倍速/缓存）.
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [gwarf/claude-plugins](https://github.com/gwarf/claude-plugins) - Claude Code mods by gwarf: a plugin marketplace.
- [gyoomun/claude-mods](https://github.com/gyoomun/claude-mods) - 다른 사람이 만든 Claude Code 모드를 내 작업 방식에 맞게 고친 것 (coach-on-call, next-steps-multi).
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [heidiks/agent-kit](https://github.com/heidiks/agent-kit) - Skills, plugins and Claude Code mods. Install only what you need.
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HikiJun97/claude-mods](https://github.com/HikiJun97/claude-mods) - Personal Claude Code mods.
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de code Claude : durée de chaque réponse, durée de réflexion de Claude et…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian.
- [ijat/prompt-polish](https://github.com/ijat/prompt-polish) - Claude Code mod that cleans up voice-dictated prompts and teaches the fix.
- [intent-driven-dev/claude-mods](https://github.com/intent-driven-dev/claude-mods) - Claude Code mods: live panes and hooks for everyday workflows.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [jambolo/claude-mods](https://github.com/jambolo/claude-mods) - Mods for Claude Code.
- [jasoncai0/claude-session-hud](https://github.com/jasoncai0/claude-session-hud) - Claude Code mod: rate-limit usage, Codeup MRs and the session.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panneau latéral d.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Liste des fichiers dans la barre latérale : fichiers créés, modifiés ou…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Un lapin hollandais nain bélier 8-bit (noir et blanc) court et bondit au-dessus…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - La barre latérale « ce que j.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Chronologie dans la barre latérale : où le temps de ce tour a été dépensé…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Échanges de tokens dans la barre latérale : combien de tokens la conversation…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Le petit mot honnête de claude code : après chaque tour, Claude murmure une…
- [jiroamato/claude-mods](https://github.com/jiroamato/claude-mods) - Jiro.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jonirafael/claude-code-mods](https://github.com/jonirafael/claude-code-mods) - Claude Code mods: context-receipt (per-turn context breakdown) and…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [Jsolee/claude-mods](https://github.com/Jsolee/claude-mods) - Mods de Claude Code de Joan Solé: comunitat, el panell dels subagents amb el…
- [jumpei-kurata/claude-mods](https://github.com/jumpei-kurata/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vit dans un bandeau au-dessus de votre prompt Claude Code : il met en…
- [kaisudo0520/cc-dashboard](https://github.com/kaisudo0520/cc-dashboard) - Live mission-control pane for Claude Code: Fable and Codex usage, branch review…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod qui lit les réponses et notifications de Claude Code à voix haute avec…
- [kargarisaac/subagents-tree](https://github.com/kargarisaac/subagents-tree) - Claude Code mod: a docked pane showing every subagent as a tree with model…
- [katipally/modz](https://github.com/katipally/modz) - Claude Code mods: install with /plugin install &lt;mod&gt; --marketplace…
- [keithwalsh/claude-code-mods](https://github.com/keithwalsh/claude-code-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [Krishna30396/Pixel-Progress](https://github.com/Krishna30396/Pixel-Progress) - A pixel progress bar with time left for Claude Code: tasks done, percent and…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high.
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [lperezmo/cache-caffeine](https://github.com/lperezmo/cache-caffeine) - Claude Code mod: keeps the prompt cache warm while you step away, and wakes…
- [lperezmo/session-relaunch](https://github.com/lperezmo/session-relaunch) - Claude Code mod: /relaunch reopens the current session in a new terminal tab so…
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Claude Code mod: guards the 1-hour prompt cache of idle sessions — countdown…
- [m-aoki1348125/next-compass](https://github.com/m-aoki1348125/next-compass) - Claude Code mod: four predicted next instructions in four directions, and a…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de code Claude qui affiche ce que fait Claude dans le sous-titre de…
- [macollins27/owner-rep](https://github.com/macollins27/owner-rep) - A Claude Code mod that watches the coding agent for the person who owns the…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude.
- [Marceux-Croix/Claudeopticon](https://github.com/Marceux-Croix/Claudeopticon) - A process monitoring and ticket system for Claude Code: your todo as a live…
- [Marensius-Andersen/auto-model](https://github.com/Marensius-Andersen/auto-model) - Claude Code mod: picks the cheapest model that fits each prompt.
- [marwansaab/Claude-Mods](https://github.com/marwansaab/Claude-Mods)
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods communautaires pour Claude Code : protections, volets et commandes qui…
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace.
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de code Claude qui réactive les outils todo pour les modèles qui les…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod Claude Code qui attend une pause sûre, puis transmet votre session ou la…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de code Claude : une ligne par tâche au-dessus du prompt avec la tâche…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jouez au Puissance 4 contre une IA dans Claude Code (/connect-four).
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de code Claude : lorsqu.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code mod pour les dépôts partagés par plusieurs agents IA : empêche les…
- [narley/sessions-sidebar](https://github.com/narley/sessions-sidebar) - Claude Code mod: a sidebar listing every Claude Code session, for Warp.
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un seul mod pour Claude Code, Windows et le CJK en priorité : aperçus d.
- [oklahaha/deepseek-balance](https://github.com/oklahaha/deepseek-balance) - Claude Code mod: DeepSeek balance gauge, today.
- [osinelnikov/activity-dashboard](https://github.com/osinelnikov/activity-dashboard) - Claude Code mod: live activity pane with time, tokens, agents, cost and PDF…
- [pappusinghadip/pappu-claude-mods](https://github.com/pappusinghadip/pappu-claude-mods)
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack : un mod Code Claude. Worktrees permanents avec un départ en lecture…
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [phatjam98/claude-mods](https://github.com/phatjam98/claude-mods) - Claude Code mods by phatjam98.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panneau latéral de statistiques de session en direct pour l.
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [poska-lab/cc-work-buddy](https://github.com/poska-lab/cc-work-buddy) - Unofficial Claude Code mod: a little Claude above your prompt that shows what…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [PurpleDotStudio/claude-mods](https://github.com/PurpleDotStudio/claude-mods) - Claude Code mods: a side panel for what the session needs from you.
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [r1305/claude-mods](https://github.com/r1305/claude-mods) - Mods para Claude Code: enrutado de modelos con dashboard de consumo y…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [reedchan7/claude-mods-pulse](https://github.com/reedchan7/claude-mods-pulse) - Pulse: live TTFT, tok/s, prompt-cache hit rate and usage left in Claude Code.
- [retogo/claude-media-view](https://github.com/retogo/claude-media-view) - A Claude Code mod that shows images and GIFs inline in the terminal — and lets…
- [revilo-digital/second-opinion](https://github.com/revilo-digital/second-opinion) - Claude Code mod: ask OpenAI, Gemini or Grok for a second opinion on Claude.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code : des pompes à faire pendant que Claude travaille. Aucun token.
- [Roberdinho/claude-mods](https://github.com/Roberdinho/claude-mods) - Claude Code mods: prompt-polaroid makes CodeSnap-style Polaroids of your prompts.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain : un guide de terrain des mods Code Claude, de ELI5 à l.
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [RuahTechSolutions/code-buddy](https://github.com/RuahTechSolutions/code-buddy) - Claude Code mod: staging guard, blast radius, edit replay and an agents panel…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code : transforme le plan que vous approuvez en mode plan en une…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Une liste soigneusement sélectionnée de mods Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode sans coût : les agents auxiliaires fonctionnent sur Haiku, et les gros…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Une bande-son lofi qui suit la session : calme, concentration, fluidité, ainsi…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Apprenez pendant que Claude code : après un tour ayant modifié le code, une…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Un enregistrement de chaque modification effectuée par Claude : rejouez chaque…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - A Claude Code mod: a project dashboard and isometric city map of tasks, agents…
- [schudarin/chudarin-context-mod](https://github.com/schudarin/chudarin-context-mod) - A Claude Code mod: a side panel that shows what fills your context, how much of…
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker.
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Marketplace de mods Claude Code personnalisés (cc-mods), avec des mods…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messages de commit en un clic pour Claude Code avec une Malenia en pixel art…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de code Claude qui affiche l.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Mods Claude Code non officiels par tanmen (marketplace : tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod Claude Code qui affiche la session actuelle dans un panneau : chaque…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins Claude Code de mods : des plugins function-hooks qui…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace.
- [timoranjes/agent-arcade](https://github.com/timoranjes/agent-arcade) - Playful live view of Claude and its subagents: animated dashboard, stats band…
- [tyler4400/tyler-claude-mods](https://github.com/tyler4400/tyler-claude-mods) - Claude Code plugins: status-card (会话状态卡片) &amp; session-title (智能自动标题) — Live…
- [UlongChaS2/learn-trail-mods](https://github.com/UlongChaS2/learn-trail-mods) - Claude Code mod: 설명의 목차를 패널에 띄우고 항목별 설명을 저장해 /recall 로 다시 본다.
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [user0027/claude-mods](https://github.com/user0027/claude-mods)
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code : barre de progression animée et résumé de complétion pour les…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trois petits mods Claude Code : voyez quand vos sous-agents auront terminé…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Dites « I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Posez à Claude une question annexe dans un panneau à côté de votre travail.
- [vdvoorder/filemap](https://github.com/vdvoorder/filemap) - A Claude Code mod that draws a git repository as a treemap in a side pane and…
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vmlinuz82/claude-mods](https://github.com/vmlinuz82/claude-mods) - Claude Code mods: a task checklist and a skill/MCP usage band, for the terminal…
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wonjangcloud9/wj-mods](https://github.com/wonjangcloud9/wj-mods) - Claude Code mods: cross-session work progress pane, usage band, long-turn…
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Claude Code mod 모음 (wonr-mods 마켓플레이스).
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Code Claude : vos limites d.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods pour Code Claude. agent-crew : surveillez le travail de vos sous-agents…
- [ya8282/claude-code-mods](https://github.com/ya8282/claude-code-mods) - Small productivity mods for Claude Code.
- [Yumbang/scopus-for-dobby](https://github.com/Yumbang/scopus-for-dobby) - Stateful CLI for searching, collecting, and managing academic papers from the…
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [zhuobichen/zhaowen-claudemod](https://github.com/zhuobichen/zhaowen-claudemod) - 我自用的 Claude Code mod 合集（function hooks）：以 marketplace 形式分发，/plugin install 装.
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
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Un tableau de bord statusline complet pour Claude Code — informations de…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon : suivez l.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills et mods publics pour Claude Code.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, sous-agents, hooks, commandes slash et guides pour Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs et agents de codage gratuits et légaux — auto-mis à jour, vérifiés…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill qui transforme votre agent de codage en expert des firmwares de…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horaires de prière, date hégirienne, adhkar, ayah quotidienne, jeûne sunnah…
- [LikeACloud7/awesome-frontier-ai-papers](https://github.com/LikeACloud7/awesome-frontier-ai-papers) - Daily tracker for frontier AI lab papers, model cards, system cards, and…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [romacv/claude-plan-usage-statusline](https://github.com/romacv/claude-plan-usage-statusline) - Claude Code status line showing model, usage limits, git info, and workspace…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Collection de plugins pour Claude Code, pi et DeepSeek Harness : HUD de barre…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Boîte à outils Claude Code portable pour l.
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuration globale portable de Claude Code : compétences personnalisées…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods non officiels pour l.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins Claude Code que j.
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Ligne d.
- [MindLab-Research/dsh-generative-ui](https://github.com/MindLab-Research/dsh-generative-ui) - Generative UI for DeepSeek Harness — the agent writes TSX and the web UI…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [wide3751/switchboard](https://github.com/wide3751/switchboard) - A Claude Code plugin (mod) that shows every local Claude Code session in one…
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins et de skills Claude Code pour faciliter la création de…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Dépôt de mods Awesome Media pour Claude Code.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
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
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - Personal Claude Code plugin marketplace (todo-pane).
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline Claude Code de qualité professionnelle : durée de session, coût…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - Les plugins Claude Code de divramod, une marketplace : skills d.
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Une ligne d.
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Two-row status line for Claude Code: context, rate limits with pace markers…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust.
- [federbenjamin/claude-statusline](https://github.com/federbenjamin/claude-statusline) - A two-line Claude Code status line showing branch, PR, model, context, cost…
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [itamartz/ClaudeCode-Mods](https://github.com/itamartz/ClaudeCode-Mods) - A Claude Code plugin marketplace of personal mods: hooks, panes and commands…
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [LemonYangZW/cc-mods](https://github.com/LemonYangZW/cc-mods) - Practical, low-distraction mods for Claude Code.
- [LiamMorganDev/claude-setup](https://github.com/LiamMorganDev/claude-setup) - My complete Claude Code setup: mods, skills, commands, hooks and CLAUDE.md…
- [lover40x/claude-browser-comment-mod](https://github.com/lover40x/claude-browser-comment-mod) - Claude Browser Comment Mod: click an element on your dev server, leave a…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [Monte9/claude-memory-mods](https://github.com/Monte9/claude-memory-mods) - Curate Claude Code&#x27;s own memory files: a pane to view every project&#x27;s memory…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [n0nuser/claude-statusline](https://github.com/n0nuser/claude-statusline) - 3-line status bar for Claude Code — model, context usage, cost, git status, and…
- [nhooey/claude-code-usage-statusline](https://github.com/nhooey/claude-code-usage-statusline) - A Claude Code status line and per-turn cost readout in one program: token…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [Recokioshi/claude-kit](https://github.com/Recokioshi/claude-kit) - a set of useful skills and mods for claude code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Ligne d.
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ StatusLine multi-protocole universelle, auto-apprentissage du contexte et…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Détecteur de dégradation du contexte 2026 - Mémoire proactive d.
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, sous-agents et lignes d.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods pour Claude Code : volets, bandes et compagnons fondés sur des hooks de…
- [ryanclark/statusline](https://github.com/ryanclark/statusline) - Simple status line for Claude Code showing context window/usage limits.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Transférez des tâches entre vos sessions Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker : retrouvez ce que vous demandez encore et encore à Claude Code et…
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Ceci dans un serveur MCP pour contrôler MODS, l.
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Bibliothèque de 3 compétences pour Claude Code : session-handoff…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill Codex et Claude Code pour traduire les mods CK3 avec un LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods open source et autres extensions pour Claude Code.
- [Grandullon/diariovida-mods](https://github.com/Grandullon/diariovida-mods) - Mods gratis para Claude Code: entiende lo que hace Claude, mejora tus prompts y…
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability.

</details>

<a id="dsh-cordis"></a>

## Écosystèmes de plugins DSH et Cordis

DeepSeek Harness et Cordis atteignent le même objectif par une autre voie : chez eux, le plugin est le mécanisme de mods ; un plugin y équivaut donc à un mod ici.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250780 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 Utilisé dans le code: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                          |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **250780** |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐75341 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **75341**  |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4651 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Le plugin TUI officiellement le plus recommandé par DSH — hautes performances, faible surcharge, adorable baleine pixelisée et interaction fluide à la souris. Installation en une commande via npm. / Plugin TUI officiellement recommandé en priorité par DSH, hautes performances et faible consommation, adorable baleine pixelisée, interaction fluide à la souris, installation en une commande via npm

<sub>🔧 Utilisé dans le code: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                          |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4651**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐725 · Python · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Une liste sélectionnée des meilleurs plugins IA remarquables pour les assistants IA, notamment Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi et bien d’autres. https://hol.org/plugins

<sub>🔧 Utilisé dans le code: `README.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                          |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | Python                                                                          |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **725**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐279847 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **279847** |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101429 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **101429** |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84234 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **84234**  |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/80b6efa0c1ca677d.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35817 · Go · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **35817**  |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐31033 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Une solution de bureau moderne conçue pour l’écosystème de plugins DeepSeek Harness (DSH). Tout est « plugin », le bureau lui-même est aussi un « plugin ».

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **31033**  |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25677 · Python · 🔎 inferred · 3 天</summary>

##### 📝 Résumé

Distilly — Distillez leur manière de penser en Skills réutilisables pour n’importe quel Agent ou Bot. Anciennement Colleague Skill（anciennement collègue Skill）.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **25677**  |
| Dernière mise à jour du dépôt | 2026-10-13 |
| Première apparition           | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐18533 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **18533**  |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/a67bb180136008be.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EverMind-AI/EverOS">EverMind-AI/EverOS</a></b> · ⭐13446 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **13446**  |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-memory` · `agentic-ai` · `ai` · `chats` · `clawdbot` · `clawdbot-skill` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/evermind-ai--everos/1c468e299d8b9fe7.png" width="100%" alt="EverMind-AI/EverOS screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8812 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Écosystème d’agrégation de plugins Web DeepSeek Harness (DSH) · Tout est un plugin, distribué via l’atelier créatif｜｜Écosystème d’agrégation de plugins Web DeepSeek Harness (DSH) · Tout est un plugin, distribué via l’atelier créatif

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8812**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/loopx-project/loopx">loopx-project/loopx</a></b> · ⭐6334 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

A control plane with a durable state kernel for long-horizon agents and teams. Keep work moving and improving across sessions, with less human attention.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **6334**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-control-plane` · `agent-harness` · `ai-agents` · `claude-code` · `codex` · `dsh-plugin` · `local-first` · `long-horizon-agents`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/8582e0735bb2d9e1.webp" width="100%" alt="loopx-project/loopx screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/34519ef8d110de64.gif" width="100%" alt="loopx-project/loopx animation"><br><sub>enregistrement animé · <a href="https://raw.githubusercontent.com/loopx-project/loopx/main/docs/assets/personal-workspace/loopx-dashboard-launch.mp4">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Q00/ouroboros">Q00/ouroboros</a></b> · ⭐6231 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **6231**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-os` · `agentic-ai` · `ai-agent` · `ai-coding-agent` · `claude-code` · `cli` · `codex` · `coding-agent`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/5b0b313f6f066fb8.png" width="100%" alt="Q00/ouroboros screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/099492564830e817.gif" width="100%" alt="Q00/ouroboros animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4275 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4275**   |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4206 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, side chat, Git, and sub-agent pages.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4206**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/5570cd36873fb95c.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>enregistrement animé · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3495 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Répondez-moi avec du HTML — une compétence d’agent qui répond aux questions difficiles avec une page HTML que vous pouvez réellement lire. Faites répondre l’AI Agent aux questions complexes sur une seule page HTML.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **3495**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3458 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Agent local, privé, open source et multiplateforme de découverte de contenu IA auto-évolutif : il vous comprend d’abord, puis recherche activement du contenu sur Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo et le Web ouvert. (prend en charge le plugin deepseek harness) | Agent multiplateforme open source de découverte de contenu IA, privilégiant l’exécution locale : il vous comprend, puis recherche activement du contenu sur Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo et le Web ouvert. (prise en charge du plugin deepseek harness)

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **3458**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3056 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **3056**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐2413 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **2413**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/T-Auto.png?size=160" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2185 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, agent teams, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板、浏览器、侧栏、命令，透视上下文组成、演进、压缩、多 Agent等。

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **2185**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐2039 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **2039**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1208 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Go                                                                                       |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1208**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/TencentCloudBase/CloudBase-AI-Toolkit">TencentCloudBase/CloudBase-AI-Toolkit</a></b> · ⭐1138 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Backend for AI coding agents on CloudBase — database, auth, functions via Plugin, Skills & MCP.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1138**   |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-skills` · `ai` · `aicoding` · `claude-code` · `cloudbase` · `cursor` · `database` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tencentcloudbase--cloudbase-ai-toolkit/9b9897d8b439ac14.png" width="100%" alt="TencentCloudBase/CloudBase-AI-Toolkit screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐709 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **709**    |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

📚 Bibliothèque de micro-leçons sans dépendance, adossée à git, permettant aux AI Agents de partager et de rechercher de manière asynchrone des expériences de débogage vérifiées. | https://misakanet.org

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
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zenstory-ai/oh-story-dsh">zenstory-ai/oh-story-dsh</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek 写网文/小说的工作流插件：DeepSeek Harness 社区插件，内置小说、短剧、游戏、视频解说四个工作台 | Community DeepSeek Harness plugin with novel, short-drama, game and video-recap workbenches.

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
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-skills` · `ai-agents` · `ai-novel-writing` · `ai-writing` · `claude-code` · `creative-writing` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zenstory-ai--oh-story-dsh/03bef6389f0bf9ba.gif" width="100%" alt="zenstory-ai/oh-story-dsh screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zenstory-ai--oh-story-dsh/03bef6389f0bf9ba.gif" width="100%" alt="zenstory-ai/oh-story-dsh animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐277 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **277**    |
| Dernière mise à jour du dépôt | 2026-10-15 |
| Première apparition           | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **256**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin de personnalisation / fonds d’écran / packs de thèmes DeepSeek Harness (dsh-plugin) — 8 thèmes Mirage, couleur d’accent par utilisateur, Wallpaper 2.0, importation, exportation et liens de partage de packs de thèmes, favoris et aléatoire, le tout implémenté avec un système de tokens entièrement natif.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **247**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dshplugin/dsh-plugin-hub">dshplugin/dsh-plugin-hub</a></b> · ⭐232 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 10000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、搜索、安装各类 AI 插件。

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **232**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent` · `ai` · `cli` · `community-plugins` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `dsh-plugin-org`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dshplugin--dsh-plugin-hub/7dd84080ee0003e9.png" width="100%" alt="dshplugin/dsh-plugin-hub screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐206 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin natif DeepSeek Harness (DSH) intégrant TypeSafe Jev ou une API de décision comme luna comme couche de décision System One pour la sélection, la supervision, les corrections et les approbations d’agents.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **206**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐199 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **199**    |
| Dernière mise à jour du dépôt | 2026-10-16 |
| Première apparition           | 2026-10-16 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 71</sub></summary>

- [cordiverse/cordis](https://github.com/cordiverse/cordis) - Méta-framework de composabilité spatiotemporelle.
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Une protection de pré-exécution pour agents de codage AI.
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [sixtysevenlf/dsh-blender-plugin](https://github.com/sixtysevenlf/dsh-blender-plugin) - DSH x Blender direct realtime plugin v2.0 — an AI drives Blender over a direct…
- [xiajiajun516/dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) - Plugin de sauvegarde et de restauration de DeepSeek Harness (DSH) — exportez…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Marché de plugins DSH / DSH Plugin Marketplace : parcourez, installez et mettez…
- [Nwflower/dsh-claude-style](https://github.com/Nwflower/dsh-claude-style) - Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的…
- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - DeepSeek Harness plugin for previewable cross-preset session migration.
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - L.
- [yannicksong0106/dsh-550c-boot](https://github.com/yannicksong0106/dsh-550c-boot) - 550C 开机动画 for DeepSeek Harness — 首帧由宿主半边注入，DSH 的 Loading 卡片不露脸；桌面原生标题栏按钮收编成终端配色…
- [drewnekota/cetus](https://github.com/drewnekota/cetus) - One macOS app for Claude Code, Codex, and every agent runtime you use…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins pour des logiciels qui itèrent sur eux-mêmes — le…
- [MichengAI/dsh-agency-agents](https://github.com/MichengAI/dsh-agency-agents) - DSH Agency Agents — 为 DeepSeek Harness 提供 321 名可召唤的专业智能体 · 321 summonable…
- [Sutera-Diffusus/dsh-whale-musume](https://github.com/Sutera-Diffusus/dsh-whale-musume) - Plugin animal de bureau DeepSeek Harness : une baleine pleine d.
- [Fishsb/dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) - DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启.
- [morluto/leantoken](https://github.com/morluto/leantoken) - Code intelligence for agents: find the code that matters and keep your context…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Agent version bureau construit sur le socle central Deepseek-Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Le répertoire vivant des plugins DeepSeek Harness — actualisé toutes les…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Recherche de contexte d.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Répertoire sélectionné de plugins DeepSeek Harness (DSH) — plus de 280 plugins…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Plugin DeepSeek Harness : associez en un clic le modèle à sa fenêtre de…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - Version Android de dsh : intègre DeepSeek Harness, un environnement d.
- [naodeng/dsh-qa](https://github.com/naodeng/dsh-qa) - dsh-qa · QA Workbench — A local software testing workbench plugin for DeepSeek…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Navigation des sessions DSH.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, outils, skills et ressources d.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vrai PowerPoint, pas du HTML. Indiquez à votre IA les sujets à couvrir et…
- [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) - Plugin DeepSeek Harness : transforme automatiquement les conversations en…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Registre de plugins, bundles et compétences DeepSeek Harness (dsh), basé sur…
- [Lenonss/DSH_VsCodeMode](https://github.com/Lenonss/DSH_VsCodeMode) - VSCode-style coding for DeepSeek Harness: Monaco editor (tabs/QuickOpen), agent…
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [qinyre/dsh-plugin-capabilities](https://github.com/qinyre/dsh-plugin-capabilities) - 在 dsh 设置页管理技能与 MCP 服务器，支持从 Claude Code、Codex 导入.
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [chengshenyangtai/dsh-workbuddy-trae-qoder-connect](https://github.com/chengshenyangtai/dsh-workbuddy-trae-qoder-connect) - 把 WorkBuddy（多账号/企业版）、Trae CN / TRAE SOLO CN、Qoder CN 三家订阅聚合进同一个 DSH…
- [OMSociety/dsh-ppt-maker](https://github.com/OMSociety/dsh-ppt-maker) - DSH 插件：内含 kimi-ppt 技能。创建 / 编辑 / 复刻 / 导出 PPT，DSH 内纯本地导出.
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - Liste organisée de plugins, outils, personnalisations et extensions pour…
- [bloodtmai-cmyk/dsh-ai-hub](https://github.com/bloodtmai-cmyk/dsh-ai-hub) - 面向企业内部 Harness 工作台的轻量控制面.
- [bloodtmai-cmyk/dsh-harness-enterprise](https://github.com/bloodtmai-cmyk/dsh-harness-enterprise) - 面向企业内部管控的 DeepSeek Harness 统一智能工作台入口.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayons X pour les plugins DeepSeek Harness : capacités déclarées contre…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH : fenêtre d.
- [Xiaofei-fei/dsh-prompt-history](https://github.com/Xiaofei-fei/dsh-prompt-history) - DSH web plugin: terminal-style composer — shell history.
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode sur DeepSeek Harness — plugin DSH qui permet à OpenCode Zen + Go…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Visualisez chaque action observable de l.
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - Le plugin DeepSeek Harness Personalization Settings sert à configurer le…
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh daemon: register the DeepSeek Harness web server (dsh web) as an…
- [duhu2000/qcc-mcp-oauth](https://github.com/duhu2000/qcc-mcp-oauth) - DeepSeek Harness 插件：一键 OAuth 授权连接企查查（Qichacha）MCP 服务 / One-click OAuth connect…
- [FeatherHunter/dsh-plugin-update](https://github.com/FeatherHunter/dsh-plugin-update) - 给 DSH 插件加「检查更新 / 安装更新」能力的 npm 包：宿主一段接线 + 面板一个现成组件，查新版、装更新、失败兜底、更新日志与多插件日志一次包掉.
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - Collection de plugins DSH : authentification par mot de passe + relation de…
- [higekibaka/dsh-vertex-argon](https://github.com/higekibaka/dsh-vertex-argon) - Vertex Argon — Google Vertex AI &amp; Gemini API dual-route Gemini 4 Argon plugin…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard de vérification sans dépendances pour les plugins DeepSeek Harness…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Permanently delete archived DeepSeek Harness sessions along with their on-disk…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web DeepSeek Harness (DSH) : onglet latéral market-dashboard de suivi du…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins tiers et gestionnaire de cycle de vie…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx est un espace de travail de bureau extensible et centré sur l.
- [DoveLi-Gu/dsh-showcase](https://github.com/DoveLi-Gu/dsh-showcase) - Local, verifiable delivery evidence reports and DSH plugin for coding-agent…
- [duhu2000/qcc-mcp-legal-oauth](https://github.com/duhu2000/qcc-mcp-legal-oauth) - DeepSeek Harness 插件：一键 OAuth 授权连接企查查法律数据 MCP（法律产品：法规/案例） / One-click OAuth…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入.
- [lemonmmice/dsh-agent-toolchain](https://github.com/lemonmmice/dsh-agent-toolchain) - Evidence over claims for coding agents: 55 DSH/MCP tools (23 read-only) that…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - 为 DeepSeek Harness 桌面版提供「限网段 + 可选数字密码」的远程访问入口.
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色：换装、白饭、摸头、问候、登录账户余额和本机今日用量预估.
- [smj-1680/dsh-plugin-liquid-glass](https://github.com/smj-1680/dsh-plugin-liquid-glass) - 适用于 DSH 桌面端的液态玻璃美化插件：输入框、消息气泡、侧栏与顶栏等主要界面元素改为液态玻璃材质，可搭配各类壁纸插件使用（需深色模式）.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin DeepSeek Harness : transforme l.
- [akkefa/deepseek-cordis](https://github.com/akkefa/deepseek-cordis) - Python plugin runtime targeting DeepSeek Harness vendored Cordis semantics.
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…

</details>

<a id="writing"></a>

## Articles, discussions et vidéos

Articles, discussions et vidéos consacrés aux fonctionnalités des mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐16 · 👁️ observed · 1 天</summary>

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
| Première apparition | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
| Première apparition | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| Première apparition | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 14 天</summary>

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
| Première apparition | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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

| Langage    | Entrées | Exemples                                                                                                      |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 375     | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 87      | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 47      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13      | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 10      | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 3       | `vulcanshen/ccdrawu`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                         |
| PowerShell | 2       | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| AutoHotkey | 1       | `keithwalsh/claude-code-mods`                                                                                 |
| C          | 1       | `reporails/arcade`                                                                                            |
| C#         | 1       | `DimeDataCloud/open-ClaudeOS`                                                                                 |
| Java       | 1       | `bloodtmai-cmyk/dsh-ai-hub`                                                                                   |
| Kotlin     | 1       | `dphmoblie/deepseek-harness-android`                                                                          |
| MDX        | 1       | `jkf87/mod-guide`                                                                                             |
| Ruby       | 1       | `romacv/claude-plan-usage-statusline`                                                                         |
| Swift      | 1       | `eovidiu/cordis-ios`                                                                                          |
| jq         | 1       | `n0nuser/claude-statusline`                                                                                   |

<sub>Seules les entrées qui déclarent un langage sont comptabilisées. Les entrées de documentation et de discussion sont exclues de ce tableau.</sub>

## Contribuer

Les corrections sont les bienvenues et constituent le moyen le plus rapide d’améliorer cette liste. Ouvrez une issue ou une pull request si une entrée est mal classée, mal évaluée, ou si un projet a été exclu à tort en raison d’une homonymie — c’est la catégorie dans laquelle les filtres automatisés risquent le plus de se tromper.

---

<sub>Projet communautaire indépendant. Non affilié à Anthropic, qui ne l’a ni approuvé ni évalué. Claude Code, Claude et Anthropic sont des marques commerciales de Anthropic. Le comportement des produits peut changer sans préavis ; vérifiez tout élément critique dans la documentation officielle. Les ressources restent la propriété de leurs projets d’origine et ne sont reproduites que lorsque la licence l’autorise.</sub>

<sub>Dernière mise à jour · 2026-10-16T17:05:57+08:00</sub>
