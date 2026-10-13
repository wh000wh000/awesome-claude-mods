<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Круті моди для Claude">
</p>

<h1 align="center">Круті моди для Claude</h1>

<p align="center"><b>Індекс модів і плагінів для Claude Code, оцінених за доказовістю, а також глибших змін у поведінці, які вони вносять.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-494-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <b>Українська</b></sub></p>

> [!NOTE]
> **Актуальний індекс** · Остання синхронізація: `2026-10-13T21:42:20+08:00` (UTC+8)
> · Записи: **494** · Додано під час останнього оновлення: **0** · Мови реалізації: **13**

<sub>Кожен наведений нижче запис було автоматично зібрано, відфільтровано та повторно перевірено. Тут немає платних розміщень.</sub>

<a id="featured"></a>

## Актуальна добірка

<sub>По одному запису на категорію, упорядкованому за рівнем доказовості та кількістю зірок; рейтинг перераховується під час кожного оновлення. Це рейтинг, а не рекомендація; кожна добірка веде до повної картки нижче. Перевагу надано проєктам, які опублікували знімок екрана або запис, щоб добірка залишалася візуальною.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9493 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2548 · Python · 👁️ observed</sub>
<sub>Знайдіть токени-привиди. Виправте їх. Переживіть ущільнення. Уникайте погіршення якості контексту.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74489 · TypeScript · 👁️ observed</sub>
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
- [Офіційні: власні репозиторії та примітки до випусків Anthropic](#офіційні-власні-репозиторії-та-примітки-до-випусків-anthropic) — **14**
- [Моди: створені за допомогою можливості модифікації](#моди-створені-за-допомогою-можливості-модифікації) — **371**
- [Екосистеми плагінів DSH і Cordis](#екосистеми-плагінів-dsh-і-cordis) — **98**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150543 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Опис

Claude Code — це агентний інструмент для програмування, що працює в терміналі, розуміє вашу кодову базу й допомагає програмувати швидше, виконуючи рутинні завдання, пояснюючи складний код і керуючи робочими процесами git — усе за допомогою команд природною мовою.

<sub>🔧 Знайдено використання в коді: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | TypeScript                                                       |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **150543** |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9493 · TypeScript · ✅ official · 3 天</summary>

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
| Зірки                   | **9493**   |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8261 · Python · ✅ official · 3 天</summary>

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
| Зірки                   | **8261**   |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6361 · Python · ✅ official · 243 天</summary>

##### 📝 Опис

Огляд безпеки на основі ШІ GitHub Action із використанням Claude для аналізу змін у коді на вразливості безпеки.

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | Python                                                           |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **6361**   |
| Останній push           | 2026-02-11 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1804 · Shell · ✅ official · 3 天</summary>

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
| Зірки                   | **1804**   |
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

##### 📝 Опис

Додаткові матеріали для карток моделей Claude

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
| Вперше додано до списку | 2026-10-11 |

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
<summary><b>Більше в цій категорії</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Додано `$.ui.notify` для модифікацій: створює нативне сповіщення через власне…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Виправлено завершення безголових сеансів, очищення введеного промпту або…

</details>

<a id="mods"></a>

## Моди: створені за допомогою можливості модифікації

Кожен запис тут містить докази використання можливості, яку Claude Code отримав у версії 2.1.287: він виводить дані через `ui.render`, має власну панель, смугу або картку, читає `$.ui.selection()`, запускає колег за допомогою `agent.spawn` або прямо називає себе модом.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2548 · Python · 👁️ observed · 0 天</summary>

##### 📝 Опис

Знайдіть токени-привиди. Виправте їх. Переживіть ущільнення. Уникайте погіршення якості контексту.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | Python                                                                    |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **2548**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>анімований запис</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐548 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Спільнотний каталог загальнодоступних модифікацій Claude Code (функціональних hooks), просканованих із GitHub, із зазначенням того, що кожна модифікація може читати, записувати, запускати або надсилати мережею. Переглянути https://mods.aidojo.si/

<sub>🔧 Знайдено використання в коді: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **548**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐339 · Python · 👁️ observed · 0 天</summary>

##### 📝 Опис

macOS menu bar & Windows tray app pinning Claude Code, Codex, Antigravity & Grok CLI quota, burn rate, and cost to your screen. Local-first, no LLM API calls. HTML reports, 14 themes.

<sub>🔧 Знайдено використання в коді: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | Python                                                                    |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **339**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐221 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Модифікації Claude Code: плагіни на основі хуків, які додають динамічні рядки над запитом, захисти, панелі та ігри. Панель контексту, вимірювач використання, відстеження перевірок Codex, попередній перегляд Markdown, поточне відтворення Spotify та багато іншого.

<sub>🔧 Знайдено використання в коді: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **221**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐166 · TypeScript · 👁️ observed · 9 天</summary>

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
| Зірки                   | **166**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐164 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Claude Code показує зображення та відтворює відео безпосередньо у вашому терміналі: знімки екрана, записи Playwright і синхронізоване QA до та після. Ghostty і kitty.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **164**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐128 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Скіни для Claude Code: рядки інструментів з піктограмами, картки diff, таблиць і діаграм Mermaid, панель використання та п’ятнадцять тем. /skin змінює їх у реальному часі.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **128**    |
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Барвисті відповіді Claude Code із підтримкою тем: таблиці, код, діаграми, графіки та рядки інструментів у 15 темах із кнопками копіювання. Мод Claude Code.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **96**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 4 天</summary>

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
| Зірки                   | **79**     |
| Останній push           | 2026-10-08 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐77 · TypeScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **77**     |
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

##### 📝 Опис

Модифікації Claude Code від Darrell Wang — смуги над запитом, нуль токенів моделі. Панель тайванських／американських акцій + інші функції в майбутньому.

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
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 6 天</summary>

##### 📝 Опис

Експертні Skills, агенти, команди, правила, хуки та стилі виведення для Claude Code — безперервність сеансів + сучасні інструменти CLI для реальних робочих процесів розробки

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
| Зірки                   | **62**     |
| Останній push           | 2026-10-07 |
| Вперше додано до списку | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐49 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Опис

Модифікації Claude Code: динамічні індикатори прогресу плану над запитом

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **49**     |
| Останній push           | 2026-10-08 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>анімований запис · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Відкрити відео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arjun0014/project-sentinel">Arjun0014/project-sentinel</a></b> · ⭐47 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Центр керування тривалими запусками Claude Code: контекст і перебіг запуску з першого погляду, передавання Autopilot, захисні обмеження та спокійний перегляд активності в терміналі й Claude Desktop.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **47**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-agents-automation` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arjun0014--project-sentinel/cd63c979e03573e7.png" width="100%" alt="Arjun0014/project-sentinel screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐29 · TypeScript · 👁️ observed · 10 天</summary>

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
| Зірки                   | **29**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐28 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Оновлений вигляд Claude Code: панель керування в реальному часі, теми, якими можна ділитися, і піксельний улюбленець, який показує, що робить Claude

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **28**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Піксельний Pokémon, який живе над запитом у Claude Code

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **25**     |
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>анімований запис</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Опис

Збирання, тести, консоль і попередній перегляд SwiftUI з Xcode усередині Claude Code

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
| Вперше додано до списку | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Опис

Модифікації Claude Code: 21 стиль і повний набір функцій, які можна вмикати за потреби, для термінала й настільного застосунку. · Одним натисканням додайте Claude новий стиль і отримайте повний набір функцій, які можна вмикати за потреби.

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
| Вперше додано до списку | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 Опис

Десять модифікацій Claude Code, посібники для початківців, підказки для створення, безпечні демонстрації та шаблон для власної збірки.

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
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐18 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Claude Code mod: Clawd розігрує те, що робить Claude, над prompt

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **18**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Опис

Дві модифікації Claude Code: міст Codex computer-use і скоординовані сеанси Claude. Вихідний код, підказки для збірки, налаштування й тести.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **16**     |
| Останній push           | 2026-10-05 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Опис

Модифікації Claude Code: usage-band показує ваші обмеження 5h/7d, контекстне вікно та коефіцієнт влучань у кеш над запитом

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **13**     |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

##### 📝 Опис

Десять модифікацій з відкритим кодом для Claude Code: динамічні панелі, смуги, statusline та захисти викликів інструментів. Burn meter, launch codes, session wrapped, boss fight, code pet та багато іншого.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **13**     |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Опис

Модифікації Claude Code, які роблять запитання Claude легшими для читання й відповідей (qa-guide).

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
| Останній push           | 2026-10-07 |
| Вперше додано до списку | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>анімований запис · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Відкрити відео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **12**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

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
| Зірки                   | **9**      |
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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Інтерфейс для ваших терміналів Claude Code і Codex, який створюють ваші агенти, тож єдина модель у вашій голові — ваша.

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
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Опис

KOZMOS — інтерактивні візуальні моди для Claude Code (CLI + робочий стіл): смуги над полем запиту, бічні панелі, рядок стану, компаньйони, захисники та звук.

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
| Вперше додано до списку | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

LINE усередині Claude Code: TUI enil як мод Claude Code

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
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Опис

Зробіть тариф Claude Pro довговічнішим: моди Claude Code для точного HUD використання, коротшого виводу оболонки та відсутності повторного читання файлів. Моди не витрачають токенів.

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
| Останній push           | 2026-10-09 |
| Вперше додано до списку | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Опис

Шість модів Claude Code в одному плагіні (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) з окремими перемикачами для кожного моду, а також звіт про моди й хуки.

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
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary><b>Більше в цій категорії</b> <sub>· 337</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Колекція з понад 100 модифікацій, які можна використовувати з Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Модифікації Claude і інструменти для їх створення: спочатку навичка створення…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Модифікації Claude Code від Ray Amjad: панелі, смуги, захист запитів, робота із…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Середовище Claude Code, яке я використовую щодня, опубліковане під цією назвою…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Змініть дах Claude Code за допомогою Claude Mods: без зміни бінарного файлу…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Чотири модифікації Claude Code: Cache Keeper, Recording Mode, Goal Meter і…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Модифікації Claude Code від Learning Hacker: перетворюють роботу агента на…
- [kakha13/claude](https://github.com/kakha13/claude) - Модифікації Claude Code, які виправляють і перекладають ваші підказки перед…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - База знань Obsidian із джерелами про Claude Code mods: як вони працюють, як їх…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods і навички від Nekyia Labs, створені та щодня використовувані…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Вигляд desktop-app для стенограми термінала Claude Code як mod.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: меню інструментів Claude, режим Zen, теми термінала…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Бічна панель Claude Desktop (вкладка Code): перелічує незавершені та поточні…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Смуга використання над полем введення Claude Desktop (вкладка Code): ліміти 5h…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Бічна панель для Claude Code: субагенти, яких запускає сеанс, що робить кожен…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Навичка, яка навчає агентів Claude Code створювати Claude Mods.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Модифікації, плагіни та навички Claude від спільноти, які можна встановити з…
- [davekiss/mods](https://github.com/davekiss/mods) - Моди Claude Code від Dave Kiss.
- [devbrother2024/devbrothers-mods](https://github.com/devbrother2024/devbrothers-mods) - Добірка Claude Code mods від 개발동생. Пакет таксі: лічильник, навігація, камери…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (плагіни з функціональними хуками) для Claude Code.
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Ваш план, який стежить сам за собою. Локальне дерево дорожньої карти для…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Галерея модів Baselane: Claude Code mods, перевірені та закріплені.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Черга рішень CLI/TUI для людей, які працюють із розмовними агентами.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Модифікація панелі IDE Claude Code: дошка агентів, дерево файлів і переглядач…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Модифікація Claude Code, яка відображає відмінності Edit і Write у двох…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, який відображається в полі запиту Claude Code під час введення.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: панель використання 像素螃蟹 usage-hud + HTML-посилання, на які…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плаваюча картка стану для Claude Code — модель, контекст, обмеження швидкості…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Моди для Claude Code: плагіни function-hook, що додають динамічні панелі та…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Універсальний плагін Claude Code. Спілкуйтеся зі своєю командою, діліться кодом…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Тест набору тексту на час, поки працює Claude. Мод Claude Code.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard приховує імена та секрети під час демонстрації…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Модифікації та оболонки для Claude Code: індикатор перебігу завдань Claude у…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Розширення Claude Code. Розкрийте повну потужність Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Мод Claude Code (плагін), що додає бічну панель із вкладками Activity, Files…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Панелі, захисні механізми та моди для зручності роботи з Claude Code: контекст…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Два моди Claude Code над полем запиту: індикатор контекстного вікна, 5-годинний…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Читає markdown-файли, назви яким дає Claude Code, відображає їх поруч із…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Мод Claude Code: мініатюри вставлених зображень над полем запиту в будь-якому…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Голосовий напарник для Claude Code. Обговорюйте питання з 3D-вовком на основі…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow для Claude Code: спокійний список завдань над полем запиту, що…
- [BatuhanCakmakk/wavy-usage](https://github.com/BatuhanCakmakk/wavy-usage) - Кільця використання, заповнені рідиною, над промптом Claude Code: ліміти 5…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: панель контексту, панель агентів, розмиття PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, індикатор швидкості набору в реальному часі зі…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Феєрверки для Claude Code: кожне натискання клавіші, виклик інструмента, коміт…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Моди для Claude Code: панелі, команди та хуки, створені за допомогою плагіна…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Відкривайте Claude Code mods, плагіни та розширення з анімованими…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Мод Claude Code: діаграми mermaid, намальовані безпосередньо в стенограмі.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Невеликі моди Claude Code (плагіни function-hook): session-switcher та інші.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Магазин модів для Claude Code усередині Claude Code: введіть /mods, щоб…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Шість модифікацій Claude Code: обмеження плану й контекст над полем запиту…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout (пошук модів, якими ви користувалися б найчастіше)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Два моди Claude Code для одночасного запуску багатьох сеансів: картка контексту…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Модифікації Claude Code на вимогу — навичка, яка читає вашу розмову й створює…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: знаходження, перевірка, перемикання та оновлення модів Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Найкращі Claude Code Mods: відібрані вручну, перевірені, закріплені.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Плагін Claude Code: автоматична маршрутизація моделей Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Модифікація Claude Code: жива панель GitHub PR, які відкриває або надсилає…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Шість модів для Claude Code: анімований маскот Clawd, панелі ліміту…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Маркетплейс модів для Claude Code: покроковий налагоджувач циклу агента…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Моди з відкритим кодом для Claude Code: панелі, рядки стану, сповіщення, захист…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Найкращий універсальний набір модифікацій для Claude Code: ліміти використання…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Дивіться YouTube Shorts у Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набір інструментів Claude від Naren: навички, модифікації та MCP servers для…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Моди для Claude Code: Clawd, крихітний піксельний талісман, який відтворює дії…
- [reporails/arcade](https://github.com/reporails/arcade) - Класичні настільні ігри як моди Claude Code, у які можна грати на панелі, поки…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods для claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Власний marketplace плагінів модів для Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Добірний список модів для Claude Code, які можна встановити як маркетплейс…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Два моди Claude Code: cache-keeper і ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Моди Claude Code, які допомагають агенту бути чесним — функціональні хуки, що…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Щойно з фабрики. Модифікація Claude Code: попросіть мем і продовжуйте…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Мод для Claude Code: панель кешу prompt, наступні кроки, кнопки швидких дій і…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Мод Claude Code, який відображає ваші ліміти використання та витрати в смузі…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Мод Claude Code для фіксації думок посеред роботи, їхнього сортування між…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Статус PR GitHub у реальному часі, готовність до злиття, перевірки, коментарі…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Вирощуйте чайне яйце, яке повільно просочується смаком, поки ви пишете код ·…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моди Herman для Claude Code (marketplace herman-mods).
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Переглядайте, що Claude Code виконує у фоновому режимі: субагенти, завдання…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Модифікація Claude Code: відповідайте на запитання Claude по черзі…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Польові нотатки першого дня про моди Claude Code на Windows: індикатор палива…
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Мод Claude Code: динамічний статус запиту на злиття GitHub.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живі лічильники вартості, контексту й квоти плану над запитом.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin і mod: AI-native SDLC.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Модифікація Claude Code, яка вмикає або вимикає ваші глобальні навички, агенти…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Перевірені моди Claude Code, що встановлюються однією командою: захисні…
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Добірка модів для claude code, створених мною.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Модифікації Claude Code. touch-map: переглядайте, які файли Claude перелічив…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Вивчайте іноземну мову під час роботи з Claude Code.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Скажіть Claude, чого ви хочете. Отримайте це зібраним, протестованим, reviewed…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Супроводжує тривалий сеанс Claude Code замість вас: стежить за заповненням…
- [Akeuuh/claude-mods](https://github.com/Akeuuh/claude-mods) - Маркетплейс плагінів Claude Code: модифікації на основі функціональних хуків.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Бічна панель із поточними витратами, токенами та використанням контексту для…
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Моди з функціональними хуками для Claude Code: рядок телеметрії лімітів, панелі…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Мод Claude Code, який підтримує поточний список відкритих питань у розмові та…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моди Claude Code для справжніх інженерів.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Підсумок термінальної сесії Claude Code у вкладці Code настільного застосунку…
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Мод Claude Code: переглядайте, які навички, плагіни, субагенти та інструменти…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Дивіться, які файли кожен агент Claude Code має у своєму контексті та яку…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Невеликі моди Claude Code для термінала й настільного застосунку.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навичка + мод Claude CLI, що додає іспанські слова у відповіді агента.
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Мод Claude Code — припиніть марнувати токени: /keepwarm.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Події Alarum над prompt Claude Code: що щойно надійшло, і передача цього агенту…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Ваш список завдань Floatee над підказкою Claude Code: запускайте, спрямовуйте…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Мод Claude Code, який стилізує його під The Machine з Person of Interest.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: модифікація Claude Code для обов.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Мод Claude Code: стан сеансу, живий прогрес Spec Kit і керування usage-window.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Вікно контексту як один рядок над запитом, відтворений так, як Claude Code…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Мод коду Claude: вибирає модель і рівень зусиль для міркування кожного субагента.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: графік у реальному часі того, що знає Claude Code.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Поточний HUD завдань для Claude Code Desktop: смуга над промптом під час роботи…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Плагін (мод) Claude Code, який робить термінальний інтерфейс Claude Code схожим…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Не дозволяйте своїй увазі блукати, поки чекаєте на відповідь Claude Code.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Безкоштовний плагін із відкритим кодом для Claude Code.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Черга промптів для Claude Code у вигляді моду: /after &lt;task&gt; запускає завдання…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Моди Claude Code: відібрані, протестовані, і кожен мод містить промпт, на…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навички Claude Code: перевірка фактів у документації, аудит коду, журнал…
- [partalemre/MODZ](https://github.com/partalemre/MODZ) - 17 плагінів Claude Code на одній панелі.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Мод Claude Code: клікабельні шляхи у відповідях — натисніть папку, щоб відкрити…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагін-компаньйон для Claude Code: ASCII-компаньйон над запитом, який памʼятає…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Добірка чудових модів Claude Code | 모음집 модів Клод Код.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Він говорить: модифікація Claude Code, яка за запитом уголос читає відповіді…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Відшмагайте Claude, коли він помиляється — модифікація для зняття стресу в…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Модифікації Claude Code: невеликі плагіни для живих панелей, маршрутизації…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code із підтвердженнями. Плагін, який планує, делегує та доводить…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Модифікація Claude Code: квота 5h/7d, вікно контексту, час до завершення кешу…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Модифікація та плагін Claude Code: монітор використання, відстеження токенів…
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Модифікації Claude Code: EMCC (Every Mod Claude Code), відібрана й протестована…
- [adithepmeekhun/self-clear](https://github.com/adithepmeekhun/self-clear) - Модифікація Claude Code, яка підтримує тривалі запуски агентів: при вибраному…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анімований брайлівський кіт над запитом Claude Code.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Піксельний кіт над запитом Claude Code, який запускає тестовий виклик…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, який обирає вдалий момент для ущільнення, щоб зберегти…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модифікації Claude для Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Універсальні моди для Claude Code: bands, панелі, сповіщення та хуки.
- [aott33/model-router](https://github.com/aott33/model-router) - Модифікація Claude Code, яка вибирає модель для кожного субагента перед його…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Мод Claude Code: вікно вашого контексту в одному спокійному рядку, сірому, доки…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Корабель LGTM Lines пропливає повз після кожної зміни коду — мод Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Ваші ліміти використання Claude у вигляді анімованої картки здоров.
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Моди Claude Code для команди S2 (ринок ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткі тренування, поки Claude працює: щоденна ціль, серії, значки та…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Дошка використання для Claude Code: витрати за моделлю.
- [bahaospanov/skills](https://github.com/bahaospanov/skills) - Модифікації Claude Code від Bakhtiyar Ospanov: плагіни, побудовані на…
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Модифікація Claude Code, яка показує, чим зайняті ваші субагенти: індикатор…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Модифікація Claude Code, яка показує, скільки часу тривала кожна відповідь, у…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Модифікація Now Playing для Claude Code: Apple Music і Spotify над запитом, з…
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - Вкладка Performance для Claude Code перетворює кожен запит до моделі та виклик…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Модифікації для Claude Code: Cache-Uhr, Blast Radius, Vorschlaege…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашого Claude Code.
- [cerebrai/ironman-mod](https://github.com/cerebrai/ironman-mod) - Модифікація claude code для робочого процесу, доповненого людським ШІ, — як у…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Тримайте Claude Code на plan: stages, approval gates і file budget, enforced by…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Тамагочі, що живе всередині Claude Code: він вилуплюється, їсть код, який пише…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Вибране для Claude Code: піктограми команд і навичок одним натисканням.
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Моди для Claude Code (плагіни для перехоплення функцій): session-meter та інші.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: одна маленька кнопка, яка приховує всі модифікації Claude…
- [finalpantasy/claude-mod-pack](https://github.com/finalpantasy/claude-mod-pack) - Пакет модів Claude: невеликі моди Claude Code.
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Мод Claude Code: заморозьте сесію та відновіть її пізніше так, ніби нічого не…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+клацання копіює посилання на кожен блок коду у відповідях Claude Code…
- [guojunjie0614-cyber/workhorse](https://github.com/guojunjie0614-cyber/workhorse) - Модифікація Claude Code: передавайте завдання з написання коду, перевірки та…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Індикатор поточних витрат для Claude Code: вартість сесії із субагентами та…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Мод Claude Code: скільки часу тривала кожна відповідь, скільки думав Claude і…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Панель керування над вашим полем запиту Claude Code. Качка читає показники.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Автоматично читає креслення вашого проєкту, а потім моделює його в SolidWorks.
- [jBeyondstars/ultracode-models](https://github.com/jBeyondstars/ultracode-models) - Модифікація Claude Code: вибирайте модель і рівень зусиль, на яких працює кожен…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - Жива дошка субагентів Claude Code усередині VS Code: субагенти кожної розмови…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Бічна панель із використанням контексту: загальний обсяг, категорії, зростання…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Бічна панель зі списком файлів: які файли створено, змінено або видалено в цій…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пухнастик у стилі 8-bit (чорно-білий голландський висловухий кролик) бігає та…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Бічна панель «Мої запитання»: кожне речення, яке власник вводив у цій розмові;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Бічна панель із часовою шкалою: на що витрачено час у цьому раунді.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Бічна панель обміну токенами: скільки токенів головна розмова щоразу надсилає…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Чесна коробочка для claude code: після кожної відповіді Claude тихо каже одну…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI спрощеною китайською (самокерована версія) — власна таблиця…
- [jidhra/claude-mods](https://github.com/jidhra/claude-mods) - Модифікації Claude Code від Jidhra на одному маркетплейсі плагінів.
- [kadaliao/claude-mods](https://github.com/kadaliao/claude-mods) - Модифікації Claude Code: плагіни функціональних хуків, які змінюють власний…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живе в смузі над вашим prompt Claude Code: розігрує сесію, показує, що…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод для озвучення відповідей і сповіщень Claude Code за допомогою VOICEVOX /…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Моди для Claude Code. PixBar: піксельна істота над вашим запитом, яка рухається…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Мод Claude Code: кожна сесія Claude Code в одному плаваючому вікні, з живими…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Невеликі модифікації Claude Code в одному маркетплейсі плагінів.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Посібник зіставлених спільнотою модів Claude Code: варіанти використання…
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Модифікація Claude Code: ліміти вашого плану (сесія 5h, тиждень) і поновлення…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод для Claude Code, який показує, що робить Claude, у підзаголовку вкладки…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy — неофіційний піксельний супутник, створений фанатами, який розташований…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Пухнастий чорний кіт над вашим промптом Claude Code.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Невеликі моди для Claude Code: runner-avatar, маленький аватар, що бігає над…
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Модифікація Claude Code: панель у реальному часі, що показує, чого прагне ваш…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Мод Claude Code: панель /sessions для перегляду й видалення сеансів разом із…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Модифікації спільноти для Claude Code: засоби захисту, панелі та команди, що…
- [mkiselyow/diff-lens](https://github.com/mkiselyow/diff-lens) - Мод Claude Code: попросіть Claude провести вас через PR, натисніть будь-яке…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Мод коду Claude: Codex (підписка ChatGPT) та інші моделі не-Anthropic як моделі…
- [MohamedHamed001/claude-mods](https://github.com/MohamedHamed001/claude-mods) - Плагіни Claude Code: делегування.
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Мод коду Claude: називає вкладку термінала, у якій працює Claude.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, який знову вмикає інструменти todo для моделей, що їх не…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Мод Claude Code, який чекає на безпечну паузу, а потім передає вашу сесію або…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одному рядку для кожного завдання над запитом із поточним…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Грайте в Connect Four проти AI всередині Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Модифікація Claude Code: коли інший агент програмування робить коміт у ваш…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Модифікація Claude Code для репозиторіїв, спільних для кількох AI-агентів: не…
- [niksavis/handily](https://github.com/niksavis/handily) - Модифікації Claude Code, що показують ваші робочі елементи, завдання та сеанси…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Захисний бар.
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Панель блокнота для Claude Code як мод.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Одна модифікація для Claude Code, із пріоритетом Windows і CJK: попередній…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Найкращі моди Claude Code, упорядковані за тим, що вони роблять для вас.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Два моди Claude для Claude Code: garde-du-corps.
- [partalemre/transceiver](https://github.com/partalemre/transceiver) - Плагін Claude Code (бета): командний чат усередині Claude Code.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: мод коду Claude. Постійні робочі дерева з початковим режимом лише…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Бічна панель поточної статистики сесії для вкладки Code настільного застосунку…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod: відтискання, які треба робити, поки працює Claude. Без токенів.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: практичний посібник із модів коду Claude — від ELI5 до розробки…
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Відкритий маркетплейс модів Claude Code, із навичками репозиторію для внесків і…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Модифікація Claude Code: перетворює план, який ви схвалюєте в режимі…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Ретельно відібраний список модів Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Безкоштовний режим: допоміжні агенти працюють на Haiku, а великі файли й…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музичний супровід у стилі lofi, що супроводжує сесію: спокій, зосередженість…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Навчайтеся, поки Claude пише код: після ходу, який змінив код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запис кожної зміни, яку вносить Claude: відтворюйте кожну зміну, спостерігаючи…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Моди Showrin для Claude Code для продуктивнішої щоденної роботи.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Мод коду Claude: ліміти контексту й плану з прогнозом швидкості витрачання, а…
- [sohi2212/claude-agent-radar](https://github.com/sohi2212/claude-agent-radar) - Модифікація Claude Code: живий радар фонових агентів + полотно плану в стилі…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Мод коду Claude, який підтримує роботу сеансів без нагляду через ліміти…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Маркетплейс користувацьких модифікацій Claude Code (cc-mods) із вбудованими…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Повідомлення комітів одним кліком для Claude Code з танцюючою піксель-арт…
- [SummerRiversound/review-inbox](https://github.com/SummerRiversound/review-inbox) - Модифікація Claude Code: PR, що очікують на вашу перевірку, кожен із підсумком…
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Моди для Claude Code. cache-meter: коефіцієнт влучань у кеш запитів, заповнення…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — мод Claude Code, який показує використання вашого плану Claude…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Неофіційні модифікації Claude Code від tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, що показує поточний сеанс в окремій області: кожен запит…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Маркетплейс плагінів Claude Code із модами: плагіни function-hooks, що малюють…
- [thunini/thinking-flow](https://github.com/thunini/thinking-flow) - Модифікація Claude Code, яка показує, як Claude дійшов кожної відповіді: ваше…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Слухайте відповіді Claude Code, поки речення, яке читається, підсвічується.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Мод коду Claude: одна кнопка під останньою відповіддю Claude копіює кожну…
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - Режим CC, який показує, у який обліковий запис, організацію та план Claude ви…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анімована смуга поступу та підсумок завершення для тривалих…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Три невеликі моди для Claude Code: переглядайте, коли ваші субагенти завершать…
- [varunmoka7/disk-sweep](https://github.com/varunmoka7/disk-sweep) - Попереджає, коли на вашому Mac мало місця на диску, а за допомогою /disk…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажіть &quot;I.
- [varunmoka7/park](https://github.com/varunmoka7/park) - Збережіть цей сеанс Claude Code і напишіть нотатку для наступного.
- [varunmoka7/read-fence](https://github.com/varunmoka7/read-fence) - Не дає Claude відкривати ваші теки навичок, правил і плагінів файл за файлом…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Поставте Claude додаткове запитання в панелі поруч із вашою роботою.
- [varunmoka7/skills-az](https://github.com/varunmoka7/skills-az) - Показує список ваших слеш-команд і навичок у алфавітному порядку, щойно ви…
- [varunmoka7/unattended](https://github.com/varunmoka7/unattended) - Не дає сеансу Claude Code ставити вам запитання, коли за клавіатурою нікого…
- [vcdim/claude-code-sciplot](https://github.com/vcdim/claude-code-sciplot) - Модифікація Claude Code для наукових графіків: Python, R, TikZ, MATLAB і…
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Плагін Claude Code: зворотний відлік кешу промптів, частота влучань у кеш…
- [wonwoo/tool-timeline](https://github.com/wonwoo/tool-timeline) - Модифікація Claude Code, яка показує, на що пішов час кожного кроку: рядок під…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Плагін Claude Code: ваші ліміти використання Claude Pro/Max із прогнозом…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моди для Claude Code. agent-crew: спостерігайте за роботою ваших субагентів як…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Ретельно підібрана колекція найкращих ресурсів для найкрутіших агентів, Claude…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Плагін Claude Code, який показує, що відбувається: використання контексту…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Красивий, надзвичайно налаштовуваний рядок стану для Claude Code CLI із…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Усі частини системного запиту Claude Code, 27 описів вбудованих інструментів…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Навичка створення відео зі штучним інтелектом для Claude Code і Codex…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Понад 45 порад, як отримати максимум від Claude Code — від основ до складних…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — створюйте каруселі Xiaohongshu і пари обкладинок…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Переглядайте diff вашого агента кодування в панелі термінала й надсилайте…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Комплексний плагін рядка стану для Claude Code із використанням контексту…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Створюйте модифікації для Claude Code: перехоплюйте будь-який запит, змінюйте…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Комплексна панель статусу для Claude Code — інформація про сеанс, індикатори…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: відстеження вуглецевого сліду ваших сеансів Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Естетична statusline для Claude Code від awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Загальнодоступні Skills і модифікації Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, модифікації, субагенти, хуки, slash-команди та посібники для Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Юридично безкоштовні LLM APIs і coding agents — самостійно оновлюються, двічі…
- [aiedwardyi/claude-usage-monitor](https://github.com/aiedwardyi/claude-usage-monitor) - Плагін рядка стану Claude Code для відображення квоти на 5 годин/7 днів…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live-рахунки футбольних матчів, календарі та турнірні таблиці для змагання…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, який перетворює вашого агента програмування на експерта з прошивок…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Час молитви, дата за календарем Хіджри, азкари, щоденний аят, піст за сунною…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Персональна конфігурація Claude Code з версіюванням у ~/.claude — агенти…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Набір плагінів для Claude Code, pi та DeepSeek Harness: HUD у рядку стану…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Портативний набір інструментів Claude Code для .NET DDD/Clean Architecture…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Переносна глобальна конфігурація Claude Code: власні навички, хуки PreToolUse і…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Неофіційні моди для вкладки Code у Claude Desktop — usage-pet: смуга…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагіни Claude Code, якими я користуюся щодня: навички та моди, очищені так…
- [vtmocanu/cc-statusline](https://github.com/vtmocanu/cc-statusline) - Дворядковий рядок стану ANSI для Claude Code: контекст git + k8s, індикатори…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Аналізуйте використання tokens і витрати Claude Code з локальних conversation…
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Гарний інформативний status line для Claude Code.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Візуальна дошка для ваших агентів Claude Code: переглядайте сесії, субагентів і…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Налаштовуваний status line для Claude Code з редактором перетягуванням.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Маркетплейс плагінів і навичок Claude Code для створення модів гри Hytale.
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Однорядковий статусний рядок із кольоровим кодуванням для Claude Code — папка…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Переглядач із розділеною панеллю для Claude Code у терміналі Windows та tmux…
- [ian-exnodes/statusbar](https://github.com/ian-exnodes/statusbar) - Плагін Claude Code: поточний дворядковий рядок стану під підказкою з моделлю…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Рядок стану поточної фази робочого процесу для Claude Code.
- [mvrozanti/claude-progressbar](https://github.com/mvrozanti/claude-progressbar) - Смуги поступу для команд Bash, які виконує Claude Code, намальовані в його…
- [naturalmoods/herdr-telegram-notify](https://github.com/naturalmoods/herdr-telegram-notify) - Надсилає вам повідомлення в Telegram, коли агент завершує роботу або потребує…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Мікродашборд із 3 рядків для термінала Claude Code — модель, витрачання…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Репозиторій модів Awesome Media для Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Скорочуйте витрати Claude Code і Codex токенів: спрямовуйте пошук і тестові…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Швидкий, налаштовуваний статусний рядок для Claude Code — один статичний…
- [barkleesanders/claude-hud](https://github.com/barkleesanders/claude-hud) - Інформаційна панель у реальному часі для Claude Code — стан контексту…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Посилений статусний рядок із градуйованими кольорами та без залежностей для…
- [ist-j-ichikawa/claude-code-statusline](https://github.com/ist-j-ichikawa/claude-code-statusline) - Користувацький рядок стану j-ichikawa для Claude Code CLI.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Показує ключові відомості про стан Claude Code, зокрема модель, контекст…
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Компактний status line для Claude Code, який активно підтримується — модель…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Нативні команди агентів. Під контролем.
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Рядок стану PowerShell для Claude Code від Windows: 5-годинні та тижневі ліміти…
- [barnabys-drew/claude-code-statusline](https://github.com/barnabys-drew/claude-code-statusline) - statusLine Claude Code — смуги контексту й обмеження швидкості безпосередньо з…
- [black-astro/claude-statusline-astro](https://github.com/black-astro/claude-statusline-astro) - Рядок стану Claude Code — папка, гілка, модель і використання в одному рядку, а…
- [Chy-Zaber-Bin-Zahid/claude-code-statusline](https://github.com/Chy-Zaber-Bin-Zahid/claude-code-statusline) - Рядок стану Claude Code з контекстом і смугами використання за 5 годин та за…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Рядок стану Claude Code у Lua із Neovim-майданчиком у реальному часі.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Статусний рядок Claude Code професійного рівня: тривалість сеансу, вартість у…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - Плагіни Claude Code від divramod, один маркетплейс: навички агентів і панелі в…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Рядок стану для Claude Code: контекст, ліміти й темп тижня, CI, деплої та PR…
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - Розширення VS Code: прогрес завдання Claude Code, орієнтовний час завершення та…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Попередній перегляд зображень усередині Claude Code: наведіть курсор на чип під…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Рядок стану Claude Code: модель, смуги квот 5 годин/7 днів, смуга місячних…
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Синхронізуйте завдання Claude з Fizzy.do для видимості команди в реальному…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Показує докладну кольорову панель стану для Claude Code з інформацією про…
- [KitchenSink4AI/claude-code-statusline](https://github.com/KitchenSink4AI/claude-code-statusline) - Індикатор контексту для Claude Code: фактична швидкість витрачання, кількість…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Дворядковий рядок стану для термінального агента кодування: каталог, git, PR…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Хук рядка стану Claude Code — відстежує використання токенів і контекст між…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Рядок стану Claude Code зі встановлювачем для Linux і Git Bash на Windows.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — рядок стану Claude Code для macOS + Linux.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Відстежуйте стан Claude Code у рядку меню macOS за допомогою індикаторів у…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Користувацький рядок стану Claude Code.
- [sgarcia-dev/claude-agent-watch](https://github.com/sgarcia-dev/claude-agent-watch) - Поточна панель і рядок стану для субагентів Codex, OpenCode, Antigravity…
- [silee-tools/claude-statusline](https://github.com/silee-tools/claude-statusline) - Вертикально стекований HUD статусного рядка для Claude Code, незалежний від…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Портативна конфігурація Claude Code (рядок стану + інсталятор).
- [steemandavid/claude-code-statusline](https://github.com/steemandavid/claude-code-statusline) - Користувацький рядок стану для Claude Code — модель, контекст і статистика…
- [Synforger/claude-code-statusline](https://github.com/Synforger/claude-code-statusline) - Статусний рядок для Claude Code, який одразу показує обмеження частоти запитів…
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - 4-рядковий рядок стану для Claude Code.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Портативна конфігурація Claude Code: CLAUDE.md, settings, statusline, skills.
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Універсальний багатопротокольний StatusLine, контекст із самонавчанням і…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Відстежуйте використання контексту Claude Code, витрати сеансів і скидання…
- [wcampbell-dw/claude-plugins](https://github.com/wcampbell-dw/claude-plugins) - Плагіни Claude Code: індикатори активності субагентів у реальному часі, рядок…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Синхронізація користувацької конфігурації Claude Code між кількома машинами…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Детектор виснаження контексту 2026 — проактивна пам.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Хуки, субагенти та рядки стану Claude Code: колекції інструментів із відкритим…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Візуальний конструктор рядків стану Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Рядок стану Claude Code із показом використання токенів у реальному часі та…
- [lexfrei/ailine](https://github.com/lexfrei/ailine) - Рядок стану Claude Code із реальними лімітами використання від Anthropic API.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Моди для Claude Code: панелі, смуги та компаньйони на основі функціональних…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Передавайте завдання між сеансами Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Це сервер MCP для керування MODS — модульним кросплатформним інструментом для…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: знаходьте те, про що ви знову й знову просите Claude Code, і…
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Бібліотека з 3 навичок для Claude Code: session-handoff, session-statusline і…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Навичка Codex і Claude Code для перекладу модів CK3 за допомогою локального LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Моди з відкритим кодом та інші розширення для Claude Code.

</details>

<a id="dsh-cordis"></a>

## Екосистеми плагінів DSH і Cordis

DeepSeek Harness і Cordis досягають того самого результату іншим шляхом: для них плагін є механізмом модів, тож плагін там — еквівалент мода тут.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74489 · TypeScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **74489**  |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐184903 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **184903** |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100875 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **100875** |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82831 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **82831**  |
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35774 · Go · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **35774**  |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30656 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Сучасне настільне рішення для екосистеми плагінів DeepSeek Harness (DSH). Усе є «плагіном», і сам робочий стіл також є «плагіном».

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **30656**  |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25562 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Distilly — перетворюйте спосіб їхнього мислення на багаторазово використовувані Skills для будь-якого Agent або Bot. Раніше Colleague Skill（原同事 Skill）.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Python                                                                          |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **25562**  |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9157 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **9157**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8691 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **8691**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4532 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Офіційно рекомендований TUI-плагін DSH — висока продуктивність, низьке навантаження, милий піксельний кит, плавна взаємодія мишею. Встановлення однією командою через npm. / Офіційно рекомендований TUI-плагін DSH — висока продуктивність, низьке навантаження, милий піксельний кит, плавна взаємодія мишею, встановлення однією командою через npm

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **4532**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3684 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Перший у світі віртуальний термінал для AI-агентів

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **3684**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3422 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Локальний приватний кросплатформний AI-агент із відкритим кодом для саморозвитку та пошуку контенту: спочатку розуміє вас, а потім активно шукає контент на Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo та у відкритому вебі (підтримує плагін deepseek harness) | Локальний кросплатформний AI-агент із відкритим кодом для пошуку контенту: розуміє вас, а потім активно шукає контент на Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo та у відкритому вебі (підтримує плагін deepseek harness)

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Python                                                                          |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **3422**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2064 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Найкращий плагін DeepSeek Harness для аналізу та керування контекстом, із панеллю контексту / браузером / бічною панеллю та командою контексту для статистики контексту, його складу, деталізації, еволюції, розуміння того, з чого складається контекст і як він змінюється. Універсальний плагін візуалізації контексту для DeepSeek Harness: панель Context, браузер і бічна панель, а також команда Context для перегляду складу, еволюції, стискання, обрізання та інших подій і дій із контекстом.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **2064**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1942 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Підключайте IM-ботів до DeepSeek Harness за допомогою QR-коду або облікових даних (підтримуються 飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord і WhatsApp). Підключайте IM-ботів до DeepSeek Harness за допомогою QR-коду або облікових даних (9 каналів).

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1942**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1185 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Пам’ять для Claude Code, Codex, Cursor та ще 38 агентів для програмування, створена з історії сеансів, яка вже зберігається на вашому диску. Локальний пошук, MCP і хуки, без LLM, один бінарний файл Go.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Go                                                                              |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1185**   |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/shengsheng90/DSH-taskboard">shengsheng90/DSH-taskboard</a></b> · ⭐334 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Нативний локальний плагін Taskboard для DeepSeek Harness. Проєкти на основі SQLite, призначення та перевірка агентами, нативний Web UI — без iframe і без другого середовища виконання чату.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **334**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `task-management` · `taskboard`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/shengsheng90--dsh-taskboard/641e63303f0eed9c.png" width="100%" alt="shengsheng90/DSH-taskboard screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐231 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Плагін DeepSeek Harness для зміни оболонки / шпалер / пакетів тем (dsh-plugin) — 8 тем Mirage, акцентний колір для кожного користувача, Wallpaper 2.0, імпорт, експорт і посилання для поширення пакетів тем, обране та випадковий вибір; реалізовано суто на нативній системі токенів.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **231**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐205 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Нативний плагін DeepSeek Harness, що інтегрує TypeSafe Jev або Decision api, як-от luna, як рівень прийняття рішень System One для вибору агентів, нагляду, виправлень і затверджень.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **205**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐186 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Плагін резервного копіювання та відновлення DeepSeek Harness (DSH) — експортуйте, імпортуйте, переносьте й синхронізуйте повну конфігурацію DSH, плагіни, сервери MCP, навички та робочий простір. Міграція на іншу машину одним натисканням.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **186**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐124 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Плагін настільного улюбленця DeepSeek Harness: енергійна дівчина-кит — персонаж на панелі, що супроводжує вас під час написання коду 🐋 Підтримує настільну версію DSH 0.2.0-rc.2 і стару версію Web (desktop pet / mascot, local-first)

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **124**    |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐89 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Skills і плагіни You.com для вебпошуку, вилучення вмісту, досліджень, фінансів і пошуку інтеграцій, що допомагають AI agents працювати з актуальним вебконтекстом.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **89**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-wsl-workspace-maintainers/dsh-wsl-workspace">dsh-wsl-workspace-maintainers/dsh-wsl-workspace</a></b> · ⭐80 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Підтримка робочих просторів WSL для DeepSeek Harness — безшовна робота з робочими просторами WSL без потреби встановлювати dsh у WSL. Після встановлення цього плагіна можна безпосередньо додати робочий простір WSL у GUI. Підтримка робочих просторів WSL для DeepSeek Harness — насолоджуйтеся безшовною роботою з робочими просторами WSL без потреби встановлювати dsh у WSL. Після встановлення цього плагіна можна безпосередньо додати робочий простір WSL через GUI.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **80**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-wsl-workspace-maintainers--dsh-wsl-workspace/252926072330fff2.png" width="100%" alt="dsh-wsl-workspace-maintainers/dsh-wsl-workspace screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Настільний Agent, створений на основі ядра Deepseek-Harness. Наслідує всі можливості основи та доповнює функції, пов’язані з IDE.

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
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **59**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Пошук контексту робочого простору та відстеження життєвого циклу з урахуванням завдання для AI Coding Agent: пошук, упорядкування й постійне відстеження найрелевантніших для поточного завдання документів, коду та медіа. Повністю локально, без викликів моделей і без мережі. Пошук контексту робочого простору та відстеження життєвого циклу з урахуванням завдання для AI coding agents. Знаходить, упорядковує та відстежує контекст робочого простору, найрелевантніший для поточного завдання — локально, детерміновано, без викликів моделей і без мережі.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **54**     |
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-plugin-guide">PerryLink/dsh-plugin-guide</a></b> · ⭐50 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

База знань із розробки плагінів DeepSeek Harness (dsh): посібник із розробки з 10 розділів, посібник із випуску, перевірені джерелами невиправлені проблеми upstream і виміряні дані екосистеми — встановлюється як пакет DSH.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **50**     |
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `ai-agents` · `checker` · `cli` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/d665a08f58e38532.png" width="100%" alt="PerryLink/dsh-plugin-guide screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/3aee78fb7bcfc697.gif" width="100%" alt="PerryLink/dsh-plugin-guide animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Плагін DeepSeek Harness: одним клацанням підбирає контекстне вікно моделі, показує джерело місткості, підтримує пакетне налаштування вибраних елементів, керування наявними вікнами та ручне редагування.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **34**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Навігація сеансами DSH

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **23**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HaoyueQin/dsh-usage-statistics-panel">HaoyueQin/dsh-usage-statistics-panel</a></b> · ⭐23 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Вебплагін DSH: щоденна статистика використання токенів із тепловою картою активності у стилі GitHub, кривою коефіцієнта потрапляння в кеш і розподілом за моделями

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **23**     |
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `data-visualization` · `deepseek-harness` · `dsh-plugin` · `llm` · `plugin` · `react` · `settings-panel`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/haoyueqin--dsh-usage-statistics-panel/e57757e1005cbc5b.png" width="100%" alt="HaoyueQin/dsh-usage-statistics-panel screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/pptwise">liustack/pptwise</a></b> · ⭐21 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **21**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skill` · `agent-skills` · `ai-agent` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deck-generation`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--pptwise/e6f193d6fc2ea355.png" width="100%" alt="liustack/pptwise screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KannaKuron/dsh-better-workspace">KannaKuron/dsh-better-workspace</a></b> · ⭐18 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Вебплагін DSH: ієрархічне дерево робочого простору для бічної панелі — заголовки, що містять /, об’єднуються у віртуальні папки; у процесі додавання робочого простору з’являється спливаюче вікно батьківської групи

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
| Останній push           | 2026-10-12 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `sidebar` · `tree` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kannakuron--dsh-better-workspace/83cddff440dfe49a.png" width="100%" alt="KannaKuron/dsh-better-workspace screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vecnode/vncode">vecnode/vncode</a></b> · ⭐8 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

vncode 🤖 Agent-Human IDE ⌨️ Веб- і настільні версії, що містять Plugins, Skills та Interfaces.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **8**      |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent-skills` · `deepseek-ai` · `deepseek-api` · `deepseek-chat` · `deepseek-harness` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vecnode--vncode/73837d3e9e3dc179.png" width="100%" alt="vecnode/vncode screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/unStone/dsh-xray">unStone/dsh-xray</a></b> · ⭐7 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Рентген для плагінів DeepSeek Harness: заявлені можливості проти фактичної поведінки. Реєстр + статичний сканер + значки.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Python                                                                          |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **7**      |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent-security` · `ai-agents` · `ai-security` · `capability-analysis` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unstone--dsh-xray/35167f8867e8b79d.png" width="100%" alt="unStone/dsh-xray screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/alone-tree/dsh-skill-mcp-manager">alone-tree/dsh-skill-mcp-manager</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Бібліотека можливостей (Capability) — універсальне візуальне керування DSH Skills і MCP: завантаження MCP за запитом, гаряче перезавантаження під час сеансу та перегляд описів SKILL/MCP у плагіні.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **6**      |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp` · `skill`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/alone-tree--dsh-skill-mcp-manager/bc0fce1b6eabef09.png" width="100%" alt="alone-tree/dsh-skill-mcp-manager screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary><b>Більше в цій категорії</b> <sub>· 64</sub></summary>

- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) - Відповідай мені за допомогою HTML — навичка агента, що відповідає на складні…
- [anywhere-labs/Agents-Anywhere](https://github.com/anywhere-labs/Agents-Anywhere) - Міжплатформний робочий простір Agent з відкритим кодом.
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Захист перед виконанням для AI coding agents.
- [LivXue/dsh-plugin-shop](https://github.com/LivXue/dsh-plugin-shop) - Найповніший ринок плагінів DeepSeek Harness — щоденне оновлення, джерела з…
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Добірний список найкращих чудових ШІ-плагінів для ШІ-асистентів, зокрема Claude…
- [Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet) - 📚 Бібліотека мікроуроків для AI-агентів без залежностей, на основі git, для…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Плагін DSH — безкоштовні моделі OpenCode Zen для DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Ринок плагінів DSH / DSH Plugin Marketplace: перегляд, встановлення та…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - Вбудована в DeepSeek інтерактивна оповідь 18+ із пробиванням броні: NPC із…
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - Постійно оновлювані статті з графіки, 3DGS і просторового інтелекту;
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - Після встановлення ви одразу отримуєте 27 інженерних навичок і навичок…
- [arcships/rutis](https://github.com/arcships/rutis) - Середовище виконання плагінів для програмного забезпечення, яке вдосконалює…
- [JingbiaoMei/Tokdash](https://github.com/JingbiaoMei/Tokdash) - Панель агента: візуалізація та аналітика сеансів і використання квоти.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Каталог вибраних плагінів DeepSeek Harness (DSH) — понад 280 плагінів спільноти…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Плагін DSH: оболонка Git Bash для всіх режимів агента на Windows.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: багатоплатформна система інтелектуальних агентів для групових чатів…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh для Android: інтеграція DeepSeek Harness, середовища виконання Ubuntu…
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion: розширює dsh-im концепцією помічників і домівок — одразу…
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Плагін DeepSeek Harness · оптимізація чернетки промпту одним натисканням у…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Плагіни, інструменти, навички й навчальні ресурси DeepSeek Harness (dsh)…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Середовище виконання переговорів у сфері A2A commerce + плагін DeepSeek Harness…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - AI сперечається. Код вирішує. Втрати залишаються на сторінці.
- [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) - Плагін пам.
- [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) - Плагін DeepSeek Harness: автоматично перетворює діалоги на картки знань, із…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Реєстр плагінів, пакетів і навичок DeepSeek Harness (dsh) із відкритими даними…
- [realguan/dsh-dock](https://github.com/realguan/dsh-dock) - Кросплатформний настільний центр керування, створений спеціально для DeepSeek…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - Плагін DSH: три інструменти — пошук на сайті, пошук за індексом усього вебу та…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Постійне тестування сумісності плагінів DeepSeek Harness: точні випуски…
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - Відновлює сеанси DeepSeek Harness, які відмовляються завантажуватися.
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - Добірний список плагінів, інструментів, оболонок і розширень для DeepSeek…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - Плагін DSH: Git-панель у стилі IDE у веб-інтерфейсі — огляд гілок і історії…
- [jiangnanquan/dsh-ux](https://github.com/jiangnanquan/dsh-ux) - Плагін розширення DSH web UI + безрамкова оболонка Electron для настільних…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - Плагін DSH: підключає моделі з настільного застосунку WorkBuddy до DeepSeek…
- [EdwinZDZ/dsh-api-balance-ring](https://github.com/EdwinZDZ/dsh-api-balance-ring) - Кільце балансу DeepSeek API у реальному часі для поля створення повідомлень…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Робочий простір із кількома папками: дозвольте агенту DSH (DeepSeek Harness)…
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - Двомовний реєстр та інсталятор екосистеми плагінів DeepSeek Harness із…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Плагін DSH: вікно інструментів Git рівня IDE як нативна вкладка…
- [mjylfz/dsh-skill-mover](https://github.com/mjylfz/dsh-skill-mover) - Переносьте навички інших агентів у DeepSeek Harness одним клацанням: підтримка…
- [xiaoso456/dsh-workflow-lite](https://github.com/xiaoso456/dsh-workflow-lite) - Плагін програмного робочого процесу DeepSeek Harness: проєктуйте процес на…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Бачте кожну спостережувану дію AI-агента програмування.
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - Плагін налаштувань персоналізації DeepSeek Harness використовується для…
- [cv-superding/dsh-webin](https://github.com/cv-superding/dsh-webin) - Неофіційний плагін DSH: керуйте вебінтерфейсами AI (DeepSeek/Qwen/...) у…
- [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) - Сторонній адаптер: реєструє службу MCP від REA.
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - Колекція плагінів DSH: автентифікація за паролем + довіра для доступу dsh web…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Надає агенту DeepSeek Harness рідні можливості для керування GitHub! Повторно…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт перевірки плагінів DeepSeek Harness (dsh) без залежностей — контрольні…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Екосистема DeepSeek Harness plugin: 86 open-source plugins у family зі 101…
- [SuCriss/dsh-leekbox](https://github.com/SuCriss/dsh-leekbox) - 韭菜盒子 LeekBox — помічник для перегляду котирувань акцій A-share · вебплагін…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Вебплагін DeepSeek Harness (DSH): вкладка бічної панелі market-dashboard для…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode на DeepSeek Harness — плагін DSH, який забезпечує роботу OpenCode Zen…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонній маркетплейс плагінів і захищений менеджер життєвого циклу…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx — це орієнтований на людину розширюваний настільний робочий простір…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Повністю укомплектований агент програмування для DeepSeek Harness — робочі…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - Плагін DSH: показує баланс вашого облікового запису DeepSeek унизу лівої бічної…
- [iluluyu/dsh-ui-outline](https://github.com/iluluyu/dsh-ui-outline) - Плагін навігації переходами праворуч у стилі ChatGPT для вебверсії DeepSeek…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — набір інструментів для локального розгортання й експлуатації…
- [Wenston-dev/awesome-dsh-plugin](https://github.com/Wenston-dev/awesome-dsh-plugin) - Чудовий список плагінів dsh — автоматизований каталог плагінів DeepSeek…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Плагін DeepSeek Harness: перетворює помилку підготовки ACL пісочниці Windows…
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Дедлайни на рівні розгортання для викликів інструмента dsh, які їх не…
- [fshoocn/cordis-port](https://github.com/fshoocn/cordis-port) - Порт ядра Cordis для Python · плагінний середовищі виконання / впровадження…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Плагін Cordis / DeepSeek Harness — нормалізовані інструменти GitHub API для…
- [majiayu000/dsh-desk](https://github.com/majiayu000/dsh-desk) - Дистрибутив DeepSeek Harness для настільних систем на базі Tauri, доступний для…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [LittleCar30/dsh-deepseek-web](https://github.com/LittleCar30/dsh-deepseek-web) - Окремий настільний плагін dsh для керування DeepSeek Web через спеціальний…

</details>

<a id="writing"></a>

## Тексти, обговорення та відео

Статті, обговорення та відео про можливості модифікацій.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
| TypeScript | 296    | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 72     | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 45     | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 25     | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13     | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 6      | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                               |
| Go         | 4      | `mitre/claude-statusline`, `lexfrei/ailine`, `esengine/DeepSeek-Reasonix`                                     |
| PowerShell | 2      | `markallisongit/claude-statusline`, `czcdr/dsh-plugin-rea`                                                    |
| C          | 1      | `reporails/arcade`                                                                                            |
| C#         | 1      | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1      | `dphmoblie/deepseek-harness-android`                                                                          |
| Lua        | 1      | `crafts69guy/claude-statusline.nvim`                                                                          |
| Swift      | 1      | `peaceinitiativemenhadenoil263/claude-status-bar`                                                             |

<sub>Враховуються лише записи, у яких зазначено мову. Документація та записи обговорень не включені до цієї таблиці.</sub>

## Участь у розробці

Виправлення вітаються — це найшвидший спосіб покращити цей список. Створіть issue або pull request, якщо запис віднесено не до тієї категорії, неправильно оцінено або якщо проєкт помилково виключено через збіг назви — саме в цій останній категорії автоматизовані фільтри найчастіше помиляються.

---

<sub>Незалежний проєкт спільноти. Не пов’язаний із Anthropic, не схвалений і не перевірений ним. Claude Code, Claude і Anthropic — торговельні марки Anthropic. Поведінка продукту може змінюватися без попередження; усе критично важливе перевіряйте за офіційною документацією. Права на ресурси залишаються за їхніми проєктами-джерелами; вони відтворюються лише там, де це дозволено ліцензією.</sub>

<sub>Востаннє оновлено · 2026-10-13T21:42:20+08:00</sub>
