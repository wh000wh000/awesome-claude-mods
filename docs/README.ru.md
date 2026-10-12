<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Отличные моды для Claude">
</p>

<h1 align="center">Отличные моды для Claude</h1>

<p align="center"><b>Индекс модов, плагинов Claude Code и более глубоких изменений поведения, составленный с оценкой доказательности.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-605-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <b>Русский</b> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Актуальный индекс** · Последняя синхронизация: `2026-10-12T19:16:21+08:00` (UTC+8)
> · Записей: **605** · Добавлено в последнем обновлении: **0** · Языки реализации: **14**

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
<sub>⭐74394 · TypeScript · 👁️ observed</sub>
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
- [Официальные: собственные репозитории и примечания к выпускам Anthropic](#официальные-собственные-репозитории-и-примечания-к-выпускам-anthropic) — **16**
- [Моды: созданы с использованием возможности модификации](#моды-созданы-с-использованием-возможности-модификации) — **474**
- [Экосистемы плагинов DSH и Cordis](#экосистемы-плагинов-dsh-и-cordis) — **103**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150319 · TypeScript · ✅ official · 0 天</summary>

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
| Звёзды           | **150319** |
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
<summary><b>Больше в этой категории</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Добавлен `$.ui.notify` для модов: вызывает нативное уведомление через ваши…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Исправлена ситуация, когда Esc или прерывание во время хука `UserPromptSubmit`…
- [AlekDob/blockodile-claude-mod](https://github.com/AlekDob/blockodile-claude-mod) - Официальный мод Blockodile для Claude Code: анимированная боковая панель с…

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐512 · JavaScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **512**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐200 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **200**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐151 · TypeScript · 👁️ observed · 7 天</summary>

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
| Звёзды           | **151**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐125 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **125**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐106 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **106**    |
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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐81 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **81**     |
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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐71 · TypeScript · 👁️ observed · 9 天</summary>

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
| Звёзды           | **71**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐61 · Shell · 👁️ observed · 5 天</summary>

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
| Звёзды           | **61**     |
| Последний push   | 2026-10-07 |
| Впервые в списке | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

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

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Коллекция из более чем 100 модов, которые можно использовать с Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Модификации Claude и инструменты для их создания: сначала навык-сборщик, затем…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Среда Claude Code, которую я запускаю каждый день, публикуемая под этим именем…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Наденьте новую крышу на Claude Code с помощью Claude Mods: не изменяя бинарный…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Четыре мода Claude Code: Cache Keeper, Recording Mode, Goal Meter и Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Моды Claude Code от Learning Hacker: сделайте работу агента понятной для…
- [kakha13/claude](https://github.com/kakha13/claude) - Моды Claude Code, исправляющие и переводящие ваши подсказки до того, как их…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Моды и навыки Claude Code от Nekyia Labs, создаваемые и ежедневно используемые…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - База знаний Obsidian с указанием источников о модах Claude Code: как они…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Модификация, придающая терминальному журналу Claude Code вид настольного…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Боковая панель для кода Claude: субагенты, запускаемые сессией, выполняемая…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Панель боковой панели Claude Desktop (вкладка Code): перечисляет все…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Навык, обучающий агентов Claude Code создавать Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Полоса использования над полем ввода Claude Desktop (вкладка Code): лимиты 5h /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Пользовательские моды, плагины и навыки Claude, устанавливаемые из одного…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (плагины с перехватчиками функций) для Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Галерея модов Baselane: моды Claude Code, проверенные и закреплённые.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Очередь решений CLI/TUI для людей, работающих с разговорными агентами.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Модификация панели IDE Claude Code: доска агентов, дерево файлов и просмотрщик…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Мод Claude Code, отображающий различия Edit и Write в двух расположенных рядом…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, отрисовываемый в поле приглашения Claude Code по мере ввода.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Моды Claude Code: панель использования 像素螃蟹 usage-hud + HTML-ссылки, по которым…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плавающая карточка состояния для Claude Code — модель, контекст, ограничения…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Моды для Claude Code: плагины с функциональными хуками, добавляющие…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Моды Claude Code: screen-guard маскирует имена и секреты во время демонстрации…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Расширения Claude Code. Раскройте всю мощь Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Мод Claude Code (плагин), который добавляет боковую панель с вкладками…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Панели, защитные механизмы и полезные моды для Claude Code: контекст…
- [ngothanhluc/claude-mermaid-mod](https://github.com/ngothanhluc/claude-mermaid-mod) - Мод для Claude Code: отображает блоки mermaid в ответах Claude в виде диаграмм…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Два мода Claude Code над полем приглашения: измеритель контекстного окна…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Продлите действие плана Claude Pro: моды Claude Code для точного HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Чтение markdown-файлов, которым код Claude даёт имена, с отображением рядом с…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Мод Claude Code: миниатюры вставленных изображений над приглашением в любом…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Голосовой напарник для Claude Code. Обсуждайте задачи с 3D-волком на базе…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Моды Claude Code: typing-speed, спидометр скорости печати в реальном времени со…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Фейерверки для Claude Code: каждое нажатие клавиши, вызов инструмента, коммит и…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Тест скорости печати на время, пока работает Claude.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Моды для Claude Code: панели, команды и хуки, созданные с помощью плагина…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Находите моды, плагины и расширения Claude Code с анимированными…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Мод Claude Code: диаграммы mermaid, встроенно отображаемые в расшифровке.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Модификации и скины для Claude Code: индикатор выполнения задач Claude в…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Небольшие моды Claude Code (плагины с перехватчиками функций): session-switcher…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Моды Claude Code: меню инструментов Claude, режим Zen, темы терминала, элементы…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Моды Claude Code: mod-scout (поиск наиболее нужных вам модов), usage-meter…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Два мода Claude Code для одновременного запуска множества сеансов: карточка…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Моды Claude Code от Ray Amjad: панели, полосы, защита приглашений, работа с…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: поиск, просмотр, переключение и обновление модов Claude Code.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Моды Claude Code: панель контекста, панель агентов, размытие PDPA.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Лучшие моды Claude Code: отобранные вручную, проверенные, закреплённые.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Плагин Claude Code: автоматическая маршрутизация моделей Claude.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Обрезает огромные выводы инструментов до того, как они заполнят контекст Code…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Мод для Claude Code: интерактивная панель с GitHub PR, которые открывает или…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Шесть модов для Claude Code: анимированный маскот Clawd, индикаторы лимита…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Маркетплейс модов для Claude Code: пошаговый отладчик цикла агента, подсказки…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Моды с открытым исходным кодом для Claude Code: панели, строки состояния…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Шесть модификаций Claude Code: ограничения плана и контекст над полем запроса…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Лучший универсальный набор модов для Claude Code: лимиты использования и HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Смотрите YouTube Shorts в своём Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набор инструментов Naren для Claude: skills, mods и MCP servers для Claude…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Моды для Claude Code: Clawd, крошечный пиксельный талисман, который показывает…
- [reporails/arcade](https://github.com/reporails/arcade) - Классические компьютерные игры в виде модов Claude Code, в которые можно играть…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Кураторский список модификаций Claude Code, устанавливаемых как через…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Моды Claude Code по запросу — навык, который читает ваш разговор и создаёт…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Два Claude Code-мода: cache-keeper и ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Крайне авторский плагин Claude Code, созданный любителем Rust, одержимым…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Моды Claude Code, которые помогают агенту не отклоняться от цели — перехватчики…
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Модификации Code для Claude, которыми я пользуюсь.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Дашборд macOS notch для Claude Code: лимиты использования, открытые сессии…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude готовит. Общайтесь со своей командой.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Мод для Claude Code: панель кэша промптов, следующие шаги, быстрые кнопки и…
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Стоимость, токены и лимиты тарифов ваших агентов программирования.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Мод Claude Code, отображающий ваши лимиты использования и расходы в полосе над…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моды Claude Code от Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Моды для Claude Code: индикаторы выполнения планов, журнал того, что Claude…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Смотрите, что Claude Code запускает в фоне: субагенты, задания Codex, shell…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code-моды от MacLeod Labs: streams распутывает перемешанную работу…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Полевые заметки первого дня о модах Claude Code на Windows: топливная шкала…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: отладчик вызовов инструментов Code для Claude.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code mod: live GitHub pull request status.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Небольшие карточки, расположенные под запросом Claude Code или закреплённые…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живые индикаторы стоимости, контекста и квоты плана над…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Мод Claude Code, который задерживает разветвление субагентов, запросы с большим…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 навыков агента для Claude в пяти наборах.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods для claude.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Плагин и мод Claude Code: AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Мод Claude Code, который включает и отключает глобальные навыки, агентов…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Плагины Claude Code (моды): переключение между несколькими аккаунтами Claude…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Протестированные Claude Code-моды, устанавливаемые одной командой: защитные…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Моды для Claude Code: плагины, созданные на основе function hooks.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Собственный маркетплейс модов-плагинов для Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Набор модов для claude code, созданных мной.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Моды Claude Code. touch-map: просматривайте в виде дерева и карты активности…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Учите иностранный язык во время работы с Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Следит за долгой сессией Claude Code, чтобы вам не пришлось: отслеживает…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Боковая панель с данными о текущих расходах, токенах и использовании контекста…
- [arifamir/nukey-kit](https://github.com/arifamir/nukey-kit) - Nukey the microwave: a Claude Code mod and plugin marketplace.
- [atharv6f/headway](https://github.com/atharv6f/headway) - Цель, задачи и агенты над вашим промптом Code для Claude — без настройки.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моды Claude Code для настоящих инженеров.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Краткий обзор терминальной сессии Code для Claude во вкладке Code приложения…
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Коллекция Claude Code-модов от jack.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Мод Claude Code: панель с задачей сеанса, тем, что требует вашего внимания…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Code-мод для Claude: ловите пиксельных Modsters в игре в режиме ожидания, пока…
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Универсальный Claude Code-мод: интерактивный HUD, защитные механизмы.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Посмотрите, какие файлы есть в контексте каждого агента Claude Code и какая…
- [deejay-hub/sf-headless-band](https://github.com/deejay-hub/sf-headless-band) - A Claude Code mod for Salesforce showing which Orgs are connected.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Превратите каждую сессию Claude Code в небольшое приключение: генеративная…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Небольшие моды Claude Code для терминала и настольного приложения.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навык + мод Claude CLI, добавляющий испанские слова в ответы агента.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - События Alarum над промптом Claude Code: что только что поступило и передача…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Ваш список задач Floatee над промптом Claude Code: запускайте, направляйте и…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - A Claude Code mod for capturing thoughts mid-work, triaging them across…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Боковая панель в стиле Evangelion для Claude Code: контекст, квота, активность…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Мод Claude Code, который стилизует его под The Machine из Person of Interest.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Мод Claude Code: отряд в стиле пиксель-арта предлагает подходящую модель…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: модификация Claude Code для обязательных проверенных рабочих…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Мод Claude Code: отдельная панель для каждого субагента, файлов, которых они…
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Code mod (CC tint mod): color each window by its repository, ring the…
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - Различные моды для claude, которые я считаю полезными.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Мод Claude Code: статус сессии, живой прогресс Spec Kit и управление окном…
- [KevinYu1580/jev-cc-model-router](https://github.com/KevinYu1580/jev-cc-model-router) - Claude Code-мод: выбирает модель один раз за сессию, а уровень усилий — на…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Окно контекста в виде строки над запросом, отображаемое так же, как Claude Code…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Интерактивный HUD задач для Claude Code Desktop: полоса над запросом во время…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Плагин Claude Code (мод), который делает интерфейс терминала Claude Code…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Не позволяйте своему вниманию отвлекаться, пока вы ждёте ответа Claude Code.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Четырнадцать Claude Code-модов в одном плагине, каждый можно включать отдельно;
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Бесплатный плагин с открытым исходным кодом для Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Подборка Claude Code-модов, демонстрации от их оригинальных создателей…
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Claude Code mods for long sessions: sitrep boxes each reply.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Сохраняйте промпты на потом и возвращайте их в поле ввода Claude Code.
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Модификации Claude Code: отобранные и протестированные, причём каждая…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Модификации Code для Claude: автоматическая передача и индикатор выполнения.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навыки Claude Code: проверка фактов в документации, аудит кода, журнал памяти…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Мод Claude Code, который переписывает черновые запросы в понятные перед…
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Мод Claude Code, который ведёт актуальный журнал Evidence, предоставляемых…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Модификации Claude Code от Pedro La Rosa — на одном маркетплейсе плагинов.
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Модификация Claude Code: ограничения использования на 5 часов и 7 дней в виде…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагин-компаньон Claude Code: ASCII-компаньон над запросом, который помнит ваши…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Плагин Claude Code для управления видимостью инструментов каждого агента…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Отображение формул LaTeX в режиме display в терминале Claude Code: MathJax…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Коллекция Claude Code-модов.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Коллекция отличных модов Claude Code | 모드 모음집 Claude Code.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: неофициальный фанатский мод по Avengers для Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Он говорит: мод Claude Code, который по запросу зачитывает вслух ответы Claude…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Spank Claude when it messes up — a stress-relief mod for Claude Code: cartoon…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Моды Claude Code: небольшие плагины для интерактивных панелей, маршрутизации…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Мод и плагин Claude Code: монитор использования, отслеживание токенов и…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Claude Code-мод, передающий небольшие решения дешёвой модели принятия решений…
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [a-pavithraa/claude-mods](https://github.com/a-pavithraa/claude-mods)
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Отслеживайте отклонение мыслей вашей сессии Claude Code прямо над запросом.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code-моды от afterever (маркетплейс плагинов).
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Маркетплейс модификаций для Claude Code: agent-board, auto-model…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code-моды: карточки статистики сессии над запросом.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анимированный кот из шрифта Брайля над приглашением Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Мод Claude Code: направляет недорогие задачи в GLM/Kimi через дочерний Claude…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Пиксельный кот над запросом Claude Code, который запускает тестовый звонок…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, который выбирает подходящий момент для компактизации, чтобы…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модификации Claude для Claude Code: token-meter.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code mod: your plan.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Моды общего назначения для Claude Code: полосы, панели, уведомления и хуки.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Ваши лимиты использования Claude в виде анимированной карточки здоровья жителя…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code-моды для команды S2 (маркетплейс ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткие тренировки, пока Claude работает: ежедневная цель, серии, значки и…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Доска использования для Claude Code: расходы по моделям.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Мод Claude Code, показывающий обратный отсчёт кэша приглашений в нижнем…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Мод Now Playing для Claude Code: Apple Music и Spotify над приглашением, с…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Claude Code-моды для сессий оркестратора и исполнителя.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Моды для Claude Code: часы кэша, радиус поражения, предложения, рабочий список…
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Моды для Claude Code: Clean View скрывает вызовы инструментов и показывает план…
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - Модификация Claude Code: журнал скоординированной работы с запусками, рабочими…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Модификации Claude Code: Suggestion Spotlight показывает, к чему относится…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашего Claude Code.
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Созданные мной моды для Claude Code (панели, команды и хуки).
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Оригинальный движок Doom с Freedoom, доступный внутри Claude Code.
- [cigarette1991/clawd-pet](https://github.com/cigarette1991/clawd-pet) - Clawd — Claude Code-мод, расположенный над полем запроса.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Просматривайте каждый файл, которого касается Claude, как pull request, не…
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Claude Code mod: a band above the prompt with the prompt-cache countdown, cache…
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Эксклюзивные Claude Code-моды для команды d3nim.
- [dankelleher/claude-mod-pin-message](https://github.com/dankelleher/claude-mod-pin-message) - Мод Claude Code: закрепление ответа над приглашением с возможностью свернуть…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Одиннадцать модов Claude Code (плагины с хуками функций) для домашнего рабочего…
- [davidcoulson/punch-list](https://github.com/davidcoulson/punch-list) - Мод для Claude Code, который ведёт единый список задач, ожидающих ваших…
- [davidcoulson/session-crew](https://github.com/davidcoulson/session-crew) - Мод для Claude Code, который показывает побочные сеансы, запускаемые настольным…
- [daviddecorso/claude-mods](https://github.com/daviddecorso/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Тамагочи, живущий внутри Claude Code: он вылупляется, ест код, который пишет…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Закладки и метки в стиле vim внутри терминальных бесед Claude Code: выделяйте…
- [devsomelife/somelife-claude-mods](https://github.com/devsomelife/somelife-claude-mods)
- [dgsantana/claude-mods](https://github.com/dgsantana/claude-mods) - Claude Code mods: omp-port.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Модификация Code для Claude: полоса над промптом с новостями Claude и срочными…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - A Claude Code mod: a board of your other sessions above the prompt — who waits…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Мод для Claude Code: после того как guard блокирует вызов инструмента…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Мод для Claude Code: фоновые задания в одном представлении с прогрессом и…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Мод для Claude Code: единый входящий ящик для сообщений от товарищей по…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Мод для Claude Code: объясняет блокировки песочницы и превращает повторные…
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Инструкции, навыки, расширения Pi и Claude Code-моды для Pi, Codex и Claude Code.
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Моды для Claude Code (плагины с перехватчиками функций): session-meter и другие.
- [g761007/hudcade](https://github.com/g761007/hudcade) - Пиксельный HUD для Claude Code: контекст, стоимость, кэш, агенты и ограничения…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Семь Claude Code-модов: savvy-progress, skins, filetree, cache-tax…
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Маркетплейс плагинов Claude Code с моими модами.
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Полезные моды для claude code.
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Частный маркетплейс модов для Claude Code.
- [hashswingingslasher/model-hint](https://github.com/hashswingingslasher/model-hint) - Мод для Claude Code: в реальном времени предлагает хайку, сонет или опус для…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Немецкоязычные моды для Claude Code: подсказки о контексте/кэше, открытые…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Claude Code-моды Hector Bailey (маркетплейс плагинов: hectorbailey).
- [hernandezsanti/claude-code-mods](https://github.com/hernandezsanti/claude-code-mods) - Claude Code-моды, принуждающие к коммитам на основе тикетов, защищающие…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Модификация Code для Claude: три следующих шага после каждого ответа на любом…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Модификация Claude Code: сколько времени занял каждый ответ, сколько времени…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Мод Claude Code: streamer-mode скрывает приватные панели, полосы и строку…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - для моих модов claude.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Пульт управления над полем запроса Claude Code. Утка считывает показания.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Обратимая редакция данных для Claude Code: приватные значения заменяются…
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Строка состояния Claude.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Небольшие Claude Code-моды: индикаторы использования контекста и плана…
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Claude Code-моды: панель контекста и HUD кибердека.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Автоматически читает ваши инженерные чертежи, а затем создаёт модель в…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Место для хранения моих модов claude.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Боковая панель с использованием контекста: общий объём, категории, рост за…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Боковая панель со списком файлов: какие файлы были созданы, изменены или…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пушистик в стиле 8-bit (чёрно-белый вислоухий голландский кролик) бегает и…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Боковая панель «Что я спрашивал»: каждое сообщение владельца в этом разговоре;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Боковая панель с временной шкалой: на что ушло время в этом раунде — ожидание…
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Боковая панель обмена токенами: сколько токенов основной разговор отправляет…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Честный пакетик с бобами для claude code: после каждого раунда Claude тихо…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Контрольный список плана для Claude Code с проверкой доказательствами…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI — упрощённая китайская локализация.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Неофициальное руководство сообщества по Claude Code-модам (функциональные хуки)…
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - Два Claude Code-мода: передача сессий с ответами и перенаправление простых…
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живет в полосе над вашим prompt Claude Code: разыгрывает сессию…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод, озвучивающий ответы и уведомления Claude Code с помощью VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Модификация Claude, позволяющая читать и объединять разговоры между вашими…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Моды Claude Code. PixBar: пиксельное существо над вашим запросом, которое…
- [Kiko-42/claude-code-hist](https://github.com/Kiko-42/claude-code-hist) - Мод для Claude Code: /hist выводит ваши прошлые запросы и перемещает…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code mod: every Claude Code session in one floating window, with live…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - моды claude.
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - Несколько доказательств концепции для claude-code-mods.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Модификации Claude Code, опубликованные как маркетплейс.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: интерактивный граф того, что знает Claude Code.
- [KunalKumarkkr01/prompt-rewriter](https://github.com/KunalKumarkkr01/prompt-rewriter) - Мод для Claude Code: /rewrite &lt;prompt&gt; выбирает ролевые и задачные персоны…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Моды Claude Code от Sanmu — маркетплейс плагинов (боковая панель задач).
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Подготовленное сообществом руководство по модам Claude Code: варианты…
- [lucaslenglet/session-namer](https://github.com/lucaslenglet/session-namer) - Claude Code mod: AI-suggested session names following your naming convention.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод Claude Code, который показывает, что делает Claude, в подзаголовке вкладки…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy — неофициальный созданный фанатами пиксельный компаньон, который…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - Насколько заполнен контекст Claude, когда его кэш остывает и сколько осталось…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Пушистая чёрная кошка над вашим промптом Claude Code.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Мод Claude Code: отвечайте на Claude построчно прямо в тексте.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Небольшие модификации для Code для Claude: runner-avatar — небольшой аватар…
- [mashiro-works/claude-mods](https://github.com/mashiro-works/claude-mods)
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - Небольшие моды Claude Code с канала MateAI.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Мод Claude Code: панель в реальном времени с тем, к чему стремится ваш AI-агент…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Модификация Claude Code: панель /sessions для просмотра и удаления сессий…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Моды сообщества для Claude Code: защиты, панели и команды, выполняемые внутри…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Боковая панель для Claude Code: файлы, записанные Claude, разделённые…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Мод Claude Code: по вашей недавней скорости использования прогнозирует, что…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Тихая боковая панель для Claude Code: чем занята эта сессия, её план, агенты и…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Тусклое время над каждым приглашением и каждым ответом в транскрипте Claude…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - Плагины Claude Code для сессий и памяти: мод панели Memory и навык…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, включающий обратно инструменты todo для моделей, которые их не…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Мод для Claude Code, который ждёт безопасной паузы, а затем передаёт вашу…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одной строке на каждую задачу над запросом — текущая…
- [mwmrs/claude-mods](https://github.com/mwmrs/claude-mods)
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Играйте в Connect Four против AI внутри Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Мод Claude Code: когда другой агент программирования делает коммит в ваш…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Мод для Claude Code: поддерживает лёгкость сеансов — строка использования…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Мод Claude Code для репозиториев, которыми пользуются несколько ИИ-агентов: не…
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Весёлые бесплатные моды для Claude Code, которые никогда не тратят токены.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Повторно запускает длительные наблюдения Monitor в Claude Code после их…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Защитный механизм для SQL в Claude Code: запрашивает подтверждение перед тем…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Один мод для Claude Code и Windows, с приоритетом CJK: предварительный просмотр…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Моды Claude Code: миниатюры изображений и строка состояния.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Лучшие моды Claude Code, отсортированные по пользе для вас.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Два мода Claude для Claude Code: garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Временные метки для Claude Code: время каждого сообщения, ответа и вызова…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Отслеживание изменений для Claude Code: точно покажите, что Claude изменил в…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Моды для Claude Code: плагины функциональных хуков, работающие в любом…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Различные моды и навыки для моей конфигурации Claude Desktop.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Модификация Claude Code: отслеживает модель, токены, инструменты и время…
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Модификация Claude Code: каждый субагент представлен маленьким человечком в…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Моды для Claude Code: safety-guard блокирует разрушительные команды и доступ к…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Анимированный пиксельный краб Claude для Claude Code: он изображает действия…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Моды Claude Code, опубликованные как единый marketplace плагинов.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Мод Claude Code: отжимания, которые нужно делать, пока работает Claude.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 корейских версий модов для Claude Code: запись предположений, простой язык…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - просто список используемых мной модов.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Три модификации Claude Code без зависимостей: адаптивная строка состояния…
- [Ron-Nefyodov/security-poc-mod](https://github.com/Ron-Nefyodov/security-poc-mod) - POC-only Claude Code mod for explicit, scoped local security demonstrations.
- [RuahTechSolutions/code-buddy](https://github.com/RuahTechSolutions/code-buddy) - Claude Code mod: staging guard, blast radius, edit replay and an agents panel…
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - Мои моды для Claude Code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Мод Claude Code: превращает план, который вы утверждаете в plan mode, в живой…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Подборка Claude Code-модов. Каждый элемент клонирован и проверен с помощью…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Бесплатный режим: вспомогательные агенты работают на Haiku, а большие файлы и…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музыка в стиле lofi, сопровождающая сессию: спокойствие, концентрация, поток, а…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Учитесь, пока Claude пишет код: после хода, изменившего код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запись каждого изменения, которое вносит Claude: воспроизводите каждое…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Моды Claude Code: token-bar, окно контекста и лимиты использования над промптом.
- [shaharz/pr-watch](https://github.com/shaharz/pr-watch) - Мод для Claude Code: отслеживает проверки PR и комментарии к ревью.
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Центр управления Claude Code: флот субагентов в реальном времени, использование…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Моды Showrin для Claude Code, помогающие сделать повседневную работу…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Персональные моды Claude Code.
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Мод для Claude Code: измеритель контекстного окна для каждого сеанса, с…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Моды Claude Code (function hooks): панель агентов, индикатор бюджета, флот…
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Не позволяйте вспомогательным агентам (субагентам) Claude расходовать ваши…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Commit messages в один клик для Claude Code с танцующей pixel-art Malenia.
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - Коллекция самостоятельно созданных модов Claude Code (marketplace плагинов).
- [sunwu51/english-assistant](https://github.com/sunwu51/english-assistant) - Claude Code Mods plugin for contextual Chinese-English translation, spelling…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Локальное хранилище модов Claude Code.
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Мод Claude Code: показывает ваш файл Cursor / VS Code и выделение над промптом…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — мод Claude Code, показывающий использование вашего плана Claude…
- [texxmexx/claude-usage-bar](https://github.com/texxmexx/claude-usage-bar) - Мод для Claude Code: полоса использования над текстовым полем.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, отображающий текущую сессию на панели: каждое приглашение…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Plugin marketplace модов Claude Code: function-hooks plugins, которые рисуют…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Мод Claude Code: переписывает черновой промпт на месте, называя подходящие…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Моды Claude Code от Toptaab.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Мод для Claude Code, который проверяет английский язык вашего запроса во время…
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Небольшие, забавные и полезные моды для Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анимированная полоса прогресса и сводка по завершении для…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Три небольших мода Claude Code: узнайте, когда завершат работу ваши субагенты…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажите «Я потерялся», и Claude снова объяснит свой последний ответ простыми…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Задайте Claude дополнительный вопрос на панели рядом с вашей работой.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code отправляет вам сообщения в Telegram, когда задача выполнена или…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Мои моды для Claude Code.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Мод Claude Code: маркер для ответов, боковая панель для результатов запросов в…
- [wendyyyanto/usage-meter-mod](https://github.com/wendyyyanto/usage-meter-mod) - Мод для Claude Code, который показывает ограничения использования, контекст…
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter) - This Claude Code mod shows a card above the prompt.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Мод для Claude Code: скрытые секреты, задачи, проверки и CI, дневник, diff…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Плагин Claude Code: лимиты использования Claude Pro/Max с прогнозом темпа…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моды для Claude Code. agent-crew: наблюдайте за работой субагентов как за живой…
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - Моды боковой панели терминала для Claude Code — трассировка агентов, работающий…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Интерактивная доска задач для Claude Code: планируйте перед началом работы…
- [Young-in/pinboard](https://github.com/Young-in/pinboard) - Claude Code mod: pin tables, artifact links and answers from the conversation…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Отобранная вручную коллекция лучших ресурсов для самых потрясающих агентов…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Плагин Claude Code, показывающий, что происходит: использование контекста…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Красивая, полностью настраиваемая строка состояния для Claude Code CLI с…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Все части системного промпта Claude Code, 27 встроенных описаний инструментов…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Более 45 советов по максимально эффективному использованию Claude Code — от…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — создание каруселей Xiaohongshu и пар обложек…
- [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) - A terminal window manager that knows what your agents are doing.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Красивый powerline в стиле vim для Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Просматривайте diff вашего агента кодирования в панели терминала и отправляйте…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Комплексный плагин статусной строки для Claude Code с использованием контекста…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Создавайте моды для Claude Code: перехватывайте любой запрос, изменяйте любой…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Комплексная панель statusline для Claude Code — информация о сессии, шкалы…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: отслеживайте углеродный след своих сессий Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Эстетичная statusline для Claude Code от awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Общедоступные Skills и моды для Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, моды, субагенты, хуки, slash-команды и руководства для Claude Code…
- [ChanMeng666/echook](https://github.com/ChanMeng666/echook) - 【Every star you give feeds a hungry developer.
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Законно бесплатные LLM APIs и агенты программирования — самообновление…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Быстрый калькулятор стоимости без зависимостей и настраиваемая строка состояния…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Строка состояния терминала для сессий Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Онлайн-счета футбольных матчей, расписание и турнирные таблицы для…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, превращающий вашего агента программирования в эксперта по…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Время молитв, дата по хиджре, азкары, ежедневный аят, пост по сунне, Рамадан…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Личная конфигурация Claude Code, версионируемая внутри ~/.claude — агенты…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — плагин DeepSeek Harness для исследовательских тем…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Набор плагинов для Claude Code, pi и DeepSeek Harness: HUD в строке состояния…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Портативный набор инструментов Claude Code для .NET DDD/Clean Architecture…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Лёгкая строка состояния Claude Code — один Bash-скрипт примерно на 170 строк…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагины Claude Code, которые я использую каждый день: навыки и моды…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Неофициальные моды для вкладки Code в Claude Desktop — usage-pet: полоса…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Мост DSH &lt;-&gt; Feishu (Lark), разработанный самостоятельно (не форк): потоковая…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Маркетплейс плагинов и навыков Claude Code для создания модов игры Hytale.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Управление токенами для Claude Code: лучшая модель направляет работу, а…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Просмотрщик с разделённой панелью для Claude Code в Windows Terminal и tmux…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Репозиторий модов Awesome Media для Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Сократите расходы на Claude Code и токены Codex: направляет запросы и тестовые…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Настраиваемая строка состояния Claude Code для Linux, WSL, Windows и macOS с…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Отображение строки состояния Claude Code с ограничениями частоты запросов…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Строка состояния и строка токенов для Claude Code: контекст, использование за 5…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - the friendly, fiddle-with-everything status line for Claude Code — truecolor…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Нативные команды агентов. Под контролем.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Дополнения Claude Code: наблюдатель цветных точек статуса вкладок + встроенная…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Определяемые программные фабрики для Claude Code на herdr: графы станций…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Строка состояния использования Claude Code для macOS и Linux, упакованная как…
- [CosminBd/claude-git-file-tree](https://github.com/CosminBd/claude-git-file-tree) - A git pane for Claude Code: review what Claude changed, read diffs and rendered…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Строка состояния Claude Code в Lua с интерактивной площадкой Neovim в реальном…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Профессиональная строка состояния Claude Code: длительность сессии, стоимость в…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Строка состояния Claude Code с учётом подписки.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Строка состояния Claude Code на испанском языке: задача, навыки, контекст со…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Красочная строка состояния Claude Code: лимиты плана, контекст, стоимость и…
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Строка состояния Claude Code для Windows: общее количество токенов, стоимость…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Однострочная строка состояния для Claude Code: модель, git, контекст, токены…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Предпросмотр изображений внутри Claude Code: наведите курсор на чип под…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Personal Claude Code configuration: permissions, statusline, MCP servers.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Строка состояния Claude Code со строками панели агентов.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Синхронизируйте задачи Claude с Fizzy.do, чтобы команда видела изменения в…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: переносимая настройка Claude Code — глобальные правила…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Отображает подробную цветовую панель состояния для Claude Code с информацией о…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Отслеживайте состояние Claude Code с помощью компактной панели, показывающей…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Two-line status bar for a terminal coding agent: directory, git, PR, model…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Хук строки состояния Claude Code — отслеживает использование токенов и контекст…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, пиксель-арт-компаньон Claude Code, и atelier, защитный механизм для…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Установщик окружения Claude Code: skills, statusline, hooks, permissions и…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness Claude Code от Nacho (правила, доска, моды).
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Многострочная строка состояния Claude Code: панель контекста, ветка git, полосы…
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - Плагины и моды OrihuelaConde для Claude Code.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — строка состояния Claude Code для macOS +…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Отслеживайте состояние Claude Code из строки меню macOS с индикаторами в…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Навыки и моды для Claude Code и Cowork — трекер проектов, справочный документ и…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Строка состояния Claude Code для Windows (PowerShell): индикаторы…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Навыки, моды, хуки и строка состояния для Claude Code, а также механизм…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Двухстрочная строка состояния для Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Настраиваемая строка состояния Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Конфигурация и моды Claude Code с общим набором компонентов, песочницей и…
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Стартовый каркас для Claude Code: хуки, строка состояния, локальные модели…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Портативная конфигурация Claude Code (строка состояния + установщик).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Небольшая панель для Claude Code: процент контекста, обратный отсчёт кэша…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Пользовательская строка состояния терминала для Claude Code: модель, каталог…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Отслеживайте использование контекста Claude Code, стоимость сеансов и сбросы…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Набор модификаций для Claude Code.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Строка состояния Claude Code: текущий идентификатор модели, имя хоста…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Навык Claude Code (VS Code, Windows): предварительный просмотр изображений и…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - 多机同步 Claude Code 用户级配置（settings.json + statusline），GitHub / Gitee 双源.
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Строка состояния Claude Code с градиентными индикаторами выполнения…
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
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74394 · TypeScript · 👁️ observed · 0 天</summary>

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
| Звёзды           | **74394**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐130074 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **130074** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100669 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **100669** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82332 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **82332**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35770 · Go · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **35770**  |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25513 · Python · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **25513**  |
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
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8654 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **8654**   |
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
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4565 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **4565**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4362 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **4362**   |
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
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3054 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **3054**   |
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
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1601 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Кроссплатформенное рабочее место агента с открытым исходным кодом

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1601**   |
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
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1599 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Защита перед выполнением для AI-агентов программирования. Она блокирует деструктивные команды Git и файловой системы, а также распространённые попытки доступа к конфиденциальным файлам до запуска вызова инструмента. Поддерживаются Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode и Pi.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1599**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hyhmrright/brooks-lint">hyhmrright/brooks-lint</a></b> · ⭐1514 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

AI code reviews grounded in 12 classic engineering books — decay risk diagnostics with book citations, severity labels, and 6 analysis modes including full-sweep auto-fix

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | HTML                                                                   |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **1514**   |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `agent-skills` · `ai-code-review` · `architecture-review` · `auto-fix` · `claude-code` · `claude-code-plugin` · `clean-architecture` · `code-health`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hyhmrright--brooks-lint/1d89101c540d575a.gif" width="100%" alt="hyhmrright/brooks-lint screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hyhmrright--brooks-lint/1d89101c540d575a.gif" width="100%" alt="hyhmrright/brooks-lint animation"><br><sub>анимированная запись</sub></td>
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
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐372 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **372**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐230 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **230**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐181 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **181**    |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐176 · Python · 🔎 inferred · 0 天</summary>

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
| Звёзды           | **176**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/yyh-001/dsh-meme">yyh-001/dsh-meme</a></b> · ⭐173 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness 表情包插件：输入框一键发图、文字 token 斗图、情绪主动发图、AI 自动学图，图库市场一键安装。 · Meme/sticker plugin for DeepSeek Harness: one-click picker in the composer, text-token memes, mood-driven sending, AI learns your images, marketplace packs.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **173**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `deepseek-harness` · `dsh-plugin` · `meme` · `qq-bot` · `selfloom` · `semantic-search`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/yyh-001--dsh-meme/fb2c32b0de04c6c7.jpg" width="100%" alt="yyh-001/dsh-meme screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

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
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐121 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

DeepSeek Harness 桌宠插件：元气鲸鱼娘看板娘陪你写代码 🐋 支持 DSH 桌面端 0.2.0-rc.2 与旧版 Web（desktop pet / mascot，local-first）

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **121**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Tabbit-Browser/dsh-tabbit">Tabbit-Browser/dsh-tabbit</a></b> · ⭐107 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Tabbit Browser plugins for Deepseek Harness

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **107**    |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `awesome-dsh-plugin` · `browser-automation` · `browser-use` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `dsh-plugin-market`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tabbit-browser--dsh-tabbit/5236e4418ecd9821.png" width="100%" alt="Tabbit-Browser/dsh-tabbit screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/webkubor/dsh-bloom-theme">webkubor/dsh-bloom-theme</a></b> · ⭐59 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин темы DeepSeek Harness (DSH): Bloom — 10 китайских наименований палитр в стиле Мора́нди (黛蓝/朱砂/桃夭/天青/竹青/赭石/青金/琥珀/落霞/青莲), настройка цветов OKLCH, светлая и тёмная темы, переключение верхней панели одним нажатием; все 20 наборов палитр на практике соответствуют WCAG AA

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
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Извлечение контекста рабочего пространства с учётом задачи и отслеживание жизненного цикла для AI coding agents: поиск, организация и постоянное отслеживание наиболее релевантных задаче документов, кода и медиа. Полностью локально, без вызовов моделей и без сети. Извлечение контекста рабочего пространства с учётом задачи и отслеживание жизненного цикла для AI coding agents. Поиск, организация и отслеживание наиболее релевантного текущей задаче контекста рабочего пространства — локально, детерминированно, без вызовов моделей и без сети.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | JavaScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **54**     |
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
<summary>🧵 <b><a href="https://github.com/Tkingxiao/dsh-any-background">Tkingxiao/dsh-any-background</a></b> · ⭐43 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Deepseek Harness 自定义主题插件，支持自定义图片/视频壁纸，对话框，侧边栏等透明度模糊度调整，全局主题色的色轮调整插件

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **43**     |
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tkingxiao--dsh-any-background/3791f4d31d740ce0.png" width="100%" alt="Tkingxiao/dsh-any-background screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐37 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Альтернатива GrokBot с открытым исходным кодом на базе DeepSeek Harness. Создайте команду личных ботов: несколько персональных агентов с постоянной памятью, идентичностями и разрешениями, расширяемых через плагины DSH.｜Открытая альтернатива GrokBot на базе DeepSeek Harness: команда персональных AI-ботов с долговременной памятью, поддержкой совместной работы нескольких ботов, идентичностями, разрешениями и расширением через экосистему плагинов DSH.MIT.

##### 📌 Основные сведения

| Поле          | Значение                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Категория     | `Экосистемы плагинов DSH и Cordis`                                     |
| Подтверждение | `заявлен мод, плагин или хук, но ничего конкретно о поверхности модов` |
| Язык          | TypeScript                                                             |

##### 📊 Данные

| Метрика          | Значение   |
| ---------------- | ---------- |
| Звёзды           | **37**     |
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
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

Плагин DeepSeek Harness: сопоставление окна контекста модели в один клик, отображение источника ёмкости, массовая настройка с помощью флажков, управление существующими окнами и ручное редактирование.

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
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/YRN-playmaker/dsh-wallpaper_share">YRN-playmaker/dsh-wallpaper_share</a></b> · ⭐31 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Сводка

一键同步壁纸引擎各类动态场景壁纸的插件，设置应用启动项。A "wallpaper engine" synchronization plugin mounted on the deepseek harness can synchronize static wallpapers

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
| Последний push   | 2026-10-12 |
| Впервые в списке | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Изображение</th><th align="center" width="50%">🎬 Видео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/yrn-playmaker--dsh-wallpaper_share/6dee518b3fc3dad7.png" width="100%" alt="YRN-playmaker/dsh-wallpaper_share screenshot"></td>
<td align="center" valign="top"><sub>медиафайлы не опубликованы</sub></td>
</tr></table>

</details>

<details>
<summary><b>Больше в этой категории</b> <sub>· 69</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Отобранный список лучших отличных ИИ-плагинов для ИИ-ассистентов, включая…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Плагин DSH — бесплатные модели OpenCode Zen для DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Рынок плагинов DSH / DSH Plugin Marketplace: в веб-интерфейсе DeepSeek Harness…
- [arcships/rutis](https://github.com/arcships/rutis) - Среда выполнения плагинов для самоизменяющегося программного обеспечения…
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - 把 DSH Web 状态行换成 1063 条梗:打字机 + 炫彩渐变 + 弹幕 + 12 个主题词库包,设置页可视化编辑.
- [wqty123/dsh-browser](https://github.com/wqty123/dsh-browser) - Shared real browser plugin for DeepSeek Harness.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Избранный каталог плагинов DeepSeek Harness (DSH) — более 280 плагинов…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin: Git Bash shell for all agent modes on Windows.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [huaizhuanghub/dsh-persona-dafeiyu](https://github.com/huaizhuanghub/dsh-persona-dafeiyu) - Persona library plugin for DeepSeek Harness: built-in personas, import your…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Коллекция веб-плагинов GUI для DSH (DeepSeek Harness) — уведомления о задачах…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH 会话导航.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Плагины, инструменты, навыки и учебные материалы DeepSeek Harness (dsh)…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - Управление обновлениями основной программы DeepSeek Harness и плагинов…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Среда выполнения для коммерческих переговоров A2A + плагин DeepSeek Harness…
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Панель инструментов для DeepSeek Harness Web: менеджер MCP.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Настоящий PowerPoint, а не HTML. Расскажите ИИ, что нужно осветить, и pptwise…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Локальный граф знаний кода и среда контекста для агентов программирования.
- [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution plugin for DeepSeek Harness: versioned, auditable…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - AI argues. Code settles. The losses stay on the page.
- [webkubor/dsh-llm-hub](https://github.com/webkubor/dsh-llm-hub) - 给 DSH 模型页补上官方适配器缺的那半：网关可达性探测、模型目录拉取并勾选写回、余额/配额常驻、协议与接入地址可见。零运行时依赖，不改动 DSH 安装.
- [webkubor/dsh-env-inspector](https://github.com/webkubor/dsh-env-inspector) - DSH 环境自检：让读者看到自己电脑装了什么 —— 系统/CLI/DSH 插件/秘钥是否存在.
- [webkubor/dsh-mirror](https://github.com/webkubor/dsh-mirror) - Let the AI know you. 让模型主动记下你的判断依据（原则/红线/工作方式），跨会话复用 —— 有容量、会遗忘、每条都说得出为什么记.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [huangziyuan-general/dsh-novel-forge](https://github.com/huangziyuan-general/dsh-novel-forge) - DSH 小说锻炉：把 AI 长篇写作通病变成代码强制的硬约束（事实账本/上下文包/阶段门禁/零费用去AI味扫描/确定性审计/提案制修订）.
- [Lenonss/DSH_VsCodeMode](https://github.com/Lenonss/DSH_VsCodeMode) - VSCode-style coding for DeepSeek Harness: Monaco editor (tabs/QuickOpen), agent…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Превратите модели, уже авторизованные в настольном приложении WorkBuddy на этом…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - Плагин DSH: три инструмента, созданные на основе официального API открытой…
- [sueccku/dsh-plugin-wps-office-next](https://github.com/sueccku/dsh-plugin-wps-office-next) - 在 DeepSeek Harness（DSH）里用中文对话操作 WPS 表格 / 文字 / 演示：读写数据、排版、公式图表、批量转 PDF.
- [evoelsewhere/evoflux](https://github.com/evoelsewhere/evoflux) - Evoflux is an open-source, local-first workspace where AI agents build…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - плагин dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Постоянное тестирование совместимости плагинов DeepSeek Harness: точные версии…
- [drscrewdriver/dsh-thinking-levels](https://github.com/drscrewdriver/dsh-thinking-levels) - deepseek-harness dsh thinging levels 调整 reasoning强度调整.
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - Repair DeepSeek Harness sessions that refuse to load. 修好打不开的 DSH 会话文件.
- [losebird/dsh-plugin-market](https://github.com/losebird/dsh-plugin-market) - DeepSeek Harness plugins market｜DSH 插件市场.
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - A curated list of plugins, tools, skins, and extensions for DeepSeek Harness…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Хост-плагин DeepSeek Harness, который хранит документы проектов и…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray для плагинов DeepSeek Harness: заявленные возможности против фактического…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Рабочее пространство с несколькими папками: позволяет агенту DSH.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - Плагин DSH: подключает модели из настольного приложения WorkBuddy к DeepSeek…
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Podman-backed execution for DeepSeek Harness (dsh).
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Глубокие ссылки на сеансы + полный экспорт сеанса (markdown/JSON) + одобренный…
- [yh4922/dsh-workspace](https://github.com/yh4922/dsh-workspace) - A remote workspace plugin for DeepSeek Harness (DSH).
- [JessenReinhart/dsh-tokenslash](https://github.com/JessenReinhart/dsh-tokenslash)
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Плагин DSH: окно инструментов Git уровня IDE в виде нативной вкладки…
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - The DeepSeek Harness Personalization Settings plugin is used to configure the…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [laoduu/DeepSeek-Harness-yizi-themes](https://github.com/laoduu/DeepSeek-Harness-yizi-themes) - 19 тщательно отобранных стильных тем для Web UI DeepSeek Harness（dsh）…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт проверки плагинов DeepSeek Harness (dsh) без зависимостей…
- [SuCriss/dsh-leekbox](https://github.com/SuCriss/dsh-leekbox) - 韭菜盒子 LeekBox — помощник для просмотра котировок акций A股 · веб-плагин DeepSeek…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode в DeepSeek Harness — плагин DSH, поддерживающий работу OpenCode Zen и…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонний маркетплейс плагинов и защищённый менеджер жизненного…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx 是一款以人为本的可拓展桌面工作台：对话、笔记、表格、文件在同一工作台；自建服务端即可开启多人实时协作.
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Запускайте DeepSeek Harness на настольном компьютере без затрат токенов…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Полностью оснащённый агент программирования для DeepSeek Harness — рабочие…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - Плагин DSH: показывает баланс вашего аккаунта DeepSeek в нижней части левой…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Bots workbench: Cordis plugin bridging the sdk-bots orchestration gateway…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — набор инструментов для локального развёртывания и эксплуатации…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Веб-плагин DeepSeek Harness (DSH): вкладка боковой панели market-dashboard для…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Independent third-party plugins and tools for DeepSeek Harness, maintained by…
- [Wenston-dev/awesome-dsh-plugin](https://github.com/Wenston-dev/awesome-dsh-plugin) - Awesome dsh plugin list — automated DeepSeek Harness plugin directory.
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Use OpenCode Zen free models in DeepSeek Harness with anonymous access or an…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Плагин DeepSeek Harness: превращает сбой выделения ACL песочницы Windows…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Оценка прогресса для автономных раундов целей dsh: откладывает цикл, пока…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - Плагин dsh: превращает остановку из-за усечения длины в восстановление после…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Плагины, которые убирают за собой: порт фреймворка плагинов cordis для iOS и…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Среда выполнения плагинов Rust с проверенным Verus ядром жизненного цикла и…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Arkme account, records, chat and interwoven-moments integration for DeepSeek…

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

| Язык       | Записей | Примеры                                                                                                       |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 395     | `anthropics/claude-code`, `anthropics/claude-code-action`, `AlekDob/blockodile-claude-mod`                    |
| JavaScript | 84      | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 39      | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 27      | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12      | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 5       | `Gaurav-Gosain/tuios`, `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`                              |
| Rust       | 4       | `persiyanov/herdr-reviewr`, `arcships/rutis`, `Atelyx/Atelyx`                                                 |
| PowerShell | 2       | `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win`                                   |
| Swift      | 2       | `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`                                       |
| C          | 1       | `reporails/arcade`                                                                                            |
| C#         | 1       | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1       | `sorsama/deepseek-harness-mobile`                                                                             |
| Lua        | 1       | `crafts69guy/claude-statusline.nvim`                                                                          |
| MDX        | 1       | `jkf87/mod-guide`                                                                                             |

<sub>Учитываются только записи, в которых указан язык. Документация и обсуждения исключены из этой таблицы.</sub>

## Участие

Исправления приветствуются и являются самым быстрым способом улучшить этот список. Откройте issue или pull request, если запись попала не в тот раздел, получила неверную оценку или если проект был ошибочно исключен как совпадение имени — именно в этой последней категории автоматические фильтры чаще всего ошибаются.

---

<sub>Независимый проект сообщества. Не аффилирован с Anthropic, не одобрен и не проверен им. Claude Code, Claude и Anthropic являются товарными знаками Anthropic. Поведение продукта может меняться без уведомления; всё критически важное проверяйте по официальной документации. Материалы остаются собственностью исходных проектов и воспроизводятся только там, где это разрешено лицензией.</sub>

<sub>Последнее обновление · 2026-10-12T19:16:21+08:00</sub>
