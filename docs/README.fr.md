<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Excellents mods Claude">
</p>

<h1 align="center">Excellents mods Claude</h1>

<p align="center"><b>L’index de Claude Code regroupant les mods et plugins évalués selon les preuves, ainsi que les comportements sous-jacents qu’ils modifient.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-534-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <b>Français</b> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Index en ligne** · Dernière synchronisation: `2026-10-11T23:26:48+08:00` (UTC+8)
> · Entrées: **534** · Ajoutées lors de la dernière mise à jour: **0** · Langages d’implémentation: **12**

<sub>Chaque entrée ci-dessous a été collectée, filtrée et revérifiée automatiquement. Aucun contenu présenté ici n’est sponsorisé.</sub>

<a id="featured"></a>

## Sélections du moment

<sub>Une entrée par catégorie, classée selon le niveau de preuve et le nombre d’étoiles, puis recalculée à chaque mise à jour. Il s’agit d’un classement, pas d’une recommandation ; chaque sélection renvoie à sa fiche complète ci-dessous. Les projets ayant publié une capture d’écran ou un enregistrement sont privilégiés, afin que le bandeau reste visuel.</sub>

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
<sub>Trouvez les jetons fantômes. Corrigez-les. Survivez à la compaction. Évitez la dégradation de la qualité du contexte.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74336 · TypeScript · 👁️ observed</sub>
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
- [Officiel : les propres dépôts et notes de version de Anthropic](#officiel--les-propres-dépôts-et-notes-de-version-de-anthropic) — **14**
- [Mods : conçus avec la capacité de mod](#mods--conçus-avec-la-capacité-de-mod) — **408**
- [Écosystèmes de plugins DSH et Cordis](#écosystèmes-de-plugins-dsh-et-cordis) — **101**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150172 · TypeScript · ✅ official · 0 天</summary>

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
| Étoiles                       | **150172** |
| Dernière mise à jour du dépôt | 2026-10-10 |
| Première apparition           | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9474 · TypeScript · ✅ official · 1 天</summary>

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
| Étoiles                       | **9474**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

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
| Étoiles                       | **8248**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

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
| Étoiles                       | **6342**   |
| Dernière mise à jour du dépôt | 2026-02-11 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

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
| Étoiles                       | **1797**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

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
<summary><b>Plus dans cette catégorie</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Ajout de `$.ui.notify` pour les mods : déclenche une notification native via…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Correction d.

</details>

<a id="mods"></a>

## Mods : conçus avec la capacité de mod

Every entry here shows evidence of using the capability Claude Code gained in 2.1.287: it draws through `ui.render`, owns a pane, band or card, reads `$.ui.selection()`, spawns teammates with `agent.spawn`, or says plainly that it is a mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **2534**   |
| Dernière mise à jour du dépôt | 2026-10-10 |
| Première apparition           | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐486 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Catalogue communautaire de mods publics Claude Code (hooks de fonctions), analysés depuis GitHub avec indication de ce que chaque mod peut lire, écrire, exécuter ou envoyer sur le réseau. Parcourir https://mods.aidojo.si/

<sub>🔧 Utilisé dans le code: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **486**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐338 · Python · 👁️ observed · 0 天</summary>

##### 📝 Résumé

macOS menu bar & Windows tray app pinning Claude Code, Codex, Antigravity & Grok CLI quota, burn rate, and cost to your screen. Local-first, no LLM API calls. HTML reports, 14 themes.

<sub>🔧 Utilisé dans le code: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | Python                                                                          |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **338**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐186 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Résumé

Claude Code mods: plugins built on hooks that add live lines above the prompt, guards, panes and games. Context bar, usage meter, Codex review watch, Markdown preview, Spotify now playing and more.

<sub>🔧 Utilisé dans le code: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **186**    |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐132 · TypeScript · 👁️ observed · 7 天</summary>

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
| Étoiles                       | **132**    |
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
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Un CLI QA natif pour les agents sur les pages Web. Déterministe, aucun test à écrire, aucun LLM.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | HTML                                                                            |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **104**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Skins pour Claude Code : lignes d'outils avec icônes, cartes de différences, de tableaux et de graphiques Mermaid, bande d'utilisation et quinze thèmes. /skin les remplace instantanément.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **96**     |
| Dernière mise à jour du dépôt | 2026-10-10 |
| Première apparition           | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Résumé

A collection of claude code mods

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **77**     |
| Dernière mise à jour du dépôt | 2026-10-08 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **75**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

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
| Étoiles                       | **66**     |
| Dernière mise à jour du dépôt | 2026-10-02 |
| Première apparition           | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Résumé

Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens. 台股／美股看板 + more to come.

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Résumé

Expert skills, agents, commands, rules, hooks & output styles for Claude Code — session continuity + modern CLI tooling for real-world dev workflows

<sub>🔧 Utilisé dans le code: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | Shell                                                                           |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **59**     |
| Dernière mise à jour du dépôt | 2026-10-07 |
| Première apparition           | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Résumé

Claude Code mods: live plan progress bars above the prompt

<sub>🔧 Utilisé dans le code: `README.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **46**     |
| Dernière mise à jour du dépôt | 2026-10-08 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>enregistrement animé · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐44 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Claude Code affiche des images et lit des vidéos directement dans votre terminal : captures d’écran, enregistrements Playwright et QA avant/après synchronisée. Ghostty & kitty.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **44**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
| Étoiles                       | **27**     |
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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

A pixel Pokémon that lives above the prompt in Claude Code

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
| Dernière mise à jour du dépôt | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **23**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Résumé

Xcode's build, tests, console and SwiftUI previews inside Claude Code

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Résumé

Claude Code mods: 21 styles and a full set of features you turn on when you need them, for the terminal and the desktop app. · 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Ten Claude Code mods, beginner guides, creation prompts, safe demos, and a build-your-own template.

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Claude Code mods: usage-band shows your 5h/7d limits, context window and cache hit rate above the prompt

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Résumé

Claude Code mods that make Claude's questions easier to read and answer (qa-guide).

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **11**     |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Ten open-source mods for Claude Code: live panes, bands, status lines and tool-call guards. Burn meter, launch codes, session wrapped, boss fight, code pet and more.

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Résumé

Two Claude Code mods: Codex computer-use bridge and coordinated Claude sessions. Source, build prompts, setup and tests.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **11**     |
| Dernière mise à jour du dépôt | 2026-10-05 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Résumé

A UI around your Claude Code and Codex terminals that your agents build, so the only model in your head is yours.

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
| Dernière mise à jour du dépôt | 2026-10-08 |
| Première apparition           | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Résumé

KOZMOS — live, visual mods for Claude Code (CLI + desktop): bands above the prompt, sidebars, status ticker, companions, guards and sound.

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

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
| Étoiles                       | **8**      |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Résumé

Six Claude Code mods in one plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) with per-mod switches, plus a mods-vs-hooks report.

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Résumé

개발동생의 Claude Code mods 모음. 택시 팩: 미터기, 내비, 과속 단속 카메라, 블랙박스

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **7**      |
| Dernière mise à jour du dépôt | 2026-10-04 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Regarder sur youtube.com</a> · la lecture s’ouvre sur le site hôte ; GitHub ne peut pas l’intégrer directement</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Résumé

Markdown, peint dans la boîte de prompt de Claude Code pendant la saisie. Le code délimité devient une carte avec coloration syntaxique avant même que vous ne fermiez la délimitation.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **7**      |
| Dernière mise à jour du dépôt | 2026-10-03 |
| Première apparition           | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Résumé

Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **7**      |
| Dernière mise à jour du dépôt | 2026-10-08 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 374</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Collection of 100+ mods you can use with Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods Claude et outils pour les créer : un skill de construction, puis des mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - The Claude Code harness I run every day, published under this name since day…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Four Claude Code mods: Cache Keeper, Recording Mode, Goal Meter, and Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods that fix and translate your prompts before Claude reads them.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Une apparence d.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un volet latéral pour Claude Code : les sous-agents exécutés par une session…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Source-cited Obsidian knowledge base about Claude Code mods: how they work, how…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panneau latéral Claude Desktop (onglet Code) : répertorie les tâches inachevées…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods and skills from Nekyia Labs, built and used daily by AIs…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill that teaches Claude Code agents to build Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barre d.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins et skills communautaires pour Claude, installables depuis une…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (function-hooks plugins) for Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - The Baselane mods gallery: Claude Code mods, checked and pinned.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Une file de décisions CLI/TUI pour les humains travaillant avec des agents…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Carte d.
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods pour Claude Code : plugins de hooks de fonctions qui ajoutent des panneaux…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard masks names and secrets while you screen-share;
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Tableau de bord GSD en direct pour Claude Code : roadmap, arbre d.
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Unlock the full power of Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) pour Claude Code qui ajoute un panneau latéral avec les onglets…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, guardrails and quality-of-life mods for Claude Code: context, usage…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Two Claude Code mods above the prompt box: context-window meter, 5-hour limit…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Make the Claude Pro plan last longer: Claude Code mods for an exact usage HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lit les fichiers markdown nommés par Claude Code, affichés à côté de la…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collègue vocal pour Claude Code. Discutez avec un loup en 3D propulsé par l.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, a live typing speedometer with per-prompt stats.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Feux d.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Discover Claude Code mods, plugins and extensions with animated demos, category…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod: mermaid diagrams drawn inline in the transcript.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Petits mods Claude Code (plugins à hooks de fonction) : session-switcher et…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: pasted image thumbnails above the prompt, in any terminal.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: Claude Tools menu, Zen mode, terminal themes, effort and mode…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Two Claude Code mods for running many sessions at once: a context card above…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: discover, inspect, toggle and update Claude Code mods.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Best Claude Code Mods: hand-picked, validated, pinned.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code : routage automatique des modèles Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Six mods pour Claude Code : mascotte Clawd animée, barres de limite…
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Modification de Claude Code permettant à Claude d.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - A marketplace of mods for Claude Code: a step debugger for the agent loop, git…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six mods Claude Code : limites de plan et contexte au-dessus du prompt, coach…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Le meilleur pack de mods tout-en-un pour Claude Code : limites d.
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Lisez des YouTube Shorts dans votre Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Boîte à outils Claude de Naren : skills, mods et serveurs MCP pour Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod pour Claude Code qui affiche les diffs Edit et Write dans deux colonnes…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods for Claude Code: Clawd, a tiny pixel mascot who acts out what Claude is…
- [reporails/arcade](https://github.com/reporails/arcade) - Classic desktop games as Claude Code mods, played in a pane while Claude works.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Une liste organisée de mods de Claude Code, installables comme une marketplace…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code très affirmé, conçu par un Rustacean passionné d.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code mods that keep an agent honest — function hooks that guard scope…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Un rappel d.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Tableau de bord macOS notch pour Claude Code : limites d.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della prompt cache, prossimi passi, bottoni rapidi e…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Modification de Claude Code : panneau en direct des PR GitHub qu.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code qui affiche vos limites d.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods: progress bars for plans, a ledger of what Claude left…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Un compagnon Naruto en pixel art pour Claude Code : 20 ninjas, 60 jutsu…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Voyez ce que Claude Code exécute en arrière-plan : sous-agents, tâches Codex…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notes de terrain du premier jour sur les mods Claude Code sur Windows : une…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod pour Claude Code : compteurs en direct du coût, du contexte et du quota de…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Un mod de Claude Code qui retient les déploiements de sous-agents, les invites…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods for claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod Claude Code qui active ou désactive vos compétences, agents, règles et…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins Claude Code (mods) : passez d.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de Claude Code testés et installables en une commande : garde-fous pour…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods for Claude Code: plugins built on function hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Générique de film pour votre session de codage.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - A bunch of claude code mods built by me.
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods Code Claude à la demande — une compétence qui lit votre conversation et…
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - A cliamp-backed YouTube player inside Claude Code (Claude Code mod).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude Code mods by vynnlee. One folder per mod, installable from one…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Apprenez une langue étrangère tout en travaillant avec Claude Code.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Modifications de Claude Code pour exécuter de nombreuses sessions sur de…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Lorsque l.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Coût, tokens et utilisation du contexte en direct dans la barre latérale de…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Modification de Claude Code : un backlog des suivis que Claude suggère dans…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio Internet dans Claude Code : barre latérale cliamp, mini-lecteur, favoris…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Modifications amusantes et utiles de Claude Code : une créature pixelisée…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude cuisine. Discutez avec votre équipe.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Mod Claude Code tout-en-un : HUD en direct, protections de sécurité.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Une bataille spatiale au-dessus du prompt de Claude Code pendant qu.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Voyez quels fichiers chaque agent de Claude Code a dans son contexte, et quelle…
- [dbroadhurst/claude-mod-todos](https://github.com/dbroadhurst/claude-mod-todos) - Claude Code mod: a pane summarising the remaining todos, with Do, Chat, Defer…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Gardez la tête froide. Un thermomètre pour vos journées Claude Code : chaque…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Cache de prompts, contexte et limites du plan visibles d.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Petits mods Claude Code pour le terminal et l.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod Claude Code : un panneau de progression pour les tâches, sous-agents…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Mod Claude Code : une table des matières cliquable et horodatée de toute la…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod Claude Code : limites de débit du plan, remplissage du contexte, coût de…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI qui ajoute des mots espagnols aux réponses des agents.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Your Alarum events above Claude Code.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Votre liste de tâches Floatee au-dessus du prompt de Claude Code : exécutez…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barre latérale au style d.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code qui le transforme en The Machine de Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow : mod Claude Code pour des workflows DAG obligatoires et vérifiés…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods open source pour Claude Code : panneaux, lignes d.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code : état de la session, progression Spec Kit en direct et…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La fenêtre de contexte sous forme d.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tâches en direct pour Claude Code Desktop : une barre au-dessus de…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuit et open source pour Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Stash prompts for later and pop them back into Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Modification de Claude Code qui affiche les images directement dans Ghostty et…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un mod Claude qui affiche les demandes de fusion GitHub de la session dans un…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod: generate sound effects from text prompts with a local Stable…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Compétences de Claude Code : vérificateur de faits pour la documentation…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod Claude Code : lignes de code du jour par Claude — nouvelles, modifiées…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod Claude Code : chemins cliquables dans les réponses — cliquez sur un dossier…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compagnon de Claude Code : un compagnon ASCII au-dessus de votre invite…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Modification de Claude Code : routage du modèle/de l.
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods : couche de sécurité pour Claude Code — masquage des secrets…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin et mod de Claude Code : un SDLC natif de l.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Collection Awesome de mods Claude Code | collection de mods 클로드 코드.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Un mod HUD de RPG chaleureux pour Claude Code.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks : un mod de Claude Code qui lit à voix haute, à la demande, les…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Donnez une fessée à Claude quand il se trompe — un mod anti-stress pour…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code : petits plugins pour les panneaux en direct, le routage…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod et plugin Claude Code : moniteur d.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods Claude Code. touch-map : voyez quels fichiers Claude a listés, lus…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod Code Claude qui indique en direct quels fichiers Claude a modifiés et…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods : cartes de statistiques de session au-dessus du prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un chat animé en braille au-dessus de l.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code : acheminez les tâches peu coûteuses vers GLM/Kimi via un…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un chat pixel au-dessus de votre prompt Claude Code qui exécute un appel de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code qui choisit le bon moment pour compacter afin de garder…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods de Claude pour Claude Code : compteur de tokens.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Place de marché de plugins Claude Code par anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - General-purpose mods for Claude Code: bands, panes, toasts and hooks.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Le navire LGTM Lines passe au loin après chaque modification du code — un mod…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Vos limites d.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - De courtes séances d.
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Progression du plan, des tâches et des agents à côté du prompt Claude Code — un…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un tableau d.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Un mod Claude Code : aperçu en direct de la fenêtre de contexte au-dessus de…
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Un mod pour Claude Code qui affiche le compte à rebours du cache de prompt dans…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing pour Claude Code : Apple Music et Spotify au-dessus de…
- [benlrice/logpane](https://github.com/benlrice/logpane) - Claude Code mod: a pane that tails the files your Bash calls write to.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods pour Claude Code : horloge du cache, rayon d.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Simplement un hibou pour votre Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Bande Claude Code sur une ligne.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Le moteur Doom original avec Freedoom, jouable dans Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Un mod Claude Code qui conserve une liste actualisée des éléments ouverts d.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Examinez chaque fichier modifié par Claude, comme dans une pull request, sans…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods Claude Code pour de vrais ingénieurs.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi qui vit dans Claude Code : il éclot, mange le code écrit par…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mods de Claude Code écrits comme des hooks de fonctions, et la marketplace qui…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code : après qu&#x27;un guard bloque un appel d&#x27;outil, il arrête les…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code : tâches en arrière-plan dans une seule vue, avec progression…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code : une seule boîte de réception pour les messages des…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code : explique les blocages du sandbox et transforme les blocages…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoris pour Claude Code : icônes en un clic pour vos commandes et skills.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hé, je l.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Mods de code : delete-guard (confirmer les suppressions de fichiers) et…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod de code Claude : utilisation de l.
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Mod pour Claude Code : vos agents d.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar en direct de vos branches parallèles et worktrees au-dessus de…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Un Claude Code mod pour capturer des réflexions en cours de travail, les trier…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+clic pour copier le lien sur chaque bloc de code dans les réponses de…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mods de code Claude (plugins function-hook), installés via un marketplace…
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code mods : context-bar-plus.
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Mod pour Claude Code : capturez vos idées dans la boîte de réception d.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de code Claude : durée de chaque réponse, durée de réflexion de Claude et…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mods de code Claude : streamer-mode masque les volets privés, les bandes et la…
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook plugins (mods).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod Claude Code : attend la fin de la limite d.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Un cockpit au-dessus de votre prompt Claude Code. Le canard lit les jauges.
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code mod: sidebar file tree that pulses on files Claude just edited.
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker : un mod pour Claude Code avec un panneau latéral indiquant où en…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Un mod de Claude Code : un panneau pour chaque sous-agent, les fichiers qu.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panneau latéral d.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Liste des fichiers dans la barre latérale : fichiers créés, modifiés ou…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Un lapin hollandais nain bélier 8-bit (noir et blanc) court et bondit au-dessus…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - La barre latérale « ce que j.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Chronologie dans la barre latérale : où le temps de ce tour a été dépensé…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Échanges de tokens dans la barre latérale : combien de tokens la conversation…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Le petit mot honnête de claude code : après chaque tour, Claude murmure une…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Petits mods pour Claude Code, comme de nouvelles commandes slash et des…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vit dans un bandeau au-dessus de votre prompt Claude Code : il met en…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod qui lit à voix haute les réponses et notifications de Claude Code avec…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod Claude pour lire et rejoindre les conversations entre vos sessions…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods pour Claude Code. PixBar : une créature pixelisée au-dessus de votre…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Mod Claude Code : sous-agents en cours d.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Mods de code Claude (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Deux mods de Claude Code : folio, un panneau de fichiers à côté du chat, et…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph : un graphique en direct de ce que Claude Code sait.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Ne laissez pas votre attention vagabonder pendant que vous attendez la réponse…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guide des mods de code Claude sélectionnés par la communauté : cas…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de code Claude qui affiche ce que fait Claude dans le sous-titre de…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Un adorable chat noir au-dessus de votre invite Claude Code.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod de Claude Code avec des profils d.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods communautaires pour Claude Code : protections, panneaux et commandes qui…
- [merrickxxx/grill-pane](https://github.com/merrickxxx/grill-pane) - Claude Code mod: grilling interviews with clickable answers in a side pane.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Volet latéral pour Claude Code : fichiers écrits par Claude, divisions du…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Mod pour Claude Code : projette ce qu.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un panneau latéral discret pour Claude Code : ce que fait cette session, son…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Une heure discrète au-dessus de chaque invite et de chaque réponse dans la…
- [mmedum/spor](https://github.com/mmedum/spor) - Restaure ce que Claude Code replie : les fichiers lus par Claude, les commandes…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code mod : utilisation de la fenêtre de contexte dans l.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de code Claude qui réactive les outils todo pour les modèles qui les…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod that waits for a safe pause, then hands your session over or…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de code Claude : une ligne par tâche au-dessus du prompt avec la tâche…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jouez au Puissance 4 contre une IA dans Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de code Claude : lorsqu.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code mod pour les dépôts partagés par plusieurs agents IA : empêche les…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Marketplace de mods pour Claude Code.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Fun, free mods for Claude Code that never spend a token.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Un garde-fou pour le SQL dans Claude Code : demande confirmation avant que…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un seul mod pour Claude Code, Windows et le CJK en priorité : aperçus d.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Les meilleurs Mods de Claude Code, classés selon ce qu.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Deux Mods Claude pour Claude Code : garde-corps.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Jurez contre Claude Code et une main de dessin animé vous répond d.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panneau latéral de statistiques de session en temps réel pour l.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods pour Claude Code : safety-guard bloque les commandes destructrices et…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod Claude Code : ticker boursier en direct, volet /quote, alertes de prix…
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code mod: a band above the prompt showing context used and a countdown…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code mod: a side pane that pins every diagram Claude draws and keeps a…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code mod: a dreaming pass that merges, rewrites and prunes Claude.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Mod pour Claude Code : maintient auto-memory à jour en arrière-plan après…
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code mod: drops vague prompts before Claude sees them, and suggests the…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod Claude Code : hôte SSH, RAM et limites d.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code : des pompes à faire pendant que Claude travaille. Aucun token.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods for claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code : transforme le plan que vous approuvez en mode plan en une…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Une liste soigneusement sélectionnée de mods Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode sans coût : les agents auxiliaires fonctionnent sur Haiku, et les gros…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Une bande-son lofi qui suit la session : calme, concentration, fluidité, ainsi…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Apprenez pendant que Claude code : après un tour ayant modifié le code, une…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Un enregistrement de chaque modification effectuée par Claude : rejouez chaque…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - Un mod pour claude code qui permet de basculer entre les comptes.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Chaque lien mentionné par votre session, sur une seule ligne au-dessus de…
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Démonstration minimale des function hooks de Claude Code : panneau en temps…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis : un mod de fans non officiel des Avengers pour Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod Claude Code pour le contexte, la croissance, le quota, le cache, le coût…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Mod Code Claude : achemine les requêtes simples et les sous-agents vers des…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - Le DOOM original dans un panneau Claude Code, sans rien à installer : le moteur…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messages de commit en un clic pour Claude Code avec une Malenia en pixel art…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de code Claude qui affiche l.
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - Un mod pour Claude Code qui choisit le modèle et l.
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Small mods that change how Claude Code looks and sounds.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod Claude Code qui affiche la session actuelle dans un panneau : chaque…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins Claude Code de mods : des plugins function-hooks qui…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod: rewrites a rough prompt in place, naming fitting skills, open…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Personnalisations pour Claude Code.
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code : quota 5h/7d, fenêtre de contexte, temps restant du cache…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code : barre de progression animée et résumé de complétion pour les…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trois petits mods Claude Code : voyez quand vos sous-agents auront terminé…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Réduit la taille des grandes captures d.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Dites « I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Affiche des prompts suivants suggérés au-dessus de la zone de prompt.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Posez à Claude une question annexe dans un panneau à côté de votre travail.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace de mods pour Claude Code avec installation en une étape et guide…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Compte à rebours des limites de débit et prévision du taux de consommation pour…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods para o Claude Code: faixa de limites de uso (5h/semanal) e painel de…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Code Claude : vos limites d.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods pour Code Claude. agent-crew : surveillez le travail de vos sous-agents…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Affichez des formules mathématiques LaTeX en ligne et en mode affichage, ainsi…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Un tableau de tâches en direct pour Claude Code : planifiez avant de…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Une collection soigneusement sélectionnée des meilleures ressources pour les…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin Claude Code qui montre ce qui se passe - utilisation du contexte…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Ligne d.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Toutes les parties du prompt système de Claude Code, les 27 descriptions…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Plus de 45 conseils pour tirer le meilleur parti de Claude Code, des bases aux…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline élégant de style vim pour Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Examinez le diff de votre agent de programmation dans un panneau de terminal et…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de ligne d.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Build mods for Claude Code: Hook any request, modify any response, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - A comprehensive statusline dashboard for Claude Code — session info, quota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: track the carbon footprint of your Claude Code sessions.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - An aesthetic statusline for Claude Code by awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agent de jeu de rôle longue durée pour DeepSeek Harness (plugin de taverne DSH)…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Public Claude Code skills and mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash commands and guides for Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legal free LLM APIs &amp; coding agents — self-updating, probe-verified twice a…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Calculateur de coûts rapide et sans dépendances, avec ligne d.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Ligne d.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Scores, calendriers et classements de football en direct pour les…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plan de contrôle local pour Claude Code sur Windows et macOS : changez de…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill that turns your coding agent into a keyboard firmware expert.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuration personnelle Claude Code versionnée dans ~/.claude — agents…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horaires de prière, date hégirienne, adhkar, ayah quotidienne, jeûne sunnah…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Image generation &amp; visual processing suite for DeepSeek Harness: pluggable…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Barre d.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Carte flottante des périodes de pointe et de faible activité pour DeepSeek…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Boîte à outils Claude Code portable pour l.
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuration globale portable de Claude Code : compétences personnalisées…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins Claude Code que j.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, a Tamagotchi companion mod for Claude Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace for Claude Code Plugins and Skills to facilitate mods of the game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gouvernance des tokens pour Claude Code : le meilleur modèle dirige…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Ligne d.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository for Claude Code Awesome Media mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Réduisez les dépenses de tokens de Claude Code et Codex : achemine les…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Configuration simple et utile de la ligne d.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Alertes de limites d.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Affichez la barre d.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Ligne d.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Ligne d.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Tableau de bord d.
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Une ligne d.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Affichez les informations d.
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Ligne d.
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Ligne d.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Équipes d.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Modules complémentaires Claude Code : observateur de point coloré de statut…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Ligne d.
- [alexleveled/claude-read-aloud](https://github.com/alexleveled/claude-read-aloud) - Hear Claude Code.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Ligne d.
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Une ligne d.
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Mod HUD CRT Claude : un panneau d.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins Code Claude avec baloo : compétences, agent qui vérifie…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Ligne d.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Ligne d.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Une ligne d.
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin Code Claude qui affiche magnifiquement les diagrammes Mermaid dans la…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Outils, compétences et agents pour Code Claude — à commencer par une ligne…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Barre d.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Dépenses DeepSeek réelles de API pour Code Claude : recalcule le prix des…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Prévisualisez les images dans Claude Code : survolez une pastille sous une…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Ligne d.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronisez les tâches de Claude avec Fizzy.do pour une visibilité d.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu des paramètres, ligne d.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Suivez l.
- [msetsma/claude-style](https://github.com/msetsma/claude-style) - Claude Code style mod: prompt bubbles, tool-call cards and rails, framed bands…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Installateur d.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Ligne d.
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugins et mods Code Claude pour comprendre ce que fait Claude : formats de…
- [pbhwheeler/claude-config](https://github.com/pbhwheeler/claude-config) - Portable Claude Code config: settings.json, hooks, status line, and a bootstrap…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Barre d.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Ligne d.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuration portable de Claude Code.
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Un petit tableau de bord pour Claude Code : pourcentage de contexte, compte à…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Barre d.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuration Claude Code portable : CLAUDE.md, paramètres, ligne d.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Mod Desktop Code Claude (macOS) : notifications de session permettant d.
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Mod compagnon de lecteur d.
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Exploration pratique et vérifiée de Claude Code — CLAUDE.md, sous-agents…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Suivi des coûts en temps réel et ligne d.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Compétence Claude Code (VS Code, Windows) : aperçus d.
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Une ligne d.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Détecteur de dégradation du contexte 2026 - Mémoire proactive d.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, sous-agents et lignes d.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Un constructeur visuel de barres d.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Barre d.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods for Claude Code: panes, bands and buddies built on function hooks.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pass tasks between your Claude Code sessions.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - This in a MCP server to control MODS, the modular cross platforms tool for…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex and Claude Code skill for translating CK3 mods with a local LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods and other extensions for Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Barre d.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: find what you ask Claude Code again and again, and turn it into a…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## Écosystèmes de plugins DSH et Cordis

DeepSeek Harness et Cordis atteignent le même objectif par une autre voie : chez eux, le plugin est le mécanisme de mods ; un plugin y équivaut donc à un mod ici.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74336 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **74336**  |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100521 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **100521** |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐91711 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **91711**  |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81929 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **81929**  |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **35760**  |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25495 · Python · 🔎 inferred · 19 天</summary>

##### 📝 Résumé

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **25495**  |
| Dernière mise à jour du dépôt | 2026-09-22 |
| Première apparition           | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18380 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **18380**  |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8629 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Écosystème d'agrégation de plugins web DeepSeek Harness (DSH) · Tout est un plugin, distribué via l'atelier créatif｜｜Écosystème d'agrégation de plugins web DeepSeek Harness (DSH) · Tout est un plugin, distribué via l'atelier créatif

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8629**   |
| Dernière mise à jour du dépôt | 2026-10-10 |
| Première apparition           | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐8510 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **8510**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/212e73dc2aecbd46.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6159 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Le marché de plugins dans DeepSeek Harness — parcourir, rechercher, installer en un clic · marché visuel de plugins DSH

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **6159**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4486 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness（DSH）une petite baleine qui vit dans le coin inférieur droit de l’interface DSH et vous aide à surveiller le solde de votre compte DeepSeek. Toute douce et rebondissante, elle prend en charge le glisser-déposer avec aimantation, l’inversion lors de l’aimantation à gauche et l’animation de défilement des chiffres. Elle s’active automatiquement avec l’interface ; il est recommandé d’appeler directement votre installation dsh.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4486**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4286 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Le plugin TUI officiellement recommandé en priorité par DSH — hautes performances, faible surcharge, adorable baleine pixelisée, interaction fluide avec la souris. Installation en une commande via npm. / Plugin TUI officiellement recommandé en priorité par DSH : hautes performances, faible consommation de ressources, adorable baleine pixelisée, interaction fluide avec la souris, installation en une commande via npm

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4286**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4107 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **4107**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>enregistrement animé · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3119 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness Tauri 桌面版 | Installateur de seulement 8 Mo, configuration d’environnement nulle, plugins prédéfinis, Windows / macOS / Linux.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **3119**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1406 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Logiciel d’écriture de romans par IA : organise inspirations, personnages, construction d’univers, plans, rédaction de chapitres, relecture et révision dans un flux de travail contrôlable ; propose des versions bureau Windows/macOS, prend en charge les modèles locaux et en ligne. Logiciel d’écriture de romans par IA : organise les inspirations, les personnages, le worldbuilding, les plans, la rédaction de chapitres, la relecture et la révision dans un flux de travail contrôlable. Comprend des applications bureau pour Windows/macOS, l’intégration Ollama et un aperçu du plugin DeepSeek Harness (DSH).

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1406**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **1171**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Client de bureau DeepSeek Harness (dsh) Windows — Node.js intégré + dsh CLI, lancement en un clic

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **704**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
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
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐334 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **334**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐284 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Ouvrez simplement votre navigateur — accomplissez tout votre travail.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **284**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

ACRYL - Agent Context Relay Yielding Lifecycles. Un espace de travail persistant, un contexte canonique, n’importe quel agent de programmation.

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
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin DeepSeek Harness (DSH) natif intégrant TypeSafe Jev ou une API Decision comme luna comme couche de décision System One pour la sélection, la supervision, les corrections et les approbations des agents.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **203**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Délégation de tâches différée pour DeepSeek Harness (dsh) : planifiez vos tâches quand vous le souhaitez, elles s’exécutent sans surveillance pendant les heures creuses, puis revenez consulter un rapport. Arbitrage humain, ordinateur de bureau + Web.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **170**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin DeepSeek Harness pour la migration inter-préréglages de sessions avec prévisualisation. Les transferts à schéma fixe préservent l'état, l'intention du modèle source et les images non résolues ; la session d'origine reste inchangée.

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
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐133 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Des preuves d’exécution qui aident les agents à tracer, profiler et réduire les points chauds dans le code applicatif et natif, les noyaux GPU et les piles d’inférence.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **133**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐132 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Thème Claude Code Desktop pour DeepSeek Harness｜Thème de bureau Claude Code conçu pour l'interface GUI Web de DeepSeek Harness

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **132**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin de compagnon de bureau DeepSeek Harness : la fille baleine pleine d’énergie vous accompagne pendant que vous codez 🐋 Compatible avec DSH Desktop 0.2.0-rc.2 et l’ancienne version Web (desktop pet / mascot, local-first)

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **120**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin DSH · Optimiseur par injection 0.8 (branche principale) : vous parlez comme d’habitude ; après votre envoi et avant la réception par l’IA, il clarifie « ce qui est réellement demandé cette fois », puis transmet cette compréhension à l’IA de travail (injection de contexte) — les propos originaux ne sont pas réécrits et chaque élément est accompagné de sa justification mot à mot. Comprend une interface de contrôle (niveau/permissions/modèle/contexte/outils en lecture seule), une couche flottante d’interception (couche de réflexion + couche de production) et l’utilisation réelle des tokens. Peut améliorer nettement la stabilité des performances de la plupart des modèles, en particulier DeepSeek-V4.1-Flash, avec des gains significatifs possibles

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **113**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/JingbiaoMei/Tokdash">JingbiaoMei/Tokdash</a></b> · ⭐85 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Agent Dashboard: Visualization and analytics for Sessions and Quota Usage. Track, analyze, and optimize token usage across providers with heatmaps, cost tracking, token counting and quota resets..

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Python                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **85**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `agent` · `analytics` · `anthropic` · `claude-code` · `claude-code-plugin` · `codex` · `codex-cli` · `dashboard`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jingbiaomei--tokdash/cb7e85100dfe6e93.png" width="100%" alt="JingbiaoMei/Tokdash screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐66 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **66**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Le répertoire vivant des plugins DeepSeek Harness — actualisé toutes les heures, testé quotidiennement pour la compatibilité, avec une boutique de plugins intégrée et un générateur. Répertoire vivant des plugins DSH : actualisation horaire, tests quotidiens de compatibilité, boutique de plugins et générateur intégrés.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | HTML                                                                                     |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **59**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Contexera/dsh-agent-team">Contexera/dsh-agent-team</a></b> · ⭐57 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

dsh-agent-team gives DeepSeek Harness agents that don't reset: durable Members with their own memory, notes, and skills across sessions, rollovers, and restarts. You set the direction; agents coordinate through Channels and Tasks.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **57**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `agent-orchestration` · `agent-team` · `ai-agents` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `multi-agent`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/contexera--dsh-agent-team/25f8cc5a2a3231a3.png" width="100%" alt="Contexera/dsh-agent-team screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Récupération de contexte de l’espace de travail et suivi du cycle de vie, sensibles aux tâches, pour les agents de programmation IA : trouver, organiser et suivre en continu les documents, le code et les médias les plus pertinents pour la tâche actuelle. Entièrement local, zéro appel de modèle, zéro réseau.  Récupération de contexte de l’espace de travail et suivi du cycle de vie, sensibles aux tâches, pour les agents de programmation IA. Trouvez, organisez et suivez le contexte de l’espace de travail le plus pertinent pour la tâche en cours — localement, de manière déterministe, avec zéro appel de modèle et zéro réseau.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **53**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐43 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin maître des ressources de jeu dsh. Intègre le modèle de génération d’images seedream et le modèle de génération vidéo minimax pour créer toutes sortes de ressources de jeu.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **43**     |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 67</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - A pre-execution guard for AI coding agents.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Une liste sélectionnée des meilleurs plugins IA remarquables pour les…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin DSH — modèles OpenCode Zen gratuits pour DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Marché de plugins DSH / DSH Plugin Marketplace : parcourez, installez et mettez…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins pour des logiciels qui itèrent sur eux-mêmes — le…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [PensiveFei/dsh-secure-audit](https://github.com/PensiveFei/dsh-secure-audit) - Read-only security &amp; compliance plugin for DeepSeek Harness: prompt-injection…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Répertoire sélectionné de plugins DeepSeek Harness (DSH) — plus de 280 plugins…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Plugin DeepSeek Harness : maintient une fenêtre de contexte précise pour le…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Boîte à outils Zotero pour DeepSeek harness ;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH : shell Git Bash pour tous les modes d.
- [PensiveFei/deep-read-summarize](https://github.com/PensiveFei/deep-read-summarize) - Workflow de lecture approfondie et de synthèse pour les livres, articles…
- [gulagala001/oh-my-dsh](https://github.com/gulagala001/oh-my-dsh) - 让你的 DSH，火力全开。长上下文、任务验证、提示词优化、代码理解、电脑操作与四套完整主题.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - Plugin web DSH : développement distant similaire à VSCode Remote-SSH.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT : système d.
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - La suite bureautique en trois pièces ! Outils de documents Office pour DeepSeek…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh pour Android : intègre DeepSeek Harness, un environnement d.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Collection de plugins d.
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Navigation de sessions DSH.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin Web DSH : statistiques quotidiennes d.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, outils, compétences et ressources d.
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin gestionnaire de serveur MCP pour DeepSeek Harness : page Settings → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Plugin DeepSeek Harness : 15 compétences d.
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de négociation commerciale A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Toolbox panel for DeepSeek Harness Web: MCP manager.
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催更姬 : un espace de travail romanesque pour 大肥鱼.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin DeepSeek Harness · Bouton « optimiser » en un clic dans la barre d.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vrai PowerPoint, pas du HTML. Indiquez à votre IA les sujets à couvrir et…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Plugin d.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Gestionnaire tout-en-un de skills, subagents, MCP et LSP pour DeepSeek Harness…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [sueccku/dsh-plugin-wps-office-next](https://github.com/sueccku/dsh-plugin-wps-office-next) - 在 DeepSeek Harness（DSH）里用中文对话操作 WPS 表格 / 文字 / 演示：读写数据、排版、公式图表、批量转 PDF.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Tests de compatibilité permanents pour les plugins DeepSeek Harness : versions…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Compression agressive du contexte pour les agents privilégiant le local.
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [chengshenyangtai/dsh-workbuddy-trae-qoder-connect](https://github.com/chengshenyangtai/dsh-workbuddy-trae-qoder-connect) - 把 WorkBuddy（多账号/企业版）、Trae CN / TRAE SOLO CN、Qoder CN 三家订阅聚合进同一个 DSH…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayons X pour les plugins DeepSeek Harness : capacités déclarées comparées au…
- [zzhang82/Agent-Memory-Bridge](https://github.com/zzhang82/Agent-Memory-Bridge) - Persistent engineering memory for coding agents over MCP.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - Plugin DSH : connectez les modèles de l.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - Boîte à outils de base de connaissances pour la recherche et la revue…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [xyrrrrr-r/dsh-eval-control](https://github.com/xyrrrrr-r/dsh-eval-control) - Host-side DSH evaluation control plugin for aeval：一次评测试次的配置注入、预算封顶与证据归属.
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - Vérification des affirmations de conception et de code : comparaison des faits…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espace de travail multi-dossiers : permet à l.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard de vérification sans dépendances pour les plugins DeepSeek Harness…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) plugin: one-click OpenCode Go model sync in the settings…
- [umineko987/dsh-search-enhance](https://github.com/umineko987/dsh-search-enhance) - 提供 Grok-compatible 网页搜索、保留来源分页、Context7 与 Exa 文档检索、有界网页提取、站点映射、离线研究计划和只读诊断.
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode sur DeepSeek Harness — plugin DSH qui permet à OpenCode Zen + Go…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins tiers et gestionnaire de cycle de vie…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx est un espace de travail de bureau extensible et centré sur l.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Agent de programmation complet pour DeepSeek Harness — flux de travail de type…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite communautaire de déploiement et d.
- [SuperWheel/cliworker-now](https://github.com/SuperWheel/cliworker-now) - DeepSeek Harness 多 CLI 智能体侧栏插件：独立对话、账号管理、角色预设与任务续聊.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web DeepSeek Harness (DSH) : onglet latéral market-dashboard de suivi du…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Rend réessayable une tentative vide du modèle sans attribution, pour la seule…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins qui nettoient après leur passage : un portage de Swift 6 du framework…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Préréglage d.
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins Rust avec un noyau de cycle de vie vérifié par Verus et…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [ArisaYamatogi/dsh-lecture-copilot](https://github.com/ArisaYamatogi/dsh-lecture-copilot) - A Dsh plugin that automatically records, translates lecture and generates notes…

</details>

<a id="writing"></a>

## Articles, discussions et vidéos

Articles, discussions et vidéos consacrés aux fonctionnalités des mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 338     | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 79      | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 40      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 24      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12      | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 5       | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 5       | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| PowerShell | 2       | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1       | `reporails/arcade`                                                                                            |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1       | `dphmoblie/deepseek-harness-android`                                                                          |
| Swift      | 1       | `eovidiu/cordis-ios`                                                                                          |

<sub>Seules les entrées qui déclarent un langage sont comptabilisées. Les entrées de documentation et de discussion sont exclues de ce tableau.</sub>

## Contribuer

Les corrections sont les bienvenues et constituent le moyen le plus rapide d’améliorer cette liste. Ouvrez une issue ou une pull request si une entrée est mal classée, mal évaluée, ou si un projet a été exclu à tort en raison d’une homonymie — c’est la catégorie dans laquelle les filtres automatisés risquent le plus de se tromper.

---

<sub>Projet communautaire indépendant. Non affilié à Anthropic, qui ne l’a ni approuvé ni évalué. Claude Code, Claude et Anthropic sont des marques commerciales de Anthropic. Le comportement des produits peut changer sans préavis ; vérifiez tout élément critique dans la documentation officielle. Les ressources restent la propriété de leurs projets d’origine et ne sont reproduites que lorsque la licence l’autorise.</sub>

<sub>Dernière mise à jour · 2026-10-11T23:26:48+08:00</sub>
