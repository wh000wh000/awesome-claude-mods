<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods increíbles de Claude">
</p>

<h1 align="center">Mods increíbles de Claude</h1>

<p align="center"><b>El índice de mods y plugins de Claude Code, clasificados según la evidencia, y del comportamiento más profundo que modifican.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-584-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <b>Español</b> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice activo** · Última sincronización: `2026-10-11T19:01:04+08:00` (UTC+8)
> · Entradas: **584** · Añadidas en la última actualización: **0** · Lenguajes de implementación: **13**

<sub>Todas las entradas siguientes se recopilaron, filtraron y revisaron de nuevo automáticamente. Nada de lo que aparece aquí es contenido promocional de pago.</sub>

<a id="featured"></a>

## Selecciones del momento

<sub>Una entrada por categoría, clasificadas según el nivel de evidencia y las estrellas, y recalculadas con cada actualización. Es una clasificación, no una recomendación; cada selección enlaza con su ficha completa más abajo. Se prefieren los proyectos que han publicado una captura de pantalla o una grabación, para que la franja siga siendo visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kuangre123--codex-switch/dcd3073c9c57be83.png" width="100%" alt="kuangre123/codex-switch">
<b>🏛️ <a href="https://github.com/kuangre123/codex-switch">kuangre123/codex-switch</a></b>
<sub>⭐70 · Python · 🔎 inferred</sub>
<sub>Codex Switch 是一个 macOS 工具，一键配置 Codex 的自定义 API，同时保留官方 OpenAI 登录。保存后 Codex 的模型选择器里只会出现你选的那个 provider 的模型。也支持 Claude Code 的官方 / 自定义 API 切换。Codex Switch is a lightweight…</sub>
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
<sub>⭐74319 · TypeScript · 👁️ observed</sub>
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
- [Oficiales: repositorios propios y notas de versión de Anthropic](#oficiales-repositorios-propios-y-notas-de-versión-de-anthropic) — **11**
- [Mods: creados con la capacidad de mods](#mods-creados-con-la-capacidad-de-mods) — **463**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150125 · TypeScript · ✅ official · 0 天</summary>

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
| Estrellas         | **150125** |
| Último envío      | 2026-10-10 |
| Primera inclusión | 2026-10-04 |

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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.295 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Se añadió `$.ui.notify` para los mods: muestra una notificación nativa mediante tu propia configuración de notificaciones e indica qué canal la envió Se añadieron elementos secundarios a `Button` de un mod: cadenas y `Text`, de modo que una fila de una lista se puede pulsar una vez y contiene un chip o un detalle atenuado dentro Se corrigió que el hook de un mod recibiera una entrada de herramienta profundamente anidada truncada sin ningún error, lo que permitía a una protección pasar contenido que nunca había visto Se corrigieron las llamadas que realiza un mod mientras se recarga durante el reinicio de un trabajador de hooks de plugins, que conseguían superar el hook de protección de otro mod que tiene un `.catch`; ahora esas llamadas se rechazan Se corrigió que la recarga en caliente de un mod no detectara un guardado realizado mientras `/r

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-09 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.296 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Resumen

Corregido Esc o una interrupción durante un hook de `UserPromptSubmit` o un hook `prompt.submit` de un mod que terminaba sesiones headless, borraba el prompt escrito o dejaba pasar el prompt sin comprobar. Corregido `$.agent.register` que tenía éxito desde el hook de un mod que seguía ejecutándose después de que el mod se recargara o eliminara; ahora la llamada se rechaza. Corregido `$.http.fetch` en mods que rechazan una solicitud `HEAD` cuando la respuesta declara un `Content-Length` por encima del límite de cuerpo de 4 MiB

##### 📌 Datos básicos

| Campo     | Valor                                                             |
| --------- | ----------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic` |
| Evidencia | `publicado por Anthropic mismo`                                   |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Primera inclusión | 2026-10-10 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/kuangre123/codex-switch">kuangre123/codex-switch</a></b> · ⭐70 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Codex Switch 是一个 macOS 工具，一键配置 Codex 的自定义 API，同时保留官方 OpenAI 登录。保存后 Codex 的模型选择器里只会出现你选的那个 provider 的模型。也支持 Claude Code 的官方 / 自定义 API 切换。Codex Switch is a lightweight helper for configuring multiple coding-agent API routes. For Codex, it keeps Official OpenAI and a custom API provider configured in parallel, registers the custom model in Codex's mod

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Oficiales: repositorios propios y notas de versión de Anthropic`                 |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **70**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `codex` · `codex-app` · `codex-cli` · `codex-desktop` · `codex-github` · `codex-pet` · `codex-plugin` · `codex-project`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kuangre123--codex-switch/dcd3073c9c57be83.png" width="100%" alt="kuangre123/codex-switch screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/X-C1811/dsh-web-search-plugin">X-C1811/dsh-web-search-plugin</a></b> · ⭐3 · JavaScript · 🔎 inferred · 1 天</summary>

##### 📝 Resumen

为你的DeepSeek Harness agent提供更多网页搜索方式。在设置中于9个提供商之间切换，从官方DeepSeek和Google结果到自托管SearXNG。无需API密钥即可试用Tavily，或在一个位置管理提供商密钥。

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
| Primera inclusión | 2026-10-11 |

🏷 `brave-search` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `exa` · `firecrawl` · `search`

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐483 · JavaScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **483**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐184 · TypeScript · 👁️ observed · 1 天</summary>

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
| Estrellas         | **184**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

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
| Estrellas         | **59**     |
| Último envío      | 2026-10-07 |
| Primera inclusión | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Resumen

Colección de más de 100 mods que puedes usar con Claude Code.

<sub>🔧 Encontrado en el código: `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`, `docs/COMMUNITY_MODS.md`</sub>

##### 📌 Datos básicos

| Campo     | Valor                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Categoría | `Mods: creados con la capacidad de mods`                                |
| Evidencia | `su propio texto menciona un mod API o declara la capacidad de modding` |
| Lenguaje  | TypeScript                                                              |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **47**     |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

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
| Estrellas         | **46**     |
| Último envío      | 2026-10-08 |
| Primera inclusión | 2026-10-04 |

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
| Estrellas         | **13**     |
| Último envío      | 2026-10-03 |
| Primera inclusión | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary><b>Más en esta categoría</b> <sub>· 429</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods de Claude y las herramientas para crearlos: primero una skill de creación…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - El harness de Claude Code que uso a diario, publicado con este nombre desde el…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Cambia el tejado de Claude Code con Claude Mods: sustituye el prompt del…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Cuatro mods de Claude Code: Cache Keeper, Recording Mode, Goal Meter y…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods de Claude Code de Learning Hacker: convierten el funcionamiento del agente…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods de Claude Code que corrigen y traducen tus prompts antes de que Claude los…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - 为Claude Code的终端记录打造桌面应用外观的mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Un panel lateral para Claude Code: los subagentes que ejecuta una sesión, qué…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conocimiento de Obsidian con fuentes sobre los mods de Claude Code…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel de barra lateral de Claude Desktop (pestaña Code): enumera todas las…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods y habilidades de Claude Code de Nekyia Labs, creados y usados a diario por…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Habilidad que enseña a los agentes de Claude Code a crear Mods de Claude…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso encima del cuadro de entrada de Claude Desktop (pestaña Code)…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins y habilidades comunitarios de Claude, instalables desde un único…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (plugins de enlaces de funciones) para Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - La galería de mods de Baselane: mods de Claude Code, revisados y fijados.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Una cola de decisiones CLI/TUI para personas que trabajan con agentes…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Tarjeta de estado flotante para Claude Code — modelo, contexto, límites de…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nombres y secretos mientras compartes…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensiones de Claude Code. Desbloquea todo el poder de Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) de Claude Code que añade un panel lateral con pestañas Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Paneles, protecciones y mods para mejorar la experiencia en Claude Code…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dos mods de Claude Code sobre el cuadro de prompt: medidor de ventana de…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Tu plan, observándose a sí mismo. Árbol local de hoja de ruta de escritorio que…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Lee los archivos markdown que nombra Claude Code, renderizados junto a la…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Compañero de voz para Claude Code. Habla sobre tus ideas con un lobo 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, un velocímetro de escritura activo con…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fuegos artificiales para Claude Code: cada pulsación, llamada a herramienta…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubre mods, plugins y extensiones de Claude Code con demos animadas, listas…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas de mermaid dibujados en línea en la transcripción.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequeños mods de Claude Code (plugins de function-hook): session-switcher y más.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imágenes pegadas encima del prompt, en…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - 查看下一条Claude Code消息的成本：提示词上方的实时横幅显示提示词缓存倒计时、重新预热价格、会话成本、上下文以及5小时/每周使用限额.
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
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Un plugin de Claude Code muy particular, diseñado por un Rustacean obsesionado…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantienen al agente honesto — hooks de funciones que…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Mi colección de mods de Claude Code, un mod por directorio.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 适用于Claude Code的被动攻击式喝水提醒。零token，最大限度的评判.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Recién salido de fábrica. Un mod de Claude Code: pide un meme y sigue…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod para Claude Code: barra de caché de prompts, próximos pasos, botones…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Un mod de Claude Code que muestra tus límites de uso y gasto en la banda sobre…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Una tienda de apps para mods de Claude Code, dentro de Claude Code: /mods para…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods de Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods de Claude Code: barras de progreso para planes, un registro de lo que…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Un compañero de Naruto en pixel art para Claude Code: 20 ninjas, 60 jutsu…
- [iamumeransari/claude-show-your-work](https://github.com/iamumeransari/claude-show-your-work) - Claude Code shows images and plays videos right in your terminal: screenshots…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: límites de plan y contexto sobre el prompt, un coach…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Mira lo que Claude Code ejecuta en segundo plano: subagentes, trabajos de…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs开发的Claude Code mods：streams将会话中交错的工作拆分为带颜色标记的流.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo del primer día sobre mods de Claude Code en Windows: una barra…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods que hice y uso personalmente en mi configuración de Claude Code.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod de Claude Code: medidores en vivo de coste, contexto y cuota del plan…
- [pawandeepdhall/claude-mods](https://github.com/pawandeepdhall/claude-mods) - Claude Code mods: always-visible 5-hour &amp; weekly usage limits with reset…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Un mod de Claude Code que retiene la distribución de subagentes, las…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods para claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Un mod de Claude Code que activa o desactiva tus habilidades, agentes, reglas y…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins (mods) de Claude Code: cambia entre varias cuentas de Claude, supervisa…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods de código de Claude probados e instalables con un comando: protecciones…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods para Claude Code: plugins creados sobre hooks de función.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Créditos al estilo cinematográfico para tu sesión de programación.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 自有Claude Code mod插件市场.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Un montón de mods de claude code creados por mí.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Un reproductor de YouTube respaldado por cliamp dentro de Claude Code.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Mods de Claude Code: panel de flota de agentes y piloto automático.
- [vynnlee/mods](https://github.com/vynnlee/mods) - Mods de Claude Code de vynnlee. Una carpeta por mod, instalables desde un único…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprende un idioma extranjero mientras trabajas con Claude Code.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Respuestas con tema, diagramas de ancho completo y tu contexto y límites de un…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Cuando el agente escribe Java, el código que infringe la convención p3c de…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de coste, tokens y uso del contexto en tiempo real para Claude…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Mod de Claude Code: un registro de seguimientos pendientes sugeridos por Claude…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio por Internet dentro de Claude Code: barra lateral cliamp…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - 用于产品开发工作的Herdr设置+Claude Code mods.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Panel del notch de macOS para Claude Code: límites de uso, sesiones abiertas…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude está cocinando. Chatea con tu escuadrón.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack的Claude Code mods合集.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - 一个Claude Code mod：在Claude工作时，在休闲游戏中捕捉像素艺术Modsters.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Mod todo en uno para Claude Code: un HUD en vivo, protecciones de seguridad…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - A space battle above Claude Code.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Ve qué archivos tiene cada agente de Claude Code en su contexto, y cuánto de…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code的mods：使用插件function-hooks API构建的面板、命令和hooks.
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Mantén la cabeza fría. Un termómetro para tus días de Claude Code: cada hora…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - 在Claude Code的提示词页脚和提示词上方，一览提示词缓存、上下文和计划限额.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Mod de Claude Code: un panel en tiempo real de las solicitudes de incorporación…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequeños mods de Claude Code para el terminal y la aplicación de escritorio.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Claude Code mods合集，每个mod都位于独立仓库中：usage-meter、progress-board、session-toc.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod de Claude Code: un panel de progreso para tareas, subagents, ejecuciones de…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Mod de Claude Code: una tabla de contenidos clicable y con marcas de tiempo de…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod de Claude Code: límites de tasa del plan, llenado de contexto, coste de…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidad + mod de Claude CLI que añade palabras en español a las respuestas…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Un mod de Claude Code que lo rediseña como The Machine de Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Mod de Claude Code: compacta en el momento adecuado.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow：用于强制执行并验证subagents DAG工作流的Claude Code mod，带有实时DAG面板.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código abierto para Claude Code: paneles, líneas de estado…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Un mod de Claude Code: un panel para cada subagente, los archivos que toca y el…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod de Claude Code: estado de sesión, progreso en vivo de Spec Kit y…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - La ventana de contexto como una fila sobre el prompt, dibujada como Claude Code…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratuito y de código abierto para Claude Code.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Un Mod de Claude que muestra las solicitudes de extracción de GitHub de la…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Mod de Claude Code: genera efectos de sonido a partir de indicaciones de texto…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Habilidades de Claude Code: un verificador de hechos de documentación, un…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod de Claude Code: líneas de código de hoy por Claude — nuevas, editadas…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod de Claude Code: rutas clicables en las respuestas;
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Claude Code mod: picks /effort per prompt with Jev.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin compañero de Claude Code: un acompañante ASCII sobre el prompt que…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin de Claude Code para la visibilidad de herramientas por agente: oculta y…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Modificaciones de Claude Code: capa de seguridad para Claude Code: redacción de…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin y mod de Claude Code: un SDLC nativo de IA.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Colección Awesome de mods de Claude Code | Colección de mods de 클로드 코드.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Habla: un mod de Claude Code que lee en voz alta, cuando se solicita, las…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Azota a Claude cuando se equivoca — un mod antiestrés para Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods de Claude Code: pequeños plugins para paneles en tiempo real, enrutamiento…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod y plugin de Claude Code: monitor de uso, rastreador de tokens y línea de…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Una modificación de Claude Code que delega las decisiones pequeñas a un modelo…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Tres modificaciones gratuitas de Claude Code: oculta los valores de .env de los…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods de Claude Code. touch-map: muestra qué archivos enumeró, leyó, editó o…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Un mod de Claude Code que resume en inglés sencillo los mensajes del agente que…
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Modificaciones para Claude Code: paneles en directo, bandas y hooks.
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Marketplace de plugins de Claude Code para los mods de 0xnicholasy…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Modificación de Claude Code: barras de progreso de uso (contexto, 5h, 7d) y un…
- [akkaradej/hawkeye](https://github.com/akkaradej/hawkeye) - Claude Code mod: status dot, extend prompt cache, context ring, reborn, auto…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Modificaciones de Claude Code: tarjetas de estadísticas de la sesión sobre la…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Un gato braille animado sobre el prompt de Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod de Claude Code: dirige el trabajo barato a GLM/Kimi mediante un Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Un gato pixelado sobre el prompt de Claude Code que ejecuta una llamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Un mod de Claude Code que elige un buen momento para compactar y mantener…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Mods para Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Mercado de plugins de Claude Code de anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code mod: your plan.
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Modificaciones de Claude Code para observar el mercado desde el terminal: panel…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Modificaciones para Claude Code.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - My private Claude Code mods.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - El barco de LGTM Lines navega tras cada cambio de código: un mod de Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Tus límites de uso de Claude como tarjeta animada de salud de aldeano: un mod…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mods de Claude Code para el equipo S2 (el marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Entrenamientos cortos mientras Claude trabaja: un objetivo diario, rachas…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Progreso del plan, las tareas y los agentes junto a la indicación de Claude…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Un panel de uso para Claude Code: gasto por modelo.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Un mod de Claude Code: desglose del contexto de la ventana en directo sobre el…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para Claude Code: Apple Music y Spotify sobre el aviso, con…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Cinco mods de Claude Code para ejecutar muchas sesiones a la vez: tablero de…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Paquete de modificaciones de Claude Code del vídeo de Berko: Mask, View, Guard…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: reloj de caché, radio de impacto, sugerencias, lista de…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Solo un búho para tu Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Banda de Claude Code de una línea.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - El motor original de Doom con Freedoom, jugable dentro de Claude Code.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Claude Code mod: estimated electricity ⚡ and water 💧 behind each turn and…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Un mod de Claude Code que mantiene una lista continua de los elementos abiertos…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Claude Code mods for real Engineers.
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Modificaciones de Claude Code exclusivas para el equipo d3nim.
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code mods: rule-keeper saves your corrections as permanent rules.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Un Tamagotchi que vive dentro de Claude Code: eclosiona, se come el código que…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods para Claude Code, como marketplace de plugins.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Mod de Claude Code: muestra la hora de cada prompt y respuesta en el terminal y…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mods de Claude Code escritos como hooks de funciones y el marketplace que los…
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Modificaciones de Claude Code y sistemas de diseño: crab-crew y el sistema de…
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - Mis modificaciones de Claude Code, compartidas como un mercado de plugins.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod de Claude Code: después de que un guard bloquee una llamada a una…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod de Claude Code: trabajos en segundo plano en una sola vista, con progreso y…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod de Claude Code: una sola bandeja de entrada para mensajes de compañeros de…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod de Claude Code: explica los bloqueos del sandbox y convierte los bloqueos…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favourites for Claude Code: one-click icons for your commands and skills.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - ¡Ey, lo silencié! Deshazte del diff, corta el riff;
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - Modificaciones para claude.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code mods: delete-guard (confirm file deletions) and octopus-crew.
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod de Claude Code: uso de la suscripción (5h / 7d) como una banda sobre el…
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Mods con diseño de movimiento para Claude Code: un monitor activo y adaptable…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Un radar en tiempo real de tus ramas y worktrees paralelos sobre el prompt…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Embed Alarum.me in your Claude code CLI or Desktop.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Embed Floatee.me in your Claude code CLI or Desktop.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Una modificación de Claude Code para capturar pensamientos durante el trabajo…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Modificaciones y skins para Claude Code: una barra de progreso en directo para…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Mods de Claude Code (plugins de function-hook): banda de contexto, asuntos…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Siete modificaciones de Claude Code: savvy-progress, skins, filetree…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Copiar el enlace con Ctrl+clic en cada bloque de código de las respuestas de…
- [Gersom/claude-mod-agent-radar](https://github.com/Gersom/claude-mod-agent-radar) - Modificación de Claude Code: monitor visual y pasivo del agente principal y sus…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mods para Claude Code: plugins de hooks, como usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Claude Code mods (function-hook plugins), installed through one marketplace.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra lateral al estilo de Evangelion para Claude Code: contexto, cuota…
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Modificaciones de Claude Code: context-bar-plus.
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Auditor estático de la cadena de suministro para las modificaciones de Claude…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Modificaciones en alemán para Claude Code: avisos de contexto/caché, puntos…
- [helenkwok/open-links](https://github.com/helenkwok/open-links) - Modificación de Claude Code: las rutas de archivos en las respuestas de Claude…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Resultados de pruebas en un panel de Claude Code: fallos, sus detalles e…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de Claude Code: cuánto tardó cada respuesta, cuánto tiempo pensó Claude y…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - para mis modificaciones de claude.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod de Claude Code: espera a que pase el límite de uso de 5 horas y envía…
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Pequeñas modificaciones para Claude Code, empezando por la continuación…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Una cabina sobre tu indicación de Claude Code. El pato lee los medidores.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Pequeñas modificaciones de Claude Code: medidores de contexto y uso del plan…
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
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Mod de Claude Code: subagents en ejecución como mascotas pixel Claude sobre el…
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Modificaciones de Claude para mejorar los detalles y la calidad de uso.
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code mods (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dos mods de Claude Code: folio, un panel de archivos junto al chat, y tint, un…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Un HUD de tareas en tiempo real para Claude Code Desktop: una franja sobre el…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - No dejes que tu atención se desvíe mientras esperas la respuesta de Claude Code.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Modificaciones de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Guía de Mods de Claude Code seleccionada por la comunidad: casos de uso…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Un mod de Claude Code que muestra lo que Claude está haciendo en el subtítulo…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Un gato negro y esponjoso sobre tu prompt de Claude Code.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Las modificaciones de Claude Code de Marcel en un solo mercado de plugins…
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Un mod de Claude Code con perfiles de permisos intercambiables: una base…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Modificación de Claude Code para realizar un seguimiento de artefactos y…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods de la comunidad para Claude Code: protecciones, paneles y comandos que se…
- [MehdiChebbi13/clean-view](https://github.com/MehdiChebbi13/clean-view) - Claude Code mod: hide tool-call noise, show Claude.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel lateral para Claude Code: archivos que escribió Claude, divisiones del…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Un discreto panel lateral para Claude Code: qué está haciendo esta sesión, su…
- [mmedum/nuet](https://github.com/mmedum/nuet) - A dim time above each prompt and each reply in the Claude Code transcript…
- [mmedum/spor](https://github.com/mmedum/spor) - Devuelve lo que Claude oculta: los archivos que Claude leyó, los comandos que…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Modificación de Claude Code: uso de la ventana de contexto en el espacio del…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod de código de Claude que vuelve a activar las herramientas de tareas para…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod de código de Claude: una línea por tarea encima del prompt con la tarea…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Juega Connect Four contra una AI dentro de Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: cuando otro agente de programación hace un commit en tu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositorios compartidos por varios agentes de IA…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Una barrera de protección para SQL en Claude Code: pregunta antes de que Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Un mod para Claude Code, Windows y CJK en primer plano: vistas previas de…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Modificaciones de Claude Code: miniaturas de imágenes y línea de estado.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Los mejores Mods de Claude Code, ordenados por lo que hacen por ti.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Un mod de Claude Code que retiene comandos de shell arriesgados.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dos Mods de Claude para Claude Code: guardaespaldas.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Modificaciones de Claude Code con telemetría de agentes, paneles de cronología…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Insulta a Claude Code y una mano de dibujos animados te devuelve una bofetada.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Modificaciones de Claude Code: usage-both muestra el uso de 5 horas y semanal…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel lateral de estadísticas de sesión en vivo para la pestaña Code de la…
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Mods de Claude Code para la interfaz de pompeitech, con el sistema de diseño…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods para Claude Code: safety-guard bloquea comandos destructivos y el acceso a…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mods para Claude Code: plugins function-hook que se ejecutan dentro de la…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod de Claude Code: cotización bursátil en tiempo real, panel /quote, alertas…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod de Claude Code: host SSH, RAM y límites de uso de 5 h/7 d en una fila sobre…
- [RexWei1016/claude-project-progress](https://github.com/RexWei1016/claude-project-progress) - Mod de Claude Code: panel de progreso del proyecto a partir de hitos…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod de Claude Code: flexiones para hacer mientras Claude trabaja. Sin tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 mods de Claude Code en coreano: registro de suposiciones, lenguaje sencillo…
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - Un mod de Claude Code que dirige las tareas a otros modelos de IA.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - La tienda de mods para Claude Code: extrae mods de GitHub, muestra vistas…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod de Claude Code: convierte el plan que apruebas en modo plan en una lista de…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Una lista seleccionada manualmente de mods de código de Claude.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sin coste: los agentes auxiliares se ejecutan en Haiku, y los archivos…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Una banda sonora lo-fi que sigue la sesión: calma, concentración y fluidez…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprende mientras Claude programa: después de un turno que haya cambiado el…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Una cinta de cada edición que hace Claude: reproduce cada cambio mientras se…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Cada enlace que menciona tu sesión, en una fila sobre el prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Demostración mínima de hooks de funciones de Claude Code: panel de tokens/coste…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Claude Code Mod: 5h-, Wochen- und Fable-Limit als Leiste über dem Prompt.
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Una colección de plugins para Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: un mod no oficial de fans de Avengers para Claude Code.
- [shawnbotha/claude-mods](https://github.com/shawnbotha/claude-mods) - Diferentes mods de Claude.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod de Claude Code para contexto, crecimiento, cuota, caché, coste nativo y…
- [shezis/claude-api-cost-compare](https://github.com/shezis/claude-api-cost-compare) - Mod de Claude Code: comprueba en directo cuánto costaría tu sesión en Claude…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Mod de Claude Code: dirige las interacciones sencillas y los subagentes a…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Un mod de HUD de RPG acogedor para Claude Code.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensajes de commit con un clic para Claude Code con una Malenia bailarina en…
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Mods personales de Claude Code.
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - Una barra de estado configurable para Claude Code — banda, línea de estado…
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugins para Claude Code.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Repositorio local de mods de Claude Code.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — a Claude Code mod that shows your Claude plan usage.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Mod de Claude Code: panel de equipo en tiempo real para cada subagente.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Un mod de Claude Code que muestra la sesión actual en un panel: cada aviso, el…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Un marketplace de plugins de Claude Code de mods: plugins function-hooks que…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de Claude Code bajo demanda — una habilidad que lee tu conversación y crea…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Repositorio para gestionar mods de Claude.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Personalizaciones para Claude Code.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Mod de Claude Code: una banda y un panel que siguen a tus subagentes, junto con…
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Claude Code mod that checks the English of your prompt while you write it.
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
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Capa de seguridad de Roblox Studio para Claude Code: auditoría de RemoteEvent…
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Pequeños mods para mejorar la experiencia con Claude Code.
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin de Claude Code: tus límites de uso de Claude Pro/Max con una previsión…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para Claude Code. agent-crew: observa trabajar a tus subagentes como un…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Matemáticas en LaTeX en línea y visibles, además de figuras TikZ opcionales, en…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Un panel de tareas en directo para Claude Code: planifica antes de construir…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod de Claude Code que informa en directo de qué archivos cambió Claude y por…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Banda siempre activa sobre el prompt de Claude Code: carga de contexto y…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Una colección cuidadosamente seleccionada de los mejores recursos para los…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Un plugin de Claude Code que muestra lo que está ocurriendo: uso del contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Línea de estado atractiva y altamente personalizable para Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas las partes del indicador de sistema de Claude Code, las descripciones de…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Más de 45 consejos para sacar el máximo partido a Claude Code, desde los…
- [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) - A terminal window manager that knows what your agents are doing.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline elegante al estilo de vim para Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revisa el diff de tu agente de programación en un panel de terminal y envía…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin de línea de estado completo para Claude Code con uso de contexto…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Seguimiento local de tokens de Claude Code y Codex — barra de estado.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crea modificaciones para Claude Code: intercepta cualquier solicitud, modifica…
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agente de rol de larga duración para DeepSeek Harness (plugin DSH Tavern)…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Habilidades y mods públicos de Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos de barra y guías para Claude Code…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Línea de estado de terminal para sesiones de Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Resultados, calendarios y clasificaciones de fútbol en vivo para la…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plano de control local para Claude Code en Windows y macOS: cambia los gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Habilidad de agente que convierte tu agente de programación en un experto en…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuración personal de Claude Code versionada dentro de ~/.claude — agentes…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horarios de oración, fecha Hijri, adhkar, ayah diaria, ayuno sunnah, Ramadan…
- [LikeACloud7/awesome-frontier-ai-papers](https://github.com/LikeACloud7/awesome-frontier-ai-papers) - Daily tracker for frontier AI lab papers, model cards, system cards, and…
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) - Tavily-powered optional search tool for DeepSeek Harness.
- [livlign/ccbit](https://github.com/livlign/ccbit) - Línea de estado consciente de las sesiones para Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DeepSeek Harness Research Graph · 研图 — Plugin de DeepSeek Harness para temas de…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Línea de estado truecolor de dos líneas para Claude Code.
- [William2333ZZ/mywork-deepseekharness](https://github.com/William2333ZZ/mywork-deepseekharness) - MyWork — a personal agent on DeepSeek Harness: AI teammates that each own a…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Colección de plugins para Claude Code, pi y DeepSeek Harness: HUD de barra de…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de herramientas de código Portable Claude para .NET DDD/Clean Architecture…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuración global portátil de Claude Code: skills personalizadas, hooks de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins de Claude Code que uso a diario: skills y mods, depurados para que…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram dentro de Claude Code: lee chats y canales en un panel y recibe…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama，适用于Claude Code的Tamagotchi伴侣mod.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins y skills de Claude Code para facilitar mods del juego…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Gobernanza de tokens para Claude Code: el modelo principal dirige y la…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Línea de estado en directo de la fase del flujo de trabajo para Claude Code…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods no oficiales para la pestaña Code de Claude Desktop — usage-pet: una banda…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositorio para mods Awesome Media de Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Reduce el gasto de Tokens de Claude Code y Codex: dirige las consultas y…
- [zhuravel/magnum](https://github.com/zhuravel/magnum) - Your AI coding agents as a pull-request review team: Claude Code, Codex and…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Configuración sencilla y útil de la línea de estado para Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Alertas de límites de uso para Claude Code: notificaciones de macOS…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Línea de estado configurable de Claude Code para Linux, WSL, Windows y macOS…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Línea de estado rápida de Rust Code para Claude Code — centrada en la carga…
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Línea de estado de Claude Code con barra de contexto, sparkline de tokens y…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Panel de uso en tiempo real para Claude Code — desglose del contexto, aciertos…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Una línea de estado y una línea de tokens para Claude Code: contexto, uso de 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Muestra detalles clave del estado de Claude Code, incluidos el modelo, el…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - la línea de estado amigable y llena de opciones para Claude Code — barras…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Línea de estado de Claude Code en varias filas: gasto, % de contexto, git y…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Línea de estado con información útil para claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipos de agentes nativos. Bajo control.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Línea de estado personalizada para Claude Code — barra de contexto con…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Una línea de estado limpia e informativa para Claude Code: muestra el proyecto…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod: a CRT-style status panel for Claude Code, in the terminal…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins de Claude Code con baloo: skills, un agente que verifica…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Línea de estado de Claude Code de nivel profesional: duración de sesión, coste…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Línea de estado de Claude Code consciente de la suscripción.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Una línea de estado de terminal completa para Claude Code — Bun + TypeScript…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin de Claude Code que muestra diagramas Mermaid de forma atractiva en la…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Herramientas, habilidades y agentes para Claude Code — empezando por una línea…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Línea de estado personalizada de Claude Code.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Plugin de Claude Code: consulta siempre el límite de uso restante de 5 horas de…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Gasto real de DeepSeek de API para Claude Code: vuelve a calcular el precio de…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Previsualiza imágenes dentro de Claude Code: pasa el cursor sobre una etiqueta…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods para Claude Code y Claude Desktop en Windows con WSL: Docker y rendimiento…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Línea de estado de Claude Code con filas del panel de agentes.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincroniza las tareas pendientes de Claude con Fizzy.do para que el equipo…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Una colección de habilidades, mods y otros complementos de Claude Code que he…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Muestra una barra de estado detallada y codificada por colores para Claude…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menú de ajustes, línea de estado y configuración de Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - plugins, habilidades, mods y más de claude, hechos en casa y sin jaulas.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalador del entorno de Claude Code: skills, barra de estado, hooks, permisos…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Línea de estado estilo HUD para Claude Code — estado de la red, TPS, contexto…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugins y mods de Claude Code para entender qué hace Claude: formatos de…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Supervisa el estado de Claude Code desde la barra de menús de macOS, con…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Barra de estado colorida de varias filas para Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Línea de estado de Claude Code para Windows (PowerShell): barras de uso…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings and Glossary para Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Configuración y mods de Claude Code, con un kit de componentes compartido, un…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuración portátil de Claude Code: CLAUDE.md, ajustes, línea de estado…
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Mod de Claude Code para escritorio (macOS): notificaciones de sesión con salto…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Supervisa el uso del contexto de Claude Code, los costes de la sesión y los…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Screen reader companion mod for Claude Code (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Una inmersión práctica y verificada en Claude Code — CLAUDE.md, subagents…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Seguimiento de costes en tiempo real y línea de estado de monitorización de…
- [wmkeza/claude-plugins](https://github.com/wmkeza/claude-plugins) - Plugins de Claude Code de wmkeza: habilidades cotidianas y un mod de línea de…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Línea de estado de tres líneas de Claude Code: profundidad del contexto…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - A Claude Code status line: folder, git branch, model, context window usage and…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de degradación del contexto 2026 - Monitor proactivo de memoria de IA…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes y líneas de estado de Claude Code: colecciones y herramientas…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Constructor visual para las líneas de estado de Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Línea de estado de Claude Code que muestra el uso de tokens en tiempo real y el…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: paneles, bandas y compañeros creados sobre hooks de…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pasa tareas entre tus sesiones de Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Esto en un servidor MCP para controlar MODS, la herramienta modular…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill de Codex y Claude Code para traducir mods de CK3 con un LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código abierto y otras extensiones para Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code状态行：CCometixLine美化效果+Claude HUD功能.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encuentra lo que pides a Claude Code una y otra vez y conviértelo en…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - 适用于Claude Code的prompt-bar mod：使用限额、缓存计时器+提醒、模型/effort选择器、侧边面板.

</details>

<a id="dsh-cordis"></a>

## Ecosistemas de complementos de DSH y Cordis

DeepSeek Harness y Cordis llegan al mismo punto desde direcciones diferentes: para ellos, el complemento es el mecanismo de mods, así que allí un complemento equivale a un mod aquí.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74319 · TypeScript · 👁️ observed · 0 天</summary>

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
| Estrellas         | **74319**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100481 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **100481** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐84715 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **84715**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81841 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **81841**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35758 · Go · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **35758**  |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25487 · Python · 🔎 inferred · 18 天</summary>

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
| Estrellas         | **25487**  |
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
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8620 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **8620**   |
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
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐7828 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

技能Skills商店：收录最全、更新最快，精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流等），全部打包好，可直接安装使用！同时自动抓取GitHub上万个Skills项目，并按分类、更新时间、Star数量整理。最全面、更新最频繁的AI Agent技能库，精选涵盖文档处理、内容创作、编程、机器学习、自动化工作流等众多领域的技能包。

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | Python                                                                            |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **7828**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

<sub>Recurso enlazado directamente desde el repositorio original porque no se declaró una licencia compatible con la redistribución.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6133 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | TypeScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **6133**   |
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
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4466 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **4466**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4280 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **4280**   |
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
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

The World's First Virtual Terminal for AI Agents

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
| Primera inclusión | 2026-10-11 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1978 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1978**   |
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
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1801 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Conecta bots de IM a DeepSeek Harness mediante código QR o credenciales de bot (compatible con Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord y WhatsApp). Conecta bots de IM a DeepSeek Harness mediante código QR o credenciales (9 canales).

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **1801**   |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1398 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1398**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **1169**   |
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
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐365 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **365**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

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

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

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
| Primera inclusión | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **133**    |
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
<summary>🧵 <b><a href="https://github.com/mexiaosqwq/dsh-web-mobile">mexiaosqwq/dsh-web-mobile</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DSH Web UI移动端适配：窄屏好用，宽屏适用

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **132**    |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-ui` · `plugin` · `responsive` · `web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mexiaosqwq--dsh-web-mobile/0edd0e3313404adf.jpg" width="100%" alt="mexiaosqwq/dsh-web-mobile screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐130 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **130**    |
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
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DeepSeek Harness 桌宠插件：元气鲸鱼娘看板娘陪你写代码 🐋 支持 DSH 桌面端 0.2.0-rc.2 与旧版 Web（desktop pet / mascot，local-first）

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
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐58 · HTML · 🔎 inferred · 0 天</summary>

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
| Estrellas         | **58**     |
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

DeepSeek Harness 插件：维护 llm-pi-ai 模型的准确上下文窗口，避免长会话被误判为上下文溢出。

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
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Resumen

DSH 会话导航

##### 📌 Datos básicos

| Campo     | Valor                                                                             |
| --------- | --------------------------------------------------------------------------------- |
| Categoría | `Ecosistemas de complementos de DSH y Cordis`                                     |
| Evidencia | `declara un mod, plugin o hook, pero nada específico sobre la superficie de mods` |
| Lenguaje  | JavaScript                                                                        |

##### 📊 Datos

| Métrica           | Valor      |
| ----------------- | ---------- |
| Estrellas         | **23**     |
| Último envío      | 2026-10-11 |
| Primera inclusión | 2026-10-11 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Imagen</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>no se han publicado archivos multimedia</sub></td>
</tr></table>

</details>

<details>
<summary><b>Más en esta categoría</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Una lista seleccionada de los mejores plugins de IA para asistentes de IA…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins de DSH / DSH Plugin Marketplace: explora, instala y…
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - 把DSH Web状态行换成1063条梗：打字机+炫彩渐变+弹幕+12个主题词库包，设置页可视化编辑.
- [arcships/rutis](https://github.com/arcships/rutis) - A plugin runtime for software that iterates on itself — the substrate where…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [1475505/miliastra-beyond-simulator](https://github.com/1475505/miliastra-beyond-simulator) - 千星沙箱模拟器：Lua 驱动的 2D 奇域外置沙箱 ，支持 DeepSeek Harness、Web 和 MCP.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Directorio seleccionado de plugins de DeepSeek Harness (DSH): más de 280…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Kit de herramientas de Zotero para DeepSeek;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin de DSH: shell Git Bash para todos los modos de agente en Windows…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - 办公三件套！Office document tools for DeepSeek Harness (dsh): generate, read, and…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Banco de trabajo de escritura local para autores de novelas web en chino.
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh安卓版：集成DeepSeek Harness、Ubuntu运行环境、插件与文件管理，以及用户授权的Shizuku和无障碍自动化.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin web de DSH: estadísticas diarias de uso de tokens con un mapa de calor…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, herramientas, skills y recursos de aprendizaje de DeepSeek Harness…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin gestor de servidor MCP para DeepSeek Harness: página Settings → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Plugin de DeepSeek Harness: 15 habilidades de ingeniería de obra/superpowers…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de negociación comercial A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - Interfaz de gestión del servidor MCP para DeepSeek Harness Web — panel…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Un PowerPoint real, no HTML. Dile a tu IA qué debe incluir y pptwise creará una…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 给大肥鱼一个小说工作台：一起写正文、讨论后续情节、整理人物与世界设定，让长篇创作更贴近你的想法.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 插件 · 发送栏一键「优化」提示词草稿：五维诊断 + 改写稿 SSE 流式上屏，可替换 / 复制 /…
- [rezon-aki/dsh-streamfold](https://github.com/rezon-aki/dsh-streamfold) - 流式折叠：一个更好的 DSH 会话窗口——运行中自动展开最新思考小窗，其余过程行折成短摘要；跑完自动折起、穿插正文保留；收起/展开按 3…
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - Plugin de DeepSeek Harness: modo senior perezoso y port de escalera de 7…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Login gate for the DeepSeek Harness (dsh) web surface: password or shared-token…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 嵌入式C/C++ AI工程插件——固件技能（FreeRTOS、Keil、HardFault、状态机）+ 1% Rule / Plan Verification…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Convierte los modelos con sesión iniciada en el escritorio local de WorkBuddy…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Gestor integral de skills, subagent, MCP y LSP para DeepSeek Harness (DSH)…
- [xxww0098/dsh-plugin-oauth-subs](https://github.com/xxww0098/dsh-plugin-oauth-subs) - ChatGPT Codex and xAI Grok subscription OAuth for DeepSeek Harness — PKCE /…
- [muyuanjin/dsh-ptc-plus](https://github.com/muyuanjin/dsh-ptc-plus) - A session-bound agent-native REPL for DeepSeek Harness PTC mode.
- [white0dew/awesome-dsh-plugins](https://github.com/white0dew/awesome-dsh-plugins) - Awesome DSH Plugins: a public GitHub directory for DeepSeek Harness plugins…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pruebas de compatibilidad siempre activas para plugins de DeepSeek Harness…
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - Repair DeepSeek Harness sessions that refuse to load. 修好打不开的 DSH 会话文件.
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - DeepSeek Harness（DSH）的零成本、零麻烦工具包：一键设置四种永久免费的模型.
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - A curated list of plugins, tools, skins, and extensions for DeepSeek Harness…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host de DeepSeek Harness que mantiene los documentos del proyecto y la…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Rayos X para plugins de DeepSeek Harness: capacidades declaradas frente a…
- [Bcy2020/dsh-cc-ecosystem](https://github.com/Bcy2020/dsh-cc-ecosystem) - 让 DeepSeek Harness 用上 Claude Code 全家桶:技能、命令、规则、权限、子代理、hooks—— .claude/ 资产原样加载.
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - 让 DSH 回答变成可操作的界面：计算、图表、表单、模拟与小游戏。独立 DSH 插件 ｜ Interactive answers for DeepSeek…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: una ventana de herramientas Git de nivel IDE como pestaña nativa de…
- [NoneadChina/dsh-nonead-universal-robots](https://github.com/NoneadChina/dsh-nonead-universal-robots) - A plugin enabling DSH to directly control Universal Robots (UR) arms using…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - 设计与代码的声称核验：事实类对照源码，行为类跑可执行模型；含结构/依赖审查（单层与多粒度细化）、UML 审查、基线对比与导出.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Espacio de trabajo con varias carpetas: permite que el agente de DSH.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plugin de flujo de trabajo de ingeniería para DeepSeek Harness: etapas de…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Estándar de verificación sin dependencias para plugins de DeepSeek Harness…
- [Small-tailqwq/dsh-internet-angel-desktop](https://github.com/Small-tailqwq/dsh-internet-angel-desktop) - 一款基于主播女孩重度依赖创建的 适用于 DSH 的 实验性主题皮肤 / Unofficial pixel desktop skin for DSH Web…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode en DeepSeek Harness — plugin de DSH que mantiene funcionando OpenCode…
- [xiaoso456/dsh-workflow-lite](https://github.com/xiaoso456/dsh-workflow-lite) - DeepSeek Harness 的软工作流插件：在画布上设计流程，编译成计划提示词，由模型按计划执行；运行状态由模型自己记，没有执行引擎.
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — mercado de plugins de terceros y gestor de ciclo de vida protegido…
- [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) - Consulta archivos de registro locales con expresiones temporales en lenguaje…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx es un espacio de trabajo de escritorio ampliable y centrado en las…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Un agente de programación con todo incluido para DeepSeek Harness — flujos de…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Plugin de experiencia de entrada web de DSH: alternancia de teclas para…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Proporciona a la edición de escritorio de DeepSeek Harness un punto de acceso…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — suite comunitaria de instalación, despliegue y operaciones locales…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web de DeepSeek Harness (DSH): pestaña lateral market-dashboard para…
- [Wenston-dev/awesome-dsh-plugin](https://github.com/Wenston-dev/awesome-dsh-plugin) - Awesome dsh plugin list — automated DeepSeek Harness plugin directory.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin de DeepSeek Harness: convierte el fallo de aprovisionamiento de ACL del…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Permite volver a intentar un intento vacío de modelo sin atribución, para la…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins que se limpian solos: un port de Swift 6 del framework de plugins…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset de agente DeepSeek Harness: Codex y Claude Code como subagentes de…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Un runtime de plugins de Rust con un kernel de ciclo de vida verificado por…

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

| Lenguaje   | Entradas | Ejemplos                                                                                                    |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| TypeScript | 379      | `anthropics/claude-code`, `hamzafer/claude-code-mods`, `karanb192/cache-tax`                                |
| JavaScript | 85       | `X-C1811/dsh-web-search-plugin`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`         |
| Python     | 37       | `kuangre123/codex-switch`, `alexgreensh/token-optimizer`, `AgriciDaniel/claude-mods-brain`                  |
| Shell      | 21       | `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`, `andrewbakercloudscale/claude-code-cost-sidebar` |
| HTML       | 10       | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                          |
| Go         | 8        | `cephalofoil/kitt`, `Gaurav-Gosain/tuios`, `kylesnowschwartz/tail-claude-hud`                               |
| Rust       | 5        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`           |
| PowerShell | 2        | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                         |
| Swift      | 2        | `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`                                     |
| C          | 1        | `reporails/arcade`                                                                                          |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                     |
| Kotlin     | 1        | `dphmoblie/deepseek-harness-android`                                                                        |
| MDX        | 1        | `jkf87/mod-guide`                                                                                           |

<sub>Solo se contabilizan las entradas que declaran un idioma. Las entradas de documentación y debate se excluyen de esta tabla.</sub>

## Contribuir

Las correcciones son bienvenidas y son la forma más rápida de mejorar esta lista. Abre un issue o una pull request si una entrada está mal clasificada, tiene una categoría incorrecta o si un proyecto se ha excluido por error debido a una coincidencia de nombres; esta última categoría es donde más probablemente fallen los filtros automatizados.

---

<sub>Proyecto independiente de la comunidad. No está afiliado a Anthropic, ni cuenta con su respaldo o revisión. Claude Code, Claude y Anthropic son marcas comerciales de Anthropic. El comportamiento del producto puede cambiar sin previo aviso; verifica cualquier aspecto esencial en la documentación oficial. Los recursos siguen siendo propiedad de sus proyectos de origen y se reproducen únicamente cuando una licencia lo permite.</sub>

<sub>Última actualización · 2026-10-11T19:01:04+08:00</sub>
