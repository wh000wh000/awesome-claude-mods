<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Отличные моды для Claude">
</p>

<h1 align="center">Отличные моды для Claude</h1>

<p align="center"><b>Индекс модов, плагинов Claude Code и более глубоких изменений поведения, составленный с оценкой доказательности.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-585-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <b>Русский</b> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Актуальный индекс** · Последняя синхронизация: `2026-10-13T06:19:35+08:00` (UTC+8)
> · Записей: **585** · Добавлено в последнем обновлении: **0** · Языки реализации: **12**

<sub>Каждая запись ниже была автоматически собрана, отфильтрована и проверена повторно. Здесь нет платных размещений.</sub>

<a id="featured"></a>

## Лучшее на данный момент

<sub>По одной записи на категорию, ранжирование по степени подтверждённости и количеству звёзд, пересчитывается при каждом обновлении. Это рейтинг, а не рекомендация; каждая подборка ведёт к полной карточке ниже. Предпочтение отдаётся проектам, опубликовавшим снимок экрана или запись, чтобы лента оставалась визуальной.</sub>

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
<sub>🌊 Оригинальный agent harness. Разворачивайте интеллектуальные многопользовательские рои, координируйте автономные рабочие процессы и создавайте разговорные…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Содержание

- [Что такое мод Claude Code](#что-такое-мод-claude-code)
- [Как оцениваются записи](#как-оцениваются-записи)
- [Официальные: собственные репозитории и примечания к выпускам Anthropic](#официальные-собственные-репозитории-и-примечания-к-выпускам-anthropic) — **17**
- [Моды: созданы с использованием возможности модификации](#моды-созданы-с-использованием-возможности-модификации) — **451**
- [Экосистемы плагинов DSH и Cordis](#экосистемы-плагинов-dsh-и-cordis) — **106**
- [Тексты, обсуждения и видео](#тексты-обсуждения-и-видео) — **11**
- [Проекты по языку реализации](#проекты-по-языку-реализации)

## Что такое мод Claude Code

Claude Code получил **моды** в версии 2.1.287: расширения, которые могут менять поведение глубже, чем мог плагин, и рисовать собственный интерфейс.

Мод может подключиться к `ui.render`, чтобы нарисовать **строку, полосу, панель или карточку** вокруг промпта, читать текст, который вы последний раз выделили, через `$.ui.selection()`, запускать напарников через `agent.spawn` и владеть областью `Client`. Мод, которому не удалось отрисоваться, падает в одиночку — `ui.fault` не дает одному сломанному моду обрушить сеанс.

Этот список охватывает моды, поверхность плагинов и хуков, на которой они строятся, а также эквиваленты DSH и Cordis. Он намеренно **не** охватывает более широкую экосистему Claude Code: набор промптов — не мод.

## Как оцениваются записи

Большинство списков в этой области просто заявляют включение. Этот показывает, насколько всё было реально проверено, а затем позволяет фильтровать соответственно. Оценка описывает доказательства, а не качество проекта — хорошо сделанный мод, о котором еще никто не написал, все равно остается `inferred`.

| Оценка                                                                    | Что это означает                                                                                                                                                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `опубликовано самим Anthropic`                                            | Опубликовано самим Anthropic или взято напрямую из официального changelog.                                                                                                                                    |
| `в собственном тексте упоминается мод API или заявляется поддержка модов` | В собственном тексте упоминается часть поверхности модов — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, панель, полоса или карточка, — значит, автор описывает то, что строил на реальном API. |
| `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов`    | Называет себя модом, плагином или хуком, но в тексте нет конкретного упоминания поверхности модов. Реально, но не подтверждено.                                                                               |
| `совпало только по лексике`                                               | Совпало только по лексике. Включено, чтобы фильтр можно было проверить, а не потому, что этому доверяют.                                                                                                      |

<a id="official"></a>

## Официальные: собственные репозитории и примечания к выпускам Anthropic

Anthropic's own Claude Code repositories, and the releases that defined the mod surface. Read from the source rather than summarised.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150420 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Сводка

Claude Code — агентский инструмент для программирования, работающий в терминале, понимающий вашу кодовую базу и помогающий программировать быстрее: он выполняет рутинные задачи, объясняет сложный код и обрабатывает рабочие процессы git — всё с помощью команд на естественном языке.

<sub>🔧 Найдено использование в коде: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |
| Язык          | TypeScript                                                               |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **150420** |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9486 · TypeScript · ✅ official · 3 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |
| Язык          | TypeScript                                                               |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **9486**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8255 · Python · ✅ official · 3 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |
| Язык          | Python                                                                   |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **8255**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6354 · Python · ✅ official · 243 天</summary>

##### 📝 Сводка

Действие проверки безопасности с использованием ИИ GitHub, применяющее Claude для анализа изменений кода на наличие уязвимостей безопасности.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |
| Язык          | Python                                                                   |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6354**   |
| Последний push   | 2026-02-11 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1800 · Shell · ✅ official · 3 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |
| Язык          | Shell                                                                    |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1800**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

##### 📝 Сводка

Дополнительные материалы для Claude Model Cards

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **25**     |
| Последний push   | 2025-12-05 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Сводка

Добавлены моды Claude: теперь плагины могут изменять более глубокие уровни поведения. Добавлен You should know — встроенный мод, в котором боковой агент прикрывает вас и отмечает то, что вы или Claude могли бы пропустить. Включите его с помощью `/plugin enable cc-plugin-you-should-know@builtin` (для сторонних сессий с включённой телеметрией)

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Сводка

Добавлен `$.ui.selection()` для модов: возвращает последний выбранный текст в полноэкранном режиме, а если выделение находится в пределах одной строки транскрипции — эту строку. Исправлено: кнопка мода иногда выполняла действие другой кнопки при нажатии на представлении, отрисованном до перезапуска Claude Code. Исправлено: полноэкранные сессии завершались с ошибкой "unrecoverable interface error" при открытии диалога фоновых задач, если плагин или мод отображал строки над приглашением. Исправлено: `claude plugin test` сообщал, что моды удалённо отключены, хотя всего лишь прочитал устаревшую сохранённую настройку

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Сводка

Исправлено: правило deny или ask для вложенной части составной команды shell не сохранялось после подтверждения пользовательского мода на управляемых машинах. Исправлено: установленные моды не загружались в первой сессии после обновления. Добавлен `agent.spawn` для товарищей по команде, единый идентификатор агента для событий хуков плагинов, а также состояния бездействия и ожидания в `$.agent.list()`. Исправлено: сессии завершались с ошибкой "unrecoverable interface error", когда значение, записанное хуком `ui.render` мода, вызывало сбой строки при отрисовке; теперь движок отрисовывает собственную строку. Исправлено: содержимое, выровненное по правому краю в панели или полосе мода, отображалось под значком закрытия или `\[-\]`, wh

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Сводка

Добавлено `serverToolUses` в результат хука `turn.step` мода: инструмент вызывает API, который сам выполнял запуск (советник), для каждого указываются его идентификатор, имя, входные данные, начало и конец. Добавлено `ceiling` в вопрос и вердикт, которые читает хук `tool.check` мода, с указанием одобрения, требуемого организацией для инструмента. Добавлены типы `ThemeKey` и `Color` в типизацию хуков плагина, чтобы редактор отображал цвета темы, которые может указать отрисовка мода. Добавлено в `claude plugin validate`: каждый хук, зарегистрированный модом в точке контроля, отображается с указанием наличия `.catch` (`gatingHooks` в `--json`). Исправлен результат `turn.step` мода

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Сводка

Добавлен `prompt.autocomplete`, событие, к которому мод подключается, чтобы добавлять свои строки в список автодополнения поля промпта. Добавлено кэширование промптов в `$.model.complete` для модов: `prompt` и `system` принимают блоки текста, а `cache: true` на блоке кэширует запрос до него. Добавлены workflow-агенты в хук мода `agent.spawn`, с их запуском и индексом, чтобы мод мог их отклонять. Исправлены строки Write, Edit, NotebookEdit и LSP, а также одиночные строки Read, Grep и Glob, скрывавшие, почему мод отклонил вызов: теперь строка показывает причину. Исправлен хук мода `config.set`, `state.set`, `env.set` или `agent.spawn`, который отклоняет afte

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Сводка

Добавлен `isDeferred` в `$.tool.register` для модов: `false` с самого начала перечисляет схему инструмента в запросе, а не скрывает её за поиском инструментов. Исправлено пропускание hook-ов мода на событиях `classic.*` при перезапуске worker-а hook-ов плагина, из-за чего hook-и настроек отвечали без них. Исправлено падение `claude plugin test` для модов, вызывающих `$.session.append`; тесты могут прочитать добавленные строки обратно с помощью нового `mock.session`

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Консоль управления MCP для официального клиента MCP DeepSeek Harness: команда /mcp с диагностикой работоспособности и пробными вызовами конвейера, вкладка «Настройки» MCP с CRUD-операциями серверов (изменения требуют подтверждения, автоматические резервные копии) и консолью пробных вызовов инструментов через официальный конвейер инструментов (Apache-2.0, dsh-plugin).

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов`   |
| Язык          | TypeScript                                                               |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **74**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/fschmutz/claude-usage-panel">fschmutz/claude-usage-panel</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

See your Claude Code plan usage everywhere: GNOME top bar, macOS menu bar, a status line under the Claude Code prompt, and a get_usage MCP tool for Claude Code + Cursor. Session, weekly & per-model (Fable/Opus) limits from the official usage API, with burn-rate forecasts. One-line install, self-updating.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов`   |
| Язык          | JavaScript                                                               |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6**      |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `anthropic` · `ccusage` · `claude` · `claude-code` · `cursor` · `developer-tools` · `gnome` · `gnome-extension`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fschmutz--claude-usage-panel/40b54f8d52b03345.png" width="100%" alt="fschmutz/claude-usage-panel screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-ticktick">PerryLink/dsh-ticktick</a></b> · ⭐4 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Мост задач TickTick (Dida365) для DeepSeek Harness: панель задач в заголовке сессии (фильтр списка, представления невыполненных/завершённых задач, поиск, перетаскивание для изменения порядка), 11 отобранных инструментов агентов, карточка настроек, через официальный эндпоинт TickTick MCP.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов`   |
| Язык          | TypeScript                                                               |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **4**      |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dida365` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/aa581021cb97f4dd.png" width="100%" alt="PerryLink/dsh-ticktick screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/44088595da097cb2.gif" width="100%" alt="PerryLink/dsh-ticktick animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Добавлен `$.ui.notify` для модов: вызывает нативное уведомление через ваши…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Исправлена ситуация, когда Esc или прерывание во время хука `UserPromptSubmit`…

</details>

<a id="mods"></a>

## Моды: созданы с использованием возможности модификации

Каждая запись здесь демонстрирует использование возможности, которую Claude Code получил в версии 2.1.287: она выполняет отрисовку через `ui.render`, владеет панелью, полосой или карточкой, читает `$.ui.selection()`, создаёт товарищей с помощью `agent.spawn` или прямо указывает, что является модом.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2543 · Python · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | Python                                                                    |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2543**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>анимированная запись</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐530 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Каталог сообщества публичных модификаций Claude Code (функциональных хуков), просканированных из GitHub, с указанием того, что каждая модификация может читать, записывать, запускать или отправлять по сети. Просмотреть https://mods.aidojo.si/

<sub>🔧 Найдено использование в коде: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **530**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐210 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Сводка

Моды Claude Code: плагины на основе хуков, добавляющие над приглашением строки в реальном времени, защиты, панели и игры. Панель контекста, счётчик использования, отслеживание проверки Codex, предпросмотр Markdown, текущая композиция Spotify и многое другое.

<sub>🔧 Найдено использование в коде: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **210**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐161 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Поддерживайте кэш промпта Claude Code прогретым во время перерывов и показывайте примерную стоимость перед отправкой после простоя.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **161**    |
| Последний push   | 2026-10-04 |
| Впервые в списке | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>анимированная запись · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Открыть видео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐117 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Скины для Claude Code: строки инструментов со значками, карточки diff, таблиц и диаграмм Mermaid, индикатор использования и пятнадцать тем. /skin применяет их в реальном времени.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **117**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Красочные ответы Claude Code с поддержкой тем: таблицы, код, диаграммы, графики и строки инструментов в 15 темах, с кнопками копирования. Мод для Claude Code.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **88**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Сводка

Коллекция модов claude code

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **78**     |
| Последний push   | 2026-10-08 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Модификация кода Claude, которая добавляет в ваш терминал интерактивную панель агента: контекст и стоимость, временная шкала советника, каждая проверка разрешений, карточки субагентов и дорожки.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **75**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

##### 📝 Сводка

Моды Claude Code от Darrell Wang — полосы над приглашением, ноль токенов модели. Панель тайваньских／американских акций + новые возможности в будущем.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | HTML                                                                      |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **65**     |
| Последний push   | 2026-10-05 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Сводка

Экспертные skills, агенты, команды, правила, хуки и стили вывода для Claude Code — непрерывность сессий + современные инструменты CLI для реальных рабочих процессов разработки

<sub>🔧 Найдено использование в коде: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | Shell                                                                     |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **62**     |
| Последний push   | 2026-10-07 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐55 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Сводка

Коллекция из более чем 100 модов, которые можно использовать с Claude Code.

<sub>🔧 Найдено использование в коде: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **55**     |
| Последний push   | 2026-10-03 |
| Впервые в списке | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Сводка

Моды Claude Code: индикаторы прогресса плана в реальном времени над приглашением

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **47**     |
| Последний push   | 2026-10-08 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>анимированная запись · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Открыть видео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Сводка

Наблюдайте, как Claude Code создаёт небольшой мультфильм во время работы.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **32**     |
| Последний push   | 2026-10-02 |
| Впервые в списке | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Сводка

Панель промптов вашей сессии Claude Code: наведите курсор для чтения, нажмите для перехода (функциональные хуки / Mods)

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **28**     |
| Последний push   | 2026-10-03 |
| Впервые в списке | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐26 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Преображение для Claude Code: интерактивная панель управления, темы для обмена и пиксельный питомец, который показывает, чем занимается Claude

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **26**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Пиксельный Pokémon, живущий над приглашением в Claude Code

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **25**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>анимированная запись</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Сводка

Сборка, тесты, консоль и предпросмотры SwiftUI из Xcode внутри Claude Code

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **20**     |
| Последний push   | 2026-10-02 |
| Впервые в списке | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Моды Claude Code: 21 стиль и полный набор функций, которые можно включать по необходимости, для терминала и настольного приложения. · Одним нажатием придайте Claude новый стиль и получите полный набор функций, включаемых по необходимости.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **20**     |
| Последний push   | 2026-10-04 |
| Впервые в списке | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 Сводка

Десять модов Claude Code, руководства для начинающих, подсказки для создания, безопасные демонстрации и шаблон для самостоятельной сборки.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **20**     |
| Последний push   | 2026-10-02 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Мод для Claude Code: предварительный просмотр вставленных изображений и длинного вставленного текста над приглашением

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **19**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐17 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Мод для Claude Code: Clawd изображает действия Claude над приглашением

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **17**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Сводка

Два мода Claude Code: мост Codex для управления компьютером и скоординированные сессии Claude. Исходный код, подсказки для сборки, настройка и тесты.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **16**     |
| Последний push   | 2026-10-05 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Сводка

Моды Claude Code: usage-band показывает ограничения 5h/7d, окно контекста и долю попаданий в кэш над приглашением

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **13**     |
| Последний push   | 2026-10-03 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 Сводка

Моды Claude Code, упрощающие чтение и ответы на вопросы Claude (qa-guide).

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **12**     |
| Последний push   | 2026-10-07 |
| Впервые в списке | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>анимированная запись · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Открыть видео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Сводка

Мод для Claude Code: контекст в токенах, 5-часовые и недельные лимиты относительно времени, обратный отсчёт кэша промпта, стоимость сессии и работающие агенты — в одной полосе над промптом.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **12**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Сводка

Десять модов с открытым исходным кодом для Claude Code: динамические панели, полосы, строки состояния и защиты вызовов инструментов. Индикатор расхода, коды запуска, завершение сессии, битва с боссом, питомец-код и многое другое.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **12**     |
| Последний push   | 2026-10-03 |
| Впервые в списке | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Анимированная пиксельная графика над промптом Claude Code, реагирующая во время работы Claude. Семь сцен или ваше собственное изображение либо GIF. Ноль токенов.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **10**     |
| Последний push   | 2026-10-04 |
| Впервые в списке | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

##### 📝 Сводка

Трекеры сессий для Claude Code, созданные как моды: окно контекста, скорость расходования квоты плана, стоимость каждого хода

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **9**      |
| Последний push   | 2026-09-15 |
| Впервые в списке | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>анимированная запись</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Интерфейс для ваших терминалов Claude Code и Codex, который создают ваши агенты, поэтому единственная модель в вашей голове — ваша собственная.

<sub>🔧 Найдено использование в коде: `CLAUDE.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **9**      |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Сводка

KOZMOS — интерактивные визуальные моды для Claude Code (CLI + desktop): полосы над приглашением, боковые панели, бегущая строка состояния, компаньоны, защитники и звук.

<sub>🔧 Найдено использование в коде: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **9**      |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Сводка

Продлите действие плана Claude Pro: моды Claude Code для точного HUD использования, сокращённого вывода shell и отсутствия повторного чтения файлов. Моды не расходуют токены.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **9**      |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Шесть модов Claude Code в одном плагине (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) с отдельными переключателями для каждого мода, а также отчёт о различиях между модами и хуками.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **8**      |
| Последний push   | 2026-10-04 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Коллекция модов Claude Code от 개발동생. Пакет такси: счётчик, навигатор, камеры контроля скорости, видеорегистратор

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **8**      |
| Последний push   | 2026-10-04 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Смотреть на youtube.com</a> · воспроизведение открывается на сайте-источнике; GitHub не может встроить его в страницу</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Ваш план, наблюдающий за собой. Локальное дерево дорожной карты рабочего стола, которое Claude Code и любой хост MCP поддерживают в актуальном состоянии в реальном времени. Простой JSON, без облака.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **8**      |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 417</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Модификации Claude и инструменты для их создания: сначала навык-сборщик, затем…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Среда Claude Code, которую я запускаю каждый день, публикуемая под этим именем…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Моды Claude Code от Ray Amjad: панели, полосы, защита приглашений, работа с…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Наденьте новую крышу на Claude Code с помощью Claude Mods: не изменяя бинарный…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Четыре мода Claude Code: Cache Keeper, Recording Mode, Goal Meter и Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Моды Claude Code от Learning Hacker: сделайте работу агента понятной для…
- [kakha13/claude](https://github.com/kakha13/claude) - Моды Claude Code, исправляющие и переводящие ваши подсказки до того, как их…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - База знаний Obsidian с указанием источников о модах Claude Code: как они…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Моды и навыки Claude Code от Nekyia Labs, создаваемые и ежедневно используемые…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Панель управления для Claude Code: динамические полосы планов, ленты…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Модификация, придающая терминальному журналу Claude Code вид настольного…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Боковая панель для кода Claude: субагенты, запускаемые сессией, выполняемая…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Моды Claude Code: меню инструментов Claude, режим Zen, темы терминала, элементы…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Панель боковой панели Claude Desktop (вкладка Code): перечисляет все…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Полоса использования над полем ввода Claude Desktop (вкладка Code): лимиты 5h /…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Навык, обучающий агентов Claude Code создавать Claude Mods.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Пользовательские моды, плагины и навыки Claude, устанавливаемые из одного…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (плагины с перехватчиками функций) для Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Галерея модов Baselane: моды Claude Code, проверенные и закреплённые.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Очередь решений CLI/TUI для людей, работающих с разговорными агентами.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Мод Claude Code, отображающий различия Edit и Write в двух расположенных рядом…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, отрисовываемый в поле приглашения Claude Code по мере ввода.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Моды Claude Code: панель использования 像素螃蟹 usage-hud + HTML-ссылки, по которым…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плавающая карточка состояния для Claude Code — модель, контекст, ограничения…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Моды для Claude Code: плагины с функциональными хуками, добавляющие…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Моды Claude Code: screen-guard маскирует имена и секреты во время демонстрации…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Модификации и скины для Claude Code: индикатор выполнения задач Claude в…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Расширения Claude Code. Раскройте всю мощь Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Мод Claude Code (плагин), который добавляет боковую панель с вкладками…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Панели, защитные механизмы и полезные моды для Claude Code: контекст…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Два мода Claude Code над полем приглашения: измеритель контекстного окна…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Чтение markdown-файлов, которым код Claude даёт имена, с отображением рядом с…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude готовит. Общайтесь со своей командой.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Тест скорости печати на время, пока работает Claude.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Мод Claude Code: миниатюры вставленных изображений над приглашением в любом…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Голосовой напарник для Claude Code. Обсуждайте задачи с 3D-волком на базе…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow для Claude Code: спокойный список над полем запроса, показывающий…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Моды Claude Code: панель контекста, панель агентов, размытие PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Моды Claude Code: typing-speed, спидометр скорости печати в реальном времени со…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Фейерверки для Claude Code: каждое нажатие клавиши, вызов инструмента, коммит и…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Моды для Claude Code: панели, команды и хуки, созданные с помощью плагина…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Находите моды, плагины и расширения Claude Code с анимированными…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Мод Claude Code: диаграммы mermaid, встроенно отображаемые в расшифровке.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Небольшие моды Claude Code (плагины с перехватчиками функций): session-switcher…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Шесть модификаций Claude Code: ограничения плана и контекст над полем запроса…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Моды Claude Code: mod-scout (поиск наиболее нужных вам модов), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Два мода Claude Code для одновременного запуска множества сеансов: карточка…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Моды Claude Code по запросу — навык, который читает ваш разговор и создаёт…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: поиск, просмотр, переключение и обновление модов Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Лучшие моды Claude Code: отобранные вручную, проверенные, закреплённые.
- [davekiss/mods](https://github.com/davekiss/mods) - Моды Claude Code от Dave Kiss.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Плагин Claude Code: автоматическая маршрутизация моделей Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Мод для Claude Code: интерактивная панель с GitHub PR, которые открывает или…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Шесть модов для Claude Code: анимированный маскот Clawd, индикаторы лимита…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Магазин приложений для модов Claude Code внутри Claude Code: используйте /mods…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Маркетплейс модов для Claude Code: пошаговый отладчик цикла агента, подсказки…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Моды с открытым исходным кодом для Claude Code: панели, строки состояния…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Лучший универсальный набор модов для Claude Code: лимиты использования и HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Смотрите YouTube Shorts в своём Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набор инструментов Naren для Claude: skills, mods и MCP servers для Claude…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Моды для Claude Code: Clawd, крошечный пиксельный талисман, который показывает…
- [reporails/arcade](https://github.com/reporails/arcade) - Классические компьютерные игры в виде модов Claude Code, в которые можно играть…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods для claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Собственный маркетплейс модов-плагинов для Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Кураторский список модификаций Claude Code, устанавливаемых как через…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Два Claude Code-мода: cache-keeper и ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Крайне авторский плагин Claude Code, созданный любителем Rust, одержимым…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Моды Claude Code, которые помогают агенту не отклоняться от цели — перехватчики…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Fresh from the factory. A Claude Code mod: ask for a meme, keep working.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Мод для Claude Code: панель кэша промптов, следующие шаги, быстрые кнопки и…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Мод Claude Code, отображающий ваши лимиты использования и расходы в полосе над…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Мод для Claude Code для записи мыслей в процессе работы, их сортировки по…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Статус PR GitHub в реальном времени, готовность к слиянию, проверки…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моды Claude Code от Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Моды для Claude Code: индикаторы выполнения планов, журнал того, что Claude…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Полевые заметки первого дня о модах Claude Code на Windows: топливная шкала…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: отладчик вызовов инструментов Code для Claude.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Мод Claude Code: динамический статус запроса на слияние GitHub.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Небольшие карточки, расположенные под запросом Claude Code или закреплённые…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живые индикаторы стоимости, контекста и квоты плана над…
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 Мы создаём немного TECHNO, детка 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Плагин и мод Claude Code: AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Мод Claude Code, который включает и отключает глобальные навыки, агентов…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Протестированные Claude Code-моды, устанавливаемые одной командой: защитные…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Уютный мод RPG-интерфейса для Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Набор модов для claude code, созданных мной.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Моды Claude Code: панель управления флотом агентов и автопилот.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Моды Claude Code. touch-map: просматривайте в виде дерева и карты активности…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Учите иностранный язык во время работы с Claude Code.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Мод Claude Code, который сообщает, какие файлы изменил Claude и почему…
- [0xctx/sysop](https://github.com/0xctx/sysop) - Скажите Claude, чего вы хотите. В ответ вы получите результат, собранный…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Следит за долгой сессией Claude Code, чтобы вам не пришлось: отслеживает…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - Мод Claude Code, который поддерживает кэш приглашений в актуальном состоянии…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Боковая панель с данными о текущих расходах, токенах и использовании контекста…
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - Моды ayagmar для Claude Code: маркетплейс плагинов.
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Моды с функциональными хуками для Claude Code: строка телеметрии лимитов…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моды Claude Code для настоящих инженеров.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Резюме терминальной сессии Claude Code во вкладке Code настольного приложения…
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Мод Claude Code: панель с задачей сеанса, тем, что требует вашего внимания…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Code-мод для Claude: ловите пиксельных Modsters в игре в режиме ожидания, пока…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Посмотрите, какие файлы есть в контексте каждого агента Claude Code и какая…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Небольшие моды Claude Code для терминала и настольного приложения.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навык + мод Claude CLI, добавляющий испанские слова в ответы агента.
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Мод Claude Code, который избавляет от повторной записи кэша промптов: /keepwarm…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - События Alarum над промптом Claude Code: что только что поступило и передача…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Ваш список задач Floatee над промптом Claude Code: запускайте, направляйте и…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Мод Claude Code, который стилизует его под The Machine из Person of Interest.
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Мод для Claude Code (мод CC tint): окрашивает каждое окно в цвет его…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Мод Claude Code: статус сессии, живой прогресс Spec Kit и управление окном…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Окно контекста в виде строки над запросом, отображаемое так же, как Claude Code…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: интерактивный граф того, что знает Claude Code.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Интерактивный HUD задач для Claude Code Desktop: полоса над запросом во время…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Плагин Claude Code (мод), который делает интерфейс терминала Claude Code…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Не позволяйте своему вниманию отвлекаться, пока вы ждёте ответа Claude Code.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Четырнадцать Claude Code-модов в одном плагине, каждый можно включать отдельно;
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Бесплатный плагин с открытым исходным кодом для Claude Code.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Мод Claude Code: отвечайте на вопросы Claude по пунктам прямо в тексте.
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Моды для Claude Code для длительных сессий: sitrep фиксирует результат и…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Очередь промптов для Claude Code в виде мода: /after &lt;task&gt; запускает задачу…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Модификации Claude Code: отобранные и протестированные, причём каждая…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навыки Claude Code: проверка фактов в документации, аудит кода, журнал памяти…
- [Orfila-antoine/claude-mods](https://github.com/Orfila-antoine/claude-mods)
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Мод Claude Code, который ведёт актуальный журнал Evidence, предоставляемых…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагин-компаньон Claude Code: ASCII-компаньон над запросом, который помнит ваши…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Плагин Claude Code для управления видимостью инструментов каждого агента…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Моды Claude Code: уровень безопасности для Claude Code — скрытие секретов…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Отображение формул LaTeX в режиме display в терминале Claude Code: MathJax…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Коллекция отличных модов Claude Code | Коллекция модов Claude Code.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: неофициальный фанатский мод по Avengers для Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Он говорит: мод Claude Code, который по запросу зачитывает вслух ответы Claude…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Шлёпайте Claude, когда он ошибается — мод для снятия стресса в Claude Code…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Моды Claude Code: небольшие плагины для интерактивных панелей, маршрутизации…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code с подтверждениями. Плагин, который планирует, делегирует и…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Мод и плагин Claude Code: монитор использования, отслеживание токенов и…
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC (Every Mod Claude Code): отобранная и протестированная коллекция модов для…
- [yyosifov/prompt-mods](https://github.com/yyosifov/prompt-mods) - Небольшие завершённые моды Claude Code для поля промпта.
- [0xgigilau/claude-usage-meters](https://github.com/0xgigilau/claude-usage-meters) - Мод Claude Code: индикаторы прогресса для контекста, использования за…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Маркетплейс модов Claude Code (my-claude-mods): полоса состояния, панели…
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Моды Claude Code: карточки статистики сессии над полем запроса.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анимированный кот из шрифта Брайля над приглашением Claude Code.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Пиксельный кот над запросом Claude Code, который запускает тестовый звонок…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, который выбирает подходящий момент для компактизации, чтобы…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модификации Claude для Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Моды общего назначения для Claude Code: полосы, панели, уведомления и хуки.
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - Мод Claude Code, выбирающий модель для каждого субагента до его запуска и…
- [arthurseredaa/herdr-pane-peek](https://github.com/arthurseredaa/herdr-pane-peek) - Claude Code mod for herdr: search panes across all workspaces and insert the…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Ваши лимиты использования Claude в виде анимированной карточки здоровья жителя…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code-моды для команды S2 (маркетплейс ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткие тренировки, пока Claude работает: ежедневная цель, серии, значки и…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Доска использования для Claude Code: расходы по моделям.
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Моды Claude Code: интерактивные панели, полосы и защитные механизмы, работающие…
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Мод Claude Code, показывающий, чем заняты ваши субагенты: индикатор прогресса…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Мод Claude Code, показывающий, сколько времени занял каждый ход, в виде…
- [benelog/claude-mods](https://github.com/benelog/claude-mods) - Mods for Claude Code: a status-line HUD and more.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Мод Now Playing для Claude Code: Apple Music и Spotify над приглашением, с…
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - Поддерживаемые проверенные копии модов Claude Code (filetree, cache-tax).
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - The Performance tab for Claude Code turns: a live waterfall of every model…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Моды для Claude Code: часы кэша, радиус поражения, предложения, рабочий список…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашего Claude Code.
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - Личные моды Claude Code.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Оригинальный движок Doom с Freedoom, доступный внутри Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Небольшие, понятные моды Claude Code из канала CorporateChittyChat.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Удерживайте Claude Code в рамках плана: этапы, контрольные точки утверждения и…
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Моды Claude Code.
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Мод для Claude Code: полоса над полем промпта с обратным отсчётом prompt-cache…
- [curran-gehring/claude-dot](https://github.com/curran-gehring/claude-dot) - Мод Claude Code, переносящий точки OpenAI в Claude: постоянно работающий…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - Мои личные моды Claude Code, настроенные под мою конфигурацию.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Эксклюзивные Claude Code-моды для команды d3nim.
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Мод Claude Code: просмотр навыков, плагинов, подагентов и инструментов MCP…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Одиннадцать модов Claude Code (плагины с хуками функций) для домашнего рабочего…
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Моды Claude Code: доска OpenSpec и субагентов, передача перед сжатием…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Тамагочи, живущий внутри Claude Code: он вылупляется, ест код, который пишет…
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Мод Claude Code: состояние проверки PR, одобрения, проверки и конфликты над…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Мод для Claude Code: панель ваших других сессий над полем промпта — кто вас…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - My collection of claude mods.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Мод для Claude Code: после того как guard блокирует вызов инструмента…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Мод для Claude Code: фоновые задания в одном представлении с прогрессом и…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Мод для Claude Code: единый входящий ящик для сообщений от товарищей по…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Мод для Claude Code: объясняет блокировки песочницы и превращает повторные…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Избранное для Claude Code: значки для команд и навыков, запускаемые одним…
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - Динамическая волновая доска плана вашего сеанса над приглашением Claude Code.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Инструкции, навыки, расширения Pi и Claude Code-моды для Pi, Codex и Claude Code.
- [esinecan/mental-model-mod](https://github.com/esinecan/mental-model-mod) - Мод Claude Code: рабочая модель Claude об Eren, изложенная его словами, с…
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Мод Claude Code для отображения прогресса фоновых тестов: JUnit, Karma, pytest…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Моды для Claude Code (плагины с перехватчиками функций): session-meter и другие.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: one tiny button that hides every Claude Code mod above your…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Тестовые моды команды Hospedin для Claude Code.
- [fran343/claude-mods](https://github.com/fran343/claude-mods)
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Мод Claude Code: заморозка сессии и её последующее возобновление, как будто…
- [g761007/hudcade](https://github.com/g761007/hudcade) - Пиксельный HUD для Claude Code: контекст, стоимость, кэш, агенты и ограничения…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Копирование ссылки по Ctrl+щелчку в каждом блоке кода в ответах Claude Code…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - Мод Claude Code для приложения рабочего стола: нажмите ссылку на файл в ответе…
- [h3h/blocks-only](https://github.com/h3h/blocks-only) - Мод Claude Code: ходы программирования завершаются проверенным отчётом о…
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Частный маркетплейс модов для Claude Code.
- [haruki-cl/claude-code-mods](https://github.com/haruki-cl/claude-code-mods) - Моды Claude Code: token-weather (панель использования контекста и памяти)…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Немецкоязычные моды для Claude Code: подсказки о контексте/кэше, открытые…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - A live spend meter for Claude Code: the session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Модификация Claude Code: сколько времени занял каждый ответ, сколько времени…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - маркетплейс модов claude.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Пульт управления над полем запроса Claude Code. Утка считывает показания.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Автоматически читает ваши инженерные чертежи, а затем создаёт модель в…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - Интерактивная доска подагентов Claude Code внутри VS Code: подагенты каждого…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Боковая панель с использованием контекста: общий объём, категории, рост за…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Боковая панель со списком файлов: какие файлы были созданы, изменены или…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пушистик в стиле 8-bit (чёрно-белый вислоухий голландский кролик) бегает и…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Боковая панель «Что я спрашивал»: каждое сообщение владельца в этом разговоре;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Боковая панель с временной шкалой: на что ушло время в этом раунде — ожидание…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Боковая панель обмена токенами: сколько токенов основной разговор отправляет…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Честный пакетик с бобами для claude code: после каждого раунда Claude тихо…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Контрольный список плана для Claude Code с проверкой доказательствами…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code.
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Моды Claude Code от Joseph Ayoub: маркетплейс плагинов (joseph-mods).
- [jrojasdeveloper/naruto-buddy](https://github.com/jrojasdeveloper/naruto-buddy) - Мод Claude Code: анимированный пиксельный Наруто над полем промпта.
- [jrpferreira2002-jpg/clawd-vibe](https://github.com/jrpferreira2002-jpg/clawd-vibe) - Мод Claude Code: Clawd над полем запроса, у clawd есть настроения.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живет в полосе над вашим prompt Claude Code: разыгрывает сессию…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод для озвучивания ответов и уведомлений Claude Code с помощью VOICEVOX /…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Моды Claude Code. PixBar: пиксельное существо над вашим запросом, которое…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Мод для Claude Code: каждая сессия Claude Code в одном плавающем окне, с…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Небольшие моды Claude Code в одном маркетплейсе плагинов.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Мод для Claude Code: выбирает модель и интенсивность рассуждений каждого…
- [kyuskoj/claude-mods](https://github.com/kyuskoj/claude-mods)
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Десять модов Code для Claude: анимированный пиксельный питомец, Code Wrapped…
- [Loup0007A/claude-mods](https://github.com/Loup0007A/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Подготовленное сообществом руководство по модам Claude Code: варианты…
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Mod de Claude Code: los límites de tu plan (sesión 5h, semana) y la renovación…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Отдельные моды Claude Code из Mod Box, каждый устанавливается самостоятельно.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод Claude Code, который показывает, что делает Claude, в подзаголовке вкладки…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Пушистая чёрная кошка над вашим промптом Claude Code.
- [malitov/effort-per-model](https://github.com/malitov/effort-per-model) - Claude Code mod: remembers the effort level per model and restores it on switch.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Моды Marcel для Claude Code на одном рынке плагинов (marcel-mods).
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Небольшие модификации для Code для Claude: runner-avatar — небольшой аватар…
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Моды Claude: счётчик токенов (token-meter).
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Мод Claude Code: панель в реальном времени с тем, к чему стремится ваш AI-агент…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Модификация Claude Code: панель /sessions для просмотра и удаления сессий…
- [melandres8/claude-mods](https://github.com/melandres8/claude-mods) - Claude Code mods: relevo (planner/builder relay between two sessions) and…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Боковая панель для Claude Code: файлы, записанные Claude, разделённые…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Мод для Claude Code: Codex (подписка ChatGPT) и другие модели, не относящиеся к…
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [MoriHiroshiDesu/hiroshi-claude-mods](https://github.com/MoriHiroshiDesu/hiroshi-claude-mods) - Mods pessoais do Claude Code (interface e comportamento).
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Мод для Claude Code: задаёт имя вкладке терминала, в которой выполняется Claude…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, включающий обратно инструменты todo для моделей, которые их не…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Мод для Claude Code, который ждёт безопасной паузы, а затем передаёт вашу…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одной строке на каждую задачу над запросом — текущая…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Играйте в Connect Four против AI внутри Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Мод Claude Code: когда другой агент программирования делает коммит в ваш…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Мод для Claude Code: поддерживает лёгкость сеансов — строка использования…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Мод Claude Code для репозиториев, которыми пользуются несколько ИИ-агентов: не…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Мод Code для Claude: по одной кнопке над промптом для каждого исполнителя…
- [NicoSKOOL/seo-mods](https://github.com/NicoSKOOL/seo-mods) - Моды для Claude Code для SEO: актуальные рейтинги DataWise над промптом и…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Повторно запускает длительные наблюдения Monitor в Claude Code после их…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Защитный механизм для SQL в Claude Code: запрашивает подтверждение перед тем…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Панель блокнота для Claude Code в виде мода.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Один мод для Claude Code и Windows, с приоритетом CJK: предварительный просмотр…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Моды для Claude Code: миниатюры изображений и строка состояния.
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid: конвейер коллективной проверки → планирования → исправления…
- [omarnaman/claude-mods](https://github.com/omarnaman/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Лучшие моды Claude Code, отсортированные по пользе для вас.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Два мода Claude для Claude Code: garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Временные метки для Claude Code: время каждого сообщения, ответа и вызова…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: мод для Claude Code. Постоянные worktrees с начальным доступом…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Live session-stats side pane for the Claude desktop app.
- [PhilRoli/claude-mods](https://github.com/PhilRoli/claude-mods) - Мод для Claude Code: приостанавливает сессии до прибытия поезда TrainTracker.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Моды для Claude Code: safety-guard блокирует разрушительные команды и доступ к…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Анимированный пиксельный краб Claude для Claude Code: он изображает действия…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Моды для Claude Code: плагины function-hook, работающие внутри сессии…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Мод Claude Code: отжимания, которые нужно делать, пока работает Claude.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: практическое руководство по модам для Claude Code — от ELI5 до…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - просто список используемых мной модов.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Три модификации Claude Code без зависимостей: адаптивная строка состояния…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Моды для claude code.
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Открытый маркетплейс модов Code для Claude с навыками репозитория для участия и…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Мод Claude Code: превращает план, который вы утверждаете в plan mode, в живой…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Подборка Claude Code-модов. Каждый элемент клонирован и проверен с помощью…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Бесплатный режим: вспомогательные агенты работают на Haiku, а большие файлы и…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музыка в стиле lofi, сопровождающая сессию: спокойствие, концентрация, поток, а…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Учитесь, пока Claude пишет код: после хода, изменившего код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запись каждого изменения, которое вносит Claude: воспроизводите каждое…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - Мод для Claude Code: панель проекта и изометрическая карта города с задачами…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board и другие моды для Claude Code от André Servaes.
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Центр управления Claude Code: флот субагентов в реальном времени, использование…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Моды Showrin для Claude Code, помогающие сделать повседневную работу…
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Мод для Claude Code: лимиты контекста и плана с прогнозом скорости…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Мод для Claude Code, поддерживающий работу сессий без присмотра при достижении…
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Claude Code mod: context-window meter per session, with Compact now…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - Коллекция модов Code для Claude: хуки TypeScript функций, поставляемая как…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commit messages в один клик для Claude Code с танцующей pixel-art Malenia.
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Моды для Claude Code. cache-meter: частота попаданий в кэш промпта, заполнение…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — мод Claude Code, показывающий использование вашего плана Claude…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Unofficial Claude Code mods by tanmen (marketplace: tanmen).
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Мод для Claude Code: интерактивная панель команды для каждого субагента…
- [thangnguyen-69/claude-mods](https://github.com/thangnguyen-69/claude-mods) - Рынок плагинов Claude Code: проверки Plannotator в tailnet и многое другое в…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, отображающий текущую сессию на панели: каждое приглашение…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Plugin marketplace модов Claude Code: function-hooks plugins, которые рисуют…
- [tiger3645/claude-tts](https://github.com/tiger3645/claude-tts) - Claude Code мод: зачитывает вслух ответы Claude (плагин для озвучивания).
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Мод для Claude Code: одна кнопка под последним ответом Claude копирует все…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Моды Claude Code от Toptaab.
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - Режим CC, показывающий, в какую учётную запись Claude, организацию и план вы…
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Некоторые моды Claude.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анимированная полоса прогресса и сводка по завершении для…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Три небольших мода Claude Code: узнайте, когда завершат работу ваши субагенты…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажите «Я потерялся», и Claude снова объяснит свой последний ответ простыми…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Задайте Claude дополнительный вопрос на панели рядом с вашей работой.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Плагин Code для Claude: обратный отсчёт prompt-cache, процент попаданий в кэш…
- [webfront/claude-mods](https://github.com/webfront/claude-mods) - Специальные моды для claude code и code в приложении claude.
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Claude Code мод: собственная модель сеанса выбирает модель и уровень усилий для…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Небольшие моды для повышения удобства работы с Code для Claude.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — когда контекст перерастает свою оболочку, сбросьте её в папку и…
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Мод для Claude Code: скрытые секреты, задачи, проверки и CI, дневник, diff…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Плагин Claude Code: лимиты использования Claude Pro/Max с прогнозом темпа…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моды для Claude Code. agent-crew: наблюдайте за работой субагентов как за живой…
- [zhitongLIU/claude-code-mods](https://github.com/zhitongLIU/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Отобранная вручную коллекция лучших ресурсов для самых потрясающих агентов…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Плагин Claude Code, показывающий, что происходит: использование контекста…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Красивая, полностью настраиваемая строка состояния для Claude Code CLI с…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Все части системного промпта Claude Code, 27 встроенных описаний инструментов…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Навык создания видео с ИИ для Claude Code и Codex — кинематографичные рекламные…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Более 45 советов по максимально эффективному использованию Claude Code — от…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — создание каруселей Xiaohongshu и пар обложек…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Просматривайте diff вашего агента кодирования в панели терминала и отправляйте…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Комплексный плагин статусной строки для Claude Code с использованием контекста…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Создавайте моды для Claude Code: перехватывайте любой запрос, изменяйте любой…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Комплексная панель statusline для Claude Code — информация о сессии, шкалы…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: отслеживайте углеродный след своих сессий Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Эстетичная statusline для Claude Code от awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Длинноформатный агент ролевой игры для DeepSeek Harness (плагин DSH酒馆): импорт…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Общедоступные Skills и моды для Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, моды, субагенты, хуки, slash-команды и руководства для Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Законно бесплатные LLM APIs и агенты программирования — самообновление…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Онлайн-счета футбольных матчей, расписание и турнирные таблицы для…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, превращающий вашего агента программирования в эксперта по…
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) - Цикл сеанса с приоритетом голоса для DeepSeek Harness: кнопка микрофона в…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Время молитв, дата по хиджре, азкары, ежедневный аят, пост по сунне, Рамадан…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Личная конфигурация Claude Code, версионируемая внутри ~/.claude — агенты…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — плагин DeepSeek Harness для исследовательских тем…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - Слой оркестрации мультиагентной работы для DeepSeek Harness (omd) — режимы…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Набор плагинов для Claude Code, pi и DeepSeek Harness: HUD в строке состояния…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Portable Claude Code toolkit for .NET DDD/Clean Architecture: strict TDD…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Лёгкая строка состояния Claude Code — один Bash-скрипт примерно на 170 строк…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Переносимая глобальная конфигурация Claude Code: пользовательские навыки, хуки…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Неофициальные моды для вкладки Code в Claude Desktop — usage-pet: полоса…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагины Claude Code, которые я использую каждый день: навыки и моды…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Анализируйте использование токенов и затраты Claude Code по локальным журналам…
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Красивая информативная строка состояния для Claude Code.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Визуальная доска для ваших агентов Claude Code: просматривайте сессии…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Настраиваемая строка состояния для Claude Code с редактором перетаскиванием.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Маркетплейс плагинов и навыков Claude Code для создания модов игры Hytale.
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Однострочный цветной статуслайн для Claude Code — папка, модель, использование…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Управление токенами для Claude Code: лучшая модель направляет работу, а…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Просмотрщик с разделённой панелью для Claude Code в Windows Terminal и tmux…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Микродашборд из 3 строк для терминала Claude Code — модель, расход контекста…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Репозиторий модов Awesome Media для Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Сократите расходы на Claude Code и токены Codex: направляет запросы и тестовые…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Быстрая настраиваемая строка состояния для Claude Code — один статический…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Отображение строки состояния Claude Code с ограничениями частоты запросов…
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Компактная активно поддерживаемая строка состояния для Claude Code — модель…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - дружелюбная строка состояния для Claude Code, с которой можно…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Определяемые программные фабрики для Claude Code на herdr: графы станций…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows Строка состояния PowerShell для Claude Код: 5-часовые и недельные…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Строка состояния Claude Code в Lua с интерактивной площадкой Neovim в реальном…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod.
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - Расширение VS Code: прогресс выполнения задач Claude Code, расчётное время и…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Моды для Claude Code: интерактивные панели, индикаторы и многое другое…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Красочная строка состояния Claude Code: лимиты плана, контекст, стоимость и…
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Строка состояния Claude Code для Windows: общее количество токенов, стоимость…
- [gvart/claude-config](https://github.com/gvart/claude-config) - Моя настройка Code для Claude: мод agent-monitor, навыки, агенты и установщик с…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Однострочная строка состояния для Claude Code: модель, git, контекст, токены…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Предпросмотр изображений внутри Claude Code: наведите курсор на чип под…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Строка состояния Claude Code: модель, шкалы квот 5 ч/7 д, шкала месячных…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Персональная конфигурация Claude Code: разрешения, statusline, серверы MCP.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Строка состояния Claude Code со строками панели агентов.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: переносимая настройка Claude Code — глобальные правила…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Отображает подробную цветовую панель состояния для Claude Code с информацией о…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Отслеживайте состояние Claude Code с помощью компактной панели, показывающей…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Двухстрочная строка состояния для терминального агента программирования…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Хук строки состояния Claude Code — отслеживает использование токенов и контекст…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Строка состояния Claude Code с установщиком для Linux и Git Bash в Windows.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - самодельные claude-плагины без клеток, навыки, моды и многое другое.
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Маркетплейс Code для Claude от MSF Supply: моды, отобранные и зафиксированные…
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Подробная многострочная строка состояния для Code Claude — актуальные лимиты…
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Многострочная строка состояния Claude Code: панель контекста, ветка git, полосы…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — строка состояния Claude Code для macOS +…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Отслеживайте состояние Claude Code из строки меню macOS с индикаторами в…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Навыки и моды для Claude Code и Cowork — трекер проектов, справочный документ и…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Строка состояния Claude Code для Windows (PowerShell): индикаторы…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Настраиваемая строка состояния Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Конфигурация и моды Claude Code с общим набором компонентов, playground и…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Меры защиты управления рисками моделей для Claude Code: 25 средств контроля в…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Стартовый каркас для Claude Code: хуки, строка состояния, локальные модели…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Портативная конфигурация Claude Code (строка состояния + установщик).
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Строка состояния из 4 строк для Claude Code.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Переносимая конфигурация Claude Code: CLAUDE.md, settings, statusline, skills.
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Универсальная многопротокольная StatusLine, самообучение контекста и плагин…
- [tylergraydev/cc-mods](https://github.com/tylergraydev/cc-mods) - Моды для Claude Code: боковые панели, строки состояния, уведомления и защиты…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Отслеживайте использование контекста Claude Code, стоимость сеансов и сбросы…
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - Мои навыки, плагины и моды для Claude Code (маркетплейс: vladdu).
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Синхронизация пользовательской конфигурации Claude Code между несколькими…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Строка состояния Claude Code с градиентными индикаторами выполнения…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Строка состояния Claude Code: папка, ветка git, модель, использование…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Детектор деградации контекста 2026 — проактивный монитор памяти ИИ и лимитов…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, субагенты и statusline для Claude Code: open-source коллекции и…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Статусная строка Claude Code с отображением использования токенов в реальном…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Моды для Claude Code: панели, полосы и компаньоны на основе перехватчиков…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Передавайте задачи между сеансами Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Это на сервере MCP для управления MODS — модульным кроссплатформенным…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Навык Codex и Claude Code для перевода модов CK3 с помощью локального LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Моды с открытым исходным кодом и другие расширения для Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: находите то, о чём вы снова и снова просите Claude Code, и…

</details>

<a id="dsh-cordis"></a>

## Экосистемы плагинов DSH и Cordis

DeepSeek Harness и Cordis приходят к тому же результату с другой стороны: для них плагин является механизмом модификаций, поэтому плагин там эквивалентен моду здесь.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74439 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

🌊 Оригинальный agent harness. Разворачивайте интеллектуальные многопользовательские рои, координируйте автономные рабочие процессы и создавайте разговорные AI-системы. Поддерживает адаптивную память, самообучающийся интеллект, федерацию, интеграцию с vector RAG и нативные Claude Code / Codex / Hermes, а также многие другие интеграции.

<sub>🔧 Найдено использование в коде: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                        |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **74439**  |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐153127 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Проводите обратную разработку чего угодно с помощью агентов — от поведения приложения до нативных бинарных файлов.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **153127** |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100748 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

🎨 Лучший плагин для дизайна DeepSeek Harness. Альтернатива с открытым исходным кодом Claude Design. 🖥️ Десктопное приложение с приоритетом локальной работы. 🖼️ Ваш агент программирования становится движком дизайна: прототипы, целевые страницы, панели мониторинга, слайды, изображения и видео — реальные файлы, экспорт в HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode и более 20 CLI через BYOK.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **100748** |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82525 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Превращает любую идею, план или кодовую базу в красивую интерактивную диаграмму. Навык агента для Claude Code, Codex и других.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **82525**  |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Надёжный агент для программирования, предназначенный для сложных задач разработки ПО.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Go                                                                     |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **35769**  |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25532 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Distilly — превращайте то, как они думают, в многоразовые Skills для любого Agent или Bot. Ранее Colleague Skill（原同事 Skill）.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Python                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **25532**  |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18516 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Кураторский список плагинов для DeepSeek Harness (dsh) · Избранный список плагинов DeepSeek Harness

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **18516**  |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8667 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Экосистема веб-плагинов DeepSeek Harness (DSH) · Всё является плагином и распространяется через Creative Workshop · Экосистема агрегации веб-плагинов DeepSeek Harness (DSH) · Всё является плагином и распространяется через Creative Workshop

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **8667**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6275 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Магазин плагинов внутри DeepSeek Harness — просмотр, поиск и установка в один клик · Визуальный магазин плагинов DSH

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6275**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4461 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Официально рекомендуемый DSH плагин TUI — высокая производительность, низкие накладные расходы, милый пиксельный кит и плавное взаимодействие с мышью. Установка одной командой через npm. / Официально рекомендуемый DSH плагин TUI: высокая производительность, низкие накладные расходы, милый пиксельный кит, плавное взаимодействие с мышью, установка одной командой через npm

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **4461**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3680 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Первый в мире виртуальный терминал для ИИ-агентов

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3680**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3034 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Настольная версия DeepSeek Harness на Tauri | Установщик размером всего 8 МБ, настройка окружения не требуется, предустановленные плагины, Windows / macOS / Linux.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3034**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1911 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Подключение IM-ботов к DeepSeek Harness с помощью QR-кода или учётных данных бота (поддерживаются 飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord и WhatsApp). Подключайте IM-ботов к DeepSeek Harness через QR-код или учётные данные (9 каналов).

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1911**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1423 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Программа для написания романов с ИИ: организует идеи, персонажей, построение мира, планы, написание глав, рецензирование и редактирование в управляемый рабочий процесс; предоставляет настольные версии для Windows/macOS, поддерживает локальные и онлайн-модели. Программа для написания романов с ИИ: организует идеи, персонажей, построение мира, планы, написание глав, рецензирование и редактирование в управляемый рабочий процесс. Предоставляет настольные приложения для Windows/macOS, интеграцию с Ollama и предварительную версию плагина DeepSeek Harness (DSH).

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1423**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1182 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Память для Claude Code, Codex, Cursor и ещё 38 агентов для программирования, созданная на основе истории сессий, уже сохранённой на вашем диске. Локальный поиск, MCP и хуки, без LLM, один бинарный файл Go.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Go                                                                     |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1182**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wecode-ai/Wegent">wecode-ai/Wegent</a></b> · ⭐870 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Plan, build, and deliver with an open-source, self-hostable AI workspace for coding, collaboration, and automation.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **870**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agent` · `ai` · `chatbot` · `claude-code` · `codex` · `dsh-plugin` · `wework`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wecode-ai--wegent/991765bc5aba6a3c.png" width="100%" alt="wecode-ai/Wegent screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **593**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Python                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **526**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐261 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Неофициальный плагин DSH (DeepSeek Harness): использование веб-моделей chat.deepseek.com в качестве провайдера LLM — захват входа через браузер, решение PoW, потоковая передача SSE, вызовы инструментов на основе промптов.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **261**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

ACRYL — Agent Context Relay Yielding Lifecycles. Одно постоянное рабочее пространство, один канонический контекст, любой агент программирования.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **255**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-research-report">PerryLink/dsh-research-report</a></b> · ⭐214 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Движок проверяемых исследовательских отчётов для DeepSeek Harness: реестр доказательств с адресацией по содержимому (привязка утверждений к снимкам, защита от незаметного изменения), а также версионируемые запечатанные отчёты с вердиктами проверки по каждому утверждению и каталогом, запечатанным манифестом.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **214**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `audit` · `citation-verification` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/2a270ca82dba24d3.png" width="100%" alt="PerryLink/dsh-research-report screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/dafefe1b3e0cd96e.gif" width="100%" alt="PerryLink/dsh-research-report animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Терминальный интерфейс в стиле Claude Code для DeepSeek Harness с поддержкой Windows, macOS и Linux, совместимый с прозрачным терминалом, темами VS Code и пользовательскими цветовыми схемами.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **197**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐194 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

🚀 Плагин DeepSeek Harness для многоканального удалённого доступа и безопасной защиты | прямое подключение по QR-коду в локальной сети, Cloudflare / самостоятельно размещаемые общедоступные туннели, полный жизненный цикл диалогов через ботов 微信 / QQ / 飞书 / Telegram | встроенная аутентификация безопасности доступа по всем протоколам, защита от изменения данных в фоне и система аварийного восстановления

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **194**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин DeepSeek Harness для предварительно просматриваемой миграции сессий между пресетами. Передача данных по фиксированной схеме сохраняет состояние, намерение исходной модели и нерешённые изображения; исходная сессия остаётся неизменной.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **165**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐144 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Тема рабочего стола Claude Code для DeepSeek Harness｜Тема рабочего стола Claude Code, созданная для веб-интерфейса DeepSeek Harness

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **144**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>анимированная запись</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-memento">PerryLink/dsh-memento</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Ограниченная, многоуровневая, требующая подтверждения и проверяемая межсессионная память для DeepSeek Harness: интерфейс возможностей ctx.memory с провайдером SQLite без зависимостей, инструментом памяти и внедрением замороженных снимков. Статус сопровождения: FROZEN с 2026-10-05.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **141**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agent-memory` · `ai-agent` · `ai-agents` · `approval` · `audit` · `cordis` · `deepseek-harness` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/f63bd5eb5a8052b8.png" width="100%" alt="PerryLink/dsh-memento screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/0ce3328d348abdce.gif" width="100%" alt="PerryLink/dsh-memento animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐140 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Сразу после установки содержит 27 инженерных и рабочих навыков из mattpocock/skills v1.3.1 — устанавливать навыки вручную не требуется. Этот плагин создан с использованием 40 миллиардов токенов и обеспечивает десятикратное повышение эффективности разработки по сравнению с исходными навыками, а также помогает новичкам быстрее освоить этот набор навыков. Полная поддержка issue на GitHub; Markdown пока находится в предварительной версии; GitLab пока не поддерживается. Спасибо за использование и поддержку 💗

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **140**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-permission-rules">PerryLink/dsh-permission-rules</a></b> · ⭐122 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Декларативные правила разрешений в стиле Claude Code для DeepSeek Harness: упорядоченные правила разрешения/запрета/запроса с сопоставлением имени инструмента, аргумента (glob/regex) и пути рабочего пространства в конвейере tools/pre-execute, аудитом журнала сеанса и перезагрузкой HMR.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **122**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `ai-safety` · `allow-deny-ask` · `approval` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/d950618f5f9cf382.png" width="100%" alt="PerryLink/dsh-permission-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-permission-rules/25c9ccd2f2133850.gif" width="100%" alt="PerryLink/dsh-permission-rules animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AskTheWay/dsh-auto-memory">AskTheWay/dsh-auto-memory</a></b> · ⭐106 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Claude Code-style auto-memory plugin for DeepSeek Harness (dsh): typed memory files + MEMORY.md index auto-injected into the system prompt. File-only, no external services.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **106**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agent-harness` · `agent-memory` · `ai-agent` · `ai-tools` · `auto-memory` · `claude-code` · `coding-agent` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/asktheway--dsh-auto-memory/1ff60db2b929f245.png" width="100%" alt="AskTheWay/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин DeepSeek Harness (DSH): ✨ улучшение промптов в один клик + 💬 распознавание речи (автоматическая остановка после окончания речи · два движка: облачный/локальный) · 🔁 перезапуск службы в один клик при сбое

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **90**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Настольный Agent, созданный на базе ядра Deepseek-Harness. Наследует все возможности основы и дополняет функции, связанные с IDE.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **69**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Маркетплейс плагинов сообщества DeepSeek-Harness с автоматической классификацией, отбором и проверкой. Автоматически классифицирует, отбирает и проверяет плагины сообщества DeepSeek-Harness.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **69**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-fund-research">PerryLink/dsh-fund-research</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Детерминированные исследовательские отчёты о китайских публичных паевых инвестиционных фондах в виде плагина DeepSeek Harness: на вход подаётся код фонда, на выходе — версионируемый отчёт Markdown с декомпозицией доходности, анализом проникновения в состав активов, атрибуцией стиля и явными заявлениями о пробелах в данных. Метрики вычисляются в коде, а не моделью.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **68**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `finance` · `fund-research`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/9a258f42b5375ed7.png" width="100%" alt="PerryLink/dsh-fund-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/c127c0b5eda50892.gif" width="100%" alt="PerryLink/dsh-fund-research animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐60 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Тематический плагин Catppuccin для DeepSeek Harness Web GUI: мгновенное переключение между четырьмя темами — Latte / Frappé / Macchiato / Mocha; встроенный отключаемый эффект стекла (Glassmorphism)

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **60**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-13 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Защита перед выполнением для AI-агентов программирования.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Отобранный список лучших отличных ИИ-плагинов для ИИ-ассистентов, включая…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Рынок плагинов DSH / DSH Plugin Marketplace: в веб-интерфейсе DeepSeek Harness…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、211个世界与上万素材、开局随心定制、世界自行运转、零漂移存档.
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - Постоянно обновляемые статьи по компьютерной графике, 3DGS и пространственному…
- [arcships/rutis](https://github.com/arcships/rutis) - Среда выполнения плагинов для самоизменяющегося программного обеспечения…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Сообщество плагинов DeepSeek Harness — автоматическая синхронизация…
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Живой каталог плагинов DeepSeek Harness — обновляется ежечасно, ежедневно…
- [Nyasers/DSHana](https://github.com/Nyasers/DSHana) - DSHana: DeepSeek Harness как субагент для HanaAgent.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Извлечение контекста рабочего пространства с учётом задачи и отслеживание…
- [GDWhisper/dsh-web-startup-auth](https://github.com/GDWhisper/dsh-web-startup-auth) - Плагин удалённого запуска Web для DSH（DeepSeek Harness）с аутентификацией по…
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - Плагин DeepSeek Harness: детерминированное профилирование, очистка и проверка…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent — FDE Harness с открытым исходным кодом для ИИ-агентов…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Альтернатива GrokBot с открытым исходным кодом на базе DeepSeek Harness.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Избранный каталог плагинов DeepSeek Harness (DSH) — более 280 плагинов…
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - База знаний по разработке плагинов DeepSeek Harness (dsh): руководство по…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: мультиплатформенная система агентов групповых чатов на базе DeepSeek…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Плагин DSH: оболочка Git Bash для всех режимов агентов на Windows.
- [YRN-playmaker/dsh-wallpaper_share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - Плагин для синхронизации различных динамических обоев движка обоев одним кликом…
- [AskTheWay/dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor) - ⚡ Millisecond System-1 judgement for every tool call in DeepSeek Harness…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Коллекция веб-плагинов GUI для DSH (DeepSeek Harness) — уведомления о задачах…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Веб-плагин DSH: ежедневная статистика использования токенов с тепловой картой…
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - Прозрачный рейтинг и рекомендации экосистемы плагинов DSH: ежедневный…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Настоящий PowerPoint, а не HTML. Расскажите ИИ, что нужно осветить, и pptwise…
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - Синхронизация сеансов DeepSeek Harness между устройствами: выделенное…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Локальный граф знаний кода и среда контекста для агентов программирования.
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - Веб-плагин DSH: иерархическое дерево рабочих пространств на боковой панели…
- [ddtcorex/govard](https://github.com/ddtcorex/govard) - Локальный оркестратор разработки на базе Go для Magento, Laravel, Symfony…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Превратите модели, уже авторизованные в настольном приложении WorkBuddy на этом…
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) - Перевод параметров провайдеров и детерминированное исправление JSON для…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - Двуязычный постоянно поддерживаемый каталог плагинов для DeepSeek Harness (DSH).
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - Многомерная оценка качества плагинов DeepSeek Harness: оценка репозитория или…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Изолированные тестовые установки и проверки работоспособности плагинов DeepSeek…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Плагин функциональной панели DeepSeek Harness: одна панель для…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Постоянное тестирование совместимости плагинов DeepSeek Harness: точные версии…
- [liang-today/dsh-liangxiang](https://github.com/liang-today/dsh-liangxiang) - 众香成势，梁子显相。DeepSeek Harness 的 WebUI 插件，欢迎一起打梁.
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Хост-плагин DeepSeek Harness, который хранит документы проектов и…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - Тщательно отобранный каталог плагинов DeepSeek Harness (DSH), основанный на…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray для плагинов DeepSeek Harness: заявленные возможности против фактического…
- [ayingQAQ/dsh-web-launcher](https://github.com/ayingQAQ/dsh-web-launcher) - Windows 上的 DeepSeek Harness Web 一键启动器｜One-click launcher with background…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Рабочее пространство с несколькими папками: позволяет агенту DSH.
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Выполнение DeepSeek Harness (dsh) на базе Podman.
- [kelemiao/dsh-animation-optimization](https://github.com/kelemiao/dsh-animation-optimization) - Оптимизация анимации DSH: плагин потоковой анимации вывода и внешнего вида в…
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - Голосовые разговоры для DSH с приоритетом локального запуска.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Плагин DSH: окно инструментов Git уровня IDE в виде нативной вкладки…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - Творческий режим на основе режима PTC: плагин DSH, объединяющий оркестрацию…
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Набор возможностей страницы для DeepSeek Harness (dsh): терминальная панель…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Дайте агенту DeepSeek Harness нативные руки и ноги для управления GitHub!
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт проверки плагинов DeepSeek Harness (dsh) без зависимостей…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Экосистема плагинов DeepSeek Harness: 86 плагинов с открытым исходным кодом в…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Маркетплейс плагинов DeepSeek Harness — просмотр, поиск и установка плагинов из…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode в DeepSeek Harness — плагин DSH, поддерживающий работу OpenCode Zen и…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонний маркетплейс плагинов и защищённый менеджер жизненного…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx — расширяемая настольная рабочая среда, ориентированная на человека…
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Запускайте DeepSeek Harness на настольном компьютере без затрат на токены…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - Рабочая среда dsh Bots: плагин Cordis, подключающий шлюз оркестрации sdk-bots к…
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Семейство плагинов для самоэволюции агентов, вдохновлённое Hermes и специально…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — набор инструментов для локального развёртывания и эксплуатации…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Веб-плагин DeepSeek Harness (DSH): вкладка боковой панели market-dashboard для…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Независимые сторонние плагины и инструменты для DeepSeek Harness…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Используйте бесплатные модели OpenCode Zen в DeepSeek Harness с анонимным…
- [yangzhe1991/dsh-web-enhance](https://github.com/yangzhe1991/dsh-web-enhance) - Плагин улучшений DSH Web UI: цепочка рассуждений развёрнута по умолчанию…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Плагин DeepSeek Harness: превращает сбой выделения ACL песочницы Windows…
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Сроки на уровне развёртывания для вызовов инструмента dsh, в которых срок не…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Среда выполнения плагинов Rust с проверенным Verus ядром жизненного цикла и…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Плагин Cordis / DeepSeek Harness — нормализованные инструменты GitHub API для…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Встроенная панель Antigravity: токенов/с, коэффициент попаданий в кэш в стиле…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Arkme account, records, chat and interwoven-moments integration for DeepSeek…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Магазин плагинов dsh — автоматическое обнаружение и ежечасная синхронизация на…

</details>

<a id="writing"></a>

## Тексты, обсуждения и видео

Статьи, обсуждения и видео о возможностях модов.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Сводка

Привет, HN, я создал это для себя и решил открыть исходный код. Проблема: мне нужен был способ получать напоминания между промптами, поскольку я часто провожу долгие часы в терминале, особенно теперь, когда мы обычно обрабатываем так много агентов параллельно. Первая версия была простым rep

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

##### 📝 Сводка

Я создал это потому, что с последними моделями для программирования Claude переходит в режим глубокой работы с непонятными командами, и я больше не понимаю, чем он занимается. Это мод (плагин, использующий новые функциональные хуки Claude Code), который рисует одну строку над запросом: — текущий шаг,

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Тексты, обсуждения и видео`                                              |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Впервые в списке | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Проекты по языку реализации

Экосистема сосредоточена в Python и TypeScript, но типизированные клиенты продолжают появляться и на других языках. Эта таблица генерируется из самих записей.

| Язык       | Записей | Примеры                                                                                                         |
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

<sub>Учитываются только записи, в которых указан язык. Документация и обсуждения исключены из этой таблицы.</sub>

## Участие

Исправления приветствуются и являются самым быстрым способом улучшить этот список. Откройте issue или pull request, если запись попала не в тот раздел, получила неверную оценку или если проект был ошибочно исключен как совпадение имени — именно в этой последней категории автоматические фильтры чаще всего ошибаются.

---

<sub>Независимый проект сообщества. Не аффилирован с Anthropic, не одобрен и не проверен им. Claude Code, Claude и Anthropic являются товарными знаками Anthropic. Поведение продукта может меняться без уведомления; всё критически важное проверяйте по официальной документации. Материалы остаются собственностью исходных проектов и воспроизводятся только там, где это разрешено лицензией.</sub>

<sub>Последнее обновление · 2026-10-13T06:19:35+08:00</sub>
