<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods increíbles de Claude">
</p>

<h1 align="center">Mods increíbles de Claude</h1>

<p align="center"><b>El índice de mods y plugins de Claude Code, clasificados según la evidencia, y del comportamiento más profundo que modifican.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-506-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <b>Español</b> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice activo** · Última sincronización: `2026-10-11T21:12:49+08:00` (UTC+8)
> · Entradas: **506** · Añadidas en la última actualización: **0** · Lenguajes de implementación: **12**

<sub>Todas las entradas siguientes se recopilaron, filtraron y revisaron de nuevo automáticamente. Nada de lo que aparece aquí es contenido promocional de pago.</sub>

<a id="featured"></a>

## Selecciones del momento

<sub>Una entrada por categoría, clasificadas según el nivel de evidencia y las estrellas, y recalculadas con cada actualización. Es una clasificación, no una recomendación; cada selección enlaza con su ficha completa más abajo. Se prefieren los proyectos que han publicado una captura de pantalla o una grabación, para que la franja siga siendo visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9473 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2534 · Python · 👁️ observed</sub>
<sub>Encuentra los tokens fantasma. Arréglalos. Sobrevive a la compactación. Evita el deterioro de la calidad del contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74325 · TypeScript · 👁️ observed</sub>
<sub>🌊 El agent harness original. Implementa enjambres inteligentes de varios agentes, coordina flujos de trabajo autónomos y crea sistemas de IA conversacional. Incluye…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Contenido

