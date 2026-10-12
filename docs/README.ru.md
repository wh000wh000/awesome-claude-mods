<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Отличные моды для Claude">
</p>

<h1 align="center">Отличные моды для Claude</h1>

<p align="center"><b>Индекс модов, плагинов Claude Code и более глубоких изменений поведения, составленный с оценкой доказательности.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-597-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <b>Русский</b> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Актуальный индекс** · Последняя синхронизация: `2026-10-12T17:03:53+08:00` (UTC+8)
> · Записей: **597** · Добавлено в последнем обновлении: **0** · Языки реализации: **15**

<sub>Каждая запись ниже была автоматически собрана, отфильтрована и проверена повторно. Здесь нет платных размещений.</sub>

<a id="featured"></a>

## Лучшее на данный момент

<sub>По одной записи на категорию, ранжирование по степени подтверждённости и количеству звёзд, пересчитывается при каждом обновлении. Это рейтинг, а не рекомендация; каждая подборка ведёт к полной карточке ниже. Предпочтение отдаётся проектам, опубликовавшим снимок экрана или запись, чтобы лента оставалась визуальной.</sub>

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
<sub>⭐2540 · Python · 👁️ observed</sub>
<sub>Найдите призрачные токены. Исправьте их. Переживите компактификацию. Избегайте ухудшения качества контекста.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74385 · TypeScript · 👁️ observed</sub>
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
- [Официальные: собственные репозитории и примечания к выпускам Anthropic](#официальные-собственные-репозитории-и-примечания-к-выпускам-anthropic) — **18**
- [Моды: созданы с использованием возможности модификации](#моды-созданы-с-использованием-возможности-модификации) — **474**
- [Экосистемы плагинов DSH и Cordis](#экосистемы-плагинов-dsh-и-cordis) — **93**
- [Тексты, обсуждения и видео](#тексты-обсуждения-и-видео) — **11**
- [Другие проекты](#другие-проекты) — **1**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150297 · TypeScript · ✅ official · 0 天</summary>

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
| Звёзды           | **150297** |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9479 · TypeScript · ✅ official · 2 天</summary>

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
| Звёзды           | **9479**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8252 · Python · ✅ official · 2 天</summary>

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
| Звёзды           | **8252**   |
| Последний push   | 2026-10-09 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242 天</summary>

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
| Звёзды           | **6347**   |
| Последний push   | 2026-02-11 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 2 天</summary>

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
| Звёзды           | **1799**   |
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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Официальные модификации Claude Code от See Stack: динамический HUD контекстного окна, панель голосовой озвучки и инструменты терминала. Установка через: npx seestack

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic`  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **0**      |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/redfox-data/redfox-community-dsh">redfox-data/redfox-community-dsh</a></b> · ⭐7 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

The official bundle plugin package of DSH (DeepSeek Harness) from RedFoxHub（红狐数据）: Over 100 social media data skills (Douyin / Xiaohongshu / Kuaishou / Bilibili / Official Accounts / Video Accounts / Weibo / YouTube / TikTok, etc.), installed in the native DSH skill format with just one click.

##### 📌 Основные сведения

| Поле          | Значение                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| Категория     | `Официальные: собственные репозитории и примечания к выпускам Anthropic` |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов`   |
| Язык          | Python                                                                   |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **7**      |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-skills` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-skill` · `plugin` · `skills`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/redfox-data--redfox-community-dsh/cb0297dc6c545a28.png" width="100%" alt="redfox-data/redfox-community-dsh screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
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
| Впервые в списке | 2026-10-12 |

🏷 `anthropic` · `ccusage` · `claude` · `claude-code` · `cursor` · `developer-tools` · `gnome` · `gnome-extension`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fschmutz--claude-usage-panel/40b54f8d52b03345.png" width="100%" alt="fschmutz/claude-usage-panel screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Добавлен `$.ui.notify` для модов: вызывает нативное уведомление через ваши…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Исправлена ситуация, когда Esc или прерывание во время хука `UserPromptSubmit`…
- [AlekDob/blockodile-claude-mod](https://github.com/AlekDob/blockodile-claude-mod) - Blockodile official Claude Code mod: an animated croc sidebar that explains…

</details>

<a id="mods"></a>

## Моды: созданы с использованием возможности модификации

Каждая запись здесь демонстрирует использование возможности, которую Claude Code получил в версии 2.1.287: она выполняет отрисовку через `ui.render`, владеет панелью, полосой или карточкой, читает `$.ui.selection()`, создаёт товарищей с помощью `agent.spawn` или прямо указывает, что является модом.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2540 · Python · 👁️ observed · 0 天</summary>

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
| Звёзды           | **2540**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐510 · JavaScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **510**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐199 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **199**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐149 · TypeScript · 👁️ observed · 7 天</summary>

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
| Звёзды           | **149**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐120 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **120**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐104 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Скины для Claude Code: строки инструментов с иконками, карточки с diff, таблицами и диаграммами Mermaid, полоса использования и пятнадцать тем. /skin переключает их в реальном времени.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **104**    |
| Последний push   | 2026-10-11 |
| Впервые в списке | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐80 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **80**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 3 天</summary>

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
| Звёзды           | **79**     |
| Последний push   | 2026-10-08 |
| Впервые в списке | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SaM-runtime/claude-console">SaM-runtime/claude-console</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Multi-project console for Claude Code, built as a Claude Code mod: live project board, trigger actions, quota batteries; executes via Claude Code or Codex.

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
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sam-runtime--claude-console/7502a46951d79adb.gif" width="100%" alt="SaM-runtime/claude-console screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sam-runtime--claude-console/7502a46951d79adb.gif" width="100%" alt="SaM-runtime/claude-console animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐69 · TypeScript · 👁️ observed · 9 天</summary>

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
| Звёзды           | **69**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Claude Code mod: preview pasted images and long pasted text above the prompt

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
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Используйте Codex, GLM и других агентов программирования в качестве субагентов Claude Code.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Моды: созданы с использованием возможности модификации`                  |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **16**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6 天</summary>

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
| Звёзды           | **14**     |
| Последний push   | 2026-10-05 |
| Впервые в списке | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
| Последний push   | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/natsukium/claude-code-figures-plugin">natsukium/claude-code-figures-plugin</a></b> · ⭐7 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Рисуйте диаграммы, формулы LaTeX и изображения результатов инструментов непосредственно в терминалах kitty-graphics — плагин Claude Code

<sub>🔧 Найдено использование в коде: `hooks/register.tsx`</sub>

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
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `d2` · `diagrams` · `graphviz` · `kitty-graphics` · `latex`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/natsukium--claude-code-figures-plugin/8b6e1b6a10ace52e.png" width="100%" alt="natsukium/claude-code-figures-plugin screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 440</sub></summary>

- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Экспертные skills, агенты, команды, правила, хуки и стили вывода для Claude…
- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Коллекция из более чем 100 модов, которые можно использовать с Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Модификации Claude и инструменты для их создания: сначала навык-сборщик, затем…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Среда Claude Code, которую я запускаю каждый день, публикуемая под этим именем…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Наденьте новую крышу на Claude Code с помощью Claude Mods: не изменяя бинарный…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Четыре мода Claude Code: Cache Keeper, Recording Mode, Goal Meter и Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Моды Claude Code от Learning Hacker: сделайте работу агента понятной для…
- [kakha13/claude](https://github.com/kakha13/claude) - Моды Claude Code, исправляющие и переводящие ваши подсказки до того, как их…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Моды и навыки Claude Code от Nekyia Labs, создаваемые и ежедневно используемые…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - База знаний Obsidian с указанием источников о модах Claude Code: как они…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Модификация, придающая терминальному журналу Claude Code вид настольного…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Боковая панель для кода Claude: субагенты, запускаемые сессией, выполняемая…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Панель боковой панели Claude Desktop (вкладка Code): перечисляет все…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Навык, обучающий агентов Claude Code создавать Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Полоса использования над полем ввода Claude Desktop (вкладка Code): лимиты 5h /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Пользовательские моды, плагины и навыки Claude, устанавливаемые из одного…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (плагины с перехватчиками функций) для Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Галерея модов Baselane: моды Claude Code, проверенные и закреплённые.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Очередь решений CLI/TUI для людей, работающих с разговорными агентами.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Модификация панели IDE Claude Code: доска агентов, дерево файлов и просмотрщик…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, отрисовываемый в поле приглашения Claude Code по мере ввода.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Моды Claude Code: панель использования 像素螃蟹 usage-hud + HTML-ссылки, по которым…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плавающая карточка состояния для Claude Code — модель, контекст, ограничения…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Моды для Claude Code: плагины с функциональными хуками, добавляющие…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Моды Claude Code: screen-guard маскирует имена и секреты во время демонстрации…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Расширения Claude Code. Раскройте всю мощь Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Мод Claude Code (плагин), который добавляет боковую панель с вкладками…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Панели, защитные механизмы и полезные моды для Claude Code: контекст…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Два мода Claude Code над полем приглашения: измеритель контекстного окна…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Продлите действие плана Claude Pro: моды Claude Code для точного HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Чтение markdown-файлов, которым код Claude даёт имена, с отображением рядом с…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Мод Claude Code: миниатюры вставленных изображений над приглашением в любом…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Голосовой напарник для Claude Code. Обсуждайте задачи с 3D-волком на базе…
- [ngothanhluc/claude-mermaid-mod](https://github.com/ngothanhluc/claude-mermaid-mod) - Claude Code mod: draws mermaid blocks in Claude.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Моды Claude Code: typing-speed, спидометр скорости печати в реальном времени со…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Фейерверки для Claude Code: каждое нажатие клавиши, вызов инструмента, коммит и…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Тест скорости печати на время, пока работает Claude.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Находите моды, плагины и расширения Claude Code с анимированными…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Мод Claude Code: диаграммы mermaid, встроенно отображаемые в расшифровке.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Модификации и скины для Claude Code: индикатор выполнения задач Claude в…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Небольшие моды Claude Code (плагины с перехватчиками функций): session-switcher…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Моды Claude Code: меню инструментов Claude, режим Zen, темы терминала, элементы…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Моды Claude Code: mod-scout (поиск наиболее нужных вам модов), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Два мода Claude Code для одновременного запуска множества сеансов: карточка…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: поиск, просмотр, переключение и обновление модов Claude Code.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Моды Claude Code: панель контекста, панель агентов, размытие PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Лучшие моды Claude Code: отобранные вручную, проверенные, закреплённые.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Плагин Claude Code: автоматическая маршрутизация моделей Claude.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Моды для Claude Code: панели, команды и хуки, созданные с помощью плагина…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Обрезает огромные выводы инструментов до того, как они заполнят контекст Code…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Шесть модов для Claude Code: анимированный маскот Clawd, индикаторы лимита…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Маркетплейс модов для Claude Code: пошаговый отладчик цикла агента, подсказки…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Шесть модификаций Claude Code: ограничения плана и контекст над полем запроса…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Лучший универсальный набор модов для Claude Code: лимиты использования и HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Смотрите YouTube Shorts в своём Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набор инструментов Naren для Claude: skills, mods и MCP servers для Claude…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Мод Claude Code, отображающий различия Edit и Write в двух расположенных рядом…
- [nsodhi-cmu/claude-code-ripple](https://github.com/nsodhi-cmu/claude-code-ripple) - Claude Code mod that creates call graphs of your code changes.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Моды для Claude Code: Clawd, крошечный пиксельный талисман, который показывает…
- [reporails/arcade](https://github.com/reporails/arcade) - Классические компьютерные игры в виде модов Claude Code, в которые можно играть…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Кураторский список модификаций Claude Code, устанавливаемых как через…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Моды Claude Code по запросу — навык, который читает ваш разговор и создаёт…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Two Claude Code mods: cache-keeper and ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Крайне авторский плагин Claude Code, созданный любителем Rust, одержимым…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Моды Claude Code, которые помогают агенту не отклоняться от цели — перехватчики…
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Модификации Code для Claude, которыми я пользуюсь.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Дашборд macOS notch для Claude Code: лимиты использования, открытые сессии…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Мод для Claude Code: панель кэша промптов, следующие шаги, быстрые кнопки и…
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Стоимость, токены и лимиты тарифов ваших агентов программирования.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Мод Claude Code, отображающий ваши лимиты использования и расходы в полосе над…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моды Claude Code от Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Моды для Claude Code: индикаторы выполнения планов, журнал того, что Claude…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Смотрите, что Claude Code запускает в фоне: субагенты, задания Codex, shell…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods by MacLeod Labs: streams untangles a session.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Полевые заметки первого дня о модах Claude Code на Windows: топливная шкала…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: отладчик вызовов инструментов Code для Claude.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Небольшие карточки, расположенные под запросом Claude Code или закреплённые…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живые индикаторы стоимости, контекста и квоты плана над…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Мод Claude Code, который задерживает разветвление субагентов, запросы с большим…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 навыков агента для Claude в пяти наборах.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods для claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Мод Claude Code, который включает и отключает глобальные навыки, агентов…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Плагины Claude Code (моды): переключение между несколькими аккаунтами Claude…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Протестированные Claude Code-моды, устанавливаемые одной командой: защитные…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Моды для Claude Code: плагины, созданные на основе function hooks.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Собственный маркетплейс модов-плагинов для Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Набор модов для claude code, созданных мной.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Моды Claude Code. touch-map: просматривайте в виде дерева и карты активности…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Учите иностранный язык во время работы с Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Следит за долгой сессией Claude Code, чтобы вам не пришлось: отслеживает…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Live cost, token and context usage sidebar for Claude Code: a mod that shows…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Цель, задачи и агенты над вашим промптом Code для Claude — без настройки.
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude готовит. Общайтесь со своей командой.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моды Claude Code для настоящих инженеров.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Краткий обзор терминальной сессии Code для Claude во вкладке Code приложения…
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack 的 Claude Code mods 合集.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - A Claude Code mod: a pane with the session.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - A Claude Code mod: catch pixel-art Modsters in an idle game while Claude works.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - All-in-one Claude Code mod: a live HUD, safety guards.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Посмотрите, какие файлы есть в контексте каждого агента Claude Code и какая…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Превратите каждую сессию Claude Code в небольшое приключение: генеративная…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Небольшие моды Claude Code для терминала и настольного приложения.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навык + мод Claude CLI, добавляющий испанские слова в ответы агента.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - События Alarum над промптом Claude Code: что только что поступило и передача…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Ваш список задач Floatee над промптом Claude Code: запускайте, направляйте и…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Боковая панель в стиле Evangelion для Claude Code: контекст, квота, активность…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Мод Claude Code, который стилизует его под The Machine из Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Мод Claude Code: отряд в стиле пиксель-арта предлагает подходящую модель…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: модификация Claude Code для обязательных проверенных рабочих…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Моды с открытым исходным кодом для Claude Code: панели, строки состояния…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Мод Claude Code: отдельная панель для каждого субагента, файлов, которых они…
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - Various mods I have made for claude that I find helpful.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Мод Claude Code: статус сессии, живой прогресс Spec Kit и управление окном…
- [KevinYu1580/jev-cc-model-router](https://github.com/KevinYu1580/jev-cc-model-router) - Claude Code mod: picks the model once per session and the effort every turn…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Окно контекста в виде строки над запросом, отображаемое так же, как Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Интерактивный HUD задач для Claude Code Desktop: полоса над запросом во время…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code plugin (mod) that makes the Claude Code terminal UI look like the…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Бесплатный плагин с открытым исходным кодом для Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Personal Claude Code mods (function-hook plugins): context handoff, repo…
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Сохраняйте промпты на потом и возвращайте их в поле ввода Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Модификация Claude Code, отображающая изображения непосредственно в Ghostty и…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Мод Claude, показывающий pull request.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Модификации Claude Code: отобранные и протестированные, причём каждая…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Модификации Code для Claude: автоматическая передача и индикатор выполнения.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навыки Claude Code: проверка фактов в документации, аудит кода, журнал памяти…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Мод Claude Code, который переписывает черновые запросы в понятные перед…
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - A Claude Code mod that keeps a live casebook of the Evidence rea gives the…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Модификации Claude Code от Pedro La Rosa — на одном маркетплейсе плагинов.
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Модификация Claude Code: ограничения использования на 5 часов и 7 дней в виде…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагин-компаньон Claude Code: ASCII-компаньон над запросом, который помнит ваши…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Плагин Claude Code для управления видимостью инструментов каждого агента…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Render LaTeX display math in Claude Code.
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - A collection of Claude Code mods.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Плагин и мод Claude Code: AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Коллекция отличных модов Claude Code | 모드 모음집 Claude Code.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: неофициальный фанатский мод по Avengers для Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Он говорит: мод Claude Code, который по запросу зачитывает вслух ответы Claude…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Моды Claude Code: небольшие плагины для интерактивных панелей, маршрутизации…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Мод и плагин Claude Code: монитор использования, отслеживание токенов и…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Catch the drift of your Claude Code session.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Маркетплейс модификаций для Claude Code: agent-board, auto-model…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods: session stat cards above the prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анимированный кот из шрифта Брайля над приглашением Claude Code.
- [aliahmadcse/claude-usage-status](https://github.com/aliahmadcse/claude-usage-status) - Claude Code mod: model, effort, context, cost, and 5-hour/weekly usage limits…
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Мод Claude Code: направляет недорогие задачи в GLM/Kimi через дочерний Claude…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Пиксельный кот над запросом Claude Code, который запускает тестовый звонок…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, который выбирает подходящий момент для компактизации, чтобы…
- [Amel-DZRV/claude-code-auto-handoff](https://github.com/Amel-DZRV/claude-code-auto-handoff) - Claude Code mod: context bar with a handoff mark, prompt-cache countdown…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модификации Claude для Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Моды общего назначения для Claude Code: полосы, панели, уведомления и хуки.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Ваши лимиты использования Claude в виде анимированной карточки здоровья жителя…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткие тренировки, пока Claude работает: ежедневная цель, серии, значки и…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Доска использования для Claude Code: расходы по моделям.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Мод Now Playing для Claude Code: Apple Music и Spotify над приглашением, с…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Claude Code mods for orchestrator and worker sessions.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Моды для Claude Code: часы кэша, радиус поражения, предложения, рабочий список…
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - Модификация Claude Code: журнал скоординированной работы с запусками, рабочими…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Модификации Claude Code: Suggestion Spotlight показывает, к чему относится…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашего Claude Code.
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Mods do Claude Code criados por mim (painéis, comandos e hooks).
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Оригинальный движок Doom с Freedoom, доступный внутри Claude Code.
- [cigarette1991/clawd-pet](https://github.com/cigarette1991/clawd-pet) - Clawd, a Claude Code mod that lives above the prompt box.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Просматривайте каждый файл, которого касается Claude, как pull request, не…
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀 전용 Claude Code mods (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [dankelleher/pin-message](https://github.com/dankelleher/pin-message) - Claude Code mod: pin a reply above the prompt, collapsible to a one-line summary.
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Eleven Claude Code mods (function-hook plugins) for a many-parallel-sessions…
- [davidcoulson/punch-list](https://github.com/davidcoulson/punch-list) - A Claude Code mod that keeps one to-do list of the things waiting on you…
- [davidcoulson/session-crew](https://github.com/davidcoulson/session-crew) - A Claude Code mod that shows the side sessions a desktop session starts as…
- [daviddecorso/claude-mods](https://github.com/daviddecorso/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Тамагочи, живущий внутри Claude Code: он вылупляется, ест код, который пишет…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Закладки и метки в стиле vim внутри терминальных бесед Claude Code: выделяйте…
- [devsomelife/somelife-claude-mods](https://github.com/devsomelife/somelife-claude-mods)
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Модификация Code для Claude: полоса над промптом с новостями Claude и срочными…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Мод для Claude Code: после того как guard блокирует вызов инструмента…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Мод для Claude Code: фоновые задания в одном представлении с прогрессом и…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Мод для Claude Code: единый входящий ящик для сообщений от товарищей по…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Мод для Claude Code: объясняет блокировки песочницы и превращает повторные…
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [ecombuilder-web/TripleDigit-crab-agents](https://github.com/ecombuilder-web/TripleDigit-crab-agents) - Claude Code mod: right-side Agents pane showing every working and finished…
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods: rewrite-prompt (Ctrl+P rewrites your draft before you send it).
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods: auto-model-detector routes each prompt to the right model and…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods (function-hook plugins): session-meter and more.
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi — a Claude Code mod: a mascot that reads the room above the prompt, with…
- [g761007/hudcade](https://github.com/g761007/hudcade) - A pixel-art HUD for Claude Code: context, cost, cache, agents and rate limits…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Seven Claude Code mods: savvy-progress, skins, filetree, cache-tax…
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Claude Code plugin marketplace with my mods.
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Useful claude code mods.
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Private marketplace of Claude Code mods.
- [hashswingingslasher/model-hint](https://github.com/hashswingingslasher/model-hint) - Claude Code mod: suggests haiku, sonnet or opus for the task you are typing…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey.
- [hernandezsanti/claude-code-mods](https://github.com/hernandezsanti/claude-code-mods) - Claude Code mods that enforce ticket-based commits, protect paid CI minutes and…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Модификация Code для Claude: три следующих шага после каждого ответа на любом…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Модификация Claude Code: сколько времени занял каждый ответ, сколько времени…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Мод Claude Code: streamer-mode скрывает приватные панели, полосы и строку…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Пульт управления над полем запроса Claude Code. Утка считывает показания.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Обратимая редакция данных для Claude Code: приватные значения заменяются…
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code mod: sidebar file tree that pulses on files Claude just edited.
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Claude Status Bar.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Claude Code mods: context bar and the cyberdeck HUD.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - 自动读取你的工程图，然后在 SolidWorks 里建模。Reads your engineering drawings…
- [jatinmayekar/claude-task-list](https://github.com/jatinmayekar/claude-task-list) - Claude Code mod: task list above the prompt, managed with /task.
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Боковая панель с использованием контекста: общий объём, категории, рост за…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Боковая панель со списком файлов: какие файлы были созданы, изменены или…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пушистик в стиле 8-bit (чёрно-белый вислоухий голландский кролик) бегает и…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Боковая панель «Что я спрашивал»: каждое сообщение владельца в этом разговоре;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Боковая панель с временной шкалой: на что ушло время в этом раунде — ожидание…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Боковая панель обмена токенами: сколько токенов основной разговор отправляет…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Честный пакетик с бобами для claude code: после каждого раунда Claude тихо…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Контрольный список плана для Claude Code с проверкой доказательствами…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI 简体中文汉化（自管版）——自己的翻译表 + patch 工具 + 升级检查.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - Two Claude Code mods: session handoffs with replies, and routing simple turns…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живет в полосе над вашим prompt Claude Code: разыгрывает сессию…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод, озвучивающий ответы и уведомления Claude Code с помощью VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Модификация Claude, позволяющая читать и объединять разговоры между вашими…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Моды Claude Code. PixBar: пиксельное существо над вашим запросом, которое…
- [Kiko-42/claude-code-hist](https://github.com/Kiko-42/claude-code-hist) - Claude Code mod: /hist lists your past prompts and jumps the transcript to the…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Модификация Claude Code для macOS: одно плавающее окно, показывающее, чем…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods.
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - Some proof of concepts for claude-code-mods.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Модификации Claude Code, опубликованные как маркетплейс.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Два мода Claude Code: folio — панель файлов рядом с чатом, и tint…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: интерактивный граф того, что знает Claude Code.
- [KunalKumarkkr01/prompt-rewriter](https://github.com/KunalKumarkkr01/prompt-rewriter) - Claude Code mod: /rewrite &lt;prompt&gt; picks role + task personas, adds recent web…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Не позволяйте своему вниманию отвлекаться, пока вы ждёте ответа Claude Code.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Моды Claude Code от Sanmu — маркетплейс плагинов (боковая панель задач).
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Подготовленное сообществом руководство по модам Claude Code: варианты…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод Claude Code, который показывает, что делает Claude, в подзаголовке вкладки…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy — неофициальный созданный фанатами пиксельный компаньон, который…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - Насколько заполнен контекст Claude, когда его кэш остывает и сколько осталось…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Мод Claude Code: отвечайте на Claude построчно прямо в тексте.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Небольшие модификации для Code для Claude: runner-avatar — небольшой аватар…
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - Small Claude Code mods from the MateAI channel.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Мод Claude Code: панель в реальном времени с тем, к чему стремится ваш AI-агент…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Модификация Claude Code: панель /sessions для просмотра и удаления сессий…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Моды сообщества для Claude Code: защиты, панели и команды, выполняемые внутри…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Боковая панель для Claude Code: файлы, записанные Claude, разделённые…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Тихая боковая панель для Claude Code: чем занята эта сессия, её план, агенты и…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Тусклое время над каждым приглашением и каждым ответом в транскрипте Claude…
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - Claude Code plugins for sessions and memory: a Memory pane mod and a…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, включающий обратно инструменты todo для моделей, которые их не…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Мод для Claude Code, который ждёт безопасной паузы, а затем передаёт вашу…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одной строке на каждую задачу над запросом — текущая…
- [mwmrs/claude-mods](https://github.com/mwmrs/claude-mods)
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Играйте в Connect Four против AI внутри Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Мод Claude Code: когда другой агент программирования делает коммит в ваш…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Claude Code mod: keeps sessions light — usage line, heads-up and one…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Мод Claude Code для репозиториев, которыми пользуются несколько ИИ-агентов: не…
- [netgfx/claude-flow-explainer](https://github.com/netgfx/claude-flow-explainer) - A Claude mod to guide the user step by step on how a flow or code works.
- [netgfx/claude-html-mod](https://github.com/netgfx/claude-html-mod) - A Claude code mod for displaying html in a side panel.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Весёлые бесплатные моды для Claude Code, которые никогда не тратят токены.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Re-arms Claude Code.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Защитный механизм для SQL в Claude Code: запрашивает подтверждение перед тем…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Один мод для Claude Code и Windows, с приоритетом CJK: предварительный просмотр…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Лучшие моды Claude Code, отсортированные по пользе для вас.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Два мода Claude для Claude Code: garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Временные метки для Claude Code: время каждого сообщения, ответа и вызова…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Отслеживание изменений для Claude Code: точно покажите, что Claude изменил в…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Mods for Claude Code: plugins of function hooks that work in any repository.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Various mods and skills for my Claude Desktop setup.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Модификация Claude Code: отслеживает модель, токены, инструменты и время…
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Модификация Claude Code: каждый субагент представлен маленьким человечком в…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Моды для Claude Code: safety-guard блокирует разрушительные команды и доступ к…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Анимированный пиксельный краб Claude для Claude Code: он изображает действия…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [razzamatazm/cache-keeper](https://github.com/razzamatazm/cache-keeper) - Claude Code mod: keeps an idle session.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Мод Claude Code: отжимания, которые нужно делать, пока работает Claude.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - just a list of mods I.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Три модификации Claude Code без зависимостей: адаптивная строка состояния…
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - My mods for Claude Code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Мод Claude Code: превращает план, который вы утверждаете в plan mode, в живой…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Подборка Claude Code-модов. Каждый элемент клонирован и проверен с помощью…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Бесплатный режим: вспомогательные агенты работают на Haiku, а большие файлы и…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музыка в стиле lofi, сопровождающая сессию: спокойствие, концентрация, поток, а…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Учитесь, пока Claude пишет код: после хода, изменившего код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запись каждого изменения, которое вносит Claude: воспроизводите каждое…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Claude Code mods: token-bar, your context window and usage limits above the…
- [shaharz/pr-watch](https://github.com/shaharz/pr-watch) - Claude Code mod: watch PR checks and review comments (Codex included) in a…
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Mission control for Claude Code: live subagent fleet, token/cost usage, effort…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Showrin.
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Персональные моды Claude Code.
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Claude Code mod: context-window meter per session, with Compact now…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Mody Claude Code (function hooks): panel agentów, pasek budżetu, flota sesji.
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Не позволяйте вспомогательным агентам (субагентам) Claude расходовать ваши…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commit messages в один клик для Claude Code с танцующей pixel-art Malenia.
- [Stoneeu/zh-tw-dictation](https://github.com/Stoneeu/zh-tw-dictation) - Claude Code mod: Simplified Chinese in the prompt box.
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - 직접 만든 Claude Code mod 모음 (플러그인 마켓플레이스).
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 手元で使う Claude Code の mod 置き場.
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Claude Code mod: see your Cursor / VS Code file and selection above the prompt…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — мод Claude Code, показывающий использование вашего плана Claude…
- [texxmexx/claude-usage-bar](https://github.com/texxmexx/claude-usage-bar) - Claude Code-mod: förbrukningsband ovanför textrutan.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, отображающий текущую сессию на панели: каждое приглашение…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Plugin marketplace модов Claude Code: function-hooks plugins, которые рисуют…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod: rewrites a rough prompt in place, naming fitting skills, open…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Слушайте ответы Claude Code, пока читаемое предложение выделяется.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Claude Code mods by Toptaab.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Claude Code mod that checks the English of your prompt while you write it.
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Small, fun and useful mods for Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анимированная полоса прогресса и сводка по завершении для…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Три небольших мода Claude Code: узнайте, когда завершат работу ваши субагенты…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажите «Я потерялся», и Claude снова объяснит свой последний ответ простыми…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Задайте Claude дополнительный вопрос на панели рядом с вашей работой.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code отправляет вам сообщения в Telegram, когда задача выполнена или…
- [WarrenLin/claude-typing-practice](https://github.com/WarrenLin/claude-typing-practice) - ⌨️ Claude Code mod：等 AI 回覆時練打字，即時顯示 WPM 與正確率.
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Мод Claude Code: маркер для ответов, боковая панель для результатов запросов в…
- [wendyyyanto/usage-meter-mod](https://github.com/wendyyyanto/usage-meter-mod) - A Claude Code mod that shows your usage limits, context, model and effort in a…
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter)
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod per Claude Code: segreti oscurati, cose da fare, verifiche e CI, diario…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Плагин Claude Code: лимиты использования Claude Pro/Max с прогнозом темпа…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моды для Claude Code. agent-crew: наблюдайте за работой субагентов как за живой…
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - Terminal side-panel mods for Claude Code — agent tracing, token-powered Tetris…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Интерактивная доска задач для Claude Code: планируйте перед началом работы…
- [youngin-abel-kim/context-gauge](https://github.com/youngin-abel-kim/context-gauge) - A Claude Code mod: the context window as a one-line gauge above the prompt…
- [yu1745/claude-code-image-view](https://github.com/yu1745/claude-code-image-view) - Claude Code mod: show images inline in the terminal.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Отобранная вручную коллекция лучших ресурсов для самых потрясающих агентов…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Плагин Claude Code, показывающий, что происходит: использование контекста…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Красивая, полностью настраиваемая строка состояния для Claude Code CLI с…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Все части системного промпта Claude Code, 27 встроенных описаний инструментов…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Более 45 советов по максимально эффективному использованию Claude Code — от…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — создание каруселей Xiaohongshu и пар обложек…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Красивый powerline в стиле vim для Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Просматривайте diff вашего агента кодирования в панели терминала и отправляйте…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Комплексный плагин статусной строки для Claude Code с использованием контекста…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Создавайте моды для Claude Code: перехватывайте любой запрос, изменяйте любой…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Комплексная панель statusline для Claude Code — информация о сессии, шкалы…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: отслеживайте углеродный след своих сессий Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Эстетичная statusline для Claude Code от awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Общедоступные Skills и моды для Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, моды, субагенты, хуки, slash-команды и руководства для Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Законно бесплатные LLM APIs и агенты программирования — самообновление…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Быстрый калькулятор стоимости без зависимостей и настраиваемая строка состояния…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Строка состояния терминала для сессий Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Онлайн-счета футбольных матчей, расписание и турнирные таблицы для…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, превращающий вашего агента программирования в эксперта по…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Время молитв, дата по хиджре, азкары, ежедневный аят, пост по сунне, Рамадан…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Личная конфигурация Claude Code, версионируемая внутри ~/.claude — агенты…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — плагин DeepSeek Harness для исследовательских тем…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Двухстрочная статусная строка truecolor для Claude Code.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Набор плагинов для Claude Code, pi и DeepSeek Harness: HUD в строке состояния…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Портативный набор инструментов Claude Code для .NET DDD/Clean Architecture…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Лёгкая строка состояния Claude Code — один Bash-скрипт примерно на 170 строк…
- [yuyongyan29-dev/claude-pet](https://github.com/yuyongyan29-dev/claude-pet) - Clawd, a pixel pet that lives above your Claude Code prompt — a Claude Code…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагины Claude Code, которые я использую каждый день: навыки и моды…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Неофициальные моды для вкладки Code в Claude Desktop — usage-pet: полоса…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Мост DSH &lt;-&gt; Feishu (Lark), разработанный самостоятельно (не форк): потоковая…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Маркетплейс плагинов и навыков Claude Code для создания модов игры Hytale.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Управление токенами для Claude Code: лучшая модель направляет работу, а…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Split-pane viewer for Claude Code in Windows Terminal and tmux: the session as…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Репозиторий модов Awesome Media для Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Сократите расходы на Claude Code и токены Codex: направляет запросы и тестовые…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Настраиваемая строка состояния Claude Code для Linux, WSL, Windows и macOS с…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Отображение строки состояния Claude Code с ограничениями частоты запросов…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Строка состояния и строка токенов для Claude Code: контекст, использование за 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Отображение ключевых сведений о состоянии Claude Code, включая модель…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Нативные команды агентов. Под контролем.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Дополнения Claude Code: наблюдатель цветных точек статуса вкладок + встроенная…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [zirkelc/claude-quick-actions](https://github.com/zirkelc/claude-quick-actions) - One-click buttons above the Claude Code prompt for the skills, prompts and…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Строка состояния использования Claude Code для macOS и Linux, упакованная как…
- [aromarious/claude-code-plugins](https://github.com/aromarious/claude-code-plugins) - Личный маркетплейс плагинов Claude Code (todo-pane).
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD Mod: a CRT-style status panel for Claude Code, in the terminal…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Строка состояния Claude Code в Lua с интерактивной площадкой Neovim в реальном…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Профессиональная строка состояния Claude Code: длительность сессии, стоимость в…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Строка состояния Claude Code с учётом подписки.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Строка состояния Claude Code на испанском языке: задача, навыки, контекст со…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Красочная строка состояния Claude Code: лимиты плана, контекст, стоимость и…
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Строка состояния Claude Code для Windows: общее количество токенов, стоимость…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Однострочная строка состояния для Claude Code: модель, git, контекст, токены…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Предпросмотр изображений внутри Claude Code: наведите курсор на чип под…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Claude Code status line with agent panel rows.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Синхронизируйте задачи Claude с Fizzy.do, чтобы команда видела изменения в…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Display a detailed, color-coded status bar for Claude Code showing context, git…
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Talk to Claude Code by voice on Windows: a Mod + helper using codex app-server…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Отслеживайте состояние Claude Code с помощью компактной панели, показывающей…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Хук строки состояния Claude Code — отслеживает использование токенов и контекст…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Установщик окружения Claude Code: skills, statusline, hooks, permissions и…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness de Claude Code de Nacho (reglas, tablero, mods).
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Multi-line Claude Code status line: context bar, git branch, 9router…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Строка состояния в стиле HUD для Claude Code — состояние сети, TPS, контекст…
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - OrihuelaConde.
- [Paradigm-Study/claude-share](https://github.com/Paradigm-Study/claude-share) - Shared Claude Code sessions: share a session with a link, teammates join from…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — строка состояния Claude Code для macOS +…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitor Claude Code status from your macOS menu bar with real-time indicators…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Навыки и моды для Claude Code и Cowork — трекер проектов, справочный документ и…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Claude Code status line for Windows (PowerShell): usage bars, 5h/7d reset…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Двухстрочная строка состояния для Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Настраиваемая строка состояния Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Starter harness for Claude Code: hooks, statusline, local models, swarm…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Портативная конфигурация Claude Code (строка состояния + установщик).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Небольшая панель для Claude Code: процент контекста, обратный отсчёт кэша…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Пользовательская строка состояния терминала для Claude Code: модель, каталог…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Портативная конфигурация Claude Code: CLAUDE.md, settings, statusline, skills.
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Track Claude Code context usage, session costs, and rate limit resets with a…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Набор модификаций для Claude Code.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Строка состояния Claude Code: текущий идентификатор модели, имя хоста…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Навык Claude Code (VS Code, Windows): предварительный просмотр изображений и…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Строка состояния Claude Code: папка, ветка git, модель, использование…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Детектор деградации контекста 2026 — проактивный монитор памяти ИИ и лимитов…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, субагенты и statusline для Claude Code: open-source коллекции и…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Статусная строка Claude Code с отображением использования токенов в реальном…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - Строка состояния на основе Deno для Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Моды для Claude Code: панели, полосы и компаньоны на основе перехватчиков…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Пакет интерфейса в стиле Claude Code для агента программирования Pi…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Передавайте задачи между сеансами Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Это на сервере MCP для управления MODS — модульным кроссплатформенным…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Навык Codex и Claude Code для перевода модов CK3 с помощью локального LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Моды с открытым исходным кодом и другие расширения для Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Строка состояния Claude Code: эстетика CCometixLine + функциональность HUD…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: находите то, о чём вы снова и снова просите Claude Code, и…

</details>

<a id="dsh-cordis"></a>

## Экосистемы плагинов DSH и Cordis

DeepSeek Harness и Cordis приходят к тому же результату с другой стороны: для них плагин является механизмом модификаций, поэтому плагин там эквивалентен моду здесь.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74385 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **74385**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐125056 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **125056** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100648 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **100648** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82288 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **82288**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35767 · Go · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **35767**  |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25508 · Python · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **25508**  |
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
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8651 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **8651**   |
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
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐7881 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Python                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **7881**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

<sub>Материал подключён по прямой ссылке из исходного репозитория, поскольку лицензия, разрешающая свободное распространение, не указана.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4544 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **4544**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4323 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **4323**   |
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
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐2954 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Answer me with HTML — an agent skill that answers hard questions with a one-page HTML you can actually read. 让 AI Agent 用一页 HTML 回答复杂问题。

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **2954**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1600 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **1600**   |
| Последний push   | 2026-10-12 |
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
<summary>🧵 <b><a href="https://github.com/OpenPetsHQ/openpets">OpenPetsHQ/openpets</a></b> · ⭐1281 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Local first, desktop companion platform with animated pets, plugin SDK and coding-agent integrations.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1281**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `ai-agents` · `claude-code` · `coding-agents` · `desktop-companion` · `desktop-pet` · `dsh-plugin` · `electron` · `mcp`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/openpetshq--openpets/cc09d7a603fef14d.png" width="100%" alt="OpenPetsHQ/openpets screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1178 · Go · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **1178**   |
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
<summary>🧵 <b><a href="https://github.com/ysr666/dsh-vision-router">ysr666/dsh-vision-router</a></b> · ⭐1145 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Eyes for text-only DeepSeek Harness agents: built-in free vision chain (no key) + pixel-level vision tools (Q&A, grounding, crop, pixel diff, colors, OCR, SVG trace, cutout, screenshots). One-command install, no Python, image turns work like ordinary tool-calling turns.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1145**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `multimodal` · `vision`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ysr666--dsh-vision-router/106ad9ed68079834.png" width="100%" alt="ysr666/dsh-vision-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ysr666--dsh-vision-router/d79f0c95491a7bc3.gif" width="100%" alt="ysr666/dsh-vision-router animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1009 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

The most comprehensive DeepSeek Harness plugin market — refreshed daily, sourced across the Internet, reviewed before publishing.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1009**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐552 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **552**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>анимированная запись · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">Открыть видео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/1692775560/dsh-Mimir-Academic-research">1692775560/dsh-Mimir-Academic-research</a></b> · ⭐548 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Mimir — 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表、GPU 服务器 SSH 任务编排，管理科研全周期。An open-source research workbench plugin for the whole research cycle.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **548**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `arxiv` · `bibtex` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `experiment-tracking` · `gpu-cluster` · `latex`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/1692775560--dsh-mimir-academic-research/3574bee232095c3c.png" width="100%" alt="1692775560/dsh-Mimir-Academic-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/1692775560--dsh-mimir-academic-research/e05a56815f6c9f53.gif" width="100%" alt="1692775560/dsh-Mimir-Academic-research animation"><br><sub>анимированная запись · <a href="https://raw.githubusercontent.com/1692775560/dsh-Mimir-Academic-research/main/docs/media/mimir-demo.mp4">Открыть видео</a></sub></td>
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
| Впервые в списке | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **204**    |
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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐180 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин резервного копирования и восстановления DeepSeek Harness (DSH) — экспортируйте, импортируйте, переносите и синхронизируйте всю конфигурацию DSH, плагины, серверы MCP, навыки и рабочее пространство. Перенос на другой компьютер в один клик.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **180**    |
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
<summary>🧵 <b><a href="https://github.com/sorsama/deepseek-harness-mobile">sorsama/deepseek-harness-mobile</a></b> · ⭐146 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Android — компаньон для DeepSeek Harness | чаты, цели, подтверждения и уведомления с телефона через локальную сеть. Kotlin + Jetpack Compose.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Kotlin                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **146**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `ai-agents` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sorsama--deepseek-harness-mobile/11352624becb7d93.jpg" width="100%" alt="sorsama/deepseek-harness-mobile screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

27 навыков для разработки и повышения эффективности из mattpocock/skills v1.3.1 устанавливаются вместе с плагином, поэтому устанавливать навыки вручную не нужно. Плагин создан с использованием 40 миллиардов токенов и обеспечивает десятикратное повышение эффективности разработки по сравнению с исходными навыками, а также помогает новичкам быстрее освоить этот набор навыков. Полная поддержка GitHub issue; Markdown пока в предварительной версии; GitLab пока не поддерживается. Спасибо за использование и поддержку 💗

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **137**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

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

自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and validate the DeepSeek-Harness community plugin marketplace.

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
| Впервые в списке | 2026-10-12 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐60 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）

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
| Впервые в списке | 2026-10-12 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/webkubor/dsh-bloom-theme">webkubor/dsh-bloom-theme</a></b> · ⭐59 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness (DSH) 主题插件：Bloom 莫兰迪配色 10 套中国风命名（黛蓝/朱砂/桃夭/天青/竹青/赭石/青金/琥珀/落霞/青莲），OKLCH 调色，明暗双主题，顶栏一键切换，20 组配色实测全部达 WCAG AA

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **59**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `accessibility` · `color-scheme` · `dark-theme` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `morandi`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/webkubor--dsh-bloom-theme/107985cbb7fe6b29.png" width="100%" alt="webkubor/dsh-bloom-theme screenshot"></td>
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
| Последний push   | 2026-10-12 |
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

面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体。纯本地、零模型调用、零网络。  Task-aware workspace context retrieval and lifecycle tracking for AI coding agents. Find, organize, and track the workspace context most relevant to the task at hand — locally, deterministically, zero model calls, zero network.

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
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/398894496-arch/KRouter">398894496-arch/KRouter</a></b> · ⭐44 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Your coding agents remember what you decided — and what you changed. Plain-Markdown memory in Obsidian, shared by Claude Code, Codex and Cursor over MCP. Every answer cites its page; when the vault does not know, it says so. Imports your past sessions on install.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | Python                                                                 |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **44**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-memory` · `ai-agents` · `chinese` · `claude-code` · `claude-code-plugin` · `codex` · `cursor` · `deepseek`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/398894496-arch--krouter/482bdf9e0e0aaa00.gif" width="100%" alt="398894496-arch/KRouter screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/398894496-arch--krouter/482bdf9e0e0aaa00.gif" width="100%" alt="398894496-arch/KRouter animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **44**     |
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
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐36 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **36**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>анимированная запись</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

NekroNXT: мультиплатформенная система агентов для групповых чатов на базе DeepSeek Harness (DSH)｜Мультиплатформенная система агентов для групповых чатов на базе DSH

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **35**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 59</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Защита перед выполнением для AI-агентов программирования.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Отобранный список лучших отличных ИИ-плагинов для ИИ-ассистентов, включая…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Плагин DSH — бесплатные модели OpenCode Zen для DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Рынок плагинов DSH / DSH Plugin Marketplace: в веб-интерфейсе DeepSeek Harness…
- [arcships/rutis](https://github.com/arcships/rutis) - Среда выполнения плагинов для самоизменяющегося программного обеспечения…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Избранный каталог плагинов DeepSeek Harness (DSH) — более 280 плагинов…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Плагин DeepSeek Harness: сопоставление окна контекста модели в один клик…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Коллекция веб-плагинов GUI для DSH (DeepSeek Harness) — уведомления о задачах…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - Управление обновлениями основной программы DeepSeek Harness и плагинов…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Среда выполнения для коммерческих переговоров A2A + плагин DeepSeek Harness…
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Панель инструментов для DeepSeek Harness Web: менеджер MCP.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Настоящий PowerPoint, а не HTML. Расскажите ИИ, что нужно осветить, и pptwise…
- [ppy-web/dsh-plugin-xiaomi-mimo-tts](https://github.com/ppy-web/dsh-plugin-xiaomi-mimo-tts) - 给DSH接入免费的 Xiaomi MiMo TTS API，支持使用预置/自定义/浏览器内置声音朗读正文.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Локальный граф знаний кода и среда контекста для агентов программирования.
- [MichengAI/dsh-btw](https://github.com/MichengAI/dsh-btw) - DSH 一次性只读旁问插件：基于当前上下文回答，独立气泡，不执行工具 · One-shot read-only side-ask plugin…
- [zhu1090093659/dsh-skins](https://github.com/zhu1090093659/dsh-skins) - Skin center plugin and built-in skins for the DSH Web GUI: skins are pure asset…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Плагин AI-инженерии Embedded C/C++ — навыки работы с прошивками.
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [biedongbin/dsh-claude-compat](https://github.com/biedongbin/dsh-claude-compat) - DSH plugin: bridge Claude Code.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Превратите модели, уже авторизованные в настольном приложении WorkBuddy на этом…
- [zhu1090093659/dsh-pet](https://github.com/zhu1090093659/dsh-pet) - Multi-pet companion plugin for the DSH Web GUI: a registry-driven floating pet…
- [islibaodong/dsh-login](https://github.com/islibaodong/dsh-login) - Multi-user login gateway plugin for the DeepSeek Harness Web GUI: login wall…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - плагин dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Постоянное тестирование совместимости плагинов DeepSeek Harness: точные версии…
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - Zero-cost, zero-hassle toolkit for DeepSeek Harness (DSH): one-click setup for…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Защищённое сжатие контекста для DeepSeek Harness (dsh): LLM предлагает…
- [FrostLeafKEE/dsh-chat-bridge](https://github.com/FrostLeafKEE/dsh-chat-bridge) - Switch between DeepSeek web chat and workspaces in DeepSeek Harness.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Хост-плагин DeepSeek Harness, который хранит документы проектов и…
- [tafcear/kimi-tide](https://github.com/tafcear/kimi-tide) - 🌊 月汐（kimi-tide）— DSH…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray для плагинов DeepSeek Harness: заявленные возможности против фактического…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [PeterBon/dsh-hooks](https://github.com/PeterBon/dsh-hooks) - Config-driven lifecycle hooks plugin for DeepSeek Harness.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Рабочее пространство с несколькими папками: позволяет агенту DSH.
- [JessenReinhart/dsh-tokenslash](https://github.com/JessenReinhart/dsh-tokenslash)
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Плагин DSH: окно инструментов Git уровня IDE в виде нативной вкладки…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [laoduu/DeepSeek-Harness-yizi-themes](https://github.com/laoduu/DeepSeek-Harness-yizi-themes) - 为 DeepSeek Harness（dsh）Web UI 提供的 19 个精品风格主题，完整移植自 YiziMarkdown 的设计语言.
- [openbkn-ai/bkn-dsh](https://github.com/openbkn-ai/bkn-dsh) - OpenBKN.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт проверки плагинов DeepSeek Harness (dsh) без зависимостей…
- [SuCriss/dsh-leekbox](https://github.com/SuCriss/dsh-leekbox) - 韭菜盒子 LeekBox — A股看盘助手 · DeepSeek Harness (DSH) web 插件.
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode в DeepSeek Harness — плагин DSH, поддерживающий работу OpenCode Zen и…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонний маркетплейс плагинов и защищённый менеджер жизненного…
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Run DeepSeek Harness on desktop with zero token costs—a free, open-source GUI…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) - DSH的插件创意市场来啦!～～～欢迎使用&amp;提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Веб-плагин DeepSeek Harness (DSH): вкладка боковой панели market-dashboard для…
- [whyself/Amadeus](https://github.com/whyself/Amadeus) - Amadeus: a web workspace for DSH with cloud and web agents, online code…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Плагин DeepSeek Harness: превращает сбой выделения ACL песочницы Windows…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Делает повторно запускаемой неатрибутированную попытку с пустой моделью для…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Оценка прогресса для автономных раундов целей dsh: откладывает цикл, пока…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - Плагин dsh: превращает остановку из-за усечения длины в восстановление после…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Плагины, которые убирают за собой: порт фреймворка плагинов cordis для iOS и…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Среда выполнения плагинов Rust с проверенным Verus ядром жизненного цикла и…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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

<a id="other"></a>

## Другие проекты

Записи, затрагивающие поверхность модификаций, но сами модами не являющиеся; они остаются видимыми, а не скрываются.

<details>
<summary>📦 <b><a href="https://github.com/rajmand/claude_mods">rajmand/claude_mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Сводка

Описание из upstream не было опубликовано.

##### 📌 Основные сведения

| Поле          | Значение                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категория     | `Другие проекты`                                                          |
| Подтверждение | `в собственном тексте упоминается мод API или заявляется поддержка модов` |
| Язык          | TypeScript                                                                |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **0**      |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

</details>

<a id="projects-by-implementation-language"></a>

## Проекты по языку реализации

Экосистема сосредоточена в Python и TypeScript, но типизированные клиенты продолжают появляться и на других языках. Эта таблица генерируется из самих записей.

| Язык       | Записей | Примеры                                                                                                            |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 399     | `anthropics/claude-code`, `anthropics/claude-code-action`, `AlekDob/blockodile-claude-mod`                         |
| JavaScript | 72      | `fschmutz/claude-usage-panel`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                  |
| Python     | 37      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `redfox-data/redfox-community-dsh` |
| Shell      | 28      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`                |
| HTML       | 11      | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                                 |
| Go         | 4       | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `esengine/DeepSeek-Reasonix`                            |
| Rust       | 4       | `persiyanov/herdr-reviewr`, `OpenClawFarm/claude-statusline`, `arcships/rutis`                                     |
| PowerShell | 3       | `GoSlowPoke168/claude-statusline`, `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win`     |
| Swift      | 2       | `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`                                            |
| C          | 1       | `reporails/arcade`                                                                                                 |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                            |
| CSS        | 1       | `zhu1090093659/dsh-skins`                                                                                          |
| Kotlin     | 1       | `sorsama/deepseek-harness-mobile`                                                                                  |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                               |
| MDX        | 1       | `jkf87/mod-guide`                                                                                                  |

<sub>Учитываются только записи, в которых указан язык. Документация и обсуждения исключены из этой таблицы.</sub>

## Участие

Исправления приветствуются и являются самым быстрым способом улучшить этот список. Откройте issue или pull request, если запись попала не в тот раздел, получила неверную оценку или если проект был ошибочно исключен как совпадение имени — именно в этой последней категории автоматические фильтры чаще всего ошибаются.

---

<sub>Независимый проект сообщества. Не аффилирован с Anthropic, не одобрен и не проверен им. Claude Code, Claude и Anthropic являются товарными знаками Anthropic. Поведение продукта может меняться без уведомления; всё критически важное проверяйте по официальной документации. Материалы остаются собственностью исходных проектов и воспроизводятся только там, где это разрешено лицензией.</sub>

<sub>Последнее обновление · 2026-10-12T17:03:53+08:00</sub>
