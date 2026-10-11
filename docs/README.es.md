<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods increíbles de Claude">
</p>

<h1 align="center">Mods increíbles de Claude</h1>

<p align="center"><b>El índice de mods y plugins de Claude Code, clasificados según la evidencia, y del comportamiento más profundo que modifican.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-591-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <b>Español</b> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice activo** · Última sincronización: `2026-10-12T06:04:10+08:00` (UTC+8)
> · Entradas: **591** · Añadidas en la última actualización: **0** · Lenguajes de implementación: **12**

<sub>Todas las entradas siguientes se recopilaron, filtraron y revisaron de nuevo automáticamente. Nada de lo que aparece aquí es contenido promocional de pago.</sub>

<a id="featured"></a>

## Selecciones del momento

<sub>Una entrada por categoría, clasificadas según el nivel de evidencia y las estrellas, y recalculadas con cada actualización. Es una clasificación, no una recomendación; cada selección enlaza con su ficha completa más abajo. Se prefieren los proyectos que han publicado una captura de pantalla o una grabación, para que la franja siga siendo visual.</sub>

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
<sub>⭐2535 · Python · 👁️ observed</sub>
<sub>Encuentra los tokens fantasma. Arréglalos. Sobrevive a la compactación. Evita el deterioro de la calidad del contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74358 · TypeScript · 👁️ observed</sub>
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
- [Oficiales: repositorios propios y notas de versión de Anthropic](#oficiales-repositorios-propios-y-notas-de-versión-de-anthropic) — **14**
- [Mods: creados con la capacidad de mods](#mods-creados-con-la-capacidad-de-mods) — **460**
- [Ecosistemas de complementos de DSH y Cordis](#ecosistemas-de-complementos-de-dsh-y-cordis) — **106**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150215 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Resumen

Claude Code es una herramienta de programación agéntica que funciona en tu terminal, comprende tu base de código y te ayuda a programar más rápido ejecutando tareas rutinarias, explicando código complejo y gestionando flujos de trabajo de git, todo mediante comandos en lenguaje natural.

<sub>🔧 Encontrado en el código: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |
| Lenguaje  | TypeScript                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **150215** |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9479 · TypeScript · ✅ official · 2 天</summary>

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
| Estrellas         | **9479**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| Estrellas         | **8249**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6346 · Python · ✅ official · 242 天</summary>

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
| Estrellas         | **6346**   |
| Último envío      | 2026-02-11 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| Estrellas         | **1798**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

##### 📝 Resumen

Materiales complementarios para las tarjetas de modelo Claude

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
<summary><b>Más en esta categoría</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Se añadió `$.ui.notify` para los mods: muestra una notificación nativa mediante…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Corregido Esc o una interrupción durante un hook de `UserPromptSubmit` o un…

</details>

<a id="mods"></a>

## Mods: creados con la capacidad de mods

Cada entrada aquí muestra pruebas de que usa la capacidad que Claude Code obtuvo en 2.1.287: renderiza mediante `ui.render`, incluye un panel, una banda o una tarjeta, lee `$.ui.selection()`, genera compañeros con `agent.spawn`, o afirma claramente que es un mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2535 · Python · 👁️ observed · 0 天</summary>

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
| Estrellas         | **2535**   |
| Último envío      | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐497 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Catálogo comunitario de mods públicos de Claude Code (hooks de funciones), analizados desde GitHub con información sobre lo que cada mod puede leer, escribir, ejecutar o enviar por la red. Explora https://mods.aidojo.si/

<sub>🔧 Encontrado en el código: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **497**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐188 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Mods de Claude Code: plugins basados en hooks que añaden líneas dinámicas sobre el prompt, protecciones, paneles y juegos. Barra de contexto, medidor de uso, monitor de revisión de Codex, vista previa de Markdown, reproducción actual de Spotify y mucho más.

<sub>🔧 Encontrado en el código: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **188**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐142 · TypeScript · 👁️ observed · 7 天</summary>

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
| Estrellas         | **142**    |
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
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐99 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Skins for Claude Code: tool rows with icons, diff, table and Mermaid chart cards, a usage band and fifteen themes. /skin swaps them live.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **99**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐91 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **91**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐78 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **78**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

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
| Estrellas         | **78**     |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐67 · TypeScript · 👁️ observed · 9 天</summary>

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
| Estrellas         | **67**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

##### 📝 Resumen

Mods de Claude Code creados por Darrell Wang — bandas sobre el prompt, sin tokens del modelo. Paneles de acciones de Taiwán y EE. UU. + más próximamente.

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
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Resumen

Skills, agentes, comandos, reglas, hooks y estilos de salida expertos para Claude Code — continuidad de sesión + herramientas modernas de CLI para flujos de desarrollo del mundo real

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
| Estrellas         | **59**     |
| Último envío      | 2026-10-07 |
| Primera inclusión | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Resumen

Mods de Claude Code: barras de progreso del plan en tiempo real sobre el prompt

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **46**     |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>grabación animada · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Abrir vídeo</a></sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Un Pokémon pixelado que vive sobre el prompt en Claude Code

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | JavaScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **25**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>grabación animada</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Resumen

Compilación, pruebas, consola y vistas previas de SwiftUI de Xcode dentro de Claude Code

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
| Primera inclusión | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Mods de Claude Code: 21 estilos y un conjunto completo de funciones que activas cuando las necesitas, para el terminal y la aplicación de escritorio. · Aplica un nuevo estilo a Claude con un clic y ofrece un conjunto completo de funciones activables según las necesidades.

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
| Primera inclusión | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

##### 📝 Resumen

Diez mods de Claude Code, guías para principiantes, prompts de creación, demostraciones seguras y una plantilla para crear los tuyos.

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
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Use Codex, GLM, and other coding agents as Claude Code subagents.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **16**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Mods de Claude Code: usage-band muestra tus límites de 5 h/7 d, la ventana de contexto y la tasa de aciertos de caché sobre el prompt

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **13**     |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/paulbkim-dev/claude-code-cache-warmer">paulbkim-dev/claude-code-cache-warmer</a></b> · ⭐13 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Claude Code mod that keeps the prompt cache warm and shows each refresh's cost and saving

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **13**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `claude-code` · `claude-code-plugin` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Resumen

Mods de Claude Code que hacen que las preguntas de Claude sean más fáciles de leer y responder (qa-guide).

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
| Primera inclusión | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>grabación animada · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Abrir vídeo</a></sub></td>
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Diez mods de código abierto para Claude Code: paneles dinámicos, bandas, líneas de estado y protecciones para llamadas a herramientas. Medidor de consumo, códigos de lanzamiento, sesión finalizada, pelea contra el jefe, mascota de código y mucho más.

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
| Primera inclusión | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Resumen

Dos mods de código de Claude: puente de uso del ordenador de Codex y sesiones coordinadas de Claude. Código fuente, prompts de compilación, configuración y pruebas.

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
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
| Estrellas         | **9**      |
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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 3 天</summary>

##### 📝 Resumen

Una interfaz para tus terminales de Claude Code y Codex que construyen tus agentes, para que el único modelo en tu cabeza sea el tuyo.

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
| Primera inclusión | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Resumen

KOZMOS — mods visuales en directo para Claude Code (CLI + escritorio): bandas sobre el prompt, barras laterales, ticker de estado, compañeros, protectores y sonido.

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
| Primera inclusión | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Seis mods de Claude Code en un solo plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) con interruptores por mod, además de un informe de mods frente a hooks.

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
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Resumen

Colección de mods de Claude Code de 개발동생. Paquete taxi: taxímetro, navegación, cámaras de control de velocidad y dashcam

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
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Ver en youtube.com</a> · la reproducción se abre en el sitio anfitrión; GitHub no puede insertarlo en línea</sub></td>
</tr></table>

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
<summary><b>Más en esta categoría</b> <sub>· 426</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Colección de más de 100 mods que puedes usar con Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods de Claude y las herramientas para crearlos: primero una skill de creación…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - El harness de Claude Code que uso a diario, publicado con este nombre desde el…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Dale un nuevo techo a Claude Code con Claude Mods: cambia los avisos del…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cuatro mods de Claude Code: Cache Keeper, Recording Mode, Goal Meter y…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods de Claude Code de Learning Hacker: convierte el funcionamiento del agente…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods de Claude Code que corrigen y traducen tus prompts antes de que Claude los…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods de código y habilidades de Claude Code de Nekyia Labs, creados y usados a…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 为Claude Code的终端记录打造桌面应用外观的mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un panel lateral para Claude Code: los subagentes que ejecuta una sesión, qué…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conocimiento de Obsidian con fuentes citadas sobre los mods de código…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel de barra lateral de Claude Desktop (pestaña Code): enumera todas las…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Habilidad que enseña a los agentes de Claude Code a crear Mods de Claude…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso encima del cuadro de entrada de Claude Desktop (pestaña Code)…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins y habilidades comunitarios de Claude, instalables desde un único…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods de Claude (plugins de enlaces de funciones) para Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galería de mods de Baselane: mods de Claude Code, revisados y fijados.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una cola de decisiones CLI/TUI para personas que trabajan con agentes…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods de Claude Code: panel de uso usage-hud 像素螃蟹 y enlaces HTML en los que se…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Tarjeta de estado flotante para Claude Code — modelo, contexto, límites de…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods para Claude Code: plugins de enlaces de funciones que añaden paneles…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nombres y secretos al compartir la…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Panel GSD en vivo para Claude Code: roadmap, árbol de agentes con forks…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensiones de Claude Code. Desbloquea todo el potencial de Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) de Claude Code que añade un panel lateral con pestañas Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Paneles, protecciones y mods para mejorar la experiencia de Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dos mods de Claude Code sobre el cuadro de prompts: medidor de la ventana de…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Haz que el plan Claude Pro dure más: mods de Claude Code para un HUD de uso…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lee los archivos markdown que nombra Claude Code, renderizados junto a la…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Compañero de voz para Claude Code. Habla sobre tus ideas con un lobo 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, un velocímetro de escritura en directo con…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuegos artificiales para Claude Code: cada pulsación, llamada a herramienta…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubre mods, plugins y extensiones de Claude Code con demostraciones…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas de mermaid dibujados dentro de la transcripción.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods y skins para Claude Code: una barra de progreso en directo para las tareas…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequeños mods de Claude Code (plugins de function-hook): session-switcher y más.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imágenes pegadas sobre el prompt, en…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods de Claude Code: menú de herramientas de Claude, modo Zen, temas de…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods de Claude Code: mod-scout (encuentra los mods que más usarías)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dos mods de Claude Code para ejecutar muchas sesiones a la vez: una tarjeta de…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: descubre, inspecciona, activa y actualiza mods de Claude Code.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods de Claude Code: barra de contexto, panel de agentes y desenfoque PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Los mejores mods de Claude Code: seleccionados, validados y fijados.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin de Claude Code: enrutamiento automático de modelos Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Seis mods para Claude Code: mascota Clawd animada, barras de límite de uso y…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Un marketplace de mods para Claude Code: depurador paso a paso para el ciclo…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: límites de plan y contexto sobre el prompt, un coach…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - El mejor paquete de mods todo en uno para Claude Code: límites de uso y HUD del…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Reproduce YouTube Shorts en tu Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de herramientas Claude de Naren: skills, mods y servidores MCP para Claude…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod de Claude Code que muestra las diferencias de Edit y Write en dos columnas…
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code mod that lets Claude log unfinished work to Docs/todos.md, with a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods para Claude Code: Clawd, una diminuta mascota pixelada que representa lo…
- [reporails/arcade](https://github.com/reporails/arcade) - Juegos de escritorio clásicos como mods de Claude Code, jugables en un panel…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Una lista seleccionada de mods de código de Claude Code, instalables como un…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de Claude Code bajo demanda — una habilidad que lee tu conversación y crea…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Un plugin de Claude Code muy particular, diseñado por un Rustacean obsesionado…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantienen honesto a un agente: enlaces de funciones que…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Mi colección de mods de Claude Code, un mod por directorio.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 适用于Claude Code的被动攻击式喝水提醒。零token，最大限度的评判.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Los mods de Claude Code que uso.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: un mod de Claude Code para diseñar y ejecutar grafos de agentes…
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Panel del notch de macOS para Claude Code: límites de uso, sesiones abiertas…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Una prueba de mecanografía para pasar el tiempo mientras Claude trabaja.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod por Claude Code: barra de caché del prompt, próximos pasos, botones rápidos…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods para Claude Code: paneles, comandos y hooks creados con el plugin de…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Recorta las enormes salidas de herramientas antes de que llenen el contexto de…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - 在Claude Code的提示词页脚和提示词上方，一览提示词缓存、上下文和计划限额.
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Cost, tokens and plan limits of your coding agents.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code que muestra tus límites de uso y gasto en la banda sobre…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods de Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods de Claude Code: barras de progreso para planes, un registro de lo que…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Mira lo que Claude Code ejecuta en segundo plano: subagentes, trabajos de…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mods de Claude Code de MacLeod Labs: streams desenreda el trabajo intercalado…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo del primer día sobre mods de Claude Code en Windows: una barra…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods que hice y uso personalmente en mi configuración de Claude Code.
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: un depurador para las llamadas a herramientas de Claude Code.
- [olddonkey/cache-refresher](https://github.com/olddonkey/cache-refresher) - Mod de Claude Code: muestra cuándo caduca la caché de prompts y cuánto costaría…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod de Claude Code: medidores en vivo de coste, contexto y cuota del plan…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Un mod de Claude Code que retiene la distribución de subagentes, las…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills para Claude en cinco paquetes.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods para claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod de Claude Code que activa o desactiva tus habilidades, agentes, reglas y…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins (mods) de Claude Code: cambia entre varias cuentas de Claude, supervisa…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de código de Claude probados e instalables con un comando: protecciones…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods para Claude Code: plugins creados sobre hooks de funciones.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Créditos al estilo cinematográfico para tu sesión de programación.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace de mis propios mods de Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un montón de mods de claude code creados por mí.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods de Claude Code. touch-map: muestra qué archivos enumeró, leyó, editó o…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprende un idioma extranjero mientras trabajas con Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Babysits a long Claude Code session so you don.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Mods de Claude Code para ejecutar muchas sesiones en muchos repositorios desde…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de coste, tokens y uso del contexto en tiempo real para Claude…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Objetivo, tareas y agentes por encima de tu prompt de Claude Code, sin…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio por Internet dentro de Claude Code: barra lateral cliamp…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Mods divertidos y útiles de Claude Code: una criatura pixelada sobre tu prompt…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude está cocinando. Chatea con tu escuadrón.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods de Code de Claude para Engineers reales.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Resumen de la sesión de terminal de Claude Code, en la pestaña Code de la…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Una batalla espacial sobre el prompt de Claude Code mientras trabaja.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Ve qué archivos tiene cada agente de Claude Code en su contexto, y cuánto de…
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Mod de Claude Code: línea de estado con la memoria, la CPU y el tiempo de…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Mantén la cabeza fría. Un termómetro para tus días de Claude Code: cada hora…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequeños mods de Claude Code para el terminal y la aplicación de escritorio.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Mods de Claude Code (mercado de plugins): barra lateral en directo con…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod de Claude Code: un panel de progreso para tareas, subagents, ejecuciones de…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod de Claude Code: límites de tasa del plan, llenado de contexto, coste de…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidad + mod de Claude CLI que añade palabras en español a las respuestas…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Tus eventos de Alarum sobre el prompt de Claude Code: qué acaba de llegar y una…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Tu lista de pendientes de Floatee sobre el prompt de Claude Code: ejecuta, guía…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra lateral al estilo de Evangelion para Claude Code: contexto, cuota…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code que lo rediseña como The Machine de Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：用于强制执行并验证subagents DAG工作流的Claude Code mod，带有实时DAG面板.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código abierto para Claude Code: paneles, líneas de estado…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Un mod de Claude Code: un panel para cada subagente, los archivos que toca y el…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod de Claude Code: estado de sesión, progreso en vivo de Spec Kit y…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La ventana de contexto como una fila sobre el prompt, dibujada como Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tareas en tiempo real para Claude Code Desktop: una franja sobre el…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuito y de código abierto para Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Guarda prompts para más tarde y devuélvelos al cuadro de entrada de Claude…
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Mod de Claude Code que muestra imágenes integradas en Ghostty y kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un Mod de Claude que muestra las solicitudes de extracción de GitHub de la…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mods de Claude Code: cambio automático y barra de progreso.
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Mod de Claude Code: genera efectos de sonido a partir de prompts de texto con…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Habilidades de Claude Code: un verificador de hechos de documentación, un…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Claude Code mod that rewrites rough prompts into clear ones before you send…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod de Claude Code: líneas de código de hoy por Claude — nuevas, editadas…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod de Claude Code: rutas clicables en las respuestas;
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compañero de Claude Code: un acompañante ASCII sobre el prompt que…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Mod de Claude Code: enrutamiento de modelos/esfuerzo guiado por Jev, compresión…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Modificaciones de Claude Code: capa de seguridad para Claude Code: redacción de…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Una colección de mods de Claude Code.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin y mod de Claude Code: un SDLC nativo de IA.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Colección Awesome de mods de Claude Code | Colección de mods de 클로드 코드.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Mods de Claude Code: paneles en directo y hooks para el trabajo diario.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Habla: un mod de Claude Code que lee en voz alta, cuando se solicita, las…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Azota a Claude cuando se equivoca — un mod antiestrés para Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code: pequeños plugins para paneles en tiempo real, enrutamiento…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod y plugin de Claude Code: monitor de uso, rastreador de tokens y línea de…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Un mod de Claude Code que delega las decisiones pequeñas en un modelo de…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod de Claude Code que informa en directo de qué archivos cambió Claude y por…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Mods de Claude Code de afterever (mercado de plugins).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Mod de Claude Code: dirige cada subagente al modelo Claude más barato, evaluado…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Modificaciones de Claude Code: tarjetas de estadísticas de la sesión sobre la…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gato braille animado sobre el prompt de Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code: dirige el trabajo barato a GLM/Kimi mediante un Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gato pixelado sobre el prompt de Claude Code que ejecuta una llamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code que elige un buen momento para compactar y mantener…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods para Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Mercado de plugins de Claude Code de anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods de propósito general para Claude Code: bandas, paneles, toasts y hooks.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - Mis mods privados de Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Tus límites de uso de Claude como una tarjeta animada de salud de aldeano, con…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mods de Claude Code para el equipo S2 (el otro mercado).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - Un mod de Claude Code que hace que Claude escriba en inglés sencillo y señala…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Entrenamientos cortos mientras Claude trabaja: un objetivo diario, rachas…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un panel de uso para Claude Code: gasto por modelo.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Un mod de Claude Code: desglose del contexto de la ventana en directo sobre el…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para Claude Code: Apple Music y Spotify sobre el aviso, con…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: reloj de caché, radio de impacto, sugerencias, lista de…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un búho para tu Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Banda de Claude Code de una línea.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - El motor original de Doom con Freedoom, jugable dentro de Claude Code.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Panel de diccionario de palabras y plugin de barra de estado de Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Un mod de Claude Code que mantiene una lista continua de los elementos abiertos…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Revisa cada archivo que Claude modifica, como una solicitud de incorporación de…
- [CTeitzel/cache-band](https://github.com/CTeitzel/cache-band) - Claude Code mod: a band above the prompt with the prompt-cache countdown, cache…
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Mods de Claude.
- [danielmertens/Claude-mods](https://github.com/danielmertens/Claude-mods) - Collection of personal Claude mods.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi que vive dentro de Claude Code: eclosiona, se come el código que…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [dbroadhurst/claude-mod-goal](https://github.com/dbroadhurst/claude-mod-goal) - Un panel Goal para Claude Code: el objetivo general hacia el que trabaja…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Turn every Claude Code session into a little adventure: generative music that…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - Mod de Claude Code para explicar los comandos ejecutados por el agente.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mods de Claude Code escritos como hooks de funciones y el marketplace que los…
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Un mod de Claude Code: una banda sobre el prompt con noticias de Claude y las…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod de Claude Code: después de que un guard bloquee una llamada a una…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod de Claude Code: trabajos en segundo plano en una sola vista, con progreso y…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod de Claude Code: una sola bandeja de entrada para mensajes de compañeros de…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod de Claude Code: explica los bloqueos del sandbox y convierte los bloqueos…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoritos para Claude Code: iconos de un clic para tus comandos y skills.
- [Dyarchia/dyarchia](https://github.com/Dyarchia/dyarchia) - Dyarchia: compilación y Kanban en todas las superficies.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ¡Ey, lo silencié! Deshazte del diff, corta el riff;
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Mods de Claude Code: rewrite-prompt.
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instrucciones, skills, extensiones de Pi y mods de Claude Code para Pi, Codex y…
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code mods: delete-guard (confirmar eliminaciones de archivos) y…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod de Claude Code: uso de la suscripción (5h / 7d) como una banda sobre el…
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Mods de Claude Code: auto-model-detector dirige cada prompt al modelo y nivel…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar en tiempo real de tus ramas y worktrees paralelos sobre el prompt…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Mods de Claude Code (plugins function-hook): banda de contexto, cabos sueltos…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mods de Claude Code (plugins de enlaces de funciones), instalados a través de…
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Claude Code plugin marketplace with my mods.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Mods en alemán para Claude Code: avisos de contexto/caché, puntos pendientes…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Claude Code mod: a pixel-art squad suggests the right model.
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Mod de Claude Code: tres próximos pasos después de cada respuesta, en cualquier…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de Claude Code: cuánto tardó cada respuesta, cuánto tiempo pensó Claude y…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mods de Claude Code: el modo streamer oculta los paneles privados, las bandas y…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - para mis mods de claude.
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Plugins de hooks de funciones de Claude Code (mods).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod de Claude Code: espera a que pase el límite de uso de 5 horas y envía…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Una cabina sobre tu indicación de Claude Code. El pato lee los medidores.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Mods de Claude Code (plugins function-hook): seguimiento posterior a la fusión…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Pequeños mods de Claude Code: indicadores de contexto y uso del plan, un…
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Mod de Claude Code: uso de tokens, modelos y subagentes en directo por prompt.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel lateral de uso del contexto: total, categorías, crecimiento por ronda…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista lateral de archivos: qué archivos se han creado, modificado o eliminado…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, un conejo belier neerlandés en blanco y negro con estilo de 8 bits, corre y…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel lateral de «Lo que he preguntado»: cada frase que el usuario ha escrito…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Línea de tiempo lateral: en qué se ha empleado el tiempo de esta ronda…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Intercambio de tokens en el panel lateral: cuántos tokens envía la conversación…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - El bocadillo de tofu honesto de claude code: al terminar cada ronda, Claude…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Pequeños mods para Claude Code, como nuevos comandos de barra y paneles…
- [juro-mont/claude-ev-charging](https://github.com/juro-mont/claude-ev-charging) - An EV-charging progress bar and session panel for Claude Code helper agents.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive en una banda sobre tu prompt de Claude Code: representa la sesión…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod que lee en voz alta las respuestas y notificaciones de Claude Code mediante…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod de Claude para leer y unirse a las conversaciones entre tus sesiones de…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods de Code de Claude. PixBar: una criatura pixelada sobre tu prompt que se…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - mods de claude.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Mods de Claude Code (usage-meter, ...).
- [koenrohrer/hearth-band](https://github.com/koenrohrer/hearth-band) - Mod de Claude Code: una criatura pixelada por modelo junto a una fogata de…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dos mods de Claude Code: folio, un panel de archivos junto al chat, y tint, un…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: un gráfico en tiempo real de lo que sabe Code de Claude.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - No dejes que tu atención se desvíe mientras esperas la respuesta de Claude Code.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Mods de Claude Code de Sanmu — un marketplace de plugins.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guía de Mods de Claude Code seleccionada por la comunidad: casos de uso…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Mods individuales de Claude Code de Mod Box, cada uno instalable por separado.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Catorce mods de Claude Code en un solo plugin, cada uno activable por separado…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de Claude Code que muestra lo que Claude está haciendo en el subtítulo…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: answer Claude point by point, right on the text.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod de Claude Code con perfiles de permisos intercambiables: una base…
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Pequeños mods para Claude Code: runner-avatar, un pequeño avatar que corre…
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of what your AI coding agent is aiming for…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods de la comunidad para Claude Code: protecciones, paneles y comandos que se…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel lateral para Claude Code: archivos que escribió Claude, divisiones del…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un discreto panel lateral para Claude Code: qué está haciendo esta sesión, su…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Una hora atenuada sobre cada prompt y cada respuesta en la transcripción de…
- [mmedum/spor](https://github.com/mmedum/spor) - Devuelve lo que Claude oculta: los archivos que Claude leyó, los comandos que…
- [mrkshw/cold-cache](https://github.com/mrkshw/cold-cache) - Claude Code mod: warns when a session.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de código de Claude que vuelve a activar las herramientas de tareas para…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod de Claude Code que espera una pausa segura y después entrega tu sesión o la…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de código de Claude: una línea por tarea encima del prompt con la tarea…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Juega Connect Four contra una AI dentro de Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: cuando otro agente de programación hace un commit en tu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositorios compartidos por varios agentes de IA…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Installe et configure mes mods Claude Code en une commande.
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code mod: flashes the terminal tab while Claude waits on you.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Mercado de mods de Code de Claude.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Mods divertidos y gratuitos para Claude Code que nunca gastan tokens.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barrera de protección para SQL en Claude Code: pregunta antes de que Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un mod para Claude Code, Windows y CJK en primer plano: vistas previas de…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - Claude Code mods made by the OrbitMap team.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Los mejores Mods de Claude Code, ordenados por lo que hacen por ti.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dos Mods de Claude para Claude Code: guardaespaldas.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel lateral de estadísticas de sesión en vivo para la pestaña Code de la…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Various mods and skills for my Claude Desktop setup.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods para Claude Code: safety-guard bloquea comandos destructivos y el acceso a…
- [ptsnac/claude-session-handoff](https://github.com/ptsnac/claude-session-handoff) - Claude Code mod: session timer and one-click handoff to a fresh context window.
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod de Claude Code: cotización bursátil en tiempo real, panel /quote, alertas…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Mod de Claude Code: una banda sobre el prompt que muestra el contexto utilizado…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Mod de Claude Code: un panel lateral que fija cada diagrama que Claude dibuja y…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Mod de Claude Code: una pasada de ensoñación que fusiona, reescribe y poda la…
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Mod de Claude Code: descarta los prompts vagos antes de que Claude los vea y…
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod: Claude uses your secrets without seeing them.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - A Claude Code mod that keeps secrets out of the session transcript: every key…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod de Claude Code: host SSH, RAM y límites de uso de 5 h/7 d en una fila sobre…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod de Claude Code: flexiones para hacer mientras Claude trabaja. Sin tokens.
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - paceline as a Claude Code mod: paces your usage limits in a line above the…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods para claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod de Claude Code: convierte el plan que apruebas en modo plan en una lista de…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una lista seleccionada manualmente de mods de código de Claude.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sin coste: los agentes auxiliares se ejecutan en Haiku, y los archivos…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una banda sonora lo-fi que sigue la sesión: calma, concentración y fluidez…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprende mientras Claude programa: después de un turno que haya cambiado el…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una cinta de cada edición que hace Claude: reproduce cada cambio mientras se…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: un mod no oficial de fans de Avengers para Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod de Claude Code para contexto, crecimiento, cuota, caché, coste nativo y…
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods.
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Claude Code mods, installable as a plugin marketplace: deviation-kernel guards…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - El DOOM original en un panel de Code de Claude sin necesidad de instalar nada…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Mody Claude Code (function hooks): panel agentów, pasek budżetu, flota sesji.
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Keep Claude.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensajes de commit con un clic para Claude Code con una Malenia bailarina en…
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de Claude Code que muestra el uso de tu plan de Claude…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Pequeños mods que cambian el aspecto y el sonido de Claude Code.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod de Claude Code que muestra la sesión actual en un panel: cada aviso, el…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins de Claude Code de mods: plugins function-hooks que…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Escucha las respuestas de Claude Code mientras se resalta la frase que se está…
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code mod: your context window as Scrooge McDuck.
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod de Claude Code: cuota de 5h/7d, ventana de contexto, tiempo restante de la…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod de Claude Code: banda de progreso animada y resumen de finalización para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tres pequeños mods de Claude Code: descubre cuándo terminarán tus subagentes…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Reduce capturas de pantalla grandes antes de que Claude las lea, para que las…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di «I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Muestra los siguientes prompts sugeridos encima del cuadro de prompt.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Hazle a Claude una pregunta aparte en un panel junto a tu trabajo.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code pings you in Telegram when a task is done or it waits for…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Mis mods de Claude Code.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - A Claude Code mod: a highlighter pen for replies, a side panel for query…
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - A Claude Code mod: your Godville hero and diary in a sidebar.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods para Claude Code: barra de límites de uso (5 h/semanal) y panel de…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin de Claude Code: tus límites de uso de Claude Pro/Max con una previsión…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para Claude Code. agent-crew: observa trabajar a tus subagentes como un…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Matemáticas en LaTeX en línea y visibles, además de figuras TikZ opcionales, en…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Un panel de tareas en directo para Claude Code: planifica antes de construir…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una colección cuidadosamente seleccionada de los mejores recursos para los…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin de Claude Code que muestra lo que está ocurriendo: uso del contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Línea de estado atractiva y altamente personalizable para Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas las partes del indicador de sistema de Claude Code, las descripciones de…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Más de 45 consejos para sacar el máximo partido a Claude Code, desde los…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — genera carruseles de Xiaohongshu y pares de…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline elegante al estilo de vim para Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revisa el diff de tu agente de programación en un panel de terminal y envía…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Cliente para navegador y teléfono de herdr: chat y terminal en directo para…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de línea de estado completo para Claude Code con uso de contexto…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crea mods para Claude Code: intercepta cualquier solicitud, modifica cualquier…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Un panel de línea de estado completo para Claude Code — información de sesión…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: registra la huella de carbono de tus sesiones de Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Una línea de estado estética para Claude Code, creada por awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills y mods públicos de Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos slash y guías para Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legales y gratuitos, además de agentes de programación…
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - Plugin Tavern de DeepSeek Harness: interpretación de personajes mediante…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Calculadora de costes rápida y sin dependencias, y línea de estado…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Línea de estado de terminal para sesiones de Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Resultados, calendarios y clasificaciones de fútbol en vivo para la…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plano de control local para Claude Code en Windows y macOS: cambia los gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Skill de Agent que convierte tu agente de programación en un experto en…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horarios de oración, fecha Hijri, adhkar, ayah diaria, ayuno sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuración personal de Claude Code versionada dentro de ~/.claude — agentes…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Línea de estado truecolor de dos líneas para Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Tarjeta flotante de marea de horas punta y valle para DeepSeek Harness: i18n…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Colección de plugins para Claude Code, pi y DeepSeek Harness: HUD de barra de…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de herramientas de código Portable Claude para .NET DDD/Clean Architecture…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuración global portátil de Claude Code: skills personalizadas, hooks de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins de Claude Code que uso a diario: skills y mods, depurados para que…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods no oficiales para la pestaña Code de Claude Desktop — usage-pet: una banda…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Puente DSH &lt;-&gt; Feishu (Lark), desarrollado internamente (no es un fork)…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins y habilidades de Claude Code para facilitar mods del…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gobernanza de tokens para Claude Code: el modelo principal dirige y la…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Línea de estado en directo de la fase del flujo de trabajo para Claude Code…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositorio de mods de Awesome Media para Claude Code.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Configuración sencilla y útil de la línea de estado para Claude Code.
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Mercado de plugins para Claude Code: mods, skills, agentes, hooks, estilos de…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Muestra la línea de estado de Claude Code con límites de frecuencia, directorio…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Línea de estado configurable de Claude Code para Linux, WSL, Windows y macOS…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Línea de estado rápida de Rust Code para Claude Code — centrada en la carga…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Panel de uso en tiempo real para Claude Code — desglose del contexto, aciertos…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Una línea de estado y una línea de tokens para Claude Code: contexto, uso de 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Muestra detalles clave del estado de Claude Code, incluidos el modelo, el…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Línea de estado de Claude Code en varias filas: gasto, % de contexto, git y…
- [QingqiShi/claude](https://github.com/QingqiShi/claude) - Personal ~/.claude for Claude Code: settings, global CLAUDE.md, hooks, status…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Línea de estado con información útil para claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipos de agentes nativos. Bajo control.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Complementos de Claude Code: indicador de estado de pestañas con punto de color…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Fábricas de software definibles para Claude Code en herdr: grafos de estaciones…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Línea de estado de uso de Claude Code para macOS y Linux, empaquetada como…
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code desktop mod: prompt-cache TTL countdown, hit rate and misses.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Línea de estado personalizada para Claude Code — barra de contexto con…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Una línea de estado limpia e informativa para Claude Code: muestra el proyecto…
- [aubinhaba/claude-code-payment-skills](https://github.com/aubinhaba/claude-code-payment-skills) - Claude Code plugin: code-review skills for payments, consistency, boundaries…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins de Claude Code con baloo: skills, un agente que verifica…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Línea de estado de Claude Code de nivel profesional: duración de sesión, coste…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Línea de estado de Claude Code consciente de la suscripción.
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - A Claude Code plugin: a pane of the live Claude Code and Codex sessions on your…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Una línea de estado de terminal completa para Claude Code — Bun + TypeScript…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Herramientas, habilidades y agentes para Claude Code — empezando por una línea…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Línea de estado personalizada de Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Gasto real de DeepSeek de API para Claude Code: vuelve a calcular el precio de…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Previsualiza imágenes dentro de Claude Code: pasa el cursor sobre una etiqueta…
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - My Claude Code setup: mods, skills and plugins.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincroniza las tareas pendientes de Claude con Fizzy.do para que el equipo…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Controla el estado de Code de Claude con un panel compacto que muestra el…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalador del entorno de Claude Code: skills, barra de estado, hooks, permisos…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Línea de estado estilo HUD para Claude Code — estado de la red, TPS, contexto…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skills and mods for Claude Code and Cowork — project-tracker, reference-doc…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuración portátil de Code de Claude (barra de estado + instalador).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Un pequeño panel para Code de Claude: porcentaje de contexto, cuenta regresiva…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Barra de estado personalizada del terminal para Code de Claude: modelo…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuración portátil de Claude Code: CLAUDE.md, ajustes, línea de estado…
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Seguimiento de costes en tiempo real y línea de estado de monitorización de…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Habilidad de Code de Claude (VS Code, Windows): vistas previas de imágenes y…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Una línea de estado de Claude Code: carpeta, rama de git, modelo, uso de la…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de degradación del contexto 2026 - Monitor proactivo de memoria de IA…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes y líneas de estado de Claude Code: colecciones y herramientas…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Constructor visual para las líneas de estado de Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Línea de estado de Claude Code que muestra el uso de tokens en tiempo real y el…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: paneles, bandas y compañeros basados en enlaces de…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Paquete de interfaz al estilo de Claude Code para el agente de programación Pi…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pasa tareas entre tus sesiones de Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Esto en un servidor MCP para controlar MODS, la herramienta modular…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Habilidad de Codex y Claude Code para traducir mods de CK3 con un LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código abierto y otras extensiones para Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code状态行：CCometixLine美化效果+Claude HUD功能.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encuentra lo que pides a Claude Code una y otra vez y conviértelo en…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - mod de prompt-bar para Claude Code: límites de uso, temporizador de caché +…

</details>

<a id="dsh-cordis"></a>

## Ecosistemas de complementos de DSH y Cordis

DeepSeek Harness y Cordis llegan al mismo punto desde direcciones diferentes: para ellos, el complemento es el mecanismo de mods, así que allí un complemento equivale a un mod aquí.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74358 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **74358**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐100891 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **100891** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100557 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **100557** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82028 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **82028**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35768 · Go · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **35768**  |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25499 · Python · 🔎 inferred · 19 天</summary>

##### 📝 Resumen

Distilly — Destila cómo piensan en Skills reutilizables para cualquier Agent o Bot. Anteriormente Colleague Skill（原同事 Skill）.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **25499**  |
| Último envío      | 2026-09-22 |
| Primera inclusión | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4493 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **4493**   |
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
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

El primer terminal virtual del mundo para agentes de IA

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3682**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3093 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DeepSeek Harness Tauri, versión de escritorio | Instalador de solo 8 MB, configuración de entorno cero, plugins preestablecidos, Windows / macOS / Linux.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **3093**   |
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
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1995 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

El mejor plugin de DeepSeek Harness para comprender y gestionar el contexto, con panel / navegador / barra lateral de contexto y comando de contexto, para consultar estadísticas, composición, desglose y detalles de evolución del contexto, comprender de qué está compuesto y cómo evoluciona. Plugin de visualización del contexto de DeepSeek Harness todo en uno, con panel Context, navegador y barra lateral, además del comando Context, para analizar la composición, evolución, compresión, poda y otros eventos y acciones del contexto.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1995**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1841 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Conecta bots de mensajería instantánea a DeepSeek Harness mediante un código QR o credenciales de bot (admite 飞书, 微信, 钉钉, 企业微信, QQ, Slack, Telegram, Discord y WhatsApp). Conecta bots de mensajería instantánea a DeepSeek Harness mediante un código QR o credenciales (9 canales).

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1841**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1591 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Protección previa a la ejecución para agentes de programación con IA. Bloquea comandos destructivos de Git y del sistema de archivos, además de intentos habituales de acceder a archivos sensibles, antes de que se ejecute una llamada a una herramienta. Compatible con Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode y Pi.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1591**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1578 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Entorno de trabajo Agent de código abierto para varios dispositivos

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1578**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1410**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1173 · Go · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1173**   |
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
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **705**    |
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
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Aplicación de escritorio de DeepSeek Harness: un espacio de trabajo local de IA para sesiones de DSH, proyectos, archivos, investigación web, plugins y artefactos de Office.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **592**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **526**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Proveedor gratuito de búsqueda web para DeepSeek Harness: backend de DuckDuckGo, no se necesita ninguna clave de API

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **369**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de DeepSeek Harness para cambiar la apariencia / fondos de pantalla / paquetes de temas (dsh-plugin) — 8 temas Mirage, color de énfasis por usuario, Fondos de pantalla 2.0, importación y exportación de paquetes de temas / enlaces para compartir, favoritos y selección aleatoria, implementado íntegramente con el sistema de tokens nativo.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **225**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **204**    |
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
<summary>🧵 <b><a href="https://github.com/cocofhu/anime-find">cocofhu/anime-find</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de búsqueda de series para DeepSeek Harness: busca series desde la conversación en múltiples fuentes, muestra en tarjetas las valoraciones y detalles de Bangumi, y permite copiar enlaces magnet.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **176**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `anime` · `anime-search` · `bangumi` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `magnet`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cocofhu--anime-find/4e8000425bf8bf5f.jpg" width="100%" alt="cocofhu/anime-find screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de copia de seguridad y restauración de DeepSeek Harness (DSH): exporta, importa, migra y sincroniza toda tu configuración de DSH, plugins, servidores MCP, habilidades y espacio de trabajo. Migración con un clic a otra máquina.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **176**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **172**    |
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
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐160 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Usa tu suscripción ChatGPT Plus / Pro (Codex) en DeepSeek Harness (DSH): modelos GPT-6 y Codex, imágenes, búsqueda web y cuota mediante el inicio de sesión de ChatGPT — sin clave OpenAI API. Beta: controla DSH desde la aplicación móvil de ChatGPT. Usa tu suscripción de ChatGPT en DSH y controla DSH de forma remota con la aplicación móvil de ChatGPT.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **160**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐143 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Evidencia del tiempo de ejecución que ayuda a los agentes a rastrear, crear perfiles y eliminar puntos críticos en código de aplicaciones y nativo, kernels de GPU y pilas de inferencia.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **143**    |
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐135 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Incluye de serie 27 habilidades de ingeniería y productividad de mattpocock/skills v1.3.1, sin necesidad de instalarlas manualmente. Creado con 40 mil millones de tokens, este plugin ofrece una eficiencia de desarrollo 10 veces superior a las habilidades originales y también ayuda a los principiantes a familiarizarse más rápidamente con este conjunto de habilidades. Compatibilidad total con incidencias de GitHub; Markdown está en versión preliminar; GitLab aún no es compatible. Gracias por usarlo y apoyarlo 💗

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **135**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

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
| Primera inclusión | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **133**    |
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
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Plugin de DSH · Optimizador por inyección 0.8 (rama principal): hablas con normalidad y, después de que envías el mensaje y antes de que lo reciba la IA de trabajo, aclara qué se necesita realmente en esta ronda y entrega esa comprensión a la IA de trabajo (inyección de contexto) — no reescribe las palabras originales y cada punto incluye su fundamento textual. Incluye una interfaz de control (nivel/modo, permisos, modelo, contexto y herramientas de solo lectura), capas flotantes de interceptación (capa de pensamiento + capa de resultados) y uso real de tokens. Puede mejorar notablemente la estabilidad del rendimiento de la mayoría de los modelos, especialmente DeepSeek-V4.1-Flash, con mejoras apreciables

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
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐100 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DSH plugin - framework upgrade safety & plugin gating: contract pre-check, rollback point, auto-rollback on failure, evidence-based auto-disable; plus a multi-source plugin market. Unofficial. | DSH 插件：框架升级安全 + 插件门控——升级前契约预检、回滚点、失败自动回滚、有确证证据才自动禁用；另带多源插件市场。非官方社区项目。

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **100**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

StudyHub: un plugin de DeepSeek Harness (DSH) que convierte tus propios materiales en preguntas y repasos espaciados · Plugin de aprendizaje de DSH que convierte tus materiales en preguntas y repasos espaciados

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **90**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-12 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 72</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Una lista seleccionada de los mejores plugins de IA para asistentes de IA…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - Encuentra en 30 segundos el plugin de DeepSeek Harness que realmente se adapta…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin de DSH — modelos OpenCode Zen gratuitos para DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins de DSH / DSH Plugin Marketplace: explora, instala y…
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins para software que itera sobre sí mismo: la base donde los…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [ZASENJC/dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) - 自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Agent de escritorio creado sobre la base central de Deepseek-Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - El directorio activo de plugins de DeepSeek Harness — actualizado cada hora…
- [1475505/miliastra-beyond-simulator](https://github.com/1475505/miliastra-beyond-simulator) - 千星沙箱模拟器：Lua 驱动的 2D 奇域外置沙箱 ，支持 DeepSeek Harness、Web 和 MCP.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Recuperación de contexto del espacio de trabajo y seguimiento del ciclo de…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent es un FDE Harness de código abierto para agentes de programación con…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directorio seleccionado de plugins de DeepSeek Harness (DSH): más de 280…
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - Plataforma visual de orquestación de agentes｜Basada en DeepSeek Harness…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Plugin maestro de recursos para juegos de dsh.
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Plugin de DeepSeek Harness: empareja modelos con la ventana de contexto con un…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistema de agentes de chat grupal multiplataforma basado en DeepSeek…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Colección de plugins GUI web de DSH (DeepSeek Harness) — notificaciones de…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, herramientas, skills y recursos de aprendizaje de DeepSeek Harness…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Alternativa de código abierto a GrokBot basada en DeepSeek Harness.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin gestor de servidor MCP para DeepSeek Harness: página Settings → MCP…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de negociación comercial A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Panel de herramientas para DeepSeek Harness Web: gestor de MCP.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin de DeepSeek Harness · Botón «Optimizar» con un clic en la barra de envío…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Mercado de plugins verificados y registro autónomo para DeepSeek Harness.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un PowerPoint real, no HTML. Dile a tu IA qué debe incluir y pptwise creará una…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Grafo de conocimiento de código y harness de contexto para agentes de…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Registro de datos abiertos filtrado contra spam de plugins, paquetes y…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 嵌入式C/C++ AI工程插件——固件技能（FreeRTOS、Keil、HardFault、状态机）+ 1% Rule / Plan Verification…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Convierte los modelos en los que has iniciado sesión en la aplicación de…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - plugin dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pruebas de compatibilidad siempre activas para plugins de DeepSeek Harness…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Compresión agresiva del contexto para agentes locales.
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Compactación protegida del contexto para DeepSeek Harness (dsh): LLM propone y…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 IDE Agent-Human ⌨️ Versiones web y de escritorio, con Plugins, Skills…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host de DeepSeek Harness que conserva los documentos del proyecto y la…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - Directorio seleccionado y basado en evidencias de plugins de DeepSeek Harness…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayos X para plugins de DeepSeek Harness: capacidades declaradas frente a…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - Mercado de plugins de DSH — instala plugins de la comunidad con un clic desde…
- [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) - Plugin Mixture of Agents (MoA) para DeepSeek Harness con el comando de barra…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin de DSH: ventana de herramientas Git de nivel IDE como pestaña nativa de…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - Clasificación y directorio de plugins de DeepSeek Harness (DSH)｜Directorio /…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espacio de trabajo con varias carpetas: permite que el agente de DSH.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Registro de plugins de DeepSeek Harness con búsqueda, listados seleccionados y…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Estándar de verificación sin dependencias para plugins de DeepSeek Harness…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - Plugin de DeepSeek Harness (DSH): sincronización de modelos de OpenCode Go con…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Mercado de plugins de DeepSeek Harness: explora, busca e instala plugins del…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode en DeepSeek Harness — plugin de DSH que mantiene funcionando OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — mercado de plugins de terceros y gestor de ciclo de vida protegido…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx es un espacio de trabajo de escritorio ampliable y centrado en las…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Un agente de programación con todo incluido para DeepSeek Harness — flujos de…
- [GooDAnDReaDY/dsh-live-canvas](https://github.com/GooDAnDReaDY/dsh-live-canvas) - Interactive Visual Frontend Studio, Retool-Style CRUD Engine, Time-Travel…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - ¡Dale a DeepSeek Harness Agent manos y pies nativos para operar GitHub!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite comunitaria de instalación, despliegue y operaciones locales…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Elimina permanentemente las sesiones archivadas de DeepSeek Harness junto con…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web de DeepSeek Harness (DSH): pestaña lateral market-dashboard para…
- [tiphareth0/dsh-hardssh](https://github.com/tiphareth0/dsh-hardssh) - Ejecuta tu trabajo con plugins de DSH existentes en servidores remotos, en…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Permite volver a intentar un intento vacío de modelo sin atribución, para la…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins que se limpian solos: un port de Swift 6 del framework de plugins…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset de agente DeepSeek Harness: Codex y Claude Code como subagentes de…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins de Rust con un kernel de ciclo de vida verificado por…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Panel de Antigravity integrado: tok/s, tasa de aciertos de caché al estilo DSH…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - Plugin proveedor Paseo de DeepSeek Harness (proveedor directo).
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Tienda de plugins de dsh: descubrimiento automático y sincronización programada…

</details>

<a id="writing"></a>

## Escritura, debates y vídeos

Artículos, debates y vídeos sobre la capacidad de modding.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 377      | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 90       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 38       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 25       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 17       | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Rust       | 6        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| Go         | 5        | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| PowerShell | 2        | `GoSlowPoke168/claude-statusline`, `YangShen-SWE/dsh-plugin-simple-pet`                                       |
| C          | 1        | `reporails/arcade`                                                                                            |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1        | `crafts69guy/claude-statusline.nvim`                                                                          |
| Swift      | 1        | `eovidiu/cordis-ios`                                                                                          |

<sub>Solo se contabilizan las entradas que declaran un idioma. Las entradas de documentación y debate se excluyen de esta tabla.</sub>

## Contribuir

Las correcciones son bienvenidas y son la forma más rápida de mejorar esta lista. Abre un issue o una pull request si una entrada está mal clasificada, tiene una categoría incorrecta o si un proyecto se ha excluido por error debido a una coincidencia de nombres; esta última categoría es donde más probablemente fallen los filtros automatizados.

---

<sub>Proyecto independiente de la comunidad. No está afiliado a Anthropic, ni cuenta con su respaldo o revisión. Claude Code, Claude y Anthropic son marcas comerciales de Anthropic. El comportamiento del producto puede cambiar sin previo aviso; verifica cualquier aspecto esencial en la documentación oficial. Los recursos siguen siendo propiedad de sus proyectos de origen y se reproducen únicamente cuando una licencia lo permite.</sub>

<sub>Última actualización · 2026-10-12T06:04:10+08:00</sub>
