<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Круті моди для Claude">
</p>

<h1 align="center">Круті моди для Claude</h1>

<p align="center"><b>Індекс модів і плагінів для Claude Code, оцінених за доказовістю, а також глибших змін у поведінці, які вони вносять.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-502-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <b>Українська</b></sub></p>

> [!NOTE]
> **Актуальний індекс** · Остання синхронізація: `2026-10-16T03:45:33+08:00` (UTC+8)
> · Записи: **502** · Додано під час останнього оновлення: **0** · Мови реалізації: **9**

<sub>Кожен наведений нижче запис було автоматично зібрано, відфільтровано та повторно перевірено. Тут немає платних розміщень.</sub>

<a id="featured"></a>

## Актуальна добірка

<sub>По одному запису на категорію, упорядкованому за рівнем доказовості та кількістю зірок; рейтинг перераховується під час кожного оновлення. Це рейтинг, а не рекомендація; кожна добірка веде до повної картки нижче. Перевагу надано проєктам, які опублікували знімок екрана або запис, щоб добірка залишалася візуальною.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9524 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2568 · Python · 👁️ observed</sub>
<sub>Знайдіть токени-привиди. Виправте їх. Переживіть ущільнення. Уникайте погіршення якості контексту.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74991 · TypeScript · 👁️ observed</sub>
<sub>🌊 Оригінальний агентний рушій. Розгортайте інтелектуальні багатокористувацькі рої, координуйте автономні робочі процеси та створюйте розмовні системи ШІ. Серед…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## Зміст

