<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Отличные моды для Claude">
</p>

<h1 align="center">Отличные моды для Claude</h1>

<p align="center"><b>Индекс модов, плагинов Claude Code и более глубоких изменений поведения, составленный с оценкой доказательности.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-506-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <b>Русский</b> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Актуальный индекс** · Последняя синхронизация: `2026-10-11T21:12:49+08:00` (UTC+8)
> · Записей: **506** · Добавлено в последнем обновлении: **0** · Языки реализации: **12**

<sub>Каждая запись ниже была автоматически собрана, отфильтрована и проверена повторно. Здесь нет платных размещений.</sub>

<a id="featured"></a>

## Лучшее на данный момент

<sub>По одной записи на категорию, ранжирование по степени подтверждённости и количеству звёзд, пересчитывается при каждом обновлении. Это рейтинг, а не рекомендация; каждая подборка ведёт к полной карточке ниже. Предпочтение отдаётся проектам, опубликовавшим снимок экрана или запись, чтобы лента оставалась визуальной.</sub>

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
<sub>Найдите призрачные токены. Исправьте их. Переживите компактификацию. Избегайте ухудшения качества контекста.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74325 · TypeScript · 👁️ observed</sub>
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
- [Официальные: собственные репозитории и примечания к выпускам Anthropic](#официальные-собственные-репозитории-и-примечания-к-выпускам-anthropic) — **15**
- [Моды: созданы с использованием возможности модификации](#моды-созданы-с-использованием-возможности-модификации) — **381**
- [Экосистемы плагинов DSH и Cordis](#экосистемы-плагинов-dsh-и-cordis) — **99**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150151 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Сводка

Claude Code — агентский инструмент для программирования, работающий в терминале, понимающий вашу кодовую базу и помогающий программировать быстрее: он выполняет рутинные задачи, объясняет сложный код и обрабатывает рабочие процессы git — всё с помощью команд на естественном языке.

<sub>🔧 Найдено использование в коде: `feed.xml`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |
| Язык          | TypeScript                                                               |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **150151** |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9473 · TypeScript · ✅ official · 1 天</summary>

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
| Звёзды           | **9473**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

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
| Звёзды           | **8248**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

##### 📝 Сводка

An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `опубликовано самим Anthropic`                                           |
| Язык          | Python                                                                   |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6342**   |
| Последний push   | 2026-02-11 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

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
| Звёзды           | **1797**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Сводка

Supplementary materials for Claude Model Cards

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
<summary><b>Больше в этой категории</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Добавлен `$.ui.notify` для модов: вызывает нативное уведомление через ваши…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Исправлена ситуация, когда Esc или прерывание во время хука `UserPromptSubmit`…
- [riffkit/skill](https://github.com/riffkit/skill) - Official Riffkit skill — riff a winning TikTok into your own short video from…

</details>

<a id="mods"></a>

## Моды: созданы с использованием возможности модификации

Каждая запись здесь демонстрирует использование возможности, которую Claude Code получил в версии 2.1.287: она выполняет отрисовку через `ui.render`, владеет панелью, полосой или карточкой, читает `$.ui.selection()`, создаёт товарищей с помощью `agent.spawn` или прямо указывает, что является модом.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Найдите призрачные токены. Исправьте их. Переживите компактификацию. Избегайте ухудшения качества контекста.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | Python                                                                    |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2534**   |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>анимированная запись</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐484 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Каталог сообщества публичных модификаций Claude Code (функциональных хуков), просканированных из GitHub, с указанием того, что каждая модификация может читать, записывать, запускать или отправлять по сети. Просмотреть https://mods.aidojo.si/

<sub>🔧 Найдено использование в коде: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **484**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 7 天</summary>

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
| Звёзды           | **127**    |
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
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Сводка

QA CLI для веб-страниц, ориентированный на агентов. Детерминированный, не требует написания тестов и не использует LLM.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | HTML                                                                      |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **104**    |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐93 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Скины для Claude Code: строки инструментов со значками, карточки с diff, таблицами и диаграммами Mermaid, полоса использования и пятнадцать тем. /skin мгновенно переключает их.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **93**     |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **74**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

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
| Звёзды           | **66**     |
| Последний push   | 2026-10-02 |
| Впервые в списке | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/claude-code-mods">karanb192/claude-code-mods</a></b> · ⭐40 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Сводка

Модификации Claude и инструменты для их создания: сначала навык-сборщик, затем модификации

<sub>🔧 Найдено использование в коде: `plugins/mod-builder/skills/mod-builder/references/migrate.md`, `plugins/mod-builder/skills/mod-builder/references/nouns.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **40**     |
| Последний push   | 2026-10-03 |
| Впервые в списке | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
| Звёзды           | **27**     |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐24 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Claude Code показывает изображения и воспроизводит видео прямо в терминале: скриншоты, записи Playwright и синхронизированные проверки до / после. Ghostty и kitty.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **24**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/9ee7df00aee28636.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/adcbff13953c23f1.gif" width="100%" alt="iamumeransari/claude-show-your-work animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **23**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **11**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

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
| Звёзды           | **8**      |
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
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Markdown, отрисовываемый в поле приглашения Claude Code по мере ввода. Код в ограждённом блоке превращается в карточку с подсветкой синтаксиса ещё до закрытия блока.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **7**      |
| Последний push   | 2026-10-03 |
| Впервые в списке | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Моды для Claude Code: плагины с функциональными хуками, добавляющие интерактивные панели и поведение в интерфейс терминала

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6**      |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Интерактивная панель GSD для Claude Code: дорожная карта, дерево агентов с ответвлениями, контекст и стоимость, рабочие потоки и средство чтения Markdown для .planning. Только для чтения.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6**      |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/a31036b15398e820.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Сводка

Мод Claude Code (плагин), который добавляет боковую панель с вкладками Activity, Files, Agents, Context и MCP, строку состояния над prompt, переработанный chat, диаграммы Mermaid в терминале, таблицы, а также панели code и diff. Цвета соответствуют как /color, так и /theme (dark, light и другим).

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6**      |
| Последний push   | 2026-10-06 |
| Впервые в списке | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Ваш план, который следит за собой. Локальное настольное дерево дорожной карты, которое Claude Code и любой хост MCP поддерживают в актуальном состоянии в реальном времени. Обычный JSON, без облака.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6**      |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/leopiney/wolfbud-claude-mod">leopiney/wolfbud-claude-mod</a></b> · ⭐5 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Сводка

Голосовой напарник для Claude Code. Обсуждайте задачи с 3D-волком на базе разговорного AI ElevenLabs; когда вы соглашаетесь, он отправляет промпт в Claude и сообщает, когда Claude завершён.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **5**      |
| Последний push   | 2026-10-08 |
| Впервые в списке | 2026-10-10 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/leopiney/wolfbud-claude-mod/main/assets/banner.png" width="100%" alt="leopiney/wolfbud-claude-mod screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HMarzban/claude-mod">HMarzban/claude-mod</a></b> · ⭐4 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Узнайте стоимость вашего следующего сообщения Claude Code: живая полоса над промптом с обратным отсчётом кэширования промпта, ценой повторного прогрева, стоимостью сеанса, контекстом и недельными ограничениями использования 5h.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **4**      |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-ai` · `claude-code` · `claude-code-plugin` · `claude-mod` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dominicrico/jev-router">dominicrico/jev-router</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Плагин Claude Code: автоматическая маршрутизация моделей Claude. Выбирает Haiku, Sonnet или Opus и уровень рассуждений для каждого запроса, шага и субагента; ограничение усилий, защита кэша промптов, статусная полоса, бенчмарки.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3**      |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-09 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-marketplace` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/e9ab68584ed9c404.jpg" width="100%" alt="dominicrico/jev-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/2a6620c49438b369.gif" width="100%" alt="dominicrico/jev-router animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/FynnXland/fynn-mods">FynnXland/fynn-mods</a></b> · ⭐3 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Сводка

Шесть модов для Claude Code: анимированный маскот Clawd, индикаторы лимита использования и prompt-cache, проверка сообщения перед отправкой, быстрые ответы, очередь задач и журнал затрат. Терминал и desktop app, английский/немецкий.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3**      |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-07 |

🏷 `ai-coding-assistant` · `claude` · `claude-ai` · `claude-code` · `claude-code-marketplace` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mertkayacs/ultramod">mertkayacs/ultramod</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Лучший универсальный набор модов для Claude Code: лимиты использования и HUD контекста, защита с отменой для rm -rf и git reset --hard, защита .env и секретов, а также квитанция для каждого хода. Десять модов, одна установка.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3**      |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-09 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/0f9d8b2253819dc8.gif" width="100%" alt="mertkayacs/ultramod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/1537defa7233d7f2.gif" width="100%" alt="mertkayacs/ultramod animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mthli/cc-shorts">mthli/cc-shorts</a></b> · ⭐3 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Смотрите YouTube Shorts в своём Claude Code 💃

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3**      |
| Последний push   | 2026-10-02 |
| Впервые в списке | 2026-10-10 |

🏷 `claude-mods` · `youtube-shorts`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mthli--cc-shorts/ef652fff732c023d.png" width="100%" alt="mthli/cc-shorts screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/chenyuxiaojin/cyxj-notch">chenyuxiaojin/cyxj-notch</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Дашборд macOS notch для Claude Code: лимиты использования, открытые сессии, прогресс задач, обратный отсчёт кэша промптов и список дел — данные поступают от пяти модов Claude Code (включены).

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools` · `dynamic-island` · `macos` · `menu-bar`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Christandoh/context-cache">Christandoh/context-cache</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Claude Code mod: context usage, session / weekly / Fable limits and prompt-cache temperature above the prompt

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/christandoh--context-cache/3cdd3b2c5a09da7d.png" width="100%" alt="Christandoh/context-cache screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/CodyAMaughan/meme-factory">CodyAMaughan/meme-factory</a></b> · ⭐2 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Прямо с завода. Мод Claude Code: попросите мем и продолжайте работу. Черновики готовятся в боковой панели; выбирайте, перерабатывайте, утверждайте и публикуйте в Slack.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `fun` · `meme-generator` · `memes` · `slack`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/7417dc8940c4a087.png" width="100%" alt="CodyAMaughan/meme-factory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/8c9d44287267796f.gif" width="100%" alt="CodyAMaughan/meme-factory animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/estruyf/claude-stats-mod">estruyf/claude-stats-mod</a></b> · ⭐2 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Сводка

Мод Claude Code, отображающий ваши лимиты использования и расходы в полосе над промптом.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-02 |
| Впервые в списке | 2026-10-10 |

🏷 `claude` · `claude-code` · `claude-mod` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/estruyf/claude-stats-mod/main/assets/desktop.png" width="100%" alt="estruyf/claude-stats-mod screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/i-harsha-reddy/naruto-mod">i-harsha-reddy/naruto-mod</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Пиксельный компаньон Naruto для Claude Code: 20 ниндзя, 60 дзюцу, выполняемых во время работы Claude

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `naruto` · `pixel-art`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lorenzh/rabe">lorenzh/rabe</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Смотрите, что Claude Code запускает в фоне: субагенты, задания Codex, shell, мониторы, cron jobs и workflows.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/macleodlabs-ai/claudeflow">macleodlabs-ai/claudeflow</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Модификации Claude Code от MacLeod Labs: streams распутывает перемешанную работу сеанса в потоки, выделенные разными цветами

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/macleodlabs-ai/claudeflow/main/assets/hero.jpg" width="100%" alt="macleodlabs-ai/claudeflow screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/MankhongGarden/claude-code-mods-field-notes">MankhongGarden/claude-code-mods-field-notes</a></b> · ⭐2 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Сводка

Полевые заметки первого дня о модах Claude Code на Windows: топливная шкала контекста/квоты, мод тайского интерфейса, вступление загрузки Matrix и безопасный обновлятор, плюс что не сработало и почему (панели, полосы над промптом, тайский в Windows Terminal).

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2**      |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-07 |

🏷 `anthropic` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mankhonggarden--claude-code-mods-field-notes/832ffcdb7bad9007.png" width="100%" alt="MankhongGarden/claude-code-mods-field-notes screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 347</sub></summary>

- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Модификация, придающая терминальному журналу Claude Code вид настольного…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Боковая панель для кода Claude: субагенты, запускаемые сессией, выполняемая…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Панель боковой панели Claude Desktop (вкладка Code): перечисляет все…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Полоса использования над полем ввода Claude Desktop (вкладка Code): лимиты 5h /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Пользовательские моды, плагины и навыки Claude, устанавливаемые из одного…
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Очередь решений CLI/TUI для людей, работающих с разговорными агентами.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плавающая карточка состояния для Claude Code — модель, контекст, ограничения…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Чтение markdown-файлов, которым код Claude даёт имена, с отображением рядом с…
- [atomashevic/claude-latex-math](https://github.com/atomashevic/claude-latex-math) - Claude Code mod that typesets the LaTeX math in Claude.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Фейерверки для Claude Code: каждое нажатие клавиши, вызов инструмента, коммит и…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Небольшие моды Claude Code (плагины с перехватчиками функций): session-switcher…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Шесть модификаций Claude Code: ограничения плана и контекст над полем запроса…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набор инструментов Naren для Claude: skills, mods и MCP servers для Claude…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Мод Claude Code, отображающий различия Edit и Write в двух расположенных рядом…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Кураторский список модификаций Claude Code, устанавливаемых как через…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Крайне авторский плагин Claude Code, созданный любителем Rust, одержимым…
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Пассивно-агрессивное напоминание о воде для Claude Code.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моды Claude Code от Herman (marketplace herman-mods).
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живые индикаторы стоимости, контекста и квоты плана над…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Мод Claude Code, который задерживает разветвление субагентов, запросы с большим…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Мод Claude Code, который включает и отключает глобальные навыки, агентов…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Плагины Claude Code (моды): переключение между несколькими аккаунтами Claude…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Протестированные Claude Code-моды, устанавливаемые одной командой: защитные…
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Титры в стиле кино для вашей сессии программирования.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Учите иностранный язык во время работы с Claude Code.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude Code mods for running many sessions across many repos from one control…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Когда Agent пишет Java, код, нарушающий правила Alibaba Java (p3c), не попадает…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Боковая панель с отображением стоимости, токенов и использования контекста в…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Модификация Claude Code: список последующих действий, которые Claude предлагает…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Интернет-радио внутри Claude Code: боковая панель cliamp, мини-плеер…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Fun, useful Claude Code mods: a pixel critter above your prompt, a tools menu…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude готовит. Общайтесь со своей командой.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Коллекция модификаций Claude Code от jack.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Модификация Claude Code: ловите пиксельных Modsters в игре в режиме ожидания…
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Модификация Claude Code «всё в одном»: интерактивный HUD, защитные механизмы…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Космическая битва над приглашением Claude Code во время его работы.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Посмотрите, какие файлы есть в контексте каждого агента Claude Code и какая…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Сохраняйте холодную голову. Термометр для ваших дней с Claude Code: каждый час…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Кэш промпта, контекст и ограничения плана для Claude Code как на ладони — в…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Модификация Claude Code: панель в реальном времени с PR GitHub, которые сессия…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Небольшие моды Claude Code для терминала и настольного приложения.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Коллекция модификаций Claude Code, каждая в собственном репозитории…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Модификация Claude Code: панель прогресса для задач, субагентов, запусков…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Модификация Claude Code: кликабельное оглавление всего сеанса с временными…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Модификация Claude Code: ограничения частоты плана, заполненность контекста…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навык + мод Claude CLI, добавляющий испанские слова в ответы агента.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Встраивайте Alarum.me в Claude Code CLI или Desktop.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Боковая панель в стиле Evangelion для Claude Code: контекст, квота, активность…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Мод Claude Code, который стилизует его под The Machine из Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: модификация Claude Code для обязательных проверенных рабочих…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Моды с открытым исходным кодом для Claude Code: панели, строки состояния…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Мод Claude Code: статус сессии, живой прогресс Spec Kit и управление окном…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Окно контекста в виде строки над запросом, отображаемое так же, как Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Интерактивный HUD задач для Claude Code Desktop: полоса над запросом во время…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Бесплатный плагин с открытым исходным кодом для Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod that shows images inline in Ghostty and kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Мод Claude, показывающий pull request.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навыки Claude Code: проверка фактов в документации, аудит кода, журнал памяти…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Модификация Claude Code: строки кода за сегодня по версии Claude — добавленные…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Модификация Claude Code: кликабельные пути в ответах — нажмите на папку, чтобы…
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Мод Claude Code: выбирает /effort для каждого запроса с помощью Jev.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагин-компаньон Claude Code: ASCII-компаньон над запросом, который помнит ваши…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Модификации Claude Code: уровень безопасности для Claude Code — удаление…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Плагин и мод Claude Code: AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Коллекция отличных модов Claude Code | 모드 모음집 Claude Code.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Уютный мод с интерфейсом RPG для Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Он говорит: мод Claude Code, который по запросу зачитывает вслух ответы Claude…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Моды Claude Code по запросу — навык, который читает ваш разговор и создаёт…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Отшлёпайте Claude, когда он ошибается — модификация Claude Code для снятия…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Моды Claude Code: небольшие плагины для интерактивных панелей, маршрутизации…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Мод и плагин Claude Code: монитор использования, отслеживание токенов и…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Три бесплатные модификации Claude Code: скрытие значений .env в результатах…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Моды Claude Code. touch-map: просматривайте в виде дерева и карты активности…
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Магазин плагинов Claude Code для модов 0xnicholasy.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Модификация Claude Code: индикаторы прогресса использования.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Модификации Claude Code: карточки статистики сессии над полем запроса.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анимированный кот из шрифта Брайля над приглашением Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Мод Claude Code: направляет недорогие задачи в GLM/Kimi через дочерний Claude…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Пиксельный кот над запросом Claude Code, который запускает тестовый звонок…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, который выбирает подходящий момент для компактизации, чтобы…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модификации Claude для Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Маркетплейс плагинов Claude Code от anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Мод Claude Code: 5-часовое и недельное использование вашего плана в виде одной…
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Модификации Claude Code для наблюдения за рынком из терминала: панель A股/港股/美股…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Модификации для Claude Code.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - Мои частные моды Claude Code.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Корабль LGTM Lines проплывает мимо после каждого изменения кода — мод Claude…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code моды для команды S2 (маркетплейс ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткие тренировки, пока Claude работает: ежедневная цель, серии, значки и…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Прогресс планов, задач и агентов рядом с полем запроса Claude Code…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Доска использования для Claude Code: расходы по моделям.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Мод для Claude Code: разбивка окна контекста в реальном времени над полем…
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Мод Now Playing для Claude Code: Apple Music и Spotify над приглашением, с…
- [bitcars/ctx-bar](https://github.com/bitcars/ctx-bar) - ctx-bar: a Claude Code mod that keeps the context window visible at all times.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Моды для Claude Code: часы кэша, радиус поражения, предложения, рабочий список…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашего Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Однострочная полоса Claude Code.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Оригинальный движок Doom с Freedoom, доступный внутри Claude Code.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Мод Claude Code: расчётные затраты электроэнергии ⚡ и воды 💧 для каждого хода и…
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Модификация Claude Code, которая ведёт список открытых вопросов в разговоре и…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моды Claude Code для настоящих инженеров.
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Модификации Claude Code только для команды d3nim.
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Моды Claude Code: rule-keeper сохраняет ваши исправления как постоянные правила.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Тамагочи, живущий внутри Claude Code: он вылупляется, ест код, который пишет…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Модификации для Claude Code в формате магазина плагинов.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Мод Claude Code: показывает время каждого запроса и ответа в терминале и…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Моды Claude Code, написанные как хуки функций, и маркетплейс, на котором они…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Мод для Claude Code: после того как guard блокирует вызов инструмента…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Мод для Claude Code: фоновые задания в одном представлении с прогрессом и…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Мод для Claude Code: единый входящий ящик для сообщений от товарищей по…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Мод для Claude Code: объясняет блокировки песочницы и превращает повторные…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Избранное для Claude Code: значки команд и навыков с запуском одним щелчком.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Эй, заглушили! Брось diff, срежь riff, больше никаких правок, меньше credits.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - Модификации для claude.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code-моды: delete-guard (подтверждение удаления файлов) и octopus-crew…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Мод Claude Code: использование подписки (5h / 7d) в виде полосы над prompt в…
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code mod: your background agents as pixel critters, one sprite per model.
- [FeidaWang/edit-replay](https://github.com/FeidaWang/edit-replay) - Edit Replay: step through the file edits Claude made in the last turn, one diff…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Интерактивный радар параллельных веток и рабочих деревьев над запросом: какие…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Модификация Claude Code для захвата мыслей во время работы, их распределения по…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Модификации и темы оформления для Claude Code: интерактивная полоса прогресса…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Моды для Claude Code (плагины с хуками функций): полоса контекста…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Семь модификаций Claude Code: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Копирование ссылки сочетанием Ctrl+щелчок в каждом блоке кода в ответах Claude…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Моды для Claude Code: плагины хуков, например usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Моды Claude Code (плагины function-hook), устанавливаемые через единый…
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Модификации Claude Code: context-bar-plus.
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Статический аудитор цепочки поставок для модификаций Claude Code — локальный…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Модификации Claude Code на немецком языке: сведения о контексте и кэше…
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code mod: capture ideas into an Obsidian vault inbox from any session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Модификация Claude Code: сколько времени занял каждый ответ, сколько времени…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Мод Claude Code: streamer-mode скрывает приватные панели, полосы и строку…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - для моих модификаций claude.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Модификация Claude Code: пережидает 5-часовой лимит использования и отправляет…
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Небольшие модификации для Claude Code, начиная с автоматического продолжения…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Пульт управления над полем запроса Claude Code. Утка считывает показания.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Небольшие модификации Claude Code: индикаторы использования контекста и плана…
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: a Claude Code mod with a side pane showing where each work item…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Мод Claude Code: отдельная панель для каждого субагента, файлов, которых они…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Боковая панель с использованием контекста: общий объём, категории, рост за…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Боковая панель со списком файлов: какие файлы были созданы, изменены или…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пушистик в стиле 8-bit (чёрно-белый вислоухий голландский кролик) бегает и…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Боковая панель «Что я спрашивал»: каждое сообщение владельца в этом разговоре;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Боковая панель с временной шкалой: на что ушло время в этом раунде — ожидание…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Боковая панель обмена токенами: сколько токенов основной разговор отправляет…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Честный пакетик с бобами для claude code: после каждого раунда Claude тихо…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Небольшие моды для Claude Code, например новые команды со слешем и боковые…
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Неофициальное руководство сообщества по модификациям Claude Code (хуки функций)…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живет в полосе над вашим prompt Claude Code: разыгрывает сессию…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод, озвучивающий ответы и уведомления Claude Code с помощью VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Модификация Claude, позволяющая читать и объединять разговоры между вашими…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Модификация Claude Code: работающие субагенты в виде пиксельных маскотов Claude…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - моды claude.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Моды Claude Code (usage-meter и другие).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Два мода Claude Code: folio — панель файлов рядом с чатом, и tint…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph oh what Claude Code knows.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Не позволяйте своему вниманию отвлекаться, пока вы ждёте ответа Claude Code.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Модификации Claude Code для проектов Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Подготовленное сообществом руководство по модам Claude Code: варианты…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод Claude Code, который показывает, что делает Claude, в подзаголовке вкладки…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Пушистая чёрная кошка над вашим промптом Claude Code.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Модификация Claude Code с переключаемыми профилями разрешений: безопасная…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Моды сообщества для Claude Code: защиты, панели и команды, выполняемые внутри…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Боковая панель для Claude Code: файлы, созданные Claude, разделы терминала…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Тихая боковая панель для Claude Code: чем занята эта сессия, её план, агенты и…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Тусклое время над каждым приглашением и каждым ответом в транскрипте Claude…
- [mmedum/spor](https://github.com/mmedum/spor) - Возвращает то, что Claude Code сворачивает: файлы, которые прочитал Claude…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Модификация Claude Code: использование окна контекста в слоте режима нижнего…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, включающий обратно инструменты todo для моделей, которые их не…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одной строке на каждую задачу над запросом — текущая…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Играйте в Connect Four против AI внутри Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Мод Claude Code: когда другой агент программирования делает коммит в ваш…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Мод Claude Code для репозиториев, которыми пользуются несколько ИИ-агентов: не…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods marketplace.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Защитный механизм для SQL в Claude Code: запрашивает подтверждение перед тем…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Один мод для Claude Code и Windows, с приоритетом CJK: предварительный просмотр…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Лучшие моды Claude Code, отсортированные по пользе для вас.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Мод Claude Code, который задерживает рискованные shell-команды.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Два мода Claude для Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Модификации Claude Code с телеметрией агентов, панелями временной шкалы…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Ругайтесь на Claude Code — и мультяшная рука даст сдачи.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Модификации Claude Code: usage-both показывает использование за 5 часов и за…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Боковая панель со статистикой сеанса в реальном времени для вкладки Code…
- [PhilRoli/traintracker-claude](https://github.com/PhilRoli/traintracker-claude) - Claude Code mod: pause sessions before your TrainTracker train arrives.
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Моды Claude Code для интерфейса pompeitech, оформленные в стиле системы дизайна…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Моды для Claude Code: safety-guard блокирует разрушительные команды и доступ к…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Модификации для Claude Code: плагины function-hook, работающие внутри сеанса…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Мод Claude Code: текущая биржевая лента, панель /quote, оповещения о ценах…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code mod: keeps auto-memory up to date in the background after every turn.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Мод Claude Code: хост SSH, оперативная память и ограничения использования 5h/7d…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Мод Claude Code: отжимания, которые нужно делать, пока работает Claude.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 модов Claude Code на корейском языке: запись предположений, простой язык…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Мод Claude Code: превращает план, который вы утверждаете в plan mode, в живой…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Подборка Claude Code-модов. Каждый элемент клонирован и проверен с помощью…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Бесплатный режим: вспомогательные агенты работают на Haiku, а большие файлы и…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музыка в стиле lofi, сопровождающая сессию: спокойствие, концентрация, поток, а…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Учитесь, пока Claude пишет код: после хода, изменившего код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запись каждого изменения, которое вносит Claude: воспроизводите каждое…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Каждая ссылка, упомянутая в вашей сессии, в одной строке над приглашением.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code function hooks — минимальная демонстрация: интерактивная панель…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Мод Claude Code: 5h-, недельный и Fable-лимиты в виде полосы над приглашением.
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in a terminal pane…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Коллекция плагинов для Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: неофициальный фанатский мод по Avengers для Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Модификация Claude Code для контекста, роста, квоты, кэша, нативной стоимости и…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Мод Claude Code: направляет простые запросы и субагентов к более дешёвым…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Персональные моды Claude Code.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - The original DOOM in a Claude Code pane with nothing to install: the engine…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commit messages в один клик для Claude Code с танцующей pixel-art Malenia.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Персональные моды Claude Code.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Место для локально используемых модов Claude Code.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — мод Claude Code, показывающий использование вашего плана Claude…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, отображающий текущую сессию на панели: каждое приглашение…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Plugin marketplace модов Claude Code: function-hooks plugins, которые рисуют…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Репозиторий для управления модами Claude Mods.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Настройки для Claude Code.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Некоторые моды Claude.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Мод Claude Code, проверяющий английский язык вашего приглашения во время его…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Кураторский каталог модов Claude Code, каждый из которых содержит промпт для…
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Моды Claude Code: индикатор контекста и лимита плана над промптом и…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Мод для Claude Code: квота 5h/7d, окно контекста, оставшееся время кэша промпта…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анимированная полоса прогресса и сводка по завершении для…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Три небольших мода Claude Code: узнайте, когда завершат работу ваши субагенты…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Уменьшает большие снимки экрана перед тем, как Claude их прочитает, чтобы…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажите «Я потерялся», и Claude снова объяснит свой последний ответ простыми…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Показывает предлагаемые следующие промпты над полем ввода.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Задайте Claude дополнительный вопрос на панели рядом с вашей работой.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Маркетплейс модов Claude Code с установкой в один шаг и видеоинструкцией на…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Обратный отсчёт до снятия ограничения частоты и прогноз темпа расходования для…
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Плагин Claude Code: лимиты использования Claude Pro/Max с прогнозом темпа…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моды для Claude Code. agent-crew: наблюдайте за работой субагентов как за живой…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Встраивание и отображение математических формул LaTeX, а также необязательных…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Интерактивная доска задач для Claude Code: планируйте перед началом работы…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Мод Claude Code, который в реальном времени сообщает, какие файлы изменил…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Отобранная вручную коллекция лучших ресурсов для самых потрясающих агентов…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Плагин Claude Code, показывающий, что происходит: использование контекста…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Красивая, полностью настраиваемая строка состояния для Claude Code CLI с…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Все части системного промпта Claude Code, 27 встроенных описаний инструментов…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Более 45 советов по максимально эффективному использованию Claude Code — от…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Красивый powerline в стиле vim для Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Просматривайте diff вашего агента кодирования в панели терминала и отправляйте…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Комплексный плагин статусной строки для Claude Code с использованием контекста…
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Полноформатный агент для ролевых игр в DeepSeek Harness (плагин DSH Tavern)…
- [L-Forster/open-jet](https://github.com/L-Forster/open-jet) - An offline coding agent for local models.
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Fast, zero-dependency cost calculator and customizable statusline for Claude…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Строка состояния терминала для сессий Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Онлайн-счета футбольных матчей, расписание и турнирные таблицы для…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Локальная плоскость управления для Claude Code на Windows и macOS: переключение…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Личная конфигурация Claude Code, версионируемая внутри ~/.claude — агенты…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Время молитв, дата по хиджре, азкары, ежедневный аят, пост по сунне, Рамадан…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Строка состояния с осведомлённостью о сессии для Claude Code.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Двухстрочная статусная строка truecolor для Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - A floating peak/off-peak tide card for DeepSeek Harness: i18n (en/zh/ru)…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Портативный набор инструментов Claude Code для .NET DDD/Clean Architecture…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Переносимая глобальная конфигурация Claude Code: пользовательские навыки, хуки…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагины Claude Code, которые я использую каждый день: навыки и моды…
- [chaybits/ai-session-usage](https://github.com/chaybits/ai-session-usage) - Claude Code and ChatGPT (Codex) subscription limits in one card: a KDE Plasma 6…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Управление токенами для Claude Code: лучшая модель направляет работу, а…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Статусная строка текущей фазы рабочего процесса для Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Сократите расходы на токены Claude Code и Codex: направляйте запросы и тестовые…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Простая и полезная настройка строки состояния для Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Оповещения об ограничениях использования для Claude Code: уведомления macOS…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Настраиваемая строка состояния Claude Code для Linux, WSL, Windows и macOS с…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Быстрая строка состояния Rust для Claude Code — сначала данные, кэшированный…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Живая панель использования для Claude Code — разбивка контекста, cache hits…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Строка состояния и строка токенов для Claude Code: контекст, использование за 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Отображение ключевых сведений о состоянии Claude Code, включая модель…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - Дружелюбная строка состояния Claude Code, которую можно настраивать до мелочей…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Многострочная строка состояния Claude Code: расходы, процент контекста, git и…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Строка состояния с полезной информацией для claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Нативные команды агентов. Под контролем.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Дополнения Claude Code: наблюдатель цветных точек статуса вкладок + встроенная…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Строка состояния использования Claude Code для macOS и Linux, упакованная как…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Пользовательская statusline для Claude Code — панель контекста с процентом…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Чистая информативная строка состояния для Claude Code — показывает проект…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod: a CRT-style status panel for Claude Code, in the terminal…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Маркетплейс плагинов Claude Code с baloo: навыки, агент, проверяющий изменения…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Профессиональная строка состояния Claude Code: длительность сессии, стоимость в…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Строка состояния Claude Code с учётом подписки.
- [dave-net-positive/Claude_Code_PII_Redactor](https://github.com/dave-net-positive/Claude_Code_PII_Redactor) - Mod that detects and redacts PII in Claude Code before it reaches the model.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Расширенная строка состояния терминала для Claude Code — Bun + TypeScript, без…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Плагин Claude Code, который красиво отображает диаграммы Mermaid в транскрипте…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Инструменты, skills и агенты для Claude Code — начиная со status line…
- [FunDrivenDev/claude-plugins](https://github.com/FunDrivenDev/claude-plugins) - Public Claude Code plugins: a context-budget status line.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Пользовательская статусная строка Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Фактические расходы DeepSeek API для Claude Code: перерасчитывает стоимость…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Предпросмотр изображений внутри Claude Code: наведите курсор на чип под…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Моды для Claude Code и Claude Desktop в Windows с WSL: Docker и…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Строка состояния Claude Code со строками панели агентов.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Синхронизируйте задачи Claude с Fizzy.do, чтобы команда видела изменения в…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Коллекция навыков, модов и других дополнений для Claude Code, которые я создал…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Меню настроек, строка состояния и конфигурация Claude Code.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - Самодельные плагины, навыки, моды claude без клеток и многое другое.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Установщик окружения Claude Code: skills, statusline, hooks, permissions и…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Строка состояния в стиле HUD для Claude Code — состояние сети, TPS, контекст…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Плагины и модификации Claude Code для понимания того, что делает Claude…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Красочная многострочная строка состояния для Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Строка состояния Claude Code для Windows (PowerShell): индикаторы…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Модификация Bearings and Glossary для Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Конфигурация и моды Claude Code с общей библиотекой компонентов, песочницей и…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - A small dashboard for Claude Code: context %, cache countdown, 5-hour &amp; weekly…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Custom terminal status bar for Claude Code: model, directory, git state…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Портативная конфигурация Claude Code: CLAUDE.md, settings, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Мод Claude Code для настольной версии (macOS): уведомления о сеансах с…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Мод-компаньон для чтения с экрана для Claude Code (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Практическое проверенное подробное руководство по Claude Code — CLAUDE.md…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Строка состояния Claude Code для отслеживания стоимости и мониторинга сессии в…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Строка состояния Claude Code: папка, ветка git, модель, использование…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Детектор деградации контекста 2026 — проактивный монитор памяти ИИ и лимитов…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, субагенты и statusline для Claude Code: open-source коллекции и…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Визуальный конструктор статусных строк Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Статусная строка Claude Code с отображением использования токенов в реальном…
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Строка состояния Claude Code: эстетика CCometixLine + функциональность HUD…

</details>

<a id="dsh-cordis"></a>

## Экосистемы плагинов DSH и Cordis

DeepSeek Harness и Cordis приходят к тому же результату с другой стороны: для них плагин является механизмом модификаций, поэтому плагин там эквивалентен моду здесь.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74325 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **74325**  |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100497 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **100497** |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐87809 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **87809**  |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81879 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **81879**  |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35759 · Go · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **35759**  |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8626 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Экосистема агрегации веб-плагинов DeepSeek Harness (DSH) · Всё является плагином, распространяемым через Мастерскую творчества ｜｜Экосистема агрегации веб-плагинов DeepSeek Harness (DSH) · Всё является плагином, распространяемым через Мастерскую творчества

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **8626**   |
| Последний push   | 2026-10-10 |
| Впервые в списке | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6146 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Рынок плагинов внутри DeepSeek Harness — просмотр, поиск, установка одним щелчком · Визуальный рынок плагинов DSH

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **6146**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4478 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness（DSH）интерактивная китти, живущая в правом нижнем углу интерфейса DSH и следящая за балансом аккаунта DeepSeek. Упругая и живая, поддерживает перетаскивание с прилипаниями, переворот при прилипаниях слева и анимацию прокрутки цифр, автоматически включается вместе с интерфейсом; рекомендуется просто вызвать её при установке dsh

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **4478**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4285 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Официально рекомендуемый TUI-плагин для DSH — высокая производительность, низкое потребление ресурсов, милый пиксельный кит и плавное взаимодействие с мышью. Установка одной командой через npm. / Официально рекомендуемый TUI-плагин для DSH: высокая производительность, низкое потребление ресурсов, милый пиксельный кит, плавное взаимодействие с мышью, установка одной командой через npm

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **4285**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3153 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3153**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1983 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Лучший плагин DeepSeek Harness для анализа и управления контекстом: панель контекста, браузер, боковая панель и команда контекста для статистики контекста, анализа состава, детализации, отслеживания изменений и понимания того, как формируется и развивается контекст. Одностраничный плагин визуализации контекста DeepSeek Harness: панель Context, браузер, боковая панель и команда Context для анализа состава, развития, сжатия, обрезки и других событий и действий с контекстом.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1983**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1561 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

跨设备的开源Agent工作台

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1561**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1464 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Python                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1464**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1401 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Программа для создания AI-романов: организует идеи, персонажей, мир, план, написание глав, рецензирование и редактирование в управляемый процесс; предоставляет настольные версии для Windows/macOS, поддерживает локальные и онлайн-модели. Программа для написания AI-романов: организует идеи, персонажей, построение мира, планы, написание глав, рецензирование и редактирование в управляемый процесс. Включает настольные приложения для Windows/macOS, интеграцию с Ollama и предварительную версию плагина DeepSeek Harness (DSH).

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1401**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **1171**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness (dsh) Windows desktop-клиент — в комплекте Node.js + dsh CLI, запуск в один клик

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **704**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐283 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Just open your browser — get all your work done.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **283**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

ACRYL - Agent Context Relay Yielding Lifecycles. Одно постоянное рабочее пространство, один канонический контекст, любой агент программирования.

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
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Нативный плагин DeepSeek Harness (DSH), интегрирующий TypeSafe Jev или Decision api, например luna, в качестве System One уровня принятия решений для выбора, контроля, исправления и утверждения действий агентов.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **203**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Делегирование задач со сдвигом по времени для DeepSeek Harness (dsh): планируйте задачи в удобное время, они выполняются без присмотра в непиковые часы, а затем вы получаете отчёт. Решения принимаются человеком, поддерживаются desktop и web.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **170**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин DeepSeek Harness для предпросматриваемой миграции сессий между пресетами. Передачи с фиксированной схемой сохраняют состояние, намерение исходной модели и неразрешённые изображения; исходная сессия остаётся нетронутой.

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
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

После установки вы сразу получаете 27 навыков для разработки и повышения эффективности из mattpocock/skills v1.3.1 — устанавливать навыки вручную не требуется. Плагин создан с использованием 40 млрд токенов и обеспечивает десятикратное повышение эффективности разработки по сравнению с исходными навыками, а также помогает новичкам быстрее освоить этот набор. Полностью поддерживаются GitHub issue; Markdown находится в режиме предварительного просмотра; GitLab пока не поддерживается. Спасибо за использование и поддержку 💗

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **134**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **133**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐131 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Тема Claude Code Desktop для DeepSeek Harness｜ Claude Code desktop-тема, созданная для веб-GUI DeepSeek Harness

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **131**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>анимированная запись</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐130 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Runtime evidence that helps agents trace, profile, and burn down hotspots in application and native code, GPU kernels, and inference stacks.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Python                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **130**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин питомца рабочего стола DeepSeek Harness: энергичная девушка-кит в качестве компаньона помогает вам писать код 🐋 Поддерживает DSH для настольных систем 0.2.0-rc.2 и старую Web-версию (desktop pet / mascot, local-first)

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **120**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **113**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐65 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **65**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Живой каталог плагинов DeepSeek Harness — обновляется ежечасно, ежедневно проверяется на совместимость, включает встроенный магазин плагинов и генератор шаблонов. Живой каталог плагинов DSH: обновление каждый час, ежедневное тестирование совместимости, встроенные магазин плагинов и генератор шаблонов.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | HTML                                                                   |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **59**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Извлечение контекста рабочего пространства и отслеживание жизненного цикла с учётом задачи для AI-агентов программирования: поиск, организация и постоянное отслеживание наиболее релевантных текущей задаче документов, кода и медиа. Полностью локально, без вызовов моделей и без сети. Отслеживание контекста рабочего пространства и жизненного цикла с учётом задачи для AI-агентов программирования. Находит, организует и отслеживает наиболее релевантный текущей задаче контекст рабочего пространства — локально, детерминированно, без вызовов моделей и без сети.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **53**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/skyf0xx/hedgehog">skyf0xx/hedgehog</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

HEDGEHOG codes Cleaner, Faster and with Fewer Tokens. Hedgehog's AI-driven development builds a task dependency graph from your spec-driven, BMAD-METHOD plan, so Claude Code, Cursor & Gemini CLI stay locked to it. A CLI-enforced state machine for agentic coding. Now builds DeepSeek DSH Plugins. DeepSeek Harness、DSH 插件、AI 编程、BMAD 方法. AI Copywriting

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **44**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-skills` · `agentic-coding` · `ai-agents` · `ai-assisted-development` · `ai-coding` · `ai-copywriting` · `ai-engineering` · `ai-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/skyf0xx--hedgehog/326d2d3a663269a4.jpg" width="100%" alt="skyf0xx/hedgehog screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐42 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин dsh — мастер игровых ресурсов. Подключается к модели генерации изображений seedream и модели генерации видео minimax, позволяет создавать различные игровые ресурсы.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **42**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин DeepSeek Harness: поддерживает точное контекстное окно модели llm-pi-ai и предотвращает ошибочное определение переполнения контекста в длинных сессиях.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **34**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/6c743bbe3da63616.jpg" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PensiveFei/deep-read-summarize">PensiveFei/deep-read-summarize</a></b> · ⭐31 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Deep reading & summarization workflow for books/papers/videos/web — plugin parsers, MapReduce deep-read, JSON Schema output, Obsidian-ready (DSH)

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **31**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agent` · `content-summarization` · `deepseek` · `dsh-plugin` · `pipeline` · `workflow`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pensivefei--deep-read-summarize/800b10f03f25fe11.png" width="100%" alt="PensiveFei/deep-read-summarize screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Отобранный список лучших отличных ИИ-плагинов для ИИ-ассистентов, включая…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Рынок плагинов DSH / DSH Plugin Marketplace: в веб-интерфейсе DeepSeek Harness…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [arcships/rutis](https://github.com/arcships/rutis) - Среда выполнения плагинов для самоизменяющегося программного обеспечения…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Избранный каталог плагинов DeepSeek Harness (DSH) — более 280 плагинов…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Набор инструментов Zotero для DeepSeek harness;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Плагин DSH: оболочка Git Bash для всех режимов агентов на Windows.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: мультиплатформенная система агентов для групповых чатов на базе…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - Офисная тройка! Инструменты документов Office для DeepSeek Harness (dsh)…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - Версия dsh для Android: интеграция DeepSeek Harness, среды выполнения Ubuntu…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Навигация по сессиям DSH.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [weishao2/tizhuang-agent-skills](https://github.com/weishao2/tizhuang-agent-skills) - 2000万+中小学K12真题题库 Skill：免费注册、免费抽题、教材/章节/知识点检索、练习测验与AI智能组卷.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Веб-плагин DSH: статистика использования токенов по дням с тепловой картой…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Подобранные сообществом плагины, инструменты, навыки и учебные ресурсы DeepSeek…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Плагин управления серверами MCP для DeepSeek Harness: страница Settings → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Плагин DeepSeek Harness: 15 инженерных навыков obra/superpowers, двуязычные…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Среда выполнения для коммерческих переговоров A2A + плагин DeepSeek Harness…
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - Интерфейс управления сервером MCP для DeepSeek Harness Web — плавающая панель…
- [liustack/pptwise](https://github.com/liustack/pptwise) - Настоящий PowerPoint, а не HTML. Расскажите ИИ, что нужно осветить, и pptwise…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催更姬：给大肥鱼一个小说工作台。写正文、理设定、画情节，和 AI 一起讨论、续写与改稿.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Плагин DeepSeek Harness · оптимизация черновика запроса одним щелчком в панели…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Экран входа для веб-интерфейса DeepSeek Harness (dsh): вход по паролю или…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Плагин AI-инженерии Embedded C/C++ — навыки работы с прошивками.
- [Chael-Chael/dsh-reference-anything](https://github.com/Chael-Chael/dsh-reference-anything) - The best DeepSeek Harness plugin for referencing anything — enhanced @ menu for…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Единый менеджер skills, subagent, MCP и LSP для DeepSeek Harness (DSH)…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Постоянное тестирование совместимости плагинов DeepSeek Harness: точные версии…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive context compaction for local-first agents.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Хост-плагин DeepSeek Harness, который хранит документы проекта и долговременную…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray для плагинов DeepSeek Harness: заявленные возможности против фактического…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - A knowledge base toolkit for research and literature review.
- [Mcd0LUO/dsh-guard-repeat-output](https://github.com/Mcd0LUO/dsh-guard-repeat-output) - Host-side degeneration guard for DSH: strips garbage code points, detects…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - Превращает ответы DSH в интерактивный интерфейс: вычисления, графики, формы…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - Проверка заявлений о дизайне и коде: фактические утверждения сопоставляются с…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Рабочее пространство с несколькими папками: позволяет агенту DSH.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Плагин инженерного рабочего процесса для DeepSeek Harness: этапы задач, записи…
- [Kr-ATG/dsh-chat-plus](https://github.com/Kr-ATG/dsh-chat-plus) - DSH 对话体验增强套件（零源码改动，纯插件注入）。Seeker 双栏执行大盘：右栏任务 / 操作面板 / 子智能体 / 产出物四张卡 +…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт проверки плагинов DeepSeek Harness (dsh) без зависимостей…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode в DeepSeek Harness — плагин DSH, поддерживающий работу OpenCode Zen и…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонний маркетплейс плагинов и защищённый менеджер жизненного…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx — это ориентированная на человека расширяемая настольная рабочая среда…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Укомплектованный всем необходимым агент программирования для DeepSeek Harness…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Плагин ввода DSH Web: переключение клавиш отправки и перевода строки…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Предоставляет настольной версии DeepSeek Harness удалённый доступ «только из…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — набор инструментов для локального развёртывания и эксплуатации…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Веб-плагин DeepSeek Harness (DSH): вкладка боковой панели market-dashboard для…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Делает повторно запускаемой неатрибутированную попытку с пустой моделью для…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Плагины, которые убирают за собой: порт фреймворка плагинов cordis для iOS и…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Пресет агента DeepSeek Harness: Codex и Claude Code в качестве субагентов…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Среда выполнения плагинов Rust с проверенным Verus ядром жизненного цикла и…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Тексты, обсуждения и видео

Статьи, обсуждения и видео о возможностях модов.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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

| Язык       | Записей | Примеры                                                                                                            |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 322     | `anthropics/claude-code`, `anthropics/claude-code-action`, `karanb192/cache-tax`                                   |
| JavaScript | 69      | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `augiefra/claude-mods`                         |
| Python     | 32      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`      |
| Shell      | 19      | `anthropics/claude-agent-sdk-typescript`, `andrewbakercloudscale/claude-code-cost-sidebar`, `Gharib89/claude-mods` |
| HTML       | 12      | `awss1i/assay`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                                       |
| Go         | 6       | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                         |
| Rust       | 5       | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`                  |
| PowerShell | 2       | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                                |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                            |
| Kotlin     | 1       | `dphmoblie/deepseek-harness-android`                                                                               |
| MDX        | 1       | `jkf87/mod-guide`                                                                                                  |
| Swift      | 1       | `eovidiu/cordis-ios`                                                                                               |

<sub>Учитываются только записи, в которых указан язык. Документация и обсуждения исключены из этой таблицы.</sub>

## Участие

Исправления приветствуются и являются самым быстрым способом улучшить этот список. Откройте issue или pull request, если запись попала не в тот раздел, получила неверную оценку или если проект был ошибочно исключен как совпадение имени — именно в этой последней категории автоматические фильтры чаще всего ошибаются.

---

<sub>Независимый проект сообщества. Не аффилирован с Anthropic, не одобрен и не проверен им. Claude Code, Claude и Anthropic являются товарными знаками Anthropic. Поведение продукта может меняться без уведомления; всё критически важное проверяйте по официальной документации. Материалы остаются собственностью исходных проектов и воспроизводятся только там, где это разрешено лицензией.</sub>

<sub>Последнее обновление · 2026-10-11T21:12:49+08:00</sub>
