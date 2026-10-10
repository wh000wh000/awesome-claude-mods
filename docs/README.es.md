<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods increíbles de Claude">
</p>

<h1 align="center">Mods increíbles de Claude</h1>

<p align="center"><b>El índice de mods y plugins de Claude Code, clasificados según la evidencia, y del comportamiento más profundo que modifican.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-617-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <b>Español</b> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice activo** · Última sincronización: `2026-10-11T05:58:46+08:00` (UTC+8)
> · Entradas: **617** · Añadidas en la última actualización: **0** · Lenguajes de implementación: **10**

<sub>Todas las entradas siguientes se recopilaron, filtraron y revisaron de nuevo automáticamente. Nada de lo que aparece aquí es contenido promocional de pago.</sub>

<a id="featured"></a>

## Selecciones del momento

<sub>Una entrada por categoría, clasificadas según el nivel de evidencia y las estrellas, y recalculadas con cada actualización. Es una clasificación, no una recomendación; cada selección enlaza con su ficha completa más abajo. Se prefieren los proyectos que han publicado una captura de pantalla o una grabación, para que la franja siga siendo visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9466 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2532 · Python · 👁️ observed</sub>
<sub>Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74280 · TypeScript · 👁️ observed</sub>
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
- [Oficiales: repositorios propios y notas de versión de Anthropic](#oficiales-repositorios-propios-y-notas-de-versión-de-anthropic) — **16**
- [Mods: creados con la capacidad de mods](#mods-creados-con-la-capacidad-de-mods) — **493**
- [Ecosistemas de complementos de DSH y Cordis](#ecosistemas-de-complementos-de-dsh-y-cordis) — **97**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150059 · TypeScript · ✅ official · 1 天</summary>

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
| Estrellas         | **150059** |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9466 · TypeScript · ✅ official · 1 天</summary>

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
| Estrellas         | **9466**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8244 · Python · ✅ official · 1 天</summary>

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
| Estrellas         | **8244**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6335 · Python · ✅ official · 241 天</summary>

##### 📝 Resumen

Una GitHub Action de revisión de seguridad basada en IA que utiliza Claude para analizar cambios de código en busca de vulnerabilidades de seguridad.

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |
| Lenguaje  | Python                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6335**   |
| Último envío      | 2026-02-11 |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 1 天</summary>

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
| Estrellas         | **1799**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Resumen

Materiales complementarios para las tarjetas de modelos Claude

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
| Primera inclusión | 2026-10-05 |

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
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Consola de gestión de MCP para el cliente oficial MCP de DeepSeek Harness: comando /mcp con diagnósticos de estado y llamadas de prueba de pipelines, pestaña Settings MCP con operaciones CRUD de servidores (escrituras con aprobación y copias de seguridad automáticas) y consola de prueba de herramientas sobre el pipeline oficial de herramientas (Apache-2.0, dsh-plugin).

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic`                 |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **74**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

esto es un lanzador para el DeepSeek Harness oficial. no hace modificaciones, solo inicia lo que desarrolla DeepSeek.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic`                 |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Se añadió `$.ui.notify` para los mods: muestra una notificación nativa mediante…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Corregido Esc o una interrupción durante un hook de `UserPromptSubmit` o un…

</details>

<a id="mods"></a>

## Mods: creados con la capacidad de mods

Cada entrada aquí muestra pruebas de que usa la capacidad que Claude Code obtuvo en 2.1.287: renderiza mediante `ui.render`, incluye un panel, una banda o una tarjeta, lee `$.ui.selection()`, genera compañeros con `agent.spawn`, o afirma claramente que es un mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2532 · Python · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | Python                                                                  |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2532**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐467 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Catálogo comunitario de mods públicos de Claude Code (hooks de funciones), analizados desde GitHub con información sobre lo que cada mod puede leer, escribir, ejecutar o enviar por la red. Explora https://mods.aidojo.si/

<sub>🔧 Encontrado en el código: `data/seeds.txt`, `data/duplicates.txt`, `data/repos.txt`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **467**    |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐181 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Resumen

Mods de Claude Code: plugins creados sobre hooks que añaden líneas en vivo sobre el prompt, guardas, paneles y juegos. Barra de contexto, medidor de uso, vigilancia de revisión Codex, vista previa de Markdown, reproducción actual de Spotify y más.

<sub>🔧 Encontrado en el código: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **181**    |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐115 · TypeScript · 👁️ observed · 6 天</summary>

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
| Estrellas         | **115**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐106 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

<sub>🔧 Encontrado en el código: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | HTML                                                                    |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **106**    |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Resumen

An agent-native QA CLI for web pages. Deterministic, no tests to write, no LLM.

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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **88**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Resumen

Una colección de mods de claude code

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **77**     |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Colorful, themeable Claude Code replies: tables, code, diagrams, charts and tool rows in 15 themes, with copy buttons. A Claude Code mod.

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
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Resumen

Modificaciones de Claude Code de Darrell Wang: bandas sobre el prompt, cero tokens del modelo. Paneles de acciones taiwanesas y estadounidenses + más próximamente.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | HTML                                                                    |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **65**     |
| Último envío      | 2026-10-05 |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐59 · TypeScript · 👁️ observed · 8 天</summary>

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
| Estrellas         | **59**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐57 · Shell · 👁️ observed · 3 天</summary>

##### 📝 Resumen

Skills expertos, agentes, comandos, reglas, hooks y estilos de salida para Claude Code: continuidad de sesión + herramientas modernas de CLI para flujos de trabajo de desarrollo reales

<sub>🔧 Encontrado en el código: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | Shell                                                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **57**     |
| Último envío      | 2026-10-07 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐45 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Resumen

Mods de Claude Code: barras de progreso del plan en directo sobre el prompt

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **45**     |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>grabación animada · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

A glow-up for Claude Code: a live cockpit pane, shareable themes, and a pixel pet that acts out what Claude is doing

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
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Compilación, pruebas, consola y previsualizaciones de SwiftUI de Xcode dentro de Claude Code

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **20**     |
| Último envío      | 2026-10-02 |
| Primera inclusión | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Resumen

Mods de Claude Code: 21 estilos y un conjunto completo de funciones que activas cuando las necesitas, para el terminal y la aplicación de escritorio. · Da a Claude un estilo nuevo con un clic y disfruta de un conjunto completo de funciones activables bajo demanda.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **20**     |
| Último envío      | 2026-10-04 |
| Primera inclusión | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Diez mods de Claude Code, guías para principiantes, prompts de creación, demos seguras y una plantilla para crear el tuyo.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **20**     |
| Último envío      | 2026-10-02 |
| Primera inclusión | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Mods de Claude Code: usage-band muestra tus límites de 5h/7d, ventana de contexto y tasa de aciertos de caché encima del prompt

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **12**     |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Resumen

Mods de Claude Code que facilitan la lectura y respuesta a las preguntas de Claude (qa-guide).

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **11**     |
| Último envío      | 2026-10-07 |
| Primera inclusión | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>grabación animada · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

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
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Diez mods de código abierto para Claude Code: paneles en vivo, bandas, líneas de estado y protecciones de llamadas a herramientas. Medidor de consumo, códigos de lanzamiento, sesión envuelta, pelea de jefe, mascota de código y más.

<sub>🔧 Encontrado en el código: `swarm/README.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **11**     |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Resumen

Dos mods de Claude Code: puente de uso del ordenador Codex y sesiones Claude coordinadas. Código fuente, prompts de compilación, configuración y pruebas.

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
| Último envío      | 2026-10-05 |
| Primera inclusión | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Resumen

Una UI alrededor de tus terminales de Claude Code y Codex que construyen tus agentes, para que el único modelo en tu cabeza sea el tuyo.

<sub>🔧 Encontrado en el código: `CLAUDE.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **9**      |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

KOZMOS — mods visuales en directo para Claude Code (CLI + escritorio): bandas sobre el prompt, barras laterales, ticker de estado, compañeros, protecciones y sonido.

<sub>🔧 Encontrado en el código: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **9**      |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Resumen

Seis mods de Claude Code en un solo plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) con interruptores por mod, además de un informe mods-vs-hooks.

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
| Último envío      | 2026-10-04 |
| Primera inclusión | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 25 天</summary>

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
| Estrellas         | **7**      |
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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Resumen

Colección de mods de Claude Code de 개발동생. Paquete taxi: taxímetro, navegación, cámaras de control de velocidad y caja negra

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
| Último envío      | 2026-10-04 |
| Primera inclusión | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Ver en youtube.com</a> · la reproducción se abre en el sitio anfitrión; GitHub no puede insertarlo en línea</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Resumen

Mods de Claude Code: 像素螃蟹用量面板 usage-hud + enlaces HTML clicables en la terminal y tarjetas de código con copia en un clic html-shelf

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
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>grabación animada</sub></td>
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
<summary><b>Más en esta categoría</b> <sub>· 459</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Colección de más de 100 mods que puedes usar con Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods de Claude y las herramientas para crearlos: primero una skill de creación…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - El harness de Claude Code que uso a diario, publicado con este nombre desde el…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Cambia el tejado de Claude Code con Claude Mods: sustituye el prompt del…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cuatro mods de Claude Code: Cache Keeper, Recording Mode, Goal Meter y…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods de Claude Code de Learning Hacker: convierten el funcionamiento del agente…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods de Claude Code que corrigen y traducen tus prompts antes de que Claude los…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un panel lateral para Claude Code: los subagentes que ejecuta una sesión, qué…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Una cabina para Claude Code: barras de planes en tiempo real, franjas de…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conocimiento de Obsidian con fuentes sobre los mods de Claude Code…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Habilidad que enseña a los agentes de Claude Code a crear Mods de Claude…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel de barra lateral de Claude Desktop (pestaña Code): enumera todas las…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods y habilidades de Claude Code de Nekyia Labs, creados y usados a diario por…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (plugins de enlaces de funciones) para Claude Code.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso encima del cuadro de entrada de Claude Desktop (pestaña Code)…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins y habilidades comunitarios de Claude, instalables desde un único…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galería de mods de Baselane: mods de Claude Code, revisados y fijados.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una cola de decisiones CLI/TUI para personas que trabajan con agentes…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod del panel IDE de Claude Code: panel de agentes, árbol de archivos y visor…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Tarjeta de estado flotante para Claude Code — modelo, contexto, límites de…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nombres y secretos mientras compartes…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensiones de Claude Code. Desbloquea todo el poder de Claude.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Paneles, protecciones y mods para mejorar la experiencia en Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dos mods de Claude Code sobre el cuadro de prompt: medidor de ventana de…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Your plan, watching itself. Local desktop roadmap tree that Claude Code and any…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lee los archivos markdown que nombra Claude Code, renderizados junto a la…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Compañero de voz para Claude Code. Habla sobre tus ideas con un lobo 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, un velocímetro de escritura activo con…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuegos artificiales para Claude Code: cada pulsación, llamada a herramienta…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubre mods, plugins y extensiones de Claude Code con demos animadas, listas…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas de mermaid dibujados en línea en la transcripción.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequeños mods de Claude Code (plugins de function-hook): session-switcher y más.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imágenes pegadas encima del prompt, en…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods de Claude Code: mod-scout (encuentra los mods que más utilizarías)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dos mods de Claude Code para ejecutar muchas sesiones a la vez: una tarjeta de…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Mod de Claude Code: controla nativamente el contenido de la autocompactación…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Haz que el plan Pro de Claude dure más: mods de Claude Code para un HUD de uso…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow para Claude Code: una lista de verificación tranquila sobre el…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Los mejores mods de Claude Code: seleccionados a mano, validados y fijados.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin de Claude Code: enrutamiento automático de modelos Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Seis mods para Claude Code: mascota Clawd animada, barras de límite de uso y…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Un marketplace de mods para Claude Code: un depurador paso a paso para el bucle…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods de Claude Code: menú Herramientas de Claude, modo Zen, temas de terminal…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - El mejor paquete de mods todo en uno para Claude Code: límites de uso y HUD del…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Reproduce YouTube Shorts en tu Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de herramientas Claude de Naren: skills, mods y servidores MCP para Claude…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod de Claude Code que muestra las diferencias de Edit y Write en dos columnas…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods para Claude Code: Clawd, una diminuta mascota de píxeles que representa lo…
- [reporails/arcade](https://github.com/reporails/arcade) - Juegos de escritorio clásicos como mods de Claude Code, jugables en un panel…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Una lista seleccionada de mods de código de Claude Code, instalables como un…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantienen al agente honesto — hooks de funciones que…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Mi colección de mods de Claude Code, un mod por directorio.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Cinco mods gratuitos de Claude Code: Simple Mode, Usage Tally, Context Handoff…
- [arviaja/token-watch](https://github.com/arviaja/token-watch) - Mod de Claude Code: muestra el uso de tokens, los límites del plan y la…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Recién salido de fábrica. Un mod de Claude Code: pide un meme y sigue…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod para Claude Code: barra de caché de prompts, próximos pasos, botones…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code que muestra tus límites de uso y gasto en la banda sobre…
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - El mod skill-router: Jev selecciona y carga las habilidades que necesita cada…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Una tienda de apps para mods de Claude Code, dentro de Claude Code: /mods para…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods de Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods de Claude Code: barras de progreso para planes, un registro de lo que…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Mods de Claude Code para la experiencia de usuario diaria: límites del plan…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mods de Claude Code de MacLeod Labs: streams desenreda el trabajo intercalado…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo del primer día sobre mods de Claude Code en Windows: una barra…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods que hice y uso personalmente en mi configuración de Claude Code.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod de Claude Code: medidores en vivo de coste, contexto y cuota del plan…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Un mod de Claude Code que retiene la distribución de subagentes, las…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods para claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod de Claude Code que activa o desactiva tus habilidades, agentes, reglas y…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods para Claude Code: plugins creados sobre hooks de función.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Créditos al estilo cinematográfico para tu sesión de programación.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un montón de mods de claude code creados por mí.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Un reproductor de YouTube respaldado por cliamp dentro de Claude Code.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Mods de Claude Code: panel de flota de agentes y piloto automático.
- [vynnlee/mods](https://github.com/vynnlee/mods) - Mods de Claude Code de vynnlee. Una carpeta por mod, instalables desde un único…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprende un idioma extranjero mientras trabajas con Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Supervisa una sesión larga de Claude Code para que no tengas que hacerlo…
- [akerskuuug/claude-mods](https://github.com/akerskuuug/claude-mods) - Claude Code mod: usage, limits, branch and model around the prompt.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Respuestas con tema, diagramas de ancho completo y tu contexto y límites de un…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Cuando el agente escribe Java, el código que infringe la convención p3c de…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de coste, tokens y uso del contexto en tiempo real para Claude…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Llamadas de radio de Counter-Strike 1.6 para Claude Code — «Fire in the hole»…
- [burnrate-ai/burnrate](https://github.com/burnrate-ai/burnrate) - Consulta y ralentiza la velocidad a la que Claude Code consume tus límites de…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Herdr setup + Claude Code mods for product dev work.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Panel del notch de macOS para Claude Code: límites de uso, sesiones abiertas…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude está cocinando. Chatea con tu escuadrón.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Un mod de Claude Code: atrapa Modsters de pixel art en un juego inactivo…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Una batalla espacial sobre el prompt de Claude Code mientras trabaja.
- [davidbalzan/status-band](https://github.com/davidbalzan/status-band) - Mods de Claude Code de David Balzan: status-band, una banda de estado sobre el…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Ve qué archivos tiene cada agente de Claude Code en su contexto, y cuánto de…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Mantén la cabeza fría. Un termómetro para tus días de Claude Code: cada hora…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Recorta las salidas enormes de las herramientas antes de que llenen el contexto…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequeños mods de Claude Code para el terminal y la aplicación de escritorio.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidad + mod de Claude CLI que añade palabras en español a las respuestas…
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Mods de Claude.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - A Claude Code mod that restyles it as The Machine from Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Mod de Claude Code: compacta en el momento adecuado.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod de Claude Code para flujos de trabajo DAG obligatorios y…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - A pixel-art Naruto companion for Claude Code: 20 ninja, 60 jutsu, performed…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-source mods for Claude Code: panes, status lines, toasts, tool guards and…
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Un directorio comunitario de mods, plugins, habilidades, agentes, hooks y…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod de Claude Code: estado de sesión, progreso en vivo de Spec Kit y…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La ventana de contexto como una fila sobre el prompt, dibujada como Claude Code…
- [koslowskyj/tdd-mod](https://github.com/koslowskyj/tdd-mod) - Experimental Claude Code mod that enforces test-driven development: on coding…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) de Claude Code que hace que la interfaz de terminal de Claude Code…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Mira lo que Claude Code ejecuta en segundo plano: subagentes, trabajos de…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Limpia el chat, conserva el trabajo. Plugin de Claude Code + mod relay: Claude…
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - Personal Claude Code mods: otto-hud, Otto the octopus with context weather and…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un Mod de Claude que muestra las solicitudes de extracción de GitHub de la…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: un depurador para las llamadas a herramientas de Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Habilidades de Claude Code: un verificador de hechos de documentación, un…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod de Claude Code que reescribe los prompts preliminares para hacerlos claros…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compañero de Claude Code: un acompañante ASCII sobre el prompt que…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin de Claude Code para la visibilidad de herramientas por agente: oculta y…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Mod de Claude Code: enrutamiento de modelos/esfuerzo guiado por Jev…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods: security layer for Claude Code - secret redaction…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Una colección de mods de Claude Code.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin y mod de Claude Code: un SDLC nativo de IA.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Colección Awesome de mods de Claude Code | Colección de mods de 클로드 코드.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins (mods) de Claude Code: cambia entre varias cuentas de Claude, supervisa…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de código de Claude probados e instalables con un comando: protecciones…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Mods de Claude Code: paneles en vivo y hooks para el trabajo diario.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Habla: un mod de Claude Code que lee en voz alta, cuando se solicita, las…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code: pequeños plugins para paneles en tiempo real, enrutamiento…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod y plugin de Claude Code: monitor de uso, rastreador de tokens y línea de…
- [Verinoda-Labs/verinoda-symbiosis](https://github.com/Verinoda-Labs/verinoda-symbiosis) - Verinoda + Claude Code, juntos: Verinoda con verinoda-live, un mod de Claude…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods de Claude Code. touch-map: muestra qué archivos enumeró, leyó, editó o…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Un mod de Claude Code que resume en inglés sencillo los mensajes del agente que…
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code mods + cheap-executor driver: one Claude session as lead, MiniMax…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gato braille animado sobre el prompt de Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code: dirige el trabajo barato a GLM/Kimi mediante un Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gato pixelado sobre el prompt de Claude Code que ejecuta una llamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code que elige un buen momento para compactar y mantener…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods para Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace de plugins de Claude Code de anderson-spider.
- [ankits3a/cache-keeper](https://github.com/ankits3a/cache-keeper) - Claude Code mod: prompt-cache band, keep-warm, handoff judge trial.
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - Un mod de Claude Code que elige el modelo para cada subagente antes de que se…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Un mod de Claude Code: tu ventana de contexto en una línea discreta, gris hasta…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - El barco de LGTM Lines navega tras cada cambio de código: un mod de Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Tus límites de uso de Claude como tarjeta animada de salud de aldeano: un mod…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mods de Claude Code para el equipo S2 (el marketplace ather).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Entrenamientos cortos mientras Claude trabaja: un objetivo diario, rachas…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un panel de uso para Claude Code: gasto por modelo.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para Claude Code: Apple Music y Spotify sobre el aviso, con…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Cinco mods de Claude Code para ejecutar muchas sesiones a la vez: tablero de…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Mods de Claude Code para sesiones de orquestador y trabajador.
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Mods de Claude Code: banda de uso, lista de chat, /cube, /handoff, limpieza de…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: reloj de caché, radio de impacto, sugerencias, lista de…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mods de Claude Code: Suggestion Spotlight muestra a qué se refiere el siguiente…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un búho para tu Claude Code.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Mods de Claude Code para el harness ai-architect.tools: una preocupación por…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Banda de Claude Code de una línea.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - El motor original de Doom con Freedoom, jugable dentro de Claude Code.
- [cmorss/claude-mods](https://github.com/cmorss/claude-mods) - Mods de Claude Code para git worktrees: /terminal y /worktree-files abren un…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods de Claude Code para Engineers reales.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Mods de Claude Code exclusivos para el equipo d3nim.
- [David-AP-TON618/claude-explain](https://github.com/David-AP-TON618/claude-explain) - Claude Code mod: /explain re-renders an answer as controlled language (STE), a…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi que vive dentro de Claude Code: eclosiona, se come el código que…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Marcadores y marcas estilo vim dentro de conversaciones de terminal de Claude…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Convierte cada sesión de Claude Code en una pequeña aventura: música generativa…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code mod: shows the time on each prompt and reply in the terminal and…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mods de Claude Code escritos como hooks de funciones y el marketplace que los…
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code mods and design systems: crab-crew and the Crab Crew design system.
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - Mods de Claude Code de divramod: paneles en tiempo real y ajustes para la…
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - Los mods de Claude Code que uso en todas las máquinas: savvy-progress…
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ¡Ey, lo silencié! Deshazte del diff, corta el riff;
- [elkinaguas/claude-mods](https://github.com/elkinaguas/claude-mods)
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod de Claude Code: uso de la suscripción (5h / 7d) como una banda sobre el…
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Claude Code Mod for background test progress: JUnit, Karma, pytest and unittest.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Mods con diseño de movimiento para Claude Code: un monitor activo y adaptable…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - A live radar of your parallel branches and worktrees above the prompt: which…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - Mis mods de Claude Code.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+click copy link on every code block in Claude Code replies.
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - El mod jev: $.jev para Claude Code, juicios tipados de TypeSafe Jev.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Mod de Claude Code: panel que muestra si el caché de prompts está caliente o…
- [Gersom/claude-mod-usage-meter](https://github.com/Gersom/claude-mod-usage-meter) - Mod de Claude Code: recuadro con el % de contexto y de los límites de 5 horas y…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mods para Claude Code: plugins de hooks, como usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mods de Claude Code (plugins de function-hook), instalados mediante un único…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra lateral al estilo de Evangelion para Claude Code: contexto, cuota…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Useful claude code mods.
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Claude-Code Plugin (Mod) lets you see what the model is doing while it works.
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Resultados de pruebas en un panel de Claude Code: fallos, sus detalles e…
- [hfknight/claude-mod-said](https://github.com/hfknight/claude-mod-said) - Un mod de Claude Code: /said abre un panel lateral de los mensajes que…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de Claude Code: cuánto tardó cada respuesta, cuánto tiempo pensó Claude y…
- [icedevil2001/session-sidebar](https://github.com/icedevil2001/session-sidebar) - Mod de Claude Code: enlaces, información importante y acciones pendientes de la…
- [iddhi-sulakshana/claude-mods](https://github.com/iddhi-sulakshana/claude-mods) - Mods para Claude Code: botones para el siguiente paso, mensajería entre…
- [jagp/xray-mod](https://github.com/jagp/xray-mod) - ⋐∿⋑ Observa profundamente tus contextos: un mod activo de Claude Code que…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - A Claude Code mod: one pane for every subagent, the files they touch, and your…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel lateral de uso del contexto: total, categorías, crecimiento por ronda…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista lateral de archivos: qué archivos se han creado, modificado o eliminado…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, un conejo belier neerlandés en blanco y negro con estilo de 8 bits, corre y…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel lateral de «Lo que he preguntado»: cada frase que el usuario ha escrito…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Línea de tiempo lateral: en qué se ha empleado el tiempo de esta ronda…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Intercambio de tokens en el panel lateral: cuántos tokens envía la conversación…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - El bocadillo de tofu honesto de claude code: al terminar cada ronda, Claude…
- [jgilb17/claude-mods](https://github.com/jgilb17/claude-mods)
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Lista de comprobación del plan para Claude Code condicionada a evidencias: los…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Pequeños mods para Claude Code, como nuevos comandos de barra y paneles…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Juegos multijugador para jugar dentro de Claude Code mientras trabaja.
- [juliomyitbrain/claude-code-git-graph](https://github.com/juliomyitbrain/claude-code-git-graph) - Claude Code mod: a pane that draws the repository.
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Mod de Claude Code: mantiene caliente la caché del prompt mientras estás…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive en una banda sobre tu prompt de Claude Code: representa la sesión…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - Un mod de Claude Code que muestra la cuota de límites de velocidad, los tokens…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod que lee en voz alta las respuestas y notificaciones de Claude Code mediante…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod de Claude para leer y unirse a las conversaciones entre tus sesiones de…
- [kikostefanov-lab/claude-code-mods](https://github.com/kikostefanov-lab/claude-code-mods) - Mods de Claude Code: un panel de Whiteboard donde Claude dibuja diagramas de…
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Niceties/quality of life improvement Claude mods.
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - Exprime las sesiones frías de claude code con haiku: una banda de caché de una…
- [kk5190/claude-code-mods](https://github.com/kk5190/claude-code-mods) - Mods para Claude Code: medidor de contexto y paneles de servidores de desarrollo.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - A live task HUD for Claude Code Desktop: a strip above the prompt while Claude…
- [KytioisaCat/playpen](https://github.com/KytioisaCat/playpen) - ¿Quién necesita atención? Tus otras sesiones de Claude Code como tarjetas sobre…
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guía de Mods de Claude Code seleccionada por la comunidad: casos de uso…
- [lucasram20/claude-mods](https://github.com/lucasram20/claude-mods)
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de Claude Code que muestra lo que Claude está haciendo en el subtítulo…
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Mod de Claude Code: anima a la sesión principal a delegar en subagentes y…
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - My personal collection of claude mod plugins.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod de Claude Code con perfiles de permisos intercambiables: una base…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community mods for Claude Code: guards, panes, and commands that run inside…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel lateral para Claude Code: archivos que Claude escribió, divisiones del…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mikejhill/claude-usage-status](https://github.com/mikejhill/claude-usage-status) - Claude Code mod: always-on band showing 5h/weekly limits, context fill, and…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un discreto panel lateral para Claude Code: qué está haciendo esta sesión, su…
- [mmedum/spor](https://github.com/mmedum/spor) - Devuelve lo que Claude oculta: los archivos que Claude leyó, los comandos que…
- [moonteek/claude-mods](https://github.com/moonteek/claude-mods) - Mods de Claude Code: una barra de memoria y una lista de tareas activa sobre el…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mods de Claude Code: transferencia automática y barra de progreso.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de código de Claude que vuelve a activar las herramientas de tareas para…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de código de Claude: una línea por tarea encima del prompt con la tarea…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Juega Connect Four contra una AI dentro de Claude Code (/connect-four).
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Un canario pixel art para Claude Code: muere cuando Claude deja de seguir tus…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: cuando otro agente de programación hace un commit en tu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositorios compartidos por varios agentes de IA…
- [narley/sessions-sidebar](https://github.com/narley/sessions-sidebar) - Claude Code mod: a sidebar listing every Claude Code session, for Warp.
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Un panel de radio por Internet ciberneón para Claude Code: dial synthwave…
- [niksavis/handily](https://github.com/niksavis/handily) - Mods de Claude Code que muestran tus elementos de trabajo, tareas y sesiones…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Reactiva las supervisiones largas de Monitor de Claude Code cuando caducan, sin…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barrera de protección para SQL en Claude Code: pregunta antes de que Claude…
- [OctopiAI/claude-code-statusline](https://github.com/OctopiAI/claude-code-statusline) - Un Mod ligero de Claude Code.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un mod para Claude Code, Windows y CJK en primer plano: vistas previas de…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime para Claude Code: un sonido cuando Claude termina, necesita tu…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mods de Claude Code: miniaturas de imágenes y línea de estado.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Los mejores Mods de Claude Code, ordenados por lo que hacen por ti.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Mod de Claude Code: ve todas las imágenes y archivos que ha consultado tu…
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - A Claude Code mod that holds risky shell commands.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dos Mods de Claude para Claude Code: guardaespaldas.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Lazy Panda Panel para Claude Code: revisa documentos sin levantar una pata.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel lateral de estadísticas de sesión en vivo para la pestaña Code de la…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Varios mods y habilidades para mi configuración de Claude Desktop.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods para Claude Code: safety-guard bloquea comandos destructivos y el acceso a…
- [prompteafacil-hub/mods-claude-code](https://github.com/prompteafacil-hub/mods-claude-code) - Mods de Claude Code de la comunidad prompteafacil.
- [ptpmediabr/ideas-shelf](https://github.com/ptpmediabr/ideas-shelf) - Estantería de ideas por proyecto: anota ideas en un panel y márcalas como…
- [ptpmediabr/mods-manager](https://github.com/ptpmediabr/mods-manager) - Panel para ver, activar, desactivar, instalar y agrupar tus mods y plugins en…
- [ptpmediabr/side-chat](https://github.com/ptpmediabr/side-chat) - Un panel lateral de chat dentro de la sesión que responde preguntas o ejecuta…
- [ptpmediabr/usage-weather](https://github.com/ptpmediabr/usage-weather) - Una línea discreta sobre el prompt: contexto, uso de 5 horas y semanal, si la…
- [qarge/claude-mods](https://github.com/qarge/claude-mods)
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod de Claude Code: cotización bursátil en tiempo real, panel /quote, alertas…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Modificaciones de código de Claude, publicadas como un único mercado de plugins.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod de Claude Code: host SSH, RAM y límites de uso de 5 h/7 d en una fila sobre…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod de Claude Code: flexiones para hacer mientras Claude trabaja. Sin tokens.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - La tienda de mods para Claude Code: extrae mods de GitHub, muestra vistas…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod de Claude Code: convierte el plan que apruebas en modo plan en una lista de…
- [sadhirr1/claude-mods](https://github.com/sadhirr1/claude-mods) - Just a repo with different claude mods.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una lista seleccionada manualmente de mods de código de Claude.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sin coste: los agentes auxiliares se ejecutan en Haiku, y los archivos…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una banda sonora lo-fi que sigue la sesión: calma, concentración y fluidez…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprende mientras Claude programa: después de un turno que haya cambiado el…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una cinta de cada edición que hace Claude: reproduce cada cambio mientras se…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Cada enlace que menciona tu sesión, en una fila sobre el prompt.
- [SanjayPG/claude-code-usage-tracker](https://github.com/SanjayPG/claude-code-usage-tracker) - Claude Code mod: live usage-quota progress bars above your prompt.
- [SanjayPG/claude-quota-band.](https://github.com/SanjayPG/claude-quota-band.) - Claude Code mod: live usage-quota progress bars above your prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Demostración mínima de hooks de funciones de Claude Code: panel de tokens/coste…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board y otros mods de Claude Code de André Servaes.
- [shaheershoaib/agent-warehouse](https://github.com/shaheershoaib/agent-warehouse) - agent-warehouse: a Claude Code mod by Shaheer Shoaib.
- [shaheershoaib/usage-meter](https://github.com/shaheershoaib/usage-meter) - usage-meter: a Claude Code mod by Shaheer Shoaib.
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - Modificaciones de código de Claude (plugins de function-hook) de ShellTime.
- [siller/supermod](https://github.com/siller/supermod) - Claude Code mod: Superpowers progress, context window and agents above the…
- [simplybychris/claude-code-mods](https://github.com/simplybychris/claude-code-mods) - Mods para Claude Code: Rec Mode, Cache Bar, Snake y panel de agentes.
- [skryvets/claude-code-session-mod](https://github.com/skryvets/claude-code-session-mod) - Claude Code mod: coloured session info under the prompt - context, model…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Un mod de HUD de RPG acogedor para Claude Code.
- [sstani-bgv/claude-crew](https://github.com/sstani-bgv/claude-crew) - Mod de Claude Code: barra lateral de cangrejo pixelado para subagentes.
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Marketplace personal de mods de Claude Code: clean-view, where-am-i…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensajes de commit con un clic para Claude Code con una Malenia bailarina en…
- [StevenGFX/claude-gh-actions](https://github.com/StevenGFX/claude-gh-actions) - Claude Code mod: GitHub Actions runs in a /ci pane, the status line and toasts.
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude code mods.
- [stylusnexus/claude-mods](https://github.com/stylusnexus/claude-mods)
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Claude Code mods: mini-bar HUD.
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugins for Claude Code.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Mods for Claude Code: delete-guard.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Mod de Claude Code: consulta el uso de tu plan Claude.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Mod de Claude Code: panel de equipo en tiempo real para cada subagente.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod de Claude Code que muestra la sesión actual en un panel: cada aviso, el…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins de Claude Code de mods: plugins function-hooks que…
- [thickiran/claude-coaster-tycoon](https://github.com/thickiran/claude-coaster-tycoon) - 🎢 Claude builds you a RollerCoaster Tycoon-style theme park while it works.
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code mod: a docked pane showing the session.
- [tjanuki/claude-mod-context-meter](https://github.com/tjanuki/claude-mod-context-meter) - Claude Code mod: context-window fill in the status line and a hand-off reminder…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Haz que el uso de Claude Code te rinda hasta el doble.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Mods de Claude Code de Toptaab.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Mod de Claude Code: una banda y un panel que siguen a tus subagentes, junto con…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - A curated catalogue of Claude Code mods, each with a copy-paste prompt that…
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod de Claude Code: banda de progreso animada y resumen de finalización para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Three small Claude Code mods: see when your subagents will finish, queue…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di «I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Hazle a Claude una pregunta aparte en un panel junto a tu trabajo.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace de mods do Claude Code com instalação em um passo e guia em vídeo…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Rate-limit countdowns and a burn-rate forecast for Claude Code.
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Capa de seguridad de Roblox Studio para Claude Code: auditoría de RemoteEvent…
- [was865/usage-band](https://github.com/was865/usage-band) - Claude Code mod: context window, prompt cache hit rate and countdown, rate…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Claude Code mods: stage-toons, a workflow progress bar above the prompt with…
- [wolves/usage-line](https://github.com/wolves/usage-line) - Claude Code mod: usage, model, effort and advisor readout above the prompt.
- [wszaq/claude-mods](https://github.com/wszaq/claude-mods) - Pequeños plugins de Claude Code para flujos de trabajo locales más seguros y…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para Claude Code. agent-crew: observa trabajar a tus subagentes como un…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Mods de Claude Code: cápsula del siguiente paso en 繁中, copia de bloques…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Banda siempre activa sobre el prompt de Claude Code: carga de contexto y…
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - Personal Claude Code mods (plugin marketplace).
- [zhuzhu0710/claude-mods](https://github.com/zhuzhu0710/claude-mods)
- [ziedgithub/claude-code-mods](https://github.com/ziedgithub/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una colección cuidadosamente seleccionada de los mejores recursos para los…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin de Claude Code que muestra lo que está ocurriendo: uso del contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Línea de estado atractiva y altamente personalizable para Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas las partes del indicador de sistema de Claude Code, las descripciones de…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Más de 45 consejos para sacar el máximo partido a Claude Code, desde los…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / habilidad de Codex — genera carruseles de Xiaohongshu y pares…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Beautiful vim-style powerline for Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revisa el diff de tu agente de programación en un panel de terminal y envía…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de línea de estado completo para Claude Code con uso de contexto…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Seguimiento local de tokens de Claude Code y Codex — barra de estado.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crea modificaciones para Claude Code: intercepta cualquier solicitud, modifica…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Un panel completo de línea de estado para Claude Code — información de sesión…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: realiza un seguimiento de la huella de carbono de tus sesiones…
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Una línea de estado estética para Claude Code, creada por awesomejun.
- [fatihaydost/brand-identity-skill](https://github.com/fatihaydost/brand-identity-skill) - A Claude Code skill that designs a brand identity as one system: logo…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Habilidades y mods públicos de Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos de barra y guías para Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legales y gratuitos, y agentes de programación — actualización…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Línea de estado de terminal para sesiones de Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Resultados, calendarios y clasificaciones de fútbol en vivo para la…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Habilidad de agente que convierte tu agente de programación en un experto en…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuración personal de Claude Code versionada dentro de ~/.claude — agentes…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horarios de oración, fecha Hijri, adhkar, ayah diaria, ayuno sunnah, Ramadan…
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) - Tavily-powered optional search tool for DeepSeek Harness.
- [livlign/ccbit](https://github.com/livlign/ccbit) - Línea de estado consciente de las sesiones para Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DeepSeek Harness Research Graph · 研图 — Plugin de DeepSeek Harness para temas de…
- [igdigitallab/cardloop](https://github.com/igdigitallab/cardloop) - Your AI dev team on your own server, steered from your phone.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de herramientas de código Portable Claude para .NET DDD/Clean Architecture…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Colección de plugins para Claude Code, pi y DeepSeek Harness: HUD de barra de…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuración global portátil de Claude Code: skills personalizadas, hooks de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins de Claude Code que uso a diario: skills y mods, depurados para que…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram dentro de Claude Code: lee chats y canales en un panel y recibe…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Puente DSH &lt;-&gt; Feishu (Lark), desarrollado internamente (no es un fork)…
- [Dakaric/claude-code-statusline](https://github.com/Dakaric/claude-code-statusline) - Línea de estado integrada para Claude Code: barra de ventana de contexto, TTL…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins y skills de Claude Code para facilitar mods del juego…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gobernanza de tokens para Claude Code: el modelo principal dirige y la…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visor de panel dividido para Claude Code en Windows Terminal y tmux: la sesión…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods no oficiales para la pestaña Code de Claude Desktop — usage-pet: una banda…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositorio para mods Awesome Media de Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Reduce el gasto de Tokens de Claude Code y Codex: dirige las consultas y…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Alertas de límites de uso para Claude Code: notificaciones de macOS…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Línea de estado configurable de Claude Code para Linux, WSL, Windows y macOS…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Fast Rust statusline for Claude Code — payload-first, cached git, ~10ms renders.
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Línea de estado de Claude Code con barra de contexto, sparkline de tokens y…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Panel de uso en tiempo real para Claude Code — desglose del contexto, aciertos…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Muestra detalles clave del estado de Claude Code, incluidos el modelo, el…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - la línea de estado amigable y llena de opciones para Claude Code — barras…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Multi-row Claude Code status line: spend, context %, git, and active account…
- [QingqiShi/claude](https://github.com/QingqiShi/claude) - Personal ~/.claude for Claude Code: settings, global CLAUDE.md, hooks, status…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Línea de estado con información útil para claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Plantilla inicial para organizar un espacio de trabajo de Claude Code para…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipos de agentes nativos. Bajo control.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Línea de estado personalizada para Claude Code — barra de contexto con…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins de Claude Code con baloo: skills, un agente que verifica…
- [chrisns/claude-image-cli-mod](https://github.com/chrisns/claude-image-cli-mod) - Consulta las imágenes que imprimen los comandos.
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Línea de estado de Claude Code: uso del contexto, barras de cuota de 5 h/7 d…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Línea de estado de Claude Code de nivel profesional: duración de sesión, coste…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Línea de estado de Claude Code consciente de la suscripción.
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - A Claude Code plugin: a pane of the live Claude Code and Codex sessions on your…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - A rich terminal statusline for Claude Code — Bun + TypeScript, zero runtime…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Línea de estado de dos filas para Claude Code: contexto, límites de velocidad…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin de Claude Code que muestra diagramas Mermaid de forma atractiva en la…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Herramientas, habilidades y agentes para Claude Code — empezando por una línea…
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Claude Code global config: agents, skills, mods, settings.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Plugin de Claude Code: consulta siempre el límite de uso restante de 5 horas de…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Gasto real de DeepSeek de API para Claude Code: vuelve a calcular el precio de…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Línea de estado de Claude Code con filas del panel de agentes.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincroniza las tareas pendientes de Claude con Fizzy.do para que el equipo…
- [izzatum/claude-code-cockpit](https://github.com/izzatum/claude-code-cockpit) - Plugin de línea de estado de Claude Code (cockpit): contexto %, coste de la…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - A status line and token line for Claude Code: context, 5-hour and weekly usage…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Muestra una barra de estado detallada y codificada por colores para Claude…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menú de ajustes, línea de estado y configuración de Claude Code.
- [Larg0Winch/claude-label](https://github.com/Larg0Winch/claude-label) - Etiqueta editable por ventana en la línea de estado de Claude Code.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Habla con Claude Code por voz en Windows: un mod + ayudante que usa codex…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook de statusline de Claude Code — rastrea el uso de tokens y el contexto…
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Línea de estado personalizada de Claude Code con ventana de contexto…
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - Línea de estado rápida de Rust para Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - home-grown, cage-free claude plugins, skills, mods, and more.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalador del entorno de Claude Code: skills, barra de estado, hooks, permisos…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugins y mods de Claude Code para entender qué hace Claude: formatos de…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Supervisa el estado de Claude Code desde la barra de menús de macOS, con…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Barra de estado colorida de varias filas para Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Línea de estado de Claude Code para Windows (PowerShell): barras de uso…
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Plugins de Claude Code. Usage Bars muestra tus límites de frecuencia de la…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings and Glossary para Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Línea de estado personalizada de Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Configuración y mods de Claude Code, con un kit de componentes compartido, un…
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Un pequeño panel para Claude Code: porcentaje de contexto, cuenta atrás de la…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuración portátil de Claude Code: CLAUDE.md, ajustes, línea de estado…
- [thurtado1993/claude-cabina](https://github.com/thurtado1993/claude-cabina) - Cabina: a live session dashboard for the Claude Code Desktop side panel.
- [tichara1/ai.claude-status-panel](https://github.com/tichara1/ai.claude-status-panel) - Mod pro Claude Code: panel nad promptem s kontextem, limity, cenou, stavem…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Supervisa el uso del contexto de Claude Code, los costes de la sesión y los…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用の mod 集 (goal-orchestrator: /goal をタスク分解して SubAgent に委譲させる).
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Real-time cost tracking and session monitoring statusline for Claude Code.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Plugin de Cordis / DeepSeek Harness: el agente pide al humano un secreto en una…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Línea de estado de tres líneas de Claude Code: profundidad del contexto…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de degradación del contexto 2026 - Monitor proactivo de memoria de IA…
- [zerofaultlabs/claude-statusline](https://github.com/zerofaultlabs/claude-statusline) - Una línea de estado de Claude Code: uso del contexto, límites de velocidad…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes y líneas de estado de Claude Code: colecciones y herramientas…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Línea de estado de Claude Code — indicadores de uso de Claude/Codex que…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code statusline showing real-time token usage and estimated energy…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: paneles, bandas y compañeros creados sobre hooks de…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pasa tareas entre tus sesiones de Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Esto en un servidor MCP para controlar MODS, la herramienta modular…
- [pedrotspinola/lps-statusline](https://github.com/pedrotspinola/lps-statusline) - Statusline personalizada de Claude Code: modelo + nivel de esfuerzo, cuota de…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill de Codex y Claude Code para traducir mods de CK3 con un LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código abierto y otras extensiones para Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encuentra lo que pides a Claude Code una y otra vez y conviértelo en…

</details>

<a id="dsh-cordis"></a>

## Ecosistemas de complementos de DSH y Cordis

DeepSeek Harness y Cordis llegan al mismo punto desde direcciones diferentes: para ellos, el complemento es el mecanismo de mods, así que allí un complemento equivale a un mod aquí.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74280 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **74280**  |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100394 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **100394** |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81639 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **81639**  |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐70094 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **70094**  |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **35760**  |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30358 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Solución de escritorio moderna para el ecosistema de plugins de DeepSeek Harness (DSH). Todo es un «plugin»; el propio escritorio también es un «plugin».

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **30358**  |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25470 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Resumen

Distilly: destila cómo piensan en habilidades reutilizables para cualquier agente o bot. Anteriormente Colleague Skill（原同事 Skill）.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **25470**  |
| Último envío      | 2026-09-22 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Meta-framework de composabilidad espaciotemporal

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **9112**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8594 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **8594**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4266 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **4266**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3162 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Versión de escritorio de DeepSeek Harness Tauri | Instalador de solo 8 MB, configuración de entorno cero, plugins preconfigurados, Windows / macOS / Linux.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3162**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1583 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Una protección previa a la ejecución para agentes de programación de AI. Bloquea comandos destructivos de Git y del sistema de archivos, además de intentos habituales de acceder a archivos sensibles, antes de que se ejecute una llamada a una herramienta. Es compatible con Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode y Pi.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1583**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1167 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Memory for Claude Code, Codex, Cursor and 38 more coding agents, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Go                                                                                |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1167**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1139 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Go                                                                                |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1139**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1007 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

The most comprehensive DeepSeek Harness plugin market — refreshed daily, sourced across the Internet, reviewed before publishing.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1007**   |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐702 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **702**    |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **593**    |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-11 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin no oficial de DSH (DeepSeek Harness): utiliza los modelos web de chat.deepseek.com como proveedor de LLM mediante captura del inicio de sesión del navegador, resolución de PoW, transmisión SSE y llamadas a herramientas basadas en prompts.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **247**    |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
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
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
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
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐130 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

La instalación incluye 27 habilidades de ingeniería y productividad de mattpocock/skills v1.3.1, sin necesidad de instalarlas manualmente. Este plugin se ha creado con 40 000 millones de tokens y ofrece una eficiencia de desarrollo 10 veces superior a la de las habilidades originales; también ayuda a los principiantes a familiarizarse más rápidamente con este conjunto de habilidades. Se admiten plenamente los issues de GitHub; Markdown está en versión preliminar; GitLab todavía no es compatible. Gracias por usarlo y apoyarlo 💗

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **130**    |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐127 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **127**    |
| Último envío      | 2026-10-10 |
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
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐87 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Skills y plugins de You.com para búsqueda web, extracción de contenido, investigación, finanzas y descubrimiento de integraciones, que ayudan a los agentes de IA a trabajar con contexto web actualizado.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **87**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐85 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

StudyHub: un plugin de DeepSeek Harness (DSH) que convierte tus propios materiales en preguntas y repasos espaciados · plugin de aprendizaje de DSH que convierte tus materiales en preguntas y repasos espaciados

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **85**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

dsh-sieve: plugin de ingeniería de contexto y optimización de tokens para DeepSeek Harness (DSH) — filtrado de resultados de herramientas, poda de contexto y divulgación progresiva de habilidades. Carga útil un 36 % menor en la reproducción sin conexión. Plugin de gestión de contexto y optimización de tokens de DSH para ahorrar tokens.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **72**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Mercado que clasifica, recopila y verifica automáticamente los plugins de la comunidad de DeepSeek-Harness. Clasifica, recopila y valida automáticamente el mercado de plugins de la comunidad de DeepSeek-Harness.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **69**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐57 · HTML · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **57**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐27 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

NekroNXT: sistema de agentes de chat grupal multiplataforma basado en DeepSeek Harness (DSH) | Sistema de agentes de chat grupal multiplataforma impulsado por DSH

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **27**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zp-home/dsh-recommend">zp-home/dsh-recommend</a></b> · ⭐22 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Ranking y recomendaciones transparentes del ecosistema de plugins de DSH: recopila automáticamente cada día el tema dsh-plugin + modelo de puntuación público + plugins clasificados/recomendados y sitio estático

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **22**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `deepseek-harness` · `dsh-plugin` · `plugin` · `rankings` · `recommendations`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zp-home--dsh-recommend/fbc10141cf0df5b3.png" width="100%" alt="zp-home/dsh-recommend screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-superpower">Wenaixi/dsh-superpower</a></b> · ⭐21 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de DeepSeek Harness: 15 habilidades de ingeniería de obra/superpowers, descripciones bilingües y activación independiente por habilidad | Plugin de DeepSeek Harness: 15 habilidades de disciplina de ingeniería de obra/superpowers, con cambio libre entre descripciones bilingües y activación independiente de cada habilidad

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **21**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agent` · `brainstorming` · `chinese` · `code-review` · `cordis` · `debugging` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-superpower/72fd369dacf071c0.png" width="100%" alt="Wenaixi/dsh-superpower screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-mcp-manager-ui">Imzl-zl/dsh-mcp-manager-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Interfaz de gestión del servidor MCP para DeepSeek Harness Web — panel flotante, importación de JSON y persistencia basada en perfiles.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **20**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-mcp-manager-ui/344d069db6cf421d.png" width="100%" alt="Imzl-zl/dsh-mcp-manager-ui screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/pptwise">liustack/pptwise</a></b> · ⭐19 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Un PowerPoint real, no HTML. Dile a tu IA qué debe incluir y pptwise creará una presentación editable en tu propia máquina. Habilidad de agente + plugin de DSH, sin cuenta ni clave de API para renderizar. | Un PPT real, no HTML. Dile a la IA qué quieres explicar y pptwise creará un PPT editable en tu propio ordenador. Habilidad de agente + plugin de DSH, sin registro y sin clave de API para renderizar.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **19**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skill` · `agent-skills` · `ai-agent` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deck-generation`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--pptwise/e6f193d6fc2ea355.png" width="100%" alt="liustack/pptwise screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-ponytail">Wenaixi/dsh-ponytail</a></b> · ⭐18 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de DeepSeek Harness: modo senior perezoso y port de escalera de 7 peldaños de DietrichGebert/ponytail, 6 habilidades con descripciones bilingües y activación independiente, cero herramientas y cero fallos de caché | Plugin de DeepSeek Harness: port perfecto del modo senior perezoso y la escalera de siete peldaños de DietrichGebert/ponytail, 6 habilidades con cambio libre entre descripciones bilingües, activación independiente de cada habilidad, cero registros de herramientas y cero destrucción de caché en todos los escenarios

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **18**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `agent-skills` · `ai-agents` · `claude-code` · `code-review` · `cordis` · `cursor` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-ponytail/ffd031e53f39269a.png" width="100%" alt="Wenaixi/dsh-ponytail screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KannaKuron/dsh-better-workspace">KannaKuron/dsh-better-workspace</a></b> · ⭐17 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin web de DSH: árbol jerárquico de espacios de trabajo para la barra lateral — los títulos que contienen / se agrupan en carpetas virtuales; el flujo de adición de espacios de trabajo incorpora una ventana emergente de grupo principal

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **17**     |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-10 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `sidebar` · `tree` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kannakuron--dsh-better-workspace/83cddff440dfe49a.png" width="100%" alt="KannaKuron/dsh-better-workspace screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 63</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Una lista seleccionada de los mejores plugins de IA para asistentes de IA…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins de DSH / DSH Plugin Marketplace: explora, instala y…
- [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) - Remote-work assistant for DeepSeek Harness (DSH): connect SSH.
- [morluto/flameox](https://github.com/morluto/flameox) - Runtime evidence that helps agents trace, profile, and burn down hotspots in…
- [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) - DSH plugin - framework upgrade safety &amp; plugin gating: contract pre-check…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins para programas que siguen ejecutándose — núcleo Rust…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Comunidad de agregación de plugins de DeepSeek Harness — sincronización…
- [mrRisega/dsh-remote](https://github.com/mrRisega/dsh-remote) - 公网远程控制 DeepSeek Harness.
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directorio seleccionado de plugins de DeepSeek Harness (DSH): más de 280…
- [Cerbur/clutch-dsh](https://github.com/Cerbur/clutch-dsh) - Open-source DSH plugins for DeepSeek Harness：Git Worktree session…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin: Git Bash shell for all agent modes on Windows.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Kit de herramientas de Zotero para DeepSeek;
- [maxwell-feng/dsh-tinyfish-search](https://github.com/maxwell-feng/dsh-tinyfish-search) - TinyFish-backed web search provider for DeepSeek Harness (ctx.web) — 将内置…
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - Acción comunitaria GitHub para DeepSeek Harness — revisión de código con AI ·…
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Banco de trabajo de escritura local para autores de novelas web en chino.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, herramientas, habilidades y recursos de aprendizaje de DeepSeek…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [miuzel/dsh-graph](https://github.com/miuzel/dsh-graph) - 把工作组织成目标看板的 DeepSeek Harness (dsh) 插件：目标 / 判据 / 上下文卡片 / 执行 attempt…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Convierte los modelos con sesión iniciada en el escritorio local de WorkBuddy…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Pruebas aisladas de instalación y humo para plugins de DeepSeek Harness…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Plugin de base de funciones de DeepSeek Harness: un único panel para…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pruebas de compatibilidad siempre activas para plugins de DeepSeek Harness…
- [gezi-wen/sage-mem](https://github.com/gezi-wen/sage-mem) - File-based cross-session memory for DeepSeek Harness (DSH) — every memory is a…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeekBot: la alternativa de código abierto a GrokBot, creada sobre DeepSeek…
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - The bilingual, source-backed registry and installer for the DeepSeek Harness…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayos X para plugins de DeepSeek Harness: capacidades declaradas frente a…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host de DeepSeek Harness que mantiene los documentos del proyecto y la…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Podman-backed execution for DeepSeek Harness (dsh).
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Local-first voice conversations for DSH.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: una ventana de herramientas Git de nivel IDE como pestaña nativa de…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC 模式基础上的创造模式:DSH 插件,合成 Code Mode 工具编排 + 自引用 Cordis 工具与 preset 创作指导,物化为…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plugin de flujo de trabajo de ingeniería para DeepSeek Harness: etapas de…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH 角色扮演插件：角色卡（系统提示词注入 + 用户提示词改写）、可分享的单文件卡包、复刻原版 UI 的角色页签与首轮选角 chip.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Estándar de verificación sin dependencias para plugins de DeepSeek Harness…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Mercado de plugins de DeepSeek Harness: explora, busca e instala plugins del…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode en DeepSeek Harness — plugin de DSH que mantiene funcionando OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — mercado de plugins de terceros y gestor de ciclo de vida protegido…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx es un espacio de trabajo de escritorio ampliable y centrado en las…
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh daemon: registra el servidor web de DeepSeek Harness (dsh web) como un…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Plugin de experiencia de entrada web de DSH: alternancia de teclas para…
- [grloper/dsh-claude-oauth](https://github.com/grloper/dsh-claude-oauth) - Claude Pro/Max OAuth model provider for DeepSeek Harness with Google/Gmail…
- [iasiv5/dsh-skip-browser-auth](https://github.com/iasiv5/dsh-skip-browser-auth) - DSH 插件：（Web Profile 专用）自动跳过 BrowserAuth，访问 Web 地址即可直接使用，无需每次复制启动 URL 中的随机 Token…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Proporciona a la edición de escritorio de DeepSeek Harness un punto de acceso…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin de DeepSeek Harness: convierte el fallo de aprovisionamiento de ACL del…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Permite volver a intentar un intento vacío de modelo sin atribución, para la…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins de Rust con un kernel de ciclo de vida verificado por…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Mercado de plugins de dsh: descubrimiento automático y sincronización…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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

| Lenguaje   | Entradas | Ejemplos                                                                                                      |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 396      | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                          |
| JavaScript | 87       | `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                  |
| Python     | 43       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 16       | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7        | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2        | `rainyfei/claude-statusline-win`, `YangShen-SWE/dsh-plugin-simple-pet`                                        |
| Swift      | 2        | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1        | `reporails/arcade`                                                                                            |

<sub>Solo se contabilizan las entradas que declaran un idioma. Las entradas de documentación y debate se excluyen de esta tabla.</sub>

## Contribuir

Las correcciones son bienvenidas y son la forma más rápida de mejorar esta lista. Abre un issue o una pull request si una entrada está mal clasificada, tiene una categoría incorrecta o si un proyecto se ha excluido por error debido a una coincidencia de nombres; esta última categoría es donde más probablemente fallen los filtros automatizados.

---

<sub>Proyecto independiente de la comunidad. No está afiliado a Anthropic, ni cuenta con su respaldo o revisión. Claude Code, Claude y Anthropic son marcas comerciales de Anthropic. El comportamiento del producto puede cambiar sin previo aviso; verifica cualquier aspecto esencial en la documentación oficial. Los recursos siguen siendo propiedad de sus proyectos de origen y se reproducen únicamente cuando una licencia lo permite.</sub>

<sub>Última actualización · 2026-10-11T05:58:46+08:00</sub>
