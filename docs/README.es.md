<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods increíbles de Claude">
</p>

<h1 align="center">Mods increíbles de Claude</h1>

<p align="center"><b>El índice de mods y plugins de Claude Code, clasificados según la evidencia, y del comportamiento más profundo que modifican.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-602-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <b>Español</b> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice activo** · Última sincronización: `2026-10-12T14:51:24+08:00` (UTC+8)
> · Entradas: **602** · Añadidas en la última actualización: **0** · Lenguajes de implementación: **14**

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
<sub>⭐2539 · Python · 👁️ observed</sub>
<sub>Encuentra los tokens fantasma. Arréglalos. Sobrevive a la compactación. Evita el deterioro de la calidad del contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74376 · TypeScript · 👁️ observed</sub>
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
- [Mods: creados con la capacidad de mods](#mods-creados-con-la-capacidad-de-mods) — **470**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150273 · TypeScript · ✅ official · 0 天</summary>

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
| Estrellas         | **150273** |
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8250 · Python · ✅ official · 2 天</summary>

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
| Estrellas         | **8250**   |
| Último envío      | 2026-10-09 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242 天</summary>

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
| Estrellas         | **6347**   |
| Último envío      | 2026-02-11 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 2 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Modificaciones oficiales de Claude Code de See Stack: HUD de la ventana de contexto en tiempo real, panel de narración de voz y herramientas de terminal. Instala mediante: npx seestack

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic`       |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **0**      |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>grabación animada</sub></td>
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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2539 · Python · 👁️ observed · 0 天</summary>

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
| Estrellas         | **2539**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐504 · JavaScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **504**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐196 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **196**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐147 · TypeScript · 👁️ observed · 7 天</summary>

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
| Estrellas         | **147**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐112 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **112**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐103 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Skins para Claude Code: filas de herramientas con iconos, tarjetas de diferencias, tablas y gráficos Mermaid, una banda de uso y quince temas. /skin los cambia en directo.

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **103**    |
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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐80 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **80**     |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 3 天</summary>

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
| Estrellas         | **79**     |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SaM-runtime/claude-console">SaM-runtime/claude-console</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Multi-project console for Claude Code, built as a Claude Code mod: live project board, trigger actions, quota batteries; executes via Claude Code or Codex.

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
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sam-runtime--claude-console/7502a46951d79adb.gif" width="100%" alt="SaM-runtime/claude-console screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sam-runtime--claude-console/7502a46951d79adb.gif" width="100%" alt="SaM-runtime/claude-console animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐68 · TypeScript · 👁️ observed · 9 天</summary>

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
| Estrellas         | **68**     |
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
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Resumen

Mods de Claude Code: barras de progreso del plan en tiempo real sobre el prompt

<sub>🔧 Encontrado en el código: `README.md`</sub>

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
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

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

Usa Codex, GLM y otros agentes de programación como subagentes de Claude Code.

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
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6 天</summary>

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
| Estrellas         | **14**     |
| Último envío      | 2026-10-05 |
| Primera inclusión | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 4 天</summary>

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
| Estrellas         | **12**     |
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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **12**     |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

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
| Estrellas         | **12**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

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
| Último envío      | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/natsukium/claude-code-figures-plugin">natsukium/claude-code-figures-plugin</a></b> · ⭐7 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Resumen

Dibuja diagramas, fórmulas matemáticas LaTeX e imágenes de resultados de herramientas en línea en terminales kitty-graphics — un complemento de Claude Code

<sub>🔧 Encontrado en el código: `hooks/register.tsx`</sub>

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
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `d2` · `diagrams` · `graphviz` · `kitty-graphics` · `latex`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/natsukium--claude-code-figures-plugin/8b6e1b6a10ace52e.png" width="100%" alt="natsukium/claude-code-figures-plugin screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary><b>Más en esta categoría</b> <sub>· 436</sub></summary>

- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Skills, agentes, comandos, reglas, hooks y estilos de salida expertos para…
- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Colección de más de 100 mods que puedes usar con Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods de Claude y las herramientas para crearlos: primero una skill de creación…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - El harness de Claude Code que uso a diario, publicado con este nombre desde el…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Dale un nuevo techo a Claude Code con Claude Mods: cambia los avisos del…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cuatro mods de Claude Code: Cache Keeper, Recording Mode, Goal Meter y…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods de Claude Code de Learning Hacker: convierte el funcionamiento del agente…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods de Claude Code que corrigen y traducen tus prompts antes de que Claude los…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods de código y habilidades de Claude Code de Nekyia Labs, creados y usados a…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conocimiento de Obsidian con fuentes citadas sobre los mods de código…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 为Claude Code的终端记录打造桌面应用外观的mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un panel lateral para Claude Code: los subagentes que ejecuta una sesión, qué…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel de barra lateral de Claude Desktop (pestaña Code): enumera todas las…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Habilidad que enseña a los agentes de Claude Code a crear Mods de Claude…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso encima del cuadro de entrada de Claude Desktop (pestaña Code)…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins y habilidades comunitarios de Claude, instalables desde un único…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods de Claude (plugins de enlaces de funciones) para Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galería de mods de Baselane: mods de Claude Code, revisados y fijados.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una cola de decisiones CLI/TUI para personas que trabajan con agentes…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Modificación del panel IDE de Claude Code: tablero de agentes, árbol de…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods de Claude Code: panel de uso usage-hud 像素螃蟹 y enlaces HTML en los que se…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Tarjeta de estado flotante para Claude Code — modelo, contexto, límites de…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods para Claude Code: plugins de enlaces de funciones que añaden paneles…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nombres y secretos al compartir la…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensiones de Claude Code. Desbloquea todo el potencial de Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) de Claude Code que añade un panel lateral con pestañas Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Paneles, protecciones y mods para mejorar la experiencia de Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dos mods de Claude Code sobre el cuadro de prompts: medidor de la ventana de…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Haz que el plan Claude Pro dure más: mods de Claude Code para un HUD de uso…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lee los archivos markdown que nombra Claude Code, renderizados junto a la…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imágenes pegadas sobre el prompt, en…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Compañero de voz para Claude Code. Habla sobre tus ideas con un lobo 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, un velocímetro de escritura en directo con…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuegos artificiales para Claude Code: cada pulsación, llamada a herramienta…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Una prueba de mecanografía para pasar el tiempo mientras Claude trabaja.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubre mods, plugins y extensiones de Claude Code con demostraciones…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas de mermaid dibujados dentro de la transcripción.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods y skins para Claude Code: una barra de progreso en directo para las tareas…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequeños mods de Claude Code (plugins de function-hook): session-switcher y más.
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - Descubre cuánto cuesta tu próximo mensaje de Claude Code: una banda activa…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods de Claude Code: menú de herramientas de Claude, modo Zen, temas de…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods de Claude Code: mod-scout (encuentra los mods que más usarías)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dos mods de Claude Code para ejecutar muchas sesiones a la vez: una tarjeta de…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: descubre, inspecciona, activa y actualiza mods de Claude Code.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods de Claude Code: barra de contexto, panel de agentes y desenfoque PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Los mejores mods de Claude Code: seleccionados, validados y fijados.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin de Claude Code: enrutamiento automático de modelos Claude.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods para Claude Code: paneles, comandos y hooks creados con el plugin de…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Recorta las enormes salidas de herramientas antes de que llenen el contexto de…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Seis mods para Claude Code: mascota Clawd animada, barras de límite de uso y…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Un marketplace de mods para Claude Code: depurador paso a paso para el ciclo…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: límites de plan y contexto sobre el prompt, un coach…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - El mejor paquete de mods todo en uno para Claude Code: límites de uso y HUD del…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Reproduce YouTube Shorts en tu Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de herramientas Claude de Naren: skills, mods y servidores MCP para Claude…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod de Claude Code que muestra las diferencias de Edit y Write en dos columnas…
- [nsodhi-cmu/claude-code-ripple](https://github.com/nsodhi-cmu/claude-code-ripple) - Claude Code mod that creates call graphs of your code changes.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods para Claude Code: Clawd, una diminuta mascota pixelada que representa lo…
- [reporails/arcade](https://github.com/reporails/arcade) - Juegos de escritorio clásicos como mods de Claude Code, jugables en un panel…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Una lista seleccionada de mods de código de Claude Code, instalables como un…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de Claude Code bajo demanda — una habilidad que lee tu conversación y crea…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Un plugin de Claude Code muy particular, diseñado por un Rustacean obsesionado…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantienen honesto a un agente: enlaces de funciones que…
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Los mods de Claude Code que uso.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Panel del notch de macOS para Claude Code: límites de uso, sesiones abiertas…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod por Claude Code: barra de caché del prompt, próximos pasos, botones rápidos…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Una batalla espacial sobre el prompt de Claude Code mientras trabaja.
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Coste, tokens y límites del plan de tus agentes de programación.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code que muestra tus límites de uso y gasto en la banda sobre…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods de Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods de Claude Code: barras de progreso para planes, un registro de lo que…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Mira lo que Claude Code ejecuta en segundo plano: subagentes, trabajos de…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods by MacLeod Labs: streams untangles a session.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo del primer día sobre mods de Claude Code en Windows: una barra…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: un depurador para las llamadas a herramientas de Claude Code.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Tarjetas pequeñas que se sitúan bajo el prompt de Claude Code o acopladas junto…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod de Claude Code: medidores en vivo de coste, contexto y cuota del plan…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Un mod de Claude Code que retiene la distribución de subagentes, las…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills para Claude en cinco paquetes.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods para claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod de Claude Code que activa o desactiva tus habilidades, agentes, reglas y…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins (mods) de Claude Code: cambia entre varias cuentas de Claude, supervisa…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de código de Claude probados e instalables con un comando: protecciones…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods para Claude Code: plugins creados sobre hooks de funciones.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace de mis propios mods de Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un montón de mods de claude code creados por mí.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Two Claude Code mods: cache-keeper and ctx-mod.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods de Claude Code. touch-map: muestra qué archivos enumeró, leyó, editó o…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprende un idioma extranjero mientras trabajas con Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Supervisa una sesión larga de Claude Code para que no tengas que hacerlo…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Objetivo, tareas y agentes por encima de tu prompt de Claude Code, sin…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio por Internet dentro de Claude Code: barra lateral cliamp…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude está cocinando. Chatea con tu escuadrón.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods de Code de Claude para Engineers reales.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Resumen de la sesión de terminal de Claude Code, en la pestaña Code de la…
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack 的 Claude Code mods 合集.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - All-in-one Claude Code mod: a live HUD, safety guards.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Ve qué archivos tiene cada agente de Claude Code en su contexto, y cuánto de…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Convierte cada sesión de Claude Code en una pequeña aventura: música generativa…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequeños mods de Claude Code para el terminal y la aplicación de escritorio.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code mods (plugin marketplace): live sidebar with context, cost and…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidad + mod de Claude CLI que añade palabras en español a las respuestas…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Tus eventos de Alarum sobre el prompt de Claude Code: qué acaba de llegar y una…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Tu lista de pendientes de Floatee sobre el prompt de Claude Code: ejecuta, guía…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra lateral al estilo de Evangelion para Claude Code: contexto, cuota…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code que lo rediseña como The Machine de Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Mod de Claude Code: un escuadrón de arte pixelado sugiere el modelo adecuado…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: modificación de Claude Code para flujos de trabajo DAG…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código abierto para Claude Code: paneles, líneas de estado…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Un mod de Claude Code: un panel para cada subagente, los archivos que toca y el…
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - Various mods I have made for claude that I find helpful.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod de Claude Code: estado de sesión, progreso en vivo de Spec Kit y…
- [KevinYu1580/jev-cc-model-router](https://github.com/KevinYu1580/jev-cc-model-router) - Claude Code mod: picks the model once per session and the effort every turn…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La ventana de contexto como una fila sobre el prompt, dibujada como Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tareas en tiempo real para Claude Code Desktop: una franja sobre el…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code plugin (mod) that makes the Claude Code terminal UI look like the…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuito y de código abierto para Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Guarda prompts para más tarde y devuélvelos al cuadro de entrada de Claude…
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Mod de Claude Code que muestra imágenes integradas en Ghostty y kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un Mod de Claude que muestra las solicitudes de extracción de GitHub de la…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Modificaciones de Claude Code: seleccionadas y probadas, y cada modificación…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mods de Claude Code: cambio automático y barra de progreso.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods marketplace.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Habilidades de Claude Code: un verificador de hechos de documentación, un…
- [olilllioli287/claude-code-image-shelf](https://github.com/olilllioli287/claude-code-image-shelf) - Claude Code mod: pasted images as a thumbnail shelf above the prompt, even in…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod de Claude Code que reescribe las indicaciones imprecisas para convertirlas…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Modificaciones de Claude Code de Pedro La Rosa, en un único mercado de…
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Modificación de Claude Code: tus límites de uso de 5 horas y 7 días como barras…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compañero de Claude Code: un acompañante ASCII sobre el prompt que…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin de Claude Code para controlar la visibilidad de herramientas por agente…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Mod de Claude Code: enrutamiento de modelos/esfuerzo guiado por Jev, compresión…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - A collection of Claude Code mods.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin y mod de Claude Code: un SDLC nativo de IA.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Colección Awesome de mods de Claude Code | Colección de mods de 클로드 코드.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: un mod no oficial de fans de Avengers para Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Habla: un mod de Claude Code que lee en voz alta, cuando se solicita, las…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code: pequeños plugins para paneles en tiempo real, enrutamiento…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod de Claude Code: cuota de 5h/7d, ventana de contexto, tiempo restante de la…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod y plugin de Claude Code: monitor de uso, rastreador de tokens y línea de…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod de Claude Code que informa en directo de qué archivos cambió Claude y por…
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Catch the drift of your Claude Code session.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Mercado de mods de Claude Code: agent-board, auto-model, session-collab + mods…
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Mod de Claude Code: dirige cada subagente al modelo Claude más barato, evaluado…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods: session stat cards above the prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gato braille animado sobre el prompt de Claude Code.
- [aliahmadcse/claude-usage-status](https://github.com/aliahmadcse/claude-usage-status) - Claude Code mod: model, effort, context, cost, and 5-hour/weekly usage limits…
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code: dirige el trabajo barato a GLM/Kimi mediante un Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gato pixelado sobre el prompt de Claude Code que ejecuta una llamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code que elige un buen momento para compactar y mantener…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods para Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods de propósito general para Claude Code: bandas, paneles, toasts y hooks.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Tus límites de uso de Claude como una tarjeta animada de salud de aldeano, con…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Entrenamientos cortos mientras Claude trabaja: un objetivo diario, rachas…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un panel de uso para Claude Code: gasto por modelo.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para Claude Code: Apple Music y Spotify sobre el aviso, con…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Claude Code mods for orchestrator and worker sessions.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: reloj de caché, radio de impacto, sugerencias, lista de…
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - Un mod de Claude Code: el registro del trabajo orquestado, con ejecuciones…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mods de Claude Code: Suggestion Spotlight muestra a qué se refiere el siguiente…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un búho para tu Claude Code.
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Mods do Claude Code criados por mim (painéis, comandos e hooks).
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - El motor original de Doom con Freedoom, jugable dentro de Claude Code.
- [cigarette1991/clawd-pet](https://github.com/cigarette1991/clawd-pet) - Clawd, a Claude Code mod that lives above the prompt box.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Revisa cada archivo que Claude modifica, como una solicitud de incorporación de…
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀 전용 Claude Code mods (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [danielmertens/Claude-mods](https://github.com/danielmertens/Claude-mods) - Collection of personal Claude mods.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi que vive dentro de Claude Code: eclosiona, se come el código que…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Marcadores y marcas al estilo de vim dentro de las conversaciones de terminal…
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Un mod de Claude Code: una banda sobre el prompt con noticias de Claude y las…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod de Claude Code: después de que un guard bloquee una llamada a una…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod de Claude Code: trabajos en segundo plano en una sola vista, con progreso y…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod de Claude Code: una sola bandeja de entrada para mensajes de compañeros de…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod de Claude Code: explica los bloqueos del sandbox y convierte los bloqueos…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoritos para Claude Code: iconos de un clic para tus comandos y skills.
- [ecombuilder-web/TripleDigit-crab-agents](https://github.com/ecombuilder-web/TripleDigit-crab-agents) - Claude Code mod: right-side Agents pane showing every working and finished…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ¡Ey, lo silencié! Deshazte del diff, corta el riff;
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods: rewrite-prompt (Ctrl+P rewrites your draft before you send it).
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods: auto-model-detector routes each prompt to the right model and…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar en tiempo real de tus ramas y worktrees paralelos sobre el prompt…
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi — a Claude Code mod: a mascot that reads the room above the prompt, with…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Seven Claude Code mods: savvy-progress, skins, filetree, cache-tax…
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Claude Code plugin marketplace with my mods.
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Useful claude code mods.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey.
- [hernandezsanti/claude-code-mods](https://github.com/hernandezsanti/claude-code-mods) - Claude Code mods that enforce ticket-based commits, protect paid CI minutes and…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Mod de Claude Code: tres próximos pasos después de cada respuesta, en cualquier…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de Claude Code: cuánto tardó cada respuesta, cuánto tiempo pensó Claude y…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mods de Claude Code: el modo streamer oculta los paneles privados, las bandas y…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Una cabina sobre tu indicación de Claude Code. El pato lee los medidores.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Redacción reversible para Claude Code: los valores privados se reemplazan por…
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code mod: sidebar file tree that pulses on files Claude just edited.
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Claude Status Bar.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Claude Code mods: context bar and the cyberdeck HUD.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel lateral de uso del contexto: total, categorías, crecimiento por ronda…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista lateral de archivos: qué archivos se han creado, modificado o eliminado…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, un conejo belier neerlandés en blanco y negro con estilo de 8 bits, corre y…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Panel lateral de «Lo que he preguntado»: cada frase que el usuario ha escrito…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Línea de tiempo lateral: en qué se ha empleado el tiempo de esta ronda…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Intercambio de tokens en el panel lateral: cuántos tokens envía la conversación…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - El bocadillo de tofu honesto de claude code: al terminar cada ronda, Claude…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Lista de verificación de planes con validación de evidencias para Claude Code…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 简体中文汉化（自管版）——自己的翻译表 + patch 工具 + 升级检查.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - Two Claude Code mods: session handoffs with replies, and routing simple turns…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive en una banda sobre tu prompt de Claude Code: representa la sesión…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod que lee en voz alta las respuestas y notificaciones de Claude Code mediante…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Un mod de Claude para leer y unirse a las conversaciones entre tus sesiones de…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods de Code de Claude. PixBar: una criatura pixelada sobre tu prompt que se…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod de Claude Code para macOS: una ventana flotante que muestra qué está…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods.
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - Some proof of concepts for claude-code-mods.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Mods de Claude Code, publicados como un mercado.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dos mods de Claude Code: folio, un panel de archivos junto al chat, y tint, un…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: un gráfico en tiempo real de lo que sabe Code de Claude.
- [KunalKumarkkr01/prompt-rewriter](https://github.com/KunalKumarkkr01/prompt-rewriter) - Claude Code mod: /rewrite &lt;prompt&gt; picks role + task personas, adds recent web…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - No dejes que tu atención se desvíe mientras esperas la respuesta de Claude Code.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Mods de Claude Code de Sanmu — un marketplace de plugins.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guía de Mods de Claude Code seleccionada por la comunidad: casos de uso…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Claude Code mod: guards the 1-hour prompt cache of idle sessions — countdown…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de Claude Code que muestra lo que Claude está haciendo en el subtítulo…
- [madjagstudios/podium](https://github.com/madjagstudios/podium) - A Claude Code mod that hands work to Codex, Gemini, Muse and other agent CLIs…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, un compañero pixelado no oficial creado por fans que vive sobre el…
- [Magithar/agent-board](https://github.com/Magithar/agent-board) - A task board several coding agents share: one CLI for any agent, a Claude Code…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - Cuánto se ha llenado el contexto de Claude, cuándo se enfría su caché y cuánto…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod de Claude Code: responde a Claude punto por punto, directamente sobre el…
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Pequeños mods para Claude Code: runner-avatar, un pequeño avatar que corre…
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - Small Claude Code mods from the MateAI channel.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod de Claude Code: un panel en directo de aquello a lo que aspira tu agente de…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod de Claude Code: panel /sessions para explorar y eliminar sesiones junto con…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods de la comunidad para Claude Code: protecciones, paneles y comandos que se…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel lateral para Claude Code: archivos que escribió Claude, divisiones del…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [minhdevtree/claude-lens](https://github.com/minhdevtree/claude-lens) - A Claude Code mod that shows images, SVGs and PDF pages where they appear…
- [mlabo-org/context-git-band](https://github.com/mlabo-org/context-git-band) - Claude Code mod: context window weather with a compact link, subscription quota…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un discreto panel lateral para Claude Code: qué está haciendo esta sesión, su…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Una hora atenuada sobre cada prompt y cada respuesta en la transcripción de…
- [mmedum/spor](https://github.com/mmedum/spor) - Devuelve lo que Claude oculta: los archivos que Claude leyó, los comandos que…
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - Claude Code plugins for sessions and memory: a Memory pane mod and a…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de código de Claude que vuelve a activar las herramientas de tareas para…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod de Claude Code que espera una pausa segura y después entrega tu sesión o la…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de código de Claude: una línea por tarea encima del prompt con la tarea…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Juega Connect Four contra una AI dentro de Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: cuando otro agente de programación hace un commit en tu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositorios compartidos por varios agentes de IA…
- [netgfx/claude-html-mod](https://github.com/netgfx/claude-html-mod) - A Claude code mod for displaying html in a side panel.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Mods divertidos y gratuitos para Claude Code que nunca gastan tokens.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barrera de protección para SQL en Claude Code: pregunta antes de que Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un mod para Claude Code, Windows y CJK en primer plano: vistas previas de…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Los mejores Mods de Claude Code, ordenados por lo que hacen por ti.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dos Mods de Claude para Claude Code: guardaespaldas.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Marcas de tiempo para Claude Code: la hora de cada mensaje, respuesta y llamada…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Seguimiento de cambios para Claude Code: ve exactamente qué cambió Claude en…
- [patrick-lai/claude-craft-shop](https://github.com/patrick-lai/claude-craft-shop) - Craft Shop: a Claude Code mod with a worktree head start, crew dials, a context…
- [paudelnirajan/burrow](https://github.com/paudelnirajan/burrow) - Claude Code mod: dive into side explorations, then surface back to where you…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Mods for Claude Code: plugins of function hooks that work in any repository.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Various mods and skills for my Claude Desktop setup.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Mod de Claude Code: registra el modelo, los tokens, las herramientas y el…
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Mod de Claude Code: cada subagente aparece como una pequeña figura de palitos…
- [poppydad/dino-run](https://github.com/poppydad/dino-run) - Claude Code mod: a dino-run game in a side pane that opens while your…
- [poppydad/done-chime](https://github.com/poppydad/done-chime) - Claude Code mod: plays a chime when a long turn finishes, a low tone when it…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods para Claude Code: safety-guard bloquea comandos destructivos y el acceso a…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Un cangrejo de pixel art animado de Claude para Claude Code: representa lo que…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/decision-tree](https://github.com/ray-amjad/decision-tree) - Claude Code mod: explains the question at the end of Claude.
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod: Claude uses your secrets without seeing them.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - A Claude Code mod that keeps secrets out of the session transcript: every key…
- [razzamatazm/cache-keeper](https://github.com/razzamatazm/cache-keeper) - Claude Code mod: keeps an idle session.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod de Claude Code: flexiones para hacer mientras Claude trabaja. Sin tokens.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Tres mods sin dependencias para Claude Code: una línea de estado adaptable, un…
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - My mods for Claude Code.
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - A Claude Code mod that routes tasks to other AI models.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod de Claude Code: convierte el plan que apruebas en modo plan en una lista de…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una lista seleccionada manualmente de mods de código de Claude.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sin coste: los agentes auxiliares se ejecutan en Haiku, y los archivos…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una banda sonora lo-fi que sigue la sesión: calma, concentración y fluidez…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprende mientras Claude programa: después de un turno que haya cambiado el…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una cinta de cada edición que hace Claude: reproduce cada cambio mientras se…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Claude Code mods: token-bar, your context window and usage limits above the…
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod de Claude Code para contexto, crecimiento, cuota, caché, coste nativo y…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Mods personales de Claude Code.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - El DOOM original en un panel de Code de Claude sin necesidad de instalar nada…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Mody Claude Code (function hooks): panel agentów, pasek budżetu, flota sesji.
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Evita que los agentes auxiliares (subagentes) de Claude consuman tu uso.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensajes de commit con un clic para Claude Code con una Malenia bailarina en…
- [Stoneeu/zh-tw-dictation](https://github.com/Stoneeu/zh-tw-dictation) - Claude Code mod: Simplified Chinese in the prompt box.
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - 직접 만든 Claude Code mod 모음 (플러그인 마켓플레이스).
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場.
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Claude Code mod: see your Cursor / VS Code file and selection above the prompt…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — un mod de Claude Code que muestra el uso de tu plan de Claude…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod de Claude Code que muestra la sesión actual en un panel: cada aviso, el…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins de Claude Code de mods: plugins function-hooks que…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod: rewrites a rough prompt in place, naming fitting skills, open…
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Claude Code mod that writes your Claude usage limits to a file other tools can…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Escucha las respuestas de Claude Code mientras se resalta la frase que se está…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Claude Code mods by Toptaab.
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Small, fun and useful mods for Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod de Claude Code: banda de progreso animada y resumen de finalización para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tres pequeños mods de Claude Code: descubre cuándo terminarán tus subagentes…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Di «I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Hazle a Claude una pregunta aparte en un panel junto a tu trabajo.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code te envía avisos por Telegram cuando una tarea termina o espera…
- [WarrenLin/claude-typing-practice](https://github.com/WarrenLin/claude-typing-practice) - ⌨️ Claude Code mod：等 AI 回覆時練打字，即時顯示 WPM 與正確率.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Un mod de Claude Code: un marcador para las respuestas, un panel lateral para…
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter)
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod per Claude Code: segreti oscurati, cose da fare, verifiche e CI, diario…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin de Claude Code: tus límites de uso de Claude Pro/Max con una previsión…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para Claude Code. agent-crew: observa trabajar a tus subagentes como un…
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - Terminal side-panel mods for Claude Code — agent tracing, token-powered Tetris…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Un panel de tareas en directo para Claude Code: planifica antes de construir…
- [Young-in/pinboard](https://github.com/Young-in/pinboard) - Claude Code mod: pin tables, artifact links and answers from the conversation…
- [youngin-abel-kim/context-gauge](https://github.com/youngin-abel-kim/context-gauge) - A Claude Code mod: the context window as a one-line gauge above the prompt…
- [zyx1121/secret-mod](https://github.com/zyx1121/secret-mod) - Claude Code mod: credentials in the macOS keychain that Claude uses without…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una colección cuidadosamente seleccionada de los mejores recursos para los…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin de Claude Code que muestra lo que está ocurriendo: uso del contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Línea de estado atractiva y altamente personalizable para Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas las partes del indicador de sistema de Claude Code, las descripciones de…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Más de 45 consejos para sacar el máximo partido a Claude Code, desde los…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — genera carruseles de Xiaohongshu y pares de…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline elegante al estilo de vim para Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revisa el diff de tu agente de programación en un panel de terminal y envía…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de línea de estado completo para Claude Code con uso de contexto…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crea mods para Claude Code: intercepta cualquier solicitud, modifica cualquier…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Un panel de línea de estado completo para Claude Code — información de sesión…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: registra la huella de carbono de tus sesiones de Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Una línea de estado estética para Claude Code, creada por awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills y mods públicos de Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos slash y guías para Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legales y gratuitos, además de agentes de programación…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Calculadora de costes rápida y sin dependencias, y línea de estado…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Línea de estado de terminal para sesiones de Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Resultados, calendarios y clasificaciones de fútbol en vivo para la…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plano de control local para Claude Code en Windows y macOS: cambia los gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Skill de Agent que convierte tu agente de programación en un experto en…
- [Tripstack-Corp/spyc](https://github.com/Tripstack-Corp/spyc) - A Rust TUI file commander where the AI agent in the side pane can query the…
- [Corsinvest/cv4vs-agents](https://github.com/Corsinvest/cv4vs-agents) - Agentic coding inside Visual Studio: Claude Code with a rich chat pane, an…
- [MichengAI/dsh-pua](https://github.com/MichengAI/dsh-pua) - DSH PUA — 为 DeepSeek Harness 提供 PUA 任务推进、角色风味、验收循环和运行状态卡片 · PUA task…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horarios de oración, fecha Hijri, adhkar, ayah diaria, ayuno sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuración personal de Claude Code versionada dentro de ~/.claude — agentes…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — Complemento de DeepSeek Harness para temas de…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Línea de estado truecolor de dos líneas para Claude Code.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Colección de plugins para Claude Code, pi y DeepSeek Harness: HUD de barra de…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de herramientas de código Portable Claude para .NET DDD/Clean Architecture…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Línea de estado ligera de Claude Code: un único script Bash de unas 170 líneas…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuración global portátil de Claude Code: skills personalizadas, hooks de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins de Claude Code que uso a diario: skills y mods, depurados para que…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods no oficiales para la pestaña Code de Claude Desktop — usage-pet: una banda…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Puente DSH &lt;-&gt; Feishu (Lark), desarrollado internamente (no es un fork)…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins y habilidades de Claude Code para facilitar mods del…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gobernanza de tokens para Claude Code: el modelo principal dirige y la…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Split-pane viewer for Claude Code in Windows Terminal and tmux: the session as…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositorio de mods de Awesome Media para Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Reduce el gasto de Claude Code y Codex tokens: dirige consultas y ejecuciones…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Línea de estado configurable de Claude Code para Linux, WSL, Windows y macOS…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Muestra la línea de estado de Claude Code con límites de frecuencia, directorio…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Una línea de estado y una línea de tokens para Claude Code: contexto, uso de 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Muestra detalles clave del estado de Claude Code, incluidos el modelo, el…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipos de agentes nativos. Bajo control.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Complementos de Claude Code: indicador de estado de pestañas con punto de color…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Línea de estado de uso de Claude Code para macOS y Linux, empaquetada como…
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - Mercado personal de plugins de Claude Code (todo-pane).
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Una línea de estado limpia e informativa para Claude Code: muestra el proyecto…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins de Claude Code con baloo: skills, un agente que verifica…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Línea de estado de Claude Code en Lua, con un playground de Neovim en directo.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Línea de estado de Claude Code de nivel profesional: duración de sesión, coste…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Línea de estado de Claude Code consciente de la suscripción.
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - Los plugins de Claude Code de divramod, en un solo mercado: habilidades de…
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Línea de estado para Claude Code en español: tarea, habilidades, contexto con…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Línea de estado colorida de Claude Code: límites del plan, contexto, coste y…
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Línea de estado de Claude Code para Windows: totales de tokens, coste por…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Línea de estado personalizada de Claude Code.
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Barra de estado de una sola línea para Claude Code: modelo, git, contexto…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Previsualiza imágenes dentro de Claude Code: pasa el cursor sobre una etiqueta…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code status line with agent panel rows.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincroniza las tareas pendientes de Claude con Fizzy.do para que el equipo…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Controla el estado de Code de Claude con un panel compacto que muestra el…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook de línea de estado de Claude Code — realiza un seguimiento del uso de…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalador del entorno de Claude Code: skills, barra de estado, hooks, permisos…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness de Claude Code de Nacho (reglas, tablero, mods).
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Línea de estado estilo HUD para Claude Code — estado de la red, TPS, contexto…
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - OrihuelaConde.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — línea de estado de Claude Code para macOS +…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skills y mods para Claude Code y Cowork — project-tracker, reference-doc y más…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code status line for Windows (PowerShell): usage bars, 5h/7d reset…
- [Rezwan3App/claude-usage-meter-mod](https://github.com/Rezwan3App/claude-usage-meter-mod) - Session pane and control bar mod for Claude Code.
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Una línea de estado de dos líneas para Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Línea de estado personalizada de Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Starter harness for Claude Code: hooks, statusline, local models, swarm…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuración portátil de Code de Claude (barra de estado + instalador).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Un pequeño panel para Code de Claude: porcentaje de contexto, cuenta regresiva…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Barra de estado personalizada del terminal para Code de Claude: modelo…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuración portátil de Claude Code: CLAUDE.md, ajustes, línea de estado…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Colección de mods para Claude Code.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Línea de estado de Claude Code: el ID del modelo actual, el nombre de host, un…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Habilidad de Code de Claude (VS Code, Windows): vistas previas de imágenes y…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Una línea de estado de Claude Code: carpeta, rama de git, modelo, uso de la…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de degradación del contexto 2026 - Monitor proactivo de memoria de IA…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes y líneas de estado de Claude Code: colecciones y herramientas…
- [cuddly-guacamole/opencode-routing-suite](https://github.com/cuddly-guacamole/opencode-routing-suite) - Task-aware reasoning-mode routing for opencode: spec/react/weak three-band…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Línea de estado de Claude Code que muestra el uso de tokens en tiempo real y el…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - Una línea de estado basada en Deno para Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: paneles, bandas y compañeros basados en enlaces de…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Paquete de interfaz al estilo de Claude Code para el agente de programación Pi…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pasa tareas entre tus sesiones de Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Esto en un servidor MCP para controlar MODS, la herramienta modular…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Habilidad de Codex y Claude Code para traducir mods de CK3 con un LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código abierto y otras extensiones para Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code状态行：CCometixLine美化效果+Claude HUD功能.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encuentra lo que pides a Claude Code una y otra vez y conviértelo en…

</details>

<a id="dsh-cordis"></a>

## Ecosistemas de complementos de DSH y Cordis

DeepSeek Harness y Cordis llegan al mismo punto desde direcciones diferentes: para ellos, el complemento es el mecanismo de mods, así que allí un complemento equivale a un mod aquí.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74376 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **74376**  |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐118707 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **118707** |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100632 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **100632** |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82213 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **82213**  |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35767 · Go · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **35767**  |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25506 · Python · 🔎 inferred · 19 天</summary>

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
| Estrellas         | **25506**  |
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
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐9885 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **9885**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/212e73dc2aecbd46.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8644 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Ecosistema de agregación de complementos web de DeepSeek Harness (DSH) · Todo es un complemento, distribuido mediante el Taller creativo｜｜Ecosistema de agregación de complementos web de DeepSeek Harness (DSH) · Todo es un complemento, distribuido mediante el Taller creativo

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **8644**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4533 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **4533**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4303 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

El complemento TUI oficialmente más recomendado por DSH: alto rendimiento, bajo consumo, una simpática ballena pixelada e interacción fluida con el ratón. Instalación con un solo comando mediante npm. / El complemento TUI oficialmente más recomendado por DSH: alto rendimiento, bajo consumo, una simpática ballena pixelada, interacción fluida con el ratón e instalación con un solo comando mediante npm

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **4303**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3051 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **3051**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2004 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **2004**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1876 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1876**   |
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
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1595 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1595**   |
| Último envío      | 2026-10-12 |
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
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1466 · Python · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1466**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1176 · Go · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1176**   |
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
<summary>🧵 <b><a href="https://github.com/Clearailhc/clearai-dsh">Clearailhc/clearai-dsh</a></b> · ⭐1094 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

ClearAI: complemento DSH nativo y centrado en ontologías: investigaciones verificadas mediante evidencias que se convierten en una ontología de dominio navegable. · ClearAI: un ajuste preestablecido de agente DSH centrado en ontologías: investigaciones verificadas mediante evidencias que se convierten en una ontología de dominio.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1094**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `agent-preset` · `ai-agents` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `epistemic-loop` · `scientific-discovery`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/clearailhc--clearai-dsh/5621617dc3784a37.png" width="100%" alt="Clearailhc/clearai-dsh screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1009 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1009**   |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/1692775560/dsh-Mimir-Academic-research">1692775560/dsh-Mimir-Academic-research</a></b> · ⭐548 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Mimir — 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表、GPU 服务器 SSH 任务编排，管理科研全周期。An open-source research workbench plugin for the whole research cycle.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **548**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `arxiv` · `bibtex` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `experiment-tracking` · `gpu-cluster` · `latex`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/1692775560--dsh-mimir-academic-research/3574bee232095c3c.png" width="100%" alt="1692775560/dsh-Mimir-Academic-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/1692775560--dsh-mimir-academic-research/e05a56815f6c9f53.gif" width="100%" alt="1692775560/dsh-Mimir-Academic-research animation"><br><sub>grabación animada · <a href="https://raw.githubusercontent.com/1692775560/dsh-Mimir-Academic-research/main/docs/media/mimir-demo.mp4">Abrir vídeo</a></sub></td>
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
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Tu inteligencia, orquestada. Cada creador. Cada equipo. Cada agente. Para todos.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Go                                                                                |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **351**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>grabación animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐289 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **289**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐179 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **179**    |
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
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐173 · TypeScript · 🔎 inferred · 1 天</summary>

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
| Estrellas         | **173**    |
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
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐163 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Usa tu suscripción ChatGPT Plus / Pro (Codex) en DeepSeek Harness (DSH): modelos GPT-6 y Codex, imágenes, búsqueda web y cuota mediante el inicio de sesión de ChatGPT, sin clave OpenAI API. Beta: controla DSH desde la aplicación móvil de ChatGPT. Usa tu suscripción de ChatGPT en DSH y controla DSH de forma remota desde la aplicación móvil de ChatGPT.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **163**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/sorsama/deepseek-harness-mobile">sorsama/deepseek-harness-mobile</a></b> · ⭐146 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Compañero Android para DeepSeek Harness | chat, objetivos, aprobaciones y notificaciones desde tu teléfono, a través de tu LAN. Kotlin + Jetpack Compose.

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Kotlin                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **146**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `ai-agents` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sorsama--deepseek-harness-mobile/11352624becb7d93.jpg" width="100%" alt="sorsama/deepseek-harness-mobile screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **137**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MichengAI/dsh-codex-ui">MichengAI/dsh-codex-ui</a></b> · ⭐136 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DSH Codex UI — 为 DeepSeek Harness Web 提供 Codex 风格侧栏、工作区会话树、全局搜索和轮次导航 · A Codex-style sidebar, workspace session tree, global search, and turn navigation for DSH Web

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **136**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/michengai--dsh-codex-ui/24e91fea2ad1b1d0.png" width="100%" alt="MichengAI/dsh-codex-ui screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐136 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **136**    |
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
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MichengAI/dsh-archive-manager">MichengAI/dsh-archive-manager</a></b> · ⭐120 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DSH Archive Manager — 在 DeepSeek Harness 中安全查看、恢复和管理已归档会话 · Safely view, restore, and manage archived sessions in DSH

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **120**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/michengai--dsh-archive-manager/09204832afc71a71.webp" width="100%" alt="MichengAI/dsh-archive-manager screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xcisxc29/dsh-wechat">xcisxc29/dsh-wechat</a></b> · ⭐118 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Canal de WeChat para DeepSeek Harness

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **118**    |
| Último envío      | 2026-10-12 |
| Primera inclusión | 2026-10-12 |

🏷 `ai-agent` · `automation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `remote-control` · `wechat` · `wechat-bot`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xcisxc29--dsh-wechat/689ef8e1483bcfd7.png" width="100%" alt="xcisxc29/dsh-wechat screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Protección previa a la ejecución para agentes de programación con IA.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Una lista seleccionada de los mejores plugins de IA para asistentes de IA…
- [sixtysevenlf/dsh-blender-plugin](https://github.com/sixtysevenlf/dsh-blender-plugin) - DSH x Blender direct realtime plugin v1.0 — let an AI model drive Blender over…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin de DSH — modelos OpenCode Zen gratuitos para DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins de DSH / DSH Plugin Marketplace: explora, instala y…
- [beancookie/awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin) - Awesome DeepSeek Harness (DSH) Plugin.
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、39个世界与上千素材、开局随心定制、世界自行运转、零漂移存档.
- [arcships/rutis](https://github.com/arcships/rutis) - Un runtime de plugins para software que itera sobre sí mismo: la base donde los…
- [MichengAI/dsh-skills-manager](https://github.com/MichengAI/dsh-skills-manager) - DSH Skills Manager — 在 DeepSeek Harness 中统一加载并安全管理本机 Agent Skills · Load and…
- [MichengAI/dsh-agency-agents](https://github.com/MichengAI/dsh-agency-agents) - DSH Agency Agents — 为 DeepSeek Harness 提供 321 名可召唤的专业智能体 · 321 summonable…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Agent de escritorio creado sobre la base central de Deepseek-Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - El directorio activo de plugins de DeepSeek Harness — actualizado cada hora…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directorio seleccionado de plugins de DeepSeek Harness (DSH): más de 280…
- [MichengAI/dsh-im-connect](https://github.com/MichengAI/dsh-im-connect) - DSH IM Connect — 将主流即时通讯平台接入本机 DeepSeek Harness · Connect major messaging…
- [398894496-arch/KRouter](https://github.com/398894496-arch/KRouter) - Your coding agents remember what you decided — and what you changed.
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Plugin maestro de recursos para juegos de dsh.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistema de agentes de chat grupal multiplataforma basado en DeepSeek…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Plugin de DeepSeek Harness: empareja modelos con la ventana de contexto con un…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Complemento de Zotero para DeepSeek Harness: busca artículos, lee PDF y notas a…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [YRN-playmaker/dsh-wallpaper_share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - 一键同步壁纸引擎各类动态场景壁纸的插件，设置应用启动项。A &quot;wallpaper engine&quot; synchronization plugin mounted…
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - Community GitHub Action for DeepSeek Harness — AI Code Review · CI Diagnosis ·…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - Gestión de grupos QQ mediante IA: ¡moderación y aprobación, envío de archivos…
- [MichengAI/dsh-automation](https://github.com/MichengAI/dsh-automation) - DSH Automation — 在独立 DSH Session 中按计划执行和管理编码任务 · Schedule and manage coding…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Colección de plugins GUI web de DSH (DeepSeek Harness) — notificaciones de…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - Gestión de actualizaciones del programa principal y los complementos de…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de negociación comercial A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Panel de herramientas para DeepSeek Harness Web: gestor de MCP.
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - AI argues. Code settles. The losses stay on the page.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un PowerPoint real, no HTML. Dile a tu IA qué debe incluir y pptwise creará una…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Grafo de conocimiento de código y harness de contexto para agentes de…
- [MichengAI/dsh-btw](https://github.com/MichengAI/dsh-btw) - DSH 一次性只读旁问插件：基于当前上下文回答，独立气泡，不执行工具 · One-shot read-only side-ask plugin…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 嵌入式C/C++ AI工程插件——固件技能（FreeRTOS、Keil、HardFault、状态机）+ 1% Rule / Plan Verification…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Convierte los modelos en los que has iniciado sesión en la aplicación de…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - plugin dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pruebas de compatibilidad siempre activas para plugins de DeepSeek Harness…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Compresión agresiva del contexto para agentes locales.
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Compactación protegida del contexto para DeepSeek Harness (dsh): LLM propone y…
- [morlay/dsh-plugin](https://github.com/morlay/dsh-plugin) - complementos de dsh.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host de DeepSeek Harness que conserva los documentos del proyecto y la…
- [MichengAI/dsh-code-review](https://github.com/MichengAI/dsh-code-review) - DSH Code Review — 为 DeepSeek Harness 提供 Codex 风格代码审查、原生独立子 Agent、灵活范围选择和中英文报告 ·…
- [MichengAI/dsh-simplify](https://github.com/MichengAI/dsh-simplify) - DSH Simplify — 为 DeepSeek Harness 提供限定 Git 变更范围的代码简化，支持未跟踪文件、跨平台路径与可靠的 Git 异常处理…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayos X para plugins de DeepSeek Harness: capacidades declaradas frente a…
- [0x7A7A6572/dsh-forge-studio](https://github.com/0x7A7A6572/dsh-forge-studio) - Aggregated dsh plugins for daily use — a dsh-plugin rewrite of Forge Studio.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [JessenReinhart/dsh-tokenslash](https://github.com/JessenReinhart/dsh-tokenslash)
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin de DSH: ventana de herramientas Git de nivel IDE como pestaña nativa de…
- [studyzy/dsh-suggest-prompt](https://github.com/studyzy/dsh-suggest-prompt) - dsh-plugin 根据AI回复给出建议的下一个提示词.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espacio de trabajo con varias carpetas: permite que el agente de DSH.
- [CoolTea001/dsh-cool-theme](https://github.com/CoolTea001/dsh-cool-theme) - Complemento de temas de DeepSeek Harness: admite el cambio de apariencia Oscuro…
- [MHfire/dsh-im-bridge](https://github.com/MHfire/dsh-im-bridge) - 即时通讯渠道(企微、飞书等) ⇄ DeepSeek Harness Agent 桥接.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Estándar de verificación sin dependencias para plugins de DeepSeek Harness…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode en DeepSeek Harness — plugin de DSH que mantiene funcionando OpenCode…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — mercado de plugins de terceros y gestor de ciclo de vida protegido…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx es un espacio de trabajo de escritorio ampliable y centrado en las…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [InterPSS-Project/ipss-agent](https://github.com/InterPSS-Project/ipss-agent) - InterPSS Agentic Power System Simulation Agent for AC load flow, DC-based…
- [MichengAI/dsh-codex-pet](https://github.com/MichengAI/dsh-codex-pet) - DSH Codex Pet — 为 DeepSeek Harness 提供宠物陪伴、多任务提醒与交互，以及 Skill 自定义宠物 · A pet…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web de DeepSeek Harness (DSH): pestaña lateral market-dashboard para…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Complemento de DeepSeek Harness: convierte el fallo de aprovisionamiento de ACL…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Permite volver a intentar un intento vacío de modelo sin atribución, para la…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Evaluación del progreso para las rondas de objetivos autónomos de dsh: pospone…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - Plugin de dsh: convierte una detención por longitud truncada en la recuperación…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins que se limpian solos: un port de Swift 6 del framework de plugins…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins de Rust con un kernel de ciclo de vida verificado por…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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

| Lenguaje   | Entradas | Ejemplos                                                                                                       |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| TypeScript | 390      | `anthropics/claude-code`, `anthropics/claude-code-action`, `see-stack/claude-code-mods`                        |
| JavaScript | 81       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                 |
| Python     | 42       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`  |
| Shell      | 24       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`            |
| HTML       | 12       | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                             |
| Go         | 6        | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                          |
| Rust       | 6        | `persiyanov/herdr-reviewr`, `Tripstack-Corp/spyc`, `OpenClawFarm/claude-statusline`                            |
| PowerShell | 3        | `GoSlowPoke168/claude-statusline`, `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win` |
| Swift      | 3        | `olilllioli287/claude-code-image-shelf`, `KiranPothana/session-board`, `eovidiu/cordis-ios`                    |
| C          | 1        | `reporails/arcade`                                                                                             |
| C#         | 1        | `Corsinvest/cv4vs-agents`                                                                                      |
| Kotlin     | 1        | `sorsama/deepseek-harness-mobile`                                                                              |
| Lua        | 1        | `crafts69guy/claude-statusline.nvim`                                                                           |
| MDX        | 1        | `jkf87/mod-guide`                                                                                              |

<sub>Solo se contabilizan las entradas que declaran un idioma. Las entradas de documentación y debate se excluyen de esta tabla.</sub>

## Contribuir

Las correcciones son bienvenidas y son la forma más rápida de mejorar esta lista. Abre un issue o una pull request si una entrada está mal clasificada, tiene una categoría incorrecta o si un proyecto se ha excluido por error debido a una coincidencia de nombres; esta última categoría es donde más probablemente fallen los filtros automatizados.

---

<sub>Proyecto independiente de la comunidad. No está afiliado a Anthropic, ni cuenta con su respaldo o revisión. Claude Code, Claude y Anthropic son marcas comerciales de Anthropic. El comportamiento del producto puede cambiar sin previo aviso; verifica cualquier aspecto esencial en la documentación oficial. Los recursos siguen siendo propiedad de sus proyectos de origen y se reproducen únicamente cuando una licencia lo permite.</sub>

<sub>Última actualización · 2026-10-12T14:51:24+08:00</sub>
