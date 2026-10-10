<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Круті моди для Claude">
</p>

<h1 align="center">Круті моди для Claude</h1>

<p align="center"><b>Індекс модів і плагінів для Claude Code, оцінених за доказовістю, а також глибших змін у поведінці, які вони вносять.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-617-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <b>Українська</b></sub></p>

> [!NOTE]
> **Актуальний індекс** · Остання синхронізація: `2026-10-11T05:58:46+08:00` (UTC+8)
> · Записи: **617** · Додано під час останнього оновлення: **0** · Мови реалізації: **10**

<sub>Кожен наведений нижче запис було автоматично зібрано, відфільтровано та повторно перевірено. Тут немає платних розміщень.</sub>

<a id="featured"></a>

## Актуальна добірка

<sub>По одному запису на категорію, упорядкованому за рівнем доказовості та кількістю зірок; рейтинг перераховується під час кожного оновлення. Це рейтинг, а не рекомендація; кожна добірка веде до повної картки нижче. Перевагу надано проєктам, які опублікували знімок екрана або запис, щоб добірка залишалася візуальною.</sub>

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
<sub>🌊 Оригінальний агентний рушій. Розгортайте інтелектуальні багатокористувацькі рої, координуйте автономні робочі процеси та створюйте розмовні системи ШІ. Серед…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Зміст

