<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Excellents mods Claude">
</p>

<h1 align="center">Excellents mods Claude</h1>

<p align="center"><b>L’index de Claude Code regroupant les mods et plugins évalués selon les preuves, ainsi que les comportements sous-jacents qu’ils modifient.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-588-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <b>Français</b> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Index en ligne** · Dernière synchronisation: `2026-10-12T10:26:44+08:00` (UTC+8)
> · Entrées: **588** · Ajoutées lors de la dernière mise à jour: **0** · Langages d’implémentation: **13**

<sub>Chaque entrée ci-dessous a été collectée, filtrée et revérifiée automatiquement. Aucun contenu présenté ici n’est sponsorisé.</sub>

<a id="featured"></a>

## Sélections du moment

<sub>Une entrée par catégorie, classée selon le niveau de preuve et le nombre d’étoiles, puis recalculée à chaque mise à jour. Il s’agit d’un classement, pas d’une recommandation ; chaque sélection renvoie à sa fiche complète ci-dessous. Les projets ayant publié une capture d’écran ou un enregistrement sont privilégiés, afin que le bandeau reste visuel.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9478 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2538 · Python · 👁️ observed</sub>
<sub>Trouvez les jetons fantômes. Corrigez-les. Survivez à la compaction. Évitez la dégradation de la qualité du contexte.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74363 · TypeScript · 👁️ observed</sub>
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
- [Officiel : les propres dépôts et notes de version de Anthropic](#officiel--les-propres-dépôts-et-notes-de-version-de-anthropic) — **16**
- [Mods : conçus avec la capacité de mod](#mods--conçus-avec-la-capacité-de-mod) — **455**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150244 · TypeScript · ✅ official · 0 天</summary>

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
| Étoiles                       | **150244** |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9478 · TypeScript · ✅ official · 2 天</summary>

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
| Étoiles                       | **9478**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| Étoiles                       | **8249**   |
| Dernière mise à jour du dépôt | 2026-10-09 |
| Première apparition           | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6346 · Python · ✅ official · 242 天</summary>

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
| Étoiles                       | **6346**   |
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
<summary>🏛️ <b><a href="https://github.com/1na-ko/dsh-hdc-bridge">1na-ko/dsh-hdc-bridge</a></b> · ⭐19 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DSH 原生鸿蒙开发助手：hdc 设备闭环调试 + 设备面板（官方 client 插件形态）+ 离线官方知识层（Tier-1 随包）+ DevEco CLI 构建/签名/模拟器控制 / DSH-native HarmonyOS dev assistant: hdc device loop, live device panel, offline official knowledge, DevEco CLI build/sign/emulator

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Officiel : les propres dépôts et notes de version de Anthropic`                         |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **19**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `arkts` · `deepseek-harness` · `deveco` · `devtools` · `dsh` · `dsh-plugin` · `harmonyos` · `hdc`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/1na-ko--dsh-hdc-bridge/6bdcb2e78b3d7fc3.png" width="100%" alt="1na-ko/dsh-hdc-bridge screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary><b>Plus dans cette catégorie</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Ajout de `$.ui.notify` pour les mods : déclenche une notification native via…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Correction d.
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - A curated directory of source-verified DeepSeek Harness (DSH) plugins, tools…

</details>

<a id="mods"></a>

## Mods : conçus avec la capacité de mod

Every entry here shows evidence of using the capability Claude Code gained in 2.1.287: it draws through `ui.render`, owns a pane, band or card, reads `$.ui.selection()`, spawns teammates with `agent.spawn`, or says plainly that it is a mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2538 · Python · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **2538**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐499 · JavaScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **499**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐193 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **193**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐128 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Mod Claude Code : choisit l’effort de raisonnement pour chaque requête, affiche le cache de requête et le contexte, et transfère ou compacte en un clic

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
| Étoiles                       | **128**    |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-12 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>enregistrement animé</sub></td>
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐101 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **101**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐99 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **99**     |
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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐78 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **78**     |
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
<summary>🧩 <b><a href="https://github.com/paulbkim-dev/claude-code-cache-warmer">paulbkim-dev/claude-code-cache-warmer</a></b> · ⭐13 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Résumé

Mod de Claude Code qui conserve le cache des invites à chaud et affiche le coût et l’économie de chaque actualisation

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
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-12 |

🏷 `claude-code` · `claude-code-plugin` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐12 · JavaScript · 👁️ observed · 6 天</summary>

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
| Étoiles                       | **12**     |
| Dernière mise à jour du dépôt | 2026-10-05 |
| Première apparition           | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
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
<summary><b>Plus dans cette catégorie</b> <sub>· 421</sub></summary>

- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Skills, agents, commandes, règles, hooks et styles de sortie experts pour…
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
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods Claude Code : menu Tools de Claude, mode Zen, thèmes de terminal…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods Claude Code : mod-scout (trouver les mods que vous utiliseriez le plus)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Deux mods Claude Code pour exécuter de nombreuses sessions simultanément : une…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr : découvrir, inspecter, activer ou désactiver et mettre à jour les mods…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods Claude Code : barre de contexte, panneau des agents, floutage PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Meilleurs mods Claude Code : sélectionnés, validés et épinglés.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code : routage automatique des modèles Claude.
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Mod Code Claude : ligne d.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Raccourcit les énormes sorties des outils avant qu.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Six mods pour Claude Code : mascotte Clawd animée, barres de limite…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Une marketplace de mods pour Claude Code : un débogueur pas à pas pour la…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Six mods Claude Code : limites de plan et contexte au-dessus du prompt, coach…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Le meilleur pack de mods tout-en-un pour Claude Code : limites d.
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Lisez des YouTube Shorts dans votre Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Boîte à outils Claude de Naren : skills, mods et serveurs MCP pour Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod pour Claude Code qui affiche les diffs Edit et Write dans deux colonnes…
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Mod de Claude Code permettant à Claude d.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods pour Claude Code : Clawd, une minuscule mascotte pixelisée qui met en…
- [reporails/arcade](https://github.com/reporails/arcade) - Jeux de bureau classiques sous forme de mods Claude Code, auxquels on joue dans…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Une liste organisée de mods de Claude Code, installables comme une marketplace…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods Code Claude à la demande — une compétence qui lit votre conversation et…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code très affirmé, conçu par un Rustacean passionné d.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods Claude Code qui gardent un agent honnête — des hooks de fonction qui…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Ma collection de mods pour Claude Code, un mod par répertoire.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Un rappel d.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Les mods Code de Claude que j.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph : un mod Claude Code pour concevoir et exécuter des graphes…
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Tableau de bord macOS notch pour Claude Code : limites d.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod pour Claude Code : barre de cache d.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods pour Claude Code : volets, commandes et hooks créés avec le plugin…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Cache de prompts, contexte et limites du plan visibles d.
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Coût, tokens et limites de forfait de vos agents de programmation.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code qui affiche vos limites d.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods pour Claude Code : barres de progression pour les plans, registre de ce…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Voyez ce que Claude Code exécute en arrière-plan : sous-agents, tâches Codex…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mods Code de Claude par MacLeod Labs : streams démêle le travail entremêlé…
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
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Générique de film pour votre session de codage.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace de mes propres mods pour Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un ensemble de mods claude code créés par mes soins.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods Claude Code. touch-map : voyez quels fichiers Claude a listés, lus…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Apprenez une langue étrangère tout en travaillant avec Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - S.
- [AbhiramDwivedi/claude-ops](https://github.com/AbhiramDwivedi/claude-ops) - Claude Code plugins: an audit of how you use Claude Code, and early warnings…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Coût, tokens et utilisation du contexte en direct dans la barre latérale de…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Objectif, tâches et agents au-dessus de votre prompt Claude Code — sans…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio Internet dans Claude Code : barre latérale cliamp, mini-lecteur, favoris…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude cuisine. Discutez avec votre équipe.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods Claude Code pour de vrais ingénieurs.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Récapitulatif de la session de terminal de Claude Code, dans l.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Une bataille spatiale au-dessus du prompt de Claude Code pendant qu.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Voyez quels fichiers chaque agent de Claude Code a dans son contexte, et quelle…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Transformez chaque session Claude Code en petite aventure : musique générative…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Petits mods Claude Code pour le terminal et l.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Mods Code de Claude (marché de plugins) : barre latérale en direct avec…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI qui ajoute des mots espagnols aux réponses des agents.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Vos événements Alarum au-dessus de l.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Votre liste de tâches Floatee au-dessus du prompt de Claude Code : exécutez…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barre latérale au style d.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code qui le transforme en The Machine de Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Mod de Claude Code : une escouade en pixel art suggère le modèle adapté.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods open source pour Claude Code : panneaux, lignes d.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Un mod de Claude Code : un panneau pour chaque sous-agent, les fichiers qu.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code : état de la session, progression Spec Kit en direct et…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La fenêtre de contexte sous forme d.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tâches en direct pour Claude Code Desktop : une barre au-dessus de…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Quatorze mods Code Claude dans un seul plugin, chacun activable, avec une…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuit et open source pour Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Mettez les invites de côté pour plus tard et réinsérez-les dans la zone de…
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Modification de Claude Code qui affiche les images directement dans Ghostty et…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un mod Claude qui affiche les demandes de fusion GitHub de la session dans un…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mods Code de Claude : transfert automatique et barre de progression.
- [Nasrallah-Adel/claude-task-pilot](https://github.com/Nasrallah-Adel/claude-task-pilot) - Claude Code mod: Status / Next steps / Plan next buttons above the prompt.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Marketplace de mods pour Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Compétences de Claude Code : vérificateur de faits pour la documentation…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod de Claude Code qui réécrit les invites approximatives en invites claires…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Pedro La Rosa.
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod Claude Code : lignes de code du jour par Claude — nouvelles, modifiées…
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Claude Code mod: your 5-hour and 7-day usage limits as live, animated bars…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compagnon de Claude Code : un compagnon ASCII au-dessus de votre invite…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin Claude Code pour la visibilité des outils par agent — masquer et refuser…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Modification de Claude Code : routage du modèle/de l.
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Une collection de mods Code Claude.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin et mod de Claude Code : un SDLC natif de l.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Collection Awesome de mods Claude Code | collection de mods 클로드 코드.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis : un mod de fans non officiel des Avengers pour Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks : un mod de Claude Code qui lit à voix haute, à la demande, les…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code : petits plugins pour les panneaux en direct, le routage…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code : quota 5h/7d, fenêtre de contexte, temps restant du cache…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod et plugin Claude Code : moniteur d.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod Code Claude qui indique en direct quels fichiers Claude a modifiés et…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Mods Code de Claude par afterever (marché de plugins).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Claude Code mods marketplace: agent-board, auto-model, session-collab +…
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Mod Code Claude : achemine chaque sous-agent vers le modèle Claude le moins…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods : cartes de statistiques de session au-dessus du prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un chat animé en braille au-dessus de l.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code : acheminez les tâches peu coûteuses vers GLM/Kimi via un…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un chat pixel au-dessus de votre prompt Claude Code qui exécute un appel de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code qui choisit le bon moment pour compacter afin de garder…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods de Claude pour Claude Code : compteur de tokens.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Place de marché de plugins Claude Code par anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods polyvalents pour Claude Code : bandes, volets, notifications et hooks.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Vos limites d.
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mods Code Claude pour l&#x27;équipe S2 (l&#x27;autre marché).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - Un mod Code Claude qui fait écrire Claude en anglais simple et signale ses…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - De courtes séances d.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un tableau d.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing pour Claude Code : Apple Music et Spotify au-dessus de…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Mods Claude Code pour les sessions d.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods pour Claude Code : horloge du cache, rayon d.
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - A Claude Code mod: the record of orchestrated work, with runs, lanes…
- [BuddyLim/claude-code-mod-parked](https://github.com/BuddyLim/claude-code-mod-parked) - A Claude Code mod: a per-project backlog of things that need your attention…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Simplement un hibou pour votre Claude Code.
- [catsmonster/claude-quota-guard](https://github.com/catsmonster/claude-quota-guard) - Claude Code mod: compacts and pauses before usage limits, then auto-resumes…
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Mods do Claude Code criados por mim (painéis, comandos e hooks).
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Bande Claude Code sur une ligne.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Le moteur Doom original avec Freedoom, jouable dans Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Un mod Claude Code qui conserve une liste actualisée des éléments ouverts d.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Examinez chaque fichier modifié par Claude, comme dans une pull request, sans…
- [CTeitzel/cache-band](https://github.com/CTeitzel/cache-band) - Mod de Claude Code : un bandeau au-dessus de l.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀 전용 Claude Code mods (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Mods Claude.
- [danielmertens/Claude-mods](https://github.com/danielmertens/Claude-mods) - Collection de mods Claude personnels.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi qui vit dans Claude Code : il éclot, mange le code écrit par…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Signets et marques de style vim dans les conversations du terminal Claude Code…
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Un mod Code Claude : une bande au-dessus du prompt avec les actualités de…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code : après qu&#x27;un guard bloque un appel d&#x27;outil, il arrête les…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code : tâches en arrière-plan dans une seule vue, avec progression…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code : une seule boîte de réception pour les messages des…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code : explique les blocages du sandbox et transforme les blocages…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoris pour Claude Code : icônes en un clic pour vos commandes et skills.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hé, je l.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Mods Code Claude : rewrite-prompt.
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, compétences, extensions Pi et mods Code Claude pour Pi, Codex et…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod de code Claude : utilisation de l.
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Mods Code Claude : auto-model-detector achemine chaque prompt vers le modèle et…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar en direct de vos branches parallèles et worktrees au-dessus de…
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi — a Claude Code mod: a mascot that reads the room above the prompt, with…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Mods Code Claude (plugins function-hook) : bande de contexte, tâches en…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mods de code Claude (plugins function-hook), installés via un marketplace…
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Marché de plugins Claude Code avec mes mods.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Mods en allemand pour Claude Code : indications de contexte/cache, points en…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Mods Claude Code de Hector Bailey (marché de plugins : hectorbailey).
- [hernandezsanti/claude-code-mods](https://github.com/hernandezsanti/claude-code-mods) - Mods Claude Code qui imposent les commits liés aux tickets, protègent les…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Mod Code Claude : trois prochaines étapes après chaque réponse, dans n.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de code Claude : durée de chaque réponse, durée de réflexion de Claude et…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mods de code Claude : streamer-mode masque les volets privés, les bandes et la…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - pour mes mods claude.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod Claude Code : attend la fin de la limite d.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Un cockpit au-dessus de votre prompt Claude Code. Le canard lit les jauges.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Mods Code Claude (plugins function-hook) : suivi de la fusion des PR, relais…
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Claude Status Bar.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Petits mods Code Claude : indicateurs de contexte et d.
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Mod Code Claude : utilisation des tokens, modèles et sous-agents en direct pour…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panneau latéral d.
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Liste des fichiers dans la barre latérale : fichiers créés, modifiés ou…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Un lapin hollandais nain bélier 8-bit (noir et blanc) court et bondit au-dessus…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - La barre latérale « ce que j.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Chronologie dans la barre latérale : où le temps de ce tour a été dépensé…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Échanges de tokens dans la barre latérale : combien de tokens la conversation…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Le petit mot honnête de claude code : après chaque tour, Claude murmure une…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Evidence-gated plan checklist for Claude Code: approved plans become a…
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Guide communautaire non officiel des mods Claude Code (hooks de fonctions) dans…
- [jsni94/usage-band](https://github.com/jsni94/usage-band) - Claude Code mod: /usage windows as colored bars above the prompt.
- [juro-mont/claude-ev-charging](https://github.com/juro-mont/claude-ev-charging) - Barre de progression de recharge d.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vit dans un bandeau au-dessus de votre prompt Claude Code : il met en…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod qui lit à voix haute les réponses et notifications de Claude Code avec…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod Claude pour lire et rejoindre les conversations entre vos sessions…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods pour Claude Code. PixBar : une créature pixelisée au-dessus de votre…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - mods claude.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Claude Code mods, published as a marketplace.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Deux mods de Claude Code : folio, un panneau de fichiers à côté du chat, et…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph : un graphique en direct de ce que Claude Code sait.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Ne laissez pas votre attention vagabonder pendant que vous attendez la réponse…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Mods Claude Code de Sanmu — une marketplace de plugins (volet latéral de tâches).
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods Code de Claude pour les projets d.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guide des mods de code Claude sélectionnés par la communauté : cas…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Mods Code Claude individuels de la Mod Box, chacun installable séparément.
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Mod Claude Code : protège le cache de requête d.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de code Claude qui affiche ce que fait Claude dans le sous-titre de…
- [Magithar/agent-board](https://github.com/Magithar/agent-board) - A task board several coding agents share: one CLI for any agent, a Claude Code…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - À quel point le contexte de Claude est rempli, quand son cache devient froid et…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod de Claude Code : répondez à Claude point par point, directement sur le…
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod de Claude Code avec des profils d.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Petits mods pour Claude Code : runner-avatar, un petit avatar qui court…
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod de Claude Code : panneau en direct présentant les objectifs, hypothèses…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code mod: /sessions pane to browse and delete sessions with their…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods communautaires pour Claude Code : protections, panneaux et commandes qui…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panneau latéral pour Claude Code : fichiers écrits par Claude, divisions du…
- [minhdevtree/claude-lens](https://github.com/minhdevtree/claude-lens) - A Claude Code mod that shows images, SVGs and PDF pages where they appear…
- [MkGut/claude-tutor](https://github.com/MkGut/claude-tutor) - Mod Claude Code : un tuteur dans la barre latérale qui explique ce que fait…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un panneau latéral discret pour Claude Code : ce que fait cette session, son…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Une heure discrète au-dessus de chaque invite et de chaque réponse dans la…
- [mmedum/spor](https://github.com/mmedum/spor) - Restaure ce que Claude Code replie : les fichiers lus par Claude, les commandes…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de code Claude qui réactive les outils todo pour les modèles qui les…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod Claude Code qui attend une pause sûre, puis transmet votre session ou la…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de code Claude : une ligne par tâche au-dessus du prompt avec la tâche…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jouez au Puissance 4 contre une IA dans Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de code Claude : lorsqu.
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Claude Code mod pour les dépôts partagés par plusieurs agents IA : empêche les…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Installe et configure mes mods Claude Code en une commande.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Des mods amusants et gratuits pour Claude Code qui ne dépensent jamais de…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Un garde-fou pour le SQL dans Claude Code : demande confirmation avant que…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un seul mod pour Claude Code, Windows et le CJK en priorité : aperçus d.
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mods Claude Code : miniatures d.
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - Mods Claude Code créés par l.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Les meilleurs Mods de Claude Code, classés selon ce qu.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Deux Mods Claude pour Claude Code : garde-corps.
- [patrick-lai/claude-craft-shop](https://github.com/patrick-lai/claude-craft-shop) - Craft Shop: a Claude Code mod with a worktree head start, crew dials, a context…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Mods for Claude Code: plugins of function hooks that work in any repository.
- [petershk/explain-permission](https://github.com/petershk/explain-permission) - Mod Claude Code : explique chaque demande d.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panneau latéral de statistiques de session en temps réel pour l.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Divers mods et compétences pour ma configuration Claude Desktop.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods pour Claude Code : safety-guard bloque les commandes destructrices et…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Un crabe Claude en pixel art animé pour Claude Code : il met en scène ce que…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod Claude Code : ticker boursier en direct, volet /quote, alertes de prix…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Mods Claude Code, publiés sous forme d.
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Mod Claude Code : une passe de rêve qui fusionne, réécrit et élague le dossier…
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude mod Code : Claude utilise vos secrets sans les voir.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - Un mod Claude Code qui garde les secrets hors de la transcription de session…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod Claude Code : hôte SSH, RAM et limites d.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Claude Code : des pompes à faire pendant que Claude travaille. Aucun token.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Three dependency-free mods for Claude Code: a responsive statusline, a…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code : transforme le plan que vous approuvez en mode plan en une…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Une liste soigneusement sélectionnée de mods Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode sans coût : les agents auxiliaires fonctionnent sur Haiku, et les gros…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Une bande-son lofi qui suit la session : calme, concentration, fluidité, ainsi…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Apprenez pendant que Claude code : après un tour ayant modifié le code, une…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Un enregistrement de chaque modification effectuée par Claude : rejouez chaque…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Claude Code mods: token-bar, your context window and usage limits above the…
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod Claude Code pour le contexte, la croissance, le quota, le cache, le coût…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Mods Claude Code personnels.
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Mods Claude Code, installables comme un marketplace de plugins…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - Le DOOM original dans un panneau Claude Code, sans rien à installer : le moteur…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Marketplace de mods Claude Code personnels : clean-view, where-am-i…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Mods Claude Code (hooks de fonctions) : panneau d.
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Empêchez les agents auxiliaires de Claude (sous-agents) d.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Messages de commit en un clic pour Claude Code avec une Malenia en pixel art…
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - 직접 만든 Claude Code mod 모음 (플러그인 마켓플레이스).
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Mods Claude Code — marketplace sunkanxx-mods.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de code Claude qui affiche l.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod Claude Code qui affiche la session actuelle dans un panneau : chaque…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins Claude Code de mods : des plugins function-hooks qui…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Écoutez les réponses de Claude Code pendant que la phrase lue est mise en…
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Mods Claude Code de Tempered Works : ship-state, timeline, limit-resume — plus…
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Des mods Claude Code petits, amusants et utiles.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code : barre de progression animée et résumé de complétion pour les…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Trois petits mods Claude Code : voyez quand vos sous-agents auront terminé…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Réduit la taille des grandes captures d.
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Dites « I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Affiche des prompts suivants suggérés au-dessus de la zone de prompt.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Posez à Claude une question annexe dans un panneau à côté de votre travail.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code vous envoie un message sur Telegram lorsqu.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Un mod de Claude Code : surligneur pour les réponses, panneau latéral pour les…
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods pour Claude Code : barre des limites d.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod pour Claude Code : secrets masqués, tâches à faire, vérifications et CI…
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
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — générez des carrousels Xiaohongshu et des paires…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline élégant de style vim pour Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Examinez le diff de votre agent de programmation dans un panneau de terminal et…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de ligne d.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Créez des mods pour Claude Code : interceptez toute requête, modifiez toute…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Tableau de bord complet de ligne d.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon : suivez l.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Une ligne d.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agent de jeu de rôle longue durée DeepSeek Harness（plugin de taverne DSH）…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills et mods publics pour Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, sous-agents, hooks, commandes slash et guides pour Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs légaux gratuits et agents de codage — mise à jour automatique…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Calculateur de coûts rapide et sans dépendances, avec ligne d.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Ligne d.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Scores, calendriers et classements de football en direct pour les…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plan de contrôle local pour Claude Code sur Windows et macOS : changez de…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill qui transforme votre agent de codage en expert des firmwares de…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horaires de prière, date hégirienne, adhkar, ayah quotidienne, jeûne sunnah…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuration personnelle Claude Code versionnée dans ~/.claude — agents…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Barre d.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Carte flottante des périodes de pointe et de faible activité pour DeepSeek…
- [William2333ZZ/mywork-deepseekharness](https://github.com/William2333ZZ/mywork-deepseekharness) - MyWork — a personal agent on DeepSeek Harness: AI teammates that each own a…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Collection de plugins pour Claude Code, pi et DeepSeek Harness : HUD de barre…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Boîte à outils Claude Code portable pour l.
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuration globale portable de Claude Code : compétences personnalisées…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins Claude Code que j.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods non officiels pour l.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Pont DSH &lt;-&gt; Feishu (Lark), développé en interne (pas un fork) : carte de…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins et de skills Claude Code pour faciliter la création de…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gouvernance des tokens pour Claude Code : le meilleur modèle dirige…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Ligne d.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Dépôt de mods Awesome Media pour Claude Code.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Ligne d.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Configuration simple et utile de la ligne d.
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Marché de plugins pour Claude Code : mods, compétences, agents, hooks, styles…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Affichez la barre d.
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Ligne d.
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Une ligne d.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Affichez les informations d.
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Ligne d.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Équipes d.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Modules complémentaires Claude Code : observateur de point coloré de statut…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Usines logicielles définissables pour Claude Code sur herdr : graphes de…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Ligne d.
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - Personal Claude Code plugin marketplace (todo-pane).
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Une ligne d.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins Code Claude avec baloo : compétences, agent qui vérifie…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Ligne d.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Ligne d.
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Ligne d.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Ligne d.
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Ligne d.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Ligne d.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Barre d.
- [gvart/claude-config](https://github.com/gvart/claude-config) - Ma configuration Claude Code : mod de surveillance des agents, compétences…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Single-line status bar for Claude Code: model, git, context, tokens, cost…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Prévisualisez les images dans Claude Code : survolez une pastille sous une…
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - Ma configuration Claude Code : mods, compétences et plugins.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Synchronisez les tâches de Claude avec Fizzy.do pour une visibilité d.
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Une collection de compétences, mods et autres extensions Claude Code que j.
- [kevinbadi/creatoros-claude-plugin](https://github.com/kevinbadi/creatoros-claude-plugin) - Creator OS pour Claude Code : le connecteur, les compétences et un mod…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Suivez l.
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook de ligne d.
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Installateur d.
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness de Claude Code de Nacho (reglas, tablero, mods).
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Ligne d.
- [Paradigm-Study/claude-share](https://github.com/Paradigm-Study/claude-share) - Shared Claude Code sessions: share a session with a link, teammates join from…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — ligne d.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Compétences et mods pour Claude Code et Cowork — suivi de projet, document de…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Compétences, mods, hooks et ligne d.
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Une ligne d.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Custom Claude Code statusline (upstream: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Configuration et mods Claude Code, avec une bibliothèque de composants…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuration portable de Claude Code.
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Un petit tableau de bord pour Claude Code : pourcentage de contexte, compte à…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Barre d.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuration Claude Code portable : CLAUDE.md, paramètres, ligne d.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Ligne d.
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Suivi des coûts en temps réel et ligne d.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Compétence Claude Code (VS Code, Windows) : aperçus d.
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Une ligne d.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Détecteur de dégradation du contexte 2026 - Mémoire proactive d.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, sous-agents et lignes d.
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Claude Code status line — Claude/Codex usage gauges that stay live while you…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Un constructeur visuel de barres d.
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
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Mod prompt-bar pour Claude Code : limites d.

</details>

<a id="dsh-cordis"></a>

## Écosystèmes de plugins DSH et Cordis

DeepSeek Harness et Cordis atteignent le même objectif par une autre voie : chez eux, le plugin est le mécanisme de mods ; un plugin y équivaut donc à un mod ici.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74363 · TypeScript · 👁️ observed · 0 天</summary>

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
| Étoiles                       | **74363**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐108647 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **108647** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100582 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **100582** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82094 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **82094**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35767 · Go · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **35767**  |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25501 · Python · 🔎 inferred · 19 天</summary>

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
| Étoiles                       | **25501**  |
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
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4508 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **4508**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4294 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **4294**   |
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
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Le premier terminal virtuel au monde pour les agents IA

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **3682**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1999 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1999**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1856 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **1856**   |
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
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1591 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Protection avant exécution pour les agents de codage IA. Elle bloque les commandes Git et système de fichiers destructrices, ainsi que les tentatives courantes d'accès aux fichiers sensibles, avant l'exécution d'un appel d'outil. Compatible avec Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode et Pi.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1591**   |
| Dernière mise à jour du dépôt | 2026-10-11 |
| Première apparition           | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **1410**   |
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
<summary>🧵 <b><a href="https://github.com/PC2005-cloud/dsh-pet">PC2005-cloud/dsh-pet</a></b> · ⭐1257 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

DSH 桌面宠物：一行命令装好即用的透明动画小桌宠，支持多开、大小位置随心配置；还内置 DIY 素材链，能用 AI 视频自造专属宠物

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **1257**   |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `deepseek-harness` · `desktop-pet` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pc2005-cloud--dsh-pet/2b101f3bcf23988f.png" width="100%" alt="PC2005-cloud/dsh-pet screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pc2005-cloud--dsh-pet/9f4b7093fcbfacf4.gif" width="100%" alt="PC2005-cloud/dsh-pet animation"><br><sub>enregistrement animé</sub></td>
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
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

📚 Une bibliothèque de micro-leçons sans dépendances, adossée à git, permettant aux agents IA de partager et rechercher de manière asynchrone des expériences de débogage vérifiées. | https://misakanet.org

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
| Première apparition           | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>aucun média publié</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Han-1413141/dsh-cost-meter">Han-1413141/dsh-cost-meter</a></b> · ⭐390 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Cost tracking for DeepSeek Harness: session and model costs, token usage, budgets, provider balances, and coding-plan quotas. Bilingual English/Chinese UI.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | JavaScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **390**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `cost-tracking` · `deepseek` · `deepseek-api` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/han-1413141--dsh-cost-meter/ea3a53e99a515021.png" width="100%" alt="Han-1413141/dsh-cost-meter screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐285 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Ouvrez simplement votre navigateur — faites tout votre travail.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **285**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **176**    |
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
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 1 天</summary>

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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐162 · Python · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **162**    |
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
<summary>🧵 <b><a href="https://github.com/drewnekota/cetus">drewnekota/cetus</a></b> · ⭐146 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

One macOS app for Claude Code, Codex, and every agent runtime you use — scheduled runs, global hotkey launcher, per-run git worktrees, one review board.

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **146**    |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `ai` · `ai-agent` · `ai-agents` · `automation` · `claude-code` · `codex` · `coding-agent` · `computer-use`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/drewnekota--cetus/97952f3eefa1f1eb.png" width="100%" alt="drewnekota/cetus screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/drewnekota--cetus/729e7a8aa22d8966.gif" width="100%" alt="drewnekota/cetus animation"><br><sub>enregistrement animé</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐136 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **136**    |
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
<summary>🧵 <b><a href="https://github.com/xcisxc29/dsh-wechat">xcisxc29/dsh-wechat</a></b> · ⭐112 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Étoiles                       | **112**    |
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
<summary>🧵 <b><a href="https://github.com/kenz1117/dsh-ui-usage-billing">kenz1117/dsh-ui-usage-billing</a></b> · ⭐77 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Résumé

Usage billing dashboard plugin for DeepSeek Harness: sidebar cost metrics, real usage aggregation from session logs, current multi-provider pricing catalog

##### 📌 Informations générales

| Champ     | Valeur                                                                                   |
| --------- | ---------------------------------------------------------------------------------------- |
| Catégorie | `Écosystèmes de plugins DSH et Cordis`                                                   |
| Source    | `déclare un mod, un plugin ou un hook, mais rien de spécifique sur l’interface des mods` |
| Langage   | TypeScript                                                                               |

##### 📊 Données

| Indicateur                    | Valeur     |
| ----------------------------- | ---------- |
| Étoiles                       | **77**     |
| Dernière mise à jour du dépôt | 2026-10-12 |
| Première apparition           | 2026-10-12 |

🏷 `billing` · `dashboard` · `deepseek-harness` · `deepseek-harness-plugins` · `dsh` · `dsh-bundle` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Image</th><th align="center" width="50%">🎬 Vidéo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kenz1117--dsh-ui-usage-billing/f3c59d67919ea128.png" width="100%" alt="kenz1117/dsh-ui-usage-billing screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kenz1117--dsh-ui-usage-billing/38fba69ac8bb173c.gif" width="100%" alt="kenz1117/dsh-ui-usage-billing animation"><br><sub>enregistrement animé</sub></td>
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
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 1 天</summary>

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
<summary><b>Plus dans cette catégorie</b> <sub>· 72</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Une liste sélectionnée des meilleurs plugins IA remarquables pour les…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin DSH — modèles OpenCode Zen gratuits pour DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Marché de plugins DSH / DSH Plugin Marketplace : parcourez, installez et mettez…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins pour des logiciels qui itèrent sur eux-mêmes — le…
- [ZASENJC/dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) - Marché de plugins qui classe, répertorie et vérifie automatiquement les plugins…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana: DeepSeek Harness as a subagent for HanaAgent.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Répertoire sélectionné de plugins DeepSeek Harness (DSH) — plus de 280 plugins…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Plugin maître des ressources de jeu dsh.
- [Links2008/DeepSeek-Harness-Desktop](https://github.com/Links2008/DeepSeek-Harness-Desktop) - Version de bureau de DeepSeek Harness Windows, prenant en charge les…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Plugin DeepSeek Harness : associez les fenêtres de contexte des modèles en un…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT : système d.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Alternative open source à GrokBot basée sur DeepSeek Harness.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Collection de plugins d.
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - Classement et recommandations transparents de l.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, outils, compétences et ressources d.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin gestionnaire de serveur MCP pour DeepSeek Harness : page Settings → MCP…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de négociation commerciale A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Panneau Toolbox pour DeepSeek Harness Web : gestionnaire de MCP.
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Marché de plugins vérifiés et registre autonome pour DeepSeek Harness.
- [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution plugin for DeepSeek Harness: versioned, auditable…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un vrai PowerPoint, pas du HTML. Indiquez à votre IA les sujets à couvrir et…
- [ppy-web/dsh-plugin-xiaomi-mimo-tts](https://github.com/ppy-web/dsh-plugin-xiaomi-mimo-tts) - 给DSH接入免费的 Xiaomi MiMo TTS API，支持使用预置/自定义/浏览器内置声音朗读正文.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Graphe de connaissances du code et harness de contexte local d.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Registre de données ouvertes filtré contre le spam pour les plugins, bundles et…
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - Une liste sélectionnée de plugins pour DeepSeek Harness (dsh) — liste…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Plugin d.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Transformez les modèles déjà connectés sur l.
- [xxww0098/dsh-plugin-oauth-subs](https://github.com/xxww0098/dsh-plugin-oauth-subs) - ChatGPT Codex and xAI Grok subscription OAuth for DeepSeek Harness — PKCE /…
- [dabaicai001/star-dsh-desktop](https://github.com/dabaicai001/star-dsh-desktop) - StarHub — All-in-One DevOps Desktop Command Center.
- [evoelsewhere/evoflux](https://github.com/evoelsewhere/evoflux) - Evoflux is an open-source, local-first workspace where AI agents build…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - équipe du plugin dsh.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Tests de compatibilité permanents pour les plugins DeepSeek Harness : versions…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Compression agressive du contexte pour les agents privilégiant le local.
- [liuup/dsh-latex-tools](https://github.com/liuup/dsh-latex-tools) - ♾️ Copy and export the LaTeX in DeepSeek Harness 悬停任意 LaTeX 公式即可复制 TeX…
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - Repair DeepSeek Harness sessions that refuse to load. 修好打不开的 DSH 会话文件.
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Compression protégée du contexte pour DeepSeek Harness (dsh) : LLM propose, les…
- [morlay/dsh-plugin](https://github.com/morlay/dsh-plugin) - dsh plugins.
- [1321928757/dsh-mysql](https://github.com/1321928757/dsh-mysql) - MySQL connector plugin for DeepSeek Harness: configure connections in settings…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin hôte DeepSeek Harness qui conserve les documents du projet et la mémoire…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayons X pour les plugins DeepSeek Harness : capacités déclarées comparées au…
- [fan56/dsh-subagent-registry](https://github.com/fan56/dsh-subagent-registry) - dsh plugin: register ~/.dsh/agents/*.md as dsh-callable subagents.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH : fenêtre d.
- [studyzy/dsh-suggest-prompt](https://github.com/studyzy/dsh-suggest-prompt) - dsh-plugin 根据AI回复给出建议的下一个提示词.
- [yu502950715yang/dsh-use-wallpaper](https://github.com/yu502950715yang/dsh-use-wallpaper) - 把 Wallpaper Engine 动态壁纸搬进 DeepSeek Harness 的 Web GUI：浏览器内实时渲染 scene 壁纸.
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - Classement et répertoire des plugins DeepSeek Harness (DSH)｜Classement /…
- [aaronlei/dsh-web-search-diy](https://github.com/aaronlei/dsh-web-search-diy) - DeepSeek Harness（DSH）网页搜索提供方插件：把内置 web_search 工具接到 OpenAI 兼容 Responses API 及其原生…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espace de travail multi-dossiers : permet à l.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Registre consultable des plugins DeepSeek Harness avec listes sélectionnées et…
- [milisp/keke-agent](https://github.com/milisp/keke-agent) - Lightweight coding agent harness built in Rust for zero vendor lock-in.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standard de vérification sans dépendances pour les plugins DeepSeek Harness…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Marché de plugins DeepSeek Harness — parcourez, recherchez et installez les…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode sur DeepSeek Harness — plugin DSH qui permet à OpenCode Zen + Go…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins tiers et gestionnaire de cycle de vie…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx est un espace de travail de bureau extensible et centré sur l.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Agent de programmation complet pour DeepSeek Harness — flux de travail de type…
- [jerryxff26-alt/dsh-delivery-board](https://github.com/jerryxff26-alt/dsh-delivery-board) - DeepSeek Harness (dsh) plugin: delivery board with stage pipeline, handoff…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Famille de plugins d.
- [lnyuqian/dsh-skill-sidebar](https://github.com/lnyuqian/dsh-skill-sidebar) - dsh-skill-sidebar 技能面板：DSH 右侧边栏技能面板（Skills panel）— 扫描本机技能目录列出全部技能，4-6 字功能短语 +…
- [memorax-ai/dsh-webui-studio](https://github.com/memorax-ai/dsh-webui-studio) - DeepSeek WebUI Studio for interactive, visual-first client plugin development.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite communautaire de déploiement et d.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web DeepSeek Harness (DSH) : onglet latéral market-dashboard de suivi du…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Rend réessayable une tentative vide du modèle sans attribution, pour la seule…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Évaluation de la progression pour les cycles d.
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - plugin dsh : transforme un arrêt pour longueur tronquée en récupération de…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins qui nettoient après leur passage : un portage de Swift 6 du framework…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins Rust avec un noyau de cycle de vie vérifié par Verus et…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Marché de plugins dsh - basé sur GitHub topic:dsh-plugin pour la découverte…

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
| TypeScript | 378     | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 83      | `1na-ko/dsh-hdc-bridge`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                   |
| Python     | 37      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 26      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 15      | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Rust       | 8       | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| Go         | 6       | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| PowerShell | 2       | `GoSlowPoke168/claude-statusline`, `Gabriel-Dalton/claude-statusline-tokens`                                  |
| C          | 1       | `reporails/arcade`                                                                                            |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                          |
| MDX        | 1       | `jkf87/mod-guide`                                                                                             |
| Swift      | 1       | `eovidiu/cordis-ios`                                                                                          |

<sub>Seules les entrées qui déclarent un langage sont comptabilisées. Les entrées de documentation et de discussion sont exclues de ce tableau.</sub>

## Contribuer

Les corrections sont les bienvenues et constituent le moyen le plus rapide d’améliorer cette liste. Ouvrez une issue ou une pull request si une entrée est mal classée, mal évaluée, ou si un projet a été exclu à tort en raison d’une homonymie — c’est la catégorie dans laquelle les filtres automatisés risquent le plus de se tromper.

---

<sub>Projet communautaire indépendant. Non affilié à Anthropic, qui ne l’a ni approuvé ni évalué. Claude Code, Claude et Anthropic sont des marques commerciales de Anthropic. Le comportement des produits peut changer sans préavis ; vérifiez tout élément critique dans la documentation officielle. Les ressources restent la propriété de leurs projets d’origine et ne sont reproduites que lorsque la licence l’autorise.</sub>

<sub>Dernière mise à jour · 2026-10-12T10:26:44+08:00</sub>
