<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Excellents mods Claude">
</p>

<h1 align="center">Excellents mods Claude</h1>

<p align="center"><b>L’index de Claude Code regroupant les mods et plugins évalués selon les preuves, ainsi que les comportements sous-jacents qu’ils modifient.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-485-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <b>Français</b> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Index en ligne** · Dernière synchronisation: `2026-10-12T12:37:21+08:00` (UTC+8)
> · Entrées: **485** · Ajoutées lors de la dernière mise à jour: **0** · Langages d’implémentation: **13**

<sub>Chaque entrée ci-dessous a été collectée, filtrée et revérifiée automatiquement. Aucun contenu présenté ici n’est sponsorisé.</sub>

<a id="featured"></a>

## Sélections du moment

<sub>Une entrée par catégorie, classée selon le niveau de preuve et le nombre d’étoiles, puis recalculée à chaque mise à jour. Il s’agit d’un classement, pas d’une recommandation ; chaque sélection renvoie à sa fiche complète ci-dessous. Les projets ayant publié une capture d’écran ou un enregistrement sont privilégiés, afin que le bandeau reste visuel.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9479 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2539 · Python · 👁️ observed</sub>
<sub>Trouvez les jetons fantômes. Corrigez-les. Survivez à la compaction. Évitez la dégradation de la qualité du contexte.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74370 · TypeScript · 👁️ observed</sub>
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
- [Mods : conçus avec la capacité de mod](#mods--conçus-avec-la-capacité-de-mod) — **369**
- [Écosystèmes de plugins DSH et Cordis](#écosystèmes-de-plugins-dsh-et-cordis) — **88**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150265 · TypeScript · ✅ official · 0 天</summary>

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
| Étoiles                       | **150265** |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9479 · TypeScript · ✅ official · 2 天</summary>

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
| Étoiles                       | **9479**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8250 · Python · ✅ official · 2 天</summary>

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
| Étoiles                       | **8250**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242 天</summary>

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
| Étoiles                       | **6347**   |
| Dernière mise à jour du dépôt | 2026-02-11 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| Étoiles                       | **1798**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Official Claude Code mods by See Stack: live context window HUD, voice narration deck, and terminal tools. Install via: npx seestack

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic`                |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **0**      |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/sjh9714/dsh-win32">sjh9714/dsh-win32</a></b> · ⭐111 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell, Workspace Write, shortcuts, and legacy preset repair. No WSL.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic`                         |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **111**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `ai-agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `deepseek-v4` · `doctor` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sjh9714--dsh-win32/3aeddbabbfa99912.gif" width="100%" alt="sjh9714/dsh-win32 screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sjh9714--dsh-win32/3aeddbabbfa99912.gif" width="100%" alt="sjh9714/dsh-win32 animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/cheshireez/dsh-skill-hub">cheshireez/dsh-skill-hub</a></b> · ⭐28 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness（dsh）Web GUI 技能中枢：浏览/搜索完整本地技能目录、启用/禁用、查看正文、排查诊断、新建技能，基于官方 ctx.skills 注册表。 In-GUI skill hub for dsh: browse, search, enable/disable, inspect, diagnose and scaffold local skills from the official ctx.skills registry.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic`                         |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **28**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent-skills` · `deepseek-harness` · `dsh` · `dsh-plugin` · `skill` · `skill-hub` · `skills`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cheshireez--dsh-skill-hub/a960a5b7c4981b8e.png" width="100%" alt="cheshireez/dsh-skill-hub screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2539 · Python · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **2539**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐501 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Catalogue communautaire de mods publics Claude Code (hooks de fonctions), analysés depuis GitHub avec indication de ce que chaque mod peut lire, écrire, exécuter ou envoyer sur le réseau. Parcourir https://mods.aidojo.si/

<sub>🔧 Utilisé dans le code: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | JavaScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **501**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐196 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **196**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐145 · TypeScript · 👁️ observed · 7 天</summary>

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
| Étoiles                       | **145**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐104 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **104**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐100 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Thèmes pour Claude Code : lignes d’outils avec icônes, cartes de différences, de tableaux et de graphiques Mermaid, bandeau d’utilisation et quinze thèmes. /skin les échange en direct.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **100**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐79 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **79**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐68 · TypeScript · 👁️ observed · 9 天</summary>

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
| Étoiles                       | **68**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐60 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Résumé

Skills, agents, commandes, règles, hooks et styles de sortie experts pour Claude Code — continuité des sessions et outils CLI modernes pour les flux de développement réels

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
| Étoiles                       | **60**     |
| Dernière mise à jour du dépôt | 2026-10-07 |
| Première apparition           | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Résumé

Mods Claude Code : barres de progression du plan en direct au-dessus de l'invite

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
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Utilisez Codex, GLM et d’autres agents de programmation comme sous-agents de Claude Code.

##### 📌 Informations générales

| Champ     | Valeur                                                                          |
| --------- | ------------------------------------------------------------------------------- |
| Catégorie | `Mods : conçus avec la capacité de mod`                                         |
| Source    | `son propre texte mentionne un mod API, ou déclare la prise en charge des mods` |
| Langage   | TypeScript                                                                      |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **16**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6 天</summary>

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
| Étoiles                       | **14**     |
| Dernière mise à jour du dépôt | 2026-10-05 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
| Dernière mise à jour du dépôt | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/natsukium/claude-code-figures-plugin">natsukium/claude-code-figures-plugin</a></b> · ⭐7 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics terminals — a Claude Code plugin

<sub>🔧 Utilisé dans le code: `hooks/register.tsx`</sub>

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
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `d2` · `diagrams` · `graphviz` · `kitty-graphics` · `latex`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/natsukium--claude-code-figures-plugin/8b6e1b6a10ace52e.png" width="100%" alt="natsukium/claude-code-figures-plugin screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary><b>Plus dans cette catégorie</b> <sub>· 335</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Collection de plus de 100 mods utilisables avec Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods Claude et outils pour les créer : un skill de construction, puis des mods.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Le harness Claude Code que j.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Donnez un nouveau toit à Claude Code avec Claude Mods : sans modifier le…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quatre mods Claude Code : Cache Keeper, Recording Mode, Goal Meter et Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods Claude Code de Learning Hacker : rendre le fonctionnement de l.
- [kakha13/claude](https://github.com/kakha13/claude) - Mods Claude Code qui corrigent et traduisent vos prompts avant que Claude ne…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods et skills Claude Code de Nekyia Labs, créés et utilisés quotidiennement…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Une apparence d.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un volet latéral pour Claude Code : les sous-agents exécutés par une session…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de connaissances Obsidian citant ses sources sur les mods de Claude Code…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panneau latéral Claude Desktop (onglet Code) : répertorie les tâches inachevées…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill qui apprend aux agents Claude Code à créer des mods Claude.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barre d.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins et skills communautaires pour Claude, installables depuis une…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods Claude (plugins à hooks de fonction) pour Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galerie de mods Baselane : mods Claude Code, vérifiés et épinglés.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Une file de décisions CLI/TUI pour les humains travaillant avec des agents…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE pane mod: agent board, file tree and HWP/PDF viewer, system…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods Claude Code : panneau d.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Carte d.
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods pour Claude Code : plugins de hooks de fonctions qui ajoutent des panneaux…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods Claude Code : screen-guard masque les noms et les secrets pendant le…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Tableau de bord GSD en direct pour Claude Code : roadmap, arbre d.
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensions Claude Code. Débloquez toute la puissance de Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) pour Claude Code qui ajoute un panneau latéral avec les onglets…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panneaux, garde-fous et mods améliorant le confort d.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Deux mods Claude Code au-dessus de la zone d.
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Faites durer plus longtemps le forfait Claude Pro : des mods Claude Code pour…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lit les fichiers markdown nommés par Claude Code, affichés à côté de la…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code : miniatures des images collées au-dessus de l.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Collègue vocal pour Claude Code. Discutez avec un loup en 3D propulsé par l.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods Claude Code : typing-speed, un compteur de vitesse de frappe en direct…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Feux d.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Un test de frappe pour patienter pendant que Claude travaille.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Découvrez les mods, plugins et extensions Claude Code grâce à des démos…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code : diagrammes Mermaid dessinés directement dans la transcription.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods et skins pour Claude Code : barre de progression en direct pour les tâches…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Petits mods Claude Code (plugins à hooks de fonction) : session-switcher et…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods Claude Code : menu Tools de Claude, mode Zen, thèmes de terminal…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods Claude Code : mod-scout (trouver les mods que vous utiliseriez le plus)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Deux mods Claude Code pour exécuter de nombreuses sessions simultanément : une…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr : découvrir, inspecter, activer ou désactiver et mettre à jour les mods…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods Claude Code : barre de contexte, panneau des agents, floutage PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Meilleurs mods Claude Code : sélectionnés, validés et épinglés.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code : routage automatique des modèles Claude.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods pour Claude Code : volets, commandes et hooks créés avec le plugin…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Raccourcit les énormes sorties des outils avant qu.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Six mods pour Claude Code : mascotte Clawd animée, barres de limite…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Une marketplace de mods pour Claude Code : un débogueur pas à pas pour la…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six mods Claude Code : limites de plan et contexte au-dessus du prompt, coach…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Le meilleur pack de mods tout-en-un pour Claude Code : limites d.
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Lisez des YouTube Shorts dans votre Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Boîte à outils Claude de Naren : skills, mods et serveurs MCP pour Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod pour Claude Code qui affiche les diffs Edit et Write dans deux colonnes…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods pour Claude Code : Clawd, une minuscule mascotte pixelisée qui met en…
- [reporails/arcade](https://github.com/reporails/arcade) - Jeux de bureau classiques sous forme de mods Claude Code, auxquels on joue dans…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Une liste organisée de mods de Claude Code, installables comme une marketplace…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods Code Claude à la demande — une compétence qui lit votre conversation et…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code très affirmé, conçu par un Rustacean passionné d.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods Claude Code qui gardent un agent honnête — des hooks de fonction qui…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Ma collection de mods pour Claude Code, un mod par répertoire.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Un rappel d.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Les mods Code de Claude que j.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Tableau de bord macOS notch pour Claude Code : limites d.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod pour Claude Code : barre de cache d.
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Cache de prompts, contexte et limites du plan visibles d.
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Coût, tokens et limites de forfait de vos agents de programmation.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code qui affiche vos limites d.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods pour Claude Code : barres de progression pour les plans, registre de ce…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Voyez ce que Claude Code exécute en arrière-plan : sous-agents, tâches Codex…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notes de terrain du premier jour sur les mods Claude Code sur Windows : une…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools : un débogueur pour les appels d.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - De petites cartes qui se placent sous l.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod pour Claude Code : compteurs en direct du coût, du contexte et du quota de…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Un mod de Claude Code qui retient les déploiements de sous-agents, les invites…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 compétences Agent pour Claude en cinq packs.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods pour claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod Claude Code qui active ou désactive vos compétences, agents, règles et…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins Claude Code (mods) : passez d.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de Claude Code testés et installables en une commande : garde-fous pour…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods pour Claude Code : plugins reposant sur des function hooks.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace de mes propres mods pour Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un ensemble de mods claude code créés par mes soins.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods Claude Code. touch-map : voyez quels fichiers Claude a listés, lus…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Apprenez une langue étrangère tout en travaillant avec Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - S.
- [atharv6f/headway](https://github.com/atharv6f/headway) - Objectif, tâches et agents au-dessus de votre prompt Claude Code — sans…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio Internet dans Claude Code : barre latérale cliamp, mini-lecteur, favoris…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude cuisine. Discutez avec votre équipe.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods Claude Code pour de vrais ingénieurs.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Récapitulatif de la session de terminal de Claude Code, dans l.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Une bataille spatiale au-dessus du prompt de Claude Code pendant qu.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Voyez quels fichiers chaque agent de Claude Code a dans son contexte, et quelle…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Transformez chaque session Claude Code en petite aventure : musique générative…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Petits mods Claude Code pour le terminal et l.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI qui ajoute des mots espagnols aux réponses des agents.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Vos événements Alarum au-dessus de l.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Votre liste de tâches Floatee au-dessus du prompt de Claude Code : exécutez…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barre latérale au style d.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code qui le transforme en The Machine de Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Mod de Claude Code : une escouade en pixel art suggère le modèle adapté.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code mod for mandatory, verified DAG workflows of…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods open source pour Claude Code : panneaux, lignes d.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Un mod de Claude Code : un panneau pour chaque sous-agent, les fichiers qu.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code : état de la session, progression Spec Kit en direct et…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La fenêtre de contexte sous forme d.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tâches en direct pour Claude Code Desktop : une barre au-dessus de…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuit et open source pour Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Mettez les invites de côté pour plus tard et réinsérez-les dans la zone de…
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Modification de Claude Code qui affiche les images directement dans Ghostty et…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un mod Claude qui affiche les demandes de fusion GitHub de la session dans un…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated, tested, and every mod ships with the prompt that…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mods Code de Claude : transfert automatique et barre de progression.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Compétences de Claude Code : vérificateur de faits pour la documentation…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod de Claude Code qui réécrit les invites approximatives en invites claires…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Pedro La Rosa.
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Claude Code mod: your 5-hour and 7-day usage limits as live, animated bars…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compagnon de Claude Code : un compagnon ASCII au-dessus de votre invite…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin Claude Code pour la visibilité des outils par agent — masquer et refuser…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Modification de Claude Code : routage du modèle/de l.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin et mod de Claude Code : un SDLC natif de l.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Collection Awesome de mods Claude Code | collection de mods 클로드 코드.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis : un mod de fans non officiel des Avengers pour Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks : un mod de Claude Code qui lit à voix haute, à la demande, les…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code : petits plugins pour les panneaux en direct, le routage…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code : quota 5h/7d, fenêtre de contexte, temps restant du cache…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod et plugin Claude Code : moniteur d.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod Code Claude qui indique en direct quels fichiers Claude a modifiés et…
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Claude Code mods marketplace: agent-board, auto-model, session-collab +…
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Mod Code Claude : achemine chaque sous-agent vers le modèle Claude le moins…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un chat animé en braille au-dessus de l.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code : acheminez les tâches peu coûteuses vers GLM/Kimi via un…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un chat pixel au-dessus de votre prompt Claude Code qui exécute un appel de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code qui choisit le bon moment pour compacter afin de garder…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods de Claude pour Claude Code : compteur de tokens.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods polyvalents pour Claude Code : bandes, volets, notifications et hooks.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Vos limites d.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - De courtes séances d.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un tableau d.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing pour Claude Code : Apple Music et Spotify au-dessus de…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods pour Claude Code : horloge du cache, rayon d.
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - A Claude Code mod: the record of orchestrated work, with runs, lanes…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code mods: Suggestion Spotlight shows what Claude.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Simplement un hibou pour votre Claude Code.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Le moteur Doom original avec Freedoom, jouable dans Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Un mod Claude Code qui conserve une liste actualisée des éléments ouverts d.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Examinez chaque fichier modifié par Claude, comme dans une pull request, sans…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi qui vit dans Claude Code : il éclot, mange le code écrit par…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Signets et marques de style vim dans les conversations du terminal Claude Code…
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Un mod Code Claude : une bande au-dessus du prompt avec les actualités de…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code : après qu&#x27;un guard bloque un appel d&#x27;outil, il arrête les…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code : tâches en arrière-plan dans une seule vue, avec progression…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code : une seule boîte de réception pour les messages des…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code : explique les blocages du sandbox et transforme les blocages…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoris pour Claude Code : icônes en un clic pour vos commandes et skills.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hé, je l.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar en direct de vos branches parallèles et worktrees au-dessus de…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Mod Code Claude : trois prochaines étapes après chaque réponse, dans n.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de code Claude : durée de chaque réponse, durée de réflexion de Claude et…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mods de code Claude : streamer-mode masque les volets privés, les bandes et la…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Un cockpit au-dessus de votre prompt Claude Code. Le canard lit les jauges.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: private values are replaced with…
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Mod Code Claude : utilisation des tokens, modèles et sous-agents en direct pour…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panneau latéral d.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Liste des fichiers dans la barre latérale : fichiers créés, modifiés ou…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Un lapin hollandais nain bélier 8-bit (noir et blanc) court et bondit au-dessus…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - La barre latérale « ce que j.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Chronologie dans la barre latérale : où le temps de ce tour a été dépensé…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Échanges de tokens dans la barre latérale : combien de tokens la conversation…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Le petit mot honnête de claude code : après chaque tour, Claude murmure une…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Evidence-gated plan checklist for Claude Code: approved plans become a…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vit dans un bandeau au-dessus de votre prompt Claude Code : il met en…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod qui lit à voix haute les réponses et notifications de Claude Code avec…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod Claude pour lire et rejoindre les conversations entre vos sessions…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods pour Claude Code. PixBar : une créature pixelisée au-dessus de votre…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code mod for macOS: one floating window that shows what every Claude…
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Claude Code mods, published as a marketplace.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Deux mods de Claude Code : folio, un panneau de fichiers à côté du chat, et…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph : un graphique en direct de ce que Claude Code sait.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Ne laissez pas votre attention vagabonder pendant que vous attendez la réponse…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Mods Claude Code de Sanmu — une marketplace de plugins (volet latéral de tâches).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guide des mods de code Claude sélectionnés par la communauté : cas…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de code Claude qui affiche ce que fait Claude dans le sous-titre de…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, an unofficial fan-made pixel companion that lives above the Claude Code…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - À quel point le contexte de Claude est rempli, quand son cache devient froid et…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod de Claude Code : répondez à Claude point par point, directement sur le…
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod de Claude Code avec des profils d.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Petits mods pour Claude Code : runner-avatar, un petit avatar qui court…
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod de Claude Code : panneau en direct présentant les objectifs, hypothèses…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code mod: /sessions pane to browse and delete sessions with their…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods communautaires pour Claude Code : protections, panneaux et commandes qui…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panneau latéral pour Claude Code : fichiers écrits par Claude, divisions du…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un panneau latéral discret pour Claude Code : ce que fait cette session, son…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Une heure discrète au-dessus de chaque invite et de chaque réponse dans la…
- [mmedum/spor](https://github.com/mmedum/spor) - Restaure ce que Claude Code replie : les fichiers lus par Claude, les commandes…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de code Claude qui réactive les outils todo pour les modèles qui les…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod Claude Code qui attend une pause sûre, puis transmet votre session ou la…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de code Claude : une ligne par tâche au-dessus du prompt avec la tâche…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jouez au Puissance 4 contre une IA dans Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de code Claude : lorsqu.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code mod pour les dépôts partagés par plusieurs agents IA : empêche les…
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Des mods amusants et gratuits pour Claude Code qui ne dépensent jamais de…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Un garde-fou pour le SQL dans Claude Code : demande confirmation avant que…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un seul mod pour Claude Code, Windows et le CJK en priorité : aperçus d.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Les meilleurs Mods de Claude Code, classés selon ce qu.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Deux Mods Claude pour Claude Code : garde-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Timestamps for Claude Code: the time on every message, reply and tool call…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Track changes for Claude Code: see exactly what Claude changed in your Excel…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panneau latéral de statistiques de session en temps réel pour l.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Claude Code mod: tracks every subagent.
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Claude Code mod: every subagent as a little stick person in a side pane, with…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods pour Claude Code : safety-guard bloque les commandes destructrices et…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Un crabe Claude en pixel art animé pour Claude Code : il met en scène ce que…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code : des pompes à faire pendant que Claude travaille. Aucun token.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Three dependency-free mods for Claude Code: a responsive statusline, a…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code : transforme le plan que vous approuvez en mode plan en une…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Une liste soigneusement sélectionnée de mods Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode sans coût : les agents auxiliaires fonctionnent sur Haiku, et les gros…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Une bande-son lofi qui suit la session : calme, concentration, fluidité, ainsi…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Apprenez pendant que Claude code : après un tour ayant modifié le code, une…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Un enregistrement de chaque modification effectuée par Claude : rejouez chaque…
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod Claude Code pour le contexte, la croissance, le quota, le cache, le coût…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Mods Claude Code personnels.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - Le DOOM original dans un panneau Claude Code, sans rien à installer : le moteur…
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Empêchez les agents auxiliaires de Claude (sous-agents) d.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messages de commit en un clic pour Claude Code avec une Malenia en pixel art…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de code Claude qui affiche l.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod Claude Code qui affiche la session actuelle dans un panneau : chaque…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins Claude Code de mods : des plugins function-hooks qui…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Écoutez les réponses de Claude Code pendant que la phrase lue est mise en…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code : barre de progression animée et résumé de complétion pour les…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trois petits mods Claude Code : voyez quand vos sous-agents auront terminé…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Dites « I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Posez à Claude une question annexe dans un panneau à côté de votre travail.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code vous envoie un message sur Telegram lorsqu.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Un mod de Claude Code : surligneur pour les réponses, panneau latéral pour les…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Code Claude : vos limites d.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods pour Code Claude. agent-crew : surveillez le travail de vos sous-agents…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Affichez des formules mathématiques LaTeX en ligne et en mode affichage, ainsi…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Un tableau de tâches en direct pour Claude Code : planifiez avant de…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Une collection soigneusement sélectionnée des meilleures ressources pour les…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin Claude Code qui montre ce qui se passe - utilisation du contexte…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Ligne d.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Toutes les parties du prompt système de Claude Code, les 27 descriptions…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Plus de 45 conseils pour tirer le meilleur parti de Claude Code, des bases aux…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — générez des carrousels Xiaohongshu et des paires…
- [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) - A terminal window manager that knows what your agents are doing.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline élégant de style vim pour Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Examinez le diff de votre agent de programmation dans un panneau de terminal et…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de ligne d.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Créez des mods pour Claude Code : interceptez toute requête, modifiez toute…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Tableau de bord complet de ligne d.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon : suivez l.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Une ligne d.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills et mods publics pour Claude Code.
- [Amakurai/dsh-liketavern](https://github.com/Amakurai/dsh-liketavern) - A DeepSeek Harness (dsh) plugin — turns dsh web into a SillyTavern-style…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, sous-agents, hooks, commandes slash et guides pour Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs légaux gratuits et agents de codage — mise à jour automatique…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Calculateur de coûts rapide et sans dépendances, avec ligne d.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Ligne d.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Scores, calendriers et classements de football en direct pour les…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plan de contrôle local pour Claude Code sur Windows et macOS : changez de…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill qui transforme votre agent de codage en expert des firmwares de…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horaires de prière, date hégirienne, adhkar, ayah quotidienne, jeûne sunnah…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuration personnelle Claude Code versionnée dans ~/.claude — agents…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness plugin for research topics…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Barre d.
- [William2333ZZ/mywork-deepseekharness](https://github.com/William2333ZZ/mywork-deepseekharness) - MyWork — a personal agent on DeepSeek Harness: AI teammates that each own a…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Collection de plugins pour Claude Code, pi et DeepSeek Harness : HUD de barre…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Boîte à outils Claude Code portable pour l.
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Lightweight Claude Code status line — one ~170-line Bash script, zero…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuration globale portable de Claude Code : compétences personnalisées…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins Claude Code que j.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods non officiels pour l.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Pont DSH &lt;-&gt; Feishu (Lark), développé en interne (pas un fork) : carte de…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins et de skills Claude Code pour faciliter la création de…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gouvernance des tokens pour Claude Code : le meilleur modèle dirige…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Dépôt de mods Awesome Media pour Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Cut Claude Code &amp; Codex token spend: routes lookups and test runs to cheaper…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Ligne d.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Configuration simple et utile de la ligne d.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Affichez la barre d.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Ligne d.
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Une ligne d.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Affichez les informations d.
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Ligne d.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Équipes d.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Modules complémentaires Claude Code : observateur de point coloré de statut…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Ligne d.
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - Personal Claude Code plugin marketplace (todo-pane).
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Une ligne d.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins Code Claude avec baloo : compétences, agent qui vérifie…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Ligne d.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Ligne d.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Ligne d.
- [dangerousplay/claude-usage-bar](https://github.com/dangerousplay/claude-usage-bar) - Claude Code plugin: colorful status line with context, cache tokens and weekly…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Ligne d.
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Ligne d.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Ligne d.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Barre d.
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Single-line status bar for Claude Code: model, git, context, tokens, cost…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Prévisualisez les images dans Claude Code : survolez une pastille sous une…
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronisez les tâches de Claude avec Fizzy.do pour une visibilité d.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Suivez l.
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook de ligne d.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Installateur d.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Ligne d.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — ligne d.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Compétences et mods pour Claude Code et Cowork — suivi de projet, document de…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Une ligne d.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Custom Claude Code statusline (upstream: kamranahmedse/claude-statusline).
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuration portable de Claude Code.
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Un petit tableau de bord pour Claude Code : pourcentage de contexte, compte à…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Barre d.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuration Claude Code portable : CLAUDE.md, paramètres, ligne d.
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用の mod 集 (goal-orchestrator: /goal をタスク分解して SubAgent に委譲させる).
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Ligne d.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Compétence Claude Code (VS Code, Windows) : aperçus d.
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Une ligne d.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Détecteur de dégradation du contexte 2026 - Mémoire proactive d.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, sous-agents et lignes d.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Barre d.
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - Une ligne d.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods pour Claude Code : volets, bandes et compagnons fondés sur des hooks de…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Ensemble d.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Transférez des tâches entre vos sessions Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Ceci dans un serveur MCP pour contrôler MODS, l.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill Codex et Claude Code pour traduire les mods CK3 avec un LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods open source et autres extensions pour Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Barre d.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker : retrouvez ce que vous demandez encore et encore à Claude Code et…

</details>

<a id="dsh-cordis"></a>

## Écosystèmes de plugins DSH et Cordis

DeepSeek Harness et Cordis atteignent le même objectif par une autre voie : chez eux, le plugin est le mécanisme de mods ; un plugin y équivaut donc à un mod ici.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74370 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **74370**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐113763 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **113763** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100614 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **100614** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82159 · JavaScript · 🔎 inferred · 1 天</summary>

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
| Étoiles                       | **82159**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35764 · Go · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **35764**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25505 · Python · 🔎 inferred · 19 天</summary>

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
| Étoiles                       | **25505**  |
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
<summary>🧵 <b><a href="https://github.com/EverMind-AI/EverOS">EverMind-AI/EverOS</a></b> · ⭐13402 · Python · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **13402**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent-memory` · `agentic-ai` · `ai` · `chats` · `clawdbot` · `clawdbot-skill` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/evermind-ai--everos/1c468e299d8b9fe7.png" width="100%" alt="EverMind-AI/EverOS screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8643 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **8643**   |
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
<summary>🧵 <b><a href="https://github.com/loopx-project/loopx">loopx-project/loopx</a></b> · ⭐6245 · Python · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **6245**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent-control-plane` · `agent-harness` · `ai-agents` · `claude-code` · `codex` · `dsh-plugin` · `local-first` · `long-horizon-agents`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/8582e0735bb2d9e1.webp" width="100%" alt="loopx-project/loopx screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/34519ef8d110de64.gif" width="100%" alt="loopx-project/loopx animation"><br><sub>enregistrement animé · <a href="https://raw.githubusercontent.com/loopx-project/loopx/main/docs/assets/personal-workspace/loopx-dashboard-launch.mp4">Ouvrir la vidéo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4521 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **4521**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4298 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DSH's officially top-recommended TUI plugin — high performance, low overhead, cute pixel whale, smooth mouse interaction. One-command install via npm. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **4298**   |
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
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1867 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Connectez des robots IM à DeepSeek Harness par code QR ou identifiants (Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord et WhatsApp). Connectez des robots IM à DeepSeek Harness via un code QR ou des identifiants (9 canaux).

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1867**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1413 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **1413**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1176 · Go · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **1176**   |
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
<summary>🧵 <b><a href="https://github.com/Clearailhc/clearai-dsh">Clearailhc/clearai-dsh</a></b> · ⭐1083 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

ClearAI：以本体为纲的原生 DSH 插件 —— 经证据核验的研究长成可浏览的领域本体。 · ClearAI: an ontology-first DSH agent preset — evidence-checked research that grows into a domain ontology.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1083**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent-preset` · `ai-agents` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `epistemic-loop` · `scientific-discovery`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/clearailhc--clearai-dsh/5621617dc3784a37.png" width="100%" alt="Clearailhc/clearai-dsh screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/aerovato/operator-memory">aerovato/operator-memory</a></b> · ⭐426 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

The self-improving context engine for coding agents.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **426**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent` · `agent-memory` · `ai` · `chatgpt` · `claude` · `claude-code` · `claude-code-plugin` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aerovato--operator-memory/b69195f907887378.jpg" width="100%" alt="aerovato/operator-memory screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Your Intelligence, Orchestrated. Every builder. Every team. Every agent. For Everyone.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Go                                                                                       |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **351**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>enregistrement animé</sub></td>
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
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-trading">zhu1090093659/dsh-trading</a></b> · ⭐239 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Agent-native trading terminal built on DeepSeek Harness. Crypto, US, CN and HK in one three-column GUI, 19+ hot-swappable connectors, dry-run by default with human approval on every live order. BYOK, no data redistribution.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **239**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent-native` · `ai-agent` · `cryptocurrency` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `trading-terminal`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhu1090093659/dsh-trading/main/docs/banners/banner-en.jpg" width="100%" alt="zhu1090093659/dsh-trading screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

<sub>Ressource liée directement depuis le dépôt source, car aucune licence autorisant la redistribution n’a été déclarée.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **204**    |
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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐177 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Plugin de sauvegarde et restauration DeepSeek Harness (DSH) — exportez, importez, migrez et synchronisez votre configuration DSH complète, vos plugins, serveurs MCP, compétences et espace de travail. Migration en un clic vers une autre machine.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **177**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **172**    |
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
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐162 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **162**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/sorsama/deepseek-harness-mobile">sorsama/deepseek-harness-mobile</a></b> · ⭐146 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Android companion for DeepSeek Harness | chat, goals, approvals & notifications from your phone, over your LAN. Kotlin + Jetpack Compose.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | Kotlin                                                                                   |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **146**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `ai-agents` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sorsama--deepseek-harness-mobile/11352624becb7d93.jpg" width="100%" alt="sorsama/deepseek-harness-mobile screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Installe automatiquement les 27 compétences d’ingénierie et de productivité de mattpocock/skills v1.3.1, sans installation manuelle. Créé avec 40 milliards de jetons, ce plugin offre une efficacité de développement 10 fois supérieure aux compétences d’origine et aide également les débutants à les prendre en main plus rapidement. Prise en charge complète des issues GitHub ; Markdown en version préliminaire ; GitLab non pris en charge pour le moment. Merci pour votre utilisation et votre soutien 💗

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **137**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐134 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **134**    |
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
<summary>🧵 <b><a href="https://github.com/tencent-connect/dsh-qqbot">tencent-connect/dsh-qqbot</a></b> · ⭐128 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

让 QQ Bot 接入 DeepSeek Harness（dsh）的官方插件

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **128**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `dsh` · `dsh-plugin` · `qqbot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tencent-connect--dsh-qqbot/4ada91a60b499824.png" width="100%" alt="tencent-connect/dsh-qqbot screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xcisxc29/dsh-wechat">xcisxc29/dsh-wechat</a></b> · ⭐115 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

WeChat channel for DeepSeek Harness

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **115**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `ai-agent` · `automation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `remote-control` · `wechat` · `wechat-bot`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xcisxc29--dsh-wechat/689ef8e1483bcfd7.png" width="100%" alt="xcisxc29/dsh-wechat screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐91 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into questions and spaced review · 把自己的资料变成题目与间隔复习的 DSH 学习插件

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **91**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **68**     |
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
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zexadev/dsh-tether">zexadev/dsh-tether</a></b> · ⭐59 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Mobile client for the DeepSeek Harness — use the dsh on your dev machine from your Android or iOS phone, remotely across networks, peer-to-peer over iroh with no server to set up (falls back to a relay that only sees ciphertext)

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **59**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `ai-agent` · `android` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `hole-punching`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zexadev--dsh-tether/0ffdc271ad99985f.jpg" width="100%" alt="zexadev/dsh-tether screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
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
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

NekroNXT : système d’agents de discussion de groupe multiplateforme basé sur DeepSeek Harness (DSH)｜Système d’agents de discussion de groupe multiplateforme propulsé par DSH

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **35**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 54</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Protection avant exécution pour les agents de codage IA.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Une liste sélectionnée des meilleurs plugins IA remarquables pour les…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin DSH — modèles OpenCode Zen gratuits pour DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Marché de plugins DSH / DSH Plugin Marketplace : parcourez, installez et mettez…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins pour des logiciels qui itèrent sur eux-mêmes — le…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Répertoire sélectionné de plugins DeepSeek Harness (DSH) — plus de 280 plugins…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Plugin DeepSeek Harness : associez les fenêtres de contexte des modèles en un…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Zotero plugin for DeepSeek Harness: search papers, read full-text PDFs and…
- [vritser/dsh-emacs](https://github.com/vritser/dsh-emacs) - An Emacs client for DeepSeek Harness.
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh安卓版：集成 DeepSeek Harness、Ubuntu 运行环境、插件与文件管理，以及用户授权的 Shizuku 和无障碍自动化.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Collection de plugins d.
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de négociation commerciale A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Panneau Toolbox pour DeepSeek Harness Web : gestionnaire de MCP.
- [SeverusZh/dsh-plugin-subagent-director](https://github.com/SeverusZh/dsh-plugin-subagent-director) - Subagent Director: per-subagent LLM provider/model selection with role…
- [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution plugin for DeepSeek Harness: versioned, auditable…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vrai PowerPoint, pas du HTML. Indiquez à votre IA les sujets à couvrir et…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Graphe de connaissances du code et harness de contexte local d.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Plugin d.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Transformez les modèles déjà connectés sur l.
- [baosfeng/my-dsh-plugins](https://github.com/baosfeng/my-dsh-plugins) - DSH（DeepSeek Harness）插件与技能集合仓库：插件独立版本、GitHub Release 发布（插件与技能清单见仓库 README）.
- [dabaicai001/star-dsh-desktop](https://github.com/dabaicai001/star-dsh-desktop) - StarHub — All-in-One DevOps Desktop Command Center.
- [evoelsewhere/evoflux](https://github.com/evoelsewhere/evoflux) - Evoflux is an open-source, local-first workspace where AI agents build…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - équipe du plugin dsh.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Tests de compatibilité permanents pour les plugins DeepSeek Harness : versions…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Compression agressive du contexte pour les agents privilégiant le local.
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Compression protégée du contexte pour DeepSeek Harness (dsh) : LLM propose, les…
- [morlay/dsh-plugin](https://github.com/morlay/dsh-plugin) - dsh plugins.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin hôte DeepSeek Harness qui conserve les documents du projet et la mémoire…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayons X pour les plugins DeepSeek Harness : capacités déclarées comparées au…
- [IT-coder-Yy/dsh-lazygit-plugin](https://github.com/IT-coder-Yy/dsh-lazygit-plugin) - A visual Git workbench for DeepSeek Harness Web—inspect repositories, run…
- [JessenReinhart/dsh-tokenslash](https://github.com/JessenReinhart/dsh-tokenslash)
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH : fenêtre d.
- [minglu6/dsh-provider-qoder](https://github.com/minglu6/dsh-provider-qoder) - Qoder CN adapter plugin for DeepSeek Harness.
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - The DeepSeek Harness Personalization Settings plugin is used to configure the…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espace de travail multi-dossiers : permet à l.
- [CoolTea001/dsh-cool-theme](https://github.com/CoolTea001/dsh-cool-theme) - DeepSeek Harness theme plugin — supports Dark / Light / System appearance…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard de vérification sans dépendances pour les plugins DeepSeek Harness…
- [shenhuanageshei/dsh-thincoder-suite](https://github.com/shenhuanageshei/dsh-thincoder-suite) - DSH plugin porting thincoder self-discipline suite: advisor convergent review /…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode sur DeepSeek Harness — plugin DSH qui permet à OpenCode Zen + Go…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins tiers et gestionnaire de cycle de vie…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx est un espace de travail de bureau extensible et centré sur l.
- [SeverusZh/dsh-yolo-mode](https://github.com/SeverusZh/dsh-yolo-mode) - dsh-yolo-mode - an LLM-powered auto-approval plugin for DeepSeek Harness…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web DeepSeek Harness (DSH) : onglet latéral market-dashboard de suivi du…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness plugin: turns the Windows sandbox ACL provisioning failure…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Rend réessayable une tentative vide du modèle sans attribution, pour la seule…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Évaluation de la progression pour les cycles d.
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - plugin dsh : transforme un arrêt pour longueur tronquée en récupération de…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins qui nettoient après leur passage : un portage de Swift 6 du framework…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins Rust avec un noyau de cycle de vie vérifié par Verus et…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - Site d.

</details>

<a id="writing"></a>

## Articles, discussions et vidéos

Articles, discussions et vidéos consacrés aux fonctionnalités des mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
| TypeScript | 300     | `anthropics/claude-code`, `anthropics/claude-code-action`, `see-stack/claude-code-mods`                       |
| JavaScript | 67      | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 36      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 22      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 11      | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 7       | `Gaurav-Gosain/tuios`, `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`                              |
| Rust       | 7       | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| Kotlin     | 2       | `sorsama/deepseek-harness-mobile`, `dphmoblie/deepseek-harness-android`                                       |
| PowerShell | 2       | `GoSlowPoke168/claude-statusline`, `Gabriel-Dalton/claude-statusline-tokens`                                  |
| Swift      | 2       | `KiranPothana/session-board`, `eovidiu/cordis-ios`                                                            |
| C          | 1       | `reporails/arcade`                                                                                            |
| Emacs Lisp | 1       | `vritser/dsh-emacs`                                                                                           |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                          |

<sub>Seules les entrées qui déclarent un langage sont comptabilisées. Les entrées de documentation et de discussion sont exclues de ce tableau.</sub>

## Contribuer

Les corrections sont les bienvenues et constituent le moyen le plus rapide d’améliorer cette liste. Ouvrez une issue ou une pull request si une entrée est mal classée, mal évaluée, ou si un projet a été exclu à tort en raison d’une homonymie — c’est la catégorie dans laquelle les filtres automatisés risquent le plus de se tromper.

---

<sub>Projet communautaire indépendant. Non affilié à Anthropic, qui ne l’a ni approuvé ni évalué. Claude Code, Claude et Anthropic sont des marques commerciales de Anthropic. Le comportement des produits peut changer sans préavis ; vérifiez tout élément critique dans la documentation officielle. Les ressources restent la propriété de leurs projets d’origine et ne sont reproduites que lorsque la licence l’autorise.</sub>

<sub>Dernière mise à jour · 2026-10-12T12:37:21+08:00</sub>
