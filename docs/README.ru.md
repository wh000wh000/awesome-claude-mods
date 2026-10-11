<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Отличные моды для Claude">
</p>

<h1 align="center">Отличные моды для Claude</h1>

<p align="center"><b>Индекс модов, плагинов Claude Code и более глубоких изменений поведения, составленный с оценкой доказательности.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-595-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <b>Русский</b> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Актуальный индекс** · Последняя синхронизация: `2026-10-12T03:53:55+08:00` (UTC+8)
> · Записей: **595** · Добавлено в последнем обновлении: **0** · Языки реализации: **12**

<sub>Каждая запись ниже была автоматически собрана, отфильтрована и проверена повторно. Здесь нет платных размещений.</sub>

<a id="featured"></a>

## Лучшее на данный момент

<sub>По одной записи на категорию, ранжирование по степени подтверждённости и количеству звёзд, пересчитывается при каждом обновлении. Это рейтинг, а не рекомендация; каждая подборка ведёт к полной карточке ниже. Предпочтение отдаётся проектам, опубликовавшим снимок экрана или запись, чтобы лента оставалась визуальной.</sub>

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
<sub>⭐2535 · Python · 👁️ observed</sub>
<sub>Найдите призрачные токены. Исправьте их. Переживите компактификацию. Избегайте ухудшения качества контекста.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74351 · TypeScript · 👁️ observed</sub>
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
- [Официальные: собственные репозитории и примечания к выпускам Anthropic](#официальные-собственные-репозитории-и-примечания-к-выпускам-anthropic) — **14**
- [Моды: созданы с использованием возможности модификации](#моды-созданы-с-использованием-возможности-модификации) — **464**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150197 · TypeScript · ✅ official · 0 天</summary>

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
| Звёзды           | **150197** |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9478 · TypeScript · ✅ official · 2 天</summary>

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
| Звёзды           | **9478**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| Звёзды           | **8249**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6345 · Python · ✅ official · 242 天</summary>

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
| Звёзды           | **6345**   |
| Последний push   | 2026-02-11 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| Звёзды           | **1798**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary><b>Больше в этой категории</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Добавлен `$.ui.notify` для модов: вызывает нативное уведомление через ваши…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Исправлена ситуация, когда Esc или прерывание во время хука `UserPromptSubmit`…

</details>

<a id="mods"></a>

## Моды: созданы с использованием возможности модификации

Каждая запись здесь демонстрирует использование возможности, которую Claude Code получил в версии 2.1.287: она выполняет отрисовку через `ui.render`, владеет панелью, полосой или карточкой, читает `$.ui.selection()`, создаёт товарищей с помощью `agent.spawn` или прямо указывает, что является модом.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2535 · Python · 👁️ observed · 0 天</summary>

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
| Звёзды           | **2535**   |
| Последний push   | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐493 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Каталог сообщества публичных модификаций Claude Code (функциональных хуков), просканированных из GitHub, с указанием того, что каждая модификация может читать, записывать, запускать или отправлять по сети. Просмотреть https://mods.aidojo.si/

<sub>🔧 Найдено использование в коде: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | JavaScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **493**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐187 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **187**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐137 · TypeScript · 👁️ observed · 7 天</summary>

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
| Звёзды           | **137**    |
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
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐80 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **80**     |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐76 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **76**     |
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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐67 · TypeScript · 👁️ observed · 8 天</summary>

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
| Звёзды           | **67**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Сводка

Экспертные skills, агенты, команды, правила, хуки и стили вывода для Claude Code — непрерывность сессий + современные инструменты CLI для реальных рабочих процессов разработки

<sub>🔧 Найдено использование в коде: `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | Shell                                                                     |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **59**     |
| Последний push   | 2026-10-07 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 8 天</summary>

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
| Звёзды           | **50**     |
| Последний push   | 2026-10-03 |
| Впервые в списке | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Сводка

Моды Claude Code: индикаторы прогресса плана в реальном времени над приглашением

<sub>🔧 Найдено использование в коде: `README.md`</sub>

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **46**     |
| Последний push   | 2026-10-08 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>анимированная запись · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Открыть видео</a></sub></td>
</tr></table>

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
| Последний push   | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
| Звёзды           | **11**     |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

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
| Звёзды           | **11**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

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
| Звёзды           | **11**     |
| Последний push   | 2026-10-05 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

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
| Последний push   | 2026-10-08 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
| Звёзды           | **7**      |
| Последний push   | 2026-10-04 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Смотреть на youtube.com</a> · воспроизведение открывается на сайте-источнике; GitHub не может встроить его в страницу</sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Сводка

Моды Claude Code: панель использования 像素螃蟹 usage-hud + HTML-ссылки, по которым можно нажимать в терминале, и карточки кода для копирования одним нажатием html-shelf

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
| Последний push   | 2026-10-08 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>анимированная запись</sub></td>
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
<summary><b>Больше в этой категории</b> <sub>· 430</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Модификации Claude и инструменты для их создания: сначала навык-сборщик, затем…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Среда Claude Code, которую я запускаю каждый день, публикуемая под этим именем…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Наденьте новую крышу на Claude Code с помощью Claude Mods: не изменяя бинарный…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Четыре мода Claude Code: Cache Keeper, Recording Mode, Goal Meter и Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Моды Claude Code от Learning Hacker: сделайте работу агента понятной для…
- [kakha13/claude](https://github.com/kakha13/claude) - Моды Claude Code, исправляющие и переводящие ваши подсказки до того, как их…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Моды и навыки Claude Code от Nekyia Labs, создаваемые и ежедневно используемые…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Модификация, придающая терминальному журналу Claude Code вид настольного…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Боковая панель для кода Claude: субагенты, запускаемые сессией, выполняемая…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - База знаний Obsidian с указанием источников о модах Claude Code: как они…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Панель боковой панели Claude Desktop (вкладка Code): перечисляет все…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Навык, обучающий агентов Claude Code создавать Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Полоса использования над полем ввода Claude Desktop (вкладка Code): лимиты 5h /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Пользовательские моды, плагины и навыки Claude, устанавливаемые из одного…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (плагины с перехватчиками функций) для Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Галерея модов Baselane: моды Claude Code, проверенные и закреплённые.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Очередь решений CLI/TUI для людей, работающих с разговорными агентами.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плавающая карточка состояния для Claude Code — модель, контекст, ограничения…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Моды Claude Code: screen-guard маскирует имена и секреты во время демонстрации…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Интерактивная панель GSD для Claude Code: дорожная карта, дерево агентов с…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Расширения Claude Code. Раскройте всю мощь Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Мод Claude Code (плагин), который добавляет боковую панель с вкладками…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Панели, защитные механизмы и полезные моды для Claude Code: контекст…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Два мода Claude Code над полем приглашения: измеритель контекстного окна…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Продлите действие плана Claude Pro: моды Claude Code для точного HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Чтение markdown-файлов, которым код Claude даёт имена, с отображением рядом с…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Голосовой напарник для Claude Code. Обсуждайте задачи с 3D-волком на базе…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Моды Claude Code: typing-speed, спидометр скорости печати в реальном времени со…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Фейерверки для Claude Code: каждое нажатие клавиши, вызов инструмента, коммит и…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Находите моды, плагины и расширения Claude Code с анимированными…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Мод Claude Code: диаграммы mermaid, встроенно отображаемые в расшифровке.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Небольшие моды Claude Code (плагины с перехватчиками функций): session-switcher…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Мод Claude Code: миниатюры вставленных изображений над приглашением в любом…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Моды Claude Code: меню инструментов Claude, режим Zen, темы терминала, элементы…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Моды Claude Code: mod-scout (поиск наиболее нужных вам модов), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Два мода Claude Code для одновременного запуска множества сеансов: карточка…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: поиск, просмотр, переключение и обновление модов Claude Code.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Моды Claude Code: панель контекста, панель агентов, размытие PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Лучшие моды Claude Code: отобранные вручную, проверенные, закреплённые.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Плагин Claude Code: автоматическая маршрутизация моделей Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Шесть модов для Claude Code: анимированный маскот Clawd, индикаторы лимита…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Маркетплейс модов для Claude Code: пошаговый отладчик цикла агента, подсказки…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Шесть модификаций Claude Code: ограничения плана и контекст над полем запроса…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Лучший универсальный набор модов для Claude Code: лимиты использования и HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Смотрите YouTube Shorts в своём Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набор инструментов Naren для Claude: skills, mods и MCP servers для Claude…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Мод Claude Code, отображающий различия Edit и Write в двух расположенных рядом…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Моды для Claude Code: Clawd, крошечный пиксельный талисман, который показывает…
- [reporails/arcade](https://github.com/reporails/arcade) - Классические компьютерные игры в виде модов Claude Code, в которые можно играть…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Кураторский список модификаций Claude Code, устанавливаемых как через…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Моды Claude Code по запросу — навык, который читает ваш разговор и создаёт…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Крайне авторский плагин Claude Code, созданный любителем Rust, одержимым…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Моды Claude Code, которые помогают агенту не отклоняться от цели — перехватчики…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Моя коллекция модов для Claude Code, по одному моду в каталоге.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Пассивно-агрессивное напоминание о воде для Claude Code.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - The Claude Code mods I use.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Дашборд macOS notch для Claude Code: лимиты использования, открытые сессии…
- [Danovich/turntype](https://github.com/Danovich/turntype) - A typing test for the time while Claude works. A Claude Code mod.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Мод для Claude Code: панель кэша промптов, следующие шаги, быстрые кнопки и…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Моды для Claude Code: панели, команды и хуки, созданные с помощью плагина…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Trims huge tool outputs before they fill Claude Code.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Мод Claude Code, отображающий ваши лимиты использования и расходы в полосе над…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моды Claude Code от Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Моды для Claude Code: индикаторы выполнения планов, журнал того, что Claude…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Смотрите, что Claude Code запускает в фоне: субагенты, задания Codex, shell…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods by MacLeod Labs: streams untangles a session.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Полевые заметки первого дня о модах Claude Code на Windows: топливная шкала…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Моды, которые я создал и лично использую в своей конфигурации Claude Code.
- [olddonkey/cache-refresher](https://github.com/olddonkey/cache-refresher) - Claude Code mod: shows when the prompt cache expires and what a lapse would…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живые индикаторы стоимости, контекста и квоты плана над…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Мод Claude Code, который задерживает разветвление субагентов, запросы с большим…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods для claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Мод Claude Code, который включает и отключает глобальные навыки, агентов…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Плагины Claude Code (моды): переключение между несколькими аккаунтами Claude…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Протестированные Claude Code-моды, устанавливаемые одной командой: защитные…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Моды для Claude Code: плагины, созданные на основе function hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Титры в стиле кино для вашей сессии программирования.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Собственный маркетплейс модов-плагинов для Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Набор модов для claude code, созданных мной.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Моды Claude Code. touch-map: просматривайте в виде дерева и карты активности…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Учите иностранный язык во время работы с Claude Code.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Модификации Claude Code для запуска множества сеансов в множестве репозиториев…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Когда Agent пишет Java, код, нарушающий правила Alibaba Java (p3c), не попадает…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Боковая панель с отображением стоимости, токенов и использования контекста в…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Модификация Claude Code: список последующих действий, которые Claude предлагает…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Goal, tasks and agents above your Claude Code prompt — zero setup.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Интернет-радио внутри Claude Code: боковая панель cliamp, мини-плеер…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Забавные и полезные модификации Claude Code: пиксельное существо над промптом…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: мод для Claude Code, предназначенный для проектирования и запуска…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude готовит. Общайтесь со своей командой.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моды Claude Code для настоящих инженеров.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code&#x27;s terminal session recap, in the Claude desktop app&#x27;s Code tab.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Модификация Claude Code «всё в одном»: интерактивный HUD, защитные механизмы…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Космическая битва над приглашением Claude Code во время его работы.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Посмотрите, какие файлы есть в контексте каждого агента Claude Code и какая…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Сохраняйте холодную голову. Термометр для ваших дней с Claude Code: каждый час…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Кэш промпта, контекст и ограничения плана для Claude Code как на ладони — в…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Небольшие моды Claude Code для терминала и настольного приложения.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code mods (plugin marketplace): live sidebar with context, cost and…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Модификация Claude Code: панель прогресса для задач, субагентов, запусков…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Модификация Claude Code: кликабельное оглавление всего сеанса с временными…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Модификация Claude Code: ограничения частоты плана, заполненность контекста…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навык + мод Claude CLI, добавляющий испанские слова в ответы агента.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - События Alarum над промптом Claude Code: что только что поступило и передача…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Ваш список задач Floatee над промптом Claude Code: запускайте, направляйте и…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Боковая панель в стиле Evangelion для Claude Code: контекст, квота, активность…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Мод Claude Code, который стилизует его под The Machine из Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: модификация Claude Code для обязательных проверенных рабочих…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Моды с открытым исходным кодом для Claude Code: панели, строки состояния…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Мод Claude Code: отдельная панель для каждого субагента, файлов, которых они…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Мод Claude Code: статус сессии, живой прогресс Spec Kit и управление окном…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Окно контекста в виде строки над запросом, отображаемое так же, как Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Интерактивный HUD задач для Claude Code Desktop: полоса над запросом во время…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Бесплатный плагин с открытым исходным кодом для Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Сохраняйте промпты на потом и возвращайте их в поле ввода Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Модификация Claude Code, отображающая изображения непосредственно в Ghostty и…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Мод Claude, показывающий pull request.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Мод для Claude Code: создание звуковых эффектов из текстовых промптов с помощью…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: a debugger for Claude Code tool calls.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навыки Claude Code: проверка фактов в документации, аудит кода, журнал памяти…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Модификация Claude Code: строки кода за сегодня по версии Claude — добавленные…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Модификация Claude Code: кликабельные пути в ответах — нажмите на папку, чтобы…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагин-компаньон Claude Code: ASCII-компаньон над запросом, который помнит ваши…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Модификация Claude Code: маршрутизация моделей/уровня усилий под управлением…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Модификации Claude Code: уровень безопасности для Claude Code — удаление…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - A collection of Claude Code mods.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Плагин и мод Claude Code: AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Коллекция отличных модов Claude Code | 모드 모음집 Claude Code.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Уютный мод с интерфейсом RPG для Claude Code.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Моды для Claude Code: панели и хуки в реальном времени для повседневной работы.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Он говорит: мод Claude Code, который по запросу зачитывает вслух ответы Claude…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Отшлёпайте Claude, когда он ошибается — модификация Claude Code для снятия…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Моды Claude Code: небольшие плагины для интерактивных панелей, маршрутизации…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Мод и плагин Claude Code: монитор использования, отслеживание токенов и…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Мод Claude Code, который в реальном времени сообщает, какие файлы изменил…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Модификации Claude Code: карточки статистики сессии над полем запроса.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анимированный кот из шрифта Брайля над приглашением Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Мод Claude Code: направляет недорогие задачи в GLM/Kimi через дочерний Claude…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Пиксельный кот над запросом Claude Code, который запускает тестовый звонок…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, который выбирает подходящий момент для компактизации, чтобы…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модификации Claude для Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Маркетплейс плагинов Claude Code от anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Моды общего назначения для Claude Code: полосы, панели, уведомления и хуки.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - My private Claude Code mods.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Корабль LGTM Lines проплывает мимо после каждого изменения кода — мод Claude…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Ваши лимиты использования Claude в виде анимированной карточки здоровья жителя…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткие тренировки, пока Claude работает: ежедневная цель, серии, значки и…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Доска использования для Claude Code: расходы по моделям.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Мод для Claude Code: разбивка окна контекста в реальном времени над полем…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Мод Now Playing для Claude Code: Apple Music и Spotify над приглашением, с…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Моды для Claude Code: часы кэша, радиус поражения, предложения, рабочий список…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашего Claude Code.
- [cesarroger/skill-deck](https://github.com/cesarroger/skill-deck) - A Claude Code mod: keep skills manual-only and switch them on in profiles, per…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Однострочная полоса Claude Code.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Оригинальный движок Doom с Freedoom, доступный внутри Claude Code.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Модификация Claude Code, которая ведёт список открытых вопросов в разговоре и…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Просматривайте каждый файл, которого касается Claude, как pull request, не…
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Claude Mods.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code mods: rule-keeper saves your corrections as permanent rules.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Тамагочи, живущий внутри Claude Code: он вылупляется, ест код, который пишет…
- [dbroadhurst/claude-mod-goal](https://github.com/dbroadhurst/claude-mod-goal) - A Goal pane for Claude Code: the overall goal Claude is working toward, why…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - Claude Code Mod to explain commands ran by the agent.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Моды Claude Code, написанные как хуки функций, и маркетплейс, на котором они…
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - A Claude Code mod: a band above the prompt with Claude news and the breaking or…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Мод для Claude Code: после того как guard блокирует вызов инструмента…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Мод для Claude Code: фоновые задания в одном представлении с прогрессом и…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Мод для Claude Code: единый входящий ящик для сообщений от товарищей по…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Мод для Claude Code: объясняет блокировки песочницы и превращает повторные…
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Claude Code mod: status line with the session.
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Избранное для Claude Code: значки команд и навыков с запуском одним щелчком.
- [Dyarchia/dyarchia](https://github.com/Dyarchia/dyarchia) - Dyarchia: Build and Kanban on every surface.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Эй, заглушили! Брось diff, срежь riff, больше никаких правок, меньше credits.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods: rewrite-prompt (Ctrl+P rewrites your draft before you send it).
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code-моды: delete-guard (подтверждение удаления файлов) и octopus-crew…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Мод Claude Code: использование подписки (5h / 7d) в виде полосы над prompt в…
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods: auto-model-detector routes each prompt to the right model and…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Интерактивный радар параллельных веток и рабочих деревьев над запросом: какие…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Моды Claude Code (плагины function-hook), устанавливаемые через единый…
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Модификации Claude Code: context-bar-plus.
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Static supply-chain auditor for Claude Code Mods — local, offline, stdlib-only.
- [hahahahahahahahah6/task-progress-mod](https://github.com/hahahahahahahahah6/task-progress-mod) - Claude Code Mod: live TodoWrite progress bar above the prompt.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Модификация Claude Code: сколько времени занял каждый ответ, сколько времени…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Мод Claude Code: streamer-mode скрывает приватные панели, полосы и строку…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Плагины function-hook для Claude Code (моды).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Модификация Claude Code: пережидает 5-часовой лимит использования и отправляет…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Пульт управления над полем запроса Claude Code. Утка считывает показания.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Claude Code mods (function-hook plugins): PR merge follow-through, /clear…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Claude Code mod: live token usage, models and subagents per prompt.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Боковая панель с использованием контекста: общий объём, категории, рост за…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Боковая панель со списком файлов: какие файлы были созданы, изменены или…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пушистик в стиле 8-bit (чёрно-белый вислоухий голландский кролик) бегает и…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Боковая панель «Что я спрашивал»: каждое сообщение владельца в этом разговоре;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Боковая панель с временной шкалой: на что ушло время в этом раунде — ожидание…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Боковая панель обмена токенами: сколько токенов основной разговор отправляет…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Честный пакетик с бобами для claude code: после каждого раунда Claude тихо…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Небольшие моды для Claude Code, например новые команды со слешем и боковые…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живет в полосе над вашим prompt Claude Code: разыгрывает сессию…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод, озвучивающий ответы и уведомления Claude Code с помощью VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Модификация Claude, позволяющая читать и объединять разговоры между вашими…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Моды Claude Code. PixBar: пиксельное существо над вашим запросом, которое…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Моды Claude Code (usage-meter и другие).
- [koenrohrer/hearth-band](https://github.com/koenrohrer/hearth-band) - Claude Code mod: a pixel creature per model beside a prompt-cache campfire…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Два мода Claude Code: folio — панель файлов рядом с чатом, и tint…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: интерактивный граф того, что знает Claude Code.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Не позволяйте своему вниманию отвлекаться, пока вы ждёте ответа Claude Code.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Моды Claude Code от Sanmu — маркетплейс плагинов (боковая панель задач).
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Подготовленное сообществом руководство по модам Claude Code: варианты…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод Claude Code, который показывает, что делает Claude, в подзаголовке вкладки…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Пушистая чёрная кошка над вашим промптом Claude Code.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Модификация Claude Code с переключаемыми профилями разрешений: безопасная…
- [Mark-Hickey/claude-nine](https://github.com/Mark-Hickey/claude-nine) - Claude Code mods: Linear + PR watch, cortex mesh toasts, safe repo sync.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Small mods for Claude Code: runner-avatar, a little avatar that runs above your…
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of the agent.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Моды сообщества для Claude Code: защиты, панели и команды, выполняемые внутри…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Боковая панель для Claude Code: файлы, созданные Claude, разделы терминала…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Мод Claude Code: по вашему недавнему темпу использования прогнозирует, что…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Тихая боковая панель для Claude Code: чем занята эта сессия, её план, агенты и…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Тусклое время над каждым приглашением и каждым ответом в транскрипте Claude…
- [mmedum/spor](https://github.com/mmedum/spor) - Возвращает то, что Claude Code сворачивает: файлы, которые прочитал Claude…
- [mrkshw/cold-cache](https://github.com/mrkshw/cold-cache) - Claude Code mod: warns when a session.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, включающий обратно инструменты todo для моделей, которые их не…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Мод для Claude Code, который ждёт безопасной паузы, а затем передаёт вашу…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одной строке на каждую задачу над запросом — текущая…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Играйте в Connect Four против AI внутри Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Мод Claude Code: когда другой агент программирования делает коммит в ваш…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Мод Claude Code для репозиториев, которыми пользуются несколько ИИ-агентов: не…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Installe et configure mes mods Claude Code en une commande.
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code mod: flashes the terminal tab while Claude waits on you.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Маркетплейс модов Claude Code.
- [netgfx/claude-flow-explainer](https://github.com/netgfx/claude-flow-explainer) - A Claude mod to guide the user step by step on how a flow or code works.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Весёлые бесплатные моды для Claude Code, которые никогда не тратят токены.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Защитный механизм для SQL в Claude Code: запрашивает подтверждение перед тем…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Один мод для Claude Code и Windows, с приоритетом CJK: предварительный просмотр…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - Claude Code mods made by the OrbitMap team.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Лучшие моды Claude Code, отсортированные по пользе для вас.
- [pakornkub/session-insight](https://github.com/pakornkub/session-insight) - Claude Code mod: session usage, skills and agents, with an agent diagram.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Два мода Claude для Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Ругайтесь на Claude Code — и мультяшная рука даст сдачи.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Боковая панель со статистикой сеанса в реальном времени для вкладки Code…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Моды для Claude Code: safety-guard блокирует разрушительные команды и доступ к…
- [ptsnac/claude-session-handoff](https://github.com/ptsnac/claude-session-handoff) - Claude Code mod: session timer and one-click handoff to a fresh context window.
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Мод Claude Code: текущая биржевая лента, панель /quote, оповещения о ценах…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Мод для Claude Code: полоса над промптом, показывающая использованный контекст…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Мод для Claude Code: боковая панель, закрепляющая каждую диаграмму, которую…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Мод для Claude Code: этап сновидения, который объединяет, переписывает и…
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Мод для Claude Code: отбрасывает расплывчатые промпты до того, как их увидит…
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod: Claude uses your secrets without seeing them.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - A Claude Code mod that keeps secrets out of the session transcript: every key…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Мод Claude Code: хост SSH, оперативная память и ограничения использования 5h/7d…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Мод Claude Code: отжимания, которые нужно делать, пока работает Claude.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - paceline as a Claude Code mod: paces your usage limits in a line above the…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Моды для claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Мод Claude Code: превращает план, который вы утверждаете в plan mode, в живой…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Подборка Claude Code-модов. Каждый элемент клонирован и проверен с помощью…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Бесплатный режим: вспомогательные агенты работают на Haiku, а большие файлы и…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музыка в стиле lofi, сопровождающая сессию: спокойствие, концентрация, поток, а…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Учитесь, пока Claude пишет код: после хода, изменившего код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запись каждого изменения, которое вносит Claude: воспроизводите каждое…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: неофициальный фанатский мод по Avengers для Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Модификация Claude Code для контекста, роста, квоты, кэша, нативной стоимости и…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Мод Claude Code: направляет простые запросы и субагентов к более дешёвым…
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods.
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Claude Code mods, installable as a plugin marketplace: deviation-kernel guards…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - Оригинальный DOOM на панели Claude Code без необходимости что-либо…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Keep Claude.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commit messages в один клик для Claude Code с танцующей pixel-art Malenia.
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — мод Claude Code, показывающий использование вашего плана Claude…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Небольшие моды, которые меняют внешний вид и звучание Claude Code.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, отображающий текущую сессию на панели: каждое приглашение…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Plugin marketplace модов Claude Code: function-hooks plugins, которые рисуют…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Мод для Claude Code: переписывает черновой промпт на месте, указывая подходящие…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Слушайте ответы Claude Code, пока читаемое предложение выделяется.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code mod: your context window as Scrooge McDuck.
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Мод для Claude Code: квота 5h/7d, окно контекста, оставшееся время кэша промпта…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анимированная полоса прогресса и сводка по завершении для…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Три небольших мода Claude Code: узнайте, когда завершат работу ваши субагенты…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Уменьшает большие снимки экрана перед тем, как Claude их прочитает, чтобы…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажите «Я потерялся», и Claude снова объяснит свой последний ответ простыми…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Показывает предлагаемые следующие промпты над полем ввода.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Задайте Claude дополнительный вопрос на панели рядом с вашей работой.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code pings you in Telegram when a task is done or it waits for…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Мои моды для Claude Code.
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - A Claude Code mod: your Godville hero and diary in a sidebar.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Моды для Claude Code: полоса лимитов использования (5 ч/неделя) и панель…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Плагин Claude Code: лимиты использования Claude Pro/Max с прогнозом темпа…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моды для Claude Code. agent-crew: наблюдайте за работой субагентов как за живой…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Встраивание и отображение математических формул LaTeX, а также необязательных…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Интерактивная доска задач для Claude Code: планируйте перед началом работы…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Отобранная вручную коллекция лучших ресурсов для самых потрясающих агентов…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Плагин Claude Code, показывающий, что происходит: использование контекста…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Красивая, полностью настраиваемая строка состояния для Claude Code CLI с…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Все части системного промпта Claude Code, 27 встроенных описаний инструментов…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI video skill for Claude Code &amp; Codex — cinematic product videos with…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Более 45 советов по максимально эффективному использованию Claude Code — от…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — создание каруселей Xiaohongshu и пар обложек…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Красивый powerline в стиле vim для Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Просматривайте diff вашего агента кодирования в панели терминала и отправляйте…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Комплексный плагин статусной строки для Claude Code с использованием контекста…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Создавайте моды для Claude Code: перехватывайте любой запрос, изменяйте любой…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Комплексная панель statusline для Claude Code — информация о сессии, шкалы…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: отслеживайте углеродный след своих сессий Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Эстетичная statusline для Claude Code от awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Полноформатный агент для ролевых игр в DeepSeek Harness (плагин DSH Tavern)…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Общедоступные Skills и моды для Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, моды, субагенты, хуки, slash-команды и руководства для Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Законно бесплатные LLM APIs и агенты программирования — самообновление…
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - DeepSeek Harness Tavern Plugin - character card roleplay, worldbook management…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Быстрый калькулятор стоимости без зависимостей и настраиваемая строка состояния…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Строка состояния терминала для сессий Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Онлайн-счета футбольных матчей, расписание и турнирные таблицы для…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Локальная плоскость управления для Claude Code на Windows и macOS: переключение…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, превращающий вашего агента программирования в эксперта по…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Время молитв, дата по хиджре, азкары, ежедневный аят, пост по сунне, Рамадан…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Личная конфигурация Claude Code, версионируемая внутри ~/.claude — агенты…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Комплекс для генерации изображений и визуальной обработки для DeepSeek Harness…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Двухстрочная статусная строка truecolor для Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Всплывающая карточка прилива пиковых/непиковых периодов для DeepSeek Harness…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Набор плагинов для Claude Code, pi и DeepSeek Harness: HUD в строке состояния…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Портативный набор инструментов Claude Code для .NET DDD/Clean Architecture…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Переносимая глобальная конфигурация Claude Code: пользовательские навыки, хуки…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагины Claude Code, которые я использую каждый день: навыки и моды…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Неофициальные моды для вкладки Code в Claude Desktop — usage-pet: полоса…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Маркетплейс плагинов и навыков Claude Code для создания модов игры Hytale.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Управление токенами для Claude Code: лучшая модель направляет работу, а…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Статусная строка текущей фазы рабочего процесса для Claude Code.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Репозиторий модов Awesome Media для Claude Code.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Простая и полезная настройка строки состояния для Claude Code.
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Marketplace de plugins para o Claude Code: mods, skills, agentes, hooks…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Отображение строки состояния Claude Code с ограничениями частоты запросов…
- [eddundead/claude-poker](https://github.com/eddundead/claude-poker) - 8-bit Texas Hold.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Настраиваемая строка состояния Claude Code для Linux, WSL, Windows и macOS с…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Быстрая строка состояния Rust для Claude Code — сначала данные, кэшированный…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Живая панель использования для Claude Code — разбивка контекста, cache hits…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Строка состояния и строка токенов для Claude Code: контекст, использование за 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Отображение ключевых сведений о состоянии Claude Code, включая модель…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Многострочная строка состояния Claude Code: расходы, процент контекста, git и…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Строка состояния с полезной информацией для claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Нативные команды агентов. Под контролем.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Дополнения Claude Code: наблюдатель цветных точек статуса вкладок + встроенная…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Определяемые программные фабрики для Claude Code на herdr: графы станций…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Строка состояния использования Claude Code для macOS и Linux, упакованная как…
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code desktop mod: prompt-cache TTL countdown, hit rate and misses.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Пользовательская statusline для Claude Code — панель контекста с процентом…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Чистая информативная строка состояния для Claude Code — показывает проект…
- [aubinhaba/claude-code-payment-skills](https://github.com/aubinhaba/claude-code-payment-skills) - Claude Code plugin: code-review skills for payments, consistency, boundaries…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod: панель состояния в стиле CRT для Claude Code в терминале и…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Маркетплейс плагинов Claude Code с baloo: навыки, агент, проверяющий изменения…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Профессиональная строка состояния Claude Code: длительность сессии, стоимость в…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Строка состояния Claude Code с учётом подписки.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Расширенная строка состояния терминала для Claude Code — Bun + TypeScript, без…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Инструменты, skills и агенты для Claude Code — начиная со status line…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Пользовательская статусная строка Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Фактические расходы DeepSeek API для Claude Code: перерасчитывает стоимость…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Предпросмотр изображений внутри Claude Code: наведите курсор на чип под…
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - My Claude Code setup: mods, skills and plugins.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Синхронизируйте задачи Claude с Fizzy.do, чтобы команда видела изменения в…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Отслеживайте состояние Claude Code с помощью компактной панели, показывающей…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Установщик окружения Claude Code: skills, statusline, hooks, permissions и…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Строка состояния в стиле HUD для Claude Code — состояние сети, TPS, контекст…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Портативная конфигурация Claude Code (строка состояния + установщик).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Небольшая панель для Claude Code: процент контекста, обратный отсчёт кэша…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Пользовательская строка состояния терминала для Claude Code: модель, каталог…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Портативная конфигурация Claude Code: CLAUDE.md, settings, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Мод Claude Code для настольной версии (macOS): уведомления о сеансах с…
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Строка состояния Claude Code для отслеживания стоимости и мониторинга сессии в…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Навык Claude Code (VS Code, Windows): предварительный просмотр изображений и…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Строка состояния Claude Code: папка, ветка git, модель, использование…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Детектор деградации контекста 2026 — проактивный монитор памяти ИИ и лимитов…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, субагенты и statusline для Claude Code: open-source коллекции и…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Визуальный конструктор статусных строк Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Статусная строка Claude Code с отображением использования токенов в реальном…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Моды для Claude Code: панели, полосы и компаньоны на основе перехватчиков…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Claude Code-style UI bundle for the Pi coding agent — tool rendering, spinner…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Передавайте задачи между сеансами Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Это на сервере MCP для управления MODS — модульным кроссплатформенным…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Навык Codex и Claude Code для перевода модов CK3 с помощью локального LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Моды с открытым исходным кодом и другие расширения для Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Строка состояния Claude Code: эстетика CCometixLine + функциональность HUD…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: находите то, о чём вы снова и снова просите Claude Code, и…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Мод prompt-bar для Claude Code: лимиты использования, таймер кэша и…

</details>

<a id="dsh-cordis"></a>

## Экосистемы плагинов DSH и Cordis

DeepSeek Harness и Cordis приходят к тому же результату с другой стороны: для них плагин является механизмом модификаций, поэтому плагин там эквивалентен моду здесь.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74351 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **74351**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100550 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **100550** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐97943 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **97943**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82003 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **82003**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35766 · Go · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **35766**  |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25500 · Python · 🔎 inferred · 19 天</summary>

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
| Звёзды           | **25500**  |
| Последний push   | 2026-09-22 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18396 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Подборка плагинов для DeepSeek Harness (dsh) · подборка плагинов DeepSeek Harness

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **18396**  |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4492 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **4492**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4292 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **4292**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Открытая основа боковой панели с поддержкой сторонних расширений для регистрации новых страниц боковой панели. Встроены страницы рендеринга и редактирования файлов, терминала, бокового чата, Git и субагентов ｜ Открытая основа боковой панели, поддерживающая сторонние расширения для регистрации новых страниц боковой панели. Встроены рендеринг и редактирование файлов, терминал, боковой чат, Git и страницы субагентов.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **4112**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>анимированная запись · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Открыть видео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

The World's First Virtual Terminal for AI Agents

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3682**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3092 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Настольная версия DeepSeek Harness Tauri | Установщик всего 8 МБ, настройка окружения не требуется, предустановленные плагины, Windows / macOS / Linux.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **3092**   |
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
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1995 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1995**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1837 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1837**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1577 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **1577**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **1410**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1172 · Go · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **1172**   |
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
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1140 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Go                                                                     |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1140**   |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **705**    |
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
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **592**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/d-dev0101/open-sea-skin">d-dev0101/open-sea-skin</a></b> · ⭐389 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

🌊 DeepSeek Harness 海洋皮肤与动态主题 | Real-time ocean theme with adjustable waves, sunset & glass opacity. DSH plugin + Chrome/Edge extension; keeps your new-tab homepage.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **389**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `animated-background` · `chrome-extension` · `customization` · `deepseek` · `deepseek-harness` · `deepseek-theme` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/3d9689f0d936d1b0.png" width="100%" alt="d-dev0101/open-sea-skin screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/ccd6ac3920478ffa.gif" width="100%" alt="d-dev0101/open-sea-skin animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **369**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **225**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/cocofhu/anime-find">cocofhu/anime-find</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **176**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `anime` · `anime-search` · `bangumi` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `magnet`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cocofhu--anime-find/4e8000425bf8bf5f.jpg" width="100%" alt="cocofhu/anime-find screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **176**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **172**    |
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
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐160 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **160**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐142 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Данные о среде выполнения, помогающие агентам отслеживать и профилировать узкие места, а также устранять их в приложениях и нативном коде, ядрах GPU и стеках инференса.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Python                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **142**    |
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

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
| Впервые в списке | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **133**    |
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
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин DSH · инъекционный оптимизатор 0.8 (основная ветка): вы говорите как обычно, а после отправки и до получения запроса ИИ он уточняет, «что именно нужно в этом раунде», а затем передаёт это понимание рабочему ИИ (инъекция в контекст) — исходные слова не переписываются, каждое утверждение сопровождается дословным обоснованием. Включает панель управления (уровень/разрешения/модель/контекст/инструменты только для чтения), всплывающий слой перехвата (слой рассуждений + слой результата) и фактическое использование токенов. Может заметно повысить стабильность работы большинства моделей, особенно DeepSeek-V4.1-Flash, обеспечивая ощутимое улучшение

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
<summary><b>Больше в этой категории</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Защита перед выполнением для AI-агентов программирования.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Отобранный список лучших отличных ИИ-плагинов для ИИ-ассистентов, включая…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Плагин DSH — бесплатные модели OpenCode Zen для DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Рынок плагинов DSH / DSH Plugin Marketplace: в веб-интерфейсе DeepSeek Harness…
- [arcships/rutis](https://github.com/arcships/rutis) - Среда выполнения плагинов для самоизменяющегося программного обеспечения…
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Настольный Agent, созданный на базе ядра Deepseek-Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Живой каталог плагинов DeepSeek Harness — обновляется ежечасно, ежедневно…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Извлечение контекста рабочего пространства и отслеживание жизненного цикла с…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Избранный каталог плагинов DeepSeek Harness (DSH) — более 280 плагинов…
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - 可视化 Agent 编排平台｜基于 DeepSeek Harness，支持 Workflow、Multi-Agent、元编排、MCP 与…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Плагин dsh — мастер игровых ресурсов. Подключается к модели генерации…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: мультиплатформенная система агентов для групповых чатов на базе…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Коллекция веб-плагинов GUI для DSH (DeepSeek Harness) — уведомления о задачах…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Подобранные сообществом плагины, инструменты, навыки и учебные ресурсы DeepSeek…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Плагин управления серверами MCP для DeepSeek Harness: страница Settings → MCP…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Среда выполнения для коммерческих переговоров A2A + плагин DeepSeek Harness…
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Панель инструментов для DeepSeek Harness Web: менеджер MCP.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Плагин DeepSeek Harness · оптимизация черновика запроса одним щелчком в панели…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Настоящий PowerPoint, а не HTML. Расскажите ИИ, что нужно осветить, и pptwise…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Локальный граф знаний кода и среда контекста для агентов программирования.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Плагин AI-инженерии Embedded C/C++ — навыки работы с прошивками.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Превратите модели, уже авторизованные в настольном приложении WorkBuddy на этом…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - плагин dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Постоянное тестирование совместимости плагинов DeepSeek Harness: точные версии…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Агрессивное сжатие контекста для агентов, ориентированных на локальную работу.
- [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) - Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Guarded context compaction for DeepSeek Harness (dsh): the LLM proposes…
- [GooDAnDReaDY/dsh-voice](https://github.com/GooDAnDReaDY/dsh-voice) - Voice input for DeepSeek Harness: dictation and voice messages with…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness host plugin that keeps project documents and long-term memory…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) - Native ClineBot / ClinePass provider companion plugin for DeepSeek Harness (DSH).
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray для плагинов DeepSeek Harness: заявленные возможности против фактического…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [GooDAnDReaDY/dsh-lanmode](https://github.com/GooDAnDReaDY/dsh-lanmode) - Mobile gateway and secure local network access for DeepSeek Harness WebUI.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) - Mixture of Agents (MoA) plugin for DeepSeek Harness with /moa slash command…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [chen731215-dev/dsh-muv-table](https://github.com/chen731215-dev/dsh-muv-table) - MUV Variable Table Editor - tavern companion plugin for DeepSeek Harness…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Рабочее пространство с несколькими папками: позволяет агенту DSH.
- [GooDAnDReaDY/dsh-gitea](https://github.com/GooDAnDReaDY/dsh-gitea) - Gitea/Forgejo toolkit for DeepSeek Harness: issues, PRs, CI, releases…
- [jinhuang712/dsh-survey](https://github.com/jinhuang712/dsh-survey) - Questionnaire-style batch questioning plugin for DeepSeek Harness: 10+…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт проверки плагинов DeepSeek Harness (dsh) без зависимостей…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - Плагин DeepSeek Harness (DSH): синхронизация моделей OpenCode Go одним нажатием…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode в DeepSeek Harness — плагин DSH, поддерживающий работу OpenCode Zen и…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонний маркетплейс плагинов и защищённый менеджер жизненного…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx — это ориентированная на человека расширяемая настольная рабочая среда…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Укомплектованный всем необходимым агент программирования для DeepSeek Harness…
- [GooDAnDReaDY/dsh-tts](https://github.com/GooDAnDReaDY/dsh-tts) - Natural speech synthesis plugin for DeepSeek Harness.
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Оснастите DeepSeek Harness Agent нативными руками и ногами для управления…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — набор инструментов для локального развёртывания и эксплуатации…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Permanently delete archived DeepSeek Harness sessions along with their on-disk…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Веб-плагин DeepSeek Harness (DSH): вкладка боковой панели market-dashboard для…
- [tiphareth0/dsh-hardssh](https://github.com/tiphareth0/dsh-hardssh) - Run your work with existing DSH plugins on remote servers, across any number of…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Делает повторно запускаемой неатрибутированную попытку с пустой моделью для…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Плагины, которые убирают за собой: порт фреймворка плагинов cordis для iOS и…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Пресет агента DeepSeek Harness: Codex и Claude Code в качестве субагентов…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Среда выполнения плагинов Rust с проверенным Verus ядром жизненного цикла и…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Тексты, обсуждения и видео

Статьи, обсуждения и видео о возможностях модов.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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

| Язык       | Записей | Примеры                                                                                                       |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 382     | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 96      | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 35      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 23      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 15      | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 6       | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 6       | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| C          | 1       | `reporails/arcade`                                                                                            |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                          |
| PowerShell | 1       | `GoSlowPoke168/claude-statusline`                                                                             |
| Swift      | 1       | `eovidiu/cordis-ios`                                                                                          |

<sub>Учитываются только записи, в которых указан язык. Документация и обсуждения исключены из этой таблицы.</sub>

## Участие

Исправления приветствуются и являются самым быстрым способом улучшить этот список. Откройте issue или pull request, если запись попала не в тот раздел, получила неверную оценку или если проект был ошибочно исключен как совпадение имени — именно в этой последней категории автоматические фильтры чаще всего ошибаются.

---

<sub>Независимый проект сообщества. Не аффилирован с Anthropic, не одобрен и не проверен им. Claude Code, Claude и Anthropic являются товарными знаками Anthropic. Поведение продукта может меняться без уведомления; всё критически важное проверяйте по официальной документации. Материалы остаются собственностью исходных проектов и воспроизводятся только там, где это разрешено лицензией.</sub>

<sub>Последнее обновление · 2026-10-12T03:53:55+08:00</sub>