- [Що таке мод для Claude Code](#що-таке-мод-для-claude-code)
- [Як оцінюються записи](#як-оцінюються-записи)
- [Офіційні: власні репозиторії та примітки до випусків Anthropic](#офіційні-власні-репозиторії-та-примітки-до-випусків-anthropic) — **17**
- [Моди: створені за допомогою можливості модифікації](#моди-створені-за-допомогою-можливості-модифікації) — **382**
- [Екосистеми плагінів DSH і Cordis](#екосистеми-плагінів-dsh-і-cordis) — **95**
- [Тексти, обговорення та відео](#тексти-обговорення-та-відео) — **8**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151049 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Опис

Claude Code — це агентний інструмент для програмування, що працює в терміналі, розуміє вашу кодову базу й допомагає програмувати швидше, виконуючи рутинні завдання, пояснюючи складний код і керуючи робочими процесами git — усе за допомогою команд природною мовою.

<sub>🔧 Знайдено використання в коді: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                         |
| ------------- | ---------------------------------------------------------------- |
| Категорія     | `Офіційні: власні репозиторії та примітки до випусків Anthropic` |
| Підтвердження | `опубліковано безпосередньо Anthropic`                           |
| Мова          | TypeScript                                                       |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **151049** |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9524 · TypeScript · ✅ official · 0 天</summary>

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
| Зірки                   | **9524**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8286 · Python · ✅ official · 0 天</summary>

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
| Зірки                   | **8286**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6390 · Python · ✅ official · 246 天</summary>

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
| Зірки                   | **6390**   |
| Останній push           | 2026-02-11 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

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
| Зірки                   | **1813**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>Більше в цій категорії</b> <sub>· 5</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Додано `$.ui.notify` для модифікацій: створює нативне сповіщення через власне…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Виправлено завершення безголових сеансів, очищення введеного промпту або…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod.

</details>

<a id="mods"></a>

## Моди: створені за допомогою можливості модифікації

Кожен запис тут містить докази використання можливості, яку Claude Code отримав у версії 2.1.287: він виводить дані через `ui.render`, має власну панель, смугу або картку, читає `$.ui.selection()`, запускає колег за допомогою `agent.spawn` або прямо називає себе модом.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2568 · Python · 👁️ observed · 0 天</summary>

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
| Зірки                   | **2568**   |
| Останній push           | 2026-10-15 |
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
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐826 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Опис

Custom Claude Code Mods that I need

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **826**    |
| Останній push           | 2026-10-14 |
| Вперше додано до списку | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐594 · JavaScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **594**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐254 · TypeScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **254**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐212 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **212**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐193 · TypeScript · 👁️ observed · 11 天</summary>

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
| Зірки                   | **193**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐151 · TypeScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **151**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐115 · TypeScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **115**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐99 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 Знайдено використання в коді: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **99**     |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐92 · TypeScript · 👁️ observed · 3 天</summary>

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
| Зірки                   | **92**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

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
| Зірки                   | **80**     |
| Останній push           | 2026-10-08 |
| Вперше додано до списку | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐68 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Опис

Колекція з понад 100 модифікацій, які можна використовувати з Claude Code.

<sub>🔧 Знайдено використання в коді: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **68**     |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Модифікації Claude Code: динамічні індикатори прогресу плану над запитом

<sub>🔧 Знайдено використання в коді: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | JavaScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **54**     |
| Останній push           | 2026-10-14 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>анімований запис · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Відкрити відео</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐33 · TypeScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **33**     |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐29 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

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
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Опис

Claude Code mods: меню інструментів Claude, режим Zen, теми термінала, керування зусиллям і режимом

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Моди: створені за допомогою можливості модифікації`                      |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **24**     |
| Останній push           | 2026-10-14 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>анімований запис</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

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
| Зірки                   | **22**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

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
| Зірки                   | **15**     |
| Останній push           | 2026-10-13 |
| Вперше додано до списку | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Зірки                   | **14**     |
| Останній push           | 2026-10-03 |
| Вперше додано до списку | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Зірки                   | **14**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 5 天</summary>

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
| Зірки                   | **11**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
| Зірки                   | **10**     |
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 30 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 1 天</summary>

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
| Останній push           | 2026-10-14 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 Опис

Добірка Claude Code mods від 개발동생. Пакет таксі: лічильник, навігація, камери контролю швидкості, відеореєстратор

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
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Переглянути на youtube.com</a> · відтворення відкривається на сайті-джерелі; GitHub не може вбудувати його безпосередньо</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Опис

Панелі, захисні механізми та моди для зручності роботи з Claude Code: контекст, використання, активність у реальному часі, сповіщення, правила безпеки, помічник запитів, центр команд.

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
| Останній push           | 2026-10-06 |
| Вперше додано до списку | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/timoncool/givememod">timoncool/givememod</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Модифікації Claude Code на вимогу — навичка, яка читає вашу розмову й створює відповідну модифікацію: індикатор перебігу плану, панель файлів, індикатор контексту, захист від ризикованих команд, спостерігач за тестами. 11 перевірених шаблонів, 29 будівельних блоків, карта 3 057 публічних модифікацій. Термінал і робочий стіл.

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
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-11 |

🏷 `agent-skills` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-skill`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/timoncool--givememod/6fb8ba0c74031f7f.png" width="100%" alt="timoncool/givememod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/timoncool--givememod/5f58df5c7bdd37f9.gif" width="100%" alt="timoncool/givememod animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Danovich/turntype">Danovich/turntype</a></b> · ⭐7 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Опис

Тест набору тексту на час, поки працює Claude. Мод Claude Code.

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
| Останній push           | 2026-10-11 |
| Вперше додано до списку | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `claude-mods` · `typing` · `typing-game` · `typing-practice` · `typing-test`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary><b>Більше в цій категорії</b> <sub>· 348</sub></summary>

- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Модифікації Claude Code від Darrell Wang — смуги над запитом, нуль токенів…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Модифікації Claude Code від Ray Amjad: панелі, смуги, захист запитів, робота із…
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Експертні Skills, агенти, команди, правила, хуки та стилі виведення для Claude…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Модифікації Claude і інструменти для їх створення: спочатку навичка створення…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Чотири модифікації Claude Code: Cache Keeper, Recording Mode, Goal Meter і…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Середовище Claude Code, яке я використовую щодня, опубліковане під цією назвою…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Змініть дах Claude Code за допомогою Claude Mods: без зміни бінарного файлу…
- [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) - A measured tool-call firewall for AI agents: allow, ask or deny before the…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Збирання, тести, консоль і попередній перегляд SwiftUI з Xcode усередині Claude…
- [BrianHuang813/clawd-actor](https://github.com/BrianHuang813/clawd-actor) - Claude Code mod: Clawd розігрує те, що робить Claude, над prompt.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - База знань Obsidian із джерелами про Claude Code mods: як вони працюють, як їх…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Модифікації Claude Code від Learning Hacker: перетворюють роботу агента на…
- [kakha13/claude](https://github.com/kakha13/claude) - Модифікації Claude Code, які виправляють і перекладають ваші підказки перед…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods і навички від Nekyia Labs, створені та щодня використовувані…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Бічна панель для Claude Code: субагенти, яких запускає сеанс, що робить кожен…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Бічна панель Claude Desktop (вкладка Code): перелічує незавершені та поточні…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Смуга використання над полем введення Claude Desktop (вкладка Code): ліміти 5h…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (плагіни з функціональними хуками) для Claude Code.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Плаваюча картка стану для Claude Code — модель, контекст, обмеження швидкості…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Навичка, яка навчає агентів Claude Code створювати Claude Mods.
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Черга рішень CLI/TUI для людей, які працюють із розмовними агентами.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Модифікації, плагіни та навички Claude від спільноти, які можна встановити з…
- [davekiss/mods](https://github.com/davekiss/mods) - Моди Claude Code від Dave Kiss.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Галерея модів Baselane: Claude Code mods, перевірені та закріплені.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Магазин модів для Claude Code усередині Claude Code: введіть /mods, щоб…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Шість модифікацій Claude Code: обмеження плану й контекст над полем запиту…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Мод Claude Code (плагін), що додає бічну панель із вкладками Activity, Files…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Модифікація Claude Code, яка відображає відмінності Edit і Write у двох…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code mods: панель використання 像素螃蟹 usage-hud + HTML-посилання, на які…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Моди для Claude Code: плагіни function-hook, що додають динамічні панелі та…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard приховує імена та секрети під час демонстрації…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Модифікації та оболонки для Claude Code: індикатор перебігу завдань Claude у…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Розширення Claude Code. Розкрийте повну потужність Claude.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Два моди Claude Code над полем запиту: індикатор контекстного вікна, 5-годинний…
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Власний marketplace плагінів модів для Claude Code.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Читає markdown-файли, назви яким дає Claude Code, відображає їх поруч із…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow для Claude Code: спокійний список завдань над полем запиту, що…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: панель контексту, панель агентів, розмиття PDPA.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Мод Claude Code: мініатюри вставлених зображень над полем запиту в будь-якому…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Голосовий напарник для Claude Code. Обговорюйте питання з 3D-вовком на основі…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Два моди Claude Code для одночасного запуску багатьох сеансів: картка контексту…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, індикатор швидкості набору в реальному часі зі…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Моди для Claude Code: панелі, команди та хуки, створені за допомогою плагіна…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Відкривайте Claude Code mods, плагіни та розширення з анімованими…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Мод Claude Code: діаграми mermaid, намальовані безпосередньо в стенограмі.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Невеликі моди Claude Code (плагіни function-hook): session-switcher та інші.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout (пошук модів, якими ви користувалися б найчастіше)…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Набір інструментів Claude від Naren: навички, модифікації та MCP servers для…
- [nuromirzak/nibbl](https://github.com/nuromirzak/nibbl) - A tiny pixel pet that nibbles your bugs. Lives above your Claude Code prompt.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Добірка модів для claude code, створених мною.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: знаходження, перевірка, перемикання та оновлення модів Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Найкращі Claude Code Mods: відібрані вручну, перевірені, закріплені.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Моди Claude Code для справжніх інженерів.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Плагін Claude Code: автоматична маршрутизація моделей Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Шість модів для Claude Code: анімований маскот Clawd, панелі ліміту…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Моди з відкритим кодом для Claude Code: панелі, рядки стану, сповіщення, захист…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Модифікація Claude Code: відповідайте на запитання Claude по черзі…
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Моди для Claude Code: Clawd, крихітний піксельний талісман, який відтворює дії…
- [reporails/arcade](https://github.com/reporails/arcade) - Класичні настільні ігри як моди Claude Code, у які можна грати на панелі, поки…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods для claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Модифікація Claude Code, яка вмикає або вимикає ваші глобальні навички, агенти…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Перевірені моди Claude Code, що встановлюються однією командою: захисні…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Добірний список модів для Claude Code, які можна встановити як маркетплейс…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Два моди Claude Code: cache-keeper і ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Моди Claude Code, які допомагають агенту бути чесним — функціональні хуки, що…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Мод Claude Code для фіксації думок посеред роботи, їхнього сортування між…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Вирощуйте чайне яйце, яке повільно просочується смаком, поки ви пишете код ·…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Моди Herman для Claude Code (marketplace herman-mods).
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Плагін (мод) Claude Code, який робить термінальний інтерфейс Claude Code схожим…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Переглядайте, що Claude Code виконує у фоновому режимі: субагенти, завдання…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Польові нотатки першого дня про моди Claude Code на Windows: індикатор палива…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Мод Claude Code: живі лічильники вартості, контексту й квоти плану над запитом.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin і mod: AI-native SDLC.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Відшмагайте Claude, коли він помиляється — модифікація для зняття стресу в…
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar for Claude Code: usage limits, context, model, cost, git and session…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Вивчайте іноземну мову під час роботи з Claude Code.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Бічна панель із поточними витратами, токенами та використанням контексту для…
- [Azertyuiop442/deepshrink](https://github.com/Azertyuiop442/deepshrink) - Proven-freshness context store for coding agents - mtime-verified reuse, TF-IDF…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Мод Claude Code, який підтримує поточний список відкритих питань у розмові та…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Тримайте Claude Code на plan: stages, approval gates і file budget, enforced by…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Дивіться, які файли кожен агент Claude Code має у своєму контексті та яку…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Невеликі моди Claude Code для термінала й настільного застосунку.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Навичка + мод Claude CLI, що додає іспанські слова у відповіді агента.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Ваш список завдань Floatee над підказкою Claude Code: запускайте, спрямовуйте…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: модифікація Claude Code для обов.
- [joaquinsalinas06/crabbus](https://github.com/joaquinsalinas06/crabbus) - See what every Claude Code subagent is really doing — two-way messaging, tokens…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Вікно контексту як один рядок над запитом, відтворений так, як Claude Code…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Мод коду Claude: вибирає модель і рівень зусиль для міркування кожного субагента.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Не дозволяйте своїй увазі блукати, поки чекаєте на відповідь Claude Code.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Безкоштовний плагін із відкритим кодом для Claude Code.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [nonputtipong/claude-code-prompt-enhancer](https://github.com/nonputtipong/claude-code-prompt-enhancer) - ✻ A Claude Code mod that rewrites your rough draft into a clear, project-aware…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Навички Claude Code: перевірка фактів у документації, аудит коду, журнал…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Плагін-компаньйон для Claude Code: ASCII-компаньйон над запитом, який памʼятає…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Він говорить: модифікація Claude Code, яка за запитом уголос читає відповіді…
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Модифікації Claude Code: невеликі плагіни для живих панелей, маршрутизації…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Модифікація та плагін Claude Code: монітор використання, відстеження токенів…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Модифікації Claude Code: EMCC (Every Mod Claude Code), відібрана й протестована…
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [aiob3/claude-grounds-demo](https://github.com/aiob3/claude-grounds-demo) - Demo for claude-grounds (Claude Code mods): a median() bug with text sort and a…
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Анімований брайлівський кіт над запитом Claude Code.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Піксельний кіт над запитом Claude Code, який запускає тестовий виклик…
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Мод Claude Code, який обирає вдалий момент для ущільнення, щоб зберегти…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Модифікації Claude для Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Універсальні моди для Claude Code: bands, панелі, сповіщення та хуки.
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Ваші ліміти використання Claude у вигляді анімованої картки здоров.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Короткі тренування, поки Claude працює: щоденна ціль, серії, значки та…
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Модифікація Now Playing для Claude Code: Apple Music і Spotify над запитом, з…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [Br4inergy/claude-hands-off](https://github.com/Br4inergy/claude-hands-off) - Your AI agent can&#x27;t push to a repo, deploy a project or drop a table that isn&#x27;t…
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [Br4inergy/claude-loadout](https://github.com/Br4inergy/claude-loadout) - Loadout, the mod manager for Claude Code: audits every mod and every update…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Модифікації для Claude Code: Cache-Uhr, Blast Radius, Vorschlaege…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Просто сова для вашого Claude Code.
- [CiroVilmer/jev-agent-router](https://github.com/CiroVilmer/jev-agent-router) - Claude Code mod that picks the model and effort of every subagent from its task…
- [CoderDayton/vii-mods](https://github.com/CoderDayton/vii-mods) - Claude Code mods for memory, safety and workflow.
- [danieldeusing/capi-cc-mod](https://github.com/danieldeusing/capi-cc-mod) - Capi: a Claude Code mod that teaches you a language above the prompt, one…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Моди для Claude Code (плагіни для перехоплення функцій): session-meter та інші.
- [flaviorg/claude-mods](https://github.com/flaviorg/claude-mods) - Hub marketplace for my original Claude Code mods: tripwire, canopy, crew…
- [flaviorg/crew](https://github.com/flaviorg/crew) - Claude Code mod: a live panel of the subagents Claude delegates to — model…
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Індикатор поточних витрат для Claude Code: вартість сесії із субагентами та…
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-effort-switch](https://github.com/HuliLulu46/cc-effort-switch)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Мод Claude Code: скільки часу тривала кожна відповідь, скільки думав Claude і…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Бічна панель із використанням контексту: загальний обсяг, категорії, зростання…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Бічна панель зі списком файлів: які файли створено, змінено або видалено в цій…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Пухнастик у стилі 8-bit (чорно-білий голландський висловухий кролик) бігає та…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Бічна панель «Мої запитання»: кожне речення, яке власник вводив у цій розмові;
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Бічна панель із часовою шкалою: на що витрачено час у цьому раунді.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Бічна панель обміну токенами: скільки токенів головна розмова щоразу надсилає…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Чесна коробочка для claude code: після кожної відповіді Claude тихо каже одну…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [Jsolee/claude-mods](https://github.com/Jsolee/claude-mods) - Mods de Claude Code de Joan Solé: comunitat, el panell dels subagents amb el…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd живе в смузі над вашим prompt Claude Code: розігрує сесію, показує, що…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Мод для озвучення відповідей і сповіщень Claude Code за допомогою VOICEVOX /…
- [katipally/modz](https://github.com/katipally/modz) - Claude Code mods: install with /plugin install &lt;mod&gt; --marketplace…
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high.
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Посібник зіставлених спільнотою модів Claude Code: варіанти використання…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Мод для Claude Code, який показує, що робить Claude, у підзаголовку вкладки…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Модифікації спільноти для Claude Code: засоби захисту, панелі та команди, що…
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Мод Claude Code, який знову вмикає інструменти todo для моделей, що їх не…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Мод Claude Code, який чекає на безпечну паузу, а потім передає вашу сесію або…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Мод Claude Code: по одному рядку для кожного завдання над запитом із поточним…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Грайте в Connect Four проти AI всередині Claude Code (/connect-four).
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Модифікація Claude Code: коли інший агент програмування робить коміт у ваш…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Модифікація Claude Code для репозиторіїв, спільних для кількох AI-агентів: не…
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: мод коду Claude. Постійні робочі дерева з початковим режимом лише…
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Бічна панель поточної статистики сесії для вкладки Code настільного застосунку…
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [rakavanagh/savvy-status](https://github.com/rakavanagh/savvy-status) - Claude Code mod: watch your subagents work as a crew of crabs, with live file…
- [ramonfabrega/mods](https://github.com/ramonfabrega/mods) - Claude Code mods: hooks modules that change the interface.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code mod: відтискання, які треба робити, поки працює Claude. Без токенів.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: практичний посібник із модів коду Claude — від ELI5 до розробки…
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [RomuloDrumond/claude-last-turn-diff](https://github.com/RomuloDrumond/claude-last-turn-diff) - A Claude Code mod: GitHub-style diffs of the files Claude edited in the last…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Модифікація Claude Code: перетворює план, який ви схвалюєте в режимі…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Ретельно відібраний список модів Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Безкоштовний режим: допоміжні агенти працюють на Haiku, а великі файли й…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Музичний супровід у стилі lofi, що супроводжує сесію: спокій, зосередженість…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Навчайтеся, поки Claude пише код: після ходу, який змінив код, над промптом…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Запис кожної зміни, яку вносить Claude: відтворюйте кожну зміну, спостерігаючи…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Повідомлення комітів одним кліком для Claude Code з танцюючою піксель-арт…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — мод Claude Code, який показує використання вашого плану Claude…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Мод Claude Code, що показує поточний сеанс в окремій області: кожен запит…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Маркетплейс плагінів Claude Code із модами: плагіни function-hooks, що малюють…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Мод Claude Code: анімована смуга поступу та підсумок завершення для тривалих…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Три невеликі моди для Claude Code: переглядайте, коли ваші субагенти завершать…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Скажіть &quot;I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Поставте Claude додаткове запитання в панелі поруч із вашою роботою.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Плагін Claude Code: ваші ліміти використання Claude Pro/Max із прогнозом…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Моди для Claude Code. agent-crew: спостерігайте за роботою ваших субагентів як…
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
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
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Загальнодоступні Skills і модифікації Claude Code.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, модифікації, субагенти, хуки, slash-команди та посібники для Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Юридично безкоштовні LLM APIs і coding agents — самостійно оновлюються, двічі…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Live-рахунки футбольних матчів, календарі та турнірні таблиці для змагання…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill, який перетворює вашого агента програмування на експерта з прошивок…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Час молитви, дата за календарем Хіджри, азкари, щоденний аят, піст за сунною…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Набір плагінів для Claude Code, pi та DeepSeek Harness: HUD у рядку стану…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Портативний набір інструментів Claude Code для .NET DDD/Clean Architecture…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Переносна глобальна конфігурація Claude Code: власні навички, хуки PreToolUse і…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Неофіційні моди для вкладки Code у Claude Desktop — usage-pet: смуга…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Плагіни Claude Code, якими я користуюся щодня: навички та моди, очищені так…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Налаштовуваний status line для Claude Code з редактором перетягуванням.
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [rapita/claude-grammar](https://github.com/rapita/claude-grammar) - Background English grammar coach for Claude Code.
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Візуальна дошка для ваших агентів Claude Code: переглядайте сесії, субагентів і…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Маркетплейс плагінів і навичок Claude Code для створення модів гри Hytale.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Переглядач із розділеною панеллю для Claude Code у терміналі Windows та tmux…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Репозиторій модів Awesome Media для Claude Code.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [michalschroeder/claude-statusline](https://github.com/michalschroeder/claude-statusline) - My Claude Code statusline + supporting hooks.
- [RaggioS/claude-code-statusline](https://github.com/RaggioS/claude-code-statusline) - Single-file POSIX statusline for Claude Code: dir, git branch, model, context…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Посилений статусний рядок із градуйованими кольорами та без залежностей для…
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens.
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [31c0c3/claude-statusline](https://github.com/31c0c3/claude-statusline) - One-line Claude Code status line in bash and jq: context, cache, limits, cost.
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code plugin marketplace with baloo: skills, an agent that verifies…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Статусний рядок Claude Code професійного рівня: тривалість сеансу, вартість у…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Рядок стану для Claude Code: контекст, ліміти й темп тижня, CI, деплої та PR…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust.
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Попередній перегляд зображень усередині Claude Code: наведіть курсор на чип під…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [jamesyoung-dev/claude-cache-countdown](https://github.com/jamesyoung-dev/claude-cache-countdown) - Keeps claude_statusline_plus.
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jdmalter/claude-code-statusline](https://github.com/jdmalter/claude-code-statusline) - A muted three-line status line for Claude Code, in bash for Git Bash on Windows.
- [JesseWebDotCom/claude-overview](https://github.com/JesseWebDotCom/claude-overview) - A live Claude Code side pane: Claude and Codex usage limits, context breakdown…
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Хук рядка стану Claude Code — відстежує використання токенів і контекст між…
- [milan44i/claude-setup](https://github.com/milan44i/claude-setup) - An installable Claude Code setup: self-healing TypeScript hook…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [mr-pmillz/claude-code-pmillz-statusline](https://github.com/mr-pmillz/claude-code-pmillz-statusline) - a status line variant for claude code that shows useful info.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [rperez93/claude-progress](https://github.com/rperez93/claude-progress) - Progress bars with an honest ETA in the Claude Code status line: count…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Користувацький рядок стану Claude Code.
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company.
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Універсальний багатопротокольний StatusLine, контекст із самонавчанням і…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Детектор виснаження контексту 2026 — проактивна пам.
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Хуки, субагенти та рядки стану Claude Code: колекції інструментів із відкритим…
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Моди для Claude Code: панелі, смуги та компаньйони на основі функціональних…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Передавайте завдання між сеансами Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: знаходьте те, про що ви знову й знову просите Claude Code, і…
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Це сервер MCP для керування MODS — модульним кросплатформним інструментом для…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Навичка Codex і Claude Code для перекладу модів CK3 за допомогою локального LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Моди з відкритим кодом та інші розширення для Claude Code.
- [Isllanrx/status_cli](https://github.com/Isllanrx/status_cli) - Status line in Rust for Claude Code, Codex CLI and Antigravity CLI: usage…

</details>

<a id="dsh-cordis"></a>

## Екосистеми плагінів DSH і Cordis

DeepSeek Harness і Cordis досягають того самого результату іншим шляхом: для них плагін є механізмом модів, тож плагін там — еквівалент мода тут.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250372 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 Знайдено використання в коді: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                        |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **250372** |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74991 · TypeScript · 👁️ observed · 0 天</summary>

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
| Зірки                   | **74991**  |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4635 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Опис

Офіційно рекомендований TUI-плагін DSH — висока продуктивність, низьке навантаження, милий піксельний кит, плавна взаємодія мишею. Встановлення однією командою через npm. / Офіційно рекомендований TUI-плагін DSH — висока продуктивність, низьке навантаження, милий піксельний кит, плавна взаємодія мишею, встановлення однією командою через npm

<sub>🔧 Знайдено використання в коді: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                        |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | TypeScript                                                                |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **4635**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐702 · Python · 👁️ observed · 0 天</summary>

##### 📝 Опис

Добірний список найкращих чудових ШІ-плагінів для ШІ-асистентів, зокрема Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi та інших. https://hol.org/plugins

<sub>🔧 Знайдено використання в коді: `README.md`</sub>

##### 📌 Основні факти

| Поле          | Значення                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                        |
| Підтвердження | `у власному тексті згадується мод API або заявлено підтримку модифікацій` |
| Мова          | Python                                                                    |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **702**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐266429 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **266429** |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101333 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **101333** |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84002 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **84002**  |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35805 · Go · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **35805**  |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30954 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **30954**  |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25659 · Python · 🔎 inferred · 2 天</summary>

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
| Зірки                   | **25659**  |
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
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18885 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **18885**  |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9205 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **9205**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8795 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **8795**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4270 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **4270**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3019 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **3019**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1473 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Опис

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Python                                                                          |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1473**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1204 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Go                                                                              |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **1204**   |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐703 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **703**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Опис

📚 Бібліотека мікроуроків для AI-агентів без залежностей, на основі git, для асинхронного обміну та пошуку перевіреного досвіду налагодження. | https://misakanet.org

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | Python                                                                          |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **526**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐483 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **483**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐274 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **274**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **256**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐164 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **164**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>анімований запис</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐163 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **163**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐151 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Після встановлення ви одразу отримуєте 27 інженерних навичок і навичок продуктивності з mattpocock/skills v1.3.1, без потреби встановлювати навички вручну. Цей плагін створено за допомогою 40 мільярдів токенів; він забезпечує десятикратне підвищення ефективності розробки порівняно з оригінальними навичками та допомагає новачкам швидше опанувати цей набір навичок. Повна підтримка GitHub issue; Markdown — попередня версія; GitLab наразі не підтримується. Дякуємо за використання та підтримку 💗

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **151**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Duskriver/dsh-opencode-go">Duskriver/dsh-opencode-go</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

用于deepseek-harness的opencode-go套餐增强插件。多账号管理、额度UI面板、自动更新模型。An opencode-go subscription enhancement plugin for deepseek-harness — featuring multi-account management, a quota UI panel, and automatic model updates.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **133**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/duskriver--dsh-opencode-go/a745e1f7913eaf45.png" width="100%" alt="Duskriver/dsh-opencode-go screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/duskriver--dsh-opencode-go/d75a597695831f54.gif" width="100%" alt="Duskriver/dsh-opencode-go animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐128 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **128**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Microqian2th/dsh-codex-effort-slider">Microqian2th/dsh-codex-effort-slider</a></b> · ⭐124 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Codex 风格的推理等级滑条（DeepSeek Harness 插件）：可拖动连续滑条 + 高档位渐变星尘特效

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
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `ai` · `ai-agents` · `codex` · `deepseek` · `deepseek-ai` · `deepseek-harness` · `deepseek-plugin` · `deepseek-v4`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/microqian2th--dsh-codex-effort-slider/eb0c0410e75227ba.png" width="100%" alt="Microqian2th/dsh-codex-effort-slider screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐119 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **119**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐107 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into questions and spaced review · 把自己的资料变成题目与间隔复习的 DSH 学习插件

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **107**    |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐98 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **98**     |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-15 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>анімований запис</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐92 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | JavaScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **92**     |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

<sub>Ресурс підключено безпосередньо з репозиторію-джерела, оскільки ліцензію, придатну для повторного розповсюдження, не зазначено.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐77 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Зірки                   | **77**     |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐70 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Опис

自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and validate the DeepSeek-Harness community plugin marketplace.

##### 📌 Основні факти

| Поле          | Значення                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Категорія     | `Екосистеми плагінів DSH і Cordis`                                              |
| Підтвердження | `заявлено мод, плагін або хук, але нічого конкретного про поверхню модифікацій` |
| Мова          | TypeScript                                                                      |

##### 📊 Дані

| Метрика                 | Значення   |
| ----------------------- | ---------- |
| Зірки                   | **70**     |
| Останній push           | 2026-10-15 |
| Вперше додано до списку | 2026-10-16 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Зображення</th><th align="center" width="50%">🎬 Відео</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>медіа не опубліковано</sub></td>
</tr></table>

</details>

<details>
<summary><b>Більше в цій категорії</b> <sub>· 61</sub></summary>

- [strukto-ai/mirage](https://github.com/strukto-ai/mirage) - Перший у світі віртуальний термінал для AI-агентів.
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Захист перед виконанням для AI coding agents.
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Ринок плагінів DSH / DSH Plugin Marketplace: перегляд, встановлення та…
- [arcships/rutis](https://github.com/arcships/rutis) - Середовище виконання плагінів для програмного забезпечення, яке вдосконалює…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Актуальний каталог плагінів DeepSeek Harness — оновлюється щогодини, щодня…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Каталог вибраних плагінів DeepSeek Harness (DSH) — понад 280 плагінів спільноти…
- [hkkz9522/dsh-session-manager](https://github.com/hkkz9522/dsh-session-manager) - DeepSeek Harness session and workspace manager —— Workspaces: archive and…
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [Lxiayu/DshCockpit](https://github.com/Lxiayu/DshCockpit) - Desktop cockpit for DeepSeek Harness (dsh): token usage &amp; cost tracking, budget…
- [Fengze233/dsh-vscode](https://github.com/Fengze233/dsh-vscode) - 在 VS Code 侧边栏内嵌使用 DeepSeek Harness（DSH）网页界面的插件.
- [GooDAnDReaDY/dsh-russian-lang](https://github.com/GooDAnDReaDY/dsh-russian-lang) - 100% русская локализация и Smart UX для DeepSeek Harness (DSH v0.1.7+): 7574…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Плагін DSH: оболонка Git Bash для всіх режимів агента на Windows.
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [UncleK/dsh-think-translate](https://github.com/UncleK/dsh-think-translate) - Thinking-chain UI translation for DeepSeek Harness: 8 target languages, local…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 给中文网文作者的本地写作工作台.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站.
- [pearjelly/deep-blend](https://github.com/pearjelly/deep-blend) - Create and refine Blender product scenes in DSH: editable recipes, model…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Реєстр плагінів, пакетів і навичок DeepSeek Harness (dsh) із відкритими даними…
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) - 一个设置面板，统一管理 MCP、技能、记忆、子智能体、提示词和归档会话；可自定义搭配场景，一个场景即可切换整个环境；Agent也能帮你操作这个插件.
- [earthwalker17/MiniDSH](https://github.com/earthwalker17/MiniDSH) - Minimal surface, complete architecture: a small, local-first coding-agent…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - Плагін DSH: Git-панель у стилі IDE у веб-інтерфейсі — огляд гілок і історії…
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) - Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Рентген для плагінів DeepSeek Harness: заявлені можливості проти фактичної…
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) - J-Space Cognition Suite SV1 原生 DeepSeek Harness 智能体预设与独立 Cordis…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Бачте кожну спостережувану дію AI-агента програмування.
- [GooDAnDReaDY/dsh-dsml-artifact-guard](https://github.com/GooDAnDReaDY/dsh-dsml-artifact-guard) - Sanitizes leaked DeepSeek DSML closing tags from model text streams.
- [kolawong/fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh) - Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Стандарт перевірки плагінів DeepSeek Harness (dsh) без залежностей — контрольні…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Екосистема DeepSeek Harness plugin: 86 open-source plugins у family зі 101…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Вебплагін DeepSeek Harness (DSH): вкладка бічної панелі market-dashboard для…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode на DeepSeek Harness — плагін DSH, який забезпечує роботу OpenCode Zen…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — сторонній маркетплейс плагінів і захищений менеджер життєвого циклу…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx — це орієнтований на людину розширюваний настільний робочий простір…
- [DDDFXYqiming/dsh-layered-memory](https://github.com/DDDFXYqiming/dsh-layered-memory) - Cross-session long-term memory plugin for DeepSeek Harness.
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入.
- [higekibaka/dsh-vertex-argon](https://github.com/higekibaka/dsh-vertex-argon) - Vertex Argon — Google Vertex AI &amp; Gemini API dual-route Gemini 4 Argon plugin…
- [moonbowterfly/dsh-bio-genie](https://github.com/moonbowterfly/dsh-bio-genie) - 生物信息学「许愿式分析」dsh 插件：57 个语义化工具 + bio_python 执行器.
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色插件：三套服装、任务表情、三口白饭、摸头鼓脸、铁盆帽与手写问候.
- [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [shenhuanageshei/dsh-thincoder-suite](https://github.com/shenhuanageshei/dsh-thincoder-suite) - DSH plugin porting thincoder self-discipline suite: advisor convergent review /…
- [viyiviyi/dsh-tree-task-flow](https://github.com/viyiviyi/dsh-tree-task-flow) - 树形任务流 · DeepSeek Harness 插件：把多步任务组织成目标→任务→子任务三级树，节点完成时由 AI…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Плагін DeepSeek Harness: перетворює помилку підготовки ACL пісочниці Windows…
- [zhang-guo-wen/dsh-claude-compat](https://github.com/zhang-guo-wen/dsh-claude-compat) - deepseek harness 插件，兼容claude的skill、rules加载规则，mcp配置.
- [q253595422/dsh-imagegen-video](https://github.com/q253595422/dsh-imagegen-video) - DeepSeek Harness plugin: image + video generation studio with an infinite…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Тексти, обговорення та відео

Статті, обговорення та відео про можливості модифікацій.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 0 天</summary>

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
| Вперше додано до списку | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| TypeScript | 298    | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 85     | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 35     | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 33     | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 11     | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 7      | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 3      | `vulcanshen/ccdrawu`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                         |
| PowerShell | 2      | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| C          | 1      | `reporails/arcade`                                                                                            |

<sub>Враховуються лише записи, у яких зазначено мову. Документація та записи обговорень не включені до цієї таблиці.</sub>

## Участь у розробці

Виправлення вітаються — це найшвидший спосіб покращити цей список. Створіть issue або pull request, якщо запис віднесено не до тієї категорії, неправильно оцінено або якщо проєкт помилково виключено через збіг назви — саме в цій останній категорії автоматизовані фільтри найчастіше помиляються.

---

<sub>Незалежний проєкт спільноти. Не пов’язаний із Anthropic, не схвалений і не перевірений ним. Claude Code, Claude і Anthropic — торговельні марки Anthropic. Поведінка продукту може змінюватися без попередження; усе критично важливе перевіряйте за офіційною документацією. Права на ресурси залишаються за їхніми проєктами-джерелами; вони відтворюються лише там, де це дозволено ліцензією.</sub>

<sub>Востаннє оновлено · 2026-10-16T03:45:33+08:00</sub>