- [Qué es un mod de Claude Code](#qué-es-un-mod-de-claude-code)
- [Cómo se evalúan las entradas](#cómo-se-evalúan-las-entradas)
- [Oficiales: repositorios propios y notas de versión de Anthropic](#oficiales-repositorios-propios-y-notas-de-versión-de-anthropic) — **15**
- [Mods: creados con la capacidad de mods](#mods-creados-con-la-capacidad-de-mods) — **381**
- [Ecosistemas de complementos de DSH y Cordis](#ecosistemas-de-complementos-de-dsh-y-cordis) — **99**
- [Escritura, debates y vídeos](#escritura-debates-y-vídeos) — **11**
- [Proyectos por lenguaje de implementación](#proyectos-por-lenguaje-de-implementación)

## Qué es un mod de Claude Code

Claude Code incorporó los **mods** en la versión 2.1.287: extensiones que pueden cambiar el comportamiento más profundamente que un plugin y dibujar su propia interfaz.

Un mod puede conectarse a `ui.render` para dibujar una **fila, banda, panel o tarjeta** alrededor del prompt, leer el texto que seleccionaste por última vez con `$.ui.selection()`, generar compañeros de equipo con `agent.spawn` y hacerse cargo de una región de `Client`. Si un mod falla al dibujar, solo falla él: `ui.fault` evita que un mod defectuoso cierre la sesión.

Esta lista incluye mods, la superficie de plugins y hooks sobre la que se construyen, y sus equivalentes en DSH y Cordis. Deliberadamente, **no** incluye el ecosistema más amplio de Claude Code: un paquete de prompts no es un mod.

## Cómo se evalúan las entradas

La mayoría de las listas de este ámbito afirman que algo está incluido. Esta explica cuánto se ha verificado realmente y permite filtrar en consecuencia. Una categoría describe las pruebas disponibles, no la calidad del proyecto: un mod bien construido del que aún no ha escrito nadie sigue siendo `inferred`.

| Evaluación                                                                        | Qué significa                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `publicado por Anthropic mismo`                                                   | Publicado por Anthropic mismo, o leído directamente en el registro de cambios oficial.                                                                                                                           |
| `su propio texto menciona un mod API o declara la capacidad de modding`           | Su propio texto menciona una parte de la superficie de mods —`ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, un panel, banda o tarjeta—, por lo que el autor describe algo creado sobre el API real. |
| `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` | Se describe como un mod, plugin o hook, pero nada de su texto menciona específicamente la superficie de mods. Es real, pero no está confirmado.                                                                  |
| `coincide únicamente por vocabulario`                                             | Coincide únicamente por vocabulario. Se incluye para que el filtro sea auditable, no porque se considere fiable.                                                                                                 |

<a id="official"></a>

## Oficiales: repositorios propios y notas de versión de Anthropic

Los repositorios propios de Claude Code de Anthropic, y las versiones que definieron la superficie de mods. Léelos desde el código fuente en lugar de resumirlos.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150151 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Resumen

Claude Code es una herramienta de programación agéntica que funciona en tu terminal, comprende tu base de código y te ayuda a programar más rápido ejecutando tareas rutinarias, explicando código complejo y gestionando flujos de trabajo de git, todo mediante comandos en lenguaje natural.

<sub>🔧 Encontrado en el código: `feed.xml`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |
| Lenguaje  | TypeScript                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **150151** |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9473 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |
| Lenguaje  | TypeScript                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **9473**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |
| Lenguaje  | Python                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **8248**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

##### 📝 Resumen

An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |
| Lenguaje  | Python                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6342**   |
| Último envío      | 2026-02-11 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |
| Lenguaje  | Shell                                                             |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1797**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Resumen

Supplementary materials for Claude Model Cards

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **25**     |
| Último envío      | 2025-12-05 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Se añadieron los Mods de Claude: ahora los plugins pueden modificar comportamientos más profundos. Se añadió You should know, un mod integrado donde un agente secundario te cubre las espaldas y señala cosas que tú o Claude podrían pasar por alto. Actívalo con `/plugin enable cc-plugin-you-should-know@builtin` (para sesiones propias con telemetría activada)

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Se añadió `$.ui.selection()` para mods: devuelve el texto que seleccionaste por última vez en modo de pantalla completa y, cuando la selección está dentro de una fila de transcripción, devuelve esa fila. Se corrigió que el botón de un mod a veces ejecutara la acción de otro botón al pulsarlo en una vista dibujada antes de que Claude Code se reiniciara. Se corrigieron las sesiones de pantalla completa que salían con «unrecoverable interface error» al abrir el diálogo de tareas en segundo plano mientras un plugin o mod mostraba filas sobre el aviso. Se corrigió que `claude plugin test` informara de que los mods estaban desactivados remotamente cuando solo había leído una configuración guardada obsoleta

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Se corrigió que una regla de denegación o consulta sobre una parte anidada de un comando shell compuesto no prevaleciera sobre la aprobación de un mod instalado por el usuario en máquinas administradas. Se corrigió que los mods instalados no se cargaran en la primera sesión tras una actualización. Se añadió `agent.spawn` para compañeros de equipo, un id de agente en todos los eventos de hooks de plugins y estados de inactividad y espera en `$.agent.list()`. Se corrigieron las sesiones que terminaban con «unrecoverable interface error» cuando un valor escrito por el hook `ui.render` de un mod hacía que una fila fallara al dibujarse; ahora el motor dibuja su propia fila. Se corrigió que el contenido alineado a la derecha del panel o banda de un mod se dibujara debajo de la marca de cierre o `\[-\]`, wh

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Añadido `serverToolUses` al resultado del hook `turn.step` de un mod: las llamadas a herramientas que ejecutó el propio API (el asesor), cada una con su id, nombre, entrada, inicio y fin. Añadido `ceiling` a la pregunta y veredicto que lee el hook `tool.check` de un mod, nombrando la aprobación que una organización requiere para una herramienta. Añadidos los tipos `ThemeKey` y `Color` a los typings de hooks de plugins, para que un editor liste los colores de tema que el dibujo de un mod puede nombrar. Añadido a `claude plugin validate`: cada hook que un mod registra en un sitio de gating se lista con si tiene un `.catch` (`gatingHooks` bajo `--json`). Corregido el resultado `turn.step` de un mod

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Añadido `prompt.autocomplete`, un evento al que un mod se engancha para añadir sus propias filas a la lista de autocompletado del cuadro de prompt Añadido almacenamiento en caché de prompts a `$.model.complete` para mods: `prompt` y `system` toman bloques de texto, y `cache: true` en un bloque almacena en caché la solicitud hasta ese punto Añadidos agentes de flujo de trabajo al hook del mod `agent.spawn`, con su ejecución e índice, para que un mod pueda rechazarlos Corregidas las filas Write, Edit, NotebookEdit y LSP, y filas únicas Read, Grep y Glob, ocultando por qué un mod denegó la llamada: ahora la fila muestra el motivo Corregido el hook `config.set`, `state.set`, `env.set` o `agent.spawn` de un mod que deniega despué

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Se añadió `isDeferred` a `$.tool.register` para los mods: `false` muestra el esquema de la herramienta en el prompt desde el principio en lugar de ocultarlo tras la búsqueda de herramientas. Se corrigieron los hooks de un mod en eventos de `classic.*` que se omitían mientras se reiniciaba el worker de hooks del plugin, lo que hacía que los hooks de configuración respondieran sin ellos. Se corrigió `claude plugin test`, que fallaba con mods que llaman a `$.session.append`; las pruebas pueden volver a leer las filas añadidas con el nuevo `mock.session`

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-08 |

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Se añadió `$.ui.notify` para los mods: muestra una notificación nativa mediante…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Corregido Esc o una interrupción durante un hook de `UserPromptSubmit` o un…
- [riffkit/skill](https://github.com/riffkit/skill) - Official Riffkit skill — riff a winning TikTok into your own short video from…

</details>

<a id="mods"></a>

## Mods: creados con la capacidad de mods

Cada entrada aquí muestra pruebas de que usa la capacidad que Claude Code obtuvo en 2.1.287: renderiza mediante `ui.render`, incluye un panel, una banda o una tarjeta, lee `$.ui.selection()`, genera compañeros con `agent.spawn`, o afirma claramente que es un mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Encuentra los tokens fantasma. Arréglalos. Sobrevive a la compactación. Evita el deterioro de la calidad del contexto.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | Python                                                                  |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2534**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>grabación animada</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐484 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Catálogo comunitario de mods públicos de Claude Code (hooks de funciones), analizados desde GitHub con información sobre lo que cada mod puede leer, escribir, ejecutar o enviar por la red. Explora https://mods.aidojo.si/

<sub>🔧 Encontrado en el código: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **484**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Mantén caliente la caché del prompt de Claude Code durante las pausas y muestra el coste estimado antes de un envío en frío.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **127**    |
| Último envío      | 2026-10-04 |
| Primera inclusión | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>grabación animada · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Un CLI de QA nativo para agentes en páginas web. Determinista, sin necesidad de escribir pruebas y sin LLM.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | HTML                                                                    |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **104**    |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐93 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Skins para Claude Code: filas de herramientas con iconos, tarjetas de diferencias, tablas y gráficos Mermaid, una banda de uso y quince temas. /skin los cambia al instante.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **93**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Respuestas coloridas y personalizables por temas de Claude Code: tablas, código, diagramas, gráficos y filas de herramientas en 15 temas, con botones de copia. Un mod de Claude Code.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **74**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Un mod de Claude Code que coloca un panel de agente en vivo en tu terminal: contexto y coste, cronología del asesor, cada comprobación de permisos, tarjetas de subagentes y carriles.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **66**     |
| Último envío      | 2026-10-02 |
| Primera inclusión | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/claude-code-mods">karanb192/claude-code-mods</a></b> · ⭐40 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Mods de Claude y las herramientas para crearlos: primero una skill de creación y después los mods

<sub>🔧 Encontrado en el código: `plugins/mod-builder/skills/mod-builder/references/migrate.md`, `plugins/mod-builder/skills/mod-builder/references/nouns.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **40**     |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Observa cómo Claude Code crea un pequeño dibujo animado mientras trabajas.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **32**     |
| Último envío      | 2026-10-02 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Una barra con los prompts de tu sesión de Claude Code: pasa el cursor para leerlos y haz clic para saltar a ellos (hooks de funciones / Mods)

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **27**     |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐24 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Claude Code muestra imágenes y reproduce vídeos directamente en tu terminal: capturas de pantalla, grabaciones de Playwright y control de calidad sincronizado antes / después. Ghostty y kitty.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **24**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/9ee7df00aee28636.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/adcbff13953c23f1.gif" width="100%" alt="iamumeransari/claude-show-your-work animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Una mejora radical para Claude Code: un panel de cabina en directo, temas compartibles y una mascota pixelada que representa lo que está haciendo Claude

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **23**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Claude Code mod: contexto en tokens, límites de 5 horas y semanales frente al reloj, cuenta atrás de la caché de prompts, coste de la sesión y agentes en ejecución, todo en una banda sobre el prompt.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **11**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Pixel art animado sobre tu prompt de Claude Code que reacciona mientras Claude trabaja. Siete escenas, o tu propia imagen o GIF. Cero tokens.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **10**     |
| Último envío      | 2026-10-04 |
| Primera inclusión | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

##### 📝 Resumen

Seguimiento de sesiones para Claude Code creado como mods: ventana de contexto, consumo de cuota del plan y coste por turno

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **8**      |
| Último envío      | 2026-09-15 |
| Primera inclusión | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>grabación animada</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Markdown, pintado en el cuadro de texto de Claude Code mientras escribes. El código delimitado se convierte en una tarjeta con resaltado de sintaxis antes incluso de que cierres el delimitador.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **7**      |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Mods para Claude Code: plugins de enlaces de funciones que añaden paneles activos y comportamiento a la interfaz de terminal

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Panel GSD en vivo para Claude Code: roadmap, árbol de agentes con forks, contexto y coste, flujos de trabajo y lector de markdown para .planning. Solo lectura.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6**      |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/a31036b15398e820.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Resumen

Mod (plugin) de Claude Code que añade un panel lateral con pestañas Activity, Files, Agents, Context y MCP, una línea de estado sobre el prompt, un chat rediseñado, diagramas Mermaid en la terminal, tablas y paneles de código y diff. Los colores siguen tanto /color como /theme (dark, light y otros).

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6**      |
| Último envío      | 2026-10-06 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Tu plan, observándose a sí mismo. Árbol local de hoja de ruta de escritorio que Claude Code y cualquier host MCP mantienen actualizado en directo. JSON sin formato, sin nube.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/leopiney/wolfbud-claude-mod">leopiney/wolfbud-claude-mod</a></b> · ⭐5 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Resumen

Compañero de voz para Claude Code. Habla sobre tus ideas con un lobo 3D impulsado por la IA conversacional de ElevenLabs; cuando estés de acuerdo, envía el prompt a Claude y habla cuando Claude haya terminado.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **5**      |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/leopiney/wolfbud-claude-mod/main/assets/banner.png" width="100%" alt="leopiney/wolfbud-claude-mod screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HMarzban/claude-mod">HMarzban/claude-mod</a></b> · ⭐4 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

查看下一条Claude Code消息的成本：提示词上方的实时横幅显示提示词缓存倒计时、重新预热价格、会话成本、上下文以及5小时/每周使用限额。

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **4**      |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-ai` · `claude-code` · `claude-code-plugin` · `claude-mod` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dominicrico/jev-router">dominicrico/jev-router</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Plugin de Claude Code: enrutamiento automático de modelos Claude. Selecciona Haiku, Sonnet u Opus y el esfuerzo de razonamiento para cada prompt, paso y subagente; límite de esfuerzo, protección de la caché del prompt, banda de estado y benchmarks.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-09 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-marketplace` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/e9ab68584ed9c404.jpg" width="100%" alt="dominicrico/jev-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/2a6620c49438b369.gif" width="100%" alt="dominicrico/jev-router animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/FynnXland/fynn-mods">FynnXland/fynn-mods</a></b> · ⭐3 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Resumen

Seis mods para Claude Code: mascota Clawd animada, barras de límite de uso y caché de prompts, verificador de mensajes antes del envío, respuestas rápidas, cola de tareas pendientes y libro de costes. Terminal y app de escritorio, inglés/alemán.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3**      |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-07 |

🏷 `ai-coding-assistant` · `claude` · `claude-ai` · `claude-code` · `claude-code-marketplace` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mertkayacs/ultramod">mertkayacs/ultramod</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

El mejor paquete de mods todo en uno para Claude Code: límites de uso y HUD del contexto, protección con deshacer para rm -rf y git reset --hard, protección de .env y secretos, y un recibo por cada turno. Diez mods, una instalación.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-09 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/0f9d8b2253819dc8.gif" width="100%" alt="mertkayacs/ultramod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/1537defa7233d7f2.gif" width="100%" alt="mertkayacs/ultramod animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mthli/cc-shorts">mthli/cc-shorts</a></b> · ⭐3 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Reproduce YouTube Shorts en tu Claude Code 💃

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3**      |
| Último envío      | 2026-10-02 |
| Primera inclusión | 2026-10-10 |

🏷 `claude-mods` · `youtube-shorts`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mthli--cc-shorts/ef652fff732c023d.png" width="100%" alt="mthli/cc-shorts screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/chenyuxiaojin/cyxj-notch">chenyuxiaojin/cyxj-notch</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Panel del notch de macOS para Claude Code: límites de uso, sesiones abiertas, progreso de tareas, cuenta atrás de la caché de prompts y tareas pendientes — alimentado por cinco mods de Claude Code (incluidos).

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools` · `dynamic-island` · `macos` · `menu-bar`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Christandoh/context-cache">Christandoh/context-cache</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Claude Code mod: context usage, session / weekly / Fable limits and prompt-cache temperature above the prompt

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/christandoh--context-cache/3cdd3b2c5a09da7d.png" width="100%" alt="Christandoh/context-cache screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/CodyAMaughan/meme-factory">CodyAMaughan/meme-factory</a></b> · ⭐2 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Recién salido de fábrica. Un mod de Claude Code: pide un meme y sigue trabajando. Los borradores se preparan en un panel lateral; elige, remezcla, aprueba y publica en Slack.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `fun` · `meme-generator` · `memes` · `slack`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/7417dc8940c4a087.png" width="100%" alt="CodyAMaughan/meme-factory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/8c9d44287267796f.gif" width="100%" alt="CodyAMaughan/meme-factory animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/estruyf/claude-stats-mod">estruyf/claude-stats-mod</a></b> · ⭐2 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Un mod de Claude Code que muestra tus límites de uso y gasto en la banda sobre el prompt.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-02 |
| Primera inclusión | 2026-10-10 |

🏷 `claude` · `claude-code` · `claude-mod` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/estruyf/claude-stats-mod/main/assets/desktop.png" width="100%" alt="estruyf/claude-stats-mod screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/i-harsha-reddy/naruto-mod">i-harsha-reddy/naruto-mod</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Un compañero de Naruto en pixel art para Claude Code: 20 ninjas, 60 jutsu, realizados mientras Claude trabaja

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `naruto` · `pixel-art`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lorenzh/rabe">lorenzh/rabe</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Mira lo que Claude Code ejecuta en segundo plano: subagentes, trabajos de Codex, shells, monitores, trabajos de cron y flujos de trabajo.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/macleodlabs-ai/claudeflow">macleodlabs-ai/claudeflow</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

MacLeod Labs开发的Claude Code mods：streams将会话中交错的工作拆分为带颜色标记的流

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/macleodlabs-ai/claudeflow/main/assets/hero.jpg" width="100%" alt="macleodlabs-ai/claudeflow screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/MankhongGarden/claude-code-mods-field-notes">MankhongGarden/claude-code-mods-field-notes</a></b> · ⭐2 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Resumen

Notas de campo del primer día sobre mods de Claude Code en Windows: una barra de combustible de contexto/cuota, un mod de UI tailandesa, una intro de arranque Matrix y un actualizador seguro, además de qué falló y por qué (paneles, bandas encima del prompt, tailandés en Windows Terminal).

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2**      |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-07 |

🏷 `anthropic` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mankhonggarden--claude-code-mods-field-notes/832ffcdb7bad9007.png" width="100%" alt="MankhongGarden/claude-code-mods-field-notes screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 347</sub></summary>

- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 为Claude Code的终端记录打造桌面应用外观的mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un panel lateral para Claude Code: los subagentes que ejecuta una sesión, qué…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel de barra lateral de Claude Desktop (pestaña Code): enumera todas las…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso encima del cuadro de entrada de Claude Desktop (pestaña Code)…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins y habilidades comunitarios de Claude, instalables desde un único…
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una cola de decisiones CLI/TUI para personas que trabajan con agentes…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Tarjeta de estado flotante para Claude Code — modelo, contexto, límites de…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lee los archivos markdown que nombra Claude Code, renderizados junto a la…
- [atomashevic/claude-latex-math](https://github.com/atomashevic/claude-latex-math) - Claude Code mod that typesets the LaTeX math in Claude.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuegos artificiales para Claude Code: cada pulsación, llamada a herramienta…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequeños mods de Claude Code (plugins de function-hook): session-switcher y más.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: límites de plan y contexto sobre el prompt, un coach…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de herramientas Claude de Naren: skills, mods y servidores MCP para Claude…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod de Claude Code que muestra las diferencias de Edit y Write en dos columnas…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Una lista seleccionada de mods de código de Claude Code, instalables como un…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Un plugin de Claude Code muy particular, diseñado por un Rustacean obsesionado…
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 适用于Claude Code的被动攻击式喝水提醒。零token，最大限度的评判.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods de Claude Code de Herman (marketplace herman-mods).
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod de Claude Code: medidores en vivo de coste, contexto y cuota del plan…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Un mod de Claude Code que retiene la distribución de subagentes, las…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod de Claude Code que activa o desactiva tus habilidades, agentes, reglas y…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins (mods) de Claude Code: cambia entre varias cuentas de Claude, supervisa…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de código de Claude probados e instalables con un comando: protecciones…
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Créditos al estilo cinematográfico para tu sesión de programación.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprende un idioma extranjero mientras trabajas con Claude Code.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude Code mods for running many sessions across many repos from one control…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Cuando el agente escribe Java, el código que infringe la convención p3c de…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de coste, tokens y uso del contexto en tiempo real para Claude…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Mod de Claude Code: un registro de seguimientos pendientes sugeridos por Claude…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio por Internet dentro de Claude Code: barra lateral cliamp…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Fun, useful Claude Code mods: a pixel critter above your prompt, a tools menu…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude está cocinando. Chatea con tu escuadrón.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack的Claude Code mods合集.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - 一个Claude Code mod：在Claude工作时，在休闲游戏中捕捉像素艺术Modsters.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Mod todo en uno para Claude Code: un HUD en vivo, protecciones de seguridad…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Una batalla espacial sobre el prompt de Claude Code mientras trabaja.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Ve qué archivos tiene cada agente de Claude Code en su contexto, y cuánto de…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Mantén la cabeza fría. Un termómetro para tus días de Claude Code: cada hora…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - 在Claude Code的提示词页脚和提示词上方，一览提示词缓存、上下文和计划限额.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Mod de Claude Code: un panel en tiempo real de las solicitudes de incorporación…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequeños mods de Claude Code para el terminal y la aplicación de escritorio.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Claude Code mods合集，每个mod都位于独立仓库中：usage-meter、progress-board、session-toc.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod de Claude Code: un panel de progreso para tareas, subagents, ejecuciones de…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Mod de Claude Code: una tabla de contenidos clicable y con marcas de tiempo de…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod de Claude Code: límites de tasa del plan, llenado de contexto, coste de…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidad + mod de Claude CLI que añade palabras en español a las respuestas…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Integra Alarum.me en tu código de Claude CLI o en Desktop.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra lateral al estilo de Evangelion para Claude Code: contexto, cuota…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code que lo rediseña como The Machine de Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：用于强制执行并验证subagents DAG工作流的Claude Code mod，带有实时DAG面板.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código abierto para Claude Code: paneles, líneas de estado…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod de Claude Code: estado de sesión, progreso en vivo de Spec Kit y…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La ventana de contexto como una fila sobre el prompt, dibujada como Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tareas en tiempo real para Claude Code Desktop: una franja sobre el…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuito y de código abierto para Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod that shows images inline in Ghostty and kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un Mod de Claude que muestra las solicitudes de extracción de GitHub de la…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Habilidades de Claude Code: un verificador de hechos de documentación, un…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod de Claude Code: líneas de código de hoy por Claude — nuevas, editadas…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod de Claude Code: rutas clicables en las respuestas;
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Mod de Claude Code: elige /effort para cada prompt con Jev.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compañero de Claude Code: un acompañante ASCII sobre el prompt que…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Modificaciones de Claude Code: capa de seguridad para Claude Code: redacción de…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin y mod de Claude Code: un SDLC nativo de IA.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Colección Awesome de mods de Claude Code | Colección de mods de 클로드 코드.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Un mod de HUD de RPG acogedor para Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Habla: un mod de Claude Code que lee en voz alta, cuando se solicita, las…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de Claude Code bajo demanda — una habilidad que lee tu conversación y crea…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Azota a Claude cuando se equivoca — un mod antiestrés para Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code: pequeños plugins para paneles en tiempo real, enrutamiento…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod y plugin de Claude Code: monitor de uso, rastreador de tokens y línea de…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Tres modificaciones gratuitas de Claude Code: oculta los valores de .env de los…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods de Claude Code. touch-map: muestra qué archivos enumeró, leyó, editó o…
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Marketplace de plugins de Claude Code para los mods de 0xnicholasy…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Modificación de Claude Code: barras de progreso de uso (contexto, 5h, 7d) y un…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Modificaciones de Claude Code: tarjetas de estadísticas de la sesión sobre la…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gato braille animado sobre el prompt de Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code: dirige el trabajo barato a GLM/Kimi mediante un Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gato pixelado sobre el prompt de Claude Code que ejecuta una llamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code que elige un buen momento para compactar y mantener…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods para Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Mercado de plugins de Claude Code de anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Mod de Claude Code: el uso de 5 horas y semanal de tu plan como una sola línea…
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Modificaciones de Claude Code para observar el mercado desde el terminal: panel…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Modificaciones para Claude Code.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - Mis mods privados de Claude Code.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - El barco de LGTM Lines navega tras cada cambio de código: un mod de Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mods de Claude Code para el equipo S2 (el marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Entrenamientos cortos mientras Claude trabaja: un objetivo diario, rachas…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Progreso del plan, las tareas y los agentes junto a la indicación de Claude…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un panel de uso para Claude Code: gasto por modelo.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Un mod de Claude Code: desglose del contexto de la ventana en directo sobre el…
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para Claude Code: Apple Music y Spotify sobre el aviso, con…
- [bitcars/ctx-bar](https://github.com/bitcars/ctx-bar) - ctx-bar: a Claude Code mod that keeps the context window visible at all times.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: reloj de caché, radio de impacto, sugerencias, lista de…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un búho para tu Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Banda de Claude Code de una línea.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - El motor original de Doom con Freedoom, jugable dentro de Claude Code.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Mod de Claude Code: electricidad ⚡ y agua 💧 estimadas detrás de cada turno y…
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Un mod de Claude Code que mantiene una lista continua de los elementos abiertos…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code mods for real Engineers.
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Modificaciones de Claude Code exclusivas para el equipo d3nim.
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Mods de Claude Code: rule-keeper guarda tus correcciones como reglas permanentes.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi que vive dentro de Claude Code: eclosiona, se come el código que…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods para Claude Code, como marketplace de plugins.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Mod de Claude Code: muestra la hora de cada prompt y respuesta en el terminal y…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mods de Claude Code escritos como hooks de funciones y el marketplace que los…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod de Claude Code: después de que un guard bloquee una llamada a una…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod de Claude Code: trabajos en segundo plano en una sola vista, con progreso y…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod de Claude Code: una sola bandeja de entrada para mensajes de compañeros de…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod de Claude Code: explica los bloqueos del sandbox y convierte los bloqueos…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoritos para Claude Code: iconos de un clic para tus comandos y skills.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ¡Ey, lo silencié! Deshazte del diff, corta el riff;
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - Modificaciones para claude.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code mods: delete-guard (confirmar eliminaciones de archivos) y…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod de Claude Code: uso de la suscripción (5h / 7d) como una banda sobre el…
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code mod: your background agents as pixel critters, one sprite per model.
- [FeidaWang/edit-replay](https://github.com/FeidaWang/edit-replay) - Edit Replay: step through the file edits Claude made in the last turn, one diff…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Marketplace de mods de Claude.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar en tiempo real de tus ramas y worktrees paralelos sobre el prompt…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Una modificación de Claude Code para capturar pensamientos durante el trabajo…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Modificaciones y skins para Claude Code: una barra de progreso en directo para…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Mods de Claude Code (plugins de function-hook): banda de contexto, asuntos…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Siete modificaciones de Claude Code: savvy-progress, skins, filetree…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Copiar el enlace con Ctrl+clic en cada bloque de código de las respuestas de…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mods para Claude Code: plugins de hooks, como usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mods de Claude Code (plugins de enlaces de funciones), instalados a través de…
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Modificaciones de Claude Code: context-bar-plus.
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Auditor estático de la cadena de suministro para las modificaciones de Claude…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Modificaciones en alemán para Claude Code: avisos de contexto/caché, puntos…
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code mod: capture ideas into an Obsidian vault inbox from any session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de Claude Code: cuánto tardó cada respuesta, cuánto tiempo pensó Claude y…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mods de Claude Code: el modo streamer oculta los paneles privados, las bandas y…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - para mis modificaciones de claude.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod de Claude Code: espera a que pase el límite de uso de 5 horas y envía…
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Pequeñas modificaciones para Claude Code, empezando por la continuación…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Una cabina sobre tu indicación de Claude Code. El pato lee los medidores.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Pequeñas modificaciones de Claude Code: medidores de contexto y uso del plan…
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: a Claude Code mod with a side pane showing where each work item…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Un mod de Claude Code: un panel para cada subagente, los archivos que toca y el…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel lateral de uso del contexto: total, categorías, crecimiento por ronda…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista lateral de archivos: qué archivos se han creado, modificado o eliminado…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, un conejo belier neerlandés en blanco y negro con estilo de 8 bits, corre y…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel lateral de «Lo que he preguntado»: cada frase que el usuario ha escrito…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Línea de tiempo lateral: en qué se ha empleado el tiempo de esta ronda…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Intercambio de tokens en el panel lateral: cuántos tokens envía la conversación…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - El bocadillo de tofu honesto de claude code: al terminar cada ronda, Claude…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Pequeños mods para Claude Code, como nuevos comandos de barra y paneles…
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Guía comunitaria no oficial de las modificaciones de Claude Code.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive en una banda sobre tu prompt de Claude Code: representa la sesión…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod que lee en voz alta las respuestas y notificaciones de Claude Code mediante…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod de Claude para leer y unirse a las conversaciones entre tus sesiones de…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Mod de Claude Code: subagents en ejecución como mascotas pixel Claude sobre el…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - mods de claude.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Mods de Claude Code (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dos mods de Claude Code: folio, un panel de archivos junto al chat, y tint, un…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph oh what Claude Code knows.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - No dejes que tu atención se desvíe mientras esperas la respuesta de Claude Code.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Modificaciones de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guía de Mods de Claude Code seleccionada por la comunidad: casos de uso…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de Claude Code que muestra lo que Claude está haciendo en el subtítulo…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Un gato negro y esponjoso sobre tu prompt de Claude Code.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod de Claude Code con perfiles de permisos intercambiables: una base…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods de la comunidad para Claude Code: protecciones, paneles y comandos que se…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel lateral para Claude Code: archivos que escribió Claude, divisiones del…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un discreto panel lateral para Claude Code: qué está haciendo esta sesión, su…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Una hora atenuada sobre cada prompt y cada respuesta en la transcripción de…
- [mmedum/spor](https://github.com/mmedum/spor) - Devuelve lo que Claude oculta: los archivos que Claude leyó, los comandos que…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Modificación de Claude Code: uso de la ventana de contexto en el espacio del…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de código de Claude que vuelve a activar las herramientas de tareas para…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de código de Claude: una línea por tarea encima del prompt con la tarea…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Juega Connect Four contra una AI dentro de Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: cuando otro agente de programación hace un commit en tu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositorios compartidos por varios agentes de IA…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods marketplace.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barrera de protección para SQL en Claude Code: pregunta antes de que Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un mod para Claude Code, Windows y CJK en primer plano: vistas previas de…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Los mejores Mods de Claude Code, ordenados por lo que hacen por ti.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Un mod de Claude Code que retiene comandos de shell arriesgados.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dos Mods de Claude para Claude Code: guardaespaldas.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Modificaciones de Claude Code con telemetría de agentes, paneles de cronología…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Insulta a Claude Code y una mano de dibujos animados te devuelve una bofetada.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Modificaciones de Claude Code: usage-both muestra el uso de 5 horas y semanal…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel lateral de estadísticas de sesión en vivo para la pestaña Code de la…
- [PhilRoli/traintracker-claude](https://github.com/PhilRoli/traintracker-claude) - Claude Code mod: pause sessions before your TrainTracker train arrives.
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Mods de Claude Code para la interfaz de pompeitech, con el sistema de diseño…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods para Claude Code: safety-guard bloquea comandos destructivos y el acceso a…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods para Claude Code: plugins function-hook que se ejecutan dentro de la…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod de Claude Code: cotización bursátil en tiempo real, panel /quote, alertas…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code mod: keeps auto-memory up to date in the background after every turn.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod de Claude Code: host SSH, RAM y límites de uso de 5 h/7 d en una fila sobre…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod de Claude Code: flexiones para hacer mientras Claude trabaja. Sin tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 mods de Claude Code en coreano: registro de suposiciones, lenguaje sencillo…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod de Claude Code: convierte el plan que apruebas en modo plan en una lista de…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una lista seleccionada manualmente de mods de código de Claude.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sin coste: los agentes auxiliares se ejecutan en Haiku, y los archivos…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una banda sonora lo-fi que sigue la sesión: calma, concentración y fluidez…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprende mientras Claude programa: después de un turno que haya cambiado el…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una cinta de cada edición que hace Claude: reproduce cada cambio mientras se…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Cada enlace que menciona tu sesión, en una fila sobre el prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Demostración mínima de hooks de funciones de Claude Code: panel de tokens/coste…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Mod de Claude Code: el límite de 5 h, semanal y de Fable como barra sobre el…
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in a terminal pane…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Una colección de plugins para Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: un mod no oficial de fans de Avengers para Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod de Claude Code para contexto, crecimiento, cuota, caché, coste nativo y…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Mod de Claude Code: dirige las interacciones sencillas y los subagentes a…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Mods personales de Claude Code.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - The original DOOM in a Claude Code pane with nothing to install: the engine…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensajes de commit con un clic para Claude Code con una Malenia bailarina en…
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Mods personales de Claude Code.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Repositorio local de mods de Claude Code.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de Claude Code que muestra el uso de tu plan de Claude…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod de Claude Code que muestra la sesión actual en un panel: cada aviso, el…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins de Claude Code de mods: plugins function-hooks que…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Repositorio para gestionar mods de Claude.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Personalizaciones para Claude Code.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Algunos mods de Claude.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Mod de Claude Code que comprueba el inglés de tu prompt mientras lo escribes.
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Un catálogo seleccionado de mods de Claude Code, cada uno con un prompt para…
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Mods de Claude Code: un medidor de contexto y límite del plan sobre el prompt…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod de Claude Code: cuota de 5h/7d, ventana de contexto, tiempo restante de la…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod de Claude Code: banda de progreso animada y resumen de finalización para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tres pequeños mods de Claude Code: descubre cuándo terminarán tus subagentes…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Reduce capturas de pantalla grandes antes de que Claude las lea, para que las…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di «I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Muestra los siguientes prompts sugeridos encima del cuadro de prompt.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Hazle a Claude una pregunta aparte en un panel junto a tu trabajo.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace de mods de Claude Code con instalación en un paso y guía en vídeo…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Cuenta atrás de los límites de frecuencia y previsión del ritmo de consumo para…
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin de Claude Code: tus límites de uso de Claude Pro/Max con una previsión…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para Claude Code. agent-crew: observa trabajar a tus subagentes como un…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Matemáticas en LaTeX en línea y visibles, además de figuras TikZ opcionales, en…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Un panel de tareas en directo para Claude Code: planifica antes de construir…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod de Claude Code que informa en directo de qué archivos cambió Claude y por…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una colección cuidadosamente seleccionada de los mejores recursos para los…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin de Claude Code que muestra lo que está ocurriendo: uso del contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Línea de estado atractiva y altamente personalizable para Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas las partes del indicador de sistema de Claude Code, las descripciones de…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Más de 45 consejos para sacar el máximo partido a Claude Code, desde los…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline elegante al estilo de vim para Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revisa el diff de tu agente de programación en un panel de terminal y envía…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de línea de estado completo para Claude Code con uso de contexto…
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agente de rol de larga duración para DeepSeek Harness (plugin DSH Tavern)…
- [L-Forster/open-jet](https://github.com/L-Forster/open-jet) - An offline coding agent for local models.
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Fast, zero-dependency cost calculator and customizable statusline for Claude…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Línea de estado de terminal para sesiones de Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Resultados, calendarios y clasificaciones de fútbol en vivo para la…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plano de control local para Claude Code en Windows y macOS: cambia los gateways…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuración personal de Claude Code versionada dentro de ~/.claude — agentes…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horarios de oración, fecha Hijri, adhkar, ayah diaria, ayuno sunnah, Ramadan…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Línea de estado consciente de las sesiones para Claude Code.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Línea de estado truecolor de dos líneas para Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - A floating peak/off-peak tide card for DeepSeek Harness: i18n (en/zh/ru)…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de herramientas de código Portable Claude para .NET DDD/Clean Architecture…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuración global portátil de Claude Code: skills personalizadas, hooks de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins de Claude Code que uso a diario: skills y mods, depurados para que…
- [chaybits/ai-session-usage](https://github.com/chaybits/ai-session-usage) - Claude Code and ChatGPT (Codex) subscription limits in one card: a KDE Plasma 6…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gobernanza de tokens para Claude Code: el modelo principal dirige y la…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Línea de estado en directo de la fase del flujo de trabajo para Claude Code…
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Reduce el gasto de Tokens de Claude Code y Codex: dirige las consultas y…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Configuración sencilla y útil de la línea de estado para Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Alertas de límites de uso para Claude Code: notificaciones de macOS…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Línea de estado configurable de Claude Code para Linux, WSL, Windows y macOS…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Línea de estado rápida de Rust Code para Claude Code — centrada en la carga…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Panel de uso en tiempo real para Claude Code — desglose del contexto, aciertos…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Una línea de estado y una línea de tokens para Claude Code: contexto, uso de 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Muestra detalles clave del estado de Claude Code, incluidos el modelo, el…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - la línea de estado amigable y llena de opciones para Claude Code — barras…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Línea de estado de Claude Code en varias filas: gasto, % de contexto, git y…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Línea de estado con información útil para claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipos de agentes nativos. Bajo control.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Complementos de Claude Code: indicador de estado de pestañas con punto de color…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Línea de estado de uso de Claude Code para macOS y Linux, empaquetada como…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Línea de estado personalizada para Claude Code — barra de contexto con…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Una línea de estado limpia e informativa para Claude Code: muestra el proyecto…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Mod CRT HUD de Claude: un panel de estado al estilo CRT para Claude Code, en el…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins de Claude Code con baloo: skills, un agente que verifica…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Línea de estado de Claude Code de nivel profesional: duración de sesión, coste…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Línea de estado de Claude Code consciente de la suscripción.
- [dave-net-positive/Claude_Code_PII_Redactor](https://github.com/dave-net-positive/Claude_Code_PII_Redactor) - Mod that detects and redacts PII in Claude Code before it reaches the model.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Una línea de estado de terminal completa para Claude Code — Bun + TypeScript…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin de Claude Code que muestra diagramas Mermaid de forma atractiva en la…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Herramientas, habilidades y agentes para Claude Code — empezando por una línea…
- [FunDrivenDev/claude-plugins](https://github.com/FunDrivenDev/claude-plugins) - Public Claude Code plugins: a context-budget status line.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Línea de estado personalizada de Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Gasto real de DeepSeek de API para Claude Code: vuelve a calcular el precio de…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Previsualiza imágenes dentro de Claude Code: pasa el cursor sobre una etiqueta…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods para Claude Code y Claude Desktop en Windows con WSL: Docker y rendimiento…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Línea de estado de Claude Code con filas del panel de agentes.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincroniza las tareas pendientes de Claude con Fizzy.do para que el equipo…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Una colección de habilidades, mods y otros complementos de Claude Code que he…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menú de ajustes, línea de estado y configuración de Claude Code.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - plugins, habilidades, mods y más de claude, hechos en casa y sin jaulas.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalador del entorno de Claude Code: skills, barra de estado, hooks, permisos…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Línea de estado estilo HUD para Claude Code — estado de la red, TPS, contexto…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugins y mods de Claude Code para entender qué hace Claude: formatos de…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Barra de estado colorida de varias filas para Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Línea de estado de Claude Code para Windows (PowerShell): barras de uso…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings and Glossary para Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Configuración y mods de Claude Code, con un kit de componentes compartido, un…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - A small dashboard for Claude Code: context %, cache countdown, 5-hour &amp; weekly…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Custom terminal status bar for Claude Code: model, directory, git state…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuración portátil de Claude Code: CLAUDE.md, ajustes, línea de estado…
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Mod de Claude Code para escritorio (macOS): notificaciones de sesión con salto…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Mod complementario de lector de pantalla para Claude Code.
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Una inmersión práctica y verificada en Claude Code — CLAUDE.md, subagents…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Seguimiento de costes en tiempo real y línea de estado de monitorización de…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Una línea de estado de Claude Code: carpeta, rama de git, modelo, uso de la…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de degradación del contexto 2026 - Monitor proactivo de memoria de IA…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes y líneas de estado de Claude Code: colecciones y herramientas…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Constructor visual para las líneas de estado de Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Línea de estado de Claude Code que muestra el uso de tokens en tiempo real y el…
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code状态行：CCometixLine美化效果+Claude HUD功能.

</details>

<a id="dsh-cordis"></a>

## Ecosistemas de complementos de DSH y Cordis

DeepSeek Harness y Cordis llegan al mismo punto desde direcciones diferentes: para ellos, el complemento es el mecanismo de mods, así que allí un complemento equivale a un mod aquí.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74325 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

🌊 El agent harness original. Implementa enjambres inteligentes de varios agentes, coordina flujos de trabajo autónomos y crea sistemas de IA conversacional. Incluye memoria adaptativa, inteligencia de autoaprendizaje, federación, integración vectorial de RAG e integración nativa con Claude Code / Codex / Hermes y muchos más.

<sub>🔧 Encontrado en el código: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **74325**  |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100497 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

🎨 El mejor plugin de diseño para DeepSeek Harness. La alternativa de código abierto a Claude Design. 🖥️ Aplicación de escritorio local-first. 🖼️ Tu agente de programación se convierte en el motor de diseño: prototipos, páginas de destino, paneles, diapositivas, imágenes y vídeo; archivos reales, exportación a HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode y más de 20 CLIs mediante BYOK.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **100497** |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐87809 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Ingeniería inversa de cualquier cosa con agentes, desde el comportamiento de las aplicaciones hasta los binarios nativos.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **87809**  |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81879 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Convierte cualquier idea, plan o base de código en un hermoso diagrama interactivo. Una habilidad de agente para Claude Code, Codex y más.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **81879**  |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35759 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Un agente de programación fiable para tareas complejas de ingeniería de software.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Go                                                                                |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **35759**  |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8626 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Ecosistema de agregación de plugins web de DeepSeek Harness (DSH) · Todo es un plugin, distribuido mediante el Creative Workshop｜｜Ecosistema de agregación de plugins web de DeepSeek Harness (DSH) · Todo es un plugin, distribuido mediante el Creative Workshop

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **8626**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6146 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

El mercado de plugins dentro de DeepSeek Harness: explora, busca e instala con un clic · Mercado visual de plugins de DSH

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6146**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4478 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DeepSeek Harness（DSH） una pequeña chica ballena que vive en la esquina inferior derecha de la interfaz de DSH y te ayuda a vigilar el saldo de tu cuenta DeepSeek. Elástica y rebotante, admite arrastrar y acoplar, volteo al acoplar a la izquierda, animación de desplazamiento de números, se activa automáticamente con la interfaz; se recomienda invocarla directamente en tu instalación de dsh

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **4478**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4285 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

El plugin TUI oficialmente más recomendado por DSH: alto rendimiento, bajo consumo, adorable ballena pixelada e interacción fluida con el ratón. Instalación con un solo comando mediante npm. / El plugin TUI oficialmente más recomendado por DSH: alto rendimiento, bajo consumo, adorable ballena pixelada, interacción fluida con el ratón e instalación con un solo comando mediante npm

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **4285**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3153 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3153**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1983 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

El mejor plugin de DeepSeek Harness para comprender y gestionar el contexto, con panel, navegador y barra lateral de contexto, además de un comando de contexto, para consultar las estadísticas, composición, desglose y evolución del contexto, comprender cómo está formado y cómo evoluciona. Plugin visual de contexto todo en uno para DeepSeek Harness, con panel y navegador y barra lateral de Context, además del comando Context, para visualizar la composición, evolución, compresión, poda y otros eventos y acciones del contexto.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1983**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1561 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

跨设备的开源Agent工作台

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1561**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1464 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1464**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1401 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Software de escritura de novelas con AI: organiza inspiraciones, personajes, worldbuilding, esquemas, redacción de capítulos, revisión y corrección en un flujo de trabajo controlable; ofrece versión de escritorio para Windows/macOS, compatible con modelos locales y en línea. Software de escritura de novelas con AI: organiza inspiraciones, personajes, worldbuilding, esquemas, redacción de capítulos, revisión y corrección en un flujo de trabajo controlable. Incluye aplicaciones de escritorio para Windows/macOS, integración con Ollama y una vista previa de plugin para DeepSeek Harness (DSH).

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1401**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Memoria para Claude Code, Codex, Cursor y 38 agentes de programación más, creada a partir del historial de sesiones que ya está en tu disco. Búsqueda local, MCP y hooks, sin LLM, un único binario Go.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Go                                                                                |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1171**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Cliente de escritorio de DeepSeek Harness (dsh) Windows: Node.js incluido + dsh CLI, lanzamiento con un clic

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **704**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐283 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Just open your browser — get all your work done.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **283**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

ACRYL - Agent Context Relay Yielding Lifecycles. Un espacio de trabajo persistente, un contexto canónico, cualquier agente de programación.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **255**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin nativo de DeepSeek Harness (DSH) que integra TypeSafe Jev o una API de decisiones como luna como capa de decisiones System One para la selección, supervisión, corrección y aprobación de agentes.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **203**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Delegación de tareas con desplazamiento temporal para DeepSeek Harness (dsh): planifica tareas con calma, se ejecutan sin supervisión en horas de baja demanda y vuelves para recibir un informe. Con adjudicación humana, escritorio + web.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **170**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de DeepSeek Harness para migrar sesiones entre presets con vista previa. Las transferencias con esquema fijo conservan el estado, la intención del modelo de origen y las imágenes sin resolver; la sesión original permanece intacta.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **165**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Al instalarlo ya incluye 27 skills de ingeniería y eficiencia de mattpocock/skills v1.3.1, sin necesidad de instalar skills manualmente. Este plugin fue creado con 40 mil millones de tokens; sobre las skills originales ofrece 10 veces más eficiencia de desarrollo y también ayuda a principiantes a empezar más rápido con este conjunto de skills. Soporte completo para GitHub issue; Markdown está en versión preliminar; GitLab no es compatible por ahora. Gracias por usarlo y apoyarlo 💗

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **134**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **133**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐131 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Tema de escritorio de Claude Code para DeepSeek Harness｜ Tema de escritorio de Claude Code creado para la GUI web de DeepSeek Harness

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **131**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>grabación animada</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐130 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Runtime evidence that helps agents trace, profile, and burn down hotspots in application and native code, GPU kernels, and inference stacks.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **130**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de mascota de escritorio de DeepSeek Harness: una ballena enérgica te acompaña mientras programas 🐋 Compatible con el cliente de escritorio DSH 0.2.0-rc.2 y la Web antigua (desktop pet / mascot, local-first)

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **120**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **113**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐65 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Agent de escritorio creado sobre la base central de Deepseek-Harness. Hereda todas las capacidades de la base. Y completa funciones relacionadas con IDE.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **65**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

El directorio activo de plugins de DeepSeek Harness — actualizado cada hora, con pruebas de compatibilidad diarias, tienda de plugins integrada y generador de estructuras. Directorio activo de plugins de DSH: actualización cada hora, pruebas de compatibilidad diarias, tienda de plugins y generador de estructuras integrados.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | HTML                                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **59**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Recuperación de contexto del espacio de trabajo y seguimiento del ciclo de vida, conscientes de las tareas, para agentes de programación con IA. Encuentra, organiza y realiza un seguimiento del contexto del espacio de trabajo más relevante para la tarea actual — localmente, de forma determinista, sin llamadas a modelos y sin red.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **53**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/skyf0xx/hedgehog">skyf0xx/hedgehog</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

HEDGEHOG codes Cleaner, Faster and with Fewer Tokens. Hedgehog's AI-driven development builds a task dependency graph from your spec-driven, BMAD-METHOD plan, so Claude Code, Cursor & Gemini CLI stay locked to it. A CLI-enforced state machine for agentic coding. Now builds DeepSeek DSH Plugins. DeepSeek Harness、DSH 插件、AI 编程、BMAD 方法. AI Copywriting

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **44**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agent-skills` · `agentic-coding` · `ai-agents` · `ai-assisted-development` · `ai-coding` · `ai-copywriting` · `ai-engineering` · `ai-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/skyf0xx--hedgehog/326d2d3a663269a4.jpg" width="100%" alt="skyf0xx/hedgehog screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐42 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin maestro de recursos para juegos de dsh. Integra el modelo de generación de imágenes seedream y el modelo de generación de vídeo minimax para crear diversos recursos de juegos.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **42**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de DeepSeek Harness: mantiene una ventana de contexto precisa para el modelo llm-pi-ai y evita que las sesiones largas se diagnostiquen erróneamente como desbordamiento de contexto.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **34**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/6c743bbe3da63616.jpg" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PensiveFei/deep-read-summarize">PensiveFei/deep-read-summarize</a></b> · ⭐31 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Deep reading & summarization workflow for books/papers/videos/web — plugin parsers, MapReduce deep-read, JSON Schema output, Obsidian-ready (DSH)

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **31**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agent` · `content-summarization` · `deepseek` · `dsh-plugin` · `pipeline` · `workflow`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pensivefei--deep-read-summarize/800b10f03f25fe11.png" width="100%" alt="PensiveFei/deep-read-summarize screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Una lista seleccionada de los mejores plugins de IA para asistentes de IA…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins de DSH / DSH Plugin Marketplace: explora, instala y…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins para software que itera sobre sí mismo: la base donde los…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directorio seleccionado de plugins de DeepSeek Harness (DSH): más de 280…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Kit de herramientas de Zotero para DeepSeek;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin de DSH: shell Git Bash para todos los modos de agente en Windows…
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistema de agentes de chat grupal multiplataforma basado en DeepSeek…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - ¡El trío de herramientas de oficina! Herramientas para documentos de Office…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh安卓版：集成DeepSeek Harness、Ubuntu运行环境、插件与文件管理，以及用户授权的Shizuku和无障碍自动化.
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Navegación de sesiones de DSH.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [weishao2/tizhuang-agent-skills](https://github.com/weishao2/tizhuang-agent-skills) - 2000万+中小学K12真题题库 Skill：免费注册、免费抽题、教材/章节/知识点检索、练习测验与AI智能组卷.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin web de DSH: estadísticas diarias de uso de tokens con un mapa de calor…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, herramientas, skills y recursos de aprendizaje de DeepSeek Harness…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin gestor de servidor MCP para DeepSeek Harness: página Settings → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Plugin de DeepSeek Harness: 15 habilidades de ingeniería de obra/superpowers…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de negociación comercial A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - Interfaz de gestión del servidor MCP para DeepSeek Harness Web — panel…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un PowerPoint real, no HTML. Dile a tu IA qué debe incluir y pptwise creará una…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催更姬：给大肥鱼一个小说工作台。写正文、理设定、画情节，和 AI 一起讨论、续写与改稿.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin de DeepSeek Harness · Botón «Optimizar» con un clic en la barra de envío…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Puerta de inicio de sesión para la interfaz web de DeepSeek Harness (dsh)…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 嵌入式C/C++ AI工程插件——固件技能（FreeRTOS、Keil、HardFault、状态机）+ 1% Rule / Plan Verification…
- [Chael-Chael/dsh-reference-anything](https://github.com/Chael-Chael/dsh-reference-anything) - The best DeepSeek Harness plugin for referencing anything — enhanced @ menu for…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Gestor integral de skills, subagent, MCP y LSP para DeepSeek Harness (DSH)…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pruebas de compatibilidad siempre activas para plugins de DeepSeek Harness…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive context compaction for local-first agents.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host de DeepSeek Harness que mantiene los documentos del proyecto y la…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayos X para plugins de DeepSeek Harness: capacidades declaradas frente a…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - A knowledge base toolkit for research and literature review.
- [Mcd0LUO/dsh-guard-repeat-output](https://github.com/Mcd0LUO/dsh-guard-repeat-output) - Host-side degeneration guard for DSH: strips garbage code points, detects…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - Convierte las respuestas de DSH en interfaces accionables: cálculos, gráficos…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - Verificación de afirmaciones sobre diseño y código: contrasta las afirmaciones…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espacio de trabajo con varias carpetas: permite que el agente de DSH.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plugin de flujo de trabajo de ingeniería para DeepSeek Harness: etapas de…
- [Kr-ATG/dsh-chat-plus](https://github.com/Kr-ATG/dsh-chat-plus) - DSH 对话体验增强套件（零源码改动，纯插件注入）。Seeker 双栏执行大盘：右栏任务 / 操作面板 / 子智能体 / 产出物四张卡 +…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Estándar de verificación sin dependencias para plugins de DeepSeek Harness…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode en DeepSeek Harness — plugin de DSH que mantiene funcionando OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — mercado de plugins de terceros y gestor de ciclo de vida protegido…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx es un espacio de trabajo de escritorio ampliable y centrado en las…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Un agente de programación con todo incluido para DeepSeek Harness — flujos de…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Plugin de experiencia de entrada web de DSH: alternancia de teclas para…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Proporciona a la edición de escritorio de DeepSeek Harness un punto de acceso…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite comunitaria de instalación, despliegue y operaciones locales…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web de DeepSeek Harness (DSH): pestaña lateral market-dashboard para…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Permite volver a intentar un intento vacío de modelo sin atribución, para la…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins que se limpian solos: un port de Swift 6 del framework de plugins…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset de agente DeepSeek Harness: Codex y Claude Code como subagentes de…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins de Rust con un kernel de ciclo de vida verificado por…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Escritura, debates y vídeos

Artículos, debates y vídeos sobre la capacidad de modding.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Hola, HN. Creé esto para mí y quería publicarlo como código abierto. El problema: quería una forma de recibir recordatorios entre prompts, ya que a menudo paso muchas horas en el terminal, especialmente ahora que normalmente procesamos tantos agentes en paralelo. La primera versión era un rep

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Resumen

No se publicó ninguna descripción del repositorio original.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Creé esto porque, con los modelos de programación más recientes, Claude entra en modo de trabajo profundo con comandos poco conocidos y ya no sé qué está haciendo. Este es un mod (un plugin que utiliza los nuevos hooks de funciones de Claude Code) que dibuja una línea encima del mensaje: - el paso actual,

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Escritura, debates y vídeos`                                           |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Proyectos por lenguaje de implementación

El ecosistema se concentra en Python y TypeScript, pero siguen apareciendo clientes tipados en otros lenguajes. Esta tabla se genera a partir de las propias entradas.

| Lenguaje   | Entradas | Ejemplos                                                                                                           |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 322      | `anthropics/claude-code`, `anthropics/claude-code-action`, `karanb192/cache-tax`                                   |
| JavaScript | 69       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `augiefra/claude-mods`                         |
| Python     | 32       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`      |
| Shell      | 19       | `anthropics/claude-agent-sdk-typescript`, `andrewbakercloudscale/claude-code-cost-sidebar`, `Gharib89/claude-mods` |
| HTML       | 12       | `awss1i/assay`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                                       |
| Go         | 6        | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                         |
| Rust       | 5        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`                  |
| PowerShell | 2        | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                                |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                            |
| Kotlin     | 1        | `dphmoblie/deepseek-harness-android`                                                                               |
| MDX        | 1        | `jkf87/mod-guide`                                                                                                  |
| Swift      | 1        | `eovidiu/cordis-ios`                                                                                               |

<sub>Solo se contabilizan las entradas que declaran un idioma. Las entradas de documentación y debate se excluyen de esta tabla.</sub>

## Contribuir

Las correcciones son bienvenidas y son la forma más rápida de mejorar esta lista. Abre un issue o una pull request si una entrada está mal clasificada, tiene una categoría incorrecta o si un proyecto se ha excluido por error debido a una coincidencia de nombres; esta última categoría es donde más probablemente fallen los filtros automatizados.

---

<sub>Proyecto independiente de la comunidad. No está afiliado a Anthropic, ni cuenta con su respaldo o revisión. Claude Code, Claude y Anthropic son marcas comerciales de Anthropic. El comportamiento del producto puede cambiar sin previo aviso; verifica cualquier aspecto esencial en la documentación oficial. Los recursos siguen siendo propiedad de sus proyectos de origen y se reproducen únicamente cuando una licencia lo permite.</sub>

<sub>Última actualización · 2026-10-11T21:12:49+08:00</sub>