- [Що таке мод для Claude Code](#що-таке-мод-для-claude-code)
- [Як оцінюються записи](#як-оцінюються-записи)
- [Офіційні: власні репозиторії та примітки до випусків Anthropic](#офіційні-власні-репозиторії-та-примітки-до-випусків-anthropic) — **16**
- [Моди: створені за допомогою можливості модифікації](#моди-створені-за-допомогою-можливості-модифікації) — **493**
- [Екосистеми плагінів DSH і Cordis](#екосистеми-плагінів-dsh-і-cordis) — **97**
- [Тексти, обговорення та відео](#тексти-обговорення-та-відео) — **11**
- [Проєкти за мовою реалізації](#проєкти-за-мовою-реалізації)

## Що таке мод для Claude Code

Claude Code отримав **моди** у версії 2.1.287: розширення, які можуть змінювати глибші аспекти поведінки, ніж плагіни, і промальовувати власний інтерфейс.

Мод може підключатися до `ui.render`, щоб відображати **рядок, смугу, панель або картку** навколо запиту, читати текст, який ви востаннє вибрали за допомогою `$.ui.selection()`, створювати колег за допомогою `agent.spawn` і володіти областю `Client`. Якщо мод не може відобразити інтерфейс, він виходить з ладу сам — `ui.fault` не дає одному зламаному моду зупинити сесію.

Цей список охоплює моди, поверхню плагінів і хуків, на які вони спираються, а також відповідники для DSH і Cordis. Він навмисно **не** охоплює ширшу екосистему Claude Code: набір запитів — це не мод.

## Як оцінюються записи

Більшість списків у цій сфері просто заявляють про включення. Цей показує, що саме було перевірено, а потім дає змогу відповідно фільтрувати записи. Оцінка описує докази, а не якість проєкту — добре створений мод, про який ще ніхто не написав, усе одно має статус `inferred`.

| Оцінка                                                                          | Що це означає                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `опубліковано безпосередньо Anthropic`                                          | Опубліковано безпосередньо Anthropic або прочитано безпосередньо в офіційному журналі змін.                                                                                                                      |
| `у власному тексті згадується мод API або заявлено підтримку модифікацій`       | У власному тексті згадується частина поверхні модифікацій — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, панель, смуга або картка, — тож автор описує щось, створене для роботи зі справжнім API. |
| `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` | Називає себе модом, плагіном або хуком, але в тексті нічого конкретного про поверхню модифікацій не згадується. Справжній, але непідтверджений.                                                                  |
| `збіг лише за термінологією`                                                    | Збіг лише за термінологією. Додано, щоб фільтр можна було перевірити, а не тому, що цьому запису довіряють.                                                                                                      |

<a id="official"></a>

## Офіційні: власні репозиторії та примітки до випусків Anthropic

Anthropic's own Claude Code repositories, and the releases that defined the mod surface. Read from the source rather than summarised.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150059 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Опис

Claude Code — це агентний інструмент для програмування, що працює в терміналі, розуміє вашу кодову базу й допомагає програмувати швидше, виконуючи рутинні завдання, пояснюючи складний код і керуючи робочими процесами git — усе за допомогою команд природною мовою.

<sub>🔧 Знайдено використання в коді: `feed.xml`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | TypeScript                                                       |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **150059** |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9466 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | TypeScript                                                       |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **9466**   |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8244 · Python · ✅ official · 1 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | Python                                                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **8244**   |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6335 · Python · ✅ official · 241 天</summary>

##### 📝 Опис

Дія GitHub для перевірки безпеки на основі ШІ, яка використовує Claude для аналізу змін у коді на наявність вразливостей безпеки.

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | Python                                                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **6335**   |
| Останній push           | 2026-02-11 |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 1 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | Shell                                                            |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1799**   |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Опис

Додаткові матеріали для Claude Model Cards

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **25**     |
| Останній push           | 2025-12-05 |
| Вперше додано до списку | 2026-10-05 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Опис

Додано модифікації Claude: плагіни тепер можуть змінювати глибшу поведінку. Додано You should know — вбудовану модифікацію, у якій бічний агент стежить за вами та позначає те, що ви або Claude можете не помітити. Увімкніть її за допомогою `/plugin enable cc-plugin-you-should-know@builtin` (для сеансів першої сторони з увімкненою телеметрією)

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Опис

Додано `$.ui.selection()` для модифікацій: повертає текст, який ви востаннє вибрали в повноекранному режимі, а коли вибране міститься в одному рядку транскрипту — цей рядок. Виправлено помилку, через яку кнопка модифікації іноді виконувала дію іншої кнопки під час натискання на поданні, намальованому до перезапуску Claude Code. Виправлено завершення повноекранних сеансів із помилкою «unrecoverable interface error» під час відкриття діалогу фонових завдань, коли плагін або модифікація відображали рядки над запитом. Виправлено помилкове віддалене повідомлення `claude plugin test` про вимкнення модифікацій, коли воно лише прочитало застаріле збережене налаштування

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Опис

Виправлено помилку, через яку правило deny або ask для вкладеної частини складної команди оболонки не зберігалося після схвалення модифікації, встановленої користувачем, на керованих машинах. Виправлено незавантаження встановлених модифікацій у першому сеансі після оновлення. Додано `agent.spawn` для команд, один ідентифікатор агента для подій хуків плагінів, а також стани бездіяльності й очікування в `$.agent.list()`. Виправлено завершення сеансів із помилкою «unrecoverable interface error», коли значення, записане хуком `ui.render` модифікації, спричиняло помилку під час відображення рядка; тепер рушій натомість відображає власний рядок. Виправлено відображення вирівняного праворуч вмісту в панелі або смузі модифікації під позначкою закриття або `\[-\]`, wh

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Опис

Додано `serverToolUses` до результату хука `turn.step` мода: інструмент викликає API, який сам виконався (радника), для кожного зазначено його ідентифікатор, назву, вхідні дані, початок і завершення. Додано `ceiling` до запитання та вердикту, які читає хук `tool.check` мода, із зазначенням схвалення, якого організація вимагає для інструмента. Додано типи `ThemeKey` і `Color` до типів хуків плагіна, щоб редактор перелічував кольори теми, які може назвати малювання мода. Додано до `claude plugin validate`: кожен хук, зареєстрований модом на сайті контролю доступу, перелічується із зазначенням, чи має він `.catch` (`gatingHooks` у `--json`). Виправлено результат `turn.step` мода

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Опис

Додано `prompt.autocomplete`, подію, до якої мод під’єднується, щоб додавати власні рядки до списку автодоповнення поля запиту Додано кешування запитів до `$.model.complete` для модів: `prompt` і `system` приймають блоки тексту, а `cache: true` на блоці кешує запит до нього Додано агентів робочого процесу до хука мода `agent.spawn`, з їхнім запуском та індексом, щоб мод міг відмовити їм Виправлено рядки Write, Edit, NotebookEdit і LSP, а також одиночні рядки Read, Grep і Glob, приховуючи, чому мод відхилив виклик: тепер рядок показує причину Виправлено хук мода `config.set`, `state.set`, `env.set` або `agent.spawn`, який відхиляє піс

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Опис

Додано `isDeferred` до `$.tool.register` для модифікацій: `false` від самого початку перелічує схему інструмента в запиті, а не ховає її за пошуком інструментів Виправлено пропуск хуків модифікації на подіях `classic.*`, поки перезапускається робочий процес хуків плагіна, через що хуки налаштувань відповідали без них Виправлено збій `claude plugin test` для модифікацій, які викликають `$.session.append`; тести можуть прочитати додані рядки назад за допомогою нового `mock.session`

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

MCP Консоль керування для офіційного клієнта DeepSeek Harness MCP: команда /mcp із діагностикою стану та пробними викликами конвеєра, вкладка Settings MCP із CRUD для серверів (запис із обов’язковим схваленням, автоматичні резервні копії) і консоль пробного запуску інструментів через офіційний конвеєр інструментів (Apache-2.0, dsh-plugin).

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic`                |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **74**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

це launcher для офіційного DeepSeek Harness. без модифікацій, він просто запускає те, що розробляє DeepSeek.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic`                |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **3**      |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary><b>Більше в цій категорії</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Додано `$.ui.notify` для модифікацій: створює нативне сповіщення через власне…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Виправлено завершення безголових сеансів, очищення введеного промпту або…

</details>

<a id="mods"></a>

## Моди: створені за допомогою можливості модифікації

Кожен запис тут містить докази використання можливості, яку Claude Code отримав у версії 2.1.287: він виводить дані через `ui.render`, має власну панель, смугу або картку, читає `$.ui.selection()`, запускає колег за допомогою `agent.spawn` або прямо називає себе модом.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2532 · Python · 👁️ observed · 0 天</summary>

##### 📝 Опис

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | Python                                                                    |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **2532**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>анімований запис</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐467 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Спільнотний каталог загальнодоступних модифікацій Claude Code (функціональних hooks), просканованих із GitHub, із зазначенням того, що кожна модифікація може читати, записувати, запускати або надсилати мережею. Переглянути https://mods.aidojo.si/

<sub>🔧 Знайдено використання в коді: `data/seeds.txt`, `data/duplicates.txt`, `data/repos.txt`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **467**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐181 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Опис

Моди Claude Code: плагіни, побудовані на hooks, що додають живі рядки над промптом, guards, panes та ігри. Панель контексту, лічильник використання, спостереження за review Codex, попередній перегляд Markdown, поточне відтворення Spotify та інше.

<sub>🔧 Знайдено використання в коді: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **181**    |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐115 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Опис

Підтримуйте кеш промпту Claude Code теплим під час перерв і показуйте орієнтовну вартість перед холодним надсиланням.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **115**    |
| Останній push           | 2026-10-04 |
| Вперше додано до списку | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>анімований запис · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Відкрити відео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐106 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Опис

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

<sub>🔧 Знайдено використання в коді: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | HTML                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **106**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Опис

An agent-native QA CLI for web pages. Deterministic, no tests to write, no LLM.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | HTML                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **104**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Скіни для Claude Code: рядки інструментів зі значками, картки дифів, таблиць і діаграм Mermaid, смуга використання та п’ятнадцять тем. /skin змінює їх у реальному часі.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **88**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Опис

Колекція модифікацій claude code

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **77**     |
| Останній push           | 2026-10-08 |
| Вперше додано до списку | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Colorful, themeable Claude Code replies: tables, code, diagrams, charts and tool rows in 15 themes, with copy buttons. A Claude Code mod.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **74**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Опис

Модифікації Claude Code від Darrell Wang — смуги над промптом, нуль токенів моделі. Панель тайванських／американських акцій + більше в майбутньому.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | HTML                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **65**     |
| Останній push           | 2026-10-05 |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐59 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Опис

Мод Claude Code, який додає до термінала живу панель агента: контекст і вартість, часову шкалу радника, кожну перевірку дозволів, картки субагентів і swimlane.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **59**     |
| Останній push           | 2026-10-02 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐57 · Shell · 👁️ observed · 3 天</summary>

##### 📝 Опис

Експертні навички, агенти, команди, правила, хуки та стилі виводу для Claude Code — безперервність сесій + сучасні інструменти CLI для реальних робочих процесів розробки

<sub>🔧 Знайдено використання в коді: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | Shell                                                                     |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **57**     |
| Останній push           | 2026-10-07 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐45 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Опис

Моди Claude Code: живі індикатори перебігу плану над підказкою

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **45**     |
| Останній push           | 2026-10-08 |
| Вперше додано до списку | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>анімований запис · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Відкрити відео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Опис

Спостерігайте, як Claude Code створює маленький мультфільм під час вашої роботи.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **32**     |
| Останній push           | 2026-10-02 |
| Вперше додано до списку | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Опис

Стрічка підказок вашої сесії Claude Code: наведіть курсор, щоб прочитати, клацніть, щоб перейти (функціональні хуки / Mods)

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **27**     |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

A glow-up for Claude Code: a live cockpit pane, shareable themes, and a pixel pet that acts out what Claude is doing

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **23**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Опис

Збірка, тести, консоль і попередній перегляд SwiftUI з Xcode усередині Claude Code

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **20**     |
| Останній push           | 2026-10-02 |
| Вперше додано до списку | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Опис

Моди Claude Code: 21 стиль і повний набір функцій, які можна вмикати за потреби, для термінала й настільного застосунку. · Одним натисканням змініть стиль Claude і отримайте повний набір функцій, які можна вмикати за потреби.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **20**     |
| Останній push           | 2026-10-04 |
| Вперше додано до списку | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Опис

Десять модів Claude Code, посібники для початківців, підказки для створення, безпечні демонстрації та шаблон для створення власних модів.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **20**     |
| Останній push           | 2026-10-02 |
| Вперше додано до списку | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Опис

Моди Claude Code: usage-band показує ваші ліміти 5h/7d, контекстне вікно та частоту влучань у кеш над prompt

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **12**     |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Опис

Моди Claude Code, які полегшують читання й відповіді на запитання Claude (qa-guide).

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **11**     |
| Останній push           | 2026-10-07 |
| Вперше додано до списку | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>анімований запис · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Відкрити відео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Опис

Мод для Claude Code: контекст у токенах, 5-годинні та тижневі ліміти порівняно з годинником, зворотний відлік кешу промпту, вартість сесії та активні агенти — все в одній смузі над промптом.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **11**     |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Опис

Десять модів із відкритим кодом для Claude Code: панелі в реальному часі, смуги, рядки стану та захист викликів інструментів. Лічильник згоряння, коди запуску, завершення сеансу, бій із босом, домашній улюбленець-кодер та багато іншого.

<sub>🔧 Знайдено використання в коді: `swarm/README.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **11**     |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Опис

Два моди Claude Code: міст Codex для керування комп’ютером і скоординовані сесії Claude. Вихідний код, промпти для збирання, налаштування та тести.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **11**     |
| Останній push           | 2026-10-05 |
| Вперше додано до списку | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Опис

Анімоване піксельне зображення над вашим prompt у Claude Code, яке реагує, поки працює Claude. Сім сцен або ваше власне зображення чи GIF. Нуль токенів.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **10**     |
| Останній push           | 2026-10-04 |
| Вперше додано до списку | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Опис

Інтерфейс навколо ваших терміналів Claude Code і Codex, який створюють ваші агенти, тож єдина модель у вашій голові — ваша.

<sub>🔧 Знайдено використання в коді: `CLAUDE.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **9**      |
| Останній push           | 2026-10-08 |
| Вперше додано до списку | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

KOZMOS — живі візуальні моди для Claude Code (CLI + настільний застосунок): панелі над запитом, бічні панелі, індикатор стану, компаньйони, захист і звук.

<sub>🔧 Знайдено використання в коді: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **9**      |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Опис

Шість модів Claude Code в одному плагіні (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) з перемикачами для кожного мода, плюс звіт mods-vs-hooks.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **8**      |
| Останній push           | 2026-10-04 |
| Вперше додано до списку | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 25 天</summary>

##### 📝 Опис

Трекери сеансів для Claude Code, створені як моди: вікно контексту, швидкість витрачання квоти плану, вартість кожного ходу

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **7**      |
| Останній push           | 2026-09-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Опис

Збірка модів Claude Code від 개발동생. Таксі-пакет: лічильник, навігатор, камера контролю швидкості, відеореєстратор

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **7**      |
| Останній push           | 2026-10-04 |
| Вперше додано до списку | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Переглянути на youtube.com</a> · відтворення відкривається на сайті-джерелі; GitHub не може вбудувати його безпосередньо</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Опис

Markdown, який відображається в полі запиту Claude Code під час введення. Код у fenced-блоці перетворюється на картку з підсвічуванням синтаксису ще до того, як ви закриєте блок.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **7**      |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Опис

Моди Claude Code: 像素螃蟹用量面板 usage-hud + HTML-посилання, клікабельні в терміналі, і картки коду з копіюванням одним кліком html-shelf

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **7**      |
| Останній push           | 2026-10-08 |
| Вперше додано до списку | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Моди для Claude Code: плагіни function-hook, що додають динамічні панелі та поведінку до інтерфейсу термінала

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **6**      |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Опис

Мод Claude Code (плагін), що додає бічну панель із вкладками Activity, Files, Agents, Context і MCP, рядок стану над prompt, оновлено стилізований чат, Mermaid діаграми в терміналі, таблиці, а також панелі коду й diff. Кольори відповідають і /color, і /theme (dark, light та іншим).

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **6**      |
| Останній push           | 2026-10-06 |
| Вперше додано до списку | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary><b>Більше в цій категорії</b> <sub>· 459</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Колекція зі 100+ модів, які можна використовувати з Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Модифікації Claude і інструменти для їх створення: спочатку навичка створення…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Середовище Claude Code, яке я використовую щодня, опубліковане під цією назвою…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Заміни дах для Claude Code за допомогою Claude Mods: не змінюючи бінарний файл…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Чотири моди Claude Code: Cache Keeper, Recording Mode, Goal Meter і Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Моди Claude Code від Learning Hacker: перетворюють роботу агента на зрозумілу…
- [kakha13/claude](https://github.com/kakha13/claude) - Моди Claude Code, які виправляють і перекладають ваші prompts перед тим, як…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Бічна панель для Claude Code: субагенти, яких запускає сеанс, що робить кожен…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Кабіна керування для Claude Code: динамічні індикатори плану, смуги підлеглих…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - База знань Obsidian із посиланнями на джерела про моди Claude Code: як вони…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Навичка, яка навчає агентів Claude Code створювати моди Claude.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Бічна панель Claude Desktop (вкладка Code): перелічує незавершені та поточні…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Моди й навички Claude Code від Nekyia Labs, створені та щодня використовувані…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (плагіни function-hooks) для Claude Code.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Смуга використання над полем введення Claude Desktop (вкладка Code): ліміти 5h…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Модифікації, плагіни та навички Claude від спільноти, які можна встановити з…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Галерея модифікацій Baselane: перевірені та закріплені модифікації Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Черга рішень CLI/TUI для людей, які працюють із розмовними агентами.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Мод панелі IDE для Claude Code: дошка агентів, дерево файлів і переглядач…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плаваюча картка стану для Claude Code — модель, контекст, обмеження швидкості…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Модифікації Claude Code: screen-guard приховує імена й секрети під час…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Розширення Claude Code. Розкрийте повну потужність Claude.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Панелі, захисні механізми та моди для зручності роботи в Claude Code: контекст…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Два моди Claude Code над полем запиту: індикатор вікна контексту, ліміт на 5…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Your plan, watching itself. Local desktop roadmap tree that Claude Code and any…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Читає markdown-файли, назви яким дає Claude Code, відображає їх поруч із…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Голосовий напарник для Claude Code. Обговорюйте питання з 3D-вовком на основі…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Моди Claude Code: typing-speed — індикатор швидкості введення в реальному часі…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Феєрверки для Claude Code: кожне натискання клавіші, виклик інструмента, коміт…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Відкривайте для себе моди, плагіни та розширення Claude Code з анімованими…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Мод Claude Code: діаграми mermaid, намальовані безпосередньо в транскрипті.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Невеликі моди Claude Code (плагіни function-hook): session-switcher та інші.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Мод Claude Code: мініатюри вставлених зображень над prompt у будь-якому…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Моди Claude Code: mod-scout (пошук модів, якими ви користувалися б найчастіше)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Два моди Claude Code для одночасного запуску багатьох сеансів: картка контексту…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Мод Claude Code: нативно керуйте вмістом autocompaction з TUI.
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Зробіть тарифний план Claude Pro довговічнішим: модифікації Claude Code для…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow для Claude Code: спокійний checklist над prompt, що показує план…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Найкращі модифікації коду Claude: відібрані вручну, перевірені, закріплені.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Плагін Claude Code: автоматична маршрутизація моделей Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Шість модів для Claude Code: анімований маскот Clawd, панелі ліміту…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Маркетплейс модів для Claude Code: покроковий налагоджувач циклу агента…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Моди Claude Code: меню інструментів Claude, режим Zen, теми термінала, елементи…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Найкращий універсальний набір модифікацій для Claude Code: ліміти використання…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Дивіться YouTube Shorts у Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набір інструментів Claude від Naren: навички, модифікації та MCP servers для…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Модифікація Claude Code, яка відображає відмінності Edit і Write у двох…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Модифікації для Claude Code: Clawd — крихітний піксельний маскот, який показує…
- [reporails/arcade](https://github.com/reporails/arcade) - Класичні настільні ігри як модифікації Claude Code, у які можна грати на…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Добірний список модів для Claude Code, які можна встановити як маркетплейс…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Моди Claude Code, які допомагають агенту залишатися в межах — функціональні…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Моя колекція модів Claude Code, по одному моду в кожному каталозі.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - П.
- [arviaja/token-watch](https://github.com/arviaja/token-watch) - Мод Claude Code: показує використання токенів, ліміти плану та температуру кешу…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Щойно з фабрики. Мод Claude Code: попросіть мем і продовжуйте працювати.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Мод для Claude Code: смуга кешу промпту, наступні кроки, швидкі кнопки та…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Мод Claude Code, який відображає ваші ліміти використання та витрати в смузі…
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - Мод маршрутизатора навичок: Jev вибирає та завантажує навички, потрібні для…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - App store для модів Claude Code всередині Claude Code: /mods для перегляду…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моди Herman для Claude Code (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Моди Claude Code: індикатори виконання планів, журнал того, що Claude залишив…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Модифікації Claude Code для щоденної роботи з інтерфейсом: ліміти плану…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods від MacLeod Labs: streams розплутує переплетену роботу сеансу…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Польові нотатки першого дня про моди Claude Code на Windows: індикатор палива…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Моди, які я створив і особисто використовую у своїй конфігурації Claude Code.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живі лічильники вартості, контексту й квоти плану над запитом.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Модифікація Claude Code, яка затримує розгалуження субагентів, запити з великим…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods для claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Модифікація Claude Code, яка вмикає або вимикає ваші глобальні навички, агенти…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Моди для Claude Code: плагіни, побудовані на function hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Титри в стилі кіно для вашого сеансу програмування.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Добірка модів claude code, створених мною.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Програвач YouTube на основі cliamp усередині Claude Code (мод Claude Code).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Моди Claude Code: панель agent-fleet і автопілот (маркетплейс local-mods).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Моди Claude Code від vynnlee. Одна папка на мод, встановлення з одного…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Вивчайте іноземну мову під час роботи з Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Наглядає за довгою сесією Claude Code, щоб вам не довелося: стежить за…
- [akerskuuug/claude-mods](https://github.com/akerskuuug/claude-mods) - Claude Code mod: usage, limits, branch and model around the prompt.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Стилізовані відповіді, повноширинні діаграми та ваш контекст і ліміти одним…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Коли агент пише Java, код, що порушує правила Alibaba Java (p3c), не може бути…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Бічна панель live-витрат, token і використання контексту для Claude Code: мод…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Радіопереговори Counter-Strike 1.6 для Claude Code — «Fire in the hole» під час…
- [burnrate-ai/burnrate](https://github.com/burnrate-ai/burnrate) - Переглядайте та сповільнюйте швидкість, із якою Claude Code витрачає ваші…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Herdr setup + Claude Code mods for product dev work.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Панель notch macOS для Claude Code: ліміти використання, відкриті сесії…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude готує. Спілкуйтеся зі своєю командою.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Мод для Claude Code: ловіть піксельних Modsters в idle-грі, поки працює Claude.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Космічна битва над полем запиту Claude Code, поки він працює.
- [davidbalzan/status-band](https://github.com/davidbalzan/status-band) - Моди Claude Code від David Balzan: status-band — смуга стану над підказкою…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Дивіться, які файли кожен агент Claude Code має у своєму контексті та яку…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Зберігайте холодну голову. Термометр для ваших днів у Claude Code: кожна година…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Обрізає величезні виводи інструментів до того, як вони заповнять контекст…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Невеликі моди Claude Code для термінала й настільного застосунку.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навичка + мод Claude CLI, що додає іспанські слова у відповіді агента.
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Модифікації Claude.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - A Claude Code mod that restyles it as The Machine from Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Мод Claude Code: виконує compact у потрібний момент.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Модифікація Code для обов.
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - A pixel-art Naruto companion for Claude Code: 20 ninja, 60 jutsu, performed…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-source mods for Claude Code: panes, status lines, toasts, tool guards and…
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Каталог спільноти модів, плагінів, skills, agents, hooks і серверів MCP для…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Мод Claude Code: стан сеансу, живий прогрес Spec Kit і керування usage-window.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Вікно контексту як один рядок над запитом, відтворений так, як Claude Code…
- [koslowskyj/tdd-mod](https://github.com/koslowskyj/tdd-mod) - Experimental Claude Code mod that enforces test-driven development: on coding…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Плагін (мод) для Claude Code, який робить термінальний інтерфейс Claude Code…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Дізнайтеся, що Claude Code запускає у фоновому режимі: субагенти, завдання…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Очистіть чат, збережіть роботу. Плагін Claude Code + relay-мод: Claude зберігає…
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - Personal Claude Code mods: otto-hud, Otto the octopus with context weather and…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Мод Claude, що показує pull request-и сесії GitHub на панелі поруч із…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: налагоджувач викликів інструментів Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навички Claude Code: перевірка фактів у документації, аудит коду, журнал…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Модифікація Claude Code, яка переформульовує нечіткі підказки в зрозумілі перед…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагін-компаньйон для Claude Code: ASCII-компаньйон над запитом, який памʼятає…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Плагін Claude Code для видимості інструментів за агентами — приховувати й…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Модифікація Claude Code: маршрутизація моделей/рівня зусиль під керуванням Jev…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods: security layer for Claude Code - secret redaction…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Колекція модів Claude Code.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin і mod: AI-native SDLC.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Колекція чудових модів для Claude Code | Збірка модів Claude Code.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Плагіни Claude Code (моди): перемикайтеся між кількома обліковими записами…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Перевірені моди Claude Code, що встановлюються однією командою: захисні…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Модифікації Claude Code: панелі в реальному часі та хуки для щоденної роботи.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Він говорить: модифікація Claude Code, яка за запитом уголос читає відповіді…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Модифікації Claude Code: невеликі плагіни для живих панелей, маршрутизації…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Модифікація та плагін Claude Code: монітор використання, відстеження токенів…
- [Verinoda-Labs/verinoda-symbiosis](https://github.com/Verinoda-Labs/verinoda-symbiosis) - Verinoda + Claude Code разом: Verinoda з verinoda-live, модифікація Claude…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Модифікації Claude Code. touch-map: переглядайте, які файли Claude перелічив…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Мод Claude Code, який стисло переказує непрочитані вами повідомлення агента…
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code mods + cheap-executor driver: one Claude session as lead, MiniMax…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анімований брайлівський кіт над запитом Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Мод Claude Code: спрямовує дешеву роботу до GLM/Kimi через дочірній Claude…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Піксельний кіт над запитом Claude Code, який запускає тестовий виклик…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, який обирає вдалий момент для ущільнення, щоб зберегти…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модифікації Claude для Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Магазин плагінів Claude Code від anderson-spider.
- [ankits3a/cache-keeper](https://github.com/ankits3a/cache-keeper) - Claude Code mod: prompt-cache band, keep-warm, handoff judge trial.
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - Мод Claude Code, який вибирає модель для кожного субагента перед його запуском…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Модифікація Claude Code: ваше контекстне вікно в одному спокійному рядку…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Корабель LGTM Lines пропливає повз після кожної зміни коду — модифікація Claude…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Ваші ліміти використання Claude як анімована картка здоров.
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Моди Claude Code для команди S2 (маркетплейс the ather).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткі тренування, поки Claude працює: щоденна ціль, серії, значки та…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Дошка використання для Claude Code: витрати за моделлю.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Модифікація Now Playing для Claude Code: Apple Music і Spotify над запитом, з…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - П.
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Модифікації Claude Code для сеансів оркестратора та працівників.
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Модифікації Claude Code: смуга використання, список чатів, /cube, /handoff…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Модифікації для Claude Code: Cache-Uhr, Blast Radius, Vorschlaege…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Моди Claude Code: Suggestion Spotlight показує, на що посилається…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашого Claude Code.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Моди Claude Code для harness ai-architect.tools: одна проблема на мод, стан…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Однорядкова смуга Claude Code.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Оригінальний рушій Doom із Freedoom, у який можна грати всередині Claude Code.
- [cmorss/claude-mods](https://github.com/cmorss/claude-mods) - Моди Claude Code для git worktrees: /terminal і /worktree-files відкривають…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моди Claude Code для справжніх Engineers.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Модифікації Claude Code лише для команди d3nim.
- [David-AP-TON618/claude-explain](https://github.com/David-AP-TON618/claude-explain) - Claude Code mod: /explain re-renders an answer as controlled language (STE), a…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Тамагочі, що живе всередині Claude Code: він вилуплюється, їсть код, який пише…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Закладки та позначки у стилі vim усередині термінальних розмов Claude Code…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Перетворіть кожен сеанс Claude Code на маленьку пригоду: генеративна музика, що…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code mod: shows the time on each prompt and reply in the terminal and…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Моди Claude Code, написані як хуки функцій, і маркетплейс, що їх пропонує.
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code mods and design systems: crab-crew and the Crab Crew design system.
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - Модифікації Claude Code від divramod: динамічні панелі та налаштування…
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - Модифікації Claude Code, які я використовую на кожному комп.
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Гей, вимкнув звук! Відкинь diff, обріж riff — більше ніяких редагувань, менше…
- [elkinaguas/claude-mods](https://github.com/elkinaguas/claude-mods)
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Мод Claude Code: використання підписки (5h / 7d) у вигляді смуги над полем…
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Claude Code Mod for background test progress: JUnit, Karma, pytest and unittest.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Модифікації Claude Code із продуманою анімацією: монітор у реальному часі, що…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - A live radar of your parallel branches and worktrees above the prompt: which…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - Мої моди Claude Code.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+click copy link on every code block in Claude Code replies.
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - Модифікація jev: $.jev для Claude Code, типізовані судження від TypeSafe Jev.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Mod de Claude Code: panel que muestra si el caché de prompts está caliente o…
- [Gersom/claude-mod-usage-meter](https://github.com/Gersom/claude-mod-usage-meter) - Mod de Claude Code: recuadro con el % de contexto y de los límites de 5 horas y…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Моди для Claude Code: плагіни хуків, як-от usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Моди Claude Code (плагіни function-hook), що встановлюються через один…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Бічна панель у стилі Evangelion для Claude Code: контекст, квота, активність…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Useful claude code mods.
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Claude-Code Plugin (Mod) lets you see what the model is doing while it works.
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Результати тестів на панелі Claude Code: помилки, їхні подробиці та історія…
- [hfknight/claude-mod-said](https://github.com/hfknight/claude-mod-said) - Модифікація Claude Code: /said відкриває бічну панель надісланих вами…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Мод Claude Code: скільки часу тривала кожна відповідь, скільки думав Claude і…
- [icedevil2001/session-sidebar](https://github.com/icedevil2001/session-sidebar) - Модифікація Claude Code: посилання, важливі відомості та завдання для сеансу на…
- [iddhi-sulakshana/claude-mods](https://github.com/iddhi-sulakshana/claude-mods) - Модифікації для Claude Code: кнопки наступного кроку, обмін повідомленнями між…
- [jagp/xray-mod](https://github.com/jagp/xray-mod) - ⋐∿⋑ Уважно вдивляйтеся у свої контексти: живий мод Claude Code, який показує…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - A Claude Code mod: one pane for every subagent, the files they touch, and your…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Бічна панель із використанням контексту: загальний обсяг, категорії, зростання…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Бічна панель зі списком файлів: які файли створено, змінено або видалено в цій…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пухнастик у стилі 8-bit (чорно-білий голландський висловухий кролик) бігає та…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Бічна панель «Мої запитання»: кожне речення, яке власник вводив у цій розмові;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Бічна панель із часовою шкалою: на що витрачено час у цьому раунді.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Бічна панель обміну токенами: скільки токенів головна розмова щоразу надсилає…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Чесна коробочка для claude code: після кожної відповіді Claude тихо каже одну…
- [jgilb17/claude-mods](https://github.com/jgilb17/claude-mods)
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Контрольний список плану для Claude Code із перевіркою доказів: затверджені…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Невеликі модифікації для Claude Code, як-от нові команди зі слешем і бічні…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Багатокористувацькі ігри, у які можна грати всередині Claude Code, поки він…
- [juliomyitbrain/claude-code-git-graph](https://github.com/juliomyitbrain/claude-code-git-graph) - Claude Code mod: a pane that draws the repository.
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Модифікація Claude Code: підтримує кеш підказок у теплому стані, поки вас…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живе в смузі над вашим prompt Claude Code: розігрує сесію, показує, що…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - Модифікація Claude Code, яка показує доступний ліміт запитів, токени сесії та…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод, що озвучує відповіді та сповіщення Claude Code за допомогою VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Мод Claude, який читає та об.
- [kikostefanov-lab/claude-code-mods](https://github.com/kikostefanov-lab/claude-code-mods) - Моди Claude Code: панель Whiteboard, де Claude створює діаграми Mermaid/UML, що…
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Niceties/quality of life improvement Claude mods.
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - стискання неактивних сеансів claude code за допомогою haiku — однорядкова смуга…
- [kk5190/claude-code-mods](https://github.com/kk5190/claude-code-mods) - Модифікації для Claude Code: вимірювач контексту та панелі серверів розробки.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - A live task HUD for Claude Code Desktop: a strip above the prompt while Claude…
- [KytioisaCat/playpen](https://github.com/KytioisaCat/playpen) - Кому потрібна увага? Інші сеанси Claude Code у вигляді карток над полем запиту…
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Посібник зіставлених спільнотою модів Claude Code: варіанти використання…
- [lucasram20/claude-mods](https://github.com/lucasram20/claude-mods)
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод для Claude Code, який показує, що робить Claude, у підзаголовку вкладки…
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Мод Claude Code: спонукає основний сеанс делегувати завдання субагентам і…
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - My personal collection of claude mod plugins.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Модифікація Claude Code із перемиканням профілів дозволів: безпечна базова…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community mods for Claude Code: guards, panes, and commands that run inside…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Бічна панель для Claude Code: файли, які написав Claude, розділення термінала…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mikejhill/claude-usage-status](https://github.com/mikejhill/claude-usage-status) - Claude Code mod: always-on band showing 5h/weekly limits, context fill, and…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Спокійна бічна панель для Claude Code: що робить цей сеанс, його план, агенти…
- [mmedum/spor](https://github.com/mmedum/spor) - Повертає те, що Claude Code приховує: файли, які прочитав Claude, виконані ним…
- [moonteek/claude-mods](https://github.com/moonteek/claude-mods) - Моди Claude Code: смуга пам.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Моди Claude Code: автоматична передача та індикатор перебігу.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, який знову вмикає інструменти todo для моделей, що їх не…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одному рядку для кожного завдання над запитом із поточним…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Грайте в Connect Four проти AI всередині Claude Code (/connect-four).
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Піксельний канарок для Claude Code: він гине, коли Claude припиняє виконувати…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Модифікація Claude Code: коли інший агент програмування робить коміт у ваш…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Модифікація Claude Code для репозиторіїв, спільних для кількох AI-агентів: не…
- [narley/sessions-sidebar](https://github.com/narley/sessions-sidebar) - Claude Code mod: a sidebar listing every Claude Code session, for Warp.
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Панель кібернеонової інтернет-радіостанції для Claude Code…
- [niksavis/handily](https://github.com/niksavis/handily) - Модифікації Claude Code, які показують ваші робочі елементи, завдання та сеанси…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Повторно активує тривалі спостереження Monitor у Claude Code після їх…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Захисний бар.
- [OctopiAI/claude-code-statusline](https://github.com/OctopiAI/claude-code-statusline) - Легкий Mod для Claude Code.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Одна модифікація для Claude Code, із пріоритетом Windows і CJK: попередній…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime для Claude Code: звук, коли Claude завершує роботу, потребує вашого…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Модифікації Claude Code: мініатюри зображень і рядок стану.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Найкращі моди Claude Code, упорядковані за тим, що вони роблять для вас.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Модифікація Claude Code: перегляд кожного зображення та файлу, які переглядав…
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - A Claude Code mod that holds risky shell commands.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Два моди Claude для Claude Code: garde-du-corps.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Lazy Panda Panel для Claude Code: переглядайте документи, не піднімаючи лапи.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Бічна панель статистики сеансу в реальному часі для вкладки Code настільного…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Різноманітні моди та навички для мого налаштування Claude Desktop.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Модифікації для Claude Code: safety-guard блокує руйнівні команди та доступ до…
- [prompteafacil-hub/mods-claude-code](https://github.com/prompteafacil-hub/mods-claude-code) - Mods de Claude Code de la comunidad prompteafacil.
- [ptpmediabr/ideas-shelf](https://github.com/ptpmediabr/ideas-shelf) - Полиця ідей для кожного проєкту: записуйте ідеї на дошці та позначайте їх як…
- [ptpmediabr/mods-manager](https://github.com/ptpmediabr/mods-manager) - Панель для перегляду, увімкнення, вимкнення, встановлення та групування ваших…
- [ptpmediabr/side-chat](https://github.com/ptpmediabr/side-chat) - Бічна панель чату всередині сесії, яка відповідає на запитання або виконує…
- [ptpmediabr/usage-weather](https://github.com/ptpmediabr/usage-weather) - Один непомітний рядок над полем запиту: контекст, використання за 5 годин і за…
- [qarge/claude-mods](https://github.com/qarge/claude-mods)
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Модифікація Claude Code: тикер котирувань у реальному часі, панель /quote…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Модифікації Claude Code, опубліковані як єдиний маркетплейс плагінів.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Модифікація Claude Code: хост SSH, RAM і ліміти використання 5h/7d у рядку над…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod: відтискання, які треба робити, поки працює Claude. Без токенів.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Крамниця модів для Claude Code: збирає моди з GitHub, показує їх попередній…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Модифікація Claude Code: перетворює план, який ви схвалюєте в режимі…
- [sadhirr1/claude-mods](https://github.com/sadhirr1/claude-mods) - Just a repo with different claude mods.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Ретельно відібраний список модів Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Безкоштовний режим: допоміжні агенти працюють на Haiku, а великі файли й…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музичний супровід у стилі lofi, що супроводжує сесію: спокій, зосередженість…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Навчайтеся, поки Claude пише код: після ходу, який змінив код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запис кожної зміни, яку вносить Claude: відтворюйте кожну зміну, спостерігаючи…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Кожне посилання, згадане у вашому сеансі, в одному рядку над запитом.
- [SanjayPG/claude-code-usage-tracker](https://github.com/SanjayPG/claude-code-usage-tracker) - Claude Code mod: live usage-quota progress bars above your prompt.
- [SanjayPG/claude-quota-band.](https://github.com/SanjayPG/claude-quota-band.) - Claude Code mod: live usage-quota progress bars above your prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Мінімальна демонстрація function hooks Claude Code: панель токенів/вартості в…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board та інші модифікації Claude Code від André Servaes.
- [shaheershoaib/agent-warehouse](https://github.com/shaheershoaib/agent-warehouse) - agent-warehouse: a Claude Code mod by Shaheer Shoaib.
- [shaheershoaib/usage-meter](https://github.com/shaheershoaib/usage-meter) - usage-meter: a Claude Code mod by Shaheer Shoaib.
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - Моди Claude Code (плагіни функціональних хуків) від ShellTime.
- [siller/supermod](https://github.com/siller/supermod) - Claude Code mod: Superpowers progress, context window and agents above the…
- [simplybychris/claude-code-mods](https://github.com/simplybychris/claude-code-mods) - Моди для Claude Code: режим запису, панель кешу, Snake і панель агентів.
- [skryvets/claude-code-session-mod](https://github.com/skryvets/claude-code-session-mod) - Claude Code mod: coloured session info under the prompt - context, model…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Затишний RPG HUD-мод для Claude Code.
- [sstani-bgv/claude-crew](https://github.com/sstani-bgv/claude-crew) - Мод Claude Code: бічна панель із піксельним крабом для субагентів.
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Особистий маркетплейс модифікацій Claude Code…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Повідомлення комітів одним кліком для Claude Code з танцюючою піксель-арт…
- [StevenGFX/claude-gh-actions](https://github.com/StevenGFX/claude-gh-actions) - Claude Code mod: GitHub Actions runs in a /ci pane, the status line and toasts.
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude code mods.
- [stylusnexus/claude-mods](https://github.com/stylusnexus/claude-mods)
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Claude Code mods: mini-bar HUD.
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugins for Claude Code.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Mods for Claude Code: delete-guard.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Мод Claude Code: переглядайте використання свого плану Claude.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Мод Claude Code: панель у реальному часі для кожного субагента.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, що показує поточний сеанс в окремій області: кожен запит…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Маркетплейс плагінів Claude Code із модами: плагіни function-hooks, що малюють…
- [thickiran/claude-coaster-tycoon](https://github.com/thickiran/claude-coaster-tycoon) - 🎢 Claude builds you a RollerCoaster Tycoon-style theme park while it works.
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code mod: a docked pane showing the session.
- [tjanuki/claude-mod-context-meter](https://github.com/tjanuki/claude-mod-context-meter) - Claude Code mod: context-window fill in the status line and a hand-off reminder…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Збільште використання Claude Code до двох разів.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Моди Claude Code від Toptaab.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Модифікація Claude Code: смуга та панель для відстеження ваших субагентів і…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - A curated catalogue of Claude Code mods, each with a copy-paste prompt that…
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анімована смуга поступу та підсумок завершення для тривалих…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Three small Claude Code mods: see when your subagents will finish, queue…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажіть &quot;I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Поставте Claude додаткове запитання в панелі поруч із вашою роботою.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace de mods do Claude Code com instalação em um passo e guia em vídeo…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Rate-limit countdowns and a burn-rate forecast for Claude Code.
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Рівень безпеки Roblox Studio для Claude Code: аудит RemoteEvent, скасування…
- [was865/usage-band](https://github.com/was865/usage-band) - Claude Code mod: context window, prompt cache hit rate and countdown, rate…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Claude Code mods: stage-toons, a workflow progress bar above the prompt with…
- [wolves/usage-line](https://github.com/wolves/usage-line) - Claude Code mod: usage, model, effort and advisor readout above the prompt.
- [wszaq/claude-mods](https://github.com/wszaq/claude-mods) - Невеликі плагіни Claude Code для безпечніших і зрозуміліших локальних робочих…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моди для Claude Code. agent-crew: спостерігайте за роботою ваших субагентів як…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Моди Claude Code: капсула наступного кроку 繁中, копіювання блоків, мініатюри…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Постійна смуга над полем запиту Claude Code: заповнення контексту та вікна…
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - Personal Claude Code mods (plugin marketplace).
- [zhuzhu0710/claude-mods](https://github.com/zhuzhu0710/claude-mods)
- [ziedgithub/claude-code-mods](https://github.com/ziedgithub/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Ретельно підібрана колекція найкращих ресурсів для найкрутіших агентів, Claude…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Плагін Claude Code, який показує, що відбувається: використання контексту…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Красивий, надзвичайно налаштовуваний рядок стану для Claude Code CLI із…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Усі частини системного запиту Claude Code, 27 описів вбудованих інструментів…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Понад 45 порад, як отримати максимум від Claude Code — від основ до складних…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / навичка Codex — створює каруселі Xiaohongshu та пари обкладинок…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Beautiful vim-style powerline for Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Переглядайте diff вашого агента кодування в панелі термінала й надсилайте…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Комплексний плагін рядка стану для Claude Code із використанням контексту…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code і Codex — локальне відстеження токенів: рядок стану.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Створюйте модифікації для Claude Code: перехоплюйте будь-який запит, змінюйте…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Комплексна інформаційна панель рядка стану для Claude Code — інформація про…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: відстеження вуглецевого сліду ваших сеансів Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Естетичний рядок стану для Claude Code від awesomejun.
- [fatihaydost/brand-identity-skill](https://github.com/fatihaydost/brand-identity-skill) - A Claude Code skill that designs a brand identity as one system: logo…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Публічні навички та моди Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Навички, моди, допоміжні агенти, хуки, slash-команди та посібники для Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Законні безкоштовні LLM APIs і агенти для програмування — самостійне…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Рядок стану термінала для сесій Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live-рахунки футбольних матчів, календарі та турнірні таблиці для змагання…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Навичка агента, що перетворює вашого агента програмування на експерта з…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Персональна конфігурація Claude Code з версіюванням у ~/.claude — агенти…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Час молитви, дата за календарем Хіджри, азкари, щоденний аят, піст за сунною…
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) - Tavily-powered optional search tool for DeepSeek Harness.
- [livlign/ccbit](https://github.com/livlign/ccbit) - Рядок стану з урахуванням сеансів для Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · Дослідницький граф — плагін DeepSeek Harness для…
- [igdigitallab/cardloop](https://github.com/igdigitallab/cardloop) - Your AI dev team on your own server, steered from your phone.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Портативний набір інструментів Claude Code для .NET DDD/Clean Architecture…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Набір плагінів для Claude Code, pi і DeepSeek Harness: HUD у рядку стану…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Портативна глобальна конфігурація Claude Code: власні навички, хуки PreToolUse…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагіни Claude Code, якими я користуюся щодня: навички та моди, очищені так…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram усередині Claude Code: читайте чати й канали в панелі, отримуйте…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Міст між DSH і Feishu (Lark), розроблений власноруч (не форк): картка потокової…
- [Dakaric/claude-code-statusline](https://github.com/Dakaric/claude-code-statusline) - Готовий до встановлення статусний рядок для Claude Code: смуга вікна контексту…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Маркетплейс плагінів і навичок Claude Code для полегшення модифікації гри Hytale.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Керування токенами для Claude Code: найкраща модель керує, а виконання…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Переглядач із розділеною панеллю для Claude Code у Windows Terminal і tmux…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Неофіційні моди для вкладки Code у Claude Desktop — usage-pet: смуга…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Репозиторій модифікацій Claude Code Awesome Media.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Скоротіть витрати токенів Claude Code і Codex: спрямовує запити та тестові…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Сповіщення про ліміти використання для Claude Code: macOS сповіщень…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Налаштовуваний рядок стану Claude Code для Linux, WSL, Windows і macOS, із…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Fast Rust statusline for Claude Code — payload-first, cached git, ~10ms renders.
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Рядок стану Claude Code з панеллю контексту, спарклайном токенів і відстеженням…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Панель моніторингу використання Claude Code у реальному часі — розподіл…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Відображення ключових відомостей про стан Claude Code, зокрема моделі…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - дружній рядок стану Claude Code, у якому можна налаштувати все — панелі…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Multi-row Claude Code status line: spend, context %, git, and active account…
- [QingqiShi/claude](https://github.com/QingqiShi/claude) - Personal ~/.claude for Claude Code: settings, global CLAUDE.md, hooks, status…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline з корисною інформацією для claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Стартовий шаблон для організації робочого простору Claude Code кількох…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Власні команди агентів. Під контролем.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Власний рядок стану для Claude Code — панель контексту з відсотком…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Магазин плагінів Claude Code із baloo: навички, агент, який перевіряє зміни…
- [chrisns/claude-image-cli-mod](https://github.com/chrisns/claude-image-cli-mod) - Переглядайте зображення, які виводять команди.
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Рядок стану Claude Code: використання контексту, смуги квот 5h/7d, час…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Рядок стану Claude Code професійного рівня: тривалість сесії, вартість у…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Рядок стану Claude Code з урахуванням підписки.
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - A Claude Code plugin: a pane of the live Claude Code and Codex sessions on your…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - A rich terminal statusline for Claude Code — Bun + TypeScript, zero runtime…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Дворядковий рядок стану для Claude Code: контекст, обмеження швидкості з…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Плагін Claude Code, який красиво відображає діаграми Mermaid у транскрипті…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Інструменти, навички та агенти для Claude Code — починаючи з рядка стану, який…
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Claude Code global config: agents, skills, mods, settings.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Плагін Claude Code: завжди бачите залишок свого ліміту використання Claude на 5…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Реальні витрати DeepSeek API для Claude Code: перераховує вартість стенограм…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Рядок стану Claude Code із рядками панелі агентів.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Синхронізуйте завдання Claude із Fizzy.do, щоб команда бачила їх у реальному…
- [izzatum/claude-code-cockpit](https://github.com/izzatum/claude-code-cockpit) - Плагін статусного рядка Claude Code (cockpit): % контексту, вартість сесії та…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - A status line and token line for Claude Code: context, 5-hour and weekly usage…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Показує детальний статус-рядок із кольоровим кодуванням для Claude Code…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Меню налаштувань, рядок стану та конфігурація Claude Code.
- [Larg0Winch/claude-label](https://github.com/Larg0Winch/claude-label) - Редагована мітка для кожного вікна в рядку стану Claude Code.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Спілкуйтеся з Claude Code голосом у Windows: Mod + helper, що використовує…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Хук статусного рядка Claude Code — відстежує використання токенів і контекст…
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Власний рядок стану Claude Code із вікном контексту, відстеженням використання…
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - Швидкий рядок стану Rust для Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - home-grown, cage-free claude plugins, skills, mods, and more.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Інсталятор середовища Claude Code: навички, рядок стану, хуки, дозволи та…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Плагіни та модифікації Claude Code для розуміння того, що робить Claude…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Відстежуйте стан Claude Code зі своєї панелі меню macOS за допомогою…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Кольоровий багаторядковий рядок стану для Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Рядок стану Claude Code для Windows (PowerShell): смуги використання, зворотний…
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Плагіни Claude Code. Usage Bars показує ліміти сеансу та тижневі ліміти…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Модифікація Bearings and Glossary для Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Власний рядок стану Claude Code (upstream: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Конфігурація та моди Claude Code зі спільним набором компонентів, пісочницею та…
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Невелика панель для Claude Code: відсоток контексту, зворотний відлік кешу…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Портативна конфігурація Claude Code: CLAUDE.md, settings, statusline, skills.
- [thurtado1993/claude-cabina](https://github.com/thurtado1993/claude-cabina) - Cabina: a live session dashboard for the Claude Code Desktop side panel.
- [tichara1/ai.claude-status-panel](https://github.com/tichara1/ai.claude-status-panel) - Mod pro Claude Code: panel nad promptem s kontextem, limity, cenou, stavem…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Відстежуйте використання контексту Claude Code, витрати сеансу та скидання…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用の mod 集 (goal-orchestrator: /goal をタスク分解して SubAgent に委譲させる).
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Real-time cost tracking and session monitoring statusline for Claude Code.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Плагін Cordis / DeepSeek Harness — агент запитує в людини секрет у вбудованій…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Трирядковий рядок стану Claude Code: глибина контексту, міжсеансові обмеження…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Детектор виснаження контексту 2026 — проактивна пам.
- [zerofaultlabs/claude-statusline](https://github.com/zerofaultlabs/claude-statusline) - Рядок стану Claude Code: використання контексту, обмеження швидкості, вартість…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Хуки, субагенти та рядки стану Claude Code: колекції інструментів із відкритим…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Рядок стану Claude Code — індикатори використання Claude/Codex, що залишаються…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code statusline showing real-time token usage and estimated energy…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Моди для Claude Code: панелі, смуги й помічники на основі function hooks.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Передавайте завдання між сеансами Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Це сервер MCP для керування MODS — модульним кросплатформним інструментом для…
- [pedrotspinola/lps-statusline](https://github.com/pedrotspinola/lps-statusline) - Користувацький статусний рядок Claude Code: модель і рівень зусиль, нативна…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Навичка Codex і Claude Code для перекладу модів CK3 за допомогою локального LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Моди з відкритим кодом та інші розширення для Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: знаходить те, що ви знову й знову просите Claude Code, і перетворює…

</details>

<a id="dsh-cordis"></a>

## Екосистеми плагінів DSH і Cordis

DeepSeek Harness і Cordis досягають того самого результату іншим шляхом: для них плагін є механізмом модів, тож плагін там — еквівалент мода тут.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74280 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

🌊 Оригінальний агентний рушій. Розгортайте інтелектуальні багатокористувацькі рої, координуйте автономні робочі процеси та створюйте розмовні системи ШІ. Серед можливостей: адаптивна пам’ять, інтелект із самонавчанням, федерація, інтеграція векторного RAG та нативна інтеграція з Claude Code / Codex / Hermes і багатьма іншими

<sub>🔧 Знайдено використання в коді: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                        |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **74280**  |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100394 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

🎨 Найкращий плагін дизайну DeepSeek Harness. Альтернатива дизайну з відкритим кодом для Claude. 🖥️ Настільний застосунок із пріоритетом локальної роботи. 🖼️ Ваш агент програмування стає рушієм дизайну: прототипи, цільові сторінки, інформаційні панелі, слайди, зображення та відео — реальні файли, експорт у HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode та понад 20 CLI через BYOK.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **100394** |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81639 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Перетворюйте будь-яку ідею, план або кодову базу на красиву інтерактивну діаграму. Навичка агента для Claude Code, Codex та інших.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **81639**  |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐70094 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Здійснюйте зворотне проєктування чого завгодно за допомогою агентів — від поведінки застосунків до нативних бінарних файлів.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **70094**  |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Надійний агент програмування для складних завдань з розробки програмного забезпечення.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Go                                                                              |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **35760**  |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30358 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Сучасне десктопне рішення для екосистеми плагінів DeepSeek Harness (DSH). Усе є «плагіном», і сам робочий стіл також є «плагіном».

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **30358**  |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25470 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Опис

Distilly — перетворюйте спосіб їхнього мислення на багаторазово використовувані навички для будь-якого агента або бота. Раніше — Colleague Skill（原同事 Skill）.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Python                                                                          |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **25470**  |
| Останній push           | 2026-09-22 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Метафреймворк просторово-часової композиційності

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **9112**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8594 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Екосистема агрегації вебплагінів DeepSeek Harness (DSH) · Усе є плагіном, що поширюється через Creative Workshop｜｜Екосистема агрегації вебплагінів DeepSeek Harness (DSH) · Усе є плагіном, що поширюється через Creative Workshop

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **8594**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4266 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Офіційно найрекомендованіший TUI-плагін DSH — висока продуктивність, низькі накладні витрати, милий піксельний кит, плавна взаємодія з мишею. Встановлення однією командою через npm. / Офіційно першочергово рекомендований TUI-плагін DSH: висока продуктивність, низьке споживання, милий піксельний кит, плавна взаємодія з мишею, встановлення npm в один клік

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **4266**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3162 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Десктопна версія DeepSeek Harness на Tauri | Лише 8 МБ у встановлювачі, нульове налаштування середовища, попередньо встановлені плагіни, Windows / macOS / Linux.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **3162**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1583 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Захист перед виконанням для AI-агентів програмування. Він блокує деструктивні команди Git і файлової системи, а також поширені спроби доступу до конфіденційних файлів до виконання виклику інструмента. Підтримує Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode і Pi.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1583**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1167 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Memory for Claude Code, Codex, Cursor and 38 more coding agents, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Go                                                                              |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1167**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1139 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Опис

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Go                                                                              |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1139**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-11 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1007 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

The most comprehensive DeepSeek Harness plugin market — refreshed daily, sourced across the Internet, reviewed before publishing.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1007**   |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐702 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Настільний клієнт DeepSeek Harness (dsh) Windows — у комплекті Node.js + dsh CLI, запуск одним натисканням

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **702**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **593**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-11 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Неофіційний плагін DSH (DeepSeek Harness): використовуйте вебмоделі chat.deepseek.com як провайдера LLM — захоплення входу через браузер, розв’язання PoW, потокова передача SSE, виклики інструментів на основі промптів.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **247**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Нативний плагін DeepSeek Harness (DSH), що інтегрує TypeSafe Jev або Decision api на кшталт luna як шар ухвалення рішень System One для вибору агентів, нагляду, виправлень і затверджень.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **203**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Плагін DeepSeek Harness для міграції сеансів між наборами налаштувань із попереднім переглядом. Передавання за фіксованою схемою зберігає стан, задум вихідної моделі та невирішені зображення; оригінальний сеанс залишається незмінним.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **165**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐130 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Після встановлення автоматично доступні 27 навичок mattpocock/skills v1.3.1 для інженерії та продуктивності — встановлювати навички вручну не потрібно. Для створення цього плагіна використано 40 мільярдів токенів; він забезпечує 10-кратне підвищення ефективності розробки порівняно з оригінальними навичками, а також допомагає новачкам швидше опанувати цей набір навичок. Повна підтримка GitHub issue; Markdown — попередня версія; GitLab наразі не підтримується. Дякуємо за використання та підтримку 💗

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **130**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐127 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Тема Claude Code для DeepSeek Harness｜ Настільна тема Claude Code для вебграфічного інтерфейсу DeepSeek Harness

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **127**    |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>анімований запис</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐87 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Навички та плагіни You.com для вебпошуку, вилучення вмісту, досліджень, фінансів і пошуку інтеграцій, які допомагають агентам ШІ працювати з актуальним вебконтекстом.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **87**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐85 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

StudyHub: плагін DeepSeek Harness (DSH), що перетворює ваші власні матеріали на запитання та інтервальне повторення · DSH-плагін для навчання, який перетворює власні матеріали на завдання й інтервальне повторення

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **85**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

dsh-sieve: плагін інженерії контексту та оптимізації токенів для DeepSeek Harness (DSH) — фільтрація виводу інструментів, обрізання контексту, поступове розкриття навичок. На 36% менше даних під час офлайн-відтворення. Плагін керування контекстом і оптимізації токенів DSH для економії.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **72**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Маркетплейс, що автоматично класифікує, каталогізує та перевіряє плагіни спільноти DeepSeek-Harness. Автоматично категоризуйте, куруйте та перевіряйте маркетплейс плагінів спільноти DeepSeek-Harness.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **69**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐57 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Актуальний каталог плагінів DeepSeek Harness — оновлюється щогодини, щодня проходить перевірку сумісності, містить вбудований магазин плагінів і генератор каркасів. Актуальний каталог плагінів DSH: оновлення щогодини, щоденне практичне тестування сумісності, вбудований магазин плагінів і генератор каркасів.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | HTML                                                                            |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **57**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐27 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

NekroNXT: багатоплатформна система агентів для групових чатів на основі DeepSeek Harness (DSH)｜Багатоплатформна система агентів для групових чатів на основі DSH

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **27**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zp-home/dsh-recommend">zp-home/dsh-recommend</a></b> · ⭐22 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Прозорий рейтинг і рекомендації екосистеми DSH-плагінів: щоденне автоматичне збирання topic dsh-plugin + публічна модель оцінювання + рейтингові/рекомендовані плагіни та статичний сайт

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **22**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `deepseek-harness` · `dsh-plugin` · `plugin` · `rankings` · `recommendations`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zp-home--dsh-recommend/fbc10141cf0df5b3.png" width="100%" alt="zp-home/dsh-recommend screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-superpower">Wenaixi/dsh-superpower</a></b> · ⭐21 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Плагін DeepSeek Harness: 15 інженерних навичок obra/superpowers, двомовні описи, перемикачі для кожної навички | Плагін DeepSeek Harness: 15 навичок інженерної дисципліни obra/superpowers, вільне перемикання між китайськими та англійськими описами навичок, окремий перемикач для кожної навички

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **21**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `ai-agent` · `brainstorming` · `chinese` · `code-review` · `cordis` · `debugging` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-superpower/72fd369dacf071c0.png" width="100%" alt="Wenaixi/dsh-superpower screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-mcp-manager-ui">Imzl-zl/dsh-mcp-manager-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

UI керування сервером MCP для DeepSeek Harness Web — плаваюча панель, імпорт JSON і persistence на основі профілів.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **20**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-mcp-manager-ui/344d069db6cf421d.png" width="100%" alt="Imzl-zl/dsh-mcp-manager-ui screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/pptwise">liustack/pptwise</a></b> · ⭐19 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Справжній PowerPoint, а не HTML. Скажіть ШІ, що потрібно висвітлити, і pptwise створить редаговану презентацію на вашому комп’ютері. Навичка агента + плагін DSH, без облікового запису та без ключа API для рендерингу. | Справжній PPT, а не HTML. Скажіть ШІ, про що потрібно розповісти, і pptwise створить редагований PPT на вашому комп’ютері. Навичка агента + плагін DSH, без реєстрації, для рендерингу не потрібен ключ API.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **19**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skill` · `agent-skills` · `ai-agent` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deck-generation`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--pptwise/e6f193d6fc2ea355.png" width="100%" alt="liustack/pptwise screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-ponytail">Wenaixi/dsh-ponytail</a></b> · ⭐18 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Плагін DeepSeek Harness: лінивий senior-режим DietrichGebert/ponytail і порт семирівневої драбини, 6 навичок із двомовними описами та перемикачами для кожної навички, нуль інструментів, нуль промахів кешу | Плагін DeepSeek Harness: ідеально перенесені лінивий senior-режим і семирівнева драбина DietrichGebert/ponytail, двомовне перемикання описів 6 навичок, окремий перемикач для кожної навички, без реєстрації інструментів, без руйнування кешу в будь-яких сценаріях

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **18**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent-skills` · `ai-agents` · `claude-code` · `code-review` · `cordis` · `cursor` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-ponytail/ffd031e53f39269a.png" width="100%" alt="Wenaixi/dsh-ponytail screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KannaKuron/dsh-better-workspace">KannaKuron/dsh-better-workspace</a></b> · ⭐17 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Вебплагін DSH: ієрархічне дерево робочого простору для бічної панелі — заголовки, що містять /, об’єднуються у віртуальні папки; у процесі додавання робочого простору з’являється спливне вікно батьківської групи

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **17**     |
| Останній push           | 2026-10-10 |
| Вперше додано до списку | 2026-10-10 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `sidebar` · `tree` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kannakuron--dsh-better-workspace/83cddff440dfe49a.png" width="100%" alt="KannaKuron/dsh-better-workspace screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary><b>Більше в цій категорії</b> <sub>· 63</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Добірний список найкращих чудових ШІ-плагінів для ШІ-асистентів, зокрема Claude…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Ринок плагінів DSH / DSH Plugin Marketplace: перегляд, встановлення та…
- [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) - Remote-work assistant for DeepSeek Harness (DSH): connect SSH.
- [morluto/flameox](https://github.com/morluto/flameox) - Runtime evidence that helps agents trace, profile, and burn down hotspots in…
- [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) - DSH plugin - framework upgrade safety &amp; plugin gating: contract pre-check…
- [arcships/rutis](https://github.com/arcships/rutis) - Plugin runtime для програм, що продовжують працювати — ядро Rust, плагіни…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Спільнота-агрегатор плагінів DeepSeek Harness — автоматична синхронізація…
- [mrRisega/dsh-remote](https://github.com/mrRisega/dsh-remote) - 公网远程控制 DeepSeek Harness.
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Каталог вибраних плагінів DeepSeek Harness (DSH) — понад 280 плагінів спільноти…
- [Cerbur/clutch-dsh](https://github.com/Cerbur/clutch-dsh) - Open-source DSH plugins for DeepSeek Harness：Git Worktree session…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin: Git Bash shell for all agent modes on Windows.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Інструментарій Zotero для DeepSeek harness;
- [maxwell-feng/dsh-tinyfish-search](https://github.com/maxwell-feng/dsh-tinyfish-search) - TinyFish-backed web search provider for DeepSeek Harness (ctx.web) — 将内置…
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - Community GitHub Action для DeepSeek Harness — AI Code Review · CI Diagnosis ·…
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Локальний робочий стіл для авторів китайської вебпрози (19 інструментів): перед…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Підібрані спільнотою плагіни, інструменти, навички й навчальні ресурси DeepSeek…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [miuzel/dsh-graph](https://github.com/miuzel/dsh-graph) - 把工作组织成目标看板的 DeepSeek Harness (dsh) 插件：目标 / 判据 / 上下文卡片 / 执行 attempt…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Перетворює моделі, у які вже виконано вхід у локальному десктопному WorkBuddy…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Ізольовані запуски встановлення та smoke-тестування для плагінів DeepSeek…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Плагін функціональної панелі DeepSeek Harness: одна панель для…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Постійне тестування сумісності плагінів DeepSeek Harness: точні випуски…
- [gezi-wen/sage-mem](https://github.com/gezi-wen/sage-mem) - File-based cross-session memory for DeepSeek Harness (DSH) — every memory is a…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeekBot: альтернатива GrokBot із відкритим кодом на основі DeepSeek Harness…
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - The bilingual, source-backed registry and installer for the DeepSeek Harness…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Рентген для плагінів DeepSeek Harness: заявлені можливості проти фактичної…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Хост-плагін DeepSeek Harness, який зберігає документи проєкту та довготривалу…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Podman-backed execution for DeepSeek Harness (dsh).
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Local-first voice conversations for DSH.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Плагін DSH: інструментальне вікно Git рівня IDE як нативна вкладка…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC 模式基础上的创造模式:DSH 插件,合成 Code Mode 工具编排 + 自引用 Cordis 工具与 preset 创作指导,物化为…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Плагін інженерного робочого процесу для DeepSeek Harness: етапи завдань, записи…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH 角色扮演插件：角色卡（系统提示词注入 + 用户提示词改写）、可分享的单文件卡包、复刻原版 UI 的角色页签与首轮选角 chip.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт перевірки плагінів DeepSeek Harness (dsh) без залежностей — контрольні…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Маркетплейс плагінів DeepSeek Harness - перегляд, пошук і встановлення плагінів…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode на DeepSeek Harness — плагін DSH, який забезпечує роботу OpenCode Zen…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонній маркетплейс плагінів і захищений менеджер життєвого циклу…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx — це людиноцентричний розширюваний настільний робочий простір: чати…
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - Демон dsh: реєструє вебсервер DeepSeek Harness (dsh web) як фонову службу з…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Плагін для введення у вебверсії DSH: перемикання клавіш надсилання/перенесення…
- [grloper/dsh-claude-oauth](https://github.com/grloper/dsh-claude-oauth) - Claude Pro/Max OAuth model provider for DeepSeek Harness with Google/Gmail…
- [iasiv5/dsh-skip-browser-auth](https://github.com/iasiv5/dsh-skip-browser-auth) - DSH 插件：（Web Profile 专用）自动跳过 BrowserAuth，访问 Web 地址即可直接使用，无需每次复制启动 URL 中的随机 Token…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Надає для десктопної версії DeepSeek Harness точку входу віддаленого доступу з…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Плагін DeepSeek Harness: перетворює збій підготовки ACL пісочниці Windows…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Робить безіменну спробу порожньої моделі доступною для повторної спроби — для…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Середовище виконання плагінів Rust із перевіреним Verus ядром життєвого циклу…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Магазин плагінів dsh - автоматичне виявлення на основі GitHub topic:dsh-plugin…

</details>

<a id="writing"></a>

## Тексти, обговорення та відео

Статті, обговорення та відео про можливості модифікацій.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 2 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Опис

Привіт, HN, я створив це для себе й захотів опублікувати у відкритому доступі. Проблема була в тому, що мені потрібен спосіб отримувати нагадування між промптами, оскільки я часто проводжу довгі години в терміналі, особливо тепер, коли ми зазвичай обробляємо так багато агентів паралельно. Перша версія була простою rep

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 7 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Опис

Опис від upstream не було опубліковано.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Опис

Я створив це, тому що з новітніми моделями програмування Claude переходить у режим глибокої роботи з незрозумілими командами, і я вже не розумію, що саме відбувається. Це мод (плагін, який використовує нові функціональні хуки Claude Code), що малює над підказкою один рядок: — поточний крок,

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Тексти, обговорення та відео`                                            |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Вперше додано до списку | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Проєкти за мовою реалізації

Екосистема зосереджена навколо Python і TypeScript, але типізовані клієнти продовжують з’являтися й іншими мовами. Цю таблицю сформовано на основі самих записів.

| Мова       | Записи | Приклади                                                                                                      |
| ---------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 396    | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                          |
| JavaScript | 87     | `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                  |
| Python     | 43     | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30     | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 16     | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7      | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5      | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2      | `rainyfei/claude-statusline-win`, `YangShen-SWE/dsh-plugin-simple-pet`                                        |
| Swift      | 2      | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1      | `reporails/arcade`                                                                                            |

<sub>Враховуються лише записи, у яких зазначено мову. Документація та записи обговорень не включені до цієї таблиці.</sub>

## Участь у розробці

Виправлення вітаються — це найшвидший спосіб покращити цей список. Створіть issue або pull request, якщо запис віднесено не до тієї категорії, неправильно оцінено або якщо проєкт помилково виключено через збіг назви — саме в цій останній категорії автоматизовані фільтри найчастіше помиляються.

---

<sub>Незалежний проєкт спільноти. Не пов’язаний із Anthropic, не схвалений і не перевірений ним. Claude Code, Claude і Anthropic — торговельні марки Anthropic. Поведінка продукту може змінюватися без попередження; усе критично важливе перевіряйте за офіційною документацією. Права на ресурси залишаються за їхніми проєктами-джерелами; вони відтворюються лише там, де це дозволено ліцензією.</sub>

<sub>Востаннє оновлено · 2026-10-11T05:58:46+08:00</sub>
